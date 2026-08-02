---
title: Carbon Porting Guide
apple_id: TP30000991
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-12-01'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/carbon_porting_guide/cpg_newtechstruct/cpg_newtech_struct.html
archived_at: '2026-07-15T05:24:54.095645Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon Porting Guide](Introduction%20to%20Carbon%20Porting%20Guide.md)


[Next](New%20Carbon%20Functions.md)[Previous](A%20Porting%20Example.md)

# New Carbon Technologies

This chapter describes several Mac OS technologies that are new with Carbon. While these technologies are not required in Carbon applications, adopting them can result in improved performance and user experience as well as reduced development cycles.

The Carbon Event Manager is an event handling API that replaces the Classic Mac OS Event Manager. It simplifies the event model and it is well-suited for the preemptive multitasking capabilities of Mac OS X. For example, when using Carbon events, an application that is performing periodic actions while idle (blinking the cursor, for example) does not have to endlessly cycle through a `WaitNextEvent` loop while doing so. The advantages of the Carbon Event Manager include the following:

- Handlers for common events (such as mouse events and keyboard events) are included. You don’t need to write your own event handlers unless you want to override default behaviors.
- The Carbon Event Manager can handle any number of event types (as opposed to the16 event types available in the Classic event record).
- The Carbon Event Manager handles notifications and defproc messaging in addition to the usual events.
- The streamlining of the event handling system results in a more responsive system and a better user experience.

When adapting an application to use Carbon events, you typically replace the `WaitNextEvent` loop and event processing functions with one of more simple event handling calls. Your application must register the types of events it wishes to be notified about, and then implement handlers to address the registered events.

The Carbon Event Manager is available for Carbon applications running on Mac OS 8.6 and later, so if you do not need compatibility back to Mac OS 8.1, we highly encourage you to adopt it. The Carbon event model is flexible enough to coexist with `WaitNextEvent`, so you can make the adoption as gradual as you like. While the `WaitNextEvent` event model still works on Mac OS X, your programs and the overall system will perform better if you use Carbon events.

For more information about the Carbon Event Manager, see the documentation available at

