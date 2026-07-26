---
title: nonretainedObjectValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsvalue/nonretainedobjectvalue
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/nonretainedobjectvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/nonretainedobjectvalue.json'
content_hash: 'sha256:49cc397d23bd43ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# nonretainedObjectValue

<sub>Instance Property</sub>

The value as a non-retained pointer to an object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nonretainedObjectValue: Any? { get }
```

## Discussion

If the value was not created to hold a pointer-sized data item, the result is undefined.

## See Also

### Working with Pointer and Object Values

- [+ valueWithPointer:](<init(pointer_).md>) — Creates a value object containing the specified pointer.
- [+ valueWithNonretainedObject:](<init(nonretainedobject_).md>) — Creates a value object containing the specified object.
- [pointerValue](pointervalue.md) — Returns the value as an untyped pointer.
