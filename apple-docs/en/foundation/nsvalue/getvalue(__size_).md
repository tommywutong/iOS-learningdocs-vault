---
title: 'getValue(_:size:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/getvalue(_:size:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/getvalue(_:size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/getvalue%28_%3Asize%3A%29.json'
content_hash: 'sha256:7ae56d4ff762b319'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# getValue(_:size:)

<sub>Instance Method</sub>

Copies the value into the specified buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getValue(_ value: UnsafeMutableRawPointer, size: Int)
```

## Parameters

- `value` — A buffer into which to copy the value. The buffer must be large enough to hold the value.

- `size` — The number of bytes to copy.
