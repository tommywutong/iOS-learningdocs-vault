---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/Resizing.html
archived_at: '2026-07-15T05:17:30.927427Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashboard Programming Topics](Introduction%20to%20Dashboard%20Programming%20Topics.md)


[Next](Drawing%20Content.md)[Previous](Declaring%20Control%20Regions.md)

# Resizing Widgets

Widgets can be resized to fit content. Resizing your widget may be appropriate if your content scales well or if it has varying degrees of detail to display. You can resize to fixed dimensions (for instance, a "More Information" mode) or provide a resize thumb control for live resizing.

There are two ways to resize your widget: relatively and absolutely.

To resize your widget relative to its current size, use the method `window.resizeBy(width, height)`. This method takes the current size of your widget and adds the values found within the _width_ and _height_ parameters. Note that these values may be negative, allowing you to shrink the size of your widget.

The other way to resize your widget is to specify the absolute size the widget should be. To do this, use the method `window.resizeTo(width, height)`.

Live resizing means that your widget can change its size and contents based on the user's preference. Try to limit using live-resizing to cases where it is absolutely necessary. If your content can be shown in a fixed, simple user interface, do so.

To enable live resizing, you need to provide a resize control and an event handler for when it is clicked upon:

```
    <img id='resize' src='/System/Library/WidgetResources/resize.png' onmousedown='mouseDown(event);'/>
```

Also, the resize control is placed in the bottom-right corner of the widget using CSS in your style sheet:

```
#resize {
    position:absolute;
    top: 208px;
    right: 2px;
    -apple-dashboard-region: dashboard-region(control rectangle);
}
```

In your JavaScript file, include this code:

```
var growboxInset;

function mouseDown(event)
{

    document.addEventListener("mousemove", mouseMove, true);
    document.addEventListener("mouseup", mouseUp, true);

    growboxInset = {x:(window.innerWidth - event.x), y:(window.innerHeight - event.y)};

    event.stopPropagation();
    event.preventDefault();
}

function mouseMove(event)
{

    var x = event.x + growboxInset.x;
    var y = event.y + growboxInset.y;

    document.getElementById("resize").style.top = (y-12);
    window.resizeTo(x,y);

    event.stopPropagation();
    event.preventDefault();
}


function mouseUp(event)
{
    document.removeEventListener("mousemove", mouseMove, true);
    document.removeEventListener("mouseup", mouseUp, true);

    event.stopPropagation();
    event.preventDefault();
}
```

The three functions in this code handle the different mouse events that happen during a drag. First, `mouseDown` is called when the resize control is clicked upon. It records the initial placement of the click in `lastPos` and registers two handlers for the when the mouse moves and the mouse click ends.

Next, `mouseMove` is called every time the mouse is moved any distance. The code as listed here has no constraints, meaning that the widget can be as large or small as the user wants. If you have size constraints on your widget, add them here.

Finally, `mouseUp` is called when the mouse click ends. It removes itself and the `mouseMove` function as handlers. If you don’t do this, these functions are still called whenever a mouse moves or a click ends.

Depending on how your widget resizes and in which directions, you may need to adjust the placement of your widget’s close box. The `setCloseBoxOffset` method gives you the ability to do this:

```
widget.setCloseBoxOffset(x,y);
```

The `x` and `y` coordinates that you provide are in relation to the top-left corner of the widget, where the values `0,0` places the center of the close box over the actual top-left corner of the widget window. The `x` and `y` values can not be larger than 100.

[Next](Drawing%20Content.md)[Previous](Declaring%20Control%20Regions.md)

