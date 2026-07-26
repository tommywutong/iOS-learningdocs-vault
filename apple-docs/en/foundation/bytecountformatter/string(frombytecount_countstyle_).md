---
title: 'string(fromByteCount:countStyle:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bytecountformatter/string(frombytecount:countstyle:)'
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter/string(frombytecount:countstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter/string%28frombytecount%3Acountstyle%3A%29.json'
content_hash: 'sha256:119dc8bebeeed00a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatter](../bytecountformatter.md)

# string(fromByteCount:countStyle:)

<sub>Type Method</sub>

Converts a byte count into the specified string format without creating an `NSNumber` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func string(fromByteCount byteCount: Int64, countStyle: ByteCountFormatter.CountStyle) -> String
```

## Parameters

- `byteCount` — The byte count.

- `countStyle` — The formatter style. See [CountStyle](countstyle-swift.enum.md) for possible values.

## Return Value

A string containing the formatted `byteCount` value.

## See Also

### Related Documentation

- [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)

### Creating Strings from Byte Count

- [- stringFromByteCount:](<string(frombytecount_).md>) — Converts a byte count into a string without creating an `NSNumber` object.
