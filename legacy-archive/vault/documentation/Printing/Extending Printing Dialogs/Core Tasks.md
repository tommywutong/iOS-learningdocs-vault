---
title: Extending Printing Dialogs
apple_id: TP30000979
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/Printing/Conceptual/ExtPrintingDialogs/Core/Core.html
archived_at: '2026-07-18T01:51:37.266491Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Extending Printing Dialogs](Introduction%20to%20Extending%20Printing%20Dialogs.md)


[Next](Custom%20Tasks.md)[Previous](Creating%20a%20Plug-in%20Project.md)

# Core Tasks

This chapter shows you how to implement most of the required callback functions in a printing dialog extension—that is, the functions in the `IUnknownVTbl` and `PlugInIntfVTable` interfaces. The source code presented here contains a core set of data types and functions that you can use in a real-world project with little or no modification.

All the code examples in this chapter are adapted from a complete sample project for writing a printing dialog extension. To view or download the current version of the sample project, see _[PDEProject](../../../samplecode/PDEProject/PDEProject.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanzugu)_ in the ADC Reference Library.

A printing dialog extension is implemented as a loadable bundle that must perform a core set of tasks—including registration, interface discovery, and instance management—that allow it to operate as a printing plug-in in Mac OS X.

To provide a way for the printing system to use your callback functions at runtime, you need to define the data structures described in the following sections:

- [Defining Function Tables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywueqsdivaukqke) describes how to define two static tables with pointers to your callback functions.
- [Defining an Instance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywugskii5fessce) describes how to define a structure that represents an instance of one of your printing dialog extension interfaces.

For each of the two required interfaces that your printing dialog extension must implement—`IUnknownVTbl` and `PlugInIntfVTable`—you need to define a table of function pointers. Taken together, these two tables give your client access to all of the required functions in your printing dialog extension.

Listing 5-1 shows how to define two static data structures for this purpose.

__Listing 5-1__  Function tables for the two required interfaces

```
static const IUnknownVTbl sMyIUnknownVTable =
{
    NULL, // required padding for COM
    MyQueryInterface,
    MyIUnknownRetain,
    MyIUnknownRelease
};

static const PlugInIntfVTable sMyPDEVTable =
{
    {
        MyPMRetain,
        MyPMRelease,
        MyPMGetAPIVersion
    },
    MyPrologue,
    MyInitialize,
    MySync,
    MyGetSummary,
    MyOpen,
    MyClose,
    MyTerminate
};
```

The `sMyIUnknownTable` structure consists of a table of pointers to the three callback functions that all Core Foundation plug-ins must implement.

The `sMyPDEVTable` structure consists of a table of pointers to three functions that all printing plug-ins must implement and to seven functions that all printing dialog extensions must implement.

Your printing dialog extension supplies the base address of each table at runtime, as explained in [Defining an Instance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywugskii5fessce).

Listing 5-2 illustrates how you might define instance structures for these two interfaces. Because both interfaces support reference counting, each structure includes an integer counter.

__Listing 5-2__  Definition of instances in a printing dialog extension

```
typedef struct
{
    const IUnknownVTbl *vtable;
    SInt32 refCount;
    CFUUIDRef factoryID;

} MyIUnknownInstance;

typedef struct
{
    const PlugInIntfVTable *vtable;
    SInt32 refCount;

} MyPDEInstance;
```

Each `vtable` field points to a function table for one of the two required interfaces. You should assign a pointer to the appropriate function table described in [Defining Function Tables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywueqsdivaukqke).

Each `refCount` field is an integer used to keep track of the number of references to an instance. For more information on reference counting, see the discussion of memory management in _Core Foundation Overview_.

In the`IUnknownVTbl` instance, the `factoryID` field identifies the factory function that created the instance.

When a caller asks for an interface at runtime, you should construct an instance and pass its address back to the caller. The caller will pass this pointer back to your printing dialog extension later, giving various callback functions access to the same instance.

