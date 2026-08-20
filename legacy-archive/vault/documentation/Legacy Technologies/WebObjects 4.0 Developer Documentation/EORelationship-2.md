---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EORelationship.html
archived_at: '2026-07-18T01:28:17.138406Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOQualifier%20Additions.md)
[!](Creating%20Relationships-3.md)

---

# EORelationship

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
EOAccess/EORelationship.h

---

## Class Description

An EORelationship describes an association between two entities, based on attributes of those two entities. By defining EORelationships in your application's EOModel, you can cause the relationships defined in the database to be automatically resolved as enterprise objects are fetched. For example, a Movie entity may contain its `studioId` as an attribute, but without an EORelationship `studioId` will only appear in a movie enterprise object as a number. With an EORelationship explicitly connecting the Movie entity to a Studio entity, a movie enterprise object will automatically be given its studio enterprise object when an EODatabaseChannel fetches it from the database. The two entities that make up a relationship can be in the same model or two different models, as long as they are in the same model group.

You usually define relationships in your EOModel with the EOModeler application, which is documented in _WebObjects Tools and Techniques_. EORelationships are primarily for use by the Enterprise Objects Framework; unless you have special needs you shouldn't need to access them in your application's code. If you have such a need, you can create your own EORelationship objects as outlined in "[Creating Relationships](Creating%20Relationships-3.md#apple-gm2tgmy)."

A relationship is directional: One entity is considered the source, and the other is considered the destination. The relationship belongs to the source entity, and may only be traversed from source to destination. To simulate a two-way relationship you have to create an EORelationship for each direction. Although the relationship is directional, no inverse is implied (although an inverse relationship may exist).

A relationship maintains an array of joins identifying attributes from the related entities (see the [EOJoin](EOJoin-2.md) class specification for more information). Most relationships simply relate the objects of one entity to those of another by comparing attribute values between them. Such a relationship must be defined as to-one or to-many based on how many objects of the destination match each object of the source. This is called the _cardinality_ of the relationship. In a to-one relationship, there must be exactly one destination object for each source object; in a to-many relationship there can be any number of destination objects for each source object. See "[Creating a Simple Relationship](Creating%20Relationships-3.md#apple-gm2tqnq)" for more information.

A chain of relationships across several entities can be flattened, creating a single relationship that spans them all. For example, suppose you have a relationship between movies and directors, and a relationship between directors and talent. You can traverse these relationships to create a flattened relationship going directly from movies to talent. A flattened relationship is determined to be to-many or to-one based on the relationships it spans; if all are to-one, then the flattened relationship is to-one, but if any of them is to-many the flattened relationship is to-many. See "[Creating a Flattened Relationship](Creating%20Relationships-3.md#apple-gm2tkni)" for more information.

Like the other major modeling classes, EORelationship provides a user dictionary that the application can use to store application-specific information related to the relationship.

---

## Specifying the Join Semantic

