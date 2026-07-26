---
title: lowercased()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/lowercased()
source_url: 'https://developer.apple.com/documentation/swift/character/lowercased()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/lowercased%28%29.json'
content_hash: 'sha256:2e2d329f6e39b74f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# lowercased()

<sub>Instance Method</sub>

Returns a lowercased version of this character.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func lowercased() -> String
```

## Discussion

Because case conversion can result in multiple characters, the result of `lowercased()` is a string.

```swift
let chars: [Character] = ["E", "É", "И", "Π", "1"]
for ch in chars {
    print(ch, "-->", ch.lowercased())
}
// Prints:
// E --> e
// É --> é
// И --> и
// Π --> π
// 1 --> 1
```

## See Also

### Checking a Character’s Case

- [isCased](iscased.md) — A Boolean value indicating whether this character changes under any form of case conversion.
- [isUppercase](isuppercase.md) — A Boolean value indicating whether this character is considered uppercase.
- [uppercased()](<uppercased().md>) — Returns an uppercased version of this character.
- [isLowercase](islowercase.md) — A Boolean value indicating whether this character is considered lowercase.
