---
title: AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy.repeatPreviousFrame
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum/repeatpreviousframe
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum/repeatpreviousframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum/repeatpreviousframe.json'
content_hash: 'sha256:f3fcca26c40247c3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureBroadcastVideoOutput](../../avcapturebroadcastvideooutput.md) · [DroppedFrameReplacementPolicy](../droppedframereplacementpolicy-swift.enum.md)

# AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy.repeatPreviousFrame

<sub>Case</sub>

Repeat the previous frame as replacement. When a frame is dropped, the most recent successfully output frame is repeated at the expected presentation time. This is the default behavior and provides smoother visual continuity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case repeatPreviousFrame
```
