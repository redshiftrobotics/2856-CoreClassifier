//
//  ViewController.swift
//  realTimeMineralTester
//
//  Created by Zoe IAMZOE.io on 10/16/18.
//  Copyright © 2018 Zoe IAMZOE.io. All rights reserved.
//

import UIKit
import AVFoundation

import Vision
import CoreML

@available(iOS 12.0, *)
class ViewController: UIViewController, AVCaptureVideoDataOutputSampleBufferDelegate {
    
    @IBOutlet weak var classificationText: UILabel!
    @IBOutlet weak var cameraView: UIView!
    
    private var requests = [VNRequest]()

    // for displaying camera frames
    private lazy var cameraLayer: AVCaptureVideoPreviewLayer = AVCaptureVideoPreviewLayer(session: self.captureSession)
    
    // caputure session
    private lazy var captureSession: AVCaptureSession = {
        let session = AVCaptureSession()
        session.sessionPreset = AVCaptureSession.Preset.photo
        guard
            let backCamera = AVCaptureDevice.default(.builtInWideAngleCamera, for: .video, position: .back),
            let input = try? AVCaptureDeviceInput(device: backCamera)
            else { return session }
        session.addInput(input)
        return session
    }()
    
    private lazy var classifier: m = m()

    override func viewDidLoad() {
        super.viewDidLoad()
        
        cameraView.layer.addSublayer(cameraLayer)
        cameraLayer.frame = cameraView.bounds
        
        let videoOutput = AVCaptureVideoDataOutput()
        videoOutput.videoSettings = [kCVPixelBufferPixelFormatTypeKey as String: Int(kCVPixelFormatType_32BGRA)]
        videoOutput.setSampleBufferDelegate(self, queue: DispatchQueue(label: "MyQueue"))
        
        self.captureSession.addOutput(videoOutput)
        self.captureSession.startRunning()
        
        setupVision()
    }
    
    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        self.cameraLayer.frame = self.cameraView?.bounds ?? .zero
    }
    
    private func setupVision() {
        guard let visionModel = try? VNCoreMLModel(for: classifier.model) else {
            fatalError("Can’t load VisionML model")
        }
        
        let classificationRequest = VNCoreMLRequest(model: visionModel, completionHandler: classify)
        classificationRequest.imageCropAndScaleOption = VNImageCropAndScaleOption.scaleFill
        requests = [classificationRequest]
    }
    
    private func classify(request: VNRequest, error: Error?) {        
        guard let observations = request.results as? [VNRecognizedObjectObservation]
            else { fatalError("unexpected result type from VNCoreMLRequest") }
        
        let predictions: [Prediction] = observations.map { prediction in
            return Prediction(label: prediction.labels.getGreatest()?.identifier, confidence: prediction.confidence, boundingBox: prediction.boundingBox)
        }
        
        var strings: [String] = []
        for prediction in predictions {
            let pct = Float(Int(prediction.confidence * 10000)) / 100
            strings.append("\(prediction.label ?? ""): \(pct)%")
        }
        
        DispatchQueue.main.async {
            self.cameraLayer.sublayers?.removeSubrange(1...)
            
            for prediction in predictions {
                self.drawBox(boundingRect: prediction.boundingBox)
            }
            self.classificationText.text = strings.joined(separator: ", ")
        }
    }
    
    private func drawBox (boundingRect: CGRect) {
        let source = self.cameraView.frame
        
        let rectWidth = source.size.width * boundingRect.size.width
        let rectHeight = source.size.height * boundingRect.size.height
        
        let outline = CALayer()
        outline.frame = CGRect(x: boundingRect.origin.x * source.size.width, y:boundingRect.origin.y * source.size.height, width: rectWidth, height: rectHeight)
        
        outline.borderWidth = 5.0
        outline.borderColor = UIColor.blue.cgColor
        
        self.cameraLayer.addSublayer(outline)
    }
    
    func captureOutput(_ output: AVCaptureOutput, didOutput sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection) {
        guard let pixelBuffer = CMSampleBufferGetImageBuffer(sampleBuffer) else {
            return
        }
        var requestOptions:[VNImageOption : Any] = [:]
        if let cameraIntrinsicData = CMGetAttachment(sampleBuffer, key: kCMSampleBufferAttachmentKey_CameraIntrinsicMatrix, attachmentModeOut: nil) {
            requestOptions = [.cameraIntrinsics:cameraIntrinsicData]
        }
        let imageRequestHandler = VNImageRequestHandler(cvPixelBuffer: pixelBuffer, orientation: CGImagePropertyOrientation(rawValue: 6)!, options: requestOptions)
        do {
            try imageRequestHandler.perform(self.requests)
        } catch {
            print(error)
        }
    }
}

