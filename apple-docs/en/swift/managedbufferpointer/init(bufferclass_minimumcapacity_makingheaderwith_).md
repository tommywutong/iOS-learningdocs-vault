---
title: 'init(bufferClass:minimumCapacity:makingHeaderWith:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/managedbufferpointer/init(bufferclass:minimumcapacity:makingheaderwith:)'
source_url: 'https://developer.apple.com/documentation/swift/managedbufferpointer/init(bufferclass:minimumcapacity:makingheaderwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managedbufferpointer/init%28bufferclass%3Aminimumcapacity%3Amakingheaderwith%3A%29.json'
content_hash: 'sha256:6b0d53f3fd32ed5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ManagedBufferPointer](../managedbufferpointer.md)

# init(bufferClass:minimumCapacity:makingHeaderWith:)

<sub>Initializer</sub>

Create with new storage containing an initial `Header` and space for at least `minimumCapacity` `element`s.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bufferClass: AnyClass, minimumCapacity: Int, makingHeaderWith factory: (AnyObject, (AnyObject) -> Int) throws -> Header) rethrows
```

## Parameters

- `bufferClass` — The class of the object used for storage.

- `minimumCapacity` — The minimum number of `Element`s that must be able to be stored in the new buffer.

- `factory` — A function that produces the initial `Header` instance stored in the buffer, given the `buffer` object and a function that can be called on it to get the actual number of allocated elements.

## Discussion

> [!info] Precondition
> `minimumCapacity >= 0`, and the type indicated by `bufferClass` is a non-`@objc` class with no declared stored properties.  The `deinit` of `bufferClass` must destroy its stored `Header` and any constructed `Element`s.

## See Also

### Creating a Buffer

- [init(unsafeBufferObject:)](<init(unsafebufferobject_).md>) — Manage the given `buffer`.
