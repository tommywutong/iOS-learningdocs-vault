---
title: inverted
framework: RegexBuilder
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder/characterclass/inverted
source_url: 'https://developer.apple.com/documentation/regexbuilder/characterclass/inverted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/characterclass/inverted.json'
content_hash: 'sha256:db69d4ae2cbbf19e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [CharacterClass](../characterclass.md)

# inverted

<sub>Instance Property</sub>

A character class that matches any character that does not match this character class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var inverted: CharacterClass { get }
```

## Discussion

For example, you can use the `inverted` property to create a character class that excludes a specific group of characters:

```swift
let validCharacters = CharacterClass("a"..."z", .anyOf("-_"))
let invalidCharacters = validCharacters.inverted

let username = "user123"
if username.contains(invalidCharacters) {
    print("Invalid username: '\(username)'")
}
// Prints "Invalid username: 'user123'"
```
