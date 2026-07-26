---
title: 'init(buffer:initializedCount:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/outputspan/init(buffer:initializedcount:)-3tbg3'
source_url: 'https://developer.apple.com/documentation/swift/outputspan/init(buffer:initializedcount:)-3tbg3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputspan/init%28buffer%3Ainitializedcount%3A%29-3tbg3.json'
content_hash: 'sha256:cb5d157fedcb8576'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OutputSpan](../outputspan.md)

# init(buffer:initializedCount:)

<sub>Initializer</sub>

Unsafely create an OutputSpan over partly-initialized memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(buffer: UnsafeMutableBufferPointer<Element>, initializedCount: Int)
```

## Parameters

- `buffer` — An `UnsafeMutableBufferPointer` to be initialized

- `initializedCount` — The number of initialized elements at the beginning of `buffer`.

## Discussion

The memory in `buffer` must remain valid throughout the lifetime of the newly-created `OutputSpan`. Its prefix must contain `initializedCount` initialized instances, followed by uninitialized memory. The default value of `initializedCount` is 0, representing the common case of a completely uninitialized `buffer`.
