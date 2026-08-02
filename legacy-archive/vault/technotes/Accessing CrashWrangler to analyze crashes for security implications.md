---
title: Accessing CrashWrangler to analyze crashes for security implications
apple_id: DTS40014171
resource_type: Technical Note
platform: macOS
topic: Security
technology: null
published: '2014-03-03'
source_url: https://developer.apple.com/library/archive/technotes/tn2334/_index.html
archived_at: '2026-07-26T19:54:13.755364Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2334

# Accessing CrashWrangler to analyze crashes for security implications

This Technical Note discusses how to download CrashWrangler, a tool that can be used to determine if a crash is an exploitable security issue.

[Downloading CrashWrangler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjxgewugsbrfvke4vcbi4yq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjxgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Downloading CrashWrangler

CrashWrangler is a set of developer tools that help in analyzing crashes on OS X. The tools work by inspecting the application's state at the time of the crash, as well as the application crash logs. Using these tools on a reproducible test case can determine if a crash could lead to a potentially exploitable security issue.

It should be understood that CrashWrangler uses advanced heuristics, but that false positives and false negatives are possible. It's intended for quick assessment. A detailed manual inspection is the only way to be sure something is or isn't exploitable.

You can download CrashWrangler by going to [https://developer.apple.com/downloads/index.action?name=CrashWrangler](https://developer.apple.com/downloads/index.action?name=CrashWrangler). This can be accessed with a free Registered Apple Developer account. Please see the README.txt file in the CrashWrangler download for instructions on how to use CrashWrangler and interpret its output.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-03 | New document that describes how to download CrashWrangler |

