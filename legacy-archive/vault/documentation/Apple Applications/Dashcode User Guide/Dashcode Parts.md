---
title: Dashcode User Guide
apple_id: TP40004692
resource_type: Guide
platform: Safari|Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashcode_UserGuide/Contents/Resources/en.lproj/PartsReference/PartsReference.html
archived_at: '2026-07-15T05:17:47.009860Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashcode User Guide](Introduction%20to%20Dashcode%20User%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Dashcode%20Templates.md)

# Dashcode Parts

Dashcode includes a number of unique elements that you use on your widget’s or web application’s interface to display information. Some of these elements, called Dashcode parts, can be modified programmatically. For those that can be modified programmatically, this appendix describes some of the methods you can use to do so. To look at the code that implements these parts, choose the Files view in the navigator and select the appropriate file.

Some parts listed in this appendix are specifically designed to work with web applications, not widgets, and are described as such.

After you add a part to the canvas, you can change its attributes using the Attributes inspector, create bindings to it using the Bindings inspector, and assign to it event handlers using the Behaviors inspector. For more information about the inspector window, read [Changing an Element’s Properties](Designing%20the%20User%20Interface%20of%20a%20Widget%20or%20Web%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnjnknlte).

The Activity Indicator part is designed for use in a web application. An activity indicator shows the user that a task or process is progressing, but does not indicate when it will finish.

The Activity Indicator part includes JavaScript code that starts and stops the spinning action. You can use the `startAnimation` and `stopAnimation` methods to coordinate the spinning of an activity indicator with the progress of a task or process.

The Back button part is designed for use in a mobile Safari web application. In a mobile Safari web application that displays multiple levels of information, a back button gives users a convenient way to retrace their steps within the application. This allows an application to present its own navigational hierarchy within a single URL.

The Back button part is automatically included in the code for a mobile Safari project based on the Browser template. It is set up to appear on all levels except the first.

The Box part is an area that is optionally wrapped with scroll bars, meant for showing content larger than a widget’s or web application’s interface. You can customize a box’s appearance using the Attributes inspector. Options you can set include whether the box automatically hides when its contents fit in its bounds and the dimensions of its bounds and margins.

To change the contents of a box, use the `content` property from the box’s object, as shown here:


```
var content = document.getElementById("box").object.content;
content.innerText = someText;
```

Once you obtain the box’s `content` property, you have access to the `<div>` element that is inside the box. From there, you can use the `innerText` or `innerHTML` properties to change the box’s contents.

The Browser part is designed for use in a web application. A browser provides an area for grouping elements and browsing back and forth. When you select the Browser web application template, a Browser part is included automatically.

The Browser part includes JavaScript code to perform some standard actions. In particular, a browser supplies a method you can use to reveal the next level in a hierarchy of information. Typically, you call the `goForward` method in the controller code for a list part, assigning it to handle the `onclick` event associated with a list row. The Browser part handles the analogous “go back” functionality automatically.

The Canvas part is a custom drawing region you can add to your widget. “Using the Canvas” in _[WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483)_ discusses how to draw on a canvas using JavaScript.

The Call button part is designed for use in a web application. A call button gives users a convenient way to initiate a phone call. In the Attributes inspector, you can specify a default phone number to dial when users tap the button.

The Call button part includes JavaScript code to perform some standard actions, such as methods to get and set the phone number. If the button is enabled, the default action is to initiate a phone call to the currently set phone number when the user taps it. You can use the `setPhoneNumber` method to allow users to change the phone number dynamically.

The Column Layout part is an area you can use for laying out content side by side. This part is especially useful for web applications because each column can be set to position its content absolutely or relatively.

If, for example, you wanted to provide one column to display fixed-size images and another column to display variably sized descriptions about the images, you could specify the first column to use absolute positioning and the second column to use relative positioning. The Column Layout part handles much of this for you.

The Edge-to-Edge List part provides a list format in which each row stretches from one side of its container to the other. An edge-to-edge list contains a customizable row template that is used to create new rows in the list.

You can specify static data to display in each row, or you can set up your web application to provide data dynamically at runtime. If you’re using Dashcode version 3.0 and later, you can provide data dynamically using data sources and bindings. To learn how to do this, see [Adding a Data Source](Adding%20Source%20Code%20and%20Creating%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcni) and [Creating Bindings](Adding%20Source%20Code%20and%20Creating%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcnq).

