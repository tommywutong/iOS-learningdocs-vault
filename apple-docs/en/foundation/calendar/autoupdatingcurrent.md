---
title: autoupdatingCurrent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/autoupdatingcurrent
source_url: 'https://developer.apple.com/documentation/foundation/calendar/autoupdatingcurrent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/autoupdatingcurrent.json'
content_hash: 'sha256:a77938aceb589141'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# autoupdatingCurrent

<sub>Type Property</sub>

A calendar that tracks changes to user’s preferred calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var autoupdatingCurrent: Calendar { get }
```

## Discussion

If mutated, this calendar will no longer track the user’s preferred calendar.

> [!note] Note
> The autoupdating Calendar will only compare equal to another autoupdating Calendar.

## See Also

### Getting the User’s Calendar

- [current](current.md) — The user’s current calendar.
