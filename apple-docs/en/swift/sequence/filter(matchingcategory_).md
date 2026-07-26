---
title: 'filter(matchingCategory:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/filter(matchingcategory:)'
source_url: 'https://developer.apple.com/documentation/swift/sequence/filter(matchingcategory:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/filter%28matchingcategory%3A%29.json'
content_hash: 'sha256:66a6fffaf9eb3cb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# filter(matchingCategory:)

<sub>Instance Method</sub>

Filters a sequence of tags based on matching the specified category.  Returns the tags that match the specified category.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filter<T>(matchingCategory category: CMTypedTag<T>.Category) -> [CMTypedTag<T>] where T : Sendable
```

## Discussion

- category: The category to match.
