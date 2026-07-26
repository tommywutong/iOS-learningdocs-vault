---
title: 'register(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/register(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/register(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/register%28_%3A%29.json'
content_hash: 'sha256:a5bd24e39c500da2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# register(_:)

<sub>Instance Method</sub>

Adds representations of a specified transferable type to an item provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func register<T>(_ transferable: @autoclosure @escaping @Sendable () -> T) where T : Transferable
```

## See Also

### Registering objects

- [- registerObject:visibility:](<registerobject(__visibility_).md>) — Adds representations of a specified object to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [- registerObjectOfClass:visibility:loadHandler:](<registerobject(ofclass_visibility_loadhandler_)-9sndn.md>) — Lazily adds representations of a specified object class to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [registerObject(ofClass:visibility:loadHandler:)](<registerobject(ofclass_visibility_loadhandler_)-133rx.md>) — Lazily adds representations of a specified object type to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
