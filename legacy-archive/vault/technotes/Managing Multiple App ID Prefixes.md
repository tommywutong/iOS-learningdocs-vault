---
title: Managing Multiple App ID Prefixes
apple_id: DTS40014135
resource_type: Technical Note
platform: iOS|Xcode Developer Tools|macOS
topic: Languages & Utilities
technology: Security
published: '2014-02-12'
source_url: https://developer.apple.com/library/archive/technotes/tn2311/_index.html
archived_at: '2026-07-26T19:54:13.573515Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2311

# Managing Multiple App ID Prefixes

This document explains why your team might have multiple App ID prefixes and talks about pros and cons of moving to a single App ID prefix.

[Overview](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjtguwugsbrfvhvmrkskzeukvy)[Determining if your team has multiple App ID prefixes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjtguwugsbrfvcekvcfkjgustsjjzdv6skgl5mu6vksl5kekqknl5eecu27jvkuyvcjkbgekx2bkbif6skel5iferkgjfmekuy)[Advantages of having a single App ID prefix](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjtguwugsbrfvauivsbjzkecr2fknpu6rs7jbavmskoi5pucx2tjfheotcfl5avauc7jfcf6ucsivdeswa)[A one-time loss in keychain data will occur if you switch your App ID prefix](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjtguwugsbrfvav6t2oivpvisknivpuyt2tknpusts7jncvsq2iifeu4x2eifkecx2xjfgeyx2pinbvkus7jfdf6wkpkvpvgv2jkrbuqx2zj5kvex2bkbif6skel5iferkgjfma)[Steps to move an App ID from a non-Team ID prefix to the Team ID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjtguwugsbrfvjvirkqknpvit27jvhvmrk7ifhf6qkqkbpusrc7izje6tk7ifpu4t2ol5kekqknl5euix2qkjcumskyl5ke6x2ujbcv6vcfifgv6ske)[Converting wildcard based App IDs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjtguwugsbrfvjvirkqknpvit27jvhvmrk7ifhf6qkqkbpusrc7izje6tk7ifpu4t2ol5kekqknl5euix2qkjcumskyl5ke6x2ujbcv6vcfifgv6skefvbu6tswivjfiskoi5pvoskmirbucusel5becu2firpucucql5euiuy)[All other prefixes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjtguwugsbrfvjvirkqknpvit27jvhvmrk7ifhf6qkqkbpusrc7izje6tk7ifpu4t2ol5kekqknl5euix2qkjcumskyl5ke6x2ujbcv6vcfifgv6skefvauytc7j5keqrksl5iferkgjfmekuy)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjtguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Overview

An App ID prefix is a unique identifier used to group a collection of apps so they can share keychain and `UIPasteboard` data. iOS has two different types of App ID prefixes: a new kind that is your Team ID and an older-style that uses a ten digit alphanumeric string instead of your Team ID. If you have been writing apps for a long time, you may have a number of the older-style prefixes in place, but that would only be the case if you have created additional prefixes yourself (this was only possible prior to the introduction of iCloud in June 2011). Newer app developers who joined the developer program after June 2011 will only have a single App ID prefix associated with their account.

Developers who have more than one App ID prefix should read this document. It is not necessary to convert all of your projects over to using a single App ID prefix, but you may wish to do so depending on your specific needs. Information in this document should help you make an informed choice about what to do. Below, we talk about the the implications of having more than one App ID prefix, the benefits of having a single Team ID based one, and steps you can take to change to a single Team ID based App ID prefix.

