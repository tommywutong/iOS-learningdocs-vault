---
title: timeZone
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/iso8601dateformatter/timezone
source_url: 'https://developer.apple.com/documentation/foundation/iso8601dateformatter/timezone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/iso8601dateformatter/timezone.json'
content_hash: 'sha256:4e2c289b02e29783'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ISO8601DateFormatter](../iso8601dateformatter.md)

# timeZone

<sub>Instance Property</sub>

The time zone used to create and parse date representations. When unspecified, GMT is used.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeZone: TimeZone! { get set }
```

## Discussion

Resetting this property can incur a significant performance cost, as it may cause internal state to be regenerated.

## See Also

### Configuring the Formatter

- [formatOptions](formatoptions.md) — Options for generating and parsing ISO 8601 date representations. See [Options](options.md) for possible values.
