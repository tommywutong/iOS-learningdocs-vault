---
title: Apple Events Programming Guide
apple_id: TP40001449
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/responding_aepg/responding_aepg.html
archived_at: '2026-07-15T05:19:29.841743Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Events Programming Guide](Introduction%20to%20Apple%20Events%20Programming%20Guide.md)


[Next](Creating%20and%20Sending%20Apple%20Events.md)[Previous](Working%20With%20the%20Data%20in%20an%20Apple%20Event.md)

# Responding to Apple Events

Your application must be able to respond to certain Apple events sent by the Mac OS, such as the `open application` and `quit` events. If your application has defined additional Apple events that it supports, either to supply services to other applications or to make itself scriptable, it must be ready to respond to those events as well.

This chapter describes how you write handlers to respond to the Apple events your application receives. It also provides an overview of how Carbon applications work with Apple events sent by the Mac OS.

To respond to Apple events, your application registers handler functions with the Apple Event Manager for the events it can handle, as described in [Apple Event Dispatching](Apple%20Event%20Dispatching.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgqwueqkcirauur2c). Your application will only receive Apple events that target it—that is, events that specify your application in their target address descriptor. These include the events described in [Handling Apple Events Sent by the Mac OS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywuerkkijcekr2j). Should your application receive an Apple event it is not expecting, the Apple Event Manager will not find it in your dispatch table, so the event will not be dispatched to one of your handlers, unless you have installed a wildcard handler.

As a result, your event handlers should generally be called only for events they understand. If a problem occurs, it is most commonly due to an error in constructing the event that was sent to your application. Because of this possibility, you may want to test the error handling in your Apple event code by intentionally sending your application Apple events containing unexpected information.

When you declare an Apple event handler, the syntax must match the `AEEventHandlerProcPtr` data type, which is described in detail in _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_. Listing 5-1 shows the declaration for a function that handles the `open documents` Apple event—all your handler declarations use a similar declaration.

__Listing 5-1__  Definition for an Apple event handler

```
static pascal OSErr HandleOpenDocAE (// 1
    const AppleEvent * theAppleEvent,// 2
    AppleEvent * reply,// 3
    SInt32 handlerRefcon);// 4
```

Here’s a description of this function declaration:

1. The `pascal` keyword ensures proper ordering of parameters on the stack.
2. The Apple event for the function to handle. You’ll often extract information from it to help you process the Apple event.
3. The default reply (provided by the Apple Event Manager). It contains no parameters. If no reply is requested, the reply event is a null descriptor.
4. The 32-bit reference constant you supplied for the handler when you first registered it by calling `AEInstallEventHandler`. You can use the reference constant to provide information about the Apple event, or for any other purpose you want.

   For example, you can install, for multiple Apple events, dispatch table entries that specify the same handler but different reference constants. Your handler can then use the reference constant to distinguish between the different Apple events it receives.

When your application handles an Apple event, it may need to interact with the user. For example, your handler for the `print documents` event may need to display a print dialog before printing. Your application should not just assume it is okay to interact with the user in response to an Apple event. It should always call the `AEInteractWithUser` function to make sure it is in the foreground before it interacts with the user.

If `AEInteractWithUser` returns the value `noErr`, then your application is currently in front and is free to interact with the user. If `AEInteractWithUser` returns the value `errAENoUserInteraction`, your application should not attempt to interact with the user.

You can specify flags to the `AESetInteractionAllowed` function to allow the following types of interaction with your application:

- Only when your application is sending an Apple event to itself.
- Only when the client application is on the same computer as your application.
- For any event sent by any client application on any computer.

Both client and server applications specify their preferences for user interaction: the client specifies whether the server should be allowed to interact with the user, and the server (your application) specifies when it allows user interaction while processing an Apple event. For interaction to take place, these two conditions must be met:

- The client application must set flags in the `sendMode` parameter of the `AESend` function indicating that user interaction is allowed.
- The server application must either set no user interaction preferences, in which case it is assumed that only interaction with a client on the local computer is allowed; or it must use the `AESetInteractionAllowed` function to indicate that user interaction is allowed.

