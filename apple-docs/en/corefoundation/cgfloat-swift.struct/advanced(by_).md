---
title: 'advanced(by:)'
framework: Core Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cgfloat-swift.struct/advanced(by:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cgfloat-swift.struct/advanced(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cgfloat-swift.struct/advanced%28by%3A%29.json'
content_hash: 'sha256:6ab7b4980553026c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CGFloat](../cgfloat-swift.struct.md)

# advanced(by:)

<sub>Instance Method</sub>

Returns a `Self` `x` such that `self.distance(to: x)` approximates `n`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func advanced(by amount: CGFloat) -> CGFloat
```

## Discussion

Complexity: O(1).
