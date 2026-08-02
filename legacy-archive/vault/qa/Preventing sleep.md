---
title: Preventing sleep
apple_id: DTS10003426
resource_type: QA
platform: macOS
topic: General
technology: CoreServices
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/qa/qa1160/_index.html
archived_at: '2026-07-18T02:29:59.672300Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1160

# Preventing sleep

## Q:  How can I prevent system sleep while my application is running?

A: Most applications should not prevent system sleep, however, there are exceptions. For example, if your application is playing a long movie or slideshow, the user will probably get annoyed if the computer keeps going to sleep. Your application can prevent system sleep by calling `UpdateSystemActivity` once every 30 seconds. The following code shows how to create a `CFRunLoopTimer` that calls `UpdateSystemActivity` every 30 seconds.

__Listing 1__  Example usage of `UpdateSystemActivity`.

```c
#include <CoreServices/CoreServices.h>

void
MyTimerCallback(CFRunLoopTimerRef timer, void *info)
{
    UpdateSystemActivity(OverallAct);
}


int
main (int argc, const char * argv[])
{
    CFRunLoopTimerRef timer;
    CFRunLoopTimerContext context = { 0, NULL, NULL, NULL, NULL };

    timer = CFRunLoopTimerCreate(NULL, CFAbsoluteTimeGetCurrent(), 30, 0, 0, MyTimerCallback, &context);
    if (timer != NULL); {
        CFRunLoopAddTimer(CFRunLoopGetCurrent(), timer, kCFRunLoopCommonModes);
    }

    /* Start the run loop to receive timer callbacks. You don't need to
    call this if you already have a Carbon or Cocoa EventLoop running. */
    CFRunLoopRun();

    CFRunLoopTimerInvalidate(timer);
    CFRelease(timer);

    return (0);
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-06-04 | Moved to Retired Documents Library. |
| 2004-10-22 | Explains how your application can prevent the system from sleeping. |
|  | Explains how your application can prevent the system from sleeping. |

