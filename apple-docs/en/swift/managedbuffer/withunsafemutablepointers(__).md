---
title: 'withUnsafeMutablePointers(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/managedbuffer/withunsafemutablepointers(_:)'
source_url: 'https://developer.apple.com/documentation/swift/managedbuffer/withunsafemutablepointers(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managedbuffer/withunsafemutablepointers%28_%3A%29.json'
content_hash: 'sha256:0c144c9352b6548c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ManagedBuffer](../managedbuffer.md)

# withUnsafeMutablePointers(_:)

<sub>Instance Method</sub>

Call `body` with `UnsafeMutablePointer`s to the stored `Header` and raw `Element` storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func withUnsafeMutablePointers<E, R>(_ body: (UnsafeMutablePointer<Header>, UnsafeMutablePointer<Element>) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

## Discussion

> [!note] Note
> These pointers are valid only for the duration of the call to `body`. The caller is responsible for ensuring that the buffer is not being accessed elsewhere while performing this call.
