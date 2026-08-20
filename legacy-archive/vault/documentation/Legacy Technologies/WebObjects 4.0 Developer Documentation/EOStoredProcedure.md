---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOStoredProcedure.html
archived_at: '2026-07-18T01:28:10.876498Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOSQLQualifier.md)
[!](EOAdaptorChannel.Delegate.md)

---

# EOStoredProcedure

__Inherits From:__
NSObject

[EOPropertyListEncoding](EOPropertyListEncoding.md)

__Inherits From:__
com.apple.yellow.eoaccess

---

## Class Description

An EOStoredProcedure represents a stored procedure defined in a database, and associates a name internal to the Framework with an external name by which the stored procedure is known to the database. If a stored procedure has arguments, its EOStoredProcedure object also maintains a group of EOAttributes which represent the stored procedure's arguments. See the [EOAttribute](EOAttribute.md) class specification for more information

You usually define stored procedures in your EOModel with the EOModeler application, which is documented in the _Enterprise Objects Framework Developer's Guide_. EOStoredProcedures are primarily used by the Enterprise Objects Framework to map operations for an EOEntity to stored procedures (see the description for EOEntity's [`setStoredProcedure`](EOEntity.md#apple-hezti) method). You can assign stored procedures to an entity for any of the following scenarios:

- Fetching all the objects for the entity
- Fetching a single object by its primary key
- Inserting a new object
- Deleting an object
- Generating a new primary key

Your code probably won't use EOStoredProcedures unless you're working at the adaptor level.

Like the other major modeling classes, EOStoredProcedure provides a user dictionary for your application to store any application-specific information related to the stored procedure.

**[EOPropertyListEncoding](EOPropertyListEncoding.md)**

**[awakeWithPropertyList](EOPropertyListEncoding.md#apple-hazto)

**[encodeIntoPropertyList](EOPropertyListEncoding.md#apple-ha3di)****

---

## Method Types

**Constructors**

**[EOStoredProcedure](#apple-ge4dmmi)**

**Accessing the model**

**[model](#apple-ge4deoi)**

**Accessing the name**

**[setName](#apple-gizdc)

**[beautifyName](#apple-ge4dina)

**[name](#apple-ge4dcna)******

**Accessing the external name**

**[setExternalName](#apple-gizdcna)

**[externalName](#apple-ge4to)****

**Accessing the arguments**

**[setArguments](#apple-giytkna)

**[arguments](#apple-gi2dany)****

**Accessing the user dictionary**

**[setUserInfo](#apple-gizdk)

**[userInfo](#apple-gizds)****

---

## Constructors

---

### EOStoredProcedure

public `next.eo.EOStoredProcedure`()

Creates and returns a new EOStoredProcedure.

public `next.eo.EOStoredProcedure`(java.lang.String _name_)

Creates and returns a new EOStoredProcedure named _name_.

public `next.eo.EOStoredProcedure`(next.util.ImmutableHashtable _propertyList_, java.lang.Object _owner_)

Creates and returns a new EOStoredProcedure initialized from _propertyList_-a dictionary containing only property list data types (that is, String, NSDictionary, NSArray, and NSData). This constructor is used by EOModeler when it reads in an EOModel object from a file, for example. The _owner_ argument should be the EOStoredProcedure's EOModel. EOStoredProcedures created from a property list must receive an [`awakeWithPropertyList`](../Protocols/EOPropertyListEncoding.md#apple-hazto) message immediately after creation before they are fully functional, but the `awake...` message should be deferred until the all of the other objects in the model have also been created.

__See also:__
[`awakeWithPropertyList`](../Protocols/EOPropertyListEncoding.md#apple-hazto) (PropertyListEncoding), [`encodeIntoPropertyList`](../Protocols/EOPropertyListEncoding.md#apple-ha3di)
(PropertyListEncoding) [`setName`](#apple-gizdc), [`name`](#apple-ge4dcna)

---

## Instance Methods

---

### arguments

 public next.util.ImmutableVector `arguments`()

Returns the EOAttribute objects that describe the stored procedure's arguments or `null` if the stored procedure has no arguments.

---

### beautifyName

 public void `beautifyName`()

Renames the receiver's name and its arguments to conform to the Framework's naming conventions. For example, "NAME" is renamed "name" and "FIRST_NAME" is renamed "firstName". This method is used in reverse-engineering a model.

__See also:__
[`setArguments`](#apple-giytkna), [`beautifyNames`](EOModel.md#apple-gqzde) (EOModel)

---

### externalName

public java.lang.String `externalName`()

Returns the name of the stored procedure as it is defined in the database, or `null` if the receiver doesn't have an external name.

__See also:__
[`setExternalName`](#apple-gizdcna)

---

### model

 public next.eo.Model `model`()

Returns the model to which the receiver belongs.

__See also:__
[`addStoredProcedure`](EOModel.md#apple-gqytq)(EOModel)

---

### name

 public java.lang.String `name`()

Returns the name of the receiver.

__See also:__
[`setName`](#apple-gizdc), ["Constructors"](#apple-ge4dkoi)

---

### setArguments

public void `setArguments`(next.util.ImmutableVector _arguments_)

Sets _arguments_ as the array of EOAttributes that describe the receiver's arguments. The EOAttribute objects in _arguments_ must be ordered to match the database stored procedure definition.

__See also:__
[`arguments`](#apple-gi2dany)

---

### setExternalName

public void `setExternalName`(java.lang.String _name_)

Sets the external name of the stored procedure to _name_. _name_ should be the name of the stored procedure as it is defined in the database.

__See also:__
[`externalName`](#apple-ge4to)

---

### setName

public void `setName`(java.lang.String _name_)

Sets the name of the receiver.

__See also:__
[`name`](#apple-ge4dcna), ["Constructors"](#apple-ge4dkoi)

---

### setUserInfo

public void `setUserInfo`(next.util.ImmutableHashtable _dictionary_)

Sets the _dictionary_ of auxiliary data, which your application can use for whatever it needs. _dictionary_ can only contain property list data types (that is, String, NSDictionary, NSArray, and NSData).

__See also:__
[`userInfo`](#apple-gizds)

---

### userInfo

public next.util.ImmutableHashtable `userInfo`()

Returns a dictionary of user data. Your application can use this to store any auxiliary information it needs.

__See also:__
[`setUserInfo`](#apple-gizdk)

---

[!](EOSQLQualifier.md)
[!](EOAdaptorChannel.Delegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
