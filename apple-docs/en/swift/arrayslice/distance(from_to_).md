---
title: 'distance(from:to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/arrayslice/distance(from:to:)'
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/distance(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/distance%28from%3Ato%3A%29.json'
content_hash: 'sha256:0f676d6518e10ea9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

# distance(from:to:)

<sub>Instance Method</sub>

Returns the distance between two indices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(from start: Int, to end: Int) -> Int
```

## Parameters

- `start` — A valid index of the collection.

- `end` — Another valid index of the collection. If `end` is equal to `start`, the result is zero.

## Return Value

The distance between `start` and `end`.
