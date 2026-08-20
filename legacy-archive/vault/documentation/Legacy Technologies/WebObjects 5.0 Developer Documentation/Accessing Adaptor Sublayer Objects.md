---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.30.html
archived_at: '2026-07-15T08:14:53.172047Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.2f.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.31.md)

#   Accessing Adaptor Sublayer Objects

##  Synopsis

Describes how to get the adaptor, adaptor context, and adaptor channel objects used by an editing context or a display group.

##  Description

To access an EOEditingContext's adaptor sublayer objects, you get the editing context's EOObjectStoreCoordinator from the editing context, you get an EODatabaseContext from the object store coordinator, and you get the adaptor sublayer objects from there. The following code demonstrates the process.

```

EOEditingContext editingContext;    // Assume this exists.

String entityName;                  // Assume this exists.

EOAdaptor adaptor;

EOAdaptorContext adContext;

EOAdaptorChannel adChannel;

EOFetchSpecification fspec =

    new EOFetchSpecification(entityName, null, null);

EOObjectStoreCoordinator rootStore =

    (EOObjectStoreCoordinator)editingContext.rootObjectStore();

EODatabaseContext dbContext = (EODatabaseContext)rootStore.

    objectStoreForFetchSpecification(fspec);

EODatabaseChannel dbChannel = dbContext.availableChannel();

adaptor = dbContext.database().adaptor();

adContext = dbContext.adaptorContext();

adChannel = dbChannel.adaptorChannel();

adChannel.openChannel();  // before you use the database
                          // channel or the adaptor channel
```


This example first creates a fetch specification, providing just the entity name as an argument. Of course, you can use a fetch specification that has non-_null_
values for all of its arguments, but only the entity name is used by the EOObjectStore
objectStoreForFetchSpecification
method. Next, the example gets the editing context's EOObjectStoreCoordinator using the EOEditingContext method
rootObjectStore
. This method returns an EOObjectStore and not an EOObjectStoreCoordinator, because it's possible to substitute a custom object store in place of an object store coordinator. Similarly, the EOObjectStoreCoordinator method
objectStoreForFetchSpecification
returns an EOCooperatingObjectStore instead of an EODatabaseContext because it's possible to substitute a custom cooperating object store in place of a database context. If your code performs any such substitutions, you should alter the above code example to match your custom object store's API. See the class specifications for EOObjectStore, EOObjectStoreCoordinator, and EOCooperatingObjectStore for more information.

The EODatabaseContext maintains a link to its EOAdaptorContext from which the code gets the EOAdaptor. To get the EOAdaptorChannel, the code invokes
availableChannel
on the EODatabaseContext, which creates an EODatabaseChannel and an EOAdaptorChannel if they don't already exist.

###  Accessing Multiple Adaptor Sublayer Objects

An EOEditingContext's EOObjectStoreCoordinator can have more than one set of database and adaptor sublayer objects. Consequently, to get a database context from the object store coordinator, you have to provide information that the coordinator can use to choose the correct database context. The code example above provides an EOFetchSpecification using the method
objectStoreForFetchSpecification
, but you could specify different criteria by using one of the following EOObjectStoreCoordinator methods instead:

|   Method |   Description |
| --- | --- |
|    cooperatingObjectStores |   Returns an array of the EOObjectStoreCoordinator's cooperating object stores. |
|    objectStoreForGlobalID |   Returns the cooperating object store for the enterprise object identified by the provided EOGlobalID |
|    objectStoreForObject |   Returns the cooperating object store for the provided enterprise object. |

After you have the database context, you can get the corresponding EOAdaptor and EOAdaptorContext as shown in the example above.

###  Accessing Adaptor Layer Objects From a Display Group

If you are using a display group and a corresponding EODatabaseDataSource, the code to access the adaptor layer objects is a little simpler.

```

WODisplayGroup myDisplayGroup;   // Assume exists
EOAdaptorContext myAdaptorContext;
EOAdaptor myAdaptor;

EODatabaseDataSource ds = (EODatabaseDataSource)myDisplayGroup.dataSource();
EODatabaseContext dbContext = ds.databaseContext();
EODatabaseChannel dbChannel = dbContext.availableChannel();

myAdaptorContext = dbContext().adaptorContext();
myAdaptor = myAdaptorContext.adaptor();
myAdaptorChannel = dbChannel.adaptorChannel();
```


The code first gets the display group's EODatabaseDataSource. From there it finds the display group's EODatabaseContext.

##  See Also

- 

  [Creating Adaptor Sublayer Objects and Connecting Them to the Server](Creating%20Adaptor%20Sublayer%20Objects%20and%20Connecting%20Them%20to%20the%20Server.md#apple-ge3tknrv)

##  Questions

- 

  How do I access adaptor sublayer objects?

##  Keywords

- 

  EOAdaptor
- 

  EOEditingContext
- 

  Adaptor Sublayer

##  Revision History

10 March 1999. Clif Liu. First Draft.

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.2f.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.31.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
