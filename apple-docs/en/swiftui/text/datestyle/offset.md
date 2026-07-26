---
title: offset
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/datestyle/offset
source_url: 'https://developer.apple.com/documentation/swiftui/text/datestyle/offset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/datestyle/offset.json'
content_hash: 'sha256:5880489a01d6fde8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Text](../../text.md) · [DateStyle](../datestyle.md)

# offset

<sub>Type Property</sub>

A style displaying a date as offset from now.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let offset: Text.DateStyle
```

## Discussion

```swift
Text(event.startDate, style: .offset)
```

Example output: +2 hours -3 months

## See Also

### Getting text date styles

- [date](date.md) — A style displaying a date.
- [relative](relative.md) — A style displaying a date as relative to now.
- [time](time.md) — A style displaying only the time component for a date.
- [timer](timer.md) — A style displaying a date as timer counting from now.
