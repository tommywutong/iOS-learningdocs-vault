---
title: 'CGPDFObjectGetValue(_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfobjectgetvalue(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfobjectgetvalue(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfobjectgetvalue%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8faefac5fd75c4c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFObjectGetValue(_:_:_:)

<sub>Function</sub>

Returns whether an object is of a given type and if it is, retrieves its value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFObjectGetValue(_ object: CGPDFObjectRef, _ type: CGPDFObjectType, _ value: UnsafeMutableRawPointer?) -> Bool
```

## Parameters

- `object` — A PDF object.

- `type` — A PDF object type.

- `value` — If the `object` parameter is a PDF object of the specified type, then on return contains that object, otherwise the value is unspecified.

## Return Value

Returns [true](../swift/true.md) if the specified object is a PDF object of the specified type, otherwise [false](../swift/false.md).

## Discussion

The function gets the value of the `object` parameter. If the type of `object` is equal to the type specified, then:

- If the `value` parameter is not a null pointer, then the value of `object` is copied to `value`, and the function returns [true](../swift/true.md).
- If the `value` parameter is a null pointer, then the function simply returns [true](../swift/true.md). This allows you to test whether `object` is of the type specified.

If the type of `object` is [kCGPDFObjectTypeInteger](cgpdfobjecttype/integer.md) and `type` is equal to [kCGPDFObjectTypeReal](cgpdfobjecttype/real.md), then the value of `object` is converted to floating point, the result copied to `value`, and the function returns [true](../swift/true.md). If none of the preceding conditions is met, returns [false](../swift/false.md).

## See Also

### Getting Object Types and Values

- [CGPDFObjectGetType](<cgpdfobjectgettype(__).md>) — Returns the PDF type identifier of an object.
