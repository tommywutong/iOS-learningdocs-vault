---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/DeleteAdaptor.html
archived_at: '2026-07-15T08:01:03.943905Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Deleting with the Adaptor Level

##  Synopsis

Describes how to delete a row from the database using the adaptor level.

##  Description

The adaptor level is a server-independent interface for working with the relational database consisting of an EOAdaptor, an EOAdaptorContext and an EOAdaptorChannel. In this level, the database rows are represented as instances of NSDictionary.

The EOAdaptor manages the EOModel, a model that maps the tables and relationships in the database to EOF objects. The EOAdaptor is also responsible for instantiating the correct subclass for the database specific adaptor layer. The EOAdaptorContext manages the database transactions. The EOAdaptorChannel does all the inserts, updates, and deletes, as well as executing SQL. Before you send any SQL to the database, you need to:

· Create an EOAdaptor for the database.

· Create an EOAdaptorContext from the EOAdaptor.

· Create an EOAdaptorChannel from the EOAdaptorContext.

· Open the EOAdaptorChannel.

To update the database at the adaptor level, you need to specify an EOQualifier which specifies the row to delete. The following code uses the adaptor level to delete a row from the database.

#####  Figure 1. Objective-C Code

```objc
- (void) rawDelete:(EOEditingContext *)ec forModelNamed:(NSString *)
```



```
    modelName forEntityNamed:(NSString *)entityName withQualifierString:
```



```
    (NSString *)qualString
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
    EOQualifier *myQualifier;
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
    // get the model, entity, and qualifier describing row to update
```



```
    myModel = [[ec modelGroup] modelNamed:modelName];
```



```
    myEntity = [ec entityNamed:entityName];
```



```
    myQualifier = [EOQualifier qualifierWithQualifierFormat:qualString];
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
    // delete the row from the database
```



```
    [myAdaptorChannel openChannel];
```



```
    [myAdaptorChannel deleteRowDescribedByQualifier:myQualifier
```



```
        entity:myEntity];
```



```
    [myAdaptorChannel closeChannel];
```



```
}
```


The deletion can fail for the following reasons:

· The EOAdaptorChannel is not open.

· The user logged on to the database does not have permission to update the row.

· The EOAdaptorChannel is in an invalid state (for example, when a fetch is in progress).

· The updated row fails to satisfy constraints defined in the database.

##  See Also

· Inserting in the Adaptor Layer

· Updating in the Adaptor Layer

· When to Choose the Adaptor Level to Improve Performance

· Executing Arbitrary SQL Statements

· EOQualifier

· EOAdaptor

· EOAdaptorContext

· EOAdaptorChannel

##  Questions

· How do I delete an object using the adaptor level?

· How do I delete an array of objects described by a qualifier?

· How do I access the adaptor level?

· How can I improve performance?

##  Keywords

· Delete Row

##  Revision History

22 July, 1998. Seejo Pylappan. First Draft.
13 November, 1998. Clif Liu. Second Draft.

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
