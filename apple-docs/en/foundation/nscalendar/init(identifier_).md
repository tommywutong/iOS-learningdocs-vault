---
title: 'init(identifier:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/init(identifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/init(identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/init%28identifier%3A%29.json'
content_hash: 'sha256:274485d168a1e7e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# init(identifier:)

<sub>Initializer</sub>

Creates a new calendar specified by a given identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(identifier calendarIdentifierConstant: NSCalendar.Identifier)
```

## Parameters

- `calendarIdentifierConstant` — The identifier for the new calendar. For valid identifiers, see `Calendar Identifiers`.

## Return Value

The initialized calendar, or `nil` if the identifier is unknown (if, for example, it is either an unrecognized string or the calendar is not supported by the current version of the operating system).

## Discussion

The returned calendar defaults to the current locale and default time zone.

## See Also

### Related Documentation

- [calendarIdentifier](calendaridentifier.md) — An identifier for the calendar.
- [autoupdatingCurrentCalendar](autoupdatingcurrent.md) — A calendar that tracks changes to user’s preferred calendar.

### Creating and Initializing Calendars

- [- initWithCalendarIdentifier:](<init(calendaridentifier_).md>) — Initializes a calendar according to a given identifier.
- [Identifier](identifier.md) — The supported calendar types.
