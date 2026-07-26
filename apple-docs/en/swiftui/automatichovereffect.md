---
title: AutomaticHoverEffect
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/automatichovereffect
source_url: 'https://developer.apple.com/documentation/swiftui/automatichovereffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/automatichovereffect.json'
content_hash: 'sha256:7d108898b38f63a8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AutomaticHoverEffect

<sub>Structure</sub>

The default hover effect based on the surrounding context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct AutomaticHoverEffect
```

## Overview

The automatic effect will resolve to any [defaultHoverEffect(_:)](<view/defaulthovereffect(__).md>) applied to the current View hierarchy, or a system-defined effect if no default effect has been defined.

You can also use [automatic](customhovereffect/automatic.md) to construct this hover effect.

## Relationships

- **Conforms To**: [CustomHoverEffect](customhovereffect.md)

## Topics

### Initializers

- [init()](<automatichovereffect/init().md>) — Creates an automatic hover effect.

## See Also

### Supporting types

- [EmptyHoverEffect](emptyhovereffect.md) — A base hover effect used to build additional effects.
- [HighlightHoverEffect](highlighthovereffect.md) — A hover effect that highlights views using a light source to indicate position.
- [LiftHoverEffect](lifthovereffect.md) — A hover effect that slides the pointer under the view and disappears as the view scales up and gains a shadow.
