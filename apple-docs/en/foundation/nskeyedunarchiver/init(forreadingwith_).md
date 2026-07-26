---
title: 'init(forReadingWith:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.14 起废弃）, tvOS 9.0+（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（5.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nskeyedunarchiver/init(forreadingwith:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/init(forreadingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/init%28forreadingwith%3A%29.json'
content_hash: 'sha256:eb058eb5faa0a867'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# init(forReadingWith:)

<sub>Initializer</sub>

Initializes an archiver to decode data from the specified location.

> [!warning] Deprecated
> Use [- initForReadingFromData:error:](<init(forreadingfrom_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(forReadingWith data: Data)
```

## Parameters

- `data` — An archive previously encoded by [NSKeyedArchiver](../nskeyedarchiver.md).

## Return Value

An [NSKeyedUnarchiver](../nskeyedunarchiver.md) object initialized for for decoding `data`.

## Discussion

When you finish decoding data, you should invoke [- finishDecoding](<finishdecoding().md>).

This method throws an exception if `data` is not a valid archive.

## See Also

### Related Documentation

- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)

### Creating a Keyed Unarchiver

- [- initForReadingFromData:error:](<init(forreadingfrom_).md>) — Initializes an archiver to decode data from the specified location.
- [- init](<init().md>) — Initializes an archiver to decode data. _(deprecated)_
