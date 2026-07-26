---
title: 'padding(toLength:withPad:startingAt:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/padding(tolength:withpad:startingat:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/padding(tolength:withpad:startingat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/padding%28tolength%3Awithpad%3Astartingat%3A%29.json'
content_hash: 'sha256:6c6facbf486154f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# padding(toLength:withPad:startingAt:)

<sub>Instance Method</sub>

Returns a new string formed from the `String` by either removing characters from the end, or by appending as many occurrences as necessary of a given pad string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func padding<T>(toLength newLength: Int, withPad padString: T, startingAt padIndex: Int) -> String where T : StringProtocol
```
