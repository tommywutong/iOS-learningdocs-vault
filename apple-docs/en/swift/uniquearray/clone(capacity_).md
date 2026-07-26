---
title: 'clone(capacity:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/clone(capacity:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/clone(capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/clone%28capacity%3A%29.json'
content_hash: 'sha256:3ab8a0212ad084ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# clone(capacity:)

<sub>Instance Method</sub>

Copy the contents of this array into a newly allocated unique array instance with the specified capacity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func clone(capacity: Int) -> UniqueArray<Element>
```

## Parameters

- `capacity` — The desired capacity of the resulting unique array. `capacity` must be greater than or equal to `count`.

## Discussion

> [!abstract] Complexity
> O(`count`)
