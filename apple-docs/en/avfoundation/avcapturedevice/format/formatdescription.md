---
title: formatDescription
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/formatdescription
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/formatdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/formatdescription.json'
content_hash: 'sha256:f586f8d18bf8b98a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# formatDescription

<sub>Instance Property</sub>

An object describing the capture format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var formatDescription: CMFormatDescription { get }
```

## Discussion

Calling this method doesn’t assume ownership of the returned [CMFormatDescription](../../../coremedia/cmformatdescription.md).

## See Also

### Determining supported media formats

- [mediaType](mediatype.md) — A constant describing the media type of an `AVCaptureDevice` active or supported format.
