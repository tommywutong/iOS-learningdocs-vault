---
title: Safari HTML5 Canvas Guide
apple_id: TP40010542
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/HTML-canvas-guide/SettingUptheCanvas/SettingUptheCanvas.html
archived_at: '2026-07-15T05:21:14.797257Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Canvas Guide](About%20Canvas.md)


[Next](Drawing%20Lines%20and%20Shapes.md)[Previous](About%20Canvas.md)

# Setting Up the Canvas

To set up a canvas for drawing, you need to add a `<canvas>` tag to your HTML and assign a 2D drawing context to it. All your drawing operations are performed on the context.

In your HTML, include a line that defines the `canvas` element, giving it a width and height. Be sure to include a closing tag.

`<canvas width="400" height="300">`

`</canvas>`

If you don’t specify a width or height, the default width of 300 pixels and the default height of 150 pixels are used. The canvas is initially empty and transparent.

Put any fallback behavior for older browsers between the opening and closing `<canvas>` tags.

```
<canvas width="400" height="300">
    <img src="fallback.jpg" />
</canvas>
```

HTML5-savvy browsers ignore everything between the opening and closing `<canvas>` tags. Browsers that don’t support the `canvas` element ignore the `<canvas>` tags and display the fallback content.

Using JavaScript, get the `canvas` element into an object and get a `"2d"` drawing context. You perform all drawing operations on the context. Currently, only a `"2d"` context is supported. The canvas specification is designed to support 3D drawing contexts, such as WebGL, in the future.

```
<html>
<head>
    <title>Simple Canvas</title>
    <script type="text/javascript">
        function init() {
            var can = document.getElementById("myCanvas");
            var ctx = can.getContext("2d");
        }
    </script>
</head>
<body onload="init()">
    <canvas id="myCanvas" height="300" width="400">
    </canvas>
</body>
</html>
```


Enabling your canvas to appear crisp on Retina as well as standard-definition displays is as simple as multiplying your canvas instructions by a ratio determined by the screen’s pixel density. First, you need to understand how pixel values are stored in a canvas.

The __backing store__ is where the canvas stores data for each pixel’s color value. The goal is to provide a pixel in the backing store for each display pixel rendered on the canvas. Before the pixels are pushed to the screen, their values are computed here. However, the number of pixels represented in the backing store might not be equal to the number of pixels pushed to the screen. On Retina devices, the canvas width and height is doubled to maintain consistent size and position relative to other HTML elements, and as a result, it stretches and blurs its contents. To counteract this stretching, you need to double the width and height of the backing store when appropriate.

If you are dealing with raster image or video data, find out how to further optimize your canvas for Retina displays in [Pixel Manipulation](Pixel%20Manipulation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmjwfvjvona).

Because a larger canvas may not be advantageous under all circumstances, you need to opt in to optimize your canvas for Retina devices. First, determine whether the display presenting your canvas is indeed of Retina caliber. If it is, scale your backing store by the device pixel ratio.

Retina devices have a pixel ratio of 2 because there is a 2:1 ratio of display pixels to backing store pixels in both the x and y direction. Standard-resolution displays, on the other hand, map one backing store pixel to one display pixel, so their device pixel ratio will always be 1.

You can determine the factor of the backing scale in JavaScript. First, see whether the browser visiting your web page has `window.devicePixelRatio` defined. If the device pixel ratio is greater than 1, the user is on a Retina display. The code for determining the appropriate backing scale is listed in Listing 1-1.

__Listing 1-1__  Determining a backing store multiplier

```
function backingScale(context) {
    if ('devicePixelRatio' in window) {
        if (window.devicePixelRatio > 1) {
            return window.devicePixelRatio;
        }
    }
    return 1;
}
```

You must manually multiply your canvas pixel values by the device pixel ratio as demonstrated in Listing 1-2. Drawing instructions that refer to points in the coordinate space must also be multiplied by this backing scale to ensure your canvas is Retina-ready.

__Listing 1-2__  Scaling a canvas with a backing store multipler

```
var can = document.getElementById("myCanvas");
var ctx = can.getContext("2d");
var scaleFactor = backingScale(ctx);

if (scaleFactor > 1) {
    can.width = can.width * scaleFactor;
    can.height = can.height * scaleFactor;
    // update the context for the new canvas scale
    var ctx = can.getContext("2d");
}
```

For more information regarding how to present images on displays of all resolutions in Safari, read _[Safari Image Delivery Best Practices](../../Networking%20Internet/Safari%20Image%20Delivery%20Best%20Practices/About%20Proper%20Image%20Delivery%20on%20the%20Web.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdinbz)_.

The context is, among other things, where you store settings such as line color, fill color, line thickness, rotation, and scaling.

To draw different elements in different colors or at different rotations, for example, you need to change the context settings.

Instead of setting and resetting large numbers of drawing parameters, it’s easier to save the current context with all its settings, then restore it as needed.

When you save a context, the settings are pushed onto a stack. When you restore a context, the settings are popped off the stack. Saving and restoring contexts is therefore a very fast operation, and is nestable.

You save the current context settings by calling the `save()` method on the context. Restore the previous settings by calling `restore()`.

The following snippet saves the context, changes the rotation, calls a drawing operation, then restores the context.

```
ctx.save();
ctx.rotate(Math.PI);
drawSomething();
ctx.restore();
```

[Next](Drawing%20Lines%20and%20Shapes.md)[Previous](About%20Canvas.md)

