---
title: Operation could not be completed. No such file or directory
apple_id: DTS40010279
resource_type: QA
platform: iOS
topic: Xcode
technology: null
published: '2010-08-31'
source_url: https://developer.apple.com/library/archive/qa/qa1711/_index.html
archived_at: '2026-07-18T02:34:18.755856Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1711

# Operation could not be completed. No such file or directory

## Q:  Xcode displays an "Operation could not be completed. No such file or directory" error message when I try to archive my application. How do I resolve this error?

A: When you run the Build and Archive command, Xcode 3.2.2 or later fetches your application binary and its associated `.dSYM` file and saves them in your home folder. The `.dSYM`, which contains symbol information that are useful for debugging and symbolizing crash reports, is created by setting the "Debug Information Format" build setting to `DWARF with dSYM File` and enabling the "Generate Debug Symbols" build setting in Xcode. You are getting the "Operation could not be completed. No such file or directory" error message because Xcode cannot find the `.dSYM` associated with your application. You may have set "Debug Information Format" to `Stabs` or `DWARF` or unwittingly unchecked "Generate Debug Symbols" in your project. As a result, Xcode did not create the `.dSYM`, which is one of the requirements for archiving your application.

Be sure to set "Debug Information Format" to `DWARF with dSYM File` and turn on "Generate Debug Symbols" in the Build pane of your Target as respectively shown in Figure 1 and Figure 2 to resolve this issue.

__Figure 1__  Debug Information Format set to DWARF with dSYM File in the Build pane of your Target.

!

__Figure 2__  Generate Debug Symbols turned on in the Build pane of your Target.

!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-08-31 | New document that describes how to resolve the "Operation could not be completed. No such file or directory" message in Xcode. |