The relationship holds the join semantic; you specify this semantic with [`setJoinSemantic:`](#apple-gyydk). There are four types of join semantic, as specified by the EOJoinSemantic type: [EOInnerJoin](#apple-gu2dk), [EOFullOuterJoin](#apple-gu2dk), [EOLeftOuterJoin](#apple-gu2dk), and [EORightOuterJoin](#apple-gu2dk). An inner join produces results only for destinations of the join relationship that have non-NULL values. A full outer join produces results for all source records, regardless of the values of the relationships. A left outer join preserves rows in the left (source) table, keeping them even if there's no corresponding row in the right table, while a right outer join preserves rows in the right (destination) table.

__Note:__
Not all join semantics are supported by all database servers.

---

# Adopted Protocols

**[EOPropertyListEncoding](EOPropertyListEncoding-2.md)**

**---

#

[- awakeWithPropertyList](EOPropertyListEncoding-2.md#apple-hazto)

**---

#

[- encodeIntoPropertyList:](EOPropertyListEncoding-2.md#apple-ha3di)

**[- initWithPropertyList:owner:](EOPropertyListEncoding-2.md#apple-gi3tgny)******

---

## Method Types

**Accessing the relationship name [- beautifyName](#apple-gq4ta)**

**[- name](#apple-gu2ti)

**[- setName:](#apple-gm3tcna)

**[- validateName:](#apple-gyztm)******

**Using joins**

**[- addJoin:](#apple-gm4dkoa)

**[- joins](#apple-gq4tamy)

**[- joinSemantic](#apple-gu2dk)

**[- removeJoin:](#apple-gu3ts)

**[- setJoinSemantic:](#apple-gyydk)**********

**Accessing attributes joined on**

**[- destinationAttributes](#apple-guyti)

**[- sourceAttributes](#apple-gyzds)****

**Accessing the definition**

**[- componentRelationships](#apple-gq4tq)

**[- definition](#apple-guyde)

**[- setDefinition:](#apple-gu4do)******

**Accessing the entities joined**

**[- anyInverseRelationship](#apple-gq4dm)

**[- destinationEntity](#apple-guytq)

**[- entity](#apple-guzde)

**[- inverseRelationship](#apple-guzdm)

**[- setEntity:](#apple-gu4to)**********

**Checking the relationship type**

**[- isCompound](#apple-guzta)

**[- isFlattened](#apple-guzti)

**[- isMandatory](#apple-guzto)

**[- setIsMandatory:](#apple-gezdmnry)

**[- validateValue:](#apple-gm3dama)**********

**Accessing whether the relationship is to-many**

**[- isToMany](#apple-gu2dc)

**[- setToMany:](#apple-gyzde)****

**Relationship qualifiers**

**[- qualifierWithSourceRow:](#apple-gu3tc)**

**Checking references**

**[- referencesProperty:](#apple-gqztq)**

**Controlling batch fetches**

**[- numberOfToManyFaultsToBatchFetch](#apple-gu2to)

**[- setNumberOfToManyFaultsToBatchFetch:](#apple-gq4dkoi)****

**Taking action upon a change**

**[- deleteRule](#apple-guydm)

**[- propagatesPrimaryKey](#apple-gu3di)

**[- setDeleteRule:](#apple-gu4te)

**[- setPropagatesPrimaryKey:](#apple-gyyts)

**[- ownsDestination](#apple-gu3da)

**[- setOwnsDestination:](#apple-gy2do)************

**Accessing the user dictionary**

**[- setUserInfo:](#apple-gyzdm)

**[- userInfo](#apple-gyztg)****

---

## Instance Methods

---

### addJoin:

- (void)`addJoin:`(EOJoin \*)_aJoin_

Adds a source-destination attribute pair to the relationship. Raises an NSInvalidArgumentException if the relationship is flattened, if either the source or destination attributes are flattened, or if either of _aJoin_'s attributes already belongs to another join of the relationship.

__See also:__
[- `joins`](#apple-gq4tamy), [- `isFlattened`](#apple-guzti), [- `setDefinition:`](#apple-gu4do)

---

### anyInverseRelationship

- (EORelationship \*)`anyInverseRelationship`

Searches the relationship's destination entity for a user-created, back-pointing relationship joining on the same keys. If none is found, it looks for a "hidden" inverse relationship that was manufactured by the Framework. If none is found, the Enterprise Objects Framework creates a "hidden" inverse relationship and returns that. Hidden relationships are used internally by the Framework.

__See also:__
[- `inverseRelationship`](#apple-guzdm)

---

### beautifyName

- (void)`beautifyName`

Makes the relationship's name conform to a standard convention. Names that conform to this style are all lower-case except for the initial letter of each embedded word other than the first, which is upper case. Thus, "NAME" becomes "name", and "FIRST_NAME" becomes "firstName". This method is used in reverse-engineering a model.

__See also:__
[- `setName:`](#apple-gm3tcna), [- `validateName:`](#apple-gyztm), [- `beautifyNames`](EOModel.md#apple-gqzde) (EOModel)

---

### componentRelationships

- (NSArray \*)`componentRelationships`

Returns an array of base relationships making up a flattened relationship, or `nil` if the relationship isn't flattened.

__See also:__
[- `definition`](#apple-guyde)

---

### definition

- (NSString \*)`definition`

Returns the data path of a flattened relationship; for example "department.facility". If the relationship isn't flattened, `definition` returns `nil`.

__See also:__
[- `componentRelationships`](#apple-gq4tq)

---

### deleteRule

- (EODeleteRule)`deleteRule`

Returns a rule that describes the action to take when an object is being deleted. The returned rule is one of the following:

| __Value__ | __Type__ | __Description__ |
| EODeleteRuleNullify | int | Delete the department and remove any back pointer the employee has to the department. |
| EODeleteRuleCascade | int | Delete the department and all of the employees it contains. |
| EODeleteRuleDeny | int | Refuse the deletion if the department contains employees. |
| EODeleteRuleNoAction | int | Delete the department, but ignore the department's __employees__  relationship. You should use this delete rule with caution since it can leave dangling references in your object graph. |

```
```


---

### destinationAttributes

- (NSArray \*)`destinationAttributes`

Returns the destination attributes of the relationship. These correspond one-to-one with the attributes returned by [`sourceAttributes`](#apple-gyzds). Returns `nil` if the relationship is flattened.

__See also:__
[- `joins`](#apple-gq4tamy), [- `destinationAttribute`](EOJoin.md#apple-ha2q) (EOJoin)

---

### destinationEntity

- (EOEntity \*)`destinationEntity`

Returns the relationship's destination entity, which is determined by the destination entity of its joins for a simple relationship, and by whatever ends the data path for a flattened relationship. For example, if a flattened relationship's definition is "department.facility", the destination entity is the Facility entity.

__See also:__
[- `entity`](#apple-guzde)

---

### entity

- (EOEntity \*)`entity`

Returns the relationship's source entity.

__See also:__
[- `destinationEntity`](#apple-guytq), [- `addRelationship:`](EOEntity.md#apple-g4zdm) (EOEntity)

---

### inverseRelationship

- (EORelationship \*)`inverseRelationship`

Searches the relationship's destination entity for a user-created, back-pointing relationship joining on the same keys. Returns the inverse relationship if one is found, `nil` otherwise.

__See also:__
[- `anyInverseRelationship`](#apple-gq4dm)

---

### isCompound

- (BOOL)`isCompound`

Returns YES if the relationship contains more than one join (that is, if it joins more than one pair of attributes), NO if it has only one join. See "[Creating a Simple Relationship](Creating%20Relationships-3.md#apple-gm2tqnq)" for information on compound relationships.

__See also:__
[- `joins`](#apple-gq4tamy), [- `joinSemantic`](#apple-gu2dk)

---

### isFlattened

- (BOOL)`isFlattened`

Returns YES if the relationship traverses more than two entities, NO otherwise. See "[Creating a Flattened Relationship](Creating%20Relationships-3.md#apple-gm2tkni)" for an example of a flattened relationship.

---

### isMandatory

- (BOOL)`isMandatory`

Returns YES if the target of the relationship is required, NO if it can be `nil`.

__See also:__
[- `setIsMandatory:`](#apple-gezdmnry)

---

### isToMany

- (BOOL)`isToMany`

Returns YES if the relationship is to-many, NO if it's to-one.

__See also:__
[- `setToMany:`](#apple-gyzde)

---

### joinSemantic

- (EOJoinSemantic)`joinSemantic`

Returns the semantic used to create SQL expressions for this relationship. The returned join semantic is one of the following:

| __Constant__ | __Description__ |
| EOInnerJoin | Produces results only for destinations of the join relationship that have non-NULL values. |
| EOFullOuterJoin | Produces results for all source records, regardless of the values of the relationships. |
| EOLeftOuterJoin | Preserves rows in the left (source) table, keeping them even if there's no corresponding row in the right table. |
| EORightOuterJoin | Preserves rows in the right (destination) table, keeping them even if there's no corresponding row in the left table. |

```
```

__See also:__
[- `joins`](#apple-gq4tamy)

---

### joins

- (NSArray \*)`joins`

Returns all joins used by relationship.

__See also:__
[- `destinationAttributes`](#apple-guyti)`,` [- `joinSemantic`](#apple-gu2dk)`,` [- `sourceAttributes`](#apple-gyzds)

---

### name

- (NSString \*)`name`

Returns the relationship's name.

---

### numberOfToManyFaultsToBatchFetch

- (unsigned int)`numberOfToManyFaultsToBatchFetch`

Returns the number of to-many faults that are triggered at one time.

---

### ownsDestination

- (BOOL)`ownsDestination`

Returns YES if the receiver's source object owns its destination objects, NO otherwise. See the method description for [`setOwnsDestination:`](#apple-gy2do) for more discussion of this topic.

__See also:__
[- `destinationAttributes`](#apple-guyti)

---

### propagatesPrimaryKey

- (BOOL)`propagatesPrimaryKey`

Returns YES if objects should propagate their primary key to related objects through this relationship. Objects only propagate their primary key values if the corresponding values in the destination object aren't already set.

---

### qualifierWithSourceRow:

- (EOQualifier \*)`qualifierWithSourceRow:`(NSDictionary \*)_sourceRow_

Returns a qualifier that can be used to fetch the destination of the receiving relationship, given _sourceRow_.

---

### referencesProperty:

- (BOOL)`referencesProperty:`(id)_aProperty_

Returns YES if _aProperty_ is in the relationship's data path or is an attribute belonging to one of the relationship's joins; otherwise, it returns NO. See the class description for information on how relationships reference properties.

__See also:__
`[- referencesProperty:](EOEntity.md#apple-ha2to)` (EOEntity)

---

### removeJoin:

- (void)`removeJoin:`(EOJoin \*)_aJoin_

Deletes _aJoin_ from the relationship. Does nothing if the relationship is flattened.

__See also:__
[- `addJoin:`](#apple-gm4dkoa)

---

### setDefinition:

- (void)`setDefinition:`(NSString \*)_definition_

Changes the relationship to a flattened relationship by releasing any joins and attributes (both source and destination) associated with the relationship and setting _definition_ as its data path. "department.facility" is an example of a definition that could be supplied to this method.

If the relationship's entity hasn't been set, this method won't work correctly. See "[Creating a Flattened Relationship](Creating%20Relationships-3.md#apple-gm2tkni)" for more information on flattened relationships.

__See also:__
[- `addJoin:`](#apple-gm4dkoa), [- `setEntity:`](#apple-gu4to)

---

### setDeleteRule:

- (void)`setDeleteRule:`(EODeleteRule)_deleteRule_

Set a rule describing the action to take when object is being deleted. _deleteRule_ can be one of the following:

- [EODeleteRuleNullify](#apple-guydm)
- [EODeleteRuleCascade](#apple-guydm)
- [EODeleteRuleDeny](#apple-guydm)
- [EODeleteRuleNoAction](#apple-guydm)

For more discussion of what these rules mean, see the method description for [`deleteRule`](#apple-guydm).

---

### setEntity:

- (void)`setEntity:`(EOEntity \*)_anEntity_

Sets the entity of the relationship to _anEntity_. If the relationship is currently owned by a different entity, this method will remove the relationship from that entity. This method doesn't add the relationship to the new entity. EOEntity's [`addRelationship:`](EOEntity.md#apple-g4zdm) method invokes this method.

You only need to use this method when creating a flattened relationship; use EOEntity's `addRelationship:` to associate an existing relationship with an entity.

__See also:__
[- `setDefinition:`](#apple-gu4do)

---

### setIsMandatory:

- (void)`setIsMandatory:`(BOOL)_flag_

Specifies according to _flag_ whether the target of the relationship must be supplied or can be `nil`.

---

### setJoinSemantic:

- (void)`setJoinSemantic:`(EOJoinSemantic)_joinSemantic_

Sets the semantic used to create SQL expressions for this relationship. _joinSemantic_ should be one of the following:

- [EOInnerJoin](#apple-gu2dk)
- EOFullOuterJoin
- EOLeftOuterJoin
- EORightOuterJoin

__See also:__
[- `addJoin:`](#apple-gm4dkoa), [- `joinSemantic`](#apple-gu2dk)

---

### setName:

- (void)`setName:`(NSString \*)_name_

Sets the relationship's name to _name_. Raises a verification exception if _name_ is not a valid relationship name, and NSInvalidArgumentException if _name_ is already in use by an attribute or another relationship in the same entity.

This method forces all objects in the model to be loaded into memory.

__See also:__
[- `beautifyName`](#apple-gq4ta), [- `validateName:`](#apple-gyztm)

---

### setNumberOfToManyFaultsToBatchFetch:

- (void)`setNumberOfToManyFaultsToBatchFetch:`(unsigned int)_size_

Sets the number of "toMany" faults that are fired at one time to _size_.

__See also:__
[- `isToMany`](#apple-gu2dc), [- `numberOfToManyFaultsToBatchFetch`](#apple-gu2to)

---

### setOwnsDestination:

- (void)`setOwnsDestination:`(BOOL)flag

Sets according to _flag_ whether a receiver's source object owns its destination objects. The default is NO. When a source object owns its destination objects, it means that the destination objects can't exist independently. For example, in a personnel database, dependents can't exist without having an associated employee. Removing a dependent from an employee's `dependents` array would have the effect of also deleting the dependent from the database, unless you transferred the dependent to a different employee.

__See also:__
[- `deleteRule`](#apple-guydm), [- `setDeleteRule:`](#apple-gu4te), [- `ownsDestination`](#apple-gu3da)

---

### setPropagatesPrimaryKey:

- (void)`setPropagatesPrimaryKey:`(BOOL)_flag_

Specifies according to _flag_ whether objects should propagate their primary key to related objects through this relationship. For example, an Employee object might propagate its primary key to an EmployeePhoto object. Objects only propagate their primary key values if the corresponding values in the destination object aren't already set.

---

### setToMany:

- (void)`setToMany:`(BOOL)_flag_

Sets a simple relationship as to-many according to _flag_. Raises an NSInvalidArgumentException if the receiver is flattened. See the class description for considerations in setting this flag.

__See also:__
[- `isFlattened`](#apple-guzti)

---

### setUserInfo:

- (void)`setUserInfo:`(NSDictionary \*)_dictionary_

Sets the _dictionary_ of auxiliary data, which your application can use for whatever it needs. _dictionary_ can only contain property list data types (that is, NSDictionary, NSString, NSArray, and NSData).

---

### sourceAttributes

- (NSArray \*)`sourceAttributes`

Returns the source attributes of a simple (non-flattened) relationship. These correspond one-to-one with the attributes returned by [`destinationAttributes`](#apple-guyti). Returns `nil` if the relationship is flattened.

__See also:__
[- `joins`](#apple-gq4tamy), [- `sourceAttribute`](EOJoin.md#apple-he4a) (EOJoin)

---

### userInfo

- (NSDictionary \*)`userInfo`

Returns a dictionary of user data. Your application can use this data for whatever it needs.

---

### validateName:

- (NSException \*)`validateName:`(NSString \*)_name_

Validates _name_ and returns `nil` if its a valid name, or an exception if it isn't. A name is invalid if it has zero length; starts with a character other than a letter, a number, or "@", "#", or "_"; or contains a character other than a letter, a number, "@", "#", "_", or "$". A name is also invalid if the receiver's EOEntity already has an EORelationship with the same name, or if the model has a stored procedure that has an argument with the same name.

[`setName:`](#apple-gm3tcna) uses this method to validate its argument.

---

### validateValue:

- (NSException \*)`validateValue:`(id \*)_valueP_

For relationships marked as mandatory, returns a validation exception if the receiver is to-one and _valueP_ is `nil`, or if the receiver is to-many an _valueP_ has a count of 0. A mandatory relationship is one in which the target of the relationship is required. Returns `nil` to indicate success.

__See also:__
[- `isMandatory`](#apple-guzto), [- `setIsMandatory:`](#apple-gezdmnry)

---

[!](EOQualifier%20Additions.md)
[!](Creating%20Relationships-3.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
