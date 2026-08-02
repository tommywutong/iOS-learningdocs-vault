---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOFetchSpecification.html
archived_at: '2026-07-18T01:28:26.072599Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOFaultHandler.md)
[!](EOGenericRecord.md)

---

# EOFetchSpecification

__Inherits From:__
Object (Java Client)
NSObject (Yellow Box)

__Implements:__
NSCoding (Java Client only)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

An EOFetchSpecification collects the criteria needed to select and order a group of records or enterprise objects, whether from an external repository such as a relational database or an internal store such as an EOEditingContext. An EOFetchSpecification contains these elements:

- The name of an entity for which to fetch records or objects. This is the only mandatory element.
- An EOQualifier, indicating which properties to select by and how to do so.
- An array of EOSortOrderings, which indicate how the selected records or objects should be ordered when fetched.
- An indicator of whether to produce distinct results or not. Normally if a record or object is selected several times, such as when forming a join, it appears several times in the fetched results. An EOFetchSpecification that makes distinct selections causes duplicates to be filtered out, so each record or object selected appears exactly once in the result set.
- An indicator of whether to fetch deeply or not. This is used with inheritance hierarchies when fetching for an entity with sub-entities. A deep fetch produces all instances of the entity and its sub-entities, while a shallow fetch produces instances only of the entity in the fetch specification.
- A fetch limit indicating how many objects to fetch before giving the user or program an opportunity to intervene.
- A listing of relationships for which the destination of the relationship should be prefetched along with the entity being fetched. Proper use of this feature allows for substantially increased performance in some cases.
- A dictionary of hints, which an EODatabaseContext or other object can use to optimize or alter the results of the fetch.

EOFetchSpecifications are most often used with the method __objectsWithFetchSpecification:editingContext:__ , defined by EOObjectStore, EOEditingContext, and EODatabaseContext. EOAdaptorChannel and EODatabaseChannel also define methods that use EOFetchSpecifications.

---

## Adopted Protocols

**NSCoding (Java Client only)**

**classForCoder

**encodeWithCoder

**initWithCoder******

## Method Types

**Constructors**

**EOFetchSpecification**

**Creating instances**

**- fetchSpecificationWithQualifierBindings (Yellow Box only)**

**Setting the qualifier**

**- setQualifier

**- qualifier****

**Sorting**

**- setSortOrderings

**- sortOrderings****

**Removing duplicates**

**- setUsesDistinct

**- usesDistinct****

**Fetching objects in an inheritance hierarchy**

**- setIsDeep

**- isDeep

**- setEntityName

**- entityName********

**Controlling fetching behavior**

**- setFetchLimit

**- fetchLimit

**- setFetchesRawRows

**- fetchesRawRows

**- setPrefetchingRelationshipKeyPaths

**- prefetchingRelationshipKeyPaths

**- setPromptsAfterFetchLimit

**- promptsAfterFetchLimit

**- setRawRowKeyPaths

**- rawRowKeyPaths

**- setRequiresAllQualifierBindingVariables

**- requiresAllQualifierBindingVariables

**- setHints

**- hints****************************

**Locking objects**

**- setLocksObjects

**- locksObjects****

**Refreshing refetched objects**

**- setRefreshesRefetchedObjects

**- refreshesRefetchedObjects****

## Constructors

---

#### EOFetchSpecification

public __EOFetchSpecification__ ()

public __EOFetchSpecification__ (java.lang.String _entityName_, EOQualifier _qualifier_, NSArray _sortOrderings_)

public __EOFetchSpecification__ (java.lang.String _entityName_, EOQualifier _qualifier_, NSArray _sortOrderings_, boolean _distinctFlag_, boolean _deepFlag_, NSDictionary _hints_)

Creates a new EOFetchSpecification with the arguments specified. If no arguments are provided, the new EOFetchSpecification has no state, except that it fetches deeply and doesn't use distinct. Use the __set...__ methods to add other parts of the specification. Minimally, you must set the entity name.

If only _entityName_, _qualifier_, and _sortOrderings_ are provided, the new EOFetchSpecification is deep, doesn't perform distinct selection, and has no hints.

