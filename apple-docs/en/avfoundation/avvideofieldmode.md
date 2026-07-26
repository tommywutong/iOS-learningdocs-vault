---
title: AVVideoFieldMode
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideofieldmode
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideofieldmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideofieldmode.json'
content_hash: 'sha256:33886eaf9cc3a3cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoFieldMode

<sub>Enumeration</sub>

Constants that indicate which interlacing modes the connection applies to video flowing through it.

<sub>macOS</sub>

```swift
enum AVVideoFieldMode
```

## Overview

The values apply to the [videoFieldMode](avcaptureconnection/videofieldmode.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [AVVideoFieldModeBoth](avvideofieldmode/both.md) — A value that indicates that a video connection passes both the top and bottom video fields.
- [AVVideoFieldModeTopOnly](avvideofieldmode/toponly.md) — A value that indicates that a video connection only passes the top video field.
- [AVVideoFieldModeBottomOnly](avvideofieldmode/bottomonly.md) — A value that indicates that a video connection only passes the bottom video field.
- [AVVideoFieldModeDeinterlace](avvideofieldmode/deinterlace.md) — A value that indicates that a video connection deinterlaces the top and bottom video fields.

### Initializers

- [init(rawValue:)](<avvideofieldmode/init(rawvalue_).md>)

## See Also

### Interlacing video

- [supportsVideoFieldMode](avcaptureconnection/isvideofieldmodesupported.md) — A Boolean value that indicates whether the connection supports setting a video field mode.
- [videoFieldMode](avcaptureconnection/videofieldmode.md) — A setting that tells the connection how to interlace video flowing through it.
