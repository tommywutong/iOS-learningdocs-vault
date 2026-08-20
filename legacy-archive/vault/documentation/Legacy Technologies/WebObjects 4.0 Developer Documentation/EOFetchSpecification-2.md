---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOFetchSpecification.html
archived_at: '2026-07-18T01:28:36.095786Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOFaultHandler-2.md)
[!](EOGenericRecord-2.md)

---

# EOFetchSpecification

__Inherits From:__
NSObject

__Conforms To:__ NSCoding
NSCopying
NSObject (NSObject)

__Declared in:__ EOControl/EOFetchSpecification.h

An EOFetchSpecification collects the criteria needed to select and order a group of records or enterprise objects, whether from an external repository such as a relational database or an internal store such as an EOEditingContext. An EOFetchSpecification contains these elements:

- The name of an entity for which to fetch records or objects. This is the only mandatory element.
- An EOQualifier, indicating which properties to select by and how to do so.
- An array of EOSortOrderings, which indicate how the selected records or objects should be ordered when fetched.
- An indicator of whether to produce distinct results or not. Normally if a record or object is selected several times, such as when forming a join, it appears several times in the fetched results. An EOFetchSpecification that makes distinct selections causes duplicates to be filtered out, so each record or object selected appears exactly once in the result set.
- An indicator of whether to fetch deeply or not. This is used with inheritance hierarchies when fetching for an entity with sub-entities. A deep fetch produces all instances of the entity and its sub-entities, while a shallow fetch produces instances only of the entity in the fetch specification.
- A fetch limit indicating how many objects to fetch before giving the user or program an opportunity to intervene.
- A listing of relationships for which the destination of the relationship should be prefetched along with the entity being fetched. Proper use of this feature allows for substantially increased performance in some cases.
- A dictionary of hints, which an EODatabaseContext or other object can use to optimize or alter the results of the fetch.

EOFetchSpecifications are most often used with the method __objectsWithFetchSpecification:editingContext:__ , defined by EOObjectStore, EOEditingContext, and EODatabaseContext, as well as __objectsWithFetchSpecification:__ , defined by EOEditingContext alone. EOAdaptorChannel and EODatabaseChannel also define methods that use EOFetchSpecifications.

---

## Adopted Protocols

**NSCoding**

**- encodeWithCoder:

**- initWithCoder:****

**NSCopying**

**- copyWithZone:**

**Creating instances**

**+ fetchSpecificationWithEntityName:qualifier:sortOrderings:

**- fetchSpecificationWithQualifierBindings:

**- init

**- initWithEntityName:qualifier:sortOrderings:usesDistinct:
isDeep:hints:********

**Setting the qualifier**

**- setQualifier:

**- qualifier****

**Sorting**

**- setSortOrderings:

**- sortOrderings:****

**Removing duplicates**

**- setUsesDistinct:

**- usesDistinct:****

**Fetching objects in an inheritance hierarchy**

**- setIsDeep:

**- isDeep

**- setEntityName:

**- entityName********

**Controlling fetching behavior**

**- setFetchLimit:

**- fetchLimit

**- setFetchesRawRows:

**- fetchesRawRows

**- setPrefetchingRelationshipKeyPaths:

**- prefetchingRelationshipKeyPaths

**- setPromptsAfterFetchLimit:

**- promptsAfterFetchLimit

**- setRawRowKeyPaths:

**- rawRowKeyPaths

**- setRequiresAllQualifierBindingVariables:

**- requiresAllQualifierBindingVariables

**- setHints:

**- hints****************************

**Locking objects**

**- setLocksObjects:

**- locksObjects****

**Refreshing refetched objects**

**- setRefreshesRefetchedObjects:

**- refreshesRefetchedObjects****

---

#### fetchSpecificationWithEntityName:qualifier:sortOrderings:

+ (EOFetchSpecification \*)__fetchSpecificationWithEntityName:__ (NSString \*)_entityName___qualifier:__ (EOQualifier \*)_qualifier___sortOrderings:__ (NSArray \*)_sortOrderings_

Returns an EOFetchSpecification for _entityName_, using _qualifier_ to select and _sortOrderings_ to sort the results. The EOFetchSpecification created with this method is deep, doesn't perform distinct selection, and has no hints.