The instance pointer you supply must also point to the base address of the function table for the requested interface. In other words, the address of the function table must always be the first field in the instance structure. In Listing 5-2 this is the `vtable` field.

Later in this chapter, you will learn when and how to construct a new instance for each of the two required interfaces.

Your factory function is the main entry point for your printing dialog extension. When the printing system calls `CFPlugInInstanceCreate` to request an instance of your `IUnknownVTbl` interface, Plug-in Services loads your executable and invokes its factory function.

You can give your factory function any name you wish. To support runtime name binding, you need to

- use this name in the `CFPlugInFactories` entry in your property list
- direct the compiler to export the name

Listing 5-3 implements a factory function that constructs an instance of your `IUnknownVTbl` interface and returns its address to the caller.

__Listing 5-3__  A factory function that supplies an instance of the `IUnknownVTbl` interface

```swift
extern void* MyCFPlugInFactory (
    CFAllocatorRef allocator,
    CFUUIDRef typeUUID
)

{
    CFBundleRef         myBundle    = NULL;
    CFDictionaryRef     myTypes     = NULL;
    CFStringRef         requestType = NULL;
    CFArrayRef          factories   = NULL;
    CFStringRef         factory     = NULL;
    CFUUIDRef           factoryID   = NULL;
    MyIUnknownInstance  *instance   = NULL;// 1

    myBundle = MyGetBundle();// 2

    if (myBundle != NULL)
    {
        myTypes = CFBundleGetValueForInfoDictionaryKey (// 3
            myBundle, CFSTR("CFPlugInTypes"));

        if (myTypes != NULL)
        {
            requestType = CFUUIDCreateString (allocator, typeUUID);
            if (requestType != NULL)
            {
                factories = CFDictionaryGetValue (myTypes, requestType);// 4
                CFRelease (requestType);
                if (factories != NULL)
                {
                    factory = CFArrayGetValueAtIndex (factories, 0);// 5
                    if (factory != NULL)
                    {
                        factoryID = CFUUIDCreateFromString (
                            allocator, factory);
                        if (factoryID != NULL)
                        {
                            instance = malloc (sizeof(MyIUnknownInstance));// 6
                            if (instance != NULL)
                            {
                                instance->vtable = &sMyIUnknownVTable;
                                instance->refCount = 1;// 7
                                instance->factoryID = factoryID;// 8
                                CFPlugInAddInstanceForFactory (factoryID);// 9
                            }
                            else {
                                CFRelease (factoryID);
                            }
                        }
                    }
                }
            }
        }
    }

    return instance;
}
```

Here’s what the factory function in Listing 5-3 does:

1. Sets the default return value to `NULL`. The factory function returns `NULL` if there is an error, to indicate that no instance was created.
2. Calls a utility function that returns a reference to your plug-in bundle. An implementation of `MyGetBundle` is provided in the sample project.
3. Gets a reference to the `CFPlugInTypes` dictionary in the property list, which contains the type identifier for this plug-in.
4. Gets a reference to the `CFPlugInFactories` entry for the plug-in type requested by the caller.
5. Gets a reference to the factory identifier for this plug-in type. If your plug-in has more than one factory function, you may need to modify this code.
6. Allocates memory for a new instance of `IUnknownVTbl`.
7. Sets the initial reference count to 1, because the caller owns this instance.
8. Saves the identifier for the factory that created this instance. This identifier is needed later when you remove the registration for this instance.
9. Registers this instance with Plug-in Services. Plug-In Services will not unload your printing dialog extension while an instance is registered.

As a Core Foundation plug-in, your printing dialog extension must implement the three functions in `IUnknownVTbl`. These functions give the printing system access to the other interfaces your printing dialog extension implements. To learn more about how a plug-in provides access to an interface, see [Instantiation of a Programming Interface](Printing%20Dialog%20Extension%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgqwviucykjcummjwgy).

Listing 5-4 implements a query interface function that creates an instance of the `PlugInIntfVTable` interface.

__Listing 5-4__  A query interface function in a printing dialog extension

