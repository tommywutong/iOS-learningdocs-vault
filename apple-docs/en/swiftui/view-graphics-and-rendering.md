---
title: Graphics and rendering modifiers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-graphics-and-rendering
source_url: 'https://developer.apple.com/documentation/swiftui/view-graphics-and-rendering'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-graphics-and-rendering.json'
content_hash: 'sha256:e679f6be14037b0f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md) · [View](view.md)

# Graphics and rendering modifiers

<sub>API Collection</sub>

Affect the way the system draws a view, for example by scaling or masking a view, or by applying graphical effects.

## Overview

Use these view modifiers to apply many of the rendering effects typically associated with a graphics context, like adding masks and creating composites. You can apply these effects to graphical views, like [Shapes](shapes.md), as well as any other SwiftUI view.

When you do need the flexibility of immediate mode drawing in a graphics context, use a [Canvas](canvas.md) view instead. This can be particularly helpful when you want to draw an extremely large number of dynamic shapes — for example, to create particle effects.

For more information about using these effects in your app, see [Drawing and graphics](drawing-and-graphics.md).

## Topics

### Masks and clipping

- [mask(alignment:_:)](<view/mask(alignment___).md>) — Masks this view using the alpha channel of the given view.
- [clipped(antialiased:)](<view/clipped(antialiased_).md>) — Clips this view to its bounding rectangular frame.
- [clipShape(_:style:)](<view/clipshape(__style_).md>) — Sets a clipping shape for this view.
- [containerShape(_:)](<view/containershape(__).md>) — Sets the container shape to use for any container relative shape or concentric rectangle within this view.

### Scale

- [scaledToFill()](<view/scaledtofill().md>) — Scales this view to fill its parent.
- [scaledToFill3D()](<view/scaledtofill3d().md>) — Scales this view to fill its parent.
- [scaledToFit()](<view/scaledtofit().md>) — Scales this view to fit its parent.
- [scaledToFit3D()](<view/scaledtofit3d().md>) — Scales this view to fit its parent.
- [scaleEffect(_:anchor:)](<view/scaleeffect(__anchor_).md>) — Scales this view uniformly by the specified factor, relative to an anchor point.
- [scaleEffect(x:y:anchor:)](<view/scaleeffect(x_y_anchor_).md>) — Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [scaleEffect(x:y:z:anchor:)](<view/scaleeffect(x_y_z_anchor_).md>) — Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [imageScale(_:)](<view/imagescale(__).md>) — Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [aspectRatio(_:contentMode:)](<view/aspectratio(__contentmode_).md>) — Constrains this view’s dimensions to the specified aspect ratio.
- [aspectRatio3D(_:contentMode:)](<view/aspectratio3d(__contentmode_).md>) — Constrains this view’s dimensions to the specified 3D aspect ratio.

### Rotation and transformation

- [rotationEffect(_:anchor:)](<view/rotationeffect(__anchor_).md>) — Rotates a view’s rendered output in two dimensions around the specified point.
- [rotation3DEffect(_:anchor:)](<view/rotation3deffect(__anchor_).md>) — Rotates the view’s content by the specified 3D rotation value.
- [rotation3DEffect(_:axis:anchor:anchorZ:perspective:)](<view/rotation3deffect(__axis_anchor_anchorz_perspective_).md>) — Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [rotation3DEffect(_:axis:anchor:)](<view/rotation3deffect(__axis_anchor_).md>) — Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [rotation3DLayout(_:)](<view/rotation3dlayout(__).md>) — Rotates a view with impacts to its frame in a containing layout
- [rotation3DLayout(_:axis:)](<view/rotation3dlayout(__axis_).md>) — Rotates a view with impacts to its frame in a containing layout
- [perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)](<view/perspectiverotationeffect(__axis_anchor_anchorz_perspective_).md>) — Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [projectionEffect(_:)](<view/projectioneffect(__).md>) — Applies a projection transformation to this view’s rendered output.
- [transformEffect(_:)](<view/transformeffect(__).md>) — Applies an affine transformation to this view’s rendered output.
- [transform3DEffect(_:)](<view/transform3deffect(__).md>) — Applies a 3D transformation to this view’s rendered output.

### Graphical effects

