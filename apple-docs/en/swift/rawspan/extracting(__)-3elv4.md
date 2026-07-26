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
doc_path: '/documentation/swift/rawspan/extracting(_:)-3elv4'
source_url: 'https://developer.apple.com/documentation/swift/rawspan/extracting(_:)-3elv4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawspan/extracting%28_%3A%29-3elv4.json'
content_hash: 'sha256:4e97d5b65f275bc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawSpan](../rawspan.md)

# extracting(_:)

<sub>Instance Method</sub>

Constructs a new span over all the bytes of this span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func extracting(_: UnboundedRange) -> RawSpan
```

## Return Value

A `RawSpan` over all the bytes of this span.

## Discussion

The returned span’s first byte is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

> [!abstract] Complexity
> O(1)
