---
title: 'replacing(subrange:maxReplacements:content:with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangereplaceablecollection/replacing(subrange:maxreplacements:content:with:)'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/replacing(subrange:maxreplacements:content:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/replacing%28subrange%3Amaxreplacements%3Acontent%3Awith%3A%29.json'
content_hash: 'sha256:e7a24de4c9637798'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# replacing(subrange:maxReplacements:content:with:)

<sub>Instance Method</sub>

Returns a new collection in which all matches for the regex are replaced, using the given closures to create the replacement and the regex.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacing<Output, Replacement>(subrange: Range<Self.Index>, maxReplacements: Int = .max, @RegexComponentBuilder content: () -> some RegexComponent, with replacement: (Regex<Output>.Match) throws -> Replacement) rethrows -> Self where Replacement : Collection, Replacement.Element == Character
```

## Parameters

- `subrange` — The range in the collection in which to search for the regex, using `content` to create the regex.

- `maxReplacements` — A number specifying how many occurrences of the regex to replace.

- `content` — A closure that returns the collection to search for and replace.

- `replacement` — A closure that receives the full match information, including captures, and returns a replacement collection.

## Return Value

A new collection in which all matches for regex in `subrange` are replaced by the result of calling `replacement`, where regex is the result of calling `content`.
