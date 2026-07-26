---
title: dateDecodingStrategy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsondecoder/datedecodingstrategy-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/jsondecoder/datedecodingstrategy-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsondecoder/datedecodingstrategy-swift.property.json'
content_hash: 'sha256:5d16559804521b69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONDecoder](../jsondecoder.md)

# dateDecodingStrategy

<sub>Instance Property</sub>

The strategy used when decoding dates from part of a JSON object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dateDecodingStrategy: JSONDecoder.DateDecodingStrategy { get set }
```

## Discussion

The default strategy is the [JSONDecoder.DateDecodingStrategy.deferredToDate](datedecodingstrategy-swift.enum/deferredtodate.md) strategy.

## See Also

### Decoding Dates

- [DateDecodingStrategy](datedecodingstrategy-swift.enum.md) — The strategies available for formatting dates when decoding them from JSON.
