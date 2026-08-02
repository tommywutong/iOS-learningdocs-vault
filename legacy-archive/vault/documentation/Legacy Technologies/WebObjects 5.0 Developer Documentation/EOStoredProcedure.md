---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOStoredProcedure.html
archived_at: '2026-07-15T08:13:41.791298Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOStoredProcedure

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : EOPropertyListEncoding:

> **__Package:__**
> : com.webobjects.eoaccess

---

## Class Description

---

An EOStoredProcedure represents a stored procedure defined in a database, and associates a name internal to the Framework with an external name by which the stored procedure is known to the database. If a stored procedure has arguments, its EOStoredProcedure object also maintains a group of EOAttributes which represent the stored procedure's arguments. See the EOAttribute class specification for more information

You usually define stored procedures in your EOModel with the EOModeler application, which is documented in the _Enterprise Objects Framework Developer's Guide_. EOStoredProcedures are primarily used by the Enterprise Objects Framework to map operations for an EOEntity to stored procedures (see the description for EOEntity's setStoredProcedure method). You can assign stored procedures to an entity for any of the following scenarios:

- Fetching all the objects for the entity
- Fetching a single object by its primary key
- Inserting a new object
- Deleting an object
- Generating a new primary key

Your code probably won't use EOStoredProcedures unless you're working at the adaptor level.

Like the other major modeling classes, EOStoredProcedure provides a user dictionary for your application to store any application-specific information related to the stored procedure.

## Interfaces Implemented

---

> EOPropertyListEncoding: awakeWithPropertyList: encodeIntoPropertyList

## Method Types

---

> **Constructors**
> : [EOStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5cu6u3un5zgkzcqojxwgzleovzgk)
>
> **Accessing the model**
> : [model](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5ww6zdfnq)
>
> **Accessing the name**
> : [setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5comfwwk): [beautifyName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5rgkylvoruwm6komfwwk): [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5xgc3lf)
>
> **Accessing the external name**
> : [setExternalName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5cfpb2gk4tomfwe4ylnmu): [externalName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5sxq5dfojxgc3comfwwk)
>
> **Accessing the arguments**
> : [setArguments](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5cbojtxk3lfnz2hg): [arguments](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5qxez3vnvsw45dt)
>
> **Accessing the user dictionary**
> : [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5cvonsxeslomzxq): [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff52xgzlsjfxgm3y)

## Constructors

---

### EOStoredProcedure

`public EOStoredProcedure(String name)`

Description forthcoming.

`public EOStoredProcedure( NSDictionary propertyList, Object owner)`

Creates and returns a new EOStoredProcedure initialized from _propertyList_-a dictionary containing only property list data types (that is, String, NSDictionary, NSArray, and NSData). This constructor is used by EOModeler when it reads in an EOModel object from a file, for example. The _owner_ argument should be the EOStoredProcedure's EOModel. EOStoredProcedures created from a property list must receive an awakeWithPropertyList message immediately after creation before they are fully functional, but the __awake...__ message should be deferred until the all of the other objects in the model have also been created.

__See Also:__ encodeIntoPropertyList (EOPropertyListEncoding) [setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5comfwwk), [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5xgc3lf)

Creates and returns a new EOStoredProcedure named _name_.

---

## Instance Methods

---

### arguments

`public NSArray arguments()`

Returns the EOAttribute objects that describe the stored procedure's arguments or `null` if the stored procedure has no arguments.

---

### __awakeWithPropertyList__

`public void awakeWithPropertyList(NSDictionary pList)`

Description forthcoming.

---

### beautifyName

`public void beautifyName()`

Renames the receiver's name and its arguments to conform to the Framework's naming conventions. For example, "NAME" is renamed "name" and "FIRST_NAME" is renamed "firstName". This method is used in reverse-engineering a model.

__See Also:__ [setArguments](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5cbojtxk3lfnz2hg), beautifyNames (EOModel)

---

### __encodeIntoPropertyList__

`public void encodeIntoPropertyList(NSMutableDictionary pList)`

Description forthcoming.

---

### externalName

`public String externalName()`

Returns the name of the stored procedure as it is defined in the database, or `null` if the receiver doesn't have an external name.

__See Also:__ [setExternalName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5cfpb2gk4tomfwe4ylnmu)

---

### model

`public EOModel model()`

Returns the model to which the receiver belongs.

__See Also:__ addStoredProcedure (EOModel)

---

### name

`public String name()`

Returns the name of the receiver.

__See Also:__ [setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5comfwwk), [EOStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5cu6u3un5zgkzcqojxwgzleovzgk) constructor

---

### setArguments

`public void setArguments(NSArray arguments)`

Sets _arguments_ as the array of EOAttributes that describe the receiver's arguments. The EOAttribute objects in _arguments_ must be ordered to match the database stored procedure definition.

__See Also:__ [arguments](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5qxez3vnvsw45dt)

---

### setExternalName

`public void setExternalName(String name)`

Sets the external name of the stored procedure to _name_. _name_ should be the name of the stored procedure as it is defined in the database.

__See Also:__ [externalName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5sxq5dfojxgc3comfwwk)

---

### setName

`public void setName(String name)`

Sets the name of the receiver.

__See Also:__ [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5xgc3lf), [EOStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5cu6u3un5zgkzcqojxwgzleovzgk) constructor

---

### setUserInfo

`public void setUserInfo(NSDictionary dictionary)`

Sets the _dictionary_ of auxiliary data, which your application can use for whatever it needs. _dictionary_ can only contain property list data types (that is, String, NSDictionary, NSArray, and NSData).

__See Also:__ [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff52xgzlsjfxgm3y)

---

### __toString__

`public String toString()`

Description forthcoming.

---

### userInfo

`public NSDictionary userInfo()`

Returns a dictionary of user data. Your application can use this to store any auxiliary information it needs.

__See Also:__ [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5cvonsxeslomzxq)

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
