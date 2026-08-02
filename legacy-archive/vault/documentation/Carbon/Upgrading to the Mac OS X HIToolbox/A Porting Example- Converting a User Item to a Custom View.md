---
title: Upgrading to the Mac OS X HIToolbox
apple_id: TP30001140
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2004-06-28'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Upgrading_HIToolbox/upgrading_hitoolbox_samp/upgrading_hitoolbox_samp.html
archived_at: '2026-07-15T05:24:42.296521Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Upgrading to the Mac OS X HIToolbox](Introduction%20to%20Upgrading%20to%20the%20Mac%20OS%20X%20HIToolbox.md)


[Next](Document%20Revision%20History.md)[Previous](Porting%20Steps.md)

# A Porting Example: Converting a User Item to a Custom View

This chapter describes how you might convert a dialog-based user item into a custom HIView.

This example user item/view draws a black box outline, sized to fit inside its bounds. Within the box is a square spot that the user can move or drag around by clicking in the box. The work needed to convert the user item covers many of the steps outined in [Porting Steps](Porting%20Steps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbqfvbuqmrqgmwueqkcjbbusqkd): updating Dialog Manager functions, adopting Carbon events, adopting Quartz, and creating a custom view.

- [The Old Dialog Manager Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbqfvbuqmrqgqwueqkcireuirkf) summarizes the Dialog Manager code used to implement the user item and describes how you might update it to use views.
- [The New Custom View](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbqfvbuqmrqgqwugskbjffeersh) describes a possible implementation for the new custom view, based on the recommendations given in the previous section.

This section reviews the Dialog Manager code used to create the custom item, along with the recommendations for how to update it. This example assumes a worst-case scenario of System 6 or System 7–era code.

[Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbqfvbuqmrqgqwueqkci5degqkc) shows a section of the dialog creation code dealing with the user item.

__Listing 3-1__  Creating the dialog with the user item

```
void ThisOldDialog(void)
    {
    SInt16 itemHit;
    DialogItemType itemType;
    Handle itemHandle;
    Rect itemBox;

    DialogRef theDialog = GetNewDialog(256, NULL, (WindowRef)-1L);// 1
    if (theDialog == NULL) return;
    …
    // Setting the draw proc for the user item
    GetDialogItem(theDialog, 13, &itemType, &itemHandle, &itemBox);// 2
    gUserH = (itemBox.left + itemBox.right) / 2;
    gUserV = (itemBox.top + itemBox.bottom) / 2;
    SetDialogItem(theDialog, 13, itemType, (Handle)&MyOldDrawUserItem,// 3
                     &itemBox);
    …
    DisposeDialog (theDialog);// 4
    }
```

To update this code, you need to make the following changes:

1. Replace the dialog resource (ID 256) with a nib file–based window.
2. Instead of calling `GetDialogItem` to obtain the user item’s bounds, call `HIViewGetBounds` , specifying the HIView reference of the custom view.
3. Instead of using `SetDialogItem` to set a draw handler for the user item, register your view for the `kEventControlDraw` event and do your drawing from the handler you specify for that event.
4. Call `DisposeWindow` to remove the dialog because you have made it a window instead.

The old drawing function simply draws the box and the current position of the spot using QuickDraw calls, as shown in [Listing 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbqfvbuqmrqgqwueqkci5bucq2h).

__Listing 3-2__  The user item drawing function

```
void MyDrawUserItem(DialogRef theDialog, DialogItemIndex itemNo)// 1
    {
    DialogItemType itemType;
    Handle itemHandle;
    Rect itemBox;
    GetDialogItem(theDialog, itemNo, &itemType, &itemHandle, &itemBox);// 2

    CGrafPtr savePort;// 3
    GetPort(&savePort);
    SetPortDialogPort(theDialog);

    PenState penState;// 4
    GetPenState(&penState);

    PenSize(3, 3);
    if (itemType & itemDisable)
        {
        Pattern gray;
        PenPat(GetQDGlobalsGray(&gray));
        }
    FrameRect(&itemBox);
    Rect userRect = {gUserV-4, gUserH-4, gUserV+4, gUserH+4};
    PaintRect(&userRect);

    SetPenState(&penState);
    SetPort(savePort);
    }
```

To update this code, you want to make the following changes:

