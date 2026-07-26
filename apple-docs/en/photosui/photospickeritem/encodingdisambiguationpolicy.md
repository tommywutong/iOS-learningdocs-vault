---
title: PhotosPickerItem.EncodingDisambiguationPolicy
framework: PhotosUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/photospickeritem/encodingdisambiguationpolicy
source_url: 'https://developer.apple.com/documentation/photosui/photospickeritem/encodingdisambiguationpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/photospickeritem/encodingdisambiguationpolicy.json'
content_hash: 'sha256:42a91ed6c1a78ca9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PhotosPickerItem](../photospickeritem.md)

# PhotosPickerItem.EncodingDisambiguationPolicy

<sub>Structure</sub>

A type that determines the encoding to use when multiple encodings are available, based on the content type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct EncodingDisambiguationPolicy
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting standard encoding policies

- [automatic](encodingdisambiguationpolicy/automatic.md) — An encoding policy that chooses the best encoding.
- [current](encodingdisambiguationpolicy/current.md) — An encoding policy that chooses the current encoding to avoid transcoding, if possible.
- [compatible](encodingdisambiguationpolicy/compatible.md) — An encoding policy that chooses the most compatible encoding even if transcoding is necessary.
