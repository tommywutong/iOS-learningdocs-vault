---
title: Core Animation
framework: Core Animation
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore
source_url: 'https://developer.apple.com/documentation/quartzcore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore.json'
content_hash: 'sha256:f2e300905c225712'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Core Animation

<sub>Framework</sub>

Render, compose, and animate visual elements.

## Overview

Core Animation provides high frame rates and smooth animations without burdening the CPU or slowing down your app. Core Animation does most of the work of drawing each frame of an animation for you. You’re responsible for configuring the animation parameters, such as the start and end points, and Core Animation does the rest. It accelerates the rendering by handing over most of the work to dedicated graphics hardware. For more details, see [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514).

## Topics

### Layer Basics

- [CALayer](quartzcore/calayer.md) — An object that manages image-based content and allows you to perform animations on that content.
- [CALayerDelegate](quartzcore/calayerdelegate.md) — Methods your app can implement to respond to layer-related events.
- [CAConstraint](quartzcore/caconstraint.md) — A representation of a single layout constraint between two layers.
- [CALayoutManager](quartzcore/calayoutmanager.md) — Methods that allow an object to manage the layout of a layer and its sublayers.
- [CAConstraintLayoutManager](quartzcore/caconstraintlayoutmanager.md) — An object that provides a constraint-based layout manager.
- [CAAction](quartzcore/caaction.md) — An interface that allows instances to respond to actions triggered by a Core Animation layer change.

### Text, Shapes, and Gradients

- [CATextLayer](quartzcore/catextlayer.md) — A layer that provides simple text layout and rendering of plain or attributed strings.
- [CAShapeLayer](quartzcore/cashapelayer.md) — A layer that draws a cubic Bezier spline in its coordinate space.
- [CAGradientLayer](quartzcore/cagradientlayer.md) — A layer that draws a color gradient over its background color, filling the shape of the layer.

### Animation

- [CAAnimation](quartzcore/caanimation.md) — The abstract superclass for animations in Core Animation.
- [CAAnimationDelegate](quartzcore/caanimationdelegate.md) — Methods your app can implement to respond when animations start and stop.
- [CAPropertyAnimation](quartzcore/capropertyanimation.md) — An abstract subclass for creating animations that manipulate the value of layer properties.
- [CABasicAnimation](quartzcore/cabasicanimation.md) — An object that provides basic, single-keyframe animation capabilities for a layer property.
- [CAKeyframeAnimation](quartzcore/cakeyframeanimation.md) — An object that provides keyframe animation capabilities for a layer object.
- [CASpringAnimation](quartzcore/caspringanimation.md) — An animation that applies a spring-like force to a layer’s properties.
- [CATransition](quartzcore/catransition.md) — An object that provides an animated transition between a layer’s states.
- [CAValueFunction](quartzcore/cavaluefunction.md) — An object that provides a flexible method of defining animated transformations.

### Animation Groups

- [CAAnimationGroup](quartzcore/caanimationgroup.md) — An object that allows multiple animations to be grouped and run concurrently.
- [CATransaction](quartzcore/catransaction.md) — A mechanism for grouping multiple layer-tree operations into atomic updates to the render tree.

### Animation Timing

- [CACurrentMediaTime](<quartzcore/cacurrentmediatime().md>) — Returns the current absolute time, in seconds.
- [CAMediaTimingFunction](quartzcore/camediatimingfunction.md) — A function that defines the pacing of an animation as a timing curve.
- [CAMediaTiming](quartzcore/camediatiming.md) — Methods that model a hierarchical timing system, allowing objects to map time between their parent and local time.
- [CADisplayLink](quartzcore/cadisplaylink.md) — A timer object that allows your app to synchronize its drawing to the refresh rate of the display.
- [CAMetalDisplayLink](quartzcore/cametaldisplaylink.md) — A class your Metal app uses to register for callbacks to synchronize its animations for a display.
- [Update](quartzcore/cametaldisplaylink/update.md) — Stores information about a single update from a Metal display link instance.
- [CAMetalDisplayLinkDelegate](quartzcore/cametaldisplaylinkdelegate.md) — A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.

### Particle Systems

- [CAEmitterLayer](quartzcore/caemitterlayer.md) — A layer that emits, animates, and renders a particle system.
- [CAEmitterCell](quartzcore/caemittercell.md) — The definition of a particle emitted by a particle layer.

### Advanced Layer Options

- [CAScrollLayer](quartzcore/cascrolllayer.md) — A layer that displays scrollable content larger than its own bounds.
- [CATiledLayer](quartzcore/catiledlayer.md) — A layer that provides a way to asynchronously provide tiles of the layer’s content, potentially cached at multiple levels of detail.
- [CATransformLayer](quartzcore/catransformlayer.md) — Objects used to create true 3D layer hierarchies, rather than the flattened hierarchy rendering model used by other layer types.
- [CAReplicatorLayer](quartzcore/careplicatorlayer.md) — A layer that creates a specified number of sublayer copies with varying geometric, temporal, and color transformations.

### Metal and OpenGL

- [CAMetalLayer](quartzcore/cametallayer.md) — A Core Animation layer that Metal can render into, typically displayed onscreen.
- [CAMetalDrawable](quartzcore/cametaldrawable.md) — A Metal drawable associated with a Core Animation layer.
- [CAEAGLLayer](quartzcore/caeagllayer.md) — A layer that supports drawing OpenGL content in iOS and tvOS applications. _(deprecated)_
- [CAEDRMetadata](quartzcore/caedrmetadata.md) — Metadata describing how extended dynamic range (EDR) values should be tone mapped.
- [CAOpenGLLayer](quartzcore/caopengllayer.md) — A layer that provides a layer suitable for rendering OpenGL content. _(deprecated)_
- [CARenderer](quartzcore/carenderer.md) — A layer that allows an application to render a layer tree into a Core OpenGL context.

### ProMotion

- [Optimizing iPhone and iPad apps to support ProMotion displays](quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md) — Improve your app’s visual appearance and save power by requesting preferred refresh rates and synchronizing your animations with the system.

### Remote Display of Layer Content

- [CARemoteLayerClient](quartzcore/caremotelayerclient.md) — A legacy class for cross-process rendering.
- [CARemoteLayerServer](quartzcore/caremotelayerserver.md) — A legacy class for cross-process rendering.

### Transforms

- [Transforms](quartzcore/transforms.md) — Define transform matrices to apply affine transformations to layers in Core Animation.

### Quartz Composer

- [QCCompositionLayer](quartz/qccompositionlayer.md) — A layer that loads, plays, and controls Quartz Composer compositions in a Core Animation layer hierarchy. _(deprecated)_

### Reference

- [Core Animation Structures](quartzcore/core-animation-structures.md)
- [Core Animation Constants](quartzcore/core-animation-constants.md)
- [QuartzCore Functions](quartzcore/quartzcore-functions.md)
- [Core Animation Data Types](quartzcore/core-animation-data-types.md)

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
