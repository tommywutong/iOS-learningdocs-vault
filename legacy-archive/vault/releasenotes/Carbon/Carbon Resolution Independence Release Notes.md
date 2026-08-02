---
title: Carbon Resolution Independence Release Notes
apple_id: TP40001375
resource_type: Release Note
platform: macOS
topic: null
technology: null
published: '2005-04-29'
source_url: https://developer.apple.com/library/archive/releasenotes/Carbon/RN-CarbonResolutionIndependence/index.html
archived_at: '2026-07-18T02:50:21.849173Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Carbon Resolution Independence Notes for Mac OS X v10.4

> [!IMPORTANT]
> 

#### Contents:

- [Overview](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzvfvcg63tujruw422fnrsw2zlooreuixzr)
- [Magnified Mode and the Virtual Coordinate Space](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzvfvcg63tujruw422fnrsw2zlooreuixzs)
- [Converting between the Virtual Coordinate Space and screen pixels](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzvfvcg63tujruw422fnrsw2zlooreuixzt)
- [Resolution Independence-savvy Windows and the four resolution modes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzvfvcg63tujruw422fnrsw2zlooreuixzu)
- [Framework Scaled mode:](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzvfvcg63tujruw422fnrsw2zlooreuixzv)
- [Application Scaled mode:](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzvfvcg63tujruw422fnrsw2zlooreuixzw)
- [Magnified mode:](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzvfvcg63tujruw422fnrsw2zlooreuixzx)
- [Unscaled mode:](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzvfvcg63tujruw422fnrsw2zlooreuixzy)
- [More Coordinate Conversion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzvfvcg63tujruw422fnrsw2zlooreuixzz)
- [Special Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzvfvcg63tujruw422fnrsw2zlooreuixzrga)

### Overview

An overview of resolution independence concepts can be found in the general resolution independence documentation. Please read the general documentation first. This document explains only the Carbon-specific concepts, issues, and details.

### Magnified Mode and the Virtual Coordinate Space

Not all applications will rev to support resolution independence in the short term, but we still want to offer a reasonable experience in unmodified applications when the user has chosen a non-1.0 scale factor. To this end, HIToolbox automatically "magnifies" windows that are not resolution independence savvy. (Magnification is achieved by setting up a transformation on the Window Server window object that backs a Carbon WindowRef.)

Whenever HIToolbox magnifies a window, we must make sure that event coordinates, window bounding rectangles, and all other constructs related to the window are also similarly "magnified". This magnification is achieved by translating actual screen pixel units into a virtual coordinate space where every virtual coordinate may represent more than one screen pixel. At the API level, the window must appear to the application to be 200 virtual units tall even if the onscreen representation is (for example) 267 screen pixels tall. Likewise, all events that destined for the window must have coordinates that match the virtual coordinate space. In fact, almost every Carbon API that speaks in terms of global coordinates must match the virtual coordinate space.

The virtual coordinate space is referred to using the kHICoordSpace72DPIGlobal with the HIPoint/Rect/SizeConvert APIs. More details on these APIs can be found below.

(We are often asked about adding a per-process flag that marks an application as resolution independence savvy in order to avoid these virtual <-> pixel coordinate conversions. Unfortunately, though an application developer can reliably make his own code savvy, any given plugin or system service (print dialogs, open/save, font panel, etc.) that the application uses may not be savvy and could break if its unmodified coordinate expectations are not met. Therefore, we cannot allow a developer to mark its app as resolution independence savvy. However, we can allow developers to mark individual windows as savvy as explained later.)

Points, rectangles, and regions that are passed to/from the following APIs and contained within the following structures will be in and must be interpreted within the virtual coordinate space:

- GDevice
- GlobalToLocal
- LocalToGlobal
- QDGlobalToLocalPoint/Rect/Region
- QDLocalToGlobalPoint/Rect/Region
- EventRecord
- FindWindow
- DragWindow
- GrowWindow
- ResizeWindow
- MoveWindow
- SizeWindow
- Get/SetWindowBounds
- Get/SetWindowResizeLimits
- TrackMouseLocation[WithOptions]
- GetMouse
- WaitMouseMoved
- TrackDrag
- Get/SetDragItemBounds
- Get/SetDragMouse
- GetDragOrigin
- SetDragImage[WithCGImage]
- MenuEvent
- MenuSelect
- PopUpMenuSelect
- GetMBarHeight

That list is not necessarily intended to be exhaustive. More APIs and structures may be added to that list by the time resolution independence becomes a user feature. In addition, every Carbon Event point, rectangle, size, region or shape parameter that represents "global" coordinates (but not parameters that represent "window" coordinates) will be in and must also be interpreted in the virtual coordinate space.

Caveat: Some of the above APIs are essentially a method on a WindowRef object. When an application marks a particular WindowRef as resolution independence savvy (see below), some of the APIs may be able to speak in screen pixel coordinates when used with that window. That's how many of them behave currently, but I we won't know whether that is desirable until we get feedback from developers.

