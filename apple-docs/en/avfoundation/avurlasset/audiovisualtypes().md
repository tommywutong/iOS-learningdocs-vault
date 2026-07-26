---
title: audiovisualTypes()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avurlasset/audiovisualtypes()
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset/audiovisualtypes()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset/audiovisualtypes%28%29.json'
content_hash: 'sha256:b66beb1a4189f220'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVURLAsset](../avurlasset.md)

# audiovisualTypes()

<sub>Type Method</sub>

Returns an array of the file types the asset supports.

> [!warning] Deprecated
> Use audiovisualContentTypes instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func audiovisualTypes() -> [AVFileType]
```

## Return Value

An array of supported file types.

## See Also

### Determining supported media types

- [+ audiovisualMIMETypes](<audiovisualmimetypes().md>) — Returns an array of the MIME types the asset supports.
- [+ isPlayableExtendedMIMEType:](<isplayableextendedmimetype(__).md>) — Returns a Boolean value that indicates whether the asset is playable with the specified codecs and container type.
- [audiovisualContentTypes](audiovisualcontenttypes.md) — Provides the content types the AVURLAsset class understands.
