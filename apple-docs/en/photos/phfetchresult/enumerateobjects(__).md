---
title: 'enumerateObjects(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phfetchresult/enumerateobjects(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phfetchresult/enumerateobjects(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresult/enumerateobjects%28_%3A%29.json'
content_hash: 'sha256:99ec0ddfeb3fc3fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchResult](../phfetchresult.md)

# enumerateObjects(_:)

<sub>Instance Method</sub>

Executes the specified block using each object in the fetch result, starting with the first object and continuing in order to the last object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func enumerateObjects(_ block: @escaping (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `block` — The block to apply to elements in the fetch result. The block takes three parameters: - **obj** — The element in the fetch result. - **idx** — The index of the element in the fetch result. - **stop** — A pointer to a Boolean value. Set `*stop` to `true` within the block to cancel further processing of the fetch result.

## Discussion

This method executes synchronously.

## See Also

### Performing Operations with Objects in a Fetch Result

- [- enumerateObjectsAtIndexes:options:usingBlock:](<enumerateobjects(at_options_using_).md>) — Executes the specified block using the objects in the fetch result at the specified indexes.
- [- enumerateObjectsWithOptions:usingBlock:](<enumerateobjects(options_using_).md>) — Executes the specified block using each object in the fetch result.