```swift
static HRESULT MyQueryInterface (
    void *this, // 1
    REFIID iID, // 2
    LPVOID *ppv// 3
)

{
    CFUUIDRef requestID = NULL;
    CFUUIDRef actualID  = NULL;
    HRESULT   result = E_UNEXPECTED;

    requestID = CFUUIDCreateFromUUIDBytes (kCFAllocatorDefault, iID);// 4
    if (requestID != NULL)
    {
        actualID = CFUUIDCreateFromString (// 5
            kCFAllocatorDefault,
            kDialogExtensionIntfIDStr
        );

        if (actualID != NULL)
        {
            if (CFEqual (requestID, actualID))// 6
            {
                MyPDEInstance *instance = malloc (sizeof(MyPDEInstance));
                if (instance != NULL)
                {
                    instance->vtable = &sMyPDEVTable;
                    instance->refCount = 1;
                    *ppv = instance;// 7
                    result = S_OK;
                }
            }
            else
            {
                if (CFEqual (requestID, IUnknownUUID))// 8
                {
                    MyIUnknownRetain (this);
                    *ppv = this;
                    result = S_OK;
                }
                else
                {
                    *ppv = NULL;
                    result = E_NOINTERFACE;
                }
            }

            CFRelease (actualID);
        }

        CFRelease (requestID);
    }

    return result;
}
```

Here’s what the code in Listing 5-4 does:

1. Receives a pointer to the same `IUnknownVTbl` instance that was constructed by your factory function. (To the caller, this pointer is the address of a pointer to the function table for your `IUnknownVTbl` interface.)
2. Receives a string that contains the UUID of the interface the client wants.
3. Receives the address of storage in the calling function for a pointer to a pointer to the function table.
4. Gets a reference to the `CFUUID` for the requested interface. In general, you should always convert a UUID string into a `CFUUID` object before using it.
5. Gets a reference to the conventional `CFUUID` for a printing dialog extension interface. The printing system (the caller) always requests an instance of this interface using the string constant kDialogExtensionIntfIDStr.
6. Checks to see if the caller wants an instance of the `PlugInIntfVTable` interface. This is the usual case.
7. Passes back a pointer to the new instance of the `PlugInIntfVTable` interface.
8. Checks to see if the caller wants a copy of the `IUnknownVTbl` instance. If so, this code assigns the same instance that your factory function supplied. The constant `IUnknownUUID` is defined in the Plug-in Services API.

Listing 5-5 implements a function that retains (increments the reference count of) an instance of the IUnknown interface.

__Listing 5-5__  A function that retains an instance of the IUnknown interface

```swift
static ULONG MyIUnknownRetain (void* this)
{
    MyIUnknownInstance* instance = (MyIUnknownInstance*) this;// 1
    ULONG refCount = 1;// 2

    if (instance != NULL) {
        refCount = ++instance->refCount;// 3
    }

    return (refCount);
}
```

Here’s what the code in Listing 5-5 does:

1. Defines a pointer to the `IUnknownVTbl` instance that was constructed by the factory function. This pointer provides access to the `refCount` field for this instance.
2. Defines a variable for the updated reference count, and sets its default value to 1.
3. Increments the reference count for this instance.

Listing 5-6 implements a function that releases (decrements the reference count of) an instance of the IUnknown interface.

If the reference count reaches zero, the function releases Core Foundation objects on which the instance depended, and then destroys the instance.

__Listing 5-6__  A function that releases an instance of the IUnknown interface

```swift
static ULONG MyIUnknownRelease (void* this)
{
    MyIUnknownInstance* instance = (MyIUnknownInstance*) this;// 1
    ULONG refCount = 0;// 2

    if (instance != NULL)
    {
        refCount = --instance->refCount;// 3
        if (refCount == 0)
        {
            CFPlugInRemoveInstanceForFactory (instance->factoryID);// 4
            CFRelease (instance->factoryID);// 5
            free (instance);// 6
            MyFreeBundle();// 7
        }
    }

    return refCount;
}
```

