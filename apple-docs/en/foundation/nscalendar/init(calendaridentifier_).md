---
title: 'init(calendarIdentifier:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/init(calendaridentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/init(calendaridentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/init%28calendaridentifier%3A%29.json'
content_hash: 'sha256:509736bae1c0d58c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# init(calendarIdentifier:)

<sub>Initializer</sub>

Initializes a calendar according to a given identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(calendarIdentifier ident: NSCalendar.Identifier)
```

## Parameters

- `ident` — The identifier for the new calendar. For valid identifiers, see `Calendar Identifiers`.

## Return Value

The initialized calendar, or `nil` if the identifier is unknown (if, for example, it is either an unrecognized string or the calendar is not supported by the current version of the operating system).

## See Also

### Related Documentation

- [calendarIdentifier](calendaridentifier.md) — An identifier for the calendar.
- [autoupdatingCurrentCalendar](autoupdatingcurrent.md) — A calendar that tracks changes to user’s preferred calendar.

### Creating and Initializing Calendars

- [+ calendarWithIdentifier:](<init(identifier_).md>) — Creates a new calendar specified by a given identifier.
- [Identifier](identifier.md) — The supported calendar types.
