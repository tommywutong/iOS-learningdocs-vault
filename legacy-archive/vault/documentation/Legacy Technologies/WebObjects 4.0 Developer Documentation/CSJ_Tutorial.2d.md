---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.2d.html
archived_at: '2026-07-15T07:59:56.563796Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.2c.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.2e.md)

##   What  are EODisplayGroups and EOEditingContexts?

####  EODisplayGroup

EODisplayGroups transport values between an enterprise object and a user interface object. You also need an EODatabaseDataSource, which acts on behalf of the EODisplayGroup to fetch enterprise objects from the database. In combination, EODisplayGroup and EODatabaseDataSource coordinate the flow of data between the user interface and the database. The EODisplayGroup that's created when you drag an entity from EOModeler into Interface Builder is actually a compound object that consists of both an EODisplayGroup and an EODatabaseDataSource.

####  EOEditingContext

When you drag an entity into the nib file window from your model, an EOEditingContext object is added to your application along with the EODisplayGroup that's created from the entity. An EOEditingContext manages the graph of enterprise objects in your application. The EOEditingContext is responsible for ensuring that all parts of your application stay in sync. When an enterprise object changes, the EOEditingContext broadcasts a notification so that other parts of the application (such as the user interface) can update themselves accordingly. The EOEditingContext also manages undo, and is the object through which you save changes to the database. For more information, see the EOEditingContext class specification in the _Enterprise Objects Framework Reference_
.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.2c.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.2e.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
