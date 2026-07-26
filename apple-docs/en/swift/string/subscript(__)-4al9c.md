---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/subscript(_:)-4al9c'
source_url: 'https://developer.apple.com/documentation/swift/string/subscript(_:)-4al9c'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/subscript%28_%3A%29-4al9c.json'
content_hash: 'sha256:bb672ca4519a1b74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# subscript(_:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(x: UnboundedRange) -> Self.SubSequence { get }
```

## See Also

### Getting Substrings

- [subscript(_:)](<subscript(__)-2so14.md>) — Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](<subscript(__)-4h7s3.md>) — Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [prefix(_:)](<prefix(__).md>) — Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [prefix(through:)](<prefix(through_).md>) — Returns a subsequence from the start of the collection through the specified position.
- [prefix(upTo:)](<prefix(upto_).md>) — Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [prefix(while:)](<prefix(while_).md>) — Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [suffix(_:)](<suffix(__).md>) — Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [suffix(from:)](<suffix(from_).md>) — Returns a subsequence from the specified position to the end of the collection.
