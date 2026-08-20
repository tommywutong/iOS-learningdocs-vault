---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/StateTOC.html
archived_at: '2026-07-15T07:52:22.338285Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Top](../DevGuideTOC.md)

# Managing State

---

Most applications must be able to preserve some application state between a user's requests. For example, if you're writing a catalog application, you must keep track of the items that the user has selected before the user actually fills out the purchasing information. By default, WebObjects stores application state on the server. If this doesn't meet your needs, WebObjects provides several alternatives strategies for storing state.
This chapter describes why, when, and how to store state in a WebObjects application. It compares all of the available state-storage strategies, shows you how to implement your own state-storage strategy, plus it describes how to control the amount of application state stored.
If you're fairly new to WebObjects programming, you'll probably just want to read the first three sections of this chapter and skip the rest. As you begin to write larger, more complex applications, memory demands and performance become an issue. At that point, you should read the rest of this chapter to learn about alternative state-storage strategies and how you can control the amount of state stored.
Before reading this chapter, you should be familiar with concepts presented in the chapter "[WebObjects Viewed Through Its Classes](../HowWOWorks/HowWOWorks.md)."

[****
: __Why Do You Need to Store State__](WhyStore.md#apple-gyydomy)

[****
: __When Do You Need to Store State__](WhenStore.md#apple-giztm)

[****
: __Objects and State__](ObjectsAndState.md#apple-gu2da)

[****
: The Application Object and Application State](AppObjAndState.md#apple-geytamq)[****
: The Session Object and Session State](SessionObjAndState.md#apple-geydsma)[****
: Component Objects and Component State](ComponentObjAndState.md#apple-gu3tqma)

[****
: __State Storage Strategies__](StorageStratsIntro.md#apple-gi2tg)

[****
: Comparison of Storage Options](StoreCompTable.md#apple-gmzds)[****
: A Closer Look at Storage Strategies](CloserLookAtStrats.md#apple-guytkma)

[****
: State in the Server](StateInServer.md#apple-g4ztc)[****
: State in the Page](StateInPage.md#apple-g42dg)[****
: State in Cookies](StateInCookies.md#apple-heyti)[****
: Custom State-Storage Options](CustomStorageOptions.md#apple-geydqmy)

[****
: __Storing State for Custom Objects__](StateForCustomObjects.md#apple-guzdqoa)

[****
: Archiving Custom Objects in a Database Application](UsingEOEditingContext.md#apple-ha4do)[****
: Archiving Custom Objects in Other Applications](UsingNSCoding.md#apple-gezteni)

[****
: __Controlling Session State__](ControllingSessionState.md#apple-gm2dona)

[****
: Setting Session Time-Out](SessionTimeOut.md#apple-ha2dq)[****
: Using awake and sleep](SessionAwake.md#apple-hezdc)

[****
: __Controlling Component State__](ControllingComponentState.md#apple-gy3do)

[****
: Managing Component Resources](ManagingComponentResources.md#apple-hezda)

[****
: Adjusting the Page Cache Size](PageCacheSize.md#apple-heyde)[****
: Using awake and sleep](PageAwake.md#apple-geytcnq)[****
: pageWithName: and Page Caching](PageWithName.md#apple-ha2tk)

[****
: Client-Side Page Caching](ClientCaching.md#apple-gy4tanq)

[****
: Page Refresh and WODisplayGroup](WODisplayGroupAndRefresh.md#apple-geytcna)

[!First Section](WhyStore.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
