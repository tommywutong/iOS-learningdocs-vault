---
title: NSSystemClockDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nssystemclockdidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nssystemclockdidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nssystemclockdidchange.json'
content_hash: 'sha256:9cc36b13aa9f0da9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSSystemClockDidChange

<sub>Type Property</sub>

A notification posted whenever the system clock is changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSSystemClockDidChange: NSNotification.Name
```

## Discussion

This can be initiated by a call to `settimeofday(_:_:)` or the user changing values in the Date and Time Preference panel.

The notification object is `null`. This notification does not contain a `userInfo` dictionary.
