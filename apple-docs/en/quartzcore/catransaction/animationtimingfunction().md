---
title: animationTimingFunction()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransaction/animationtimingfunction()
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction/animationtimingfunction()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction/animationtimingfunction%28%29.json'
content_hash: 'sha256:5635d396884b7f1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransaction](../catransaction.md)

# animationTimingFunction()

<sub>Type Method</sub>

Returns the timing function used for all animations within this transaction group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func animationTimingFunction() -> CAMediaTimingFunction?
```

## Return Value

An instance of `CAMediaTimingFunction`.

## Discussion

This is a convenience method that returns the [CAMediaTimingFunction](../camediatimingfunction.md) for the [+ valueForKey:](<value(forkey_).md>) value returned by the  [kCATransactionAnimationTimingFunction](../kcatransactionanimationtimingfunction.md) key.

## See Also

### Overriding Animation Duration and Timing

- [+ animationDuration](<animationduration().md>) — Returns the animation duration used by all animations within this transaction group.
- [+ setAnimationDuration:](<setanimationduration(__).md>) — Sets the animation duration used by all animations within this transaction group.
- [+ setAnimationTimingFunction:](<setanimationtimingfunction(__).md>) — Sets the timing function used for all animations within this transaction group.
