---
title: HIToolbar Programming Guide
apple_id: TP40000958
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/UsingHIToolbar/HIToolbar_tasks/HIToolbar_tasks.html
archived_at: '2026-07-15T05:24:48.394129Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HIToolbar Programming Guide](HIToolbar%20Concepts.md)


[Next](Document%20Revision%20History.md)[Previous](HIToolbar%20Concepts.md)

# Toolbar Tasks

This chapter describes how to create and manipulate toolbars.

Before creating a toolbar, you should understand what goes on during the life of the HIToolbar object.

1. When the HIToolbar object is first created, it takes no additional actions until it actually becomes time to show a toolbar. For example, you can associate multiple windows with the toolbar, but it will not create any views until a toolbar must be displayed in a visible window.
2. When it is time to show a toolbar, the HIToolbar object creates a toolbar view and embeds it in the root view of the window that contains it.
3. The HIToolbar object then checks to see if any previously saved configuration information exists for this toolbar. If not, the HIToolbar object queries its delegate (through Carbon events) for the default configuration information.
4. For each item in the default configuration list, it sends a request to the delegate to create that toolbar item. The delegate should return a toolbar item reference for each item it creates. If the delegate returns `EventNotHandledErr`, the event passes to HIToolbar’s default handlers, which will create any standard toolbar items.
5. For each toolbar item reference it receives, the HIToolbar object then creates a toolbar item view and embeds it in the toolbar view. If the toolbar item creates a custom HIView, this view is embedded in the toolbar item view.
6. HIToolbar repeats steps 2, 4, and 5 for each toolbar that appears in a visible window.
7. If the user changes the toolbar configuration in one window, the HIToolbar object is notified (using Carbon events) and it can then update the views in all the other windows associated with it.
8. If the user requests the Configuration sheet, the HIToolbar object queries its delegate for a list of allowable toolbar items. Using that list and the list of default items, it then requests toolbar items from the delegate to populate the Configuration sheet before displaying it.

To create the toolbar, you simply call the `HIToolbarCreate` function. This creates an HIToolbar object, which controls the creation and display of the toolbar in associated windows. Listing 2-1 shows how you might create a toolbar and attach it to a window.

__Listing 2-1__  Creating a toolbar

```
OSStatus        err = noErr;
HIToolbarRef    toolbar;// 1

err = HIToolbarCreate( CFSTR( "com.mycompany.carbontoolbar" ),// 2
                    kHIToolbarAutoSavesConfig | kHIToolbarIsConfigurable,
                    &toolbar );


InstallEventHandler( HIObjectGetEventTarget( (HIToolbarRef)toolbar ),// 3
                    ToolbarDelegate, GetEventTypeCount( kToolbarEvents ),
                    kToolbarEvents, toolbar, NULL );

SetWindowToolbar( window, toolbar );// 4
ShowHideWindowToolbar( window, true, false );// 5

CFRelease( toolbar );// 6

ChangeWindowAttributes( window, kWindowToolbarButtonAttribute, 0 );// 7

SetAutomaticControlDragTrackingEnabledForWindow( window, true );// 8
```

Here is how the code works:

1. The toolbar is defined by a toolbar reference, which is also an HIObject reference.
2. To create a toolbar, call the `HIToolbarCreate` function. You must pass a unique identifier (as a Core Foundation string) for each toolbar your application creates. Doing so allows you to define multiple toolbars. The identifier should be in the form: com._myCompany_._myApp_._myUniqueName_.

   You can specify attributes for your toolbar when you create it. `kHIToolbarAutoSavesConfig` indicates that the toolbar will save its current configuration to the application’s user preferences file. The `kHIToolbarIsConfigurable` attribute indicates that the user can configure the toolbar (that is, the user can bring up the configuration sheet). If you do not want to specify any attributes, pass `kHIToolbarNoAttributes`.
3. You install the toolbar event handler on your delegate just as you would for any other event target. The delegate does all the event handling related to creating and managing toolbar items. When you first create the toolbar, the toolbar is its own delegate.

   To set a different delegate for the toolbar, call the `HIToolbarSetDelegate` function. Note that events are sent to the delegate with the `kEventTargetDontPropagate` option, so they cannot propagate up the event hierarchy.
4. To assign a toolbar to a window, call the `SetWindowToolbar` function. Note that you can assign the toolbar to multiple windows. Any window that contains the toolbar should use the standard window event handler.
5. The `ShowHideWindowToolbar` function shows or hides the toolbar (just as if the user pressed the toolbar button). The toolbar is initially hidden, so call this function to make it visible in the window.
6. Now that the toolbar is retained by a window, you can release your reference to it by calling `CFRelease`.
7. To add the oblong button to show and hide the toolbar, you must set the window attribute `kWindowToolbarButtonAttribute`. You can set this attribute within a nib file or when you programmatically create the window.
8. The toolbar requires automatic drag tracking, so you must set this by calling `SetAutomaticControlDragTrackingEnabledForWindow` on windows containing toolbars.

