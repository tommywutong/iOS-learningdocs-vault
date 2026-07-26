---
title: ContainerBackgroundPlacement
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/containerbackgroundplacement
source_url: 'https://developer.apple.com/documentation/swiftui/containerbackgroundplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/containerbackgroundplacement.json'
content_hash: 'sha256:5d8d7d73736a654b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ContainerBackgroundPlacement

<sub>Structure</sub>

The placement of a container background.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ContainerBackgroundPlacement
```

## Overview

This method controls where to place a background that you specify with the [containerBackground(_:for:)](<view/containerbackground(__for_).md>) or [containerBackground(for:alignment:content:)](<view/containerbackground(for_alignment_content_).md>) modifier.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting placements

- [navigation](containerbackgroundplacement/navigation.md) — A background placement inside a [NavigationStack](navigationstack.md) or [NavigationSplitView](navigationsplitview.md).
- [tabView](containerbackgroundplacement/tabview.md) — A background placement inside a [TabView](tabview.md).
- [widget](containerbackgroundplacement/widget.md) — The container background placement for a widget.

### Getting StoreKit placements

- [subscriptionStore](containerbackgroundplacement/subscriptionstore.md) — An automatic placement within a subscription store view, based on the view’s context.
- [subscriptionStoreFullHeight](containerbackgroundplacement/subscriptionstorefullheight.md) — A background placement that spans the full height of a subscription store view.
- [subscriptionStoreHeader](containerbackgroundplacement/subscriptionstoreheader.md) — A background placement behind the marketing content of a subscription store view.

### Type Properties

- [navigationSplitView](containerbackgroundplacement/navigationsplitview.md) — A background placement behind the content of a [NavigationSplitView](navigationsplitview.md).
- [window](containerbackgroundplacement/window.md) — A  background placement inside a [Window](window.md) or [WindowGroup](windowgroup.md)

## See Also

### Layering views

- [Adding a background to your view](adding-a-background-to-your-view.md) — Compose a background behind your view and extend it beyond the safe area insets.
- [ZStack](zstack.md) — A view that overlays its subviews, aligning them in both axes.
- [zIndex(_:)](<view/zindex(__).md>) — Controls the display order of overlapping views.
- [background(alignment:content:)](<view/background(alignment_content_).md>) — Layers the views that you specify behind this view.
- [background(_:ignoresSafeAreaEdges:)](<view/background(__ignoressafeareaedges_).md>) — Sets the view’s background to a style.
- [background(ignoresSafeAreaEdges:)](<view/background(ignoressafeareaedges_).md>) — Sets the view’s background to the default background style.
- [background(_:in:fillStyle:)](<view/background(__in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with a style.
- [background(in:fillStyle:)](<view/background(in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with the default background style.
- [overlay(alignment:content:)](<view/overlay(alignment_content_).md>) — Layers the views that you specify in front of this view.
- [overlay(_:ignoresSafeAreaEdges:)](<view/overlay(__ignoressafeareaedges_).md>) — Layers the specified style in front of this view.
- [overlay(_:in:fillStyle:)](<view/overlay(__in_fillstyle_).md>) — Layers a shape that you specify in front of this view.
- [backgroundMaterial](environmentvalues/backgroundmaterial.md) — The material underneath the current view.
- [containerBackground(_:for:)](<view/containerbackground(__for_).md>) — Sets the container background of the enclosing container using a view.
- [containerBackground(for:alignment:content:)](<view/containerbackground(for_alignment_content_).md>) — Sets the container background of the enclosing container using a view.
