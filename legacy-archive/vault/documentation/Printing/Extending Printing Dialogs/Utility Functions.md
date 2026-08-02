---
title: Extending Printing Dialogs
apple_id: TP30000979
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/Printing/Conceptual/ExtPrintingDialogs/Utilities/Utilities.html
archived_at: '2026-07-18T01:52:19.420135Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Extending Printing Dialogs](Introduction%20to%20Extending%20Printing%20Dialogs.md)


[Next](Printing%20Plug-in%20Header%20Functions.md)[Previous](Integration%20Tasks.md)

# Utility Functions

In your custom code, you might need to embed a control in a dialog pane, get a ticket reference, or implement a help event handler.

This appendix explains how to perform these tasks. You should be able to use this sample code in a real-world project with little or no modification.

Listing A-1 implements a function that embeds a nib-based control inside the dialog pane provided by the printing system.

This function takes three parameters—a nib-based window, a Carbon container control (called a user pane), and the ID of the nib-based control being embedded.

During execution, this function

- gets a reference to the nib-based control
- positions the control with respect to the dialog window
- embeds the control inside the dialog user pane
- returns a reference to the control being embedded

__Listing A-1__  Embedding a nib-based control inside a dialog pane

```
extern OSStatus MyEmbedControl (
    WindowRef nibWindow,
    ControlRef userPane,
    const ControlID *controlID,
    ControlRef* outControl
)

{
    ControlRef control = NULL;
    OSStatus result = noErr;

    *outControl = NULL;

    result = GetControlByID (nibWindow, controlID, &control);// 1

    if (result == noErr)
    {
        SInt16 dh, dv;
        Rect nibFrame, controlFrame, paneFrame;

        (void) GetWindowBounds (nibWindow, kWindowContentRgn, &nibFrame);
        (void) GetControlBounds (userPane, &paneFrame);
        (void) GetControlBounds (control, &controlFrame);

        dh = ((paneFrame.right - paneFrame.left) -
                (nibFrame.right - nibFrame.left))/2;// 2

        if (dh < 0) dh = 0;

        dv = ((paneFrame.bottom - paneFrame.top) -
                (nibFrame.bottom - nibFrame.top))/2;// 3

        if (dv < 0) dv = 0;

        OffsetRect (// 4
            &controlFrame,
            paneFrame.left + dh,
            paneFrame.top + dv
        );

        (void) SetControlBounds (control, &controlFrame);

        result = SetControlVisibility (control, TRUE, FALSE);// 5

        if (result == noErr)
        {
            result = EmbedControl (control, userPane);// 6

            if (result == noErr)
            {
                *outControl = control;// 7
            }
        }
    }

    return result;
}
```

Here’s what the code in Listing A-1 does:

1. Gets a reference to the desired control. This control already exists in the nib window that contains your custom interface.
2. Finds the delta needed to position the control such that the nib-based interface is horizontally center-aligned inside the dialog pane.Finds the delta needed to position the control such that the nib-based interface is vertically center-aligned inside the dialog pane.
3. Adjusts the coordinates of the top-left corner of the control, so that the control is positioned correctly with respect to the dialog pane.
4. Makes sure the control is visible if the dialog pane is displayed.
5. Embeds the control inside the dialog pane. As a side effect, the printing system now owns the control reference—your printing dialog extension should not release it.
6. Passes the embedded control back to the caller.

To get a ticket reference, you need to implement a function that calls `PMSessionGetData` for the session object associated with the current print job.

Table A-1 lists the four standard ticket identifiers defined for use by printing dialog extensions.

__Table A-1__  Ticket identifiers used by printing dialog extensions

| Identifier (CFStringRef) | Ticket | Comments |
| `kPDE_PMPrintSettingsRef` | Print settings | Used by application and printer module printing dialog extensions. |
| `kPDE_PMPageFormatRef` | Page format | Used by application and printer module printing dialog extensions. |
| `kPDE_PMJobTemplateRef` | Job template | Available only during some printer module printing dialog extension routines. |
| `kPDE_PMPrinterInfoRef` | Printer info | Available only during some printer module printing dialog extension routines. |

Listing A-2 illustrates how to write a function that constructs and passes back a ticket reference.

__Listing A-2__  A utility function that gets a ticket reference

```
extern OSStatus MyGetTicket
(
    PMPrintSession  session,
    CFStringRef     ticketID,
    PMTicketRef*    ticketPtr
)

{
    OSStatus result = noErr;
    CFTypeRef type = NULL;
    PMTicketRef ticket = NULL;

    *ticketPtr = NULL;

    result = PMSessionGetDataFromSession (session, ticketID, &type);// 1

    if (result == noErr)
    {
        if (CFNumberGetValue (// 2
            (CFNumberRef) type, kCFNumberSInt32Type, (void*) &ticket))
        {
            *ticketPtr = ticket;// 3
        }
        else {
            result = kPMInvalidValue;
        }
    }

    return result;
}
```

