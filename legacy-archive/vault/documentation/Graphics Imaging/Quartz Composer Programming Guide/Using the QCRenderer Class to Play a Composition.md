---
title: Quartz Composer Programming Guide
apple_id: TP40001357
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzComposer/qc_play_renderer/qc_play_renderer.html
archived_at: '2026-07-15T07:37:15.683195Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Composer Programming Guide](Introduction%20to%20Quartz%20Composer%20Programming%20Guide.md)


[Next](Adding%20Compositions%20to%20Webpages%20and%20Widgets.md)[Previous](Publishing%20Ports%20and%20Binding%20Them%20to%20Controls.md)

# Using the QCRenderer Class to Play a Composition

The [QCRenderer](https://developer.apple.com/documentation/quartz/qcrenderer) class is a simplified runtime object that can load and play a composition to an arbitrary OpenGL context. `QCRenderer` also provides an interface to pass data to the input ports or retrieve data from the output ports of the root macro patch of a composition.

This chapter shows how to create a `QCRenderer` object for a full screen OpenGL context and then load and render a Quartz Composer composition to that context. The sample code is part of a Cocoa application created using Xcode. Before reading this chapter, you may want to look at _[QCRenderer Class Reference](https://developer.apple.com/documentation/quartz/qcrenderer)_.

Each section in this chapter provides a code fragment and an explanation of the essential parts of the code fragment. To see how to put all the code together into a complete, working application, you will need to open, build, and run the Player sample application that’s provided with the OS X v10.5 developer tools. See [Building and Running the Player Sample Project](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqhewueqkkineeiskd).

The following tasks are essential to creating a sample application that plays a full-screen composition using a `QCRenderer` object. Each is described in more detail in the rest of the chapter.

1. [Declaring the Application Interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqhewueqkkirfeqrkf)
2. [Getting a Composition File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqhewueqkkizdeessg)
3. [Capturing the Main Display](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqhewueqkkjfcecscc)
4. [Setting Up the OpenGL Context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqhewueqkkjbfeiskb)
5. [Setting Up Full Screen Display and Syncing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqhewueqkki5eeiscg)
6. [Creating a QCRenderer Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqhewueqkkineecrcg)
7. [Creating a Timer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqhewueqkkjfcesqkg)
8. [Writing the Rendering Routine](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqhewueqkkireekssj)
9. [Overriding the sendEvent Method](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqhewueqkkizauorsd)

This application is one of the rare ones that requires you to subclass `NSApplication`. You need to create a subclass so that you can override the `sendEvent:` method to catch user events while the application is displaying a full-screen OpenGL context, and also to set the `NSApplication` instance as its own delegate. See _[NSApplication Class Reference](https://developer.apple.com/documentation/appkit/nsapplication)_ for more information.

You need to replace the principal class (`NSApplication`) by your custom subclass of `NSApplication` (in this example, PlayerApplication) in the `Info.plist` file. Open the `Info.plist` file from within Xcode, then find the following key-value pair:

```
<key>NSPrincipalClass</key>
<string>NSApplication</string>
```

Then replace `NSApplication` with the name of the subclass. For this example, the revised key-value pair would look as follows:

```
<key>NSPrincipalClass</key>
<string>PlayerApplication</string>
```

[Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqhewueqkkizcemrsd) shows the interface for PlayerApplication, which requires variables to create the OpenGL context, `QCRenderer`, and other objects that support rendering a composition.

__Listing 3-1__  The interface for PlayerApplication

```objc
@interface PlayerApplication : NSApplication
{
    NSOpenGLContext* _openGLContext;
    QCRenderer*      _renderer;
    NSString*        _filePath;
    NSTimer*         _renderTimer;
    NSTimeInterval   _startTime;
    NSSize           _screenSize;
}
@end
```


A [QCRenderer](https://developer.apple.com/documentation/quartz/qcrenderer) object requires an OpenGL context and a Quartz Composer file for its creation. If the user drags a composition to your application icon, implement this `NSApplication` delegate method to retain the file pathname for later use when you create the `QCRenderer` object.

```objc
- (BOOL) application:(NSApplication*)theApplication
                    openFile:(NSString*)filename
{
    _filePath = [filename retain];

    return YES;
}
```

If the user opens your application by double-clicking its icon, ask the user to specify a composition and then retain the file pathname by including the following code in the `applicationDidFinishLaunching:` delegate method.

```
NSOpenPanel *openPanel;

if(_filePath == nil)
    {
        openPanel = [NSOpenPanel openPanel];
        [openPanel setAllowsMultipleSelection:NO];
        [openPanel setCanChooseDirectories:NO];
        [openPanel setCanChooseFiles:YES];
        if([openPanel runModalForDirectory:nil
                    file:nil
                    types:[NSArray arrayWithObject:@"qtz"]] != NSOKButton)
            {
                NSLog(@"No composition file specified");
                [NSApp terminate:nil];
            }
        _filePath = [[[openPanel filenames] objectAtIndex:0] retain];
    }
```


The Quartz Services programming interface provides functions that configure and control displays. Use its functions to capture the main screen and cache its dimensions. See _[Quartz Display Services Reference](https://developer.apple.com/documentation/coregraphics/quartz_display_services)_ for more information on these functions.

You can capture the main display by using the code in Listing 3-2. A detailed explanation for each numbered line of code follows the listing.

__Listing 3-2__  Code that captures the main display

```
CGDisplayCapture (kCGDirectMainDisplay);// 1
CGDisplayHideCursor (kCGDirectMainDisplay);
_screenSize.width = CGDisplayPixelsWide(kCGDirectMainDisplay);// 2
_screenSize.height = CGDisplayPixelsHigh(kCGDirectMainDisplay);
```

Here what the code does:

1. Captures the main display. Capturing the screen is important because later you’ll set the receiver of the OpenGL context to full screen mode. A captured display prevents contention from other applications and system services. In addition, applications are not notified of display changes, preventing them from repositioning their windows and the Finder from repositioning desktop icons.
2. Caches the screen dimensions. The rendering method uses the screen dimensions to normalize the mouse coordinates. See [Writing the Rendering Routine](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqhewueqkkireekssj).

An OpenGL context pixel format requires a pixel format that specifies the buffers (depth buffer, alpha buffer, stencil buffer, and accumulation buffer) as well as other attributes of a context. Listing 3-3 shows how to set up an OpenGL context. A detailed explanation for each numbered line of code follows the listing.

__Listing 3-3__  Setting up an OpenGL context

```
NSOpenGLPixelFormat *format;// 1
NSOpenGLPixelFormatAttribute attributes[] = {// 2
                    NSOpenGLPFAFullScreen,
                    NSOpenGLPFAScreenMask,
                    CGDisplayIDToOpenGLDisplayMask(kCGDirectMainDisplay),
                    NSOpenGLPFANoRecovery,
                    NSOpenGLPFADoubleBuffer,
                    NSOpenGLPFAAccelerated,
                    NSOpenGLPFADepthSize,
                    24,
                    (NSOpenGLPixelFormatAttribute) 0
                };

format = [[[NSOpenGLPixelFormat alloc] initWithAttributes:attributes]
                                         autorelease];// 3
_openGLContext = [[NSOpenGLContext alloc] // 4
                    initWithFormat:format
                    shareContext:nil];
if(_openGLContext == nil) // 5
    {
        NSLog(@"Cannot create OpenGL context");
        [NSApp terminate:nil];
    }
```

Here’s what the code does:

1. Declares storage for an [NSOpenGLPixelFormat](https://developer.apple.com/documentation/appkit/nsopenglpixelformat) object. You specify a format when you create an OpenGL context.
2. Sets up the attributes for the pixel format. These attributes specify, among other things, a full-screen context and a depth buffer. _[NSOpenGLPixelFormat Class Reference](https://developer.apple.com/documentation/appkit/nsopenglpixelformat)_ provides a complete description of the available format attributes. At the very least, you must provide a color buffer and a depth buffer for the `QCRenderer` object.
3. Allocates a pixel format object and initializes it with the pixel format attributes.
4. Allocates an OpenGL context and initializes it with the pixel format object.
5. Checks to make sure the OpenGL context is not nil. If it is, the application must terminate.

You need to set the OpenGL context to full-screen mode and then set the swap interval to `1` to ensure that the buffers are swapped only during the vertical retrace of the monitor. If the buffers aren’t synchronized with the retrace, the composition could render with tearing artifacts. (For more information on swap intervals, see _[OpenGL Programming Guide for Mac](../OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_.)

```
long    value = 1;

[_openGLContext setFullScreen];
[_openGLContext setValues:&value forParameter:kCGLCPSwapInterval];
```


A [QCRenderer](https://developer.apple.com/documentation/quartz/qcrenderer) object requires an OpenGL context, the OpenGL pixel format, and a file pathname. If for some reason the renderer can’t be created, the application must terminate. Use the following code to create the renderer and check for its creation.

```
_renderer = [[QCRenderer alloc]
            initWithOpenGLContext:_openGLContext
            pixelFormat:format
            file:_filePath];
if(_renderer == nil)
    {
        NSLog(@"Cannot create QCRenderer");
        [NSApp terminate:nil];
    }
```


You need to set up a timer to regularly render the composition. This timer set up in the following code is scheduled to fire 60 times per second. Each time it fires, it invokes the render routine that’s created in the next section. If the timer can’t be created, the application must terminate, so make sure you include code to check for the existence of the timer. For more information on times, see _[NSTimer Class Reference](https://developer.apple.com/documentation/foundation/timer)_.

```
#define kRendererFPS 60.0

_renderTimer = [[NSTimer scheduledTimerWithTimeInterval:(1.0 /
                                (NSTimeInterval)kRendererFPS)
                        target:self
                        selector:@selector(_render:)
                        userInfo:nil
                        repeats:YES]
                        retain];
if(_renderTimer == nil)
    {
        NSLog(@"Cannot create NSTimer");
        [NSApp terminate:nil];
    }
```


When the timer fires or when a user event needs to be processed, the `renderWithEvent:` method is invoked. Recall that for this application the timer is set to fire 60 times per second. Listing 3-4 shows the `_render` and `renderWithEvent:` methods. A detailed explanation for each numbered line of code follows the listing.

__Listing 3-4__  The rendering methods

```objc
- (void) _render:(NSTimer*)timer
{
    [self renderWithEvent:nil];
}

- (void) renderWithEvent:(NSEvent*)event
{
    NSTimeInterval  time = [NSDate timeIntervalSinceReferenceDate];
    NSPoint             mouseLocation;
    NSMutableDictionary  *arguments;

    if(_startTime == 0)// 1
    {
        _startTime = time;
        time = 0;
    }
    else
        time -= _startTime;

    mouseLocation = [NSEvent mouseLocation];// 2
    mouseLocation.x /= _screenSize.width;// 3
    mouseLocation.y /= _screenSize.height;// 4
    arguments = [NSMutableDictionary dictionaryWithObject:[NSValue // 5
                    valueWithPoint:mouseLocation]
                    forKey:QCRendererMouseLocationKey];
    if(event)// 6
        [arguments setObject:event forKey:QCRendererEventKey];
    // Your code to set input port values // 7
    if(![_renderer renderAtTime:time arguments:arguments])// 8
                NSLog(@"Rendering failed at time %.3fs", time);
    // Your code to get output port values// 9
    [_openGLContext flushBuffer];// 10
}
```

Here’s what the code does:

1. Computes the composition time as the difference between the current time and the time at which rendering started.
2. Gets the current mouse position, in screen coordinates. Mouse coordinates need to be normalized relative to the OpenGL context viewport (`[0,1],x[0,1]`) with the origin `(0,0)` at the lower-left corner.
3. Normalizes the x mouse coordinate.
4. Normalizes the y mouse coordinate.
5. Creates a dictionary and writes the normalized mouse coordinates to it. Coordinates are specified as an [NSPoint](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSPoint) object stored in an [NSValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/cl/NSValue) object.
6. If there is a user event, adds it to the arguments dictionary.
7. This is where you could add code to set the value for an input parameter that’s published to the root macro patch of a composition. You use the method `setValue:forInputKey:`, making sure to pass a valid key.
8. Renders a frame at the specified time, passing the arguments dictionary.
9. This is where you could add code to retrieve the value of a published output parameter. You use the method `valueForOutputKey:`, making sure to pass a valid key.
10. Flushes the OpenGL context to display the rendered frame onscreen.

Recall that this example subclasses `NSApplication` so that it could override the `sendEvent:` method to ensure that user events are processed while there is a full screen OpenGL context on screen. The `sendEvent:` method in Listing 3-5 checks for:

- An Escape key press, and terminates the application if there is one.
- A meaningful event for the composition, and invokes the renderer immediately with such an event.

__Listing 3-5__  The overridden event-sending method

```objc
#define kRendererEventMask (NSLeftMouseDownMask|NSLeftMouseDraggedMask |
                    NSLeftMouseUpMask | NSRightMouseDownMask |
                    NSRightMouseDraggedMask | NSRightMouseUpMask |
                    NSOtherMouseDownMask | NSOtherMouseUpMask |
                    NSOtherMouseDraggedMask | NSKeyDownMask |
                    NSKeyUpMask | NSFlagsChangedMask |
                    NSScrollWheelMask)

- (void) sendEvent:(NSEvent*)event
{
    if(([event type] == NSKeyDown) && ([event keyCode] == 0x35))
            [NSApp terminate:nil];

    if(_renderer && (NSEventMaskFromType ([event type]) &
                 kRendererEventMask))
            [self renderWithEvent:event];
    else
    [       super sendEvent:event];
}
```


The best way to experiment with using the [QCRenderer](https://developer.apple.com/documentation/quartz/qcrenderer) class is to build and run the Player sample application that’s supplied with the OS X v10.5 developer tools. After installing the developer tools, you can find the Player Xcode project in the following location:

`/Developer/Examples/Quartz Composer Sample Code`

After you compile the Player application, you can open a composition in two ways. Either launch the application and specify a composition to play or drag a composition onto the Player application icon. To support opening a composition by dragging it to the application icon, you need to change the Info.plist file. Listing 3-6 shows the Info.plist file for the Player sample project. You can view this file from within Xcode by double-clicking Info.plist in the file list. Note that the listing has a `CFBundleTypeExtensions` key followed by the `qtz` extension.

__Listing 3-6__  Specifying the qtz extension in the Info.plist file

```
<key>CFBundleDocumentTypes</key>
    <array>
        <dict>
            <key>CFBundleTypeExtensions</key>
            <array>
                <string>qtz</string>
            </array>
        </dict>
    </array>
```


_[NSApplication Class Reference](https://developer.apple.com/documentation/appkit/nsapplication)_ discusses the class, its methods, and the cases for which you might want to subclass `NSApplication`.

[Next](Adding%20Compositions%20to%20Webpages%20and%20Widgets.md)[Previous](Publishing%20Ports%20and%20Binding%20Them%20to%20Controls.md)

