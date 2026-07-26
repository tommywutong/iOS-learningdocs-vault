---
title: 'contains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/reversedcollection/contains(_:)'
source_url: 'https://developer.apple.com/documentation/swift/reversedcollection/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/reversedcollection/contains%28_%3A%29.json'
content_hash: 'sha256:38c7fc9732c983db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ReversedCollection](../reversedcollection.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the sequence contains the given element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ element: Self.Element) -> Bool
```

## Parameters

- `element` — The element to find in the sequence.

## Return Value

`true` if the element was found in the sequence; otherwise, `false`.

## Discussion

This example checks to see whether a favorite actor is in an array storing a movie’s cast.

```swift
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
print(cast.contains("Marlon"))
// Prints "true"
print(cast.contains("James"))
// Prints "false"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the sequence.
