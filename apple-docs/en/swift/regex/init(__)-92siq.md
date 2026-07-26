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
doc_path: '/documentation/swift/regex/init(_:)-92siq'
source_url: 'https://developer.apple.com/documentation/swift/regex/init(_:)-92siq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/init%28_%3A%29-92siq.json'
content_hash: 'sha256:1a3bad471d31700a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# init(_:)

<sub>Initializer</sub>

Creates a regular expression with a dynamic capture list from the given regular expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<OtherOutput>(_ regex: Regex<OtherOutput>)
```

## Parameters

- `regex` — A regular expression to convert to use a dynamic capture list.

## Discussion

You can use this initializer to convert a `Regex` with strongly-typed captures into a `Regex` with `AnyRegexOutput` as its output type.