__See also:__ - __initWithEntityName:qualifier:sortOrderings:usesDistinct:isDeep:hints:__

---

#### entityName

- (NSString \*)__entityName__

Returns the name of the entity to be fetched.

__See also:__ - __isDeep__ , - __setEntityName:__

---

#### fetchLimit

- (unsigned)__fetchLimit__

Returns the fetch limit value which indicates the maximum number of objects to fetch. Depending on the value of promptsAfterFetchLimit, the EODatabaseContext will either stop fetching objects when this limit is reached or it will ask the editing context's message handler to prompt the user as to whether or not it should continue fetching. Use 0 (zero) to indicate no fetch limit. The default is 0.

__See also:__ - __setFetchLimit:__

---

#### fetchesRawRows

- (BOOL)__fetchesRawRows__

Returns YES if __rawRowKeyPaths__ returns non-nil.

__See also:__ - __rawRowKeyPaths__ , - __setFetchesRawRows:__

---

#### fetchSpecificationWithQualifierBindings:

- (EOFetchSpecification \*)__fetchSpecificationWithQualifierBindings:__ (NSDictionary \*)_bindings_

Applies bindings from _bindings_ to its qualifier if there is one, and returns a new fetch specification that can be used in a fetch. The default behavior is to prune any nodes for which there are no bindings. Invoke __setRequiresAllQualifierBindingVariables:__ with an argument of YES to force an exception to be raised if a binding is missing during variable substitution.

__See also:__ - __setRequiresAllQualifierBindingVariables:__

---

#### hints

- (NSDictionary \*)__hints__

Returns the receiver's hints, which other objects can use to alter or optimize fetch operations.

__See also:__ - __setHints:__

---

#### init

- (id)__init__

Initializes a new EOFetchSpecification with no state, except that it fetches deeply and doesn't use distinct. Use the __set...__ methods to add other parts of the specification. This is the designated initializer for the EOFetchSpecification class. Returns __self__ .

__See also:__ - __initWithEntityName:qualifier:sortOrderings:usesDistinct:isDeep:hints:__

---

#### initWithEntityName:qualifier:sortOrderings:usesDistinct:isDeep:hints:

- (id)__initWithEntityName:__ (NSString \*)_entityName___qualifier:__ (EOQualifier \*)_qualifier___sortOrderings:__ (NSArray \*)_sortOrderings___usesDistinct:__ (BOOL)_distinctFlag___isDeep:__ (BOOL)_deepFlag___hints:__ (NSDictionary \*)_hints_

Initializes a new EOFetchSpecification with the given arguments. Returns __self__ .

__See also:__ + __fetchSpecificationWithEntityName:qualifier:sortOrderings:__

---

#### isDeep

- (BOOL)__isDeep__

Returns YES if a fetch should include sub-entities of the receiver's entity, NO if it shouldn't. EOFetchSpecifications are deep by default.

For example, if you have a Person entity with two sub-entities, Employee and Customer, fetching Persons deeply also fetches all Employees and Customers matching the qualifier. Fetching Persons shallowly fetches only Persons matching the qualifier.

__See also:__ - __setIsDeep:__

---

#### locksObjects

- (BOOL)__locksObjects__

Returns YES if a fetch should result in the selected objects being locked in the data repository, NO if it shouldn't. The default is NO.

__See also:__ - __setLocksObjects:__

---

#### prefetchingRelationshipKeyPaths

- (NSArray \*)__prefetchingRelationshipKeyPaths__

Returns an array of relationship key paths that should be prefetched along with the main fetch. For example, if fetching from the Movie entity, you might specify paths of the form (@"directors", @"roles.talent", @"plotSummary").

__See also:__ - __setPrefetchingRelationshipKeyPaths:__

---

#### promptsAfterFetchLimit

- (BOOL)__promptsAfterFetchLimit__

Returns whether to prompt user after the fetch limit has been reached. Default is NO.

__See also:__ - __setPromptsAfterFetchLimit:__

---

#### qualifier

- (EOQualifier \*)__qualifier__

Returns the EOQualifier that indicates which records or objects the receiver is to fetch.

__See also:__ - __setQualifier:__

---

#### rawRowKeyPaths

- (NSArray \*)__rawRowKeyPaths__

