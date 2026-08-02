---
title: WebKit Plug-In Programming Topics
apple_id: TP40001521
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: WebKit
published: '2011-05-17'
source_url: https://developer.apple.com/library/archive/documentation/InternetWeb/Conceptual/WebKit_PluginProgTopic/Tasks/WebKitPlugins.html
archived_at: '2026-07-15T07:44:15.767342Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Plug-In Programming Topics](Introduction%20to%20WebKit%20Plug-in%20Programming%20Topics.md)


[Next](Document%20Revision%20History.md)[Previous](Creating%20Plug-ins%20with%20the%20Netscape%20API.md)

# Creating Legacy Plug-ins with Cocoa and WebKit

In versions of OS X prior to version 10.7, WebKit supported plug-ins written to the native WebKit plug-in API. Because WebKit plug-ins are so closely tied to browser data structures, these plug-ins cannot run in a separate process. Thus, to improve security and stability, Safari in OS X v10.7 no longer supports this model.

Newer versions of the Netscape plug-in model and the Extensions model supersede the functionality of WebKit plug-ins. For more information on the Netscape plug-in model, read [Creating Plug-ins with the Netscape API](Creating%20Plug-ins%20with%20the%20Netscape%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi2talkciffeosskifea).

WebKit-based plug-ins are written using Objective-C API that is unique to WebKit. Although the API is not cross-platform, any plug-in created in this fashion can be used in Safari and all other WebKit-based applications prior to OS X v10.7.

WebKit plug-ins are based on core Cocoa API. Written in Objective-C, WebKit-based plug-ins are supported only by WebKit-based applications and cannot be ported to other platforms.

A WebKit plug-in itself is simply an instance of the `NSView` class, which is a common class in many other Objective-C applications. It provides a wide range of features, including management of events such as mouse and keyboard input. Your plug-in inherits these “for free.” For example, you can easily load URLs using an `NSURLConnection` object.

Apple has also provided these types of plug-ins with access to the enclosing scripting environment; a script can call methods and read properties from the plug-in, and vice versa. You can also access WebKit classes through the plug-in’s `WebFrame` object and the browser scripting environment through the WebKit `WebScriptMethods` protocol.

When you create a WebKit-based plug-in you need to compile it as a universal binary. For more information, see _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_.

