---
title: Determining console user login status
apple_id: DTS10001680
resource_type: QA
platform: macOS
topic: Data Management
technology: SystemConfiguration
published: '2008-04-14'
source_url: https://developer.apple.com/library/archive/qa/qa1133/_index.html
archived_at: '2026-07-18T02:29:55.996509Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1133

# Determining console user login status

## Q:  How do I tell whether a console user is currently logged in?

A: How do I tell whether a console user is currently logged in?

It really depends on what you mean by "currently logged in". With the introduction of fast user switching in Mac OS X 10.3, multiple users can be logged into the system at the same time. So, you have to split the question in two:

1. How do I get a list of GUI login sessions?
2. Which GUI login session, if any, is currently using the console?

These are clear questions with clear answers (see below). However, it's likely that, if you're asking these questions, you need to rethink your architecture.

One of the fundamental design principles of the Mac OS X is that high-level services can depend on low-level services, but not the other way around. For example, it's fine for an application to depend on the kernel, but it's a problem if the kernel depends on an application.

The question of determining the current console user typically arises when you break this design principle. Only application-level services should care whether a user's session is currently active on the console, and it's easy for such services to [determine that](https://developer.apple.com/documentation/MacOSX/Conceptual/BPMultipleUsers/BPMultipleUsers.html). On the other hand, a daemon should not be concerned about whether a user is logged in on the console, and thus it's tricky to get this information from that context.

This issue is discussed in great depth in [Technical Note TN2083, 'Daemons and Agents'](https://developer.apple.com/technotes/tn2005/tn2083.html) and, specifically, in the "Design Considerations" section of that technote. So, before you read the rest of this document, I strongly recommend that you read that technote and think about how you can align your architecture with the overall Mac OS X architecture.

- It assumes that the computer has a single GUI console. While that's true currently, it may not be true forever. If you use this technique you will have to change your code if this situation changes.
- It has no way of indicating that multiple users are logged in.
- It has no way of indicating that a user is logged in but has switched to the login window.

Because of these issues, routines like `SCDynamicStoreCopyConsoleUser` exist only for compatibility purposes. It's likely that they will be formally deprecated in a future version of Mac OS X.

If you choose to ignore all of the warnings above, here are the answers to your questions:

1. How do I get a list of GUI login sessions? — In Mac OS X 10.5 and later you can use the utmpx API to get this information. For an example of this, see [Sample Code 'UTXplorer'](https://developer.apple.com/samplecode/UTXplorer/index.html).

   Prior to Mac OS X 10.5 there was no supported way to get this information directly. [Technical Note TN2083, 'Daemons and Agents'](https://developer.apple.com/technotes/tn2005/tn2083.html) suggests an indirect way to do it, based a central daemon with a set of cooperating agents. This design will work on all versions of Mac OS X and is generally aligned with the overall Mac OS X design principle described earlier.
2. Which GUI login session, if any, is currently using the console? — This is answered below.

You can get the user name of the current console user by calling the `SCDynamicStoreCopyConsoleUser` function (from the System Configuration framework). Listing 1 shows how to do this.

__Listing 1__  Getting the current console user

```
static CFStringRef CopyCurrentConsoleUsername(SCDynamicStoreRef store)     // Returns the name of the current console user, or NULL if there is      // none. store may be NULL, in which case a transient dynamic store      // session is used. {     CFStringRef result;      result = SCDynamicStoreCopyConsoleUser(store, NULL, NULL);      // If the current console user is "loginwindow", treat that as equivalent      // to none.      if ( (result != NULL) && CFEqual(result, CFSTR("loginwindow")) ) {         CFRelease(result);         result = NULL;     }      return result; }
```

The System Configuration framework also makes it easy to be notified when this setting changes. Listing 2 shows how to do that.

__Listing 2__  Discovering when that setting changes

```c
#include <assert.h>  #include <SystemConfiguration/SystemConfiguration.h>  static CFStringRef CopyCurrentConsoleUsername(SCDynamicStoreRef store);     // defined above  static CFStringRef gCurrentConsoleUser;  static void MyNotificationProc(     SCDynamicStoreRef	store,     CFArrayRef          changedKeys,     void *              info )     // Called out of our runloop when the current console user value      // changes in the dynamic store. It's possible to get multiple      // redundant notifications, so we debounce the notification by checking      // for changes relative to gCurrentConsoleUser. {     #pragma unused(changedKeys)     #pragma unused(info)     CFStringRef         currentConsoleUser;     Boolean             didChange;      // Get the current console user.      currentConsoleUser = CopyCurrentConsoleUsername(store);      // See if it changed.      didChange = (gCurrentConsoleUser != NULL) != (currentConsoleUser != NULL);     if ( ! didChange && (gCurrentConsoleUser != NULL) ) {         assert(currentConsoleUser != NULL); // because if it was NULL,                                              // didChange would already be true         didChange = ! CFEqual(gCurrentConsoleUser, currentConsoleUser);     }      // If it did, log that fact and remember the current value.      if (didChange) {         if (gCurrentConsoleUser != NULL) {             CFRelease(gCurrentConsoleUser);         }         gCurrentConsoleUser = currentConsoleUser;         if (gCurrentConsoleUser != NULL) {             CFRetain(gCurrentConsoleUser);         }          CFShow(gCurrentConsoleUser);     } }  int main(int argc, char **argv) {     #pragma unused(argc)     #pragma unused(argv)     Boolean             success;     SCDynamicStoreRef   store;     CFStringRef         key;     CFArrayRef          keys;     CFRunLoopSourceRef  rls;      // Set up our connection to the dynamic store so that notifications are      // delivered by calling MyNotificationProc.      store = SCDynamicStoreCreate(         NULL,          CFSTR("com.apple.dts.ConsoleUser"),          MyNotificationProc,          NULL     );     assert(store != NULL);      // Set it up to notify us when the console user value changes.      key = SCDynamicStoreKeyCreateConsoleUser(NULL);     assert(key != NULL);      keys = CFArrayCreate(NULL, (const void **) &key, 1, &kCFTypeArrayCallBacks);     assert(keys != NULL);      success = SCDynamicStoreSetNotificationKeys(store, keys, NULL);     assert(success);      // Add it to the runloop.      rls = SCDynamicStoreCreateRunLoopSource(NULL, store, 0);     assert(rls != NULL);      CFRunLoopAddSource(CFRunLoopGetCurrent(), rls, kCFRunLoopDefaultMode);      // Print the current value.      gCurrentConsoleUser = CopyCurrentConsoleUsername(store);     CFShow(gCurrentConsoleUser);      // Run forever printing any changes.      CFRunLoopRun();      // Clean up code. This simple tool will never execute this code      // (because CFRunLoopRun will never return), but I've left it here      // in case you adapt the code for a more complex situation.      if (gCurrentConsoleUser != NULL) {         CFRelease(gCurrentConsoleUser);     }     CFRunLoopSourceInvalidate(rls);     CFRelease(rls);     CFRelease(keys);     CFRelease(key);     CFRelease(store);      return EXIT_SUCCESS; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-04-14 | A complete rewrite to account for fast user switching, and to simplify the code. |
| 2002-04-08 | New document that how to determine whether a user is logged in on the console, and be notified of changes. |

