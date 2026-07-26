---
title: 'replace(_:with:maxReplacements:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangereplaceablecollection/replace(_:with:maxreplacements:)-5u0yu'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/replace(_:with:maxreplacements:)-5u0yu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/replace%28_%3Awith%3Amaxreplacements%3A%29-5u0yu.json'
content_hash: 'sha256:895a0a5567ee8844'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# replace(_:with:maxReplacements:)

<sub>Instance Method</sub>

Replaces all occurrences of a target sequence with a given collection

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replace<C, Replacement>(_ other: C, with replacement: Replacement, maxReplacements: Int = .max) where C : Collection, Replacement : Collection, Self.Element == C.Element, C.Element == Replacement.Element
```

## Parameters

- `other` — The sequence to replace.

- `replacement` — The new elements to add to the collection.

- `maxReplacements` — A number specifying how many occurrences of `other` to replace. Default is `Int.max`.
