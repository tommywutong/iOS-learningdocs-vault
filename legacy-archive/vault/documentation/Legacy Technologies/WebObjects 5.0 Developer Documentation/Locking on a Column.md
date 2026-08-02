---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.2b.html
archived_at: '2026-07-15T08:14:52.647653Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.2a.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.2c.md)

#   Locking on a Column

##  Synopsis

Describes a locking approach that uses a single column to lock records.

##  Discussion

A single database column that contains locking state information can be useful in certain situations. Sometimes an object must be locked for a long period. Optimistic or pessimistic locking won't work in this case because when an application saves or reverts an object, the object is released. For these cases you should add a column whose value changes when the object is locked.

Locking on a column is normally used with optimistic or pessimistic locking to ensure that only one user can update the locking column. For example, if you are using optimistic locking, the locking column should be selected as a locking attribute in EOModeler. This step ensures that when the user tries to save the object no one else has already locked it.

Setting the lock on the column can be somewhat tricky. To lock the object you should create a separate EOEditingContext and use that context to update the record for the lock object. An separate editing context is needed because if other objects have been modified in the main EOEditingContext they would also be saved along with the lock object. A simple way to lock and unlock objects is to add the following two methods to your enterprise objects and only invoke them before any modifications are made to the object.

```objc

- (void)lock
{
    EOEditingContext *aContext;
    id lockingObject;
    aContext = [[EOEditingContext alloc] init];
    lockingObject = [aContext faultForGlobalId:[[self editingContext]         globalIDForObject:self] editingContext:aContext];
    [lockingObject setLock:@"Y"];
    [aContext saveChanges];
    [aContext release];
}
- (void)unlock
{
    EOEditingContext *aContext;
    id lockingObject;
    aContext = [[EOEditingContext alloc] init];
    lockingObject = [aContext faultForGlobalId:[[self editingContext]         globalIDForObject:self] editingContext:aContext];
    [lockingObject setLock:@"N"];
    [aContext saveChanges];
    [aContext release];
}
```


###  Using a Boolean Column

The simplest way to lock an object is to use a simple Boolean column. This can be a single bit (0 or 1) or a single char (Y or N). This approach preserves table space but gives you no way to know who locked the record or when they locked it.

###   Using a Date in the Locked Column

You can also create a date column that is set to the current date when the object is lock and to NULL when the object is not locked. This technique enables you to determine when the object was locked. It can enable you to implement automatic lock removal after a specific period has elapsed. This technique, however, takes up more table space than a Boolean and it does not give you a way to determine who locked the record.

###   Using a User Identifier

You can also set the locked column to be the user name or user ID of the user who locked the column (NULL otherwise). This approach allows you to determine who locked the object. It also gives you a way to allow them access to this object across different instances of an application. However, this approach also takes up more table space than a Boolean and it gives you no way to know when the record was locked.

###  Combining a User Identifier and a Date

You can combine two columns for locking, one to store the user ID (or name) and the other to store the date. This technique combines the strengths of the two approaches described earlier ("[Using a Date in the Locked Column](#apple-gi4tqmrt)
" and "[Using a User Identifier](#apple-gm4dinbz)
"). However, it requires more table space than all the other options.

##  See Also

- 

  [Choosing an Approach for Locking](Choosing%20an%20Approach%20for%20Locking.md#apple-ge2tmmjy)
- 

  [Optimistic Locking](Optimistic%20Locking.md#apple-ge4donrq)
- 

  [Pessimistic Locking](Pessimistic%20Locking.md#apple-ge2dgmrw)

##  Questions

- 

  What is locking?
- 

  How do I lock an object for a long period?
- 

  How do I keep an object locked across different instances or transactions?
- 

  How do I specify who has locked a record?
- 

  How do I specify when a record was locked?

##  Keywords

- 

  Lock
- 

  Column

##  Revision History

22 July, 1998. Paul Haddad. First Draft.

18 November, 1998. Terry Donoghue. Second Draft.


```

```

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.2a.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.2c.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
