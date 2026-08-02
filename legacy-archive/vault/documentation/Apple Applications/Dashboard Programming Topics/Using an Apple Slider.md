---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/AppleSlider.html
archived_at: '2026-07-15T05:17:18.923460Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashboard Programming Topics](Introduction%20to%20Dashboard%20Programming%20Topics.md)


[Next](Using%20Animation.md)[Previous](Using%20Scroll%20Areas.md)

# Using an Apple Slider

Apple provides a JavaScript class that functions as a slider control, useful for depicting a range of values that a user can select between. The class that provides this, `AppleSlider`, is one of the Apple Classes included in OS X v10.4.3 and later.

For more on using all of the Apple Classes, including `AppleSlider`, read [Introduction to the Apple Classes](Introduction%20to%20the%20Apple%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobwfvjvomi).

To use an `AppleSlider`, you need to:

- Include the `AppleSlider` class in your HTML file
- Provide a `<div>` element in your HTML to represent your slider
- Declare an `onload` handler, a JavaScript function called when your widget loads that constructs an `AppleSlider` object
- Place the slider using CSS
- Construct your slider using the `AppleSlider` class in JavaScript

By default, the `AppleSlider` uses artwork supplied by Apple to represent the various parts of the slider. It is possible to provide your own artwork as well.

There are two types of sliders available to you: vertical and horizontal. You should take into account which type of slider you want to use when designing and coding your widget. Both are subclasses of the `AppleSlider` class, and are used in JavaScript to construct the type of slider you want to use.

__Figure 26__  A horizontal slider created from the `AppleSlider` class

!

In order to declare an `AppleSlider` and to use it in JavaScript, you need to include the class in your widget's HTML file, provide a `<div>` that represents your slider in your widget's structure, and have an `onload` handler that's called when your widget's HTML is loaded; the handler is used in JavaScript to construct the `AppleSlider`.

First, you need to include the `AppleSlider` class in your main HTML file. If you're planning backward compatibility with pre-OS X v.10.4.3 versions, follow the directions in [Backwards Compatible Usage](Introduction%20to%20the%20Apple%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobwfvjvomq) and include this path:

```
<script type='text/javascript' src='AppleClasses/AppleSlider.js' charset='utf-8'/>
```

If you plan on requiring OS X v.10.4.3 or newer for your widget, include the `AppleSlider` class in its location in `/System/Library/WidgetResources/`:

```
<script type='text/javascript' src='/System/Library/WidgetResources/AppleClasses/AppleSlider.js' charset='utf-8'/>
```

Once you've included the `AppleSlider` class, you also need to declare a `<div>` element to represent the slider:

```
<body onload="setup();">
    ...
    <div id="mySlider"></div>
    ...
</body>
```

Typically, this entails using a `<div>` element somewhere in the `<body>` portion of your HTML. The only attribute required of this element is an `id`, which is used by CSS to position the slider and by JavaScript to construct the slider. The `id` attribute is required over the `class` attribute, because elements with `id` attributes can be accessed via JavaScript.

Also note the declaration of an `onload` handler within the `<body>` tag. This handler is called when your widget's HTML is loaded. It's used to construct the `AppleSlider` object in your JavaScript, as discussed in [An Apple Slider, in JavaScript](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenbsfvjvomi).

Now that the slider is properly declared in your HTML file, you need to position it in your CSS. This entails including a style with the element's name and any other placement parameters you see fit to use:

```
#mySlider {
    position: absolute;
    top: 20px;
    left: 20px;
    width: 100px;    /* use height for vertical sliders */
}
```

Of particular note here is the `width` attribute, which is needed for horizontal sliders. If you plan on using a vertical slider, specify a `height` attribute instead.

In your HTML file, you included an `onload` handler as an attribute of the `<body>` tag. That handler is called once Dashboard has loaded your widget's HTML file and is used to call the constructor for an `AppleSlider` subclass. Based on which type of slider you are using, you call the constructor for either an `AppleVerticalSlider` or `AppleHorizontalSlider`. The constructors are defined as:

__Table 6__  `AppleSlider` Subclasses

| Horizontal Slider Constructor | Vertical Slider Constructor |
| `AppleHorizontalSlider(slider, onchanged)` | `AppleVerticalSlider(slider, onchanged)` |

