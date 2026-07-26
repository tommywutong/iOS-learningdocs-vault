---
title: 'replacing(_:with:subrange:maxReplacements:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangereplaceablecollection/replacing(_:with:subrange:maxreplacements:)-1uswm'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/replacing(_:with:subrange:maxreplacements:)-1uswm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/replacing%28_%3Awith%3Asubrange%3Amaxreplacements%3A%29-1uswm.json'
content_hash: 'sha256:889084ebd32a29b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# replacing(_:with:subrange:maxReplacements:)

<sub>Instance Method</sub>

Returns a new collection in which all occurrences of a target sequence are replaced by another collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacing<C, Replacement>(_ other: C, with replacement: Replacement, subrange: Range<Self.Index>, maxReplacements: Int = .max) -> Self where C : Collection, Replacement : Collection, Self.Element == C.Element, C.Element == Replacement.Element
```

## Parameters

- `other` — The sequence to replace.

- `replacement` — The new elements to add to the collection.

- `subrange` — The range in the collection in which to search for `other`.

- `maxReplacements` — A number specifying how many occurrences of `other` to replace. Default is `Int.max`.

## Return Value

A new collection in which all occurrences of `other` in `subrange` of the collection are replaced by `replacement`.
