---
title: Accessing Shared Data from an App Extension and its Containing App
apple_id: DTS40014939
resource_type: Technical Note
platform: iOS
topic: Data Management
technology: null
published: '2015-05-11'
source_url: https://developer.apple.com/library/archive/technotes/tn2408/_index.html
archived_at: '2026-07-26T19:54:14.841696Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2408

# Accessing Shared Data from an App Extension and its Containing App

Explains file coordination issues when used by an app extension to access a container shared with its containing app.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojthewugsbrfvke4vcbi4yq)[File Coordination and Shared Containers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojthewugsbrfvke4vcbi4za)[Solutions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojthewugsbrfvke4vcbi4zq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojthewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Using file coordination in an app extension to access a container shared with its containing app may result in a deadlock in iOS versions 8.1.x and earlier. This is usually the case if a process is suspended mid coordinated I/O. This can be more prevalent on iOS where most apps will be suspended after a short period of time after being moved to the background. Extensions should use alternatives to file coordination. This has since been resolved in iOS 8.2.

__Important:__ When you create a shared container for use by an app extension and its containing app in iOS 8.0 or later, you are obliged to write to that container in a coordinated manner to avoid data corruption. However, you must not use file coordination APIs directly for this in iOS 8.1.x and earlier. If you use file coordination APIs directly to access a shared container from an extension in iOS 8.1.x and earlier, there are certain circumstances under which the file coordination machinery deadlocks.

Instead, use CFPreferences, atomic safe save operations on flat files, SQLite or Core Data.

[Back to Top](#)

## File Coordination and Shared Containers

File coordination does not have a mechanism for handling process suspensions. On iOS, processes can be suspended as part of jetsam and process management. On OS X, this only happens in the debugger. The recommended practice on iOS 7, and for applications in general, is to handle the UIApplication notifications that the app has been backgrounded and cancel coordinated actions and remove file presenters. When the app is brought back to the foreground, the file presenters can be re-added. Extensions do not get UIApplication backgrounding notifications and cannot do that. Extensions also cannot take additional background task assertions, so they cannot avoid being suspended like applications.

[Back to Top](#)

## Solutions

You can use CFPreferences, atomic safe save operations on flat files, or SQLite or Core Data to share data in a group container between multiple processes even if one is suspended mid transaction. For SQLite/Core Data, processes using databases in DELETE journal mode will be instantly killed instead of suspended. Processes using database in WAL journal mode will only be jetsam'd if they attempt to hold a write transaction open at the time of suspension. Posix file locks also work, and behave similarly to SQLite database in DELETE journal mode, so open(O_EXLOCK) or flock() could also be used.

Regardless of this issue, the containing app (and all applications) should properly use background task assertions around file operations they require completed in a shared container (with or without extensions). This includes all writes or deletions. Such a process might still be killed by jetsam but at a much lower frequency.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-05-11 | Updated to indicate workarounds only apply to iOS 8.1 and earlier, issue resolved in iOS 8.2 and later. |
| 2014-09-10 | New document that explains file coordination issues when used by an app extension to access a container shared with its containing app. |

