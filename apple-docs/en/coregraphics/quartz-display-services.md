---
title: Quartz Display Services
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/quartz-display-services
source_url: 'https://developer.apple.com/documentation/coregraphics/quartz-display-services'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/quartz-display-services.json'
content_hash: 'sha256:ec52302b6e87b7f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# Quartz Display Services

<sub>API Collection</sub>

Provides direct access to features in the macOS window server for configuring and controlling display hardware.

## Overview

You can use Quartz Display Services to:

- Examine and change display mode properties such as width, height, and pixel depth
- Configure a set of displays in a single operation
- Capture one or more displays for exclusive use
- Stream the contents of a display
- Perform fade effects
- Activate display mirroring
- Configure gamma color correction tables
- Receive notification of screen update operations

## Topics

### Finding Displays

- [CGMainDisplayID](<cgmaindisplayid().md>) — Returns the display ID of the main display.
- [CGGetOnlineDisplayList](<cggetonlinedisplaylist(______).md>) — Provides a list of displays that are online (active, mirrored, or sleeping).
- [CGGetActiveDisplayList](<cggetactivedisplaylist(______).md>) — Provides a list of displays that are active for drawing.
- [CGGetDisplaysWithOpenGLDisplayMask](<cggetdisplayswithopengldisplaymask(________).md>) — Provides a list of displays that corresponds to the bits set in an OpenGL display mask.
- [CGGetDisplaysWithPoint](<cggetdisplayswithpoint(________).md>) — Provides a list of online displays with bounds that include the specified point.
- [CGGetDisplaysWithRect](<cggetdisplayswithrect(________).md>) — Gets a list of online displays with bounds that intersect the specified rectangle.
- [CGOpenGLDisplayMaskToDisplayID](<cgopengldisplaymasktodisplayid(__).md>) — Maps an OpenGL display mask to a display ID.
- [CGDisplayIDToOpenGLDisplayMask](<cgdisplayidtoopengldisplaymask(__).md>) — Maps a display ID to an OpenGL display mask.

### Capturing and Releasing Displays

- [CGDisplayCapture](<cgdisplaycapture(__).md>) — Obtains exclusive use of a display, preventing other applications and system services from using the display or changing its configuration.
- [CGDisplayCaptureWithOptions](<cgdisplaycapturewithoptions(____).md>) — Obtains exclusive use of a display for an application using the options you specify.
- [CGDisplayRelease](<cgdisplayrelease(__).md>) — Releases a captured display.
- [CGDisplayIsCaptured](<cgdisplayiscaptured(__).md>) — Returns a Boolean value indicating whether a display is captured. _(deprecated)_
- [CGCaptureAllDisplays](<cgcapturealldisplays().md>) — Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [CGCaptureAllDisplaysWithOptions](<cgcapturealldisplayswithoptions(__).md>) — Captures all attached displays, using the specified options.
- [CGReleaseAllDisplays](<cgreleasealldisplays().md>) — Releases all captured displays.
- [CGShieldingWindowID](<cgshieldingwindowid(__).md>) — Returns the window ID of the shield window for a captured display.
- [CGShieldingWindowLevel](<cgshieldingwindowlevel().md>) — Returns the window level of the shield window for a captured display.
- [CGDisplayGetDrawingContext](<cgdisplaygetdrawingcontext(__).md>) — Returns a graphics context suitable for drawing to a captured display.

### Configuring Displays

- [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>) — Begins a new set of display configuration changes.
- [CGCancelDisplayConfiguration](<cgcanceldisplayconfiguration(__).md>) — Cancels a set of display configuration changes.
- [CGCompleteDisplayConfiguration](<cgcompletedisplayconfiguration(____).md>) — Completes a set of display configuration changes.
- [CGConfigureDisplayMirrorOfDisplay](<cgconfiguredisplaymirrorofdisplay(______).md>) — Changes the configuration of a mirroring set.
- [CGConfigureDisplayMode](<cgconfiguredisplaymode(______).md>) — Configures the display mode of a display. _(deprecated)_
- [CGConfigureDisplayOrigin](<cgconfiguredisplayorigin(________).md>) — Configures the origin of a display relative to the global display coordinate space.
- [CGRestorePermanentDisplayConfiguration](<cgrestorepermanentdisplayconfiguration().md>) — Restores the permanent display configuration settings for the current user.
- [CGConfigureDisplayStereoOperation](<cgconfiguredisplaystereooperation(________).md>) — Enables or disables stereo operation for a display, as part of a display configuration.
- [CGDisplaySetStereoOperation](<cgdisplaysetstereooperation(________).md>) — Immediately enables or disables stereo operation for a display.
- [CGConfigureDisplayWithDisplayMode](<cgconfiguredisplaywithdisplaymode(________).md>) — Configures the display mode of a display.

