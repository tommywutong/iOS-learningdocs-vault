---
title: 'classNameDecoded(forArchiveClassName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsunarchiver/classnamedecoded(forarchiveclassname:)-swift.method'
source_url: 'https://developer.apple.com/documentation/foundation/nsunarchiver/classnamedecoded(forarchiveclassname:)-swift.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsunarchiver/classnamedecoded%28forarchiveclassname%3A%29-swift.method.json'
content_hash: 'sha256:b4fd53a0037feea1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUnarchiver](../nsunarchiver.md)

# classNameDecoded(forArchiveClassName:)

<sub>Instance Method</sub>

Returns the name of the class that will be used when instantiating objects whose ostensible class, according to the archived data, is a given name.

> [!warning] Deprecated
> Use NSKeyedUnarchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
func classNameDecoded(forArchiveClassName inArchiveName: String) -> String
```

## Parameters

- `inArchiveName` — The ostensible name of a class in an archive.

## Return Value

The name of the class that will be used when instantiating objects whose ostensible class, according to the archived data, is `nameInArchive`. Returns `nameInArchive` unless a substitute name has been specified using the instance method (not the class method) [- decodeClassName:asClassName:](<decodeclassname(__asclassname_)-swift.method.md>).

## See Also

### Substituting classes or objects

- [+ classNameDecodedForArchiveClassName:](<classnamedecoded(forarchiveclassname_)-swift.type.method.md>) — Returns the name of the class used when instantiating objects whose ostensible class, according to the archived data, is a given name. _(deprecated)_
- [+ decodeClassName:asClassName:](<decodeclassname(__asclassname_)-swift.type.method.md>) — Instructs instances of `NSUnarchiver` to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name. _(deprecated)_
- [- decodeClassName:asClassName:](<decodeclassname(__asclassname_)-swift.method.md>) — Instructs the receiver to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name. _(deprecated)_
- [- replaceObject:withObject:](<replace(__with_).md>) — Causes the receiver to substitute one given object for another whenever the latter is extracted from the archive. _(deprecated)_
