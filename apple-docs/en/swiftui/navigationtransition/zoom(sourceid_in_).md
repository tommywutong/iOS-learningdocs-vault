---
title: 'zoom(sourceID:in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/navigationtransition/zoom(sourceid:in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationtransition/zoom(sourceid:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationtransition/zoom%28sourceid%3Ain%3A%29.json'
content_hash: 'sha256:debd1235913e6194'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationTransition](../navigationtransition.md)

# zoom(sourceID:in:)

<sub>Type Method</sub>

A navigation transition that zooms the appearing view from a given source view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static func zoom(sourceID: some Hashable, in namespace: Namespace.ID) -> ZoomNavigationTransition
```

## Parameters

- `sourceID` — The identifier you provide to a corresponding `matchedTransitionSource` modifier.

- `namespace` — The namespace where you define the `id`. You can create new namespaces by adding the [Namespace](../namespace.md) attribute to a [View](../view.md) type, then reading its value in the view’s body method.

## Discussion

Indicate the source view using the [matchedTransitionSource(id:in:)](<../view/matchedtransitionsource(id_in_).md>) modifier.

> [!note] Note
> The zoom transition is not supported in tvOS. Navigation uses [automatic](automatic.md) instead.

## See Also

### Getting built-in transitions

- [automatic](automatic.md) — A style that automatically chooses the appropriate presentation transition for the current context.
- [AutomaticNavigationTransition](../automaticnavigationtransition.md) — A style that automatically chooses the appropriate presentation transition for the current context.
- [crossFade](crossfade.md) — A navigation transition that cross-fades between the appearing view and the disappearing view. _(beta)_
- [CrossFadeNavigationTransition](../crossfadenavigationtransition.md) — A navigation transition that cross-fades between the appearing view and the disappearing view. _(beta)_
- [ZoomNavigationTransition](../zoomnavigationtransition.md) — A navigation transition that zooms the appearing view from a given source view.