Here’s what the code in Listing A-2 does:

1. Searches the printing session object for a specialized job ticket. The value passed back is a generic object reference. The printing system provides the session object when it calls the sync function.
2. Gets a numeric value that represents an opaque ticket reference. This function returns `true` if the operation was successful.
3. Passes back the ticket reference to the caller.

This section explains how your printing dialog extension can override the default behavior of the help button in a printing dialog. Of course, you don’t want to override the help button unless your pane is visible.

The tasks are straightforward:

- Add a field for a handler reference to the context described in [Defining a Context](Core%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywugskijbcucr2d).
- In the open function described in [Open](Core%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywueqsdinduoqsi), install a Carbon event handler that handles the command event associated with the help button. Save the handler reference in the context.
- In the close function described in [Close](Core%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywueqsdjjfeqskj), remove the handler to restore the default behavior of the help button.

Listing A-3 shows how to implement a Carbon event handler that detects and handles a help-button click in a printing dialog. The installing function—described in [Installing a Help Event Handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqhewviucykjcummjwgy)—configures this handler for command events only.

__Listing A-3__  An event handler for the help event in a printing dialog

```
static OSStatus MyHandleHelpEvent// 1
(
    EventHandlerCallRef call,
    EventRef event,
    void *userData
)

{
    HICommand commandStruct;// 2
    OSStatus result = eventNotHandledErr;// 3

    GetEventParameter (// 4
        event, kEventParamDirectObject,
        typeHICommand, NULL, sizeof(HICommand),
        NULL, &commandStruct
    );

    if (commandStruct.commandID == 'help') {// 5
        result = MyDisplayHelp();// 6
    }

    return result;
}
```

Here’s what the code in Listing A-3 does:

1. Declares the name and parameters for a Carbon event handler of type `EventHandlerProcPtr`. In this implementation, `event` is the only parameter actually used.
2. Declares a data structure for a command event. See the Carbon Event Manager reference for details.
3. Initializes the return code. The usual default value `noErr` is not appropriate here, because in this context `noErr` means “event handled”.
4. Retrieves the event data. Since this handler is installed at the window level, the event could contain one of several different commands.
5. Checks the command signature to see if the help button was clicked.
6. Calls a custom function you implement to display the help book for your application or printer module.

Listing A-4 shows how to write a function that installs a help event handler, specifying the printing dialog as the event target.

__Listing A-4__  Installing a help event handler

```
#define kMyNumberOfEventTypes   1

extern OSStatus MyInstallHelpEventHandler
(
    WindowRef inWindow,
    EventHandlerRef *outHandler
)

{
    static const EventTypeSpec sEventTypes [kMyNumberOfEventTypes] =// 1
    {
        { kEventClassCommand, kEventCommandProcess }
    };

    OSStatus result = noErr;
    EventHandlerRef handler = NULL;
    EventHandlerUPP handlerUPP = NewEventHandlerUPP (MyHandleHelpEvent);// 2

    result = InstallWindowEventHandler (// 3
        inWindow,
        handlerUPP,
        kMyNumberOfEventTypes,
        sEventTypes,
        NULL,
        &handler
    );

    *outHandler = handler;// 4
    return result;
}
```

Here’s what the code in Listing A-4 does:

1. Defines an array of event type specifiers. This array represents the set of event types you want to handle. In this case, you need to handle only one type.
2. Creates the universal procedure pointer used by the Carbon Event Manager to call your event handler.
3. Installs the handler. On return, `context->handler` contains the `EventHandlerRef` used later to remove the event handler.
4. Stores this handler reference in the context.

Listing A-5 shows how to write a function that removes the help event handler described in [Installing a Help Event Handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqhewviucykjcummjwgy).

__Listing A-5__  Removing a help event handler

```
extern OSStatus MyRemoveHelpEventHandler (
    EventHandlerRef *helpHandlerP,
    EventHandlerUPP *helpHandlerUPP
)

{
    OSStatus result = noErr;

    if (*helpHandlerP != NULL)
    {
        result = RemoveEventHandler (*helpHandlerP);// 1
        *helpHandlerP = NULL;// 2
    }

    if (*helpHandlerUPP != NULL)
    {
        DisposeEventHandlerUPP (*helpHandlerUPP);// 3
        *helpHandlerUPP = NULL;// 4
    }

    return result;
}
```

Here’s what the code in Listing A-4 does:

1. Removes the help event handler.
2. Deletes the reference to the handler in your context.
3. Deallocates the UPP used by the Carbon Event Manager to call your help event handler.
4. Deletes the reference to this UPP in your context.

For more information about the Carbon event model and writing Carbon event handlers, and see _[Carbon Event Manager Programming Guide](../../Carbon/Carbon%20Event%20Manager%20Programming%20Guide/Introduction%20to%20Carbon%20Event%20Manager%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobz)_.

[Next](Printing%20Plug-in%20Header%20Functions.md)[Previous](Integration%20Tasks.md)

