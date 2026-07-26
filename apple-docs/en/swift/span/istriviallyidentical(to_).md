---
title: 'isTriviallyIdentical(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/span/istriviallyidentical(to:)'
source_url: 'https://developer.apple.com/documentation/swift/span/istriviallyidentical(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/span/istriviallyidentical%28to%3A%29.json'
content_hash: 'sha256:134a8a8c7f5dde41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Span](../span.md)

# isTriviallyIdentical(to:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether two instances refer to the same memory region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isTriviallyIdentical(to other: Span<Element>) -> Bool
```

## Parameters

- `other` — A span to compare with this one.

## Return Value

Whether `self` and `other` reference the same region in memory.

## Discussion

Two spans are identical if they reference the same starting address and have the same number of elements.

> [!abstract] Complexity
> O(1)
