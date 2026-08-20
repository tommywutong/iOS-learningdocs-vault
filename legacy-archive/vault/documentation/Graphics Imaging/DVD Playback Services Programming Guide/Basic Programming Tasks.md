---
title: DVD Playback Services Programming Guide
apple_id: TP40002163
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: DVDPlayback
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/DVDPlaybackGuide/dvdguide_tasks_1/dvdguide_tasks_1.html
archived_at: '2026-07-15T07:35:41.781250Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [DVD Playback Services Programming Guide](Introduction%20to%20DVD%20Playback%20Services%20Programming%20Guide.md)


[Next](Additional%20Programming%20Tasks.md)[Previous](Programming%20Concepts.md)

# Basic Programming Tasks

In this chapter, you'll learn about the basic operations you must implement in order to play DVD-Video media. To play DVD-Video media using DVD Playback Services, you'll need to perform this sequence of operations:

1. Begin a new DVD playback session.
2. Set the window to be used for video playback.
3. Set the video display device for the window.
4. Set the bounds of the video area inside the window.
5. Open a DVD-Video media folder.
6. Play the media and respond to user actions.
7. Close the media folder.
8. End the DVD playback session.

When your application is ready to begin a DVD playback session, the first step is to call the `DVDInitialize` function. The result code indicates whether the API is available for use. If the result code is `noErr`, you're ready to proceed to the next step.

In this example, the application quits if DVD Playback Services cannot be initialized:

```
OSStatus err = DVDInitialize();
if (err != noErr) {
    NSLog(@"DVDInitialize returned %d", err);
    [NSApp terminate:self];
}
```


DVD Playback Services uses a callback mechanism to notify your application if an I/O error makes it impossible to play the media. Typically this error occurs when the optical disc is dirty or damaged. If you don't register a callback function to receive this error, your application may crash unexpectedly. Your error callback should do two things: (1) notify the user that a fatal error has occured, and (2) end the playback session (see [Ending a Playback Session](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnjqfvjvomq)).

This line of code shows how to register a callback function to handle a fatal error:

```
OSStatus err = DVDSetFatalErrorCallBack (MyDVDErrorHandler, (UInt32) self);
```

In this example, the callback passes the error code to a method that handles the error:

```objc
void MyDVDErrorHandler (DVDErrorCode inErrorCode, UInt32 inRefCon) {
    Controller *controller = (Controller *)inRefCon;
    [controller handleDVDError:inErrorCode];
}

- (void) handleDVDError:(DVDErrorCode)error {
    NSLog(@"fatal error %d", error);
    [NSApp terminate:self];
}
```


Once the session is active, your application needs to create a window for video playback. Typically the characteristics of your video window are specified in an Interface Builder nib file, and the window is instantiated at runtime when your application loads the nib.

The recommended window type is a document window with zoom, minimize, and resize controls. The recommended initial view size is 640 x 480, which corresponds to the standard DVD aspect ratio of 4:3.

If the video window is a Cocoa window, you set the video playback window with the `DVDSetVideoWindowID` function. In CocoaDVDPlayer, the video window is a subclass of NSWindow, which has a method to get the window number. Here's the line of code that sets the window:

```
OSStatus err = DVDSetVideoWindowID ([self windowNumber]);
```

Here's the line of code that sets the video window in a Carbon application. The window is a variable of type `WindowRef`):

```
OSStatus err = DVDSetVideoPort (GetWindowPort (myWindow));
```


After the video window is created, your application needs to tell DVD Playback Services which graphics display to use for DVD playback.

Cocoa applications should set the playback display with `DVDSwitchToDisplay`, a convenience function that also validates the display to make sure it's supported for playback. Be sure the check the boolean value that's passed back to verify that the display is supported. If it's not supported, your application should notify the user and terminate the playback session.

A Cocoa window can find its display ID and set the display as follows:

```
CGDirectDisplayID display = (CGDirectDisplayID)
    [[[[self screen] deviceDescription] valueForKey:@"NSScreenNumber"] intValue];
Boolean isSupported;
OSStatus err = DVDSwitchToDisplay (display, &isSupported);
```

Carbon applications can find the graphics device for their video window using the Window Manager function `GetWindowGreatestAreaDevice`, and can set the playback display using the convenience function `DVDSwitchToDevice`. As with `DVDSwitchToDisplay`, be sure to check the boolean value that's passed back.

