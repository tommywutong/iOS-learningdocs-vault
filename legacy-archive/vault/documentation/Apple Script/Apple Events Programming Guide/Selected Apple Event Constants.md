---
title: Apple Events Programming Guide
apple_id: TP40001449
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/appendix2_aepg/appendix2_aepg.html
archived_at: '2026-07-15T05:19:25.564623Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Events Programming Guide](Introduction%20to%20Apple%20Events%20Programming%20Guide.md)


[Next](Default%20Coercion%20Handlers.md)[Previous](Selected%20Apple%20Event%20Manager%20Functions.md)

# Selected Apple Event Constants

This appendix describes some commonly used Apple event constants. For more complete documentation, see _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_.

Table B-1 lists several event class constants. For related information, see [Event Class and Event ID](Building%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgmwvgvzr).

__Table B-1__  Examples of Apple event class constants

| Event class | Value | Description |
| `kCoreEventClass` | `'aevt'` | An Apple event sent by the Mac OS that your application should support if appropriate (sometimes called “required” events) |
| `kAECoreSuite` | `'core'` | A core Apple event; events with this type or with the `kCoreEventClass` type make up the “standard” events—basic events that scriptable applications should support if applicable |
| `kAEFinderSuite` | `'fndr'` | An event that the Finder accepts |
| `kAEFinderEvents` | `'FNDR'` | Deprecated constant for Finder event |
| `kAERPCClass` | `'rpc '` | Remote procedure call event |
| `kAETextSuite` | `'TEXT'` | Text suite event |
| `kFASuiteCode` | `'faco'` | Folder actions event |
| `kAEInternetSuite` | `'gurl'` | Internet suite event |
| `kAETableSuite` | `'tbls'` | Table suite event |

Table B-2 shows event IDs for various Apple events that may be sent to your application by the Mac OS. For more information, see [Handling Apple Events Sent by the Mac OS](Responding%20to%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywuerkkijcekr2j). These events are sometimes referred to as the “required” events, and have the event class value `'aevt'`, defined by the constant `kCoreEventClass`. For related information, see [Event Class and Event ID](Building%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgmwvgvzr).

__Table B-2__  Event ID constants for Apple events sent by the Mac OS

| Event ID | Value | Description |
| `kAEOpenApplication` | `'oapp'` | Sent when a user opens your application without opening or printing any documents. |
| `kAEReopenApplication` | `'rapp'` | Sent when the application is reopened. |
| `kAEOpenDocuments` | `'odoc'` | Sent with a list of documents to be opened. |
| `kAEPrintDocuments` | `'pdoc'` | Sent with a list of documents to be printed. |
| `kAEOpenContents` | `'ocon`' | Sent with content to be displayed (such as when dragged content is dropped on an application icon in the Dock). |
| `kAEQuitApplication` | `'quit`' | Sent when the application is quitting. |
| `kAEShowPreferences` | `'pref`' | Sent when the user chooses the Preferences menu item. |
| `kAEApplicationDied` | `'obit`' | Sent to an application that launched another application when the launched application quits or terminates. |

Table B-3 shows event IDs for Apple events that represent various standard AppleScript commands. Each scriptable application should support as many of these commands as make sense for that particular application. These events are sometimes referred to as "standard" or "core" events, and have the event class value `'core'`, defined by the constant `kAECoreSuite`. For related information, see [Event Class and Event ID](Building%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgmwvgvzr).

__Table B-3__  Event ID constants for Apple events for AppleScript commands

| Event ID | Value | Description |
| `kAEClone` | `'clon'` | Duplicate the specified AppleScript object or objects. |
| `kAEClose` | `'clos'` | Close the specified object or objects, usually consisting of windows or documents. |
| `kAECountElements` | `'cnte'` | Return the number of objects of a particular class contained by the specified object or objects. |
| `kAECreateElement` | `'crel`' | Create a new object. |
| `kAEDelete` | `'delo`' | Delete the specified object or objects. |
| `kAEDoObjectsExist` | `'doex`' | Return a boolean value indicating whether the specified object or objects exist. |
| `kAEGetData` | `'getd`' | Return the specified data from an object or set of objects. |
| `kAEMove` | `'move`' | Move an object or set of objects. |
| `kAESave` | `'save`' | Save an object or objects, often consisting of windows or documents. |
| `kAESetData` | `'setd`' | Set the data of an object or objects. |

In a descriptor, the `descriptorType` structure member stores a value that is a four-character code. Table B-4 lists constants for some of the main descriptor types, along with their four-character code values and a description of the kinds of data they identify. For a complete list of the basic descriptor types, see _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_.

__Table B-4__  Common descriptor type constants

