---
title: WebKit Plug-In Programming Topics
apple_id: TP40001521
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: WebKit
published: '2011-05-17'
source_url: https://developer.apple.com/library/archive/documentation/InternetWeb/Conceptual/WebKit_PluginProgTopic/Tasks/NetscapePlugins.html
archived_at: '2026-07-15T07:44:15.171048Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Plug-In Programming Topics](Introduction%20to%20WebKit%20Plug-in%20Programming%20Topics.md)


[Next](Creating%20Legacy%20Plug-ins%20with%20Cocoa%20and%20WebKit.md)[Previous](About%20Web%20Browser%20Plug-ins.md)

# Creating Plug-ins with the Netscape API

Netscape-style plug-ins are written using a cross-platform C API, and, provided that you are building in Mach-O form, can be developed and debugged with Xcode. These plug-ins are compatible with a wide range of web browsers.

The original Netscape plug-in architecture was integrated into Netscape 2.0 in 1996. Since then, the API has been adopted by most common web browsers, including Safari. It has built-in support for onscreen drawing, various types of event handling, and networking functions.

In addition to the core plug-in functionality, Apple has extended the capabilities of the Netscape-style plug-ins. Starting with the WebKit framework bundled with Safari 1.3 (on OS X version 10.3) or Safari 2.0 (on OS X version 10.4), the Netscape-style plug-ins can also perform scripting functions.

The Netscape-style plug-in scripting environment allows plug-ins to access scripting languages such as JavaScript (including accessing script elements such as a web page’s Document Object Model). It also allows scripting languages to access and control elements of the plug-in.

In OS X v10.5 and earlier, Netscape-style plug-ins can be compiled in OS X into either the Mach-O or PEF (CFM) binary format (although CFM is PowerPC-only). Beginning in OS X v10.6, Netscape-style plug-ins should be updated to use a 64-bit binary to work with 64-bit instances of Safari or other WebKit clients. To do this, they must be built as 32/64-bit multi-architecture binaries using the Mach-O file format.

Though the API supports both formats, OS X natively supports the Mach-O style, and you will find that your plug-in will run much faster if compiled as a Mach-O binary. In the future, WebKit will continue to support Netscape plug-ins built with the Mach-O format; no such assurance can be given for plug-ins compiled in the PEF (CFM) format. You can also develop and debug Mach-O plug-ins in Xcode, but not PEF plug-ins. Once compiled, the plug-ins can be installed and used in most web browsers.

The scripting capabilities of Netscape-style plug-ins are provided by extensions onto the original plug-in specification. They allow a browser (through JavaScript) to access and control elements of the plug-in and its content, and allow the plug-in to access the enclosing web page and its content through the plug-in script interface.

When a plug-in is loaded, the browser calls the `NPP_GetValue` callback in your plug-in, which returns a retained `NPObject` structure that represent your plug-in. This `NPObject` structure contains an pointer to an `NPClass` structure. The `NPClass` structure contains a series of callbacks that define the interface between the plug-in and the scripting environment. The `NPObject` instance represents an instance of that plug-in that can then be used by the scripting environment.

If you want your plug-in to be scriptable, you need to return the appropriate retained `NPObject` by reference in your `NPP_GetValue` callback function.

