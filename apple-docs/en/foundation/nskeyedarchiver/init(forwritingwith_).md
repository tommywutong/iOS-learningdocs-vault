---
title: 'init(forWritingWith:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.14 起废弃）, tvOS 9.0+（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（5.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nskeyedarchiver/init(forwritingwith:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/init(forwritingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/init%28forwritingwith%3A%29.json'
content_hash: 'sha256:4d78c3001b0bb14f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# init(forWritingWith:)

<sub>Initializer</sub>

Initializes an archiver to encode data into a given a mutable-data object.

> [!warning] Deprecated
> Use [- initRequiringSecureCoding:](<init(requiringsecurecoding_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(forWritingWith data: NSMutableData)
```

## Parameters

- `data` — The mutable-data object into which the archive is written.

## Discussion

When you finish encoding data, you must invoke [- finishEncoding](<finishencoding().md>) at which point `data` is filled. The format of the receiver is `NSPropertyListBinaryFormat_v1_0`.

## See Also

### Related Documentation

- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)

### Creating a Keyed Archiver

- [- initRequiringSecureCoding:](<init(requiringsecurecoding_).md>) — Creates an archiver to encode data, and optionally disables secure coding.
- [- init](<init().md>) — Initializes an archiver to encode data. _(deprecated)_
