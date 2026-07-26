---
title: 'registerDataRepresentation(forTypeIdentifier:visibility:loadHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registerdatarepresentation(fortypeidentifier:visibility:loadhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registerdatarepresentation(fortypeidentifier:visibility:loadhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registerdatarepresentation%28fortypeidentifier%3Avisibility%3Aloadhandler%3A%29.json'
content_hash: 'sha256:3f0e7ecb984a2b4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerDataRepresentation(forTypeIdentifier:visibility:loadHandler:)

<sub>Instance Method</sub>

Registers a data-backed representation for an item, specifiying item visibility and a load handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func registerDataRepresentation(forTypeIdentifier typeIdentifier: String, visibility: NSItemProviderRepresentationVisibility, loadHandler: @escaping @Sendable (@escaping @Sendable (Data?, (any Error)?) -> Void) -> Progress?)
```

## See Also

### Registering data

- [registerDataRepresentation(for:visibility:loadHandler:)](<registerdatarepresentation(for_visibility_loadhandler_).md>) — Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [- registerItemForTypeIdentifier:loadHandler:](<registeritem(fortypeidentifier_loadhandler_).md>) — Lazily registers an item, according to the item provider type coercion policy. _(deprecated)_