### Getting the Display Configuration

- [CGDisplayCopyColorSpace](<cgdisplaycopycolorspace(__).md>) — Returns the color space for a display.
- [CGDisplayIOServicePort](<cgdisplayioserviceport(__).md>) — Returns the I/O Kit service port of the specified display. _(deprecated)_
- [CGDisplayIsActive](<cgdisplayisactive(__).md>) — Returns a Boolean value indicating whether a display is active.
- [CGDisplayIsAlwaysInMirrorSet](<cgdisplayisalwaysinmirrorset(__).md>) — Returns a Boolean value indicating whether a display is always in a mirroring set.
- [CGDisplayIsAsleep](<cgdisplayisasleep(__).md>) — Returns a Boolean value indicating whether a display is sleeping (and is therefore not drawable).
- [CGDisplayIsBuiltin](<cgdisplayisbuiltin(__).md>) — Returns a Boolean value indicating whether a display is built-in, such as the internal display in portable systems.
- [CGDisplayIsInHWMirrorSet](<cgdisplayisinhwmirrorset(__).md>) — Returns a Boolean value indicating whether a display is in a hardware mirroring set.
- [CGDisplayIsInMirrorSet](<cgdisplayisinmirrorset(__).md>) — Returns a Boolean value indicating whether a display is in a mirroring set.
- [CGDisplayIsMain](<cgdisplayismain(__).md>) — Returns a Boolean value indicating whether a display is the main display.
- [CGDisplayIsOnline](<cgdisplayisonline(__).md>) — Returns a Boolean value indicating whether a display is connected or online.
- [CGDisplayIsStereo](<cgdisplayisstereo(__).md>) — Returns a Boolean value indicating whether a display is running in a stereo graphics mode.
- [CGDisplayMirrorsDisplay](<cgdisplaymirrorsdisplay(__).md>) — For a secondary display in a mirroring set, returns the primary display.
- [CGDisplayModelNumber](<cgdisplaymodelnumber(__).md>) — Returns the model number of a display monitor.
- [CGDisplayPrimaryDisplay](<cgdisplayprimarydisplay(__).md>) — Returns the primary display in a hardware mirroring set.
- [CGDisplayRotation](<cgdisplayrotation(__).md>) — Returns the rotation angle of a display in degrees.
- [CGDisplayScreenSize](<cgdisplayscreensize(__).md>) — Returns the width and height of a display in millimeters.
- [CGDisplaySerialNumber](<cgdisplayserialnumber(__).md>) — Returns the serial number of a display monitor.
- [CGDisplayUnitNumber](<cgdisplayunitnumber(__).md>) — Returns the logical unit number of a display.
- [CGDisplayUsesOpenGLAcceleration](<cgdisplayusesopenglacceleration(__).md>) — Returns a Boolean value indicating whether Quartz is using OpenGL-based window acceleration (Quartz Extreme) to render in a display.
- [CGDisplayVendorNumber](<cgdisplayvendornumber(__).md>) — Returns the vendor number of the specified display’s monitor.

### Registering for Notification of Display Configuration Changes

- [CGDisplayRegisterReconfigurationCallback](<cgdisplayregisterreconfigurationcallback(____).md>) — Registers a callback function to be invoked whenever a local display is reconfigured.
- [CGDisplayRemoveReconfigurationCallback](<cgdisplayremovereconfigurationcallback(____).md>) — Removes the registration of a callback function that’s invoked whenever a local display is reconfigured.

### Retrieving Display Parameters

- [CGDisplayBounds](<cgdisplaybounds(__).md>) — Returns the bounds of a display in the global display coordinate space.
- [CGDisplayPixelsHigh](<cgdisplaypixelshigh(__).md>) — Returns the display height in pixel units.
- [CGDisplayPixelsWide](<cgdisplaypixelswide(__).md>) — Returns the display width in pixel units.

