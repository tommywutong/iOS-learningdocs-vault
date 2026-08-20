---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/InsertAdaptor.html
archived_at: '2026-07-15T08:01:14.436888Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Inserting with the Adaptor Layer

##  Synopsis

Describes how to insert a row into the database using the adaptor level.

##  Description

The adaptor level is a server-independent interface for working with the relational database consisting of an EOAdaptor, an EOAdaptorContext and an EOAdaptorChannel. In this level, the database rows are represented as instances of NSDictionary.

The EOAdaptor manages the EOModel, a model that maps the tables and relationships in the database to EOF objects. The EOAdaptor is also responsible for instantiating the correct subclass for the database specific adaptor layer. The EOAdaptorContext manages the database transactions. The EOAdaptorChannel does all the inserts, updates, and deletes, as well as executing SQL. Before you send any SQL to the database, you need to:

· Create an EOAdaptor for the database.

· Create an EOAdaptorContext from the EOAdaptor.

· Create an EOAdaptorChannel from the EOAdaptorContext.

· Open the EOAdaptorChannel.

To insert into the database at the adaptor level, the row should be stored in a NSDictionary where the keys are NSStrings containing the database-dependent attributes, and the values are their corresponding values.

The keys representing the attributes depend on the database. In ODBC, the keys are the column names. For example, in Oracle, the first column to which the SQL _INSERT_
refers has the key "Attribute0", the second column has the key "Attribute1" and so on.

The following code inserts a row using the adaptor level.

#####  Figure 1. Objective-C Code

```objc
- (void) rawInsert:(EOEditingContext *)ec forModelNamed:(NSString *)
```



```
    modelName forEntityNamed:(NSString *)entityName
```



```
    dictionary:(NSDictionary *)dict
```



```
{
```



```
    EOModel *myModel;
```



```
    EOEntity *myEntity;
```



```

```



```
    EOAdaptor *myAdaptor;
```



```
    EOAdaptorContext *myAdaptorContext;
```



```
    EOAdaptorChannel *myAdaptorChannel;
```



```

```



```
    // get the model, entity describing table to insert into
```



```
    myModel = [[ec modelGroup] modelNamed:modelName];
```



```
    myEntity = [ec entityNamed:entityName];
```



```

```



```
    // get the adaptor, adaptor context, and adaptor channel
```



```
    myAdaptor = [EOAdaptor adaptorWithModel:myModel];
```



```
    myAdaptorContext = [myAdaptor createAdaptorContext];
```



```
    myAdaptorChannel = [myAdaptorContext createAdaptorChannel];
```



```

```



```
    // insert row into the database
```



```
    [myAdaptorChannel openChannel];
```



```
    [myAdaptorChannel insertRow:dict forEntity:myEntity];
```



```
    [myAdaptorChannel closeChannel];
```



```
}
```


The insertion can fail for the following reasons:

· The
EOAdaptorChannel is not open.

· The user logged on to the database does not have permission to insert a row.

· The EOAdaptorChannel is in an invalid state (for example, when a fetch is in progress).

· The inserted row fails to satisfy constraints defined in the database.

· The primary key is missing or has an improper value.

##  See Also

· Updating Objects at the Adaptor Level

· Deleting Objects at the Adaptor Level

· When to Choose the Adaptor Level to Improve Performance

· Executing Arbitrary SQL Statements

· EOAdaptor

· EOAdaptorContext

· EOAdaptorChannel

##  Questions

· How do I insert a row using the adaptor level?

· How do I access the adaptor level?

· How can I improve performance?

##  Keywords

· Insert row

· Adaptor

· Performance

##  Revision History

22 July, 1998. Seejo Pylappan. First Draft.
13 November, 1998. Clif Liu. Second Draft.

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