## Instance Methods

---

#### entityName

public java.lang.String __entityName__ ()

Returns the name of the entity to be fetched.

__See also:__ - __isDeep__ , - __setEntityName__

---

#### fetchLimit

public int __fetchLimit__ ()

Returns the fetch limit value which indicates the maximum number of objects to fetch. Depending on the value of promptsAfterFetchLimit, the EODatabaseContext will either stop fetching objects when this limit is reached or it will ask the editing context's message handler to prompt the user as to whether or not it should continue fetching. Use 0 (zero) to indicate no fetch limit. The default is 0.

__See also:__ - __setFetchLimit__

---

#### fetchesRawRows

public boolean __fetchesRawRows__ ()

Returns true if __rawRowKeyPaths__ returns non-nil.

__See also:__ - __rawRowKeyPaths__ , - __setFetchesRawRows__

---

#### fetchSpecificationWithQualifierBindings

public EOFetchSpecification __fetchSpecificationWithQualifierBindings__ (NSDictionary _bindings_)

This method is only available in Yellow Box; there is no equivalent in Java Client. Applies bindings from _bindings_ to its qualifier if there is one, and returns a new fetch specification that can be used in a fetch. The default behavior is to prune any nodes for which there are no bindings. Invoke __setRequiresAllQualifierBindingVariables__ with an argument of __true__ to force an exception to be raised if a binding is missing during variable substitution.

__See also:__ - __setRequiresAllQualifierBindingVariables__

---

#### hints

public NSDictionary __hints__ ()

Returns the receiver's hints, which other objects can use to alter or optimize fetch operations.

__See also:__ - __setHints__

---

#### isDeep

public boolean __isDeep__

Returns __true__ if a fetch should include sub-entities of the receiver's entity, __false__ if it shouldn't. EOFetchSpecifications are deep by default.

For example, if you have a Person entity with two sub-entities, Employee and Customer, fetching Persons deeply also fetches all Employees and Customers matching the qualifier. Fetching Persons shallowly fetches only Persons matching the qualifier.

__See also:__ - __setIsDeep__

---

#### locksObjects

public boolean __locksObjects__

()Returns __true__ if a fetch should result in the selected objects being locked in the data repository, __false__ if it shouldn't. The default is __false__ .

__See also:__ - __setLocksObjects__

---

#### prefetchingRelationshipKeyPaths

public NSArray __prefetchingRelationshipKeyPaths__ ()

Returns an array of relationship key paths that should be prefetched along with the main fetch. For example, if fetching from the Movie entity, you might specify paths of the form (@"directors", @"roles.talent", @"plotSummary").

__See also:__ - __setPrefetchingRelationshipKeyPaths__

---

#### promptsAfterFetchLimit

public boolean __promptsAfterFetchLimit__ ()

Returns whether to prompt user after the fetch limit has been reached. Default is __false__ .

__See also:__ - __setPromptsAfterFetchLimit__

---

#### qualifier

EOQualifier __qualifier__ ()

Returns the EOQualifier that indicates which records or objects the receiver is to fetch.

__See also:__ - __setQualifier__

---

#### rawRowKeyPaths

public NSArray __rawRowKeyPaths__ ()

Returns an array of attribute key paths that should be fetched as raw data and returned as an array of dictionaries (instead of the normal result of full objects). The raw fetch can increase speed, but forgoes most of the benefits of full Enterprise Objects. The default value is nil, indicating that full objects will be returned from the fetch. An empty array may be used to indicate that the fetch should query the entity named by the fetch specification using the method __attributesToFetch__ . As long as the primary key attributes are included in the raw attributes, the raw row may be used to generate a fault for the corresponding object using EOEditingContext's __[faultForRawRow](EOEditingContext.md)__ method. (Note that this faulting behavior does not occur in Java Client.)

__See also:__ - __fetchesRawRows__ , - __setFetchesRawRows__ , - __setRawRowKeyPaths__

---

#### refreshesRefetchedObjects

public boolean __refreshesRefetchedObjects__ ()

