---
title: Drawing Performance Guidelines
apple_id: 10000151i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/Drawing/Articles/FlushingContent.html
archived_at: '2026-07-18T01:47:12.041969Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Drawing Performance Guidelines](Introduction%20to%20Drawing%20Performance%20Guidelines.md)


[Next](Cocoa%20Live%20Window%20Resizing.md)[Previous](Measuring%20Drawing%20Performance.md)

# Flushing to the Window Buffer

If your program displays animated content, because it is a game or other multimedia-based application, your code should avoid updating your window content faster than the screen refresh rate. Drawing content to your local window buffer and flushing that content to the screen at more than 30 frames per second is usually a waste of CPU time. Most users cannot perceive updates at rates greater than 30 frames per second, so flushing more frequently is rarely needed.

Flush requests do not send the data to the screen immediately. Instead, flush requests are deferred until it is time to refresh the display. At that time, the window server coalesces the updates and pushes the changes to the graphics card. This new “coalesced update” behavior can cause a performance problem for applications that try to update their window buffers more frequently than the screen refresh rate. Drawing routines block the current thread until the window buffer has been completely flushed. With coalesced updates, this means your code could block for as much as 1/60th of a second.

To avoid performance problems, you should never draw or flush your window buffers faster than the screen refresh rate. If you typically draw your content and then immediately flush it to the screen, you can use timers to notify your code when it is time to draw. Simply set a timer to fire at the same frequency as the screen refresh rate and have it call your drawing routine.

If an application is spending more time drawing (or has a reduced frame rate) then the same application built and linked on a previous system, it is probably being affected by coalesced updates. The Quartz Debug tool lets you detect whether your application may be experiencing problems because of coalesced updates.

Quartz Debug is a debugging tool for the Quartz graphics system with several powerful features to help you identify a number of graphics display and performance problems. Quartz Debug is a part of a separate graphics tools release that can be downloaded from inside Xcode. From within Xcode, choose Xcode > Open Developer Tool > More Developer Tools.

To determine if coalesced updates are affecting your application, you use the beam sync tools and frame meter of Quartz Debug. With your application running, launch Quartz Debug, and do the following:

1. Choose Tools > Show Beam Sync Tools.
2. In the Beam Sync Tools dialog, choose the Force Beam Synchronization option. This causes coalesced updates to be used by all applications.
3. Choose Tools > Show Frame Meter.

If your application is affected by coalesced updates, its frame rate will be lower when beam synchronization is enabled. This lowered frame rate will often coincide with increased CPU usage as well. To learn more about using Quartz Debug to see the affect of coalesced updates see _[Debugging Graphics with QuartzDebug](https://developer.apple.com/library/archive/qa/qa1236/_index.html#//apple_ref/doc/uid/DTS10002281)_.

To ensure that your application's performance does not deteriorate when coalesced updates are enabled, you should follow the guidelines listed in the sections that follow. For additional drawing guidelines, see and [Cocoa Drawing Tips](Cocoa%20Drawing%20Tips.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinzqfvbecsskifdeori).

If you are using Quartz, you should avoid calling [CGContextFlush](https://developer.apple.com/documentation/coregraphics/cgcontext/1454895-flush) to force the automatic update of the window. Instead call [CGContextSynchronize](https://developer.apple.com/documentation/coregraphics/cgcontext/1455450-synchronize) to let Quartz determine the appropriate time at which to update the window.

If you are using Cocoa, you should avoid using [display](https://developer.apple.com/documentation/appkit/nsview/1483487-display) and its related method to force updates. Instead, use the [setNeedsDisplay:](https://developer.apple.com/documentation/appkit/nsview/1483360-needsdisplay) and [setNeedsDisplayInRect:](https://developer.apple.com/documentation/appkit/nsview/1483475-setneedsdisplayinrect) methods and let the run loop handle updates to those areas during the next update cycle.

If you must flush to the buffers, use a timer to synchronize your drawing cycles with the screen refresh rate. Flushing is also still appropriate in cases where your application needs to display some content once and cannot wait for the event loop, such as when displaying a splash screen.

Applications generally should not draw or flush faster than the user can see. For most graphics, a refresh rate of 30 frames per second is sufficient for smooth transitions. If your software needs to update at a faster rate, make sure that the rate does not exceed the refresh rate of the screen. For information about how to get the screen refresh rate, see [Getting the Refresh Rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmzvfuytcnzvgiya).

In your drawing routines, you should minimize the amount of time between when you first touch the graphics context and when you are done with it. This might mean decoupling your data engine from the graphics engine and reorganizing your code to perform any needed calculations prior to drawing. By performing any needed calculations first, you delay the point at which you need to actually touch the graphics context. If the context is currently being flushed, this can help minimize the time your application spends waiting for it.

You can get the current screen refresh rate from Quartz. The [CGDisplayCurrentMode](https://developer.apple.com/documentation/coregraphics/1562062-cgdisplaycurrentmode) function returns a dictionary of display properties. The refresh rate for the specified screen is associated with the [kCGDisplayRefreshRate](https://developer.apple.com/documentation/coregraphics/kcgdisplayrefreshrate) key. If the value of this key is 0, the screen is an LCD and you should assume a refresh rate of 60 Hz.

Listing 1 shows a sample function that gets the current refresh rate for the screen.

__Listing 1__  Getting the screen refresh rate

```
int GetMainScreenRefreshRate()
{
    CFDictionaryRef modeInfo;
    int refreshRate = 60; // Assume LCD screen

    modeInfo = CGDisplayCurrentMode(CGMainDisplayID());

    if (modeInfo)
    {
        CFNumberRef value = (CFNumberRef) CFDictionaryGetValue(modeInfo, kCGDisplayRefreshRate);

        if (value)
        {
            CFNumberGetValue(value, kCFNumberIntType, &refreshRate);
            if (refreshRate == 0)
                refreshRate = 60;
        }
    }

    return refreshRate;
}
```

[Next](Cocoa%20Live%20Window%20Resizing.md)[Previous](Measuring%20Drawing%20Performance.md)

