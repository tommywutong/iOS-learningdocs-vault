---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regex/init(_:)-4ef55'
source_url: 'https://developer.apple.com/documentation/swift/regex/init(_:)-4ef55'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/init%28_%3A%29-4ef55.json'
content_hash: 'sha256:6259543399309154'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# init(_:)

<sub>Initializer</sub>

Creates a regular expression using a RegexBuilder closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(@RegexComponentBuilder _ content: () -> some RegexComponent<Output>)
```
