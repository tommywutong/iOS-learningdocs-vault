---
title: 'formSymmetricDifference(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/formsymmetricdifference(_:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/formsymmetricdifference(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/formsymmetricdifference%28_%3A%29.json'
content_hash: 'sha256:a6124c0f3e663e35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# formSymmetricDifference(_:)

<sub>Instance Method</sub>

Removes the contents of this range set that are also in the given set and adds the contents of the given set that are not already in this range set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func formSymmetricDifference(_ other: RangeSet<Bound>)
```

## Parameters

- `other` — A range set to perform a symmetric difference against.
