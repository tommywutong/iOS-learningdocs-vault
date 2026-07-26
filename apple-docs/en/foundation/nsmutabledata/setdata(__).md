---
title: 'setData(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledata/setdata(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/setdata(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/setdata%28_%3A%29.json'
content_hash: 'sha256:fa9bf50c8d663e5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# setData(_:)

<sub>Instance Method</sub>

Replaces the entire contents of the receiver with the contents of another data object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setData(_ data: Data)
```

## Parameters

- `data` — The data object whose content replaces that of the receiver.

## Discussion

As part of its implementation, this method calls [- replaceBytesInRange:withBytes:](<replacebytes(in_withbytes_).md>).

## See Also

### Modifying Bytes

- [- replaceBytesInRange:withBytes:](<replacebytes(in_withbytes_).md>) — Replaces with a given set of bytes a given range within the contents of the receiver.
- [- replaceBytesInRange:withBytes:length:](<replacebytes(in_withbytes_length_).md>) — Replaces with a given set of bytes a given range within the contents of the receiver.
- [- resetBytesInRange:](<resetbytes(in_).md>) — Replaces with zeroes the contents of the receiver in a given range.
