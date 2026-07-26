---
title: 'enumerateObjects(options:using:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phfetchresult/enumerateobjects(options:using:)'
source_url: 'https://developer.apple.com/documentation/photos/phfetchresult/enumerateobjects(options:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresult/enumerateobjects%28options%3Ausing%3A%29.json'
content_hash: 'sha256:2bd09c7cbea5a11e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchResult](../phfetchresult.md)

# enumerateObjects(options:using:)

<sub>Instance Method</sub>

Executes the specified block using each object in the fetch result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func enumerateObjects(options opts: NSEnumerationOptions = [], using block: @escaping (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `opts` — A bit mask that specifies the options for the enumeration (whether it should be performed concurrently and whether it should be performed in reverse order).

- `block` — The block to apply to elements in the fetch result. The block takes three parameters: - **obj** — The element in the fetch result. - **idx** — The index of the element in the fetch result. - **stop** — A pointer to a Boolean value. Set `*stop` to `true` within the block to cancel further processing of the fetch result.

## Discussion

By default, the enumeration starts with the first object and continues in order through the fetch result to the last element specified by the index set. Specify the `concurrent` or `reverse` options to modify this behavior.

This method executes synchronously.

## See Also

### Performing Operations with Objects in a Fetch Result

- [- enumerateObjectsAtIndexes:options:usingBlock:](<enumerateobjects(at_options_using_).md>) — Executes the specified block using the objects in the fetch result at the specified indexes.
- [- enumerateObjectsUsingBlock:](<enumerateobjects(__).md>) — Executes the specified block using each object in the fetch result, starting with the first object and continuing in order to the last object.
