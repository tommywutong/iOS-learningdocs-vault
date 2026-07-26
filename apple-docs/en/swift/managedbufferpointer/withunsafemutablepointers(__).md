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
doc_path: '/documentation/swift/managedbufferpointer/withunsafemutablepointers(_:)'
source_url: 'https://developer.apple.com/documentation/swift/managedbufferpointer/withunsafemutablepointers(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managedbufferpointer/withunsafemutablepointers%28_%3A%29.json'
content_hash: 'sha256:bf456a38ba3757f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ManagedBufferPointer](../managedbufferpointer.md)

# withUnsafeMutablePointers(_:)

<sub>Instance Method</sub>

Call `body` with `UnsafeMutablePointer`s to the stored `Header` and raw `Element` storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeMutablePointers<E, R>(_ body: (UnsafeMutablePointer<Header>, UnsafeMutablePointer<Element>) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

## Discussion

> [!note] Note
> These pointers are valid only for the duration of the call to `body`. The caller is responsible for ensuring that the buffer is not being accessed elsewhere while performing this call.

## See Also

### Accessing Buffer Contents

- [withUnsafeMutablePointerToElements(_:)](<withunsafemutablepointertoelements(__).md>) — Call `body` with an `UnsafeMutablePointer` to the `Element` storage.
- [withUnsafeMutablePointerToHeader(_:)](<withunsafemutablepointertoheader(__).md>) — Call `body` with an `UnsafeMutablePointer` to the stored `Header`.