### Creating and Managing Display Modes

- [CGDisplayAvailableModes](<cgdisplayavailablemodes(__).md>) — Returns information about the currently available display modes. _(deprecated)_
- [CGDisplayBestModeForParameters](<cgdisplaybestmodeforparameters(__________).md>) — Returns information about the display mode closest to a specified depth and screen size. _(deprecated)_
- [CGDisplayBestModeForParametersAndRefreshRate](<cgdisplaybestmodeforparametersandrefreshrate(____________).md>) — Returns information about the display mode closest to a specified depth, screen size, and refresh rate. _(deprecated)_
- [CGDisplayCurrentMode](<cgdisplaycurrentmode(__).md>) — Returns information about the current display mode. _(deprecated)_
- [CGDisplaySwitchToMode](<cgdisplayswitchtomode(____).md>) — Switches a display to a different mode. _(deprecated)_
- [CGDisplayCopyDisplayMode](<cgdisplaycopydisplaymode(__).md>) — Returns information about a display’s current configuration.
- [CGDisplayCopyAllDisplayModes](<cgdisplaycopyalldisplaymodes(____).md>) — Returns information about the currently available display modes.
- [CGDisplaySetDisplayMode](<cgdisplaysetdisplaymode(______).md>) — Switches a display to a different mode.

### Getting Information About a Display Mode

- [CGDisplayModeGetWidth](cgdisplaymode/width.md) — Returns the width of the specified display mode.
- [CGDisplayModeGetHeight](cgdisplaymode/height.md) — Returns the height of the specified display mode.
- [CGDisplayModeCopyPixelEncoding](cgdisplaymode/pixelencoding.md) — Returns the pixel encoding of the specified display mode. _(deprecated)_
- [CGDisplayModeGetRefreshRate](cgdisplaymode/refreshrate.md) — Returns the refresh rate of the specified display mode.
- [CGDisplayModeGetIOFlags](cgdisplaymode/ioflags.md) — Returns the I/O Kit flags of the specified display mode.
- [CGDisplayModeGetIODisplayModeID](cgdisplaymode/iodisplaymodeid.md) — Returns the I/O Kit display mode ID of the specified display mode.
- [CGDisplayModeIsUsableForDesktopGUI](<cgdisplaymode/isusablefordesktopgui().md>) — Returns a Boolean value indicating whether the specified display mode is usable for a desktop graphical user interface.
- [CGDisplayModeGetTypeID](cgdisplaymode/typeid.md) — Returns the type identifier of Quartz display modes.

### Adjusting the Display Gamma

- [CGSetDisplayTransferByFormula](<cgsetdisplaytransferbyformula(____________________).md>) — Sets the gamma function for a display by specifying the coefficients of the gamma transfer formula.
- [CGGetDisplayTransferByFormula](<cggetdisplaytransferbyformula(____________________).md>) — Gets the coefficients of the gamma transfer formula for a display.
- [CGSetDisplayTransferByTable](<cgsetdisplaytransferbytable(__________).md>) — Sets the color gamma function for a display by specifying the values in the RGB gamma tables.
- [CGGetDisplayTransferByTable](<cggetdisplaytransferbytable(____________).md>) — Gets the values in the RGB gamma tables for a display.
- [CGSetDisplayTransferByByteTable](<cgsetdisplaytransferbybytetable(__________).md>) — Sets the byte values in the 8-bit RGB gamma tables for a display.
- [CGDisplayRestoreColorSyncSettings](<cgdisplayrestorecolorsyncsettings().md>) — Restores the gamma tables to the values in the user’s ColorSync display profile.
- [CGDisplayGammaTableCapacity](<cgdisplaygammatablecapacity(__).md>) — Returns the capacity, or number of entries, in the gamma table for a display.

### Display Fade Effects

