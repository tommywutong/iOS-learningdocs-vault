---
title: Help Book Caching During Software Development
apple_id: DTS10003497
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2005-03-30'
source_url: https://developer.apple.com/library/archive/qa/qa1409/_index.html
archived_at: '2026-07-18T02:30:32.005661Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1409

# Help Book Caching During Software Development

## Q:  While developing my application, Help Viewer suddenly stopped displaying the help content. I confirmed that my content is inside my bundle, and the necessary property list keys are set. What's wrong?

A: While developing my application, Help Viewer suddenly stopped displaying the help content. I confirmed that my content is inside my bundle, and the necessary property list keys are set. What's wrong?

In development situations, it is not unusual for an Xcode project or built product to be moved around on the filesystem frequently. If this happens, the Help Viewer will load up with the assumption that the content is in place because there is an entry for your help content both in its cache, and in the Help Viewer preferences located at `~/Library/Preferences/com.apple.help.plist`. If the content files are no longer where the cache says they are, it is possible for Help Viewer to simply display nothing on Mac OS X 10.3 and earlier.

This is not a common occurence, but it is possible in development situations if multiple copies of a given project exist in different places, or if entirely different projects specify the same `CFBundleHelpBookName`. Deployment situations, where a single copy of an application is installed, and likely not moved, are much less prone to this problem.

If you find yourself in this situation, it can most likely be solved by deleting the `~/Library/Caches/com.apple.helpui` folder, which contains the most recent Help Viewer cache information. The next time HelpViewer is launched, a new cache will be constructed using the information taken from the preferences, which should be up-to-date, since it is revised every time a given application is launched.

Developers receiving similar reports from end-users can refer them to [Mac OS X: Can't access Help content, or content is blank or missing links](http://docs.info.apple.com/article.html?artnum=25667), from the Apple support website.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-03-30 | New document that development situations that can potentially confuse Help Viewer |

