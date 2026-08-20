---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/SessionStateMaintenance/The_Session.html
archived_at: '2026-07-15T08:13:30.102118Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Using_the_S_anage_State.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Displaying___of_Objects.md)

## The Session

A __session__ is a period of time in which
one user interacts with your application. Since each application
can have multiple users simultaneously, it may have multiple Session
objects. Each session has its own data and its own cached copies
of the components that the user has requested, as shown in [Figure 7-1](#apple-infeeqsgjbbuq).

__Figure
7-1 Relationship between application and
session__

![[image: ../Art/sessions.gif]](../Art/sessions.gif)

The session is represented as an instance of the Session class
(`Session.java`). Initially,
the session has only WebObjects-provided behavior, but you can add
your own methods and variables. For example, if you were building
an online shopping application, the session would be an appropriate
place to store a user's shopping cart, because the session is
tied to one particular user and persists as long as the user is
using the application.

When an incoming request is processed, WebObjects automatically
activates the Session instance associated with the user who originated
the request, as described in ["Request Processing"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/UserInput/iRequest_Processing.html).

The WOComponent class includes a method for accessing the
currently active session. Since all your components inherit from
this class and WebObjects automatically activates the correct session
when a request is processed, calling the `session` method
from your component (or in a keypath) provides you with the session
for the current user.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Using_the_S_anage_State.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Displaying___of_Objects.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
