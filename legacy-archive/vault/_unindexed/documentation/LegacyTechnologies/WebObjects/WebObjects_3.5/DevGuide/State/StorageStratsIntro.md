---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/StorageStratsIntro.html
archived_at: '2026-07-15T07:52:22.816435Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](ComponentObjAndState.md)

# State Storage Strategies

WebObjects gives you the option of storing state in various ways:

- In the server. State is maintained in memory within a WebObjects application.
- In the page. State is embedded in the HTML page that's returned to the user.
- In cookies. State is embedded in name-value pairs ("cookies") in the HTTP header and passed between the client and server. Like "state-in-the-page," cookies store state on the client.
- In custom stores. State is stored using a mechanism of your own design.

By default, WebObjects uses the first approach, storing state on the server. To determine whether you should use this default approach or try one of the other state-storage solutions, read the next sections, "[Comparison of Storage Options](StoreCompTable.md#apple-gmzds)" and "[A Closer Look at Storage Strategies](CloserLookAtStrats.md#apple-guytkma)." If you decide to use one of the other state-storage solutions, you may have to set up custom objects so that they can be archived. To learn more about this issue, read ["Storing State for Custom Objects"](StateForCustomObjects.md#apple-guzdqoa).

You may find you need to control the amount of state that is stored. The sections ["Controlling Session State"](ControllingSessionState.md#apple-gm2dona) and ["Controlling Component State"](ControllingComponentState.md#apple-gy3do) tell you how to do so.

[!Table of Contents](StateTOC.md) [!Next Section](StoreCompTable.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
