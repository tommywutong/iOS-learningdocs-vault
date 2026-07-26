---
title: 'formIntersection(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/formintersection(_:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/formintersection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/formintersection%28_%3A%29.json'
content_hash: 'sha256:73cfd5f109919fa0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# formIntersection(_:)

<sub>Instance Method</sub>

Removes the contents of this range set that aren’t also in the given range set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func formIntersection(_ other: RangeSet<Bound>)
```

## Parameters

- `other` — A range set to intersect with.
