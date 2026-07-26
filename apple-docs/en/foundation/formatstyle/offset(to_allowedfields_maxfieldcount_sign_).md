---
title: 'offset(to:allowedFields:maxFieldCount:sign:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatstyle/offset(to:allowedfields:maxfieldcount:sign:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/offset(to:allowedfields:maxfieldcount:sign:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/offset%28to%3Aallowedfields%3Amaxfieldcount%3Asign%3A%29.json'
content_hash: 'sha256:fe40b9ee4b497753'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# offset(to:allowedFields:maxFieldCount:sign:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func offset(to anchor: Date, allowedFields: Set<Date.ComponentsFormatStyle.Field> = [.year, .month, .day, .hour, .minute, .second], maxFieldCount: Int = 2, sign: NumberFormatStyleConfiguration.SignDisplayStrategy = .automatic) -> SystemFormatStyle.DateOffset
```
