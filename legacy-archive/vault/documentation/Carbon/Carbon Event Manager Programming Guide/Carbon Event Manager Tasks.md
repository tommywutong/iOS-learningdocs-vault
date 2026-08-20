---
title: Carbon Event Manager Programming Guide
apple_id: TP30000989
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Carbon_Event_Manager/Tasks/CarbonEventsTasks.html
archived_at: '2026-07-15T05:22:33.393286Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon Event Manager Programming Guide](Introduction%20to%20Carbon%20Event%20Manager%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Carbon%20Event%20Manager%20Concepts.md)

# Carbon Event Manager Tasks

This chapter expands on the basic concepts introduced in [Carbon Event Manager Concepts](Carbon%20Event%20Manager%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgiwueqkcireuoskg) and shows you how to create and install event handlers using the Carbon Event Manager interface.

As introduced in [Event Types](Carbon%20Event%20Manager%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgiwueqkcirdeqqki), each Carbon event is defined by an event class (for example, mouse or window events) as well as an event kind (for example, a mouse-down event).

All of the available event classes and kinds are designated by constants defined in the Universal Interfaces header file `CarbonEvents.h`. Nominally, these values are 32-bit integers; but in practice, the constants denoting event classes are specified as four-character tags—for instance,

```
kEventClassMouse = FOUR_CHAR_CODE('mous');
```

—while those representing event kinds are defined as simple integers:

```
kEventMouseDown = 1;
```

The event class and kind form a unique signature called an _event type_, which is specified in the Carbon Event Manager by the `EventTypeSpec` structure. When you register an event handler, you need to pass one or more `EventTypeSpec` structures to specify which events you want to handle.

The inclusion of standard handlers for many common events means that you can intercept actions only at the level you require. Some examples:

- If the user clicks the zoom box in a window, your handler can intercept the overall action at any of the following levels:

  - When the mouse is pressed (`kEventMouseDown`).
  - When the mouse is determined to be in the zoom region (`kEventWindowClickZoomRgn`).
  - When the mouse is released in the zoom region and the zoom is to take place (`kEventWindowZoom`).
  - When the zoom is completed (`kEventWindowZoomed`).
- When a window needs to be updated (redrawn), you can begin to take action at either of the following times:

  - Immediately (`kEventWindowUpdate`). You must handle all the usual update actions (calling `SetPort`, `BeginUpdate`/`EndUpdate`, drawing) yourself.
  - Only when it is time to draw (`kEventWindowDrawContent`). The standard handler for `kEventWindowUpdate` calls `SetPort` and `BeginUpdate`/`EndUpdate` for you. (It also sends the `kEventWindowDrawContent` event.)

The Carbon Event Manager provides several ways to execute event loops. The most common method is to simply call the function `RunApplicationEventLoop`, which does the following:

- Installs the standard application event handler
- Puts the application in a suspended state, waiting for events
- Places events into the application event queue as they occur
- Dispatches the events to your handlers or to standard event handlers

Using `RunApplicationEventLoop`, the basic structure of a Carbon application is as shown in Listing 2-1.

__Listing 2-1__  Structure of a typical Carbon application

```
void main (void)

   // Main function

   {
      Initialize (); // Do one-time-only initialization

         RunApplicationEventLoop (); // Process events until time to quit

      Finalize (); // Do one-time-only finalization

   }  /* end main */
```

You would register your event handlers in the `Initialize` function. Once in the loop, the only actions the application can take are in response to events.

To break out of the event loop, you must call the `QuitApplicationEventLoop` function from whichever event handler handles the quit event.

The `RunApplicationEventLoop` function works only on the main event loop; if your application creates preemptive threads, each of them will have its own event loop and queue, and you must retrieve and dispatch these events manually. For more information, see [Processing events manually](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiijcukskh).

Each event loop is represented by an event loop reference, an opaque data object of type `EventLoopRef`. A thread can obtain a reference to its own event loop or to the program’s main event loop by calling the functions `GetCurrentEventLoop` or `GetMainEventLoop`, respectively.

The function `RunCurrentEventLoop` runs the event loop belonging to the currently executing thread for a specified time (which can be infinite). This function can be useful if you want your thread to block for a specified time. During execution, it will place events into the queue and fire timers, but will take no other actions (for example, it won’t dispatch events to handlers). The function `QuitEventLoop` terminates a designated event loop.

The function for installing an event handler is called `InstallEventHandler`:

```
OSStatus InstallEventHandler (EventTargetRef        target,
                              EventHandlerUPP       handlerProc,
                              UInt32                numTypes,
                              const EventTypeSpec*  typeList,
                              void*                 userData,
                              EventHandlerRef*      handlerRef);
```

The second parameter, `handlerProc`, is a universal procedure pointer (UPP) to your handler routine. The conversion function `NewEventHandlerUPP` returns a UPP of the required type; for instance,

```
EventHandlerUPP  handlerUPP;

handlerUPP = NewEventHandlerUPP(ThisHandler);
```

(where `ThisHandler` is the name of your handler routine).

The target parameter to `InstallEventHandler` identifies the event target on which the handler is to be installed. You can obtain a reference to the desired target by calling one of the following functions: `GetApplicationEventTarget`, `GetWindowEventTarget`, `GetMenuEventTarget`, or `GetControlEventTarget`.

For convenience, The Carbon Event Manager also defines a set of specialized macros, `InstallWindowEventHandler`, `InstallMenuEventHandler`, and `InstallControlEventHandler`, which accept the targeted object as a parameter, obtain the corresponding target reference for you, and pass it to `InstallEventHandler`. The remaining parameters to these macros are the same as for the `InstallEventHandler` routine itself. For example, the macro call

```
WindowRef theWindow;

InstallWindowEventHandler (theWindow, handlerUPP,
                           numTypes, typeList,
                           userData, &handlerRef);
```

is equivalent to

```
WindowRef theWindow;
EventTargetRef theTarget;

theTarget = GetWindowEventTarget(theWindow);
InstallEventHandler (theTarget, handlerUPP,
                     numTypes, typeList,
                     userData, &handlerRef);
```

A similar macro, `InstallApplicationEventHandler`, needs no parameter to identify the application itself as the target; the call

```
InstallApplicationEventHandler (handlerUPP,
                                numTypes, typeList,
                                userData, &handlerRef);
```

is equivalent to

```
theTarget = GetApplicationEventTarget();
InstallEventHandler (theTarget, handlerUPP,
                     numTypes, typeList,
                     userData, &handlerRef);
```

In all of these cases, the `typeList` parameter specifies the event types for which the handler is to be installed. This parameter is nominally declared as a pointer to an event type specifier giving the class and kind of a single event type; but since the C language considers pointers and arrays to be equivalent, it may actually designate an array of such specifiers for more than one type. The `numTypes` parameter tells how many event types are being specified. For example, the following code installs a single handler for both key-down and key-repeat events:

