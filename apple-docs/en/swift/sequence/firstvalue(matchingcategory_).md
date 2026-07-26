---
title: 'firstValue(matchingCategory:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/firstvalue(matchingcategory:)'
source_url: 'https://developer.apple.com/documentation/swift/sequence/firstvalue(matchingcategory:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/firstvalue%28matchingcategory%3A%29.json'
content_hash: 'sha256:af7cf6e0cda51dcc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# firstValue(matchingCategory:)

<sub>Instance Method</sub>

Finds the first tag matching the specified category and returns the value of the matching tag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func firstValue<T>(matchingCategory category: CMTypedTag<T>.Category) -> T? where T : Sendable
```

## Discussion

- category: The category to match.
