---
title: 'encodeClassName(_:intoClassName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsarchiver/encodeclassname(_:intoclassname:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarchiver/encodeclassname(_:intoclassname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarchiver/encodeclassname%28_%3Aintoclassname%3A%29.json'
content_hash: 'sha256:c1ef8e24585b00d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArchiver](../nsarchiver.md)

# encodeClassName(_:intoClassName:)

<sub>Instance Method</sub>

Encodes a substitute name for the class with a given true name.

> [!warning] Deprecated
> Use NSKeyedArchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
func encodeClassName(_ trueName: String, intoClassName inArchiveName: String)
```

## Parameters

- `trueName` — The real name of a class in the object graph being archived.

- `inArchiveName` — The name of the class to use in the archive in place of `trueName`.

## Discussion

Any subsequently encountered objects of class `trueName` are archived as instances of class `inArchiveName`. It is safest not to invoke this method during the archiving process (that is, within an [- encodeWithCoder:](<../nscoding/encode(with_).md>) method). Instead, invoke it before [- encodeRootObject:](<encoderootobject(__).md>).

## See Also

### Substituting classes or objects

- [- classNameEncodedForTrueClassName:](<classnameencoded(fortrueclassname_).md>) — Returns the name of the class used to archive instances of the class with a given true name. _(deprecated)_
- [- replaceObject:withObject:](<replace(__with_).md>) — Causes the receiver to treat subsequent requests to encode a given object as though they were requests to encode another given object. _(deprecated)_
