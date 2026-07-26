---
title: 'archivedData(withRootObject:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsarchiver/archiveddata(withrootobject:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarchiver/archiveddata(withrootobject:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarchiver/archiveddata%28withrootobject%3A%29.json'
content_hash: 'sha256:eaabc0ae280cf8d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArchiver](../nsarchiver.md)

# archivedData(withRootObject:)

<sub>Type Method</sub>

Returns a data object containing the encoded form of the object graph whose root object is given.

> [!warning] Deprecated
> Use NSKeyedArchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
class func archivedData(withRootObject rootObject: Any) -> Data
```

## Parameters

- `rootObject` — The root object of the object graph to archive.

## Return Value

A data object containing the encoded form of the object graph whose root object is `rootObject`.

## Discussion

This method invokes [- initForWritingWithMutableData:](<init(forwritingwith_).md>) and [- encodeRootObject:](<encoderootobject(__).md>) to create a temporary archiver that encodes the object graph.

## See Also

### Related Documentation

- [- initForWritingWithMutableData:](<init(forwritingwith_).md>) — Returns an archiver, initialized to encode stream and version information into a given mutable data object. _(deprecated)_

### Archiving data

- [+ archiveRootObject:toFile:](<archiverootobject(__tofile_).md>) — Creates a temporary instance of `NSArchiver` and archives an object graph by encoding it into a data object and writing the resulting data object to a specified file. _(deprecated)_
- [- encodeRootObject:](<encoderootobject(__).md>) — Archives a given object along with all the objects to which it is connected. _(deprecated)_
- [- encodeConditionalObject:](<encodeconditionalobject(__).md>) — Conditionally archives a given object. _(deprecated)_
