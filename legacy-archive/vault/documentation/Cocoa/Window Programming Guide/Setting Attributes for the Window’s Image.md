---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/SettingWindowImageAttr.html
archived_at: '2026-07-15T07:21:17.572035Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Handling%20Events%20in%20Windows.md)[Previous](Setting%20a%20Window%E2%80%99s%20Title%20and%20Represented%20File.md)

# Setting Attributes for the Window’s Image

Nearly every window has a corresponding display window device in the window server. The window device holds the window’s drawn image, and has two attributes determined by the window server and many attributes that the window controls. The window server assigns the window device a unique identifier (within an application). This is the _window number_, and it can be accessed using the [windowNumber](https://developer.apple.com/documentation/appkit/nswindow/1419068-windownumber) method. Each window also has a _graphics state_ that most of its views share for drawing (views can create their own as well). The [gState](https://developer.apple.com/documentation/appkit/nswindow/1419412-gstate) method returns its identifier. The attributes under direct window control are the following:

- __Backing store type__, described in [Specifying How To Store the Window’s Image](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztiljxgq2dmny)
- __Backing location__, described in [Specifying Where To Store the Window’s Image](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztilktk4yq)
- __Window device creation__, described in [Specifying When the Window’s Image Is Created](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztiljxgqytaoa)
- __One shot__, described in [Specifying Whether the Window’s Image Persists When Offscreen](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztiljrgeytcmrq)
- __Depth limit__, described in [Specifying the Depth Limit for the Window’s Image](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztiljrgeytcmzw)
- __Dynamic depth limit__, described in [Specifying Whether the Depth Limit Changes to the Screen’s Capacity](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztiljxgqzdsnq)
- __Content sharing__, described in [Specifying Whether Window Content Can Be Read or Written by Another Process](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztilktk4za).

A window device’s _backing store_ type determines how the window’s image is stored. It’s set when the window is initialized and can be one of three types.

A _buffered window_ device renders all drawing into a display buffer and then flushes it to the screen. Always drawing to the buffer produces very smooth display, but can require significant amounts of memory. Buffered windows are best for displaying material that must be redrawn often, such as text. You must also use buffered windows if you want your windows to support transparency.

A _retained window_ device also uses a buffer, but draws directly to the screen where possible and to the buffer for any portions that are obscured.

A _nonretained window_ device has no buffer at all, and must redraw portions as they’re exposed. Further, this redrawing is suspended when the window’s display mechanism is preempted. For example, if the user drags a window across a nonretained window, the nonretained window is “erased” and isn’t redrawn until the user releases the mouse.

Both retained and nonretained windows are also subject to a flashing effect as individual drawing operations are performed, but their results do get to the screen more quickly than those of buffered windows.

You can change the backing store type between buffered and retained after initialization using the [setBackingType:](https://developer.apple.com/documentation/appkit/nswindow/1419599-backingtype) method.

The window server chooses whether to place the backing store for a buffered window in main memory or video memory. It will choose the location that provides the best overall performance. You can query the window server to determine where your window’s backing store is located using the [preferredBackingLocation](https://developer.apple.com/documentation/appkit/nswindow/1419102-preferredbackinglocation) method.

You may choose to set a preferred location for a Window’s backing store using the [setPreferredBackingLocation:](https://developer.apple.com/documentation/appkit/nswindow/1419102-preferredbackinglocation) method. While the window server is not required to respect this preferred backing location, it will attempt to do so. You should not change the preferred backing location without testing how it affects the performance of your application.

The `defer` argument to the initializer specifies whether the window creates its window device immediately or only when it’s moved on screen. Deferring creation of the window device can offer some performance gain for windows that aren’t displayed immediately because it reduces the amount of work that needs to be performed up front. Deferring creation of the window device is particularly useful when creation of the window itself can’t be deferred or when an window is needed for purposes other than displaying content. Submenus with key equivalents, for example, must exist for the key equivalents to work, but may never actually be displayed.

Memory can also be saved by destroying the window device when the window is removed from the screen. The [setOneShot:](https://developer.apple.com/documentation/appkit/nswindow/1419222-oneshot) method controls this behavior. One-shot window devices exist only when their windows are onscreen.

Like the display hardware, a window device’s buffer has a depth, or a limit to the memory allotted each pixel. Buffered and retained windows start out with the same depth as the main display or 16 bits, whichever is deeper. These settings stay in effect unless changed using the [setDepthLimit:](https://developer.apple.com/documentation/appkit/nswindow/1419613-depthlimit) method, which takes as an argument a window depth limit created using the [NSBestDepth](https://developer.apple.com/documentation/appkit/1473812-nsbestdepth) function.

Keeping a window’s depth at its richest preserves the displayed image, but may incur unnecessary memory overhead when the window buffer depth is deeper than the screen depth. You can use the [setDynamicDepthLimit:](https://developer.apple.com/documentation/appkit/nswindow/1419473-setdynamicdepthlimit) method to tell a window to match the depth of the screen it’s on. When it’s moved to a new screen, a window with a dynamic depth limit adjusts its buffer to the new depth before redrawing. Making a window’s depth limit dynamic overrides the limit set using [setDepthLimit:](https://developer.apple.com/documentation/appkit/nswindow/1419613-depthlimit), and removing the dynamic limit reverts the window to the default limit.

The contents of your window can be made available to other processes. By default, the contents of your window can be read but not written to by other processes. This allows system services to work with your window’s contents and also allows other applications to capture a snapshot of your windows contents.

You can override the default behavior using the [setSharingType:](https://developer.apple.com/documentation/appkit/nswindow/1419729-sharingtype) method. Changing the sharing type to [NSWindowSharingNone](https://developer.apple.com/documentation/appkit/nswindowsharingtype/nswindowsharingnone) prevents other systems from capturing your window’s image data. If you do this, however, your window will not be able to participate in a number of system services; therefore, this setting should be used with caution. If you set your window’s sharing type to [NSWindowSharingReadWrite](https://developer.apple.com/documentation/appkit/nswindowsharingtype/nswindowsharingreadwrite), other processes can both read and modify the window’s content.

[Next](Handling%20Events%20in%20Windows.md)[Previous](Setting%20a%20Window%E2%80%99s%20Title%20and%20Represented%20File.md)

