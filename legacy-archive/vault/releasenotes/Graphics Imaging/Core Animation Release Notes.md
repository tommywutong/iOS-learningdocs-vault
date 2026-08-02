---
title: Core Animation Release Notes
apple_id: TP40005258
resource_type: Release Note
platform: macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2009-06-01'
source_url: https://developer.apple.com/library/archive/releasenotes/GraphicsImaging/CoreAnimation_RN/index.html
archived_at: '2026-07-18T02:58:39.288990Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Core Animation Release Notes

#### Contents:

- [OS X v10.6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenjyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [WWDC 2007 Seed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenjyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ni)
- [March Seed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenjyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjs)

### OS X v10.6

### New Classes and Properties

There have been a number of new classes added in OS X v10.6:

|  |  |
| --- | --- |
| **[CAEmitterLayer](https://developer.apple.com/documentation/quartzcore/caemitterlayer)** | : The `CAEmitterLayer` class provides a particle emitter system for Core Animation. The particles are defined by instances of `CAEmitterCell`. |
| **[CAEmitterCell](https://developer.apple.com/documentation/quartzcore/caemittercell)** | : The `CAEmitterCell` class represents one source of particles being emitted in a `CAEmitterLayer`. An emitter cell define the direction in which they emit and the properties of the emitted particles. Emitter cells can have an array of sub-cells, which lets the particles themselves emit particles. |
| **[CAGradientLayer](https://developer.apple.com/documentation/quartzcore/cagradientlayer)** | : The `CAGradientLayer` class draws a color gradient over its background color, filling the shape of the layer (including rounded corners). |
| **[CAReplicatorLayer](https://developer.apple.com/documentation/quartzcore/careplicatorlayer)** | : The `CAReplicatorLayer` class creates a specified number of copies of its sublayers (the source layer), each copy potentially having geometric, temporal and color transformations applied to it. |
| **[CAShapeLayer](https://developer.apple.com/documentation/quartzcore/cashapelayer)** | : The `CAShapeLayer` class draws a cubic Bezier spline in its coordinate space. The shape is composited between the layer's contents and its first sublayer. |
| **[CATransformLayer](https://developer.apple.com/documentation/quartzcore/catransformlayer)** | : `CATransformLayer` objects are used to create true 3D layer hierarchies, rather than the flattened hierarchy rendering model used by other CALayer classes.. |
| **[CAValueFunction](https://developer.apple.com/documentation/quartzcore/cavaluefunction)** | : The `CAValueFunction` class provides a more flexible means of applying functions to property values during animation. A value function defines an optional transformation that is applied to the interpolated value before it is set in the presentation layer. |

### New Properties and Methods

Additional capabilities have been added to the following classes:

- [CALayer](https://developer.apple.com/documentation/quartzcore/calayer)

  - Will now only synthesize property accessor methods for properties marked `@dynamic` in their class implementation. For backwards compatibility we retain the previous behavior for executables linked on OS versions prior to 10.6.
  - New layer properties: anchorPointZ, contentsCenter, geometryFlipped, minificationFilterBias
  - New layer methods: -contentsAreFlipped, -needsDisplay, -displayIfNeeded, -needsLayout, +needsDisplayForKey, -animationKeys
  - New layer delegate method: -layoutSublayersOfLayer:
  - New minification filter: `kCAFilterTrilinear`. Enables higher quality OpenGL downsampling of images. Requires the extra cost of downsampling the image to produce the mipmap pyramid every time the image changes. Some graphics cards only support this for images with power-of-two dimensions.
  - It is now possible to animate your own properties. See [Animating Your Own Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenjyfvbuqmjnknltg) for more information.
- [CAConstraint](https://developer.apple.com/documentation/quartzcore/caconstraint)

  - New properties: `sourceName`, `offset`, `scale`, `sourceAttribute`, and `sourceName`.
- CATransaction

  - Added `lock` and `unlock` methods for managing property atomicity
  - Added method accessors for existing `disableActions` and `animationDuration` KVC properties
  - Added new KVC properties and method accessors: `animationTimingFunction`, `completionBlock`
- [CAMediaTimingFunction](https://developer.apple.com/documentation/quartzcore/camediatimingfunction)

  - A new constant, `kCAMediaTimingFunctionDefault`, defines the constant used by default for properties.
- [CAPropertyAnimation](https://developer.apple.com/documentation/quartzcore/capropertyanimation)

  - New property: `valueFunction`.
- [CATiledLayer](https://developer.apple.com/documentation/quartzcore/catiledlayer)

  - When rendering tiles a single tiled layer's [drawInContext:](https://developer.apple.com/documentation/quartzcore/calayer/1410757-draw) method may now be invoked on multiple threads concurrently. (This has always been the documented behavior, but OS X v10.5 restricted each layer instance to being called on a single thread at any point in time.)
- [CATextLayer](https://developer.apple.com/documentation/quartzcore/catextlayer)

  - The [fontSize](https://developer.apple.com/documentation/quartzcore/catextlayer/1515290-fontsize) and [setForegroundColor:](https://developer.apple.com/documentation/quartzcore/catextlayer/1515305-foregroundcolor) properties are now animatable. Implicit animations are enabled for these properties, but only for applications that were linked on OS X v10.6 or later.
  - Trilinear filtering (with configurable filter bias) is also supported for tiled layers. However the level of detail selection is currently per-polygon rather than per-pixel.
- [CARenderer](https://developer.apple.com/documentation/quartzcore/carenderer)

  - The supplied `CGLContextObj` is now retained for the lifetime of the `CARenderer` instance.
- [CAOpenGLLayer](https://developer.apple.com/documentation/quartzcore/caopengllayer)

  - This class may now call the draw method of the subclass with the OpenGL context bound to a non-zero framebuffer object. This means that OpenGL code that uses framebuffer objects for offscreen rendering must always save and restore the initial framebuffer binding.
  - Related to these changes, subclasses are no longer required to flush the OpenGL context after rendering, `CAOpenGLLayer` does this. However to ensure backwards compatibility with OS X v10.5, subclasses are recommended to call the base implementation of the [drawInCGLContext:pixelFormat:forLayerTime:displayTime:](https://developer.apple.com/documentation/quartzcore/caopengllayer/1522316-draw) method after rendering, e.g.:

```objc
- (void)drawInCGLContext:(CGLContextObj)ctx pixelFormat:(CGLPixelFormatObj)pf
    forLayerTime:(CFTimeInterval)t displayTime:(const CVTimeStamp *)ts
{
    // rendering code…

    // ensure context is flushed if required
    [super drawInCGLContext:ctx pixelFormat:pf forLayerTime:t displayTime:ts];
}
```


### Renderer Changes

Restrictions on the size of layer images have been removed. (In OS X v10.5 images are silently ignored when they are larger than the maximum texture size of the current graphics card.)

Sibling layers that intersect in 3D space are now rendered correctly—intersecting layers are resolved into multiple non-intersecting fragments before being rendered (i.e. compositing and background filters will be applied in the correct order.)

### Animating Your Own Properties

Animating custom layer properties is now supported. Override [needsDisplayForKey:](https://developer.apple.com/documentation/quartzcore/calayer/1410769-needsdisplayforkey): to mark the properties your layer subclass uses to draw its contents. Animations targeting those properties will then cause your [drawInContext:](https://developer.apple.com/documentation/quartzcore/calayer/1410757-draw) method to be called on a copy of the layer containing the current animation values.

### WWDC 2007 Seed

### Deprecated API

The [CAMediaTiming](https://developer.apple.com/documentation/quartzcore/camediatiming) constant [kCAFillModeFrozen](https://developer.apple.com/documentation/quartzcore/camediatiming/fill_modes/kcafillmodefrozen) has been deprecated and replaced by `kCAFillModeForwards`. See [New API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenjyfvbuqmjnknlte) for more information.

### New API

New API has been added to several Core Animation classes.

### New Getter Methods

The Core Animation API now uses the `is`_Property_ accessor pattern for Boolean properties. The affected classes and the new getters are:

- CAAnimation

  - isRemovedOnCompletion
  - isAdditive
  - isCumulative
- CIFilterAdditions

  - isEnabled
- CALayer

  - isHidden
  - isDoubleSided
  - isOpaque
- CAOpenGLLayer

  - isAsynchronous
- CATextLayer

  - isWrapped

### CAMediaTiming class

The following API has been added to [CAMediaTiming](https://developer.apple.com/documentation/quartzcore/camediatiming):

```objc

@protocol CAMediaTiming

/* Deprecate kCAFillModeFrozen. Replace with: */

CA_EXTERN NSString * const kCAFillModeForwards;
CA_EXTERN NSString * const kCAFillModeBackwards;
CA_EXTERN NSString * const kCAFillModeBoth;

/* `forwards' is equivalent to existing `frozen', `backwards' clamps time
 * values before zero to zero, `both' clamps time values at both ends
 * of the object's time space. */

@end
```


### CAKeyframeAnimation

The following API has been added to [CAKeyframeAnimation](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation):

```objc

@interface CAKeyframeAnimation

/* Defines whether objects animating along paths rotate to match the
 * path tangent. Possible values are `auto' and `autoReverse'. Defaults
 * to nil. The effect of setting this property to a non-nil value when
 * no path object is supplied is undefined. `autoReverse' rotates to
 * match the tangent plus 180 degrees. */

@property(copy) NSString *rotationMode;

CA_EXTERN NSString * const kCAAnimationRotateAuto;
CA_EXTERN NSString * const kCAAnimationRotateAutoReverse;

@end
```


### CATiledLayer

The following new API has been added to [CATiledLayer](https://developer.apple.com/documentation/quartzcore/catiledlayer):

```objc

@interface CATiledLayer

/* The time in seconds that newly added images take to "fade-in" to the
 * rendered representation of the tiled layer. The default implementation
 * returns 0.25 seconds. */

+ (CFTimeInterval)fadeDuration;

@end
```


### CALayer

The following new API has been added to [CALayer](https://developer.apple.com/documentation/quartzcore/calayer):

```objc

@interface CALayer

/* Returns a copy of the layer containing all properties as they were
 * at the start of the current transaction, with any active animations
 * applied. This gives a close approximation to the version of the layer
 * that is currently displayed.
 *
 * The effect of attempting to modify the returned layer in any way is
 * undefined.
 *
 * The `sublayers', `mask' and `superlayer' properties of the returned
 * layer return the presentation versions of these properties. This
 * carries through to read-only layer methods. E.g., calling -hitTest:
 * on the result of the -presentationLayer will query the presentation
 * values of the layer tree. */

- (id)presentationLayer;

/* When called on the result of the -presentationLayer method, returns
 * the underlying layer with the current model values. The result of
 * calling this method after the transaction that produced the
 * presentation layer has completed is undefined. */

- (id)modelLayer;

/* This initializer is used to create shadow copies of layers, e.g.
 * for the -presentationLayer method. Subclasses can optionally copy
 * their instance variables into the new object. Subclasses should
 * always invoke the superclass implementation; calling this method in
 * any other situations will produce undefined behavior. */

- (id)initWithLayer:(id)layer;

/* Returns the animation added to the layer with identifier 'key', or nil
 * if no such animation exists. Attempting to modify any properties of
 * the returned object will result in undefined behavior. */

- (CAAnimation *)animationForKey:(NSString *)key;

/* A rectangle in the unit coordinate space defining the subrectangle
 * of the `contents' property that will be drawn into the layer. If
 * pixels outside the unit rectangles are requested, the edge pixels of
 * the contents image will be extended outwards. If an empty rectangle
 * is provided, the results are undefined. Defaults to the unit
 * rectangle [0 0 1 1]. Animatable. */

@property CGRect contentsRect;

/* A bitmask defining how the edges of the layer are rasterized. For
 * each of the four edges (left, right, bottom, top) if the
 * corresponding bit is set the edge will be antialiased. Typically
 * this property is used to disable antialiasing for edges that abut
 * edges of other layers, to eliminate the seams that would otherwise
 * occur. The default value is for all edges to be antialiased. */

enum CAEdgeAntialiasingMask
{
  kCALayerLeftEdge    = 1U << 0,
  kCALayerRightEdge    = 1U << 1,
  kCALayerBottomEdge    = 1U << 2,
  kCALayerTopEdge    = 1U << 3,
};

@property unsigned int edgeAntialiasingMask;

/** Layer `contentsGravity' values. **/

/* Similar to kCAGravityResizeAspect except that it resizes the contents
 * of the layer to fill the bounds (while preserving its aspect ratio.) */

CA_EXTERN NSString * const kCAGravityResizeAspectFill;

@end
```


### March Seed

### Core Animation API Renaming

In OS X V10.5 release 365 and later the Core Animation API has undergone a significant renaming. The earlier API will be maintained temporarily for compatibility; it will be removed in a future seed. You must update your projects to use the new API names before Leopard is released.

Table 1-1 details the mapping of old class and protocol names to the new naming scheme.

__Table 1-1__New Core Animation class names

| Original Class/Protocol Name | New Class/Protocol Name |
| --- | --- |
| LKAction | CAAction |
| LKAnimation | CAAnimation |
| LKAnimationGroup | CAAnimationGroup |
| LKBasicAnimation | CABasicAnimation |
| LKConstraint | CAConstraint |
| LKConstraintLayoutManager | CAConstraintLayoutManager |
| LKConstraintManager | CAConstraintManager |
| LKKeyframeAnimation | CAKeyframeAnimation |
| LKLayer | CALayer |
| LKLayoutManager | CALayoutManager |
| LKOpenGLLayer | CAOpenGLLayer |
| LKPropertyAnimation | CAPropertyAnimation |
| LKScrollLayer | CAScrollLayer |
| LKTextLayer | CATextLayer |
| LKTiledLayer | CATiledLayer |
| LKTiming | CAMediaTiming |
| LKTimingFunction | CAMediaTimingFunction |
| LKTransaction | CATransaction |
| LKTransition | CATransition |

The `LKObject` protocol has been deprecated. The methods that were exposed have now been directly added to the `CAAnimation` and `CALayer` classes. The key-value coding extensions that were documented in the `LKObject` reference have been temporarily added to _[Core Animation Programming Guide](../../documentation/Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmju)_.

The `LKTransform` stuct has been renamed `CATransform3D`. The related `LKTransform*` functions have been renamed accordingly.

The `LKCurrentAbsoluteTime()` function has been renamed `CACurrentMediaTime()`.

The constants exposed using the prefix `kLK*` have all been renamed `kCA*`.

### New Classes and Properties

Two new classes have been added to Core Animation: [CATiledLayer](https://developer.apple.com/documentation/quartzcore/catiledlayer) and [CARenderer](https://developer.apple.com/documentation/quartzcore/carenderer). The `CATiledLayer` class allows you to provide content incrementally. The `CARenderer` class allows you to render an animation into a Core OpenGL context directly.

Several new properties have been added to the [CALayer](https://developer.apple.com/documentation/quartzcore/calayer) class. The `minification` and `magnification` properties allow you to specify a filter to use when scaling the content of a layer. The `anchorPoint` property allows you to specify the location in a layer around which transforms are applied.
