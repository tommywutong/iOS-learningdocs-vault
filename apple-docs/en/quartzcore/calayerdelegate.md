---
title: CALayerDelegate
framework: Core Animation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayerdelegate
source_url: 'https://developer.apple.com/documentation/quartzcore/calayerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayerdelegate.json'
content_hash: 'sha256:354d2e3c4edaaa29'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CALayerDelegate

<sub>Protocol</sub>

Methods your app can implement to respond to layer-related events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CALayerDelegate : NSObjectProtocol
```

## Overview

You can implement the methods of this protocol to provide the layer’s content, handle the layout of sublayers, and provide custom animation actions to perform. The object that implements this protocol must be assigned to the [delegate](calayer/delegate.md) property of the layer object.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Providing the Layer’s Content

- [- displayLayer:](<calayerdelegate/display(__).md>) — Tells the delegate to implement the display process.
- [- drawLayer:inContext:](<calayerdelegate/draw(__in_).md>) — Tells the delegate to implement the display process using the layer’s context.
- [- layerWillDraw:](<calayerdelegate/layerwilldraw(__).md>) — Notifies the delegate of an imminent draw.

### Laying Out Sublayers

- [- layoutSublayersOfLayer:](<calayerdelegate/layoutsublayers(of_).md>) — Tells the delegate a layer’s bounds have changed.

### Providing a Layer’s Actions

- [- actionForLayer:forKey:](<calayerdelegate/action(for_forkey_).md>) — Returns the default action of the [- actionForKey:](<calayer/action(forkey_).md>) method.

## See Also

### Layer Basics

- [CALayer](calayer.md) — An object that manages image-based content and allows you to perform animations on that content.
- [CAConstraint](caconstraint.md) — A representation of a single layout constraint between two layers.
- [CALayoutManager](calayoutmanager.md) — Methods that allow an object to manage the layout of a layer and its sublayers.
- [CAConstraintLayoutManager](caconstraintlayoutmanager.md) — An object that provides a constraint-based layout manager.
- [CAAction](caaction.md) — An interface that allows instances to respond to actions triggered by a Core Animation layer change.
