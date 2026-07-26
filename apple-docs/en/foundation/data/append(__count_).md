---
title: 'append(_:count:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/append(_:count:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/append(_:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/append%28_%3Acount%3A%29.json'
content_hash: 'sha256:b82d7829671ed3a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# append(_:count:)

<sub>Instance Method</sub>

Appends the specified bytes from memory to the end of the data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append(_ bytes: UnsafePointer<UInt8>, count: Int)
```

## See Also

### Adding Bytes

- [append(_:)](<append(__)-vjwy.md>) — Appends the specified data to the end of this data.
- [append(_:)](<append(__)-xtlw.md>) — Append a buffer of bytes to the data.
- [reserveCapacity(_:)](<reservecapacity(__).md>) — Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.
