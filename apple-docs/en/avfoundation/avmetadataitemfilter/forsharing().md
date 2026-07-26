---
title: forSharing()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataitemfilter/forsharing()
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitemfilter/forsharing()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitemfilter/forsharing%28%29.json'
content_hash: 'sha256:b43721a211ca75a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItemFilter](../avmetadataitemfilter.md)

# forSharing()

<sub>Type Method</sub>

Returns a metadata filter to use for sharing assets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func forSharing() -> AVMetadataItemFilter
```

## Return Value

An instance of an `AVMetadataItemFilter`.

## Discussion

Removes user-identifying metadata items, such as location information, and leaves only metadata related to commerce or playback itself. For example, playback, copyright, and commercial-related metadata, such as a purchaser’s ID as set by a vendor of digital media, along with metadata either derivable from the media itself or necessary for its proper behavior are all left intact.
