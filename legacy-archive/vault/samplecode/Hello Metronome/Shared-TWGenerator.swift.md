---
title: Hello Metronome
apple_id: TP40017587
resource_type: Sample Code
platform: watchOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-02-24'
source_url: https://developer.apple.com/library/archive/samplecode/HelloMetronome/Listings/Shared_TWGenerator_swift.html
archived_at: '2026-07-18T03:11:51.447666Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Hello Metronome](Hello%20Metronome.md)


[Next](LICENSE.txt.md)[Previous](iOSHelloMetronome-ViewController.m.md)

# Shared/TWGenerator.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Triangle Wave Generator
*/

import Foundation
import AVFoundation

class TriangleWaveGenerator : NSObject {
    var mSampleRate: Float = 44100.0
    var mFreqHz: Float = 440.0
    var mAmplitude: Float = 0.25
    var mFrameCount: Float = 0.0

    override init() {
        super.init()
    }

    convenience init(sampleRate: Float) {
        self.init(sampleRate: sampleRate, frequency: 440.0, amplitude: 0.25)
    }

    convenience init(sampleRate: Float, frequency: Float) {
        self.init(sampleRate: sampleRate, frequency: frequency, amplitude: 0.25)
    }

    init(sampleRate: Float, frequency: Float, amplitude: Float) {
        super.init()

        self.mSampleRate = sampleRate
        self.mFreqHz = frequency
        self.mAmplitude = amplitude
    }

    func render(_ buffer: AVAudioPCMBuffer) {
        print("Buffer: \(buffer.format.description) \(buffer.description)\n")

        let nFrames = buffer.frameLength
        let nChannels = buffer.format.channelCount
        let isInterleaved = buffer.format.isInterleaved

        let amp = mAmplitude

        let phaseStep = mFreqHz / mSampleRate;

        if (isInterleaved) {
            var ptr = buffer.floatChannelData?[0]

            for frame in 0 ..< nFrames {
                let phase = fmodf(Float(frame) * phaseStep, 1.0)
                let value = (fabsf(2.0 - 4.0 * phase) - 1.0) * amp;

                for _ in 0 ..< nChannels {
                    ptr?.pointee = value;
                    ptr = ptr?.successor()
                }
            }
        } else {
            for ch in 0 ..< nChannels {
                var ptr = buffer.floatChannelData?[Int(ch)]

                for frame in 0 ..< nFrames {
                    let phase = fmodf(Float(frame) * phaseStep, 1.0)
                    let value = (fabsf(2.0 - 4.0 * phase) - 1.0) * amp;

                    ptr?.pointee = value

                    ptr = ptr?.successor()
                }
            }
        }
        mFrameCount = Float(nFrames);
    }
}
```

[Next](LICENSE.txt.md)[Previous](iOSHelloMetronome-ViewController.m.md)

