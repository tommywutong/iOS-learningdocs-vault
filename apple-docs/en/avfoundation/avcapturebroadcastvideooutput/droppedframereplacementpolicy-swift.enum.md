---
title: AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum.json'
content_hash: 'sha256:219d4b08d3af4ea1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureBroadcastVideoOutput](../avcapturebroadcastvideooutput.md)

# AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy

<sub>Enumeration</sub>

Constants indicating the replacement policy when a video frame is dropped.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum DroppedFrameReplacementPolicy
```

## Overview

These constants specify how the broadcast video output should handle dropped frames by providing replacement content.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [AVCaptureBroadcastVideoOutputDroppedFrameReplacementPolicyBlackFrame](droppedframereplacementpolicy-swift.enum/blackframe.md) — Insert a black frame as replacement. When a frame is dropped, a black frame is inserted at the expected presentation time. This maintains output timing continuity while providing a clear visual indication of the dropped frame. _(beta)_
- [AVCaptureBroadcastVideoOutputDroppedFrameReplacementPolicyRepeatPreviousFrame](droppedframereplacementpolicy-swift.enum/repeatpreviousframe.md) — Repeat the previous frame as replacement. When a frame is dropped, the most recent successfully output frame is repeated at the expected presentation time. This is the default behavior and provides smoother visual continuity. _(beta)_

### Initializers

- [init(rawValue:)](<droppedframereplacementpolicy-swift.enum/init(rawvalue_).md>) _(beta)_
