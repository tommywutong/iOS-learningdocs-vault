---
title: 'enumerateBytes(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（5.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/data/enumeratebytes(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/enumeratebytes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/enumeratebytes%28_%3A%29.json'
content_hash: 'sha256:d7f5ba63c7489707'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# enumerateBytes(_:)

<sub>Instance Method</sub>

Enumerates the contents of the data’s buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateBytes(_ block: (UnsafeBufferPointer<UInt8>, Data.Index, inout Bool) -> Void)
```

## Parameters

- `block` — The closure to invoke for each region of data. You may stop the enumeration by setting the `stop` parameter to `true`.

## Discussion

In some cases, (for example, a [Data](../data.md) backed by a `dispatch_data_t`, the bytes may be stored discontiguously. In those cases, this function invokes the closure for each contiguous region of bytes.

## See Also

### Iterating Over Bytes

- [makeIterator()](<makeiterator().md>) — Returns an iterator over the contents of the data.
- [Iterator](iterator.md) — An iterator that operates over the contents of data.
