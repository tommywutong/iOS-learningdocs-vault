---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/AppleScrollArea.html
archived_at: '2026-07-15T05:17:18.542931Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashboard Programming Topics](Introduction%20to%20Dashboard%20Programming%20Topics.md)


[Next](Using%20an%20Apple%20Slider.md)[Previous](Introduction%20to%20the%20Apple%20Classes.md)

# Using Scroll Areas

Apple provides JavaScript classes that allow you to declare a scroll area and associated scroll bars. The classes that provide this, `AppleScrollArea` and `AppleScrollbar`, are two of the Apple Classes included in OS X v10.4.3 and later.

For more on using all of the Apple Classes, including `AppleScrollArea` and `AppleScrollbar`, read [Introduction to the Apple Classes](Introduction%20to%20the%20Apple%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobwfvjvomi).

To use scroll areas, you need to:

- Include the `AppleScrollArea` and `AppleScrollbar` classes in your HTML file
- Provide a `<div>` element in your HTML for the scrollable content
- Provide a `<div>` element in your HTML for the scroll bar
- Declare an `onload` handler, a JavaScript function called when your widget loads that constructs `AppleScrollArea` and `AppleScrollbar` objects
- Place the content and scroll bar `<div>` elements using CSS
- Construct your scroll area and scroll bars using the `AppleScrollArea` and `AppleScrollbar` classes in JavaScript

By default, the `AppleScrollbar` uses artwork supplied by Apple to represent the various parts of the scroll bar. It is possible to provide your own artwork as well.

There are two types of scroll bars available to you: vertical and horizontal. You should take into account which type of scroll bar you want to use when designing and coding your widget. Both are subclasses of the `AppleScrollbar` class and are used in JavaScript to construct the type of scroll bar you want to use. Figure 25 shows an example of a standard vertical scroll bar inside a scroll area (the entire white area is the scroll area).

__Figure 25__  A vertical scroll bar created from the `AppleScrollbar` class

!

In order to declare a scroll area and to use it in JavaScript, you need to include the `AppleScrollArea` and `AppleScrollbar` classes in your widget's HTML file, provide `<div>` elements that represent your scrollable content and your scroll bars in your widget's structure, and have an `onload` handler that's called when your widget's HTML is loaded. The handler is used in JavaScript to construct the scroll areas and scroll bars.

First, you need to include the `AppleScrollArea` and `AppleScrollbar` classes in your main HTML file. If you're planning backward compatibility with pre-OS X v.10.4.3 versions, follow the directions in [Backwards Compatible Usage](Introduction%20to%20the%20Apple%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobwfvjvomq) and include this path:

```
<script type='text/javascript' src='AppleClasses/AppleScrollArea.js' charset='utf-8'/>
<script type='text/javascript' src='AppleClasses/AppleScrollbar.js' charset='utf-8'/>
```

If you plan on requiring OS X v.10.4.3 or newer for your widget, include the `AppleScrollArea` and `AppleScrollbar` classes from their location in `/System/Library/WidgetResources/`:

```
<script type='text/javascript' src='/System/Library/WidgetResources/AppleClasses/AppleScrollArea.js' charset='utf-8'/>
<script type='text/javascript' src='/System/Library/WidgetResources/AppleClasses/AppleScrollbar.js' charset='utf-8'/>
```

Once you've included the `AppleScrollArea` and `AppleScrollbar` classes, you also need to declare `<div>` elements for your scrollable content and a scroll bar:

```
<body onload="setup();">
    ...
    <div id="myScrollArea">...</div>
    <div id="myScrollbar"></div>
    ...
</body>
```

The only attribute required of either `<div>` element is an `id`, which is used by CSS to position scroll area and scroll bar, and by JavaScript to construct them. The `id` attribute is required over the `class` attribute because elements with `id` attributes can be accessed via JavaScript.

Also note the declaration of an `onload` handler within the `<body>` tag. This handler is called when your widget's HTML is loaded. It's used to construct the `AppleScrollArea` and `AppleScrollbar` objects in your JavaScript, as discussed in [Scroll Areas and Scroll Bars, in JavaScript](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenbrfvjvomi).

Now that the scroll area and scroll bar are properly declared in your HTML file, you need to position them in your CSS. This entails including a style with the element's name and any other placement parameters you see fit to use:

```
#myScrollArea {
    position: absolute;
    top: 10px;
    bottom: 10px;
    left: 10px;
    right: 30px;
}
#myScrollbar {
    position: absolute;
    top: 10px;
    bottom: 10px;
    right: 10px;
    width: 19px;
}
```

