---
title: 'classNameEncoded(forTrueClassName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsarchiver/classnameencoded(fortrueclassname:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarchiver/classnameencoded(fortrueclassname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarchiver/classnameencoded%28fortrueclassname%3A%29.json'
content_hash: 'sha256:096d360136a4939a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArchiver](../nsarchiver.md)

# classNameEncoded(forTrueClassName:)

<sub>Instance Method</sub>

Returns the name of the class used to archive instances of the class with a given true name.

> [!warning] Deprecated
> Use NSKeyedArchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
func classNameEncoded(forTrueClassName trueName: String) -> String?
```

## Parameters

- `trueName` — The real name of an encoded class.

## Return Value

The name of the class used to archive instances of the class `trueName`.

## See Also

### Substituting classes or objects

- [- encodeClassName:intoClassName:](<encodeclassname(__intoclassname_).md>) — Encodes a substitute name for the class with a given true name. _(deprecated)_
- [- replaceObject:withObject:](<replace(__with_).md>) — Causes the receiver to treat subsequent requests to encode a given object as though they were requests to encode another given object. _(deprecated)_
