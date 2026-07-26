---
title: 'index(before:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/randomaccesscollection/index(before:)'
source_url: 'https://developer.apple.com/documentation/swift/randomaccesscollection/index(before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/randomaccesscollection/index%28before%3A%29.json'
content_hash: 'sha256:fca251411e78db12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RandomAccessCollection](../randomaccesscollection.md)

# index(before:)

<sub>Instance Method</sub>

Returns the position immediately before the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
override func index(before i: Self.Index) -> Self.Index
```

## Parameters

- `i` — A valid index of the collection. `i` must be greater than `startIndex`.

## Return Value

The index value immediately before `i`.

## Default Implementations

### BidirectionalCollection Implementations

- [index(before:)](<../bidirectionalcollection/index(before_)-2jmfj.md>) — Returns the position immediately after the given index.
