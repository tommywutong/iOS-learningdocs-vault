---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/inlinearray/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/inlinearray/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/inlinearray/init%28_%3A%29.json'
content_hash: 'sha256:f8c8b84258027bc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [InlineArray](../inlinearray.md)

# init(_:)

<sub>Initializer</sub>

Initializes every element in this array, by calling the given closure with each index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<E>(_ body: (InlineArray<count, Element>.Index) throws(E) -> Element) throws(E) where E : Error
```

## Parameters

- `body` — A closure that returns an owned `Element` to emplace at the passed in index.

## Discussion

This will call the closure `count` times, where `count` is the static count of the array, to initialize every element by passing the closure the index of the current element being initialized.

```swift
InlineArray<4, Int> { $0 * 2 }  // [0, 2, 4, 6]
```

The closure is allowed to throw an error at any point during initialization at which point the array will stop initialization, deinitialize every currently initialized element, and throw the given error back out to the caller.
