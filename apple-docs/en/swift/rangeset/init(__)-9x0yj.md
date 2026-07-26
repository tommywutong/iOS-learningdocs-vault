---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/init(_:)-9x0yj'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/init(_:)-9x0yj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/init%28_%3A%29-9x0yj.json'
content_hash: 'sha256:97936e7639ac7a94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# init(_:)

<sub>Initializer</sub>

Creates a range set containing the values in the given ranges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ ranges: some Sequence<Range<Bound>>)
```

## Parameters

- `ranges` — The ranges to use for the new range set.

## Discussion

Any empty ranges in `ranges` are ignored, and non-empty ranges are merged to eliminate any overlaps. As such, the `ranges` collection in the resulting range set may not be equivalent to the sequence of ranges passed to this initializer.