After creating your toolbar, you need to assign an event handler to create and manage its toolbar items. These events are automatically sent to either the toolbar event target (the default) or an event target you specify by calling the `HIToolbarSetDelegate` function. In most cases, the toolbar itself is the appropriate delegate.

Listing 2-2 shows an example of a toolbar event handler.

__Listing 2-2__  A toolbar event handler

```
static const EventTypeSpec kToolbarEvents[] =// 1
{
    { kEventClassToolbar, kEventToolbarGetDefaultIdentifiers },
    { kEventClassToolbar, kEventToolbarGetAllowedIdentifiers },
    { kEventClassToolbar, kEventToolbarCreateItemWithIdentifier },
    { kEventClassToolbar, kEventToolbarCreateItemFromDrag }
};

static OSStatus ToolbarDelegate( EventHandlerCallRef inCallRef,
                                EventRef inEvent, void* inUserData )
{
    OSStatus            result = eventNotHandledErr;
    CFMutableArrayRef   array;
    CFStringRef         identifier;

    switch ( GetEventKind( inEvent ) )
    {
        case kEventToolbarGetDefaultIdentifiers:// 2
            GetEventParameter( inEvent, kEventParamMutableArray,
                            typeCFMutableArrayRef, NULL,
                            sizeof( CFMutableArrayRef ), NULL, &array );
            GetToolbarDefaultItems( array ); // application-defined
            result = noErr;
            break;

        case kEventToolbarGetAllowedIdentifiers:// 3
            GetEventParameter( inEvent, kEventParamMutableArray,
                            typeCFMutableArrayRef, NULL,
                            sizeof( CFMutableArrayRef ), NULL, &array );
            GetToolbarAllowedItems( array ); // application-defined
            result = noErr;
            break;

        case kEventToolbarCreateItemWithIdentifier:// 4
            {
                HIToolbarItemRef        item;
                CFTypeRef               data = NULL;

                GetEventParameter( inEvent,
                        kEventParamToolbarItemIdentifier, typeCFStringRef,
                        NULL, sizeof( CFStringRef ), NULL, &identifier );

                GetEventParameter( inEvent,
                        kEventParamToolbarItemConfigData, typeCFTypeRef,
                        NULL, sizeof( CFTypeRef ), NULL, &data );

                item = CreateToolbarItemForIdentifier( identifier, data );

                if ( item )// 5
                {
                    SetEventParameter( inEvent, kEventParamToolbarItem,
                            typeHIToolbarItemRef,
                            sizeof(HIToolbarItemRef ), &item );
                    result = noErr;
                }
            }
            break;

        case kEventToolbarCreateItemFromDrag:// 6
            {
                HIToolbarItemRef        item;
                DragRef                 drag;

                GetEventParameter( inEvent, kEventParamDragRef, typeDragRef,
                        NULL, sizeof( DragRef ), NULL, &drag );

                item = CreateToolbarItemFromDrag( drag );

                if ( item )
                {
                    SetEventParameter( inEvent, kEventParamToolbarItem,
                            typeHIToolbarItemRef,
                            sizeof( HIToolbarItemRef ), &item );
                    result = noErr;
                }
            }
            break;
    }

    return result;
}
```

Here is how the code works:

1. This example handler covers the four possible toolbar events:

   - A query for the default toolbar items. Default items are those contained in the toolbar when it first appears.
   - A query for allowable toolbar items. Allowable items are those that the user can place into the toolbar when in configuration mode. Note that if your toolbar is not configurable, you do not need to handle this event.
   - A query to create a specific toolbar item. Each toolbar item has an unique identifier, which is passed in this event when the system wants to create it.
   - A query to create a toolbar item based on a drag-and-drop action. For example, the Finder allows you to drag folders into the toolbar. If you want to add similar functionality to create folders, URLs, and so on from drags into your toolbar, you must handle this event.
2. When you receive the `kEventToolbarGetDefaultIdentifiers` event, you receive a pointer to a Core Foundation mutable array (obtained using the `kEventParamMutableArray` parameter). You must populate this array with the default toolbar item identifiers. The function to do so might look like this:

```
static void GetToolbarDefaultItems( CFMutableArrayRef array )
{
    CFArrayAppendValue( array, CFSTR( "com.apple.carbontoolbar.anchored" ) );
    CFArrayAppendValue( array, kHIToolbarSeparatorIdentifier );
    CFArrayAppendValue( array, CFSTR( "com.apple.carbontoolbar.permanent" ) );
    CFArrayAppendValue( array, kHIToolbarFlexibleSpaceIdentifier );
    CFArrayAppendValue( array, CFSTR( "MyCustomIdentifier" ) );
    CFArrayAppendValue( array, CFSTR( "com.apple.carbontoolbar.trash" ) );
}
```

   The items appear in the toolbar in the order they are added to the array. In this default arrangement, the “anchored” item will appear on the far left, followed by the separator, and so on.
