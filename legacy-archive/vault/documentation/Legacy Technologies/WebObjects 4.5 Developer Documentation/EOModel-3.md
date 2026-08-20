---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOModel.html
archived_at: '2026-07-15T08:11:33.709720Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOModel

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EOModel.h

---

## Class Description

---

An EOModel represents a mapping between a database schema
and a set of classes based on the entity-relationship model. The
model contains a number of EOEntity objects representing the entities (tables)
of the database schema. Each [EOEntity](EOEntity-3.md#apple-irauuq2ginduu) object
has a number of [EOAttribute](EOAttribute-3.md#apple-incuqq2ijfeue) and [EORelationship](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#BFCDGGAG) objects representing
the properties (columns or fields) of the entity in the database
schema. For more information on attributes and relationships, see
their respective class specifications.

An EOModel maintains a mapping between each of its EOEntity
objects and a corresponding enterprise object class for use with
the database level of the Enterprise Objects Framework. You can
determine the EOEntity for a particular enterprise object with the [entityForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lupfdg64spmjvgky3uhi) method.

An EOModel is specific to a particular database server, and
stores information needed to connect to that server. This includes
the name of an adaptor framework to load so that the Enterprise
Objects Framework can communicate with the database. Models are
stored in the file system in a manner similar to adaptor framework.
EOModel objects are usually loaded from model files built with the EOModeler
application rather than built programmatically. If you need to programmatically
load a model file, see the section ["Loading a Model File"](EOModel-4.md#apple-ineeoqsfizcuu).

Models can have relationships that reference other models
in the same model group. The other models may map to different databases
and types of servers.

Models are organized into model groups; see the [EOModelGroup](EOModelGroup-3.md#apple-ivhu233emvweo4tpovya) class specification for
more information.

## Creating an EOModel Programmatically

The EOAdaptorChannel class declares methods for reading basic
schema information from a relational database. You can use this
information to build up an EOModel programmatically, and then enhance that
model by defining extra relationships, flattening attributes, and
so on. See the class description in the [EOAdaptorChannel](EOAdaptorChannel-3.md#apple-ijaucqsbjfcei) class specification
for information on reading basic schema information, and see the
other modeling classes' specifications for information on creating
additional attributes and relationships.

## Constants

---

In EOModel.h, EOModelEOAccess defines
an NSString constant for the name of the notification it posts. For
more information, see ["Notifications"](#apple-ineeorchjjbuk).

## Method Types

---

> **Initializing an EOModel
> instance**
> : [- initWithContentsOfFile:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpnfxgs5cxnf2gqq3pnz2gk3tuonhwmrtjnrstu)
> : [- initWithTableOfContentsPropertyList:path:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpnfxgs5cxnf2gqvdbmjwgkt3ginxw45dfnz2hgudsn5ygk4tupfggs43uhjygc5dihi)
>
> **Saving a model**
> : [- encodeTableOfContentsIntoPropertyList:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxgg33emvkgcytmmvhwmq3pnz2gk3tuonew45dpkbzg64dfoj2hstdjon2du)
> : [- writeToFile:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpo5zgs5dfkrxum2lmmu5a)
>
> **Loading a model's objects**
> : [- loadAllModelObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpnrxwczcbnrwe233emvwe6ytkmvrxi4y)
>
> **Working with entities**
> : [- addEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmfsgirlooruxi6j2)
> : [- removeEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpojsw233wmvcw45djor4tu)
> : [- removeEntityAndReferences:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpojsw233wmvcw45djor4uc3tekjswmzlsmvxggzlthi)
> : [- entityNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lupfhgc3lfom)
> : [- entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lupfhgc3lfmq5a)
> : [- entities](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lunfsxg)
> : [- entitiesWithSharedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lunfsxgv3jorufg2dbojswit3cnjswg5dt)
>
> **Naming a model's components**
> : [- beautifyNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmjswc5lunfthsttbnvsxg)
>
> **Accessing the model's
> name**
> : [- setName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bponsxittbnvstu)
> : [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpnzqw2zi)
> : [- path](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpobqxi2a)
>
> **Checking references**
> : [- referencesToProperty:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpojswmzlsmvxggzltkrxva4tpobsxe5dzhi)
> : [- externalModelsReferenced](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmv4hizlsnzqwytlpmrswy42smvtgk4tfnzrwkza)
>
> **Getting an object's
> entity**
> : [- entityForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lupfdg64spmjvgky3uhi)
>
> **Accessing the adaptor
> bundle**
> : [- adaptorName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmfsgc4dun5ze4ylnmu)
> : [- setAdaptorName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bponsxiqlemfyhi33sjzqw2zj2)
>
> **Accessing the connection
> dictionary**
> : [- setConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bponsxiq3pnzxgky3unfxw4rdjmn2gs33omfzhsoq)
> : [- connectionDictionary](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmnxw43tfmn2gs33oiruwg5djn5xgc4tz)
>
> **Accessing the user dictionary**
> : [- setUserInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bponsxivltmvzes3tgn45a)
> : [- userInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpovzwk4sjnztg6)
>
> **Working with stored procedures**
> : [- addStoredProcedure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmfsgiu3un5zgkzcqojxwgzleovzgkoq)
> : [- removeStoredProcedure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpojsw233wmvjxi33smvsfa4tpmnswi5lsmu5a)
> : [- storedProcedureNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpon2g64tfmrihe33dmvshk4tfjzqw2zlt)
> : [- storedProcedureNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpon2g64tfmrihe33dmvshk4tfjzqw2zlehi)
> : [- storedProcedures](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpon2g64tfmrihe33dmvshk4tfom)
>
> **Accessing the model's
> group**
> : [- setModelGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bponsxitlpmrswyr3sn52xaoq)
> : [- modelGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpnvxwizlmi5zg65lq)
>
> **Accessing prototype attributes**
> : [- availablePrototypeAttributeNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmf3gc2lmmfrgyzkqojxxi33upfygkqluorzgsytvorsu4ylnmvzq)
> : [- prototypeAttributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpobzg65dpor4xazkbor2he2lcov2gkttbnvswioq)

## Instance Methods

---

### adaptorName

`- (NSString *)adaptorName`

Returns the name of the adaptor for the receiver.
This name can be used with EOAdaptor's [adaptorWithName:](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbhgc3lfhi) class method to
create an adaptor.

---

### addEntity:

`- (void)addEntity:(EOEntity
*)anEntity`

Adds _anEntity_ to
the receiver. Raises an `NSInvalidArgumentException` if
an error occurs (for example, if _anEntity_ doesn't
exist, if the entity belongs to another model, or if an entity of
the same name is already in the receiver).

__See
Also:__  [- entities](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lunfsxg), [- removeEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpojsw233wmvcw45djor4tu), [- removeEntityAndReferences:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpojsw233wmvcw45djor4uc3tekjswmzlsmvxggzlthi)

---

### addStoredProcedure:

`- (void)addStoredProcedure:(EOStoredProcedure
*)storedProcedure`

Adds _storedProcedure_ to
the receiver. Raises an `NSInvalidArgumentException` if
an error occurs (for example, if a stored procedure of the same
name is already in the receiver).

__See Also:__  [- removeStoredProcedure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpojsw233wmvjxi33smvsfa4tpmnswi5lsmu5a), [- storedProcedures](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpon2g64tfmrihe33dmvshk4tfom), [- storedProcedureNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpon2g64tfmrihe33dmvshk4tfjzqw2zlehi), [- storedProcedureNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpon2g64tfmrihe33dmvshk4tfjzqw2zlt)

---

### availablePrototypeAttributeNames

`- (NSArray *)availablePrototypeAttributeNames`

Returns a list of available prototype names.

__See
Also:__  [- prototypeAttributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpobzg65dpor4xazkbor2he2lcov2gkttbnvswioq)

---

### beautifyNames

`- (void)beautifyNames`

Makes all of the receiver's named components
conform to a standard convention. Names that conform to this style
are all lower-case except for the initial letter of each embedded
word other than the first, which is upper case. Thus, "NAME"
becomes "name", and "FIRST_NAME" becomes "firstName".

__See
Also:__  [+ externalNameForInternalName:separatorString:useAllCaps:](NSString%20Additions.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpjzjvg5dsnfxgoicbmrsgs5djn5xhgl3fpb2gk4tomfwe4ylnmvdg64sjnz2gk4tomfwe4ylnmu5hgzlqmfzgc5dpojjxi4tjnzttu5ltmvawy3cdmfyhgoq) (NSString
Additions), __- beautifyName__ ( [EOEntity](EOEntity-3.md#apple-irauuq2ginduu), [EOAttribute](EOAttribute-3.md#apple-incuqq2ijfeue), [EORelationship](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#BFCDGGAG), [EOStoredProcedure](EOStoredProcedure-2.md#apple-inbuuqsdjjeei)), [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpnzqw2zi)

---

### connectionDictionary

`- (NSDictionary *)connectionDictionary`

Returns a dictionary containing information
used to connect to the database server. The connection dictionary
is the place to specify default login information for applications
using the model. See the EOAdaptor class specification for more
information.

---

### encodeTableOfContentsIntoPropertyList:

`- (void)encodeTableOfContentsIntoPropertyList:(NSMutableDictionary
*)propertyList`

Encodes the receiver into _propertyList_.
This method is used to get an ASCII representation of an EOModel
in property list format.

__See Also:__  [- initWithTableOfContentsPropertyList:path:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpnfxgs5cxnf2gqvdbmjwgkt3ginxw45dfnz2hgudsn5ygk4tupfggs43uhjygc5dihi)

---

### entities

`- (NSArray *)entities`

Returns an array containing the receiver's
entities. Note that this method loads every entity, and thus defeats
the benefits of incremental model loading.

__See
Also:__  [- entityNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lupfhgc3lfom)

---

### entitiesWithSharedObjects

`- (NSArray *)entitiesWithSharedObjects`

Returns an
array of entities that have objects to load into a shared editing
context.

---

### entityForObject:

`- (EOEntity *)entityForObject:(id)anEO`

Returns the entity associated with _anEO_,
whether _anEO_ is an instance of an
enterprise object class, an instance of EOGenericRecord, or a fault (see
the EOFault class specification for information on faults). Returns nil if _anEO_ has
no associated entity.

---

### entityNamed:

`- (EOEntity *)entityNamed:(NSString
*)name`

Returns the entity named _name_,
or nil if no such entity exists. Posts an [EOEntityLoadedNotification](#apple-ineeoq2dijfei) when the
entity is loaded.

__See Also:__  [- entityNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lupfhgc3lfom), [- entities](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lunfsxg)

---

### entityNames

`- (NSArray *)entityNames`

Returns an array containing the names of the
EOModel's entities.

__See Also:__  [- entities](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lunfsxg), [- entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lupfhgc3lfmq5a)

---

### externalModelsReferenced

`- (NSArray *)externalModelsReferenced`

Returns an array containing those models that
are referenced by this model.

__See Also:__  [- referencesToProperty:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpojswmzlsmvxggzltkrxva4tpobsxe5dzhi)

---

### initWithContentsOfFile:

`- initWithContentsOfFile:(NSString
*)path`

Initializes a newly-allocated EOModel by reading
the contents of the file named _path_ as
a model archive. The file specified by path can either be an old-style
(__.eomodel__) or new-style (__.eomodeld__)
model file. Sets the EOModel's name and path. __initWithContentsOfFile:__ raises
an `NSInvalidArgumentException` if
for any reason it cannot initialize the model from the file specified
by _path_.

__See
Also:__  [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpnzqw2zi), [- path](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpobqxi2a)

---

### initWithTableOfContentsPropertyList:path:

`- initWithTableOfContentsPropertyList:(NSDictionary
*)tableOfContents path:(NSString
*)path`

Uses _tableOfContents_ (which
is the property list representation of an EOModel) with the file
name _path_ to initialize the receiver.

__See
Also:__  [- encodeTableOfContentsIntoPropertyList:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxgg33emvkgcytmmvhwmq3pnz2gk3tuonew45dpkbzg64dfoj2hstdjon2du)

---

### loadAllModelObjects

`- (void)loadAllModelObjects`

Loads any of the receiver's entities, stored
procedures, attributes, and relationships that have not yet been
loaded.

__See Also:__  [- attributes](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5qxi5dsnfrhk5dfom) (EOEntity), [- entities](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lunfsxg), [- relationships](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zgk3dboruw63ttnbuxa4y) (EOEntity), [- storedProcedures](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpon2g64tfmrihe33dmvshk4tfom)

---

### modelGroup

`- (EOModelGroup *)modelGroup`

Returns the model group of which the receiver
is a part.

__See Also:__  [- setModelGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bponsxitlpmrswyr3sn52xaoq)

---

### name

`- (NSString *)name`

Returns the receiver's name.

__See
Also:__  [- path](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpobqxi2a), [- initWithTableOfContentsPropertyList:path:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpnfxgs5cxnf2gqvdbmjwgkt3ginxw45dfnz2hgudsn5ygk4tupfggs43uhjygc5dihi)

---

### path

`- (NSString *)path`

Returns the name of the EOModel file used to
create the receiver, or nil if the model wasn't initialized from
a file.

__See Also:__  [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpnzqw2zi) [- initWithContentsOfFile:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpnfxgs5cxnf2gqq3pnz2gk3tuonhwmrtjnrstu)

---

### prototypeAttributeNamed:

`- (EOAttribute *)prototypeAttributeNamed:(NSString
*)attributeName`

Returns the prototype attribute for the given _attributeName_.
It first looks for the prototype in an entity named EOadaptorNamePrototypes
(which can be in any model in the receiver's model group). If
the prototype isn't found there or if the EOadaptorNamePrototypes
entity doesn't exist, it then looks in an entity named EOPrototypes
(in any model in the model group). If the search is still unsuccessful,
this method finally looks for the prototype in the list of prototypes
provided by the adaptor itself.

__See Also:__  [- availablePrototypeAttributeNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmf3gc2lmmfrgyzkqojxxi33upfygkqluorzgsytvorsu4ylnmvzq)

---

### referencesToProperty:

`- (NSArray *)referencesToProperty:(id)aProperty`

Returns an array of all properties in the receiver
that reference _aProperty_, whether
derived attributes, relationships that reference _aProperty_,
and so on. Returns nil if _aProperty_ isn't
referenced by any of the properties in the model.

__See
Also:__  [- externalModelsReferenced](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmv4hizlsnzqwytlpmrswy42smvtgk4tfnzrwkza)

---

### removeEntity:

`- (void)removeEntity:(EOEntity
*)name`

Removes the entity with the given _name_ without
performing any referential integrity checking.

__See
Also:__  [- addEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmfsgirlooruxi6j2), [- removeEntityAndReferences:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpojsw233wmvcw45djor4uc3tekjswmzlsmvxggzlthi)

---

### __removeEntityAndReferences:__

`- (void)removeEntityAndReferences:(EOEntity
*)entity`

Removes _entity_ and
any attributes or relationships in other entities that reference _entity_.

__See
Also:__  [- removeEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpojsw233wmvcw45djor4tu), [- addEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmfsgirlooruxi6j2)

---

### removeStoredProcedure:

`- (void)removeStoredProcedure:(EOStoredProcedure
*)storedProcedure`

Removes _storedProcedure_ without
checking to see if an entity uses it.

__See
Also:__  [- addStoredProcedure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmfsgiu3un5zgkzcqojxwgzleovzgkoq), [- storedProcedures](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpon2g64tfmrihe33dmvshk4tfom)

---

### setAdaptorName:

`- (void)setAdaptorName:(NSString
*)adaptorName`

Sets the name of the receiver's adaptor to _adaptorName_.

__See
Also:__  [+ availableAdaptorNames](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmf3gc2lmmfrgyzkbmrqxa5dpojhgc3lfom) (EOAdaptor)

---

### setConnectionDictionary:

`- (void)setConnectionDictionary:(NSDictionary
*)connectionDictionary`

Sets the dictionary containing information used
to connect to the database to _connectionDictionary_.
See the [EOAdaptor](EOAdaptor-3.md#apple-ivhuczdbob2g64q) class specification for
more information on working with connection dictionaries.

__See
Also:__  [adaptorWithModel:](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbgw6zdfnq5a) (EOAdaptor)

---

### setModelGroup:

`- (void)setModelGroup:(EOModelGroup
*)group`

Sets the model group of which the receiver should
be a part. Note that you shouldn't change an EOModel's model
group after it has been bound to other models in its group.

__See
Also:__  [- modelGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpnvxwizlmi5zg65lq)

---

### setName:

`- (void)setName:(NSString
*)name`

Sets the name of the receiver to _name_.

---

### setUserInfo:

`- (void)setUserInfo:(NSDictionary
*)dictionary`

Sets the _dictionary_ of
auxiliary data, which your application can use for whatever it needs. _dictionary_ can
only contain property list data types-that is, NSString, NSDictionary,
NSArray, and NSData.

---

### storedProcedureNamed:

`- (EOStoredProcedure *)storedProcedureNamed:(NSString
*)name`

Returns the stored procedure named _name_,
or nil if the model doesn't contain a stored procedure with the
given name.

__See Also:__  [- storedProcedureNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpon2g64tfmrihe33dmvshk4tfjzqw2zlt), [- storedProcedures](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpon2g64tfmrihe33dmvshk4tfom)

---

### storedProcedureNames

`- (NSArray *)storedProcedureNames`

Returns an array containing the names of all
of the model's stored procedures.

__See Also:__  [- storedProcedureNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpon2g64tfmrihe33dmvshk4tfjzqw2zlehi), [- storedProcedures](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpon2g64tfmrihe33dmvshk4tfom)

---

### storedProcedures

`- (NSArray *)storedProcedures`

Returns an array containing all of the model's
stored procedures. Note that this method loads each of the model's
stored procedures, thus defeating the benefits of incremental model
loading.

__See Also:__  [- storedProcedureNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpon2g64tfmrihe33dmvshk4tfjzqw2zlt), [- storedProcedureNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpon2g64tfmrihe33dmvshk4tfjzqw2zlehi)

---

### userInfo

`- (NSDictionary *)userInfo`

Returns a dictionary of user data. You can use
this to store any auxiliary information it needs.

__See
Also:__  [- setUserInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bponsxivltmvzes3tgn45a)

---

### writeToFile:

`- (void)writeToFile:(NSString
*)path`

Saves the receiver in the directory specified
by _path_. If the file specified by
path already exists, a backup copy is first created (using path
with a "~" character appended). As a side-effect, this method
resets the current path.

Raises an `NSInvalidArgumentException` on
any error which prevents the file from being written.

__See
Also:__  [- path](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpobqxi2a)

---

## Notifications

---

EOModel declares and posts the following notification.

### EOEntityLoadedNotification

Posted after an EOEntity is loaded into memory.
The notification contains:

|  |  |
| --- | --- |
| Notification Object | The entity that was loaded. |
| Userinfo | None |

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
