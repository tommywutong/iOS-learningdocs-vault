---
title: 'startRecording(to:outputFileType:recordingDelegate:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureaudiofileoutput/startrecording(to:outputfiletype:recordingdelegate:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiofileoutput/startrecording(to:outputfiletype:recordingdelegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiofileoutput/startrecording%28to%3Aoutputfiletype%3Arecordingdelegate%3A%29.json'
content_hash: 'sha256:4d9d6c7b5be072c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureAudioFileOutput](../avcaptureaudiofileoutput.md)

# startRecording(to:outputFileType:recordingDelegate:)

<sub>Instance Method</sub>

Tells the receiver to start recording to a new file of the specified format, and specifies a delegate that will be notified when recording is finished.

<sub>macOS</sub>

```swift
func startRecording(to outputFileURL: URL, outputFileType fileType: AVFileType, recordingDelegate delegate: any AVCaptureFileOutputRecordingDelegate)
```

## Parameters

- `outputFileURL` — The URL of the output file. This method throws an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) if the URL is not a valid file URL. If a file at the given URL already exists when capturing starts, recording to the new file will fail.

- `fileType` — A UTI indicating the format of the file to be written. UTIs for common audio file types are declared in `AVMediaFormat.h`.

- `delegate` — An object conforming to the [AVCaptureFileOutputRecordingDelegate](../avcapturefileoutputrecordingdelegate.md) protocol. You must specify a delegate to be notified when recording is finished.

## Discussion

You do not need not to call [- stopRecording](<../avcapturefileoutput/stoprecording().md>) before calling this method while another recording is in progress. If this method is invoked while an existing output file was already being recorded, no media samples will be discarded between the old file and the new file.

When recording is stopped—by calling `stopRecording`, by changing files using this method, or because of an error—the remaining data that needs to be included to the file will be written in the background. Therefore, you must specify a delegate that will be notified when all data has been written to the file using the [- captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:](<../avcapturefileoutputrecordingdelegate/fileoutput(__didfinishrecordingto_from_error_).md>) method. The recording delegate can also optionally implement methods that inform it when data starts being written, when recording is paused and resumed, and when recording is about to be finished.

In macOS, if this method is called within the [- captureOutput:didOutputSampleBuffer:fromConnection:](<../avcaptureaudiodataoutputsamplebufferdelegate/captureoutput(__didoutput_from_).md>) delegate method, the first samples written to the new file are guaranteed to be those contained in the sample buffer passed to that method.
