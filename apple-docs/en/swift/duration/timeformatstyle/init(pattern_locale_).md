---
title: 'init(pattern:locale:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/timeformatstyle/init(pattern:locale:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/timeformatstyle/init(pattern:locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/timeformatstyle/init%28pattern%3Alocale%3A%29.json'
content_hash: 'sha256:53c9d642ed1bdf96'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Duration](../../duration.md) · [TimeFormatStyle](../timeformatstyle.md)

# init(pattern:locale:)

<sub>Initializer</sub>

Creates a time format style using the provided pattern and optional locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(pattern: Duration.TimeFormatStyle.Pattern, locale: Locale = .autoupdatingCurrent)
```

## Parameters

- `pattern` — A `Pattern` that specifies the units to include in the displayed string and the behavior of the units.

- `locale` — The `Locale` used to create the string representation of the duration. This parameter defaults to [autoupdatingCurrent](../../../foundation/locale/autoupdatingcurrent.md).

## See Also

### Creating a time format style

- [Pattern](pattern-swift.struct.md) — The units — including hours, minutes, or seconds — and the configuration of those units, used to format a duration.
