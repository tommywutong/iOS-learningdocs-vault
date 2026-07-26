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
doc_path: '/documentation/foundation/integerparsestrategy/init(format:lenient:)-124xn'
source_url: 'https://developer.apple.com/documentation/foundation/integerparsestrategy/init(format:lenient:)-124xn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerparsestrategy/init%28format%3Alenient%3A%29-124xn.json'
content_hash: 'sha256:a7bb0c33140cdc96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IntegerParseStrategy](../integerparsestrategy.md)

# init(format:lenient:)

<sub>Initializer</sub>

Creates a parse strategy instance using the specified integer format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Value>(format: Format, lenient: Bool = true) where Format == IntegerFormatStyle<Value>, Value : BinaryInteger
```

## Parameters

- `format` — A configured [IntegerFormatStyle](../integerformatstyle.md) that describes the string format to parse.

- `lenient` — A Boolean value that indicates whether the parse strategy should permit some discrepencies when parsing. Defaults to `true`.

## See Also

### Creating an integer parse strategy

- [init(format:lenient:)](<init(format_lenient_)-7tox3.md>) — Creates a parse strategy instance using the specified integer currency format style.
- [init(format:lenient:)](<init(format_lenient_)-3gbvo.md>) — Creates a parse strategy instance using the specified integer percentage format style.
