---
title: 'finalize(for:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/outputrawspan/finalize(for:)-4su35'
source_url: 'https://developer.apple.com/documentation/swift/outputrawspan/finalize(for:)-4su35'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputrawspan/finalize%28for%3A%29-4su35.json'
content_hash: 'sha256:9e46553487665e46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OutputRawSpan](../outputrawspan.md)

# finalize(for:)

<sub>Instance Method</sub>

Consume the output span and return the number of initialized bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
consuming func finalize(for buffer: Slice<UnsafeMutableRawBufferPointer>) -> Int
```

## Parameters

- `buffer` — The buffer we expect the `OutputRawSpan` to reference. This must be the same region of memory passed to the `OutputRawSpan` initializer.

## Return Value

The number of initialized bytes in the same buffer, as tracked by the consumed `OutputRawSpan` instance.

## Discussion

This method should be invoked in the scope where the `OutputRawSpan` was created, when it is time to commit the contents of the updated buffer back into the construct being initialized.

The context that created the output span is expected to remember what memory region the span is addressing. This consuming method expects to receive a copy of the same buffer pointer as a (loose) proof of ownership.