```
GDHandle device;
OSStatus err = GetWindowGreatestAreaDevice (myWindow, kWindowContentRgn, &device, NULL);
Boolean isSupported;
err = DVDSwitchToDevice (device, &isSupported);
```

If the video window is moved to a different display during playback, you should use the same procedure to set the new display.

The next step is to use the `DVDSetVideoBounds` function to tell DVD Playback Services where to display the video content. This function takes a QuickDraw rectangle (`Rect`) that represents the bounds of the video area inside your window. The rectangle is expressed in window local coordinates. DVD Playback Services automatically scales the video content to fit inside this video area. Typically the dimensions of the video area are the same as the content area of the window, but this isn't a requirement.

For the video content to look right, the video area should always have one of two aspect ratios: standard (4:3) or wide (16:9). The initial aspect ratio of the video area is typically 4:3, the aspect ratio of the first title or menu on most DVDs.

Applications that use a Cocoa rectangle ([NSRect](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSRect)) or a Quartz rectangle ([CGRect](https://developer.apple.com/documentation/coregraphics/cgrect) to represent the bounds of the video area must convert it to a QuickDraw rectangle before calling `DVDSetVideoBounds`. Listing 2-1 shows how this is done for a Cocoa window in which the video area and the content view have the same bounds.

__Listing 2-1__  Setting the video bounds

```objc
- (void) setVideoBounds
{
    NSRect content = [[self contentView] bounds]; // 1
    NSRect frame = [self frame]; // 2

    Rect qdRect; // 3
    qdRect.left = 0;
    qdRect.right = content.size.width;
    qdRect.bottom = frame.size.height;
    qdRect.top = frame.size.height - content.size.height; // 4

    OSStatus err = DVDSetVideoBounds (&qdRect);
}
```

Here's what this code does:

1. Gets the height and width of the content view.
2. Gets the height of the window, including the title bar.
3. Creates a QuickDraw rectangle to represent the video bounds.
4. Computes the position of the top edge in window local coordinates.

Whenever the user resizes the window or displays a new title with a different the aspect ratio, your application needs to call `DVDSetVideoBounds` again to notify DVD Playback Services that the video area has changed.

Now you're ready to open DVD-Video media for playback. Standard-definition media is stored inside a media folder named VIDEO_TS. A standard-definition DVD-Video disc has a VIDEO_TS folder in its root directory, for example. DVD Playback Services allows only one media folder to be open at a time; before you attempt to open a media folder, you should use the `DVDHasMedia` function to check to see if media is already open.

DVD Playback Services provides two functions to open media:

- To open DVD-Video media on a disc volume, you should call the `DVDOpenMediaVolume` function and pass a file object that specifies the media folder at the root level of the volume—for example, `/Volumes/CITIZEN_KANE/VIDEO_TS`.
- To open DVD-Video media on a hard drive, you should call the `DVDOpenMediaFile` function and pass a file object that specifies the full path to the media folder—for example, `/Users/Orson/Movies/CITIZEN_KANE/VIDEO_TS`.

Both functions take as input a file object of type [FSRef](https://developer.apple.com/documentation/coreservices/fsref) that specifies the path to the media folder. Before calling one of these functions, you should validate the file object using the `DVDIsValidMediaRef` function.

Listing 2-2 shows how to use these functions:

__Listing 2-2__  Opening media

```objc
- (BOOL) openMedia:(FSRef *)media isVolume:(BOOL)isVolume
{
    Boolean isValid;
    OSStatus err = DVDIsValidMediaRef (media, &isValid);
    if (isValid)
    {
        if ([self hasMedia] == YES) {
            [self closeMedia];
        }

        if (isVolume) {
            err = DVDOpenMediaVolume (media);
        }
        else {
            err = DVDOpenMediaFile (media);
        }
    }
    return isValid;
}
```


DVD authoring applications such as iDVD and DVD Studio Pro can be used to create VIDEO_TS media folders on the users' hard drive. Your application may be called upon to open such a folder and play its contents. Listing 2-3 shows how a Cocoa application could display an Open dialog that allows the user to navigate to and open a media folder.

__Listing 2-3__  Opening a media folder

```objc
- (IBAction) onOpenMediaFolder:(id)sender
{
    NSOpenPanel *panel = [NSOpenPanel openPanel]; // 1
    [panel setCanChooseFiles:NO];
    [panel setCanChooseDirectories:YES];
    [panel setAllowsMultipleSelection:NO];

    if ([panel runModalForTypes:nil] == NSOKButton) // 2
    {
        NSString *folderPath = [[panel filenames] objectAtIndex:0]; // 3
        const char *cPath = [folderPath cStringUsingEncoding:NSASCIIStringEncoding]; // 4
        FSRef fileRef;
        OSStatus err = FSPathMakeRef ((UInt8*)cPath, &fileRef, NULL); // 5
        [self openMedia:&fileRef isVolume:NO]; // 6
    }
}
```

Here's what this code does:

1. Creates an Open panel and configures it to open a single folder.
2. Displays the panel and checks for the OK button.
3. Retrieves a POSIX path to the selected folder.
4. Gets a C string representation of the path.
5. Converts the path string into a file object.
6. Passes the path to the `openMedia` method (see [Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnjqfvjvomjt).

If media is open and playback is stopped or paused, you can begin playing media by calling the `DVDPlay` function. This function does not take any arguments to control the position at which playback begins. Instead, DVD Playback Services maintains a position marker called the _last play bookmark_. This bookmark specifies the last known playback position. In a new playback session, the last play bookmark is cleared to indicate that playback should start at the beginning of the media. Your application can update or reset this bookmark using the functions `DVDSetLastPlayBookmark` and `DVDClearLastPlayBookmark`.

The initial media playback stream usually takes the viewer to an on-screen menu. To play a feature title or branch to a different menu, the user operates the mouse or keyboard to select and press a menu button. In response, DVD Playback Services uses instructions embedded in the media itself to update the last play bookmark and begin playing the specified choice. In this situation, your application does not need to use `DVDPlay`.

While media is playing, you can pause or stop playback at the current frame. If you call the `DVDStop` function twice in succession, the last play bookmark is cleared.

When a title is playing and the user decides to display a menu, you should respond by calling the `DVDGoToMenu` function. Conversely, you should call the `DVDReturnToTitle` function when a menu is on the screen and the user decides to return to the current title.

If the user clicks the Menu button in CocoaDVDPlayer, for example, this action method switches between a title and its root menu:

```objc
- (IBAction) onToggleMenu:(id)sender
{
    if ((mDVDState == kDVDStatePlaying) ||
        (mDVDState == kDVDStatePlayingStill) ||
        (mDVDState == kDVDStatePaused))
    {
        Boolean onMenu = false;
        DVDMenu whichMenu;
        OSStatus err = DVDIsOnMenu (&onMenu, &whichMenu);
        if (onMenu) {
            err = DVDReturnToTitle();
        } else {
            err = DVDGoToMenu (kDVDMenuRoot);
        }
    }
}
```

When a DVD menu is first displayed, generally the first (topmost) button is selected, as shown in [Figure 1-2](Programming%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnbzfvjvomy). As the user operates the mouse or keyboard to select and press the desired button, your application responds by notifying DVD Playback Services. DVD Playback Services responds by selecting or activating the correct button on screen.

To implement this behavior, your application needs to perform the following actions:

- If the user presses an arrow key or chooses a navigation command such as Up or Down from an application menu, call the `DVDDoUserNavigation` function, passing a constant such as `kDVDUserNavigationMoveDown` to select the next button.
- If the user presses the Enter or Return key, call the `DVDDoUserNavigation` function to activate the selected button, passing the constant `kDVDUserNavigationEnter` to activate the selected button.
- If the user moves the mouse somewhere inside the video area, call the `DVDDoMenuMouseOver` function and pass in the location of the mouse.
- If the user clicks the mouse inside the video area, call the `DVDDoMenuClick` function and pass in the location of the mouse.

Listing 2-4 shows how to handle mouse events in the video window. In a Cocoa application, to receive mouse-moved events you'll also need to send the [setAcceptsMouseMovedEvents:](https://developer.apple.com/documentation/appkit/nswindow/1419340-acceptsmousemovedevents) message to the window.

__Listing 2-4__  Handling mouse events in the video window

```objc
- (void) sendEvent:(NSEvent *)theEvent
{
    SInt32 index = kDVDButtonIndexNone; // 1

    NSPoint location = [theEvent locationInWindow]; // 2
    Point portPt;
    portPt.h = location.x;
    portPt.v = [self frame].size.height - location.y;

    switch ([theEvent type])
    {
        OSStatus err;
        case NSMouseMoved:
            err = DVDDoMenuMouseOver (portPt, &index); // 3
            break;
        case NSLeftMouseDown:
            err = DVDDoMenuClick (portPt, &index); // 4
            break;
        default:
            break;
    }

    /* sync the cursor */
    NSCursor *cursor;
    if (index != kDVDButtonIndexNone) { // 5
        cursor = [NSCursor pointingHandCursor];
    } else {
            cursor = [NSCursor arrowCursor];
    }
    [cursor set];

    [super sendEvent:theEvent];
}
```

Here's what the code does:

1. Declares a variable to receive the button index if the mouse is over a button.
2. Gets the mouse location in Quartz coordinates (origin in lower left corner of window).
3. Displays visual feedback in the video window when the mouse cursor is inside a DVD button.
4. Activates a DVD button if the mouse cursor is inside the button when the mouse is clicked.
5. Sets the cursor to a pointing hand when the mouse is over a button.

Listing 2-5 shows how to handle keyboard events when a menu is displayed.

__Listing 2-5__  Handling keyboard events

```objc
- (BOOL) onKeyDown: (NSEvent *)theEvent
{
    NSString *keyString = [theEvent characters]; // 1
    unichar key = [keyString characterAtIndex:0]; // 2
    BOOL keyIsHandled = YES;

    switch (key) { // 3
        case NSUpArrowFunctionKey:
            DVDDoUserNavigation(kDVDUserNavigationMoveUp);
            break;
        case NSDownArrowFunctionKey:
            DVDDoUserNavigation(kDVDUserNavigationMoveDown);
            break;
        case NSLeftArrowFunctionKey:
            DVDDoUserNavigation(kDVDUserNavigationMoveLeft);
            break;
        case NSRightArrowFunctionKey:
            DVDDoUserNavigation(kDVDUserNavigationMoveRight);
            break;
        case NSCarriageReturnCharacter:
        case NSEnterCharacter:
            DVDDoUserNavigation(kDVDUserNavigationEnter);
            break;
        case ' ':
            if (mDVDState == kDVDStatePlaying)
                [self onPause:self];
            else if (mDVDState == kDVDStatePaused)
                [self onPlay:self];
            break;
        default:
            keyIsHandled = NO;
            break;
    }

    return keyIsHandled; // 4
}
```

Here's what this code does:

1. Gets a string that contains a Unicode representation of one or more keys pressed by the user.
2. Gets the first Unicode character in the string.
3. Handles the key. The arrow keys are used to navigate between buttons; the enter and return keys are used to press a button; the spacebar toggles between play and pause.
4. Returns a status flag (indicating whether the event was handled) to the window that received the event.

When the user is finished playing a media volume or folder, you should close the media. Before attempting to close the media, you should call the `DVDHasMedia` function to make sure the media is currently open. Depending on how the media was previously opened, you need to call one of two functions to close it:

- If you opened the media with the `DVDOpenMediaFile` function, you should close it by calling the `DVDCloseMediaFile` function.
- If you opened the media with the `DVDOpenMediaVolume` function, you should close it by calling the `DVDCloseMediaVolume` function.

When the user is finished using DVD Playback Services, or when a fatal error occurs, you should end the playback session. There are two basic tasks: (1) unregister all DVD event callbacks, and (2) call the function `DVDDispose`, which allows another process to use DVD Playback Services.

In this example, the event callback registration number is used as a flag to make sure a playback session is active. You'll learn how this registration number is obtained in [Registering for DVD Events](Additional%20Programming%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrtfvkfanbqgaydgmrsgawvgvzrge).

```objc
- (void) endSession
{
    if (mEventCallBackID) {
        OSStatus err = DVDUnregisterEventCallBack (mEventCallBackID);
        err = DVDDispose();
        mEventCallBackID = 0;
    }
}
```

[Next](Additional%20Programming%20Tasks.md)[Previous](Programming%20Concepts.md)

