---
title: 'init(nonretainedObject:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(nonretainedobject:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(nonretainedobject:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28nonretainedobject%3A%29.json'
content_hash: 'sha256:d8c7e501ad2d993c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(nonretainedObject:)

<sub>Initializer</sub>

Creates a value object containing the specified object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(nonretainedObject anObject: Any?)
```

## Parameters

- `anObject` — The value for the new object.

## Return Value

A new value object that contains `anObject`.

## Discussion

This method is equivalent to invoking [+ value:withObjCType:](<init(__withobjctype_).md>) in this manner:

```objc
NSValue *theValue = [NSValue value:&anObject withObjCType:@encode(void *)];
```

This method is useful if you want to add an object to a [Collection](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10) but don’t want the collection to create a strong reference to it.

## See Also

### Working with Pointer and Object Values

- [+ valueWithPointer:](<init(pointer_).md>) — Creates a value object containing the specified pointer.
- [pointerValue](pointervalue.md) — Returns the value as an untyped pointer.
- [nonretainedObjectValue](nonretainedobjectvalue.md) — The value as a non-retained pointer to an object.
