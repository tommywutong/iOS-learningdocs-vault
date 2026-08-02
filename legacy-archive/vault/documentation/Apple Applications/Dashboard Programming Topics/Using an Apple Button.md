---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/AppleButton.html
archived_at: '2026-07-15T05:17:17.481160Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashboard Programming Topics](Introduction%20to%20Dashboard%20Programming%20Topics.md)


[Next](Widget%20Backs%20and%20Preferences.md)[Previous](Using%20Animation.md)

# Using an Apple Button

Apple provides a JavaScript class that makes it simple to add custom-styled buttons in your widget's user interface. The class that provides this, `AppleButton`, is one of the Apple Classes included in OS X v10.4.3 and newer.

For more on using all of the Apple Classes, including `AppleButton`, read [Introduction to the Apple Classes](Introduction%20to%20the%20Apple%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobwfvjvomi).

The `AppleButton` class provides all of the standard button behaviors that you expect from a button, including looking depressed when clicked on and sizing based on the button's label width. To use an `AppleButton`, you need to:

- Include the `AppleButton` class in your HTML file
- Provide a `<div>` in your HTML to represent your button
- Declare an `onload` handler, a JavaScript function called when your widget loads that constructs an `AppleButton` object
- Place the button using CSS
- Construct your button using the `AppleButton` class in JavaScript

Once the button has been created, you can also change its parameters in JavaScript. Figure 27 shows two standard versions of the `AppleButton` provided by Dashcode.

__Figure 27__  Two standard button types created from the `AppleButton` class

!

Most developers are interested in using the `AppleButton` class for its `AppleGlassButton` subclass. The `AppleGlassButton` is the standard style button commonly used on widget backs and is discussed in [The Apple Glass Button Subclass](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobvfvjvona).

In order to declare an `AppleButton` and to use it in JavaScript, you need to include the class in your widget's HTML file, provide a `<div>` that represents your button in your widget's structure, and have an `onload` handler that's called when your widget's HTML is loaded; the handler is used in JavaScript to construct the `AppleButton`.

First, you need to include the `AppleButton` class in your main HTML file. If you're planning backward compatibility with pre-OS X v.10.4.3 versions, follow the directions in [Backwards Compatible Usage](Introduction%20to%20the%20Apple%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobwfvjvomq) and include this path:

```
<script type='text/javascript' src='AppleClasses/AppleButton.js' charset='utf-8'/>
```

If you plan on requiring OS X v.10.4.3 or newer for your widget, include the `AppleButton` class in its location in `/System/Library/WidgetResources/`:

```
<script type='text/javascript' src='/System/Library/WidgetResources/AppleClasses/AppleButton.js' charset='utf-8'/>
```

Once you've included the `AppleButton` class, you also need to declare a `<div>` element to represent the button:

```
<body onload="setup();">
    ...
    <div id="myButton"></div>
    ...
</body>
```

Typically, this entails using a `<div>` element somewhere in the `<body>` portion of your HTML. The only attribute required of this element is an `id`, which is used by CSS to position the button and by JavaScript to construct the button. The `id` attribute is required over the `class` attribute, because elements with `id` attributes can be accessed via JavaScript.

Also note the declaration of an `onload` handler within the `<body>` tag. This handler is called when your widget's HTML is loaded. It's used to construct the `AppleButton` object in your JavaScript, as discussed in [An Apple Button, in JavaScript](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobvfvjvomy).

Now that the button is properly declared in your HTML file, you need to position it in your CSS. This entails including a style with the element's name and any other placement parameters you see fit to use:

```
#myButton {
    position: absolute;
    right: 20px;
    bottom: 20px;
}
```


In your HTML file, you should have included an `onload` handler as an attribute of the `<body>` tag. That handler is called once Dashboard has loaded your widget's HTML file and should be used to call the constructor for the `AppleButton` class. The constructor for an `AppleButton` is defined as:

```
AppleButton(
    buttonElement,
    label,
    height,
    leftImage,
    leftImageDown,
    leftImageWidth,
    middleImage,
    middleImageDown,
    rightImage,
    rightImageDown,
    rightImageWidth,
    onclick
);
```

The `AppleButton` parameters are defined as:

__Table 8__  `AppleButton` Constructor Parameters

