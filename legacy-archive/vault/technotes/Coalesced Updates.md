---
title: Coalesced Updates
apple_id: DTS10003496
resource_type: Technical Note
platform: macOS
topic: Performance
technology: ApplicationServices
published: '2010-08-31'
source_url: https://developer.apple.com/library/archive/technotes/tn2133/_index.html
archived_at: '2026-07-26T19:53:51.048760Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2133

# Coalesced Updates

Improving drawing performance by taking advantage of coalesced updates.

[Coalesced Updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbzgywugsbrfvjukq2ujfhu4mi)[How does this affect applications?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbzgywugsbrfvjukq2ujfhu4mq)[What tools can I use to tell if an application is being affected by coalesced updates?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbzgywugsbrfvjukq2ujfhu4my)[Quartz Debug](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbzgywugsbrfvjvkqstivbviskpjyzq)[Instruments](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbzgywugsbrfvjvkqstivbviskpjy2a)[Recommendations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbzgywugsbrfvjukq2ujfhu4nq)[General recommendations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbzgywugsbrfvjvkqstivbviskpjy3a)[Best Practices](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbzgywugsbrfvjvkqstivbviskpjy3q)[A last resort](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbzgywugsbrfvjvkqstivbviskpjy4a)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbzgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Coalesced Updates

Mac OS X 10.4 introduces a new behavior of coalescing updates that enables Quartz to more efficiently update the frame buffer during each display refresh. In addition to increasing system efficiency, coalescing updates improves visual consistency and eliminates "tearing" during scrolling and animation. To coalesce updates, the Quartz window server composites all window buffers into a single offscreen frame buffer before flushing it to the screen. When your application issues a command to flush, the system doesn't actually flush that content until the next available display refresh. This allows all updates for multiple applications to happen at the same time. Window server operations (window resize or move, for example) are handled in the same manner—coalesced into a system-wide screen update.