```
EventTypeSpec    eventTypes[2];
EventHandlerUPP  handlerUPP;

eventTypes[0].eventClass = kEventClassKeyboard;
eventTypes[0].eventKind  = kEventRawKeyDown;

eventTypes[1].eventClass = kEventClassKeyboard;
eventTypes[1].eventKind  = kEventRawKeyRepeat;

handlerUPP = NewEventHandlerUPP(KeyboardHandler);

InstallApplicationEventHandler (handlerUPP,
                                2, eventTypes,
                                NULL, NULL);
```

The `userData` parameter to `InstallEventHandler` is a pointer to an arbitrary data value. Any value you supply for this parameter will later be passed back to your handler routine each time it’s called. You can use this capability for any purpose that makes sense to your program; for example, you can use it to pass a window reference to the handler for window events.

Finally, `handlerRef` is an output parameter that returns an event handler reference, an opaque object representing the new event handler. The handler reference is needed as a parameter to Carbon routines such as `AddEventTypesToHandler` and `RemoveEventTypesFromHandler`, for dynamically changing the event types to which a handler applies, and `RemoveEventHandler`, for deinstalling it. If you’re not going to be using any of these operations, you can simply pass `NULL` for the `handlerRef` parameter, indicating that no handler reference should be returned. In particular, the handler will be disposed of automatically when you dispose of the target object it’s associated with, so there’s no need to call `RemoveEventHandler` explicitly unless for some reason you want to deinstall the handler while the underlying target object still exists.

Listing 2-2 shows an initialization function that installs an event handler for window close events.

__Listing 2-2__  Installing a Carbon event handler

```
#define kWindowTop 100
#define kWindowLeft 50
#define kWindowRight 250
#define kWindowBottom 250

void Initialize (void)

   // Do one-time-only initialization

   {
      WindowRef         theWindow;                 // Reference to window
      WindowAttributes  windowAttrs;               // Window attribute flags
      Rect              contentRect;               // Boundary of content region
      EventTypeSpec     eventType;                 // Specifier for event type
      EventHandlerUPP   handlerUPP;                // Pointer to event handler routine

      windowAttrs = kWindowStandardDocumentAttributes      // Standard document window
                       | kWindowStandardHandlerAttribute;  // Use standard event handler
      SetRect (&contentRect, kWindowLeft,  kWindowTop,     // Set content rectangle
                             kWindowRight, kWindowBottom);
      CreateNewWindow (kDocumentWindowClass, windowAttrs,  // Create the window
                       &contentRect, &theWindow);

      SetWindowTitleWithCFString (theWindow, CFSTR(“Happy Cows”)); // Set title

      eventType.eventClass = kEventClassWindow;          // Set event class
      eventType.eventKind  = kEventWindowClose;          // Set event kind
      handlerUPP = NewEventHandlerUPP(DoWindowClose);    // Point to handler
      InstallWindowEventHandler (theWindow, handlerUPP,  // Install handler
                                 1, &eventType,
                                 NULL, NULL);

      ShowWindow (theWindow);                      // Display window on the screen

      InitCursor ();                               // Set standard arrow cursor

   }  /* end Initialize */
```

By specifying the `kWindowStandardHandlerAttribute` when we call `CreateNewWindow`, we automatically install the standard window handlers. Alternatively, you could call the `InstallStandardEventHandler` function, specifying the window as the event target. 

Listing 2-3 shows an event handler that can respond to the window close event registered in Listing 2-2.

__Listing 2-3__  A window close event handler

```
pascal OSStatus DoWindowClose (EventHandlerCallRef  nextHandler,
                               EventRef             theEvent,
                               void*                userData)

   // Handle window close event

   {
      DoCloseStuff();                 // Do any interesting stuff

      return noErr;                                // Report success

   }  /* end DoWindowClose */
```

You should be aware that the Carbon Event Manager provides a standard handler for the window close event, so this example handler is useful only if you wanted to override the standard close behavior. However, installing your own handler can also be useful if you want to augment the standard behavior. For example, you may want to display a dialog asking if the user wants to save changes before letting the standard handler close the window. To do so, you use the function `CallNextEventHandler`.

The `CallNextEventHandler` function uses `theEventHandlerCallRef` parameter (passed to your event handler), which is a pointer to the next event handler in the calling hierarchy. The Carbon Event Manager will relay the event to the next handler after this one in the hierarchy of handlers for the given type of event, continuing up until it finds a handler willing to accept and process the event. A hander that chooses not to handle the event returns `eventNotHandledErr`, while one that does should return `noErr` after it has finished processing. Assuming that you have not installed any other window close handlers, Listing 2-4 shows how you can use `CallNextEventHandler` to add pre- and post-processing to the standard window close handler.

__Listing 2-4__  Augmenting the standard window close handler


```
pascal OSStatus DoWindowClose (EventHandlerCallRef  nextHandler,
                             EventRef             theEvent,
                             void*                userData)

   // Example event handler to illustrate explicit event propagation

   {
      OSStatus  result;                            // Function result


      /* Your preprocessing here */                // Do preprocessing

// Now propagate the event to the next handler (in this case the standard)
      result = CallNextEventHandler (nextHandler, theEvent);

      if (result == noErr)                         // Did it succeed?
         {
            /* Your postprocessing here */         // Do postprocessing

            /* Note that at this point the  */
            /* standard handler has removed */
            /* the window, so any attempts  */
            /* to access it will cause an   */
            /* error.                       */

            return noErr;                          // Report success

         }  /* end if (result == noErr) */
      else
         return result;                            // Report failure

   }  /* end ThisHandler */
```


Many events require more information than just the basic event to be truly useful. For example, knowing that the mouse was clicked is usually not very interesting unless you know where the click occurred. This additional information is embedded in the event reference structure, and you need to call the function `GetEventParameter` to obtain it. These additional parameters are identified by parameter name and type. A mouse-down event, for example, has four event parameters:

- `kEventParamMouseLocation`, a point (parameter type `typeQDPoint`) giving the screen coordinates at which the mouse button was pressed
- `kEventParamMouseButton`, an integer code (parameter type `typeMouseButton`) identifying which button was pressed (allowing support for a one-, two-, or three-button mouse)
- `kEventParamKeyModifiers`, a set of flag bits (parameter type `typeUInt32`) telling which modifier keys, if any, were being held down at the time the button was pressed
- `kEventParamClickCount`, an integer (parameter type `typeUInt32`) telling how many times the button was clicked in the same location (1 for a single click, 2 for a double click, and so on)

To obtain the mouse location from the event reference `mouseDownEvent`, you would make the following call:

```
EventRef mouseDownEvent;
Point wheresMyMouse;

GetEventParameter (mouseDownEvent, kEventParamMouseLocation, typeQDPoint,
                    NULL, sizeof(Point), NULL, &wheresMyMouse);
```

