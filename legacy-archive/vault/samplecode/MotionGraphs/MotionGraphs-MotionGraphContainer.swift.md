---
title: MotionGraphs
apple_id: DTS40012333
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreMotion
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/MotionGraphs/Listings/MotionGraphs_MotionGraphContainer_swift.html
archived_at: '2026-07-18T03:16:02.015855Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MotionGraphs](MotionGraphs.md)


[Next](MotionGraphs-AccelerometerViewController.swift.md)[Previous](MotionGraphs-AppDelegate.swift.md)

# MotionGraphs/MotionGraphContainer.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Defines a protocol that the view controllers conform to and provides helper methods for updating labels.
 */

import CoreMotion
import UIKit
import simd

protocol MotionGraphContainer {

    var motionManager: CMMotionManager? { get set }

    var updateIntervalLabel: UILabel! { get }

    var updateIntervalSlider: UISlider! { get }

    var updateIntervalFormatter: MeasurementFormatter { get }

    var valueLabels: [UILabel]! { get }

    func startUpdates()

    func stopUpdates()
}

extension MotionGraphContainer {
    private var sortedLabels: [UILabel] {
        return valueLabels.sorted { $0.center.y < $1.center.y }
    }

    func setValueLabels(rollPitchYaw: double3) {
        let sortedLabels = self.sortedLabels
        sortedLabels[0].text = String(format: "Roll: %+6.4f", rollPitchYaw[0])
        sortedLabels[1].text = String(format: "Pitch: %+6.4f", rollPitchYaw[1])
        sortedLabels[2].text = String(format: "Yaw: %+6.4f", rollPitchYaw[2])
    }

    func setValueLabels(xyz: double3) {
        let sortedLabels = self.sortedLabels
        sortedLabels[0].text = String(format: "x: %+6.4f", xyz[0])
        sortedLabels[1].text = String(format: "y: %+6.4f", xyz[1])
        sortedLabels[2].text = String(format: "z: %+6.4f", xyz[2])
    }

    var formattedUpdateInterval: String {
        updateIntervalFormatter.numberFormatter.minimumFractionDigits = 3
        updateIntervalFormatter.numberFormatter.maximumFractionDigits = 3

        let updateInterval = Measurement(value: Double(updateIntervalSlider.value), unit: UnitDuration.seconds)
        return updateIntervalFormatter.string(from: updateInterval)
    }
}
```

[Next](MotionGraphs-AccelerometerViewController.swift.md)[Previous](MotionGraphs-AppDelegate.swift.md)

