---
title: 'replace(with:maxReplacements:content:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangereplaceablecollection/replace(with:maxreplacements:content:)'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/replace(with:maxreplacements:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/replace%28with%3Amaxreplacements%3Acontent%3A%29.json'
content_hash: 'sha256:4321f66463bd7cfd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# replace(with:maxReplacements:content:)

<sub>Instance Method</sub>

Replaces all matches for the regex in this collection, using the given closure to create the regex.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replace<Replacement>(with replacement: Replacement, maxReplacements: Int = .max, @RegexComponentBuilder content: () -> some RegexComponent) where Replacement : Collection, Replacement.Element == Character
```

## Parameters

- `replacement` — The new elements to add to the collection in place of each match for the regex, using `content` to create the regex.

- `maxReplacements` — A number specifying how many occurrences of the regex to replace.

- `content` — A closure that returns the collection to search for and replace.
