---
title: Quartz Display Services Programming Topics
apple_id: TP40004316
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzDisplayServicesConceptual/Articles/DisplayInfo.html
archived_at: '2026-07-15T07:38:03.566550Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Display Services Programming Topics](Introduction%20to%20Quartz%20Display%20Services%20Programming%20Topics.md)


[Next](Capturing%20Displays.md)[Previous](Overview%20of%20Quartz%20Display%20Services.md)

# Getting Information About Displays

Quartz Display Services provides a number of functions to retrieve information about display state and display modes. This article briefly covers a few of these functions. For a complete list, see _[Quartz Display Services Reference](https://developer.apple.com/documentation/coregraphics/quartz_display_services)_.

Quartz Display Services includes accessor functions that report current properties of the display hardware, properties that are also found in the current display mode. Because these functions do not rely on information from the current display mode, they provide the most accurate information available about the display (display mode properties are subject to change by the device driver). These functions, listed next, are straightforward to use:

| Function | Description |
| --- | --- |
| `CGDisplayPixelsWide` | Returns the drawable width of a display in pixel units. |
| `CGDisplayPixelsHigh` | Returns the drawable height of a display in pixel units. |

The API includes other accessor functions that report additional information about the current configuration and state of the display. The following table lists a representative sample of these functions:

| Function | Description |
| --- | --- |
| `CGDisplayIsActive` | Returns a Boolean value indicating whether a display is active or drawable). |
| `CGDisplayIsBuiltin` | Returns a Boolean value indicating whether a display is built-in, such as the internal display in portable systems. |
| `CGDisplayIsMain` | Returns a Boolean value indicating whether a display is the main display. |
| `CGDisplayScreenSize` | Returns the width and height of a display in millimeters. |
| `CGDisplayUsesOpenGLAcceleration` | Returns a Boolean value indicating whether Quartz is using OpenGL-based window acceleration (Quartz Extreme) to render in a display. |

Quartz Display Services includes several accessor functions that report current properties of the display hardware, properties that are also found in the current display mode dictionary. Because these functions do not rely on information from the current display mode, they provide the most accurate information available about the display (display mode properties are subject to change by the device driver). These functions, listed next, are straightforward to use:

| Function | Description |
| --- | --- |
| `CGDisplayPixelsWide` | Returns the drawable width of a display in pixel units. |
| `CGDisplayPixelsHigh` | Returns the drawable height of a display in pixel units. |
| `CGDisplayBitsPerPixel` | Returns the number of bits used to represent a pixel in the frame buffer. |
| `CGDisplayBitsPerSample` | Returns the number of bits used to represent a pixel component in the frame buffer. |
| `CGDisplaySamplesPerPixel` | Returns the number of components used to represent a pixel in the frame buffer. |
| `CGDisplayBytesPerRow` | Returns the number of bytes per row in the frame buffer. |

The API includes other accessor functions that report additional information about the current configuration and state of the display. The following table lists a representative sample of these functions:

| Function | Description |
| --- | --- |
| `CGDisplayIsActive` | Returns a Boolean value indicating whether a display is active or drawable). |
| `CGDisplayIsBuiltin` | Returns a Boolean value indicating whether a display is built-in, such as the internal display in portable systems. |
| `CGDisplayIsMain` | Returns a Boolean value indicating whether a display is the main display. |
| `CGDisplayScreenSize` | Returns the width and height of a display in millimeters. |
| `CGDisplayUsesOpenGLAcceleration` | Returns a Boolean value indicating whether Quartz is using OpenGL-based window acceleration (Quartz Extreme) to render in a display. |

Each online display has a current display mode and a set of available display modes. The device driver uses information in the current display mode to configure the display.

You can retrieve the values of the properties in a display mode with the appropriate `CGDisplayMode` function. Listing 1 shows how to retrieve several mode properties.

__Listing 1__  Getting display mode properties on OS X v10.6 or later

```
bool gui;
double refresh;
uint32_t ioflags;

CGDisplayModeRef currentMode = CGDisplayCopyDisplayMode(kCGDirectMainDisplay);

refresh = CGDisplayModeGetRefreshRate(currentMode);
gui = CGDisplayModeIsUsableForDesktopGUI(currentMode);
ioflags = CGDisplayModeGetIOFlags(currentMode);

CGDisplayModeRelease(currentMode);
```


Each online display has a current display mode and a set of available display modes. The device driver uses information in the current display mode to configure the display.

You can retrieve the values of the properties in a display mode dictionary with the [CFDictionaryGetValue](https://developer.apple.com/documentation/corefoundation/1516757-cfdictionarygetvalue) function. Then, you may need to cast the returned value to the appropriate data type. Listing 1 shows how to retrieve several mode properties and cast them to a base data type.

__Listing 2__  Getting display mode properties on OS X v10.5

```
CFNumberRef number;
CFBoolean booleanValue;
Boolean gui;
long mode, refresh, ioflags;

CFDictionaryRef currentMode = CGDisplayCurrentMode (kCGDirectMainDisplay);

number = CFDictionaryGetValue (currentMode, kCGDisplayMode);
CFNumberGetValue (number, kCFNumberLongType, &mode);

number = CFDictionaryGetValue (currentMode, kCGDisplayRefreshRate);
CFNumberGetValue (number, kCFNumberLongType, &refresh);

booleanValue = CFDictionaryGetValue (currentMode, kCGDisplayModeUsableForDesktopGUI);
gui = CFBooleanGetValue (booleanValue);

number = CFDictionaryGetValue (currentMode, kCGDisplayIOFlags);
CFNumberGetValue (number, kCFNumberLongType, &ioflags);
```

[Next](Capturing%20Displays.md)[Previous](Overview%20of%20Quartz%20Display%20Services.md)

