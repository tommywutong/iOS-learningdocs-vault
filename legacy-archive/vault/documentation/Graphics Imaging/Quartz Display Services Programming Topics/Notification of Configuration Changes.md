---
title: Quartz Display Services Programming Topics
apple_id: TP40004316
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzDisplayServicesConceptual/Articles/Notification.html
archived_at: '2026-07-15T07:38:03.650297Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Display Services Programming Topics](Introduction%20to%20Quartz%20Display%20Services%20Programming%20Topics.md)


[Next](Controlling%20the%20Mouse%20Cursor.md)[Previous](Using%20Fade%20Effects.md)

# Notification of Configuration Changes

Quartz Display Services provides a general notification mechanism for applications that need to know about display configuration changes. Any application can register a display reconfiguration callback function. At several points during reconfiguration, Quartz passes to your callback function the display ID, status flags, and optional private data. During a display mode change, for example, you could use a callback to print a log message that describes the new mode.

Quartz invokes your callback function when:

- Your application calls a function to reconfigure a local display
- Your application is listening for events in the event-processing thread, and another application calls a function to reconfigure a local display
- The user changes the display hardware configuration—for example, by disconnecting a display or changing a system preferences setting

Before display reconfiguration, Quartz invokes your callback function once for each online display to indicate a pending configuration change. The `kCGDisplayBeginConfigurationFlag` flag is always set. After display reconfiguration, Quartz invokes your callback function once for each added, removed, and online display. The flags indicate how the display configuration has changed.

Cocoa already uses this notification mechanism to respond to display reconfigurations. As a result, when a user or application changes a display mode, turns on mirroring, or disconnects a display, Cocoa applications don’t need to be concerned with repositioning or resizing their windows. The application frameworks handle this task automatically.

If you want to receive notifications of configuration changes, here is a brief description of the steps:

1. Register your notification callback function.

```
CGDisplayRegisterReconfigurationCallback (MyDisplayReconfigurationCallBack, &userInfo);
```
2. When your function is called, check the parameters to see if action is required. For example:

```
void MyDisplayReconfigurationCallBack (
   CGDirectDisplayID display,
   CGDisplayChangeSummaryFlags flags,
   void *userInfo)
{
    if (flags & kCGDisplaySetModeFlag) {
        /* handle mode change for this display */
    }
}
```
3. When you no longer require notification, remove the callback registration.

```
CGDisplayRemoveReconfigurationCallback (MyDisplayReconfigurationCallBack, &userInfo);
```

[Next](Controlling%20the%20Mouse%20Cursor.md)[Previous](Using%20Fade%20Effects.md)

