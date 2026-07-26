---
title: NSArchiver
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsarchiver
source_url: 'https://developer.apple.com/documentation/foundation/nsarchiver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarchiver.json'
content_hash: 'sha256:673fad7ca8aad3b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSArchiver

<sub>Class</sub>

A coder that stores an object’s data to an archive.

> [!warning] Deprecated
> Use NSKeyedArchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
class NSArchiver
```

## Overview

[NSArchiver](nsarchiver.md), a concrete subclass of [NSCoder](nscoder.md), provides a way to encode objects into an architecture-independent format that can be stored in a file. When you archive a graph of objects, the class information and instance variables for each object are written to the archive. The companion class [NSUnarchiver](nsunarchiver.md) decodes the data in an archive and creates a graph of objects equivalent to the original set.

[NSArchiver](nsarchiver.md) stores the archive data in a mutable data object ([NSMutableData](nsmutabledata.md)). After encoding the objects, you can have the [NSArchiver](nsarchiver.md) object write this mutable data object immediately to a file, or you can retrieve the mutable data object for some other use.

In macOS 10.2 and later, [NSArchiver](nsarchiver.md) and [NSUnarchiver](nsunarchiver.md) have been replaced by [NSKeyedArchiver](nskeyedarchiver.md) and [NSKeyedUnarchiver](nskeyedunarchiver.md) respectively—see [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i).

## Relationships

- **Inherits From**: [NSCoder](nscoder.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing an NSArchiver

- [- initForWritingWithMutableData:](<nsarchiver/init(forwritingwith_).md>) — Returns an archiver, initialized to encode stream and version information into a given mutable data object. _(deprecated)_

### Archiving data

- [+ archivedDataWithRootObject:](<nsarchiver/archiveddata(withrootobject_).md>) — Returns a data object containing the encoded form of the object graph whose root object is given. _(deprecated)_
- [+ archiveRootObject:toFile:](<nsarchiver/archiverootobject(__tofile_).md>) — Creates a temporary instance of `NSArchiver` and archives an object graph by encoding it into a data object and writing the resulting data object to a specified file. _(deprecated)_
- [- encodeRootObject:](<nsarchiver/encoderootobject(__).md>) — Archives a given object along with all the objects to which it is connected. _(deprecated)_
- [- encodeConditionalObject:](<nsarchiver/encodeconditionalobject(__).md>) — Conditionally archives a given object. _(deprecated)_

### Getting the archived data

- [archiverData](nsarchiver/archiverdata.md) — The receiver’s archive data. _(deprecated)_

### Substituting classes or objects

- [- classNameEncodedForTrueClassName:](<nsarchiver/classnameencoded(fortrueclassname_).md>) — Returns the name of the class used to archive instances of the class with a given true name. _(deprecated)_
- [- encodeClassName:intoClassName:](<nsarchiver/encodeclassname(__intoclassname_).md>) — Encodes a substitute name for the class with a given true name. _(deprecated)_
- [- replaceObject:withObject:](<nsarchiver/replace(__with_).md>) — Causes the receiver to treat subsequent requests to encode a given object as though they were requests to encode another given object. _(deprecated)_

### Constants

- [Archiving Exception Names](archiving-exception-names.md) — Raised by `NSArchiver` if there are problems initializing or encoding.

### Initializers

- [init(forWritingWithMutableData:)](<nsarchiver/init(forwritingwithmutabledata_).md>) _(deprecated)_

## See Also

### Deprecated

- [NSUnarchiver](nsunarchiver.md) — A decoder that restores data from an archive. _(deprecated)_