Note: Should we decide that Magnified Mode is undesirable or if the user turns off Magnified Mode (assuming we offer such a mechanism), unmodified applications will simply display tiny windows. In this situation, none of the API/structure modifications would be necessary.

### Converting between the Virtual Coordinate Space and screen pixels

In order to properly position windows on even pixel boundaries or to otherwise fine-tune their interfaces, some applications may need to convert between the virtual coordinate space being used by a window and the screen pixel space. The following APIs can do the transformation:

```

  HICoordinateSpace inDestinationSpace, void* inDestinationObject);
```

More details, including full header documentation can be found in <HIToolbox/HIGeometry.h>

### Resolution Independence-savvy Windows and the four resolution modes

Carbon applications that wish to be resolution independence-savvy can do so by putting their windows into one of two different savvy resolution modes: Framework Scaled mode or Application Scaled mode. When there is a non-1.0 scale factor, a window that isn't in one of these two savvy modes is said to be in Magnified mode. When there is a 1.0 scale factor, all windows are in the Unscaled mode. (In this situation, there is a 1:1 correspondence between all applicable coordinate systems, so windows can behave the same way they always had before resolution independence.)

You can query a window's resolution mode via the following API:

```
typedef UInt32 HIWindowScaleMode;
enum {
  kHIWindowScaleModeUnscaled    = 0,
  kHIWindowScaleModeMagnified   = 1,
  kHIWindowScaleModeFrameworkScaled = 2,
  kHIWindowScaleModeApplicationScaled = 3
};

extern OSStatus
HIWindowGetScaleMode( HIWindowRef inWindow, HIWindowScaleMode* outMode, float* outScaleFactor);
```

Before I go into detail about how the modes differ, I need to explain the concept of a window's coordinate space. Every window has a coordinate system that is used to define size & positions of the views within it. Point, rectangle, and other event parameters that are documented to be in "window coordinates" match this coordinate space. At a 1.0 scale factor, a window's coordinate space translates directly into the screen pixel space. At other scale factors, and depending on the window's resolution mode, a window's coordinate space may differ from the screen pixel space as described in each of the resolution modes.

### Framework Scaled mode:

Framework Scaled mode allows the developer to use the same window coordinate space regardless of the global scale factor. For example, a push button will always be 20 window coordinate units tall in this mode regardless of the scale factor. This is extraordinarily useful for developers that want to load and maintain their window as a single .nib that works at all scale factors.

The term "Framework Scaled" is used because the system-supplied frameworks (mainly HIView subsystem of the HIToolbox.framework) automatically transforms the CGContextRef used to draw views such that it matches the scale factor. A Framework Scaled window's backing store matches the resolution (units per inch) of the screen. Together, these two things result in very crisp drawing.

Resolution Details:

- backing store resolution = screen pixel resolution
- window coordinate space resolution = virtual coordinate space resolution

Some applications may want to adjust the positions and/or sizes of individual views such that they fall on (and draw on) even pixel boundaries, but that isn't necessary; the HIView subsystem can correctly handle views that don't fall on even pixel boundaries.

Framework Scaled mode is only available to windows that use compositing mode (by specifying the kWindowCompositingAttribute attribute at window creation time). You cannot draw with Quickdraw in an Framework Scaled window; Quickdraw requires the window's coordinate space resolution to match the screen pixel resolution.

You can request an Framework Scaled mode window by specifying the kWindowFrameworkScaledAttribute attribute at window creation time. If the scale factor is something other than 1.0, the resulting window's resolution mode will be set to kHIWindowScaleModeFrameworkScaled. (If the scale factor is 1.0, the window's resolution mode will be kHIWindowScaleModeUnscaled.)

### Application Scaled mode:

Application Scaled mode allows developers to continue to use Quickdraw to draw their window's contents, yet still be resolution independence savvy. However, there is a cost associated with that flexibility: An Application Scaled window's coordinate space is always at the same resolution as the screen pixels. This means that (for example) at a 1.0 scale factor a push button needs to be 20 window coordinate units tall, whereas at a 1.33 scale factor a push button needs to be 26 window coordinate units tall. It is the developer's responsibility to size and position their views/controls appropriately based on the scale factor. HIToolbox automatically sizes and positions the views that it is responsible for, such as the window title bar and associated buttons, the toolbar and toolbar items, the grow box, and any subviews of standard system views (such as the scroll bars in a data browser) that are in the window's content area. (Note: Much of this work has not been completed for the WWDC seed. Many system-supplied views do not size and position its subviews properly yet.)

In order to use a single .nib to represent a window regardless of the scale factor, the developer will need to load the window and then 1) resize the window to match the scale factor, and 2) iterate over the views within the window and resize & reposition them to match the new window's size as well as the scale factor.

Drawing is as crisp in Application Scaled mode as it is in Framework Scaled mode, since the window's backing store resolution matches the screen pixel resolution.

Resolution Details:

- backing store resolution = screen pixel resolution
- window coordinate space resolution = screen pixel resolution

