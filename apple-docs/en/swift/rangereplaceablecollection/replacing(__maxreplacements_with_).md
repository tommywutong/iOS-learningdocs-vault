---
title: 'replacing(_:maxReplacements:with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangereplaceablecollection/replacing(_:maxreplacements:with:)'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/replacing(_:maxreplacements:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/replacing%28_%3Amaxreplacements%3Awith%3A%29.json'
content_hash: 'sha256:d0a9e1b3be1f194b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# replacing(_:maxReplacements:with:)

<sub>Instance Method</sub>

Returns a new collection in which all occurrences of a sequence matching the given regex are replaced by another collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacing<Output, Replacement>(_ regex: some RegexComponent, maxReplacements: Int = .max, with replacement: (Regex<Output>.Match) throws -> Replacement) rethrows -> Self where Replacement : Collection, Replacement.Element == Character
```

## Parameters

- `regex` — A regex describing the sequence to replace.

- `maxReplacements` — A number specifying how many occurrences of the sequence matching `regex` to replace. Default is `Int.max`.

- `replacement` — A closure that receives the full match information, including captures, and returns a replacement collection.

## Return Value

A new collection in which all occurrences of subsequence matching `regex` are replaced by `replacement`.
