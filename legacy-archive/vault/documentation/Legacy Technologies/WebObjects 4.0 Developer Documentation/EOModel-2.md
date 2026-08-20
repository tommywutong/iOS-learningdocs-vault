---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOModel.html
archived_at: '2026-07-18T01:28:16.791498Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOLoginPanel-2.md)
[!](Loading%20a%20Model%20File-2.md)

---

# EOModel

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
EOAccess/EOModel.h

---

## Class Description

An EOModel represents a mapping between a database schema and a set of classes based on the entity-relationship model. The model contains a number of EOEntity objects representing the entities (tables) of the database schema. Each [EOEntity](EOEntity-2.md) object has a number of [EOAttribute](EOAttribute-2.md) and [EORelationship](EORelationship-2.md) objects representing the properties (columns or fields) of the entity in the database schema. For more information on attributes and relationships, see their respective class specifications.

An EOModel maintains a mapping between each of its EOEntity objects and a corresponding enterprise object class for use with the database level of the Enterprise Objects Framework. You can determine the EOEntity for a particular enterprise object with the [`entityForObject:`](#apple-gqzto) method.

An EOModel is specific to a particular database server, and stores information needed to connect to that server. This includes the name of an adaptor framework to load so that the Enterprise Objects Framework can communicate with the database. Models are stored in the file system in a manner similar to adaptor framework. EOModel objects are usually loaded from model files built with the EOModeler application rather than built programmatically. If you need to programmatically load a model file, see the discussion in "[Loading a Model File](Loading%20a%20Model%20File-2.md#apple-gm2tgmy)."

Models can have relationships that reference other models in the same model group. The other models may map to different databases and types of servers.

Models are organized into model groups; see the [EOModelGroup](EOModelGroup-2.md) class specification for more information.

---

## Creating an EOModel Programmatically

The EOAdaptorChannel class declares methods for reading basic schema information from a relational database. You can use this information to build up an EOModel programmatically, and then enhance that model by defining extra relationships, flattening attributes, and so on. See the class description in the [EOAdaptorChannel](EOAdaptorChannel-2.md) class specification for information on reading basic schema information, and see the other modeling classes' specifications for information on creating additional attributes and relationships.

---

## Method Types

**Initializing an EOModel instance**

**[- initWithContentsOfFile:](#apple-geydcobv)

**[- initWithTableOfContentsPropertyList:path:](#apple-geydembr)****

**Saving a model**

**[- encodeTableOfContentsIntoPropertyList:](#apple-gqzds)

**[- writeToFile:](#apple-guyts)****

**Loading a model's objects**

**[- loadAllModelObjects](#apple-gq3da)**

**Working with entities**

**[- addEntity:](#apple-gqyti)

**[- removeEntity:](#apple-gq4da)

**[- removeEntityAndReferences:](#apple-gu2tg)

**[- entityNames](#apple-gq2di)

**[- entityNamed:](#apple-gm4tomy)

**[- entities](#apple-gqztg)************

**Naming a model's components**

**[- beautifyNames](#apple-gqzde)**

**Accessing the model's name**

**[- setName:](#apple-gq4tq)

**[- name](#apple-gq3dq)

**[- path](#apple-gq3te)******

**Checking references**

**[- referencesToProperty:](#apple-gmzdmny)

**[- externalModelsReferenced](#apple-gq2dq)****

**Getting an object's entity**

**[- entityForObject:](#apple-gqzto)**

**Accessing the adaptor bundle**

**[- adaptorName](#apple-gqytc)

**[- setAdaptorName:](#apple-gq4do)****

**Accessing the connection dictionary**

**[- setConnectionDictionary:](#apple-gq4ta)

**[- connectionDictionary](#apple-gqzdm)****

**Accessing the user dictionary**

**[- setUserInfo:](#apple-guydc)

**[- userInfo](#apple-guytm)****

**Working with stored procedures**

**[- addStoredProcedure:](#apple-gqytq)

**[- removeStoredProcedure:](#apple-gm2dk)

**[- storedProcedureNames](#apple-guydq)

**[- storedProcedureNamed:](#apple-guydi)

**[- storedProcedures](#apple-guyte)**********

**Accessing the model's group**

**[- setModelGroup:](#apple-gq4tg)

**[- modelGroup](#apple-gq3di)****

---

## Instance Methods

---

### adaptorName

- (NSString \*)`adaptorName`

Returns the name of the adaptor for the receiver. This name can be used with EOAdaptor's [`adaptorWithName:`](EOAdaptor.md#apple-g44di) class method to create an adaptor.

---

### addEntity:

- (void)`addEntity:`(EOEntity \*)_anEntity_

Adds _anEntity_ to the receiver. Raises an NSInvalidArgumentException if an error occurs (for example, if _anEntity_ doesn't exist, if the entity belongs to another model, or if an entity of the same name is already in the receiver).

__See also:__
[- `entities`](#apple-gqztg), [- `removeEntity:`](#apple-gq4da), [- `removeEntityAndReferences:`](#apple-gu2tg)

---

### addStoredProcedure:

- (void)`addStoredProcedure:`(EOStoredProcedure \*)_storedProcedure_

Adds _storedProcedure_ to the receiver. Raises an NSInvalidArgumentException if an error occurs (for example, if a stored procedure of the same name is already in the receiver).

__See also:__
[- `removeStoredProcedure:`](#apple-gm2dk), [- `storedProcedures`](#apple-guyte), [- `storedProcedureNamed:`](#apple-guydi),
[- `storedProcedureNames`](#apple-guydq)

---

### availablePrototypeAttributeNames

- (NSArray \*)`availablePrototypeAttributeNames`

Returns a list of available prototype names.

__See also:__
[- `prototypeAttributeNamed:`](#apple-geydinrr)

---

### beautifyNames

- (void)`beautifyNames`

Makes all of the receiver's named components conform to a standard convention. Names that conform to this style are all lower-case except for the initial letter of each embedded word other than the first, which is upper case. Thus, "NAME" becomes "name", and "FIRST_NAME" becomes "firstName".

__See also:__
, [- `name`](#apple-gq3dq)

---

### connectionDictionary

- (NSDictionary \*)`connectionDictionary`

Returns a dictionary containing information used to connect to the database server. The connection dictionary is the place to specify default login information for applications using the model. See the EOAdaptor class specification for more information.

---

### encodeTableOfContentsIntoPropertyList:

- (void)`encodeTableOfContentsIntoPropertyList:`(NSMutableDictionary \*)_propertyList_

Encodes the receiver into _propertyList_. This method is used to get an ASCII representation of an EOModel in property list format.

__See also:__
[- `initWithTableOfContentsPropertyList:path:`](#apple-geydembr)

---

### entities

- (NSArray \*)`entities`

Returns an array containing the receiver's entities. Note that this method loads every entity, and thus defeats the benefits of incremental model loading.

__See also:__
[- `entityNames`](#apple-gq2di)

---

### entityForObject:

- (EOEntity \*)`entityForObject:`(id)_anEO_

Returns the entity associated with _anEO_, whether _anEO_ is an instance of an enterprise object class, an instance of EOGenericRecord, or a fault object (see the EOFault class specification for information on faults). Returns `nil` if _anEO_ has no associated entity.

---

### entityNamed:

- (EOEntity \*)`entityNamed:`(NSString \*)_name_

Returns the entity named _name_, or `nil` if no such entity exists. Posts an [EOEntityLoadedNotification](#apple-guzdm) when the entity is loaded.

__See also:__
[- `entityNames`](#apple-gq2di), [- `entities`](#apple-gqztg)

---

### entityNames

- (NSArray \*)`entityNames`

Returns an array containing the names of the EOModel's entities.

__See also:__
[- `entities`](#apple-gqztg), [- `entityNamed:`](#apple-gm4tomy)

---

### externalModelsReferenced

- (NSArray \*)`externalModelsReferenced`

Returns an array containing those models that are referenced by this model.

__See also:__
[- `referencesToProperty:`](#apple-gmzdmny)

---

### initWithContentsOfFile:

- `initWithContentsOfFile:`(NSString \*)_path_

Initializes a newly-allocated EOModel by reading the contents of the file named _path_ as a model archive. The file specified by path can either be an old-style (`.eomodel`) or new-style (`.eomodeld`) model file. Sets the EOModel's name and path. `initWithContentsOfFile:` raises an NSInvalidArgumentException if for any reason it cannot initialize the model from the file specified by _path_.

__See also:__
[- `name`](#apple-gq3dq), [- `path`](#apple-gq3te)

---

### initWithTableOfContentsPropertyList:path:

- `initWithTableOfContentsPropertyList:`(NSDictionary \*)_tableOfContents_ `path:`(NSString \*)_path_

Uses _tableOfContents_ (which is the property list representation of an EOModel) with the file name _path_ to initialize the receiver.

__See also:__
[- `encodeTableOfContentsIntoPropertyList:`](#apple-gqzds)

---

### loadAllModelObjects

- (void)`loadAllModelObjects`

Loads any of the receiver's entities, stored procedures, attributes, and relationships that have not yet been loaded.

__See also:__
[- `attributes`](EOEntity.md#apple-g42dm) (EOEntity), [- `entities`](#apple-gqztg), [- `relationships`](EOEntity.md#apple-ha3dm) (EOEntity), [- `storedProcedures`](#apple-guyte)

---

### modelGroup

- (EOModelGroup \*)`modelGroup`

Returns the model group of which the receiver is a part.

__See also:__
[- `setModelGroup:`](#apple-gq4tg)

---

### name

- (NSString \*)`name`

Returns the receiver's name.

__See also:__
[- `path`](#apple-gq3te)

---

### path

- (NSString \*)`path`

Returns the name of the EOModel file used to create the receiver, or `nil` if the model wasn't initialized from a file.

__See also:__
[- `name`](#apple-gq3dq)

---

### prototypeAttributeNamed:

- (EOAttribute \*)`prototypeAttributeNamed:`(NSString \*)_attributeName_

Returns the prototype attribute for the given _attributeName_. [`prototypeAttributeNamed:`](#apple-geydinrr) first looks for the prototype in EO_adaptorName_Prototypes. If the prototype isn't found there, it then looks in EOPrototypes. If the search is still unsuccessful, this method finally looks for the prototype in the list of prototypes provided by the adaptor itself.

__See also:__
[- `availablePrototypeAttributeNames`](#apple-geydimjz)

---

### referencesToProperty:

- (NSArray \*)`referencesToProperty:`(id)_aProperty_

Returns an array of all properties in the receiver that reference _aProperty_, whether derived attributes, relationships that reference _aProperty_, and so on. Returns `nil` if _aProperty_ isn't referenced by any of the properties in the model.

__See also:__
[- `externalModelsReferenced`](#apple-gq2dq)

---

### removeEntity:

- (void)`removeEntity:`(EOEntity \*)_name_

Removes the entity with the given _name_ without performing any referential integrity checking.

__See also:__
[- `addEntity:`](#apple-gqyti)`, [- removeEntityAndReferences:](#apple-gu2tg)`

---

### removeEntityAndReferences:

- (void)`removeEntityAndReferences:`(EOEntity \*)_entity_

Removes _entity_ and any attributes or relationships in other entities that reference entity.

__See also:__
[- `removeEntity:`](#apple-gq4da), [- `addEntity:`](#apple-gqyti)

---

### removeStoredProcedure:

- (void)`removeStoredProcedure:`(EOStoredProcedure \*)_storedProcedure_

Removes _aStoredProcedure_ without checking to see if an entity uses it.

__See also:__
[- `addStoredProcedure:`](#apple-gqytq), `[- storedProcedures](#apple-guyte)`

---

### setAdaptorName:

- (void)`setAdaptorName:`(NSString \*)_adaptorName_

Sets the name of the receiver's adaptor to _adaptorName_.

__See also:__
[`availableAdaptorNames`](EOAdaptor.md#apple-gq3dqmi) (EOAdaptor)

---

### setConnectionDictionary:

- (void)`setConnectionDictionary:`(NSDictionary \*)_connectionDictionary_

Sets the dictionary containing information used to connect to the database to _connectionDictionary_. See the [EOAdaptor](EOAdaptor-2.md) class specification for more information on working with connection dictionaries.

__See also:__
[`adaptorWithModel:`](EOAdaptor.md#apple-gq2tmmi) (EOAdaptor)

---

### setModelGroup:

- (void)`setModelGroup:`(EOModelGroup \*)_group_

Sets the model group of which the receiver should be a part.

__Note:__
You shouldn't change an EOModel's model group after it has been bound to other models in its
group.

__See also:__
[- `modelGroup`](#apple-gq3di)

---

### setName:

- (void)`setName:`(NSString \*)_name_

Sets the name of the receiver to _name_.

---

### setUserInfo:

- (void)`setUserInfo:`(NSDictionary \*)_dictionary_

Sets the _dictionary_ of auxiliary data, which your application can use for whatever it needs. _dictionary_ can only contain property list data types-that is, NSString, NSDictionary, NSArray, and NSData.

---

### storedProcedureNamed:

- (EOStoredProcedure \*)`storedProcedureNamed:`(NSString \*)_name_

Returns the stored procedure named _name_, or `nil` if the model doesn't contain a stored procedure with the given name.

__See also:__
[- `storedProcedureNames`](#apple-guydq), [- `storedProcedures`](#apple-guyte)

---

### storedProcedureNames

- (NSArray \*)`storedProcedureNames`

Returns an array containing the names of all of the model's stored procedures.

__See also:__
[- `storedProcedureNamed:`](#apple-guydi), [- `storedProcedures`](#apple-guyte)

---

### storedProcedures

- (NSArray \*)`storedProcedures`

Returns an array containing all of the model's stored procedures. Note that this method loads each of the model's stored procedures, thus defeating the benefits of incremental model loading.

__See also:__
[- `storedProcedureNames`](#apple-guydq), [- `storedProcedureNamed:`](#apple-guydi)

---

### userInfo

- (NSDictionary \*)`userInfo`

Returns a dictionary of user data. You can use this to store any auxiliary information it needs.

__See also:__
[- `setUserInfo:`](#apple-guydc)

---

### writeToFile:

- (void)`writeToFile:`(NSString \*)_path_

Saves the receiver in the directory specified by _path_. If the file specified by path already exists, a backup copy is first created (using path with a "~" character appended). As a side-effect, this method resets the current path.

`writeToFile:` raises an NSInvalidArgumentException on any error which prevents the file from being written.

__See also:__
[- `path`](#apple-gq3te)

---

# Notifications

EOModel declares and posts the following notification.

---

### EOEntityLoadedNotification

Posted after an EOEntity is loaded into memory. The notification contains:

| Notification Object | The entity that was loaded. |
| Userinfo | None |

```
```

****

---

[!](EOLoginPanel-2.md)
[!](Loading%20a%20Model%20File-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
