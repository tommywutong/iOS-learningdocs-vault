---
title: 'repetitionBehavior(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regex/repetitionbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swift/regex/repetitionbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/repetitionbehavior%28_%3A%29.json'
content_hash: 'sha256:ecd7db8588be5698'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# repetitionBehavior(_:)

<sub>Instance Method</sub>

Returns a regular expression where quantifiers use the specified behavior by default.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func repetitionBehavior(_ behavior: RegexRepetitionBehavior) -> Regex<Regex<Output>.RegexOutput>
```

## Parameters

- `behavior` — The default behavior to use for quantifiers.

## Discussion

This setting does not affect calls to quantifier methods, such as `OneOrMore`, that include an explicit `behavior` parameter.

Passing `.eager` or `.reluctant` to this method corresponds to applying the `(?-U)` or `(?U)` option in regex syntax, respectively.
