---
title: 'replace(maxReplacements:content:with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangereplaceablecollection/replace(maxreplacements:content:with:)'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/replace(maxreplacements:content:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/replace%28maxreplacements%3Acontent%3Awith%3A%29.json'
content_hash: 'sha256:b90ba447351d110a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# replace(maxReplacements:content:with:)

<sub>Instance Method</sub>

Replaces all matches for the regex in this collection, using the given closures to create the replacement and the regex.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replace<Output, Replacement>(maxReplacements: Int = .max, @RegexComponentBuilder content: () -> some RegexComponent, with replacement: (Regex<Output>.Match) throws -> Replacement) rethrows where Replacement : Collection, Replacement.Element == Character
```

## Parameters

- `maxReplacements` — A number specifying how many occurrences of the regex to replace, using `content` to create the regex.

- `content` — A closure that returns the collection to search for and replace.

- `replacement` — A closure that receives the full match information, including captures, and returns a replacement collection.
