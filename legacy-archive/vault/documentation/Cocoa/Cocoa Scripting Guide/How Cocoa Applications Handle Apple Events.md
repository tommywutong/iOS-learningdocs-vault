---
title: Cocoa Scripting Guide
apple_id: TP40002164
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_handle_AEs/SAppsHandleAEs.html
archived_at: '2026-07-15T07:18:50.826819Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Scripting Guide](Introduction%20to%20Cocoa%20Scripting%20Guide.md)


[Next](Evolution%20of%20Cocoa%20Scriptability%20Information.md)[Previous](Cocoa%20Scripting%20Classes%20and%20Categories.md)

# How Cocoa Applications Handle Apple Events

Whether your application is scriptable or not, Cocoa provides automatic handling for certain Apple events that all applications receive. This chapter describes Cocoa's default support for handling those Apple events and what your application must do to support or modify the default behavior.

All Mac apps that present a graphical user interface should be able to respond to certain Apple events that are sent by the Mac OS. These events, sometimes called the _required events_, include those the application can receive at launch (the `open application`, `open documents`, `print documents`, and `open contents` events), as well as others it receives when already running (again including `open documents` and `print documents`, as well as the `reopen` and `quit` events). These events can also be sent by other applications and by users executing scripts.

If an application is scriptable, it can receive additional events that target the scriptable features it supports.

Applications work with the Apple Event Manager to receive and extract information from Apple events. The processing of Apple events typically follows this pattern:

1. For the Apple events an application expects to receive, it registers callback routines, called Apple event handlers, with the Apple Event Manager.
2. When the application receives an Apple event, it uses the Apple Event Manager to dispatch the event to the appropriate event handler and to identify the object or objects in the application on which to perform the specified operation. (The details vary depending on the programming environment in use.)

