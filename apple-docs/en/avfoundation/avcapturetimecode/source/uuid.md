---
title: uuid
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecode/source/uuid
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecode/source/uuid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecode/source/uuid.json'
content_hash: 'sha256:0817b021a77c733f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureTimecode](../../avcapturetimecode.md) · [Source](../source.md)

# uuid

<sub>Instance Property</sub>

A unique identifier for the timecode source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var uuid: UUID { get }
```

## Discussion

The UUID uniquely identifies this timecode source. It is particularly useful when multiple sources of the same type are available, allowing your application to distinguish between them.

> [!note] Note
> This value does not persist across application sessions.

## See Also

### Inspecting the source

- [displayName](displayname.md) — The name of the timecode source.
- [type](type.md) — The type of timecode source.