Alternatively, you can customize the list’s controller code to provide data dynamically at runtime. You can set this in the Attributes inspector. The remainder of this section describes how to customize a list’s controller code.

An edge-to-edge list that receives data dynamically needs a controller object (a static edge-to-edge list does not need a controller object). The list controller object must implement two required data source methods: `numberOfRows` and `prepareRow`. The `numberOfRows` callback method returns the total number of rows in the list. The `prepareRow` method is called once for each row as it is being prepared and it uses the values it is passed to populate the row. Specifically, the `prepareRow` method requires the following three arguments:

- `rowElement`. This is the enclosing element for the entire row. You can use this element to install click handlers for each row in the list.
- `rowIndex`. This is the zero-based index of the row. You can use this value to find the appropriate row data in application-specific data structures.
- `templateElements`. This is a dictionary that contains an entry for each element in the template row that has an ID. Each key in the dictionary is an ID and the associated value is the element within `rowElement` that corresponds to the original template elements, such as `rowTitle`. You can use the values associated with these elements to fill in the appropriate places in the row.

An edge-to-edge list also contains the public `rows` property, which gives you access to each row element in the list. If the list is dynamic, you can use the `rows` property to view currently filled rows in your `prepareRow` callback method while the list is filling, but you won’t be able to see all the rows until the list is completely filled. For both static and dynamic lists, the `rows` property is most useful for getting access to specific rows after the list is filled.

If your edge-to-edge list receives data dynamically, be sure to call the `reloadData` function to force the list to reload and display the updated content. (Note that `reloadData` is called automatically when the list part is initialized.) To do this, add this line of code to your list controller:

```
document.getElementById("myList").object.reloadData();
```


The Forward button part is designed for use in web applications. A forward button gives users a convenient way to move forward through the multiple levels of a web application.

The Gauge part is a dial with a pointer that indicates a value in a range of values. You can edit a gauge’s appearance and range of values using the Attributes inspector. If you’re using a gauge as a control, select the Track Mouse Down option in the Attributes inspector and supply your own handler function for the `onchange` event in the Behaviors inspector. Your handler is called whenever the gauge’s value changes.

If you’re using a gauge to graphically represent data, you need to update its value using JavaScript. Use the `setValue` method to update a gauge’s value, as shown here:


```
document.getElementById("gauge").object.setValue(50);
```

Note that the value provided to `setValue` should lie within the range specified in the Attributes inspector for the gauge.

The Grid part formats data in a grid of cells. You can edit a grid’s appearance, and specify whether it receives data statically or dynamically, in the Attributes inspector.

The Image part defines an area that receives an image at runtime (or, you can provide a static image resource by specifying the source location in the Attributes inspector). You can adjust the style and effects applied to the image in the Fill & Stroke inspector.

The Indicator part is a light that changes color at different values. You can edit an indicator’s appearance and range of values using the Attributes inspector.

When using an indicator, you need to update its value using JavaScript, as shown here:


```
document.getElementById("indicator").object.setValue(10);
```

Note that the value provided to `setValue` should lie within the range specified in the Attributes inspector for the indicator.

The Horizontal and Vertical Level Indicator parts are linear indicators that show a value in a range of values. You can edit a level indicator’s appearance and range of values using the Attributes inspector. If you’re using a level indicator as a control, select the Track Mouse Down option in the Attributes inspector and supply your own handler function for the `onchange` event in the Behaviors inspector. Your handler is called whenever the level indicator’s value changes.

If you’re using a level indicator to graphically represent data, you need to update its value using JavaScript. Use the `setValue` method to update a level indicator’s value, as shown here:


```
document.getElementById("horizontalLevelIndicator").object.setValue(10)
```

Note that the value provided to `setValue` should lie within the range specified in the Attributes inspector for the level indicator.

The Mail button part is designed for use in a web application. A mail button gives users a convenient way to initiate an email message. In the Attributes inspector, you can specify a default recipient (email address) and subject to use when users tap the button.

The Mail button part includes JavaScript code to perform some standard actions, such as methods to get and set the email address and to get and set the subject. If the button is enabled, the default action is to open a message composing view, with the To and Subject fields filled in with the currently set address and subject. You can use the `setEmailAddress` and `setSubject` methods to allow users to change the email address and subject dynamically.

The Map button part is designed for use in a web application. A map button gives users a convenient way to view a map for a location. In the Attributes inspector, you can specify a default location to display when users tap the button.