- [CGConfigureDisplayFadeEffect](<cgconfiguredisplayfadeeffect(____________).md>) — Modifies the settings of the built-in fade effect that occurs during a display configuration.
- [CGAcquireDisplayFadeReservation](<cgacquiredisplayfadereservation(____).md>) — Reserves the fade hardware for a specified time interval.
- [CGDisplayFade](<cgdisplayfade(________________).md>) — Performs a single fade operation.
- [CGDisplayFadeOperationInProgress](<cgdisplayfadeoperationinprogress().md>) — Returns a Boolean value indicating whether a fade operation is currently in progress. _(deprecated)_
- [CGReleaseDisplayFadeReservation](<cgreleasedisplayfadereservation(__).md>) — Releases a display fade reservation, and unfades the display if needed.

### Controlling the Mouse Cursor

- [CGDisplayHideCursor](<cgdisplayhidecursor(__).md>) — Hides the mouse cursor, and increments the hide cursor count.
- [CGDisplayShowCursor](<cgdisplayshowcursor(__).md>) — Decrements the hide cursor count, and shows the mouse cursor if the count is `0`.
- [CGDisplayMoveCursorToPoint](<cgdisplaymovecursortopoint(____).md>) — Moves the mouse cursor to a specified point relative to the upper-left corner of the display.
- [CGCursorIsVisible](<cgcursorisvisible().md>) — Returns a Boolean value indicating whether the mouse cursor is visible. _(deprecated)_
- [CGCursorIsDrawnInFramebuffer](<cgcursorisdrawninframebuffer().md>) — Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory. _(deprecated)_
- [CGAssociateMouseAndMouseCursorPosition](<cgassociatemouseandmousecursorposition(__).md>) — Connects or disconnects the mouse and cursor while an application is in the foreground.
- [CGWarpMouseCursorPosition](<cgwarpmousecursorposition(__).md>) — Moves the mouse cursor without generating events.
- [CGGetLastMouseDelta()](<cggetlastmousedelta().md>) — Reports the change in mouse position since the last mouse movement event received by the application.

### Getting Window Server Information

- [CGSessionCopyCurrentDictionary](<cgsessioncopycurrentdictionary().md>) — Returns information about the caller’s window server session.
- [CGWindowServerCFMachPort](<cgwindowservercfmachport().md>) — Returns a Core Foundation Mach port (CFMachPort) that corresponds to the macOS window server. _(deprecated)_
- [CGWindowLevelForKey](<cgwindowlevelforkey(__).md>) — Returns the window level that corresponds to one of the standard window types.

### Getting Information About Refresh and Move Operations

- [CGRegisterScreenRefreshCallback](<cgregisterscreenrefreshcallback(____).md>) — Registers a callback function to be invoked when local displays are refreshed or modified. _(deprecated)_
- [CGUnregisterScreenRefreshCallback](<cgunregisterscreenrefreshcallback(____).md>) — Removes a previously registered callback function invoked when local displays are refreshed or modified. _(deprecated)_
- [CGWaitForScreenRefreshRects](<cgwaitforscreenrefreshrects(____).md>) — Waits for screen refresh operations. _(deprecated)_
- [CGScreenRegisterMoveCallback](<cgscreenregistermovecallback(____).md>) — Registers a callback function to be invoked when an area of the display is moved. _(deprecated)_
- [CGScreenUnregisterMoveCallback](<cgscreenunregistermovecallback(____).md>) — Removes a previously registered callback function invoked when an area of the display is moved. _(deprecated)_
- [CGWaitForScreenUpdateRects](<cgwaitforscreenupdaterects(__________).md>) — Waits for screen update operations. _(deprecated)_
- [CGReleaseScreenRefreshRects](<cgreleasescreenrefreshrects(__).md>) — Deallocates a list of rectangles that represent changed areas on local displays. _(deprecated)_

### Callbacks

- [CGDisplayReconfigurationCallBack](cgdisplayreconfigurationcallback.md) — A client-supplied callback function that’s invoked whenever the configuration of a local display is changed.
- [CGScreenRefreshCallback](cgscreenrefreshcallback.md) — A client-supplied callback function that’s invoked when an area of the display is modified or refreshed.
- [CGScreenUpdateMoveCallback](cgscreenupdatemovecallback.md) — A client-supplied callback function invoked when an area of the display is moved.

### Data Types

