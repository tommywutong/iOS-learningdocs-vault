---
title: Dashcode 2.0 Release Notes
apple_id: TP40006505
resource_type: Release Note
platform: Safari|Xcode Developer Tools
topic: Xcode
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/releasenotes/DeveloperTools/RN-Dashcode/index.html
archived_at: '2026-07-18T02:50:26.612073Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Dashcode 2.0 Release Notes

> [!IMPORTANT]
> 

Welcome to Dashcode 2.0!

__Dashcode 2.0__ is an integrated environment for laying out, coding, and testing:

- Web applications for iPhone and iPod touch
- Dashboard widgets

The key features of version 2.0 support developing web applications, although most benefit widget developers as well.

For more information about Dashcode, read _[Dashcode User Guide](../../documentation/Apple%20Applications/Dashcode%20User%20Guide/Introduction%20to%20Dashcode%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojs)_.

#### Contents:

- [Key Features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbvfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Known Issues and Workarounds](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbvfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Additional Documentation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbvfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)

### Key Features

- __Web application project type and templates.__ Web application projects look similar to widget projects, but with a few differences. For example, web applications have no Default Image, and the settings in the Page Attributes of a web application are different from those in the Widget Attributes of a widget. Dashcode 2.0 also comes with an improved template chooser that contains several new templates to help you start a web application.
- __iOS Simulator integration.__ When you run (or debug) a web application project, it runs in the iOS Simulator so you can get an accurate preview of how your application will function on iPhone or iPod touch. All of Dashcode's debugging features are available when running in the Simulator. If you have the OS X Xcode Developer Tools, but not the iOS SDK, Dashcode 2.0 instead runs your application in a special environment that uses the OS X WebKit instead of the Simulator.
- __Stack Layouts and Transitions.__ A new part called Stack Layout supports multiple different content views that you can switch among when your web application or widget is running. And, for web applications running on the latest versions of iPhone or iPod touch, switching among views can be done with animated transitions. Several transitions are provided, including both 2D effects, such as Push and Dissolve, and 3D effects, such as Flip and Cube.
- __Document Flow positioning.__ Dashcode 2.0 supports designs using Document Flow positioning as well as Absolute positioning. Document Flow positioning has more constraints than Absolute positioning, but it allows you to build interfaces that can grow to accommodate their content. Dashcode 2.0 also provides some new parts that will help you overcome some of the restrictions that Document Flow positioning imposes.
- __Better support for auto-resizing.__ Dashcode 2.0 has improved support for setting up an interface that adapts to changes in screen size. In particular, you can set up your interface so that it adapts appropriately to orientation changes on iPhone or iPod touch.
- __Resource Log and Performance Meters.__ Dashcode 2.0 expands debugging support by including a resource log that shows the resources your web application or widget has loaded, including details about how they were loaded and from where. You can also get previews of the content of most resources, including the textual content of HTML, CSS, or JavaScript, and previews of image resources. In addition, there are several performance monitors that help you see how much memory, CPU, and network bandwidth your web application or widget uses over time.
- __Sharing interface.__ Dashcode 2.0 provides an interface to manage sharing or deployment of widgets and web applications. For web applications, this interface (and a set of Accounts, defined in Dashcode 2.0 Preferences) allows you to deploy your project directly to a web server.
- __Improved glass and border effects.__ The glass effect has been improved in Dashcode 2.0 and made to look more like the glass effect used in native iPhone applications. In addition, a new image generation option has been added to allow an embedded border appearance for buttons and other parts that more closely matches native iPhone controls.
- __Touch event support.__ Dashcode's button parts for web applications use touch events on iPhone to provide highlight effects and other tracking behavior that makes the controls seem more like their native counterparts.
- __Image buttons.__ Dashcode's button parts for web applications now allow both text and image placement within the button.
- __Call, email, and map buttons.__ Special button parts are provided for buttons that call a phone number, send an email, or look up a map location.
- __Other new parts.__ In addition to those already mentioned, there are several new parts that can help you build web applications that look right at home on iPhone and iPod touch.
- __HTML indentation.__ Dashcode 2.0 manages the indentation of the main HTML file, which makes it consistent and easy to read.

### Known Issues and Workarounds

