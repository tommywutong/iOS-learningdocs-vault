---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.33.html
archived_at: '2026-07-15T08:14:53.249755Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.32.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.34.md)

#   Accessing Schema Information from the Database Server

##  Synopsis

Explains how to determine table and column information from the database server using the adaptor sublayer.

##  Discussion

You can read schema information from the database server with the EOAdaptorChannel "describe" methods:

- 

  describeTableNames
- 

  describeModelWithTableNames
- 

  describeStoredProcedureNames

The

describeTableNames
method reads and returns an array of table names from the database. The
describeModelWithTableNames
method constructs an EOModel out of the database's metadata, and assigns the adaptor name and connection dictionary to the new EOModel. You generally invoke
describeModelWithTableNames
with the array of table names (or a subset) returned from
describeTableNames
. The
describeStoredProcedureNames
method reads an array of stored procedure names from the database. You can then use
addStoredProceduresNamed (addStoredProceduresNamed:toModel:
in Objective-C) to add the corresponding stored procedures to a model. The following code shows how to open an adaptor and get the database schema from it.

####  Accessing a schema from the server (Java)

```

EOAdaptor myAdaptor = EOAdaptor.adaptorWithName("OpenBaseLite");
EOAdaptorContext myContext = myAdaptor.createAdaptorContext();
EOAdaptorChannel myChannel = myContext.createAdaptorChannel();

/* The connection dictionary is adaptor and database dependent */
NSMutableDictionary connDict = new NSMutableDictionary();
connDict.setObjectForKey("Movies","DATABASENAME");
connDict.setObjectForKey("/Local/Library/Databases","PATH");

myAdaptor.setConnectionDictionary(connDict);
try {
    myAdaptor.assertConnectionDictionaryIsValid();
} catch (NSException exception) {
    /* handle bad connection dictionary */
}

myChannel.openChannel();

NSArray tableNames = myChannel.describeTableNames();
EOModel myModel = myChannel.describeModelWithTableNames(tableNames);

NSArray storedProcNames = myChannel.describeStoredProcedureNames();
myChannel.addStoredProceduresNamed(storedProcNames,myModel);

myChannel.closeChannel();
```


The code first builds a connection dictionary to connect to the database with. Then it attempts to verify the connection dictionary using
assertConnectionDictionaryIsValid
. If the connection attempt fails, the method raises an exception. Otherwise the code opens the connection to the database and gets the table names and stored procedures.

Note that the keys for the connection dictionary depend on the particular adaptor and database server you are using. You can view the connection dictionary for a database using EOModeler in the following way.

Build a model for your database in EOModeler by invoking the File->New menu item.

1. 

   When you are finished, inspect the model by selecting it in the tree view and clicking the inspector button.

##  See Also

- 

  [Creating Adaptor Sublayer Objects and Connecting Them to the Server](Creating%20Adaptor%20Sublayer%20Objects%20and%20Connecting%20Them%20to%20the%20Server.md#apple-ge3tknrv)

##  Questions

- 

  How do I access database schema information from the database server?
- 

  How do I create EOAdaptor layer objects without a model?

##  Keywords

- 

  Adaptor
- 

  Model
- 

  Schema
- 

  Connection Dictionary
- 

  Stored Procedure

##  Revision History

9 February, 1999. Clif Liu. First Draft.

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.32.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.34.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
