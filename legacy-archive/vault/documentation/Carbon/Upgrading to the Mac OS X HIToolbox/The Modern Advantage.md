---
title: Upgrading to the Mac OS X HIToolbox
apple_id: TP30001140
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2004-06-28'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Upgrading_HIToolbox/upgrading_hitoolbox_conc/upgrading_hitoolbox_conc.html
archived_at: '2026-07-15T05:24:42.278581Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Upgrading to the Mac OS X HIToolbox](Introduction%20to%20Upgrading%20to%20the%20Mac%20OS%20X%20HIToolbox.md)


[Next](Porting%20Steps.md)[Previous](Introduction%20to%20Upgrading%20to%20the%20Mac%20OS%20X%20HIToolbox.md)

# The Modern Advantage

If your Carbon user interface still uses classic Mac OS technologies—such as resources, the Dialog Manager, `WaitNextEvent`, QuickDraw, and procedure pointer–based custom window, menu, or control definitions—Apple encourages you to upgrade your code to use their modern Mac OS X replacements.

- Nib files are the modern replacement for resource files in creating and managing controls, windows, and menus.
- HIView is the object-oriented view system for implementing Carbon user interface elements in Mac OS X.
- Carbon events is the modern event messaging system for Carbon applications.
- Quartz is the modern drawing API in Mac OS X.

This chapter outlines the advantages of using these technologies.

Interface Builder provides an intuitive drag-and-drop method of laying out your user interface. It stores information about your interface in special nib files (or simply “nibs”) that you can then load into your Carbon application. It also allows you to set commonly-used values such as control/view IDs, window attributes, initial values, and so on. Because the nib file is independent of your executable file, you can make changes to your user interface without having to recompile any code. For example, you can reposition controls or adjust initial radio button or checkbox states by simply modifying the appropriate nib file.

Carbon events replaces the classic `WaitNextEvent` event handling model. It is both simpler to use and more sophisticated than its predecessor, and it offers improved performance.

Carbon events eliminate the need for polling; your application no longer has to query the system for events. Instead, you simply register for the events you want to receive. These events get dispatched directly to the relevant target where individual event handlers can then process the event.

With this event model, you no longer need boilerplate code in your application to obtain and dispatch events. In addition, you can replace many functions that polled the system with Carbon event handlers. Some examples:

- Instead of using `Button` to determine if the user pressed the mouse button, you simply register to be notified whenever the mouse button is pressed.
- In the past, if you wanted to implement a timer, you had to poll the system to determine how many ticks had passed. Now, you can simply install a Carbon event timer that calls a handler when the specified time has elapsed.
- If you wanted to change window elements as the mouse rolled over them, you used to have to poll for the mouse position. Now, you can register mouse tracking areas with the system, and you are notified with a Carbon event whenever the mouse enters or leaves a given area.

In addition, if you use the standard window handler, the Carbon Event Manager installs numerous default handlers, most of which do what you would have wanted to do anyway. For example, in a window containing multiple HIViews, pressing Tab automatically advances the keyboard focus. You also benefit from Apple updates. For example, if Apple improved the algorithm for determining how to advance the focus, your application would gain this benefit automatically.

The standard event handlers also make it easy for your application to support assistive devices, as mandated by section 508 of the Workforce Investment Act of 1998. If your application uses standard user interface elements, you gain this support automatically.

Compositing mode (which you should not confuse with Quartz compositing) is a special window setting that attempts to minimize the amount of necessary drawing; images are redrawn only when they change, and areas that are hidden beneath opaque views are never drawn. Compositing mode is available in Mac OS X v10.2 and later.

The Mac OS X HIToolbox uses the term HIView to refer to controls that have been modified to optionally or exclusively support compositing mode. At heart, an HIView is nothing more than a new name for the existing `ControlRef` type. The `HIViewRef` type is identical to the `ControlRef` type , both at the programming language level and the implementation level. You can use most standard Control Manager calls on them, as well as the new `HIViewXXX` functions.

For example, the pushbutton control is considered an HIView, because it can be used in either a compositing or non-compositing window. The ListBox control is not considered an HIView, because it cannot be used in a compositing window. The Scroll view, introduced in Mac OS X 10.2, is considered an HIView, and can be used only in compositing mode. The difference between a control and a view, therefore, is primarily one of implementation changes that allow the control to behave correctly in a compositing window.

