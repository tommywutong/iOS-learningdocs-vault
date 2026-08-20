---
title: How can I identify the runtime environment, Carbon or Cocoa, of the current
  application?
apple_id: DTS10004141
resource_type: QA
platform: macOS
topic: General
technology: null
published: '2010-03-19'
source_url: https://developer.apple.com/library/archive/qa/qa1372/_index.html
archived_at: '2026-07-18T02:30:27.359337Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1372

# How can I identify the runtime environment, Carbon or Cocoa, of the current application?

## Q:  How can I identify the runtime environment, Carbon or Cocoa, of the current application?

A: You can identify the runtime environment of the current application by calling the `ProcessInformationCopyDictionary` API (in Processes.h) and examining the value of the "Flavor" key. This API is supported in Mac OS X v10.2 and later.

This is helpful if you're developing plugins, frameworks, input methods, static libraries, etc, when you will not always know in which runtime environment, Carbon, Cocoa, or even Mac OS Classic, your code is going to run. Most of the time, you would not care about this runtime environment but if you handle User Interface elements, some situations may arise when knowing the runtime environment would simplify the code writing.

For convenience, you can use the following function which returns the flavor of the running application:

__Listing 1__  GetApplicationFlavor.

```
SInt32 GetApplicationFlavor(void)
{
  // GetApplicationFlavor returns:
  // -1 if the application flavor could not be identified
  //      0 if the application is a Mac OS Classic application
  //      2 if the application is a Carbon application
  //      3 if the application is a Cocoa application

  static SInt32 flavor = -1;
  OSStatus status;
  CFDictionaryRef processInfoDict = NULL;
  CFNumberRef processInfoFlavor = NULL;

  if (flavor == -1)
  {
    ProcessSerialNumber psn;
    status = GetCurrentProcess(&psn);
    require_noerr(status, GetCurrentProcess);

    processInfoDict = ProcessInformationCopyDictionary(&psn, kProcessDictionaryIncludeAllInformationMask);
    require(processInfoDict != NULL, ProcessInformationCopyDictionary);

    processInfoFlavor = CFDictionaryGetValue(processInfoDict, CFSTR("Flavor"));
    require(processInfoFlavor != NULL, CFDictionaryGetValue);

    CFNumberGetValue(processInfoFlavor, kCFNumberSInt32Type, &flavor);
  }

CFDictionaryGetValue:
ProcessInformationCopyDictionary:
GetCurrentProcess:

  if (processInfoFlavor != NULL)
    CFRelease(processInfoFlavor);
  if (processInfoDict != NULL)
    CFRelease(processInfoDict);

  return flavor;
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-03-19 | Removed the reference to bug (Radar #3823210) which has been closed, and original sample code description is correct. |
| 2006-11-07 | New document that identifies the runtime environment of the application. Useful only for plugins, frameworks, input methods, etc. |

