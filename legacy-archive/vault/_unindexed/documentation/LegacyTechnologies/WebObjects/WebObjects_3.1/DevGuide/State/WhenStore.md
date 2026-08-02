---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/WhenStore.html
archived_at: '2026-07-15T07:47:56.899943Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](Introduction.md)

# When Do You Need to Store State?

Web applications that store state information are necessarily somewhat more complex than those that don't. State storage can also raise scalability (such as how much physical storage should an application server have for a given number of simultaneous users) and performance issues . Given these considerations, it's clearly best to avoid storing state.

Applications differ widely in their state storage requirements. At one extreme are simple applications that vend read-only pages (company information, specifications for hardware devices, and so on). These traditional World Wide Web applications don't need to store state information. At the other extreme are commercial applications that let users wheel virtual shopping carts from page to page, selecting items for purchase. These applications must keep track of order information on a per-user basis. Considering that a popular site could have scores of simultaneous sessions, these commercial applications must employ a sophisticated means of handling state for each session. Somewhere between these extremes are applications with simple state storage requirements, such as keeping track of the total number of votes on an issue, the number of visitors to the web site, and so on.

Characteristically, WebObjects takes an object-oriented approach to fulfilling any of these state-storage requirements.

[!Table of Contents](ManagingState.book.md)
[!Next Section](ObjectsAndState.md)
