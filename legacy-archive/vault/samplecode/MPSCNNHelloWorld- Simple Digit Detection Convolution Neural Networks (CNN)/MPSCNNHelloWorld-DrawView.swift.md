---
title: 'MPSCNNHelloWorld: Simple Digit Detection Convolution Neural Networks (CNN)'
apple_id: TP40017482
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal Performance Shaders
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/MPSCNNHelloWorld/Listings/MPSCNNHelloWorld_DrawView_swift.html
archived_at: '2026-07-18T03:13:59.156224Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MPSCNNHelloWorld: Simple Digit Detection Convolution Neural Networks (CNN)](MPSCNNHelloWorld-%20Simple%20Digit%20Detection%20Convolution%20Neural%20Networks%20%28CNN%29.md)


[Next](MPSCNNHelloWorld-AppDelegate.swift.md)[Previous](MPSCNNHelloWorld-SlimMPSCNN.swift.md)

# MPSCNNHelloWorld/DrawView.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This file has routines for drwaing and detecting user touches (input digit)
*/

import UIKit

/**
    This class is used to handle the drawing in the DigitView so we can get user input digit,
    This class doesn't really have an MPS or Metal going in it, it is just used to get user input
 */
class DrawView: UIView {

    // some parameters of how thick a line to draw 15 seems to work 
    // and we have white drawings on black background just like MNIST needs its input
    var linewidth = CGFloat(15) { didSet { setNeedsDisplay() } }
    var color = UIColor.white { didSet { setNeedsDisplay() } }

    // we will keep touches made by user in view in these as a record so we can draw them.
    var lines: [Line] = []
    var lastPoint: CGPoint!

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        lastPoint = touches.first!.location(in: self)
    }

    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        let newPoint = touches.first!.location(in: self)
        // keep all lines drawn by user as touch in record so we can draw them in view
        lines.append(Line(start: lastPoint, end: newPoint))
        lastPoint = newPoint
        // make a draw call
        setNeedsDisplay()
    }

    override func draw(_ rect: CGRect) {
        super.draw(rect)

        let drawPath = UIBezierPath()
        drawPath.lineCapStyle = .round

        for line in lines{
            drawPath.move(to: line.start)
            drawPath.addLine(to: line.end)
        }

        drawPath.lineWidth = linewidth
        color.set()
        drawPath.stroke()
    }


    /**
        This function gets the pixel data of the view so we can put it in MTLTexture

        - Returns:
            Void
     */
    func getViewContext() -> CGContext? {
        // our network takes in only grayscale images as input
        let colorSpace:CGColorSpace = CGColorSpaceCreateDeviceGray()

        // we have 3 channels no alpha value put in the network
        let bitmapInfo = CGImageAlphaInfo.none.rawValue 

        // this is where our view pixel data will go in once we make the render call
        let context = CGContext(data: nil, width: 28, height: 28, bitsPerComponent: 8, bytesPerRow: 28, space: colorSpace, bitmapInfo: bitmapInfo)

        // scale and translate so we have the full digit and in MNIST standard size 28x28
        context!.translateBy(x: 0 , y: 28)
        context!.scaleBy(x: 28/self.frame.size.width, y: -28/self.frame.size.height)

        // put view pixel data in context
        self.layer.render(in: context!)

        return context
    }
}

/**
    2 points can give a line and this class is just for that purpose, it keeps a record of a line
 */
class Line{
    var start, end: CGPoint

    init(start: CGPoint, end: CGPoint) {
        self.start = start
        self.end   = end
    }
}
```

[Next](MPSCNNHelloWorld-AppDelegate.swift.md)[Previous](MPSCNNHelloWorld-SlimMPSCNN.swift.md)

