---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/SessionObjAndState.html
archived_at: '2026-07-15T07:47:50.385908Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](AppObjAndState.md)

# The Session Object and Session State

A more interesting type of state that web applications can store is the state associated with a user's session. This state might include the selections a user makes from a catalog, the total cost of the selections so far, or the user's billing information. The details of how WebObjects handles session state are discussed in "[State Management and the Request-Response Loop](StateAndRRLoop.md)" below, but a quick overview will help you understand the scope and duration of session state.

A WebObjects application centralizes session state in objects of the WOSession class (called WebSession, in Java). Each user session has one and only one session object, and a single WebObjects application has as many session objects as it has active user sessions. The session objects segregate data in one session from that in another. There's no way for one session to query or set the data in another. If data needs to be shared across sessions, the application object should be used.

The URLs that make up the requests to a WebObjects application contain an identifier for a particular session within the application. Using this identifier, the application can restore the state corresponding to that session before the request is processed. If the request is that of a user contacting the application for the first time, a new session object is created for that user.

As you can imagine, storing data for each session has the potential of consuming excessive amounts of resources, so WebObjects lets you set a timeout for session objects and lets you terminate them directly.

In summary, session state is only accessible to objects within the same session, and persists only as long as the session object persists.

[!Table of Contents](ManagingState.book.md)
[!Next Section](ComponentObjAndState.md)
