---
title: Embedding Content with Swift in Objective-C
apple_id: DTS40014995
resource_type: QA
platform: watchOS|iOS|Xcode Developer Tools
topic: Xcode
technology: null
published: '2014-10-07'
source_url: https://developer.apple.com/library/archive/qa/qa1881/_index.html
archived_at: '2026-07-18T02:35:12.029050Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1881

# Embedding Content with Swift in Objective-C

## Q:  How do I embed content with Swift in an Objective-C app?

A: Swift standard libraries are copied into a bundle if and only if you are building an application and this application contains Swift source files by itself. You can check whether a product such as a framework includes Swift source files by running `otool -L` on its executable in the Terminal. This command displays all shared libraries and frameworks that your product dynamically links against. Your product uses Swift if any of the Swift libraries appear among the result of `otool -L` as shown in Figure 1.

__Figure 1__  Running otool -L on MyFramework that contains Swift source files

!!

If you are building an app that does not use Swift but embeds content such as a framework that does, Xcode will not include these libraries in your app. As a result, your app will crash upon launching with an error message looking as follows:


```
dyld: Library not loaded: @rpath/libswiftCoreGraphics.dylib
  Referenced from: /private/var/mobile/Containers/Bundle/Application/696F0EAD-E2A6-4C83-876F-07E3D015D167/<Your_App>.app/Frameworks/<Framework_Name>.framework/<Framework_Name>
  Reason: image not found
```

where <Your_App> and <Framework_Name> are respectively your app and the framework being embedded in your app.

To workaround this issue, set the `Embedded Content Contains Swift Code (EMBEDDED_CONTENT_CONTAINS_SWIFT)` build setting to YES in your app as shown in Figure 2. This build setting, which specifies whether a target's product has embedded content with Swift code, tells Xcode to embed Swift standard libraries in your app when set to `YES`.

__Figure 2__  Setting Embedded Content Contains Swift Code to YES

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-10-07 | New document that describes how to embed content with Swift in an Objective-C app. |