Both constructors take in two parameters: at DOM object that represents where the slider should be built, and a handler, called when the value of the slider changes. The DOM object is the `<div>` that you defined in your HTML and placed in your CSS. For a horizontal slider, your `onload` handler code looks like:

```
var gMySlider;

function setup()
{
    gMySlider = new AppleHorizontalSlider(
        document.getElementById("mySlider"),
        sliderChanged
    );
}
```

The `onchanged` handler is a function that you provide. It is called when the slider is changed and should take one argument. When your handler is called, it's passed the current value of the slider. The value of a slider is always a floating point number between 0 and 1.

```
function sliderChanged(currentValue)
{
    // Do something with the currentValue passed in
}
```

Note the global variable `gMySlider`, used in the `setup()` function. This variable holds a reference to your `AppleSlider` object, which lets you interact with the slider at any point after it's been constructed. These properties and methods are available for you to interact with:

__Table 7__  `AppleSlider` object properties and methods

| Option | Type | Explanation |
| `gMySlider.onchanged` | Property | Read/Write; the handler called when the slider is moved |
| `gMySlider.continuous` | Property | Read/Write; a boolean that specifies if the onchanged handler is called while the slider thumb is moving (`true`) or only when its movement is finished (`false`); default is `true` |
| `gMySlider.padding` | Property | Read/Write; an integer that specifies the padding, in pixels, around the slider control within the bounds of the `<div>` element containing it |
| `gMySlider.value` | Property | Read only; the current value of the slider |
| `gMySlider.size` | Property | Read only; the height or width of the slider, in pixels |
| `gMySlider.trackStartPath` | Property | Read only; the path to the current image used for the left end of a horizontal slider's track or the top end of a vertical slider's track |
| `gMySlider.trackStartLength` | Property | Read only; if used on a horizontal slider, the width of the image specified as `trackStartPath` ; if vertical, the height of the image specified as `trackStartPath` |
| `gMySlider.trackMiddlePath` | Property | Read only; the path to the current image used middle of the slider's track |
| `gMySlider.trackEndPath` | Property | Read only; the path to the current image used for the right end of a horizontal slider's track or the bottom end of a vertical slider's track |
| `gMySlider.trackEndLength` | Property | Read only; if used on a horizontal slider, the width of the image specified as `trackEndPath` ; if vertical, the height of the image specified as `trackEndPath` |
| `gMySlider.thumbPath` | Property | Read only; the path to the current image used for the slider's thumb |
| `gMySlider.thumbLength` | Property | Read only; if used on a horizontal slider, the width of the image specified as `thumbPath` ; if vertical, the height of the image specified as `thumbPath` |
| `gMySlider.remove()` | Method | Remove the slider from the widget's user interface and the DOM |
| `gMySlider.refresh()` | Method | Redraws the slider's components; use when you change any aspect of the slider's display or state programmatically |
| `gMySlider.slideTo(position)` | Method | Moves the slider's thumb to `position`; takes an integer, in pixels, in the range of 0 and the height (if vertical) or width (if horizontal) of the slider |
| `gMySlider.setSize(size)` | Method | Sets the slider's width (if horizontal) or height (if vertical) to `size`, in pixels; takes an integer |
| `gMySlider.setTrackStart(imagePath, length)` | Method | Sets the image and width, in pixels, of the left end of a horizontal slider's track, or the image and width, in pixels, of the top end of a vertical slider's track |
| `gMySlider.setTrackMiddle(imagePath)` | Method | Sets image used for the middle portion of a slider's track |
| `gMySlider.setTrackEnd(imagePath, length)` | Method | Sets the image and width, in pixels, of the right end of a horizontal slider's track, or the image and width, in pixels, of the bottom end of a vertical slider's track |
| `gMySlider.setThumb(imagePath, length)` | Method | Sets image and width, in pixels, of the thumb on a horizontal slider, or the image and height, in pixels, of the thumb on a vertical slider |
| `gMySlider.setValue(value)` | Method | Sets the value of the slider and moves its thumb to `value`; takes a floating point number between 0 and 1. |

[Next](Using%20Animation.md)[Previous](Using%20Scroll%20Areas.md)

