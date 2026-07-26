---
title: 'init(forReadingWith:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsunarchiver/init(forreadingwith:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsunarchiver/init(forreadingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsunarchiver/init%28forreadingwith%3A%29.json'
content_hash: 'sha256:e76b76afe7d16310'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUnarchiver](../nsunarchiver.md)

# init(forReadingWith:)

<sub>Initializer</sub>

Returns an `NSUnarchiver` object initialized to read an archive from a given data object.

> [!warning] Deprecated
> Use NSKeyedUnarchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
init?(forReadingWith data: Data)
```

## Parameters

- `data` — The archive data.

## Return Value

An `NSUnarchiver` object initialized to read an archive from `data`. Returns `nil` if `data` is not a valid archive.

## Discussion

The method decodes the system version number that was archived in `data` prepares the `NSUnarchiver` object for a subsequent invocation of [- decodeObject](<../nscoder/decodeobject().md>).

Raises an `NSInvalidArgumentException` if `data` is `nil`.

## See Also

### Related Documentation

- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
- [systemVersion](systemversion-swift.property.md) — The system version number in effect when the archive was created. _(deprecated)_
