---
title: automatic
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/photospickeritem/encodingdisambiguationpolicy/automatic
source_url: 'https://developer.apple.com/documentation/photosui/photospickeritem/encodingdisambiguationpolicy/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/photospickeritem/encodingdisambiguationpolicy/automatic.json'
content_hash: 'sha256:c8bfeeae9597f266'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [PhotosUI](../../../photosui.md) · [PhotosPickerItem](../../photospickeritem.md) · [EncodingDisambiguationPolicy](../encodingdisambiguationpolicy.md)

# automatic

<sub>Type Property</sub>

An encoding policy that chooses the best encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static let automatic: PhotosPickerItem.EncodingDisambiguationPolicy
```

## See Also

### Getting standard encoding policies

- [current](current.md) — An encoding policy that chooses the current encoding to avoid transcoding, if possible.
- [compatible](compatible.md) — An encoding policy that chooses the most compatible encoding even if transcoding is necessary.
