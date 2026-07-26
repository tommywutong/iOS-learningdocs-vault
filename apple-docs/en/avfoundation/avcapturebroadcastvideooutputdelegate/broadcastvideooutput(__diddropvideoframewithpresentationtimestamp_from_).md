---
title: 'broadcastVideoOutput(_:didDropVideoFrameWithPresentationTimeStamp:from:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avcapturebroadcastvideooutputdelegate/broadcastvideooutput(_:diddropvideoframewithpresentationtimestamp:from:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutputdelegate/broadcastvideooutput(_:diddropvideoframewithpresentationtimestamp:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebroadcastvideooutputdelegate/broadcastvideooutput%28_%3Adiddropvideoframewithpresentationtimestamp%3Afrom%3A%29.json'
content_hash: 'sha256:3635c93dccdef9d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureBroadcastVideoOutputDelegate](../avcapturebroadcastvideooutputdelegate.md)

# broadcastVideoOutput(_:didDropVideoFrameWithPresentationTimeStamp:from:)

<sub>Instance Method</sub>

Called when a video frame is dropped during broadcast video output processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
optional func broadcastVideoOutput(_ output: AVCaptureBroadcastVideoOutput, didDropVideoFrameWithPresentationTimeStamp presentationTimeStamp: CMTime, from connection: AVCaptureConnection)
```

## Parameters

- `output` — The [AVCaptureBroadcastVideoOutput](../avcapturebroadcastvideooutput.md) instance that dropped the video frame.

- `presentationTimeStamp` — The presentation timestamp (PTS) of the dropped video frame.

- `connection` — The [AVCaptureConnection](../avcaptureconnection.md) associated with the dropped video frame.

## Discussion

This method is called whenever the broadcast video output system needs to drop a video frame due to performance constraints, destination issues, buffer overruns, or encoding failures.