1. Incorporate the drawing function into a `kEventControlDraw` handler for the custom view.
2. Instead of calling `GetDialogItem` to obtain information about the user item, obtain this information directly from the draw event using the Carbon Event Manager `GetEventParameter` function.
3. Update all QuickDraw calls to use Quartz. Instead of worrying about graphics ports, you can obtain the Quartz drawing context for your custom view from the drawing event using the `GetEventParameter` function.
4. Replace the QuickDraw drawing primitive functions to draw the item’s bounding box and spot with their Quartz equivalents (for example, `CGContextStrokeRect` replaces `FrameRect`)

Mouse clicks are handled within the dialog’s event filter, as shown in [Listing 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbqfvbuqmrqgqwueqkcjbdusq2i).

__Listing 3-3__  Dialog event filter to process user item clicks

```swift
Boolean MySystem6or7DialogFilter(DialogRef theDialog, // 1
                        EventRecord *theEvent, DialogItemIndex *itemHit)
    {
    …
    // we got a click!
    if (theEvent->what == mouseDown)// 2
        {
        DialogItemType itemType;
        Handle itemHandle;
        Rect itemBox;
        GetDialogItem(theDialog, 13, &itemType, &itemHandle, &itemBox);// 3

        CGrafPtr savePort;
        GetPort(&savePort);
        SetPortDialogPort(theDialog);
        Point thePoint = theEvent->where;// 4
        GlobalToLocal(&thePoint);
        Boolean inside = PtInRect(thePoint, &itemBox);// 5

        // is the click inside the user item?
        if (inside)
            {
            // let's constrain and move the spot!
            // it's possible to track the spot here but it's complex
            // so we just move on the click and don't track.
            // that's typical of dialog's user items of that era.
            Rect userRect1 = {gUserV-4, gUserH-4, gUserV+4, gUserH+4};
            EraseRect(&userRect1);// 6
            InvalWindowRect(GetDialogWindow(theDialog), &userRect1);
            gUserH = thePoint.h;
            gUserV = thePoint.v;
            if (gUserH < itemBox.left+4) gUserH = itemBox.left+4;
            if (gUserH > itemBox.right-4) gUserH = itemBox.right-4;
            if (gUserV < itemBox.top+4) gUserV = itemBox.top+4;
            if (gUserV > itemBox.bottom-4) gUserV = itemBox.bottom-4;
            Rect userRect2 = {gUserV-4, gUserH-4, gUserV+4, gUserH+4};
            InvalWindowRect(GetDialogWindow(theDialog), &userRect2);
            }
        SetPort(savePort);
        }

    return false;
    }
```

To update this code, you need to make the following changes:

1. Handle mouse clicks in a Carbon event handler rather than an event filter.
2. Replace the mouse-down event handler with Carbon event handlers for the `kEventControlHitTest` and `kEventControlTrack` events. The hit test event requires you to tell the system what part of the view the user clicked, while the track event is sent if the user moves the mouse while it is down.
3. Call `GetEventParameter` to obtain the view reference, bounds, and the Quartz drawing context from the Carbon event instead of calling `GetDialogItem`.
4. You will have to change the code to translate the mouse coordinates. When converting to use views, the mouse position you receive from the Carbon event is automatically converted to be in the local coordinates of the view.
5. You do not have to compare the mouse position to the bounds. Your view receives a Carbon event only if the mouse click occurs in the view.
6. Call `HIViewSetNeedsDisplay` or `HIViewSetNeedsDisplayInRegion` to mark a view or region as needing to be redrawn. You no longer need to call `EraseRect` or `InvalRect`.

To reproduce the user item in the HIView world, you implement it as a custom view. A custom view is comprised of a class name identifier, a data structure to hold the instance data, and a collection of Carbon event handlers. [Listing 4-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbqfvbuqmrqgqwueqkcinceirsi) shows an example class name and structure

__Listing 3-4__  Defining a custom view class and instance structure

```
#define kCustomSpotViewClassID// 1
                         CFSTR("com.apple.sample.dts.HICustomSpotView")

typedef struct// 2
    {
    HIViewRef   view;
    HIPoint     spot;
    }
CustomSpotViewData;
```

