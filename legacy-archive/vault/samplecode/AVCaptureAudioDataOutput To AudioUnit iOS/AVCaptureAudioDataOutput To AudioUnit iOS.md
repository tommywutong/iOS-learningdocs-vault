---
title: AVCaptureAudioDataOutput To AudioUnit iOS
apple_id: DTS40012880
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AVCaptureToAudioUnit/Introduction/Intro.html
archived_at: '2026-07-18T03:00:03.848636Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# AVCaptureAudioDataOutput To AudioUnit iOS

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2012-10-08 Demonstrates how to use the CMSampleBufferRefs vended by AVFoundation's capture AVCaptureAudioDataOutput object with various CoreAudio APIs. |
| __Build Requirements:__ | Xcode 4.5, iOS 6.0 SDK or later. |
| __Runtime Requirements:__ | iOS 6.0 SDK or later. Requires iOS device, AVFoundation Capture does not run in the simulator. |

AVCaptureToAudioUnit for iOS demonstrates how to use the CMSampleBufferRefs vended by AVFoundation's capture AVCaptureAudioDataOutput object with various CoreAudio APIs. The application uses a AVCaptureSession with a AVCaptureAudioDataOutput to capture audio from the default input, applies an effect to that audio using a simple delay effect AudioUnit and writes the modified audio to a file using the CoreAudio ExtAudioFile API. It also demonstrates using and AUGraph containing an AUConverter to convert the AVCaptureAudioDataOutput provided data format into a suitable format for the delay effect.

The CaptureSessionController class is responsible for setting up and running the AVCaptureSession and for passing the captured audio buffers to the CoreAudio AudioUnit and ExtAudioFile. The setupCaptureSession method is responsible for setting up the AVCaptureSession, while the captureOutput:didOutputSampleBuffer:fromConnection: passes the captured audio data through the AudioUnit via AudioUnitRender into the file using ExtAudioFileWriteAsync when recording.

CoreMedia provides two convenience methods to easily use the captured audio data with CoreAudio APIs. The CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer API fills in an AudioBufferList with the data from the CMSampleBuffer, and returns a CMBlockBuffer which references (and manages the lifetime of) the data in that AudioBufferList. This AudioBufferList can be used directly by AudioUnits and other CoreAudio objects. The CMSampleBufferGetNumSamples API returns the number of frames of audio contained within the sample buffer, a value that can also be passed directly to CoreAudio APIs.

Because CoreAudio AudioUnits process audio data using a "pull" model, but the AVCaptureAudioDataOutput object "pushes" audio sample buffers onto a client in real time, the captured buffers must be sent though the AudioUnit via an AudioUnit render callback which requests input audio data each time AudioUnitRender is called to retrieve output audio data. Every time captureOutput:didOutputSampleBuffer:fromConnection: receives a new sample buffer, it gets and stores the buffer as the Input AudioBufferList (so that the render callback can access it), and then immediately calls AudioUnitRender which synchronously pulls the stored input buffer list through the AudioUnit via the render callback. The output data is available in the output AudioBufferList passed to AudioUnitRender. This output buffer list may be passed to ExtAudioFile for final format conversion and writing to the file.

[Next](main.m.md)