Compositing mode results in a number of performance advantages. For example, implementing live window resizing or scrolling in the past often resulted in images and controls being redrawn multiple times. At best, this resulted in sluggish performance, and at worst there may have been flickering onscreen due to the multiple redraws. In contrast, when in compositing mode, drawing occurs only once during a given pass through the event loop, and no image or control is drawn more often than necessary. To gain the benefits of compositing mode, all drawing in your window must be done from within a compositing-aware view (either a standard view or a custom view that you have written). Classic window update events are not provided for compositing windows.

In addition, compositing mode respects the z-order (that is, the layering) of controls, which makes it much easier to manipulate controls or views independently of each other. You no longer have to worry about erasing backgrounds, keeping track of control hierarchies, or aligning patterns when drawing or redrawing controls. For example, if you partially cover one view with another, you do not need to keep track of which view is above which, or worry about what happens when a view redraws.

The HIView model introduces a number of new controls. Some of them simplify the work required to implement existing controls, while others provide new functionality altogether. Most work in both compositing and noncompositing windows.

- The combo box combines an editable text field and a pop-up menu.
- The scroll view automatically handles scrolling and live updating of scrollable information. By adopting this view, you no longer need to write code to calculate the positions of scroll thumbs or keep track of the content position. Note that the scroll view is available to windows only in compositing mode.
- The search field lets users enter search information, just as in Mail or Safari.
- The text view is a text container that uses the Multilingual Text Engine (MLTE). If you have only simple text-manipulation requirements, this view does most of the work for you.
- The web view provides an easy way to display HTML web content.
- The image view is a container for holding any sort of image.
- The segmented view is a segmented button much like the icon/list/column view switcher in the Finder.

In addition, if you want to create custom toolbar items in a toolbar, you must implement the items as custom HIViews.

The object-oriented nature of views makes it easier to customize; you can subclass or modify existing controls without too much effort, and the resulting code is much more portable. A custom view-based control may only require you to implement a few event handlers to override the behavior of a standard control. Another advantage to moving code “under the hood” is that when Apple fine-tunes, adds features, or otherwise improves functionality, your application can benefit automatically. You don’t have to worry about retuning your code to adopt every change, and there’s less likelihood of something breaking your code.

Quartz is the imaging model for Mac OS X. In terms of features and flexibility, it is far superior to QuickDraw. New Apple technologies will leverage the power of Quartz, so it’s in your best interest to make your application Quartz-savvy. Because HIView user interface objects were designed with Quartz in mind, you can easily use all its features.

Note that even though Quartz relies on a different coordinate system than QuickDraw, the system flips the context before presenting it to your HIView drawing handler, so you can continue to leverage your QuickDraw-compatible code. Also, because you receive the drawing context from a Carbon event, you do not have to worry about handling ports, creating contexts, and so on; you simply draw.

In addition, if your application used the Appearance Manager, you can now use the HITheme API which allows you to draw Aqua-compliant features using Quartz.

For more information about using Quartz, see _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.

Apple is committed to the HIViews, Carbon events, and nib files for Carbon implementations of the user interface. All new controls and other features will be based on HIView. If you want your application to take advantage of the latest features, you need to adopt the modern HIToolbox.

Because backwards compatibility has been a hallmark of Mac OS system software, you do not have to throw out all your older implementations to begin updating your user interface code.

- Nib files can coexist with resources in the same application. You can first adopt nibs for windows that require views or compositing, and address the rest as your schedule permits.
- An application can support both `WaitNextEvent` event dispatching and Carbon events. For example, you can convert to Carbon events first in windows that use HIView, and update the others as time permits. Another priority is to upgrade any user interface code that polls or otherwise makes poor use of CPU cycles.
- You can adopt compositing mode on a window-by-window basis.
- HIView supports both QuickDraw and Quartz, so you can migrate your drawing code incrementally as well.

[Next](Porting%20Steps.md)[Previous](Introduction%20to%20Upgrading%20to%20the%20Mac%20OS%20X%20HIToolbox.md)

