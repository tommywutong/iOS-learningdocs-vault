---
title: Obtaining the localized application name in Cocoa
apple_id: DTS10004442
resource_type: QA
platform: macOS
topic: User Experience
technology: Foundation
published: '2017-06-14'
source_url: https://developer.apple.com/library/archive/qa/qa1544/_index.html
archived_at: '2026-07-18T02:32:15.801771Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1544

# Obtaining the localized application name in Cocoa

## Q:  How can I get the localized name of my Cocoa application?

A: There are several different versions of the application name, all of which are readily available as an `NSString`. Depending on what you need, you can use one of the following approaches.

Use the [kCFBundleNameKey](https://developer.apple.com/reference/corefoundation/kcfbundlenamekey) key, which specifies your application's bundle name. It is your app's canonical short name and is used by the About window and main menu. Add this key to your `InfoPlist.strings` file before attempting to use it as shown in Listing 1. See [Localizing Property List Values](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/AboutInformationPropertyListFiles.html#//apple_ref/doc/uid/TP40009254-102276) for more information about `InfoPlist.strings` files.

__Listing 1__  Obtaining the application's bundle name using kCFBundleNameKey.

```
NSString *name = [NSBundle mainBundle].localizedInfoDictionary[(NSString *)kCFBundleNameKey];
```


Use the [CFBundleDisplayName](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-110725) key, which specifies your app's display name. It is typically longer and is used by the Finder to display the bundle. Add this key to your `InfoPlist.strings` file before attempting to use it as shown in Listing 2.

__Listing 2__  Obtaining the application's bundle display name using CFBundleDisplayName.

```
NSString *name = [NSBundle mainBundle].localizedInfoDictionary[@"CFBundleDisplayName"];
```


Use `NSProcessInfo`' s [processName](https://developer.apple.com/reference/foundation/nsprocessinfo/1416428-processname?language=objc) to fetch the name of your process.

__Listing 3__   Acquiring the process name using NSProcessInfo.

```
 NSString *name = [NSProcessInfo processInfo].processName;
```


Use `NSRunningApplication`'s [localizedName](https://developer.apple.com/reference/appkit/nsrunningapplication/1526751-localizedname?language=objc) to fetch your app's localized name. This approach returns the localized value of `CFBundleDisplayName` if it exists, falls back on the value of `CFBundleName` otherwise.

__Listing 4__  Obtaining the localized app name using NSRunningApplication.

```
NSString *name = [NSRunningApplication currentApplication].localizedName;
```


The better approach is to use `NSFileManager`'s [displayNameAtPath:](https://developer.apple.com/reference/foundation/nsfilemanager/1409751-displaynameatpath?language=objc) method that will return the localized display name if it exists, fall back on the bundle name if it does not, and will even reflect a renaming of the application by the user. See [Files and Directories Can Have Alternate Names](https://developer.apple.com/library/content/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html#//apple_ref/doc/uid/TP40010672-CH2-SW10) for more information.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-06-14 | Editorial update. |
| 2009-10-27 | Fixed typo in code listing 5. Added information about NSRunningApplication for Snow Leopard (code listing 4) |
| 2007-09-21 | New document that describes how to obtain several versions of the application name in Cocoa. |

