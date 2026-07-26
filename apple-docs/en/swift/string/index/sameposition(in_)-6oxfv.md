---
title: 'samePosition(in:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/index/sameposition(in:)-6oxfv'
source_url: 'https://developer.apple.com/documentation/swift/string/index/sameposition(in:)-6oxfv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/index/sameposition%28in%3A%29-6oxfv.json'
content_hash: 'sha256:0aff83181c9e0f92'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [Index](../index.md)

# samePosition(in:)

<sub>Instance Method</sub>

Returns the position in the given string that corresponds exactly to this index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func samePosition(in characters: String) -> String.Index?
```

## Parameters

- `characters` — The string to use for the index conversion. This index must be a valid index of at least one view of `characters`.

## Return Value

The position in `characters` that corresponds exactly to this index. If this index does not have an exact corresponding position in `characters`, this method returns `nil`. For example, an attempt to convert the position of a UTF-8 continuation byte returns `nil`.

## Discussion

This example first finds the position of a space (UTF-8 code point `32`) in a string’s `utf8` view and then uses this method find the same position in the string.

```swift
let cafe = "Café 🍵"
let i = cafe.unicodeScalars.firstIndex(of: "🍵")!
let j = i.samePosition(in: cafe)!
print(cafe[j...])
// Prints "🍵"
```
