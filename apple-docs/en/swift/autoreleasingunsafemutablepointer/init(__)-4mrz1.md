---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/autoreleasingunsafemutablepointer/init(_:)-4mrz1'
source_url: 'https://developer.apple.com/documentation/swift/autoreleasingunsafemutablepointer/init(_:)-4mrz1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/autoreleasingunsafemutablepointer/init%28_%3A%29-4mrz1.json'
content_hash: 'sha256:1bf9f4ad29d14014'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AutoreleasingUnsafeMutablePointer](../autoreleasingunsafemutablepointer.md)

# init(_:)

<sub>Initializer</sub>

Explicit construction from an UnsafeMutablePointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<U>(_ from: UnsafeMutablePointer<U>)
```

## Discussion

This is inherently unsafe; UnsafeMutablePointer assumes the referenced memory has +1 strong ownership semantics, whereas AutoreleasingUnsafeMutablePointer implies +0 semantics.

> [!warning] Warning
> Accessing `pointee` as a type that is unrelated to the underlying memory’s bound type is undefined.

## See Also

### Converting Pointers

- [init(_:)](<init(__)-7rndr.md>) — Explicit construction from an UnsafeMutablePointer.
