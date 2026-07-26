---
title: date
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/datestyle/date
source_url: 'https://developer.apple.com/documentation/swiftui/text/datestyle/date'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/datestyle/date.json'
content_hash: 'sha256:a2a5e7deb8b26de4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Text](../../text.md) · [DateStyle](../datestyle.md)

# date

<sub>Type Property</sub>

A style displaying a date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let date: Text.DateStyle
```

## Discussion

```swift
Text(event.startDate, style: .date)
```

Example output: June 3, 2019

## See Also

### Getting text date styles

- [offset](offset.md) — A style displaying a date as offset from now.
- [relative](relative.md) — A style displaying a date as relative to now.
- [time](time.md) — A style displaying only the time component for a date.
- [timer](timer.md) — A style displaying a date as timer counting from now.
