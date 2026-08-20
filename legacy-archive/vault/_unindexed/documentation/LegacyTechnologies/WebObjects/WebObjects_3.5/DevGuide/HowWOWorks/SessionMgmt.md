---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/SessionMgmt.html
archived_at: '2026-07-15T07:51:53.871934Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](ServerAppMgmt.md)

## Session Level

At the session level, the request-response loop looks like that shown in
[Figure 15](#apple-gi2toni).

!Figure 15. Request-Response Loop: Session Level
The objects dedicated to session management ensure that state with sessionwide scope persists between cycles of the request-response loop.
Two classes are involved at this level:

- WOSession (in Java, WebSession)

Encapsulates the state of a session. WOSession objects persist between the cycles of the request-response loop. WOSession objects store (and restore) the pages of a session, the values of session variables, and any other state that components want to persist throughout a session. The number of pages stored by the session object is dependent on the page-cache size set in WOApplication. Setting the page-cache size is described in the chapter ["Managing State"](../State/StateTOC.md#apple-gu4tmmq). Each session object is identified by a unique session ID, which is reflected in the URL.

- WOSessionStore (in Java, SessionStore)

Provides the strategy or mechanism through which WOSession objects are made persistent. A WOSessionStore object stores session objects in the server or in the page (which can include Netscape cookies), and restores them upon request by the application.

When a user makes an initial request to a WebObjects application, the application creates a session object (WOSession). At the end of the request-response cycle, the application stores the state-bearing session object using the facilities of WOSessionStore. With each subsequent cycle of the request-response loop for that user, the application restores the state of the session at the beginning of the cycle and stores it again at the end of the cycle. To learn more about how to use WOSessionStore, see the chapter ["Managing State"](../State/StateTOC.md#apple-gu4tmmq).

[!Table of Contents](HowWOWorks.md) [!Next Section](RRLoopInfo.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
