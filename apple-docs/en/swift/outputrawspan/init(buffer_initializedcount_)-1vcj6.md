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
doc_path: '/documentation/swift/outputrawspan/init(buffer:initializedcount:)-1vcj6'
source_url: 'https://developer.apple.com/documentation/swift/outputrawspan/init(buffer:initializedcount:)-1vcj6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputrawspan/init%28buffer%3Ainitializedcount%3A%29-1vcj6.json'
content_hash: 'sha256:2610e2fb8651c0cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OutputRawSpan](../outputrawspan.md)

# init(buffer:initializedCount:)

<sub>Initializer</sub>

Unsafely create an OutputRawSpan over partly-initialized memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(buffer: UnsafeMutableRawBufferPointer, initializedCount: Int)
```

## Parameters

- `buffer` — An `UnsafeMutableRawBufferPointer` to be initialized

- `initializedCount` — The number of initialized bytes at the beginning of `buffer`.

## Discussion

The memory in `buffer` must remain valid throughout the lifetime of the newly-created `OutputRawSpan`. Its prefix must contain `initializedCount` initialized bytes, followed by uninitialized memory.