Returns an array of attribute key paths that should be fetched as raw data and returned as an array of dictionaries (instead of the normal result of full objects). The raw fetch can increase speed, but forgoes most of the benefits of full Enterprise Objects. The default value is nil, indicating that full objects will be returned from the fetch. An empty array may be used to indicate that the fetch should query the entity named by the fetch specification using the method __attributesToFetch__ . As long as the primary key attributes are included in the raw attributes, the raw row may be used to generate a fault for the corresponding object using EOEditingContext's __[faultForRawRow:entityNamed:](EOEditingContext-3.md)__ method.

__See also:__ - __fetchesRawRows__ , - __setFetchesRawRows:__ , - __setRawRowKeyPaths:__

---

#### refreshesRefetchedObjects

- (BOOL)__refreshesRefetchedObjects__

Returns YES if existing objects are overwritten with fetched values when they've been updated or changed. Returns NO if existing objects aren't touched when their data is refetched (the fetched data is simply discarded). The default is NO. Note that this setting does not affect relationships

__See also:__ - __setRefreshesRefetchedObjects:__

---

#### requiresAllQualifierBindingVariables

- (BOOL)__requiresAllQualifierBindingVariables__

Returns YES to indicate that a missing binding will cause an exception to be raised during variable substitution. The default value is NO, which says to prune any nodes for which there are no bindings.

__See also:__ - __setRequiresAllQualifierBindingVariables:__

---

#### setEntityName:

- (void)__setEntityName:__ (NSString \*)_entityName_

Sets the name of the root entity to be fetched to _entityName_.

__See also:__ - __isDeep__ , - __entityName__

---

#### setFetchesRawRows:

- (void)__setFetchesRawRows:__ (BOOL)_fetchRawRows_

Sets the behavior for fetching raw rows. If set to YES, the behavior is the same as if __setRawRowKeyPaths:__ were called with an empty array. If set to NO, the behavior is as if __setRawRowKeyPaths:__ were called with a nil argument.

__See also:__ - __fetchesRawRows__ , - __setRawRowKeyPaths:__ , - __rawRowKeyPaths__

---

#### setFetchLimit:

- (void)__setFetchLimit:__ (unsigned)_fetchLimit_

Sets the fetch limit value which indicates the maximum number of objects to fetch. Depending on the value of promptsAfterFetchLimit, the EODatabaseContext will either stop fetching objects when this limit is reached or it will ask the editing context's message handler to prompt the user as to whether or not it should continue fetching. Use 0 (zero) to indicate no fetch limit. The default is 0.

__See also:__ - __fetchLimit__

---

#### setHints:

- (void)__setHints:__ (NSDictionary \*)_hints_

Sets the receiver's hints to _hints_. Any object that uses an EOFetchSpecification can define its own hints that it uses to alter or optimize fetch operations. For example, EODatabaseContext uses a hint identified by the key EOCustomQueryExpressionHintKey. EODatabaseContext is the only class in Enterprise Objects Framework that defines fetch specification hints. For information about EODatabaseContext's hints, see the EODatabaseContext class specification.

__See also:__ - __hints__

---

#### setIsDeep:

- (void)__setIsDeep:__ (BOOL)_flag_

Controls whether a fetch should include sub-entities of the receiver's entity. If _flag_ is YES, sub-entities are also fetched; if _flag_ is NO, they aren't. EOFetchSpecifications are deep by default.

For example, if you have a Person entity /class /table with two sub-entities and subclasses, Employee and Customer, fetching Persons deeply also fetches all Employees and Customers matching the qualifier, while fetching Persons shallowly fetches only Persons matching the qualifier.

__See also:__ - __isDeep__

---

#### setLocksObjects:

- (void)__setLocksObjects:__ (BOOL)_flag_

Controls whether a fetch should result in the selected objects being locked in the data repository. If _flag_ is YES it should, if NO it shouldn't. The default is NO.

__See also:__ - __locksObjects__

---

#### setPrefetchingRelationshipKeyPaths:

- (void)__setPrefetchingRelationshipKeyPaths:__ (NSArray \*)_prefetchingRelationshipKeyPaths_

Sets an array of relationship key paths that should be prefetched along with the main fetch. For example, if fetching from the Movie entity, you might specify paths of the form (@"directors", @"roles.talent", @"plotSummary").

__See also:__ - __prefetchingRelationshipKeyPaths__

---

#### setPromptsAfterFetchLimit:

