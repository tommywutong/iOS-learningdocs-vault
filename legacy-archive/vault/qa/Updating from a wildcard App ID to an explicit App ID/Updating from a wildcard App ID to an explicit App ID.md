---
title: Updating from a wildcard App ID to an explicit App ID
apple_id: DTS40009452
resource_type: QA
platform: iOS
topic: null
technology: StoreKit
published: '2010-01-09'
source_url: https://developer.apple.com/library/archive/qa/qa1680/_index.html
archived_at: '2026-07-18T02:33:46.595102Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1680

# Updating from a wildcard App ID to an explicit App ID

## Q:  My application is currently signed with a Provisioning Profile that uses a wildcard App ID. How do I enable my App ID to support In App Purchase or Apple Push Notification service?

A: In App Purchase and Apple Push Notification service require that your application is signed with a Provisioning Profile, which uses an explicit App ID such as `com.mycompany.myappname`. So, if you have shipped an application signed with a Provisioning Profile that uses a wildcard App ID such as `com.mycompany.*`, you may wonder how to enable that App ID to handle these features. The answer is to keep your project's Bundle ID the same and create a new App ID in the iPhone Portal that matches the Bundle ID you are currently using in your project. Follow the steps below to enable an App ID that supports In App Purchase or Apple Push Notification service:

1. Identify your application's current Bundle ID

   You can find your Bundle ID by looking in your project's Info.plist file, however it is best to check what iTunes Connect says it is. Log in to [iTunes Connect](http://itunesconnect.apple.com/), navigate to the Manage Your Applications module present in the home page, then select the App Details link for the application you are updating, and copy the bundle identifier displayed in the ensuing page.
2. Create a new App ID

   Your Team Agent or Team Admin should log in to the [iPhone Portal](https://developer.apple.com/iphone/manage/overview/index.action) and navigate to its App ID section to create a new App ID. In the App ID section, click on the New App ID button to navigate to the Create App ID form, which contains a Description field, a Bundle Identifier field, a Bundle Seed ID pop-up menu, and a Submit button as shown in Figure 1. Fill out the Description field with a meaningful name such as `Explicit App ID for MyAppName` for your App ID, select Generate New from the Bundle Seed ID pop-up menu, and paste the previously copied bundle identifier into the Bundle Identifier field. Click Submit to save the new App ID.

__Figure 1__  Create App ID form

!!

1. Enable the newly created App ID for In App Purchase or Apple Push Notification service

   Find your App ID in the App ID section of the Program Portal, click the Configure link next to it, and follow the instructions to enable your App ID for either In App Purchase or Apple Push Notification service.
2. Update or create, download, and install a Provisioning Profile that uses your App ID enabled for In App Purchase or Apple Push Notifications

   Edit an existing Provisioning Profile or create a new one, and then associate it with your newly created App ID. Download and install this Provisioning Profile on your machine and select it in the Code Signing Identity section of your Target's Build pane in Xcode. Update the version number of your binary, build it, test it, and upload it to [iTunes Connect](http://itunesconnect.apple.com/) for review.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-01-09 | New document that describes how to enable a wildcard App ID to support In App Purchase and Apple Push Notification service. |