The Map button part includes JavaScript code to perform some standard actions, such as methods to get and set the address to display. If the button is enabled, the default action is to display a map for the currently set location. You can use the `setAddress` method to allow users to change the map location dynamically.

The Quartz Composer part is an area that contains a Quartz Composer composition. To manipulate a composition while your widget runs, use the Quartz Composer WebKit plug-in’s JavaScript API. You can learn more about the Quartz Composer WebKit plug-in’s JavaScript API by reading _[Quartz Composer WebKit Plug-in JavaScript Reference](../../Internet%20Web/Quartz%20Composer%20WebKit%20Plug-in%20JavaScript%20Reference/Introduction%20to%20Quartz%20Composer%20WebKit%20Plug-in%20JavaScript%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjx)_.

The QuickTime part is an area used for playback of QuickTime media. Use the QuickTime JavaScript methods to control the playback of the movie or change its properties. To learn more about the QuickTime plug-in’s JavaScript methods, read _JavaScript Scripting Guide for QuickTime_.

The Rounded-Rectangle List part provides a list in which a group of rows is inset from the edges of its container and is bordered by a rounded rectangle. A rounded-rectangle list part contains a customizable row template you can use to create new rows in the list.

You can specify static data to display in each row, or you can set up your web application to provide data dynamically at runtime. If you’re using Dashcode version 3.0 and later, you can provide data dynamically using data sources and bindings. To learn how to do this, see [Adding a Data Source](Adding%20Source%20Code%20and%20Creating%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcni) and [Creating Bindings](Adding%20Source%20Code%20and%20Creating%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcnq).

Alternatively, you can customize the list’s controller code to provide data dynamically at runtime. You can set this in the Attributes inspector. The remainder of this section describes how to customize a list’s controller code.

A rounded-rectangle list that receives data dynamically needs a controller object (a static rounded-rectangle list does not need a controller object). The list controller object must implement two required data source methods: `numberOfRows` and `prepareRow`. The `numberOfRows` callback method returns the total number of rows in the list. The `prepareRow` method is called once for each row as it is being prepared and it uses the values it is passed to populate the row. These values are passed to the `prepareRow` method in the following three arguments:

- `rowElement`. This is the enclosing element for the entire row. You can use this element to install click handlers for each row in the list.
- `rowIndex`. This is the zero-based index of the row. You can use this value to find the appropriate row data in application-specific data structures.
- `templateElements`. This is a dictionary that contains an entry for each element in the template row that has an ID. Each key in the dictionary is an ID and the associated value is the element within `rowElement` that corresponds to the original template elements, such as `rowTitle`. You can use the values associated with these elements to fill in the appropriate places in the row.

A rounded-rectangle list also contains the public `rows` property, which gives you access to each row element in the list. If the list is dynamic, you can use the `rows` property to view currently filled rows in your `prepareRow` callback method while the list is filling, but you won’t be able to see all the rows until the list is completely filled. For both static and dynamic lists, the `rows` property is most useful for getting access to specific rows after the list is filled.

If your rounded-rectangle list receives data dynamically, be sure to call the `reloadData` function to force the list to reload and display the updated content. (Note that `reloadData` is called automatically when the list part is initialized.) To do this, add this line of code to your list controller:

```
document.getElementById("myList").object.reloadData();
```


The Split Layout part is designed for use in Safari web applications. A split layout is an area that contains two resizable views that are separated by a splitter. You can use the Attributes inspector to adjust the orientation of the split layout and to determine which of the two resizable views is flexible (that is, can be completely hidden when the window is resized).

The Stack Layout part is designed for use in web applications. A stack layout is an area that contains views that can be swapped.

You can use the Attributes inspector to add and remove views in the stack layout, and you can specify transition styles to be used while swapping. For example, you can change the transition between views from a push (in which the new view pushes the old view from the side) to a fade (in which the new view fades in over the top of the old view).

A stack layout part includes a number of methods you can use to access its subviews and set transitions between views. In particular, you can use:

- `getCurrentView`. This method returns the currently active view.
- `getAllViews`. This method returns a JavaScript array of views in the stack layout. You might want to use the index of the array to get the “next” view.
- `setCurrentView`. This method takes the following parameters:

  - `newView`. The new view to display.
  - `isReverse`. A Boolean value that specifies whether the transition should be performed in reverse (for example, the push transition defines a reverse transition).
  - `makeTopVisible`. A Boolean value that specifies whether the new view should be scrolled to the top.

  The `setCurrentView` method sets the current view to the passed-in view and sets the transition and scroll position appropriately.
