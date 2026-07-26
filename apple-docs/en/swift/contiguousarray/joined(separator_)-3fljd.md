---
title: 'joined(separator:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/contiguousarray/joined(separator:)-3fljd'
source_url: 'https://developer.apple.com/documentation/swift/contiguousarray/joined(separator:)-3fljd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/contiguousarray/joined%28separator%3A%29-3fljd.json'
content_hash: 'sha256:3585db6a725b9c29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ContiguousArray](../contiguousarray.md)

# joined(separator:)

<sub>Instance Method</sub>

Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func joined(separator: String = "") -> String
```

## Parameters

- `separator` — A string to insert between each of the elements in this sequence. The default separator is an empty string.

## Return Value

A single, concatenated string.

## Discussion

The following example shows how an array of strings can be joined to a single, comma-separated string:

```swift
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
let list = cast.joined(separator: ", ")
print(list)
// Prints "Vivien, Marlon, Kim, Karl"
```
