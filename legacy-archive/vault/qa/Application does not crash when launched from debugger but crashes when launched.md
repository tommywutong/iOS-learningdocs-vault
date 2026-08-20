---
title: Application does not crash when launched from debugger but crashes when launched
  by user.
apple_id: DTS40008816
resource_type: QA
platform: iOS
topic: Performance
technology: null
published: '2009-05-22'
source_url: https://developer.apple.com/library/archive/qa/qa1592/_index.html
archived_at: '2026-07-18T02:32:21.867992Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1592

# Application does not crash when launched from debugger but crashes when launched by user.

## Q:  Why does my application crash during launch unless I run it from Xcode?

A: Why does my application crash during launch unless I run it from Xcode?

iPhone OS uses a watchdog timer when applications are launched. If an application takes too long to complete its initial startup, the operating system terminates the application. Applications terminated for this reason will have the exception code `0x8badf00d` and related information noted in the associated crash report:

__Listing 1__  Crash report excerpt.

```
Exception Type: 00000020 Exception Codes: 0x8badf00d Highlighted Thread: 0  Application Specific Information: com.yourcompany.yourapp failed to launch in time  elapsed total CPU time (seconds): 11.120 (user 1.840, system 9.280), 59% CPU  elapsed application CPU time (seconds): 2.160, 12% CPU
```

When Xcode launches an application, the watchdog timer is disabled to compensate for additional overhead that may be incurred when Xcode attaches the debugger. As a result, your application's long startup may initially escape your attention if you are exclusively testing by running from Xcode.

The best applications launch quickly, allowing the user to interact with the application as soon as possible. To provide a quality user experience, you should routinely evaluate and work to improve the launch time of your application. If considerable work must be done at launch, consider performing that work on a secondary thread and visually indicating the activity.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-05-22 | New document that describes how Xcode disables the standard iPhone OS watchdog timer for application launch. |

