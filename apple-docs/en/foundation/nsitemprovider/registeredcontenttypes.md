---
title: registeredContentTypes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemprovider/registeredcontenttypes
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registeredcontenttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registeredcontenttypes.json'
content_hash: 'sha256:87f1036521fce190'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registeredContentTypes

<sub>Instance Property</sub>

Registered content types in the order the app registers each type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var registeredContentTypes: [UTType] { get }
```

## Discussion

You app should register content types in order of fidelity. The system uses content types that appear earlier in the array.

## See Also

### Registering content types

- [registeredContentTypesForOpenInPlace](registeredcontenttypesforopeninplace.md) — Registered content types that the system can load as open-in-place files.
- [- registeredContentTypesConformingToContentType:](<registeredcontenttypes(conformingto_).md>) — Returns an array of registered content types that conform to a specified content type.
