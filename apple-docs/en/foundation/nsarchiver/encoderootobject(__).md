---
title: 'encodeRootObject(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsarchiver/encoderootobject(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarchiver/encoderootobject(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarchiver/encoderootobject%28_%3A%29.json'
content_hash: 'sha256:edb98b6cf0b47ca5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArchiver](../nsarchiver.md)

# encodeRootObject(_:)

<sub>Instance Method</sub>

Archives a given object along with all the objects to which it is connected.

> [!warning] Deprecated
> Use NSKeyedArchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
func encodeRootObject(_ rootObject: Any)
```

## Parameters

- `rootObject` — The root object of the object graph to archive.

## Discussion

If any object is encountered more than once while traversing the graph, it is encoded only once, but the multiple references to it are stored. (See [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i) for more information.)

This message must not be sent more than once to a given `NSArchiver` object; an `NSInvalidArgumentException` is raised if a root object has already been encoded. If you need to encode multiple object graphs, therefore, don’t attempt to reuse an `NSArchiver` instance; instead, create a new one for each graph.

## See Also

### Archiving data

- [+ archivedDataWithRootObject:](<archiveddata(withrootobject_).md>) — Returns a data object containing the encoded form of the object graph whose root object is given. _(deprecated)_
- [+ archiveRootObject:toFile:](<archiverootobject(__tofile_).md>) — Creates a temporary instance of `NSArchiver` and archives an object graph by encoding it into a data object and writing the resulting data object to a specified file. _(deprecated)_
- [- encodeConditionalObject:](<encodeconditionalobject(__).md>) — Conditionally archives a given object. _(deprecated)_
