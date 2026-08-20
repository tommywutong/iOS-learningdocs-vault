---
title: Safari HTML5 Canvas Guide
apple_id: TP40010542
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/HTML-canvas-guide/AddingShadows/AddingShadows.html
archived_at: '2026-07-15T05:21:02.754239Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Canvas Guide](About%20Canvas.md)


[Next](Translation%2C%20Rotation%2C%20and%20Scaling.md)[Previous](Adding%20Text.md)

# Adding Shadows

Any visual element—a shape, a line, text, or an image—can be given a shadow. You can set the shadow color, the x and y offsets from the source, and set a Gaussian blur to make the shadow more realistic.

Even though the canvas drawing surface is 2D, careful use of shadows can create a sense of a third dimension, with elements seeming to lift off the page.

Shadows work well with SVG, PNG, or GIF images on transparent backgrounds, casting shadows the shape of the nontransparent parts of the images. JPG images cast rectangular shadows, however, even if the image background matches the canvas background.

Shadows from a rectangle, lines, a PNG, a JPG, and text are illustrated in Figure 6-1.

__Figure 6-1__  Shadows

!

Enable shadows by setting the context’s `shadowColor` property to a nontransparent color—for example, `ctx.shadowColor = "black";`. The shadow color must be a CSS color. It cannot be a gradient or pattern.

Disable shadows by setting the `shadowColor` to any RGBa value with an alpha component of 0—for example, `ctx.shadowColor = "rgba(80, 80, 80, 0)";`.

The default x and y offsets of a shadow are zero. To make the shadow fall away from the element, set the `shadowOffsetX` and `shadowOffsetY` properties. For example:

`ctx.shadowOffsetX = 5;`

`ctx.shadowOffsetY = 5;`

Once you’ve set the shadow color, and an x or y offset of at least 1, any drawing operation will include a shadow.

You can make shadows more realistic by adding transparency and blur to lighten and soften them.

If you set the `shadowColor` property to an RGBa color with an alpha value less than 1, the shadow is partly transparent, allowing you to see the background, which is darkened by the shadow but not completely obscured. Greater transparency lightens the shadow and mimics softer lighting.

You can make a shadow softer by applying a Gaussian blur. Light from a point source causes sharp shadows. Diffuse lighting throws softer shadows. Set the blur using the context’s `shadowBlur` property. For example: `ctx.shadowBlur=1;`

The default value is 0 (no blur). A blur of 1 is barely noticeable. A blur of 5 is a soft shadow. A blur of 10 makes the shadow a vague blob.

A canvas with four different alpha and blur values is shown in Figure 6-2.

__Figure 6-2__  Shadow hardness

!

Notice that the white background and black text are visible through the shadow, as long as the alpha value is less than 1.

Canvas shadows are not affected by rotation. A real shadow falls from the light source onto the background at the same angle, regardless of an object’s orientation. Canvas shadows mimic this real-wold behavior.

If you set the `shadowOffsetX` and `shadowOffsetY` properties both to 10, for example, the shadow falls down and to the right, no matter what rotation is applied to the context.

The example illustrated in Figure 6-3 rotates a soccer ball at the center of the canvas. A blue rectangle orbits the soccer ball. Notice that the shadows retain their orientation, regardless of the rotation.

__Figure 6-3__  Shadow rotation

A shadow’s size grows or shrinks as the object casting it is scaled up or down, but the `shadowOffsetX` and `shadowOffsetY` properties do not scale with the context. This maintains the shadow angle, mimicking real-world behavior.

[Next](Translation%2C%20Rotation%2C%20and%20Scaling.md)[Previous](Adding%20Text.md)

