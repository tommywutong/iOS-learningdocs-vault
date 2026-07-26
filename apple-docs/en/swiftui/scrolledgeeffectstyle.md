---
title: ScrollEdgeEffectStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolledgeeffectstyle
source_url: 'https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolledgeeffectstyle.json'
content_hash: 'sha256:6de863000eddce9d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollEdgeEffectStyle

<sub>Structure</sub>

A structure that specifies blur transitions between scrolling content and an area with controls, such as toolbars.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ScrollEdgeEffectStyle
```

## Overview

By default, the system sets an automatic scroll edge effect style to provide a visual transition between scrolling content and stationary controls at both edges of the scroll view in the scrolling direction. The system determines which style to apply based on the platform and context. The [hard](scrolledgeeffectstyle/hard.md) style provides a more opaque, clearly defined linear boundary, and the [soft](scrolledgeeffectstyle/soft.md) style provides a subtle blurred transition:

**Hard**

![](../../../attachments/233eca852dd9072e380bf0a300a19803/ScrollEdgeEffectStyle-2@2x.png)

<sub>A partial image of a list scrolling behind a bottom toolbar on iPhone. The area where the toolbar overlaps the list content is nearly opaque, with a defined, straight horizontal line at the top.</sub>

**Soft**

![](../../../attachments/ce6a289e80029e13b1747a9b04087530/ScrollEdgeEffectStyle-1@2x.png)

<sub>A partial image of a list scrolling behind a bottom toolbar on iPhone. The area where the toolbar overlaps the list is translucent and blurry and gets progressively more opaque from the top to the bottom.</sub>

**None**

![](../../../attachments/ebbd1937d2768b8c0ee06b7c59ff2797/ScrollEdgeEffectStyle-3@2x.png)

<sub>A partial image of a list scrolling behind a bottom toolbar on iPhone. The area where the toolbar overlaps the list is transparent.</sub>

Specify a `ScrollEdgeEffectStyle` for a scroll view using [scrollEdgeEffectStyle(_:for:)](<view/scrolledgeeffectstyle(__for_).md>) when the automatic style the system applies isn’t appropriate for your content and controls. Apply [scrollEdgeEffectHidden(_:for:)](<view/scrolledgeeffecthidden(__for_).md>) to a scroll view to remove the scroll edge effect entirely for an edge you specify.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a scroll edge effect style

- [automatic](scrolledgeeffectstyle/automatic.md) — A scroll edge effect the system applies automatically when pinned content overlaps scrolling content.
- [hard](scrolledgeeffectstyle/hard.md) — A scroll edge effect that provides a linear, nearly opaque boundary between pinned controls and scrolling content.
- [soft](scrolledgeeffectstyle/soft.md) — A scroll edge effect that provides a subtle, blurred boundary between pinned controls and scrolling content.

## See Also

### Configuring scroll edge effects

- [scrollEdgeEffectStyle(_:for:)](<view/scrolledgeeffectstyle(__for_).md>) — Configures the scroll edge effect style for scroll views within this hierarchy.
- [scrollEdgeEffectHidden(_:for:)](<view/scrolledgeeffecthidden(__for_).md>) — Hides any scroll edge effects for scroll views within this hierarchy.
- [safeAreaBar(edge:alignment:spacing:content:)](<view/safeareabar(edge_alignment_spacing_content_).md>) — Shows the specified content as a custom bar beside the modified view.
