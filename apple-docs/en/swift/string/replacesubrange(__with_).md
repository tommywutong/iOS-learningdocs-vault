---
title: 'replaceSubrange(_:with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/replacesubrange(_:with:)'
source_url: 'https://developer.apple.com/documentation/swift/string/replacesubrange(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/replacesubrange%28_%3Awith%3A%29.json'
content_hash: 'sha256:694d2c957431c6f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# replaceSubrange(_:with:)

<sub>Instance Method</sub>

Replaces the text within the specified bounds with the given characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replaceSubrange<C>(_ subrange: Range<String.Index>, with newElements: C) where C : Collection, C.Element == Character
```

## Parameters

- `subrange` — The range of text to replace. The bounds of the range must be valid indices of the string.

- `newElements` — The new characters to add to the string.

## Discussion

Calling this method invalidates any existing indices for use with this string.

> [!abstract] Complexity
> O(_m_), where _m_ is the combined length of the string and `newElements`. If the call to `replaceSubrange(_:with:)` simply removes text at the end of the string, the complexity is O(_n_), where _n_ is equal to `bounds.count`.

## See Also

### Replacing Substrings

- [replaceSubrange(_:with:)](<replacesubrange(__with_)-72947.md>) — Replaces the specified subrange of elements with the given collection.
