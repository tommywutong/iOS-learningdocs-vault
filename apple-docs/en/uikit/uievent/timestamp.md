---
title: timestamp
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uievent/timestamp
source_url: 'https://developer.apple.com/documentation/uikit/uievent/timestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uievent/timestamp.json'
content_hash: 'sha256:24c2d81224170570'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEvent](../uievent.md)

# timestamp

<sub>Instance Property</sub>

The time when the event occurred.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var timestamp: TimeInterval { get }
```

## Discussion

This property contains the number of seconds that have elapsed since system startup. For a description of this time value, see the description of the [systemUptime](../../foundation/processinfo/systemuptime.md) method of the [ProcessInfo](../../foundation/processinfo.md) class.