Note the scroll bar's `width` attribute. A value of `19px` is used here because the default artwork provided by Apple for the scroll bar is 19 pixels wide. If you are providing custom artwork for a scroll bar, use the width of your artwork instead.

If your scroll area is using a horizontal scroll bar, use the `height` attribute in place of the `width` attribute. If you are using the artwork provided by Apple, specify scroll bar heights as 19 pixels.

In your HTML file, you included an `onload` handler as an attribute of the `<body>` tag. That handler is called once Dashboard has loaded your widget's HTML file and is used to call the constructors for the `AppleScrollArea` class and an `AppleScrollbar` subclass. First, you construct the scroll bar.

Based on which type of scroll bar you are using, you call the constructor for either an `AppleHorizontalScrollbar` or `AppleVerticalScrollbar`. The constructors are defined as:

__Table 3__  `AppleScrollbar` Subclasses

| Horizontal Scroll Bar Constructor | Vertical Scroll Bar Constructor |
| `AppleHorizontalScrollbar(scrollbar)` | `AppleVerticalScrollbar(scrollbar)` |

Both constructors take in a DOM object that represents where the scroll bar should be built. The DOM object is the `<div>` that you defined in your HTML and placed in your CSS.

The `AppleScrollArea` constructor also takes in a DOM object. This is the `<div>` specified in your HTML as the scrollable content:

```
AppleScrollArea(content)
```

In your JavaScript, your `onload` handler needs to use the `AppleScrollArea` constructor and the constructor for a subclass of `AppleScrollbar`. For a vertical scroll bar, your `onload` handler code looks like:

```
var gMyScrollArea, gMyScrollbar;

function setup()
{
    gMyScrollbar = new AppleVerticalScrollbar(
        document.getElementById("myScrollbar")
    );

    gMyScrollArea = new AppleScrollArea(
        document.getElementById("myScrollArea")
    );

    gMyScrollArea.addScrollbar(gMyScrollbar);
}
```

In the last line of the `setup()` function, the `addScrollbar` method is called. This associates the constructed scroll bar with the scroll area, meaning that any interaction on the scroll bar effects the associated scroll area.

You can associate scroll areas and scroll bars via `addScrollbar` or you can add them as additional arguments to the `AppleScrollArea` constructor:

```
AppleScrollArea(content, scrollbar, ...)
```

The `AppleScrollArea` constructor can accept any number of scroll bars.

These methods and properties are also available to `AppleScrollArea` objects and allow you to modify its behavior:

__Table 4__   `AppleScrollArea` object properties and methods

| Option | Type | Explanation |
| `gMyScrollArea.scrollsVertically` | Property | Read/Write; determines if the scroll area scrolls vertically |
| `gMyScrollArea.scrollsHorizontally` | Property | Read/Write; determines if the scroll area scrolls horizontally |
| `gMyScrollArea.singlepressScrollPixels` | Property | Read/Write; the number of pixels the scroll area scrolls when an arrow key is pressed |
| `gMyScrollArea.viewHeight` | Property | Read only; the height of the scroll area |
| `gMyScrollArea.viewToContentHeightRatio` | Property | Read only; the ratio of the height of the view versus the total amount of content shown |
| `gMyScrollArea.viewWidth` | Property | Read only; the width of the scroll area |
| `gMyScrollArea.viewToContentWidthRatio` | Property | Read only; the ratio of the width of the view versus the total amount of content shown |
| `gMyScrollArea.addScrollbar(scrollbar)` | Method | Associates a scroll bar with a scroll area |
| `gMyScrollArea.removeScrollbar(scrollbar)` | Method | Disassociates a scroll bar and scroll area |
| `gMyScrollArea.remove()` | Method | Removes the scroll area from the widget |
| `gMyScrollArea.refresh()` | Method | Redraws the scroll area's scroll bars; call whenever a content change happens |
| `gMyScrollArea.reveal(element)` | Method | Accepts a DOM element; scrolls the view to make the element visible |
| `gMyScrollArea.focus()` | Method | Gives the scroll area key focus; scroll area responds to key events made while widget is in focus |
| `gMyScrollArea.blur()` | Method | Removes key focus from the scroll area; scroll area no longer responds to key events |
| `gMyScrollArea.verticalScrollTo(position)` | Method | Accepts an integer; moves the content within the scroll area to `position` |
| `gMyScrollArea.horizontalScrollTo(position)` | Method | Accepts an integer; moves the content within the scroll area to `position` |

Additionally, any object that subclasses `AppleScrollbar` has these methods and properties available:

__Table 5__  `AppleScrollbar` object properties and methods

