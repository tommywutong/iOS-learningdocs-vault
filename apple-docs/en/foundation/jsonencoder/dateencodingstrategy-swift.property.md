---
title: dateEncodingStrategy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonencoder/dateencodingstrategy-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder/dateencodingstrategy-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder/dateencodingstrategy-swift.property.json'
content_hash: 'sha256:c4feadd0a140518d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONEncoder](../jsonencoder.md)

# dateEncodingStrategy

<sub>Instance Property</sub>

The strategy used when encoding dates as part of a JSON object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dateEncodingStrategy: JSONEncoder.DateEncodingStrategy { get set }
```

## Discussion

The default strategy is the [JSONEncoder.DateEncodingStrategy.deferredToDate](dateencodingstrategy-swift.enum/deferredtodate.md) strategy.

## See Also

### Encoding Dates

- [DateEncodingStrategy](dateencodingstrategy-swift.enum.md) — The formatting strategies available for formatting dates when encoding a date as JSON.
