---
title: Manual Code Signing for both iOS and tvOS
apple_id: DTS40017615
resource_type: QA
platform: iOS
topic: Xcode
technology: null
published: '2017-06-14'
source_url: https://developer.apple.com/library/archive/qa/qa1911/_index.html
archived_at: '2026-07-18T02:36:05.922328Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1911

# Manual Code Signing for both iOS and tvOS

## Q:  How can I code sign if automatic code signing is not an option?

A: Apple recommends that all developers use Xcode managed signing as described in the document [Technical Q&A QA1814: Setting up Xcode to automatically manage your provisioning profiles](https://developer.apple.com/library/ios/qa/qa1814/_index.html#//apple_ref/doc/uid/DTS40014030). With Xcode managed signing, Xcode is able to manage many of the settings related to code signing for you automatically including refreshing your provisioning profiles for you and automatically correcting many code signing problems that can occur.

These directions are for developers who have received a special purpose provisioning profile from Apple that must be explicitly selected. For example, you may need to use manual code signing when your App ID Prefix does not match your team Team ID and you have obtained a provisioning profile to account for that. Or, you may need to use manual code signing if your provisioning profile includes special entitlements.

For the majority of development projects manual code signing is not necessary. Unless you have specific reasons for requiring manual code signing, you should use automatic code signing by following the directions provided in [Technical Q&A QA1814: Setting up Xcode to automatically manage your provisioning profiles](https://developer.apple.com/library/ios/qa/qa1814/_index.html#//apple_ref/doc/uid/DTS40014030).

Manual code signing requires adjusting the provisioning profile build setting in Xcode. The provisioning profile build setting is displayed in the code signing sections of the general settings in your target's build settings as shown in the "Manually sign an app " section of the Xcode help documentation (see the [Manually sign an app - Xcode Help](http://help.apple.com/xcode/mac/current/#/dev1bf96f17e) section of the Xcode help documentation for directions).

In previous versions of Xcode, manual code signing could be achieved by selecting the specific provisioning profiles you would like to use for the debug and release versions of your app by manually selecting them in the code signing section of the build settings as shown in Figure 1 below.

__Figure 1__  The provisioning profile selections for manual code signing prior to Xcode 8.

!!

Here, the last two fields under provisioning profile should to be set to specific provisioning profiles. In Xcode 8 and later you can inspect these settings, but you should use the fields displayed in "[Manually sign an app - Xcode Help](http://help.apple.com/xcode/mac/current/#/dev1bf96f17e)" for adjusting which provisioning profiles you would like to use. You should leave all of the other settings at the default values.

- [Xcode Help](http://help.apple.com/xcode/mac/current/)
- The "Upgrade's application-identifier does not match the installed app" section in [Technical Q&A QA1814: Setting up Xcode to automatically manage your provisioning profiles](https://developer.apple.com/library/ios/technotes/tn2319/_index.html#//apple_ref/doc/uid/DTS40013778-CH1-ERRORMESSAGES-UPGRADE_S_APPLICATION_IDENTIFIER_DOES_NOT_MATCH_THE_INSTALLED_APP).
- [Technical Note TN2311: Managing Multiple App ID Prefixes](https://developer.apple.com/library/ios/technotes/tn2311/_index.html#//apple_ref/doc/uid/DTS40014135)
- [Technical Q&A QA1726: Resolving the Potential Loss of Keychain Access warning](https://developer.apple.com/library/ios/qa/qa1726/_index.html#//apple_ref/doc/uid/DTS40014942)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-06-14 | Replaced illustrations with a reference to the relevant section in the Xcode help documentation. |
| 2017-03-09 | New document that explains how to configure Xcode for manual code signing when Team ID based Code Signing isn’t an option. |

