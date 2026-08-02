---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/ChoosingYourApproach/Rapid_Devel_siderations.html
archived_at: '2026-07-15T08:14:56.243406Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](User_Interf_equirements.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Combining_Approaches.md)

## Rapid Development Considerations

Using the Direct to Web and Direct to Java Client approaches,
you can build an application with far less time and effort than
the WebObjects HTML and Java Client approaches. You only need to
provide the database-to-enterprise objects mapping (the model) and WebObjects
creates your application from it. However, the rapid development
approaches also impose a user interface on your application and
you must be adept at WebObjects and Direct to Web to override it.

There are several types of applications at which the rapid
development approaches excel because their user interface limitations
aren't an issue:

- __Database
  maintenance tools.__ These approaches create user interfaces
  optimized for administering databases and are therefore well-suited
  for this type of application.
- __Prototypes.__ You can quickly and easily
  test a model by creating a Direct to Web or Direct to Java Client
  application based on the model. Using this application, you can test
  whether the relationships and database integrity rules are correct.
- __Internal data driven applications.__ Direct
  to Web has been used to develop in-house applications for bug and
  feature tracking, customer account management, and writing online
  help. Direct to Java Client can be used for such applications as
  well. For internal applications, the user interface polish is not
  as important as development time, making these applications ideal
  candidates for the WebObjects rapid development approaches.

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](User_Interf_equirements.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Combining_Approaches.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
