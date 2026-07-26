---
title: systemVersion
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsunarchiver/systemversion-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/nsunarchiver/systemversion-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsunarchiver/systemversion-swift.property.json'
content_hash: 'sha256:3d9fd65c784fc140'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUnarchiver](../nsunarchiver.md)

# systemVersion

<sub>Instance Property</sub>

The system version number in effect when the archive was created.

> [!warning] Deprecated
> Use NSKeyedUnarchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
var systemVersion: UInt32 { get }
```

## Discussion

This information is available as soon as the receiver has been initialized.

## See Also

### Managing an NSUnarchiver

- [atEnd](isatend.md) — A Boolean value that indicates whether the receiver has reached the end of the encoded data while decoding. _(deprecated)_
