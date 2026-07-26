---
title: time
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/datestyle/time
source_url: 'https://developer.apple.com/documentation/swiftui/text/datestyle/time'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/datestyle/time.json'
content_hash: 'sha256:5c99f32d0804873f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Text](../../text.md) · [DateStyle](../datestyle.md)

# time

<sub>Type Property</sub>

A style displaying only the time component for a date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let time: Text.DateStyle
```

## Discussion

```swift
Text(event.startDate, style: .time)
```

Example output: 11:23PM

## See Also

### Getting text date styles

- [date](date.md) — A style displaying a date.
- [offset](offset.md) — A style displaying a date as offset from now.
- [relative](relative.md) — A style displaying a date as relative to now.
- [timer](timer.md) — A style displaying a date as timer counting from now.
