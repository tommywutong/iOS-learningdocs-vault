---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOEntity.html
archived_at: '2026-07-15T08:13:41.525998Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOEntity

> __Inherits from:__ Object
>
> __Implements:__
> EOPropertyListEncoding
> EOSQLExpression.SQLValue
>
> __Package:__ com.webobjects.eoaccess

---

## Class Description

---

An EOEntity describes a table in a database and associates a name internal to the Framework with an external name by which the table is known to the database. An EOEntity maintains a group of attributes and relationships, which are collectively called properties. These are represented by the EOAttribute and EORelationship classes, respectively; see their specifications for more information.

You usually define entities in a model with the EOModeler application, which is documented in _Enterprise Objects Tools and Techniques_. EOEntity objects are primarily used by the Enterprise Objects Framework for mapping tables in the database to enterprise objects; your code will probably make limited use of them unless you're specifically working with models.

An EOEntity is associated with a specific class whose instances are used to represent records (rows) from the database in applications using layers at or above the database layer of the Enterprise Objects Framework. If an EOEntity doesn't have a specific class associated with it, instances of EOGenericRecord (defined in EOControl) are created.

An EOEntity may be marked as read-only, in which case any changes to rows or objects for that entity made by the database level objects are denied.

You can define an external query for an EOEntity to be used when a selection is attempted with an unrestricted qualifier (one that would select all rows in the entity's table). An external query is sent unaltered to the database server and so can use database-specific features such as stored procedures; external queries are thus useful for hiding records or invoking database-specific features. You can also assign stored procedures to be invoked upon particular database operations through the use of EOEntity's [setStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlukn2g64tfmrihe33dmvshk4tf) method.

Like the other major modeling classes, EOEntity provides a user dictionary for your application to store any application-specific information related to the entity.

For more information on programmatically creating EOEntity objects, see ["Creating an Entity" (page 219)](EOEntity-2.md#apple-irauurcbivdeu).

## Constants

---

EOEntity defines the following String constants:

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| FetchAllProcedureOperation | A stored procedure to fetch all records |
| FetchWithPrimaryKeyProcedureOperation | A stored procedure to fetch by primary key |
| InsertProcedureOperation | A stored procedure to insert a row |
| DeleteProcedureOperation | A stored procedure to delete a row |
| NextPrimaryKeyProcedureOperation | A stored procedure to generate a new primary key |

## Interfaces Implemented

---

> EOPropertyListEncoding awakeWithPropertyListencodeIntoPropertyList

## Method Types

---

> Constructors[EOEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexukt2fnz2gs5dz)Accessing the name[setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlujzqw2zi)[name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexw4ylnmu)[beautifyName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwezlbov2gsztzjzqw2zi)Accessing the model[model](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexw233emvwa)Specifying fetching behavior for the entity[setExternalQuery](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzluiv4hizlsnzqwyulvmvzhs)[externalQuery](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwk6dumvzg4ylmkf2wk4tz)[setRestrictingQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlukjsxg5dsnfrxi2lom5ixkylmnftgszls)[restrictingQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezltorzgsy3unfxgoulvmfwgsztjmvza)Accessing primary key qualifiers[qualifierForPrimaryKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxc5lbnruwm2lfojdg64sqojuw2ylspffwk6i)[isQualifierForPrimaryKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexws42rovqwy2lgnfsxertpojihe2lnmfzhss3fpe)Accessing a schema-based qualifier from a qualifier for in-memory evaluation[schemaBasedQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgy3imvwwcqtbonswiulvmfwgsztjmvza)Accessing attributes[addAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwczdeif2hi4tjmj2xizi)[anyAttributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc3tzif2hi4tjmj2xizkomfwwkza)[attributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc5duojuwe5lumvhgc3lfmq)[attributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc5duojuwe5lumvzq)[removeAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlnn53gkqluorzgsytvorsq)[attributesToFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc5duojuwe5lumvzvi32gmv2gg2a)Accessing relationships[addRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwczdekjswyylunfxw443infya)[anyRelationshipNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc3tzkjswyylunfxw443infye4ylnmvsa)[relationships](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlmmf2gs33oonugs4dt)[relationshipNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlmmf2gs33oonugs4comfwwkza)[removeRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlnn53gkutfnrqxi2lpnzzwq2lq)Checking referential integrity[externalModelsReferenced](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwk6dumvzg4ylmjvxwizlmonjgkztfojsw4y3fmq)[referencesProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlgmvzgk3tdmvzva4tpobsxe5dz)Accessing primary keys[globalIDForRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwo3dpmjqwyskeizxxeutpo4)[isPrimaryKeyValidInObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexws42qojuw2ylspffwk6kwmfwgszcjnzhwe2tfmn2a)[primaryKeyForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxa4tjnvqxe6klmv4um33si5wg6ytbnreui)[primaryKeyForRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxa4tjnvqxe6klmv4um33skjxxo)Accessing primary key attributes[setPrimaryKeyAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlukbzgs3lboj4uwzlzif2hi4tjmj2xizlt)[primaryKeyAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxa4tjnvqxe6klmv4uc5duojuwe5lumvzq)[primaryKeyAttributeNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxa4tjnvqxe6klmv4uc5duojuwe5lumvhgc3lfom)[primaryKeyRootName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxa4tjnvqxe6klmv4ve33porhgc3lf)[isValidPrimaryKeyAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexws42wmfwgszcqojuw2ylspffwk6kbor2he2lcov2gk)Accessing class properties[setClassProperties](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzluinwgc43tkbzg64dfoj2gszlt)[classProperties](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwg3dbonzva4tpobsxe5djmvzq)[classPropertyNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwg3dbonzva4tpobsxe5dzjzqw2zlt)[isValidClassProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexws42wmfwgszcdnrqxg42qojxxazlsor4q)Accessing the enterprise object class[classDescriptionForInstances](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwg3dbonzuizltmnzgs4dunfxw4rtpojew443umfxggzlt)[setClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzluinwgc43tjzqw2zi)[className](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwg3dbonzu4ylnmu)Accessing locking attributes[setAttributesUsedForLocking](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzluif2hi4tjmj2xizltkvzwkzcgn5zey33dnnuw4zy)[attributesUsedForLocking](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc5duojuwe5lumvzvk43fmrdg64smn5rww2lom4)[isValidAttributeUsedForLocking](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexws42wmfwgszcbor2he2lcov2gkvltmvsem33sjrxwg23jnztq)Accessing external name[setExternalName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzluiv4hizlsnzqwyttbnvsq)[externalName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwk6dumvzg4ylmjzqw2zi)[externalNameForInternalName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlooruxi6jpmv4hizlsnzqwyttbnvsum33sjfxhizlsnzqwyttbnvsq)[nameForExternalName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlooruxi6jpnzqw2zkgn5zek6dumvzg4ylmjzqw2zi)Accessing whether an entity is read only[setReadOnly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlukjswczcpnzwhs)[isReadOnly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexws42smvqwit3onr4q)Accessing the user dictionary[setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlukvzwk4sjnztg6)[userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxk43fojew4ztp)Working with stored procedures[setStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlukn2g64tfmrihe33dmvshk4tf)[storedProcedureForOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxg5dpojswiudsn5rwkzdvojsum33sj5ygk4tboruw63q)Working with fetch specifications[addFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwczdeizsxiy3iknygky3jmzuwgylunfxw4)[fetchSpecificationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwmzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zle)[fetchSpecificationNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwmzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zlt)[removeFetchSpecificationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlnn53gkrtforrwqu3qmvrwsztjmnqxi2lpnzhgc3lfmq)[addSharedObjectFetchSpecificationByName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwczdeknugc4tfmrhwe2tfmn2emzlumnufg4dfmnuwm2ldmf2gs33oij4u4ylnmu)[sharedObjectFetchSpecificationNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxg2dbojswit3cnjswg5cgmv2gg2ctobswg2lgnfrwc5djn5xe4ylnmvzq)[setSharedObjectFetchSpecificationsByName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzluknugc4tfmrhwe2tfmn2emzlumnufg4dfmnuwm2ldmf2gs33oonbhsttbnvsq)[removeSharedObjectFetchSpecificationByName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlnn53gku3imfzgkzcpmjvgky3uizsxiy3iknygky3jmzuwgylunfxw4qtzjzqw2zi)Working with entity inheritance hierarchies[parentEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxaylsmvxhirlooruxi6i)[subEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxg5lcivxhi2lunfsxg)[addSubEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwczdekn2werlooruxi6i)[removeSubEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlnn53gku3vmjcw45djor4q)[setIsAbstractEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlujfzucyttorzgcy3uivxhi2lupe)[isAbstractEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexws42bmjzxi4tbmn2ek3tunf2hs)Specifying fault behavior[setMaxNumberOfInstancesToBatchFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlujvqxqttvnvrgk4spmzew443umfxggzltkrxueylumnuemzlumnua)[maxNumberOfInstancesToBatchFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexw2ylyjz2w2ytfojhwmsloon2gc3tdmvzvi32cmf2gg2cgmv2gg2a)Caching objects[setCachesObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzluinqwg2dfonhwe2tfmn2hg)[cachesObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwgyldnbsxgt3cnjswg5dt)

## Constructors

---

### EOEntity

`public EOEntity( NSDictionary propertyList, Object owner)`

Creates a new EOEntity initialized from _propertyList_-a dictionary containing only property list data types (that is, NSDictionary, NSArray, NSData, and String). This constructor is used by EOModeler when it reads in an EOModel from a file, for example. The _owner_ argument should be the EOEntity's EOModel. Entities created from a property list must receive an awakeWithPropertyList (EOPropertyListEncoding) message after creation before they are fully functional, but the __awake...__ message should be deferred until the all of the other objects in the model have also been created.

__See Also:__ encodeIntoPropertyList (EOPropertyListEncoding)

`public EOEntity()`

Description forthcoming.

---

## Static Methods

---

### externalNameForInternalName

`public static String externalNameForInternalName( String name, String separatorString, boolean useAllCaps)`

Used by the Framework to convert modeling object names to database schema names that conform to a standard convention. A conforming database schema name is upper-case and uses "_" to separate words. Consequently "name" becomes "NAME" and "firstName" becomes "FIRST_NAME".

_separatorString_ is a character that is used to separate words. The Framework uses "_" by default as in the examples above. _useAllCaps_ indicates whether to capitalize the name. For example, providing __false__ converts "firstName" to "first_name".

---

### nameForExternalName

`public static String nameForExternalName( String name, String separatorString, boolean initialCaps)`

Used by name beautification to convert database schema names to modeling object names that conform to a standard convention. A conforming attribute, relationship, or stored procedure name is lower-case except for the initial letter of each embedded word other than the first, which is upper case. Consequently "NAME" becomes "name" and "FIRST_NAME" becomes "firstName". A conforming entity is all lower-case except for the initial letter of each word. Consequently "CUSTOMER_ACCOUNT" becomes "CustomerAccount".

_separatorString_ is a character that is used to separate words. The Framework uses "_" by default as in the examples above. _initialCaps_ indicates whether to capitalize the first letter of the first word. By default, the Framework uses __true__ for entities and __false__ for everything else.

__See Also:__ beautifyNames (EOModel), [beautifyName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwezlbov2gsztzjzqw2zi), - __beautifyName__ (EOAttribute, EORelationship, EOStoredProcedure)

---

## Instance Methods

---

### addAttribute

`public void addAttribute(EOAttribute anAttribute)`

Adds _anAttribute_ to the receiver. Throws an exception if _anAttribute_'s name is already in use by another attribute or relationship. Sets _anAttribute_'s entity to `this`.

__See Also:__ [removeAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlnn53gkqluorzgsytvorsq), [attributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc5duojuwe5lumvzq), [attributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc5duojuwe5lumvhgc3lfmq)

---

### addFetchSpecification

`public void addFetchSpecification( com.webobjects.eocontrol.EOFetchSpecification fetchSpec, String fetchSpecName)`

Adds the fetch specification and associates _fetchSpecName_ with it.

__See Also:__ [fetchSpecificationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwmzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zle), [fetchSpecificationNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwmzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zlt), [removeFetchSpecificationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlnn53gkrtforrwqu3qmvrwsztjmnqxi2lpnzhgc3lfmq)

---

### addRelationship

`public void addRelationship(EORelationship aRelationship)`

Adds _aRelationship_ to the receiver. Throws an exception if _aRelationship_'s name is already in use by another attribute or relationship. Sets _aRelationship_'s entity to `this`.

__See Also:__ [removeRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlnn53gkutfnrqxi2lpnzzwq2lq), [relationships](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlmmf2gs33oonugs4dt), [relationshipNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlmmf2gs33oonugs4comfwwkza)

---

### addSharedObjectFetchSpecificationByName

`public void addSharedObjectFetchSpecificationByName(String name)`

Adds the fetch specification identified by _name_ to the set of fetch specifications used to load objects into a shared editing context.

---

### addSubEntity

`public void addSubEntity(EOEntity child)`

Causes the child entity _child_ to "inherit" from the receiver. This is the first step in setting up an inheritance hierarchy between entities.

__See Also:__ [subEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxg5lcivxhi2lunfsxg), [removeSubEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlnn53gku3vmjcw45djor4q)

---

### anyAttributeNamed

`public EOAttribute anyAttributeNamed(String attributeName)`

Returns the user-created attribute identified by _attributeName_. If no such attribute exists, this method looks through the "hidden" attributes created by the Enterprise Objects Framework for one with the given name. Hidden attributes are used for such things as primary keys on target entities of flattened attributes. If none is found, `null` is returned.

__See Also:__ [attributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc5duojuwe5lumvhgc3lfmq), [attributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc5duojuwe5lumvzq)

---

### anyRelationshipNamed

`public EORelationship anyRelationshipNamed(String relationshipName)`

Returns the user-created relationship identified by _relationshipName_. If none exists, this method looks through the "hidden" relationships created by the Enterprise Objects Framework for one with the given name. If none is found, `null` is returned.

__See Also:__ [relationshipNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlmmf2gs33oonugs4comfwwkza), [relationships](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlmmf2gs33oonugs4dt)

---

### attributeNamed

`public EOAttribute attributeNamed(String attributeName)`

Returns the attribute named _attributeName_, or `null` if no such attribute exists.

__See Also:__ [anyAttributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc3tzif2hi4tjmj2xizkomfwwkza), [attributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc5duojuwe5lumvzq), [relationshipNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlmmf2gs33oonugs4comfwwkza)

---

### attributes

`public NSArray attributes()`

Returns all of the receiver's attributes, or `null` if the receiver has none.

__See Also:__ [anyAttributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc3tzif2hi4tjmj2xizkomfwwkza), [attributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc5duojuwe5lumvhgc3lfmq)

---

### attributesToFetch

`public NSArray attributesToFetch()`

Returns an array of the EOAttributes that need to be fetched so that they can be included in the row snapshot. The set of attributes includes:

1. Attributes that are class properties, "used for locking," or primary keys.
2. Source attributes of any to-many relationship (flattened or non-flattened) that is a class property.
3. Source attributes of any non-flattened, to-one relationship that is a class property or that is used by a flattened attribute that is a class property.
4. The foreign key attributes of any flattened, to-one relationship that is a class property or that is used by a class property.

---

### attributesUsedForLocking

`public NSArray attributesUsedForLocking()`

Returns an array containing those properties whose values must match a snapshot any time a row is updated.

Attributes used for locking are those whose values are compared when a database-level object performs an update. When the database-level classes fetch an enterprise object, they cache these attributes' values in a snapshot. Later, when the enterprise object is updated, the values of these attributes in the object are checked with those in the snapshot-if they differ, the update fails. See the EODatabaseContext class specification for more information.

---

### __awakeWithPropertyList__

`public void awakeWithPropertyList(NSDictionary pList)`

Description forthcoming.

---

### beautifyName

`public void beautifyName()`

Makes the receiver's name conform to a standard convention. EOEntity names that conform to this style are all lower-case except for the initial letter of each word, which is upper case. Thus, "MOVIE" becomes "Movie", and "MOVIE_ROLE" becomes "MovieRole".

__See Also:__ [setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlujzqw2zi), beautifyNames (EOModel)

---

### cachesObjects

`public boolean cachesObjects()`

Returns `true` if all of the objects from the receiver are to be cached in memory and queries are to be evaluated in-memory using this cache rather than in the database. This method should only be used for fairly small tables of read-only objects, since the first access to the receiver will trigger fetching the entire table. You should generally restrict this method to read-only entities to avoid cached data getting out of sync with database data. Also, you shouldn't use this method if your application will be making queries against the entity that can't be evaluated in memory.

__See Also:__ [setCachesObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzluinqwg2dfonhwe2tfmn2hg)

---

### classDescriptionForInstances

`public com.webobjects.eocontrol.EOClassDescription classDescriptionForInstances()`

Returns the EOClassDescription associated with the receiver. The EOClassDescription class provides a mechanism for extending classes by giving them access to the metadata contained in an EOModel (or another external source of information). In an application, EOClassDescriptions are registered on demand for the EOEntity on which an enterprise object is based. For more information, see the class specifications for EOClassDescription (in EOControl) and EOEntityClassDescription.

---

### className

`public String className()`

Returns the name of the enterprise object class associated with the receiver. When a row is fetched for the receiver by a database-level object, it's returned as an instance of this class. This class might not be present in the run-time system, and in fact your application may have to load it on demand. If your application doesn't load a class, EOGenericRecord is used.

An enterprise object class other than EOGenericRecord can be mapped to only one entity.

---

### classProperties

`public NSArray classProperties()`

Returns an array containing the properties that are bound to the receiver's class (so that instances of the class will be passed values corresponding to those properties). This is a subset of the receiver's attributes and relationships.

__See Also:__ [classPropertyNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwg3dbonzva4tpobsxe5dzjzqw2zlt)

---

### classPropertyNames

`public NSArray classPropertyNames()`

Returns an array containing the names of those properties that are bound to the receiver's class (so that instances of the class will be passed values corresponding to those properties). This is a subset of the receiver's attributes and relationships.

__See Also:__ [classProperties](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwg3dbonzva4tpobsxe5djmvzq)

---

### clientClassName

`public String clientClassName()`

Returns the name of the client-side enterprise object class associated with the receiver. If no client-side class name has yet been registered for the receiver, this method returns the name of the receiving class (either EOEntity or a subclass of EOEntity). Equivalent to the 4.5 com.webobjects.eodistribution.EOAccessAdditions's __clientClassNameForEntity.__

---

### clientClassProperties

`public NSArray clientClassProperties()`

Returns an array containing the properties that are bound to the client-side class corresponding to the receiver. If no information about the client-side class's properties is available, this method returns the receiver's class properties. The properties returned by this method are the attributes and relationships that are used by the client. Only these attributes and relationships will be shipped to the client. Equivalent to the 4.5 com.webobjects.eodistribution.EOAccessAdditions's __clientClassPropertiesForEntity__.

---

### clientClassPropertyNames

`public NSArray clientClassPropertyNames()`

Returns an array containing the names of the properties that are bound to the client-side class corresponding to the receiver. If no information about the client-side class's properties is available, this method returns the names of the receiver's class properties. The property names returned by this method are the attributes and relationships that are used by the client. Only these attributes and relationships will be shipped to the client. Equivalent to the 4.5 com.webobjects.eodistribution.EOAccessAdditions's __clientClassPropertyNamesForEntity__.

---

### __encodeIntoPropertyList__

`public void encodeIntoPropertyList(NSMutableDictionary aDictionary)`

Description forthcoming.

---

### externalModelsReferenced

`public NSArray externalModelsReferenced()`

Examines each of the receiver's relationships and returns a list of all external models referenced by the receiver.

__See Also:__ [referencesProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlgmvzgk3tdmvzva4tpobsxe5dz)

---

### externalName

`public String externalName()`

Returns the name of the receiver as understood by the database server.

---

### externalQuery

`public String externalQuery()`

Returns a query statement that's used by an EOAdaptorChannel to select rows for the receiver when a qualifier is empty, or `null` if the receiver has no external query. An empty qualifier is one that specifies only the entity, and would thus fetch all enterprise objects for that entity.

External queries are useful for hiding records or invoking database-specific features such as stored procedures when an application attempts to select all records for an entity. You can also use the EOStoredProcedure class to work with stored procedures; for more information see the EOStoredProcedure class specification.

__See Also:__ [setExternalQuery](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzluiv4hizlsnzqwyulvmvzhs)

---

### fetchSpecificationNamed

`public com.webobjects.eocontrol.EOFetchSpecification fetchSpecificationNamed(String fetchSpecName)`

Returns the fetch specification associated with _fetchSpecName_.

__See Also:__ [addFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwczdeizsxiy3iknygky3jmzuwgylunfxw4), [fetchSpecificationNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwmzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zlt), [removeFetchSpecificationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlnn53gkrtforrwqu3qmvrwsztjmnqxi2lpnzhgc3lfmq)

---

### fetchSpecificationNames

`public NSArray fetchSpecificationNames()`

Returns an alphabetically sorted array of names of the entity's fetch specifications.

__See Also:__ [addFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwczdeizsxiy3iknygky3jmzuwgylunfxw4), [fetchSpecificationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwmzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zle), [removeFetchSpecificationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlnn53gkrtforrwqu3qmvrwsztjmnqxi2lpnzhgc3lfmq)

---

### globalIDForRow

`public com.webobjects.eocontrol.EOGlobalID globalIDForRow(NSDictionary row)`

Constructs a global identifier from the specified row for the receiver.

__See Also:__ [primaryKeyForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxa4tjnvqxe6klmv4um33si5wg6ytbnreui)

---

### isAbstractEntity

`public boolean isAbstractEntity()`

Returns `true` to indicate that the receiver is abstract, `false` otherwise. An abstract entity is one that has no corresponding enterprise objects in your application. Abstract entities are used to model inheritance relationships. For example, you might have a Person abstract entity that acts as the parent of Customer and Employee entities. Customer and Employee would inherit certain characteristics from Person (such as name and address attributes). However, though your application might have Customer and Employee objects, it would never have a Person object.

__See Also:__ [setIsAbstractEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlujfzucyttorzgcy3uivxhi2lupe)

---

### isPrimaryKeyValidInObject

`public boolean isPrimaryKeyValidInObject(NSKeyValueCoding anObject)`

Returns `true` if every key attribute is present in _anObject_ and has a value that is not `null`. Returns `false` otherwise. This method uses the EOKeyValueCoding interface so a dictionary may be provided instead of an enterprise object.

__See Also:__ [primaryKeyForRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxa4tjnvqxe6klmv4um33skjxxo)

---

### isQualifierForPrimaryKey

`public boolean isQualifierForPrimaryKey(com.webobjects.eocontrol.EOQualifier aQualifier)`

Returns `true` if _aQualifier_ describes the primary key and nothing but the primary key, `false` otherwise.

---

### isReadOnly

`public boolean isReadOnly()`

Returns `true` if the receiver can't be modified, `false` if it can. If an entity can't be modified, then enterprise objects fetched for that entity also can't be modified (that is, inserted, deleted, or updated).

---

### isValidAttributeUsedForLocking

`public boolean isValidAttributeUsedForLocking(EOAttribute anAttribute)`

Returns `false` if _anAttribute_ isn't an EOAttribute, if the EOAttribute doesn't belong to the receiver, or if _anAttribute_ is derived. Otherwise returns `true`. An attribute that isn't valid for locking will cause [setAttributesUsedForLocking](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzluif2hi4tjmj2xizltkvzwkzcgn5zey33dnnuw4zy) to fail.

__See Also:__ [attributesUsedForLocking](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc5duojuwe5lumvzvk43fmrdg64smn5rww2lom4)

---

### isValidClassProperty

`public boolean isValidClassProperty(Object aProperty)`

Returns `false` if either _aProperty_ isn't an EOAttribute or EORelationship, or if _aProperty_ doesn't belong to the receiver. Otherwise returns `true`. Note that this method doesn't tell you whether _aProperty_ is a member of the array returned by [classProperties](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwg3dbonzva4tpobsxe5djmvzq). In other words, unlike __classProperties__, [classPropertyNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwg3dbonzva4tpobsxe5dzjzqw2zlt), and [setClassProperties](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzluinwgc43tkbzg64dfoj2gszlt), this method doesn't interact with the properties bound to the entity's enterprise object class.

---

### isValidPrimaryKeyAttribute

`public boolean isValidPrimaryKeyAttribute(EOAttribute anAttribute)`

Returns `false` if _anAttribute_ isn't an EOAttribute, doesn't belong to the receiver, or is derived. Otherwise returns `true`.

__See Also:__ [setPrimaryKeyAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlukbzgs3lboj4uwzlzif2hi4tjmj2xizlt)

---

### maxNumberOfInstancesToBatchFetch

`public int maxNumberOfInstancesToBatchFetch()`

Returns the maximum number of to-one faults from the receiver to fire at one time. See the method description for [setMaxNumberOfInstancesToBatchFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlujvqxqttvnvrgk4spmzew443umfxggzltkrxueylumnuemzlumnua) for more explanation of what this means.

---

### model

`public EOModel model()`

Returns the model that contains the receiver.

__See Also:__ addEntity (EOModel)

---

### name

`public String name()`

Returns the receiver's name.

---

### parentEntity

`public EOEntity parentEntity()`

Returns the entity from which the receiver inherits.

__See Also:__ [subEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxg5lcivxhi2lunfsxg)

---

### primaryKeyAttributeNames

`public NSArray primaryKeyAttributeNames()`

Returns an array containing the names of the attributes that make up the receiver's primary key.

__See Also:__ [primaryKeyAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxa4tjnvqxe6klmv4uc5duojuwe5lumvzq)

---

### primaryKeyAttributes

`public NSArray primaryKeyAttributes()`

Returns an array of those attributes that make up the receiver's primary key.

__See Also:__ [primaryKeyAttributeNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxa4tjnvqxe6klmv4uc5duojuwe5lumvhgc3lfom)

---

### primaryKeyForGlobalID

`public NSDictionary primaryKeyForGlobalID(com.webobjects.eocontrol.EOGlobalID globalID)`

Returns the primary key for the object identified by _globalID_.

__See Also:__ [globalIDForRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwo3dpmjqwyskeizxxeutpo4)

---

### primaryKeyForRow

`public NSDictionary primaryKeyForRow(NSDictionary aRow)`

Returns the primary key for _aRow_, or `null` if the primary key can't be computed. The primary key is a dictionary whose keys are attribute names and whose values are values for those attributes.

__See Also:__ [primaryKeyForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxa4tjnvqxe6klmv4um33si5wg6ytbnreui)

---

### primaryKeyRootName

`public String primaryKeyRootName()`

Returns the external name (that is, the name as it's understood by the database) of the receiver's root entity. If the receiver has no parent entity, returns the receiver's external name.

__See Also:__ [externalName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwk6dumvzg4ylmjzqw2zi), [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexw4ylnmu), [parentEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxaylsmvxhirlooruxi6i)

---

### qualifierForPrimaryKey

`public com.webobjects.eocontrol.EOQualifier qualifierForPrimaryKey(NSDictionary aRow)`

Returns a qualifier for the receiver that can be used to fetch an instance of the receiver with the primary key extracted from _aRow_.

__See Also:__ [isQualifierForPrimaryKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexws42rovqwy2lgnfsxertpojihe2lnmfzhss3fpe), [restrictingQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezltorzgsy3unfxgoulvmfwgsztjmvza)

---

### referencesProperty

`public boolean referencesProperty(Object aProperty)`

Returns `true` if any of the receiver's attributes or relationships reference _aProperty_, `false` otherwise. A property can be referenced by a flattened attribute or by a relationship. For example, suppose a model has an Employee entity with a __toDepartment__ relationship. If you flatten the department's name attribute into the Employee entity, creating a __departmentName__ attribute, that flattened attribute references the __toDepartment__ relationship.

If an entity has any outstanding references to a property, you shouldn't remove the property.

__See Also:__ [removeAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlnn53gkqluorzgsytvorsq), [removeRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlnn53gkutfnrqxi2lpnzzwq2lq)

---

### relationshipNamed

`public EORelationship relationshipNamed(String name)`

Returns the relationship named _name_, or `null` if the receiver has no such relationship.

__See Also:__ [anyRelationshipNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc3tzkjswyylunfxw443infye4ylnmvsa), [attributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc5duojuwe5lumvhgc3lfmq), [relationships](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlmmf2gs33oonugs4dt)

---

### relationships

`public NSArray relationships()`

Returns all of the receiver's relationships, or `null` if the receiver has none.

__See Also:__ [attributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc5duojuwe5lumvzq)

---

### removeAttribute

`public void removeAttribute(EOAttribute name)`

Removes the attribute named _name_ if it exists. You should always use [referencesProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlgmvzgk3tdmvzva4tpobsxe5dz)to check that an attribute isn't referenced by another property before removing it.

__See Also:__ [addAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwczdeif2hi4tjmj2xizi), [attributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwc5duojuwe5lumvzq)

---

### removeFetchSpecificationNamed

`public void removeFetchSpecificationNamed(String fetchSpecName)`

Removes the fetch specification referred to by _fetchSpecName_.

__See Also:__ [addFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwczdeizsxiy3iknygky3jmzuwgylunfxw4), [fetchSpecificationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwmzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zle), [fetchSpecificationNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwmzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zlt)

---

### removeRelationship

`public void removeRelationship(EORelationship name)`

Removes the relationship named _name_ if it exists. You should always use [referencesProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlgmvzgk3tdmvzva4tpobsxe5dz) to check that a relationship isn't referenced by another property before removing it.

__See Also:__ [addRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwczdekjswyylunfxw443infya), [relationships](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlmmf2gs33oonugs4dt)

---

### removeSharedObjectFetchSpecificationByName

`public void removeSharedObjectFetchSpecificationByName(String name)`

Removes the fetch specification identified by _name_ from the set of fetch specifications used to load objects into a shared editing context.

---

### removeSubEntity

`public void removeSubEntity(EOEntity child)`

Removes _child_ from the receiver's list of sub-entities.

__See Also:__ [addSubEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwczdekn2werlooruxi6i), [subEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxg5lcivxhi2lunfsxg)

---

### restrictingQualifier

`public com.webobjects.eocontrol.EOQualifier restrictingQualifier()`

Returns the qualifier used to restrict all queries made against the receiver. Restricting qualifiers are useful when there is not a one-to-one mapping between an entity and a particular database table, or when you always want to filter the data that's returned for a particular entity.

For example, if you're using the "one table" inheritance model in which parent and child data is contained in the same table, you'd use a restricting qualifier to fetch objects of the appropriate type. To give a non-inheritance example, for an Employees table you might create a "Sales" entity that has a restricting qualifier that only fetches employees who are in the Sales department.

__See Also:__ [setRestrictingQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlukjsxg5dsnfrxi2lom5ixkylmnftgszls)

---

### schemaBasedQualifier

`public com.webobjects.eocontrol.EOQualifier schemaBasedQualifier( com.webobjects.eocontrol.EOQualifier aQualifier)`

Returns a qualifier based on _aQualifier_ suitable for evaluation by a database (as opposed to in-memory evaluation). Invoked by an EODatabaseChannel object before it uses its EOAdaptorChannel to perform a database operation.

Whereas in-memory qualifier evaluation uses object instance variables to resolve relationships, a database qualifier must use foreign keys. For example, consider a qualifier that is used to fetch all employees who work in a specified department:

```
Department dept;    // Assume this exists.
EOQualifier qualifier;
NSMutableArray qualArgs = new NSMutableArray();
qualArgs.addObject(dept);
qualifier = EOQualifier.qualifierWithQualifierFormat("department = %@", qualArgs);
```

For an in-memory search, the Framework queries employee objects for their department object and includes an employee in the result list if its department object is equal to __dept__. (See EOControl's EOQualifierEvaluation interface description for more information on in-memory searching.)

For a database search, the Framework needs to qualify the fetch by specifying a foreign key value for __dept__. The Framework sends the EOEntity class a [schemaBasedQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgy3imvwwcqtbonswiulvmfwgsztjmvza) message that creates a new EOQualifier object from __qualifier__. Assume that the entity for employee objects has an attribute named __departmentID__ and that the primary key value for __dept__ is 459, the resulting qualifier specifies the search conditions as:

```
department.departmentID = 459
```

__See Also:__ selectObjectsWithFetchSpecification (EODatabaseChannel)

---

### setAttributesUsedForLocking

`public boolean setAttributesUsedForLocking(NSArray attributes)`

Sets _attributes_ as the attributes used when an EODatabaseChannel locks enterprise objects for updates. Returns `false` and doesn't set the attributes used for locking if any of the attributes in _attributes_ responds `false` to [isValidAttributeUsedForLocking](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexws42wmfwgszcbor2he2lcov2gkvltmvsem33sjrxwg23jnztq); returns `true` otherwise. See the EODatabase, EODatabaseContext, and EODatabaseChannel class specifications for information on locking.

---

### setCachesObjects

`public void setCachesObjects(boolean flag)`

Sets according to _flag_ whether all of the receiver's objects are cached the first time the associated table is queried.

__See Also:__ [cachesObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwgyldnbsxgt3cnjswg5dt)

---

### setClassName

`public void setClassName(String name)`

Assigns _name_ as the name of the class associated with the receiver or "EOGenericRecord" if _name_ is `null`. The specified class need not be present in the run-time system when this message is sent. When an EODatabaseChannel fetches objects for the receiver, they're created as instances of this class. Your application may have to load the class on demand if it isn't present in the run-time system; if it doesn't load the class, EOGenericRecord will be used.

An enterprise object class other than EOGenericRecord can be mapped to only one entity.

__See Also:__ [className](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwg3dbonzu4ylnmu)

---

### setClassProperties

`public boolean setClassProperties(NSArray properties)`

Sets the receiver's class properties to the EOAttributes and EORelationships in _properties_ and returns `true`, unless the receiver responds `false` to [isValidClassProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexws42wmfwgszcdnrqxg42qojxxazlsor4q) for any of the objects in the array. In this event, the receiver's class properties aren't changed and `false` is returned.

---

### setExternalName

`public void setExternalName(String name)`

Sets the name of the receiver as understood by the database server to _name_. For example, though your application may know the entity as "JobTitle" the database may require a form such as "JOB_TTL". An adaptor uses the external name to communicate with the database; your application should never need to use the external name.

---

### setExternalQuery

`public void setExternalQuery(String aQuery)`

Assigns _aQuery_ as the query statement used for selecting rows from the receiver when there is no qualifier.

External queries are useful for hiding records or invoking database-specific features such as stored procedures when an application attempts to select all records for an entity. You can also use the EOStoredProcedure class to work with stored procedures; for more information see the EOStoredProcedure class specification.

An external query is sent unaltered to the database server, and so must contain the external (column) names instead of the names of EOAttributes. However, to work properly with the adaptor the external query must use the columns in alphabetical order by their corresponding EOAttributes' names.

__See Also:__ columnName (EOAttribute), [externalQuery](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwk6dumvzg4ylmkf2wk4tz)

---

### setIsAbstractEntity

`public void setIsAbstractEntity(boolean flag)`

Sets according to _flag_ whether the receiver is an abstract entity. For more discussion of abstract entities, see the method description for [isAbstractEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexws42bmjzxi4tbmn2ek3tunf2hs).

---

### setMaxNumberOfInstancesToBatchFetch

`public void setMaxNumberOfInstancesToBatchFetch(int size)`

Sets the maximum number of faults from the receiver to trigger at one time. By default, only one object is fetched from the database when you trigger a fault. You can optionally use this method to set to size the number of faults of the same entity should be fetched from the database along with the first one. Using this technique helps to optimize performance by taking advantage of round trips to the database.

__See Also:__ [maxNumberOfInstancesToBatchFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexw2ylyjz2w2ytfojhwmsloon2gc3tdmvzvi32cmf2gg2cgmv2gg2a)

---

### setName

`public void setName(String name)`

Sets the receiver's name to _name_. Throws an exception `NSInvalidArgumentException` if _name_ is already in use by another entity in the same EOModel or if _name_ is not a valid entity name.

__See Also:__ [beautifyName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwezlbov2gsztzjzqw2zi)

---

### setPrimaryKeyAttributes

`public boolean setPrimaryKeyAttributes(NSArray keys)`

If the receiver responds `false` to [isValidPrimaryKeyAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexws42wmfwgszcqojuw2ylspffwk6kbor2he2lcov2gk) for any of the objects in _keys_, this method returns `false`. Otherwise, this method sets the primary key attributes to the attributes in _keys_ and returns `true`.

You should exercise care in choosing primary key attributes. Floating-point numbers, for example, can't be reliably compared for equality, and are thus unsuitable for use in primary keys. Integer and string types are the safest choice for primary keys. BigDecimal NSDecimalNumber objects will work, but they'll entail more overhead than integers.

__See Also:__ [isValidPrimaryKeyAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexws42wmfwgszcqojuw2ylspffwk6kbor2he2lcov2gk)

---

### setReadOnly

`public void setReadOnly(boolean flag)`

Sets according to _flag_ whether the database rows for the receiver can be modified by the database level objects.

__See Also:__ [isReadOnly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexws42smvqwit3onr4q)

---

### setRestrictingQualifier

`public void setRestrictingQualifier(com.webobjects.eocontrol.EOQualifier aQualifier)`

Assigns _aQualifier_ as the qualifier used to restrict all queries made against the receiver. The restricting qualifier can be used to map an entity to a subset of the rows in a table. For more discussion of this subject, see the description for [restrictingQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezltorzgsy3unfxgoulvmfwgsztjmvza).

---

### setSharedObjectFetchSpecificationsByName

`public void setSharedObjectFetchSpecificationsByName(NSArray names)`

Sets the fetch specifications used to load objects into a shared editing context to the fetch specifications identified by name in the provided array, _names_.

---

### setStoredProcedure

`public void setStoredProcedure( EOStoredProcedure storedProcedure, String operation)`

Sets _storedProcedure_ for _operation_. _operation_ can be one of the following:

- [FetchAllProcedureOperation](#apple-irauurcjijdeq)
- [FetchWithPrimaryKeyProcedureOperation](#apple-irauusscjbaui)
- [InsertProcedureOperation](#apple-irauuq2bizdus)
- [DeleteProcedureOperation](#apple-irauur2jifbec)
- [NextPrimaryKeyProcedureOperation](#apple-irauur2civdei)

This information is used when changes from the object graph have been transformed into EODatabaseOperations that are being used to construct EOAdaptorOperations. At this point, Enterprise Objects Framework checks the entities associated with the changed objects to see if the entities have any stored procedures defined for the operation being performed.

__See Also:__ [storedProcedureForOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxg5dpojswiudsn5rwkzdvojsum33sj5ygk4tboruw63q)

---

### setUserInfo

`public void setUserInfo(NSDictionary dictionary)`

Sets the _dictionary_ of auxiliary data, which your application can use for whatever it needs. _dictionary_ can only contain property list data types-that is, String, NSDictionary, NSArray, and NSData.

---

### sharedObjectFetchSpecificationNames

`public NSArray sharedObjectFetchSpecificationNames()`

Returns an array of strings, which are the names of the fetch specifications used to load objects into a shared editing context.

---

### storedProcedureForOperation

`public EOStoredProcedure storedProcedureForOperation(String operation)`

Returns the stored procedure for the specified _operation_, if one has been set. Otherwise, returns `null`. _operation_ can be one of the following:

- [FetchAllProcedureOperation](#apple-irauurcjijdeq)
- [FetchWithPrimaryKeyProcedureOperation](#apple-irauusscjbaui)
- [InsertProcedureOperation](#apple-irauuq2bizdus)
- [DeleteProcedureOperation](#apple-irauur2jifbec)
- [NextPrimaryKeyProcedureOperation](#apple-irauur2civdei)

__See Also:__ [setStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlukn2g64tfmrihe33dmvshk4tf), parameterDirection (EOAttribute), storedProcedure (EOAttribute)

---

### subEntities

`public NSArray subEntities()`

Returns a list of those entities which inherit from the receiver.

__See Also:__ [addSubEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwczdekn2werlooruxi6i), [parentEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxaylsmvxhirlooruxi6i), [removeSubEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxezlnn53gku3vmjcw45djor4q)

---

### __toString__

`public String toString()`

Returns a String representation of the receiver.

---

### userInfo

`public NSDictionary userInfo()`

Returns a dictionary of user data. Your application can use this to store any auxiliary information it needs.

__See Also:__ [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlukvzwk4sjnztg6)

---

### valueForSQLExpression

`public String valueForSQLExpression(EOSQLExpression context)`

Conformance to EOSQLExpression.SQLValue.

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
