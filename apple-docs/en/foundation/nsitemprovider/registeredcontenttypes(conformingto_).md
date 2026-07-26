---
title: 'registeredContentTypes(conformingTo:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registeredcontenttypes(conformingto:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registeredcontenttypes(conformingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registeredcontenttypes%28conformingto%3A%29.json'
content_hash: 'sha256:741c5aceb49dbbc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registeredContentTypes(conformingTo:)

<sub>Instance Method</sub>

Returns an array of registered content types that conform to a specified content type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func registeredContentTypes(conformingTo contentType: UTType) -> [UTType]
```

## Parameters

- `contentType` — The specified content type.

## Return Value

An array of registered content types.

## See Also

### Registering content types

- [registeredContentTypes](registeredcontenttypes.md) — Registered content types in the order the app registers each type.
- [registeredContentTypesForOpenInPlace](registeredcontenttypesforopeninplace.md) — Registered content types that the system can load as open-in-place files.
