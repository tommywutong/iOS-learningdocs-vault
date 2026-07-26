---
title: accessibilityActivate()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityactivate()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityactivate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityactivate%28%29.json'
content_hash: 'sha256:ed89932beed028d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityActivate()

<sub>Instance Method</sub>

Tells the element to activate itself and report the success or failure of the operation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityActivate() -> Bool
```

## Return Value

[YES](../yes.md) if the element was activated or [NO](../no.md) if it was not.

## Discussion

You can use this method to make complex controls more readily accessible to users. The accessibility system calls this method when a VoiceOver user double taps the selected element. Your implementation of this method should activate the element and perform whatever other tasks it deems appropriate. For example, you might use the method to activate a control that requires a complex gesture and would be difficult for VoiceOver users to perform, possibly because the gesture has a different meaning when VoiceOver is running.

After performing any tasks, return an appropriate Boolean value to indicate success or failure.

## See Also

### Performing an action

- [- accessibilityIncrement](<accessibilityincrement().md>) — Tells the accessibility element to increment the value of its content.
- [- accessibilityDecrement](<accessibilitydecrement().md>) — Tells the accessibility element to decrement the value of its content.
- [- accessibilityScroll:](<accessibilityscroll(__).md>) — Scrolls screen content in an application-specific way and returns the success or failure of the action.
- [- accessibilityPerformEscape](<accessibilityperformescape().md>) — Dismisses a modal view and returns the success or failure of the action.
- [- accessibilityPerformMagicTap](<accessibilityperformmagictap().md>) — Performs a salient action.
