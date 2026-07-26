---
title: 'accessibilityScroll(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/accessibilityscroll(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityscroll(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityscroll%28_%3A%29.json'
content_hash: 'sha256:02970e1d1ba12c65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityScroll(_:)

<sub>Instance Method</sub>

Scrolls screen content in an application-specific way and returns the success or failure of the action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool
```

## Parameters

- `direction` — A constant that specifies the direction of the scrolling action. See [UIAccessibilityScrollDirection](../../uikit/uiaccessibilityscrolldirection.md) for descriptions of valid constants.

## Return Value

[YES](../yes.md) if the scrolling action succeeds; otherwise, [NO](../no.md). By default, this method returns [NO](../no.md).

## Discussion

Implement this method if a view in the view hierarchy supports a scroll by page action.

- If the scrolling action succeeds for the specified direction, return [YES](../yes.md) and post the [pageScrolled](../../uikit/uiaccessibility/notification/pagescrolled.md) notification.
- If the scrolling action fails, `accessibilityScroll:` is called on a parent view in the hierarchy.

## See Also

### Performing an action

- [- accessibilityActivate](<accessibilityactivate().md>) — Tells the element to activate itself and report the success or failure of the operation.
- [- accessibilityIncrement](<accessibilityincrement().md>) — Tells the accessibility element to increment the value of its content.
- [- accessibilityDecrement](<accessibilitydecrement().md>) — Tells the accessibility element to decrement the value of its content.
- [- accessibilityPerformEscape](<accessibilityperformescape().md>) — Dismisses a modal view and returns the success or failure of the action.
- [- accessibilityPerformMagicTap](<accessibilityperformmagictap().md>) — Performs a salient action.
