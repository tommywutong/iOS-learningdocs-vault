---
title: UniqueArray.Index
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/uniquearray/index
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/index'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/index.json'
content_hash: 'sha256:0b8e7bf3c55fe43f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# UniqueArray.Index

<sub>Type Alias</sub>

A type that represents a position in the array: an integer offset from the start.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Index = Int
```

## Discussion

Valid indices consist of the position of every element and a “past the end” position that’s not valid for use as a subscript argument.
