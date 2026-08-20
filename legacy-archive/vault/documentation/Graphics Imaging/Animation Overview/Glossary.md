---
title: Animation Overview
apple_id: TP40004952
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/Animation_Overview/Glossary/Glossary.html
archived_at: '2026-07-15T07:35:25.848524Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Animation Overview](Introduction%20to%20Animation%20Overview.md)


[Next](Document%20Revision%20History.md)[Previous](Choosing%20the%20Animation%20Technology%20for%20Your%20Application.md)

# Glossary

- __animation__

  Animation is a visual technique that provides the illusion of motion by displaying a collection of images in rapid sequence.

- __animation proxy__

  An animation proxy “stands in” for an object and provides animation capabilities without significantly impacting the original objects API.

- __basic animation__

  A simple animation from a start value to a target value.

- __Core Image__

  The framework that provides image processing filters used to process still and video images.

- __duration__

  The length of time, in seconds, it takes for an animation to complete.

- __keyframe animation__

  An animation that specifies an array of values that an animation uses as sequential targets.

- __interpolation__

  The calculation of intermediate values relative to known beginning and ending values.

- __layer-backed view__

  An instance of an `NSView` object that uses a Core Animation layer to cache its drawing content. The view is responsible for managing the layer tree, the developer should not manipulate the layer tree directly.

- __layer-hosting view__

  An instance of an `NSView` object that hosts a Core Animation layer tree. The developer is responsible for managing the layer tree directly.

- __OpenGL__

  An open source graphics library. For more information see [http://www.opengl.org/](http://www.opengl.org/).

- __pacing__

  The distribution of the interpolated values of an animation across the duration of the animation.

- __transition animation__

  An animation that uses a Core Image filter to apply a visual effect to an animation object being displayed or hidden.

[Next](Document%20Revision%20History.md)[Previous](Choosing%20the%20Animation%20Technology%20for%20Your%20Application.md)

