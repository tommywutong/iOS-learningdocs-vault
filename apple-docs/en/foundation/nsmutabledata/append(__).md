---
title: 'append(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledata/append(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/append(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/append%28_%3A%29.json'
content_hash: 'sha256:e1db7103e9cb41e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# append(_:)

<sub>Instance Method</sub>

Appends the content of another data object to the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func append(_ other: Data)
```

## Parameters

- `other` — The data object whose content is to be appended to the contents of the receiver.

## See Also

### Adding Bytes

- [- appendBytes:length:](<append(__length_).md>) — Appends to the receiver a given number of bytes from a given buffer.
- [- increaseLengthBy:](<increaselength(by_).md>) — Increases the length of the receiver by a given number of bytes.
