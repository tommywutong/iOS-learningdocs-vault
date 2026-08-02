---
title: Understanding Memory Usage Limits for WatchKit Apps and Extensions
apple_id: DTS40016206
resource_type: QA
platform: iOS
topic: Performance
technology: WatchKit
published: '2015-05-23'
source_url: https://developer.apple.com/library/archive/qa/qa1894/_index.html
archived_at: '2026-07-27T06:57:05.411343Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1894

# Understanding Memory Usage Limits for WatchKit Apps and Extensions

## Q:  What are the memory limits imposed on my WatchKit App and Extension?

A: The WatchKit app running on the Apple Watch has a soft memory limit while it is in the foreground which transitions to a hard limit when the WatchKit App is suspended. This means that a memory heavy WatchKit app may be terminated once the user lowers their wrist. When a WatchKit app is terminated in response to memory pressure, a log similar to Listing 1 is sent to the paired iPhone. Crash and low-memory logs originating from the Watch will have a value for the __Hardware Model__ field beginning with __Watch__. Because the WatchKit app does not contain code, excess memory consumption by the WatchKit app is caused by displaying many images simultaneously (including animations with many frames).

WatchKit extensions always run under a hard memory limit. If the extension's memory usage exceeds this limit, it is likely to be terminated and a low-memory log similar to Listing 1 generated.

Both limits are not documented because they can change, and designing to a specific memory number is not the most efficient way to use the resources on Apple Watch. Rather, focus on ensuring that your app and extension are using resources in the most efficient way that provides the most value for your customers. For WatchKit apps, ensure that all images are properly sized for the Watch, reduce the number of frames in animations, and limit the number of images shown by individual interface controllers. For WatchKit extensions, profile your extension using Instruments to locate the sources of excess memory consumption. See [Locating Memory Issues in Your App](https://developer.apple.com/library/ios/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/MemoryManagementforYourApp/MemoryManagementforYourApp.html#//apple_ref/doc/uid/TP40004652-CH11-SW1) in the Instruments User Guide.

__Listing 1__  A low-memory report for a termination caused by excess memory usage over the imposed limit will list 'per-process-limit' under the reason column for the terminated process.

```
Incident Identifier: 09EDB127-9EC9-42EA-A3A9-05348E48BE95
CrashReporter Key: 6196484647b3431a9bc2833c19422539549f3dbe
Hardware Model: iPhone6,1
OS Version: iPhone OS 8.3 (12F70)
Kernel Version: Darwin Kernel Version 14.0.0: Sun Mar 29 19:47:37 PDT 2015; root:xnu-2784.20.34~2/RELEASE_ARM64_S5L8960X
Date: 2015-05-01 11:13:20 -0700
Time since snapshot: 41 ms

Free pages: 9751
Active pages: 106918
Inactive pages: 45823
Speculative pages: 7919
Throttled pages: 0
Purgeable pages: 834
Wired pages: 48667
File-backed pages: 65304
Anonymous pages: 95356
Compressions: 2060698
Decompressions: 1077195
Compressor Size: 44450
Uncompressed Pages in Compressor: 115952
Page Size: 16384
Largest process: Maps

Processes
     Name       | <UUID> |     CPU Time|     rpages|       purgeable| recent_max| lifetime_max| fds | [reason] | (state)
...
WatchKit Catalog WatchKit Extension <2ccb94f29239352189cb94a831218c95> 0.248        4255                0 - 5597   50 [per-process-limit] (frontmost)
...
```

A resource log similar to Listing 2 may also be generated indicating that the process crossed its memory limit.

__Listing 2__  A resource log generated for excess memory usage over the imposed limit will contain an Exception Type of EXC_RESOURCE and an exception subtype of MEMORY.

```
Incident Identifier: 5B8739E0-805D-411B-9C98-1843E7671C9E
CrashReporter Key: b703c9cd4a7c86504a7ee2a9ea35c4c7544e24dd
Hardware Model: iPhone7,2
Process: WatchKit Catalog [552]
Path: /private/var/mobile/Containers/Bundle/Application/0BDF0200-3DFF-452D-91BC-986C0FEC9ED9/WatchKit Catalog.app/PlugIns/WatchKit Catalog WatchKit Extension.appex/ WatchKit Catalog WatchKit Extension
Identifier: WatchKit Catalog WatchKit Extension
Version: ???
Code Type: ARM-64 (Native)
Parent Process: launchd [1]

Date/Time: 2015-04-27 17:04:21.380 -0700
Launch Time: 2015-04-27 15:06:50.343 -0700
OS Version: iOS 8.3 (12F70)
Report Version: 105

Exception Type: EXC_RESOURCE
Exception Subtype: MEMORY
Exception Message: Crossed High Water Mark
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-05-23 | New document that discusses memory limits on WatchKit Apps and Extensions and how to resolve terminations caused by exceeding those limits. |
