---
title: Safari HTML5 Canvas Guide
apple_id: TP40010542
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/HTML-canvas-guide/AddingText/AddingText.html
archived_at: '2026-07-15T05:21:03.892742Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Canvas Guide](About%20Canvas.md)


[Next](Adding%20Shadows.md)[Previous](Using%20Predrawn%20Images.md)

# Adding Text

The `canvas` element supports basic text rendering on a line-by-line basis. Just enter a line of text and an x,y coordinate for the text box using the `fillText("text", x, y)` or `strokeText("text", x, y)` method. The text is rendered using the current stroke or fill style, which can be a color, gradient, or pattern.

You can specify a number of text settings, such as the font family, size, and weight, and the text alignment and baseline.

For example, the following snippet prints “Figure 1” on the canvas at coordinates 10, 250 in 24-point Helvetica. The default alignment and baseline are used.

```
function drawText() {
    ctx.fillStyle = "blue";
    ctx.font = "24pt Helvetica";
    ctx.fillText("Figure 1", 10, 250);
}
```

Text is not word-wrapped at the boundaries of the canvas. The text box extends automatically to hold the specified text on a single line. You need to create a separate text box for each line of text.

Before you add text to the canvas, you need to set either the fill or stroke style (see [Set the Stroke and Fill Styles](Drawing%20Lines%20and%20Shapes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmznknlto) for details). You probably also want to specify text settings, unless you want to use the browser’s default settings.

You can specify font settings by setting the context’s `font` property. The `font` property is set using the same syntax as the all-in-one CSS `font` property. You can specify any or all of the font settings, space or comma delimited, as appropriate. For example:

`ctx.font = "24pt Helvetica bold, sans-serif"`

specifies a preference for 24-point, bold Helvetica, falling back to a generic sans-serif font if Helvetica is unavailable.

You are not limited to the fonts the user has installed on the host device. The canvas has access to any fonts loaded in your webpage using the CSS `@font-face` property, once the fonts have loaded.

The default text direction is left-to-right. You can change this by setting the canvas `dir` property to `rtl`.

For example, `document.getElementsByTagName('canvas')[0].dir = 'rtl';` would change the text direction of the first `canvas` element to right-to-left.

Possible values for `dir` are `rtl` and `ltr`.

Note that text direction is a standard HTML property, not specific to the canvas, and can be inherited from parent elements such as the document body.

Set the text alignment (sometimes called justification) by setting the context’s `textAlign` property. Possible values are `start`, `end`, `left`, `right`, and `center`.

The `start` and `end` values are the same as the `left` and `right` values, but are dependent on the text direction. If the text direction is left-to-right, `start` is the same as `left`, and if the text direction is right-to-left, `start` is the same as `right`.

The `textAlign` property changes the meaning of the x-coordinate specified in `strokeText("text", x,y)` or `fillText("text", x,y)`. The x-coordinate specifies the left, right, or center of text box, depending on the `textAlign` setting.

Figure 5-1 shows the different text alignment settings applied to text drawn at the same x-coordinate, shown by the red line.

__Figure 5-1__  Text alignment

!

The text baseline is specified by the y-coordinate in `fillText(text, x,y)` or `strokeText(text, x,y)`.

The default text baseline is the `alphabetic` baseline—the bottom of most letters in the roman alphabet (the descender of a lowercase y, p, or q drops below it).

You can change the text baseline by setting the context’s `textBaseline` property. Legal values are:

- `top`
- `hanging`
- `middle`
- `alphabetic`
- `ideographic`
- `bottom`

The position of each baseline value, relative to the bounding box, is shown in Figure 5-2.

__Figure 5-2__  Text baselines

!

The following snippet positions the text baseline so the text is vertically centered in the bounding box.

`ctx.textBaseline = "middle";`

Suppose that your canvas needs to include text that’s supplied at runtime. You might want to break the text into multiple lines, or scale the text, depending on its length, or you might need to position the text relative to a graphic element. To do any of these things, you need to know how large the bounding box for the text would be.

The `measureText()` method takes a string as an argument and returns a metric. The `width` property of the metric is the width in pixels of the needed bounding box with the current font settings.

The following snippet iterates through an array of player names, measures the width of the bounding box needed to hold each name, prints the name, and positions an image ten pixels to the right of the bounding box.