| Descriptor type | Value | Description of data |
| `typeBoolean` | `'bool'` | 1-byte Boolean value |
| `typeSInt32` | `'long'` | 32-bit integer |
| `typeUTF8Text` | `'utf8'` | Unicode text (UTF-8 encoding) |
| `typeUTF16ExternalRepresentation` | `'ut16'` | Unicode text (UTF-16 encoding) |
| `typeSInt16` | `'shor'` | 16-bit integer |
| `typeAEList` | `'list'` | List of descriptors |
| `typeAERecord` | `'reco'` | List of keyword-specified descriptors |
| `typeAppleEvent` | `'aevt'` | Apple event |
| `typeEnumerated` | `'enum'` | Enumerated data |
| `typeType` | `'type'` | Four-character code |
| `typeFSRef` | `'fsrf'` | File-system reference |
| `typeNull` | `'null'` | Nonexistent data |

The descriptor type in an address descriptor can be specified by one of the type constants shown in Table B-5 (or by any type you define for which you provide a coercion to one of these types):

__Table B-5__  Descriptor type constants for address descriptors

| Descriptor type | Value | Description |
| `typeApplSignature` | `'sign'` | Application signature |
| `typeTargetID` | `'targ'` | Deprecated; do not use in Mac OS X |
| `typeProcessSerialNumber` | `'psn '` | Process serial number |
| `typeKernelProcessID` | `'kpid'` | Kernel process ID |
| `typeApplicationBundleID` | `'bund'` | Application bundle ID (Mac OS X version 10.3 and later) |
| `typeApplicationURL` | `'aprl'` | Application URL, possibly for a remote application (Mac OS X version 10.1 and later) |
| `typeMachPort` | `'port'` | Mach port. |

For information on how to create a target descriptor, see [Specifying a Target Address](Creating%20and%20Sending%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhewueqkcinfeoqkk).

Your application cannot examine the attributes and parameters of an assembled Apple event directly. Instead, it calls Apple Event Manager functions to request an attribute or parameter by keyword. Keywords are arbitrary values used to keep track of various descriptors.

See “Keyword Parameter Constants” in _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_ for descriptions of keyword constants for additional Apple event parameters.

Table B-6 lists keyword constants for Apple event attributes:

__Table B-6__  Keyword constants for Apple event attributes

| Attribute keyword | Value | Description |
| `keyAddressAttr` | `'addr'` | Address of target or client application |
| `keyEventClassAttr` | `'evcl'` | Event class of Apple event |
| `keyEventIDAttr` | `'evid'` | Event ID of Apple event |
| `keyEventSourceAttr` | `'esrc'` | Nature of the source application |
| `keyInteractLevelAttr` | `'inte'` | Settings for whether to allow bringing a server application to the foreground, if necessary, to interact with the user |
| `keyOriginalAddressAttr` | `'from`' | Address of original source of Apple event if the event has been forwarded |
| `keyReturnIDAttr` | `'rtid'` | Return ID for reply Apple event |
| `keyTimeoutAttr` | `'timo'` | Length of time, in ticks, that the client will wait for a reply or a result from the server |
| `keyTransactionIDAttr` | `'tran'` | Transaction ID identifying a series of Apple events  |

Table B-7 lists keyword constants for commonly used Apple event parameters:

__Table B-7__  Keyword constants for common Apple event parameters

| Parameter keyword | Value | Description |
| `keyDirectObject` | `'----'` | Direct parameter |
| `keyErrorNumber` | `'errn'` | Error number parameter (used only in reply events) |
| `keyErrorString` | `'errs'` | Error string parameter (used only in reply events) |
| `keyProcessSerialNumber` | `'psn '` | Process serial number |
| `keyPreDispatch` | `'phac'` | Dispatch event to predispatch handler |
| `keyAEVersion` | `'vers'` | AppleScript version |

See “Keyword Parameter Constants” in _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_ for descriptions of keyword constants for additional Apple event parameters.

You use the constants in Table B-8 to check the value of the `keyEventSourceAttr` attribute, which specifies the source of an Apple event. [Listing 4-3](Working%20With%20the%20Data%20in%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkobsfvbecqsdi5cecri) shows how to obtain that attribute from an Apple event.

__Table B-8__  Event source type constants

| Constant | Meaning |
| `kAEUnknownSource` | Source of Apple event unknown |
| `kAEDirectCall` | A direct call that bypassed the PPC Toolbox |
| `kAESameProcess` | Target application is also the source application |
| `kAELocalProcess` | Source application is another process on the same computer as the target application |
| `kAERemoteProcess` | Source application is a process on a remote computer on the network |

When you send an Apple event with `AESend`, you use one of the constants in Table B-9 in the `sendMode` parameter to specify how to deal with replies.

__Table B-9__  Send mode constants for the AESend function

| Flag | Description |
| `kAENoReply` | Your application does not want a reply Apple event. |
| `kAEQueueReply` | Your application wants a reply Apple event; the reply appears in your event queue as soon as the server has the opportunity to process and respond to your Apple event. |
| `kAEWaitReply` | Your application wants a reply Apple event and is willing to give up the processor while waiting for the reply; for example, if the server application is on the same computer as your application, your application yields the processor to allow the server to respond to your Apple event. |

[Next](Default%20Coercion%20Handlers.md)[Previous](Selected%20Apple%20Event%20Manager%20Functions.md)

