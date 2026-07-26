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
doc_path: '/documentation/foundation/nsarchiver/replace(_:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarchiver/replace(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarchiver/replace%28_%3Awith%3A%29.json'
content_hash: 'sha256:71cb1c56f3ffa8c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArchiver](../nsarchiver.md)

# replace(_:with:)

<sub>Instance Method</sub>

Causes the receiver to treat subsequent requests to encode a given object as though they were requests to encode another given object.

> [!warning] Deprecated
> Use NSKeyedArchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
func replace(_ object: Any, with newObject: Any)
```

## Parameters

- `object` — An object in the object graph being archived.

- `newObject` — The object with which to replace `object` in the archive.

## Discussion

Both `object` and `newObject` must be valid objects.

## See Also

### Substituting classes or objects

- [- classNameEncodedForTrueClassName:](<classnameencoded(fortrueclassname_).md>) — Returns the name of the class used to archive instances of the class with a given true name. _(deprecated)_
- [- encodeClassName:intoClassName:](<encodeclassname(__intoclassname_).md>) — Encodes a substitute name for the class with a given true name. _(deprecated)_