| Option | Type | Explanation |
| `gMyScrollbar.minThumbSize` | Property | Read/Write; the smallest scroller thumb size allowed |
| `gMyScrollbar.padding` | Property | Read/Write; the padding on the scroll bar |
| `gMyScrollbar.autohide` | Property | Read only; reflects if the scroll bar is always shown or only when there is scrollable content |
| `gMyScrollbar.hidden` | Property | Read only; `TRUE` if the scroll bar is hidden, `FALSE` if it shown |
| `gMyScrollbar.size` | Property | Read only; the height of a vertical scroll bar or the width of a horizontal scroll bar, in pixels |
| `gMyScrollbar.trackStartPath` | Property | Read only; the path to the current image used for the left end of a horizontal scroll bar's track or the top end of a vertical scroll bar's track |
| `gMyScrollbar.trackStartLength` | Property | Read only; if used on a horizontal scroll bar, the width of the image specified as `trackStartPath` ; if vertical, the height of the image specified as `trackStartPath` |
| `gMyScrollbar.trackMiddlePath` | Property | Read only; the path to the current image used middle of the scroll bar's track |
| `gMyScrollbar.trackEndPath` | Property | Read only; the path to the current image used for the right end of a horizontal scroll bar's track or the bottom end of a vertical scroll bar's track |
| `gMyScrollbar.trackEndLength` | Property | Read only; if used on a horizontal scroll bar, the width of the image specified as `trackEndPath` ; if vertical, the height of the image specified as `trackEndPath` |
| `gMyScrollbar.thumbStartPath` | Property | Read only; the path to the current image used for the left end of a horizontal scroll bar's scroller thumb or the top end of a vertical scroll bar's scroller thumb |
| `gMyScrollbar.thumbStartLength` | Property | Read only; if used on a horizontal scroll bar, the width of the image specified as `thumbStartPath` ; if vertical, the height of the image specified as `thumbStartPath` |
| `gMyScrollbar.thumbMiddlePath` | Property | Read only; the path to the current image used middle of the scroll bar's scroller thumb |
| `gMyScrollbar.thumbEndPath` | Property | Read only; the path to the current image used for the right end of a horizontal scroll bar's scroller thumb or the bottom end of a vertical scroll bar's scroller thumb |
| `gMyScrollbar.thumbEndLength` | Property | Read only; if used on a horizontal scroll bar, the width of the image specified as `thumbEndPath` ; if vertical, the height of the image specified as `thumbEndPath` |
| `gMyScrollbar.remove()` | Method | Removes the scroll bar from the scroll area |
| `gMyScrollbar.setScrollArea(scrollArea)` | Method | Associates a scroll area with a scroll bar |
| `gMyScrollbar.refresh()` | Method | Redraws a scroll bar |
| `gMyScrollbar.setAutohide(display)` | Method | Determines if the scroll bar hides when there is no need for a scroll bar; pass in `TRUE` if you want the scroll bar to hide automatically, `FALSE` if you want it to always remain visible |
| `gMyScrollbar.hide()` | Method | Hides the scroll bar |
| `gMyScrollbar.show()` | Method | Shows the scroll bar |
| `gMyScrollbar.setSize(size)` | Method | Sets the scroll bar's width (if horizontal) or height (if vertical) to `size`, in pixels |
| `gMyScrollbar.setTrackStart(path, size)` | Method | Sets the image and width, in pixels, of the left end of a horizontal scroll bar's track, or the image and height, in pixels, of the top end of a vertical scroll bar's track |
| `gMyScrollbar.setTrackMiddle(path)` | Method | Sets image used for the middle portion of a scroll bar's track |
| `gMyScrollbar.setTrackEnd(path, size)` | Method | Sets the image and width, in pixels, of the right end of a horizontal scroll bar's track, or the image and height, in pixels, of the bottom end of a vertical scroll bar's track |
| `gMyScrollbar.setThumbStart(path, size)` | Method | Sets the image and width, in pixels, of the left end of a horizontal scroll bar's scroller thumb, or the image and width, in pixels, of the top end of a vertical scroll bar's scroller thumb |
| `gMyScrollbar.setThumbMiddle(path)` | Method | Sets image used for the middle portion of a scroll bar's scroller thumb |
| `gMyScrollbar.setThumbEnd(path, size)` | Method | Sets the image and width, in pixels, of the right end of a horizontal scroll bar's scroller thumb, or the image and width, in pixels, of the bottom end of a vertical scroll bar's scroller thumb |

[Next](Using%20an%20Apple%20Slider.md)[Previous](Introduction%20to%20the%20Apple%20Classes.md)

