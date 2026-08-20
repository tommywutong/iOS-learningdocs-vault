---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.25.html
archived_at: '2026-07-15T08:14:52.479272Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.24.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.26.md)

#   Deleting with the Adaptor Sublayer

##  Synopsis

Describes how to delete a row from the database using the adaptor sublayer.

##  Description

There are three ways to delete a row into the database with the adaptor sublayer. You can use raw SQL employing the adaptor channel's
evaluateExpression
method, the adaptor channel's deleteRowDescribedByQualifier method, or a stored procedure.

In this topic we describe how to delete a row using the deleteRowDescribedByQualifier method. This method eliminates the overhead associated with snapshots, uniquing, and fault creation. Furthermore, the source code does not depend on the particular database you use.

If you are working with an editing context and deleting using the adaptor sublayer at the same time, EOF does not realize that an objected has been deleted. You need to synchronize any enterprise objects with the changes to the database.

To delete a row using the adaptor channel's deleteRowDescribedByQualifier method, you need to provide

- 

  An EOModel mapping entities to database tables.
- 

  An adaptor channel that is connected to the database. (See the programming topics [Accessing Adaptor Sublayer Objects](Accessing%20Adaptor%20Sublayer%20Objects.md#apple-gi3tanbu)
  , [Creating Adaptor Sublayer Objects and Connecting Them to the Server](Creating%20Adaptor%20Sublayer%20Objects%20and%20Connecting%20Them%20to%20the%20Server.md#apple-ge3tknrv)
  , and [Accessing Schema Information from the Database Server](Accessing%20Schema%20Information%20from%20the%20Database%20Server.md#apple-gi2denrx)
  for more information about getting an adaptor channel.
- 

  The name of the entity from which you wish to delete, for example, "
  Movie
  ".
- 

  An EOQualifier specifying which row to delete. See the programming topic [Creating EOQualifiers Programmatically](Creating%20EOQualifiers%20Programmatically.md#apple-giytemrr)
  for more information about creating qualifiers.

The following code deletes a row using the adaptor sublayer.

```

EOAdaptorChannel myAdaptorChannel; // assume exists
String modelName = "movies";
String entityName = "Movie";

EOQualifier myQualifier = EOQualifier.qualifierWithQualifierFormat
    ("title = 'EOF III: The Multithreading'");

EOModel myModel = EOModelGroup.defaultGroup().modelNamed(modelName)
EOEntity myEntity = myModel.entityNamed(entityName);

// delete row
myAdaptorChannel.openChannel();
myAdaptorChannel.deleteRowsDescribedByQualifier(myQualifier,myEntity);
myAdaptorChannel.closeChannel();
```


The code first creates the qualifier that identifies the row you wish to delete.

The code then finds the EOModel corresponding to the model name in the default model group. The default model group, accessed using
EOModelGroup.defaultGroup()
is a collection of EOModel objects corresponding to the models in the project's Resources suitcase. If you already have the EOModel, you don't need this step. Next, the code determines the EOEntity corresponding to the given entity name from the EOModel.

Before performing deleteRowsDescribedByQualifier with the adaptor channel, the code establishes a connection to the database using the
openChannel
method. The
closeChannel
method invocation disconnects the channel from the database.

###  Deleting Multiple Rows

The deleteRowDescribedByQualifier method deletes a single row from the database. If the qualifier matches more than one row, the method deletes the matching rows and raises an exception. If you need to delete more than one row, use the deleteRowsDescribedByQualifier which will not raise an exception when multiple rows match the qualifier. This method also returns the number of rows that were deleted.

###  Deletion Failures

The deletion can fail for the following reasons:

- 

  The user logged on to the database does not have permission to delete the row.
- 

  The EOAdaptorChannel is in an invalid state for inserting, for example, a fetch is in progress. To test if a fetch is in progress, use the adaptor channel's
  isFetchInProgress
  method.

##  See Also

- 

  [Accessing Adaptor Sublayer Objects](Accessing%20Adaptor%20Sublayer%20Objects.md#apple-gi3tanbu)
- 

  [Creating Adaptor Sublayer Objects and Connecting Them to the Server](Creating%20Adaptor%20Sublayer%20Objects%20and%20Connecting%20Them%20to%20the%20Server.md#apple-ge3tknrv)
- 

  [Accessing Schema Information from the Database Server](Accessing%20Schema%20Information%20from%20the%20Database%20Server.md#apple-gi2denrx)
- 

  [Inserting with the Adaptor Sublayer](Inserting%20with%20the%20Adaptor%20Sublayer.md#apple-gm3dgnbu)
- 

  [Updating with the Adaptor Sublayer](Updating%20with%20the%20Adaptor%20Sublayer.md#apple-geydcnju)
- 

  [Executing Arbitrary SQL Statements](Executing%20Arbitrary%20SQL%20Statements.md#apple-gm2tgmjz)
- 

  EOQualifier class specification in the _Enterprise Objects Framework Reference_
- 

  EOAdaptor class specification in the _Enterprise Objects Framework Reference_
- 

  EOAdaptorContext class specification in the _Enterprise Objects Framework Reference_
- 

  EOAdaptorChannel class specification in the _Enterprise Objects Framework Reference_

##  Questions

- 

  How do I delete an object using the adaptor sublayer?
- 

  How do I delete an array of objects described by a qualifier?

##  Keywords

- 

  Delete Row

##  Revision History

22 July, 1998. Seejo Pylappan. First Draft.

13 November, 1998. Clif Liu. Second Draft.

16 March, 1999. Clif Liu. Third Draft.

```

```

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.24.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.26.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
