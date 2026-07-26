---
title: RelativeDateTimeFormatter.DateTimeStyle.named
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/relativedatetimeformatter/datetimestyle-swift.enum/named
source_url: 'https://developer.apple.com/documentation/foundation/relativedatetimeformatter/datetimestyle-swift.enum/named'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/relativedatetimeformatter/datetimestyle-swift.enum/named.json'
content_hash: 'sha256:613b672828862349'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [RelativeDateTimeFormatter](../../relativedatetimeformatter.md) · [DateTimeStyle](../datetimestyle-swift.enum.md)

# RelativeDateTimeFormatter.DateTimeStyle.named

<sub>Case</sub>

A style that uses named styles to describe relative dates, such as “yesterday”, “last week”, or “next week”.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case named
```

## Discussion

The formatter falls back to using [NSRelativeDateTimeFormatterStyleNumeric](numeric.md) if a name isn’t available.

## See Also

### Formatting Dates and Times

- [NSRelativeDateTimeFormatterStyleNumeric](numeric.md) — A style that uses a numeric style to describe relative dates, such as “1 day ago” or “in 3 weeks”.
