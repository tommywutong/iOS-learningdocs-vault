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
doc_path: '/documentation/swift/rangereplaceablecollection/replacing(_:with:maxreplacements:)-1tg5u'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/replacing(_:with:maxreplacements:)-1tg5u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/replacing%28_%3Awith%3Amaxreplacements%3A%29-1tg5u.json'
content_hash: 'sha256:f263e556a7860644'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# replacing(_:with:maxReplacements:)

<sub>Instance Method</sub>

Returns a new collection in which all occurrences of a sequence matching the given regex are replaced by another collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacing<Replacement>(_ regex: some RegexComponent, with replacement: Replacement, maxReplacements: Int = .max) -> Self where Replacement : Collection, Replacement.Element == Character
```

## Parameters

- `regex` — A regex describing the sequence to replace.

- `replacement` — The new elements to add to the collection.

- `maxReplacements` — A number specifying how many occurrences of the sequence matching `regex` to replace. Default is `Int.max`.

## Return Value

A new collection in which all occurrences of subsequence matching `regex` are replaced by `replacement`.