A good demonstration of accessing plug-ins from JavaScript, as well as all the other concepts in creating a Netscape plug-in, can be found in the Examples folder of the WebKit source code. See [http://www.webkit.org/](http://www.webkit.org/) to learn how to download the WebKit source code.

Safari 4.0 provides two new drawing models: Core Graphics (Quartz 2D) and Core Animation (only in OS X v10.5 and later). These drawing modes are strongly recommended going forwards, and if you move your plug-in to contain a 64-bit slice, that slice must use these drawing models. (See [Transitioning a Netscape-Style Plug-in to 64-bit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi2talktk4yq) for more information.)

Most of the effort in using these drawing models comes from learning Core Graphics and Core Animation themselves. To learn about Core Graphics, read _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_. To learn about Core Animation, read _[Core Animation Programming Guide](../../Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmju)_.

Once you understand how to draw things using Core Graphics or Core Animation, you can enable these drawing models in your `NPP_New` function as follows:

- Add support in your code for the Cocoa event model. Core Graphics and Core Animation are not supported when using the Carbon event model.

- Check to see if the host browser supports the drawing model with the following code:

```swift
NPBool supportsCG = false;
NPError error = browser->getvalue(instance,
    NPNVsupportsCoreGraphicsBool,
    &supportsCG);
```
- Set the browser drawing model with the following code:

```swift
if (err == NPERR_NO_ERROR && supportsCG) {
    error = browser->setvalue(instance,
        NPNVpluginDrawingModel,
        (void *)NPDrawingModelCoreGraphics);
    if (err == NPERR_NO_ERROR && supportsCG) {
        /* Set state flags as needed to
           tell your own code to use Core Graphics
           drawing in the future. */
    }
}
```

After you have done these two things, the browser fills the `window` field of the `NPWindow` structure with an `NP_CGContext` structure. This structure contains two fields, `context` and `window`, which are defined as follows:

```
typedef struct NP_CGContext
{
    CGContextRef context;
    WindowRef window;
} NP_CGContext;
```

The `context` value is a Core Graphics drawing context suitable for Quartz 2D drawing. For more information on how to use this context, read _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_. The window is a reference to an `NSWindow` object.

To obtain the bounds for your plug-in’s drawing region, do the following in your `NPP_SetWindow` callback:

```
NPError setwindow_cb(NPP instance, NPWindow* npw) {
    ...

    NP_CGContext *npcontext = npw.window;
    CGContextRef context = npcontext.context;
    CGRect boundingBox = CGContextGetClipBoundingBox(context);

    ...
```

The Core Animation model is similar, but reversed. If you set you set `NPNVpluginDrawingModel` to `NPDrawingModelCoreAnimation`, your `NPN_GetValue` callback must provide a retained Core Animation layer to the browser when it queries the `NPPVpluginCoreAnimationLayer` variable.

As with the Core graphics model, you can find out if the browser supports the Core Animation drawing model by checking the value of the `NPNVsupportsCoreAnimationBool` variable. For example:

```swift
NPBool supportsCA = false;
NPError error = browser->getvalue(instance,
    NPNVsupportsCoreAnimationBool,
    &supportsCA);
```


Beginning in OS X v10.6, on 64-bit-capable computers, Netscape-style plug-ins execute in an out-of-process fashion. This means that each Netscape-style plug-in gets its own process separate from the application process. This design applies to all Netscape-style plug-ins. It does not apply to WebKit plug-ins, nor at present to WebKit-based applications when running in 32-bit mode.

Out-of-process execution is used for several reasons:

- Stability—crashes in plug-ins no longer crash the entire browser.
- Security—vulnerabilities in a plug-in can't read or alter data or code in other plug-ins or in the application itself.

For your plug-in to work correctly in this new environment, you may need to make some changes to your code, depending on how it interacts with the rest of the system beyond the browser.

- __Avoid direct data structure access.__ If you directly access application data structures (menus, other windows, etc.), your plug-in will fail. All access to browser data structures should be performed through approved APIs. If no API exists, file a bug and request that one be added.
- __Draw when asked.__ Your plug-in _must_ respond to `drawRect` event.
- __Draw only when asked.__ Any drawing your plug-in performs within the graphics context that Safari provides should take place in response to an `update` event (Carbon event model) or a `drawRect` event (Cocoa event model). The behavior of drawing performed at other times is undefined.

  To provide support for animation, video, and other drawing outside the context of `update` or `drawRect` events, you should move your code to use the Core Animation drawing model, described in [Core Graphics and Core Animation Drawing Models](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi2talktk4za).
- __Get all events through the plug-in API.__ Because keyboard and mouse events are happening in a different process, if you use Carbon or Cocoa calls to obtain data from the event stream, you will not receive any events.

  It is safe to use Carbon or Cocoa calls to obtain global system state information that is outside the scope of the event stream, such as mouse position, modifier keys, and other similar information.
- __Use platform APIs sparingly.__ Wherever possible, you should use new plug-in APIs to do what you need. If no such APIs exist, file bugs requesting them.

  The plug-in API provides additional APIs for scheduling timers, opening contextual pop-up menus, and so on.
- __Avoid creating windows.__ The intent is for plug-ins to operate within the browser window. Although some plug-ins have historically done so, creating windows in your plug-in is not recommended. If you need to maintain separate windows, you should consider starting a separate application.

Beginning in Snow Leopard, Safari is moving to a 64-bit process. This section describes how to adapt a Netscape-style plug-in so that it works when compiled as a 64-bit plug-in. It describes only the changes specific to Netscape-style plug-ins, providing links to other documents for general 64-bit porting information.

Before you begin, do the following:

- If your plug-in is built using PEF (CFM) compilers (CodeWarrior, for example), you must move to a modern toolchain that generates Mach-O binaries. There are no 64-bit compilers available that support PEF. The easiest way to do this is to transition your project to Xcode. For more information, read _[Porting CodeWarrior Projects to Xcode](../../Developer%20Tools/Porting%20CodeWarrior%20Projects%20to%20Xcode/Introduction%20to%20Porting%20CodeWarrior%20Projects%20to%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydq)_.
- You must convert your GUI code from Carbon to Cocoa (or other graphical APIs that are supported in a 64-bit environment). For more information on supported and unsupported Carbon APIs, read _[64-Bit Guide for Carbon Developers](../../Carbon/64-Bit%20Guide%20for%20Carbon%20Developers/Introduction%20to%2064-Bit%20Guide%20for%20Carbon%20Developers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobr)_. Then, read _[Cocoa Fundamentals Guide](../../Cocoa/Cocoa%20Fundamentals%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzu)_ to get started learning Cocoa. The preferred APIs for drawing are described further in [Core Graphics and Core Animation Drawing Models](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi2talktk4za).
- If your plug-in uses any Cocoa APIs, read _[64-Bit Transition Guide for Cocoa](../../Cocoa/64-Bit%20Transition%20Guide%20for%20Cocoa/Introduction%20to%2064-Bit%20Transition%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denbx)_ to learn what other Cocoa-specific changes you need to make to this code.
- Read _[64-Bit Transition Guide](../../Darwin/64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru)_ to learn about 64-bit changes that apply to all software written in C-based languages.

Once you have read these documents, you need to make a few additional changes specific to Netscape-style plug-ins (at least when compiling 64-bit versions of your plug-in). These changes are as follows:

- __Use Cocoa Events.__ In a 64-bit environment, you must convert your code to use the Cocoa event model because the Carbon event model is not supported. This requires several changes:

  - Use the `NPCocoaEvent` data type with the Cocoa event model instead of the `NPEvent` data type. The `NPCocoaEvent` data type provides neatly broken out fields containing various pieces of information about the event, and is fairly self-explanatory.
  - Disable the Carbon model test code (including the test to see if the Carbon model is supported) when compiling for 64-bit by wrapping the relevant code with the `#ifndef __LP64__` and `#endif` C preprocessor directives.

    The `NPEventModelCarbon` constant (for use with the `NPNVpluginEventModel` variable) and the `NPNVsupportsCarbonBool` constant (for use with `NPN_GetValue`) are not defined at all in a 64-bit environment. By using the C preprocessor directives above, you prevent the compiler itself from ever seeing the intervening lines of code, thus avoiding a compile failure.

  Bring up your Cocoa event model code in 32-bit first. This makes it possible to test the Cocoa event code in isolation without having to worry about bugs specific to the 64-bit environment.

  Do not remove your Carbon event model code, however. Although the Cocoa event model is supported in 32-bit WebKit beginning in OS X v10.6, it may not be supported in other browsers that use Netscape-style plug-ins, nor in earlier versions of WebKit.

  For maximum backwards compatibility and cross-browser compatibility, you should check the `NPNVsupportsCarbonBool` and `NPNVsupportsCocoaBool` variable using `NPN_GetValue` to determine which event models the browser supports. If the browser supports both event models, you should use the Cocoa event model. Otherwise, use the Carbon event model.

  For testing purposes, simply hard-wire your test to always use the Cocoa event model.
- __Replace QuickDraw.__ The QuickDraw drawing model is not supported. You must rewrite any QuickDraw code using another drawing model such as the Core Graphics or Core Animation drawing modes.

  As a result, the `NPDrawingModelQuickDraw` constant (for use with the `NPNVpluginDrawingModel` variable) and the `NPNVsupportsQuickDrawBool` constant (for use with the `NPN_GetValue` function) are not defined. Thus, any code that tests for the availability of the QuickDraw drawing model must be wrapped with `#ifdef __LP64__` and `#endif` C preprocessor directives.

  Similarly, the `NPQDRegion` and `NP_Port` data types are not defined.

  In the `NP_CGContext` data type, the `window` field may be either a `WindowRef` instance or an `NSWindow` instance in 32-bit WebKit depending on the drawing model chosen. Because Carbon drawing APIs are not supported, these fields always contain an `NSWindow` instance in 64-bit WebKit.

  For more information about the Core Graphics and Core Animation drawing models, see [Core Graphics and Core Animation Drawing Models](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi2talktk4za).

Once you have accounted for these differences, you should be ready to compile your plug-in with a 64-bit slice. For more information on compiling code for 64-bit, fixing truncation bugs, and various other relevant topics, read _[64-Bit Transition Guide for Cocoa](../../Cocoa/64-Bit%20Transition%20Guide%20for%20Cocoa/Introduction%20to%2064-Bit%20Transition%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denbx)_ and _[64-Bit Transition Guide](../../Darwin/64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru)_.

[Next](Creating%20Legacy%20Plug-ins%20with%20Cocoa%20and%20WebKit.md)[Previous](About%20Web%20Browser%20Plug-ins.md)