You create a Application Scaled mode window by specifying the kWindowApplicationScaledAttribute attribute at window creation time. If the scale factor is something other than 1.0, the resulting window's resolution mode will be kHIWindowScaleModeApplicationScaled. (If the scale factor is 1.0, the window's resolution mode will be kHIWindowScaleModeUnscaled.)

### Magnified mode:

The details of magnified mode windows were covered earlier.

Resolution Details:

- backing store resolution = virtual coordinate space resolution
- window coordinate space resolution = virtual coordinate space resolution

You don't have to do anything special to create a magnified mode window. If the scale factor is something other than 1.0 and if the user has chosen to magnify un-savvy application windows, any window created without one of the resolution independence savvy attributes will be in the kHIWindowScaleModeMagnified resolution mode.

### Unscaled mode:

Unscaled mode is what developers are already used to at 72 dpi.

Resolution Details:

- backing store resolution = virtual coordinate space resolution = screen pixel resolution
- window coordinate space resolution = virtual coordinate space resolution = screen pixel resolution

You don't have to do anything special to create a unscaled mode window. A window be in the kHIWindowScaleModeUnscaled resolution mode whenever it doesn't have one of the other three modes.

### More Coordinate Conversion

Since individual windows in a given application may have different resolution modes, and since the application and/or the views within the window may need to translate between two windows' coordinate spaces or between a window's coordinate space and either the virtual coordinate space or the screen pixel coordinate space, the toolbox must offer a few more coordinate translation APIs possibilities. The following is the full set of HICoordinateSpace constants that can be used with the previously mentioned conversion APIs:

```
typedef UInt32 HICoordinateSpace;
enum {
  kHICoordSpace72DPIGlobal      = 1,
  kHICoordSpaceScreenPixel      = 2,
  kHICoordSpaceWindow           = 3,
  kHICoordSpaceView             = 4
};
```

See <HIToolbox/HIGeometry.h> for documentation on how to use the window and view coordinate spaces.

All of the conversion APIs take point, size, and rect structures that use floating point coordinates, which allows developers to make intelligent decisions about how to deal with sub-unit rounding appropriately. However, there are some basic rules that define when to outset a coordinate to integral units versus when to inset:

- When the coordinate's purpose is for communication of some kind of maximal area, such as a view's structure shape (which defines the maximal area into which it might draw), you need to outset.
- When the coordinate's purpose is for a minimal area, such as a view's opaque shape (which defines the minimal area of fully opaque view drawing), you need to inset.

The CGRectInset and CGRectIntegral APIs can help you with inset and outset operations.

Another important issue to consider is that HIShapeRefs can only contain integer coordinates. It is legal to create an HIShapeRef from a rectangle that contains non-integral coordinates, but the resulting HIShapeRef will be outset to the nearest integer coordinate. To avoid any unwanted surprises, we recommend that you outset/inset (as appropriate) your rectangle to the nearest integer coordinates before creating an HIShapeRef based on it.

### Special Issues

### Custom MDEFs

When the scale factor is not equal to 1.0, the Menu Manager automatically creates windows for menus that use a custom MDEF using the Magnified mode. Therefore, an MDEF should not need to change at all to work in resolution independence mode.

### Custom menu item drawing

Event handlers for the kEventMenuDrawItem and kEventMenuDrawItemContent events may require modifications to work properly in resolution independence mode. When the scale factor is not equal to 1.0, the Menu Manager automatically creates windows for menus that use an HIView to draw (including all standard menus) using the KitScaled mode. Since Quickdraw-based drawing is not compatible with KitScaled mode, event handlers for the DrawItem or DrawItemContent handlers that used Quickdraw to draw would not draw properly into the menu view.

To avoid this problem, the standard menu view creates a temporary GWorld and makes it the current port before sending the DrawItem event. After the DrawItem event has been handled, the Menu Manager copies the contents of the GWorld into the view. This allows Quickdraw-based custom menu item drawing to work properly in standard menu views.

Even with this compatibility workaround, however, Apple cannot ensure that all Quickdraw-based custom menu item drawing will always work in resolution independence mode. Therefore, our recommendation is that any Quickdraw-based drawing should be converted to use CoreGraphics instead. The CGContextRef passed to the DrawItem and DrawItemContent events will allow drawing directly into the menu window, with no temporary offscreen buffer. CoreGraphics drawing will give the fastest results with no pixel magnification.

The compatibility workaround using a temporary offscreen buffer is not guaranteed to be present in the final version of Mac OS X Tiger. We will be evaluating its effectiveness during the beta testing period and may remove this workaround before Tiger ships. This workaround may also be removed in a future versons of Mac OS X.

### TBD

For the final Tiger release, we play to expand the HITheme drawing APIs to support resolution independence mode drawing.

HIToolbox may need to offer HIShapeRef conversion APIs, too. The conversion set cannot be as rich as those for points, sizes, and rects, since shapes can only represent integer coordinates.
