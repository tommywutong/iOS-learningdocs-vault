---
title: 'isPlayableExtendedMIMEType(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avurlasset/isplayableextendedmimetype(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset/isplayableextendedmimetype(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset/isplayableextendedmimetype%28_%3A%29.json'
content_hash: 'sha256:224d3ae55971d3d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVURLAsset](../avurlasset.md)

# isPlayableExtendedMIMEType(_:)

<sub>Type Method</sub>

Returns a Boolean value that indicates whether the asset is playable with the specified codecs and container type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func isPlayableExtendedMIMEType(_ extendedMIMEType: String) -> Bool
```

## Parameters

- `extendedMIMEType` — An extended MIME type string such as `video/3gpp2; codecs=“mp4v.20.9, mp4a.E1”` or `audio/aac; codecs=“mp4a.E1”`.

## Return Value

[true](../../swift/true.md) if the asset is playable with the specified codec and container type; otherwise, [false](../../swift/false.md).

## See Also

### Determining supported media types

- [+ audiovisualTypes](<audiovisualtypes().md>) — Returns an array of the file types the asset supports. _(deprecated)_
- [+ audiovisualMIMETypes](<audiovisualmimetypes().md>) — Returns an array of the MIME types the asset supports.
- [audiovisualContentTypes](audiovisualcontenttypes.md) — Provides the content types the AVURLAsset class understands.
