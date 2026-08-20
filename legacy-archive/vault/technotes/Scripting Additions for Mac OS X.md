---
title: Scripting Additions for Mac OS X
apple_id: DTS10003003
resource_type: Technical Note
platform: macOS
topic: Languages & Utilities
technology: CoreServices
published: '2009-05-29'
source_url: https://developer.apple.com/library/archive/technotes/tn1164/_index.html
archived_at: '2026-07-26T19:53:45.848738Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN1164

# Scripting Additions for Mac OS X

This Technote describes the API that allow developers to create AppleScript scripting additions for Mac OS X. It is directed at application developers who are interested in creating scripting additions.

This Technote describes the API that allow developers to create AppleScript scripting additions for Mac OS X. It is directed at application developers who are interested in creating scripting additions.

[What are Scripting Additions?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfvluqqkul5averk7knbveskqkreu4r27ifceiskujfhu4u27)[Packaging Scripting Additions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfviecq2lifdustshl5jugusjkbkestshl5auircjkreu6tst)[Mac OS X v10.6 (Snow Leopard) and later: Info.plist](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfvgucq27j5jv6wc7kyytaxzwl5pvgtspk5puyrkpkbaverc7l5au4rc7jravirksl5pustsgj5pvatcjknka)[Handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfvgucq27j5jv6wc7kyytaxzwl5pvgtspk5puyrkpkbaverc7l5au4rc7jravirksl5pustsgj5pvatcjknkc2scbjzceyrks)[ThreadSafe](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfvgucq27j5jv6wc7kyytaxzwl5pvgtspk5puyrkpkbaverc7l5au4rc7jravirksl5pustsgj5pvatcjknkc2vcikjcucrctifdek)[Context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfvgucq27j5jv6wc7kyytaxzwl5pvgtspk5puyrkpkbaverc7l5au4rc7jravirksl5pustsgj5pvatcjknkc2q2pjzkekwcu)[Mac OS X v10.5 (Leopard): Info.plist](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfvgucq27j5jv6wc7kyytaxzvl5puyrkpkbaverc7l5pustsgj5pvatcjknka)[Mac OS X v10.4 (Tiger) and earlier: Required Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfviferjnjrcu6ucbkjca)[Initialization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfveu4skujfauysk2ifkest2o)[Termination](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfviferk7jrcu6ucbkjcc2vcfkjgustsbkreu6tq)[Reference Counting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfviferk7jrcu6ucbkjcc2usfizcverkoincv6q2pkvhfiskoi4)[Helpful Tips](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfveektcqizkuyx2ujfifg)[Runtime Considerations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfveektcqizkuyx2ujfifglkskvhfisknivpugt2okneuirksifkest2okm)[Locating Your Scripting Addition's Bundle Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfveektcqizkuyx2ujfifglkmj5bucvcjjzdv6wkpkvjf6u2dkjevavcjjzdv6qkeireviskpjzpvgx2ckvheitcfl5jeku2pkvjegrkt)[Local and Remote Requests](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfveektcqizkuyx2ujfifglkmj5buctc7ifheix2sivgu6vcfl5jekukvivjviuy)[References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfvjekrsfkjcu4q2fkm)[Downloadables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfvce6v2ojrhucrcbijgekuy)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## What are Scripting Additions?

Scripting additions provide a mechanism for delivery of additional functionality that can be used in AppleScripts. A scripting addition can provide Apple event handling and Apple event data coercion handling.

The Apple event handlers and Apple event data coercion handlers installed by a scripting addition are written in basically the same way that handlers used inside an application are written. What differs between scripting additions and applications is the packaging of the code and the mechanisms by which the scripting addition is installed in the system. These differences are discussed in the sections that follow.

[Back to Top](#)

## Packaging Scripting Additions

Scripting additions are packaged as bundles with a name ending with the extension `.osax` and a `CFBundleSignature` of `osax`.

__Note:__ Single-file CFM binaries linked with `CarbonLib` are supported up through Mac OS X v10.5, and only work on PowerPC systems.

[Back to Top](#)

## Mac OS X v10.6 (Snow Leopard) and later: Info.plist

Mac OS X v10.6 (Snow Leopard) uses a data-driven scheme for installing the handlers in a scripting addition. The older methods described below are still supported, but the 10.6-style Info.plist is recommended for performance reasons. The 10.6 format is not backward-compatible; an addition that uses it will only work on Mac OS X v10.6 and later.

The `Info.plist` file must contain a `OSAXHandlers` key whose value is a dictionary containing up to three other dictionaries:

- `Events`: Event handlers.
- `DescCoercions`: Coercion handlers that use the `AECoerceDesc` interface.
- `PtrCoercions`: Coercion handlers that use the `AECoercePtr` interface.

The value in each case is a dictionary whose keys are the eight-character event code (event class and event id) or the "from" and "to" `DescType` values, and whose values are dictionaries describing the handler function. Given this data, the system will take care of installing and uninstalling the handlers for you: there is no initialization or cleanup for you to write. For example, the Info.plist fragment in Listing 1 declares a handler for the `syso`/`dlog` event (better known as `display dialog`), a descriptor-based coercion for `STXT` to `utxt`, and a pointer-based coercion for `TEXT` to `utxt`.

__Listing 1__  Info.plist fragment declaring scripting addition functions.

```
<key>OSAXHandlers</key> <dict>     <key>Events</key>     <dict>         <key>sysodlog</key>         <dict>             <key>Handler</key>             <string>DisplayDialogEventHandler</string>             <key>ThreadSafe</key>             <false/>             <key>Context</key>             <string>Process</string>         </dict>      </dict>     <key>DescCoercions</key>     <dict>         <key>STXTutxt</key>         <dict>             <key>Handler</key>             <string>CoerceStyledTextToUnicodeText</string>         </dict>     </dict>     <key>PtrCoercions</key>     <dict>         <key>TEXTutxt</key>         <dict>             <key>Handler</key>             <string>CoercePlainTextToUnicodeText</string>         </dict>     </dict> </dict>
```

For each handler, the dictionary contains the name of the handler function, and for event handlers, its thread-safety and context requirements, using the keys and values described here:

__Table 1__  Handler dictionary keys

| Key | Description |
| Handler | A string; the name of the handler function. |
| ThreadSafe | A boolean; is the handler thread-safe? (Event handlers only.) |
| Context | A string, one of Any, Machine, User, or Process; the context requirements for the handler. (Event handlers only.) |

### Handler

This is the handler function name. The function must be exported as an entry point into the executable.

### ThreadSafe

OSA and AppleScript in Mac OS X v10.6 are thread-safe. If a script is executed on a background thread and invokes an event handler that is not thread-safe, it will be called on the main thread, which is slower than directly invoking it on the calling thread and may reduce application responsiveness to user input. Ideally, all handlers should be thread-safe. Some inherently cannot be; for example, almost anything that displays UI must be executed on the main thread. You are encouraged to either verify that your event handlers are thread-safe or update them to make them thread-safe.

If the value of this key is true, then the handler may be executed on a non-main thread and it may be executed concurrently from multiple threads. If false, it will only be executed on the main thread. This key is required for event handlers, and must not be present for coercion handlers, which are required to be thread-safe. If a coercion handler cannot be made safe to run on background threads, the handler must arrange to execute the coercion on the main thread, such as using by using libdispatch and the main dispatch queue.

### Context

For security reasons, Mac OS X v10.6 will only execute scripting additions in other processes if it is necessary, and in some cases may ask for authorization before doing so. Exactly how a scripting addition is handled depends on the value of the "Context" key, which describes what execution context the handler depends on in order to function correctly. In the script, a scripting addition command may be inside a `tell` block for, say, Mail.app on a remote machine, but if its "context" is relaxed enough, it will actually be executed in a different process that presents less of a security risk, typically the application running the script. The `Context` key may have one of four values:

__Table 2__  Context values

| Value | Description |
| Any | The handler depends only on its own input parameters, and may be handled within any process on any machine. (For example, offset of, round.) |
| Machine | The handler depends on the machine it is running on, and must be handled within some process on the target machine. (For example, beep, system info.) |
| User | The handler depends on the user and group id, typically because of the user's preferences or permissions, and must be handled within some process with the same user and group id as the target process. (For example, commands that perform file I/O such as open for access and info for.) |
| Process | The handler depends upon attributes that vary between individual processes, and must be handled in the target process on the target machine. (For example, display alert, which layers the alert with the target application's windows.) |

Any value of `Context` implies the dependencies of the contexts above it, so `User` implies `Machine` dependencies, and `Process` implies `User` and `Machine` dependencies. Try to write handlers with as few dependencies as possible, since more dependencies means greater security risk.

This key is required for event handlers, and must not be present for coercion handlers, which are always executed in the same process as the script.

[Back to Top](#)

## Mac OS X v10.5 (Leopard): Info.plist

Mac OS X v10.5 (Leopard) uses an Info.plist identical to the one described above, except that the value for a handler entry is simply a string specifying the name of the handler function, not a dictionary. For example, Listing 2 shows the 10.5-style declaration of `display dialog` shown in Listing 1:

__Listing 2__  Info.plist fragment declaring the display dialog command.

```
<key>OSAXHandlers</key> <dict>     <key>Events</key>     <dict>         <key>sysodlog</key>         <string>DisplayDialogEventHandler</string>     </dict> </dict>
```

Scripting addition event handlers using this format on 10.6 are assumed to be thread-unsafe and have a context of "Machine".

[Back to Top](#)

## Mac OS X v10.4 (Tiger) and earlier: Required Functions

If your scripting addition will only run on Mac OS X v10.5 or later versions, then this Info.plist entry is all you need. If you want it to run on older versions of Mac OS X, then you must supply three additional functions to install, terminate, and reference-count your scripting addition.

__Note:__ These functions are not supported in 64-bit mode. 64-bit scripting additions must use one of the Info.plist formats above.

__Note:__ When running in 10.5 and later, the initialization function will only be called if you do not provide the Info.plist data described above. The reference-count function will never be called, since Leopard will never attempt to unload a scripting addition from a process once it is loaded. The termination functions will also never be called. If your addition needs to do work at process termination time, such as releasing resources, use `atexit`(3). Bear in mind that many resources, such as allocated memory, will be freed automatically when the process exits.

### Initialization

Your scripting addition's initialization routine is responsible for installing your scripting addition's handler routines. To implement it, the scripting addition must export a routine named `SAInitialize`, which will be called by AppleScript and must install all the event and coercion handlers. Listing 3 provides a sketch of a scripting addition's initialization routine:

__Listing 3__  Sample scripting addition initialization routine.

```
OSErr SAInitialize(CFBundleRef additionBundle) {     OSErr err;      Boolean isSysHandler = true;     err = AEInstallEventHandler(theAEEventClass, theAEEventID, eventHandlerUPP, refcon, isSysHandler);     err = AEInstallCoercionHandler(fromType, toType, coercionHandlerUPP, refcon, fromIsDesc, isSysHandler);      return err; }
```

All scripting addition handlers must be installed in the system dispatch table, as shown above.

__Important:__ If your initialization routine returns any result other than `noErr`, then the addition's termination function will not be called, so the initialization function is responsible for cleaning up anything it did. In particular, it should not leave any Apple event handlers installed.

Your scripting addition should always install all of its handlers, even if functionality they require is not present in the system. That way, you have an opportunity to provide a meaningful error message when your addition is invoked, rather than the generic "doesn't understand" or "can't coerce" message.

Your initialization function may perform additional setup operations, such as allocating memory or finding files, but this is not recommended: it creates additional startup cost, and may not even be necessary, since your scripting addition may never be invoked. Initialization should be deferred until your addition is actually invoked.

The `additionBundle` parameter passed to `SAInitialize` is a reference to the scripting addition's bundle. This is only present for historical reasons. If a handler needs access to the scripting addition's bundle resources, it can locate the bundle using `CFBundleGetBundleWithIdentifier`.

Information about bundle references and the bundle format can be found in the [References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfvjekrsfkjcu4q2fkm) section at the end of this article.

### Termination

Your scripting addition's termination routine is responsible for removing your scripting addition's handler routines. To implement it, a scripting addition must export a routine named `SATerminate`, which will be called by AppleScript and must remove all the event and coercion handlers. Listing 4 provides a sketch of a scripting addition's termination routine:

__Listing 4__  Sample scripting addition termination routine.

```
void SATerminate(void) {     AERemoveEventHandler(theAEEventClass, theAEEventID, gTheHandler, true);     DisposeAEEventHandlerUPP(gTheHandler);      ...other cleanup operations... }
```

The termination routine may perform other cleanup operations, such as releasing resources. However, the termination function will never be called in Leopard. If your addition needs to do work at process termination time, such as releasing resources, use `atexit`(3). Bear in mind that many resources, such as allocated memory, will be freed automatically when the process exits.

### Reference Counting

This routine exists for historical reasons: in classic Mac OS, it was possible to crash the system by removing a scripting addition while it was still running. Therefore, scripting additions exported a function named `SAIsBusy` to indicate whether or not they were busy, and therefore not safe to unload. This possible crash was solved by other means in Mac OS X v10.2, rendering `SAIsBusy` obsolete. It still needs to exist, but can simply return `false`, as shown in Listing 5.

__Listing 5__  Sample SAIsBusy routine for a scripting addition.

```
Boolean SAIsBusy(void) {     return false; }
```

[Back to Top](#)

## Helpful Tips

### Runtime Considerations

Your scripting addition may be loaded into any application's process, and should therefore take care to not disturb the global state outside of the addition handler itself, such as the Resource Manager resource chain, effective user id, and so on.

Scripting additions are loaded separately into each application process that uses them. As a result, you should design your scripting addition keeping in mind that there may be many instances of your scripting addition open in many different applications at the same time. Some scripting additions may require additional code if they use a single shared resource such as a printer or a serial port.

### Locating Your Scripting Addition's Bundle Resources

Scripting additions may need to access resources and files located inside of their bundle. To do this, get a `CFBundleRef` using `CFBundleGetBundleWithIdentifier`, passing it the bundle identifier of your scripting addition.

Information about bundle references and the bundle format can be found in the [References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbqgmwugsbrfvjekrsfkjcu4q2fkm) section at the end of this article.

### Local and Remote Requests

If executing your scripting addition command on a remote machine is not meaningful or would constitute a security risk, your command handler should detect and reject events from remote machines. A handler can determine the source of an event by examining the `keyEventSourceAttr` attribute in the incoming event. An event from a remote system will have an attribute value of `kAERemoteProcess`.

```
DescType sourceAttr;  err = AEGetAttributePtr(eventPtr, keyEventSourceAttr, typeType, NULL, &sourceAttr, sizeof(sourceAttr), NULL); if (err != noErr || sourceAttr == kAERemoteProcess) {     return errAELocalOnly; }
```

[Back to Top](#)

## References

- [Apple Event Programming Guide](https://developer.apple.com/documentation/AppleScript/Conceptual/AppleEvents)
- [Bundle Programming Guide](https://developer.apple.com/documentation/CoreFoundation/Conceptual/CFBundles)

[Back to Top](#)

## Downloadables

- Stub scripting addition project. ("tn1164_SkeletonAddition.zip", 7.2K)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-05-29 | Updated for Mac OS X v10.6 with information about security and thread-safety Info.plist entries. |
| 2008-04-24 | Add sample project. |
| 2008-01-15 | Update to cover API changes for Leopard. |
| 2004-04-26 | Unspecified content revisions. |
| 2001-09-13 | New document that explains how to create AppleScript scripting additions (OSAX) for Mac OS X. |

