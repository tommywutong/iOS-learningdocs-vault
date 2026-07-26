---
title: 'registerObject(ofClass:visibility:loadHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registerobject(ofclass:visibility:loadhandler:)-133rx'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registerobject(ofclass:visibility:loadhandler:)-133rx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registerobject%28ofclass%3Avisibility%3Aloadhandler%3A%29-133rx.json'
content_hash: 'sha256:2642208c04260f5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerObject(ofClass:visibility:loadHandler:)

<sub>Instance Method</sub>

Lazily adds representations of a specified object type to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func registerObject<T>(ofClass: T.Type, visibility: NSItemProviderRepresentationVisibility, loadHandler: @escaping @Sendable (@Sendable (T?, (any Error)?) -> Void) -> Progress?) where T : _ObjectiveCBridgeable, T._ObjectiveCType : NSItemProviderWriting
```

## See Also

### Registering objects

- [- registerObject:visibility:](<registerobject(__visibility_).md>) — Adds representations of a specified object to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [- registerObjectOfClass:visibility:loadHandler:](<registerobject(ofclass_visibility_loadhandler_)-9sndn.md>) — Lazily adds representations of a specified object class to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [register(_:)](<register(__).md>) — Adds representations of a specified transferable type to an item provider.
