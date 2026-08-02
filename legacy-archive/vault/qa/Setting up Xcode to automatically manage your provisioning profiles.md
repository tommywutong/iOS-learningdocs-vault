---
title: Setting up Xcode to automatically manage your provisioning profiles
apple_id: DTS40014030
resource_type: QA
platform: iOS|Xcode Developer Tools|macOS
topic: General
technology: AppKit
published: '2017-06-14'
source_url: https://developer.apple.com/library/archive/qa/qa1814/_index.html
archived_at: '2026-07-18T02:34:55.881157Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1814

# Setting up Xcode to automatically manage your provisioning profiles

## Q:  How do I configure my Xcode project to use automatic provisioning?

A: Apple recommends using automatic code signing for both app development and app distribution. Automatic code signing is recommended for signing apps for both enterprise and App Store developer accounts. All developers should consider the code signing practices described in this document before resorting to manual code signing. This Q&A discusses how to opt into Xcode's automatic code signing. The practices presented in this document apply to both iOS and macOS app development.

To use automatic code signing in Xcode 8, select 'Automatically manage signing' in the signing settings displayed in the general tab for your build settings as shown in the Xcode help (see the section explaining how to [Assign a project to a team](http://help.apple.com/xcode/mac/current/#/dev23aab79b4)). After performing these operations, your project will be configured for Xcode managed signing.

After selecting Xcode managed signing, select your development team using the pop-up menu. If your app is destined for the App Store or for Enterprise distribution, then the development team you select should be the one associated with your Developer Programs account and not the personal team created for you by Xcode. You can identify your personal team by looking for the label "(Personal Team)" beside the name. Selecting the team with the label "(Personal Team)" will allow you to sign your app, but you will only be able to run your app on your own personal devices (and you will not be able to upload your app to the App Store).

If the only team available in the Team pop-up menu is your personal team and you would like to code sign your app for submission to the App Store then you will need to create Developer and distribution credentials for signing your App. For directions about how to manage your account, please see the "[Manage Signing Certificates](http://help.apple.com/xcode/mac/current/#/dev154b28f09)" section in the Xcode help documentation.

Once you have your team selected, you will have completed setting up your project to automatic code signing. With automated code signing enabled, Xcode will be able to resolve most code signing problems that can occur automatically. You should perform these same operations for all of the targets in your project.

If you have a multi-target project, then you should apply the same settings to all of your targets. For your project to be properly signed, make sure that the version numbers and the build numbers for all of your targets are set to the same value.  That is to say, you should use the same version number in all of your targets and you should use the same build number in all of your targets.

See the document [Technical Note TN2420: Version Numbers and Build Numbers](https://developer.apple.com/library/prerelease/content/technotes/tn2420/_index.html) for more information about how to properly set your version numbers and build numbers for iOS and macOS app submissions to the App Store.

With Xcode managed signing enabled Xcode will manage your entitlements automatically. Many of the entitlements that were formerly managed using a custom entitlements file are now managed using the capabilities tab. Except in specific cases, it is not necessary for you to create your own entitlements file. When you add capabilities to your app using Xcode's capabilities tab, Xcode automatically configures your provisioning profiles for you, updates (or creates) a supporting entitlements file as needed, adds technology-specific frameworks as needed, creates code signing and provisioning assets for your team and sets your code signing build settings for you.

To sign a pre-build framework that you have added to a target in your Xcode project, you must add an Embed Frameworks build phase into your project to copy the framework into your app. And, in the embed frameworks build phase you must select the 'code sign on copy' option for the library to activate code signing for it.

 If the framework you are trying to add has already been signed, then you should try to obtain an unsigned version.  Apple tools do not currently support re-signing frameworks.

You can easily identify any Xcode-managed provisioning profiles in the member center that use an explicit App ID because their name will begin with the text “iOS Team Provisioning Profile:” followed by the bundle ID. Xcode 5 required that you create your own distribution profile in the member center so any you created when using Xcode 5 will be named using the names you chose. Xcode 6 and later versions create distribution certificates or distribution provisioning profiles for you when automatic code signing is enabled. When Xcode creates a distribution provisioning profile, the name of the distribution provisioning profile begins with the text XC: followed by the App ID. If you are using a wildcard App ID, the name of the distribution provisioning profile is XC:\*.

- [Xcode Help](http://help.apple.com/xcode/mac/current/)
- [Technical Note TN2420: Version Numbers and Build Numbers](https://developer.apple.com/library/prerelease/content/technotes/tn2420/_index.html)
- [WWDC 2016 Session 401: What's New in Xcode App Signing](https://developer.apple.com/videos/play/wwdc2016/401/)
- [Technical Note TN2415: Entitlements Troubleshooting](https://developer.apple.com/library/content/technotes/tn2415/_index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-06-14 | Replaced illustration showing automatic code signing settings with a reference to the Xcode help documentation. |
| 2017-03-14 | Updated for Xcode 8. Added some information for multi-target projects. |
| 2015-12-26 | emphasized this is the recommended approach for Code Signing |
| 2015-03-31 | Added images reflecting recommended build settings. |
| 2015-03-25 | Fixed broken link. |
| 2015-03-23 | Minor change. |
| 2015-03-17 | Rewrote for improved readability |
| 2014-10-07 | updated with information about Xcode 6 |
| 2014-04-24 | Added note about bundle seed id differing from team id. Updated for both iOS and OS X. |
| 2014-01-21 | New document that talks about how to set up Xcode to automatically manage your provisioning profiles. |

