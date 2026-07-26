---
title: 'distance(to:)'
framework: Core Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cgfloat-swift.struct/distance(to:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cgfloat-swift.struct/distance(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cgfloat-swift.struct/distance%28to%3A%29.json'
content_hash: 'sha256:f550b9a552c4b4bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CGFloat](../cgfloat-swift.struct.md)

# distance(to:)

<sub>Instance Method</sub>

Returns a stride `x` such that `self.advanced(by: x)` approximates `other`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(to other: CGFloat) -> CGFloat
```

## Discussion

Complexity: O(1).
