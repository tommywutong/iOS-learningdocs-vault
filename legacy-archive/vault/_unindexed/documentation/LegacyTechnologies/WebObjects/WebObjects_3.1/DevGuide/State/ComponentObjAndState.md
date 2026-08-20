---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/ComponentObjAndState.html
archived_at: '2026-07-15T07:47:40.892915Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](SessionObjAndState.md)

# Component Objects and Component State

In WebObjects, state can also be scoped to a component, such as a dynamically generated page or a reusable component within a page. This state is encapsulated in an object of the WOComponent class (or Component in Java). A component only exists within a session; that is, each session has it own component instances. Component instances are not shared across sessions.

Component state typically includes the data that a page displays, such as a list of choices to present to the user (see __Main.wo__ in the CyberWind or DodgeLite examples). Suppose a user requests the page that lists these choices. The component that represents the page needs to initialize itself with the choice data and then return the response page. This completes one transaction. Now suppose the user looks at the list of choices, selects the third car down, and submits a new request. The same component must be present in this second transaction to identify the choice and take the appropriate action. In short, component state often needs to persist from one client-server transaction to the next.

Component state is scoped to a component object, but it only exists within a session. Within a session, a component's state is often set or queried by other components, but a component's state is not visible across user sessions. So, you can think of component state as being a specific type of session state.

Component state persists until the component object is deallocated, which occurs for various reasons, as described later.

[!Table of Contents](ManagingState.book.md)
[!Next Section](StateAndRRLoop.md)
