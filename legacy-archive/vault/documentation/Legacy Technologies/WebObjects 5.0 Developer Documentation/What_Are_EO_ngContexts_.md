---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Concepts/What_Are_EO_ngContexts_.html
archived_at: '2026-07-15T08:13:58.290849Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](What_Is_a_Model_.md)[![Next](attachments/JavaClient/Images/next.gif)](What_Is_an_Association_.md)

## What Are EODisplayGroups and EOEditingContexts?

### EODisplayGroup

EODisplayGroups transport values between an enterprise object
and a user interface object. You also need an EODatabaseDataSource,
which acts on behalf of the EODisplayGroup to fetch enterprise objects
from the database. In combination, EODisplayGroup and EODatabaseDataSource
coordinate the flow of data between the user interface and the database.
The EODisplayGroup that's created when you drag an entity from
EOModeler into Interface Builder is actually a compound object that
consists of both an EODisplayGroup and an EODatabaseDataSource.

### EOEditingContext

When you drag an entity into the nib file window from your
model, an EOEditingContext object is added to your application along
with the EODisplayGroup that's created from the entity. An EOEditingContext
manages the graph of enterprise objects in your application. The
EOEditingContext is responsible for ensuring that all parts of your
application stay in sync. When an enterprise object changes, the
EOEditingContext broadcasts a notification so that other parts of
the application (such as the user interface) can update themselves accordingly.
The EOEditingContext also manages undo, and is the object through
which you save changes to the database. For more information, see
the EOEditingContext class specification in the _Enterprise
Objects Framework Reference_.

[![Previous](attachments/JavaClient/Images/previous.gif)](What_Is_a_Model_.md)[![Next](attachments/JavaClient/Images/next.gif)](What_Is_an_Association_.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
