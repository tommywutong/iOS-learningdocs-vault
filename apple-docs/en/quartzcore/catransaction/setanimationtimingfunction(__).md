---
title: 'setAnimationTimingFunction(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransaction/setanimationtimingfunction(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction/setanimationtimingfunction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction/setanimationtimingfunction%28_%3A%29.json'
content_hash: 'sha256:b128cc2bd322a078'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransaction](../catransaction.md)

# setAnimationTimingFunction(_:)

<sub>Type Method</sub>

Sets the timing function used for all animations within this transaction group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func setAnimationTimingFunction(_ function: CAMediaTimingFunction?)
```

## Parameters

- `function` — An instance of `CAMediaTimingFunction`.

## Discussion

This is a convenience method that sets the [CAMediaTimingFunction](../camediatimingfunction.md) for the [+ valueForKey:](<value(forkey_).md>) value of  the  [kCATransactionAnimationTimingFunction](../kcatransactionanimationtimingfunction.md) key.

## See Also

### Overriding Animation Duration and Timing

- [+ animationDuration](<animationduration().md>) — Returns the animation duration used by all animations within this transaction group.
- [+ setAnimationDuration:](<setanimationduration(__).md>) — Sets the animation duration used by all animations within this transaction group.
- [+ animationTimingFunction](<animationtimingfunction().md>) — Returns the timing function used for all animations within this transaction group.
