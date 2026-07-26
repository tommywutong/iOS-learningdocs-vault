---
title: audiovisualMIMETypes()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avurlasset/audiovisualmimetypes()
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset/audiovisualmimetypes()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset/audiovisualmimetypes%28%29.json'
content_hash: 'sha256:745ed7d6e11c1a40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVURLAsset](../avurlasset.md)

# audiovisualMIMETypes()

<sub>Type Method</sub>

Returns an array of the MIME types the asset supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func audiovisualMIMETypes() -> [String]
```

## Return Value

An array of MIME type strings.

## See Also

### Determining supported media types

- [+ audiovisualTypes](<audiovisualtypes().md>) — Returns an array of the file types the asset supports. _(deprecated)_
- [+ isPlayableExtendedMIMEType:](<isplayableextendedmimetype(__).md>) — Returns a Boolean value that indicates whether the asset is playable with the specified codecs and container type.
- [audiovisualContentTypes](audiovisualcontenttypes.md) — Provides the content types the AVURLAsset class understands.
