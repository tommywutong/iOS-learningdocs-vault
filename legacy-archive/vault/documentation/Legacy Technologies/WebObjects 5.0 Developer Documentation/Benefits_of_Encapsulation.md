---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/SessionStateMaintenance/Benefits_of_Encapsulation.html
archived_at: '2026-07-15T08:13:26.766037Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Running_the_Application.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Further_Exploration.md)

## Benefits of Encapsulation

The application runs just as before. The benefits of moving
the list of users to the session are all organizational. If you
were to add other components that interacted with the list of users
to the application, they could all share the list present in the
session without any additional code.

Notice also that your UserEdit page required only a minimal
change, since you wrote it to work on any given User object without
tightly bound relationships to other parts of the application. This
is a traditional benefit of object-oriented programming allowed
by the fact that every WebObjects component is an object.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Running_the_Application.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Further_Exploration.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
