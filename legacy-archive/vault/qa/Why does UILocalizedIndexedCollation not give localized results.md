---
title: Why does UILocalizedIndexedCollation not give localized results?
apple_id: DTS40011151
resource_type: QA
platform: iOS
topic: null
technology: UIKit
published: '2011-07-14'
source_url: https://developer.apple.com/library/archive/qa/qa1739/_index.html
archived_at: '2026-07-18T02:34:32.369479Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1739

# Why does UILocalizedIndexedCollation not give localized results?

## Q:  Why does `UILocalizedIndexedCollation` not give localized results for section titles?

A: To get localized results from `UILocalizedIndexedCollation`, your application bundle must also be properly localized.

`UILocalizedIndexedCollation` is a convenience class that provides table view section and section index titles useful for organizing and sorting table view data. A common set of sections provided by `UILocalizedIndexedCollation` are sections labeled "A" through "Z". If the device is set to use an alternate language, `UILocalizedIndexedCollation` can automatically provide a set of sections appropriate for that language. As an example, for Traditional Chinese, `UILocalizedIndexedCollation` will add a set of sections that correspond to the number of strokes for a particular Traditional Chinese character. `UILocalizedIndexedCollation` also provides a "#" section that serves as a default section for Roman numerals and any rows that do not get sorted into any other section.

Using `UILocalizedIndexedCollation` is straight-forward and described in the `UILocalizedIndexedCollation` class documentation. Note that you do not need any additional code to add support for localized `UILocalizedIndexedCollation` sections and section titles.

However, the localization data that `UILocalizedIndexedCollation` uses at run-time will be based on the localization that your application bundle is using. If your application only supports English, and the device is set to use Traditional Chinese, `UILocalizedIndexedCollation` will only show English section titles and sort rows into the "A" through "Z" and "#" sections, even though `UILocalizedIndexedCollation` is capable of providing Traditional Chinese section titles and sorting row data into these sections.

To address this, your application bundle must properly declare support for the languages you want `UILocalizedIndexedCollation` to support. You can add localizations to your application bundle either by adding the appropriate `.lproj` folders, or by specifying supported localizations in your CFBundleLocalizations key in your application's `info.plist` file. Note that the former approach is preferred, as it easier to maintain if localized resources need to be added to your application in the future. Localizing your application is described in more detail in the Internationalization documentation linked below.

See also: _[UILocalizedIndexedCollation Class Reference](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation)_, _[Internationalization and Localization Guide](../documentation/Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_ documentation

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-14 | New document that provides a solution for a common problem when using UILocalizedIndexedCollation |

