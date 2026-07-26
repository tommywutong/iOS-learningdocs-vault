---
title: init()
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+（12.0 起废弃）, iPadOS 10.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.12+（10.14 起废弃）, tvOS 10.0+（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 3.0+（5.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nskeyedarchiver/init()
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/init%28%29.json'
content_hash: 'sha256:61f9d10b5fb1c1ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# init()

<sub>Initializer</sub>

Initializes an archiver to encode data.

> [!warning] Deprecated
> Use [- initRequiringSecureCoding:](<init(requiringsecurecoding_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## See Also

### Creating a Keyed Archiver

- [- initRequiringSecureCoding:](<init(requiringsecurecoding_).md>) — Creates an archiver to encode data, and optionally disables secure coding.
- [- initForWritingWithMutableData:](<init(forwritingwith_).md>) — Initializes an archiver to encode data into a given a mutable-data object. _(deprecated)_
