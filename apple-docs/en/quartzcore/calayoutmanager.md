---
title: CALayoutManager
framework: Core Animation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [Mac Catalyst 13.1+, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayoutmanager
source_url: 'https://developer.apple.com/documentation/quartzcore/calayoutmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayoutmanager.json'
content_hash: 'sha256:ab148a8b3d97d730'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CALayoutManager

<sub>Protocol</sub>

Methods that allow an object to manage the layout of a layer and its sublayers.

<sub>Mac Catalyst, macOS</sub>

```swift
protocol CALayoutManager : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [CAConstraintLayoutManager](caconstraintlayoutmanager.md)

## Topics

### Managing Layout

- [- invalidateLayoutOfLayer:](<calayoutmanager/invalidatelayout(of_).md>) — Invalidates the layout of a layer so it knows to refresh its content on the next frame.
- [- layoutSublayersOfLayer:](<calayoutmanager/layoutsublayers(of_).md>) — Override to customize layout of sublayers whenever the layer needs redrawing.
- [- preferredSizeOfLayer:](<calayoutmanager/preferredsize(of_).md>) — Override to customize layer size.

## See Also

### Layer Basics

- [CALayer](calayer.md) — An object that manages image-based content and allows you to perform animations on that content.
- [CALayerDelegate](calayerdelegate.md) — Methods your app can implement to respond to layer-related events.
- [CAConstraint](caconstraint.md) — A representation of a single layout constraint between two layers.
- [CAConstraintLayoutManager](caconstraintlayoutmanager.md) — An object that provides a constraint-based layout manager.
- [CAAction](caaction.md) — An interface that allows instances to respond to actions triggered by a Core Animation layer change.
