---
title: Apple Events Programming Guide
apple_id: TP40001449
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/create_send_aepg/create_send_aepg.html
archived_at: '2026-07-15T05:19:29.214370Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Events Programming Guide](Introduction%20to%20Apple%20Events%20Programming%20Guide.md)


[Next](Writing%20and%20Installing%20Coercion%20Handlers.md)[Previous](Responding%20to%20Apple%20Events.md)

# Creating and Sending Apple Events

This chapter provides information and sample code that will help you create and send Apple events and handle Apple events you receive in response to those you send. Before reading this chapter, you should be familiar with the information in [Building an Apple Event](Building%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgmwueqkcirauur2c).

Applications most commonly create and send Apple events for one of the reasons described in [When Applications Use Apple Events](About%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgiwugrkhi5beqrci): to communicate directly with other applications or to support recording in a scriptable application. And as described in [Two Approaches to Creating an Apple Event](Building%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgmwugrkhirbumrkk), you can create an Apple event in one step with the `AEBuildAppleEvent` function, or you can create a possibly incomplete Apple event with `AECreateAppleEvent`, then add attributes and parameters to complete the event.

In addition to the `AEBuildAppleEvent` and `AECreateAppleEvent` functions for creating Apple events, you use the following functions for creating other data structures you use with Apple events:

- For creating descriptor records and lists and adding items to lists:

  `AEBuildDesc`, `AECreateDesc`, `AECreateList`, `AEPutPtr`, `AEPutDesc`
- For adding attributes and parameters to Apple events and Apple event records:

  `AEBuildParameters`, `AEPutParameter`, `AEPutParamDesc`, `AEPutAttributePtr`, `AEPutAttributeDesc`

[Table A-1](Selected%20Apple%20Event%20Manager%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgewugrkhi5fecrcc) lists these and other Apple Event Manager functions. For complete function descriptions, see _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_.

When you create an Apple event, you must specify the address of the target. The _target address_ identifies the particular application or process to send the Apple event to. You can send Apple events to applications on the local computer or on remote computers on the network. You specify a target address with a _target address descriptor_.

The preferred descriptor types for identifying the address in an address descriptor are shown in [Address Descriptor Type Constants](Selected%20Apple%20Event%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgiwugscejjdeurce). You can also use another type if your application provides a coercion handler that coerces that type into one of the address types that the Apple Event Manager recognizes. See [Writing and Installing Coercion Handlers](Writing%20and%20Installing%20Coercion%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhawueqkcirauur2c) for more information on coercion handlers.

To address an Apple event to a target on a remote computer on the network, you generally use `typeApplicationURL` for the address descriptor type. To address an Apple event to a target on the local computer you can use any of the address types.

The fastest way for your application to send an Apple event to itself is to use a target address with a process serial number of `kCurrentProcess`. For more information, see [Addressing an Apple Event for Direct Dispatching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhewueqkciveuuq2b).

If you want to create an Apple event with the `AECreateAppleEvent` function, you need to create a target address descriptor to pass to the function. You can do so by calling the `AECreateDesc` function. Listing 6-1 shows how to create an address descriptor for a process serial number (`typeProcessSerialNumber`). Other target address descriptor types are shown in [Address Descriptor Type Constants](Selected%20Apple%20Event%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgiwugscejjdeurce).

__Listing 6-1__  Creating an address descriptor using a process serial number

```
OSErr               err;
ProcessSerialNumber thePSN;
AEAddressDesc       addressDesc;

err = GetProcessNumber(&thePSN);// 1
if (err == noErr)
{
    err = AECreateDesc(typeProcessSerialNumber,
                        &thePSN, sizeof(thePSN), &addressDesc);// 2
}
```

Here’s a description of how this code snippet works:

1. It calls an application-defined function, `GetProcessNumber`, to obtain the process serial number of another process.

   To create a target address descriptor for the current process, see [Listing 6-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhewueqkciveeqssb).
2. It calls `AECreateDesc` to create a target address based on the specified process serial number.

   Your application should call `AEDisposeDesc` to dispose of the address descriptor when it is finished with it.

When you create an Apple event with the `AEBuildAppleEvent` function, it uses information from the following three parameters to create a target address descriptor:

**`DescType addressType`**
: The address type for the address information described in the next two parameters: for example, `typeProcessSerialNumber` or `typeKernelProcessID`.

**`const void * addressData`**
: A pointer to the address information.

**`long addressLength`**
: The number of bytes pointed to by the `addressData` parameter.

