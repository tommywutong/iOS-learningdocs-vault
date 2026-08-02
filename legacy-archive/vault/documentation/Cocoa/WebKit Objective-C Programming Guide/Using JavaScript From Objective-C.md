---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/JavaScriptFromObjC.html
archived_at: '2026-07-15T07:14:51.743938Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Spoofing.md)[Previous](Using%20the%20Document%20Object%20Model%20Extensions.md)

# Using JavaScript From Objective-C

The web scripting capabilities of WebKit permit you to access JavaScript attributes and call JavaScript functions from your Cocoa Objective-C applications. Refer to _[WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483)_ if you want to access the Objective-C API from JavaScript.

JavaScript objects are represented by instances of [WebScriptObject](https://developer.apple.com/documentation/webkit/webscriptobject) in Objective-C. The API uses instances of `WebScriptObject` to wrap script objects passed from the scripting environment to Objective-C. You can use the methods of this class to call JavaScript functions and get/set properties of the JavaScript environment.

You should not create `WebScriptObject` instances explicitly. Rather, use the [windowScriptObject](https://developer.apple.com/documentation/webkit/webview/1408426-windowscriptobject) method from [WebView](https://developer.apple.com/documentation/webkit/webview) to gain access to the scripting environment.

Method parameters must be objects or basic data types like `int` and `float`. Objective-C objects will be converted to their JavaScript equivalents by WebKit:

- `NSNumber` objects will be converted to JavaScript numbers.
- `NSString` objects will be converted to JavaScript strings.
- `NSArray` objects will be mapped to special read-only arrays.
- `NSNull` will be converted to JavaScript’s null.
- All other objects will be wrapped by WebKit into appropriate objects for the JavaScript environment.

Let’s look at a couple of examples. You may want to get the URL of the current WebView from JavaScript, rather than accessing the URL from the data source of your WebView’s [WebFrame](https://developer.apple.com/documentation/webkit/webframe). You can do this with just a few lines of code:

```
id win = [webView windowScriptObject];
id location = [win valueForKey:@”location”];
NSString *href = [location valueForKey:@”href”];
```

JavaScript makes it easy to access the attributes of a web page’s window. WebKit makes it easy to get that information from JavaScript and pass it to Objective-C. Properties, such as `location` and `href`, are only available from the script object if the class overrides [isKeyExcludedFromWebScript:](https://developer.apple.com/documentation/objectivec/nsobject/1528545-iskeyexcludedfromwebscript) to return `NO` for the given properties. The same is true for any selectors. But remember, a key feature of the web scripting system in WebKit is the ability to call JavaScript functions. One of JavaScript’s built-in functions, `location.href`, returns the URL of the window in one call. With this in mind, you can slim your three-line URL accessor in the example above down to one simple line:

```
NSString *href = [[webView windowScriptObject] evaluateWebScript:@”location.href”];
```

You can also call JavaScript functions with arguments. Assume that you have written a JavaScript function which looks like this:

```
function addImage(image, width, height) { ... }
```

Its purpose is to add an image to a web page. It is called with three arguments: `image`, the URL of the image; `width`, the screen width of the image; and `height`, the screen height of the image. You can call this method one of two ways from Objective-C. The first creates the array of arguments prior to using the `WebScriptObject` bridge:

```
id win = [webView windowScriptObject];

NSArray *args = [NSArray arrayWithObjects:
                    @”sample_graphic.jpg”,
                    [NSNumber numberWithInt:320],
                    [NSNumber numberWithInt:240],
                    nil];

[win callWebScriptMethod:@"addImage"
            withArguments:args];
```

The second version sends the arguments right to JavaScript:

```
[win evaluateWebScript:
    @"addImage(’sample_graphic.jpg’, ‘320’, ‘240’)"];
```

For more information on using the `WebScriptObject` to open JavaScript to Objective-C, read the _[WebKit Objective-C Framework Reference](https://developer.apple.com/documentation/webkit)_.

[Next](Spoofing.md)[Previous](Using%20the%20Document%20Object%20Model%20Extensions.md)

