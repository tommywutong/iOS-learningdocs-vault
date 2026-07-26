---
title: 'contains(captureNamed:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regex/contains(capturenamed:)'
source_url: 'https://developer.apple.com/documentation/swift/regex/contains(capturenamed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/contains%28capturenamed%3A%29.json'
content_hash: 'sha256:e91525573140f762'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# contains(captureNamed:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether a named capture with the given name exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(captureNamed name: String) -> Bool
```

## Parameters

- `name` — The name to look for among the regular expression’s capture groups. Capture group names are case sensitive.

## Discussion

This example shows a regular expression that includes capture groups named `key` and `value`:

```swift
let regex = try Regex("(?'key'.+?): (?'value'.+)")
regex.contains(captureNamed: "key")       // true
regex.contains(captureNamed: "VALUE")     // false
regex.contains(captureNamed: "1")         // false
```
