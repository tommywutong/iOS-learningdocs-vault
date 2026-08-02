---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/AccessSession.html
archived_at: '2026-07-15T07:51:40.722180Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](TakeValues.md)

### Accessing the Session

The application determines whether to create a new session or access an existing session by searching the request URL (which was passed in as an argument to the __handleRequest:__ method) for a session ID. If the request is the first one for the session, the request URL looks like the URL shown in [Figure 20](#apple-guyteoa).

!Figure 20. URL to Start a WebObjects Application
This URL does not contain a session ID, so the application object creates a new session by performing the following steps:

- It sends itself a createSession message.
- As part of the __createSession__ method, it sends the __init__ message or the constructor message to the WOSession (or WebSession) class to create a new session object.
- It sends the __awake__ message to the session object.

If the request is part of an existing session, the request URL looks like the one shown in [Figure 21](#apple-guytcoi).

!Figure 21. WebObjects URL in an Existing Session
This URL contains all of the information necessary to restore the state of the existing session. The session ID comes right after the application name in the URL. Because sessions are designed to protect the data of one user's transactions from that of another, session IDs must not be easily predicted or faked. To this end, WebObjects uses randomly generated 32-digit integers as session IDs. (You can also override WOSession's sessionID method and implement another security scheme if you'd like.)
The application keeps existing, active sessions in the WOSessionStore object. The application object uses the session ID to retrieve the appropriate session from the session store (see [Figure 22](#apple-gyztcni)). The appropriate session object is then sent the __awake__ message to prepare it for the request.

!Figure 22. Associating a Request With a Session Object

[!Table of Contents](HowWOWorks.md) [!Next Section](RequestPage.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