3. Similarly, when you receive the `kEventToolbarGetAllowableIdentifiers` event, you must populate a Core Foundation mutable array with the identifiers for the allowable toolbar items. These items appear in the configuration sheet in the order they are placed into the array. Note that you do not have to specify toolbar items that are created only from drag-and-drop actions.
4. When you receive a `kEventToolbarCreateItemWithIdentifier` event, you must create a toolbar item based on the identifier that was passed with the event. For example, after sending the `kEventToolbarGetDefaultIdentifiers` event, when the time comes to display the toolbar, the system sends a `kEventToolbarCreateItemWithIdentifer` event for each default item.

   The handler calls `GetEventParameter` to obtain the identifier (`kEventParamToolbarItemIdentifier`) and any associated configuration data that may be associated with it (`kEventParamToolbarItemConfigData`). For example, the configuration data could hold initial values for your item, a URL, text, and so on.

   You use the identifier to determine what kind of toolbar item to create. See [Creating Items from an Identifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgmjqfvbecssijjeuora) for information about how you could implement the `CreateToolbarItemForIdentifier` function.
5. If your item creation function successfully created a toolbar item, call `SetEventParameter` to pass its reference back in the `kEventParamToolbarItem` parameter. Note that you are sent the `kEventToolbarCreateItemWithIdentifier` event even if the HIToolbar object wants to create a system-defined toolbar item. Therefore, whenever you don’t create a toolbar item, you should return `eventNotHandledErr` so the next handler in the calling chain has a chance to take the event.
6. When you receive a `kEventToolbarCreateItemFromDrag` event, you should create a toolbar item based on the user’s drag-and-drop action.

   First, use `GetEventParameter` to obtain the drag reference (`kEventParamDragRef`) from the event. This example then passes the drag reference to its own toolbar item creation function. See [Creating Items from a Drag](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgmjqfvbecsseinfeqqi) for information about how the `CreateToolbarItemFromDrag` function is implemented.

   As with the `kEventToolbarItemCreateItemWithIdentifier` function, you pass the reference of the created toolbar item back into the event using `SetEventParameter`.

In most cases, you create a toolbar item based on a unique identifier. The identifier is just that; a unique string that identifies a particular toolbar item. Identifiers you create are used only within your application, but they must be unique so that the system does not confuse them with identifiers from other applications.

The HIToolbar API defines several standard identifiers that you can use in your application. Aside from returning the proper identifiers for the default and allowable item requests, you do not need to do anything else to implement these items.

__Table 2-1__  System-defined toolbar item identifiers

| Identifier | Description |
| `kHIToolbarSeparatorIdentifier` | A thin vertical line used to group toolbar items. |
| `kHIToolbarSpaceIdentifier` | A fixed-width space. |
| `kHIToolbarFlexibleSpaceIdentifier` | A variable-width space. |
| `kHIToolbarCustomizeIdentifier` | Clicking on this item brings up the toolbar configuration sheet. |
| `kHIToolbarPrintItemIdentifier` | Clicking on this item sends a Print command event (just as if the user had selected the Print menu item) to the toolbar item view. You should install a command event handler at the window level to take this event. |
| `kHIToolbarFontsItemIdentifier` | Clicking on this item brings up the standard Fonts floating window. See the Apple Type Services (ATS) for Fonts documentation for details about how to set and obtain information from the Fonts window. |

You can set attributes in your toolbar items that influence their behavior. Table 2-2 lists the available attributes.

__Table 2-2__  Toolbar item attributes

| Attribute | Description |
| `kHIToolbarItemNoAttributes` | No attributes. |
| `kHIToolbarItemAllowDuplicates` | More than one item of this type can appear in the toolbar. |
| `kHIToolbarItemCantBeRemoved` | The user cannot drag this item out of the toolbar. |
| `kHIToolbarItemAnchoredLeft` | The item is fixed to the left side of the toolbar and cannot be moved. You can have multiple items with this attribute in a toolbar. |
| `kHIToolbarItemIsSeparator` | The item is used is a separator, and should appear as such in the overflow menu. Note that being a separator also implies that the item can draw the full height of the toolbar (unlike normal items, which typically have a label area below the graphic). |
| `kHIToolbarItemSendCmdToUserFocus` | Any command events sent in response to clicks in this item are sent to the current user focus rather than the item’s view. |

This section describes how to create your toolbar items from identifiers passed to your application in the `kEventToolbarCreateItemWithIdentifier` event.

