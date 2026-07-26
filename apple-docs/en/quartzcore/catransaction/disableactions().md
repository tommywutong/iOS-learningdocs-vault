---
title: disableActions()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransaction/disableactions()
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction/disableactions()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction/disableactions%28%29.json'
content_hash: 'sha256:a29ee328473e5474'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransaction](../catransaction.md)

# disableActions()

<sub>Type Method</sub>

Returns whether actions triggered as a result of property changes made within this transaction group are suppressed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func disableActions() -> Bool
```

## Return Value

[true](../../swift/true.md) if actions are disabled.

## Discussion

This is a convenience method that returns the `boolValue` for the [+ valueForKey:](<value(forkey_).md>) value returned by the  [kCATransactionDisableActions](../kcatransactiondisableactions.md) key.

## See Also

### Temporarily Disabling Property Animations

- [+ setDisableActions:](<setdisableactions(__).md>) — Sets whether actions triggered as a result of property changes made within this transaction group are suppressed.
