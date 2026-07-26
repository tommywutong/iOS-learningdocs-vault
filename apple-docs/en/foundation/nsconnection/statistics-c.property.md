---
title: statistics
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/statistics-c.property
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/statistics-c.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/statistics-c.property.json'
content_hash: 'sha256:3122723a008476de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# statistics

<sub>Instance Property</sub>

A dictionary containing various statistics for the receiver.

<sub>Mac Catalyst, macOS</sub>

```objc
@property (copy, readonly) NSDictionary<NSString *,NSNumber *> * statistics;
```

## Discussion

An `NSDictionary` object containing various statistics for the receiver, such as the number of vended objects, the number of requests and replies, and so on.

The statistics dictionary should be used only for debugging purposes.
