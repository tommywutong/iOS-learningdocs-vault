---
title: ManagedBuffer
framework: Swift
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/managedbuffer
source_url: 'https://developer.apple.com/documentation/swift/managedbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managedbuffer.json'
content_hash: 'sha256:70c3ca969d50efd3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ManagedBuffer

<sub>Class</sub>

A class whose instances contain a property of type `Header` and raw storage for an array of `Element`, whose size is determined at instance creation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class ManagedBuffer<Header, Element> where Element : ~Copyable
```

## Overview

Note that the `Element` array is suitably-aligned **raw memory**. You are expected to construct and—if necessary—destroy objects there yourself, using the APIs on `UnsafeMutablePointer<Element>`. Typical usage stores a count and capacity in `Header` and destroys any live elements in the `deinit` of a subclass.

> [!note] Note
> Subclasses must not have any stored properties; any storage needed should be included in `Header`.

## Topics

### Instance Properties

- [capacity](managedbuffer/capacity.md) — The actual number of elements that can be stored in this object.
- [header](managedbuffer/header.md) — The stored `Header` instance.

### Instance Methods

- [withUnsafeMutablePointerToElements(_:)](<managedbuffer/withunsafemutablepointertoelements(__).md>) — Call `body` with an `UnsafeMutablePointer` to the `Element` storage.
- [withUnsafeMutablePointerToHeader(_:)](<managedbuffer/withunsafemutablepointertoheader(__).md>) — Call `body` with an `UnsafeMutablePointer` to the stored `Header`.
- [withUnsafeMutablePointers(_:)](<managedbuffer/withunsafemutablepointers(__).md>) — Call `body` with `UnsafeMutablePointer`s to the stored `Header` and raw `Element` storage.

### Type Methods

- [create(minimumCapacity:makingHeaderWith:)](<managedbuffer/create(minimumcapacity_makingheaderwith_).md>) — Create a new instance of the most-derived class, calling `factory` on the partially-constructed object to generate an initial `Header`.

## See Also

### Buffer Implementation

- [ManagedBufferPointer](managedbufferpointer.md) — Contains a buffer object, and provides access to an instance of `Header` and contiguous storage for an arbitrary number of `Element` instances stored in that buffer.