The toolbar sends this event to your application for every identifier, even those not defined by your application. Therefore, you should make sure that your delegate event handler returns `eventNotHandledErr` if you don’t create a toolbar item.

Listing 2-3 shows a function used to create toolbar items.

__Listing 2-3__  Creating toolbar items from identifiers

```
static HIToolbarItemRef CreateToolbarItemForIdentifier( // 1
                            CFStringRef identifier, CFTypeRef configData )
{
    HIToolbarItemRef        item = NULL;

    if ( CFStringCompare( CFSTR( "com.apple.carbontoolbar.permanent" ),// 2
                identifier, kCFCompareBackwards ) == kCFCompareEqualTo )
    {

        if ( HIToolbarItemCreate( identifier, kHIToolbarItemCantBeRemoved,
                            &item ) == noErr )// 3
        {
            IconRef     icon;
            MenuRef     menu;

            GetIconRef( kOnSystemDisk, kSystemIconsCreator, kFinderIcon,// 4
                         &icon );
            HIToolbarItemSetLabel( item, CFSTR( "Can't Remove Me" ) );// 5
            HIToolbarItemSetIconRef( item, icon );// 6
            HIToolbarItemSetCommandID( item, 'shrt' );// 7
            ReleaseIconRef( icon );// 8

            menu = NewMenu( 0, "\p" );// 9
            AppendMenuItemTextWithCFString( menu, CFSTR( "Item 1" ), 0, 0,
                                 NULL );
            AppendMenuItemTextWithCFString( menu, CFSTR( "Item 2" ), 0, 0,
                                 NULL );
            AppendMenuItemTextWithCFString( menu, CFSTR( "Item 3" ), 0, 0,
                                 NULL );
            HIToolbarItemSetMenu( item, menu );// 10
            ReleaseMenu( menu );
        }
    }

    if ( CFStringCompare( CFSTR( "MyCustomIdentifier" ),// 11
                identifier, kCFCompareBackwards ) == kCFCompareEqualTo )
    {
        item = CreateMyButtonToolbarItem( CFSTR( "MyCustomIdentifier" ));
    }

    return item;
}
```

Here is how the code works:

1. This function, `CreateToolbarItemForIdentifier`, takes the two parameters passed to you in the `kEventToolbarCreateItemWithIdentifier` event.
2. Use the Core Foundation string compare function to determine which identifier is which. You specify the `kCFCompareBackwards` option to minimize the compare time.
3. If the identifier indicates the permanent toolbar item, create an unremovable toolbar item by calling the `HIToolbarItemCreate` function with the `kHIToolbarItemCantBeRemoved` attribute set. While a permanent toolbar item can be moved within the toolbar, the user cannot remove it.
4. You usually want to assign an icon to the toolbar item. In this case, you call the Icon Services function `GetIconRef` to obtain a system-defined icon (in this case, the Finder icon).
5. Call the `HIToolbarItemSetLabel` function to set the text that appears in the toolbar for this item.
6. Call the `HIToolbarItemSetIconRef` function to assign the icon reference you obtained for the toolbar item.
7. Call the `HIToolbarItemSetCommandID` function to assign a command ID to the toolbar item. Clicks on the item or its label will then generate a `kEventCommandProcess` event containing that command ID. This event is sent to the item’s view unless you specified the `kHIToolbarItemSendCmdToUserFocus` attribute for your toolbar item.

   Note that if you do not assign a command ID to a toolbar item, the item is inherently not clickable, which may be preferable for certain custom items. For example, if the toolbar item displays a pop-up menu or similar control that has multiple states, you probably don’t want the item’s label to be clickable (except perhaps in text-only mode). Similarly, if a toolbar item contains an search field HIView, you want to take action based on what’s typed into the view, not on clicks in the view or the item label.

   Also, if you do not set a command ID for your toolbar item, that item will not be enabled when it appears in the overflow menu.
8. After you assign the icon reference to the toolbar item, you can release your reference to it.
9. If desired, you can add a pop-up menu to your toolbar item. This menu is used only for multi-state toolbar items when the toolbar is in text-only display mode. For example, the Finder’s View toolbar item is a three-state button in icon view, corresponding to the three possible viewing modes (icon, list and column). In text-only mode, there is no button for the user to click, so the possible selections are made available using the pop-up menu.

   This example uses the Menu Manager function `NewMenu` to create a new empty menu, then calls the `AppendMenuItemTextWithCFString` to add menu items. You can then assign event handlers or command IDs to the menu to initiate actions when selected.
10. To assign the newly-created menu to the toolbar item, call the `HIToolbarItemSetMenu` function.
11. If the identifier indicates a custom ID, then create a custom toolbar item. For example, such a toolbar item could contain an HIView or other control, or it may be be created on the fly, from a drag-and-drop action. See [Creating Items from a Drag](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgmjqfvbecsseinfeqqi) and [Embedding Views in a Toolbar Item](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgmjqfvbecssfivceura) for more information.

