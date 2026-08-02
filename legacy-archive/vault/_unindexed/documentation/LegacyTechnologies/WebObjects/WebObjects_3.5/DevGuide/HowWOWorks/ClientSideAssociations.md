---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/ClientSideAssociations.html
archived_at: '2026-07-15T07:51:46.789575Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](Associations.md)

## Associations and Client-Side Java Components

Client-side Java components, like server-side dynamic elements, use associations to synchronize state with the parent component. However, the association class they use is not the same. Instead of using __next.wo.Association__ (the WOAssociation equivalent in Java), they use __next.wo.client.Association__, and this Association class is downloaded to the client along with the component itself.
Keys for a client-side component fall into two groups: state bindings and action bindings. _State bindings_ form the basis for state synchronization by associating state in the applets with state in the server. _Action bindings_ associate particular events in the client applet (such as clicking a button) with the invocation of methods in the server.
State is synchronized between the client and the server in three phases:

- When a page is first generated, the server sends the client all state for which there are bindings.
- Before an action is invoked in the server, the client sends the server any of its state that has changed.
- After the action is completed, the server sends the client any of its state that has changed.

This last synchronization occurs only if no new page is returned to the browser. When a method invoked remotely through an applet action binding returns null, it signals that, instead of returning a new page, the server should resynchronize its state with the applets on the page. WebObjects takes a snapshot of the changes in state in the server so that only the state that has changed is sent back to the client.
Note: The last two phases of the synchronization cycle can be initiated only on the browser side. That is, except for the first "initialization" phase, the server component can react only to an action triggered in an applet. The component cannot unilaterally update the state of an applet when its own state changes.

[!Table of Contents](HowWOWorks.md) [!Next Section](Subcomponents.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
