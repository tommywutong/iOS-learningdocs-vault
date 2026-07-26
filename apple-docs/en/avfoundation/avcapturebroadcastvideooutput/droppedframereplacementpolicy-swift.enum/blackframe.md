---
title: AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy.blackFrame
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum/blackframe
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum/blackframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum/blackframe.json'
content_hash: 'sha256:ae617859b2202a52'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureBroadcastVideoOutput](../../avcapturebroadcastvideooutput.md) · [DroppedFrameReplacementPolicy](../droppedframereplacementpolicy-swift.enum.md)

# AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy.blackFrame

<sub>Case</sub>

Insert a black frame as replacement. When a frame is dropped, a black frame is inserted at the expected presentation time. This maintains output timing continuity while providing a clear visual indication of the dropped frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case blackFrame
```
