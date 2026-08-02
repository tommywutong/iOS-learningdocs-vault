---
title: Your (Personal Team) cannot be used to Code Sign your App for submission to
  the App Store
apple_id: DTS40017617
resource_type: QA
platform: iOS
topic: Xcode
technology: null
published: '2017-03-14'
source_url: https://developer.apple.com/library/archive/qa/qa1915/_index.html
archived_at: '2026-07-18T02:36:50.168471Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1915

# Your (Personal Team) cannot be used to Code Sign your App for submission to the App Store

## Q:  How can I Code Sign my App so I can upload it to the App Store?

A: Xcode 7 and Xcode 8 allow you to select the free personal team provided with your Apple ID for signing your app. This team allows you to build apps for your personal use on devices owned by you, but it does not allow you to code sign apps destined for the App Store or for enterprise use.

You can identify this account by looking in the accounts tab of the Xcode preferences. It is also displayed in the team menu displayed in a target's general build settings. Your personal account will be the account with the string '(Personal Team)' beside the name.

If you try to submit an app to the App Store after you have built it using your personal team, you may receive one of the following error messages:


```
The selected team does not have a program membership that is eligible for this feature.
```



```
To submit to the iOS app store, you need to add an Apple id account that is enrolled in the iOS Developer Program for the development team ‘XXXXXXXXXX’
```

To code sign your app for submission to the App Store you will need to create developer and distribution credentials for signing your app. For directions about how to manage your account, please see "[Managing Accounts section of the App Distribution Guide](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/ManagingAccounts/ManagingAccounts.html)".

See Also:

- [Editing General Target Settings section of the Project Editor Help](http://help.apple.com/xcode/mac/8.0/#/dev0ac32bb34)
- [Technical Q&A QA1814: Setting up Xcode to automatically manage your provisioning profiles](https://developer.apple.com/library/ios/qa/qa1814/_index.html#//apple_ref/doc/uid/DTS40014030)
- [Apple Developer Program Membership Support Page](https://developer.apple.com/support/compare-memberships/)
- [What’s new in Xcode](https://developer.apple.com/xcode/)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-03-14 | New document that talks about why you can't code sign your App for the App Store with the free account provided with your Apple ID |