For a code example that uses `AEBuildAppleEvent`, see [Listing 6-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhewueqkcirbeercd).

Applications typically send Apple events to themselves to support recordability, discussed briefly in [When Applications Use Apple Events](About%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgiwugrkhi5beqrci). The best way for your application to send Apple events to itself is to use an address descriptor of `typeProcessSerialNumber` with the `lowLongOfPSN` field set to `kCurrentProcess` and the `highLongOfPSN` field set to 0. Listing 6-2 shows how to do this.

When you send an Apple event with this type of target address descriptor, the Apple Event Manager jumps directly to the appropriate Apple event handler without going through the normal event-processing sequence. This is not only more efficient, it avoids the situation in which an Apple event sent in response to a user action arrives in the event queue after some other event that really occurred later than the user action. For example, suppose a user chooses Cut from the Edit menu and then clicks in another window. If the `cut` Apple event arrives in the queue after the window activate event, a selection in the wrong window might be cut.

__Listing 6-2__  Creating an address descriptor that specifies the current application

```
    AEAddressDesc addressDesc;
    ProcessSerialNumber selfPSN = { 0, kCurrentProcess };// 1

    OSErr err = AECreateDesc(typeProcessSerialNumber, &selfPSN,
                                sizeof(selfPSN), &addressDesc);// 2
```

Here’s a description of how this code snippet works:

1. Sets up a process serial number for the current process, as described above.
2. Calls `AECreateDesc` to create a target address that specifies the current application by its process serial number.

   Your application should call `AEDisposeDesc` to dispose of the address descriptor when it is finished with it.

Your application can send events to itself using other forms of target addressing. However, this can lead to the event dispatching sequence problems just described.

You can use `AECreateRemoteProcessResolver` and related functions to obtain the addresses of other processes on the network. To do so you follow these steps:

1. Call `AECreateRemoteProcessResolver` to get a process resolver.
2. Call `AERemoteProcessResolverGetProcesses` to obtain a dictionary containing, for each remote application, the URL of the application and its human readable name (and possibly other information).
3. Call `AEDisposeRemoteProcessResolver` to dispose of the process resolver.
4. Create a target address descriptor based on a specified URL.

   1. Extract the URL from the dictionary entry as a `CFURLRef`.
   2. Convert it to a `CFStringRef` (for example, with `CFURLGetString`).
   3. Extract a text string in UTF-8 encoding. (For an example of code that extracts unicode text from a `CFStringRef`, see [Listing 5-3](Responding%20to%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywugrkhircecqsb).)
   4. Put the text into an address descriptor using the type `typeApplicationURL`. The format of the URL associated with this type is described in the Discussion section of “Descriptor Type Constants” in _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_.
5. Alternatively, if the dictionary entry contains a process ID for the remote process, you can create an address descriptor based on the type `typeKernelProcessID`.

You can use the remote process resolver technology, for example, to present an interface to allow a user to select a remote application. For more information on these functions, see the section “Locating Processes on Remote Computers” in _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_.

This section provides examples of how to create an Apple event with `AECreateAppleEvent` and with `AEBuildAppleEvent`. These functions are introduced in [Two Approaches to Creating an Apple Event](Building%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgmwugrkhirbumrkk).

The `AEBuildAppleEvent` function provides a mechanism for converting a specially formatted string into a complete Apple event. This function is similar to `AECreateAppleEvent`, but contains additional parameters it uses in creating the Apple event and constructing parameters for it.

