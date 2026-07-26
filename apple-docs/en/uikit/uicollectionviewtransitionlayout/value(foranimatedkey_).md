---
title: 'value(forAnimatedKey:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewtransitionlayout/value(foranimatedkey:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/value(foranimatedkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewtransitionlayout/value%28foranimatedkey%3A%29.json'
content_hash: 'sha256:c0522a28e72b1fb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewTransitionLayout](../uicollectionviewtransitionlayout.md)

# value(forAnimatedKey:)

<sub>Instance Method</sub>

Returns the most recently set value for the specified key.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func value(forAnimatedKey key: String) -> CGFloat
```

## Parameters

- `key` — A key whose value you set using the [- updateValue:forAnimatedKey:](<updatevalue(__foranimatedkey_).md>) method.

## Return Value

The last value set for the key.

## Discussion

Use this method to retrieve floating-point values that are useful when laying out the contents of your collection view. The key you specify is a string that you define and that has some meaning to your implementation. At points during an interactive transition, you can assign new values to that key using the [- updateValue:forAnimatedKey:](<updatevalue(__foranimatedkey_).md>) method.

## See Also

### Updating the transition information

- [transitionProgress](transitionprogress.md) — The completion percentage of the transition.
- [- updateValue:forAnimatedKey:](<updatevalue(__foranimatedkey_).md>) — Sets the value for an animatable key.
