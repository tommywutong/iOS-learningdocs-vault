---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/WODisplayGroupAndRefresh.html
archived_at: '2026-07-15T07:47:56.401534Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](ClientCaching.md)

# Page Refresh and WODisplayGroup

If you're using a WODisplayGroup object in your application, you must enable page refresh so that the application and the client browser stay in agreement about which objects are being displayed.

A WODisplayGroup holds a set of objects (generally enterprise objects fetched from a database) and provides "batched" access to these objects. For example, if a user submits a query (such as, "Show me the movies released in 1996.") to a Movies application, a WODisplayGroup might return ten records at a time to the user's browser. The application would offer controls to let the user display the next and previous batches of ten movie titles. When the user decides to order one of the movies, the WODisplayGroup needs to know which batch the item comes from.

As the user presses the Next Ten Movies or Previous Ten Movies buttons, the WODisplayGroup updates its record of the which ten movies are being displayed. When the user decides to order the second movie in the list, the WODisplayGroup can determine the actual record since it knows which batch is being displayed and which record is number two in that batch. But if the user backtracks to a previous page (with page refresh disabled) and chooses the second record, the WODisplayGroup will erroneously pick the second record from its current batch. By enabling page refresh, the WODisplayGroup is alerted each time the user backtracks and can update its notion of the current batch, eliminating this problem.
