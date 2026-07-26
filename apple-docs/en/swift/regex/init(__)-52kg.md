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
doc_path: '/documentation/swift/regex/init(_:)-52kg'
source_url: 'https://developer.apple.com/documentation/swift/regex/init(_:)-52kg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/init%28_%3A%29-52kg.json'
content_hash: 'sha256:a7f0050189a2a73f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# init(_:)

<sub>Initializer</sub>

Creates a regular expression from the given string, using a dynamic capture list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ pattern: String) throws
```

## Parameters

- `pattern` — A string with regular expression syntax.

## Discussion

Use this initializer to create a `Regex` instance from a regular expression that you have stored in `pattern`.

```swift
let simpleDigits = try Regex("[0-9]+")
```

This initializer throws an error if `pattern` uses invalid regular expression syntax.

The output type of the new `Regex` is the dynamic [AnyRegexOutput](../anyregexoutput.md). If you know the capture structure of `pattern` ahead of time, use the `init(_:as:)` initializer instead.
