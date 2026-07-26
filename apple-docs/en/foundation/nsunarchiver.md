---
title: NSUnarchiver
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsunarchiver
source_url: 'https://developer.apple.com/documentation/foundation/nsunarchiver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsunarchiver.json'
content_hash: 'sha256:5001d333b26f759a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUnarchiver

<sub>Class</sub>

A decoder that restores data from an archive.

> [!warning] Deprecated
> Use NSKeyedUnarchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
class NSUnarchiver
```

## Overview

[NSUnarchiver](nsunarchiver.md), a concrete subclass of [NSCoder](nscoder.md), defines methods for decoding a set of Objective-C objects from an archive. Such archives are produced by objects of the [NSArchiver](nsarchiver.md) class.

In macOS 10.2 and later, [NSArchiver](nsarchiver.md) and [NSUnarchiver](nsunarchiver.md) have been replaced by [NSKeyedArchiver](nskeyedarchiver.md) and [NSKeyedUnarchiver](nskeyedunarchiver.md) respectively—see [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i).

## Relationships

- **Inherits From**: [NSCoder](nscoder.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing an NSUnarchiver

- [- initForReadingWithData:](<nsunarchiver/init(forreadingwith_).md>) — Returns an `NSUnarchiver` object initialized to read an archive from a given data object. _(deprecated)_

### Decoding objects

- [+ unarchiveObjectWithData:](<nsunarchiver/unarchiveobject(with_).md>) — Decodes and returns the object archived in a given `NSData` object. _(deprecated)_
- [+ unarchiveObjectWithFile:](<nsunarchiver/unarchiveobject(withfile_).md>) — Decodes and returns the object archived in the file `path`. _(deprecated)_

### Managing an NSUnarchiver

- [atEnd](nsunarchiver/isatend.md) — A Boolean value that indicates whether the receiver has reached the end of the encoded data while decoding. _(deprecated)_
- [systemVersion](nsunarchiver/systemversion-swift.property.md) — The system version number in effect when the archive was created. _(deprecated)_

### Substituting classes or objects

- [+ classNameDecodedForArchiveClassName:](<nsunarchiver/classnamedecoded(forarchiveclassname_)-swift.type.method.md>) — Returns the name of the class used when instantiating objects whose ostensible class, according to the archived data, is a given name. _(deprecated)_
- [+ decodeClassName:asClassName:](<nsunarchiver/decodeclassname(__asclassname_)-swift.type.method.md>) — Instructs instances of `NSUnarchiver` to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name. _(deprecated)_
- [- classNameDecodedForArchiveClassName:](<nsunarchiver/classnamedecoded(forarchiveclassname_)-swift.method.md>) — Returns the name of the class that will be used when instantiating objects whose ostensible class, according to the archived data, is a given name. _(deprecated)_
- [- decodeClassName:asClassName:](<nsunarchiver/decodeclassname(__asclassname_)-swift.method.md>) — Instructs the receiver to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name. _(deprecated)_
- [- replaceObject:withObject:](<nsunarchiver/replace(__with_).md>) — Causes the receiver to substitute one given object for another whenever the latter is extracted from the archive. _(deprecated)_

### Initializers

- [init(forReadingWithData:)](<nsunarchiver/init(forreadingwithdata_).md>) _(deprecated)_

## See Also

### Deprecated

- [NSArchiver](nsarchiver.md) — A coder that stores an object’s data to an archive. _(deprecated)_
