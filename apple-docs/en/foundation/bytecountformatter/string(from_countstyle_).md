---
title: 'string(from:countStyle:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bytecountformatter/string(from:countstyle:)'
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter/string(from:countstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter/string%28from%3Acountstyle%3A%29.json'
content_hash: 'sha256:9cdd26da22757d06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatter](../bytecountformatter.md)

# string(from:countStyle:)

<sub>Type Method</sub>

Formats the value of the given measurement using the given `countStyle`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func string(from measurement: Measurement<UnitInformationStorage>, countStyle: ByteCountFormatter.CountStyle) -> String
```

## Discussion

Throws an exception if the given measurement’s unit does not belong to the `NSUnitInformationStorage` dimension.
