---
title: uppercased()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/uppercased()
source_url: 'https://developer.apple.com/documentation/swift/string/uppercased()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/uppercased%28%29.json'
content_hash: 'sha256:7f961c367266e809'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# uppercased()

<sub>Instance Method</sub>

Returns an uppercase version of the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func uppercased() -> String
```

## Return Value

An uppercase copy of the string.

## Discussion

The following example transforms a string to uppercase letters:

```swift
let cafe = "Café 🍵"
print(cafe.uppercased())
// Prints "CAFÉ 🍵"
```

> [!abstract] Complexity
> O(_n_)

## See Also

### Changing Case

- [lowercased()](<lowercased().md>) — Returns a lowercase version of the string.
