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
doc_path: '/documentation/swift/rangereplaceablecollection/replace(_:with:maxreplacements:)-20ctz'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/replace(_:with:maxreplacements:)-20ctz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/replace%28_%3Awith%3Amaxreplacements%3A%29-20ctz.json'
content_hash: 'sha256:4767c0e948d6dd45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# replace(_:with:maxReplacements:)

<sub>Instance Method</sub>

Replaces all occurrences of the sequence matching the given regex with a given collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replace<Replacement>(_ regex: some RegexComponent, with replacement: Replacement, maxReplacements: Int = .max) where Replacement : Collection, Replacement.Element == Character
```

## Parameters

- `regex` — A regex describing the sequence to replace.

- `replacement` — The new elements to add to the collection.

- `maxReplacements` — A number specifying how many occurrences of the sequence matching `regex` to replace. Default is `Int.max`.
