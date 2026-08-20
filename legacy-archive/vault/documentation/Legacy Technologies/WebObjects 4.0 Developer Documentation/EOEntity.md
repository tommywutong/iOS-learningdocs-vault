---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOEntity.html
archived_at: '2026-07-18T01:28:09.765931Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EODatabaseOperation.md)
[!](Creating%20an%20Entity.md)

---

# EOEntity

__Inherits From:__
NSObject

[EOPropertyListEncoding](EOPropertyListEncoding.md)

__Inherits From:__
com.apple.yellow.eoaccess

---

## Class Description

An EOEntity describes a table in a database and associates a name internal to the Framework with an external name by which the table is known to the database. An EOEntity maintains a group of attributes and relationships, which are collectively called properties. These are represented by the [EOAttribute](EOAttribute.md) and [EORelationship](EORelationship.md) classes, respectively; see their specifications for more information.

You usually define entities in a model with the EOModeler application, which is documented in _WebObjects Tools and Techniques_. EOEntity objects are primarily used by the Enterprise Objects Framework for mapping tables in the database to enterprise objects; your code will probably make limited use of them unless you're specifically working with models.

An EOEntity is associated with a specific class whose instances are used to represent records (rows) from the database in applications using layers at or above the database layer of the Enterprise Objects Framework. If an EOEntity doesn't have a specific class associated with it, instances of EOGenericRecord (defined in EOControl) are created.

An EOEntity may be marked as read-only, in which case any changes to rows or objects for that entity made by the database level objects are denied.

