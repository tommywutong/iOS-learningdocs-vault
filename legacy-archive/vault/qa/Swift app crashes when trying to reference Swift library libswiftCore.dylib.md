---
title: Swift app crashes when trying to reference Swift library libswiftCore.dylib.
apple_id: DTS40015165
resource_type: QA
platform: iOS
topic: Xcode
technology: IOKit
published: '2015-02-17'
source_url: https://developer.apple.com/library/archive/qa/qa1886/_index.html
archived_at: '2026-07-18T02:35:23.118680Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1886

# Swift app crashes when trying to reference Swift library libswiftCore.dylib.

## Q:  What can I do about the libswiftCore.dylib loading error in my device's console that happens when I try to run my Swift language app?

A: To correct this problem, you will need to sign your app using code signing certificates with the Subject Organizational Unit (OU) set to your Team ID. All Enterprise and standard iOS developer certificates that are created after iOS 8 was released have the new Team ID field in the proper place to allow Swift language apps to run.

Usually this error appears in the device's console log with a message similar to one of the following:


```
 [....] [deny-mmap] mapped file has no team identifier and is not a platform binary:
/private/var/mobile/Containers/Bundle/Application/5D8FB2F7-1083-4564-94B2-0CB7DC75C9D1/YourAppNameHere.app/Frameworks/libswiftCore.dylib
```



```
Dyld Error Message:
  Library not loaded: @rpath/libswiftCore.dylib
```

The new certificates are needed when building an archive and packaging your app. Even if you have one of the new certificates, just resigning an existing swift app archive won’t work. If it was built with a pre-iOS 8 certificate, you will need to build another archive.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-02-17 | New document that talks about the how to update your certificates for Swift apps |

