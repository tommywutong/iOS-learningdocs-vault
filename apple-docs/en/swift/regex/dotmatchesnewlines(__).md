---
title: 'dotMatchesNewlines(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regex/dotmatchesnewlines(_:)'
source_url: 'https://developer.apple.com/documentation/swift/regex/dotmatchesnewlines(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/dotmatchesnewlines%28_%3A%29.json'
content_hash: 'sha256:f057ea9fe14ac258'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# dotMatchesNewlines(_:)

<sub>Instance Method</sub>

Returns a regular expression where the “any” metacharacter (`.`) also matches against the start and end of a line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dotMatchesNewlines(_ dotMatchesNewlines: Bool = true) -> Regex<Regex<Output>.RegexOutput>
```

## Parameters

- `dotMatchesNewlines` — A Boolean value indicating whether `.` should match a newline character.

## Return Value

The modified regular expression.
