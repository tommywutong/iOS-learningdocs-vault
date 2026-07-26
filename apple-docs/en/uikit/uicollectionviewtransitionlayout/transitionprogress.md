---
title: transitionProgress
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewtransitionlayout/transitionprogress
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/transitionprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewtransitionlayout/transitionprogress.json'
content_hash: 'sha256:b35e1497d0ece69d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewTransitionLayout](../uicollectionviewtransitionlayout.md)

# transitionProgress

<sub>Instance Property</sub>

The completion percentage of the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var transitionProgress: CGFloat { get set }
```

## Discussion

During the transition, you should set the value of this property periodically and call [- invalidateLayout](<../uicollectionviewlayout/invalidatelayout().md>) to force the collection view to update item positions. If you are driving the transition with a gesture recognizer, you would likely set this property from the handler method of your gesture recognizer.

## See Also

### Updating the transition information

- [- updateValue:forAnimatedKey:](<updatevalue(__foranimatedkey_).md>) — Sets the value for an animatable key.
- [- valueForAnimatedKey:](<value(foranimatedkey_).md>) — Returns the most recently set value for the specified key.
