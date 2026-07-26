---
title: 'advanced(by:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/advanced(by:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/advanced(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/advanced%28by%3A%29.json'
content_hash: 'sha256:e1f0285654f6b4ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# advanced(by:)

<sub>Instance Method</sub>

Returns a new data buffer created by removing the given number of bytes from the front of the original buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func advanced(by amount: Int) -> Data
```

## Parameters

- `amount` — The number of bytes to strip from the input data buffer. The value must be less than the original data buffer’s length.

## Return Value

A newly created data buffer that is shorter by the given amount than the original.
