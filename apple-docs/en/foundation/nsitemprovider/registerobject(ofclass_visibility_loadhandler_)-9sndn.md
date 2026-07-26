---
title: 'registerObject(ofClass:visibility:loadHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registerobject(ofclass:visibility:loadhandler:)-9sndn'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registerobject(ofclass:visibility:loadhandler:)-9sndn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registerobject%28ofclass%3Avisibility%3Aloadhandler%3A%29-9sndn.json'
content_hash: 'sha256:747247f66747835c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerObject(ofClass:visibility:loadHandler:)

<sub>Instance Method</sub>

Lazily adds representations of a specified object class to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func registerObject(ofClass aClass: any NSItemProviderWriting.Type, visibility: NSItemProviderRepresentationVisibility, loadHandler: @escaping @Sendable (@escaping @Sendable ((any NSItemProviderWriting)?, (any Error)?) -> Void) -> Progress?)
```

## See Also

### Registering objects

- [- registerObject:visibility:](<registerobject(__visibility_).md>) — Adds representations of a specified object to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [registerObject(ofClass:visibility:loadHandler:)](<registerobject(ofclass_visibility_loadhandler_)-133rx.md>) — Lazily adds representations of a specified object type to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [register(_:)](<register(__).md>) — Adds representations of a specified transferable type to an item provider.
