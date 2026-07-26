---
title: 'unarchiveObject(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsunarchiver/unarchiveobject(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsunarchiver/unarchiveobject(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsunarchiver/unarchiveobject%28with%3A%29.json'
content_hash: 'sha256:37cedf8f8d590401'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUnarchiver](../nsunarchiver.md)

# unarchiveObject(with:)

<sub>Type Method</sub>

Decodes and returns the object archived in a given `NSData` object.

> [!warning] Deprecated
> Use NSKeyedUnarchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
class func unarchiveObject(with data: Data) -> Any?
```

## Parameters

- `data` — An `NSData` object that contains an archive created using `NSArchiver`.

## Return Value

The object, or object graph, that was archived in `data`. Returns `nil` if `data` cannot be unarchived.

## Discussion

This method invokes [- initForReadingWithData:](<init(forreadingwith_).md>) and [- decodeObject](<../nscoder/decodeobject().md>) to create a temporary `NSUnarchiver` object that decodes the object. If the archived object is the root of a graph of objects, the entire graph is unarchived.

## See Also

### Related Documentation

- [- encodeRootObject:](<../nsarchiver/encoderootobject(__).md>) — Archives a given object along with all the objects to which it is connected. _(deprecated)_

### Decoding objects

- [+ unarchiveObjectWithFile:](<unarchiveobject(withfile_).md>) — Decodes and returns the object archived in the file `path`. _(deprecated)_
