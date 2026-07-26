---
title: length
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutabledata/length
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/length'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/length.json'
content_hash: 'sha256:75015fdbb8e9428b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# length

<sub>Instance Property</sub>

The number of bytes contained in the mutable data object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var length: Int { get set }
```

## Discussion

The mutable data object’s length parameter is read-writeable. You can set this parameter to expand or truncate the number of bytes contained by the data object. If the mutable data object is expanded, the additional bytes are filled with zeros.

> [!important] Important
> Changing the length of a mutable data object invalidate any existing data pointers returned by the [bytes](../nsdata/bytes.md) or [mutableBytes](mutablebytes.md) properties.

## See Also

### Related Documentation

- [- increaseLengthBy:](<increaselength(by_).md>) — Increases the length of the receiver by a given number of bytes.
