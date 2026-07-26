---
title: mediaSubTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectionoption/mediasubtypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/mediasubtypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectionoption/mediasubtypes.json'
content_hash: 'sha256:ef8ac41924f9437c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionOption](../avmediaselectionoption.md)

# mediaSubTypes

<sub>Instance Property</sub>

The media sub-types of the media data associated with the option.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mediaSubTypes: [NSNumber] { get }
```

## Discussion

The value is an array of `NSNumber` objects carrying four character codes (of type FourCharCode) as defined in `CoreAudioTypes.h` for audio media and in `CMFormatDescription.h` for video media.

Also see [CMFormatDescriptionGetMediaSubType(_:)](<../../coremedia/cmformatdescriptiongetmediasubtype(__).md>) for more information about media subtypes.

## See Also

### Accessing media information

- [mediaType](mediatype.md) — The media type of the media data.
- [- hasMediaCharacteristic:](<hasmediacharacteristic(__).md>) — Returns a Boolean value that indicates whether the receiver has media with the given media characteristic.
