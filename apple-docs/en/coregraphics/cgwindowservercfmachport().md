---
title: CGWindowServerCFMachPort()
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgwindowservercfmachport()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowservercfmachport()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowservercfmachport%28%29.json'
content_hash: 'sha256:f9c3c6427a05c146'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGWindowServerCFMachPort()

<sub>Function</sub>

Returns a Core Foundation Mach port (CFMachPort) that corresponds to the macOS window server.

> [!warning] Deprecated
> There is no replacement.

<sub>Mac Catalyst</sub>

```swift
func CGWindowServerCFMachPort() -> CFMachPort?
```

## Return Value

A Core Foundation Mach port, or `NULL` if the window server is not running. When you no longer need the port, you should release it using the function `CFRelease`.

## Discussion

You can use this function to detect whether the window server process exits or is not running. If this function returns `NULL`, the window server is not running. This code example shows how to register a callback function to detect when the window server exits:

```objc
static void handleWindowServerDeath( CFMachPortRef port, void *info  )
{
    printf( "Window Server port death detected!\n" );
    CFRelease(port);
    exit(1);
}
 
static void watchForWindowServerDeath()
{
    CFMachPortRef port = CGWindowServerCFMachPort();
    CFMachPortSetInvalidationCallBack(port, handleWindowServerDeath);
}
```

Note that this callback only works if your program has an active run loop.

## See Also

### Functions

- [CGAcquireDisplayFadeReservation](<cgacquiredisplayfadereservation(____).md>) — Reserves the fade hardware for a specified time interval.
- [CGAssociateMouseAndMouseCursorPosition](<cgassociatemouseandmousecursorposition(__).md>) — Connects or disconnects the mouse and cursor while an application is in the foreground.
- [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>) — Begins a new set of display configuration changes.
- [CGCancelDisplayConfiguration](<cgcanceldisplayconfiguration(__).md>) — Cancels a set of display configuration changes.
- [CGCaptureAllDisplays](<cgcapturealldisplays().md>) — Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [CGCaptureAllDisplaysWithOptions](<cgcapturealldisplayswithoptions(__).md>) — Captures all attached displays, using the specified options.
- [CGCompleteDisplayConfiguration](<cgcompletedisplayconfiguration(____).md>) — Completes a set of display configuration changes.
- [CGConfigureDisplayFadeEffect](<cgconfiguredisplayfadeeffect(____________).md>) — Modifies the settings of the built-in fade effect that occurs during a display configuration.
- [CGConfigureDisplayMirrorOfDisplay](<cgconfiguredisplaymirrorofdisplay(______).md>) — Changes the configuration of a mirroring set.
- [CGConfigureDisplayMode](<cgconfiguredisplaymode(______).md>) — Configures the display mode of a display. _(deprecated)_
- [CGConfigureDisplayOrigin](<cgconfiguredisplayorigin(________).md>) — Configures the origin of a display relative to the global display coordinate space.
- [CGConfigureDisplayStereoOperation](<cgconfiguredisplaystereooperation(________).md>) — Enables or disables stereo operation for a display, as part of a display configuration.
- [CGConfigureDisplayWithDisplayMode](<cgconfiguredisplaywithdisplaymode(________).md>) — Configures the display mode of a display.
- [CGCursorIsDrawnInFramebuffer](<cgcursorisdrawninframebuffer().md>) — Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory. _(deprecated)_
- [CGCursorIsVisible](<cgcursorisvisible().md>) — Returns a Boolean value indicating whether the mouse cursor is visible. _(deprecated)_
