---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.1c.html
archived_at: '2026-07-15T07:59:33.789197Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.1b.md) | [Back Up One Level](CSJ_Tutorial.1b.md) | [Next](CSJ_Tutorial.1d.md)

###  Adding Movies to the Application

The relationships you specified in EOModeler now come into play in your application. In EOModeler you added a to-many relationship from Studio to Movie, because a Studio can have many Movies. You can now use this relationship to display the movies for the selected studio.

In this type of configuration, called 

master-detail, the master table holds records for the source of the relationship, while the detail table holds records for the destination. As individual records in the master table are selected, the contents of the detail table change to show the records that correspond to the selection in the master. In the StudioManager application, Studio is the master table and Movie is the detail table.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.1b.md) | [Back Up One Level](CSJ_Tutorial.1b.md) | [Next](CSJ_Tutorial.1d.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
