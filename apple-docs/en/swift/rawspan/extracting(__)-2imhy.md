---
title: 'extracting(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rawspan/extracting(_:)-2imhy'
source_url: 'https://developer.apple.com/documentation/swift/rawspan/extracting(_:)-2imhy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawspan/extracting%28_%3A%29-2imhy.json'
content_hash: 'sha256:d8c674edaf7085ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawSpan](../rawspan.md)

# extracting(_:)

<sub>Instance Method</sub>

Constructs a new span over the bytes within the supplied range of positions within this span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func extracting(_ bounds: Range<Int>) -> RawSpan
```

## Parameters

- `bounds` — A valid range of positions. Every position in this range must be within the bounds of this `RawSpan`.

## Return Value

A `RawSpan` over the bytes within `bounds`.

## Discussion

The returned span’s first byte is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

> [!abstract] Complexity
> O(1)
