---
title: 'indices(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/unicodescalarview/indices(of:)'
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview/indices(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview/indices%28of%3A%29.json'
content_hash: 'sha256:5b6ffefdcb129f2d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UnicodeScalarView](../unicodescalarview.md)

# indices(of:)

<sub>Instance Method</sub>

Returns the indices of all the elements that are equal to the given element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func indices(of element: Self.Element) -> RangeSet<Self.Index>
```

## Parameters

- `element` — An element to look for in the collection.

## Return Value

A set of the indices of the elements that are equal to `element`.

## Discussion

For example, you can use this method to find all the places that a particular letter occurs in a string.

```swift
let str = "Fresh cheese in a breeze"
let allTheEs = str.indices(of: "e")
// str[allTheEs].count == 7
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.
