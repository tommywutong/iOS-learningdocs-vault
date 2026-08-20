---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/StorageStratsIntro.html
archived_at: '2026-07-15T07:47:54.401711Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](AccessingExistingSession.md)

# State Storage Strategies

WebObjects gives you the option of storing state in various ways:

- __In the server__. State is maintained in memory within a WebObjects application.
- __In the page__. State is embedded in the HTML page that's returned to the user.
- __In cookies__. State is embedded in name-value pairs ("cookies") in the HTTP header and passed between the client and server. Like "state-in-the-page", cookies store state on the client.
- __In custom stores__. State is stored using a mechanism of your own design.

By default, WebObjects uses the first approach, storing state in the server. Before examining how to use these different strategies, let's take a look at some of their advantages and disadvantages.

[!Table of Contents](ManagingState.book.md)
[!Next Section](StoreCompTable.md)