The values `kEventParamMouseLocation` and `typeQDPoint` specify that you want to obtain the mouse location parameter which is of type `Point`. (There are also a pair of arguments for returning the actual parameter type and size of the value returned; you can specify `NULL` for these arguments if you don’t need this information or don’t expect the actual type and size to differ from those requested.) Obviously, certain parameter values only make sense for certain types of events (for example, you couldn’t obtain a mouse location from the event reference for a window update).

Many events specify a `kEventParamDirectObject` parameter, which usually indicates the actual object the event acted upon. For example, the direct object parameter for a window activation event (`kEventWindowActivated`) would be the reference to the window being activated (that is, a `WindowRef`).

In some cases, you can modify the behavior of an event by setting the value of one or more event parameters with the related Carbon function `SetEventParameter`. For example, if you wanted to snap the window to a particular position as it was being dragged, you could install a handler on the `kEventWindowBoundsChanging` event (which indicates that the window bounds are changing because of resizing or movement) and use `SetEventParameter` to set the origin when some condition is met.

The _Carbon Event Manager Reference_ lists the permissible parameters (and the associated values to pass to `GetEventParameter`) for many event kinds. Documentation for other event parameters is available in the API reference for each technology (such as the_HIObject Reference_).

In addition to the event parameters, you can obtain other attributes of an event by calling various accessor functions. For example, the functions `GetEventClass` and `GetEventKind` each accept an event reference as a parameter and return a 32-bit integer representing the event’s class and kind, respectively:

```
EventRef  theEvent;
UInt32    eventClass;
UInt32    eventKind;

eventClass = GetEventClass(theEvent);
eventKind  = GetEventKind(theEvent);
```

Similarly, the function `GetEventTime` returns the time an event occurred, expressed as a floating point value of type `EventTime` measured in seconds since the system was started up:

```
EventRef   theEvent;
EventTime  timeInSeconds;

timeInSeconds = GetEventTime(theEvent);
```

Another Carbon routine, `GetCurrentEventTime`, returns the current time in seconds since system startup:

```
EventTime  currentTime;

currentTime = GetCurrentEventTime();
```

The Carbon interface defines a set of convenience constants for expressing event times and intervals:

```
#define kEventDurationSecond       1.0
#define kEventDurationMillisecond  ((EventTime)(kEventDurationSecond / 1000))
#define kEventDurationMicrosecond  ((EventTime)(kEventDurationSecond
                                                        / 1000000))
#define kEventDurationNanosecond   ((EventTime)(kEventDurationSecond
                                                        / 1000000000))
#define kEventDurationMinute       kEventDurationSecond * 60
#define kEventDurationHour         kEventDurationMinute * 60
#define kEventDurationDay          kEventDurationHour * 24
#define kEventDurationNoWait       0.0
#define kEventDurationForever     -1.0
```

These constants are especially useful when creating event timers. See [Installing Timers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiinfeer2f) for more information.

Beginning with Mac OS X version 10.2, your application can distinguish between two different user event states. The hardware state is the actual state of an input device. The _queue-synchronized state_ is the state of the device according to the events dispatched from the event queue.

Depending on how long it takes to pop the event off the queue and dispatch it, this queue-synchronized user event may be different from the actual state of the hardware. For example, when the user presses the mouse, a mouse down event is placed into the event queue. If the user releases the mouse immediately while the mouse down event is being handled, then the queue-synchronized mouse button state is still down, but the hardware button state is up.

In most cases, you should determine the state of a user input device by checking the queue-synchronized state rather than polling the hardware directly. Not only does this method use less processor time, but it also provides a better user experience when using nonhardware input methods to place events in the queue (for example, when taking input through Apple events or speech recognition).

The queue-synchronized state of the mouse button and any keyboard modifiers is determined by state variables set by the event dispatcher. For example, the "mouse button state" variable is set to "down" when a mouse-down event is dispatched, and it remains in that state until a mouse-up event is dispatched. You can use the following functions to obtain the values of these state variables:

- `GetCurrentEventButtonState` determines the queue-synchronized state of the mouse button(s). You should use this function instead of the `Button` or `GetCurrentButtonState` functions.

```
UInt32 GetCurrentEventButtonState(void);
```

  Bit zero indicates the state of the primary button, bit one the state of the secondary button, and so on.
- `GetCurrentEventKeyModifiers` determines the queue-synchronized keyboard modifier state. You should use this function instead of `EventAvail` or `GetCurrentKeyModifiers`.

```
UInt32 GetCurrentEventKeyModifiers(void);
```

  See [Table 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwvgvzv) for a listing of keyboard modifier bits.

Note that `GetCurrentEventButtonState` and `GetCurrentEventKeyModifiers` do not return useful values if your application is not active. If your application wants to determine the current mouse or keyboard modifier state while in the background, it must query the hardware using `GetCurrentButtonState` or `GetCurrentKeyModifiers`.

When a user event is dispatched, the Carbon Event Manager caches it as the current event and disposes of it after the event is handled. The `GetCurrentEvent` function retrieves the event currently being dispatched (which could be `NULL` if the event is not a user event):

```
EventRef GetCurrentEvent(void);
```

You should call this function only from an event handler to determine what user event (if any) triggered the call to your handler.

The Carbon Event Manager has a special class of events that correspond with the command IDs introduced with Mac OS 8.0. A command ID is a location-independent way to identify an action or command. For example, if you associate a command ID with a menu item, a command event is generated whenever that item is selected, whether by mouse selection or keyboard equivalent. If you associate the same ID with a button, then a menu selection, keyboard equivalent command, or button press will all generate the same event. Because standard handlers can take care of much of the busywork (such as toggling the button, flashing the selected menu or menu item), you only need to handle one event for three different types of selection.

Command events are initially sent to the event target associated with the command. For example, a menu command event is sent to the menu event target, while a command associated with a button is sent to that control.

Command event handlers can be placed anywhere in the containment hierarchy, but it’s usually convenient to place them at the application level. Doing so allows you to install one handler that can take the event whether it propagates up the containment hierarchy from a control or from a menu.

Command IDs are 32-bit integers, but they are usually specified as a four-character code. Many common menu items and controls have reserved codes. For example,

```
kHICommandOK        = 'ok '; // the OK button (as in a dialog)
kHICommandCopy      = 'copy';// the Copy menu item
kHICommandAbout     = 'about';// the About item
```

If you want to create custom command IDs, you must define them in your application and register them by calling the Menu Manager function `SetMenuItemCommandID` or the Control Manager function `SetControlCommandID`, depending on the desired target.

The event class for commands is `kEventClassCommand`, and to receive commands to process, the event kind is `kEventCommandProcess`. The command ID itself is stored in the event reference and you need to call the `GetEventParameter` function to retrieve it. For example, to handle a (fictitious) menu item Explode, you would need to first define the command ID, register it with the Menu Manager, and then install the handler in your initialization code:

```
const MenuCommand kCommandExplode = FOUR_CHAR_CODE ('Boom');

void MyInitialize()
    {
    …
    SetMenuItemCommandID (GetMenuRef(mFile), iExplode, kCommandExplode);
    …
    EventTypeSpec myEvents = {kEventClassCommand, kEventCommandProcess};
    InstallApplicationEventHandler(NewEventHandlerUPP(MyEventHandler),
                                1, &myEvents, 0, NULL);
    …
    }
```

The constant `iExplode` represents the index value of the Explode item in the File menu.

This example installs the handler `MyEventHandler` on the application target, but you can choose a different target if that better suits your needs.

Your actual event handler needs to obtain the command ID of the Explode command using `GetEventParameter`. The command ID is stored as the direct object parameter:

```
HICommand commandStruct;

GetEventParameter (event, kEventParamDirectObject,
                    typeHICommand, NULL, sizeof(HICommand),
                    NULL, &commandStruct);

if (commandStruct.commandID == kCommandExplode)
    {
        // process explode command
    }
```


The Carbon Event Manager provides two ways of obtaining keyboard information: as raw keyboard events, or as text input events. (Text input events are those that have been processed by the Text Services Manager). To avoid conflict with other input methods, you should rely on text input events for handling text.

Text input events are of class `kEventClassTextInput`, and the event kind used to signify text input is `kEventTextInputUnicodeForKeyEvent`. Text returned by a text input event may be a character or a string, depending on the circumstances, so you should not make assumptions about its length. For more information about text input methods as well as about event kinds directly related to the Text Services Manager, see the Text Services Manager documentation.

To obtain the actual text, you need to call the `GetEventParameter` function, specifying the `kEventParamTextInputSendText` parameter, as shown in Listing 2-5

__Listing 2-5__  Obtaining text from a text input event

```
EventRef     theTextEvent;
UniChar      *text;
UInt32       actualSize;

GetEventParameter (theTextEvent, kEventParamTextInputSendText,
                typeUnicodeText, NULL, 0, &actualSize, NULL);

text = (UniChar*) NewPtr(actualSize);


GetEventParameter (theTextEvent, kEventParamTextInputSendText,
                typeUnicodeText, NULL, actualSize, NULL, text);
```

This example makes two calls to `GetEventParameter`, the first to obtain the size of the string, and the second to actually obtain it. The rationale for doing so is that the string can be arbitrarily large as it may have resulted from an inline input session intended for a nonRoman script.

If your application doesn’t support Unicode, you can examine the `kEventParamTextSendKeyboardEvent` parameter to obtain the raw keyboard event that generated the text event and from that event extract the equivalent Macintosh character codes.

In rare cases where your application might need to handle individual key presses (for example, for game controls, or if it will perform its own keyboard translation), you may want to obtain the key presses before the Text Services Manager processes them. In such cases, you should install handlers to obtain raw keyboard events (class `kEventClassKeyboard`).

In any case, all keyboard and text input events are sent to whichever target currently has the user focus (for example, the window, or the text field control). If desired, you can install an event handler on the _user focus event target_, which you obtain by calling `GetUserFocusEventTarget`. All events directed to the current user focus will then be sent to your handler. If you don’t handle the event (or if no handler was installed), the event is then propagated to the actual target that has the user focus.

In today’s graphical user interfaces, the mouse provides the user’s primary means of controlling and interacting with the system. All of the user’s actions with the mouse are reported to your program in the form of mouse events.

All mouse events have parameters named `kEventParamMouseLocation` and `kEventParamKeyModifiers` giving, respectively, the location of the mouse cursor on the screen and the modifier keys that were being held down at the time the event occurred. The value of `kEventParamMouseLocation` is a point giving the horizontal and vertical position of the mouse in global coordinates.

The value of the `kEventParamKeyModifiers` parameter is an unsigned 32-bit integer (type UInt32) containing flag bits corresponding to the various modifier keys. The mask constants shown in Table 2-1 can be used to extract the bit representing any desired modifier key. A bit value of 1 means that the given key was down when the event occurred; 0 means it was not. Thus, for example, you could use the code in Listing 2-6 to determine whether the Caps Lock key was down at the time of a mouse event:

__Listing 2-6__  Obtaining the modifier key for a mouse event

```
EventRef  theEvent;
UInt32    modifierKeys;

GetEventParameter (theEvent,
                   kEventParamKeyModifiers,
                   typeUInt32, NULL,
                   sizeof(modifierKeys), NULL,
                   &modifierKeys);

if (modifierKeys & alphaLock)
/* Caps Lock down */
else
   /* Caps Lock not down */
```


__Table 2-1__  Mask constants for modifier keys

| Mask constant | Modifier |
| `cmdKey` | Command |
| `shiftKey` | Shift |
| `alphaLock` | Caps Lock |
| `optionKey` | Option |
| `controlKey` | Control |
| `kEventKeyModifierNumLockMask` | Num lock (Mac OS X only) |
| `kEventKeyModifierFnMask` | Fn (Function) (Mac OS X only) |

For a complete listing of modifier constants, see the `EventModifers` enumeration in `Events.h`.

When the user presses or releases the mouse button, it’s reported to your program by a mouse-down or mouse-up event (event kind `kEventMouseDown` or `kEventMouseUp`), respectively. Ordinarily, such events are handled by the standard event handler, which analyzes them and converts them into higher-level events representing the meaning of the mouse action, such as `kEventWindowClose` (when the user clicks a window’s close button), `kEventWindowClickContentRgn` (when the click is in the window’s contents), `kEventControlHit` (when it’s in a control such as a push button or checkbox), or `kEventCommandProcess` (when the user chooses a command from a menu). These higher-level events are usually all your program needs to be concerned with. However, you’re free to intercept the “raw” mouse events and handle them yourself if necessary.

In addition to the `kEventParamMouseLocation` and `kEventParamKeyModifiers` parameters shared by all mouse events, mouse-up and mouse-down events have two additional parameters: `kEventParamMouseButton` and `kEventParamClickCount`. The latter is used to identify multiple (for instance, double or triple) mouse clicks, in case your program wishes to assign some special meaning to them. Consecutive presses of the mouse button are considered to constitute a multiple click if they fall within a certain time interval, which is under the user’s control via the Mouse pane of System Preferences (on Mac OS X) or the Mouse control panel (on earlier versions). The Classic Event Manager function `GetDblTime` returns the current value of this interval, expressed in ticks (sixtieths of a second, the time unit used by earlier versions of Mac OS). When a mouse-down event is separated from the previous such event by more than the multiple-click interval, its `kEventParamClickCount` parameter is set to 1; if it falls within the double-click interval the parameter is incremented by 1 from that of the previous event. Thus the first event in a multiple click has a click count of 1, the second has a click count of 2, the third 3, and so on. (Triple clicks are the most your program should realistically process.)

