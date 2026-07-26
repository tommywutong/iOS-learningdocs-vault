---
title: 'init(format:lenient:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/floatingpointparsestrategy/init(format:lenient:)-1nldg'
source_url: 'https://developer.apple.com/documentation/foundation/floatingpointparsestrategy/init(format:lenient:)-1nldg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/floatingpointparsestrategy/init%28format%3Alenient%3A%29-1nldg.json'
content_hash: 'sha256:9d6f9bd8ff572934'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FloatingPointParseStrategy](../floatingpointparsestrategy.md)

# init(format:lenient:)

<sub>Initializer</sub>

Creates a parse strategy instance using the specified floating-point percentage format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Value>(format: Format, lenient: Bool = true) where Format == FloatingPointFormatStyle<Value>.Percent, Value : BinaryFloatingPoint
```

## Parameters

- `format` — A configured [Percent](../floatingpointformatstyle/percent.md) that describes the percent string format to parse.

- `lenient` — A Boolean value that indicates whether the parse strategy should permit some discrepencies when parsing. Defaults to `true`.

## See Also

### Creating a floating-point parse strategy

- [init(format:lenient:)](<init(format_lenient_)-5nxey.md>) — Creates a parse strategy instance using the specified floating-point format style.
- [init(format:lenient:)](<init(format_lenient_)-9g6wm.md>) — Creates a parse strategy instance using the specified floating-point currency format style.
