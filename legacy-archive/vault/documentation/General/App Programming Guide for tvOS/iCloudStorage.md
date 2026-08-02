---
title: App Programming Guide for tvOS
apple_id: TP40015241
resource_type: Guide
platform: tvOS
topic: General
technology: null
published: '2017-01-12'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/AppleTV_PG/iCloudStorage.html
archived_at: '2026-07-15T07:33:12.931901Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Programming Guide for tvOS](index.md)



## iCloud Storage

Storage on Apple TV is limited, and there is no guarantee that information stored on the device will be available the next time a user opens your app. Also, in order to share the user’s data across multiple devices, you need to store the user’s information somewhere other than the Apple TV. Apple provides two shared storage options for Apple TV: iCloud Key-Value Storage (KVS) and CloudKit.

For small storage needs, under 1 MB, your app can use iCloud KVS. iCloud KVS automatically synchronizes information across all of a user’s devices. Only the owner of the app is able to access the information stored by iCloud KVS. Other users of your app are not able to access this information. For more information, see [Designing for Key-Value Data in iCloud](https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesigningForKey-ValueDataIniCloud.html#//apple_ref/doc/uid/TP40012094-CH7).

For large storage needs, greater than 1MB, your app needs to implement CloudKit. CloudKit allows information stored by one user to be accessed by another user. This is extremely useful in instances where the actions of one user affect the options of another user; for example, the actions taken by a user during a game turn that directly affect another user. For information on implementing CloudKit in your app, see _[CloudKit Quick Start](../../Data%20Management/CloudKit%20Quick%20Start/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dsobx)_.

[Creating Layered Images](CreatingParallaxArtwork.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbrfvbuqmjzfvjvomi)

[On-Demand Resources](OnDemandResources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbrfvbuqojnknltc)
