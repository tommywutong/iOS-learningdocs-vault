---
title: distantPast
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdate/distantpast
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/distantpast'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/distantpast.json'
content_hash: 'sha256:6e32825f719020e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# distantPast

<sub>Type Property</sub>

A date object representing a date in the distant past.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var distantPast: Date { get }
```

## Return Value

An [NSDate](../nsdate.md) object representing a date in the distant past (in terms of centuries).

## Discussion

You can use this object as a control date, a guaranteed temporal boundary.

## See Also

### Getting Temporal Boundaries

- [distantFuture](distantfuture.md) — A date object representing a date in the distant future.
