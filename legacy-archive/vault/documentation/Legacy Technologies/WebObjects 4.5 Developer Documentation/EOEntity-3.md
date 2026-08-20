---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOEntity.html
archived_at: '2026-07-15T08:11:33.615772Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOEntity

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EOEntity.h

---

## Class Description

---

An EOEntity describes a table in a database and associates
a name internal to the Framework with an external name by which
the table is known to the database. An EOEntity maintains a group
of attributes and relationships, which are collectively called properties.
These are represented by the [EOAttribute](EOAttribute-3.md#apple-incuqq2ijfeue) and [EORelationship](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#BFCDGGAG) classes, respectively;
see their specifications for more information.

You usually define entities in a model with the EOModeler
application, which is documented in _Enterprise Objects
Tools and Techniques_. EOEntity objects are primarily
used by the Enterprise Objects Framework for mapping tables in the
database to enterprise objects; your code will probably make limited
use of them unless you're specifically working with models.

An EOEntity is associated with a specific class whose instances
are used to represent records (rows) from the database in applications
using layers at or above the database layer of the Enterprise Objects Framework.
If an EOEntity doesn't have a specific class associated with it,
instances of EOGenericRecord (defined in EOControl) are created.

An EOEntity may be marked as read-only, in which case any
changes to rows or objects for that entity made by the database
level objects are denied.

You can define an external query for an EOEntity to be used
when a selection is attempted with an unrestricted qualifier (one
that would select all rows in the entity's table). An external
query is sent unaltered to the database server and so can use database-specific
features such as stored procedures; external queries are thus useful
for hiding records or invoking database-specific features. You can
also assign stored procedures to be invoked upon particular database
operations through the use of EOEntity's [setStoredProcedure:forOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5ctorxxezlekbzg6y3fmr2xezj2mzxxet3qmvzgc5djn5xdu) method.

Like the other major modeling classes, EOEntity provides a
user dictionary for your application to store any application-specific
information related to the entity.

For more information on programmatically creating EOEntity
objects, see ["Creating an Entity"](EOEntity-4.md#apple-irauurcbivdeu).

## Constants

---

EOEntityEOAccess defines the following NSString constants in EOEntity.h:

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| EOFetchAllProcedureOperation | A stored procedure to fetch all records |
| EOFetchWithPrimaryKeyProcedureOperation | A stored procedure to fetch by primary key |
| EOInsertProcedureOperation | A stored procedure to insert a row |
| EODeleteProcedureOperation | A stored procedure to delete a row |
| EONextPrimaryKeyProcedureOperation | A stored procedure to generate a new primary key |

## Adopted Protocols

---

> EOPropertyListEncoding: [- initWithPropertyList:owner:](EOPropertyListEncoding-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2qojxxazlsor4uy2ltorcw4y3pmruw4zzpnfxgs5cxnf2gqudsn5ygk4tupfggs43uhjxxo3tfoi5a)
> : [- awakeWithPropertyList](EOPropertyListEncoding-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2qojxxazlsor4uy2ltorcw4y3pmruw4zzpmf3wc23fk5uxi2cqojxxazlsor4uy2ltoq)
> : [- encodeIntoPropertyList:](EOPropertyListEncoding-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2qojxxazlsor4uy2ltorcw4y3pmruw4zzpmvxgg33emvew45dpkbzg64dfoj2hstdjon2du)

## Method Types

---

> **Accessing the name**
> : [- setName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5comfwwkoq)
> : [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5xgc3lf)
> : [- validateName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf53gc3djmrqxizkomfwwkoq)
> : [- beautifyName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5rgkylvoruwm6komfwwk)
>
> **Accessing the model**
> : [- model](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5ww6zdfnq)
>
> **Specifying fetching behavior
> for the entity**
> : [- setExternalQuery:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cfpb2gk4tomfwfc5lfoj4tu)
> : [- externalQuery](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5sxq5dfojxgc3crovsxe6i)
> : [- setRestrictingQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5csmvzxi4tjmn2gs3thkf2wc3djmzuwk4r2)
> : [- restrictingQualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk43uojuwg5djnztvc5lbnruwm2lfoi)
>
> **Accessing primary key
> qualifiers**
> : [- qualifierForPrimaryKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5yxkylmnftgszlsizxxeudsnfwwc4tzjnsxsoq)
> : [- isQualifierForPrimaryKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5uxgulvmfwgsztjmvzem33skbzgs3lboj4uwzlzhi)
>
> **Accessing attributes**
> : [- addAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qwizcbor2he2lcov2gkoq)
> : [- anyAttributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qw46kbor2he2lcov2gkttbnvswioq)
> : [- attributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfjzqw2zlehi)
> : [- attributes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfom)
> : [- removeAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3lpozsuc5duojuwe5lumu5a)
> : [- attributesToFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfonkg6rtforrwq)
>
> **Accessing relationships**
> : [- addRelationship:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qwizcsmvwgc5djn5xhg2djoa5a)
> : [- anyRelationshipNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qw46ksmvwgc5djn5xhg2djobhgc3lfmq5a)
> : [- relationships](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3dboruw63ttnbuxa4y)
> : [- relationshipNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3dboruw63ttnbuxattbnvswioq)
> : [- removeRelationship:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3lpozsvezlmmf2gs33oonugs4b2)
>
> **Checking referential
> integrity**
> : [- externalModelsReferenced](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5sxq5dfojxgc3cnn5sgk3dtkjswmzlsmvxggzle)
> : [- referencesProperty:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgkztfojsw4y3fonihe33qmvzhi6j2)
>
> **Accessing primary keys**
> : [- globalIDForRow:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5twy33cmfwesrcgn5zfe33xhi)
> : [- isPrimaryKeyValidInObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5uxgudsnfwwc4tzjnsxsvtbnruwisloj5rguzldoq5a)
> : [- primaryKeyForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5yhe2lnmfzhss3fpfdg64shnrxweylmjfcdu)
> : [- primaryKeyForRow:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5yhe2lnmfzhss3fpfdg64ssn53tu)
>
> **Accessing primary key
> attributes**
> : [- setPrimaryKeyAttributes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cqojuw2ylspffwk6kbor2he2lcov2gk4z2)
> : [- primaryKeyAttributes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5yhe2lnmfzhss3fpfaxi5dsnfrhk5dfom)
> : [- primaryKeyAttributeNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5yhe2lnmfzhss3fpfaxi5dsnfrhk5dfjzqw2zlt)
> : [- primaryKeyRootName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5yhe2lnmfzhss3fpfjg633ujzqw2zj2)
> : [- isValidPrimaryKeyAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5uxgvtbnruwiudsnfwwc4tzjnsxsqluorzgsytvorstu)
>
> **Accessing class properties**
> : [- setClassProperties:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cdnrqxg42qojxxazlsoruwk4z2)
> : [- classProperties](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5rwyyltonihe33qmvzhi2lfom)
> : [- classPropertyNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5rwyyltonihe33qmvzhi6komfwwk4y)
> : [- isValidClassProperty:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5uxgvtbnruwiq3mmfzxgudsn5ygk4tupe5a)
>
> **Accessing the enterprise
> object class**
> : [- classDescriptionForInstances](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5rwyyltoncgk43dojuxa5djn5xem33sjfxhg5dbnzrwk4y)
> : [- setClassName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cdnrqxg42omfwwkoq)
> : [- className](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5rwyyltonhgc3lf)
>
> **Accessing locking attributes**
> : [- setAttributesUsedForLocking:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cbor2he2lcov2gk42vonswirtpojgg6y3lnfxgooq)
> : [- attributesUsedForLocking](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfonkxgzleizxxetdpmnvws3th)
> : [- isValidAttributeUsedForLocking:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5uxgvtbnruwiqluorzgsytvorsvk43fmrdg64smn5rww2lom45a)
>
> **Accessing external name**
> : [- setExternalName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cfpb2gk4tomfwe4ylnmu5a)
> : [- externalName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5sxq5dfojxgc3comfwwk)
>
> **Accessing whether an
> entity is read only**
> : [- setReadOnly:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5csmvqwit3onr4tu)
> : [- isReadOnly](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5uxgutfmfse63tmpe)
>
> **Accessing the user dictionary**
> : [- setUserInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cvonsxeslomzxtu)
> : [- userInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf52xgzlsjfxgm3y)
>
> **Working with stored procedures**
> : [- setStoredProcedure:forOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5ctorxxezlekbzg6y3fmr2xezj2mzxxet3qmvzgc5djn5xdu)
> : [- storedProcedureForOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zxi33smvsfa4tpmnswi5lsmvdg64spobsxeylunfxw4oq)
>
> **Working with fetch specifications**
> : [- addFetchSpecification:withName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qwizcgmv2gg2ctobswg2lgnfrwc5djn5xdu53jorue4ylnmu5a)
> : [- fetchSpecificationNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5tgk5ddnbjxazldnftgsy3boruw63somfwwkzb2)
> : [- fetchSpecificationNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5tgk5ddnbjxazldnftgsy3boruw63somfwwk4y)
> : [- removeFetchSpecificationNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3lpozsumzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zlehi)
> : [- addSharedObjectFetchSpecificationByName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qwizctnbqxezlej5rguzldordgk5ddnbjxazldnftgsy3boruw63scpfhgc3lfhi)
> : [- sharedObjectFetchSpecificationNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwqylsmvse6ytkmvrxirtforrwqu3qmvrwsztjmnqxi2lpnzhgc3lfom)
> : [- setSharedObjectFetchSpecificationsByName:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOEntity.html#//apple_ref/occ/instm/EOEntity/setSharedObjectFetchSpecificationsByName:)
> : [- removeSharedObjectFetchSpecificationByName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3lpozsvg2dbojswit3cnjswg5cgmv2gg2ctobswg2lgnfrwc5djn5xee6komfwwkoq)
>
> **Working with entity inheritance
> hierarchies**
> : [- parentEntity](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5ygc4tfnz2ek3tunf2hs)
> : [- subEntities](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zxkysfnz2gs5djmvzq)
> : [- addSubEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qwizctovrek3tunf2hsoq)
> : [- removeSubEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3lpozsvg5lcivxhi2lupe5a)
> : [- setIsAbstractEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cjonawe43uojqwg5cfnz2gs5dzhi)
> : [- isAbstractEntity](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5uxgqlcon2heyldorcw45djor4q)
>
> **Specifying fault behavior**
> : [- setMaxNumberOfInstancesToBatchFetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cnmf4e45lnmjsxet3gjfxhg5dbnzrwk42un5bgc5ddnbdgk5ddna5a)
> : [- maxNumberOfInstancesToBatchFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5wwc6coovwwezlsj5tes3ttorqw4y3fonkg6qtborrwqrtforrwq)
>
> **Caching objects**
> : [- setCachesObjects:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cdmfrwqzltj5rguzldorztu)
> : [- cachesObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5rwcy3imvzu6ytkmvrxi4y)

## Instance Methods

---

### addAttribute:

`- (void)addAttribute:(EOAttribute
*)anAttribute`

Adds _anAttribute_ to
the receiver. Raises an `NSInvalidArgumentException` if _anAttribute_'s
name is already in use by another attribute or relationship. Sets _anAttribute_'s
entity to __self__.

__See
Also:__  [- removeAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3lpozsuc5duojuwe5lumu5a), [- attributes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfom), [- attributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfjzqw2zlehi)

---

### addFetchSpecification:withName:

`- (void)addFetchSpecification:(EOFetchSpecification
*)fetchSpec
withName:(NSString *)fetchSpecName`

Adds the fetch specification and associates _fetchSpecName_ with
it.

__See Also:__  [- fetchSpecificationNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5tgk5ddnbjxazldnftgsy3boruw63somfwwkzb2), [- fetchSpecificationNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5tgk5ddnbjxazldnftgsy3boruw63somfwwk4y), [- removeFetchSpecificationNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3lpozsumzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zlehi)

---

### addRelationship:

`- (void)addRelationship:(EORelationship
*)aRelationship`

Adds _aRelationship_ to
the receiver. Raises an `NSInvalidArgumentException` if _aRelationship_'s
name is already in use by another attribute or relationship. Sets _aRelationship_'s
entity to __self__.

__See
Also:__  [- removeRelationship:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3lpozsvezlmmf2gs33oonugs4b2), [- relationships](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3dboruw63ttnbuxa4y), [- relationshipNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3dboruw63ttnbuxattbnvswioq)

---

### addSharedObjectFetchSpecificationByName:

`- (void)addSharedObjectFetchSpecificationByName:(NSString
*)name`

Adds the fetch specification identified by _name_ to
the set of fetch specifications used to load objects into a shared
editing context.

---

### addSubEntity:

`- (void)addSubEntity:(EOEntity
*)child`

Causes the child entity _child_ to
"inherit" from the receiver. This is the first step in setting
up an inheritance hierarchy between entities.

__See
Also:__  [- subEntities](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zxkysfnz2gs5djmvzq), [- removeSubEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3lpozsvg5lcivxhi2lupe5a)

---

### anyAttributeNamed:

`- (EOAttribute *)anyAttributeNamed:(NSString
*)attributeName`

Returns the user-created attribute identified
by _attributeName_. If no such attribute
exists, this method looks through the "hidden" attributes created
by the Enterprise Objects Framework for one with the given name.
Hidden attributes are used for such things as primary keys on target
entities of flattened attributes. If none is found, nil is returned.

__See
Also:__  [- attributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfjzqw2zlehi), [- attributes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfom)

---

### anyRelationshipNamed:

`- (EORelationship *)anyRelationshipNamed:(NSString
*)relationshipName`

Returns the user-created relationship identified
by _relationshipName_. If none exists,
this method looks through the "hidden" relationships created
by the Enterprise Objects Framework for one with the given name.
If none is found, nil is returned.

__See Also:__  [- relationshipNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3dboruw63ttnbuxattbnvswioq), [- relationships](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3dboruw63ttnbuxa4y)

---

### attributeNamed:

`- (EOAttribute *)attributeNamed:(NSString
*)attributeName`

Returns the attribute named _attributeName_,
or nil if no such attribute exists.

__See Also:__  [- anyAttributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qw46kbor2he2lcov2gkttbnvswioq), [- attributes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfom), [- relationshipNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3dboruw63ttnbuxattbnvswioq)

---

### attributes

`- (NSArray *)attributes`

Returns all of the receiver's attributes,
or nil if the receiver has none.

__See Also:__  [- anyAttributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qw46kbor2he2lcov2gkttbnvswioq), [- attributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfjzqw2zlehi)

---

### attributesToFetch

`- (NSArray *)attributesToFetch`

Returns an array of the EOAttributes that need
to be fetched so that they can be included in the row snapshot.
The set of attributes includes:

1. Attributes that
   are class properties, "used for locking," or primary keys.
2. Source attributes of any to-many relationship (flattened or
   non-flattened) that is a class property.
3. Source attributes of any non-flattened, to-one relationship
   that is a class property or that is used by a flattened attribute
   that is a class property.
4. The foreign key attributes of any flattened, to-one relationship
   that is a class property or that is used by a class property.

---

### attributesUsedForLocking

`- (NSArray *)attributesUsedForLocking`

Returns an array containing those properties
whose values must match a snapshot any time a row is updated.

Attributes
used for locking are those whose values are compared when a database-level
object performs an update. When the database-level classes fetch
an enterprise object, they cache these attributes' values in a
snapshot. Later, when the enterprise object is updated, the values
of these attributes in the object are checked with those in the
snapshot-if they differ, the update fails. See the EODatabaseContext
class specification for more information.

---

### beautifyName

`- (void)beautifyName`

Makes the receiver's name conform to a standard
convention. EOEntity names that conform to this style are all lower-case
except for the initial letter of each word, which is upper case.
Thus, "MOVIE" becomes "Movie", and "MOVIE_ROLE" becomes
"MovieRole".

__See Also:__  [- setName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5comfwwkoq), [- validateName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf53gc3djmrqxizkomfwwkoq), [- beautifyNames](EOModel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmjswc5lunfthsttbnvsxg) (EOModel)

---

### cachesObjects

`- (BOOL)cachesObjects`

Returns YES if all of the objects from the receiver
are to be cached in memory and queries are to be evaluated in-memory
using this cache rather than in the database. This method should
only be used for fairly small tables of read-only objects, since
the first access to the receiver will trigger fetching the entire
table. You should generally restrict this method to read-only entities
to avoid cached data getting out of sync with database data. Also,
you shouldn't use this method if your application will be making queries
against the entity that can't be evaluated in memory.

__See
Also:__  [- setCachesObjects:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cdmfrwqzltj5rguzldorztu)

---

### classDescriptionForInstances

`- (EOClassDescription *)classDescriptionForInstances`

Returns the EOClassDescription associated with
the receiver. The EOClassDescription class provides a mechanism
for extending classes by giving them access to the metadata contained
in an EOModel (or another external source of information). In an
application, EOClassDescriptions are registered on demand for the
EOEntity on which an enterprise object is based. For more information,
see the class specifications for EOClassDescription (in EOControl)
and [EOEntityClassDescription](EOEntityClassDescription-2.md#apple-ineegrccizeum).

---

### className

`- (NSString *)className`

Returns the name of the enterprise object class
associated with the receiver. When a row is fetched for the receiver
by a database-level object, it's returned as an instance of this
class. This class might not be present in the run-time system, and
in fact your application may have to load it on demand. If your application
doesn't load a class, EOGenericRecord is used.

An enterprise
object class other than EOGenericRecord can be mapped to only one
entity.

---

### classProperties

`- (NSArray *)classProperties`

Returns an array containing the properties that
are bound to the receiver's class (so that instances of the class
will be passed values corresponding to those properties). This is
a subset of the receiver's attributes and relationships.

__See
Also:__  [- classPropertyNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5rwyyltonihe33qmvzhi6komfwwk4y)

---

### classPropertyNames

`- (NSArray *)classPropertyNames`

Returns an array containing the names of those
properties that are bound to the receiver's class (so that instances
of the class will be passed values corresponding to those properties).
This is a subset of the receiver's attributes and relationships.

__See
Also:__  [- classProperties](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5rwyyltonihe33qmvzhi2lfom)

---

### externalModelsReferenced

`- (NSArray *)externalModelsReferenced`

Examines each of the receiver's relationships
and returns a list of all external models referenced by the receiver.

__See
Also:__  [- referencesProperty:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgkztfojsw4y3fonihe33qmvzhi6j2)

---

### externalName

`- (NSString *)externalName`

Returns the name of the receiver as understood
by the database server.

---

### externalQuery

`- (NSString *)externalQuery`

Returns a query statement that's used by an
EOAdaptorChannel to select rows for the receiver when a qualifier
is empty, or nil if the receiver has no external query. An empty
qualifier is one that specifies only the entity, and would thus
fetch all enterprise objects for that entity.

External queries
are useful for hiding records or invoking database-specific features
such as stored procedures when an application attempts to select
all records for an entity. You can also use the EOStoredProcedure
class to work with stored procedures; for more information see the [EOStoredProcedure](EOStoredProcedure-2.md#apple-inbuuqsdjjeei) class specification.

__See
Also:__  [- setExternalQuery:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cfpb2gk4tomfwfc5lfoj4tu)

---

### fetchSpecificationNamed:

`- (EOFetchSpecification *)fetchSpecificationNamed:(NSString
*)fetchSpecName`

Returns the fetch specification associated with _fetchSpecName_.

__See
Also:__  [- addFetchSpecification:withName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qwizcgmv2gg2ctobswg2lgnfrwc5djn5xdu53jorue4ylnmu5a), [- fetchSpecificationNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5tgk5ddnbjxazldnftgsy3boruw63somfwwk4y), [- removeFetchSpecificationNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3lpozsumzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zlehi)

---

### fetchSpecificationNames

`- (NSArray *)fetchSpecificationNames`

Returns an alphabetically sorted array of names
of the entity's fetch specifications.

__See
Also:__  [- addFetchSpecification:withName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qwizcgmv2gg2ctobswg2lgnfrwc5djn5xdu53jorue4ylnmu5a), [- fetchSpecificationNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5tgk5ddnbjxazldnftgsy3boruw63somfwwkzb2), [- removeFetchSpecificationNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3lpozsumzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zlehi)

---

### globalIDForRow:

`- (EOGlobalID *)globalIDForRow:(NSDictionary
*)row`

Constructs a global identifier from the specified
row for the receiver.

__See Also:__  [- primaryKeyForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5yhe2lnmfzhss3fpfdg64shnrxweylmjfcdu)

---

### isAbstractEntity

`- (BOOL)isAbstractEntity`

Returns YES to indicate that the receiver is
abstract, NO otherwise. An abstract entity is one that has no corresponding
enterprise objects in your application. Abstract entities are used
to model inheritance relationships. For example, you might have
a Person abstract entity that acts as the parent of Customer and
Employee entities. Customer and Employee would inherit certain characteristics
from Person (such as name and address attributes). However, though
your application might have Customer and Employee objects, it would
never have a Person object.

__See Also:__  [- setIsAbstractEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cjonawe43uojqwg5cfnz2gs5dzhi)

---

### isPrimaryKeyValidInObject:

`- (BOOL)isPrimaryKeyValidInObject:(id)anObject`

Returns YES if every key attribute is present
in _anObject_ and has a value that
is not nil. Returns NO otherwise. This method uses the EOKeyValueCoding protocol so
a dictionary may be provided instead of an enterprise object.

__See
Also:__  [- primaryKeyForRow:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5yhe2lnmfzhss3fpfdg64ssn53tu)

---

### isQualifierForPrimaryKey:

`- (BOOL)isQualifierForPrimaryKey:(EOQualifier
*)aQualifier`

Returns YES if _aQualifier_ describes
the primary key and nothing but the primary key, NO otherwise.

---

### isReadOnly

`- (BOOL)isReadOnly`

Returns YES if the receiver can't be modified, NO if
it can. If an entity can't be modified, then enterprise objects
fetched for that entity also can't be modified (that is, inserted,
deleted, or updated).

---

### isValidAttributeUsedForLocking:

`- (BOOL)isValidAttributeUsedForLocking:(EOAttribute
*)anAttribute`

Returns NO if _anAttribute_ isn't
an EOAttribute, if the EOAttribute doesn't belong to the receiver,
or if _anAttribute_ is derived. Otherwise
returns YES. An attribute that isn't valid for locking will cause [setAttributesUsedForLocking:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cbor2he2lcov2gk42vonswirtpojgg6y3lnfxgooq) to fail.

__See
Also:__  [- attributesUsedForLocking](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfonkxgzleizxxetdpmnvws3th)

---

### isValidClassProperty:

`- (BOOL)isValidClassProperty:(id)aProperty`

Returns NO if either _aProperty_ isn't
an EOAttribute or EORelationship, or if _aProperty_ doesn't
belong to the receiver. Otherwise returns YES. Note that this method
doesn't tell you whether _aProperty_ is
a member of the array returned by [classProperties](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5rwyyltonihe33qmvzhi2lfom). In other words,
unlike __classProperties__, [classPropertyNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5rwyyltonihe33qmvzhi6komfwwk4y),
and [setClassProperties:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cdnrqxg42qojxxazlsoruwk4z2),
this method doesn't interact with the properties bound to the
entity's enterprise object class.

---

### isValidPrimaryKeyAttribute:

`- (BOOL)isValidPrimaryKeyAttribute:(EOAttribute
*)anAttribute`

Returns NO if _anAttribute_ isn't
an EOAttribute, doesn't belong to the receiver, or is derived.
Otherwise returns YES.

__See Also:__  [- setPrimaryKeyAttributes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cqojuw2ylspffwk6kbor2he2lcov2gk4z2)

---

### maxNumberOfInstancesToBatchFetch

`- (unsigned int)maxNumberOfInstancesToBatchFetch`

Returns the maximum number of to-one faults
from the receiver to fire at one time. See the method description
for [setMaxNumberOfInstancesToBatchFetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cnmf4e45lnmjsxet3gjfxhg5dbnzrwk42un5bgc5ddnbdgk5ddna5a) for
more explanation of what this means.

---

### model

`- (EOModel *)model`

Returns the model that contains the receiver.

__See
Also:__  [- addEntity:](EOModel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmfsgirlooruxi6j2) (EOModel)

---

### name

`- (NSString *)name`

Returns the receiver's name.

---

### parentEntity

`- (EOEntity *)parentEntity`

Returns the entity from which the receiver inherits.

__See
Also:__  [- subEntities](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zxkysfnz2gs5djmvzq)

---

### primaryKeyAttributeNames

`- (NSArray *)primaryKeyAttributeNames`

Returns an array containing the names of the
attributes that make up the receiver's primary key.

__See
Also:__  [- primaryKeyAttributes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5yhe2lnmfzhss3fpfaxi5dsnfrhk5dfom)

---

### primaryKeyAttributes

`- (NSArray *)primaryKeyAttributes`

Returns an array of those attributes that make
up the receiver's primary key.

__See Also:__  [- primaryKeyAttributeNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5yhe2lnmfzhss3fpfaxi5dsnfrhk5dfjzqw2zlt)

---

### primaryKeyForGlobalID:

`- (NSDictionary *)primaryKeyForGlobalID:(EOKeyGlobalID
*)globalID`

Returns the primary key for the object identified
by _globalID_.

__See
Also:__  [- globalIDForRow:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5twy33cmfwesrcgn5zfe33xhi)

---

### primaryKeyForRow:

`- (NSDictionary *)primaryKeyForRow:(NSDictionary
*)aRow`

Returns the primary key for _aRow_,
or nil if the primary key can't be computed. The primary key is
a dictionary whose keys are attribute names and whose values are
values for those attributes.

__See Also:__  [- primaryKeyForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5yhe2lnmfzhss3fpfdg64shnrxweylmjfcdu)

---

### primaryKeyRootName:

`- (NSString *)primaryKeyRootName`

Returns the external name (that is, the name
as it's understood by the database) of the receiver's root entity.
If the receiver has no parent entity, returns the receiver's external
name.

__See Also:__  [- externalName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5sxq5dfojxgc3comfwwk), [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5xgc3lf), [- parentEntity](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5ygc4tfnz2ek3tunf2hs)

---

### qualifierForPrimaryKey:

`- (EOQualifier *)qualifierForPrimaryKey:(NSDictionary
*)aRow`

Returns a qualifier for the receiver that can
be used to fetch an instance of the receiver with the primary key
extracted from _aRow_.

__See
Also:__  [- isQualifierForPrimaryKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5uxgulvmfwgsztjmvzem33skbzgs3lboj4uwzlzhi), [- restrictingQualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk43uojuwg5djnztvc5lbnruwm2lfoi)

---

### referencesProperty:

`- (BOOL)referencesProperty:(id)aProperty`

Returns YES if any of the receiver's attributes
or relationships reference _aProperty_, NO otherwise.
A property can be referenced by a flattened attribute or by a relationship.
For example, suppose a model has an Employee entity with a __toDepartment__ relationship.
If you flatten the department's name attribute into the Employee
entity, creating a __departmentName__ attribute,
that flattened attribute references the __toDepartment__ relationship.

If
an entity has any outstanding references to a property, you shouldn't
remove the property.

__See Also:__  [- removeAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3lpozsuc5duojuwe5lumu5a), [- removeRelationship:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3lpozsvezlmmf2gs33oonugs4b2)

---

### relationshipNamed:

`- (EORelationship *)relationshipNamed:(NSString
*)name`

Returns the relationship named _name_,
or nil if the receiver has no such relationship.

__See
Also:__  [- anyRelationshipNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qw46ksmvwgc5djn5xhg2djobhgc3lfmq5a), [- attributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfjzqw2zlehi), [- relationships](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3dboruw63ttnbuxa4y)

---

### relationships

`- (NSArray *)relationships`

Returns all of the receiver's relationships,
or nil if the receiver has none.

__See Also:__  [- attributes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfom)

---

### removeAttribute:

`- (void)removeAttribute:(EOAttribute
*)name`

Removes the attribute named _name_ if
it exists. You should always use [referencesProperty:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgkztfojsw4y3fonihe33qmvzhi6j2)to
check that an attribute isn't referenced by another property before
removing it.

__See Also:__  [- addAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qwizcbor2he2lcov2gkoq), [- attributes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfom)

---

### removeFetchSpecificationNamed:

`- (void)removeFetchSpecificationNamed:(NSString
*)fetchSpecName`

Removes the fetch specification referred to
by _fetchSpecName_.

__See
Also:__  [- addFetchSpecification:withName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qwizcgmv2gg2ctobswg2lgnfrwc5djn5xdu53jorue4ylnmu5a), [- fetchSpecificationNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5tgk5ddnbjxazldnftgsy3boruw63somfwwkzb2), [- fetchSpecificationNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5tgk5ddnbjxazldnftgsy3boruw63somfwwk4y)

---

### removeRelationship:

`- (void)removeRelationship:(EORelationship
*)name`

Removes the relationship named _name_ if
it exists. You should always use [referencesProperty:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgkztfojsw4y3fonihe33qmvzhi6j2) to
check that a relationship isn't referenced by another property
before removing it.

__See Also:__  [- addRelationship:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qwizcsmvwgc5djn5xhg2djoa5a), [- relationships](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3dboruw63ttnbuxa4y)

---

### removeSharedObjectFetchSpecificationByName:

`- (void)removeSharedObjectFetchSpecificationByName:(NSString
*)name`

Removes the fetch specification identified by _name_ from
the set of fetch specifications used to load objects into a shared
editing context.

---

### removeSubEntity:

`- (void)removeSubEntity:(EOEntity
*)child`

Removes _child_ from
the receiver's list of sub-entities.

__See
Also:__  [- addSubEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qwizctovrek3tunf2hsoq), [- subEntities](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zxkysfnz2gs5djmvzq)

---

### restrictingQualifier

`- (EOQualifier *)restrictingQualifier`

Returns the qualifier used to restrict all queries
made against the receiver. Restricting qualifiers are useful when
there is not a one-to-one mapping between an entity and a particular
database table, or when you always want to filter the data that's
returned for a particular entity.

For example, if you're
using the "one table" inheritance model in which parent and
child data is contained in the same table, you'd use a restricting
qualifier to fetch objects of the appropriate type. To give a non-inheritance
example, for an Employees table you might create a "Sales" entity
that has a restricting qualifier that only fetches employees who
are in the Sales department.

__See Also:__  [- setRestrictingQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5csmvzxi4tjmn2gs3thkf2wc3djmzuwk4r2)

---

### setAttributesUsedForLocking:

`- (BOOL)setAttributesUsedForLocking:(NSArray
*)attributes`

Sets _attributes_ as
the attributes used when an EODatabaseChannel locks enterprise objects
for updates. Returns NO and doesn't set the attributes used for
locking if any of the attributes in _attributes_ responds NO to [isValidAttributeUsedForLocking:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5uxgvtbnruwiqluorzgsytvorsvk43fmrdg64smn5rww2lom45a);
returns YES otherwise. See the [EODatabase](EODatabase-3.md#apple-iraukqsginbui), [EODatabaseContext](EODatabaseContext-2.md#apple-ivhuiylumfrgc43finxw45dfpb2a),
and [EODatabaseChannel](EODatabaseChannel-2.md#apple-incucrcci5eei) class specifications
for information on locking.

---

### setCachesObjects:

`- (void)setCachesObjects:(BOOL)flag`

Sets according to _flag_ whether
all of the receiver's objects are cached the first time the associated
table is queried.

__See Also:__  [- cachesObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5rwcy3imvzu6ytkmvrxi4y)

---

### setClassName:

`- (void)setClassName:(NSString
*)name`

Assigns _name_ as
the name of the class associated with the receiver or "EOGenericRecord"
if _name_ is nil. The specified class
need not be present in the run-time system when this message is
sent. When an EODatabaseChannel fetches objects for the receiver,
they're created as instances of this class. Your application may
have to load the class on demand if it isn't present in the run-time
system; if it doesn't load the class, EOGenericRecord will be
used.

An enterprise object class other than EOGenericRecord
can be mapped to only one entity.

__See
Also:__  [- className](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5rwyyltonhgc3lf)

---

### setClassProperties:

`- (BOOL)setClassProperties:(NSArray
*)properties`

Sets the receiver's class properties to the
EOAttributes and EORelationships in _properties_ and
returns YES, unless the receiver responds NO to [isValidClassProperty:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5uxgvtbnruwiq3mmfzxgudsn5ygk4tupe5a) for any of
the objects in the array. In this event, the receiver's class
properties aren't changed and NO is returned.

---

### setExternalName:

`- (void)setExternalName:(NSString
*)name`

Sets the name of the receiver as understood
by the database server to _name_. For
example, though your application may know the entity as "JobTitle"
the database may require a form such as "JOB_TTL". An adaptor
uses the external name to communicate with the database; your application
should never need to use the external name.

---

### setExternalQuery:

`- (void)setExternalQuery:(NSString
*)aQuery`

Assigns _aQuery_ as
the query statement used for selecting rows from the receiver when
there is no qualifier.

External queries are useful for hiding
records or invoking database-specific features such as stored procedures
when an application attempts to select all records for an entity.
You can also use the EOStoredProcedure class to work with stored
procedures; for more information see the [EOStoredProcedure](EOStoredProcedure-2.md#apple-inbuuqsdjjeei) class specification.

An
external query is sent unaltered to the database server, and so
must contain the external (column) names instead of the names of
EOAttributes. However, to work properly with the adaptor the external query
must use the columns in alphabetical order by their corresponding
EOAttributes' names.

__See Also:__  [- columnName](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3dn5whk3lojzqw2zi) (EOAttribute), [- externalQuery](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5sxq5dfojxgc3crovsxe6i)

---

### setIsAbstractEntity:

`- (void)setIsAbstractEntity:(BOOL)flag`

Sets according to _flag_ whether
the receiver is an abstract entity. For more discussion of abstract
entities, see the method description for [isAbstractEntity](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5uxgqlcon2heyldorcw45djor4q).

---

### setMaxNumberOfInstancesToBatchFetch:

`- (void)setMaxNumberOfInstancesToBatchFetch:(unsigned
int)size`

Sets the maximum number of faults from the receiver
to trigger at one time. By default, only one object is fetched from
the database when you trigger a fault. You can optionally use this
method to set to size the number of faults of the same entity should
be fetched from the database along with the first one. Using this
technique helps to optimize performance by taking advantage of round
trips to the database.

__See Also:__  [- maxNumberOfInstancesToBatchFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5wwc6coovwwezlsj5tes3ttorqw4y3fonkg6qtborrwqrtforrwq)

---

### setName:

`- (void)setName:(NSString
*)name`

Sets the receiver's name to _name_. Raises an `NSInvalidArgumentException` if _name_ is
already in use by another entity in the same EOModel or if _name_ is
not a valid entity name.

__See Also:__  [- beautifyName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5rgkylvoruwm6komfwwk), [- validateName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf53gc3djmrqxizkomfwwkoq)

---

### setPrimaryKeyAttributes:

`- (BOOL)setPrimaryKeyAttributes:(NSArray
*)keys`

If the receiver responds NO to [isValidPrimaryKeyAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5uxgvtbnruwiudsnfwwc4tzjnsxsqluorzgsytvorstu) for any
of the objects in _keys_, this method returns NO.
Otherwise, this method sets the primary key attributes to the attributes
in _keys_ and returns YES.

You
should exercise care in choosing primary key attributes. Floating-point
numbers, for example, can't be reliably compared for equality,
and are thus unsuitable for use in primary keys. Integer and string
types are the safest choice for primary keys. NSDecimalNumber objects
will work, but they'll entail more overhead than integers.

__See
Also:__  [- isValidPrimaryKeyAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5uxgvtbnruwiudsnfwwc4tzjnsxsqluorzgsytvorstu)

---

### setReadOnly:

`- (void)setReadOnly:(BOOL)flag`

Sets according to _flag_ whether
the database rows for the receiver can be modified by the database
level objects.

__See Also:__  [- isReadOnly](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5uxgutfmfse63tmpe)

---

### setRestrictingQualifier:

`- (void)setRestrictingQualifier:(EOQualifier
*)aQualifier`

Assigns _aQualifier_ as
the qualifier used to restrict all queries made against the receiver.
The restricting qualifier can be used to map an entity to a subset
of the rows in a table. For more discussion of this subject, see
the description for [restrictingQualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk43uojuwg5djnztvc5lbnruwm2lfoi).

---

### setSharedObjectFetchSpecificationsByName:

`- (void)setSharedObjectFetchSpecificationsByName:(NSArray
*)names`

Sets the
fetch specifications used to load objects into a shared editing
context to the fetch specifications identified by name in the provided
array, _names_.

---

### setStoredProcedure:forOperation:

`- (void)setStoredProcedure:(EOStoredProcedure
*)storedProcedure
forOperation:(NSString *)operation`

Sets _storedProcedure_ for _operation_. _operation_ can
be one of the following:

- [EOFetchAllProcedureOperation](#apple-irauurcjijdeq)
- [EOFetchWithPrimaryKeyProcedureOperation](#apple-irauusscjbaui)
- [EOInsertProcedureOperation](#apple-irauuq2bizdus)
- [EODeleteProcedureOperation](#apple-irauur2jifbec)
- [EONextPrimaryKeyProcedureOperation](#apple-irauur2civdei)

This
information is used when changes from the object graph have been
transformed into EODatabaseOperations that are being used to construct
EOAdaptorOperations. At this point, Enterprise Objects Framework
checks the entities associated with the changed objects to see if
the entities have any stored procedures defined for the operation
being performed.

__See Also:__  [- storedProcedureForOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zxi33smvsfa4tpmnswi5lsmvdg64spobsxeylunfxw4oq)

---

### setUserInfo:

`- (void)setUserInfo:(NSDictionary
*)dictionary`

Sets the _dictionary_ of
auxiliary data, which your application can use for whatever it needs. _dictionary_ can
only contain property list data types-that is, NSString, NSDictionary,
NSArray, and NSData.

---

### sharedObjectFetchSpecificationNames

`- (NSArray *)sharedObjectFetchSpecificationNames`

Returns an array of strings, which are the names
of the fetch specifications used to load objects into a shared editing
context.

---

### storedProcedureForOperation:

`- (EOStoredProcedure *)storedProcedureForOperation:(NSString
*)operation`

Returns the stored procedure for the specified _operation_,
if one has been set. Otherwise, returns nil. _operation_ can
be one of the following:

- [EOFetchAllProcedureOperation](#apple-irauurcjijdeq)
- [EOFetchWithPrimaryKeyProcedureOperation](#apple-irauusscjbaui)
- [EOInsertProcedureOperation](#apple-irauuq2bizdus)
- [EODeleteProcedureOperation](#apple-irauur2jifbec)
- [EONextPrimaryKeyProcedureOperation](#apple-irauur2civdei)

__See
Also:__  [- setStoredProcedure:forOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5ctorxxezlekbzg6y3fmr2xezj2mzxxet3qmvzgc5djn5xdu), [- parameterDirection](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3qmfzgc3lforsxerdjojswg5djn5xa) (EOAttribute), [- storedProcedure](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3torxxezlekbzg6y3fmr2xezi) (EOAttribute)

---

### subEntities

`- (NSArray *)subEntities`

Returns a list of those entities which inherit
from the receiver.

__See Also:__  [- addSubEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qwizctovrek3tunf2hsoq), [- parentEntity](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5ygc4tfnz2ek3tunf2hs), [- removeSubEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3lpozsvg5lcivxhi2lupe5a)

---

### userInfo

`- (NSDictionary *)userInfo`

Returns a dictionary of user data. Your application
can use this to store any auxiliary information it needs.

__See
Also:__  [- setUserInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5cvonsxeslomzxtu)

---

### validateName:

`- (NSException *)validateName:(NSString
*)name`

Validates _name_ and
returns nil if it is a valid name, or an exception if it isn't.
A name is invalid if it has zero length; starts with a character
other than a letter, a number, or "@", "#", or "_";
or contains a character other than a letter, a number, "@",
"#", "_", or "$". A name is also invalid if the receiver's model
already has an EOEntity that has the same name or a stored procedure
with an argument that has the same name.

[setName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5comfwwkoq) uses this method to validate
its argument.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
