---
title: 'replacing(_:with:maxReplacements:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangereplaceablecollection/replacing(_:with:maxreplacements:)-6y22p'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/replacing(_:with:maxreplacements:)-6y22p'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/replacing%28_%3Awith%3Amaxreplacements%3A%29-6y22p.json'
content_hash: 'sha256:6a25f51325df8b68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# replacing(_:with:maxReplacements:)

<sub>Instance Method</sub>

Returns a new collection in which all occurrences of a target sequence are replaced by another collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacing<C, Replacement>(_ other: C, with replacement: Replacement, maxReplacements: Int = .max) -> Self where C : Collection, Replacement : Collection, Self.Element == C.Element, C.Element == Replacement.Element
```

## Parameters

- `other` — The sequence to replace.

- `replacement` — The new elements to add to the collection.

- `maxReplacements` — A number specifying how many occurrences of `other` to replace. Default is `Int.max`.

## Return Value

A new collection in which all occurrences of `other` in `subrange` of the collection are replaced by `replacement`.