In some cases, you may want to create a special toolbar item that has nonstandard behavior. For example, you may want a toolbar item that is a slider, or a text input field, or you may want to create items from a drag-and-drop operation.

You create your custom toolbar item class by subclassing the toolbar item HIObject class and calling `HIObjectCreate` on that subclass. You need to register your subclass and provide handlers for construct, destruct, and initialize events, as well as some specific toolbar item–related events.

The sections that follow describe how to implement commonly-used custom toolbox items.

See _Inside Mac OS X: Introducing HIView_ for more information about subclassing HIObjects and creating instances of those classes.

You can associate an HIView with a toolbar item. For example, you can place buttons, sliders, editable text fields, and other controls in the toolbar item. To do so, you must create a custom HIObject, specifically a subclass of the toolbar item class.

Note that, although the toolbar item is an HIObject, your view is not embedded within that object. For each window the toolbar is associated with, the toolbar item object creates a toolbar item view and then embeds your view within that.

Also, you do not have to supply your own item labels and help tags when creating your custom toolbar item; you can assign these as before using the `HIToolbarItemSetLabel` and `HIToolbarItemSetHelpText` functions.

To register your toolbar item subclass, you call the `HIObjectRegisterSubclass` function. The function in Listing 2-4 shows how you could do this.

__Listing 2-4__  Registering a toolbar item subclass

```
#define kMyButtonToolbarItemClassID CFSTR("com.moof.buttontoolbaritem")

void RegisterMyButtonToolbarItemClass()
{
    static bool sRegistered;

    if ( !sRegistered )
    {
        HIObjectRegisterSubclass( kMyButtonToolbarItemClassID,
                kHIToolbarItemClassID, 0, MyButtonToolbarItemHandler,
                GetEventTypeCount( buttonEvents ), buttonEvents, 0, NULL );

        sRegistered = true;
    }
}
```

This example registers a new toolbar item subclass (`kMyButtonToolbarItemClassID`) and its associated event handler `MyButtonToolbarItemHandler`. This toolbar item simply contains a standard push button.

For efficiency, this example also sets a static Boolean to avoid registering the custom item multiple times (although there is no penalty for doing so).

The `MyButtonToolbarItemHandler` must handle the HIObject construct, initialize, and destruct events. In addition, because you want to embed a view into the toolbar item view, you must also handle the `kEventToolbarItemCreateCustomView` event.

Listing 2-5 shows how you might implement the event handler for your custom button toolbar item.

__Listing 2-5__  Event handler for a toolbar item with an embedded view

```swift
const EventTypeSpec buttonEvents[] =
{
    { kEventClassHIObject, kEventHIObjectConstruct },
    { kEventClassHIObject, kEventHIObjectInitialize },
    { kEventClassHIObject, kEventHIObjectDestruct },

    { kEventClassToolbarItem, kEventToolbarItemCreateCustomView }
};
const EventTypeSpec pushButtonEvents[] =
{
    { kEventClassControl, kEventControlGetSizeConstraints}
};
struct MyButtonToolbarItem// 1
{
    HIToolbarItemRef        toolbarItem;
};
typedef struct MyButtonToolbarItem MyButtonToolbarItem;

static OSStatus MyButtonToolbarItemHandler( EventHandlerCallRef inCallRef,
                             EventRef inEvent, void* inUserData )
{
    OSStatus            result = eventNotHandledErr;
    MyButtonToolbarItem*    object = (MyButtonToolbarItem*)inUserData;// 2

    switch ( GetEventClass( inEvent ) )
    {
        case kEventClassHIObject:
            switch ( GetEventKind( inEvent ) )
            {
                case kEventHIObjectConstruct:// 3
                    {
                        HIObjectRef         toolbarItem;
                        MyButtonToolbarItem*    item;

                        GetEventParameter( inEvent,
                             kEventParamHIObjectInstance, typeHIObjectRef,
                             NULL, sizeof( HIObjectRef ), NULL,
                             &toolbarItem );

                        result = ConstructMyButtonToolbarItem(toolbarItem,
                             &item );

                        if ( result == noErr )
                            SetEventParameter( inEvent,
                                kEventParamHIObjectInstance, typeVoidPtr,
                                sizeof( void * ), &item );
                    }
                    break;

                case kEventHIObjectInitialize:// 4
                    if (CallNextEventHandler(inCallRef, inEvent) == noErr )
                        {
                            HIToolbarItemSetLabel( object->toolbarItem,
                                                 CFSTR( "Press Me" ) );
                            HIToolbarItemSetHelpText( object->toolbarItem,
                                                 CFSTR("Moof!"), NULL );
                            result = noErr;
                        }
                    break;

                case kEventHIObjectDestruct:// 5
                    free (object);
                    result = noErr;
                    break;
            }
            break;

        case kEventClassToolbarItem:
            switch ( GetEventKind( inEvent ) )
            {
                case kEventToolbarItemCreateCustomView:// 6
                    {
                        EventTargetRef myButtonEventTarget;
                        HIViewRef myButton;
                        Rect myButtonRect = {0,0,20,80};

                        CreatePushButtonControl(NULL, &myButtonRect,// 7
                             CFSTR("Push!"), &myButton);

                        SetEventParameter (inEvent, kEventParamControlRef,
                             typeControlRef, sizeof(myButton), &myButton);

                        myButtonEventTarget =
                                        GetControlEventTarget(myButton);

                        InstallEventHandler (myButtonEventTarget,// 8
                                MyButtonEventHandler,
                                GetEventTypeCount(pushButtonEvents),
                                pushButtonEvents, NULL, NULL);
                        result = noErr;
                    }
                    break;
            }
            break;
    }

    return result;
}
```

