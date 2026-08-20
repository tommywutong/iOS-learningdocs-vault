---
title: icon dimensions (0x0) don't meet the size requirements.
apple_id: DTS40011744
resource_type: QA
platform: iOS
topic: Languages & Utilities
technology: null
published: '2012-02-13'
source_url: https://developer.apple.com/library/archive/qa/qa1762/_index.html
archived_at: '2026-07-18T02:34:39.843982Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1762

# icon dimensions (0x0) don't meet the size requirements.

## Q:  My app fails validation on icon size requirements but the icon(s) appear to be correct, how do I resolve it?

A: The following error messages are the result of a developer tools issue with validating app icons.


```
iPhone/iPod Touch: Icon.png: icon dimensions (0x0) don't meet the size requirements. The icon file must be 57x57 pixels, in .png format

iPad: Icon.png: icon dimensions (0x0) don't meet the size requirements. The icon file must be 72x72 pixels, in .png format
```

The solution is to download and install the latest version of [Application Loader](https://itunesconnect.apple.com/apploader/ApplicationLoader_2.5.1.dmg), restart Xcode and then reattempt your submission. In most cases, this will fix the problem with Xcode's validation process.

If the error message persists, submit the app using Application Loader. For Application Loader usage, see the section titled "Using Application Loader" within the [iTunes Connect Developer Guide](https://itunesconnect.apple.com/docs/iTunesConnect_DeveloperGuide.pdf).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-02-13 | Added the step of restarting Xcode. |
| 2012-02-07 | New document that addresses a developer tools issue regarding mistaken failed icon validation |

