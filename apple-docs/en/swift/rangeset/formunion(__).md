---
title: 'formUnion(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/formunion(_:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/formunion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/formunion%28_%3A%29.json'
content_hash: 'sha256:f896946dcb220f4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# formUnion(_:)

<sub>Instance Method</sub>

Adds the contents of the given range set to this range set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func formUnion(_ other: RangeSet<Bound>)
```

## Parameters

- `other` — A range set to merge with this one.

## Discussion

> [!abstract] Complexity
> O(_m_ + _n_), where _m_ and _n_ are the number of ranges in this and the other range set.
