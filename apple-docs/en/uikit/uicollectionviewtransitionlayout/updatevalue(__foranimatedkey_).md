---
title: 'updateValue(_:forAnimatedKey:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewtransitionlayout/updatevalue(_:foranimatedkey:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/updatevalue(_:foranimatedkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewtransitionlayout/updatevalue%28_%3Aforanimatedkey%3A%29.json'
content_hash: 'sha256:888ca30e4a537f36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewTransitionLayout](../uicollectionviewtransitionlayout.md)

# updateValue(_:forAnimatedKey:)

<sub>Instance Method</sub>

Sets the value for an animatable key.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateValue(_ value: CGFloat, forAnimatedKey key: String)
```

## Parameters

- `value` — The value you want to store for the specified key.

- `key` — A key that you define for your custom transition layout.

## Discussion

Use this method to store a floating-point value with a specific key that you define for your transition layout object. The name of the key should be one that has meaning to your layout object. For example, if you track the position of the user’s finger over time, you might define the keys “PositionX” and “PositionY” to track those changes. Each time you update the value of a key, the layout object records the change along with a timestamp value. When the layout is finalized or canceled, those values can then be used to determine the speed with which to perform the remaining animations.

For any keys you set using this method, you should get that value as part of the normal process of generating layout attribute information. Getting the value using the [- valueForAnimatedKey:](<value(foranimatedkey_).md>) method (as opposed to getting the value from a class variable) means that when the collection view performs its final animations, your layout methods provide the correct values.

## See Also

### Updating the transition information

- [transitionProgress](transitionprogress.md) — The completion percentage of the transition.
- [- valueForAnimatedKey:](<value(foranimatedkey_).md>) — Returns the most recently set value for the specified key.
