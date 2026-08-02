---
title: How can a build engineer distribute an app on behalf of the team?
apple_id: DTS40012165
resource_type: QA
platform: iOS
topic: Languages & Utilities
technology: null
published: '2014-11-13'
source_url: https://developer.apple.com/library/archive/qa/qa1763/_index.html
archived_at: '2026-07-18T02:34:39.888950Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1763

# How can a build engineer distribute an app on behalf of the team?

## Q:  How can a build engineer distribute an app on behalf of the team?

A: App Store Apps and Enterprise Apps require different handling when preparing them for distribution. Exactly how you involve your build engineer depends on the type of app you are distributing. The two sections below provide directions for distributing each type of app.

__App Store App Team Agent Actions__. The following steps must be completed by the Team Agent to allow your build engineer to have sufficient access to do their job.

1. Add the build engineer to the development team with the role of "Admin" through the [Member Center](https://developer.apple.com/membercenter/index.action). The Admin role will be required for your build engineer to manage your team distribution certificate. For more information about the roles of different team members, see the [Managing Your Team](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/ManagingYourTeam/ManagingYourTeam.html#//apple_ref/doc/uid/TP40012582-CH16-SW1) section of the App Distribution Guide.
2. If the distribution build will be submitted to the App Store, add the build engineer to the team users on [iTunes Connect](https://itunesconnect.apple.com/) with the role of Technical User. This allows the build engineer to log into iTunes Connect with their own credentials while submitting the app. Skip this step if the build is being used for Ad Hoc beta testing. For more info about the Technical User role in iTunes Connect, see [Viewing, Editing, and Deleting iTunes Connect Users](https://developer.apple.com/library/ios/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/Chapters/SettingUpUserAccounts.html#//apple_ref/doc/uid/TP40011225-CH25-SW3) in the iTunes Connect Developer Guide.

__App Store App Build Engineer Actions__. Once the Team Agent has granted the build engineer access, the build engineer can perform the following steps for distributing your App Store app:

1. If the team is creating apps for the iOS app store, then create a new distribution certificate according to [Requesting Signing Identities](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingCertificates/MaintainingCertificates.html#//apple_ref/doc/uid/TP40012582-CH31-SW6). If the team distribution certificate already exists, it must be revoked and recreated by the build engineer according to [Re-Creating Certificates and Updating Related Provisioning Profiles](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingCertificates/MaintainingCertificates.html#//apple_ref/doc/uid/TP40012582-CH31-SW34).
2. Make sure the Xcode Project is [Configured for Distribution](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/ConfiguringYourApp/ConfiguringYourApp.html#//apple_ref/doc/uid/TP40012582-CH28-SW1).
3. Archive then Submit the App to the App Store using the directions found in the [Submitting Your App to the Store](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/SubmittingYourApp/SubmittingYourApp.html#//apple_ref/doc/uid/TP40012582-CH9-SW1) section of the App Distribution Guide.

__Enterprise App Team Agent Actions__. The following steps must be completed by the Team Agent to allow your build engineer to have sufficient access to do their job.

1. The team agent can add the build engineer to the development team with the role of Admin through the Member Center. For more information on defining team roles, see Managing Your Team. The Admin role is required to manage the team distribution certificate if needed.
2. If the team is creating apps for Enterprise Distribution, then transfer a copy of the team agents certificates and profiles to the build engineers machine using Xcode for [Exporting and Importing Certificates and Profiles](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingCertificates/MaintainingCertificates.html#//apple_ref/doc/uid/TP40012582-CH31-SW15).

__Enterprise App Build Engineer Actions__. Once the Team Agent has granted the build engineer appropriate access, the build engineer can perform the following steps for distributing your enterprise apps.

1. Follow the steps provided in the [Distributing iOS Developer Enterprise Program Applications](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/DistributingEnterpriseProgramApps/DistributingEnterpriseProgramApps.html#//apple_ref/doc/uid/TP40012582-CH33-SW1) section of the App Distribution Guide.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-11-13 | reorganized contents |
| 2013-10-30 | Update links for Xcode 5 App Distribution Guide. |
| 2013-05-21 | Guide references & tools update. |
| 2012-04-27 | Minor editorial update. |
| 2012-04-04 | New document that describes the process in which a build engineer distributes an app on behalf of the team. |

