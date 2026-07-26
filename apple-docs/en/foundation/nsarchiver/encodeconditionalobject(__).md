---
title: 'encodeConditionalObject(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsarchiver/encodeconditionalobject(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarchiver/encodeconditionalobject(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarchiver/encodeconditionalobject%28_%3A%29.json'
content_hash: 'sha256:fbd00fb647f9c0bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArchiver](../nsarchiver.md)

# encodeConditionalObject(_:)

<sub>Instance Method</sub>

Conditionally archives a given object.

> [!warning] Deprecated
> Use NSKeyedArchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
func encodeConditionalObject(_ object: Any?)
```

## Parameters

- `object` — The object to archive.

## Discussion

This method overrides the superclass implementation to allow `object` to be encoded only if it is also encoded unconditionally by another object in the object graph. Conditional encoding lets you encode one part of a graph detached from the rest. (See [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i) for more information.)

This method should be invoked only from within an [- encodeWithCoder:](<../nscoding/encode(with_).md>) method. If `object` is `nil`, the `NSArchiver` object encodes it unconditionally as `nil`. This method raises an `NSInvalidArgumentException` if no root object has been encoded.

## See Also

### Archiving data

- [+ archivedDataWithRootObject:](<archiveddata(withrootobject_).md>) — Returns a data object containing the encoded form of the object graph whose root object is given. _(deprecated)_
- [+ archiveRootObject:toFile:](<archiverootobject(__tofile_).md>) — Creates a temporary instance of `NSArchiver` and archives an object graph by encoding it into a data object and writing the resulting data object to a specified file. _(deprecated)_
- [- encodeRootObject:](<encoderootobject(__).md>) — Archives a given object along with all the objects to which it is connected. _(deprecated)_
