---
title: The beta-reports-active Entitlement
apple_id: DTS40014998
resource_type: QA
platform: iOS
topic: Languages & Utilities
technology: Security
published: '2014-10-14'
source_url: https://developer.apple.com/library/archive/qa/qa1830/_index.html
archived_at: '2026-07-18T02:35:06.131066Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1830

# The beta-reports-active Entitlement

## Q:  How do I resolve the "`beta-reports-active`" code signing error?

A: There are a number of points of consider regarding this error and a couple solutions are discussed below.


```
No matching provisioning profiles found for "your.app" None of the valid provisioning profiles allowed the specified entitlements: beta-reports-active.
```

`beta-reports-active` is a new entitlement added to App Store profiles in September 2014 to allow App Store code signed builds to be tested using iTunes Connect. See __App Distribution Guide__ > Beta Testing Your iOS App > [Distributing Your Beta App Using iTunes Connect](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/TestingYouriOSApp/TestingYouriOSApp.html#//apple_ref/doc/uid/TP40012582-CH8-SW5) for more information.

To resolve this error, you need to install an App Store distribution profile within Xcode. Since App Store provisioning profiles are the only profiles containing the `beta-reports-active` entitlement, the error indicates that an App Store provisioning profile matching your app's bundle identifier couldn't be found in Xcode's local profile library.

Since `beta-reports-active` was added in September 2014, all App Store profiles that were generated prior to September 2014 must be regenerated to pick up the new entitlement. That can be done by:

1. On the Certs IDs & Profiles website > [Provisioning Profiles](https://developer.apple.com/account/ios/profile/profileList.action) page, click the App Store profile.
2. Click 'Edit'
3. Click 'Generate'

To create a new App Store profile, click the "+" button on the [Distribution Provisioning Profiles](https://developer.apple.com/account/ios/profile/profileList.action?type=production) page.

After creating or updating your App Store profile, do one of the following to install the updated profile in Xcode:

- Click 'Download' and drag/drop the provisioning profile onto the Xcode icon on the dock
- Click '↺' on Xcode > Preferences > Accounts > (your account) > View Details pane

For more information on App Store provisioning profiles, see __App Distribution Guide__ > [About Store Provisioning Profiles](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/SubmittingYourApp/SubmittingYourApp.html#//apple_ref/doc/uid/TP40012582-CH9-SW32).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-10-14 | New document that explains the beta-reports-active entitlement and helps resolve related code signing errors. |