For a plug-in to act like a standard web browser plug-in, it needs to conform to the `WebPlugIn` informal protocol. This protocol has just one required constructor method, [plugInViewWithArguments:](https://developer.apple.com/documentation/webkit/webpluginviewfactory/1405276-pluginview), which your `NSView` subclass should implement.

Optional methods you can implement include:

- [webPlugInInitialize](https://developer.apple.com/documentation/objectivec/nsobject/1537623-webplugininitialize), which is called just after the plug-in is created and allows you to perform any prestartup actions in the plug-in.
- [webPlugInStart](https://developer.apple.com/documentation/objectivec/nsobject/1536197-webpluginstart), which is called when the plug-in should begin doing whatever it has been designed to do.
- [webPlugInStop](https://developer.apple.com/documentation/objectivec/nsobject/1536433-webpluginstop), which is called to tell the plug-in to cease its usual actions.
- [webPlugInDestroy](https://developer.apple.com/documentation/objectivec/nsobject/1536659-webplugindestroy), which is called to give the plug-in a chance to deallocate any objects or resources it may have created or retained.
- [webPlugInSetIsSelected:](https://developer.apple.com/documentation/objectivec/nsobject/1536477-webpluginsetisselected), which is called when the selection state of the plug-in has changed, allowing you to do any custom drawing or actions based off that event.

These methods are implemented by the _container_ of the plug-in; that is, they affect the web view that surrounds the plug-in:

- [webPlugInContainerLoadRequest:inFrame:](https://developer.apple.com/documentation/objectivec/nsobject/1536649-webplugincontainerloadrequest) allows you to tell the browser to load a URL request into a given frame (or the container’s frame itself).
- [webPlugInContainerShowStatus:](https://developer.apple.com/documentation/objectivec/nsobject/1537604-webplugincontainershowstatus) allows you to tell the container to print a status message to the browser’s status bar.
- [webPlugInContainerSelectionColor](https://developer.apple.com/documentation/objectivec/nsobject/1536394-webplugincontainerselectioncolor) returns the color that the container should use to draw plug-in’s selection state when it is selected.
- [webFrame](https://developer.apple.com/documentation/webkit/domdocument/1536374-webframe) allows you to access the other WebKit elements of the container, such as its [WebView](https://developer.apple.com/documentation/webkit/webview).

The WebKit API allows your plug-ins to easily access a scripting environment (such as JavaScript) from the plug-in, and vice versa. Your plug-in can call JavaScript methods and read JavaScript properties, while your containing page can call methods from your plug-in from its JavaScript environment.

When the browser encounters your plug-in, it will use JavaScript to request the object representing your plug-in using [objectForWebScript](https://developer.apple.com/documentation/objectivec/nsobject/1537612-objectforwebscript). The object that you return from that method represents the interface to your plug-in. This can be, but is not required to be, the same object as your plug-in. In that case, your implementation of [objectForWebScript](https://developer.apple.com/documentation/objectivec/nsobject/1537612-objectforwebscript) would simply look like:

```objc
- (id)objectForWebScript
{
    return self;
}
```

The object you return needs to have control over which of its methods should be visible to the scripting environment. By default, Objective-C methods are not exposed as JavaScript methods. To expose some of your instance methods in JavaScript, override the following methods:

- [webScriptNameForSelector:](https://developer.apple.com/documentation/objectivec/nsobject/1528539-webscriptnameforselector) returns the name that a given selector should inherit so that it can be called from the JavaScript environment. The default renaming scheme (to prevent against namespace conflicts) can lead to confusing method names in the scripting environment, so you should make a habit of rewriting the names of all your exposed methods. For example, if you had an Objective-C method called `startMovieAtBeginning`, you might want it to reflect its own name in the scripting environment instead of going through a rewrite. An implementation example would look like:

```
(NSString *)webScriptNameForSelector:(SEL)selector {
    if(selector == @selector(startMovieAtBeginning)) {
        return @”startMovieAtBeginning”;
    }
    return nil;
}
```
- [isSelectorExcludedFromWebScript:](https://developer.apple.com/documentation/objectivec/nsobject/1528532-isselectorexcludedfromwebscript) lets the scripting environment know whether or not a given Objective-C method in your plug-in can be called from the scripting environment. A common mistake first-time plug-in developers make is forgetting to implement this method, causing the plug-in to expose no methods and making the plug-in unscriptable.

  As a security precaution this method returns `YES` by default exposing no methods. You should expose only methods that you know are secure; to export a method, this function should return `NO` for that method’s selector. You may only want to export one or two Objective-C methods to JavaScript. In the following example, the plug-in’s `play` method can be called from JavaScript, but other methods cannot:

```objc
+ (BOOL)isSelectorExcludedFromWebScript:(SEL)selector {
    if(selector == @selector(play)) {
        return NO;
    }
    return YES;
}
```

Similarly, you may want to give the scripting environment access to certain properties in your plug-in object. The syntax is very similar for restricting those:

- [webScriptNameForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1528541-webscriptnameforkey) should be implemented to return a more human-readable name for a method to the scripting environment.
- [isKeyExcludedFromWebScript:](https://developer.apple.com/documentation/objectivec/nsobject/1528545-iskeyexcludedfromwebscript) allows you to selectively expose properties to the scripting environment.

In this example, you create a QuickTime movie plug-in. This is a powerful example, because it requires very few lines of code and yet provides a useful extension to a web browser or WebKit application.

First, you need to create the view class. In this case, you use Cocoa’s built-in `NSMovieView` class and subclass it to create your `PlugInMovieView` (see Listing 1).

__Listing 1__  PlugInMovieView header (PlugInMovieView.h)

```objc
#import <AppKit/AppKit.h>

@interface PlugInMovieView : NSMovieView
{
    NSDictionary *_arguments;
    BOOL _loadedMovie;
    BOOL muted;
}

- (void)setArguments:(NSDictionary *)arguments;

@end
```

Now you can write the implementation. You first need to conform to the `WebPlugIn` protocol, by implementing [plugInViewWithArguments:](https://developer.apple.com/documentation/webkit/webpluginviewfactory/1405276-pluginview) (see Listing 2). Create an instance of your movie view, assign it the arguments passed into your method, and return it. Notice that an accessor method is being used to set the arguments—this is good Cocoa coding style.

__Listing 2__  Returning your plug-in’s view

```objc
+ (NSView *)plugInViewWithArguments:(NSDictionary *)arguments
{
    PlugInMovieView *movieView = [[[self alloc] initWithFrame:NSZeroRect] autorelease];
    [movieView setArguments:arguments];
    return movieView;
}
```

Now that you’ve returned the view, you need to make a decision. Do you have any operations to perform on initialization? In the case of the `NSMovieView` class , you can set a movie’s controller to be visible (or not) and also specify whether or not you’d like the user to be able to adjust its size. In this case, you should show the controller but prevent the user from resizing the movie in the frame—the most common layout for embedded movies (see Listing 3).

__Listing 3__  Initializing the movie plug-in

```objc
- (void)webPlugInInitialize
{
    [self showController:YES adjustingSize:NO];
}
```

From the enclosing container, nestled in an embed tag, you’ll receive a URL pointing to a movie. This will arrive in one of the keys specified by the _arguments_ dictionary that you set in Listing 2. Use that URL to load and play the movie (see Listing 4).

__Listing 4__  Loading and playing a movie from a URL

```objc
- (void)webPlugInStart
{
    if (!_loadedMovie) {
        _loadedMovie = YES;
        NSString *URLString = [[_arguments objectForKey:WebPlugInAttributesKey] objectForKey:@"src"];
        if ([URLString length] != 0) {
            NSURL *baseURL = [_arguments objectForKey:WebPlugInBaseURLKey];
            NSURL *URL = [NSURL URLWithString:URLString relativeToURL:baseURL];
            NSMovie *movie = [[NSMovie alloc] initWithURL:URL byReference:NO];
            [self setMovie:movie];
            [movie release];
        }
    }

    [self start:self];
}
```

Eventually, all good things must come to an end, and so shall your plug-in. This will be announced by a call to [webPlugInStop](https://developer.apple.com/documentation/objectivec/nsobject/1536433-webpluginstop). You should take the opportunity to stop the movie from playing (see Listing 5).

__Listing 5__  Stopping the movie

```objc
- (void)webPlugInStop
{
    [self stop:self];
}
```

You’ve just implemented a fully functional WebKit movie-playing plug-in. You could build this code, install the plug-in, and have your own working QuickTime player embedded in Safari or a WebKit-based application. However, you might want to add a little more flair and use a form—with HTML buttons—to play and pause the movie. It just takes a few more lines of code (see Listing 6).

__Listing 6__  Opening the plug-in to JavaScript

```objc
+ (BOOL)isSelectorExcludedFromWebScript:(SEL)selector
{
    if (selector == @selector(play) || selector == @selector(pause)) {
        return NO;
    }
    return YES;
}

+ (BOOL)isKeyExcludedFromWebScript:(const char *)property
{
    if (strcmp(property,"muted") == 0) {
        return NO;
    }
    return YES;
}

- (id)objectForWebScript
{
    return self;
}

- (void)play
{
    [self start:self];
}

- (void)pause
{
    [self stop:self];
}
```

You only had to add two extra methods, `play` and `pause`, so that the buttons in the interface could be tied to public methods. Then you exposed those methods to the JavaScript scripting environment.

If you want to explore further, this example is available at:

```
    /Developer/Examples/WebKit/WebKitMoviePlugIn
```

on a computer running OS X v10.5 or earlier with Xcode Tools 3.1.3 or earlier installed.

Beginning in OS X v10.6, Safari is a 64-bit WebKit-based application. Thus, all WebKit plug-ins must be updated to include 64-bit slices in their universal binaries in order to work with Safari.

Because WebKit plug-ins are inherently Cocoa-based code, relatively few changes should be needed to make your code work in a 64-bit version of Safari (beyond recompiling it with different architecture settings). You do not need to make any changes specific to WebKit plug-ins.

Before you begin, read the documents _[64-Bit Transition Guide](../../Darwin/64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru)_ and _[64-Bit Transition Guide for Cocoa](../../Cocoa/64-Bit%20Transition%20Guide%20for%20Cocoa/Introduction%20to%2064-Bit%20Transition%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denbx)_. The main transition guide describes compiler settings and changes you must make to port any code to a 64-bit environment. The Cocoa transition guide describes additional changes you must make that are specific to a Cocoa environment.

Once you have read these documents, the porting a WebKit plug-in is essentially the same as porting a Cocoa application. This is a four step process:

- Change your compile settings to build a 3-way or 4-way universal binary (with 32-bit PowerPC, 32-bit Intel, 64-bit Intel, and optionally 64-bit PowerPC slices) and recompile. Fix any problems that prevent compilation.
- Make the data type changes described in _[64-Bit Transition Guide](../../Darwin/64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru)_ and _[64-Bit Transition Guide for Cocoa](../../Cocoa/64-Bit%20Transition%20Guide%20for%20Cocoa/Introduction%20to%2064-Bit%20Transition%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denbx)_.
- Enable additional compiler warnings to help you find and fix truncation bugs, then fix as many of the warnings as possible.
- Track down and fix any remaining bugs that prevent correct operation.

Your plug-in will need to register itself with the application that uses it, so that the application knows what content types you support. Your plug-in bundle needs to contain this important registration information. In addition to setting the correct registration information for your plug-in, you must set the correct `CFBundlePackageType`. The default `CFBundlePackageType` when you create a new WebKit plug-in in Xcode is `BNDL`, this must be changed to `WBPL` to be recognized by WebKit.

There are two different ways of storing this registration information. One is with an `Info.plist` file stored within the plug-in bundle. This is an easy-to-edit and easy-to-maintain way to register your content types, but is supported only by applications based on the WebKit (no matter in what style you wrote the plug-in). The other way to register the information—and this method is required if you want other browsers on the Mac platform to support your plug-in—you also have to include a Carbon resources file.

The `Info.plist` file contains important information. Let’s use an example from the WebKit movie plug-in, which you will create in [Creating Legacy Plug-ins with Cocoa and WebKit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi2dslkciffeosskifea). First, you need to register a description of the plug-in (see Listing 7).

__Listing 7__  Plug-in description in the Info.plist file

```
<key>WebPluginDescription</key>
    <string>Simple WebKit plug-in that displays movies</string>
```

Next, you’ll need to register the MIME types that your plug-in supports (see Listing 8).

__Listing 8__  Registering MIME types in the Info.plist file

```
<key>WebPluginMIMETypes</key>
    <dict>
        <key>video/x-webkitmovie</key>
        <dict>
            <key>WebPluginExtensions</key>
            <array>
                <string>mov</string>
            </array>
            <key>WebPluginTypeDescription</key>
            <string>QuickTime Movie</string>
        </dict>
    </dict>
```

Finally, your plug-in needs a useful name for the application to call it by (see [Listing 9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi2dsljrhe4tenryfvbeeq2gijeugqi)).

__Listing 9__  Name That Plug-in

```
<key>WebPluginName</key>
    <string>WebKit Movie Plug-in</string>
```

[Next](Document%20Revision%20History.md)[Previous](Creating%20Plug-ins%20with%20the%20Netscape%20API.md)