The `AEBuildAppleEvent` function is similar to the `printf` family of routines in the standard C library. The syntax for the format string defines an Apple event as a sequence of name-value pairs, with optional parameters preceded with a tilde (~) character. For details, see Technical Note TN2106, [AEBuild\*, AEPrint\*, and Friends](https://developer.apple.com/technotes/tn/tn2045.html).

The next two code listings show how you might use `AEBuildAppleEvent` to create an Apple event that tells the Finder to reveal the startup disk (make it visible on the desktop).

__Listing 6-3__  Constants used in creating a reveal Apple event for the Finder

```
const CFStringRef startupDiskPath = CFSTR("/");// 1
const OSType finderSignature = 'MACS';// 2
```

Here’s a description of these constants, which are defined in `AERegistry.h` and used by the Finder in its Apple event support:

1. Defines a string reference for the POSIX-style path of the startup disk.
2. Defines the application signature for the Mac OS Finder application.

   Because the Finder is always running in Mac OS X, it is generally safe to send it an Apple event without first making sure it has been launched.

Listing 6-4 shows a function that creates an Apple event to reveal the startup disk in the Finder.

__Listing 6-4__  Creating a reveal Apple event with AEBuildAppleEvent

```
OSErr BuildRevealStartupDiskAE (AppleEvent * revealEvent)// 1
{
    FSRef startupDiskFSRef;
    AliasHandle startupDiskAlias;
    OSErr err = noErr;

    CFURLRef startupURLRef =
        CFURLCreateWithFileSystemPath(kCFAllocatorDefault,
            startupDiskPath, kCFURLPOSIXPathStyle, true);// 2

    if (CFURLGetFSRef(startupURLRef, &startupDiskFSRef))// 3
    {
        err = FSNewAlias(NULL, &startupDiskFSRef, &startupDiskAlias);// 4
        if (err == noErr)
        {
            err = AEBuildAppleEvent(// 5
                    kAEMiscStandards,// 6
                    kAEMakeObjectsVisible,// 7
                    typeApplSignature,// 8
                    &finderSignature,// 9
                    sizeof(finderSignature),// 10
                    kAutoGenerateReturnID, // 11
                    kAnyTransactionID,// 12
                    revealEvent,// 13
                    NULL,// 14
                    "'----':[alis(@@)]",// 15
                    startupDiskAlias);// 16
        }
    }
    else
        err = memFullErr;// 17

    return err;// 18
}
```

Here’s a description of how the `BuildRevealStartupDiskAE` function works:

1. It is passed a pointer to an Apple event data structure for the event to be created.
2. It calls `CFURLCreateWithFileSystemPath` to create a `CFURLRef` for the path to the startup disk, passing the constant `startupDiskPath` declared in Listing 6-3.
3. It calls `CFURLGetFSRef` to get an `FSRef` file reference to the startup disk from the `CFURLRef`.
4. It calls `FSNewAlias` to convert the `FSRef` to an alias handle for the startup disk, to use in creating the Apple event.
5. It calls `AEBuildAppleEvent` to create the Apple event. The next several items describe the parameters you pass to that function.
6. Specifies `kAEMiscStandards`, a constant defined in `AERegistry.h`, for the event class.
7. Specifies `kAEMakeObjectsVisible`, also defined in `AERegistry.h`, for the event ID.
8. Passes `typeApplSignature` to specify a target address type.
9. Passes `finderSignature`, defined in Listing 6-3, to specify the application signature for the Finder.
10. Passes the size of the application signature.
11. Passes the Apple Event Manager constant `kAutoGenerateReturnID`, indicating the Apple Event Manager should set a return ID for the event. Your application can specify its own return ID, if needed.
12. Passes the Apple Event Manager constant `kAnyTransactionID`, indicating the event is not part of a series of interdependent transactions.
13. Passes a pointer to the Apple event to be built.
14. Passes a value of `NULL`, indicating no error information is required.

    See Technical Note TN2106, [AEBuild\*, AEPrint\*, and Friends](https://developer.apple.com/technotes/tn/tn2045.html) for information on working with error information when using `AEBuildAppleEvent`.
15. Passes a format string containing information for any attributes and parameters to add to the Apple event. In this case, there is just one parameter, an alias (`'----'`).

    The identifier for the direct parameter in an Apple event is specified by the constant `keyDirectObject` (`'----'`). The minus sign has special meaning in AEBuild strings, so it should always be enclosed in single quotes when it is used to identify the direct parameter for an Apple event.
16. Passes the previously created alias handle as the data corresponding to the entry in the format string.
17. In the case where the function could not create an `FSRef`, it sets a return error value.
18. It returns a value indicating whether an error occurred.

To see how the `BuildRevealStartupDiskAE` function is called, and how you can send the resulting Apple event, see [Listing 6-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhewueqkcjbauir2k).

To create an Apple event with `AECreateAppleEvent`, you perform these steps:

- Prepare a target address descriptor, as described in [Creating a Target Address Descriptor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhewueqkcizdesssg).
- Call `AECreateAppleEvent` to create the Apple event, passing the event class, event ID, and other information.
- If necessary, call other Apple Event Manager functions to add additional information to the event, until it contains all the information required for the task you want to perform.

For example, suppose your application wants to send a `quit` Apple event to another application. It might do this to terminate an application it launched previously, or perhaps to make sure an application is not running so it can perform an update. Listing 6-5 shows how to create a `quit` application Apple event.

__Listing 6-5__  Creating a quit Apple event with AECreateAppleEvent

```
AppleEvent someAE;

err = AECreateAppleEvent(// 1
        kCoreEventClass,// 2
        kAEQuitApplication,// 3
        &theTarget,// 4
        kAutoGenerateReturnID,// 5
        kAnyTransactionID,// 6
        &someAE);// 7
```

Here’s how the code in Listing 6-5 works:

1. It calls `AECreateAppleEvent` to create the Apple event. The following items describe the parameters you pass to that function.
2. Specifies `kCoreEventClass`, a constant defined in `AppleEvents.h`, for the event class.
3. Specifies `kAEQuitApplication`, also defined in `AppleEvents.h`, for the event ID.
4. Passes the address of the previously constructed target address descriptor, which identifies the application to send the `quit` event to.
5. Passes the Apple Event Manager constant `kAutoGenerateReturnID`, indicating the Apple Event Manager should set a return ID for the event. Your application can specify its own return ID, if needed.
6. Passes the Apple Event Manager constant `kAnyTransactionID`, indicating the event is not part of a series of interdependent transactions.
7. It passes the address of an Apple event data structure for the event to be created.

That’s all you need to do to create a `quit` Apple event. However, to create a more complicated Apple event, you typically need to add attributes or parameters to the event. For example, your application might receive a `get data` Apple event for which it returns some specified text as the direct parameter of the reply Apple event. Listing 6-6 shows how to add such a direct parameter, using a previously defined function.

__Listing 6-6__  Adding a direct parameter to an Apple event

```
OSErr anErr = AEPutParamString(// 1
                    reply,// 2
                    keyDirectObject,// 3
                    textStringRef);// 4
```

Here’s how the code in Listing 6-6 works:

1. It calls the application-defined function `AEPutParamString`, shown in [Listing 5-3](Responding%20to%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywugrkhircecqsb). The following items describe the parameters you pass to add a direct parameter to the Apple event.
2. A pointer to the Apple event to add the parameter to.
3. An Apple Event Manager keyword constant specifying that the parameter is to be added as the direct parameter of the Apple event.
4. A `CFStringRef`, obtained prior to the call, that specifies the text for the direct parameter.

You can also use the `AEBuildParameters` function, introduced in [Two Approaches to Creating an Apple Event](Building%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgmwugrkhirbumrkk), to add more complicated attributes or parameters to an existing Apple event.

Regardless of how you create an Apple event, your application is responsible for disposing of it with the `AEDisposeDesc` function when you are finished with it. Your application must also dispose of all the descriptor records it creates when adding parameters and attributes to an Apple event—remember, many Apple Event Manager functions make copies of descriptors and of their associated data, as noted in [Disposing of Apple Event Data Structures](Working%20With%20the%20Data%20in%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkobsfvbecqsfircuosi).

You normally dispose of your Apple event and its reply, if any, after you send the event and receive a result (either from `AESend` or `AESendMessage`). You should dispose of the data structures you created even if the sending function returns an error. If you are sending the event asynchronously, you need not wait for the reply Apple event before disposing of the sent Apple event.

Once you have created an Apple event, the Apple Event Manager provides two choices for sending it. The `AESend` function provides more options but higher overhead, while the `AESendMessage` function provides fewer options but less overhead.

The `AESend` function has parameters for specifying how to handle timeouts, idle processing, and event filtering. It requires your application to link with the entire Carbon framework, which brings in the HIToolbox framework and requires a connection to the window server.

Using `AESend` is appropriate only for applications that require the use of idle processing and event filtering. This type of processing is not generally needed, or recommended, for applications that handle events with Carbon event handlers. Therefore, only Carbon applications that use older style event handling are likely to need to use `AESend`.

The `AESend` function provides these parameters that are not available to `AESendMessage`:

**`AESendPriority sendPriority`**
: This parameter is deprecated in Mac OS X.

**`AEIdleUPP idleProc`**
: A universal procedure pointer to a function that handles events (such as update, operating-system, activate, and null events) that your application receives while waiting for a reply. Your idle function can also perform other tasks (such as displaying a delay cursor) while waiting for a reply or a return receipt.

If your application specifies the `kAEWaitReply` flag in the `sendMode` parameter and you wish your application to get periodic time while waiting for the reply to return, you must provide an idle function. Otherwise, you can pass a value of `NULL` for this parameter.

For advice on whether to use idle functions, see [Specifying Send and Reply Options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhewueqkci5cucsch).

**`AEFilterUPP filterProc`**
: A universal procedure pointer to a function that determines which incoming Apple events should be received while the handler waits for a reply or a return receipt. If your application doesn’t need to filter Apple events, you can pass a value of `NULL` for this parameter. If you do so, no application-oriented Apple events are processed while waiting.

The `AESendMessage` function requires less overhead than the `AESend` function. It also allows you to send Apple events by linking with just the Application Services framework, and not the entire Carbon framework (and window server), as required by `AESend`.

Using the `AESendMessage` function is appropriate for applications that don’t require idle processing and event filtering (most modern Carbon applications), and where any of the following applies:

- Efficiency is a key concern.
- The application has no user interface.
- The application should not link with Carbon.

Regardless of which function you use to send Apple events, you’ll need to specify certain options, such as how to interact with the user, whether you want a reply Apple event, and if so, how to receive it. You do this by setting flags in the `sendMode` parameter, present in both `AESend` and `AESendMessage`. Here’s a brief description of that parameter:

**`AESendMode sendMode`**
: Specifies options for how the server application should handle the Apple event. To obtain a value for this parameter, you add together constants to set bits that specify the reply mode, the interaction level, and possibly flags for other options.

You can read a full description of all the constants for setting send mode flags in the constant section "AESendMode” in _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_. But here are some of the more common choices you might make for these flags.

If you do not want a reply to the Apple event you are sending, you specify the `kAENoReply` flag in the `sendMode` parameter.

If you’re willing to wait a certain amount of time for a reply, specify `kAEWaitReply`—the function does not return until the timeout specified by the `timeoutInTicks` parameter expires or the server application returns a reply. When the server application returns a reply, the `reply` parameter contains the reply Apple event.

If you specify the `kAEWaitReply` flag to `AESend`, you should provide an idle function to process any non-high-level events that occur while your application is waiting for a reply. You supply a pointer to your idle function as a parameter to the `AESend` function. So that your application can process other Apple events while it is waiting for a reply, you can also specify an optional filter function.

You don't provide an idle function or a filter function when you call the `AESendMessage` function because it doesn’t provide parameters for them. If you specify `kAEWaitReply` to `AESendMessage`, it executes in such a way that any timers or event sources added to your run loop are not called while inside `AESendMessage`.

Rather than wait for a reply, you can send Apple events asynchronously and receive reply events when they’re ready through normal event processing. To do this, you specify the `kAEQueueReply` flag and register a handler for reply events with the event class `kCoreEventClass` and event ID `kAEAnswer`. Your application processes reply events in the same way it does other Apple events. This approach is recommended because it is far more efficient than waiting in an idle routine. In addition, it avoids the possibility of getting into odd states, such as loops within loops while waiting for replies as the idle routine processes events.

If you specify `kAEWaitReply` or `kAEQueueReply`, the Apple Event Manager automatically passes a default reply Apple event to the server. The Apple Event Manager returns any nonzero result code from the server’s handler in the `keyErrorNumber` parameter of the reply Apple event. The server can return an error string in the `keyErrorString` parameter of the reply Apple event. The server can also use the reply Apple event to return any data you requested—for example, the results of a numeric calculation or a list of misspelled words.

If you specify the `kAENoReply` flag, the reply Apple event passed to the server application consists of a null descriptor record.

If your Apple event may require the user to interact with the server application (for example, to specify print or file options), you can communicate your user interaction preferences to the server by specifying additional flags in the `sendMode` parameter. These flags specify the conditions, if any, under which the server application can interact with the user and, if interaction is allowed, whether the server should come directly to the foreground or post a notification request.

The server application specifies its own preferences for user interaction by specifying flags to the `AESetInteractionAllowed` function, as described in [Interacting With the User](Responding%20to%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywugrkhjjcesssc).

Listing 6-7 shows how you can build an Apple event with `AEBuildAppleEvent` and send the event with `AESend`.

__Listing 6-7__  Sending an Apple event with the AESend function

```
    OSErr err = noErr;
    AppleEvent revealEvent;

    err = BuildRevealStartupDiskAE(&revealEvent);// 1

    if (err == noErr)
    {
        err = AESend(&revealEvent,// 2
                    NULL,       // No reply event needed.// 3
                    kAENoReply | kAECanInteract,// 4
                    kAENormalPriority,// Normal priority.// 5
                    kAEDefaultTimeout,// Let AE Mgr decide on timeout.// 6
                    NULL,           // No idle function.// 7
                    NULL);          // No filter function.// 8

        err = AEDisposeDesc(&revealEvent);// 9
    }
```

Here’s how the code in Listing 6-7 works:

1. Calls the application-defined function `BuildRevealStartupDiskAE`, shown in [Listing 6-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhewueqkcirbeercd), to build an Apple event that tells the Finder to reveal the startup disk.
2. Calls the function `AESend`, passing the Apple event obtained by the previous function call. The next several items describe the remaining parameters you pass to the `AESend` function.
3. Passes `NULL` for the reply event because no reply is expected.
4. Passes a logical combination of constants indicating that no reply is expected and that interaction with the user is allowed (although none is likely for this event).

   In the case where your application wants an asynchronous reply and does not allow interaction, you would pass `kAEQueueReply | kAENeverInteract`.
5. Passes a constant indicating the event should have normal priority. However, priority is ignored on Mac OS X.
6. Passes a constant indicating the Apple Event Manager should use the default timeout length (usually about thirty seconds). You can, instead, pass a specific value for the number of ticks (sixtieths of a second) to delay.
7. Passes `NULL`, indicating it will not use an idle function (needed only in specific cases where your application waits for a reply).
8. Passes `NULL`, indicating it will not use a filter function (needed, in conjunction with an idle function, only in specific cases where your application waits for a reply).
9. Calls `AEDisposeDesc` to dispose of the Apple event.

   In cases where you expect a reply Apple event, your application should dispose of that event as well, once it is finished with it. If the reply is handled asynchronously, dispose of the reply event in the reply handler.

In this example, the call to `AESend` does not supply an idle function or a filter function. As a result, `AESend` will fall through and call the `AESendMessage` function, which has less overhead. When you don’t require idle and filter functions, you can, of course, call `AESendMessage` directly, as described in the next section.

As noted in [Specifying a Reply in the Send Mode Parameter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhewueqkcineukski), even in the case where your application expects a delayed reply to an Apple event it sends, the most efficient mechanism is to ask for queued replies and register a handler to receive them.

Listing 6-8 shows how you can send an Apple event with `AESendMessage`.

__Listing 6-8__  Sending an Apple event with the AESendMessage function

```
    OSErr err = noErr;
    AppleEvent revealEvent;

    err = BuildRevealStartupDiskAE(&revealEvent);// 1

    if (err == noErr)
    {
        err = AESendMessage(&revealEvent,// 2
                    NULL,// 3
                    kAENoReply | kAENeverInteract,// 4
                    kAEDefaultTimeout);// 5

        err = AEDisposeDesc(&revealEvent);// 6
    }
```

Here’s how the code in Listing 6-7 works:

1. Calls the application-defined function `BuildRevealStartupDiskAE`, shown in [Listing 6-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhewueqkcirbeercd), to build an Apple event that tells the Finder to reveal the startup disk.
2. Calls the function `AESendMessage`, passing the Apple event obtained by the previous function call. The next several items describe the remaining parameters you pass to the `AESendMessage` function.
3. Passes `NULL` for the reply event because no reply is expected.
4. Passes a logical combination of constants indicating that no reply is expected and that interaction with the user is not allowed.
5. Passes a constant indicating the Apple Event Manager should use the default timeout length (usually about thirty seconds). You can, instead, pass a specific value for the number of ticks (sixtieths of a second) to delay.
6. Calls `AEDisposeDesc` to dispose of the Apple event.

When your application receives a reply event, either as a return parameter from the sending routine or in a return event handler, it uses Apple Event Manager functions to extract the information it needs from the event. This process is the same as the one described in [Responding to Apple Events](Responding%20to%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywueqkcirauur2c).

Whenever a server application provides an error string parameter in a reply event, it should also provide an error number. However, you can’t count on all server applications to do so. A client application should therefore check for both the `keyErrorNumber` (for example, see [Listing 5-2](Responding%20to%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywugrkhijbusq2j)) and `keyErrorString` parameters before assuming that no error has occurred.

When your application has finished using the reply Apple event, it should dispose of it by calling the `AEDisposeDesc` function. The Apple Event Manager takes care of disposing of both the Apple event and the reply Apple event after a server application’s handler returns, but the server is responsible for disposing of any data structures it creates while extracting data from the event.

[Next](Writing%20and%20Installing%20Coercion%20Handlers.md)[Previous](Responding%20to%20Apple%20Events.md)

