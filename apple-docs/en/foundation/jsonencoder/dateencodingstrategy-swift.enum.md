---
title: JSONEncoder.DateEncodingStrategy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonencoder/dateencodingstrategy-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder/dateencodingstrategy-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder/dateencodingstrategy-swift.enum.json'
content_hash: 'sha256:6d97c9f5eef8caa0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONEncoder](../jsonencoder.md)

# JSONEncoder.DateEncodingStrategy

<sub>Enumeration</sub>

The formatting strategies available for formatting dates when encoding a date as JSON.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DateEncodingStrategy
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Default Formats

- [JSONEncoder.DateEncodingStrategy.deferredToDate](dateencodingstrategy-swift.enum/deferredtodate.md) — The strategy that uses formatting from the Date structure.

### Standard Formats

- [JSONEncoder.DateEncodingStrategy.iso8601](dateencodingstrategy-swift.enum/iso8601.md) — The strategy that formats dates according to the ISO 8601 and RFC 3339 standards.

### Custom Formats

- [JSONEncoder.DateEncodingStrategy.formatted(_:)](<dateencodingstrategy-swift.enum/formatted(__).md>) — The strategy that defers formatting settings to a supplied date formatter.
- [JSONEncoder.DateEncodingStrategy.custom(_:)](<dateencodingstrategy-swift.enum/custom(__).md>) — The strategy that formats custom dates by calling a user-defined function.

### Epoch Formats

- [JSONEncoder.DateEncodingStrategy.millisecondsSince1970](dateencodingstrategy-swift.enum/millisecondssince1970.md) — The strategy that encodes dates in terms of milliseconds since midnight UTC on January 1, 1970.
- [JSONEncoder.DateEncodingStrategy.secondsSince1970](dateencodingstrategy-swift.enum/secondssince1970.md) — The strategy that encodes dates in terms of seconds since midnight UTC on January 1, 1970.

## See Also

### Encoding Dates

- [dateEncodingStrategy](dateencodingstrategy-swift.property.md) — The strategy used when encoding dates as part of a JSON object.