Here’s what the code in Listing 5-6 does:

1. Defines a pointer to an instance of the `IUnknownVTbl` interface. This is the same instance the factory function supplied.
2. Defines a variable for the updated reference count, and sets its default value to zero.
3. Decrements the reference count for this instance.
4. Removes the instance from the Plug-in Services registry.
5. Releases the factory ID, because it is no longer needed.
6. Deallocates storage for the instance.
7. Releases our bundle reference, in case the plug-in is being unloaded. For more information about `MyFreeBundle`, see the comments in the sample project that accompanies this book.

The sample code presented in this section shows you how to implement the seven required callback functions discussed in [Activation](Printing%20Dialog%20Extension%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgqwviucykjcummjq), in a manner that supports reentrancy.

To support document-modal (or sheet) dialogs, a printing dialog extension must be capable of managing the state of its pane in several dialog windows concurrently.

For each dialog window, your printing dialog extension allocates memory for pane state information and supplies its address—called a _context_—to the printing system.

Listing 5-7 shows how the context is defined in the sample project.

__Listing 5-7__  A sample context structure

```
typedef struct
{
    ControlRef       userPane;
    EventHandlerRef  helpHandler;
    EventHandlerUPP  helpHandlerUPP;
    void*            customContext;
    Boolean          initialized;

} MyContextBlock;

typedef MyContextBlock* MyContext;
```

The `userPane` field is a reference to the container control into which you embed the controls in your custom interface.

The `helpHandler` field is a reference to a Carbon event handler that’s active when your custom pane is visible. The handler detects when the help button is clicked, and displays your custom help content using Help Viewer.

The `helpHandlerUPP` field is a universal procedure pointer that’s allocated and used whenever the help event handler is installed.

The `customContext` field is for a pointer to a block of additional memory allocated in your custom code, as described in [Defining a Custom Context](Custom%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqg4wugskijbcucr2d).

The `initialized` field indicates whether the interface in your custom pane has been constructed and initialized.

All printing dialog extensions must implement the ten functions in the `PlugInIntfVTable` interface. The first three functions—`PMRetain`, `PMRelease`, and `PMGetAPIVersion`—are described in the appendix [Printing Plug-in Header Functions](Printing%20Plug-in%20Header%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrrgawviubr). The remaining seven functions are described here in this section.

The prologue function allocates a block of memory for a context, and passes this context—along with some static information about your custom pane—back to the printing system.

You can give your prologue function any name you wish. You need to enter this name in the function table for the `PlugInIntfVTable` interface, as described in [Defining Function Tables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywueqsdivaukqke).

Listing 5-8 implements a prologue function.

__Listing 5-8__  A prologue function

```swift
static OSStatus MyPrologue// 1
(
    PMPDEContext    *outContext,
    OSType          *creator,
    CFStringRef     *paneKind,
    CFStringRef     *title,
    UInt32          *maxH,
    UInt32          *maxV
)

{
    MyContext context = NULL;
    OSStatus result = kPMInvalidPDEContext;

    context = malloc (sizeof (MyContextBlock));// 2
    if (context != NULL)
    {
        context->customContext = MyCreateCustomContext();// 3
        context->initialized = false;
        context->userPane = NULL;

        *outContext = (PMPDEContext) context;// 4
        *creator    = kMyBundleCreatorCode;// 5
        *paneKind   = kMyPaneKindID;// 6
        *title      = MyGetTitle();// 7
        *maxH       = kMyMaxH;// 8
        *maxV       = kMyMaxV;// 9

        result = noErr;
    }

    return result;// 10
}
```

Here’s what the code in Listing 5-8 does:

