---
title: 'unarchiveObject(withFile:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsunarchiver/unarchiveobject(withfile:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsunarchiver/unarchiveobject(withfile:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsunarchiver/unarchiveobject%28withfile%3A%29.json'
content_hash: 'sha256:107f85991b2c305c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUnarchiver](../nsunarchiver.md)

# unarchiveObject(withFile:)

<sub>Type Method</sub>

Decodes and returns the object archived in the file `path`.

> [!warning] Deprecated
> Use NSKeyedUnarchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
class func unarchiveObject(withFile path: String) -> Any?
```

## Parameters

- `path` — The path to a file than contains an archive created using [NSArchiver](../nsarchiver.md).

## Return Value

The object, or object graph, that was archived in the file at `path`. Returns `nil` if the file at `path` cannot be unarchived.

## Discussion

This convenience method reads the file by invoking the `NSData` method [dataWithContentsOfFile:](../nsdata/datawithcontentsoffile_.md) and then invokes [+ unarchiveObjectWithData:](<unarchiveobject(with_).md>).

## See Also

### Decoding objects

- [+ unarchiveObjectWithData:](<unarchiveobject(with_).md>) — Decodes and returns the object archived in a given `NSData` object. _(deprecated)_