1. Select a unique class name for your view. You pass this name to the `HIObjectRegisterSubclass` function, and you specify it in your nib file for the custom HIView element.
2. Hold the view’s instance data in a `CustomSpotViewData` structure. At the bare minimum, it must contain the HIView reference for your view. In this example, the instance data also includes the coordinates of the spot inside the view.

Before you instantiate a window containing the custom view (whether from a nib file or by calling `HIObjectCreate`), you need to register your subclass by calling the `HIObjectRegisterSubclass` function, as shown in [Listing 4-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbqfvbuqmrqgqwueqkcijceirch).

__Listing 3-5__  Registering a custom view

```
HIObjectClassRef theClass;
EventTypeSpec kFactoryEvents[] =// 1
        {
            { kEventClassHIObject, kEventHIObjectConstruct },
            { kEventClassHIObject, kEventHIObjectInitialize },
            { kEventClassHIObject, kEventHIObjectDestruct },
            { kEventClassControl, kEventControlHitTest },
            { kEventClassControl, kEventControlTrack },
            { kEventClassControl, kEventControlDraw }
        };
HIObjectRegisterSubclass(kCustomSpotViewClassID, kHIViewClassID, // 2
        0, CustomSpotViewHandler, GetEventTypeCount(kFactoryEvents),
        kFactoryEvents, 0, &theClass);
```

1. Pass an `EventTypeSpec` array containing the events that you want your view to handle.

   All custom views must handle the `kEventHIObjectConstruct` and `kEventHIObjectDestruct` events. The `kEventHIObjectInitialize` event lets you perform any needed initializations.

   The control event class contains the events that describe the unique behavior of your view. Just about any custom view requires a `kEventControlDraw` handler to draw your content, and a `kEventControlHitTest` handler to provide feedback to the system about what part of the view the user clicked. This example also includes the `kEventControlTrack` event handler to track the mouse while it is down within the view.
2. Register your view using `HIObjectRegisterSubclass`, specifying the callback function to handle all your view’s events. This handler is just like any other Carbon event handler, except that the instance data structure for your view is passed to you in the user data (`inRefCon`) parameter.

[Listing 4-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbqfvbuqmrqgqwueqkcijcuosch) shows a possible implementation for your custom view’s event handler.

__Listing 3-6__  An event handler for the converted user item

