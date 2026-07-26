---
title: Accessible appearance
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessible-appearance
source_url: 'https://developer.apple.com/documentation/swiftui/accessible-appearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessible-appearance.json'
content_hash: 'sha256:c52e18605e07c7c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Accessible appearance

<sub>API Collection</sub>

Enhance the legibility of content in your app’s interface.

## Overview

Make content easier for people to see by making it larger, giving it greater contrast, or reducing the amount of distracting motion.

![](../../../attachments/798b84460063f228cc1996fef3379310/accessible-appearance-hero@2x.png)

For design guidance, see [Accessibility](../design/human-interface-guidelines/accessibility.md#Text-display) in the Accessibility section of the Human Interface Guidelines.

## Topics

### Managing color

- [accessibilityIgnoresInvertColors(_:)](<view/accessibilityignoresinvertcolors(__).md>) — Sets whether this view should ignore the system Smart Invert setting.
- [accessibilityInvertColors](environmentvalues/accessibilityinvertcolors.md) — Whether the system preference for Invert Colors is enabled.
- [accessibilityDifferentiateWithoutColor](environmentvalues/accessibilitydifferentiatewithoutcolor.md) — Whether the system preference for Differentiate without Color is enabled.

### Enlarging content

- [accessibilityShowsLargeContentViewer()](<view/accessibilityshowslargecontentviewer().md>) — Adds a default large content view to be shown by the large content viewer.
- [accessibilityShowsLargeContentViewer(_:)](<view/accessibilityshowslargecontentviewer(__).md>) — Adds a custom large content view to be shown by the large content viewer.
- [accessibilityLargeContentViewerEnabled](environmentvalues/accessibilitylargecontentviewerenabled.md) — Whether the Large Content Viewer is enabled.

### Improving legibility

- [accessibilityShowButtonShapes](environmentvalues/accessibilityshowbuttonshapes.md) — Whether the system preference for Show Button Shapes is enabled. _(deprecated)_
- [accessibilityReduceTransparency](environmentvalues/accessibilityreducetransparency.md) — Whether the system preference for Reduce Transparency is enabled.
- [legibilityWeight](environmentvalues/legibilityweight.md) — The font weight to apply to text.
- [LegibilityWeight](legibilityweight.md) — The Accessibility Bold Text user setting options.

### Minimizing motion

- [accessibilityDimFlashingLights](environmentvalues/accessibilitydimflashinglights.md) — Whether the setting to reduce flashing or strobing lights in video content is on. This setting can also be used to determine if UI in playback controls should be shown to indicate upcoming content that includes flashing or strobing lights.
- [accessibilityPlayAnimatedImages](environmentvalues/accessibilityplayanimatedimages.md) — Whether the setting for playing animations in an animated image is on. When this value is false, any presented image that contains animation should not play automatically.
- [accessibilityReduceMotion](environmentvalues/accessibilityreducemotion.md) — Whether the system preference for Reduce Motion is enabled.

### Using assistive access

- [accessibilityAssistiveAccessEnabled](environmentvalues/accessibilityassistiveaccessenabled.md) — A Boolean value that indicates whether Assistive Access is in use.
- [AssistiveAccess](assistiveaccess.md) — A scene that presents an interface appropriate for Assistive Access on iOS and iPadOS. On other platforms, this scene is unused.
- [assistiveAccessNavigationIcon(_:)](<view/assistiveaccessnavigationicon(__).md>) — Configures the view’s icon for purposes of navigation.
- [assistiveAccessNavigationIcon(systemImage:)](<view/assistiveaccessnavigationicon(systemimage_).md>) — Configures the view’s icon for purposes of navigation.

## See Also

### Accessibility

- [Accessibility fundamentals](accessibility-fundamentals.md) — Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Accessible controls](accessible-controls.md) — Improve access to actions that your app can undertake.
- [Accessible descriptions](accessible-descriptions.md) — Describe interface elements to help people understand what they represent.
- [Accessible navigation](accessible-navigation.md) — Enable users to navigate to specific user interface elements using rotors.
