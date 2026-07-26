---
title: 'replace(_:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsunarchiver/replace(_:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsunarchiver/replace(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsunarchiver/replace%28_%3Awith%3A%29.json'
content_hash: 'sha256:45c19d0a53de23a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUnarchiver](../nsunarchiver.md)

# replace(_:with:)

<sub>Instance Method</sub>

Causes the receiver to substitute one given object for another whenever the latter is extracted from the archive.

> [!warning] Deprecated
> Use NSKeyedUnarchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
func replace(_ object: Any, with newObject: Any)
```

## Parameters

- `object` — The archived object to replace.

- `newObject` — The object with which to replace `object`.

## Discussion

`newObject` can be of a different class from object, and the class mappings set by [+ classNameDecodedForArchiveClassName:](<classnamedecoded(forarchiveclassname_)-swift.type.method.md>) and [- decodeClassName:asClassName:](<decodeclassname(__asclassname_)-swift.method.md>) are ignored.

## See Also

### Substituting classes or objects

- [+ classNameDecodedForArchiveClassName:](<classnamedecoded(forarchiveclassname_)-swift.type.method.md>) — Returns the name of the class used when instantiating objects whose ostensible class, according to the archived data, is a given name. _(deprecated)_
- [+ decodeClassName:asClassName:](<decodeclassname(__asclassname_)-swift.type.method.md>) — Instructs instances of `NSUnarchiver` to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name. _(deprecated)_
- [- classNameDecodedForArchiveClassName:](<classnamedecoded(forarchiveclassname_)-swift.method.md>) — Returns the name of the class that will be used when instantiating objects whose ostensible class, according to the archived data, is a given name. _(deprecated)_
- [- decodeClassName:asClassName:](<decodeclassname(__asclassname_)-swift.method.md>) — Instructs the receiver to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name. _(deprecated)_
