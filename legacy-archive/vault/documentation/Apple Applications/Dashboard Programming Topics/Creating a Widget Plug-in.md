---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/WidgetPlugin.html
archived_at: '2026-07-15T05:17:34.307194Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashboard Programming Topics](Introduction%20to%20Dashboard%20Programming%20Topics.md)


[Next](Calling%20Objective-C%20Methods.md)[Previous](Accessing%20Command%20Line%20Utilities.md)

# Creating a Widget Plug-in

Widgets alone cannot access applications directly, receive distributed notifications, or read files from disk. To enable these interactions, you need to provide a plug-in. You are required to implement an interface for your plug-in that makes itself available to the widget. This interface communicates with your application in whatever manner is most appropriate, for example, by issuing AppleScript commands.

For example, if you wanted to display an Address Book contact image in your widget, you would create a plug-in to access the image, write it to a temporary file, and set the file as the `<img>` element’s `src` value. (Note that if the temporary file is outside the widget’s bundle, you would also need to specify the `AllowFileAccessOutsideOfWidget` key, as described in [Using Access Keys](Specifying%20Access%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbyfvjvomy).) Another example is if you wanted to use a widget as another way to provide an interface to an application. Providing a widget front end allows a user to interact with your application in an unobtrusive and simple way that is easily accessible.

A widget plug-in is a Cocoa bundle. In Xcode, use the "Cocoa Bundle" template to create a bundle. In the plug-in code, implement the widget plug-in interface.

For examples of widgets that use plug-ins, see _[Birthdays](../../../samplecode/Birthdays/Birthdays.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojygi)_ and _[Reminders](../../../samplecode/Reminders/Reminders.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoobxg4)_ sample code projects.

Any widget plug-in must implement this method in order to be used from within Dashboard:

```objc
- (id) initWithWebView:(WebView*)webview
```

Dashboard calls this when your plug-in is first loaded. At this point, initialize an object of your principal class and prepare any critical data structures.

To have your plug-in interact with your widget, you will need to implement the WebScripting interface, as defined in [Calling Objective-C Methods From JavaScript](Calling%20Objective-C%20Methods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiytklkcijbuerskinca) and `WebScripting`. In addition to this interface, you also need to implement this method:

```objc
- (void) windowScriptObjectAvailable:(WebScriptObject *)windowScriptObject
```

If implemented, Dashboard calls it before your widget is loaded and allows you to add JavaScript objects that your widget can use. These objects bridge the gap between JavaScript and Objective-C, and are your interface with your widget. After this message is received, call `setValue: forKey:` on the just-received `WebScriptObject` to bind it to your own object and to give it a name. In order to function properly, the object that you bind to the `WebScriptObject` must implement the WebScripting interface.

This example demonstrates what your implementation of this method should include:

```objc
- (void) windowScriptObjectAvailable:(WebScriptObject *) windowScriptObject
{
    [windowScriptObject setValue:self forKey:@"MyWindowScriptObject"];
    ...
}
```

Any methods that belong to the object that you bind to the given `windowScriptObject` will be available to your widget in JavaScript, via the specified key. However, your methods will be available using the default name created for it, which can be confusing depending on its Objective-C name. Developers are advised to implement this method to provide a more human-readable name:

```objc
+ (NSString *)webScriptNameForSelector:(SEL)aSelector
```

In the following example, your plug-in class is bound to a received `WebScriptObject`, named `windowScriptObject`. The key for the object is `MyWindowScriptObject`, meaning that, from within the widget, any method belonging to the `MyWindowScriptObject` class may be called upon it:

```
<html>
<head>
...
<script>
...
function someFunction()
{
    ...
    if (MyWindowScriptObject)
    {
        MyWindowScriptObject.someMethod(someArg);
    }
    ...
}
...
</script>
</head>
...
</html>
```

For example, you can use this to notify the plug-in when the widget is finished loading in Dashboard. You can set up a function to be called when the widget has finished loading. This function will, in turn, call any method you supply:

```
<html>
...
<body onload='MyWindowScriptObject.someMethod(someArg)'>
...
</body>
</html>
```


The Xcode standard information property list file provides most of the information you need for the plug-in to function properly. Despite this, you must provide a value for the `NSPrincipalClass` property.

Once you compile the bundle, you are ready to deploy it. For your widget to use your plugin, place it at the root level of your widget bundle.

In order for your plug-in to be loaded when you activate your widget, it needs to be specified in your widget’s `Info.plist` file. The property `Plugin` needs to be added, and its value should be a String filled with the name of your bundle.

For more information on Dashboard plug-ins, see _[Dashboard Reference](../Dashboard%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmzz)_ in Apple Applications Documentation.

To learn more about bridging your widget’s JavaScript environment with your widget plug-in’s Cocoa bundle, read [Calling Objective-C Methods From JavaScript](Calling%20Objective-C%20Methods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiytklkcijbuerskinca).

When compiling your widget plug-in, make sure you're building it as a Universal plug-in for use on PowerPC and Intel-based Macintosh computers. For more on Universal binaries, read [Technical Q&A QA1451: Intel-Based Macs, Dashboard, Safari, and You](https://developer.apple.com/qa/qa2005/qa1451.html) and _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_.

[Next](Calling%20Objective-C%20Methods.md)[Previous](Accessing%20Command%20Line%20Utilities.md)

