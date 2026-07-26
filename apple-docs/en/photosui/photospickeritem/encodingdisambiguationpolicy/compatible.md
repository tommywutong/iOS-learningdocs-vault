---
title: compatible
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/photospickeritem/encodingdisambiguationpolicy/compatible
source_url: 'https://developer.apple.com/documentation/photosui/photospickeritem/encodingdisambiguationpolicy/compatible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/photospickeritem/encodingdisambiguationpolicy/compatible.json'
content_hash: 'sha256:532e84c16d796354'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [PhotosUI](../../../photosui.md) · [PhotosPickerItem](../../photospickeritem.md) · [EncodingDisambiguationPolicy](../encodingdisambiguationpolicy.md)

# compatible

<sub>Type Property</sub>

An encoding policy that chooses the most compatible encoding even if transcoding is necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static let compatible: PhotosPickerItem.EncodingDisambiguationPolicy
```

## See Also

### Getting standard encoding policies

- [automatic](automatic.md) — An encoding policy that chooses the best encoding.
- [current](current.md) — An encoding policy that chooses the current encoding to avoid transcoding, if possible.