Here is what the code does:

1. Your subclass must have a structure associated with it that can hold any necessary instance data. This example requires only only one data item: the toolbar item reference. Note that even though this toolbar item provides an HIView, you do not store the HIView reference in this structure.
2. If your application defines any user data for this toolbar item, you can store it in the instance data.
3. When you receive the `kEventHIObjectConstruct` event, you receive a pointer to store the reference to your toolbar item in the `kEventParamHIObjectInstance` parameter. You must allocate memory for the item reference and any associated instance data. Here is a possible implementation for the `ConstructMyToolbarButtonItem` function:

```swift
static OSStatus ConstructMyButtonToolbarItem( HIToolbarItemRef inItem,
                                MyButtonToolbarItem** outItem )
{
    MyButtonToolbarItem*        item;
    OSStatus                err = noErr;

    item = (MyButtonToolbarItem*)malloc( sizeof( MyButtonToolbarItem ) );
    require_action( item != NULL, CantAllocItem, err = memFullErr );

    item->toolbarItem = inItem;

    *outItem = item;

    CantAllocItem:
    return err;
}
```

   After allocating the memory, use `SetEventParameter` to return a pointer to the space created for the toolbar item reference.
4. When you receive the `kEventHIObjectInitialize` event, you must perform any initialization that your toolbar item requires, such as setting initial values for some instance data. This example calls the `HIToolbarSetItemLabel` function to set the text portion of the toolbar item, and `HIToolbarItemSetHelpText` function to set the help tag text.
5. When you receive the `kEventHIObjectDestruct` event, you must release the memory that was allocated for your toolbar item. This example simply calls the Memory Manager function `free` to release the instance data. Note that you must not dispose your HIView reference here.
6. When you receive the `kEventToolbarItemCreateCustomView`, you must create an HIView to embed in the toolbar item view. Any sort of view is valid; you can embed a picture view, a text field, a button, or even your own custom HIView.
7. This example simply creates a standard push button control and then uses `SetEventParameter` to store its HIView reference in the `kEventParamControlRef` parameter of the event. Note that when creating standard views, you must pass `NULL` for the owning window parameter, as the view is not associated with any window.
8. All views that are associated with toolbar items must respond to the `kEventControlGetSizeConstraints` event, which asks for the maximum and minimum allowable sizes for the view. The system uses this information to determine how to best size the toolbar item view given its embedded content. In most cases you should simply return the bounds of the view, as in the following code:

```
static OSStatus MyButtonEventHandler( EventHandlerCallRef inCallRef,
                         EventRef inEvent, void* inUserData )
{

switch ( GetEventKind( inEvent ) )
            {
                case kEventControlGetSizeConstraints:
                    {
                        HISize minBounds = {80,20};
                        HISize maxBounds = {80,20};

                        SetEventParameter (inEvent,
                                 kEventParamMinimumSize, typeHISize,
                                 sizeof(HISize), &minBounds);
                        SetEventParameter (inEvent,
                                 kEventParamMaximumSize, typeHISize,
                                 sizeof(HISize), &maxBounds);

                        return noErr;
                    }
                    break;

                default:
                    break;
 }
return eventNotHandledErr;
}
```

   Note that the `HISize` type is position-independent, indicating only the width and height of the object.

   Finally, you need to call `HIObjectCreate` to create an instance of your custom toolbar item. Listing 2-6 shows a function you could use to do this.

   __Listing 2-6__  Creating a custom toolbar item instance.

