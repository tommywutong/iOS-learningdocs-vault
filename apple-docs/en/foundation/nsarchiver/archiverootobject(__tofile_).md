---
title: 'archiveRootObject(_:toFile:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsarchiver/archiverootobject(_:tofile:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarchiver/archiverootobject(_:tofile:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarchiver/archiverootobject%28_%3Atofile%3A%29.json'
content_hash: 'sha256:06e5a5c7c66566b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArchiver](../nsarchiver.md)

# archiveRootObject(_:toFile:)

<sub>Type Method</sub>

Creates a temporary instance of `NSArchiver` and archives an object graph by encoding it into a data object and writing the resulting data object to a specified file.

> [!warning] Deprecated
> Use NSKeyedArchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
class func archiveRootObject(_ rootObject: Any, toFile path: String) -> Bool
```

## Parameters

- `rootObject` — The root object of the object graph to archive.

- `path` — The location of the file into which to write the archive.

## Return Value

[true](../../swift/true.md) if the archive was written successfully, otherwise [false](../../swift/false.md).

## Discussion

This convenience method invokes [+ archivedDataWithRootObject:](<archiveddata(withrootobject_).md>) to get the encoded data, and then sends that data object the message [- writeToFile:atomically:](<../nsdata/write(tofile_atomically_).md>), using `path` for the first argument and [true](../../swift/true.md) for the second.

The archived data should be retrieved from the archive by an [NSUnarchiver](../nsunarchiver.md) object.

## See Also

### Related Documentation

- [- writeToFile:atomically:](<../nsdata/write(tofile_atomically_).md>) — Writes the data object’s bytes to the file specified by a given path.

### Archiving data

- [+ archivedDataWithRootObject:](<archiveddata(withrootobject_).md>) — Returns a data object containing the encoded form of the object graph whose root object is given. _(deprecated)_
- [- encodeRootObject:](<encoderootobject(__).md>) — Archives a given object along with all the objects to which it is connected. _(deprecated)_
- [- encodeConditionalObject:](<encodeconditionalobject(__).md>) — Conditionally archives a given object. _(deprecated)_
