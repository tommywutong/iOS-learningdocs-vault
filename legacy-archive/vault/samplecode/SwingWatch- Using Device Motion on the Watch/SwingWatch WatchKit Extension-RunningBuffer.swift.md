---
title: 'SwingWatch: Using Device Motion on the Watch'
apple_id: TP40017286
resource_type: Sample Code
platform: watchOS
topic: null
technology: CoreMotion
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/SwingWatch/Listings/SwingWatch_WatchKit_Extension_RunningBuffer_swift.html
archived_at: '2026-07-18T03:25:51.917280Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SwingWatch: Using Device Motion on the Watch](SwingWatch-%20Using%20Device%20Motion%20on%20the%20Watch.md)


[Next](LICENSE.txt.md)[Previous](SwingWatch%20WatchKit%20Extension-MotionManager.swift.md)

# SwingWatch WatchKit Extension/RunningBuffer.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This class manages a running buffer of Double values.
 */

import Foundation

class RunningBuffer {
    // MARK: Properties

    var buffer = [Double]()
    var size = 0

    // MARK: Initialization

    init(size: Int) {
        self.size = size
        self.buffer = [Double](repeating: 0.0, count: self.size)
    }

    // MARK: Running Buffer

    func addSample(_ sample: Double) {
        buffer.insert(sample, at:0)
        if buffer.count > size  {
            buffer.removeLast()
        }
    }

    func reset() {
        buffer.removeAll(keepingCapacity: true)
    }

    func isFull() -> Bool {
        return size == buffer.count
    }

    func sum() -> Double {
        return buffer.reduce(0.0, +)
    }

    func min() -> Double {
        var min = 0.0
        if let bufMin = buffer.min() {
            min = bufMin
        }
        return min
    }

    func max() -> Double {
        var max = 0.0
        if let bufMax = buffer.max() {
            max = bufMax
        }
        return max
    }

    func recentMean() -> Double {
        // Calculate the mean over the beginning half of the buffer.
        let recentCount = self.size / 2
        var mean = 0.0

        if (buffer.count >= recentCount) {
            let recentBuffer = buffer[0..<recentCount]
            mean = recentBuffer.reduce(0.0, +) / Double(recentBuffer.count)
        }

        return mean
    }
}
```

[Next](LICENSE.txt.md)[Previous](SwingWatch%20WatchKit%20Extension-MotionManager.swift.md)

