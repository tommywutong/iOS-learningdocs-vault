---
title: uppercased()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/uppercased()
source_url: 'https://developer.apple.com/documentation/swift/character/uppercased()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/uppercased%28%29.json'
content_hash: 'sha256:156d47b9fe59be9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# uppercased()

<sub>Instance Method</sub>

Returns an uppercased version of this character.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func uppercased() -> String
```

## Discussion

Because case conversion can result in multiple characters, the result of `uppercased()` is a string.

```swift
let chars: [Character] = ["e", "é", "и", "π", "ß", "1"]
for ch in chars {
    print(ch, "-->", ch.uppercased())
}
// Prints:
// e --> E
// é --> É
// и --> И
// π --> Π
// ß --> SS
// 1 --> 1
```

## See Also

### Checking a Character’s Case

- [isCased](iscased.md) — A Boolean value indicating whether this character changes under any form of case conversion.
- [isUppercase](isuppercase.md) — A Boolean value indicating whether this character is considered uppercase.
- [isLowercase](islowercase.md) — A Boolean value indicating whether this character is considered lowercase.
- [lowercased()](<lowercased().md>) — Returns a lowercased version of this character.
