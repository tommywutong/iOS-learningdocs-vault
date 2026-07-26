---
title: 'matchingSemantics(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regex/matchingsemantics(_:)'
source_url: 'https://developer.apple.com/documentation/swift/regex/matchingsemantics(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/matchingsemantics%28_%3A%29.json'
content_hash: 'sha256:ebb8ff3aeeafd9e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# matchingSemantics(_:)

<sub>Instance Method</sub>

Returns a regular expression that matches with the specified semantic level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func matchingSemantics(_ semanticLevel: RegexSemanticLevel) -> Regex<Regex<Output>.RegexOutput>
```

## Parameters

- `semanticLevel` — The semantics to use during matching.

## Return Value

The modified regular expression.

## Discussion

When matching with grapheme cluster semantics (the default), metacharacters like `.` and `\w`, custom character classes, and character class instances like `.any` match a grapheme cluster when possible, corresponding with the default string representation. In addition, matching with grapheme cluster semantics compares characters using their canonical representation, corresponding with how strings comparison works.

When matching with Unicode scalar semantics, metacharacters and character classes always match a single Unicode scalar value, even if that scalar comprises part of a grapheme cluster.

These semantic levels can lead to different results, especially when working with strings that have decomposed characters. In the following example, `queRegex` matches any 3-character string that begins with `"q"`.

```swift
let composed = "qué"
let decomposed = "que\u{301}"

let queRegex = /^q..$/

print(composed.contains(queRegex))
// Prints "true"
print(decomposed.contains(queRegex))
// Prints "true"
```

When using Unicode scalar semantics, however, the regular expression only matches the composed version of the string, because each `.` matches a single Unicode scalar value.

```swift
let queRegexScalar = queRegex.matchingSemantics(.unicodeScalar)
print(composed.contains(queRegexScalar))
// Prints "true"
print(decomposed.contains(queRegexScalar))
// Prints "false"
```
