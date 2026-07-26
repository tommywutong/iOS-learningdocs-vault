---
title: now
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdate/now
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/now'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/now.json'
content_hash: 'sha256:adc23eba9266067e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# now

<sub>Type Property</sub>

The current date and time, as of the time of access.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var now: Date { get }
```

## Discussion

This is equivalent to initializing a new instance with `NSDate()` (or `[[NSDate alloc] init]` in Objective-C). The [NSDate](../nsdate.md) instance doesn’t automatically update its time after you retrieve it.
