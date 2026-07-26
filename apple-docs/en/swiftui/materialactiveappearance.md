---
title: MaterialActiveAppearance
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/materialactiveappearance
source_url: 'https://developer.apple.com/documentation/swiftui/materialactiveappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/materialactiveappearance.json'
content_hash: 'sha256:a6d0c5dc1dc6e5b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MaterialActiveAppearance

<sub>Structure</sub>

The behavior for how materials appear active and inactive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MaterialActiveAppearance
```

## Overview

On macOS, materials have active and inactive appearances that can reinforce the active appearance of the window they are in:

- Materials used as a `window` container background and `bar` materials will appear inactive when their containing window is inactive.
- All other materials will always appear active by default.

An explicit active appearance can be set to override a material’s default behavior. For example, materials used as the `window` container background can be made to always appear active by setting the active appearance behavior to be always active:

```swift
Text("Hello, World!")
    .containerBackground(
        Material.regular.materialActiveAppearance(.active),
        for: .window)
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [active](materialactiveappearance/active.md) — Materials will always appear active.
- [automatic](materialactiveappearance/automatic.md) — Materials will automatically appear active or inactive based on context and platform convention.
- [inactive](materialactiveappearance/inactive.md) — Materials will always appear inactive.
- [matchWindow](materialactiveappearance/matchwindow.md) — Materials will have an active or inactive appearance based on the active appearance of their window.

## See Also

### Transforming colors

- [brightness(_:)](<view/brightness(__).md>) — Brightens this view by the specified amount.
- [contrast(_:)](<view/contrast(__).md>) — Sets the contrast and separation between similar colors in this view.
- [colorInvert()](<view/colorinvert().md>) — Inverts the colors in this view.
- [colorMultiply(_:)](<view/colormultiply(__).md>) — Adds a color multiplication effect to this view.
- [saturation(_:)](<view/saturation(__).md>) — Adjusts the color saturation of this view.
- [grayscale(_:)](<view/grayscale(__).md>) — Adds a grayscale effect to this view.
- [hueRotation(_:)](<view/huerotation(__).md>) — Applies a hue rotation effect to this view.
- [luminanceToAlpha()](<view/luminancetoalpha().md>) — Adds a luminance to alpha effect to this view.
- [materialActiveAppearance(_:)](<view/materialactiveappearance(__).md>) — Sets an explicit active appearance for materials in this view.
- [materialActiveAppearance](environmentvalues/materialactiveappearance.md) — The behavior materials should use for their active state, defaulting to `automatic`.
