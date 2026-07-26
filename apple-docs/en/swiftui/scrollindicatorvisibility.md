---
title: ScrollIndicatorVisibility
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollindicatorvisibility
source_url: 'https://developer.apple.com/documentation/swiftui/scrollindicatorvisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollindicatorvisibility.json'
content_hash: 'sha256:d64fc65d07be78d4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollIndicatorVisibility

<sub>Structure</sub>

The visibility of scroll indicators of a UI element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ScrollIndicatorVisibility
```

## Overview

Pass a value of this type to the [scrollIndicators(_:axes:)](<view/scrollindicators(__axes_).md>) method to specify the preferred scroll indicator visibility of a view hierarchy.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Getting visibilties

- [automatic](scrollindicatorvisibility/automatic.md) — Scroll indicator visibility depends on the policies of the component accepting the visibility configuration.
- [hidden](scrollindicatorvisibility/hidden.md) — Hide the scroll indicators.
- [never](scrollindicatorvisibility/never.md) — Scroll indicators should never be visible.
- [visible](scrollindicatorvisibility/visible.md) — Show the scroll indicators.

## See Also

### Showing scroll indicators

- [scrollIndicatorsFlash(onAppear:)](<view/scrollindicatorsflash(onappear_).md>) — Flashes the scroll indicators of a scrollable view when it appears.
- [scrollIndicatorsFlash(trigger:)](<view/scrollindicatorsflash(trigger_).md>) — Flashes the scroll indicators of scrollable views when a value changes.
- [scrollIndicators(_:axes:)](<view/scrollindicators(__axes_).md>) — Sets the visibility of scroll indicators within this view.
- [horizontalScrollIndicatorVisibility](environmentvalues/horizontalscrollindicatorvisibility.md) — The visibility to apply to scroll indicators of any horizontally scrollable content.
- [verticalScrollIndicatorVisibility](environmentvalues/verticalscrollindicatorvisibility.md) — The visiblity to apply to scroll indicators of any vertically scrollable content.
