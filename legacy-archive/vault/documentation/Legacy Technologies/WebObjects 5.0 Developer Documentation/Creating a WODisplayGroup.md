---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.15.html
archived_at: '2026-07-15T08:14:48.902268Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.14.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.16.md)

#   Creating a WODisplayGroup

##  Synopsis

Discusses the different ways to create a WODisplayGroup.

##  Description

Typically a WODisplayGroup has an EODatabaseDataSource, which in turn, has an EOEditingContext. The EODatabaseDataSource maintains a fetch specification and an array of objects obtained from the EOEditingContext. Figure 1 shows the relationship between the WODisplayGroup, its EODatabaseDataSource and the session's EOEditingContext.

!

The WODisplayGroup and its EODatabaseDataSource

!

You create most WODisplayGroups in one of these ways:

- 

  By using Project Builder's wizard to build a component with the display group. Open your project in Project Builder. Click the Web Components suitcase and select File->New in Project. This builds a component containing a WODisplayGroup, an EODatabaseDataSource, and dynamic elements that display the WODisplayGroup's objects.
- 

  By dragging an entity icon from the EOModeler application to a component opened in WebObjects Builder. This creates a WODisplayGroup and an EODatabaseDataSource.

In both cases, the EODatabaseDataSource is automatically created and attached to the session's default editing context.

###  Creating a Detail WODisplayGroup

Most WODisplayGroups operate independently of other WODisplayGroups; however, you can set up a master-detail association between two WODisplayGroups. You typically do this by dragging a to-many relationship from the EOModeler application to a component opened in the WebObjects Builder application. When you do this, the display group you create has an EODetailDataSource (defined in EOControl) as its data source, a detail key equal to the to-many relationship's key, and a master object equal to the entity from which you dragged the relationship. See "Setting Up a Master-Detail Configuration" in _Getting Started With WebObjects_
.

###  Creating a WODisplayGroup Programmatically

To create a WODisplayGroup programmatically, you instantiate a EODatabaseDataSource and a WODisplayGroup. Then you make the proper connections between the EODatabaseDataSource, the WODisplayGroup, and the session's EOEditingContext. The following Java code, placed in a component's constructor, creates a WODisplayGroup and fetches all of the rows for the "Movie" entity.

```

public Main() {    super();    EOEditingContext ec = this.session().defaultEditingContext();    EODatabaseDataSource ds = new EODatabaseDataSource(ec,"Movie");    moviesDisplayGroup = new WODisplayGroup();    moviesDisplayGroup.setDataSource(ds);    moviesDisplayGroup.fetch();}
```

##  See Also

- 

  [Setting a WODisplayGroup's Fetch Specification Programmatically](Setting%20a%20WODisplayGroup%27s%20Fetch%20Specification%20Programmatically.md#apple-gi3tanbu)
- 

  [Using Master-Peer Configurations](Using%20Master-Peer%20Configurations.md#apple-gi2denrx)
- 

  WODisplayGroup class specification in the _WebObjects Framework Reference_
- 

  EODatabaseDataSource class specification in the _Enterprise Objects Framework Reference_

##  Questions

- 

  How do I create a WODisplayGroup programmatically?

##  Keywords

- 

  WODisplayGroup
- 

  Data Source

##  Revision History

19 February 1999. Clif Liu. First Draft.

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.14.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.16.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
