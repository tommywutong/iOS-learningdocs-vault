---
title: includingFractionalSeconds
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/iso8601formatstyle/includingfractionalseconds
source_url: 'https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/includingfractionalseconds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/iso8601formatstyle/includingfractionalseconds.json'
content_hash: 'sha256:c5ba5250b897d740'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ISO8601FormatStyle](../iso8601formatstyle.md)

# includingFractionalSeconds

<sub>Instance Property</sub>

If set, the style includes fractional seconds when formatting. Before Swift 6.2, if true when parsing, fractional seconds must be present. If false when parsing, fractional seconds must not be present. After Swift 6.2, fractional seconds may be present in the String regardless of the setting of this property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var includingFractionalSeconds: Bool { get }
```
