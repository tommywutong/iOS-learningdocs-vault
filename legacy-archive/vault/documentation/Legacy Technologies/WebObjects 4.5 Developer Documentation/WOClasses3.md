---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WOClasses3.html
archived_at: '2026-07-15T08:06:19.643497Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses2.md)

## Session Level

At the session level, the request-response loop looks like that shown in [Figure 16](#apple-gi2toni).

!

Figure 16. Request-Response Loop: Session Level

The objects dedicated to session management ensure that state with session-wide scope persists between cycles of the request-response loop. These objects always exist if your application uses component actions. They do not exist if you write your application entirely using direct actions, unless your code explicitly creates them.
Two classes are involved at this level:

- WOSession

Encapsulates the state of a session. WOSession objects persist between the cycles of the request-response loop. WOSession objects store (and restore) the pages of a session, the values of session variables, and any other state that components want to persist throughout a session. The number of pages stored by the session object is dependent on the page-cache size set in WOApplication. Setting the page-cache size is described in the chapter ["Managing State"](Managing%20State.md#apple-heytena). Each session object is identified by a unique session ID, which is either reflected in the URL or stored in a cookie.

- WOSessionStore

Provides the strategy or mechanism through which WOSession objects are made persistent. A WOSessionStore object stores session objects in the server or in the page, and restores them upon request by the application.

When a user makes an initial component action request to a WebObjects application, or explicitly creates a session, the application creates a session object (WOSession). At the end of the request-response cycle, the application stores the state-bearing session object using the facilities of WOSessionStore. With each subsequent cycle of the component action request-response loop for that user, the application restores the state of the session at the beginning of the cycle and stores it again at the end of the cycle. To learn more about how to use WOSessionStore, see the chapter ["Managing State"](Managing%20State.md#apple-heytena).

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses4.md)
