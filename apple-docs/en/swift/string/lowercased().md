---
title: lowercased()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/lowercased()
source_url: 'https://developer.apple.com/documentation/swift/string/lowercased()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/lowercased%28%29.json'
content_hash: 'sha256:fba4752757d60d9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# lowercased()

<sub>Instance Method</sub>

Returns a lowercase version of the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func lowercased() -> String
```

## Return Value

A lowercase copy of the string.

## Discussion

Here’s an example of transforming a string to all lowercase letters.

```swift
let cafe = "BBQ Café 🍵"
print(cafe.lowercased())
// Prints "bbq café 🍵"
```

> [!abstract] Complexity
> O(_n_)

## See Also

### Changing Case

- [uppercased()](<uppercased().md>) — Returns an uppercase version of the string.