```swift
pascal OSStatus CustomSpotViewHandler(EventHandlerCallRef inCaller,
                                        EventRef inEvent, void* inRefcon)
    {
    OSStatus result = eventNotHandledErr;
    CustomSpotViewData* myData = (CustomSpotViewData*)inRefcon;

    switch (GetEventClass(inEvent))// 1
        {
        case kEventClassHIObject:// 2
            switch (GetEventKind(inEvent))
                {
                case kEventHIObjectConstruct:
                    {
                    myData = (CustomSpotViewData*)
                                calloc(1, sizeof(CustomSpotViewData));
                    GetEventParameter(inEvent,kEventParamHIObjectInstance,
                         typeHIObjectRef, NULL, sizeof(myData->view), NULL,
                         &myData->view);
                    result = SetEventParameter(inEvent, kEventParamHIObjectInstance,
                                     typeVoidPtr, sizeof(myData), &myData);
                    break;
                    }

                case kEventHIObjectInitialize:
                    {
                    HIRect bounds;
                    GetEventParameter(inEvent, kEventParamBounds, typeHIRect, NULL,
                                         sizeof(bounds), NULL, &bounds);
                    myData->spot.x = CGRectGetMidX(bounds) - CGRectGetMinX(bounds);
                    myData->spot.y = CGRectGetMidY(bounds) - CGRectGetMinY(bounds);

                    HIViewSetVisible(myData->view, true);
                    break;
                    }

                case kEventHIObjectDestruct:
                    {
                    free(myData);
                    result = noErr;
                    break;
                    }

                default:
                    break;
                }
            break;

        case kEventClassControl:
            switch (GetEventKind(inEvent))
                {
                case kEventControlDraw:// 3
                    {
                    CGContextRef    context;
                    HIRect          bounds;
                    result = GetEventParameter(inEvent,// 4
                             kEventParamCGContextRef, typeCGContextRef, NULL,
                                                 sizeof(context), NULL, &context);
                    HIViewGetBounds(myData->view, &bounds);// 5

                    CGContextSetRGBStrokeColor(context, 0.0, 0.0, 0.0, 0.7);// 6
                    CGContextSetRGBFillColor(context, 0.0, 0.0, 0.0, 0.7);

                    CGContextSetLineWidth(context, 3.0);// 7
                    CGContextStrokeRect(context, bounds);

                    HIRect spot = { {myData->spot.x - 4.0, myData->spot.y - 4.0},// 8
                                     {8.0, 8.0} };
                    CGContextFillRect(context, spot);

                    result = noErr;
                    break;
                    }

                case kEventControlHitTest:// 9
                    {
                    HIPoint pt;
                    HIRect  bounds;
                    GetEventParameter(inEvent, kEventParamMouseLocation, // 10
                                        typeHIPoint, NULL, sizeof(pt), NULL,&pt);
                    HIViewGetBounds(myData->view, &bounds);
                    ControlPartCode part = (CGRectContainsPoint(bounds, pt))// 11
                                            ?kControlButtonPart:kControlNoPart;
                    result = SetEventParameter(inEvent, kEventParamControlPart,// 12
                                     typeControlPartCode, sizeof(part), &part);
                    break;
                    }

                case kEventControlTrack:// 13
                    {
                    MouseTrackingResult mouseStatus;
                    ControlPartCode partCode;
                    Point theQDPoint;
                    Rect windBounds;

                    HIPoint theHIPoint;
                    HIRect  bounds;

                    HIViewGetBounds(myData->view, &bounds);

                    GetWindowBounds (GetControlOwner(myData->view),// 14
                                         kWindowStructureRgn, &windBounds);

                    GetEventParameter(inEvent, kEventParamMouseLocation,// 15
                        typeHIPoint, NULL, sizeof(theHIPoint), NULL, &theHIPoint);

                    mouseStatus = kMouseTrackingMouseDown;
                    while (mouseStatus != kMouseTrackingMouseUp)
                        {
                        partCode = (CGRectContainsPoint(bounds, theHIPoint))
                                    ?kControlButtonPart:kControlNoPart;

                        if (partCode == kControlButtonPart)// 16
                            {
                            if (theHIPoint.x < bounds.origin.x+4) // 17
                                                theHIPoint.x = bounds.origin.x + 4;
                            if (theHIPoint.x > bounds.origin.x + bounds.size.width-4)
                                theHIPoint.x = bounds.origin.x + bounds.size.width-4;
                            if (theHIPoint.y < bounds.origin.y+4)
                                                theHIPoint.y = bounds.origin.y + 4;
                            if (theHIPoint.y > bounds.origin.y + bounds.size.height-4)
                                theHIPoint.y = bounds.origin.y+bounds.size.height-4;

                            myData->spot = theHIPoint;
                            HIViewSetNeedsDisplay(myData->view, true);// 18
                            }

                        TrackMouseLocation ((GrafPtr)-1, // 19
                                                &theQDPoint, &mouseStatus);

                        theHIPoint.x = theQDPoint.h - windBounds.left;// 20
                        theHIPoint.y = theQDPoint.v - windBounds.top;

                        HIViewConvertPoint(&theHIPoint, NULL, myData->view);// 21

                        }
                    break;
                    }
                default:
                    break;
                }
            break;

        default:
            break;
        }

    return result;
    }
```

Here is how the code works:

1. When the view receives an event, obtain the event class by calling `GetEventClass`.
2. Implement the HIObject class handlers. The HIObject event class is made up of events that concern the creation and destruction of the HIObjects (of which HIView is a subclass). The actions you take here are essentially the same for any custom view:

   - `kEventHIObjectConstruct` requires you to allocate memory for your view’s instance data, and then set a pointer to this data in the construct event by calling `SetEventParameter`. The structure you allocate here is then passed to your event handler when subsequent events occur.
   - `kEventHIObjectInitialize` gives you an opportunity to perform any initialization. Typically, you use this event to process any input parameters passed to your view. If you are using nibs, you can extract any parameters you specified in the Attributes pane of Interface Builder’s Info window.
   - `kEventHIObjectDestruct` requires you to free the memory you allocated for your view.

   For more details about these events, see _[HIView Programming Guide](../HIView%20Programming%20Guide/Introduction%20to%20HIView%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrt)_.
