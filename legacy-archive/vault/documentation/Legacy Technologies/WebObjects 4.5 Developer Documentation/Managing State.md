---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/StateTOC.html
archived_at: '2026-07-15T08:06:07.196720Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Top](The%20WebObjects%20Developer%27s%20Guide.md)

# Managing State

---

Most applications must be able to preserve some application state between a user's requests. For example, if you're writing a catalog application, you must keep track of the items that the user has selected before the user actually fills out the purchasing information. By default, WebObjects stores application state on the server. If this doesn't meet your needs, WebObjects provides several alternatives strategies for storing state.
This chapter describes why, when, and how to store state in a WebObjects application. It compares all of the available state-storage strategies, shows you how to implement your own state-storage strategy, plus it describes how to control the amount of application state stored.
If you're fairly new to WebObjects programming, you'll probably just want to read the first three sections of this chapter and skip the rest. As you begin to write larger, more complex applications, memory demands and performance become an issue. At that point, you should read the rest of this chapter to learn about alternative state-storage strategies and how you can control the amount of state stored.
Before reading this chapter, you should be familiar with concepts presented in "[WebObjects Viewed Through Its Classes](WebObjects%20Viewed%20Through%20Its%20Classes.md#apple-he2tmmy)."

[****
: __Why Do You Need to Store State__](ManagingState.md#apple-gyydomy)

[****
: __When Do You Need to Store State__](ManagingState1.md#apple-giztm)

[****
: __Objects and State__](ManagingState2.md#apple-gu2da)

[****
: The Application Object and Application State](ManagingState3.md#apple-geytamq)[****
: The Session Object and Session State](ManagingState4.md#apple-geydsma)[****
: Component Objects and Component State](ManagingState5.md#apple-gu3tqma)

[****
: __State Storage Strategies__](ManagingState6.md#apple-gi2tg)

[****
: A Closer Look at Storage Strategies](ManagingState7.md#apple-g4ztanq)

[****
: State in the Server](ManagingState8.md#apple-g4ztc)[****
: Using Cookies](ManagingState9.md#apple-haydemq)

[****
: __Storing State for Custom Objects__](ManagingState10.md#apple-guzdqoa)

[****
: Archiving Custom Objects in a Database Application](ManagingState11.md#apple-ha4do)[****
: Archiving Custom Objects in Other Applications](ManagingState12.md#apple-gezteni)

[****
: __Controlling Session State__](ManagingState13.md#apple-gm2dona)

[****
: Setting Session Time-Out](ManagingState14.md#apple-ha2dq)[****
: Using awake and sleep](ManagingState15.md#apple-hezdc)

[****
: __Controlling Component State__](ManagingState16.md#apple-gy3do)

[****
: Managing Component Resources](ManagingState17.md#apple-hezda)

[****
: Adjusting the Page Cache Size](ManagingState18.md#apple-heyde)[****
: Using awake and sleep](ManagingState19.md#apple-geytcnq)

[****
: Client-Side Page Caching](ManagingState20.md#apple-gy4tanq)

[****
: Page Refresh and WODisplayGroup](ManagingState21.md#apple-geytcna)

[!First Section](When%20Do%20You%20Need%20to%20Store%20State.md)
