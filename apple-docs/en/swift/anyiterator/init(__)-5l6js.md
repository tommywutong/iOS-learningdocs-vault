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
doc_path: '/documentation/swift/anyiterator/init(_:)-5l6js'
source_url: 'https://developer.apple.com/documentation/swift/anyiterator/init(_:)-5l6js'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyiterator/init%28_%3A%29-5l6js.json'
content_hash: 'sha256:4b5cff4ea9b75d5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyIterator](../anyiterator.md)

# init(_:)

<sub>Initializer</sub>

Creates an iterator that wraps the given closure in its `next()` method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ body: @escaping () -> Element?)
```

## Parameters

- `body` — A closure that returns an optional element. `body` is executed each time the `next()` method is called on the resulting iterator.

## Discussion

The following example creates an iterator that counts up from the initial value of an integer `x` to 15:

```swift
var x = 7
let iterator: AnyIterator<Int> = AnyIterator {
    defer { x += 1 }
    return x < 15 ? x : nil
}
let a = Array(iterator)
// a == [7, 8, 9, 10, 11, 12, 13, 14]
```
