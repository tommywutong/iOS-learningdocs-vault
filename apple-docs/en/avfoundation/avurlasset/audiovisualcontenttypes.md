---
title: audiovisualContentTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avurlasset/audiovisualcontenttypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset/audiovisualcontenttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset/audiovisualcontenttypes.json'
content_hash: 'sha256:75922d14abf0e52c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVURLAsset](../avurlasset.md)

# audiovisualContentTypes

<sub>Type Property</sub>

Provides the content types the AVURLAsset class understands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var audiovisualContentTypes: [UTType] { get }
```

## Return Value

An NSArray of UTTypes identifying the content types the AVURLAsset class understands.

## See Also

### Determining supported media types

- [+ audiovisualTypes](<audiovisualtypes().md>) — Returns an array of the file types the asset supports. _(deprecated)_
- [+ audiovisualMIMETypes](<audiovisualmimetypes().md>) — Returns an array of the MIME types the asset supports.
- [+ isPlayableExtendedMIMEType:](<isplayableextendedmimetype(__).md>) — Returns a Boolean value that indicates whether the asset is playable with the specified codecs and container type.
