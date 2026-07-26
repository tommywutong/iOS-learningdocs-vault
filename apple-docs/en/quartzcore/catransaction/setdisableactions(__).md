---
title: 'setDisableActions(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransaction/setdisableactions(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction/setdisableactions(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction/setdisableactions%28_%3A%29.json'
content_hash: 'sha256:034be8fd0d7b37f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransaction](../catransaction.md)

# setDisableActions(_:)

<sub>Type Method</sub>

Sets whether actions triggered as a result of property changes made within this transaction group are suppressed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func setDisableActions(_ flag: Bool)
```

## Parameters

- `flag` — [true](../../swift/true.md), if actions should be disabled.

## Discussion

This is a convenience method that invokes [+ setValue:forKey:](<setvalue(__forkey_).md>) with an `NSNumber` containing a [true](../../swift/true.md) for the  [kCATransactionDisableActions](../kcatransactiondisableactions.md) key.

## See Also

### Temporarily Disabling Property Animations

- [+ disableActions](<disableactions().md>) — Returns whether actions triggered as a result of property changes made within this transaction group are suppressed.
