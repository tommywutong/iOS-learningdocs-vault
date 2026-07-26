---
title: 'init(_:within:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/index/init(_:within:)-2u3iq'
source_url: 'https://developer.apple.com/documentation/swift/string/index/init(_:within:)-2u3iq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/index/init%28_%3Awithin%3A%29-2u3iq.json'
content_hash: 'sha256:7def66d05a99314c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [Index](../index.md)

# init(_:within:)

<sub>Initializer</sub>

Creates an index in the given string that corresponds exactly to the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ sourcePosition: String.Index, within target: String)
```

## Parameters

- `sourcePosition` — A position in a view of the `target` parameter. `sourcePosition` must be a valid index of at least one of the views of `target`.

- `target` — The string referenced by the resulting index.

## Discussion

If the index passed as `sourcePosition` represents the start of an extended grapheme cluster—the element type of a string—then the initializer succeeds.

The following example converts the position of the Unicode scalar `"e"` into its corresponding position in the string. The character at that position is the composed `"é"` character.

```swift
let cafe = "Cafe\u{0301}"
print(cafe)
// Prints "Café"

let scalarsIndex = cafe.unicodeScalars.firstIndex(of: "e")!
let stringIndex = String.Index(scalarsIndex, within: cafe)!

print(cafe[...stringIndex])
// Prints "Café"
```

If the index passed as `sourcePosition` doesn’t have an exact corresponding position in `target`, the result of the initializer is `nil`. For example, an attempt to convert the position of the combining acute accent (`"\u{0301}"`) fails. Combining Unicode scalars do not have their own position in a string.

```swift
let nextScalarsIndex = cafe.unicodeScalars.index(after: scalarsIndex)
let nextStringIndex = String.Index(nextScalarsIndex, within: cafe)

print(nextStringIndex)
// Prints "nil"
```