If these two conditions are met and if `AEInteractWithUser` determines that both the client and server applications allow user interaction under the current circumstances, `AEInteractWithUser` brings your application to the foreground if it isn’t already in the foreground. Your application can then display a dialog or otherwise interact with the user. The `AEInteractWithUser` function brings your server application to the front either directly or after the user responds to a notification request.

To track when your Carbon or Cocoa application has been switched in or out, you can sign up for notification of the `kEventSystemUserSessionActivated` and `kEventSystemUserSessionDeactivated` events, as described in [User Switch Notifications](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPMultipleUsers/Concepts/UserSwitchNotifications.html#//apple_ref/doc/uid/20002210) in _[Multiple User Environment Programming Topics](../../Mac%20OSX/Multiple%20User%20Environment%20Programming%20Topics/Introduction%20to%20Multiple%20User%20Environments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4da2i)_.

To determine whether your application is currently running in the active user session, you can use the `CGSessionCopyCurrentDictionary` function, together with the `kCGSessionOnConsoleKey`, as described in [Supporting Fast User Switching](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPMultipleUsers/Concepts/FastUserSwitching.html#//apple_ref/doc/uid/20002209) in _[Multiple User Environment Programming Topics](../../Mac%20OSX/Multiple%20User%20Environment%20Programming%20Topics/Introduction%20to%20Multiple%20User%20Environments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4da2i)_.

For more information on working with user interaction, see [Specifying Send and Reply Options](Creating%20and%20Sending%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhewueqkci5cucsch) in this document, as well as the following in _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_:

- The section "User Interaction Level Constants.“
- The constants listed under “AESendMode.“
- The functions `AEInteractWithUser`, `AESetInteractionAllowed`, `AEGetInteractionAllowed`, and `AESend`.

Your Apple event handler typically performs the following operations:

- It extracts information from the received Apple event.
- It performs any requested actions, checking that interaction is allowed before attempting to interact with a user.
- It adds information to the reply Apple event if appropriate.
- It returns a result code. If an error occurs in extracting information from the event or if an error occurs in any other operation:

  - It may add error information to the reply Apple event.
  - It returns an appropriate error code.

For nearly all standard Apple events, your handler extracts data from the event to help determine how to process the event. The following are some kinds of information you are likely to extract:

- The event class and/or the event ID. For example, if you registered your handler with one or more wildcards, you may need to get the event class or event ID to determine which kind of event you actually received. You can obtain this information by calling a function such as `AEGetAttributePtr`, and passing `keyEventClassAttr` or `keyEventIDAttr` for the parameter that specifies the keyword of the attribute to access.
- The direct parameter, which usually specifies the data to be acted upon. [Listing 4-5](Working%20With%20the%20Data%20in%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkobsfvbecqshijeugsq) shows how to get a parameter that contains a list of files from an `open documents` Apple event.
- Additional parameters. These can be any kind of data stored in an Apple event. They might include object specifiers, which identify objects within your application on which the Apple event operates. For information on how to work with object specifiers, see [“Resolving and Creating Object Specifier Records”](https://developer.apple.com/documentation/mac/IAC/IAC-231.html#HEADING231-0) in [Inside Macintosh: Interapplication Communication](https://developer.apple.com/documentation/mac/IAC/IAC-2.html).

[Working With the Data in an Apple Event](Working%20With%20the%20Data%20in%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkobsfvbecqseiffeoqq) provides additional information and examples of how you extract data from an Apple event.

When your application responds to an Apple event, it should perform the standard action requested by that event. For example, your application should respond to the `print documents` event by printing the specified documents.

Many Apple events can ask your application to return data. For instance, if your application is a spelling checker, the client application might expect your application to return data in the form of a list of misspelled words.

If the application that sent the Apple event requested a reply, the Apple Event Manager passes a default reply Apple event to your handler. The reply event has event class `kCoreEventClass` and event ID `kAEAnswer`. If the client application does not request a reply, the Apple Event Manager passes a null descriptor instead—that is, a descriptor of type `typeNull` whose data handle has the value `NULL`.

The default reply Apple event has no parameters, but your handler can add parameters or attributes to it. If your application is a spelling checker, for example, you can return a list of misspelled words in a parameter. However, your handler should check whether the reply Apple event exists before attempting to add to it. Attempting to add to a null descriptor generates an error.

Your handler may need to add error information to the reply event, as described in subsequent sections.

When your handler finishes processing an Apple event, it should dispose of any Apple event descriptors or other data it has acquired. It should then return a result code to the Apple Event Manager. Your handler should return `noErr` if it successfully handles the Apple event or a nonzero result code if an error occurs.

If an error occurs because your application cannot understand the event, it should return `errAEEventNotHandled`. This allows the Apple Event Manager to look for a handler in the system dispatch table that might be able to handle the event. If the error occurs because the event is impossible to handle as specified, return the result code returned by whatever function caused the failure, or whatever other result code is appropriate.

For example, suppose your application receives a `get data` event requesting the name of the current printer, but it cannot handle such an event. In this situation, you can return `errAEEventNotHandled` in case another available handler can handle the `get data` event. However, this strategy is only useful if your application has installed such a system handler, or the event is one of the few for which a system handler may be installed automatically. (For information on handlers that are installed automatically, see [Handling Apple Events Sent by the Mac OS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywuerkkijcekr2j).)

However, if your application cannot handle a `get data` event that requests the fifth paragraph in a document because the document contains only four paragraphs, you should return some other nonzero error, because further attempts to handle the event are pointless.

In addition to returning a result code, your handler can also return an error string by adding a `keyErrorString` parameter to the reply Apple event. The client can use this string in an error message to the user. For more information, see [Returning Error Information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywugrkhizdueqsh).

For scriptable applications, the client is often the Script Editor, or some other application, executing a script. When you return an error code that the Apple Event Manager understands, the Script Editor automatically displays an appropriate error message to the user. You can find tables of error codes documented in _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_ and _Open Scripting Architecture Reference_.

If your handler returns a nonzero result code, the Apple Event Manager adds a `keyErrorNumber` parameter to the reply Apple event (unless you have already added a `keyErrorNumber` parameter). This parameter contains the result code that your handler returns. This can be useful because it associates the error number directly with the return event, which the client application may pass around without the result code.

Rather than just returning an error code, your handler itself can add error information to the reply Apple event. It can add both an error number and an error string. As noted previously, in many cases returning an Apple Event Manager error code will result in an appropriate error message. You should only add your own error text in cases where you can provide information the Apple Event Manager cannot, such as information specific to the operation of your application.

To directly add an error number parameter to a reply Apple event, your handler can call a function like the one in Listing 5-2.

__Listing 5-2__  A function to add an error number to a reply Apple event

```swift
static void AddErrNumberToEvent(OSStatus err, AppleEvent* reply)// 1
{
    OSStatus returnVal = errAEEventFailed;// 2

    if (reply->descriptorType != typeNull)// 3
    {
        returnVal = AESizeOfParam(reply, keyErrorNumber, NULL, NULL);
        if (returnVal != noErr))// 4
        {
            AEPutParamPtr(reply, keyErrorNumber,
                        typeSInt32, &err, sizeof(err));// 5
        }
    }
    return returnVal;
}
```

Here’s a description of how this function works:

1. It receives an error number and a pointer to the reply Apple event to modify.
2. It declares a variable for the return value and sets it to the Apple Event Manager error constant for “Apple event handler failed.” If the function is successful, this value is changed.
3. It checks the descriptor type of the reply Apple event to make sure it is not a null event.
4. It verifies that the event doesn’t already contain an error number parameter (`AESizeOfParam` returns an error if it doesn’t find the parameter).
5. It calls `AEPutParamPtr` to add an error number parameter to the reply event:

   - `keyErrorNumber` specifies the keyword for the added parameter.
   - `typeSInt32` specifies the descriptor type for the added parameter.
   - `err` specifies the error number to store in the added parameter.

In addition to returning a result code, your handler can return an error string in the `keyErrorString` parameter of the reply Apple event. Your handler should provide meaningful text in the `keyErrorString` parameter, so that the client can display this string to the user if desired.

Listing 5-3 shows a function that adds a parameter, from a string reference that refers to Unicode text, to a passed descriptor. You pass the desired keyword to identify the parameter to add. The `AEPutParamString` function calls `AEPutParamPtr`, which adds a parameter to an Apple event record or an Apple event, so those are the types of descriptors you should pass to it. ([Descriptors, Descriptor Lists, and Apple Events](Building%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgmwuerkkjjducqsd) describes the inheritance relationship between common Apple event data types.)

__Listing 5-3__  A function that adds a string parameter to a descriptor

```
OSErr AEPutParamString(AppleEvent *event,
                    AEKeyword keyword, CFStringRef stringRef)// 1
{
    UInt8 *textBuf;
    CFIndex length, maxBytes, actualBytes;

    length = CFStringGetLength(stringRef);// 2

    maxBytes = CFStringGetMaximumSizeForEncoding(length,
                                    kCFStringEncodingUTF8);// 3
    textBuf = malloc(maxBytes);// 4
    if (textBuf)
    {
        CFStringGetBytes(stringRef, CFRangeMake(0, length),
                kCFStringEncodingUTF8, 0, true,
                (UInt8 *) textBuf, maxBytes, &actualBytes);// 5

        OSErr err = AEPutParamPtr(event, keyword,
                typeUTF8Text, textBuf, actualBytes);// 6

        free(textBuf);// 7
        return err;
    }
    else
        return memFullErr;
}
```

Here’s a description of how this function works:

1. It receives a pointer to a descriptor to add a parameter to, a key word to identify the parameter, and a string reference from which to obtain the text for the parameter.
2. It gets the length of the string from the passed reference.
3. It determines the maximum number of bytes needed to store the text, based on its encoding.
4. It allocates a buffer of that size.
5. It gets the text from the string reference.
6. It adds the text as a parameter to the passed descriptor. (If called with the keyword `keyErrorString`, for example, it adds an error string parameter.)
7. It frees its local buffer.

Listing 5-4 shows how you could call `AEPutParamString` to add an error string to a reply Apple event.

__Listing 5-4__  Adding an error string to an Apple event with AEPutParamString

```
CFStringRef errStringRef = getLocalizedErrMsgForErrNumber(err);
OSErr anErr = AEPutParamString(reply, keyErrorString, errStringRef);
```

Here’s a description of how this code snippet works:

1. It calls an application-defined function to obtain a localized error message as a string reference, based on a passed error number. (For information on localized strings, see Working With Localized Strings in _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_.)
2. It calls `AEPutParamString`, passing the event (obtained previously) to add the error text to, the error string keyword, and the string reference for the error message text.

Listing 5-5 shows a handler that responds to the `open documents` Apple event.

__Listing 5-5__  An Apple event handler for the open documents event

```
static pascal OSErrOpenDocumentsAE(const AppleEvent *theAppleEvent, AppleEvent *reply, long handlerRefcon)
{
    AEDescList  docList;
    FSRef       theFSRef;
    long        index;
    long        count = 0;
    OSErr       err = AEGetParamDesc(theAppleEvent,
                            keyDirectObject, typeAEList, &docList);// 1
    require_noerr(err, CantGetDocList);// 2

    err = AECountItems(&docList, &count);// 3
    require_noerr(err, CantGetCount);

    for(index = 1; index <= count; index++)// 4
    {
        err = AEGetNthPtr(&docList, index, typeFSRef,
                        NULL, NULL, &theFSRef, sizeof(FSRef), NULL);// 5
        require_noerr(err, CantGetDocDescPtr);

        err = OpenDocument(&theFSRef);// 6
    }
    AEDisposeDesc(&docList);// 7

CantGetDocList:
CantGetCount:
CantGetDocDescPtr:
    if (err != noErr)// 8
    {
        // For handlers that expect a reply, add error information here.
    }
    return(err);// 9
}
```

Here’s a description of how this `open documents` handler works:

1. It calls an Apple Event Manager function (`AEGetParamDesc`) to obtain a descriptor list from the direct object of the received Apple event. This is a list of file aliases, one for each document to open.
2. It uses the `require_noerr` macro (defined in `AssertMacros.h`) to jump to a labeled location as a simple form of error handling.
3. It calls an Apple Event Manager function (`AECountItems`) to obtain the number of items in the descriptor list.
4. It sets up a loop over the items in the descriptor list.
5. It calls an Apple Event Manager function (`AEGetNthPtr`) to get an item from the list, by index, asking for a type of `typeFSRef`. This causes the function to coerce the retrieved item (a file alias) to the requested type.
6. It calls a function you have written (`OpenDocument`) to open the current document from the list.

   A `print documents` event handler would be very similar to this one, but in this step could call your `PrintDocument` function.
7. It disposes of the document list descriptor.
8. The `open documents` event sent by the Mac OS doesn’t expect a reply, so the `reply` parameter is a null event. For event handlers that expect a reply, this is where you can use the techniques described earlier in this chapter to add an error number or an error string. Some examples of events that expect a reply (and thus supply a non-null reply event) include `get data` events and `quit` events.
9. It returns an error code (`noErr` if no error has occurred).

As an alternative to code shown in this handler, you might use an approach that extracts the document list in the event handler, then passes it to a separate function, `OpenDocuments`, to iterate over the items in the list. This has the advantage that you can also call the `OpenDocuments` function with the document list obtained from `NavDialogGetReply` when you are working with Navigation Services. The `selection` field of the returned `NavReplyRecord` is a descriptor list like the one described above.

Mac OS X sends Apple events to communicate with applications in certain common situations, such as when launching the application or asking it to open a list of documents. These events are sometimes referred to as the “required” events, although applications are not required to support all of them. For example, if your application isn’t document-based, it won’t support the `open documents` or `print documents` events. However, any application that presents a graphical user interface through the Human Interface Toolbox or the Cocoa application framework should respond to as many of these events as it makes sense for that application to support.

Carbon applications typically install Apple event handlers to handle these events, though in some cases a default handler may be installed automatically (as described in [Common Apple Events Sent by the Mac OS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywugrkhizdeuqsc)).

For Cocoa applications, most of the work of responding to events sent by the Mac OS happens automatically, though in some cases applications may want to step in and modify the default behavior. For more details, including some information of general interest, see [How Cocoa Applications Handle Apple Events](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_handle_AEs/SAppsHandleAEs.html#//apple_ref/doc/uid/20001239) in _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_.

The following are Apple events your application is likely to receive from the Mac OS. For information on the constants associated with these events, see [Event ID Constants for Apple Events Sent by the Mac OS](Selected%20Apple%20Event%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgiwugsceirceirse).

- `open application` (or `launch`)

  Received when your application is launched. The application should perform any tasks required when a user launches it without opening or printing any existing documents, though it may of course open a new, untitled document.

  Starting in Mac OS X version 10.4, an `open application` Apple event may contain information about whether the application was launched as a login item or as a service item. For details on working with this kind of information, see “Launch Apple Event Constants” in “Apple Event Manager Constants” in _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_.
- `reopen application`

  Received when the application is reopened—for example, when the application is open but not frontmost, and the user clicks its icon in the Dock. The application should perform appropriate tasks—for example, it might create a new document if none is open.
- `open documents`

  Received with a list of documents for the application to open. [Listing 5-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywugrkhinbuqrch) shows a complete Apple event handler for this event.

  Starting in Mac OS X version 10.4, the `open documents` Apple event may contain an optional parameter identified by the key `keyAESearchText`. If present, the parameter contains the search text from the Spotlight search that identified the documents to be opened. The application should make a reasonable effort to display an occurrence of the search text in each opened document—for example by scrolling text into view that contains all or part of the search text.
- `print documents`

  Received with a list of documents for the application to print. You can obtain file system references to the items in the list using code like that you use when handling an `open documents` event. See [Interacting With the User](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywugrkhjjcesssc) for information on when it is appropriate to display a dialog or perform other interaction.

  Starting in Mac OS X version 10.3, the print documents event was extended to include an optional `print settings` parameter that defines the settings for the print job or jobs, and an optional `print dialog` parameter that specifies whether the application should display the Print dialog. By default, the application should not show the Print dialog if the caller doesn't specify a print dialog parameter. For details, see Technical Note TN2082, [The Enhanced Print Apple Event](https://developer.apple.com/technotes/tn2002/tn2082.html).
- `open contents`

  Available starting in Mac OS X version 10.4. Received when content, such as text or an image, is dropped on the application icon—for example, when a dragged image is dropped on the icon in the Dock.

  The structure of this event is very similar to the `open documents` event. The direct object parameter consists of a list of content data items to be opened. The `descriptorType` for each item in the list indicates the type of the content (`'PICT'`, `'TIFF'`, `'utf8'`, and so on).

  The application should use the content in an appropriate way—for example, if a document is open, it might insert the content at the current insertion point; if no document is open, it might open a new document and insert the provided text or image.

  If your Carbon application provides a service that can accept the type of data in an `open contents` Apple event it receives, you can handle the event without even installing an event handler for it—a default handler will be installed, if one isn’t present, and invoked automatically. As a result, your service provider will receive a `{kEventClassService, kEventServicePerform}` Carbon event.

  Because there is no way to return data from an `open contents` Apple event, the default handler only invokes a service that accepts the given data type but returns nothing.

  If your application doesn’t support services, or if you want to provide special handling for the `open contents` Apple event, your application can install a handler for the event.

  For information on working with services, see _[Setting Up Your Carbon Application to Use the Services Menu](../../Carbon/Setting%20Up%20Your%20Carbon%20Application%20to%20Use%20the%20Services%20Menu/Introduction%20to%20Setting%20Up%20Your%20Carbon%20Application%20to%20Use%20the%20Services%20Menu.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojt)_.
- `quit application`

  Received when the application should quit. The application can perform any special operations required at that time.

  If your application calls `RunApplicationEventLoop`, a simple `quit` handler is installed automatically. If you install your own handler, it can perform any required operations, then return `errAEEventNotHandled` so that the default handler continues quitting the application. If you return another error value, the application will not quit. However, your `quit` handler can call `QuitApplicationEventLoop`, which causes `RunApplicationEventLoop` to quit and return back to `main()`. In that case you can return `noErr` from your handler instead of `errAEEventNotHandled`.

  If your application does not call `RunApplicationEventLoop`, you should supply your own `quit` handler.

  You should not terminate your application from within a `quit` event handler. Instead, you should set a flag that you check outside the handler.
- `show preferences`

  Received when the user chooses the Preferences menu item. Carbon applications that handle the Preferences command can install an Apple event handler for this event, but they more commonly install a Carbon event handler for `kEventCommandProcess` and check for the `kHICommandPreferences` command ID.
- `application died`

  Received by an application that launched another application when the launched application quits or terminates. Your application can respond to the information that the other application is no longer running.

Listing 5-6 shows how your application installs handlers for various Apple events that are sent by the Mac OS. The listing assumes that you have defined the functions `OpenApplicationAE`, `ReopenApplicationAE`, `OpenDocumentsAE`, and `PrintDocumentsAE` to handle the Apple events `open application`, `reopen`, `open documents`, and `print documents`, respectively.

This function doesn’t install handlers for the `open contents` and `quit` Apple events, so the application will rely on the default handlers for those events (described previously in [Common Apple Events Sent by the Mac OS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywugrkhizdeuqsc)).

__Listing 5-6__  Installing event handlers for Apple events from the Mac OS

```
static  OSErr   InstallMacOSEventHandlers(void)
{
    OSErr       err;

    err     = AEInstallEventHandler(kCoreEventClass, kAEOpenApplication,
                NewAEEventHandlerUPP(OpenApplicationAE), 0, false);
    require_noerr(err, CantInstallAppleEventHandler);

    err     = AEInstallEventHandler(kCoreEventClass, kAEReopenApplication,
                NewAEEventHandlerUPP(ReopenApplicationAE), 0, false);
    require_noerr(err, CantInstallAppleEventHandler);

    err     = AEInstallEventHandler(kCoreEventClass, kAEOpenDocuments,
                NewAEEventHandlerUPP(OpenDocumentsAE), 0, false);
    require_noerr(err, CantInstallAppleEventHandler);

    err     = AEInstallEventHandler(kCoreEventClass, kAEPrintDocuments,
                NewAEEventHandlerUPP(PrintDocumentsAE), 0, false);
    require_noerr(err, CantInstallAppleEventHandler);


CantInstallAppleEventHandler:
    return err;
}
```

For a description of the parameters you pass to the `AEInstallEventHandler` function, see [Installing Apple Event Handlers](Apple%20Event%20Dispatching.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgqwueqkcjjdugssh).

[Next](Creating%20and%20Sending%20Apple%20Events.md)[Previous](Working%20With%20the%20Data%20in%20an%20Apple%20Event.md)

