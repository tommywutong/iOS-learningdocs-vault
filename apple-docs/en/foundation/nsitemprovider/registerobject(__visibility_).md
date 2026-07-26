---
title: 'registerObject(_:visibility:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registerobject(_:visibility:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registerobject(_:visibility:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registerobject%28_%3Avisibility%3A%29.json'
content_hash: 'sha256:a042ebcb0d8f6319'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerObject(_:visibility:)

<sub>Instance Method</sub>

Adds representations of a specified object to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func registerObject(_ object: any NSItemProviderWriting, visibility: NSItemProviderRepresentationVisibility)
```

## Discussion

If a representation for a given UTI is already registered, it is preserved (specifically, duplicate representations are ignored).

## See Also

### Registering objects

- [- registerObjectOfClass:visibility:loadHandler:](<registerobject(ofclass_visibility_loadhandler_)-9sndn.md>) — Lazily adds representations of a specified object class to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [registerObject(ofClass:visibility:loadHandler:)](<registerobject(ofclass_visibility_loadhandler_)-133rx.md>) — Lazily adds representations of a specified object type to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [register(_:)](<register(__).md>) — Adds representations of a specified transferable type to an item provider.