1. The six calling parameters are all pointers to storage provided by the caller (the printing system) to receive information from this prologue function.
2. Allocates memory for a new context.
3. Calls a function that creates and returns a custom context. This context is described in [Defining a Custom Context](Custom%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqg4wugskijbcucr2d).
4. Passes back your context to the printing system.
5. Passes back the unique 4-byte creator code that identifies your printing dialog extension. This code is described in [Defining Bundle, Pane, and Nib Identifiers](Custom%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqg4wviucykjcummjwhe).
6. Passes back the string that identifies your custom pane. This identifier is described in [Defining Bundle, Pane, and Nib Identifiers](Custom%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqg4wviucykjcummjwhe).
7. Passes back the title of your custom pane, which is supplied by the custom function described in [Providing the Title of your Custom Pane](Custom%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqg4wviucykjcummjsha). Your printing dialog extension retains ownership of the title string, and should release it when it’s no longer needed.

   If you are implementing one of the standard sets of printing features listed in [Table 1-1](Printing%20Features%20and%20Printing%20Dialog%20Panes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgiwueqsdijeeerce), the printing system may not use your custom title.
8. Passes back the desired width of the custom pane in pixel units. While this value is not used by the printing system in Mac OS X version 10.2 and earlier, it might be used in a future version of Mac OS X.
9. Passes back the desired height of the custom pane in pixel units.
10. Returns a result code to the caller. If your prologue function returns a non-zero result code, the printing system immediately unloads your printing dialog extension (without calling your terminate function.)

If your prologue function returns `noErr`, the printing system proceeds to call your initialize function.

You can give the initialize function any name you wish. You need to enter this name in the function table for the `PlugInIntfVTable` interface, as described in [Defining Function Tables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywueqsdivaukqke).

As the name suggests, the purpose of the initialize function is to provide initial values for the settings associated with your user interface. If the settings are already defined in a ticket, the initialize function should retrieve their values from the ticket at this time.

In Mac OS X version 10.2 and later, you can use `SetControlBounds` to adjust the vertical size of the user pane at this time. If your pane is displayed later, the dialog will reflect the adjusted pane height. This feature is useful if the desired size of your pane is not known until your initialize function is called.

Listing 5-9 implements a “lazy” initialize function that defers the task of creating and embedding Carbon controls until later, when the open function is called (see [Open](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywueqsdinduoqsi)). As a result, the cost of creating the user interface is not incurred unless a user actually displays the pane.

__Listing 5-9__  An initialize function

```swift
static OSStatus MyInitialize
(
    PMPDEContext inContext,
    PMPDEFlags *flags,
    PMPDERef ref,// 1
    ControlRef userPane,// 2
    PMPrintSession session// 3
)

{
    MyContext context = (MyContext) inContext;// 4
    OSStatus result = noErr;

    *flags = kPMPDENoFlags;
    context->userPane = userPane;// 5

    result = MySync (
        inContext, session, kSyncPaneFromTicket);// 6

    return result;// 7
}
```

Here’s what the code in Listing 5-9 does:

1. The `ref` parameter is not used.
2. Receives a reference to a user pane created for you by the printing system. Later, you will embed the Carbon controls for your user interface into this user pane.
3. Receives a reference to a session object that contains information about the current printing session. Your printing dialog extension uses this parameter to gain access to a job ticket.
4. Casts the parameter to your context type. This is the same context you defined and passed back to the printing system in your prologue function.
5. Saves the pane reference for later use.
6. Calls the function described in [Sync](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywviucykjcummjtga) to initialize your settings. If the job ticket does not contain your settings, then default values are used.
7. Returns a result code to the caller. If your initialize function returns a non-zero result code, the printing system immediately calls your terminate function.

The sync function in a printing dialog extension maintains the correspondence between the settings in a custom pane and their recorded values in either the `PMPageFormat` or the `PMPrintSettings` ticket.

You can give your sync function any name you wish. You need to enter this name in the function table for the `PlugInIntfVTable` interface, as illustrated in [Defining Function Tables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywueqsdivaukqke).

There are two possible ways to synchronize—update ticket from pane, or update pane from ticket. Because synchronization requires knowledge of your custom settings, the work is done in the custom functions `MySyncPaneFromTicket` and `MySyncTicketFromPane`. These two functions are described in [Synchronizing User Settings With a Ticket](Custom%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqg4wviucykjcummjtga).

