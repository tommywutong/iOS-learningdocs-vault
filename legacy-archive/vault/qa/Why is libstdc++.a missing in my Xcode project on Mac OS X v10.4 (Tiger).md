---
title: Why is libstdc++.a missing in my Xcode project on Mac OS X v10.4 (Tiger)?
apple_id: DTS10003575
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2005-04-29'
source_url: https://developer.apple.com/library/archive/qa/qa1428/_index.html
archived_at: '2026-07-18T02:30:40.705348Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1428

# Why is libstdc++.a missing in my Xcode project on Mac OS X v10.4 (Tiger)?

## Q:  Why is libstdc++.a missing in my Xcode project on Mac OS X v10.4 (Tiger)?

A: Your project was built using an old Xcode template which was containing an explicit reference to libstdc++.a which is no longer needed.

What is libstdc++? libstdc++ is the C++ Standard Library providing functionality such as `cout`.

Who needs libstdc++? Only C++ developers using an old version, 2.95.2 or older, of gcc.

If you are not using C++ then you do not need to keep an explicit reference to libstdc++ in your project.

Even if you are using C++, if you are using gcc 3 or 4, you do not need to keep an explicit reference to libstdc++ in your project either. Starting with gcc 3, the compiler will automatically link with the appropriate version of libstdc++ (if you install the Cross-Development SDKs, you will see that libstdc++ is provided for gcc 2.95.2, gcc 3.1, gcc 3.3, and gcc 4.0). Furthermore, starting with gcc 4, it's no longer libstdc++.a which is linked with automatically by the compiler but libstdc++.dylib instead.

So, unless you are still using gcc 2.95.2, you should just remove the reference to libstdc++ from your project and it will build fine.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-04-29 | New document that explains the role of libstdc++ and why you do not need it in a Xcode project. |

