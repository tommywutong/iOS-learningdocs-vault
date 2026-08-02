---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/SessionStateMaintenance/Using_the_S_anage_State.html
archived_at: '2026-07-15T08:13:31.379085Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/ComponentCommunication/iRunning_the_Application.html)[![Next](attachments/DiscoveringWO/Images/next.gif)](The_Session.md)

# Using the Session to Manage State

The Web is by its nature a stateless medium.
A Web server receives a request, reads the document, and returns
it to the requesting browser, without any knowledge of previous requests
from the same user.

A Web application, however, needs to maintain state between
one request from a particular user and the next. WebObjects encodes
a unique identifier with each incoming request. This identifier
is used to maintain state over a stateless medium. See ["Request Processing"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/UserInput/iRequest_Processing.html) for
more information.

Part of this state is the session. While you can pass information
back and forth between components, you frequently need to maintain
state that is shared between components. Rather than pass this information
from component to component (as described in ["Component Communication"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/ComponentCommunication/iComponent_Communication.html)),
you can store it at a higher level—in the Session object. Each
component has access to the Session object, so such data stored
in it is globally available.

In this chapter, you

- store persistent
  information in the Session object
- access the session from multiple components
- see the benefit of making your components reusable

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/ComponentCommunication/iRunning_the_Application.html)[![Next](attachments/DiscoveringWO/Images/next.gif)](The_Session.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
