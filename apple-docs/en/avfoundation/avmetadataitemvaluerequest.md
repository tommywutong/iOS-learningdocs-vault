---
title: AVMetadataItemValueRequest
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataitemvaluerequest
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitemvaluerequest.json'
content_hash: 'sha256:448fd3d33ef3dea2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetadataItemValueRequest

<sub>Class</sub>

An object that responds to a request to load the value of a metadata item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMetadataItemValueRequest
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling the response

- [- respondWithValue:](<avmetadataitemvaluerequest/respond(value_).md>) — Returns the metadata item’s value.
- [- respondWithError:](<avmetadataitemvaluerequest/respond(error_).md>) — Returns an error when the system fails to load the value.
- [metadataItem](avmetadataitemvaluerequest/metadataitem.md) — The metadata item to request a value for.

## See Also

### Creating a metadata item

- [init(propertiesOfMetadataItem:valueLoadingHandler:)](<avmetadataitem/init(propertiesofmetadataitem_valueloadinghandler_).md>) — Creates a metadata item whose value loads on an on-demand basis only.