| Parameter | Expected Value | Example |
| `buttonElement` | A DOM object; namely, the `<div>` declared in the HTML to contain the button | `document.getElementById("myButton")` |
| `label` | A string; the label to be shown on the button | `"Click Me"` |
| `height` | A number; the height of all of the images used in the button | `23` |
| `leftImage` | A string; the path to an image, used for the left portion of the button | `"button/buttonLeft.png"` |
| `leftImageDown` | A string; the path to an image, used for the left portion of the button as it's being clicked | `"button/buttonLeftDown.png"` |
| `leftImageWidth` | A number; the width of the images for the left portion of the button | `11` |
| `middleImage` | A string; the path to an image, used for the middle portion of the button | `"button/buttonMiddle.png"` |
| `middleImageDown` | A string; the path to an image, used for the middle portion of the button as it's being clicked | `"button/buttonMiddleDown.png"` |
| `rightImage` | A string; the path to an image, used for the right portion of the button | `"button/buttonRight.png"` |
| `rightImageDown` | A string; the path to an image, used for the right portion of the button as it's being clicked | `"button/buttonRightDown.png"` |
| `rightImageWidth` | A number; the width of the images for the left portion of the button | `11` |
| `onclick` | A function name; the function to be called when the button is clicked | `buttonClicked` |

The `AppleButton` constructor is used in the `onload` handler you specified in your HTML, which is located within your JavaScript and could look like:

```
var gMyButton;

function setup()
{
    gMyButton = new AppleButton(
        document.getElementById("myButton"),
        "Click Me",
        23,
        "button/buttonLeft.png",
        "button/buttonLeftDown.png",
        11,
        "button/buttonMiddle.png",
        "button/buttonMiddleDown.png",
        "button/buttonRight.png",
        "button/buttonRightDown.png",
        11,
        buttonClicked);
}
```

Note the global variable `gMyButton`. This variable holds a reference to the `AppleButton` object, which lets you interact with the button at any point after it's been constructed. These properties and methods are available for you to interact with:

__Table 9__  `AppleButton` object properties and methods

| Option | Type | Explanation |
| `gMyButton.onclick` | Property | Read/Write; the handler for when the button is clicked |
| `gMyButton.setDisabledImages(` `leftImageDisabled,` `middleImageDisabled,` `rightImageDisabled``)` | Method | Sets the images used to represent the button after it is disabled using `setEnabled(FALSE)` |
| `gMyButton.enabled` | Property | Read only; returns a boolean reflecting if the button is active or not |
| `gMyButton.setEnabled(boolean)` | Method | Sets whether or not the button is active; takes in either `TRUE` or `FALSE` |
| `gMyButton.remove()` | Method | Removes the button |
| `gMyButton.textElement` | Property | Read/Write; the label text element; allows you to style the label text |

Apple provides a subclass of the `AppleButton`, called the `AppleGlassButton`, to make it easy to use the standard glass-style buttons found commonly on widget backs. For example, the Done button on the back of a widget is usually a glass button, as shown in Figure 28.

__Figure 28__  The Done button is a glass-style button, which is intended for use on a widget’s back

!

To create an `AppleGlassButton`, follow the directions found above in [An Apple Button, in HTML](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobvfvjvomi) and [An Apple Button, in CSS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobvfvjvomq). When it comes time to use the `AppleGlassButton` in JavaScript, however, use the `AppleGlassButton` constructor instead of the `AppleButton` constructor, as shown below:

```
AppleGlassButton(
    buttonElement,
    label,
    onclick
);
```

The `AppleGlassButton` constructor uses Apple-supplied art to render a standard glass-style button for your widget. Its parameters are defined as:

__Table 10__  `AppleGlassButton` Constructor Parameters

| Parameter | Expected Value | Example |
| `buttonElement` | A DOM object; namely, the `<div>` declared in the HTML to contain the button | `document.getElementById("myButton")` |
| `label` | A string; the label to be shown on the button | `"Click Me"` |
| `onclick` | A function name; the function to be called when the button is clicked | `buttonClicked` |

Like the Apple Button constructor, the Apple Glass Button constructor is used in the `onload` handler in your JavaScript and could look like:

```
var gMyGlassButton;

function setup()
{
    gMyGlassButton = new AppleGlassButton(
        document.getElementById("myButton"),
        "Click Me",
        buttonClicked);
}
```

Note the global variable `gMyGlassButton`. This variable holds a reference to the `AppleGlassButton` object, which lets you interact with the button at any point after it's been constructed. These properties and methods are available for you to interact with:

__Table 11__  `AppleGlassButton` object properties and methods

| Option | Type | Explanation |
| `gMyGlassButton.onclick` | Property | Read/Write; the handler for when the button is clicked |
| `gMyGlassButton.enabled` | Property | Read only; returns a boolean reflecting if the button is active or not |
| `gMyGlassButton.setEnabled(boolean)` | Method | Sets whether or not the button is active; takes in either `TRUE` or `FALSE` |
| `gMyGlassButton.remove()` | Method | Removes the button |

[Next](Widget%20Backs%20and%20Preferences.md)[Previous](Using%20Animation.md)

