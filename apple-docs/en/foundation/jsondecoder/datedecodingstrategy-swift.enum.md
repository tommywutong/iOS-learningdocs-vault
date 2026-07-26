---
title: JSONDecoder.DateDecodingStrategy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsondecoder/datedecodingstrategy-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/jsondecoder/datedecodingstrategy-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsondecoder/datedecodingstrategy-swift.enum.json'
content_hash: 'sha256:a804754ee3c273c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONDecoder](../jsondecoder.md)

# JSONDecoder.DateDecodingStrategy

<sub>Enumeration</sub>

The strategies available for formatting dates when decoding them from JSON.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DateDecodingStrategy
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Default Formats

- [JSONDecoder.DateDecodingStrategy.deferredToDate](datedecodingstrategy-swift.enum/deferredtodate.md) — The strategy that uses formatting from the Date structure.

### Standard Formats

- [JSONDecoder.DateDecodingStrategy.iso8601](datedecodingstrategy-swift.enum/iso8601.md) — The strategy that formats dates according to the ISO 8601 standard.

### Custom Formats

- [JSONDecoder.DateDecodingStrategy.formatted(_:)](<datedecodingstrategy-swift.enum/formatted(__).md>) — The strategy that defers formatting settings to a supplied date formatter.
- [JSONDecoder.DateDecodingStrategy.custom(_:)](<datedecodingstrategy-swift.enum/custom(__).md>) — The strategy that formats custom dates by calling a user-defined function.

### Epoch Formats

- [JSONDecoder.DateDecodingStrategy.millisecondsSince1970](datedecodingstrategy-swift.enum/millisecondssince1970.md) — The strategy that decodes dates in terms of milliseconds since midnight UTC on January 1st, 1970.
- [JSONDecoder.DateDecodingStrategy.secondsSince1970](datedecodingstrategy-swift.enum/secondssince1970.md) — The strategy that decodes dates in terms of seconds since midnight UTC on January 1st, 1970.

## See Also

### Decoding Dates

- [dateDecodingStrategy](datedecodingstrategy-swift.property.md) — The strategy used when decoding dates from part of a JSON object.