- (void)__setPromptsAfterFetchLimit:__ (BOOL)_promptsAfterFetchLimit_

Sets whether to prompt user after the fetch limit has been reached. Default is NO.

__See also:__ - __promptsAfterFetchLimit__

---

#### setQualifier:

- (void)__setQualifier:__ (EOQualifier \*)_qualifier_

Sets the receiver's qualifier to _qualifier_.

__See also:__ - __qualifier__

---

#### setRawRowKeyPaths:

- (void)setRawRowKeyPaths:(NSArray \*)_rawRowKeyPaths_

Sets an array of attribute key paths that should be fetched as raw data and returned as an array of dictionaries (instead of the normal result of full objects). The raw fetch can increase speed, but forgoes most of the benefits of full Enterprise Objects. The default value is nil, indicating that full objects will be returned from the fetch. An empty array may be used to indicate that the fetch should query the entity named by the fetch specification using the method __attributesToFetch__ . As long as the primary key attributes are included in the raw attributes, the raw row may be used to generate a fault for the corresponding object using EOEditingContext's __[faultForRawRow:entityNamed:](EOEditingContext-3.md)__ method.

__See also:__ - __fetchesRawRows__ , - __rawRowKeyPaths__ , - __setFetchesRawRows:__

---

#### setRefreshesRefetchedObjects:

- (void)__setRefreshesRefetchedObjects:__ (BOOL)_flag_

Controls whether existing objects are overwritten with fetched values when they have been updated or changed. If _flag_ is YES, they are; if _flag_ is NO, they aren't (the fetched data is simply discarded). The default is NO.

For example, suppose that you fetch an employee object and then refetch it, without changing the employee between fetches. In this case, you want to refresh the employee when you refetch it, because another application might have updated the object since your first fetch. To keep your employee in sync with the employee data in the external repository, you'd need to replace the employee's outdated values with the new ones. On the other hand, if you were to fetch the employee, change it, and then refetch it, you would not want to refresh the employee. If you to refreshed it-whether or not another application had changed the employee-you would lose the changes that you had made to the object.

You can get finer-grain control on an EODatabaseContext's refreshing behavior than you can with an EOFetchSpecification by using the delegate method __databaseContext:shouldUpdateCurrentSnapshot:newSnapshot:globalID:databaseChannel:__ . For more information see the EODatabaseContext class specification.

__See also:__ - __refreshesRefetchedObjects__

---

#### setRequiresAllQualifierBindingVariables:

- (void)__setRequiresAllQualifierBindingVariables:__ (BOOL)_allVariablesRequired_

Sets the behavior when a missing binding is encountered during variable substitution. If _allVariablesRequired_ is YES, then a missing binding will cause an exception to be raised during variable substitution. The default value is NO, which says to prune any nodes for which there are no bindings.

__See also:__ - __fetchSpecificationWithQualifierBindings:__ , - __requiresAllQualifierBindingVariables__

---

#### setSortOrderings:

- (void)__setSortOrderings:__ (NSArray \*)_sortOrderings_

Sets the receiver's array of EOSortOrderings to _sortOrderings_. When a fetch is performed with the receiver, the results are sorted by applying each EOSortOrdering in the array.

__See also:__ - __sortedArrayUsingKeyOrderArray:__ (NSArray Additions), - __sortOrderings:__

---

#### setUsesDistinct:

- (void)__setUsesDistinct:__ (BOOL)_flag_

Controls whether duplicate objects or records are removed after fetching. If _flag_ is YES they're removed; if _flag_ is NO they aren't. EOFetchSpecifications by default don't use distinct.

__See also:__ - __usesDistinct:__

---

#### sortOrderings:

- (NSArray \*) __sortOrderings__

Returns the receiver's array of EOSortOrderings. When a fetch is performed with the receiver, the results are sorted by applying each EOSortOrdering in the array.

__See also:__ - __sortedArrayUsingKeyOrderArray:__ (NSArray Additions), - __setSortOrderings:__

---

#### usesDistinct:

- (BOOL)__usesDistinct__

Returns YES if duplicate objects or records are removed after fetching, NO if they aren't. EOFetchSpecifications by default don't use distinct.

__See also:__ - __setUsesDistinct:__

---

[!](EOFaultHandler-2.md)
[!](EOGenericRecord-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
