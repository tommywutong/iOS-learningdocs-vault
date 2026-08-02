---
title: Code signing fails with error 'resource fork, Finder information, or similar
  detritus not allowed'
apple_id: DTS40017555
resource_type: QA
platform: watchOS|tvOS|iOS|macOS
topic: Xcode
technology: null
published: '2016-10-10'
source_url: https://developer.apple.com/library/archive/qa/qa1940/_index.html
archived_at: '2026-07-18T02:37:25.055660Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1940

# Code signing fails with error 'resource fork, Finder information, or similar detritus not allowed'

## Q:  When I build my app, code signing fails with the error "resource fork, Finder information, or similar detritus not allowed." What does this mean and what should I do about it?

A: This is a security hardening change that was introduced with iOS 10, macOS Sierra, watchOS 3, and tvOS 10.

Code signing no longer allows any file in an app bundle to have an extended attribute containing a resource fork or Finder info.

To see which files are causing this error, run this command in Terminal:

`$ xattr -lr <path_to_app_bundle>`

replacing `<path_to_app_bundle>` with the path to your actual app bundle.

Here's an example of this command in action:


```
$ xattr -lr Foo.app
/Applications/Foo.app: com.apple.FinderInfo:
00000000  00 00 00 00 00 00 00 00 00 10 00 00 00 00 00 00  |................|
```

You can also remove all extended attributes from your app bundle with the xattr command:

`$ xattr -cr <path_to_app_bundle>`

Note that browsing files within a bundle with Finder's Show Package Contents command can cause Finder info to be added to those files. Otherwise, audit your build process to see where the extended attributes are being added.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-10-10 | New document that describes the cause of a new codesign error on iOS 10, macOS Sierra, watchOS 3, and tvOS 10. |

