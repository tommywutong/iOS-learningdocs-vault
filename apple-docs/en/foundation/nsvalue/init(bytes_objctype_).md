---
title: 'init(bytes:objCType:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(bytes:objctype:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(bytes:objctype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28bytes%3Aobjctype%3A%29.json'
content_hash: 'sha256:c7a1550f526a5ad9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(bytes:objCType:)

<sub>Initializer</sub>

Initializes a value object to contain the specified value, interpreted with the specified Objective-C type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bytes value: UnsafeRawPointer, objCType type: UnsafePointer<CChar>)
```

## Parameters

- `value` — A pointer to data to be stored in the new value object.

- `type` — The Objective-C type of `value`, as provided by the `@encode()` compiler directive. Do not hard-code this parameter as a C string.

## Return Value

An initialized value object that contains `value`, which is interpreted as being of the Objective-C type `type`. The returned object might be different than the original receiver.

## Discussion

See [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i) for other considerations in creating a value object.

This is the designated initializer for the [NSValue](../nsvalue.md) class.

## See Also

### Related Documentation

- [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i)

### Working with Raw Values

- [+ value:withObjCType:](<init(__withobjctype_).md>) — Creates a value object containing the specified value, interpreted with the specified Objective-C type.
- [- getValue:](<getvalue(__).md>) — Copies the value into the specified buffer. _(deprecated)_
- [objCType](objctype.md) — A C string containing the Objective-C type of the data contained in the value object.