- `setCurrentViewWithTransition`. This method is similar to `setCurrentView` except that it includes a `transition` parameter after the `newView` parameter that allows you to specify a transition. (See Stack Layout Transitions for more information about transition objects.)

The transition object handles transitions between views in a stack layout container. By default the transition object handles a few transition types and a number of transition properties. Transition objects are created with the `Transition` constructor function, as shown here:

```
Transition (type, duration, timing)
```

The parameters of the `Transition` function specify the type of transition, the length of time the transition takes, and the acceleration curve of the transition. Note that you can also set these properties in the inspector after a transition object has been created.

The available transition types are:

- `Transition.NONE_TYPE`. The new view simply appears in place of the old view.
- `Transition.PUSH_TYPE`. A two-dimensional transition in which the new view pushes the old view off one edge of the screen.
- `Transition.DISSOLVE_TYPE`. A two-dimensional transition in which the old view dissolves into the new view.
- `Transition.SLIDE_TYPE`. A two-dimensional transition in which the new view slides in over the old view from one edge of the screen.
- `Transition.FADE_TYPE`. A two-dimensional transition in which the new view fades in over the old view.
- `Transition.FLIP_TYPE`. A three-dimensional transition in which the old view flips over to reveal the new view.
- `Transition.CUBE_TYPE`. A three-dimensional transition in which the old view and new view appear as if they are adjacent faces of a cube, which rotates to reveal the new view.
- `Transition.SWAP_TYPE`. A three-dimensional transition in which both views move away from each other horizontally and then swap positions vertically, leaving the new view on top.
- `Transition.REVOLVE_TYPE`. A three-dimensional transition in which the old view and the new view share an axis on one edge, about which the old view revolves out as the new view revolves in.

The `duration` parameter should contain the number of seconds the transition should take, from start to finish. Finally, for the `timing` parameter, you can specify a timing function that controls the speed and acceleration of the transition (the timing functions are defined in the WebKit CSS animation specification). The available transition timing functions are:

- `Transition.EASE_TIMING`
- `Transition.LINEAR_TIMING`
- `Transition.EASE_IN_TIMING`
- `Transition.EASE_OUT_TIMING`
- `Transition.EASE_IN_OUT_TIMING`

The timing functions determine the acceleration curve of the transition. A linear curve means constant speed (that is, no acceleration), and “ease” means gaining or losing speed gradually. For example, the `Transition.EASE_IN_TIMING` function means that the transition starts slow and gradually gets faster, whereas the `Transition.EASE_OUT_TIMING` function means that the transition gradually slows down near the end.

You can also specify a direction for the `Transition.PUSH_TYPE` and `Transition.SLIDE_TYPE` transitions. The available directions are:

- `Transition.RIGHT_TO_LEFT_DIRECTION`
- `Transition.LEFT_TO_RIGHT_DIRECTION`
- `Transition.TOP_TO_BOTTOM_DIRECTION`
- `Transition.BOTTOM_TO_TOP_DIRECTION`

Finally, you specify a direction for the four three-dimensional transitions. The available directions for these transitions are:

- `Transition.RIGHT_TO_LEFT_DIRECTION`
- `Transition.LEFT_TO_RIGHT_DIRECTION`

The transition object includes the `perform` method that performs the transition. You pass in the following parameters to the `perform` method:

- `newView`. The view that will be visible after the transition.
- `oldView`. The view that is visible now (before the transition).
- `isReverse`. A Boolean flag that specifies whether the transition should be performed in reverse. (The push transition, for example, can be performed in reverse; the cross-fade transition is the same either way.)

The `perform` method ensures that the passed-in views share a common parent container element, which is important because the transition is constrained by the dimensions of the parent container. In particular, the container must constrain the transitions for overflow content.

Note that you can use transition objects to pass in for the transition parameter of the stack layout `setCurrentViewWithTransition` method. For more information about the stack layout methods, see [Stack Layout Methods](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjufvjvomrr).

The video part is an area that handles video playback and provides playback controls.

The Video part uses the HTML 5 `video` element, which means that the video is embedded in the web-view area and does not require the QuickTime plug-in to render it. This provides greater integration with the rest of your web content and makes possible sophisticated layouts and effects.

[Next](Document%20Revision%20History.md)[Previous](Dashcode%20Templates.md)

