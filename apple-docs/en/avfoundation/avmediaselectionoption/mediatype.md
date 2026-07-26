---
title: mediaType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectionoption/mediatype
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/mediatype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectionoption/mediatype.json'
content_hash: 'sha256:7d75667db357ad48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionOption](../avmediaselectionoption.md)

# mediaType

<sub>Instance Property</sub>

The media type of the media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mediaType: AVMediaType { get }
```

## Discussion

The value of the property might be, for example, [AVMediaTypeAudio](../avmediatype/audio.md) or [AVMediaTypeSubtitle](../avmediatype/subtitle.md).

## See Also

### Accessing media information

- [mediaSubTypes](mediasubtypes.md) — The media sub-types of the media data associated with the option.
- [- hasMediaCharacteristic:](<hasmediacharacteristic(__).md>) — Returns a Boolean value that indicates whether the receiver has media with the given media characteristic.
