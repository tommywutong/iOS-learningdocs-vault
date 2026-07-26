---
title: 'init(verbatim:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regex/init(verbatim:)'
source_url: 'https://developer.apple.com/documentation/swift/regex/init(verbatim:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/init%28verbatim%3A%29.json'
content_hash: 'sha256:e9a44663bbc34225'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# init(verbatim:)

<sub>Initializer</sub>

Creates a regular expression that matches the given string exactly, as though every metacharacter in it was escaped.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(verbatim verbatimString: String)
```

## Parameters

- `verbatimString` — A string to convert into a regular expression exactly, escaping any metacharacters.

## Discussion

This example creates a regular expression that matches the string `"(adj)"`, including the parentheses. Although parentheses are regular expression metacharacters, they do not need escaping in the string passed as `verbatimString`.

```swift
let adjectiveDesignator = Regex<Substring>(verbatim: "(adj.)")

print("awesome (adj.)".contains(adjectiveDesignator))
// Prints "true"
print("apple (n.)".contains(adjectiveDesignator))
// Prints "false"
```
