---
title: 'getObjectValue(_:for:errorDescription:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/datecomponentsformatter/getobjectvalue(_:for:errordescription:)'
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/getobjectvalue(_:for:errordescription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/getobjectvalue%28_%3Afor%3Aerrordescription%3A%29.json'
content_hash: 'sha256:d7f7af74220e784b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# getObjectValue(_:for:errorDescription:)

<sub>Instance Method</sub>

`NSDateComponentsFormatter` currently only implements formatting, not parsing. Until it implements parsing, this will always return `NO`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>?, for string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```
