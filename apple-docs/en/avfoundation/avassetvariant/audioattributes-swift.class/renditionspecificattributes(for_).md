---
title: 'renditionSpecificAttributes(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes%28for%3A%29.json'
content_hash: 'sha256:29559c4de38f124a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetVariant](../../avassetvariant.md) · [AudioAttributes](../audioattributes-swift.class.md)

# renditionSpecificAttributes(for:)

<sub>Instance Method</sub>

Returns specific attributes for the media option.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func renditionSpecificAttributes(for mediaSelectionOption: AVMediaSelectionOption) -> AVAssetVariant.AudioAttributes.RenditionSpecificAttributes?
```

## Parameters

- `mediaSelectionOption` — The media option for which to retrieve attributes.

## Return Value

Attributes for the rendition, or `nil` of none exist.

## See Also

### Inspecting audio attributes

- [formatIDs](formatids.md) — The audio formats of the renditions present in the variant.
- [RenditionSpecificAttributes](renditionspecificattributes.md) — An object that represents attributes specific to a particular rendition.
