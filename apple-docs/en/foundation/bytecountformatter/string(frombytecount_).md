---
title: 'string(fromByteCount:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bytecountformatter/string(frombytecount:)'
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter/string(frombytecount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter/string%28frombytecount%3A%29.json'
content_hash: 'sha256:21f5bb9906f7e99e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatter](../bytecountformatter.md)

# string(fromByteCount:)

<sub>Instance Method</sub>

Converts a byte count into a string without creating an `NSNumber` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(fromByteCount byteCount: Int64) -> String
```

## Parameters

- `byteCount` — The byte count.

## Return Value

A string containing the formatted `byteCount` value.

## See Also

### Creating Strings from Byte Count

- [+ stringFromByteCount:countStyle:](<string(frombytecount_countstyle_).md>) — Converts a byte count into the specified string format without creating an `NSNumber` object.
