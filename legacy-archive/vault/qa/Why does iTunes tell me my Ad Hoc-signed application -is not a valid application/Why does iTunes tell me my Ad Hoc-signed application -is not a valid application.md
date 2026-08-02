---
title: Why does iTunes tell me my Ad Hoc-signed application "is not a valid application"?
apple_id: DTS40008827
resource_type: QA
platform: iOS
topic: General
technology: null
published: '2009-05-26'
source_url: https://developer.apple.com/library/archive/qa/qa1640/_index.html
archived_at: '2026-07-18T02:33:02.981936Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1640

# Why does iTunes tell me my Ad Hoc-signed application "is not a valid application"?

## Q:  Why does iTunes tell me my Ad Hoc-signed application "is not a valid application"?

A: If you get the error message "The application "<applicationName>.app" could not be added to your iTunes library because it is not a valid application." (Figure 1) when installing an Ad Hoc distribution version of an iPhone application via iTunes, it's likely that the application's `Info.plist` is missing one or more required keys.

__Figure 1__  'Not a valid application' error from iTunes.

!

These required keys are:

- __Bundle identifier__ (`CFBundleIdentifier`, default value: `com.yourcompany.${PRODUCT_NAME:identifier}`)
- __Bundle version__ (`CFBundleVersion`, default value: `1.0`)
- __Bundle name__ (`CFBundleName`, default value: `${PRODUCT_NAME}`)

These keys are part of the default `Info.plist`, and may have been accidentally deleted. Add them back to your `Info.plist` and do a clean build of your project, then try the installation again. You add keys to your `Info.plist` in Xcode by selecting any line in the `Info.plist`, clicking the plus (+) button, and selecting the appropriate item (see Figure 2).

__Figure 2__  Adding the 'Bundle Version' key to Info.plist.

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-06 | First Version |
| 2009-05-26 | New document that provides the Info.plist keys which must be present for an iPhone application to be considered "valid". |

