---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WOClasses11.html
archived_at: '2026-07-15T08:06:09.128091Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses10.md)

### Accessing the Session

The component action request handler determines whether to create a new session or access an existing session by searching the request URL for a session ID. If the request is the first one for the session, the request URL looks like the URL shown in [Figure 20](WOClasses9.md#apple-g43dcnq). This URL does not contain a session ID, so the request handler creates a new session by performing the following steps:

- It sends the application a __createSessionForRequest__: message.
- As part of the __createSessionForRequest:__ method, the application sends the __init__ message or the constructor message to the WOSession class to create a new session object.
- The application sends the __awake__ message to the session object.

If the request is part of an existing session, the request URL looks like the one shown in [Figure 23](#apple-g43teoa).

!

Figure 23. Component Action Request URL

This URL contains all of the information necessary to restore the state of the existing session. The session ID comes right after the page name in the URL (the page name is optional; if it isn't present in the URL, the session ID comes right after the request handler key). Because sessions are designed to protect the data of one user's transactions from that of another, session IDs must not be easily predicted or faked. To this end, WebObjects uses randomly generated 17-character sequence of letters and numbers. (You can also override WOSession's sessionID method and implement another security scheme if you'd like.)
The application keeps active sessions in the WOSessionStore object. The application object uses the session ID to retrieve the appropriate session from the session store (see [Figure 24](#apple-gyztcni)). The appropriate session object is then sent the __awake__ message to prepare it for the request.

!

Figure 24. Associating a Request with a Session Object

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses12.md)