Unlike earlier versions of Mac OS, which were limited to a one-button mouse, Carbon is designed to support multiple mouse buttons. (Theoretically, it can handle as many as 65,535 buttons, though the most you’re likely to encounter in practice is 3.) The `kEventParamMouseButton` parameter of a mouse-down or mouse-up event identifies which button was pressed or released, using one of the following constants:

```
typedef UInt16  EventMouseButton;
enum
   {
      kEventMouseButtonPrimary   = 1,
      kEventMouseButtonSecondary = 2,
      kEventMouseButtonTertiary  = 3

   }; /* end enum */
```

On a two- or three-button mouse, the left button is normally considered primary and the right button secondary, but left-handed users can reverse these settings as a matter of preference. The middle button on a three-button mouse is always the tertiary button.

The basic task of moving the cursor around on the screen to reflect the physical movements of the mouse is handled for you automatically, with no need for any explicit action on your program’s part. In addition, each time the cursor location changes by as much as one pixel horizontally or vertically, a mouse-moved event (`kEventMouseMoved`) is generated. If the user is also holding down the mouse button (or any button on a multiple-button mouse), the result is a mouse-dragged event (`kEventMouseDragged`) instead. Both types of event have the usual `kEventParamMouseLocation` and `kEventParamKeyModifiers` parameters, and the mouse-dragged event also has a `kEventParamMouseButton` parameter to identify the button being held down, as described under [Mouse Button Events](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiireeissd).

As with the primary mouse button, it’s possible to poll the mouse’s location on the screen directly by calling the Classic Event Manager function `GetMouse`. However, using this kind of direct polling to track the mouse’s movements is usually not a good idea. For instance, as mentioned above, a common reason for tracking the mouse is to provide visual feedback on the screen during a drag by performing some repeated action for as long as the user holds down the button. Doing this with an active polling loop such as

```
while ( WaitMouseUp() )
   {
      GetMouse (&mouseLoc);
      /* Provide feedback based on mouse location */

   } /* end while ( WaitMouseUp() ) */
```

is horribly inefficient, needlessly tying up the processor while spinning the loop waiting for something to happen. Using mouse-dragged events to do the tracking offers some improvement, since the event loop suspends execution except while actively processing an event and hence consumes no extraneous processor cycles. This allows the idle time to be put to better use running other programs or processes in the background—including any periodic timers you may have installed yourself (see [Installing Timers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiinfeer2f)). However, there is an even better way, using the Carbon Event Manager function `TrackMouseLocation`, as shown in Listing 2-7.

__Listing 2-7__  Tracking the mouse with TrackMouseLocation

```
Point                mouseLoc;
MouseTrackingResult  trackingResult;

GetMouse (&mouseLoc);
trackingResult = kMouseTrackingMouseDown;

while (trackingResult != kMouseTrackingMouseUp)
   {
      /* Provide feedback based on mouse location */
      TrackMouseLocation (NULL, &mouseLoc, &trackingResult);

   } /* end while (trackingResult != kMouseTrackingMouseUp) */
```

The call to `TrackMouseLocation` suspends execution until either the mouse’s location or button state changes. It then returns, in its second and third parameters, the coordinates of the new mouse location and a tracking result indicating the nature of the mouse occurrence. (The first parameter specifies a graphics port in whose coordinate system to report the mouse location; passing `NULL` for this parameter designates the current port, which is usually what you want.) The tracking result returned is one of the following values:

```
typedef UInt16  MouseTrackingResult;
enum
   {
        kMouseTrackingMouseDown = 1,
        kMouseTrackingMouseUp = 2,
        kMouseTrackingMouseExited   = 3,
        kMouseTrackingMouseEntered  = 4,
        kMouseTrackingMouseDragged = 5,
        kMouseTrackingKeyModifiersChanged = 6,
        kMouseTrackingUserCancelled = 7,
        kMouseTrackingTimedOut = 8,
        kMouseTrackingMouseMoved = 9

   }; /* end enum */
```

The tracking results `kMouseTrackingExited` and `kMouseTrackingEntered` are used by another related Carbon routine, `TrackMouseRegion`. This is typically called after a mouse press in a control (such as a checkbox or a window’s close button), to track the mouse’s movements in and out of the control so you can provide appropriate visual feedback by highlighting and unhighlighting the control accordingly. The standard event handler ordinarily does all this for you and reports the result with a higher-level event such as `kEventWindowClose`, `kEventWindowZoom`, or `kEventControlHit`; but you may occasionally encounter a situation where you need to make the `TrackMouseRegion` call and process the results yourself.

Listing 2-8 shows a code fragment illustrating how to use `TrackMouseRegion` to respond to a mouse press in a control.

__Listing 2-8__  Tracking the mouse in a region

```
RgnHandle            controlRegion;                // Region occupied by control
Boolean              isInRegion;                   // Mouse released in region?
MouseTrackingResult  trackingResult;               // Tracking result

/* Set controlRegion to control's region */        // Indicate region

trackingResult = kMouseTrackingMouseEntered;       // Initialize for first
                                                  // pass of loop

while (trackingResult != kMouseTrackingMouseUp) // Loop until released
   {
      switch (trackingResult)                      // Dispatch on tracking result
         {
            case kMouseTrackingMouseEntered:       // Highlight on entry
               /* Highlight control */
               break;

            case kMouseTrackingMouseExited:        // Unhighlight on exit
               /* Unhighlight control */
               break;

         } /* end switch (trackingResult) */

      TrackMouseRegion (NULL, controlRegion,       // Track mouse in region
                        &isInRegion,
                        &trackingResult);

   } /* end while (trackingResult != kMouseTrackingMouseUp) */

if (isInRegion)                                    // Released in region?
   /* Perform associated action */                 // Take action in response
```

You call `TrackMouseRegion` repeatedly for as long as the mouse button remains down, passing as a parameter a region representing the area the control occupies on the screen. Each time the mouse crosses the boundary in or out of the specified region, `TrackMouseRegion` returns with a tracking result of `kMouseTrackingEntered` or `kMouseTrackingExited`, indicating whether to highlight or unhighlight the control. (Mere mouse movements that don’t cross the region boundary are not reported.) When the mouse button is released, `TrackMouseRegion` returns the tracking result `kMouseTrackingMouseReleased` along with a Boolean value indicating whether the button was released inside or outside the region; you can then use this information to determine whether to perform the action associated with the control.

In Mac OS X version 10.2 and later, you can designate special mouse tracking regions within windows. When the mouse enters one of these regions, your application receives a `kEventMouseEntered` event (`kEventClassMouse`). When the mouse leaves, the application receives a `kEventMouseExited` event. A window can contain any number of regions; each mouse tracking region has a unique ID, which makes it easy to determine which region was entered. If desired, you can also temporarily disable a region.

Mouse tracking regions make it simple to implement various rollover effects such as highlighting a clickable area, or changing the cursor when it enters a region. If you must use processor-intensive polling for mouse locations (for example, in a drawing program), you can use mouse tracking regions to allow pollling only within particular regions of interest.

