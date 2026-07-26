---
title: 'decodeCString(_:as:repairingInvalidCodeUnits:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/string/decodecstring(_:as:repairinginvalidcodeunits:)-9pdmv'
source_url: 'https://developer.apple.com/documentation/swift/string/decodecstring(_:as:repairinginvalidcodeunits:)-9pdmv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/decodecstring%28_%3Aas%3Arepairinginvalidcodeunits%3A%29-9pdmv.json'
content_hash: 'sha256:75e847050e86d871'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# decodeCString(_:as:repairingInvalidCodeUnits:)

<sub>Type Method</sub>

> [!warning] Deprecated
> Use a copy of the String argument

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func decodeCString<Encoding>(_ cString: String, as encoding: Encoding.Type, repairingInvalidCodeUnits isRepairing: Bool = true) -> (result: String, repairsMade: Bool)? where Encoding : _UnicodeEncoding
```