- Many Dashcode parts are available for both web applications and widgets. However, some parts are suitable for one project type and not the other. The Dashcode parts library displays the parts that are appropriate for the current project.
- If you choose not to install the System Components package when you install the Developer Tools, the Performance Monitor panel will not be available. However, because this package is installed by default, you can simply run the installer again, making sure the System Components package is selected.
- The design canvas supports two features that cause the canvas to be scaled when designing web applications. You can choose to see your interface scaled to device resolution so it appears on the canvas at the same size it will appear on iPhone or iPod touch. And, depending on your Page Attributes, if you choose to view your interface as it will look when iPhone or iPod touch is rotated, the content may be scaled. Currently, there are visual artifacts that may occur when the view is scaled. In the current release, these artifacts can be bad enough to make it inadvisable to do much editing while using one or both of these modes. Therefore, these modes should be treated more as previews until this can be corrected.
- Currently there is no QuickTime part supported for web application projects. For an example of how to provide access to audio or video playback within your own web application, take a look at the Podcast web application template. For more information on embedding audio and video content in your web application, see _[Safari Web Content Guide](../../documentation/Apple%20Applications/Safari%20Web%20Content%20Guide/Developing%20Web%20Content%20for%20Safari.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjr)_.
- Some of the new parts can be hard to select directly because they have selectable children that fill their whole area. Currently, these elements can be selected only by using the outline view of the DOM navigator. The Stack Layout, Browser, and Column Layout parts are the most prominent examples of parts that can be selected only in the outline view. If you need to inspect one of these parts (for example, to style them or to add views to a Stack Layout) you must use the outline view.
- When using onclick handlers, be aware that if an element with an onclick handler is inside an element with touch event handlers, depending on the behaviors of the handlers, your onclick handler might not fire, or it might fire in conjunction with whatever behavior is implemented by the touch event handlers. These types of events are mutually exclusive, but it is best not to mix touch event handling with onclick handling in the same areas. The web application button parts in Dashcode 2.0 use touch event handling to implement their clicking behavior, as do the rows in list objects.
- The Push Button and related parts (in other words, all parts that use `PushButton.js`), as well as the various List parts, have special behavior with respect to their onclick handlers. When you set an onclick handler on these elements in the Behaviors inspector, at runtime this is actually converted so that the elements use touch events and the part will invoke the "onclick" handler directly from its touch event handlers. If you are mixing onclick and touch event handling it may help to be aware of this detail.
- The Call, Mail, and Map buttons have built-in behaviors that govern what happens when they are clicked. The onclick behavior should not be displayed in the Behaviors inspector, but it currently is. Any "onclick" behavior assigned to these types of buttons will be ignored at runtime.
- It is possible for images you add to a Dashcode project to collide with the names of images that Dashcode generates. For example, when Dashcode generates an image for a button part's background, it names the image with the button element’s ID and adds the extension `.png`. If you already have an image in the project with that same name, Dashcode may overwrite it. To avoid this, make sure you name your custom images using names that are not the same as element IDs in your project.
- Reparenting a rounded rectangle list will sometimes result in a very thin (zero width) list. This is due to a miscalculated margin-right style. You can reset it to a reasonable value in the inspector or directly in the CSS.
- Duplicating a Column Layout will result in the copy having more columns than the original.
- If you use the Text Area part, you may notice that the width and height auto-resizing behavior springs in the Metrics inspector are not enabled. A workaround is to manually set the width or height to "auto" in the CSS for the element.
- If you open a Dashboard widget directly in Dashcode 2.0, the Deploy menu item is disabled. You can still deploy the widget if you use the Share pane instead (click Share in the navigator).
- A bug in the Cocoa frameworks can cause crashes when Dashcode projects are upgraded. This bug has been fixed in OS X v10.5.3. If you experience problems when upgrading project, please make sure to update to OS X v10.5.3 or later.
- Button parts do not click unless they have an onclick handler. If you have configured a button with both an image and a pressed state image, you will not see the pressed state image unless the button has an onclick behavior assigned to it.
- Images in push button parts may display slightly lower than they should. They are not vertically centered.
- Due to an issue with handling CSS rules with transitions, some properties may get incorrect values or be removed altogether. The workaround is to move the CSS transition properties (and only the transition properties) of the rule to a stylesheet other than the main CSS file.

  For example, leave code such as the following in `main.css`:

```
#animatedElement {
  width: 50px;
  height: 30px;
  position: absolute;
}
```

  And in a separate CSS file, place the transition property code:

```
#animatedElement {
  -webkit-transition: opacity 1s linear;
}
```
- The first time you create a custom code snippet, the code library might not display it right away. If this happens, quit Dashcode and restart it; this will cause the first and all subsequent code snippets you create to appear in the library.

### Additional Documentation

The following documentation is available for Dashcode and Dashboard widget development:

- _[Dashcode User Guide](../../documentation/Apple%20Applications/Dashcode%20User%20Guide/Introduction%20to%20Dashcode%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojs)_
- _[Dashboard Programming Topics](../../documentation/Apple%20Applications/Dashboard%20Programming%20Topics/Introduction%20to%20Dashboard%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqmzx)_
- _[Dashboard Reference](../../documentation/Apple%20Applications/Dashboard%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmzz)_

You can access the documentation from the ADC Reference Library, available online at [http://developer.apple.com/referencelibrary/](https://developer.apple.com/referencelibrary/). There you can find comprehensive Dashboard and Dashcode documentation in the [Reference Library > Apple Applications > Dashboard](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000418-TP40001366) and [Reference Library > Tools > Dashcode](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000436-TP40006081) sections.
