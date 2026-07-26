---
title: 'init(forWritingWith:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsarchiver/init(forwritingwith:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarchiver/init(forwritingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarchiver/init%28forwritingwith%3A%29.json'
content_hash: 'sha256:2758b46b7c21e541'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArchiver](../nsarchiver.md)

# init(forWritingWith:)

<sub>Initializer</sub>

Returns an archiver, initialized to encode stream and version information into a given mutable data object.

> [!warning] Deprecated
> Use NSKeyedArchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
init(forWritingWith mdata: NSMutableData)
```

## Parameters

- `mdata` — The mutable data object into which to write the archive. This value must not be `nil`.

## Return Value

An archiver object, initialized to encode stream and version information into `data`.

## Discussion

Raises an `NSInvalidArgumentException` if `data` is `nil`.

## See Also

### Related Documentation

- [archiverData](archiverdata.md) — The receiver’s archive data. _(deprecated)_
- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