[Back to Top](#)

## Determining if your team has multiple App ID prefixes

To find out if you have non-Team ID based App ID prefixes in your account, log in to the member center and take a look at the App ID prefixes associated with your account. If you have more than one App ID prefix, then you can consider migrating the non-Team ID based ones to your Team ID based one (all accounts will have at exactly one unique Team ID based App ID prefix associated with them).

If you only have one App ID prefix associated with your account, then there is nothing more to do.

[Back to Top](#)

## Advantages of having a single App ID prefix

These are the advantages of having a single Team ID based App ID prefix:

- Avoid App ID prefix mismatch situations that can occur during the app distribution process - if there's only one prefix so there is no chance of the wrong one being used.
- Apps can share keychain data if they have the same App ID prefix.
- Apps sharing the same Team ID prefix are eligible for `UIPasteboard` sharing in iOS 7. Here, just having the same Team ID prefix for more than two of your apps automatically enables `UIPasteboard` sharing among them.

[Back to Top](#)

## A one-time loss in keychain data will occur if you switch your App ID prefix

For apps utilizing the [Keychain Services](https://developer.apple.com/library/ios/#documentation/Security/Reference/keychainservices/Reference/reference.html) APIs, changing the App ID prefix of an existing app will have implications for your app that you should be aware of.

Every keychain item in iOS contains an attribute called the keychain access group. An iOS app can only access those keychain items it has permission to. This permission comes from the code signing entitlements stamped into the app when it is signed (using your current App ID prefix).

iOS has one keychain and one keychain only. Access to individual items is gated by their access group.

By default, an app can only access keychain items with the keychain access group matching the application-identifier code signing entitlement. However, if you would like to share keychain items amongst your apps, you can add a custom keychain-access-group code signing entitlement that specifies an array of keychain access groups that the app can access. However, if your app is using one or more custom keychain-access-groups, then if you change your App ID prefix all of your custom keychain-access-groups will be orphaned and you will no longer be able to access them.

This may have only minor implications in some cases. For example, if your keychain usage is modest it might not be a big deal for you to make a change: apps that simply store a user password in the keychain for convenience, may decide to change their App ID prefix to their Team ID based App ID prefix at the small cost of requiring the user to re-enter their password one more time.

__Important:__ If you have recently received an app from another developer by way of the App Transfer process, the transferred App ID will now have your Team ID as the App ID prefix. If the previous version of your app was writing data to the keychain, submitting an app update with the new App ID will result in a loss of access to the previous keychain data. The keychain access will only be lost after an update to the app is released on the App Store.

[Back to Top](#)

## Steps to move an App ID from a non-Team ID prefix to the Team ID

Wildcard App IDs are a special case and you can make the necessary changes yourself. If you would like to use a Team ID based prefix and you are currently using a wildcard App ID, then you can use the steps below for converting your prefix to a Team ID based one.

### Converting wildcard based App IDs

Here are the steps for converting a wildcard based non-Team ID prefixes to use your Team ID based one:

1. Log in to the iOS developer member center and navigate to "Certificates, Identifiers & Profiles".
2. Once in there, navigate into the App IDs section inside of the Identifiers section.
3. Create a new App ID with the same wildcard bundle ID you are already using but using your Team ID based prefix as its prefix. By doing so, you will be associating your wildcard bundle ID with a new Team ID. It is okay to leave your old App ID associated with your wildcard bundle ID there and not delete it - it will be ignored going forward.
4. Edit all your provisioning profiles that are associated to the old App ID and update them to use the new App ID.
5. Go into all of the provisioning profiles that you have changed and regenerate them.
6. Go into Xcode and update your provisioning profiles. For directions about how to do that, see the "[Refreshing Provisioning Profiles in Xcode](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html#//apple_ref/doc/uid/TP40012582-CH30-SW26)" section in the App Distribution Guide.
7. Re-archive your app. Then, submit your new archive making sure to sign it with your new Team ID prefix based provisioning profile.

### All other prefixes

All other App IDs will require the assistance of the member center maintainers - if you are not using a wildcard App ID, then you should contact the iOS member center maintainers for assistance. Here are the steps you can use to do that:

1. Go to [https://developer.apple.com/contact/](https://developer.apple.com/contact/).
2. Submit a request by clicking the link under Enrollment and Account.
[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-02-12 | New document that assists developers managing their App ID prefixes. |

