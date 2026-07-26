---
title: 'decodeClassName(_:asClassName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsunarchiver/decodeclassname(_:asclassname:)-swift.method'
source_url: 'https://developer.apple.com/documentation/foundation/nsunarchiver/decodeclassname(_:asclassname:)-swift.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsunarchiver/decodeclassname%28_%3Aasclassname%3A%29-swift.method.json'
content_hash: 'sha256:cb213f834a7ed355'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUnarchiver](../nsunarchiver.md)

# decodeClassName(_:asClassName:)

<sub>Instance Method</sub>

Instructs the receiver to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.

> [!warning] Deprecated
> Use NSKeyedUnarchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
func decodeClassName(_ inArchiveName: String, asClassName trueName: String)
```

## Parameters

- `inArchiveName` — The ostensible name of a class in an archive.

- `trueName` — The name of the class to use when instantiating objects whose ostensible class, according to the archived data, is `nameInArchive`.

## Discussion

This method enables easy conversion of unarchived data when the name of a class has changed since the archive was created.

Note that there’s also a class method of the same name. The class method has precedence in case of conflicts.

## See Also

### Substituting classes or objects

- [+ classNameDecodedForArchiveClassName:](<classnamedecoded(forarchiveclassname_)-swift.type.method.md>) — Returns the name of the class used when instantiating objects whose ostensible class, according to the archived data, is a given name. _(deprecated)_
- [+ decodeClassName:asClassName:](<decodeclassname(__asclassname_)-swift.type.method.md>) — Instructs instances of `NSUnarchiver` to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name. _(deprecated)_
- [- classNameDecodedForArchiveClassName:](<classnamedecoded(forarchiveclassname_)-swift.method.md>) — Returns the name of the class that will be used when instantiating objects whose ostensible class, according to the archived data, is a given name. _(deprecated)_
- [- replaceObject:withObject:](<replace(__with_).md>) — Causes the receiver to substitute one given object for another whenever the latter is extracted from the archive. _(deprecated)_
