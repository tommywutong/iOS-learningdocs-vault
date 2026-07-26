---
title: NavigationTransition
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/navigationtransition
source_url: 'https://developer.apple.com/documentation/swiftui/navigationtransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationtransition.json'
content_hash: 'sha256:febe24ba20988f6e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NavigationTransition

<sub>Protocol</sub>

A type that defines the transition to use when navigating to a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NavigationTransition
```

## Relationships

- **Conforming Types**: [AnyNavigationTransition](anynavigationtransition.md), [AutomaticNavigationTransition](automaticnavigationtransition.md), [CrossFadeNavigationTransition](crossfadenavigationtransition.md), [ZoomNavigationTransition](zoomnavigationtransition.md)

## Topics

### Getting built-in transitions

- [automatic](navigationtransition/automatic.md) — A style that automatically chooses the appropriate presentation transition for the current context.
- [AutomaticNavigationTransition](automaticnavigationtransition.md) — A style that automatically chooses the appropriate presentation transition for the current context.
- [crossFade](navigationtransition/crossfade.md) — A navigation transition that cross-fades between the appearing view and the disappearing view. _(beta)_
- [CrossFadeNavigationTransition](crossfadenavigationtransition.md) — A navigation transition that cross-fades between the appearing view and the disappearing view. _(beta)_
- [zoom(sourceID:in:)](<navigationtransition/zoom(sourceid_in_).md>) — A navigation transition that zooms the appearing view from a given source view.
- [ZoomNavigationTransition](zoomnavigationtransition.md) — A navigation transition that zooms the appearing view from a given source view.

## See Also

### Defining navigation transitions

- [navigationTransition(_:)](<view/navigationtransition(__).md>) — Sets the navigation transition style for this view.
- [AnyNavigationTransition](anynavigationtransition.md) — A type-erasing navigation transition that allows for providing any navigation transition value dynamically. _(beta)_
- [CrossFadeNavigationTransition](crossfadenavigationtransition.md) — A navigation transition that cross-fades between the appearing view and the disappearing view. _(beta)_
