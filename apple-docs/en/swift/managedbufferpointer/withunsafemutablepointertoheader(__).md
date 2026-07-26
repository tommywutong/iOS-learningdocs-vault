---
title: 'withUnsafeMutablePointerToHeader(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/managedbufferpointer/withunsafemutablepointertoheader(_:)'
source_url: 'https://developer.apple.com/documentation/swift/managedbufferpointer/withunsafemutablepointertoheader(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managedbufferpointer/withunsafemutablepointertoheader%28_%3A%29.json'
content_hash: 'sha256:301f4e0d32297d7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ManagedBufferPointer](../managedbufferpointer.md)

# withUnsafeMutablePointerToHeader(_:)

<sub>Instance Method</sub>

Call `body` with an `UnsafeMutablePointer` to the stored `Header`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeMutablePointerToHeader<E, R>(_ body: (UnsafeMutablePointer<Header>) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

## Discussion

> [!note] Note
> This pointer is valid only for the duration of the call to `body`. The caller is responsible for ensuring that the buffer is not being accessed anyone else while performing this call.

## See Also

### Accessing Buffer Contents

- [withUnsafeMutablePointerToElements(_:)](<withunsafemutablepointertoelements(__).md>) — Call `body` with an `UnsafeMutablePointer` to the `Element` storage.
- [withUnsafeMutablePointers(_:)](<withunsafemutablepointers(__).md>) — Call `body` with `UnsafeMutablePointer`s to the stored `Header` and raw `Element` storage.
