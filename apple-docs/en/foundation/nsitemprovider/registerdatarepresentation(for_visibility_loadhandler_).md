---
title: 'registerDataRepresentation(for:visibility:loadHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registerdatarepresentation(for:visibility:loadhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registerdatarepresentation(for:visibility:loadhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registerdatarepresentation%28for%3Avisibility%3Aloadhandler%3A%29.json'
content_hash: 'sha256:72ac6315e07f0891'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerDataRepresentation(for:visibility:loadHandler:)

<sub>Instance Method</sub>

Registers a data-backed representation for an item, specifiying item visibility and a load handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func registerDataRepresentation(for contentType: UTType, visibility: NSItemProviderRepresentationVisibility = .all, loadHandler: @escaping @Sendable (@escaping (Data?, (any Error)?) -> Void) -> Progress?)
```

## See Also

### Registering data

- [- registerDataRepresentationForTypeIdentifier:visibility:loadHandler:](<registerdatarepresentation(fortypeidentifier_visibility_loadhandler_).md>) — Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [- registerItemForTypeIdentifier:loadHandler:](<registeritem(fortypeidentifier_loadhandler_).md>) — Lazily registers an item, according to the item provider type coercion policy. _(deprecated)_
