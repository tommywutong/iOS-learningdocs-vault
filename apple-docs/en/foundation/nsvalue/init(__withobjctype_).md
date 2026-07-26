---
title: 'init(_:withObjCType:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(_:withobjctype:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(_:withobjctype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28_%3Awithobjctype%3A%29.json'
content_hash: 'sha256:04308de3b5d0d491'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(_:withObjCType:)

<sub>Initializer</sub>

Creates a value object containing the specified value, interpreted with the specified Objective-C type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ value: UnsafeRawPointer, withObjCType type: UnsafePointer<CChar>)
```

## Parameters

- `value` — A pointer to data to be stored in the new value object.

- `type` — The Objective-C type of `value`, as provided by the `@encode()` compiler directive. Do not hard-code this parameter as a C string.

## Return Value

A new value object that contains `value`, which is interpreted as being of the Objective-C type `type`.

## Discussion

This method has the same effect as [valueWithBytes:objCType:](valuewithbytes_objctype_.md) and may be deprecated in a future release. You should use [valueWithBytes:objCType:](valuewithbytes_objctype_.md) instead.

## See Also

### Working with Raw Values

- [- initWithBytes:objCType:](<init(bytes_objctype_).md>) — Initializes a value object to contain the specified value, interpreted with the specified Objective-C type.
- [- getValue:](<getvalue(__).md>) — Copies the value into the specified buffer. _(deprecated)_
- [objCType](objctype.md) — A C string containing the Objective-C type of the data contained in the value object.