()Returns __true__ if existing objects are overwritten with fetched values when they've been updated or changed. Returns __false__ if existing objects aren't touched when their data is refetched (the fetched data is simply discarded). The default is __false__ . Note that this setting does not affect relationships

__See also:__ - __setRefreshesRefetchedObjects__

---

#### requiresAllQualifierBindingVariables

public boolean __requiresAllQualifierBindingVariables__ ()

Returns __true__ to indicate that a missing binding will cause an exception to be raised during variable substitution. The default value is __false__ , which says to prune any nodes for which there are no bindings.

__See also:__ - __setRequiresAllQualifierBindingVariables__

---

#### setEntityName

public void __setEntityName__ (java.lang.String _entityName_)

Sets the name of the root entity to be fetched to _entityName_.

__See also:__ - __isDeep__ , - __entityName__

---

#### setFetchesRawRows

public void __setFetchesRawRows__ (boolean _fetchRawRows_)

Sets the behavior for fetching raw rows. If set to __true__ , the behavior is the same as if __setRawRowKeyPaths__ were called with an empty array. If set to __false__ , the behavior is as if __setRawRowKeyPaths__ were called with a nil argument.

__See also:__ - __fetchesRawRows__ , - __setRawRowKeyPaths__ , - __rawRowKeyPaths__

---

#### setFetchLimit

public void __setFetchLimit__ (int _fetchLimit_)

Sets the fetch limit value which indicates the maximum number of objects to fetch. Depending on the value of promptsAfterFetchLimit, the EODatabaseContext will either stop fetching objects when this limit is reached or it will ask the editing context's message handler to prompt the user as to whether or not it should continue fetching. Use 0 (zero) to indicate no fetch limit. The default is 0.

__See also:__ - __fetchLimit__

---

#### setHints

public void __setHints__ (NSDictionary _hints_)

Sets the receiver's hints to _hints_. Any object that uses an EOFetchSpecification can define its own hints that it uses to alter or optimize fetch operations. For example, EODatabaseContext uses a hint identified by the key CustomQueryExpressionHintKey. EODatabaseContext is the only class in Enterprise Objects Framework that defines fetch specification hints. For information about EODatabaseContext's hints, see the EODatabaseContext class specification.

__See also:__ - __hints__

---

#### setIsDeep

public void __setIsDeep__ (boolean _flag_)Controls whether a fetch should include sub-entities of the receiver's entity. If _flag_ is __true__ , sub-entities are also fetched; if _flag_ is __false__ , they aren't. EOFetchSpecifications are deep by default.

For example, if you have a Person entity /class /table with two sub-entities and subclasses, Employee and Customer, fetching Persons deeply also fetches all Employees and Customers matching the qualifier, while fetching Persons shallowly fetches only Persons matching the qualifier.

__See also:__ - __isDeep__

---

#### setLocksObjects

public void __setLocksObjects__ (boolean _flag_)

Controls whether a fetch should result in the selected objects being locked in the data repository. If _flag_ is __true__ it should, if __false__ it shouldn't. The default is __false__ .

__See also:__ - __locksObjects__

---

#### setPrefetchingRelationshipKeyPaths

public void __setPrefetchingRelationshipKeyPaths__ (NSArray _prefetchingRelationshipKeyPaths_)

Sets an array of relationship key paths that should be prefetched along with the main fetch. For example, if fetching from the Movie entity, you might specify paths of the form (@"directors", @"roles.talent", @"plotSummary").

__See also:__ - __prefetchingRelationshipKeyPaths__

---

#### setPromptsAfterFetchLimit

public void __setPromptsAfterFetchLimit__ (boolean _promptsAfterFetchLimit_)

Sets whether to prompt user after the fetch limit has been reached. Default is __false__ .

__See also:__ - __promptsAfterFetchLimit__

---

#### setQualifier

public void __setQualifier__ (EOQualifier _qualifier_)

Sets the receiver's qualifier to _qualifier_.

__See also:__ - __qualifier__

---

#### setRawRowKeyPaths

public void __setRawRowKeyPaths__ (NSArray _rawRowKeyPaths_)

