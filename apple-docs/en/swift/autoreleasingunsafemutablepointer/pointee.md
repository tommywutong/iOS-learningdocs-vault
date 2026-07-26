---
title: pointee
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/autoreleasingunsafemutablepointer/pointee
source_url: 'https://developer.apple.com/documentation/swift/autoreleasingunsafemutablepointer/pointee'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/autoreleasingunsafemutablepointer/pointee.json'
content_hash: 'sha256:2ff9caf997fa8f48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AutoreleasingUnsafeMutablePointer](../autoreleasingunsafemutablepointer.md)

# pointee

<sub>Instance Property</sub>

Retrieve or set the `Pointee` instance referenced by `self`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var pointee: Pointee { get nonmutating set }
```

## Discussion

`AutoreleasingUnsafeMutablePointer` is assumed to reference a value with `__autoreleasing` ownership semantics, like `NSFoo **` declarations in ARC. Setting the pointee autoreleases the new value before trivially storing it in the referenced memory.

> [!info] Precondition
> The pointee has been initialized with an instance of type `Pointee`.

## See Also

### Accessing a Pointer’s Memory

- [subscript(_:)](<subscript(__).md>) — Access the `i`th element of the raw array pointed to by `self`.
