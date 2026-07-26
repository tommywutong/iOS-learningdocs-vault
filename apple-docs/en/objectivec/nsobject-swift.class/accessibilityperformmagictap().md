---
title: accessibilityPerformMagicTap()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityperformmagictap()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityperformmagictap()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityperformmagictap%28%29.json'
content_hash: 'sha256:121aa73aba2bbb9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityPerformMagicTap()

<sub>Instance Method</sub>

Performs a salient action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityPerformMagicTap() -> Bool
```

## Return Value

[YES](../yes.md) if the magic tap action succeeds; otherwise, [NO](../no.md). By default, this method returns [NO](../no.md).

## Discussion

The exact action performed by this method depends your app, typically toggling the most important state of the app. For example, in the Phone app it answers and ends phone calls, in the Music app it plays and pauses playback, in the Clock app it starts and stops a timer, and in the Camera app it takes a picture.

## See Also

### Performing an action

- [- accessibilityActivate](<accessibilityactivate().md>) — Tells the element to activate itself and report the success or failure of the operation.
- [- accessibilityIncrement](<accessibilityincrement().md>) — Tells the accessibility element to increment the value of its content.
- [- accessibilityDecrement](<accessibilitydecrement().md>) — Tells the accessibility element to decrement the value of its content.
- [- accessibilityScroll:](<accessibilityscroll(__).md>) — Scrolls screen content in an application-specific way and returns the success or failure of the action.
- [- accessibilityPerformEscape](<accessibilityperformescape().md>) — Dismisses a modal view and returns the success or failure of the action.
