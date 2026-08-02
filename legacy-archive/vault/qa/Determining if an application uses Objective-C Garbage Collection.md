---
title: Determining if an application uses Objective-C Garbage Collection
apple_id: DTS40007967
resource_type: QA
platform: macOS
topic: General
technology: null
published: '2008-09-08'
source_url: https://developer.apple.com/library/archive/qa/qa1599/_index.html
archived_at: '2026-07-18T02:32:24.179012Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1599

# Determining if an application uses Objective-C Garbage Collection

## Q:  How can I tell if an Objective-C application has enabled Garbage Collection?

A: How can I tell if an Objective-C application has enabled Garbage Collection?

To programmatically test your application to see if garbage collection is enabled, check the class `NSGarbageCollector` for the presence of a `defaultCollector`. See Listing 1.

__Listing 1__  Programmatically determining if Garbage Collection is being used

```
 if ([NSGarbageCollector defaultCollector] != nil) {          /* the Garbage Collector is on */      } else {         /* retain/release/autorelease/dealloc are being utilized */     }
```

It may also be useful during debugging to set the environment variable `OBJC_PRINT_GC`=`YES`. When set to `YES`, this not only tells if garbage collection is on or off, but will dump the state of the collector for each Objective-C image. Look specifically for `"GC: is ON"` or `"GC: is OFF"`.

__For More Information__

See also [Introduction to Garbage Collection](../documentation/Cocoa/Garbage%20Collection%20Programming%20Guide/Introduction%20to%20Garbage%20Collection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytemrtfvbuuqshjfauorq) and [Garbage Collection API](../documentation/Cocoa/Garbage%20Collection%20Programming%20Guide/Garbage%20Collection%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinrxfvjvomi).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-08 | New document that shows how to determine if an application or executable is using Objective-C Garbage Collection. |

