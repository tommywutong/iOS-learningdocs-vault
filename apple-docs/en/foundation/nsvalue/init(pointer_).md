---
title: 'init(pointer:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(pointer:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(pointer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28pointer%3A%29.json'
content_hash: 'sha256:f98731567ef846f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(pointer:)

<sub>Initializer</sub>

Creates a value object containing the specified pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(pointer: UnsafeRawPointer?)
```

## Parameters

- `pointer` — The value for the new object.

## Return Value

A new value object that contains `aPointer`.

## Discussion

This method is equivalent to invoking [+ value:withObjCType:](<init(__withobjctype_).md>) in this manner:

```objc
NSValue *theValue = [NSValue value:&aPointer withObjCType:@encode(void *)];
```

This method does not copy the contents of `aPointer`, so you must not to free the memory at the pointer destination while the [NSValue](../nsvalue.md) object exists. [NSData](../nsdata.md) objects may be more suited for arbitrary pointers than [NSValue](../nsvalue.md) objects.

## See Also

### Working with Pointer and Object Values

- [+ valueWithNonretainedObject:](<init(nonretainedobject_).md>) — Creates a value object containing the specified object.
- [pointerValue](pointervalue.md) — Returns the value as an untyped pointer.
- [nonretainedObjectValue](nonretainedobjectvalue.md) — The value as a non-retained pointer to an object.