3. Implement a drawing handler. The system sends a `kEventControlDraw` event to your view whenever it needs to be redrawn, either due to an external change or because your application called `HIViewSetNeedsDisplay` for the view. As emphasized before, all your drawing must take place within this handler.
4. For the `kEventControlDraw` event, obtain the Quartz drawing context for the view by calling `GetEventParameter` with the `kEventParamCGContextRef` parameter tag. This context is automatically clipped to only the portion that needs to be drawn.
5. Obtain the bounds of the view by calling `HIViewGetBounds`. Note that these bounds are in a structure of type `HIRect`, not type `Rect`.
6. Set the Quartz stroke and fill color. These calls are analogous to setting the pen and fill pattern in QuickDraw.
7. Set the stroke width and draw the box outline. `CGContextStrokeRect` is the Quartz equivalent of the QuickDraw `FrameRect` function.
8. Draw the 8-by-8 spot centered at the position stored in the view’s instance data. The `CGContextFillRect` function is analogous to the QuickDraw `PaintRect` function.
9. Implement a hit test handler. The system sends a `kEventControlHitTest` event to your view whenever the user clicks in it. Your handler must determine what part of the view was clicked and report that to the system. Complex controls with multiple parts (such as a scroll bar, which has a track area, a thumb, and increment/decrement buttons) may require different responses depending on which part was hit.
10. Obtain the mouse position from the `kEventControlHitTest` event using `GetEventParameter`.
11. Determine if the mouse down happened within the view using the Quartz function `CGRectContainsPoint` function. If so, set the part code to `kControlButtonPart`; otherwise set the part to `kControlNoPart`. This example is somewhat trivial, in that the mouse down obviously occurred within the view bounds (the view would not receive the event otherwise), but if you have multiple parts within your view, you may need to perform several such tests to determine just what the user clicked.
12. Pass the part code back in the event by calling `SetEventParameter` .

    Later when the user performs additional mouse actions (mouse up, dragging, and so on), subsequent Carbon events sent to the view will have the part code parameter set to what you returned in the `kEventControlHitTest` handler.
13. Implement a mouse tracking handler. The system sends a `kEventControlTrack` event to your application when the user begins moving the mouse while holding the mouse button down. Your tracking handler must update the view depending on where the mouse goes.
14. Obtain the bounds of the window. Currently, the suggested mouse tracking function `TrackMouseLocation` returns the position of the mouse as a QuickDraw point. This means that you need to perform some calculations to convert the global QuickDraw point returned by `TrackMouseLocation` into the local coordinates of your custom view. Obtaining the bounds of the window containing the view enables you to translate the bounds later.
15. Obtain the current mouse location by calling `GetEventParameter`. If the mouse down occurred within the view, the first thing to do is to redraw the spot at that location.
16. If the part code indicates that the mouse action occurred within the view bounds, then change the spot position to be the current position of the mouse.
17. Constrain the spot to the drawn borders of the view. Use a series of conditionals to ensure that it can never be closer than 4 pixels from the actual view bounds.
18. Mark the view as needing to be redrawn by calling `HIViewSetNeedsDisplay`. On the next drawing pass, the draw handler draws the spot in the new location (that is, under the mouse).
19. Track the mouse by calling `TrackMouseLocation`. This function completes only when the user performs a mouse action (mouse up, drag, and so on), returning the action taken by the user and the current mouse position. Passing `-1` for the graphics port specifies that the mouse location should be returned in global coordinates. By keeping the `TrackMouseLocation` call within a loop, the mouse is continually tracked until the user releases the mouse button.
20. From the global coordinates of the mouse position, subtract off the top left position of the window. Doing so effectively translates the mouse position to be relative to the window’s structure region (or root view).
21. Call `HIViewConvertPoint` to translate the point from the local coordinates of the root view to the local coordinates of your custom view.

Unlike the original custom user item, the custom view is not tied to a particular dialog; you need to define it only once and then you can use it in any window in your application. To add your view to a nib window, simply drag the HIView element into the window and specify its class ID and input parameters (if any) from the Info window. The view is instantiated automatically when you create the window from the nib file.

[Next](Document%20Revision%20History.md)[Previous](Porting%20Steps.md)