[Back to Top](#)

## How does this affect applications?

The majority of applications gain the benefit of coalesced updates, however, there are some situations where it can cause performance regressions. Regressions tend to fall into two categories:

- Over-flushing: Applications that draw and flush much faster than the display refresh are throttled down to the refresh rate. Ideally, applications should not draw faster than the display refresh, as it would be wasting time drawing pixels the user won't see on the display. Once a window has been drawn into and flushed the buffer needs to be locked in preparation for window server access, so an application can do anything it likes until that flush makes it to the screen except draw into the buffer again. If an application tries to draw immediately after a flush it will block until that flush actually completes, so if the application just misses a frame sync it has to wait around until the next one, and won't be able to start drawing the next frame in the meantime.
- Extended Drawing Interval: If an animation spends more time in its drawing routine than it takes for the screen to refresh, then it will become throttled to some factor of the refresh rate. So, if the refresh rate was 60 fps and the animation can run at most 55 fps, it will be throttled down to 30 fps.

[Back to Top](#)

## What tools can I use to tell if an application is being affected by coalesced updates?

If an application that has been built and linked on Mac OS X 10.4 and later is spending more time drawing than the same application built and linked on a previous system, then it is probably being affected by coalesced updates. There are two tools that can be used to verify if an application is or isn't being affected by coalesced updates, Quartz Debug and Instruments.

### Quartz Debug

Quartz Debug is a debugging tool for the Quartz graphics system with several powerful features to help you identify a number of graphics display and performance problems. Once the Mac OS X developer tools have been installed, the Quartz Debug application is located in: /Developer/Applications/Performance Tools/. To see the affect of effects of coalesced updates on applications, including CFM applications and applications linked on systems previous to 10.4, enable forced beam synchronization in Quartz Debug. An application that is being affected by coalesced updates will have a lowered frame rate when beam synchronization is enabled than when beam synchronization is disabled, and often will have increased CPU usage. To learn more about using Quartz Debug to see the effect of coalesced updates see [Q&A 1234, Debugging Graphics with QuartzDebug](https://developer.apple.com/qa/qa2001/qa1236.html).

### Instruments

Instruments is a profiling tool included with the Mac OS X developer tools distribution. Instruments can be used to profile an application and see if too much time is being spent in drawing operations, signaling that an application is having its updates coalesced. Once the Mac OS X developer tools have been installed, the Instruments profiling tool is located on the system at: /Developer/Applications/. If needed, use Quartz Debug to force beam synchronization then, in Instruments, sample your application using the "Time Profiler" instrument. If you see time more time spent in the `CGContext` drawing operations than you do with beam synchronization disabled, your application is having its updates coalesced.

To learn more about using Instruments for profiling please see the [Instruments User Guide.](https://developer.apple.com/mac/library/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/Introduction/Introduction.html)

[Back to Top](#)

## Recommendations

To applications, this doesn't really change what they should be doing; it just enforces what has been recommended in the past.

### General recommendations

- Flush once per update event.
- Consider periodic updates when live resizing and scrolling, and if needed draw lower quality results.
- While an application can get the current screen's refresh rate, the recommendation is to assume a refresh rate of 60 Hz.
- Applications in general shouldn't draw or flush faster than the user can see. Most animations only need a refresh rate of 30 fps, if an animation needs to update more often, then a timer should be used to limit animation rates to the refresh rate or less.
- Avoid, if possible, the functions that request an immediate flush to the screen. Applications drawing with Quartz should use `CGContextSynchronize` rather than `CGContextFlush`.
- In Cocoa use `NSView`'s `setNeedsDisplay:` to request an update for a view instead of the more immediate `display:`, and in Carbon's HIToolBox use `HIViewSetNeedsDisplay` or `HIViewSetNeedsDisplayInRegion` instead of the immediate `HIWindowFlush`.

### Best Practices

- In drawing routines, do all calculations then draw, minimizing the amount of time between first touching the context and being done with it. In windows that have complex drawing routines, this will minimize the time waiting for a context that is being flushed to be released for more drawing.
- It is a good idea for animations and screen updates to be time based and frame-limited in order to work best with coalesced updates. That is, they must make a fixed amount of progress per unit of time, rather than per frame, and they must not attempt to run at a rate greater than the refresh rate.
- Applications that are displaying more than a single animation at a time in one window need to arrange for all animations in a window to run off of the same timer, updating in the same round in the runloop, and flushing together.
- Decouple your visualization engine from your data engine so that neither engine will impede the other. Avoid network or disk access that would block the UI.

### A last resort

If your application cannot adopt any of the above solutions, it is possible to disable coalesced updates for your application. To disable coalesced updates for your application, set the key `CGDisableCoalescedUpdates` to the CFBoolean value of true in your Info.plist dictionary as shown in Listing 1. This key will only disable coalesced updates for applications running on Mac OS X 10.4.4 or later.

__Important:__ Disabling coalesced updates is recommended only as a solution of last resort. The system will still, on an as needed basis, force update coalescing on your application should the need arise. Additionally, by disabling coalesced updates your application can suffer from issues ranging from visual correctness to tearing during window updates.

__Listing 1__  Using `CGDisableCoalescedUpdates`, in an applications Info.plist, to disable coalesced updates on 10.4.4 and later.

```xml
<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"         "http://www.apple.com/DTDs/PropertyList-1.0.dtd"> <plist version="1.0"> <dict>     <key>CFBundleExecutable</key>     <string>GraphicsApp</string>     <key>CFBundleName</key>     <string>GraphicsApp</string>          ...          <key>CGDisableCoalescedUpdates</key>          <true/>          ...     <key>CFBundlePackageType</key>     <string>APPL</string>     <key>CFBundleSignature</key>     <string>grap</string>     <key>CFBundleVersion</key>     <string>1.0</string> </dict> </plist>
```

__Important:__ In order to maximize compatibility, all applications linked on systems before 10.4 (including all CFM apps, even if linked on 10.4) will not have their flush operations forced into a coalesced update cycle if that flush would only go out by itself. All accelerated surface flushes that go through the window server will be done via a coalesced update cycle. If an older application or one that disables coalesced updates in its Info.plist issues a flush and a coalesced update is already in progress though, then that flush will become part of the current coalesced update. This means that newer apps that want visual correctness will take precedence over older apps that are potentially trying to flush too quickly.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-08-31 | Editorial. Grammar and spelling fixes. |
| 2006-01-20 | Changed the CGDisableCoalescedUpdates key's value in the Info.plist listing to a CFBoolean true. |
| 2006-01-12 | New document that describes how to achieve the maximum frame rate in your Mac OS X application |

