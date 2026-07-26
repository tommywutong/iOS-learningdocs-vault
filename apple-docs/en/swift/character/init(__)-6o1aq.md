---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/character/init(_:)-6o1aq'
source_url: 'https://developer.apple.com/documentation/swift/character/init(_:)-6o1aq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/init%28_%3A%29-6o1aq.json'
content_hash: 'sha256:12dedfb7e6a42725'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# init(_:)

<sub>Initializer</sub>

Creates a character from a single-character string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ s: String)
```

## Parameters

- `s` — The single-character string to convert to a `Character` instance. `s` must contain exactly one extended grapheme cluster.

## Discussion

The following example creates a new character from the uppercase version of a string that only holds one character.

```swift
let a = "a"
let capitalA = Character(a.uppercased())
```
