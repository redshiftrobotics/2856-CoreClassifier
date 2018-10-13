//
//  ViewController.swift
//  flowerRecognizer
//
//  Created by Zoe IAMZOE.io on 9/15/18.
//  Copyright © 2018 Zoe IAMZOE.io. All rights reserved.
//

import Cocoa
import CoreML
import Vision

class ViewController: NSViewController {

    @IBOutlet weak var idLabel: NSTextField!
    
    @IBOutlet weak var imageTarget: NSImageView!
    
    @IBAction func imageDropped(_ sender: NSImageView) {
        guard let image = sender.image else { return }
        
        do {
            guard #available(OSX 10.13, *) else {
                fatalError("Not available under 10.13")
            }
            
            let model = try VNCoreMLModel(for: m().model)
            
            let request = VNCoreMLRequest(model: model) { [weak self] request, error in
                guard
                    let result = request.results as? [VNClassificationObservation],
                    let first = result.first else {
                        print(error!)
                        fatalError()
                }
                
                DispatchQueue.main.async {
                    self?.idLabel.stringValue = first.identifier
                        + " (confidence \(first.confidence * 100)%)"
                }
            }
            
            let handler = VNImageRequestHandler(cgImage: image.cgImage(
                forProposedRect: nil, context: nil, hints: nil)!, options: [:])
            DispatchQueue.global(qos: .userInitiated).async {
                do {
                    try handler.perform([request])
                } catch let error {
                    print("Erro: \(error.localizedDescription)")
                    fatalError()
                }
            }
        } catch let error {
            print("Error: \(error.localizedDescription)")
        }
    }
}

