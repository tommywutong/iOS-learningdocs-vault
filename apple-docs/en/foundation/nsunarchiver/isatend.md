---
title: isAtEnd
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsunarchiver/isatend
source_url: 'https://developer.apple.com/documentation/foundation/nsunarchiver/isatend'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsunarchiver/isatend.json'
content_hash: 'sha256:b868691df9643ed7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUnarchiver](../nsunarchiver.md)

# isAtEnd

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver has reached the end of the encoded data while decoding.

> [!warning] Deprecated
> Use NSKeyedUnarchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
var isAtEnd: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the receiver has reached the end of the encoded data while decoding, otherwise [false](../../swift/false.md).

You can invoke this method after invoking `decodeObject` to discover whether the archive contains extra data following the encoded object graph. If it does, you can either ignore this anomaly or consider it an error.

## See Also

### Managing an NSUnarchiver

- [systemVersion](systemversion-swift.property.md) — The system version number in effect when the archive was created. _(deprecated)_