To create a mouse tracking region, you call the `CreateMouseTrackingRegion` function:

```
OSStatus CreateMouseTrackingRegion (WindowRef inWindow,
                            RgnHandle inRegion,
                            RgnHandle inClip,
                            MouseTrackingOptions inOptions,
                            MouseTrackingRegionID inID,
                            void* inRefCon,
                            EventTargetRef inTargetToNotify,
                            MouseTrackingRef* outTrackingRef);
```

- The `inWindow` parameter indicates which window owns this region. Mouse tracking regions are always bound to a particular window.
- The `inRegion` parameter is a standard region handle defining the tracking region.
- The `inClip` parameter specifies an optional clip region. If the clip region is valid (that is, you don’t pass `NULL)`, the active tracking region is the intersection of the tracking region and the clip region.
- For mouse tracking options you can pass either `kMouseTrackingOptionsLocalClip` or `kMouseTrackingOptionsGlobalClip`:

  - `kMouseTrackingOptionsLocalClip` indicates that the region is defined in local coordinates and that the region is clipped to the owning windows’s content region.
  - `kMouseTrackingOptionsGlobalClip` indicates the region is defined in global coordinates and that the region is clipped to the owning window’s structure region.
- The `inID` parameter holds a unique mouse tracking ID, which is a combination of an `OSType`, which is a four-character code that uniquely defines your application, and an integer:

```
struct MouseTrackingRegionID {
                    OSType signature;
                    SInt32 id;
    }
```

  If you have not already done so, you can register an application signature with Apple Developer Technical Support.
- If you want to associate any application-specific data with this region, you can pass it in the `inRefCon` parameter.
- The `inTargetToNotify` parameter is currently unused; pass `NULL`.

On return, you receive a mouse tracking reference which you can pass to additional mouse tracking region functions. This reference is also included in the event reference for the `kEventMouseEntered` and `kEventMouseExited` events. Use the `GetEventParameter` function to obtain the direct object parameter.

Additional useful mouse tracking region functions include the following:

- To dispose of a tracking region, use the `ReleaseMouseTrackingRegion` function:

```
OSStatus ReleaseMouseTrackingRegion (MouseTrackingRef inMouseRef);
```

  Note that because mouse tracking regions are associated with a window, disposing the window will also dispose of its tracking regions.
- To increase the reference count of a tracking region, call the `RetainMouseTrackingRegion` function:

```
OSStatus RetainMouseTrackingRegion (MouseTrackingRef inMouseRef);
```

  Calling `ReleaseMouseTrackingRegion` decrements the reference count; if the count reaches 0, the tracking region is disposed.
- To obtain the ID of a mouse tracking region, call the `GetMouseTrackingRegionID` function:

```
OSStatus GetMouseTrackingRegionID (MouseTrackingRef inMouseRef,
                                MouseTrackingRegionID* outID);
```
- To enable or disable a mouse tracking region, call the `SetMouseTrackingRegionEnabled` function:

```
OSStatus SetMouseTrackingRegionEnabled (MouseTrackingRef inMouseRef,
                                        Boolean inEnabled);
```

  You can use this function to adjust tracking regions that are dependent on the state of your application.
- To obtain the application-specific data associated with the tracking region, call the `GetMouseTrackingRegionRefCon` function:

```
OSStatus GetMouseTrackingRegionRefCon (MouseTrackingRef inMouseRef,
                                        void** outRefCon);
```

Mac OS X v10.4 introduced new HIView-based tracking region functions. These work much like the older mouse tracking regions, with the following exceptions:

- You create these tracking areas on a per-view, rather than per-window basis.
- The tracking areas are described using HIShape objects rather than QuickDraw regions.
- The tracking area is identified by a `UInt64` integer rather than a data structure.
- The area entered and exited events are `kEventControlTrackingAreaEntered` and `kEventControlTrackingAreaExited` respectively. You obtain the tracking area reference in the `kEventParamHIViewTrackingArea` parameter (`typeHIViewTrackingAreaRef`).

To create a view-based tracking area, call the `HIViewNewTrackingArea` function:

```
OSStatus HIViewNewTrackingArea(
  HIViewRef                inView,
  HIShapeRef               inShape,       /* can be NULL */
  HIViewTrackingAreaID     inID,
  HIViewTrackingAreaRef *  outRef)
```

To modify a tracking area, call `HIViewChangeTrackingArea`:

```
OSStatus HIViewChangeTrackingArea(
  HIViewTrackingAreaRef   inArea,
  HIShapeRef              inShape)
```

To obtain an area’s ID, call `HIViewGetTrackingAreaID`:

```
 OSStatus HIViewGetTrackingAreaID(
   HIViewTrackingAreaRef   inArea,
   HIViewTrackingAreaID *  outID)
```

To dispose of a tracking area, call `HIViewDisposeTrackingArea`:

```
OSStatus HIViewDisposeTrackingArea (HIViewTrackingAreaRef inArea)
```

If possible, you should use view-based tracking areas in place of the older tracking regions.

Installing a timer is similar to installing an event handler. Timers are associated with a particular event loop (usually the program’s main loop), and they fire as the loop runs. Instead of a list of event types, you specify an initial delay before the timer fires for the first time and a timer interval between subsequent firings, both expressed in seconds. (Setting the timer interval to 0 produces a one-shot timer that will fire only once, at the expiration of the initial delay.) As in installing an event handler, you can also supply an arbitrary item of user data that will be passed back to your timer routine each time it’s called. The timer routine itself is identified with a universal procedure pointer of type `EventLoopTimerUPP`, obtained using the conversion function `NewEventLoopTimerUPP`. Listing 2-9 shows how to install a timer routine named `TimerAction` in the program’s main event loop with an initial delay of 5 seconds, a timer interval of 1 second, and no user data item

__Listing 2-9__  Installing a timer

```
EventLoopRef       mainLoop;
EventLoopTimerUPP  timerUPP;
EventLoopTimerRef  theTimer;

mainLoop = GetMainEventLoop();
timerUPP = NewEventLoopTimerUPP(TimerAction);

InstallEventLoopTimer (mainLoop,
                       5*kEventDurationSecond,
                       kEventDurationSecond,
                       timerUPP,
                       NULL,
                       &theTimer);
```

The last parameter of the `InstallEventLoopTimer` function is an output parameter that returns a _timer reference_ representing the timer just installed. This value is needed as a parameter to various Carbon Event Manager functions that operate on timers, the most important of which is `RemoveEventLoopTimer`, for uninstalling the timer. This same timer reference will also be passed automatically to your timer routine each time it’s called.

The timer routine itself must have the following prototype:

```
pascal void TimerAction (EventLoopTimerRef  theTimer,
                         void* userData);
```

where `theTimer` is the timer reference identifying the timer and `userData` is the data value you supplied at the time the timer was installed.

One more useful function is `SetEventLoopTimerNextFireTime`, which resets the interval until the next time the timer fires. For example, if `theTimer` is the timer installed in the example above, the call

```
SetEventLoopTimerNextFireTime (theTimer, kEventDurationMinute);
```

will cause the timer to “sleep” for one minute and then resume its one-second firing cycle. The effect is equivalent to deinstalling the timer and then reinstalling it with a new initial delay and the same timer interval.

A variant of the basic timer is the idle timer, which is available in Mac OS X v.10.2 and later. The idle timer functions just like a normal timer except that it does not fire until the user has been inactive for the initial delay time. Such timers are useful for letting the application know that it is safe to do some processing without interfering with the user. For example, if the user is entering text into a search field, you should wait for a second or two after the user has stopped typing before beginning the search.

To install an idle timer, you call the `InstallEventLoopIdleTimer` function, which has the same format as the basic `InstallEventLoopTimer` function:

```
OSStatus InstallEventLoopIdleTimer(
                            EventLoopRef         inEventLoop,
                            EventTimerInterval   inFireDelay,
                            EventTimerInterval   inInterval,
                            EventLoopIdleTimerUPP    inTimerProc,
                            void *               inTimerData,
                            EventLoopTimerRef *  outTimer);
```

The only difference is that the timer callback routine takes an additional `EventIdleAction` parameter indicating the idle status:

```
pascal void IdleTimerAction (EventLoopTimerRef inTimer,
                                void *inUserData,
                                EventIdleAction inAction );
```

When your idle timer routine is called, it is passed one of three constants indicating the current idle status:

```
enum
{
    kEventLoopIdleTimerStarted,
    kEventLoopIdleTimerIdling,
    kEventLoopIdleTimerStopped
}
EventIdleAction;
```

- `kEventLoopIdleTimerStarted` indicates that the idle period has just begun (and this is the first time your callback is being called for this period).
- `kEventLoopIdleTimerIdling` indicates that your callback is being called in the middle of an idle period.
- `kEventLoopIdleTimerStopped` is sent to your callback function when the idle period ends (for example, when the user hits a key).

For example, say your application wants to calculate the value of pi. When your callback function receives the `kEventLoopIdleTimerStarted` constant, you create a special pi calculation object. Each time you receive `kEventLoopIdleTimerIdling`, you call an object method to calculate the next digit. When you receive `kEventLoopIdleTimerStopped`, you store the currently calculated value of pi and dispose of the pi calculation object.

In most cases, using the `RunApplicationEventLoop` function to collect and dispatch events is the simplest and most practical way to handle events. However, sometimes you may want more control over the event collection and dispatching mechanism, or you may need to process events that don’t occur in the main application thread. In cases like these, you can call other Carbon Event Manager functions to manually collect and dispatch your events.

The `RunApplicationEventLoop` function itself calls several Carbon Event Manager functions to accomplish its task:

- `ReceiveNextEvent` runs the low-level event loop, placing events as they occur into the event queue. The function returns when an event you specified occurs, or when the specified timeout is exceeded.

```
OSStatus ReceiveNextEvent(
            UInt32 inNumTypes,
            const EventTypeSpec *inList,
            EventTimeout inTimeout,
            Boolean inPullEvent,
            EventRef *outEvent);
```

  - The `inNumTypes` parameter specifies the number of events for which `ReceiveNextEvent` should return. Passing 0 indicates you want to return on all events.
  - The `inList` parameter points to the `EventTypeSpec` structure or array containing the class and kind of events to return on. Passing `NULL` indicates that you want to return on all events.
  - The `inTimeout` parameter is the duration to wait before timing out.
  - The `inPull` parameter specifies if whether you want `ReceiveNextEvent` to pull the event off the queue when it returns. Passing `true` causes the event to be pulled. If you pass `false`, `ReceiveNextEvent` only peeks at the event to determine its type. You still can dispatch the event, but it remains on the queue.
  - On return, `outEvent` contains the event that caused `ReceiveNextEvent` to return.
- `GetEventDispatcherTarget` gets the event target reference for the _standard toolbox dispatcher_, which is the default target for all events. The toolbox dispatcher determines the proper target for each event (window, control, and so on) and sends the event there. Note that because the toolbox dispatcher is itself a valid event target, you can actually attach a handler to it. Such a handler can intercept an event before it gets sent on to the actual event target.
- `SendEventToEventTarget` dispatches the event to the appropriate event target.
- `ReleaseEvent` releases the event (disposing of it if necessary).

Listing 2-10 shows how you can use these calls to implement the basic functionality of `RunApplicationEventLoop`.

__Listing 2-10__  Processing events manually

```
EventRef theEvent;
EventTargetRef theTarget;

theTarget = GetEventDispatcherTarget();

    while  (ReceiveNextEvent(0, NULL,kEventDurationForever,true,
            &theEvent)== noErr)
        {

            SendEventToEventTarget (theEvent, theTarget);
            ReleaseEvent(theEvent);
        }
```

The `ReceiveNextEvent` function is blocked forever (`kEventDurationForever`) until an event occurs. Specifying zero and null for the first two parameters indicates that `ReceiveNextEvent` should return on all events. (Alternatively, you could specify that the function wait only for particular events). Passing `true` in the third parameter indicates that the application should take ownership of the event (which means it is pulled off the event queue).

After an event occurs, we dispatch it to the event dispatcher target, which automatically sends it to the proper event target. Because the application owns the event, the application is then responsible for releasing it by calling `ReleaseEvent`. (There is also a complementary function `RetainEvent`, which you can use to increment the reference count of the event, thus ensuring that it will not get disposed before you are finished with it.)

The only drawback to making your own event loop dispatching calls in the main application thread is that you won’t get the standard application event handler installed. Specifically, the `RunApplicationEventLoop` function installs handlers to do the following:

- Allow clicks in the menu bar to begin menu tracking
- Dispatch Apple events by calling `AEProcessAppleEvent`
- Respond to quit Apple events by quitting `RunApplicationEventLoop`.

One way to work around this limitation is by creating a dummy custom event handler. When you are ready to process events, create the dummy event yourself, post it to the queue. and then call `RunApplicationEventLoop` (to install the standard application event handler). The dummy event handler can then process the events manually. For an example of using this method, see [Technical Q&A 1061](https://developer.apple.com/qa/qa2001/qa1061.html) in Developer Documentation Technical Q&As.

In addition to processing and dispatching events, the Carbon Event Manager also lets you create your own events. You may want to create your own custom events, or you might want to reproduce standard events.

You create an event using the `CreateEvent` function:

```
OSStatus CreateEvent( CFAllocatorRef inAllocator<null>,
                    UInt32 inClassID, UInt32 kind,EventTime when,
                    EventAttributes flags, EventRef* outEvent);
```

- The `inAllocator` parameter refers to the allocator you want to use to allocate memory for the event. You can pass `NULL` to specify the default allocator.
- The `inClassID` and `kind` parameters indicate the event class and kind. If you are creating custom events, you need to define new values that don’t conflict with existing event classes and kinds. And, of course, you must specify this class and kind when your register a handler to process this type of event.
- The `when` parameter indicates when the event occurred. You can pass 0 to specify the current event time (as returned by the `GetCurrentEventTime` function). This value may or may not be useful for custom events.
- The `flags` parameter indicates any event attributes you may want to set. The current choices are `kEventAttributeNone` and `kEventAttributeUserEvent`.
- On return, `outEvent` contains the newly-created event reference.

If your event requires additional information, you can add data by calling `SetEventParameter`. If you are creating custom events, you need to define constants for your parameter names and types if they don’t already exist. For example, if you define a parameter for a screen location, you may want to define a new parameter name, but you can probably still use `typeQDPoint` for the parameter type.

Once you create an event, you need to send it to a handler. There are two basic methods for doing so:

- You can post the event to a queue by calling the `PostEventToQueue` function. You need to obtain the queue reference for the queue you want to post to by calling either `GetCurrentEventQueue` (which returns the current thread’s queue) or `GetMainEventQueue` (which returns the queue for the main application thread). The event you post will not be processed until it is pulled from the queue and dispatched to the appropriate event target.

  Note that in Mac OS X, you can indicate in the event reference where a posted event should be dispatched by specifying a `kEventParamPostTarget` event parameter.
- You can send it directly to the desired event target by calling `SendEventToEventTarget`. If this is a custom event, the target you choose should be the one to which you attached your custom event handler. Dispatching the event yourself will ensure that your handler is called immediately.

Note that if you send an event to the standard toolbox dispatcher and it does not recognize it (that is, it’s a custom event), then it will dispatch the event to the application event target (unless you specified an event target in your custom event using the `kEventParamPostTarget` parameter).

If you want to create and process command events, the Carbon Event Manager provides the function `ProcessHICommand`:

```
OSStatus ProcessHICommand (const HICommand* inCommand);
```

When you pass an Command ID to `ProcessHICommand`, it builds a `kEventCommandProcess` event containing the ID and then dispatches the event to either

- a menu, if the command is defined in a menu, or
- the current user focus

The Carbon Event Manager scales to work with multiple execution threads. If you are creating cooperative threads, each thread shares the main application event loop and queue, so your event handling mechanism does not change. However, the `RunApplicationEventLoop` function never explicitly yields to other threads, so you should create a timer that will call the Thread Manager function `YieldToAnyThread` as necessary.

If you create preemptively-scheduled threads, each such thread contains its own event queue and needs to be processed independently.

Because `RunApplicationEventLoop` works only for the main execution thread, any preemptive threads you create should use `ReceiveNextEvent` to process events, as described in `[“Processing Events Manually”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiizeuqskg)`. Depending on the thread, you can wait for particular events to occur or process every event (much the way `RunApplicationEventLoop` does).

You use the event queues primarily to communicate between threads. For example, if you wanted your preemptive thread to tell the main application it was finished processing data, it could post a custom event on the main application event queue. One advantage of this method is that your application does not have to use extra processing time polling a Multiprocessing Services queue or semaphore.

Depending on the circumstances, either Carbon event queues or Multiprocessing Services notification methods may be suitable for signaling between threads. If you want to use Carbon event queues, here is breakdown of how you might do it:

- After first creating the thread, it should call `GetCurrentEventQueue` to obtain its queue reference. It can then create a custom event signifying that it is ready for use, call `SetEventParameter` to store the queue reference in the event, then post the event to the main thread. It can then call `ReceiveNextEvent`, blocking until someone sends it an event.
- When the main thread receives the ready event, the appropriate handler can call `GetEventParameter` to extract the queue reference. Then, whenever it needs to signal the other thread, it can create a “start processing” event and post it to the proper queue.
- Whenever the preemptive thread receives the process event, it can carry out its particular task. Afterwards, it posts a “processing completed” event to the main event queue and returns to a blocked state in `ReceiveNextEvent`.
- When it comes time to terminate the thread, the main application thread sends a termination event and waits for confirmation from the thread.

For more information about creating cooperatively-scheduled threads, see the Thread Manager documentation and [Technical Q&A 1061](https://developer.apple.com/qa/qa2001/qa1061.html), “RunApplicationEventLoop and the Thread Manager.” For information about creating preemptively-scheduled threads, see the Multiprocessing Services documentation.

If you need to create application-modal dialogs, you can use several Carbon Event Manager functions to enter and exit the modal state. A modal dialog is a window that allows no other application actions until the window is dismissed. For example, an alert that warns the user about the consequences of some action is typically a modal dialog.

For more information about the proper design and usage of modal dialogs, see _Inside Mac OS X: Aqua Human Interface Guidelines_.

The simplest way to enter the modal state is to call the function `RunAppModalLoopForWindow`, passing the window reference of the window you want to make modal. This function is analogous to the `RunApplicationEventLoop` functions for applications. It runs a sub-event loop, disables the menu bar and dispatches events.

When in a modal state, the standard toolbox dispatcher only processes events for the modal window and any window above it (that is, closer to the front). Typically a modal window is frontmost, but if another window is in front of it, that window will also receive events. This feature was designed to allow stacked modal dialogs. See [Processing Events Manually](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiizeuqskg) for more information about the toolbox dispatcher.

To leave the modal state, you call the function `QuitAppModalLoopForWindow`.

To make construction of modal dialogs simpler, the Carbon Event Manager also includes some utility functions for setting the default and cancel buttons.

```
OSStatus SetWindowDefaultButton(
                WindowRef    inWindow,
                ControlRef   inControl);      /* can be NULL */

OSStatus SetWindowCancelButton(
                WindowRef    inWindow,
                ControlRef   inControl);      /* can be NULL */

OSStatus GetWindowDefaultButton(
                WindowRef     inWindow,
                ControlRef *  outControl);

OSStatus GetWindowCancelButton(
                WindowRef     inWindow,
                ControlRef *  outControl);
```

Calling the “set” versions of these functions causes the standard event handlers to map keyboard input to the respective controls: pressing the Return or Enter keys will activate the default button, and pressing escape or Command-period will activate the cancel button.

As with the standard event loops, you can also choose to run the modal event loop manually and dispatch events yourself. To do so, you call the low-level function `BeginAppModalStateForWindow` for the desired window. Once in this state you can call the usual low-level event processing functions. (`ReceiveNextEvent`, `RunCurrentEventLoop`). Note that because the event filtering occurs in the toolbox dispatcher (not the event queue), it is possible to receive and process events that are not related to the window. To leave the modal state, you call `EndAppModalStateForWindow`.

[Next](Document%20Revision%20History.md)[Previous](Carbon%20Event%20Manager%20Concepts.md)

