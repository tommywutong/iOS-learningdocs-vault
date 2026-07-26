---
title: archiverData
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsarchiver/archiverdata
source_url: 'https://developer.apple.com/documentation/foundation/nsarchiver/archiverdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarchiver/archiverdata.json'
content_hash: 'sha256:145557d3d8f3de61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArchiver](../nsarchiver.md)

# archiverData

<sub>Instance Property</sub>

The receiver’s archive data.

> [!warning] Deprecated
> Use NSKeyedArchiver instead

<sub>Mac Catalyst, macOS</sub>

```swift
var archiverData: NSMutableData { get }
```

## Discussion

The returned data object is the same one specified as the argument to [- initForWritingWithMutableData:](<init(forwritingwith_).md>). It contains whatever data has been encoded thus far by invocations of the various encoding methods. It is safest not to invoke this method until after [- encodeRootObject:](<encoderootobject(__).md>) has returned. In other words, although it is possible for a class to invoke this method from within its [- encodeWithCoder:](<../nscoding/encode(with_).md>) method, that method must not alter the data.