- [CGDirectDisplayID](cgdirectdisplayid.md) — A unique identifier for an attached display.
- [CGDisplayBlendFraction](cgdisplayblendfraction.md) — The percentage of blend color used in a fade operation.
- [CGDisplayConfigRef](cgdisplayconfigref.md) — A reference to a display configuration transaction.
- [CGDisplayCount](cgdisplaycount.md) — The number of displays in various lists. _(deprecated)_
- [CGDisplayErr](cgdisplayerr.md) — A uniform type for result codes returned by functions in Quartz Display Services. _(deprecated)_
- [CGDisplayFadeInterval](cgdisplayfadeinterval.md) — The duration in seconds of a fade operation or a fade hardware reservation.
- [CGDisplayFadeReservationToken](cgdisplayfadereservationtoken.md) — A token issued by Quartz when reserving one or more displays for a fade operation during a specified interval.
- [CGDisplayMode](cgdisplaymode.md) — A reference to a display mode object.
- [CGDisplayReservationInterval](cgdisplayreservationinterval.md) — The time interval for a fade reservation.
- [CGGammaValue](cggammavalue.md) — A value used to map a color generated in software to a color supported by the display hardware.
- [CGOpenGLDisplayMask](cgopengldisplaymask.md) — A bitmask used in OpenGL to specify a set of attached displays.
- [CGRectCount](cgrectcount.md) — The size of an array of Quartz rectangles.
- [CGRefreshRate](cgrefreshrate.md) — A display’s refresh rate in frames per second.
- [CGScreenUpdateMoveDelta](cgscreenupdatemovedelta.md) — The distance, in pixel units, that an onscreen region moves.
- [CGWindowLevel](cgwindowlevel.md) — A level assigned to a window by an application framework.
- [CGDisplayStream](cgdisplaystream.md) — A reference to a display stream object.
- [CGDisplayStreamUpdate](cgdisplaystreamupdate.md) — A reference to frame update’s metadata.
- [CGDisplayStreamFrameAvailableHandler](cgdisplaystreamframeavailablehandler.md) — A block called when a data stream has a new frame event to process.

### Constants

- [CGCaptureOptions](cgcaptureoptions.md) — Configuration parameters that are used when capturing displays.
- [CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags.md) — The configuration parameters that are passed to a display reconfiguration callback function.
- [CGConfigureOption](cgconfigureoption.md) — The scope of the changes in a display configuration transaction.
- [Display Fade Blend Fractions](display-fade-blend-fractions.md) — The lower and upper bounds for blend color fractions during a display fade operation.
- [Display Fade Constants](display-fade-constants.md) — Values relating to fade operations.
- [Display ID Defaults](display-id-defaults.md) — Default values for a display ID.
- [Display Mode Standard Properties](display-mode-standard-properties.md) — Keys for the standard properties in a display mode dictionary.
- [Display Mode Optional Properties](display-mode-optional-properties.md) — Keys for optional properties in a display mode dictionary.
- [Reserved Window Levels](reserved-window-levels.md) — Window level constants.
- [CGScreenUpdateOperation](cgscreenupdateoperation.md) — Types of screen-update operations.
- [CGWindowLevelKey](cgwindowlevelkey.md) — Keys that represent the standard window levels in macOS. Quartz includes these keys to support application frameworks like Cocoa. Applications do not need to use them directly.
- [Window Server Session Properties](window-server-session-properties.md) — The keys for the standard properties in a window server session dictionary.
- [CGDisplayStreamUpdateRectType](cgdisplaystreamupdaterecttype.md) — Use these constants to determine which rectangles your app is interested in.
- [CGDisplayStreamFrameStatus](cgdisplaystreamframestatus.md) — Describes a frame update event.
- [Display Stream Optional Property Keys](display-stream-optional-property-keys.md) — These keys are used to populate the `properties` dictionary used when creating a new display stream.
- [Display Stream YCbCr to RGB conversion Matrix Options](display-stream-ycbcr-to-rgb-conversion-matrix-options.md) — These strings are used to specify a matrix for the `CGDisplayStream/yCbCrMatrix` option.

## See Also

### Related Documentation

- [Quartz Display Services Programming Topics](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzDisplayServicesConceptual/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004316)

### Services

- [Quartz Event Services](quartz-event-services.md) — Provides features for managing _event taps_—filters for observing and altering the stream of low-level user input events in macOS.
- [Quartz Window Services](quartz-window-services.md) — Provides information about the windows managed by the macOS window server.
