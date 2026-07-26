---
title: clone()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/uniquearray/clone()
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/clone()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/clone%28%29.json'
content_hash: 'sha256:9b1bae5d24992f88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# clone()

<sub>Instance Method</sub>

Copy the contents of this array into a newly allocated unique array instance with just enough capacity to hold all its elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func clone() -> UniqueArray<Element>
```

## Discussion

> [!abstract] Complexity
> O(`count`)
