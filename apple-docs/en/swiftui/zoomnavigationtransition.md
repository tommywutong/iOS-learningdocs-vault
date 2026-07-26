---
title: ZoomNavigationTransition
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/zoomnavigationtransition
source_url: 'https://developer.apple.com/documentation/swiftui/zoomnavigationtransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/zoomnavigationtransition.json'
content_hash: 'sha256:6f55e5af4b6914be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ZoomNavigationTransition

<sub>Structure</sub>

A navigation transition that zooms the appearing view from a given source view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct ZoomNavigationTransition
```

## Overview

Indicate the source view using the [matchedTransitionSource(id:in:)](<view/matchedtransitionsource(id_in_).md>) modifier.

> [!note] Note
> The zoom transition is not supported in tvOS. Navigation uses [automatic](navigationtransition/automatic.md) instead.

## Relationships

- **Conforms To**: [NavigationTransition](navigationtransition.md)

## See Also

### Getting built-in transitions

- [automatic](navigationtransition/automatic.md) — A style that automatically chooses the appropriate presentation transition for the current context.
- [AutomaticNavigationTransition](automaticnavigationtransition.md) — A style that automatically chooses the appropriate presentation transition for the current context.
- [crossFade](navigationtransition/crossfade.md) — A navigation transition that cross-fades between the appearing view and the disappearing view. _(beta)_
- [CrossFadeNavigationTransition](crossfadenavigationtransition.md) — A navigation transition that cross-fades between the appearing view and the disappearing view. _(beta)_
- [zoom(sourceID:in:)](<navigationtransition/zoom(sourceid_in_).md>) — A navigation transition that zooms the appearing view from a given source view.