You can read more about this process in _[Apple Events Programming Guide](../../Apple%20Script/Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_ and _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_. The implementation of code to handle Apple events can be somewhat complex. However, Cocoa provides a lot of built-in support for handling Apple events, minimizing the need for your application to work directly with Apple event data structures or the Apple Event Manager.

For every Cocoa application, the Application Kit automatically installs event handlers for Apple events it knows how to handle, including those sent by the Mac OS. These event handlers implement a default behavior, described in [Apple Events Sent by the Mac OS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgiztsljrgeytonzwhe), that in some cases depends on code implemented by your application.

A nonscriptable application can support or modify the default behavior provided by the Application Kit's Apple event handlers in these ways:

- It can implement or override the appropriate methods invoked by the Cocoa handlers, as described in [Apple Events Sent by the Mac OS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgiztsljrgeytonzwhe). This is the standard mechanism.
- It can install handlers to supersede the ones installed by Cocoa. To replace a specific event handler, read the information about that event in [Apple Events Sent by the Mac OS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgiztsljrgeytonzwhe), then read how to install a new handler in [Installing an Apple Event Handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgiztsljrgeztimzyhe).

A nonscriptable application can also install handlers for other Apple events. But if your nonscriptable application needs to install many handlers, you should consider making it scriptable.

A scriptable application can support or modify the default behavior provided by the Application Kit's Apple event handlers in the same ways a nonscriptable application can (by implementing or overriding the appropriate methods, or by installing a replacement event handler).

For other Apple events, a scriptable application doesn't typically install handlers directly (although it is free to do so) because it can use the script command mechanism. That mechanism, which automatically installs handlers based on information in the application's sdef file, is summarized in [Snapshot of Cocoa Scripting](Overview%20of%20Cocoa%20Support%20for%20Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzwfvjvonq) and described in more detail in [Script Commands](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delkcijbueq2jjjcq).

The following sections describe Apple events your application is likely to receive from the Mac OS, the response that is expected, and the default behavior supplied by the Application Kit. Your application can implement, or in some cases override, the appropriate methods to support or modify the default behavior. (These events can also be sent by scripts or by other applications.)

The `open application` (or `launch`) Apple event is received when the application is launched. The application should perform any tasks required when a user launches it without opening or printing any documents.

Here is how the `open application` event is handled in OS X version 10.4:

1. The application is launched.
2. The application determines if a new, untitled document should be created by invoking the application delegate’s `applicationShouldOpenUntitledFile:` method. If the application delegate does not implement this method, a new untitled document is created. Implement this method if you want to control that behavior (whether or not your application is `NSDocument`-based.)
3. If the application delegate responds to `applicationOpenUntitledFile:`, that message is sent.

   Otherwise:

   - If the application is `NSDocument`-based, the shared `NSDocumentController` is sent this message:

     `openUntitledDocumentAndDisplay:error:`

     You can modify the default behavior by overriding this method. Or you can override the methods this method invokes (described in the OS X version 10.4 documentation for [NSDocumentController](https://developer.apple.com/documentation/appkit/nsdocumentcontroller)).
   - It the application is not document-based, for a document to be created, your application delegate must implement this method:

     `applicationOpenUntitledFile:`

Starting in OS X version 10.4, an `open application` Apple event may contain information about whether the application was launched as a login item or as a service item. If so, the application typically should only perform actions suitable to the environment in which it is launched. For example, an application launched as a service item may not wish to open an untitled document.

The `reopen` (or `reopen application`) Apple event is received when the application is reopened—for example, when the application is open but not frontmost, and the user clicks its icon in the Dock. The application should perform appropriate tasks—for example, it might create a new document if none is open.

Here is how the `reopen application` event is handled:

1. The application delegate is sent this message (if it implements the method):

   `applicationShouldHandleReopen:hasVisibleWindows:`
2. If the method returns `YES`, and if there are no open windows, it attempts to create a new untitled document in the same way as for the `open application` event.

You can modify the default behavior by implementing the method of the application delegate.

The `open` (or `open documents`) Apple event is received when the application should open a list of one or more documents. For example, the user may have selected document files in the Finder and double-clicked.

Here is how the `open documents` event is handled in OS X version 10.4 (v10.4):

- If the application is `NSDocument`-based, the `NSDocumentController` is sent this message, once for each document to be opened:

```
openDocumentWithContentsOfURL:display:error:
```

  For your application to customize opening of documents in response to the `open documents` Apple event, it can override this method. Or it can override the methods this method invokes. These methods are described in the OS X v10.4 documentation for [NSDocumentController](https://developer.apple.com/documentation/appkit/nsdocumentcontroller), which also describes how the default implementation handles compatibility with previous versions of the Mac OS.
- If the application is not `NSDocument`-based:

  1. The application delegate is sent this message, if it responds to it:

     `application:openFiles:`
  2. If the delegate does not respond to that message, the handler checks, in the order listed, whether the application delegate responds to one of the following messages, and if so, sends it:

```
openTempFile:
openFiles:
openFile:
```

     For your application to open documents in response to this Apple event, it must implement one of these methods.

Starting in OS X version 10.4, the `open documents` Apple event may contain an optional parameter containing search text from a Spotlight search that specified the documents to be opened. This parameter is identified by the keyword `keyAESearchText`. The application should make a reasonable effort to indicate occurrences of the search text in each opened document—for example by selecting the text and scrolling the first or primary occurrence into view. The Application Kit does not currently handle this parameter, but you can provide your own implementation by adding code like that shown in [Listing 10-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgiztslktk4zq) to your method that opens files, such as `application:openFiles:`.

__Listing 10-1__  Extracting the search text parameter from the current Apple event

```
    NSString    *searchString = nil;
    searchString = [[[[NSAppleEventManager sharedAppleEventManager]// 1
        currentAppleEvent]// 2
        paramDescriptorForKeyword:keyAESearchText]// 3
        stringValue];// 4
    // Application-specific code to highlight the searched-for text, if any.// 5
```

Here's what this code snippet does:

1. It invokes the `sharedAppleEventManager` class method of the [NSAppleEventManager](https://developer.apple.com/documentation/foundation/nsappleeventmanager) class to get an instance of the shared manager.
2. It invokes the `currentAppleEvent` method of the `NSAppleEventManager` object to get the Apple event that is being handled on the current thread, if any, as an [NSAppleEventDescriptor](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor).
3. It invokes the `paramDescriptorForKeyword:` method of that class, passing the key `keyAESearchText` (and obtaining another instance of `NSAppleEventDescriptor`).
4. It invokes the `stringValue` method of that class to get the search text, if any, coercing it to Unicode text.
5. It selects instances of the specified text, if any, in the document, as appropriate for the application (not shown). For example, it might scroll the primary instance into view.

The `print` (or `print documents`) Apple event is received when the application should print a list of one or more documents.

Here is how the `print` event is handled in OS X version 10.4:

- If the application is `NSDocument`-based, each document to be printed is sent this message:

```
printDocumentWithSettings:showPrintPanel:delegate:didPrintSelector:contextInfo:
```

  Documents are opened automatically before printing, if necessary. If a document is opened just for printing, it is closed when printing is complete.

  You can modify the default behavior by overriding the methods this method invokes (described in the OS X v10.4 documentation for [NSDocumentController](https://developer.apple.com/documentation/appkit/nsdocumentcontroller)).
- If the application is not `NSDocument`-based, the handler checks, in the order listed, whether the application delegate responds to one of the following messages, and if so, sends it:

```
printFiles:withSettings:showPrintPanels:
printFiles:
printFile:
```

  For your application to print documents in response to this Apple event, it must implement one of these methods.

The `open contents` Apple event is available starting in Mac OS version 10.4. This Apple event is sent when content, such as text or an image, is dropped on the application icon—for example, when a dragged image is dropped on the icon in the Dock. The application should use the content in an appropriate way—for example, if a document is open, it might insert the content at the current insertion point; if no document is open, it might open a new document and insert the provided text or image.

If your application provides a service that can accept the type of data in a received `open contents` Apple event, the default handler will use the service.

Here is how the `open contents` event is handled:

1. It invokes this method of the application delegate, to give the application a chance to set up services: `applicationDidFinishLaunching:`

   This is unique, in that for all the other Apple events described here, `applicationDidFinishLaunching:` is called _after_ the described event handling behavior takes place.
2. It invokes Carbon's default `open contents` Apple event handler, which uses the application-provided service. (Carbon behavior is described in "Common Apple Events Sent by the Mac OS" in [Responding to Apple Events](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/responding_aepg/responding_aepg.html#//apple_ref/doc/uid/TP40001449-CH206) in _[Apple Events Programming Guide](../../Apple%20Script/Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_.

You can modify the default behavior by installing your own `open contents` Apple event handler. The structure of the event is similar to the `open documents` event. The direct parameter consists of a list of content data items to be opened. The descriptor type for each item in the list indicates the type of the content (`'PICT'`, `'TIFF'`, `'utf8'`, and so on).

The `quit` (or `quit application`) Apple event is received when your application is terminated.

Here is how the `quit` event is handled:

- If the application is `NSDocument`-based, the behavior depends on the `saving` parameter, which has one of these three values:

  - `NSSaveOptionsNo`: The application quits without sending a `close` message to any document.
  - `NSSaveOptionsYes`: Each unmodified document is sent a `close` message; each modified document is sent the following message: `saveDocumentWithDelegate:didSaveSelector:contextInfo:`
  - `NSSaveOptionsAsk`: (This is the default value if no `saving` parameter is supplied in the event.) If there are modified documents open, the `NSDocumentController` sends itself this message:

```
reviewUnsavedDocumentsWithAlertTitle:cancellable:delegate:didReviewAllSelector:contextInfo:
```
- If the application is not `NSDocument`-based, the application delegate is sent this message (if it is implemented):

  `applicationShouldTerminate:`

  You can modify the default behavior by implementing this method.

Table 10-1 shows the constants for the Apple event handlers installed by the Application Kit to handle events sent by the Mac OS. Each of these events has the same event class, `kCoreEventClass`, which has the value `'aevt'`. Your application can use these constants for the event class and event ID when installing replacement handlers to modify standard behavior.

These Apple event constants are defined in `AppleEvents.h`, a header in `AE.framework`, a subframework of `ApplicationServices.framework`. These and other constants are described in _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_.

__Table 10-1__  Event class IDs for Apple events sent by the Mac OS

| Apple event | Event ID | Value |
| `open application` (or `launch`) | `kAEOpenApplication` | `'oapp'` |
| `reopen` | `kAEReopenApplication` | `'rapp'` |
| `open` (or `open documents`) | `kAEOpenDocuments` | `'odoc'` |
| `print` (or `print documents`) | `kAEPrintDocuments` | `'pdoc'` |
| `open contents` | `kAEOpenContents` | `'ocon'` |
| `quit` (or `quit application`) | `kAEQuitApplication` | `'quit'` |

Your application, whether scriptable or not, can install Apple event handlers directly. This generally makes sense in the following cases:

- You want to customize the default handling of one of the events for which the Application Kit installs a handler, but you can't do so in the standard way, by implementing or overriding the methods described in [Apple Events Sent by the Mac OS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgiztsljrgeytonzwhe).

  For example, you might want to install a handler for the `open contents` Apple event to override its default behavior.
- You have not made your application scriptable, but you need to handle certain Apple events not supported automatically by the Application Kit.

  If you find yourself handling more than a few Apple events this way, consider making your application scriptable to take advantage of Cocoa scripting's built-in support for handling Apple events.

To install an Apple event handler, you invoke this method of the `NSAppleEventManager` class:

`setEventHandler:andSelector:forEventClass:andEventID:`

The signature for the new handler should match the one shown in Listing 10-2.

__Listing 10-2__  Signature of an event handler function

```objc
- (void)handleAppleEvent:(NSAppleEventDescriptor *)event withReplyEvent:(NSAppleEventDescriptor *)replyEvent;
```

A good place to install event handlers is in the `applicationWillFinishLaunching:` method of the application delegate. At that point, the Application Kit has installed its default event handlers, so if you install a handler for one of the same events, it will replace the Application Kit version.

Listing 10-3 shows how you could install a handler for the `get URL` Apple event.

__Listing 10-3__  Installing an Apple event handler in a Cocoa application

```
NSAppleEventManager *appleEventManager = [NSAppleEventManager sharedAppleEventManager];// 1
[appleEventManager setEventHandler:self andSelector:@selector(handleGetURLEvent:withReplyEvent:) forEventClass:kInternetEventClass andEventID:kAEGetURL];// 2
```

Here’s what the code in Listing 10-3 does:

1. It gets a reference to the shared Apple Event Manager object.
2. It invokes a method of that object to install the new handler, passing:

   - A reference to the delegate object, `self`, which will handle the event.
   - A selector for the new `get URL` handler (shown in [Listing 10-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgiztslkcifbegqscinfa)).
   - The event class constant for the Apple event (from the header `HIServices/InternetConfig.h` in the Application Services framework).
   - The event ID constant for the Apple event (from the header `HIServices/InternetConfig.h` in the Application Services framework).

   If an event handler is already installed for the specified event class and event ID, it is replaced.

Listing 10-4 provides a template for the event handler. This code resides in the implementation of your application delegate. After this handler has been installed, it is invoked whenever the application receives a `get URL` Apple event. The Apple event is passed to the handler as an instance of `NSAppleEventDescriptor`.

__Listing 10-4__  Implementation of a get URL Apple event handler

```objc
- (void)handleGetURLEvent:(NSAppleEventDescriptor *)event withReplyEvent:(NSAppleEventDescriptor *)replyEvent
{
    // Extract the URL from the Apple event and handle it here.
}
```

The implementation details are left to you, but they require using methods of the [NSAppleEventDescriptor](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor) class to extract the URL from the direct parameter of the Apple event, then performing the required operation with it (typically displaying the referenced page in a window). For a similar example, see [Listing 10-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgiztslktk4zq).

Starting with OS X version 10.3, the `NSAppleEventManager` class provides methods for suspending and resuming an individual Apple event. These methods are of use for applications that respond to Apple events without using the built-in Cocoa scripting support. For applications that do take advantage of the Cocoa scripting support, `NSScriptCommand` provides methods for suspending and resuming execution of a script command.

An application typically suspends an Apple event (or a script command) when it performs an asynchronous operation, so that the application won’t receive any more Apple events from the same script until it completes handling of the current event (or script command). For example, suppose the application must display a sheet as part of obtaining information to return in a reply Apple event. If so, it can suspend Apple events (or a script command) before displaying the sheet, insert information into the reply Apple event after the user dismisses the sheet, then resume. This need to suspend and resume can occur with other asynchronous operations (including those that may be open-ended or take a long time to complete).

To suspend an Apple event, you use the `NSAppleEventManager` method `suspendCurrentAppleEvent`, which returns a suspension ID (`NSAppleEventManagerSuspensionID`) for an Apple event being handled on the current thread. You can pass this suspension ID to `appleEventForSuspensionID:` to get an Apple event descriptor for the suspended event, or to `replyAppleEventForSuspensionID:` to get a descriptor for the corresponding reply Apple event. To resume a suspended Apple event, you pass the associated suspension ID to `resumeWithSuspensionID:`. In OS X version 10.4, this method can be invoked in any thread.

To suspend a script command, use the `NSScriptCommand` method `suspendExecution`. This method suspends execution of a script command if the receiver is being executed in the current thread by the built-in Cocoa scripting support (that is, the receiver would be returned by `[NSScriptCommand currentCommand]`). You use `resumeExecutionWithResult:` to resume a suspended script command. In OS X version 10.4, this method can be invoked in any thread.

[Next](Evolution%20of%20Cocoa%20Scriptability%20Information.md)[Previous](Cocoa%20Scripting%20Classes%20and%20Categories.md)