[http://developer.apple.com/documentation/carbon/Reference/Carbon_Event_Manager_Ref/index.html](https://developer.apple.com/documentation/carbon/Reference/Carbon_Event_Manager_Ref/index.html)

as well as [An Example: Adding Carbon Events to Sample](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojrfvbuqmrqguwueqkcijdegq2j).

Core Foundation is a new set of APIs that provides a simple interface for handling many common needs for applications. For example, CFPreference APIs provide a standard interface for creating and manipulating an application’s user preferences. As most Core Foundation functions are part of the Carbon API, they run on both Mac OS X and Mac OS 8 and 9. In addition, Core Foundation functions are compatible with the Foundation classes available in the Cocoa environment, which simplifies the sharing of data between Carbon and Cocoa applications.

In addition to Preferences Services, other Core Foundation services that you may find useful for your Carbon application include the following:

- Bundle Services, which provides the APIs used to access files and other resources stored in a bundle hierarchy. See [Consider Using Bundles](Preparing%20Your%20Code%20for%20Carbon.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojrfvbuqmrqgiwueqkcijdeqski) for more information about bundles.
- Plug-In Services, which provides a standard plug-in architecture for Mac OS X and Mac OS 8 and 9 applications. You can package plug-in binaries for multiple platforms together, and the Plug-In Services APIs can transparently load the proper one (assuming, of course, that they share the same interface).
- String Services, which provides a simple interface for storing, converting, and manipulating Unicode strings. If your application uses (or is planning to support) Unicode, you should consider adopting String Services.
- The XML Parser, which provides an interface for writing and reading XML documents.
- Property List Services, which provides an interface to organize data into property lists (“plists”). It also allows you to convert hierarchically structured combinations of basic data types in these lists to and from standard XML.

For more information about Core Foundation Services, see _Inside Mac OS X: System Overview_ and Core Foundation documentation at the Carbon documentation site:

[http://developer.apple.com/documentation/Carbon/index.html](https://developer.apple.com/documentation/Carbon/index.html)

DataBrowser is a new Control Manager control (defined in `ControlDefinitions.h`) that lets you display data in sortable, navigatable lists in a manner similar to the list view and column view settings of the Finder. If you need to organize data in manner that is easily accessible to the user, you should consider using the DataBrowser. Here are some advantages of the various views:

- The list view allows the user to sort by various column attributes related to the data you are displaying. For example, the Finder allows you to display files by type, size, or date modified, among other characteristics.
- The column view is useful for navigating large hierarchies or trees of data. For example both the Mac OS X Finder and the Navigation Services Save dialog box use DataBrowser to let the user quickly find a particular location in a volume’s file hierarchy.

For more information about DataBrowser, see the sample code included with the Carbon SDK.

The Multilingual Text Engine (MLTE) is the suggested replacement for TextEdit in Carbon applications. While you can still use TextEdit in Carbon, MLTE provides many additional features and simplifies the programming interface; you can accomplish more with fewer lines of code. Some of MLTE’s features include the following:

- Full Unicode support, including transparent access to Apple Type Services for Unicode Imaging (ATSUI) for rendering text, and the Text Encoding Converter (TEC) for converting between encodings.
- Full support for alternate input methods using the Text Services Manager (TSM).
- Support for greater than 32 KB of text.
- Built-in scroll bar handling.
- Full justification of text.
- Built-in support for basic user actions, such as highlighting selected text, dragging selected text, and moving the caret in response to arrow key presses.
- Multiple levels of undo.
- Built-in printing support.

MLTE is available in CarbonLib 1.2 and later. You can also use it in non-Carbon applications on Mac OS 8.6 and later.

For more information about MLTE, see the documentation available at

[http://developer.apple.com/documentation/Carbon/Reference/Multilingual_Text_Engine/index.html](https://developer.apple.com/documentation/Carbon/Reference/Multilingual_Text_Engine/index.html)

and the MLTE SDK at

[http://developer.apple.com/sdk/](https://developer.apple.com/sdk/)

The Carbon Event Manager is the most important of the optional technologies available with Carbon; if you plan to add only one new API to your application, it should be Carbon events. In addition to simplifying your event handling code, Carbon events will make your application a good processor-sharing citizen on Mac OS X, which will improve the performance of all running applications.

This section illustrates the adoption of the Carbon Event Manager by adding Carbon events to the Carbon version of the Sample application shown in [Listing 3-1](A%20Porting%20Example.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojrfvbuqmrqgqwueqshincucqkh) and [Listing 3-2](A%20Porting%20Example.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojrfvbuqmrqgqwueqshijbucqke).

[Determine the Appropriate CarbonLib Version](Preparing%20Your%20Code%20for%20Carbon.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojrfvbuqmrqgiwviucykjcummjrgu) indicates that the Carbon Event Manager is available only in CarbonLib 1.2 and later when Mac OS 8.6 or later is present. While this means that you cannot run on Mac OS 8.1, it also means that you are free to incorporate any newer APIs up to Mac OS 8.6 if that makes the work easier.

The basic model for Carbon events is that you register callback handlers for each event (or type of event) you wish to handle. You attach these handlers to specific objects, such as a window or a button. Different objects of the same type do not have to have the same handler. For example, two buttons can each have their own distinct handler. With this level of flexibility in handling events, it is important to determine the scope required for each event. For example, should an event affect a single window, all open windows, or the entire application? In most cases it is easier to think in terms of what object is affected rather than what event occurred.

After any initial setup, your application calls `RunApplicationEventLoop`, which essentially replaces the `WaitNextEvent` loop. From that point on, your application is notified only when an event you specified occurs.

The Carbon Event Manager provides default event handlers for many common types of events. For example, the standard handler for a window automatically handles dragging, activation, deactivation, window zooming and resizing. Of course, you will mostly likely still need to draw into or update the content region as a result of some actions, but much of the basic work is taken care of for you. A good rule of thumb is to install the standard handler first, see what actions it covers, and then write handlers for any additional actions you may want to take.

In the Carbon version of Sample, most of the event handling occurs in the functions `EventLoop` and `DoEvent`. Here is a breakdown of the events to address:

- Adjusting the cursor shape depending on the region it occupies: Previously the cursor was adjusted each time through the event loop. Because there is no equivalent event loop that we can access in Carbon events, an alternate triggering mechanism is required. One method would be to update the cursor whenever the mouse moves. Another would be to set up a timer to adjust the cursor at regular intervals.
- Menu selections: The Carbon Event Manager can associate special command events with menu items. Many common menu items have command events defined for them in `CarbonEvents.h`, and you can assign your own using the Window Manager function `SetMenuItemCommandID`. When a menu item is selected (either through menu selection or a keyboard equivalent), the Carbon Event Manager sends the appropriate command event to the handler. Some menu selections are related to the window only (such as setting the traffic light color), while others are related to the application (such as the About command). This division suggests a menu command handler at both the window level and the application level.

  Note that the standard application handler automatically handles basic menu tracking, highlighting, and so on. All you need to do is process the menu selection.
- Keyboard events: Because the only keyboard input Sample requires are keyboard equivalents for menu items, you can handle these the same as menu selections.
- Mouse clicks in the traffic light window: The light color toggles on each click in the content region of the window. This event is entirely window-related, which suggests a window-level handler.
- Window dragging, zooming, resizing, activation, and deactivation: The standard window event handler addresses these events, so all you need to do is update the content region if necessary.
- Update events: The Carbon Event Manager posts events indicating that you should change your window contents, so you should redraw the contents at that time.
- High level (Apple) events: The only case to worry about is the Quit Apple event, for which we have already installed a handler.
- Disk Events: This case deals with bad floppy disks, and Carbon does not support the `DIBadMount` function or the `diskEvt` event. This example ignores disk events.
- Application suspend and resume events: The standard application event handler covers the basic functionality required for suspend and resume events.

This information indicates that event handlers are needed at both the window-level and the application level.

Before adding your application-specific event handlers, you should install the standard handlers for window and application events.

One way to assign the standard window handler to the traffic light window is to call the function `InstallStandardWindowEventHandler` after creating the window in the `Initialize` function.

```
window = GetNewWindow(rWindow, NULL, (WindowPtr)-1);
InstallStandardEventHandler(GetWindowEventTarget(window)); /* installs the default */
                                                    /* handler for window events */
ShowWindow(window);
```

The `GetWindowEventTarget` function returns an event reference (type `EventTargetRef`) to associate with the desired object (in this case, a window). Similar functions exist to create event references for controls, menus, and other objects.

However, because the application must run in Mac OS 8.6 or later, you can call the Window Manager function `CreateNewWindow` instead, which lets you specify an attribute to use the standard window handler. Doing so also provides many of the standard window controls (resize button, and so on) for free.

```
Rect windowBounds;           /* use Rect for bounds in CreateNewWindow */
WindowAttributes windowAttr;  /* to hold window attribute flags in CreateNewWindow */
…
windowAttr = kWindowStandardDocumentAttributes| /* standard window */
                kWindowStandardHandlerAttribute| /* standard window event handler */
                kWindowInWindowMenuAttribute;

SetRect (&windowBounds, 40, 60, 280, 520); /* bounds for the new window */

CreateNewWindow(kDocumentWindowClass, windowAttr, &windowBounds, &window);
SetWindowTitleWithCFString(window, CFSTR("Traffic"));

ChangeWindowAttributes(window, NULL, /* remove close box and resize tab */
                         kWindowCloseBoxAttribute|kWindowResizableAttribute);
ShowWindow(window);
```

The `SetWindowTitleWithCFString` function is a Core Foundation String Services function.

To more closely approximate the original Sample, you can call the Window Manager function `ChangeWindowAttributes` to remove the close box and the resize tab.

The standard application event handler is installed automatically when you call `RunApplicationEventLoop`, so you do not need to explicitly install it.

After installing the standard handlers, you must register your event handlers with the system. The Carbon Event Manager defines events by the class of event (window, mouse, and so on) as well as the type (mouse moved, content region clicked, and so on). You must specify these when registering your handlers, as in this example:

```
EventTypeSpec   appEventList[] = {{kEventClassCommand, kEventCommandProcess},
                                { kEventClassMouse, kEventMouseMoved}};

EventTypeSpec   windEventList[] = {{kEventClassWindow, kEventWindowDrawContent },
                                 { kEventClassWindow, kEventWindowClickContentRgn },
                                 { kEventClassWindow, kEventWindowBoundsChanged},
                                 { kEventClassCommand, kEventCommandProcess}};

…

    /* Installing the application event handler */
    InstallApplicationEventHandler(NewEventHandlerUPP(MyAppEventHandler),
                                2, appEventList, 0, NULL);

    /* Installing the window event handler */
    InstallWindowEventHandler(window, NewEventHandlerUPP(MyWindowEventHandler),
                                4, windEventList, 0, NULL);
```

The type `EventTypeSpec` arrays hold the pairs of event classes and types which are then passed into the appropriate handler installation calls. The calls `InstallApplicationEventHandler` and `InstallWindowEventHandler` are macros derived from the more general Carbon Event Manager function `InstallEventHandler`. Remember to pass universal procedure pointers instead of normal pointers when specifying your callback handlers. `CarbonEvents.h` defines the format for your callback handlers.

If desired, you can register individual event handlers for each event. However, for this example it is convenient to group them by object.

The handlers in this example essentially take the place of the `DoEvent` function, which called other functions to process the events.

Listing 4-1 shows an application-level event handler for the Sample application.

__Listing 4-1__  Application-level event handler for Sample

```
static pascal OSStatus MyAppEventHandler (EventHandlerCallRef myHandlerChain,
                                            EventRef event, void* userData)
{
    UInt32          whatHappened;
    HICommand       commandStruct;
    Point           wheresMyMouse;
    RgnHandle       CursorRgn;
    short           itemHit;
    OSStatus        result = eventNotHandledErr; /* report failure by default */


    whatHappened = GetEventKind(event);

    switch (whatHappened)
        {
            case kEventCommandProcess:

                    GetEventParameter (event, kEventParamDirectObject,
                                        typeHICommand, NULL, sizeof(HICommand),
                                        NULL, &commandStruct);

                    switch (commandStruct.commandID)
                        {
                            case kCommandAbout:
                                itemHit = Alert (rAboutAlert, nil);
                                result = noErr;
                                break;
                            default:
                                break;
                        }
                    break;

            case kEventMouseMoved:

                    CursorRgn = NewRgn();
                    GetEventParameter (event, kEventParamMouseLocation, typeQDPoint,
                                         NULL, sizeof(Point), NULL, &wheresMyMouse);
                    AdjustCursor(wheresMyMouse, CursorRgn);
                    DisposeRgn(CursorRgn);
                    result = noErr;
                    break;

            default:
                    break;
        }
    return result;
}
```

The event handler takes three parameters:

- The `myHandlerChain` parameter is a reference to the handler calling chain; that is, the hierarchy of event handlers that could handle this event. You would pass this reference if you wanted to call `CallNextEventHandler`, for example, which you could use to add pre- or postprocessing to the actions of a standard handler.
- The `event` parameter contains specific information related to the event (much the way the fields of an event record hold event-specific information).
- The `userData` field holds any user data you specified when you registered your handler with the call to `InstallEventHandler` (none in this case).

When an event occurs, `MyAppEventHandler` gets passed the event along with any user data you may have requested (none in this case). It then calls the `GetEventKind` function to determine the type of event that occurred and then handles the event appropriately.

The`kEventCommandProcess` function indicates a menu-related command occurred. By calling the `GetEventParameter` function, the handler determines which item was selected. At the application level only one command is possible: the About selection. Note `kCommandAbout` is not defined in `CarbonEvents.h` so, you need to define it yourself. You can do so and then call the Menu Manager function `SetMenuItemCommandID` in the `Initialize` function to register it with the system.

```
const MenuCommand kCommandAbout = FOUR_CHAR_CODE ('abou');

void Initialize()
{
    …
    SetMenuItemCommandID (GetMenuRef(mApple), iAbout, kCommandAbout);
    …
}
```

Note that instead of calling `SetMenuItemCommandID` to assign the command ID, you could choose the define it in an `'xmnu'` resource.

You don’t need to handle the Quit event because the standard application event handler calls the default Quit Apple event handler when this occurs. If you need to take additional actions before quitting, you can install your own Quit Apple event handler. If you are not using `RunApplicationEventLoop`, (and therefore not using the standard application handler), you can process the Quit event here. Typically you call the function `QuitApplicationEventLoop` to break out of the Carbon event loop.

If you are running your application on Mac OS 8 and 9, you need to register the Quit command ID (defined as `kHICommandQuit` in `CarbonEvents.h`) using the `SetMenuItemCommandID` function, much as you had to for the About item. If you don’t, the Carbon Event Manager will not properly process the event when the Quit item is selected. A convenient time to do this is when you use Gestalt to determine whether to place a Quit item in the File menu.

```
    err = Gestalt(gestaltMenuMgrAttr, &result);
    if (!err && (result & gestaltMenuMgrAquaLayoutMask)) {
            menu = GetMenuHandle (mFile);
            DeleteMenuItem(menu, iQuit);
            DeleteMenuItem(menu, iQuit-1); /*•• the element above the Quit item */
                                         /*•• is a separator */
        }
        else
        {   /* Assign a command ID to the Quit Item so that the Carbon Event Manager */
            /* can recognize it. */
            SetMenuItemCommandID(GetMenuRef(mFile), iQuit, kHICommandQuit);
        }
```

The other application-level event you need to handle is the mouse-moved event, which determines whether or not to adjust the cursor shape. The handler for Sample calls `GetEventParameter` to obtain the mouse position (the types of parameters you can obtain depends on the event that occurred) and then calls `AdjustCursor`.

Alternatively, you can adjust the cursor periodically by using a Carbon event timer. Doing so merely involves creating the function to call and then registering it by calling `InstallEventLoopTimer`. However, this method is similar to polling for an event, which is more processor-intensive, and therefore not suggested for Mac OS X.

Listing 4-2 shows a window event handler for Sample.

__Listing 4-2__  Window event handler for Sample

```
static pascal OSStatus MyWindowEventHandler(EventHandlerCallRef myHandler,
                                            EventRef event, void* userData)
{
    WindowRef           window;
    Rect                bounds;
    UInt32              whatHappened;
    HICommand           commandStruct;
    MenuRef             theMenuRef;
    UInt16              theMenuItem;
    OSStatus            result = eventNotHandledErr; /* report failure by default */

    GetEventParameter(event, kEventParamDirectObject, typeWindowRef, NULL,
                         sizeof(window), NULL, &window);

    whatHappened = GetEventKind(event);

    switch (whatHappened)
        {
            case kEventWindowDrawContent:

                    DoUpdate(window);
                    result = noErr;
                    break;

            case kEventWindowBoundsChanged:

                    InvalWindowRect(window, GetWindowPortBounds(window, &bounds));
                    DoUpdate(window);
                    result = noErr;
                    break;

            case kEventWindowClickContentRgn:

                    DoContentClick(window);
                    DoUpdate(window);
                    AdjustMenus();
                    result = noErr;
                    break;

            case kEventCommandProcess:

                    GetEventParameter (event, kEventParamDirectObject,
                                        typeHICommand, NULL, sizeof(HICommand),
                                        NULL, &commandStruct);

                    theMenuRef = commandStruct.menu.menuRef;
                    if (theMenuRef == GetMenuHandle(mLight))
                        {
                            /* Because the event didn't occur *in* the window, the */
                            /* window reference isn't valid until we set it here */
                            window = FrontWindow();

                            theMenuItem = commandStruct.menu.menuItemIndex;
                            switch ( theMenuItem )
                                {
                                    case iStop:
                                        SetLight(window, true);
                                        break;
                                    case iGo:
                                        SetLight(window, false);
                                        break;
                                }
                            DoUpdate(window);
                            AdjustMenus();
                            result = noErr;
                        }
                    break;

            default:
                    /* If nobody handled the event, it gets propagated to the */
                    /* application-level handler. */
                    break;

        }

    return result;
}
```

As with the application-level handler, the window event handler first calls `GetEventKind` to determine the type of event and then processes them appropriately:

- `kEventWindowDrawContent` indicates that the window contents must be redrawn. This event is similar to an update event in the Classic event model. However, if you have the standard window handler installed, the Carbon Event Manager automatically calls `BeginUpdate` and `EndUpdate` for this event; all you need to do is draw in the window. To avoid nesting update calls, you should remove the duplicate `BeginUpdate` and `EndUpdate` calls in the `DoUpdate` function.
- `kEventWindowBoundsChanged` indicates that the window size has changed (by clicking the zoom button). The handler calls `DoUpdate` to redraw the content region to reflect the new size.
- `kEventWindowClickContentRgn` indicates that the user has clicked in the Traffic window. To toggle the light setting, the handler calls `DoContentClick` as before, but because Sample no longer receives update events, the handler also calls `DoUpdate` to draw the new setting. Similarly, because Sample cannot update the Traffic menu settings by calling `AdjustMenus` from the `WaitNextEvent` loop, the handler calls it here.
- `kEventCommandProcess` indicates that a menu-related command occurred. Because this is the window handler, the handler processes only cases related to the Traffic window (that is, the Red Light/Green Light items in the Traffic menu). Other commands will end up being handled by the application-level handler. To change the traffic light setting, the handler first isolates the menu item selected from the event parameter and then redraws the light (using the same calls as in the `kEventWindowClickContentRgn` case).

  If desired, instead of obtaining the menu item from the `commandStruct` structure, you can define and register constants for these items as you did for the About menu item.

After adapting Sample to use Carbon events, you no longer need the following functions:

- `EventLoop`: Replaced by the call to `RunApplicationEventLoop`.
- `DoEvent`: Replaced by the application and window event handlers.
- `MyGetGlobalMouse`: The application event handler now retrieves the mouse location from the event structure.
- `DoMenuCommand`: The handling of these events is split between the application and window event handlers.

[Next](New%20Carbon%20Functions.md)[Previous](A%20Porting%20Example.md)

