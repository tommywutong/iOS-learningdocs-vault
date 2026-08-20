---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/CloserLookAtStrats.html
archived_at: '2026-07-15T07:52:11.809395Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](StoreCompTable.md)

## A Closer Look at Storage Strategies

To compare and further understand state-storage options, look at the SessionStores sample application. This application presents the user with a choice of storage strategies:!Figure 33. SessionStores: Storage Choices
Once a storage strategy has been chosen, the application plays a guessing game with the user:!Figure 34. SessionStores: Guessing Game
As you can see, the application keeps track of a user's previous guesses within a session-these guesses are part of the state that must be stored from cycle to cycle.
The SessionStores example was designed to illustrate WebObjects' support for various state storage strategies, so it lets you switch between strategies while the application is running. This is not a design you should emulate in your applications-changing storage strategies midsession can cause errors. For example, imagine an application that stores state in the page during the first half of a session and stores state in cookies for the second. Now, suppose that the user backtracks from a page in the second half to one in the first and resubmits the page. The application's strategy and the actual storage mechanism won't match, and state will be lost.
In a normal WebObjects application, you should set the session storage mechanism as early as possible, usually in the application object's initialization method. You set the mechanism by sending the application object a __setSessionStore:__ message. This method takes a WOSessionStore (or SessionStore in Java) object as an argument. WOSessionStore declares these methods to create specific types of session stores:

- serverSessionStore
- pageSessionStore
- cookieSessionStoreWithDistributionDomain:secure:

The following sections describe each state-storage option in detail and show examples of setting the session store.

[!Table of Contents](StateTOC.md) [!Next Section](StateInServer.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
