---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOUtilities.html
archived_at: '2026-07-15T08:13:41.854359Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOUtilities

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.eoaccess

---

## Class Description

---

[EOUtilities](#apple-ivhukzdjoruw4z2dn5xhizlyoqqeczdenf2gs33oom) is a collection of convenience methods intended to make common operations with EOF easier. [EOUtilities](#apple-ivhukzdjoruw4z2dn5xhizlyoqqeczdenf2gs33oom) is an EOAccess class that consists entirely of static methods-you never instantiate an [EOUtilities](#apple-ivhukzdjoruw4z2dn5xhizlyoqqeczdenf2gs33oom) object.

Each method requires an editing context into which the objects should be fetched; this editing context is passed as the first argument to each method in [EOUtilities](#apple-ivhukzdjoruw4z2dn5xhizlyoqqeczdenf2gs33oom).

|  |
| --- |
| __Note:__ The Objective-C source code for EOUtilities is available as an example. On Mac OS X Server systems, see __/System/Developer/Examples/EnterpriseObjects/Sources/EOUtilities__. On NT, see $_NEXT_ROOT___\Developer\Examples\EnterpriseObjects\Sources\EOUtilities__. |

## Method Types

---

> **Creating new objects**
> : [createAndInsertInstance](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6y3smvqxizkbnzses3ttmvzhisloon2gc3tdmu)
>
> **Fetching multiple objects**
> : [objectsForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtizxxerlooruxi6komfwwkza): [objectsWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtk5uxi2crovqwy2lgnfsxertpojwwc5a): [objectsMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtjvqxiy3infxgos3fpfaw4zcwmfwhkzi): [objectsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtjvqxiy3infxgovtbnr2wk4y): [objectsOfClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtj5teg3dbonzq): [objectsWithFetchSpecificationAndBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtk5uxi2cgmv2gg2ctobswg2lgnfrwc5djn5xec3teijuw4zdjnztxg)
>
> **Fetching single objects**
> : [objectWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cxnf2gqulvmfwgsztjmvzem33snvqxi): [objectMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cnmf2gg2djnztuwzlzifxgivtbnr2wk): [objectMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cnmf2gg2djnztvmylmovsxg): [objectWithFetchSpecificationAndBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cxnf2gqrtforrwqu3qmvrwsztjmnqxi2lpnzaw4zccnfxgi2lom5zq): [objectWithPrimaryKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cxnf2gqudsnfwwc4tzjnsxs): [objectWithPrimaryKeyValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cxnf2gqudsnfwwc4tzjnsxsvtbnr2wk)
>
> **Fetching raw rows**
> : [executeStoredProcedureNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6zlymvrxk5dfkn2g64tfmrihe33dmvshk4tfjzqw2zle): [objectFromRawRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cgojxw2utbo5jg65y): [rawRowsWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64tbo5jg653tk5uxi2crovqwy2lgnfsxertpojwwc5a): [rawRowsMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64tbo5jg653tjvqxiy3infxgos3fpfaw4zcwmfwhkzi): [rawRowsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64tbo5jg653tjvqxiy3infxgovtbnr2wk4y): [rawRowsForSQL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64tbo5jg653tizxxeu2rjq): [rawRowsForStoredProcedureNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64tbo5jg653tizxxeu3un5zgkzcqojxwgzleovzgkttbnvswi)
>
> **Accessing the EOF stack**
> : [connectWithModelNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6y3pnzxgky3uk5uxi2cnn5sgk3comfwwkza): [databaseContextForModelNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6zdborqweyltmvbw63tumv4hirtpojgw6zdfnrhgc3lfmq)
>
> **Accessing object data**
> : [destinationKeyForSourceObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6zdfon2gs3tboruw63slmv4um33sknxxk4tdmvhwe2tfmn2a): [localInstanceOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs63dpmnqwysloon2gc3tdmvhwmt3cnjswg5a): [localInstancesOfObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs63dpmnqwysloon2gc3tdmvzu6zspmjvgky3uom): [primaryKeyForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64dsnfwwc4tzjnsxsrtpojhwe2tfmn2a)
>
> **Accessing model information**
> : [entityForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6zlooruxi6kgn5zeg3dbonzq): [entityForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6zlooruxi6kgn5ze6ytkmvrxi): [entityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6zlooruxi6komfwwkza): [modelGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs63lpmrswyr3sn52xa)

## Static Methods

---

### connectWithModelNamed

`public static void connectWithModelNamed( com.webobjects.eocontrol.EOEditingContext editingContext, String modelName, NSDictionary overrides)`

Connects to the database using the connection information in the specified model and the provided overrides dictionary. This method facilitates per-session database logins in WebObjects applications. Typically, you'd put a login name and password in the overrides dictionary and otherwise use the values in the model's connection dictionary. Throws an exception if the connection failed.

---

### __createAndInsertInstance__

`public static com.webobjects.eocontrol.EOEnterpriseObject createAndInsertInstance( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName)`

Creates a new enterprise object for the specified entity, inserts it into _editingContext_, and returns the new object.

---

### databaseContextForModelNamed

`public static EODatabaseContext databaseContextForModelNamed( com.webobjects.eocontrol.EOEditingContext editingContext, String modelName)`

Returns the database context used to service the specified model.

---

### destinationKeyForSourceObject

`public static NSDictionary destinationKeyForSourceObject( com.webobjects.eocontrol.EOEditingContext editingContext, com.webobjects.eocontrol.EOEnterpriseObject object, String relationshipName)`

Returns the foreign key for the rows at the destination entity of the specified relationship. As an example, given entities Department and Employee with a relationship called "department" joining `Department.ID` and `Employee.deptID`, invoking this method on a Department object with ID equal to 5 returns a dictionary with a value of 5 for the `deptID` key.

__See Also:__ [primaryKeyForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64dsnfwwc4tzjnsxsrtpojhwe2tfmn2a)

---

### entityForClass

`public static EOEntity entityForClass( com.webobjects.eocontrol.EOEditingContext editingContext, Class classObject)`

Returns the entity associated with the specified class. Throws an exception if the specified entity can't be found or if more than one entity is associated with the class.

__See Also:__ [entityForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6zlooruxi6kgn5ze6ytkmvrxi), [entityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6zlooruxi6komfwwkza), [objectsOfClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtj5teg3dbonzq)

---

### entityForObject

`public static EOEntity entityForObject( com.webobjects.eocontrol.EOEditingContext editingContext, com.webobjects.eocontrol.EOEnterpriseObject object)`

Returns the entity associated with the provided enterprise object. Throws an exception if the specified entity can't be found.

__See Also:__ [entityForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6zlooruxi6kgn5zeg3dbonzq), [entityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6zlooruxi6komfwwkza)

---

### entityNamed

`public static EOEntity entityNamed( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName)`

Returns the entity with the specified name. Throws an exception if the specified entity can't be found.

__See Also:__ [entityForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6zlooruxi6kgn5zeg3dbonzq), [entityForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6zlooruxi6kgn5ze6ytkmvrxi)

---

### executeStoredProcedureNamed

`public static NSDictionary executeStoredProcedureNamed( com.webobjects.eocontrol.EOEditingContext editingContext, String storedProcedureName, NSDictionary arguments)`

Executes the specified stored procedure with the provided arguments. Returns the stored procedure's return values (if any). Use only with stored procedures that don't return results rows.

__See Also:__ [rawRowsForStoredProcedureNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64tbo5jg653tizxxeu3un5zgkzcqojxwgzleovzgkttbnvswi)

---

### localInstanceOfObject

`public static com.webobjects.eocontrol.EOEnterpriseObject localInstanceOfObject( com.webobjects.eocontrol.EOEditingContext editingContext, com.webobjects.eocontrol.EOEnterpriseObject object)`

Translates the specified enterprise object from another editing context to the specified one.

__See Also:__ [localInstancesOfObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs63dpmnqwysloon2gc3tdmvzu6zspmjvgky3uom)

---

### localInstancesOfObjects

`public static NSArray localInstancesOfObjects( com.webobjects.eocontrol.EOEditingContext editingContext, NSArray objects)`

Translates the specified enterprise objects from another editing context to the specified one.

__See Also:__ [localInstanceOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs63dpmnqwysloon2gc3tdmvhwmt3cnjswg5a)

---

### modelGroup

`public static EOModelGroup modelGroup(com.webobjects.eocontrol.EOEditingContext editingContext)`

Returns the model group associated with the editing context's root object store, an EOObjectStoreCoordinator.

---

### objectFromRawRow

`public static com.webobjects.eocontrol.EOEnterpriseObject objectFromRawRow( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName, NSDictionary row)`

Fetches and returns the object corresponding to the specified raw row (using EOEditingContext's __faultForRawRow__). This method can only be used on raw rows that include the row's primary key.

---

### objectMatchingKeyAndValue

`public static com.webobjects.eocontrol.EOEnterpriseObject objectMatchingKeyAndValue( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName, String key, Object value)`

Creates an EOKeyValueQualifier with the specified key and value and returns matching enterprise objects. Throws an exception unless exactly one object is retrieved.

__See Also:__ [objectMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cnmf2gg2djnztvmylmovsxg), [objectsMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtjvqxiy3infxgos3fpfaw4zcwmfwhkzi)

---

### objectMatchingValues

`public static com.webobjects.eocontrol.EOEnterpriseObject objectMatchingValues( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName, NSDictionary values)`

Creates EOKeyValueQualifiers for each key-value pair in the specified dictionary, ANDs these qualifiers together into an EOAndQualifier, and returns matching enterprise objects. Throws an exception unless exactly one object is retrieved.

__See Also:__ [objectMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cnmf2gg2djnztuwzlzifxgivtbnr2wk), [objectsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtjvqxiy3infxgovtbnr2wk4y)

---

### objectsForEntityNamed

`public static NSArray objectsForEntityNamed( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName)`

Fetches and returns the enterprise objects associated with the specified entity.

__See Also:__ [objectsWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtk5uxi2crovqwy2lgnfsxertpojwwc5a), [objectsMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtjvqxiy3infxgos3fpfaw4zcwmfwhkzi), [objectsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtjvqxiy3infxgovtbnr2wk4y)

---

### objectsMatchingKeyAndValue

`public static NSArray objectsMatchingKeyAndValue( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName, String key, Object value)`

Creates an EOKeyValueQualifier with the specified key and value and returns matching enterprise objects.

__See Also:__ [objectMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cnmf2gg2djnztuwzlzifxgivtbnr2wk), [objectsForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtizxxerlooruxi6komfwwkza), [objectsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtjvqxiy3infxgovtbnr2wk4y)

---

### objectsMatchingValues

`public static NSArray objectsMatchingValues( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName, NSDictionary values)`

Creates EOKeyValueQualifiers for each key-value pair in the specified dictionary, ANDs these qualifiers together into an EOAndQualifier, and returns matching enterprise objects.

__See Also:__ [objectMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cnmf2gg2djnztvmylmovsxg), [objectsForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtizxxerlooruxi6komfwwkza), [objectsMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtjvqxiy3infxgos3fpfaw4zcwmfwhkzi)

---

### objectsOfClass

`public static NSArray objectsOfClass( com.webobjects.eocontrol.EOEditingContext editingContext, Class classObject)`

Fetches and returns the enterprise objects associated with the specified class. Throws an exception if more than one entity for the class exists.

__See Also:__ [entityForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs6zlooruxi6kgn5zeg3dbonzq)

---

### objectsWithFetchSpecificationAndBindings

`public static NSArray objectsWithFetchSpecificationAndBindings( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName, String fetchSpecName, NSDictionary bindings)`

Fetches and returns the enterprise objects retrieved with the specified fetch specification and bindings.

__See Also:__ [objectWithFetchSpecificationAndBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cxnf2gqrtforrwqu3qmvrwsztjmnqxi2lpnzaw4zccnfxgi2lom5zq)

---

### objectsWithQualifierFormat

`public static NSArray objectsWithQualifierFormat( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName, String format, NSArray arguments)`

Creates a qualifier with the provided format string and arguments, and returns matching enterprise objects.

__See Also:__ [objectWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cxnf2gqulvmfwgsztjmvzem33snvqxi), [objectsForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtizxxerlooruxi6komfwwkza)

---

### objectWithFetchSpecificationAndBindings

`public static com.webobjects.eocontrol.EOEnterpriseObject objectWithFetchSpecificationAndBindings( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName, String fetchSpecName, NSDictionary bindings)`

Fetches and returns the enterprise objects retrieved with the specified fetch specification and bindings. Throws an exception unless exactly one object is retrieved.

__See Also:__ [objectsWithFetchSpecificationAndBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtk5uxi2cgmv2gg2ctobswg2lgnfrwc5djn5xec3teijuw4zdjnztxg)

---

### objectWithPrimaryKey

`public static com.webobjects.eocontrol.EOEnterpriseObject objectWithPrimaryKey( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName, NSDictionary keyDictionary)`

Fetches and returns the enterprise object identified by the specified primary key dictionary. Throws an exception unless exactly one object is retrieved.

__See Also:__ [objectMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cnmf2gg2djnztuwzlzifxgivtbnr2wk), [objectWithPrimaryKeyValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cxnf2gqudsnfwwc4tzjnsxsvtbnr2wk), [primaryKeyForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64dsnfwwc4tzjnsxsrtpojhwe2tfmn2a)

---

### objectWithPrimaryKeyValue

`public static com.webobjects.eocontrol.EOEnterpriseObject objectWithPrimaryKeyValue( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName, Object value)`

Fetches and returns the enterprise object identified by the specified primary key value. For use only with enterprise objects that have non-compound primary keys. Throws an exception unless exactly one object is retrieved.

__See Also:__ [objectsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtjvqxiy3infxgovtbnr2wk4y), [objectWithPrimaryKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cxnf2gqudsnfwwc4tzjnsxs)

---

### objectWithQualifierFormat

`public static com.webobjects.eocontrol.EOEnterpriseObject objectWithQualifierFormat( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName, String format, NSArray arguments)`

Creates a qualifier with the provided format string and arguments, and returns matching enterprise objects. Throws an exception unless exactly one object is retrieved.

__See Also:__ [objectsWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtk5uxi2crovqwy2lgnfsxertpojwwc5a), [rawRowsWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64tbo5jg653tk5uxi2crovqwy2lgnfsxertpojwwc5a)

---

### primaryKeyForObject

`public static NSDictionary primaryKeyForObject( com.webobjects.eocontrol.EOEditingContext editingContext, com.webobjects.eocontrol.EOEnterpriseObject object)`

Returns the primary key dictionary for the specified enterprise object.

__See Also:__ [objectWithPrimaryKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cxnf2gqudsnfwwc4tzjnsxs), [objectWithPrimaryKeyValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cxnf2gqudsnfwwc4tzjnsxsvtbnr2wk)

---

### rawRowsForSQL

`public static NSArray rawRowsForSQL( com.webobjects.eocontrol.EOEditingContext editingContext, String modelName, String sqlString)`

Evaluates the specified SQL and returns the resulting raw rows.

__See Also:__ [rawRowsWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64tbo5jg653tk5uxi2crovqwy2lgnfsxertpojwwc5a), [rawRowsForStoredProcedureNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64tbo5jg653tizxxeu3un5zgkzcqojxwgzleovzgkttbnvswi)

---

### rawRowsForStoredProcedureNamed

`public static NSArray rawRowsForStoredProcedureNamed( com.webobjects.eocontrol.EOEditingContext editingContext, String storedProcedureName, NSDictionary arguments)`

Executes the specified stored procedure with the provided arguments and returns the resulting raw rows.

__See Also:__ [rawRowsForSQL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64tbo5jg653tizxxeu2rjq)

---

### rawRowsMatchingKeyAndValue

`public static NSArray rawRowsMatchingKeyAndValue( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName, String key, Object value)`

Creates an EOKeyValueQualifier with the specified key and value and returns matching raw rows.

__See Also:__ [objectMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cnmf2gg2djnztuwzlzifxgivtbnr2wk), [objectsMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtjvqxiy3infxgos3fpfaw4zcwmfwhkzi), [rawRowsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64tbo5jg653tjvqxiy3infxgovtbnr2wk4y)

---

### rawRowsMatchingValues

`public static NSArray rawRowsMatchingValues( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName, NSDictionary values)`

Creates EOKeyValueQualifiers for each key-value pair in the specified dictionary, ANDs these qualifiers together into an EOAndQualifier, and returns matching raw rows.

__See Also:__ [objectMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5cnmf2gg2djnztvmylmovsxg), [objectsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtjvqxiy3infxgovtbnr2wk4y), [rawRowsMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64tbo5jg653tjvqxiy3infxgos3fpfaw4zcwmfwhkzi)

---

### rawRowsWithQualifierFormat

`public static NSArray rawRowsWithQualifierFormat( com.webobjects.eocontrol.EOEditingContext editingContext, String entityName, String format, NSArray arguments)`

Creates a qualifier for the specified entity and with the specified qualifier format and returns matching raw row dictionaries.

__See Also:__ [objectsWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs633cnjswg5dtk5uxi2crovqwy2lgnfsxertpojwwc5a), [rawRowsForSQL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vlunfwgs5djmvzs64tbo5jg653tizxxeu2rjq)

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
