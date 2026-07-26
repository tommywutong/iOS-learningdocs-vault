---
title: 'getValue(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsvalue/getvalue(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/getvalue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/getvalue%28_%3A%29.json'
content_hash: 'sha256:d7df18f86f8a484a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# getValue(_:)

<sub>Instance Method</sub>

Copies the value into the specified buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getValue(_ value: UnsafeMutableRawPointer)
```

## Parameters

- `value` — A buffer into which to copy the value. The buffer must be large enough to hold the value.

## See Also

### Working with Raw Values

- [- initWithBytes:objCType:](<init(bytes_objctype_).md>) — Initializes a value object to contain the specified value, interpreted with the specified Objective-C type.
- [+ value:withObjCType:](<init(__withobjctype_).md>) — Creates a value object containing the specified value, interpreted with the specified Objective-C type.
- [objCType](objctype.md) — A C string containing the Objective-C type of the data contained in the value object.
