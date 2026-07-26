---
title: 'format(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/attributedstyle/bytecount/format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/attributedstyle/bytecount/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/attributedstyle/bytecount/format%28_%3A%29.json'
content_hash: 'sha256:7218d4262df09f8e'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Measurement](../../../measurement.md) · [AttributedStyle](../../attributedstyle.md) · [ByteCount](../bytecount.md)

# format(_:)

<sub>Instance Method</sub>

Formats a byte count measurment, using this style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: Measurement<UnitInformationStorage>) -> AttributedString
```

## Parameters

- `value` — The byte count measurement to format.

## Return Value

A formatted representation of `value`, formatted according to the style’s configuration.

## Discussion

Use this method when you want to create a single style instance, and then use it to format multiple values.
