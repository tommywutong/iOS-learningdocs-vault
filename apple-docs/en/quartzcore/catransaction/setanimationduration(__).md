---
title: 'setAnimationDuration(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransaction/setanimationduration(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction/setanimationduration(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction/setanimationduration%28_%3A%29.json'
content_hash: 'sha256:1fbcdfa3eefa4733'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransaction](../catransaction.md)

# setAnimationDuration(_:)

<sub>Type Method</sub>

Sets the animation duration used by all animations within this transaction group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func setAnimationDuration(_ dur: CFTimeInterval)
```

## Parameters

- `dur` — An interval of time used as the duration.

## Discussion

You can also set the animation duration for a specific transaction object by calling the [+ setValue:forKey:](<setvalue(__forkey_).md>) method of that object and specifying the [kCATransactionAnimationDuration](../kcatransactionanimationduration.md) key.

## See Also

### Overriding Animation Duration and Timing

- [+ animationDuration](<animationduration().md>) — Returns the animation duration used by all animations within this transaction group.
- [+ animationTimingFunction](<animationtimingfunction().md>) — Returns the timing function used for all animations within this transaction group.
- [+ setAnimationTimingFunction:](<setanimationtimingfunction(__).md>) — Sets the timing function used for all animations within this transaction group.
