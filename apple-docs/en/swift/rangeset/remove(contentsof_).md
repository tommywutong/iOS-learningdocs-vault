---
title: 'remove(contentsOf:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/remove(contentsof:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/remove(contentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/remove%28contentsof%3A%29.json'
content_hash: 'sha256:2395a9979ca2de90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# remove(contentsOf:)

<sub>Instance Method</sub>

Removes the given range from the range set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func remove(contentsOf range: Range<Bound>)
```

## Parameters

- `range` — The range to remove from the set.

## Discussion

> [!abstract] Complexity
> O(_n_), where _n_ is the number of ranges in the range set.