Sets an array of attribute key paths that should be fetched as raw data and returned as an array of dictionaries (instead of the normal result of full objects). The raw fetch can increase speed, but forgoes most of the benefits of full Enterprise Objects. The default value is nil, indicating that full objects will be returned from the fetch. An empty array may be used to indicate that the fetch should query the entity named by the fetch specification using the method __attributesToFetch__ . As long as the primary key attributes are included in the raw attributes, the raw row may be used to generate a fault for the corresponding object using EOEditingContext's __[faultForRawRow](EOEditingContext.md)__ method. (Note that this faulting behavior does not occur in Java Client.)

__See also:__ - __fetchesRawRows__ , - __rawRowKeyPaths__ , - __setFetchesRawRows__

---

#### setRefreshesRefetchedObjects

public void __setRefreshesRefetchedObjects__ (boolean _flag_)

Controls whether existing objects are overwritten with fetched values when they have been updated or changed. If _flag_ is __true__ , they are; if _flag_ is __false__ , they aren't (the fetched data is simply discarded). The default is __false__ .

For example, suppose that you fetch an employee object and then refetch it, without changing the employee between fetches. In this case, you want to refresh the employee when you refetch it, because another application might have updated the object since your first fetch. To keep your employee in sync with the employee data in the external repository, you'd need to replace the employee's outdated values with the new ones. On the other hand, if you were to fetch the employee, change it, and then refetch it, you would not want to refresh the employee. If you to refreshed it-whether or not another application had changed the employee-you would lose the changes that you had made to the object.

You can get finer-grain control on an EODatabaseContext's refreshing behavior in Yellow Box than you can with an EOFetchSpecification by using the delegate method __databaseContextShouldUpdateCurrentSnapshot__ . For more information see the EODatabaseContext class specification and EODatabaseContext.Delegate interface specification.

__See also:__ - __refreshesRefetchedObjects__

---

#### setRequiresAllQualifierBindingVariables

public void __setRequiresAllQualifierBindingVariables__ (boolean _allVariablesRequired_)

Sets the behavior when a missing binding is encountered during variable substitution. If _allVariablesRequired_ is __true__ , then a missing binding will cause an exception to be raised during variable substitution. The default value is __false__ , which says to prune any nodes for which there are no bindings.

__See also:__ - __fetchSpecificationWithQualifierBindings__ , - __requiresAllQualifierBindingVariables__

---

#### setSortOrderings

public void __setSortOrderings__ (NSArray _sortOrderings_)

Sets the receiver's array of EOSortOrderings to _sortOrderings_. When a fetch is performed with the receiver, the results are sorted by applying each EOSortOrdering in the array.

__See also:__ [- __sortedArrayUsingKeyOrderArray__](EOSortOrdering.md)([EOSortOrdering](EOSortOrdering.md)), [- __sortArrayUsingKeyOrderArray__](EOSortOrdering.md)([EOSortOrdering](EOSortOrdering.md)), __sortOrderings__

---

#### setUsesDistinct

public void __setUsesDistinct__ (boolean _flag)_

Controls whether duplicate objects or records are removed after fetching. If _flag_ is __true__ they're removed; if _flag_ is __false__ they aren't. EOFetchSpecifications by default don't use distinct.

__See also:__ - __usesDistinct__

---

#### sortOrderings

public NSArray __sortOrderings__ ()

__See also:__ Returns the receiver's array of EOSortOrderings. When a fetch is performed with the receiver, the results are sorted by applying each EOSortOrdering in the array.[- __sortedArrayUsingKeyOrderArray__](EOSortOrdering.md)([EOSortOrdering](EOSortOrdering.md)), [- __sortArrayUsingKeyOrderArray__](EOSortOrdering.md)([EOSortOrdering](EOSortOrdering.md)), __setSortOrderings__

---

#### usesDistinct

public boolean __usesDistinct__

(Returns __true__ if duplicate objects or records are removed after fetching, __false__ if they aren't. EOFetchSpecifications by default don't use distinct.

__See also:__ - __setUsesDistinct__

---

[!](EOFaultHandler.md)
[!](EOGenericRecord.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
