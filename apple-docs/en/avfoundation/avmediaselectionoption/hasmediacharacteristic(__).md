---
title: 'hasMediaCharacteristic(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmediaselectionoption/hasmediacharacteristic(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/hasmediacharacteristic(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectionoption/hasmediacharacteristic%28_%3A%29.json'
content_hash: 'sha256:7113c8ae9f74982c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionOption](../avmediaselectionoption.md)

# hasMediaCharacteristic(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver has media with the given media characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hasMediaCharacteristic(_ mediaCharacteristic: AVMediaCharacteristic) -> Bool
```

## Parameters

- `mediaCharacteristic` — The media characteristic of interest, for example, [AVMediaCharacteristicVisual](../avmediacharacteristic/visual.md), [AVMediaCharacteristicAudible](../avmediacharacteristic/audible.md), or [AVMediaCharacteristicLegible](../avmediacharacteristic/legible.md).

## Return Value

[true](../../swift/true.md) if the media selection option has media with mediaCharacteristic, otherwise [false](../../swift/false.md).

## See Also

### Accessing media information

- [mediaType](mediatype.md) — The media type of the media data.
- [mediaSubTypes](mediasubtypes.md) — The media sub-types of the media data associated with the option.
