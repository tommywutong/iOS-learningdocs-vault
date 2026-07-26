---
title: current
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/current
source_url: 'https://developer.apple.com/documentation/foundation/calendar/current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/current.json'
content_hash: 'sha256:efe40dce3fcde606'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# current

<sub>Type Property</sub>

The user’s current calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var current: Calendar { get }
```

## Discussion

This calendar does not track changes that the user makes to their preferences.

## See Also

### Getting the User’s Calendar

- [autoupdatingCurrent](autoupdatingcurrent.md) — A calendar that tracks changes to user’s preferred calendar.
