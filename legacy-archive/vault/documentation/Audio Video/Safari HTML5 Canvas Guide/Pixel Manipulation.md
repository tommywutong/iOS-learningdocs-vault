---
title: Safari HTML5 Canvas Guide
apple_id: TP40010542
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/HTML-canvas-guide/PixelManipulation/PixelManipulation.html
archived_at: '2026-07-15T05:21:14.777889Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Canvas Guide](About%20Canvas.md)


[Next](Creating%20Games.md)[Previous](Adding%20Sound%20to%20Canvas%20Animations.md)

# Pixel Manipulation

You have direct access to the canvas bitmap as an array of RGBa pixels.

__Table 15-1__  Standard- and high-resolution image functions

| Standard-resolution function call  _(arguments are in CSS pixels)_ | High-resolution equivalent  _(arguments are in backing store pixels)_ |
| `getImageData(x, y, width, height)` | `webkitGetImageDataHD(x, y, width, height)` |
| `putImageData(data, x, y, width, height)` | `webkitPutImageDataHD(data, x, y, width, height)` |

You can get an `imageData` object for any rectangular section of the canvas by calling the context’s `getImageData(x, y, width, height)` method.

The `imageData` object’s `data` property is a one-dimensional array having four values per pixel—red, green, blue, and alpha—expressed as integers from 0-255. The alpha value is quantized to the nearest 1 / 255th, then multiplied by 255. If the first pixel in the array is RGBa (255, 128, 20, 1.0) for example, the first four values in the array are 255, 128, 20, 255.

The pixel array you obtain using the `imageData.data` property is not a copy of the pixel data, but an actual reference to the data. Any changes you make to the pixel array you obtain are also made immediately to the `imageData` object.

You can create additional `imageData` objects by calling the context’s `createImageData()` method. You can pass in either a width and height or another `imageData` object, in which case the new `imageData` object has the same dimensions as the one you pass in.

New `imageData` objects are initialized to transparent black—each pixel in the `imageData` object’s `data` property is represented by four consecutive zeroes.

The following snippet gets the image data for the whole canvas, creates an image buffer, and copies the image data into the new buffer.

```
var theImage = ctx.getImageData(0, 0, can.width, can.height);
var buffer = ctx.createImageData(theImage);
var pixArray = theImage.data;
var bufArray = buffer.data
for (i = 0;i < pixArray.length; i++) {
    bufArray[i] = pixArray[i];
}
```


Modify pixel data on the canvas by assigning an array of pixel values to an `imageData` object’s pixel array and calling the context’s `putImageData()` method.

To blit the entire `imageData` object to the screen, call `putImageData(theImageData, x, y)`, specifying the x and y coordinates of the upper left corner of the rectangle into which you want to blit the image data.

To blit only a subsection of the `imageData` object to the screen, pass in the x, y, width, and height of the subsection as well:

`context.putImageData(imageData, x, y, subX, subY, subWidth, subHeight)`

The subsection is blitted in at `x+subX, y+subY`, just as if you had blitted the whole `imageData` object at x, y.

The example in Listing 15-1 gets an `imageData` object for the entire canvas and creates arrays of red, green, blue, and alpha values from the pixel data. When the Clear Green button is pushed, the example searches for pixels with the RGB value 0, 255, 0 and sets the alpha values for those pixels to 0. A Restore Green button sets the same pixels’ alpha values to 255 (equivalent to RGBa alpha value of 1.0). The result is illustrated in figure Figure 15-1.

__Figure 15-1__  Green clear and restore

__Listing 15-1__  Manipulating pixels

```
<html>
<head>
    <title>Pixel Manipulation</title>
    <script type="text/javascript">
        var can, ctx, theImage, pix,
            red = [], green = [], blue = [], alpha = [];

        function init() {
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            // Fill screen with red, green, and blue stripes.
            ctx.fillStyle = "red";
            ctx.fillRect(0, 0, can.width / 3, can.height);
            ctx.fillStyle = 'rgb(0,255,0)';
            ctx.fillRect(can.width / 3, 0, can.width * 2/3, can.height);
            ctx.fillStyle = "blue";
            ctx.fillRect(can.width * 2 / 3, 0, can.width, can.height);
            // Get pixel data for entire canvas.
            theImage = ctx.getImageData(0, 0, can.width, can.height);
            pix = theImage.data;
            // Separate out red, green, blue, and alpha values.
            // Every four values equals 1 pixel.
            for (i = 0; i < pix.length; i += 4) {
                red[i / 4]   = pix[i];
                green[i / 4] = pix[i + 1];
                blue[i / 4]  = pix[i + 2];
                alpha[i / 4] = pix[i + 3];
            }
        }

        function clearGreen() {
            // Check each pixel's RGB value.
            for (var i = 0, len = can.width * can.height; i < len; i++) {
                if (red[i] == 0 && green[i] == 255 && blue[i] == 0)
                    // Set alpha value for pixel to 0.
                    pix[(i * 4)+ 3] = 0;
            }
             // Blit modified image object to screen.
             ctx.putImageData(theImage,0,0);
        }

        function restoreGreen() {
            for ( var i = 0, len = can.width * can.height; i < len; i++) {
                if (red[i] == 0 && green[i] == 255 && blue[i] == 0)
                    pix[(i * 4) + 3] = 255;
            }
             ctx.putImageData(theImage, 0, 0);
        }
    </script>
</head>
<body onload="init()">
    <canvas id="can" height="200" width="300">
    </canvas>
    <br />
    <input type="button" value="Clear Green" onClick="clearGreen()" />
    <input type="button" value="Restore Green" onClick="restoreGreen()" />
</body>
</html>
```

[Next](Creating%20Games.md)[Previous](Adding%20Sound%20to%20Canvas%20Animations.md)