You can define an external query for an EOEntity to be used when a selection is attempted with an unrestricted qualifier (one that would select all rows in the entity's table). An external query is sent unaltered to the database server and so can use database-specific features such as stored procedures; external queries are thus useful for hiding records or invoking database-specific features. You can also assign stored procedures to be invoked upon particular database operations through the use of EOEntity's [`setStoredProcedure`](#apple-hezti) method.

Like the other major modeling classes, EOEntity provides a user dictionary for your application to store any application-specific information related to the entity.

For more information on programmatically creating EOEntity objects, see "[Creating an Entity](Creating%20an%20Entity.md#apple-gm2tgmq)."

**[EOPropertyListEncoding](EOPropertyListEncoding.md)**

**[awakeWithPropertyList](EOPropertyListEncoding.md#apple-hazto)

**[encodeIntoPropertyList](EOPropertyListEncoding.md#apple-ha3di)****

---

## Method Types

**Constructors**

**[EOEntity](#apple-ge2danju)**

**Accessing the name**

**[setName](#apple-heyts)

**[name](#apple-hazdm)

**[validateName](#apple-he2tq)

**[beautifyName](#apple-g42ti)********

**Accessing the model**

**[model](#apple-hazde)**

**Specifying fetching behavior for the entity**

**[setExternalQuery](#apple-heydm)

**[externalQuery](#apple-g44dk)

**[setRestrictingQualifier](#apple-heztc)

**[restrictingQualifier](#apple-gq4tkma)********

**Accessing primary key qualifiers**

**[qualifierForPrimaryKey](#apple-ha2tg)

**[isQualifierForPrimaryKey](#apple-hayde)****

**Accessing a schema-based qualifier from a qualifier for in-memory evaluation**

**[schemaBasedQualifier](#apple-ge2tonzq)**

**Accessing attributes**

**[addAttribute](#apple-g4zde)

**[anyAttributeNamed](#apple-g4zti)

**[attributeNamed](#apple-g42de)

**[attributes](#apple-g42dm)

**[removeAttribute](#apple-ha3ta)

**[attributesToFetch](#apple-ge3dsmjx)************

**Accessing relationships**

**[addRelationship](#apple-g4zdm)

**[anyRelationshipNamed](#apple-g4ztq)

**[relationships](#apple-ha3dm)

**[relationshipNamed](#apple-ha3de)

**[removeRelationship](#apple-ha3ti)**********

**Checking referential integrity**

**[externalModelsReferenced](#apple-g43tq)

**[referencesProperty](#apple-ha2to)****

**Accessing primary keys**

**[globalIDForRow](#apple-g44dq)

**[isPrimaryKeyValidInObject](#apple-g44tq)

**[primaryKeyForGlobalID](#apple-ha2dc)

**[primaryKeyForRow](#apple-guyteoi)********

**Accessing primary key attributes**

**[setPrimaryKeyAttributes](#apple-hezdg)

**[primaryKeyAttributes](#apple-hazto)

**[primaryKeyAttributeNames](#apple-haztg)

**[primaryKeyRootName](#apple-guytany)

**[isValidPrimaryKeyAttribute](#apple-haytk)**********

**Accessing class properties**

**[setClassProperties](#apple-heyda)

**[classProperties](#apple-g43ta)

**[classPropertyNames](#apple-g43ti)

**[isValidClassProperty](#apple-hayte)********

**Accessing the enterprise object class**

**[classDescriptionForInstances](#apple-g43de)

**[setClassName](#apple-ha4ti)

**[className](#apple-g43dk)******

**Accessing locking attributes**

**[setAttributesUsedForLocking](#apple-gq4tgny)

**[attributesUsedForLocking](#apple-g42ta)

**[isValidAttributeUsedForLocking](#apple-haydq)******

**Accessing external name**

**[setExternalName](#apple-heydg)

**[externalName](#apple-g44de)

**[externalNameForInternalName](#apple-ge2danzr)

**[nameForExternalName](#apple-ge2danzw)********

**Accessing whether an entity is read only**

**[setReadOnly](#apple-hezdq)

**[isReadOnly](#apple-haydk)****

**Accessing the user dictionary**

**[setUserInfo](#apple-he2di)

**[userInfo](#apple-he2tk)****

**Working with stored procedures**

**[setStoredProcedure](#apple-hezti)

**[storedProcedureForOperation](#apple-he2do)****

**Working with fetch specifications**

**[addFetchSpecification](#apple-ge3tqmbs)

**[fetchSpecificationNamed](#apple-ge3tomrr)

**[fetchSpecificationNames](#apple-ge3tonjq)

**[removeFetchSpecificationNamed](#apple-ge3tqmjz)********

**Working with entity inheritance hierarchies**

**[parentEntity](#apple-hazds)

**[subEntities](#apple-he2tc)

**[addSubEntity](#apple-g4zta)

**[removeSubEntity](#apple-ha3tq)

**[setIsAbstractEntity](#apple-gy2dqmi)

**[isAbstractEntity](#apple-g44ti)************

**Specifying fault behavior**

**[setMaxNumberOfInstancesToBatchFetch](#apple-ge3timby)

**[maxNumberOfInstancesToBatchFetch](#apple-hayts)****

**Caching objects**

**[setCachesObjects](#apple-g43dkni)

**[cachesObjects](#apple-gu2tgma)****

---

## Constructors

---

### EOEntity

public `EOEntity`()

Creates a new EOEntity.

public `EOEntity`(NSDictionary _propertyList_, java.lang.Object _owner_)

Creates a new EOEntity initialized from _propertyList_-a dictionary containing only property list data types (that is, NSDictionary, NSArray, NSData, and java.lang.String). This constructor is used by EOModeler when it reads in an EOModel from a file, for example. The _owner_ argument should be the EOEntity's EOModel. Entities created from a property list must receive an [`awakeWithPropertyList`](../Protocols/EOPropertyListEncoding.md#apple-hazto) message after creation before they are fully functional, but the `awake...` message should be deferred until the all of the other objects in the model have also been created.

__See also:__
[`awakeWithPropertyList`](../Protocols/EOPropertyListEncoding.md#apple-hazto) (EOPropertyListEncoding), [`encodeIntoPropertyList`](../Protocols/EOPropertyListEncoding.md#apple-ha3di)
(EOPropertyListEncoding)

#

---

### externalNameForInternalName

public static java.lang.String `externalNameForInternalName`(java.lang.String _name_,
java.lang.String _separatorString_,
boolean _useAllCaps_)

Used by the Framework to convert modeling object names to database schema names that conform to a standard convention. A conforming database schema name is upper-case and uses "_" to separate words. Consequently "name" becomes "NAME" and "firstName" becomes "FIRST_NAME".

_separatorString_ is a character that is used to separate words. The Framework uses "_" by default as in the examples above. _useAllCaps_ indicates whether to capitalize the name. For example, providing `false` converts "firstName" to "first_name".

---

### nameForExternalName

public static java.lang.String `nameForExternalName`(java.lang.String _name_,
java.lang.String _separatorString_,
boolean _initialCaps_)

Used by name beautification to convert database schema names to modeling object names that conform to a standard convention. A conforming attribute, relationship, or stored procedure name is lower-case except for the initial letter of each embedded word other than the first, which is upper case. Consequently "NAME" becomes "name" and "FIRST_NAME" becomes "firstName". A conforming entity is all lower-case except for the initial letter of each word. Consequently "CUSTOMER_ACCOUNT" becomes "CustomerAccount".

_separatorString_ is a character that is used to separate words. The Framework uses "_" by default as in the examples above. _initialCaps_ indicates whether to capitalize the first letter of the first word. By default, the Framework uses `true` for entities and `false` for everything else.

__See also:__
[`beautifyNames`](EOModel.md#apple-gqzde) (EOModel), [`beautifyName`](#apple-g42ti), - `beautifyName` ([EOAttribute](EOAttribute.md#apple-ge4dcmzs), [EORelationship](EORelationship.md),
[EOStoredProcedure](EOStoredProcedure.md))

---

## Instance Methods

---

### addAttribute

public void `addAttribute`(EOAttribute _anAttribute_)

Adds _anAttribute_ to the receiver. Throws an exception if _anAttribute_'s name is already in use by another attribute or relationship. Sets _anAttribute_'s entity to `this`.

__See also:__
[`removeAttribute`](#apple-ha3ta), [`attributes`](#apple-g42dm), [`attributeNamed`](#apple-g42de)

---

### addFetchSpecification

public void `addFetchSpecification`(com.apple.yellow.eocontrol.EOFetchSpecification _fetchSpec_,
java.lang.String _fetchSpecName_)

Adds the fetch specification and associates _fetchSpecName_ with it.

__See also:__
[`fetchSpecificationNamed`](#apple-ge3tomrr), [`fetchSpecificationNames`](#apple-ge3tonjq), [`removeFetchSpecificationNamed`](#apple-ge3tqmjz)

---

### addRelationship

public void `addRelationship`(EORelationship _aRelationship_)

Adds _aRelationship_ to the receiver. Throws an exception if _aRelationship_'s name is already in use by another attribute or relationship. Sets _aRelationship_'s entity to `this`.

__See also:__
[`removeRelationship`](#apple-ha3ti), [`relationships`](#apple-ha3dm), [`relationshipNamed`](#apple-ha3de)

---

### addSubEntity

public void `addSubEntity`(EOEntity _child_)

Causes the child entity _child_ to "inherit" from the receiver. This is the first step in setting up an inheritance hierarchy between entities.

__See also:__
[`subEntities`](#apple-he2tc) , [`removeSubEntity`](#apple-ha3tq)

---

### anyAttributeNamed

public EOAttribute `anyAttributeNamed`(java.lang.String _attributeName_)

Returns the user-created attribute identified by _attributeName_. If no such attribute exists, this method looks through the "hidden" attributes created by the Enterprise Objects Framework for one with the given name. Hidden attributes are used for such things as primary keys on target entities of flattened attributes. If none is found, `null` is returned.

__See also:__
[`attributeNamed`](#apple-g42de), [`attributes`](#apple-g42dm)

---

### anyRelationshipNamed

public EORelationship `anyRelationshipNamed`(java.lang.String _relationshipName_)

Returns the user-created relationship identified by _relationshipName_. If none exists, this method looks through the "hidden" relationships created by the Enterprise Objects Framework for one with the given name. If none is found, `null` is returned.

__See also:__
[`relationshipNamed`](#apple-ha3de), [`relationships`](#apple-ha3dm)

---

### attributeNamed

public EOAttribute `attributeNamed`(java.lang.String _attributeName_)

Returns the attribute named _attributeName_, or `null` if no such attribute exists.

__See also:__
[`anyAttributeNamed`](#apple-g4zti), [`attributes`](#apple-g42dm), [`relationshipNamed`](#apple-ha3de)

---

### attributes

public NSArray `attributes`()

Returns all of the receiver's attributes, or `null` if the receiver has none.

__See also:__
[`anyAttributeNamed`](#apple-g4zti), [`attributeNamed`](#apple-g42de)

---

### attributesToFetch

public NSArray `attributesToFetch`()

Returns an array of the EOAttributes that need to be fetched so that they can be included in the row snapshot. The set of attributes includes:

- Attributes that are class properties, "used for locking," or primary keys.
- Source attributes of any to-many relationship (flattened or non-flattened) that is a class property.
- Source attributes of any non-flattened, to-one relationship that is a class property or that is used by a flattened attribute that is a class property.
- The foreign key attributes of any flattened, to-one relationship that is a class property or that is used by a class property.

---

### attributesUsedForLocking

public NSArray `attributesUsedForLocking`()

Returns an array containing those properties whose values must match a snapshot any time a row is updated.

Attributes used for locking are those whose values are compared when a database-level object performs an update. When the database-level classes fetch an enterprise object, they cache these attributes' values in a snapshot. Later, when the enterprise object is updated, the values of these attributes in the object are checked with those in the snapshot-if they differ, the update fails. See the EODatabaseContext class specification for more information.

---

### beautifyName

public void `beautifyName()`

Makes the receiver's name conform to a standard convention. EOEntity names that conform to this style are all lower-case except for the initial letter of each word, which is upper case. Thus, "MOVIE" becomes "Movie", and "MOVIE_ROLE" becomes "MovieRole".

__See also:__
[`setName`](#apple-heyts), [`validateName`](#apple-he2tq), [`beautifyNames`](EOModel.md#apple-gqzde) (EOModel)

---

### cachesObjects

public boolean `cachesObjects()`

Returns `true` if all of the objects from the receiver are to be cached in memory and queries are to be evaluated in-memory using this cache rather than in the database. This method should only be used for fairly small tables of read-only objects, since the first access to the receiver will trigger fetching the entire table. You should generally restrict this method to read-only entities to avoid cached data getting out of sync with database data. Also, you shouldn't use this method if your application will be making queries against the entity that can't be evaluated in memory.

__See also:__
[`setCachesObjects`](#apple-g43dkni)

---

### classDescriptionForInstances

public com.apple.yellow.eocontrol.EOClassDescription `classDescriptionForInstances`()

Returns the EOClassDescription associated with the receiver. The EOClassDescription class provides a mechanism for extending classes by giving them access to the metadata contained in an EOModel (or another external source of information). In an application, EOClassDescriptions are registered on demand for the EOEntity on which an enterprise object is based. For more information, see the class specifications for EOClassDescription (in EOControl) and [EOEntityClassDescription](EOEntityClassDescription.md#apple-geydanbx).

---

### className

public java.lang.String `className`()

Returns the name of the enterprise object class associated with the receiver. When a row is fetched for the receiver by a database-level object, it's returned as an instance of this class. This class might not be present in the run-time system, and in fact your application may have to load it on demand. If your application doesn't load a class, EOGenericRecord is used.

An enterprise object class other than EOGenericRecord can be mapped to only one entity.

---

### classProperties

public NSArray `classProperties`()

Returns an array containing the properties that are bound to the receiver's class (so that instances of the class will be passed values corresponding to those properties). This is a subset of the receiver's attributes and relationships.

__See also:__
[`classPropertyNames`](#apple-g43ti)

---

### classPropertyNames

public NSArray `classPropertyNames`()

Returns an array containing the names of those properties that are bound to the receiver's class (so that instances of the class will be passed values corresponding to those properties). This is a subset of the receiver's attributes and relationships.

__See also:__
[`classProperties`](#apple-g43ta)

---

### externalModelsReferenced

public NSArray `externalModelsReferenced`()

Examines each of the receiver's relationships and returns a list of all external models referenced by the receiver.

__See also:__
[`referencesProperty`](#apple-ha2to)

---

### externalName

public java.lang.String `externalName`()

Returns the name of the receiver as understood by the database server.

---

### externalQuery

public java.lang.String `externalQuery`()

Returns a query statement that's used by an EOAdaptorChannel to select rows for the receiver when a qualifier is empty, or `null` if the receiver has no external query. An empty qualifier is one that specifies only the entity, and would thus fetch all enterprise objects for that entity.

External queries are useful for hiding records or invoking database-specific features such as stored procedures when an application attempts to select all records for an entity. You can also use the EOStoredProcedure class to work with stored procedures; for more information see the [EOStoredProcedure](EOStoredProcedure.md) class specification.

__See also:__
[`setExternalQuery`](#apple-heydm)

---

### fetchSpecificationNamed

public com.apple.yellow.eocontrol.EOFetchSpecification `fetchSpecificationNamed`(java.lang.String _fetchSpecName_)

Returns the fetch specification associated with _fetchSpecName_.

__See also:__
[`addFetchSpecification`](#apple-ge3tqmbs), [`fetchSpecificationNames`](#apple-ge3tonjq), [`removeFetchSpecificationNamed`](#apple-ge3tqmjz)

---

### fetchSpecificationNames

public NSArray `fetchSpecificationNames`()

Returns an alphabetically sorted array of names of the entity's fetch specifications.

__See also:__
[`addFetchSpecification`](#apple-ge3tqmbs), [`fetchSpecificationNamed`](#apple-ge3tomrr), [`removeFetchSpecificationNamed`](#apple-ge3tqmjz)

---

### globalIDForRow

public com.apple.yellow.eocontrol.EOGlobalID `globalIDForRow`(NSDictionary _row_)

Constructs a global identifier from the specified row for the receiver.

__See also:__
[`primaryKeyForGlobalID`](#apple-ha2dc)

---

### isAbstractEntity

public boolean `isAbstractEntity()`

Returns `true` to indicate that the receiver is abstract, `false` otherwise. An abstract entity is one that has no corresponding enterprise objects in your application. Abstract entities are used to model inheritance relationships. For example, you might have a Person abstract entity that acts as the parent of Customer and Employee entities. Customer and Employee would inherit certain characteristics from Person (such as name and address attributes). However, though your application might have Customer and Employee objects, it would never have a Person object.

__See also:__
[`setIsAbstractEntity`](#apple-gy2dqmi)

---

### isPrimaryKeyValidInObject

public boolean `isPrimaryKeyValidInObject`(java.lang.Object _anObject_)

Returns `true` if every key attribute is present in _anObject_ and has a value that is not `null`. Returns `false` otherwise. This method uses key-value coding so a dictionary may be provided instead of an enterprise object.

__See also:__
[`primaryKeyForRow`](#apple-guyteoi)

---

### isQualifierForPrimaryKey

public boolean `isQualifierForPrimaryKey`(com.apple.yellow.eocontrol.EOQualifier _aQualifier_)

Returns `true` if _aQualifier_ describes the primary key and nothing but the primary key, `false` otherwise.

---

### isReadOnly

public boolean `isReadOnly()`

Returns `true` if the receiver can't be modified, `false` if it can. If an entity can't be modified, then enterprise objects fetched for that entity also can't be modified (that is, inserted, deleted, or updated).

---

### isValidAttributeUsedForLocking

public boolean `isValidAttributeUsedForLocking`(EOAttribute _anAttribute_)

Returns `false` if _anAttribute_ isn't an EOAttribute, if the EOAttribute doesn't belong to the receiver, or if _anAttribute_ is derived. Otherwise returns `true`. An attribute that isn't valid for locking will cause [`setAttributesUsedForLocking`](#apple-gq4tgny) to fail.

__See also:__
[`attributesUsedForLocking`](#apple-g42ta)

---

### isValidClassProperty

public boolean `isValidClassProperty`(java.lang.Object _aProperty_)

Returns `false` if either _aProperty_ isn't an EOAttribute or EORelationship, or if _aProperty_ doesn't belong to the receiver. Otherwise returns `true`. Note that this method doesn't tell you whether _aProperty_ is a member of the array returned by [`classProperties`](#apple-g43ta). In other words, unlike `classProperties`, [`classPropertyNames`](#apple-g43ti), and [`setClassProperties`](#apple-heyda), this method doesn't interact with the properties bound to the entity's enterprise object class.

---

### isValidPrimaryKeyAttribute

public boolean `isValidPrimaryKeyAttribute`(EOAttribute _anAttribute_)

Returns `false` if _anAttribute_ isn't an EOAttribute, doesn't belong to the receiver, or is derived. Otherwise returns `true`.

__See also:__
[`setPrimaryKeyAttributes`](#apple-hezdg)

---

### maxNumberOfInstancesToBatchFetch

public int `maxNumberOfInstancesToBatchFetch`()

Returns the maximum number of to-one faults from the receiver to fire at one time. See the method description for [`setMaxNumberOfInstancesToBatchFetch`](#apple-ge3timby) for more explanation of what this means.

---

### model

public EOModel `model`()

Returns the model that contains the receiver.

__See also:__
[`addEntity`](EOModel.md#apple-gqyti) (EOModel)

---

### name

public java.lang.String `name`()

Returns the receiver's name.

---

### parentEntity

public EOEntity `parentEntity`()

Returns the entity from which the receiver inherits.

__See also:__
[`subEntities`](#apple-he2tc)

---

### primaryKeyAttributeNames

public NSArray `primaryKeyAttributeNames`()

Returns an array containing the names of the attributes that make up the receiver's primary key.

__See also:__
[`primaryKeyAttributes`](#apple-hazto)

---

### primaryKeyAttributes

public NSArray `primaryKeyAttributes`()

Returns an array of those attributes that make up the receiver's primary key.

__See also:__
[`primaryKeyAttributeNames`](#apple-haztg)

---

### primaryKeyForGlobalID

public NSDictionary `primaryKeyForGlobalID`(com.apple.yellow.eocontrol.EOKeyGlobalID _globalID_)

Returns the primary key for the object identified by _globalID_.

__See also:__
[`globalIDForRow`](#apple-g44dq)

---

### primaryKeyForRow

public NSDictionary `primaryKeyForRow`(NSDictionary _aRow_)

Returns the primary key for _aRow_, or `null` if the primary key can't be computed. The primary key is aDictionary whose keys are attribute names and whose values are values for those attributes.

__See also:__
[`primaryKeyForGlobalID`](#apple-ha2dc)

---

### primaryKeyRootName

public java.lang.String `primaryKeyRootName`()

Returns the external name (that is, the name as it's understood by the database) of the receiver's root entity. If the receiver has no parent entity, returns the receiver's external name.

__See also:__
[`externalName`](#apple-g44de), [`name`](#apple-hazdm), [`parentEntity`](#apple-hazds)

---

### qualifierForPrimaryKey

public com.apple.yellow.eocontrol.EOQualifier `qualifierForPrimaryKey`(NSDictionary _aRow_)

Returns a qualifier for the receiver that can be used to fetch an instance of the receiver with the primary key extracted from _aRow_.

__See also:__
[`isQualifierForPrimaryKey`](#apple-hayde), [`restrictingQualifier`](#apple-gq4tkma)

---

### referencesProperty

public boolean `referencesProperty`(java.lang.Object _aProperty_)

Returns `true` if any of the receiver's attributes or relationships reference _aProperty_, `false` otherwise. A property can be referenced by a flattened attribute or by a relationship. For example, suppose a model has an Employee entity with a `toDepartment` relationship. If you flatten the department's name attribute into the Employee entity, creating a `departmentName` attribute, that flattened attribute references the `toDepartment` relationship.

If an entity has any outstanding references to a property, you shouldn't remove the property.

__See also:__
[`removeAttribute`](#apple-ha3ta), [`removeRelationship`](#apple-ha3ti)

---

### relationshipNamed

public EORelationship `relationshipNamed`(java.lang.String _name_)

Returns the relationship named _name_, or `null` if the receiver has no such relationship.

__See also:__
[`anyRelationshipNamed`](#apple-g4ztq), [`attributeNamed`](#apple-g42de), [`relationships`](#apple-ha3dm)

---

### relationships

public NSArray `relationships`()

Returns all of the receiver's relationships, or `null` if the receiver has none.

__See also:__
[`attributes`](#apple-g42dm)

---

### removeAttribute

public void `removeAttribute`(EOAttribute _name_)

Removes the attribute named _name_ if it exists. You should always use [`referencesProperty`](#apple-ha2to)to check that an attribute isn't referenced by another property before removing it.

__See also:__
[`addAttribute`](#apple-g4zde), [`attributes`](#apple-g42dm)

---

### removeFetchSpecificationNamed

public void `removeFetchSpecificationNamed`(java.lang.String _fetchSpecName_)

Removes the fetch specification referred to by _fetchSpecName_.

__See also:__
[`addFetchSpecification`](#apple-ge3tqmbs), [`fetchSpecificationNamed`](#apple-ge3tomrr), [`fetchSpecificationNames`](#apple-ge3tonjq)

---

### removeRelationship

public void `removeRelationship`(EORelationship _name_)

Removes the relationship named _name_ if it exists. You should always use [`referencesProperty`](#apple-ha2to) to check that a relationship isn't referenced by another property before removing it.

__See also:__
[`addRelationship`](#apple-g4zdm), [`relationships`](#apple-ha3dm)

---

### removeSubEntity

public void `removeSubEntity`(EOEntity _child_)

Removes _child_ from the receiver's list of sub-entities.

__See also:__
[`addSubEntity`](#apple-g4zta), [`subEntities`](#apple-he2tc)

---

### restrictingQualifier

public com.apple.yellow.eocontrol.EOQualifier `restrictingQualifier`()

Returns the qualifier used to restrict all queries made against the receiver. Restricting qualifiers are useful when there is not a one-to-one mapping between an entity and a particular database table, or when you always want to filter the data that's returned for a particular entity.

For example, if you're using the "one table" inheritance model in which parent and child data is contained in the same table, you'd use a restricting qualifier to fetch objects of the appropriate type. To give a non-inheritance example, for an Employees table you might create a "Sales" entity that has a restricting qualifier that only fetches employees who are in the Sales department.

__See also:__
[`setRestrictingQualifier`](#apple-heztc)

---

### schemaBasedQualifier

public com.apple.yellow.eocontrol.EOQualifier `schemaBasedQualifier`(com.apple.yellow.eocontrol.EOQualifier _aQualifier_)

Returns a qualifier based on _aQualifier_ suitable for evaluation by a database (as opposed to in-memory evaluation). Invoked by an EODatabaseChannel object before it uses its EOAdaptorChannel to perform a database operation.

Whereas in-memory qualifier evaluation uses object instance variables to resolve relationships, a database qualifier must use foreign keys. For example, consider a qualifier that is used to fetch all employees who work in a specified department:

> ```
> Department dept;    // Assume this exists.Qualifier qualifer;MutableVector qualArgs = new MutableVector();qualArgs.addElement(dept);    qualifier = Qualifier.qualifierWithQualifierFormat("department = %@", qualArgs);
> ```

For an in-memory search, the Framework queries employee objects for their department object and includes an employee in the result list if its department object is equal to `dept`. (See the EOQualifierEvaluation interface description for more information on in-memory searching.)

For a database search, the Framework needs to qualify the fetch by specifying a foreign key value for `dept`. The Framework sends the EOEntity class a [`schemaBasedQualifier`](#apple-ge2tonzq) message that creates a new EOQualifier object from `qualifier`. Assume that the entity for employee objects has an attribute named `departmentID` and that the primary key value for `dept` is 459, the resulting qualifier specifies the search conditions as:

department.departmentID = 459

__See also:__
[`selectObjectsWithFetchSpecification`](EODatabaseChannel.md#apple-gi3te) (EODatabaseChannel)

---

### setAttributesUsedForLocking

public boolean `setAttributesUsedForLocking`(NSArray _attributes_)

Sets _attributes_ as the attributes used when an EODatabaseChannel locks enterprise objects for updates. Returns `false` and doesn't set the attributes used for locking if any of the attributes in _attributes_ responds `false` to [`isValidAttributeUsedForLocking`](#apple-haydq); returns `true` otherwise. See the [EODatabase](EODatabase.md), [EODatabaseContext](EODatabaseContext.md), and [EODatabaseChannel](EODatabaseChannel.md#apple-ha2dkmi) class specifications for information on locking.

---

### setCachesObjects

public void `setCachesObjects`(boolean _flag_)

Sets according to _flag_ whether all of the receiver's objects are cached the first time the associated table is queried.

__See also:__
[`cachesObjects`](#apple-gu2tgma)

---

### setClassName

public void `setClassName`(java.lang.String _name_)

Assigns _name_ as the name of the class associated with the receiver. This class need not be present in the run-time system when this message is sent. When an EODatabaseChannel fetches objects for the receiver, they're created as instances of this class. Your application may have to load the class on demand if it isn't present in the run-time system; if it doesn't load the class, EOGenericRecord will be used.

__Note:__
If you set the class name to `null`, the [`className`](#apple-g43dk) method returns "EOGenericRecord".

An enterprise object class other than EOGenericRecord can be mapped to only one entity.

__See also:__
[`className`](#apple-g43dk)

---

### setClassProperties

public boolean `setClassProperties`(NSArray _properties_)

Sets the receiver's class properties to the EOAttributes and EORelationships in _properties_ and returns `true`, unless the receiver responds `false` to [`isValidClassProperty`](#apple-hayte) for any of the objects in the array. In this event, the receiver's class properties aren't changed and `false` is returned.

---

### setExternalName

public void `setExternalName`(java.lang.String _name_)

Sets the name of the receiver as understood by the database server to _name_. For example, though your application may know the entity as "JobTitle" the database may require a form such as "JOB_TTL". An adaptor uses the external name to communicate with the database; your application should never need to use the external name.

---

### setExternalQuery

public void `setExternalQuery`(java.lang.String _aQuery_)

Assigns _aQuery_ as the query statement used for selecting rows from the receiver when there is no qualifier.

External queries are useful for hiding records or invoking database-specific features such as stored procedures when an application attempts to select all records for an entity. You can also use the EOStoredProcedure class to work with stored procedures; for more information see the [EOStoredProcedure](EOStoredProcedure.md) class specification.

An external query is sent unaltered to the database server, and so must contain the external (column) names instead of the names of EOAttributes. However, to work properly with the adaptor the external query must use the columns in alphabetical order by their corresponding EOAttributes' names.

__See also:__
[`columnName`](EOAttribute.md#apple-ge4dcnbz) (EOAttribute), [`externalQuery`](#apple-g44dk)

---

### setIsAbstractEntity

public void `setIsAbstractEntity`(boolean _flag_)

Sets according to _flag_ whether the receiver is an abstract entity. For more discussion of abstract entities, see the method description for [`isAbstractEntity`](#apple-g44ti).

---

### setMaxNumberOfInstancesToBatchFetch

public void `setMaxNumberOfInstancesToBatchFetch`(int _size_)

Sets the maximum number of faults from the receiver to trigger at one time. By default, only one object is fetched from the database when you trigger a fault. You can optionally use this method to set to size the number of faults of the same entity should be fetched from the database along with the first one. Using this technique helps to optimize performance by taking advantage of round trips to the database.

__See also:__
[`maxNumberOfInstancesToBatchFetch`](#apple-hayts)

---

### setName

public void `setName`(java.lang.String _name_)

Sets the receiver's name to _name_. Throws an exception if _name_ is already in use by another entity in the same EOModel or if _name_ is not a valid entity name.

__See also:__
[`beautifyName`](#apple-g42ti), [`validateName`](#apple-he2tq)

---

### setPrimaryKeyAttributes

public boolean `setPrimaryKeyAttributes`(NSArray _keys_)

If the receiver responds `false` to [`isValidPrimaryKeyAttribute`](#apple-haytk) for any of the objects in _keys_, this method returns `false`. Otherwise, this method sets the primary key attributes to the attributes in _keys_ and returns `true`.

You should exercise care in choosing primary key attributes. Floating-point numbers, for example, can't be reliably compared for equality, and are thus unsuitable for use in primary keys. Integer and string types are the safest choice for primary keys. BigDecimal objects will work, but they'll entail more overhead than integers.

---

### setReadOnly

public void `setReadOnly`(boolean _flag_)

Sets according to _flag_ whether the database rows for the receiver can be modified by the database level objects.

__See also:__
[`isReadOnly`](#apple-haydk)

---

### setRestrictingQualifier

public void `setRestrictingQualifier`(com.apple.yellow.eocontrol.EOQualifier _aQualifier_)

Assigns _aQualifier_ as the qualifier used to restrict all queries made against the receiver. The restricting qualifier can be used to map an entity to a subset of the rows in a table. For more discussion of this subject, see the description for [`restrictingQualifier`](#apple-gq4tkma).

---

### setStoredProcedure

public void `setStoredProcedure`(EOStoredProcedure _storedProcedure_, java.lang.String _operation_)

Sets _storedProcedure_ for _operation_. _operation_ can be one of the following:

| __Constant__ | __Description__ |
| FetchAllProcedureOperation | Procedure that fetches all records from the database. |
| FetchWithPrimaryKeyProcedureOperation | Procedure that performs a fetch with primary key. |
| InsertProcedureOperation | Procedure that performs an insert. |
| DeleteProcedureOperation | Procedure that performs a delete. |
| NextPrimaryKeyProcedureOperation | Procedure that performs generates a new primary key. |

```
```

This information is used when changes from the object graph have been transformed into EODatabaseOperations that are being used to construct EOAdaptorOperations. At this point, Enterprise Objects Framework checks the entities associated with the changed objects to see if the entities have any stored procedures defined for the operation being performed.

__See also:__
[`storedProcedureForOperation`](#apple-he2do)

---

### setUserInfo

public void `setUserInfo`(NSDictionary _dictionary_)

Sets the _dictionary_ of auxiliary data, which your application can use for whatever it needs. _dictionary_ can only contain property list data types-that is, String, NSDictionary, NSArray, and NSData.

---

### storedProcedureForOperation

public EOStoredProcedure `storedProcedureForOperation`(java.lang.String _operation_)

Returns the stored procedure for the specified _operation_, if one has been set. Otherwise, returns `null`. _operation_ can be one of the following:

- EOFetchAllProcedureOperation
- EOFetchWithPrimaryKeyProcedureOperation
- EOInsertProcedureOperation
- EODeleteProcedureOperation
- EONextPrimaryKeyProcedureOperation

__See also:__
[`setStoredProcedure`](#apple-hezti), [`parameterDirection`](EOAttribute.md#apple-ha3dm) (EOAttribute), [`storedProcedure`](EOAttribute.md#apple-he3ti) (EOAttribute)

---

### subEntities

public NSArray `subEntities`()

Returns a list of those entities which inherit from the receiver.

__See also:__
[`addSubEntity`](#apple-g4zta), [`parentEntity`](#apple-hazds), [`removeSubEntity`](#apple-ha3tq)

---

### userInfo

public NSDictionary `userInfo`()

Returns a dictionary of user data. Your application can use this to store any auxiliary information it needs.

__See also:__
[`setUserInfo`](#apple-he2di)

---

### validateName

public java.lang.Throwable `validateName`(java.lang.String _aString_)

Validates _name_ and returns `null` if it is a valid name, or an exception if it isn't. A name is invalid if it has zero length; starts with a character other than a letter, a number, or "@", "#", or "_"; or contains a character other than a letter, a number, "@", "#", "_", or "$". A name is also invalid if the receiver's model already has an EOEntity that has the same name or a stored procedure with an argument that has the same name.

`[setName](#apple-heyts)` uses this method to validate its argument.

---

[!](EODatabaseOperation.md)
[!](Creating%20an%20Entity.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
