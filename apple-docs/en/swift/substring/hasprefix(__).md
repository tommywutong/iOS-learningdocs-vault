---
title: 'hasPrefix(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/hasprefix(_:)'
source_url: 'https://developer.apple.com/documentation/swift/substring/hasprefix(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/hasprefix%28_%3A%29.json'
content_hash: 'sha256:4b30cb2b8ddb36fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# hasPrefix(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the string begins with the specified prefix.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hasPrefix<Prefix>(_ prefix: Prefix) -> Bool where Prefix : StringProtocol
```

## Parameters

- `prefix` — A possible prefix to test against this string.

## Return Value

`true` if the string begins with `prefix`; otherwise, `false`.

## Discussion

The comparison is both case sensitive and Unicode safe. The case-sensitive comparison will only match strings whose corresponding characters have the same case.

```swift
let cafe = "Café du Monde"

// Case sensitive
print(cafe.hasPrefix("café"))
// Prints "false"
```

The Unicode-safe comparison matches Unicode extended grapheme clusters rather than the code points used to compose them. The example below uses two strings with different forms of the `"é"` character—the first uses the composed form and the second uses the decomposed form.

```swift
// Unicode safe
let composedCafe = "Café"
let decomposedCafe = "Cafe\u{0301}"

print(cafe.hasPrefix(composedCafe))
// Prints "true"
print(cafe.hasPrefix(decomposedCafe))
// Prints "true"
```
