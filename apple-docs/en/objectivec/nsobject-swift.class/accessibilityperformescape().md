---
title: accessibilityPerformEscape()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityperformescape()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityperformescape()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityperformescape%28%29.json'
content_hash: 'sha256:cb4ad554c4479838'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityPerformEscape()

<sub>Instance Method</sub>

Dismisses a modal view and returns the success or failure of the action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityPerformEscape() -> Bool
```

## Return Value

[YES](../yes.md) if the modal view is successfully dismissed; otherwise, [NO](../no.md). By default, this method returns [NO](../no.md).

## Discussion

Implement this method on an element or containing view that can be revealed modally or in a hierarchy. When a VoiceOver user performs a dismiss action, this method dismisses the view. For example, you might implement this method for a popover in order to give users a deliberate dismiss action to perform that closes the popover.

## See Also

### Performing an action

- [- accessibilityActivate](<accessibilityactivate().md>) — Tells the element to activate itself and report the success or failure of the operation.
- [- accessibilityIncrement](<accessibilityincrement().md>) — Tells the accessibility element to increment the value of its content.
- [- accessibilityDecrement](<accessibilitydecrement().md>) — Tells the accessibility element to decrement the value of its content.
- [- accessibilityScroll:](<accessibilityscroll(__).md>) — Scrolls screen content in an application-specific way and returns the success or failure of the action.
- [- accessibilityPerformMagicTap](<accessibilityperformmagictap().md>) — Performs a salient action.
