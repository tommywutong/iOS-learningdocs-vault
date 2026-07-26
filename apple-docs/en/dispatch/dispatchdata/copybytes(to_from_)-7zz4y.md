---
title: 'copyBytes(to:from:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchdata/copybytes(to:from:)-7zz4y'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdata/copybytes(to:from:)-7zz4y'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdata/copybytes%28to%3Afrom%3A%29-7zz4y.json'
content_hash: 'sha256:ac30dfda63aa33f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchData](../dispatchdata.md)

# copyBytes(to:from:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copyBytes<DestinationType>(to buffer: UnsafeMutableBufferPointer<DestinationType>, from range: Range<DispatchData.Index>? = nil) -> Int
```

## See Also

### Copying Bytes

- [copyBytes(to:count:)](<copybytes(to_count_)-3j0qx.md>)
- [copyBytes(to:from:)](<copybytes(to_from_)-60yai.md>)
