---
title: Why is my code acting differently when I debug with Zombies?
apple_id: DTS40012620
resource_type: QA
platform: iOS|Xcode Developer Tools|macOS
topic: General
technology: null
published: '2012-08-06'
source_url: https://developer.apple.com/library/archive/qa/qa1758/_index.html
archived_at: '2026-07-18T02:34:35.803567Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1758

# Why is my code acting differently when I debug with Zombies?

## Q:  Why is my code acting differently when I debug with Zombies?

A: Enabling the Zombies debugging facility had side effects that changed the behavior of ARC code on some operating systems. Both iOS and OS X apps are effected. This has been fixed in iOS 6 or later and has been fixed in OS X 10.8 or later.

Prior to iOS 6 / OS X 10.8, using the [the Zombies instrument](https://developer.apple.com/library/ios/recipes/instruments_help-memory-allocations-help/Eliminating_Messages_To_Deallocated_Objects/06_Eliminating_Messages_To_Deallocated_Objects.html) or [NSZombieEnabled](https://developer.apple.com/library/ios/technotes/tn2239/_index.html#//apple_ref/doc/uid/DTS40010638-CH1-SUBSUBSECTION23) or the "Enable Zombie Objects" [Xcode diagnostic](https://developer.apple.com/library/ios/recipes/xcode_help-scheme_editor/Articles/SchemeDiagnostics.html), prevented ARC from "cleaning up" instance variables at deallocation-time. Your `-dealloc` methods would still be run, however any instance variables that you didn't explicitly set to `nil` would be untouched. If an instance variable strongly referenced an object, then that object would be kept alive forever by the abandoned instance variable.

For this reason, you are __strongly__ encouraged to run your app on an iOS 6+, or OS X 10.8+, system when debugging with Zombies.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-08-06 | New document that describes interactions of the Zombie debugging facility with Automatic Reference Counting (ARC) in some versions of iOS and OS X. |

