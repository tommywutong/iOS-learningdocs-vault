---
title: 'withUnsafeMutablePointerToElements(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/managedbufferpointer/withunsafemutablepointertoelements(_:)'
source_url: 'https://developer.apple.com/documentation/swift/managedbufferpointer/withunsafemutablepointertoelements(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managedbufferpointer/withunsafemutablepointertoelements%28_%3A%29.json'
content_hash: 'sha256:33f70dd52f2e98f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ManagedBufferPointer](../managedbufferpointer.md)

# withUnsafeMutablePointerToElements(_:)

<sub>Instance Method</sub>

Call `body` with an `UnsafeMutablePointer` to the `Element` storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeMutablePointerToElements<E, R>(_ body: (UnsafeMutablePointer<Element>) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

## Discussion

> [!note] Note
> This pointer is valid only for the duration of the call to `body`. The caller is responsible for ensuring that the buffer is not being accessed anyone else while performing this call.

## See Also

### Accessing Buffer Contents

- [withUnsafeMutablePointerToHeader(_:)](<withunsafemutablepointertoheader(__).md>) — Call `body` with an `UnsafeMutablePointer` to the stored `Header`.
- [withUnsafeMutablePointers(_:)](<withunsafemutablepointers(__).md>) — Call `body` with `UnsafeMutablePointer`s to the stored `Header` and raw `Element` storage.
