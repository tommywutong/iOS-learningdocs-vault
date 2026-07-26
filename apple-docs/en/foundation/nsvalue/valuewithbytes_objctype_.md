---
title: 'valueWithBytes:objCType:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/valuewithbytes:objctype:'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/valuewithbytes:objctype:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/valuewithbytes%3Aobjctype%3A.json'
content_hash: 'sha256:5ee06d30e832c393'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# valueWithBytes:objCType:

<sub>Type Method</sub>

Creates a value object containing the specified value, interpreted with the specified Objective-C type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSValue *) valueWithBytes:(const void *) value objCType:(const char *) type;
```

## Parameters

- `value` — A pointer to data to be stored in the new value object.

- `type` — The Objective-C type of `value`, as provided by the `@encode()` compiler directive. Do not hard-code this parameter as a C string.

## Return Value

A new value object that contains `value`, which is interpreted as being of the Objective-C type `type`.

## Discussion

See [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i) for other considerations in creating a value object and code examples.

## See Also

### Working with Raw Values

- [- initWithBytes:objCType:](<init(bytes_objctype_).md>) — Initializes a value object to contain the specified value, interpreted with the specified Objective-C type.
- [+ value:withObjCType:](<init(__withobjctype_).md>) — Creates a value object containing the specified value, interpreted with the specified Objective-C type.
- [- getValue:](<getvalue(__).md>) — Copies the value into the specified buffer. _(deprecated)_
- [objCType](objctype.md) — A C string containing the Objective-C type of the data contained in the value object.
