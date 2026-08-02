---
title: Loading Scripting Additions in Mac OS X
apple_id: DTS10001622
resource_type: QA
platform: macOS
topic: Languages & Utilities
technology: CoreServices
published: '2005-05-06'
source_url: https://developer.apple.com/library/archive/qa/qa1070/_index.html
archived_at: '2026-07-18T02:29:55.500636Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1070

# Loading Scripting Additions in Mac OS X

## Q:  I would like to use scripting additions in my application by sending myself Apple events, but I get "event not handled" errors. How do I load the scripting additions?

A: I would like to use scripting additions in my application by sending myself Apple events, but I get "event not handled" errors. How do I load the scripting additions?

First, a little architectural background: In classic Mac OS, scripting addition handlers are loaded at boot time into a shared system-wide table, namely the Apple Event Manager's "system handler table." Also, the scripting addition handlers are refreshed whenever someone sends a `kASAppleScriptSuite`/`kGetAEUT` event to the handler installed by AppleScript. (The event id "gdut" is short for "get dynamic user terminology.") AppleScript sends itself a `kASAppleScriptSuite`/`kGetAEUT` event when it is first initialized and before it compiles a script.

In Mac OS X, the system handler table is somewhat misnamed: there is a separate one for each application, and they are not shared at all, so each one must be initialized separately. For performance reasons, this isn't done automatically as a normal part of the application initialization sequence - it is only done if an application uses AppleScript or initializes the table itself.

The simplest way to load the scripting addition entries into the system Apple event handler table is to open a connection to the AppleScript component, as shown in Listing 1. In turn, this will load the scripting additions in the scripting additions folder and refresh the entries in the system Apple event dispatch table.

__Listing 1__  Opening a connection to the AppleScript component.

```
theComponent = OpenDefaultComponent(kOSAComponentType, typeAppleScript);
```

If your application runs or compiles AppleScript scripts, then you need to do this anyway, so simply be sure that AppleScript is initialized before your application invokes any scripting additions.

However, if your application is only interested in using the scripting additions, then initializing all of AppleScript will entail additional overhead that may not be warranted. So, if you would like to load the scripting additions without loading AppleScript, you can do so by having your application send itself a `kASAppleScriptSuite`/`kGetAEUT` Apple event.

Listing 2 shows the source code required to do this. Every time this routine is called, it will synchronize the set of loaded scripting additions with the contents of the scripting additions folder. Typically, you would only do this once, but calling it more than once would be useful if, for example, you want your application to install a new scripting addition and then use it without relaunching.

__Listing 2__  Sample routine for loading or updating scripting additions.

```
void LoadScriptingAdditions() {     OSErr err;     AppleEvent e, r;     ProcessSerialNumber selfPSN = { 0, kCurrentProcess };      #if MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_2     void (*f)();     CFBundleRef b;      /* First, call the routine that installs the kASAppleScriptSuite /        kGetAEUTApple event handler in your applications Apple event dispatch        table. This part is only required if your application is running in        Mac OS X 10.0 or 10.1. It is not necessary and will silently fail        anywhere else (such as when running in Classic or Mac OS 9). */      b = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.openscripting"));     if (b != NULL) {         f = (void (*)()) CFBundleGetFunctionPointerForName(b, CFSTR("OSAInstallStandardHandlers"));         if (f != NULL) (*f)();     }     #endif      /* Second, send ourselves a kASAppleScriptSuite / kGetAEUT        Apple event. This will load the scripting additions into our        application's system Apple event dispatch table - it will also        refresh the table so it is synchronized with the contents of        the scripting additions folder. */      err = AEBuildAppleEvent(kASAppleScriptSuite, kGetAEUT,         typeProcessSerialNumber, &selfPSN, sizeof(selfPSN),         kAutoGenerateReturnID, kAnyTransactionID, &e, NULL, "");     if (err == noErr) {         AESend(&e, &r, kAEWaitReply, kAENormalPriority, kAEDefaultTimeout, NULL, NULL);         AEDisposeDesc(&e);         AEDisposeDesc(&r);     } }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-05-06 | Document OSAInstallStandardHandlers as unnecessary in 10.2 and later. |
| 2001-09-13 | New document that explains how to load scripting additions so you can call them using Apple events. |

