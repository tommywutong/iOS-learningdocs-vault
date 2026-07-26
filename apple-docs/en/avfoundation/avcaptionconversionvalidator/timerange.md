---
title: timeRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionconversionvalidator/timerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/timerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversionvalidator/timerange.json'
content_hash: 'sha256:62dfcbc26a1eb28c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionConversionValidator](../avcaptionconversionvalidator.md)

# timeRange

<sub>Instance Property</sub>

The time range of the media timeline in which the captions must exist.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var timeRange: CMTimeRange { get }
```

## Discussion

If captions need to appear only after the start of the associated media, the start time of this time range can be less than the start time of the first caption’s time range.

If the media duration is unknown, this time range can have a duration of [positiveInfinity](../../coremedia/cmtime/positiveinfinity.md). However, to comprehensively validate the conversion of closed captions, set the duration of the time range to the duration of the associated media.

## See Also

### Inspecting the validator

- [captions](captions.md) — The array of captions that the system validates.
