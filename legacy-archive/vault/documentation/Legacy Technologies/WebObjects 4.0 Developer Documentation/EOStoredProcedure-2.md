---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOStoredProcedure.html
archived_at: '2026-07-18T01:28:17.598620Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOSQLQualifier-2.md)
[!](NSString%20Additions.md)

---

# EOStoredProcedure

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
EOAccess/EOStoredProcedure.h

---

## Class Description

An EOStoredProcedure represents a stored procedure defined in a database, and associates a name internal to the Framework with an external name by which the stored procedure is known to the database. If a stored procedure has arguments, its EOStoredProcedure object also maintains a group of EOAttributes which represent the stored procedure's arguments. See the [EOAttribute](EOAttribute-2.md) class specification for more information

You usually define stored procedures in your EOModel with the EOModeler application, which is documented in the _Enterprise Objects Framework Developer's Guide_. EOStoredProcedures are primarily used by the Enterprise Objects Framework to map operations for an EOEntity to stored procedures (see the description for EOEntity's [`setStoredProcedure:forOperation:`](EOEntity.md#apple-hezti) method). You can assign stored procedures to an entity for any of the following scenarios:

- Fetching all the objects for the entity
- Fetching a single object by its primary key
- Inserting a new object
- Deleting an object
- Generating a new primary key

Your code probably won't use EOStoredProcedures unless you're working at the adaptor level.

Like the other major modeling classes, EOStoredProcedure provides a user dictionary for your application to store any application-specific information related to the stored procedure.

---

## Method Types

**Creating a new EOStoredProcedure**

**[- initWithName:](#apple-gqytinq)**

**Accessing the model**

**[- model](#apple-ge4deoi)**

**Accessing the name**

**[- setName:](#apple-gizdc)

**[- beautifyName](#apple-ge4dina)

**[- name](#apple-ge4dcna)******

**Accessing the external name**

**[- setExternalName:](#apple-gizdcna)

**[- externalName](#apple-ge4to)****

**Accessing the arguments**

**[- setArguments:](#apple-giytkna)

**[- arguments](#apple-gi2dany)****

**Accessing the user dictionary**

**[- setUserInfo:](#apple-gizdk)

**[- userInfo](#apple-gizds)****

---

## Instance Methods

---

### arguments

- (NSArray \*)__arguments__

Returns the EOAttribute objects that describe the stored procedure's arguments or `nil` if the stored procedure has no arguments.

---

### beautifyName

- (void)__beautifyName__

Renames the receiver's name and its arguments to conform to the Framework's naming conventions. For example, "NAME" is renamed "name" and "FIRST_NAME" is renamed "firstName".

__See also:__
[- `setArguments:`](#apple-giytkna), [- `beautifyNames`](EOModel.md#apple-gqzde) (EOModel)

---

### externalName

- (NSString \*)__externalName__

Returns the name of the stored procedure as it is defined in the database, or `nil` if the receiver doesn't have an external name.

__See also:__
[- `setExternalName:`](#apple-gizdcna)

---

### initWithName:

- (EOStoredProcedure \*)__initWithName:__ (NSString \*)_name_

The designated initializer for EOStoredProcedure, this method initializes a new EOStoredProcedure object and sets its name to _name_. Returns `self`.

__See also:__
[- `setName:`](#apple-gizdc), [- `name`](#apple-ge4dcna)

---

### model

- (EOModel \*)__model__

Returns the model to which the receiver belongs.

__See also:__
[- `addStoredProcedure:`](EOModel.md#apple-gqytq)(EOModel)

---

### name

- (NSString \*)__name__

Returns the name of the receiver.

__See also:__
[- `setName:`](#apple-gizdc), [- `initWithName:`](#apple-gqytinq)

---

### setArguments:

- (void)__setArguments:__ (NSArray \*)_arguments_

Sets _arguments_ as the array of EOAttributes that describe the receiver's arguments. The EOAttribute objects in _arguments_ must be ordered to match the database stored procedure definition.

__See also:__
[- `arguments`](#apple-gi2dany)

---

### setExternalName:

- (void)__setExternalName:__ (NSString \*)_name_

Sets the external name of the stored procedure to _name_. _name_ should be the name of the stored procedure as it is defined in the database.

__See also:__
[- `externalName`](#apple-ge4to)

---

### setName:

- (void)__setName:__ (NSString \*)_name_

Sets the name of the receiver.

__See also:__
[- `name`](#apple-ge4dcna), [- `initWithName:`](#apple-gqytinq)

---

### setUserInfo:

- (void)__setUserInfo:__ (NSDictionary \*)_dictionary_

Sets the _dictionary_ of auxiliary data, which your application can use for whatever it needs. _dictionary_ can only contain property list data types (that is, NSString, NSDictionary, NSArray, and NSData).

__See also:__
[- `userInfo`](#apple-gizds)

---

### userInfo

- (NSDictionary \*)__userInfo__

Returns a dictionary of user data. Your application can use this to store any auxiliary information it needs.

__See also:__
[- `setUserInfo:`](#apple-gizdk)

---

[!](EOSQLQualifier-2.md)
[!](NSString%20Additions.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
