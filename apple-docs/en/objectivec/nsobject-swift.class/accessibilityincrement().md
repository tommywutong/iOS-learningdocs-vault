---
title: accessibilityIncrement()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityincrement()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityincrement()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityincrement%28%29.json'
content_hash: 'sha256:ba57c742f5805ddf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityIncrement()

<sub>Instance Method</sub>

Tells the accessibility element to increment the value of its content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityIncrement()
```

## Discussion

If your element has the [adjustable](../../uikit/uiaccessibilitytraits/adjustable.md) trait, you must implement this method. Use this method to increment the value of the element. For example, a [UISlider](../../uikit/uislider.md) object uses this method to increment its value by an appropriate amount.

## See Also

### Performing an action

- [- accessibilityActivate](<accessibilityactivate().md>) — Tells the element to activate itself and report the success or failure of the operation.
- [- accessibilityDecrement](<accessibilitydecrement().md>) — Tells the accessibility element to decrement the value of its content.
- [- accessibilityScroll:](<accessibilityscroll(__).md>) — Scrolls screen content in an application-specific way and returns the success or failure of the action.
- [- accessibilityPerformEscape](<accessibilityperformescape().md>) — Dismisses a modal view and returns the success or failure of the action.
- [- accessibilityPerformMagicTap](<accessibilityperformmagictap().md>) — Performs a salient action.
