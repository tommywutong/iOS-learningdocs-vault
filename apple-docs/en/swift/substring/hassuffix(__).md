---
title: 'hasSuffix(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/hassuffix(_:)'
source_url: 'https://developer.apple.com/documentation/swift/substring/hassuffix(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/hassuffix%28_%3A%29.json'
content_hash: 'sha256:455d79919f309966'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# hasSuffix(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the string ends with the specified suffix.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hasSuffix<Suffix>(_ suffix: Suffix) -> Bool where Suffix : StringProtocol
```

## Parameters

- `suffix` — A possible suffix to test against this string.

## Return Value

`true` if the string ends with `suffix`; otherwise, `false`.

## Discussion

The comparison is both case sensitive and Unicode safe. The case-sensitive comparison will only match strings whose corresponding characters have the same case.

```swift
let plans = "Let's meet at the café"

// Case sensitive
print(plans.hasSuffix("Café"))
// Prints "false"
```

The Unicode-safe comparison matches Unicode extended grapheme clusters rather than the code points used to compose them. The example below uses two strings with different forms of the `"é"` character—the first uses the composed form and the second uses the decomposed form.

```swift
// Unicode safe
let composedCafe = "café"
let decomposedCafe = "cafe\u{0301}"

print(plans.hasSuffix(composedCafe))
// Prints "true"
print(plans.hasSuffix(decomposedCafe))
// Prints "true"
```
