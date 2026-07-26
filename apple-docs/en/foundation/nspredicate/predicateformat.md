---
title: predicateFormat
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspredicate/predicateformat
source_url: 'https://developer.apple.com/documentation/foundation/nspredicate/predicateformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspredicate/predicateformat.json'
content_hash: 'sha256:b5425ec2cd0a7a56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPredicate](../nspredicate.md)

# predicateFormat

<sub>Instance Property</sub>

The predicate’s format string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var predicateFormat: String { get }
```

## Discussion

The return value of this property is not guaranteed to be the same as the string used to create the predicate using [predicateWithFormat:](predicatewithformat_.md) or similar methods.

You cannot use this method to create a persistent representation of a predicate suitable for recreating the original predicate. If you need a persistent representation of a predicate, create an archive instead, as described in [Object archiving](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Archiving.html#//apple_ref/doc/uid/TP40008195-CH1) ([NSPredicate](../nspredicate.md) adopts the [NSCoding](../nscoding.md) protocol).