- [blur(radius:opaque:)](<view/blur(radius_opaque_).md>) — Applies a Gaussian blur to this view.
- [opacity(_:)](<view/opacity(__).md>) — Sets the transparency of this view.
- [brightness(_:)](<view/brightness(__).md>) — Brightens this view by the specified amount.
- [contrast(_:)](<view/contrast(__).md>) — Sets the contrast and separation between similar colors in this view.
- [colorInvert()](<view/colorinvert().md>) — Inverts the colors in this view.
- [colorMultiply(_:)](<view/colormultiply(__).md>) — Adds a color multiplication effect to this view.
- [saturation(_:)](<view/saturation(__).md>) — Adjusts the color saturation of this view.
- [grayscale(_:)](<view/grayscale(__).md>) — Adds a grayscale effect to this view.
- [hueRotation(_:)](<view/huerotation(__).md>) — Applies a hue rotation effect to this view.
- [luminanceToAlpha()](<view/luminancetoalpha().md>) — Adds a luminance to alpha effect to this view.
- [shadow(color:radius:x:y:)](<view/shadow(color_radius_x_y_).md>) — Adds a shadow to this view.
- [visualEffect(_:)](<view/visualeffect(__).md>) — Applies effects to this view, while providing access to layout information through a geometry proxy.
- [visualEffect3D(_:)](<view/visualeffect3d(__).md>) — Applies effects to this view, while providing access to layout information through a 3D geometry proxy.
- [materialActiveAppearance(_:)](<view/materialactiveappearance(__).md>) — Sets an explicit active appearance for materials in this view.

### Shaders

- [colorEffect(_:isEnabled:)](<view/coloreffect(__isenabled_).md>) — Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [distortionEffect(_:maxSampleOffset:isEnabled:)](<view/distortioneffect(__maxsampleoffset_isenabled_).md>) — Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [layerEffect(_:maxSampleOffset:isEnabled:)](<view/layereffect(__maxsampleoffset_isenabled_).md>) — Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.

### Composites

- [blendMode(_:)](<view/blendmode(__).md>) — Sets the blend mode for compositing this view with overlapping views.
- [compositingGroup()](<view/compositinggroup().md>) — Wraps this view in a compositing group.
- [drawingGroup(opaque:colorMode:)](<view/drawinggroup(opaque_colormode_).md>) — Composites this view’s contents into an offscreen image before final display.

### Animations

- [animation(_:)](<view/animation(__).md>) — Applies the given animation to this view when this view changes.
- [animation(_:value:)](<view/animation(__value_).md>) — Applies the given animation to this view when the specified value changes.
- [animation(_:body:)](<view/animation(__body_).md>) — Applies the given animation to all animatable values within the `body` closure.
- [contentTransition(_:)](<view/contenttransition(__).md>) — Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [geometryGroup()](<view/geometrygroup().md>) — Isolates the geometry (e.g. position and size) of the view from its parent view.
- [keyframeAnimator(initialValue:repeating:content:keyframes:)](<view/keyframeanimator(initialvalue_repeating_content_keyframes_).md>) — Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [keyframeAnimator(initialValue:trigger:content:keyframes:)](<view/keyframeanimator(initialvalue_trigger_content_keyframes_).md>) — Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [matchedGeometryEffect(id:in:properties:anchor:isSource:)](<view/matchedgeometryeffect(id_in_properties_anchor_issource_).md>) — Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [matchedTransitionSource(id:in:)](<view/matchedtransitionsource(id_in_).md>) — Identifies this view as the source of a navigation transition, such as a zoom transition.
- [matchedTransitionSource(id:in:configuration:)](<view/matchedtransitionsource(id_in_configuration_).md>) — Identifies this view as the source of a navigation transition, such as a zoom transition.
- [phaseAnimator(_:content:animation:)](<view/phaseanimator(__content_animation_).md>) — Animates effects that you apply to a view over a sequence of phases that change continuously.
- [phaseAnimator(_:trigger:content:animation:)](<view/phaseanimator(__trigger_content_animation_).md>) — Animates effects that you apply to a view over a sequence of phases that change based on a trigger.
- [transition(_:)](<view/transition(__).md>) — Associates a transition with the view.
- [transaction(_:)](<view/transaction(__).md>) — Applies the given transaction mutation function to all animations used within the view.
- [transaction(value:_:)](<view/transaction(value___).md>) — Applies the given transaction mutation function to all animations used within the view.
- [transaction(_:body:)](<view/transaction(__body_).md>) — Applies the given transaction mutation function to all animations used within the `body` closure.

## See Also

### Drawing views

- [Style modifiers](view-style-modifiers.md) — Apply built-in styles to different types of views.
- [Layout modifiers](view-layout.md) — Tell a view how to arrange itself within a view hierarchy by adjusting its size, position, alignment, padding, and so on.