Listing 5-10 implements a sync function that calls the appropriate custom sync function, based on the sync direction specified by the caller. Two parameters are passed to the custom function—the custom context described in [Defining a Custom Context](Custom%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqg4wugskijbcucr2d), and the printing session.

__Listing 5-10__  A sync function

```swift
static OSStatus MySync
(
    PMPDEContext inContext,
    PMPrintSession session,
    Boolean syncDirection
)

{
    MyContext context = (MyContext) inContext;
    OSStatus result = noErr;

    if (syncDirection == kSyncPaneFromTicket) {
        result = MySyncPaneFromTicket (context->customContext, session);
    }
    else {
        result = MySyncTicketFromPane (context->customContext, session);
    }

    return result;
}
```


The summary function in a printing dialog extension provides the title and current value of each setting in its custom pane. The printing system displays this information in the Summary pane.

You can give this function any name you wish. You need to enter this name in the function table for the `PlugInIntfVTable` interface, as illustrated in [Defining Function Tables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywueqsdivaukqke).

Listing 5-11 implements a summary function that creates two summary arrays, calls the custom function `MyGetSummaryText` to fill them in, and then passes the arrays back to the printing system.

__Listing 5-11__  A summary function

```swift
static OSStatus MyGetSummary
(
    PMPDEContext inContext,
    CFArrayRef *titles,
    CFArrayRef *values
)

{
    MyContext context = (MyContext) inContext;
    CFMutableArrayRef titleArray = NULL;
    CFMutableArrayRef valueArray = NULL;

    OSStatus result = kPMInvalidPDEContext;

    titleArray = CFArrayCreateMutable (// 1
        kCFAllocatorDefault, 0, &kCFTypeArrayCallBacks);

    if (titleArray != NULL)
    {
        valueArray = CFArrayCreateMutable (// 2
            kCFAllocatorDefault, 0, &kCFTypeArrayCallBacks);

        if (valueArray != NULL)
        {
            result = MyGetSummaryText (// 3
                context->customContext,
                titleArray,
                valueArray
            );
        }
    }

    if (result != noErr)
    {
        if (titleArray != NULL)
        {
            CFRelease (titleArray);
            titleArray = NULL;
        }
        if (valueArray != NULL)
        {
            CFRelease (valueArray);
            valueArray = NULL;
        }
    }

    *titles = titleArray;// 4
    *values = valueArray;

    return result;
}
```

Here’s what the code in Listing 5-11 does:

1. Creates the mutable array `titleArray`. The second argument is zero to indicate that the array should not have a fixed size.

   Core Foundation arrays may contain references to mixed types, but in this case the printing system assumes this is an array of strings.
2. Creates the mutable array `valueArray` with the same characteristics.
3. Calls a custom function that fills in `titleArray` and `valueArray` with strings that describe the current values of the settings in your pane.
4. Passes the arrays back to the printing system, which is responsible for releasing the arrays and their contents.

When the dialog user displays your custom pane, the printing system calls your open function immediately before the pane becomes visible.

You can give this function any name you wish. You need to enter this name in the function table for the `PlugInIntfVTable` interface, as illustrated in [Defining Function Tables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywueqsdivaukqke).

Listing 5-12 implements an open function that constructs a custom nib-based interface inside a dialog pane, sets the default values of the controls in the interface, prepares the interface for display, and installs an event handler for the help button.

__Listing 5-12__  An open function

