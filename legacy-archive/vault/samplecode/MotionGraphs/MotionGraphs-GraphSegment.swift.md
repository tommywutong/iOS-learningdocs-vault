---
title: MotionGraphs
apple_id: DTS40012333
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreMotion
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/MotionGraphs/Listings/MotionGraphs_GraphSegment_swift.html
archived_at: '2026-07-18T03:16:01.785181Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MotionGraphs](MotionGraphs.md)


[Next](MotionGraphs-GraphView.swift.md)[Previous](MotionGraphs-DeviceMotionViewController.swift.md)

# MotionGraphs/GraphSegment.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A `UIView` subclass that represents a segment of data in a `GraphView`.
 */

import UIKit
import simd

class GraphSegment: UIView {
    // MARK: Properties

    static let capacity = 32

    private(set) var dataPoints = [double3]()

    private let startPoint: double3

    private let valueRanges: [ClosedRange<Double>]

    static let lineColors: [UIColor] = [.red, .green, .blue]

    var gridLinePositions = [CGFloat]()

    var isFull: Bool {
        return dataPoints.count >= GraphSegment.capacity
    }

    // MARK: Initialization

    init(startPoint: double3, valueRanges: [ClosedRange<Double>]) {
        self.startPoint = startPoint
        self.valueRanges = valueRanges

        super.init(frame: CGRect.zero)
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    func add(_ values: double3) {
        guard dataPoints.count < GraphSegment.capacity else { return }

        dataPoints.append(values)
        setNeedsDisplay()
    }

    // MARK: UIView

    override func draw(_ rect: CGRect) {
        guard let context = UIGraphicsGetCurrentContext() else { return }

        // Fill the background.
        if let backgroundColor = backgroundColor?.cgColor {
            context.setFillColor(backgroundColor)
            context.fill(rect)
        }

        // Draw static lines.
        context.drawGraphLines(in: bounds.size)

        // Plot lines for the 3 sets of values.
        context.setShouldAntialias(false)
        context.translateBy(x: 0, y: bounds.size.height / 2.0)

        for lineIndex in 0..<3 {
            context.setStrokeColor(GraphSegment.lineColors[lineIndex].cgColor)

            // Move to the start point for the current line.
            let value = startPoint[lineIndex]
            let point = CGPoint(x: bounds.size.width, y: scaledValue(for: lineIndex, value: value))
            context.move(to: point)

            // Draw lines between the data points.
            for (pointIndex, dataPoint) in dataPoints.enumerated() {
                let value = dataPoint[lineIndex]
                let point = CGPoint(x: bounds.size.width - CGFloat(pointIndex + 1), y: scaledValue(for: lineIndex, value: value))

                context.addLine(to: point)
            }

            context.strokePath()
        }
    }

    private func scaledValue(for lineIndex: Int, value: Double) -> CGFloat {
        // For simplicity, this assumes the range is centered on zero.
        let valueRange = valueRanges[lineIndex]
        let scale = Double(bounds.size.height) / (valueRange.upperBound - valueRange.lowerBound)
        return CGFloat(floor(value * -scale))
    }
}
```

[Next](MotionGraphs-GraphView.swift.md)[Previous](MotionGraphs-DeviceMotionViewController.swift.md)

