//
//  VisionExtentions.swift
//  realTimeMineralTester
//
//  Created by Zoe IAMZOE.io on 10/16/18.
//  Copyright © 2018 Zoe IAMZOE.io. All rights reserved.
//

import Vision

extension Array where Element == VNClassificationObservation {
    
    func getGreatest () -> VNClassificationObservation? {
        var greatestElemement: VNClassificationObservation? = nil
        
        for element in self {
            guard greatestElemement != nil else {
                greatestElemement = element
                continue
            }
            
            if element.confidence > greatestElemement!.confidence {
                greatestElemement = element
            }
        }
        
        return greatestElemement
    }
}
