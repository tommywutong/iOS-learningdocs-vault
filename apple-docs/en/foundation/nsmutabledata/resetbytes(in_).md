---
title: 'resetBytes(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledata/resetbytes(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/resetbytes(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/resetbytes%28in%3A%29.json'
content_hash: 'sha256:d240db29aa37091a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# resetBytes(in:)

<sub>Instance Method</sub>

Replaces with zeroes the contents of the receiver in a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resetBytes(in range: NSRange)
```

## Parameters

- `range` — The range within the contents of the receiver to be replaced by zeros. The range must not exceed the bounds of the receiver.

## Discussion

If the location of `range` isn’t within the receiver’s range of bytes, an `NSRangeException` is raised. The receiver is resized to accommodate the new bytes, if necessary.

## See Also

### Modifying Bytes

- [- replaceBytesInRange:withBytes:](<replacebytes(in_withbytes_).md>) — Replaces with a given set of bytes a given range within the contents of the receiver.
- [- replaceBytesInRange:withBytes:length:](<replacebytes(in_withbytes_length_).md>) — Replaces with a given set of bytes a given range within the contents of the receiver.
- [- setData:](<setdata(__).md>) — Replaces the entire contents of the receiver with the contents of another data object.
