---
title: Migrating to CloudKit
apple_id: DTS40016749
resource_type: Technical Note
platform: iOS|macOS
topic: Data Management
technology: CloudKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/technotes/tn2241/_index.html
archived_at: '2026-07-26T19:54:15.079304Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2241

# Migrating to CloudKit

This document covers information on how to migrate data to CloudKit.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhewugsbrfvke4vcbi4yq)[What can I migrate?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhewugsbrfvke4vcbi4za)[How do I migrate?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhewugsbrfvke4vcbi4zq)[What will it cost?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhewugsbrfvke4vcbi42a)[Migrating public non-user content](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhewugsbrfvke4vcbi42q)[Migrating user-specific content](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhewugsbrfvke4vcbi43a)[Authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhewugsbrfvke4vcbi43c2qkvkreektsujfbucvcjj5ha)[Organizing data in custom zones](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhewugsbrfvke4vcbi43c2t2si5au4sk2jfheox2eifkecx2jjzpugvktkrhu2x22j5hekuy)[Writing the data to CloudKit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhewugsbrfvke4vcbi43c2v2sjfkestshl5keqrk7iraviqk7krhv6q2mj5kuis2jkq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

CloudKit powers some of the most popular apps in iOS and OS X. It is designed to help you get started on your app quickly and scale with you as your user base grows.

Before reading this document make sure to read the [CloudKit Quick Start](https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloudKitQuickStart/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014987-CH1-SW1) and [Designing for CloudKit](https://developer.apple.com/library/ios/documentation/General/Conceptual/iCloudDesignGuide/DesigningforCloudKit/DesigningforCloudKit.html#//apple_ref/doc/uid/TP40012094-CH9-SW1) as they walk through core concepts and how to get set up.

[Back to Top](#)

## What can I migrate?

Some of the high-level features that CloudKit provides are:

- Data storage, both user-specific and app-wide, with the ability to synchronize data across users' devices.
- Full-featured APIs for iOS, OS X, and the web.
- Managed push notifications that allow you to visually notify the user or silently notify the device to new changes.
- Automatic user authentication in iOS and OS X for iCloud users.
- A web Dashboard for viewing and editing your data and schema, viewing public usage analytics, and more.

[Back to Top](#)

## How do I migrate?

In order to migrate data into CloudKit, there are two main points to consider:

- How should I get data into CloudKit?

  Data that is not associated with a user can be migrated with a background process or server-side application. Data that is associated with a user must be written to CloudKit from your client application (iOS, OS X, or web) as a user signed into iCloud.
- Where should I write data in CloudKit?

  By default, CloudKit offers a private database that is only visible to the user who wrote the data, and a public database that is visible to all users.

__Table 1__  Public and Private Data

|  | public data | private data |
| non-user-specific | Public DB, server-side migration | N/A |
| user-specific | Private DB, client-side migration | Private DB, client-side migration |

In the case of public non-user-specific data, you can use a server-side application to migrate the data, but in the case of private user-specific data you will need to migrate that data from your client application (iOS, OS X, or web). To understand more about why, make sure to read about [public and private databases](https://developer.apple.com/library/ios/documentation/General/Conceptual/iCloudDesignGuide/DesigningforCloudKit/DesigningforCloudKit.html#//apple_ref/doc/uid/TP40012094-CH9-SW8).

[Back to Top](#)

## What will it cost?

Any data stored in a user's private database counts against their personal iCloud quota whereas data stored in your container's public database counts towards your container's public usage. CloudKit provides up to 1TB of public storage and data transfer that scales with the number of users you have and to find out more, visit [iCloud for Developers](https://developer.apple.com/cloudkit) page.

[Back to Top](#)

## Migrating public non-user content

To migrate public data that doesn't need to be attached to any specific user, the easiest path is probably to build a server-side application that migrates the data. Here is the recommended approach:

1. Use the [CloudKit Dashboard](https://icloud.developer.apple.com/dashboard) to:

   1. [Configure your schema](https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloudKitQuickStart/EditingSchemesUsingCloudKitDashboard/EditingSchemesUsingCloudKitDashboard.html#//apple_ref/doc/uid/TP40014987-CH5-SW4) to support the type of data you will be storing.
   2. Set up a [Server-to-Server Key](https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/SettingUpWebServices/SettingUpWebServices.html#//apple_ref/doc/uid/TP40015240-CH24-SW6) to allow your application to write data into the public database.
2. Build a [node.js application using CloudKit.js](https://developer.apple.com/library/ios/samplecode/CloudAtlas/Listings/Node_node_client_s2s_index_js.html#//apple_ref/doc/uid/TP40014599-Node_node_client_s2s_index_js-DontLinkElementID_22) that does the following (likely in batches):
3. 1. Read the public data from your existing data source.
   2. Write that data into CloudKit.

[Back to Top](#)

## Migrating user-specific content

As mentioned above, you won't be able to migrate user-specific data using a server-side application and instead will need to do so after a user has logged in to your client application (iOS, OS X, or web).

### Authentication

When a user uses your client application to write data to CloudKit it is marked as written by that user. This is often important for controlling who can read and write specific records. On top of this, CloudKit provides you the ability to store a user's private data into their private database so that no other users can access it.

To take advantage of both of these things, your user will need to be signed in with their Apple ID. You can read more about how to do this in the [native API](https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloudKitQuickStart/CreatingaSchemabySavingRecords/CreatingaSchemabySavingRecords.html#//apple_ref/doc/uid/TP40014987-CH3-SW8), the [web services API](https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/SettingUpWebServices/SettingUpWebServices.html#//apple_ref/doc/uid/TP40015240-CH24-SW3), and [CloudKit.js](https://cdn.apple-cloudkit.com/cloudkit-catalog/#authentication). __On iOS and OS X, once a user is signed in to their Apple ID, they are automatically authenticated so you won't need to prompt them to sign into your app__. Because you are migrating a user's data from an existing data source, it's likely that they will also need to be simultaneously logged in with your existing authentication service.

### Organizing data in custom zones

When storing data in a user's private database, you have the option of storing related data in a custom zone, giving you the ability to later ask the server for the set of changes in that zone since a certain point in time. To read more, see the [CKRecordZone](https://developer.apple.com/library/ios/documentation/CloudKit/Reference/CKRecordZone_class/index.html#//apple_ref/occ/cl/CKRecordZone) and [CKFetchRecordChangesOperation](https://developer.apple.com/library/ios/documentation/CloudKit/Reference/CKFetchRecordChangesOperation_class/index.html#//apple_ref/occ/cl/CKFetchRecordChangesOperation) documentation, but consider using zones when migrating your data.

### Writing the data to CloudKit

The CloudKit APIs provide various ways to write data and we recommend that you consider the following mechanisms:

1. __Native API__

   - [CKModifyRecordZonesOperation](https://developer.apple.com/library/ios/documentation/CloudKit/Reference/CKModifyRecordZonesOperation_class/index.html#//apple_ref/occ/cl/CKModifyRecordZonesOperation) for modifying custom zones.
   - [CKModifyRecordsOperation](https://developer.apple.com/library/ios/documentation/CloudKit/Reference/CKModifyRecordsOperation_class/index.html#//apple_ref/occ/cl/CKModifyRecordsOperation) for modifying records.
   - [CKModifySubscriptionsOperation](https://developer.apple.com/library/ios/documentation/CloudKit/Reference/CKModifySubscriptionsOperation_class/index.html#//apple_ref/occ/cl/CKModifySubscriptionsOperation) if you want your users' devices to recieve push notifications (even silent ones) when they update their data on another device.
2. __Web Services API__

   - [Modifying zones](https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/ModifyZones/ModifyZones.html#//apple_ref/doc/uid/TP40015240-CH10-SW1)
   - [Modifying records](https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/ModifyRecords/ModifyRecords.html#//apple_ref/doc/uid/TP40015240-CH2-SW9)
   - [Creating](https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/CreateTokens/CreateTokens.html#//apple_ref/doc/uid/TP40015240-CH19-SW1) and [registering](https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/CreateTokens/CreateTokens.html#//apple_ref/doc/uid/TP40015240-CH19-SW1) APNs tokens
3. __CloudKit.js__

   CloudKit.js is a JavaScript wrapper around the web services API.

   - [Accessing Record Zones](https://developer.apple.com/library/ios/documentation/CloudKitJS/Reference/DatabaseClassRef/index.html#//apple_ref/doc/uid/TP40015343-CH1-SW25)
   - [Accessing Records](https://developer.apple.com/library/ios/documentation/CloudKitJS/Reference/DatabaseClassRef/index.html#//apple_ref/doc/uid/TP40015343-CH1-SW12))
   - [Subscribing to Changes](https://developer.apple.com/library/ios/documentation/CloudKitJS/Reference/DatabaseClassRef/index.html#//apple_ref/doc/uid/TP40015343-CH1-SW18)
[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-02-18 | New document that covers information on how to migrate your data to CloudKit. |

