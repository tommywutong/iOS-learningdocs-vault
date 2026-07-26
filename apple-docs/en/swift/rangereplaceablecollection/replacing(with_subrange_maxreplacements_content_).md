---
title: 'replacing(with:subrange:maxReplacements:content:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangereplaceablecollection/replacing(with:subrange:maxreplacements:content:)'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/replacing(with:subrange:maxreplacements:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/replacing%28with%3Asubrange%3Amaxreplacements%3Acontent%3A%29.json'
content_hash: 'sha256:ec330c980e59751a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# replacing(with:subrange:maxReplacements:content:)

<sub>Instance Method</sub>

Returns a new collection in which all matches for the regex are replaced, using the given closure to create the regex.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacing<Replacement>(with replacement: Replacement, subrange: Range<Self.Index>, maxReplacements: Int = .max, @RegexComponentBuilder content: () -> some RegexComponent) -> Self where Replacement : Collection, Replacement.Element == Character
```

## Parameters

- `replacement` — The new elements to add to the collection in place of each match for the regex, using `content` to create the regex.

- `subrange` — The range in the collection in which to search for the regex.

- `maxReplacements` — A number specifying how many occurrences of the regex to replace.

- `content` — A closure that returns the collection to search for and replace.

## Return Value

A new collection in which all matches for regex in `subrange` are replaced by `replacement`, using `content` to create the regex.