```
HIToolbarItemRef CreateMyButtonToolbarItem( CFStringRef inIdentifier)
{
    OSStatus            err;
    EventRef            event;
    UInt32              options = kHIToolbarItemAllowDuplicates;
    HIToolbarItemRef    result = NULL;

    RegisterMyButtonToolbarItemClass();// 1

    err = CreateEvent( NULL, kEventClassHIObject,// 2
                 kEventHIObjectInitialize, GetCurrentEventTime(), 0,
                 &event );
    require_noerr( err, CantCreateEvent );

    SetEventParameter( event, kEventParamToolbarItemIdentifier,// 3
             typeCFStringRef, sizeof( CFStringRef ), &inIdentifier );
    SetEventParameter( event, kEventParamAttributes, typeUInt32, // 4
            sizeof( UInt32 ), &options );

    err = HIObjectCreate( kMyButtonToolbarItemClassID, event,// 5
                         (HIObjectRef*)&result );
    check_noerr( err );

    ReleaseEvent( event );// 6

CantCreateEvent:
    return result;
}
```

Here is how the code works:

1. First, register your custom toolbar item by calling the `RegisterMyButtonToolbarItemClass` function in [Listing 2-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgmjqfvbecsscjfeugry).
2. Create an initialization event to send to your item once it is created. Note that this event is sent directly to the toolbar item (that is, it is not placed in the event queue).
3. Set the toolbar item’s identifier in the initialization event using the `kEventParamToolbarIdentifier` parameter.
4. Set any desired toolbar attributes in the initialization event using the `kEventParamAttributes` parameter.

   Note that the identifier and the toolbar attributes are the same parameters you would pass into the standard `HIToolbarItemCreate` function. If you do not set these parameters, the `HIObjectCreate` call fails.
5. Call `HIObjectCreate` to create an instance of your custom toolbar item class (`kMyButtonToolbarClassID`). On return, you receive a `ToolbarItemRef` (which is also an `HIObjectRef`) that points to the newly-created toolbar item.
6. After sending the initialization event to your toolbar item, you no longer need to retain it, so call `ReleaseEvent`.

If the user drags something onto the toolbar, and your toolbar accepts drags, your application will have to create a toolbar item from the drag.

Listing 2-7 shows how you could process the drag to create a toolbar item. This example creates URLs from one or more text drag items.

__Listing 2-7__  Creating a toolbar item from a drag

```
static HIToolbarItemRef CreateToolbarItemFromDrag( DragRef drag )
{
    UInt16              i, itemCount;
    HIToolbarItemRef    result = NULL;

    CountDragItems( drag, &itemCount );// 1

    for ( i = 1; i <= itemCount; i++ )
    {
        DragItemRef         itemRef;
        FlavorFlags         flags;

        GetDragItemReferenceNumber( drag, i, &itemRef );// 2

        if ( GetFlavorFlags( drag, itemRef, 'TEXT', &flags ) == noErr )// 3
        {
            Size        dataSize;
            char        string[256];
            CFURLRef    url;

            dataSize = sizeof( string );
            GetFlavorData( drag, itemRef, 'TEXT', &string, &dataSize, 0 );// 4

            url = CFURLCreateWithBytes( NULL, string, dataSize,// 5
                             kCFStringEncodingMacRoman, NULL );

            result = CreateMyURLToolbarItem( CFSTR( "MyURLIdentifier" ), url );// 6

            CFRelease( url );// 7

            break;
        }
    }

    return result;
}
```

Here is how the code works:

1. This example uses a number of Drag Manager calls to process the drag item. First, you call the `CountDragItems` function on the drag reference to determine how many items are in the drag. (For example, the user might have selected and dragged several items into the toolbar.)
2. Now iterate over the number of drag items. For each item index number, obtain the item reference by calling `GetDragItemReferenceNumber`.
3. Use the Drag Manager function `GetFlavorFlags` to determine if the drag item content is of type `TEXT`. If so, the item contents can be turned into a URL toolbar item. If not, the drag item is rejected and the contents ignored.
4. If the drag flavor is compatible, call the Drag Manager function `GetFlavorData` to obtain the actual text associated with the drag item.
5. The Core Foundation function `CFURLCreateWithBytes` converts the string into a CFURL with the specified encoding (in this case, MacRoman).
6. Now pass the CFURL to a toolbar item creation function. This function, which is analogous to the `CreateMyButtonToolbarItem` function in [Listing 2-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgmjqfvbecssfivdeiri), should register the toolbar item subclass, create a `kEventHIObjectInitialize` event, and call `HIObjectCreate`.

   You should set several parameters in the initialize event before calling `HIObjectCreate`:

   - `kEventParamToolbarIdentifier`, the identifier for this toolbar item.
   - `kEventParamAttributes`, any toolbar attributes you want to set.
   - `kEventParamToolbarItemConfigData`, a pointer to any specific configuration data. In this case, the configuration data would be a pointer to the URL obtained from the drag.
