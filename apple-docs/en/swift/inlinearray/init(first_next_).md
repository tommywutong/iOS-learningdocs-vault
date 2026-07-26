---
title: 'init(first:next:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/inlinearray/init(first:next:)'
source_url: 'https://developer.apple.com/documentation/swift/inlinearray/init(first:next:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/inlinearray/init%28first%3Anext%3A%29.json'
content_hash: 'sha256:7bd282da0db0e1b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [InlineArray](../inlinearray.md)

# init(first:next:)

<sub>Initializer</sub>

Initializes every element in this array, by calling the given closure with each preceding element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<E>(first: consuming Element, next: (borrowing Element) throws(E) -> Element) throws(E) where E : Error
```

## Parameters

- `first` — The first value to emplace into the array.

- `next` — A closure that takes an immutable borrow reference to the preceding element, and returns an owned `Element` instance to emplace into the array.

## Discussion

This will call the closure `count - 1` times, where `count` is the static count of the array, to initialize every element by passing the closure an immutable borrow reference to the preceding element.

```swift
InlineArray<4, Int>(first: 1) { $0 * 2 }  // [1, 2, 4, 8]
```

The closure is allowed to throw an error at any point during initialization at which point the array will stop initialization, deinitialize every currently initialized element, and throw the given error back out to the caller.