```swift
static OSStatus MyOpen (PMPDEContext inContext)
{
    MyContext context = (MyContext) inContext;
    OSStatus result = noErr;

    if (!context->initialized)
    {
        IBNibRef nib = NULL;

        result = CreateNibReferenceWithCFBundle (// 1
            MyGetBundle(), // 2
            kMyNibFile,
            &nib
        );

        if (result == noErr)
        {
            WindowRef nibWindow = NULL;

            result = CreateWindowFromNib (// 3
                nib,
                kMyNibWindow,
                &nibWindow
            );

            if (result == noErr)
            {
                result = MyEmbedCustomControls (// 4
                    context->customContext,
                    nibWindow,
                    context->userPane
                );

                if (result == noErr)
                {
                    context->initialized = TRUE;
                }

                DisposeWindow (nibWindow);
            }

            DisposeNibReference (nib);
        }
    }

    if (context->initialized)
    {
        result = MyInstallHelpEventHandler (// 5
            GetControlOwner (context->userPane), // 6
            &(context->helpHandler),// 7
            &(context->helpHandlerUPP)// 8
        );
    }

    return result;
}
```

Here’s what the code in Listing 5-12 does:

1. Creates a nib object, using the nib file located inside the plug-in bundle for this printing dialog extension.
2. Calls a custom function that returns a reference to the plug-in bundle. For an implementation of this function, see the sample project.
3. Instantiates your nib-based interface in an offscreen Carbon window.
4. Calls a custom function that embeds your custom controls inside the dialog pane. For more information, see [Embedding Your Controls in a Dialog Pane](Custom%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqg4wugqkdincusrkd).
5. Calls a custom function that installs a Carbon event handler when your custom pane is visible. For more information, see [Installing a Help Event Handler](Utility%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqhewviucykjcummjwgy).
6. Gets a reference to the dialog window.
7. Saves a reference to the event handler. You should remove the handler when the pane closes.
8. Saves the event handler UPP. You should deallocate the UPP when the event handler is removed.

The printing system pairs each call to the open function with a corresponding call to the close function—except when your pane is visible and the user cancels the dialog. The close function performs any necessary tasks when the printing system hides your pane.

You can give your close function any name you wish. You need to enter this name in the function table for the `PlugInIntfVTable` interface, as illustrated in [Defining Function Tables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywueqsdivaukqke).

Listing 5-13 implements a close function that removes the help event handler installed in [Open](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywueqsdinduoqsi).

__Listing 5-13__  A close function

```swift
static OSStatus MyClose (PMPDEContext inContext)
{
    MyContext context = (MyContext) inContext;
    OSStatus result = noErr;

    result = MyRemoveHelpEventHandler (
        &(context->helpHandler),
        &(context->helpHandlerUPP)
    );

    return result;
}
```


The printing system calls the terminate function when the dialog is dismissed for any reason, or when the user changes the destination printer. The terminate function performs necessary clean-up tasks, such as releasing resources and deallocating memory.

You can give this function any name you wish. You need to enter this name in the function table for the `PlugInIntfVTable` interface, as described in [Defining Function Tables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywueqsdivaukqke).

Listing 5-14 implements a terminate function that frees the two contexts allocated in the prologue function, described in [Prologue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywviucykjcummjsha).

__Listing 5-14__  A terminate function

```swift
static OSStatus MyTerminate (
    PMPDEContext inContext,
    OSStatus inStatus
)

{
    MyContext context = (MyContext) inContext;
    OSStatus result = noErr;

    if (context != NULL)
    {
        result = MyRemoveHelpEventHandler (// 1
            &(context->helpHandler),
            &(context->helpHandlerUPP)
        );

        if (context->customContext != NULL) {
            MyReleaseCustomContext (context->customContext);// 2
        }

        free (context);// 3
    }

    return result;
}
```

Here’s what the code in Listing 5-14 does:

1. Removes the help event handler if it’s still installed. For more information, see [Installing a Help Event Handler](Utility%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqhewviucykjcummjwgy).
2. Releases your custom context. For more information, see [Defining a Custom Context](Custom%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqg4wugskijbcucr2d).
3. Frees memory allocated for the context. For more information about contexts, see[Defining a Context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywugskijbcucr2d) and [Prologue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywviucykjcummjsha).

[Next](Custom%20Tasks.md)[Previous](Creating%20a%20Plug-in%20Project.md)

