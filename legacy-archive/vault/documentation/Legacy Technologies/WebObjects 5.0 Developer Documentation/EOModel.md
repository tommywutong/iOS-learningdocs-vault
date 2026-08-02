---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOModel.html
archived_at: '2026-07-15T08:13:41.611368Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOModel

> __Inherits from:__ Object

> __Package:__ com.webobjects.eoaccess

---

## Class Description

---

An EOModel represents a mapping between a database schema and a set of classes based on the entity-relationship model. The model contains a number of EOEntity objects representing the entities (tables) of the database schema. Each EOEntity object has a number of EOAttribute and EORelationship objects representing the properties (columns or fields) of the entity in the database schema. For more information on attributes and relationships, see their respective class specifications.

An EOModel maintains a mapping between each of its EOEntity objects and a corresponding enterprise object class for use with the database level of the Enterprise Objects Framework. You can determine the EOEntity for a particular enterprise object with the [entityForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djor4um33sj5rguzldoq) method.

An EOModel is specific to a particular database server, and stores information needed to connect to that server. This includes the name of an adaptor framework to load so that the Enterprise Objects Framework can communicate with the database. Models are stored in the file system in a manner similar to adaptor framework. EOModel objects are usually loaded from model files built with the EOModeler application rather than built programmatically. If you need to programmatically load a model file, see the section ["Loading a Model File" (page 249)](EOModel.Concepts.md#apple-ineeoqsfizcuu).

Models can have relationships that reference other models in the same model group. The other models may map to different databases and types of servers.

Models are organized into model groups; see the EOModelGroup class specification for more information.

## Creating an EOModel Programmatically

The EOAdaptorChannel class declares methods for reading basic schema information from a relational database. You can use this information to build up an EOModel programmatically, and then enhance that model by defining extra relationships, flattening attributes, and so on. See the class description in the EOAdaptorChannel class specification for information on reading basic schema information, and see the other modeling classes' specifications for information on creating additional attributes and relationships.

## Constants

---

EOModel defines a String constant for the name of the notification it posts. For more information, see ["Notifications" (page 247)](#apple-ineeorchjjbuk).

## Method Types

---

> Constructors
>
> [EOModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5cu6tlpmrswy)
>
> Saving a model
>
> [encodeTableOfContentsIntoPropertyList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw4y3pmrsviylcnrsu6zsdn5xhizloorzus3tun5ihe33qmvzhi6kmnfzxi)
>
> [writeToFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf53xe2lumvkg6rtjnrsq)
>
> Loading a model's objects
>
> [loadAllModelObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5wg6yleifwgytlpmrswyt3cnjswg5dt)
>
> Working with entities
>
> [addEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5qwizcfnz2gs5dz)
>
> [removeEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zgk3lpozsuk3tunf2hs)
>
> [removeEntityAndReferences](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zgk3lpozsuk3tunf2hsqlomrjgkztfojsw4y3fom)
>
> [entityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djor4u4ylnmvzq)
>
> [entityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djor4u4ylnmvsa)
>
> [entities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djoruwk4y)
>
> [entitiesWithSharedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djoruwk42xnf2gqu3imfzgkzcpmjvgky3uom)
>
> Naming a model's components
>
> [beautifyNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5rgkylvoruwm6komfwwk4y)
>
> Accessing the model's name
>
> [setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zwk5comfwwk)
>
> [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5xgc3lf)
>
> [path](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5ygc5di)
>
> Checking references
>
> [referencesToProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zgkztfojsw4y3fonkg6udsn5ygk4tupe)
>
> [externalModelsReferenced](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sxq5dfojxgc3cnn5sgk3dtkjswmzlsmvxggzle)
>
> Getting an object's entity
>
> [entityForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djor4um33sj5rguzldoq)
>
> Accessing the adaptor bundle
>
> [adaptorName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5qwiylqorxxettbnvsq)
>
> [setAdaptorName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zwk5cbmrqxa5dpojhgc3lf)
>
> Accessing the connection dictionary
>
> [setConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zwk5cdn5xg4zldoruw63senfrxi2lpnzqxe6i)
>
> [connectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5rw63tomvrxi2lpnzcgsy3unfxw4ylspe)
>
> Accessing the user dictionary
>
> [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zwk5cvonsxeslomzxq)
>
> [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf52xgzlsjfxgm3y)
>
> Working with stored procedures
>
> [addStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5qwizctorxxezlekbzg6y3fmr2xezi)
>
> [removeStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zgk3lpozsvg5dpojswiudsn5rwkzdvojsq)
>
> [storedProcedureNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zxi33smvsfa4tpmnswi5lsmvhgc3lfom)
>
> [storedProcedureNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zxi33smvsfa4tpmnswi5lsmvhgc3lfmq)
>
> [storedProcedures](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zxi33smvsfa4tpmnswi5lsmvzq)
>
> Accessing the model's group
>
> [setModelGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zwk5cnn5sgk3chojxxk4a)
>
> [modelGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5ww6zdfnrdxe33voa)
>
> Accessing prototype attributes
>
> [availablePrototypeAttributeNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5qxmyljnrqwe3dfkbzg65dpor4xazkbor2he2lcov2gkttbnvsxg)
>
> [prototypeAttributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5yhe33un52hs4dfif2hi4tjmj2xizkomfwwkza)

## Constructors

---

### EOModel

`public EOModel()`

Description forthcoming.

`public EOModel(String path)`

Creates a new EOModel object by reading the contents of the file identified by _path_ as a model archive. Sets the EOModel's name and path from the context of the model archive. Throws an exception if for any reason it cannot initialize the model from the file specified by _path_.

`protected EOModel( NSDictionary tableOfContents, String path)`

Creates a new EOModel object from _tableOfContents,_ which is the property list representation of a EOModel). Sets the EOModel's name and path using _path_.

__See Also:__ [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5xgc3lf), [path](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5ygc5di), [encodeTableOfContentsIntoPropertyList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw4y3pmrsviylcnrsu6zsdn5xhizloorzus3tun5ihe33qmvzhi6kmnfzxi)

---

## Instance Methods

---

### adaptorName

`public String adaptorName()`

Returns the name of the adaptor for the receiver. This name can be used with EOAdaptor's adaptorWithName static method to create an adaptor.

---

### addEntity

`public void addEntity(EOEntity anEntity)`

Adds _anEntity_ to the receiver. Throws an exception if an error occurs (for example, if _anEntity_ doesn't exist, if the entity belongs to another model, or if an entity of the same name is already in the receiver).

__See Also:__ [entities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djoruwk4y), [removeEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zgk3lpozsuk3tunf2hs), [removeEntityAndReferences](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zgk3lpozsuk3tunf2hsqlomrjgkztfojsw4y3fom)

---

### addStoredProcedure

`public void addStoredProcedure(EOStoredProcedure storedProcedure)`

Adds _storedProcedure_ to the receiver. Throws an exception if an error occurs (for example, if a stored procedure of the same name is already in the receiver).

__See Also:__ [removeStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zgk3lpozsvg5dpojswiudsn5rwkzdvojsq), [storedProcedures](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zxi33smvsfa4tpmnswi5lsmvzq), [storedProcedureNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zxi33smvsfa4tpmnswi5lsmvhgc3lfmq)

---

### availablePrototypeAttributeNames

`public NSArray availablePrototypeAttributeNames()`

Returns a list of available prototype names.

__See Also:__ [prototypeAttributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5yhe33un52hs4dfif2hi4tjmj2xizkomfwwkza)

---

### beautifyNames

`public void beautifyNames()`

Makes all of the receiver's named components conform to a standard convention. Names that conform to this style are all lower-case except for the initial letter of each embedded word other than the first, which is upper case. Thus, "NAME" becomes "name", and "FIRST_NAME" becomes "firstName".

__See Also:__ nameForExternalName (EOEntity), __beautifyName__ (EOEntity, EOAttribute, EORelationship, EOStoredProcedure), [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5xgc3lf)

---

### connectionDictionary

`public NSDictionary connectionDictionary()`

Returns a dictionary containing information used to connect to the database server. The connection dictionary is the place to specify default login information for applications using the model. See the EOAdaptor class specification for more information.

---

### dispose

`public void dispose()`

Conformance to NSDisposable.

---

### encodeTableOfContentsIntoPropertyList

`public void encodeTableOfContentsIntoPropertyList(NSMutableDictionary propertyList)`

Encodes the receiver into _propertyList_. This method is used to get an ASCII representation of an EOModel in property list format.

__See Also:__ [EOModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5cu6tlpmrswy) constructors

---

### entities

`public NSArray entities()`

Returns an array containing the receiver's entities. Note that this method loads every entity, and thus defeats the benefits of incremental model loading.

__See Also:__ [entityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djor4u4ylnmvzq)

---

### entitiesWithSharedObjects

`public NSArray entitiesWithSharedObjects()`

Returns an array of entities that have objects to load into a shared editing context.

---

### entityForObject

`public EOEntity entityForObject( com.webobjects.eocontrol.EOEnterpriseObject anEO)`

Returns the entity associated with _anEO_, whether _anEO_ is an instance of an enterprise object class, an instance of EOGenericRecord, or a fault . Returns `null` if _anEO_ has no associated entity.

---

### entityNamed

`public EOEntity entityNamed(String name)`

Returns the entity named _name_, or `null` if no such entity exists. Posts an [EntityLoadedNotification](#apple-ineeoq2dijfei) when the entity is loaded.

__See Also:__ [entityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djor4u4ylnmvzq), [entities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djoruwk4y)

---

### entityNames

`public NSArray entityNames()`

Returns an array containing the names of the EOModel's entities.

__See Also:__ [entities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djoruwk4y), [entityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djor4u4ylnmvsa)

---

### externalModelsReferenced

`public NSArray externalModelsReferenced()`

Returns an array containing those models that are referenced by this model.

__See Also:__ [referencesToProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zgkztfojsw4y3fonkg6udsn5ygk4tupe)

---

### loadAllModelObjects

`public void loadAllModelObjects()`

Loads any of the receiver's entities, stored procedures, attributes, and relationships that have not yet been loaded.

__See Also:__ attributes (EOEntity), [entities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djoruwk4y), relationships (EOEntity), [storedProcedures](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zxi33smvsfa4tpmnswi5lsmvzq)

---

### modelGroup

`public EOModelGroup modelGroup()`

Returns the model group of which the receiver is a part.

__See Also:__ [setModelGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zwk5cnn5sgk3chojxxk4a)

---

### name

`public String name()`

Returns the receiver's name.

__See Also:__ [path](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5ygc5di), [EOModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5cu6tlpmrswy) constructors

---

### path

`public String path()`

Returns the name of the EOModel file used to create the receiver, or `null` if the model wasn't initialized from a file.

__See Also:__ [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5xgc3lf), [EOModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5cu6tlpmrswy) constructors

---

### prototypeAttributeNamed

`public EOAttribute prototypeAttributeNamed(String attributeName)`

Returns the prototype attribute for the given _attributeName_. It first looks for the prototype in an entity named EOadaptorNamePrototypes (which can be in any model in the receiver's model group). If the prototype isn't found there or if the EOadaptorNamePrototypes entity doesn't exist, it then looks in an entity named EOPrototypes (in any model in the model group). If the search is still unsuccessful, this method finally looks for the prototype in the list of prototypes provided by the adaptor itself.

__See Also:__ [availablePrototypeAttributeNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5qxmyljnrqwe3dfkbzg65dpor4xazkbor2he2lcov2gkttbnvsxg)

---

### referencesToProperty

`public NSArray referencesToProperty(Object aProperty)`

Returns an array of all properties in the receiver that reference _aProperty_, whether derived attributes, relationships that reference _aProperty_, and so on. Returns `null` if _aProperty_ isn't referenced by any of the properties in the model.

__See Also:__ [externalModelsReferenced](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sxq5dfojxgc3cnn5sgk3dtkjswmzlsmvxggzle)

---

### removeEntity

`public void removeEntity(EOEntity name)`

Removes the entity with the given _name_ without performing any referential integrity checking.

__See Also:__ [addEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5qwizcfnz2gs5dz), [removeEntityAndReferences](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zgk3lpozsuk3tunf2hsqlomrjgkztfojsw4y3fom)

---

### __removeEntityAndReferences__

`public void removeEntityAndReferences(EOEntity entity)`

Removes _entity_ and any attributes or relationships in other entities that reference _entity_.

__See Also:__ [removeEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zgk3lpozsuk3tunf2hs), [addEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5qwizcfnz2gs5dz)

---

### removeStoredProcedure

`public void removeStoredProcedure(EOStoredProcedure storedProcedure)`

Removes _storedProcedure_ without checking to see if an entity uses it.

__See Also:__ [addStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5qwizctorxxezlekbzg6y3fmr2xezi), [storedProcedures](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zxi33smvsfa4tpmnswi5lsmvzq)

---

### setAdaptorName

`public void setAdaptorName(String adaptorName)`

Sets the name of the receiver's adaptor to _adaptorName_.

---

### setConnectionDictionary

`public void setConnectionDictionary(NSDictionary connectionDictionary)`

Sets the dictionary containing information used to connect to the database to _connectionDictionary_. See the EOAdaptor class specification for more information on working with connection dictionaries.

__See Also:__ adaptorWithModel (EOAdaptor)

---

### setModelGroup

`public void setModelGroup(EOModelGroup group)`

Sets the model group of which the receiver should be a part. Note that you shouldn't change an EOModel's model group after it has been bound to other models in its group.

__See Also:__ [modelGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5ww6zdfnrdxe33voa)

---

### setName

`public void setName(String name)`

Sets the name of the receiver to _name_.

---

### setUserInfo

`public void setUserInfo(NSDictionary dictionary)`

Sets the _dictionary_ of auxiliary data, which your application can use for whatever it needs. _dictionary_ can only contain property list data types-that is, String, NSDictionary, NSArray, and NSData.

---

### storedProcedureNamed

`public EOStoredProcedure storedProcedureNamed(String name)`

Returns the stored procedure named _name_, or `null` if the model doesn't contain a stored procedure with the given name.

__See Also:__ [storedProcedureNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zxi33smvsfa4tpmnswi5lsmvhgc3lfom), [storedProcedures](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zxi33smvsfa4tpmnswi5lsmvzq)

---

### storedProcedureNames

`public NSArray storedProcedureNames()`

Returns an array containing the names of all of the model's stored procedures.

__See Also:__ [storedProcedureNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zxi33smvsfa4tpmnswi5lsmvhgc3lfmq), [storedProcedures](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zxi33smvsfa4tpmnswi5lsmvzq)

---

### storedProcedures

`public NSArray storedProcedures()`

Returns an array containing all of the model's stored procedures. Note that this method loads each of the model's stored procedures, thus defeating the benefits of incremental model loading.

__See Also:__ [storedProcedureNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zxi33smvsfa4tpmnswi5lsmvhgc3lfom), [storedProcedureNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zxi33smvsfa4tpmnswi5lsmvhgc3lfmq)

---

### __toString__

`public String toString()`

Returns a String representation of the receiver.

---

### userInfo

`public NSDictionary userInfo()`

Returns a dictionary of user data. You can use this to store any auxiliary information it needs.

__See Also:__ [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5zwk5cvonsxeslomzxq)

---

### writeToFile

`public void writeToFile(String path)`

Saves the receiver in the directory specified by _path_. If the file specified by path already exists, a backup copy is first created (using path with a "~" character appended). As a side-effect, this method resets the current path.

Throws an exception on any error which prevents the file from being written.

__See Also:__ [path](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5ygc5di)

---

## Notifications

---

EOModel declares and posts the following notification.

### EntityLoadedNotification

Posted after an EOEntity is loaded into memory. The notification contains:

|  |  |
| --- | --- |
| Notification Object | The entity that was loaded. |
| Userinfo | None |

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