```
for (var i = 0; i < players; i++) {
   var name = playerName[i];
   var metric = measureText(name);
   var edge = metric.width;
   ctx.fillText(name, 0, 50 * i);
   ctx.drawImage(playerIcon, edge + 10, 50 * i);
}
```


The context has two methods for drawing a line of text. Both methods define a text box.

The `fillText(text, x, y [,maxWidth])` method fills the text in the current fill style. The `strokeText(text, x, y [,maxWidth])` method outlines the text in the current stroke style. Both methods accept the same arguments.

The `text` parameter must be a string, and can contain Unicode characters.

The `x` parameter is the alignment point for the text box, as set in the context’s `textAlign` property. The default is the left edge of the text box.

The `y` parameter is the text baseline within the bounding box, as set in the context’s `textBaseline` property. The default setting is `alphabetic`—in line with the bottom of roman letters without descenders.

You can pass in an optional `maxWidth` value, which scales the text, if needed, to fit in a text box no wider than `maxWidth`.

Listing 5-1 displays the text “Hello, world.” in 24-point Helvetica, centered horizontally and vertically, filled in blue on a white background. The result is shown in Figure 5-3.

__Figure 5-3__  Hello world

!

__Listing 5-1__  Drawing “Hello, world.”

```
<html>
<head>
    <title>Hello world</title>
    <script type="text/javascript">
        var can, ctx;

        function init() {
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            drawText();
        }

        function drawText() {
            ctx.fillStyle = "blue";
            ctx.font = "24pt Helvetica";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            ctx.fillText("Hello, world.", can.width / 2 , can.height / 2);
        }
</script>
</head>
<body onload="init()" style="background-color:#000">
    <canvas id="can" height="200" width="400" style="backgroundcolor:#fff">
    </canvas>
</body>
</html>
```


Like any other visual element, text can be rotated, scaled, transformed, and animated.

The usual sequence for animation applies:

1. Clear the canvas.
2. Save the context.
3. Change the context settings.
4. Draw the next frame.
5. Restore the context.

To repeat the animation, the steps are grouped into a function, and the function is called periodically after a suitable delay—using `setInterval()` for endless animations, or `setTimeout()` for animations that repeat conditionally.

When rotating an element, the simplest approach is to follow these steps:

1. Translate the context to the x and y coordinates of the element.
2. Rotate the context.
3. Draw the element, centered at 0,0.

   (For a detailed explanation of why you should follow these steps, see [Rotation](Translation%2C%20Rotation%2C%20and%20Scaling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqobnknlti).)

Listing 5-2, displays the string “Hello, world!” in 48 point Helvetica, filled in blue. The text spins in, starting small and growing to its full size as it spins, as illustrated in Figure 5-4.

__Figure 5-4__  Animated text

To achieve this effect, the text is scaled and rotated repeatedly. The rotation goes from 0 to 2 x Pi radians (0-360°). The animation takes place over a fixed number of steps, so a rotation increment of `2 * Pi / steps` is calculated. A scale increment of `1 / steps` is calculated, so the scale will grow to 1 in steps.

__Listing 5-2__  Animating text

```
<html>
<head>
    <title>Hello world!</title>
    <script type="text/javascript">
        var can, ctx, addAngle, addScale,
            step, steps = 50, delay = 20;

        function init() {
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            addAngle = Math.PI * 2 / steps;
            addScale = 1 / steps;
            step = 0;
            ctx.fillStyle = "blue";
            ctx.font = "48pt Helvetica";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            spinText();
        }

        function spinText() {
            step++;
            ctx.clearRect(0,0, can.width, can.height);
            ctx.save();
            ctx.translate(can.width / 2, can.height / 2);
            ctx.scale(addScale * step, addScale * step);
            ctx.rotate(addAngle * step);
            ctx.fillText("Hello, world!", 0, 0);
            ctx.restore();
            if (step < steps)
                var t = setTimeout('spinText()', delay);
        }
    </script>
</head>
<body onload="init()">
    <canvas id="can" height="200" width="400">
    </canvas>
</body>
</html>
```

[Next](Adding%20Shadows.md)[Previous](Using%20Predrawn%20Images.md)

