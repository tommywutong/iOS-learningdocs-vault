---
title: 'reference(to:allowedFields:maxFieldCount:thresholdField:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatstyle/reference(to:allowedfields:maxfieldcount:thresholdfield:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/reference(to:allowedfields:maxfieldcount:thresholdfield:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/reference%28to%3Aallowedfields%3Amaxfieldcount%3Athresholdfield%3A%29.json'
content_hash: 'sha256:97190059c813d523'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# reference(to:allowedFields:maxFieldCount:thresholdField:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func reference(to date: Date, allowedFields: Set<Date.RelativeFormatStyle.Field> = [.year, .month, .day, .hour, .minute], maxFieldCount: Int = 2, thresholdField: Date.RelativeFormatStyle.Field = .day) -> SystemFormatStyle.DateReference
```