7. After passing the CFURL to the toolbar item creation function, you can release your reference to it.

The event handler for your custom URL toolbar item class must handle the usual creation, destruction, and initialization events. The construction event allocates memory for the instance data, and the destruction event releases it. Note that the data structure for the instance data has two fields in this case: one to hold the toolbar item reference, and the other to hold the URL.

```
struct CustomToolbarItem
{
    HIToolbarItemRef        toolbarItem;
    CFURLRef                url;
};
typedef struct CustomToolbarItem CustomToolbarItem;
```

The initialization event handler must obtain the configuration data passed with the event and store that in the instance data as a URL. Listing 2-8 shows an example of how you could do this.

__Listing 2-8__  Initialization function for the kEventHIObjectInitialize event

```swift
/* Assume that the event handler called CallNextEventHandler before
/* calling this function */

static OSStatus InitializeCustomToolbarItem( CustomToolbarItem* inItem,// 1
                     EventRef inEvent )
{
    CFTypeRef       data;
    IconRef         iconRef;

    if ( GetEventParameter( inEvent, kEventParamToolbarItemConfigData,// 2
                     typeCFTypeRef, NULL,
            sizeof( CFTypeRef ), NULL, &data ) == noErr )
    {
        if ( CFGetTypeID( data ) == CFStringGetTypeID() )// 3
            inItem->url = CFURLCreateWithString( NULL, (CFStringRef)data,
                                         NULL );
        else
            inItem->url = (CFURLRef)CFRetain( data );
    }
    else
    {
        inItem->url = CFURLCreateWithString( NULL, // 4
                                CFSTR( "http://www.apple.com" ), NULL );
    }

    HIToolbarItemSetLabel( inItem->toolbarItem, CFSTR( "URL Item" ) );// 5

    if ( GetIconRef( kOnSystemDisk, kSystemIconsCreator, kGenericURLIcon,// 6
                     &iconRef ) == noErr )
    {
        HIToolbarItemSetIconRef( inItem->toolbarItem, iconRef );
        ReleaseIconRef( iconRef );// 7
    }

    HIToolbarItemSetHelpText( inItem->toolbarItem, // 8
                        CFURLGetString( inItem->url ), NULL );

    return noErr;
}
```

Here is how the code works:

1. This function takes two parameters: the toolbar item to initialize, and the initialization event that was sent to it.
2. Use `GetEventParameter` to obtain the configuration data stored in the initialization event. This is the URL obtained from the drag (the one stored in the `kEventHIObjectInitialize` event passed to `HIObjectCreate`.
3. If the configuration data passed is of type `CFString`, then you must call `CFURLCreateWithString` to convert it to a `CFURL` type before storing it in the instance data structure.

   If the data is already of type `CFURL`, we can simply retain its reference and store it in the instance data.
4. If for some reason no configuration data was passed in the initialization event, set the instance data URL to some default value.
5. Call `HIToolbarItemSetLabel` to set the displayed text for the toolbar item.
6. If your custom toolbar item does not create an HIView to display, in most cases you should assign it an icon. This example simply uses the Icon Services function `GetIconRef` to obtain a generic URL icon, and assigns it to the toolbar item by calling `HIToolbarItemSetIconRef`.
7. After assigning the icon reference to the toolbar item, you can release your reference to it.
8. Call `HIToolbarItemSetHelpText` to assign the help tag text for your toolbar item.

In addition to the `kEventClassHIObject` events, your custom URL toolbar item should also handle two additional events:

- `kEventToolbarItemGetPersistentData`: You receive this event when the toolbar wants to store configuration information in the user’s preferences. You should return a pointer (which must be of type `CFTypeRef`) to any data you want to store in the `kEventParamConfigData` parameter.

  Note that this data is saved in XML format; any data you store in this event must be CFPropertyList-compatible. Currently this means the data must be one of the following types: `CFString`, `CFData`, `CFNumber`, `CFBoolean`, `CFDate`, `CFArray`, and `CFDictionary`.

  Note that for CFType references, you should pass a copy of the data, as the system will dispose of the reference it receives to the configuration data.
- `kEventToolbarItemPerformAction`: You receive this event when the user clicks on your toolbar item. Your handler can then take any appropriate action. For example, if the user clicks on your custom URL toolbar item, you can call the Launch Services function `LSOpenCFURLRef` to open the URL using the user’s default browser.

  Note that if your toolbar item handles the `kEventToolbarItemPerformAction` event, you should set the command ID for the toolbar item to `kHIToolbarCommandPressAction` (value: `'tbpr'`). Doing so ensures that HIToolbar can send the perform action event when your toolbar item is selected from the overflow menu. This command ID is available in Mac OS X v.10.2.3 and later.

[Next](Document%20Revision%20History.md)[Previous](HIToolbar%20Concepts.md)

