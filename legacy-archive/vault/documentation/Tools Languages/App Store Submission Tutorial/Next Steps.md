---
title: App Store Submission Tutorial
apple_id: TP40011375
resource_type: Guide
platform: iOS
topic: Languages & Utilities
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/YourFirstAppStoreSubmission/NextSteps/NextSteps.html
archived_at: '2026-07-18T02:09:07.639796Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Store Submission Tutorial](About%20Your%20First%20App%20Store%20Submission.md)


[Next](Document%20Revision%20History.md)[Previous](Review%20and%20Troubleshooting.md)

# Next Steps

This tutorial assumes that you can develop and test your app on devices using the iOS Wildcard App ID and iOS Team Provisioning Profile. But, if you use any of the specialized technologies—such as iCloud storage, push notifications, or Game Center—you need to use an explicit App ID and specialized ad hoc and distribution provisioning profiles. Furthermore, if you are not an individual developer, you may need to add others to your team and perform other team administrative tasks.

iCloud storage allows you to share the user’s data among multiple instances of your app running on different iOS and Mac OS X devices. You can test your iCloud app using the iOS Team Provisioning Profile that Xcode creates for you. But first you need to enable and set iCloud storage entitlements using Xcode. To learn more about using iCloud storage, read _[Your Third iOS App: iCloud](../../General/Your%20Third%20iOS%20App-%20iCloud/About%20Your%20Third%20iOS%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjx)_.

If you use push notifications, In-App Purchase, or Game Center, you need to register an explicit App ID in some cases. Enable these technologies, and create specialized provisioning profiles for development and testing using Member Center. Read the _App Distribution Guide_ to learn how to perform these administrative tasks, and read the following documents to learn more about specific technologies:

- _[Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194)_
- _[In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)_
- _[Game Center Programming Guide](../../Networking%20Internet/Game%20Center%20Programming%20Guide/About%20Game%20Center.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmbu)_

If you enrolled in the iOS Developer Program as a company, you are the primary contact for your development team. If your team members also need signing certificates and provisioning profiles for development and testing, you add the team members to your account and manage these assets. Read _App Distribution Guide_ for this information.

Apps are approved only if they adhere to the published Apple guidelines. To learn how to design an app for the App Store, read _iOS Human Interface Guidelines_ and _[App Store Review Guidelines](https://developer.apple.com/appstore/resources/approval/guidelines.html)_.

There are additional tasks you need to perform to market and maintain your product. These tasks are described in _iTunes Connect Developer Guide_.

[Next](Document%20Revision%20History.md)[Previous](Review%20and%20Troubleshooting.md)

