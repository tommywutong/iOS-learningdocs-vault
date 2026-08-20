---
title: Hello Metronome
apple_id: TP40017587
resource_type: Sample Code
platform: watchOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-02-24'
source_url: https://developer.apple.com/library/archive/samplecode/HelloMetronome/Introduction/Intro.html
archived_at: '2026-07-18T03:11:50.945930Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](HelloMetronome-main.m.md)

# Hello Metronome

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2017-02-24 Added Swift triangle wave generator used by all targets and Swift Metronome class implementation for iOS target. General clean up and project reorganization.  [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tkobxfvjgk5tjonuw63sinfzxi33spewui33oorggs3tlivwgk3lfnz2esrc7ge) |
| __Build Requirements:__ | Xcode 8.2.1 or later |
| __Runtime Requirements:__ | macOS 10.11 or greater, iOS 10.0 or later, watchOS 3.0 or later |

Simple demonstration of a metronome using AVAudioEngine and AVAudioPlayerNode to schedule buffers for timing accurate playback using scheduleBuffer:atTime:options:completionHandler:. The implementation also provides for a delegate object to call with the method (metronomeTicking:bar:beat:) which can be used for timing or to provide UI.

The macOS version is a command line app and can use an included .caf file for the metronome bip sound or bips will be generated via a TriangleWaveGenerator class. Use the -f option to use the .caf file.

The iOS version provides a simple UI implementing the delegate method (metronomeTicking:bar:beat:) and uses the TriangleWaveGenerator class to generate the metronome bip sounds.

The watchOS version provides a slightly more complex UI with a delegate method to draw the animation for each tick and also uses the TriangleWaveGenerator class to generate the metronome bip sounds.

[Next](HelloMetronome-main.m.md)

