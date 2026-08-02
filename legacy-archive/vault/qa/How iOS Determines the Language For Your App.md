---
title: How iOS Determines the Language For Your App
apple_id: DTS40014938
resource_type: QA
platform: iOS
topic: User Experience
technology: null
published: '2016-03-23'
source_url: https://developer.apple.com/library/archive/qa/qa1828/_index.html
archived_at: '2026-07-18T02:35:06.030924Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1828

# How iOS Determines the Language For Your App

## Q:  How does iOS determine the language for my app?

A: To determine the language for your app, iOS considers not only the order of the user language preferences (in `General` > `Language` `&` `Region` of the `Settings` application) but also the localizations your app declares it supports. Here is the detailed process:

1. iOS first looks up your user's most preferred language, which is the first entry in their language preferences.
2. It proceeds to check if that language is supported by your app. iOS searches your app bundle for an `.lproj` folder matching the preferred language. If the folder exists, iOS infers that your app has been localized for that language and chooses it for your app. Otherwise, iOS selects the next language in the user language preferences, then repeats the above check.

   The dialect support in iOS may slightly change the above behavior. If your user's preferred language is a regional variant that is not supported by your app, iOS will try to fall back to a more generic language before giving up. For example, if your user's preferred language is British English and your app bundle doesn't contain an `en-GB.lproj` or `en_GB.lproj` folder, iOS then searches your bundle for an `en.lproj` folder and chooses English for your app if the folder exists.
3. If none of the user’s preferred languages are supported by your app, iOS chooses the language matching your app's development region ([CFBundleDevelopmentRegion](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/TP40009249-130430-BAJJHDJH)).

Once the system has chosen a language for your app, the matching `.lproj` folder is used to locate the localized resources. If your app's UI or the system-provided UI components (such as text editing menus, UIDatePicker, UIImagePickerController and UILocalizedIndexedCollation) are displayed in a wrong language, make sure that your app contains all its supported languages' `.lproj` folders and that these folders are correctly named.

If your app manages the localized resources without using any `.lproj` folders, be sure to specify the supported languages with [CFBundleLocalizations](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-109552).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-03-23 | Fixed a broken link. |
| 2014-09-10 | New document that describes how iOS determines the language for your app. |

