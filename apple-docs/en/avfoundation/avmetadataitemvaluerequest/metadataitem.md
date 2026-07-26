---
title: metadataItem
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataitemvaluerequest/metadataitem
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest/metadataitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitemvaluerequest/metadataitem.json'
content_hash: 'sha256:591098f273cfcbc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItemValueRequest](../avmetadataitemvaluerequest.md)

# metadataItem

<sub>Instance Property</sub>

The metadata item to request a value for.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var metadataItem: AVMetadataItem? { get }
```

## See Also

### Handling the response

- [- respondWithValue:](<respond(value_).md>) — Returns the metadata item’s value.
- [- respondWithError:](<respond(error_).md>) — Returns an error when the system fails to load the value.
