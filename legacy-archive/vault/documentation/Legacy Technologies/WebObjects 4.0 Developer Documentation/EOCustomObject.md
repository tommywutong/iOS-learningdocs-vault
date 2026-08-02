---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOCustomObject.html
archived_at: '2026-07-18T01:28:25.267109Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOCooperatingObjectStore.md)
[!](EODataSource.md)

---

# EOCustomObject

__Inherits From:__
Object (Java Client)
NSObject (Yellow Box)

__Implements:__
EOEnterpriseObject
EOKeyValueCoding (EOKeyValueCodingAdditions)
EOKeyValueCodingAdditions (EOEnterpriseObject)
EORelationshipManipulation (EOEnterpriseObject)
EOValidation (EOEnterpriseObject)
EOFaulting (EOEnterpriseObject)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (\Yellow Box)

## Class Description

The EOCustomObject class provides a default implementation of the EOEnterpriseObject interface. If you need to create a custom enterprise object class, you can subclass EOCustomObject and inherit the Framework's default implementations. Some of the methods are for subclasses to implement or override, but most are meant to be used as defined by EOCustomObject. For information on which methods you should implement in your subclass, see the [EOEnterpriseObject](EOEnterpriseObject.md) interface specification.

EOCustomObject's method implementations are described in the specification for the interface that declares them. For example, you can find a description of how EOCustomObject implements [__valueForKey__](EOKeyValueCoding.md)(introduced in the EOKeyValueCoding interface) in the specification for EOKeyValueCoding, and you can find a description of how EOCustomObject implements [__classDescription__](EOEnterpriseObject.md)(introduced in the EOEnterpriseObject interface) in the specification for EOEnterpriseObject.

The only methods provided in EOCustomObject that aren't defined in the EOEnterpriseObject interface are the following three static methods:

- accessInstanceVariablesDirectly
- flushAllKeyBindings
- useStoredAccessor

You would never invoke these methods, rather, they are provided in EOCustomObject to demonstrate the additional API your custom enterprise objects can implement. Similarly, EOCustomObject's constructors are not meant to be invoked; you would never create an instance of EOCustomObject. Rather, EOCustomObject provides the constructors to demonstrate the constructors your custom enterprise objects should implement.

## Interfaces Implemented

**[EOKeyValueCoding](EOKeyValueCoding.md)**

**[- handleQueryWithUnboundKey](EOKeyValueCoding.md)

**[- handleTakeValueForUnboundKey](EOKeyValueCoding.md)

**[- storedValueForKey](EOKeyValueCoding.md)

**[- takeStoredValueForKey](EOKeyValueCoding.md)

**[- takeValueForKey](EOKeyValueCoding.md)

**[- unableToSetNullForKey](EOKeyValueCoding.md)

**[- valueForKey](EOKeyValueCoding.md)**************

**[EOKeyValueCodingAdditions](EOKeyValueCodingAdditions.md)**

**[- takeValueForKeyPath](EOKeyValueCodingAdditions.md)

**[- takeValuesFromDictionary](EOKeyValueCodingAdditions.md)

**[- valueForKeyPath](EOKeyValueCodingAdditions.md)

**[- valuesForKeys](EOKeyValueCodingAdditions.md)********

**[EORelationshipManipulation](EORelationshipManipulation.md)**

**[- addObjectToBothSidesOfRelationshipWithKey](EORelationshipManipulation.md)

**[- addObjectToPropertyWithKey](EORelationshipManipulation.md)

**[- removeObjectFromBothSidesOfRelationshipWithKey](EORelationshipManipulation.md)

**[- removeObjectFromPropertyWithKey](EORelationshipManipulation.md)********

**[EOValidation](EOValidation.md)**

**[- validateForDelete](EOValidation.md)

**[- validateForInsert](EOValidation.md)

**[- validateForSave](EOValidation.md)

**[- validateForUpdate](EOValidation.md)

**[- validateValueForKey](EOValidation.md)**********

**EOEnterpriseObject**

**[allPropertyKeys](EOEnterpriseObject.md)

**[attributeKeys](EOEnterpriseObject.md)

**[awakeFromFetch](EOEnterpriseObject.md)

**[awakeFromInsertion](EOEnterpriseObject.md)

**[changesFromSnapshot](EOEnterpriseObject.md) (Yellow Box only)

**[classDescription](EOEnterpriseObject.md)

**[classDescriptionForDestinationKey](EOEnterpriseObject.md)

**[clearProperties](EOEnterpriseObject.md)

**[deleteRuleForRelationshipKey](EOEnterpriseObject.md)

**[editingContext](EOEnterpriseObject.md)

**[entityName](EOEnterpriseObject.md)

**[eoDescription](EOEnterpriseObject.md)

**[eoShallowDescription](EOEnterpriseObject.md)

**[inverseForRelationshipKey](EOEnterpriseObject.md)

**[invokeRemoteMethod](EOEnterpriseObject.md) (Java Client only)

**[isToManyKey](EOEnterpriseObject.md)

**[ownsDestinationObjectsForRelationshipKey](EOEnterpriseObject.md)

**[propagateDeleteWithEditingContext](EOEnterpriseObject.md)

**[reapplyChangesFromDictionary](EOEnterpriseObject.md) (Yellow Box only)

**[snapshot](EOEnterpriseObject.md)

**[toManyRelationshipKeys](EOEnterpriseObject.md)

**[toOneRelationshipKeys](EOEnterpriseObject.md)

**[updateFromSnapshot](EOEnterpriseObject.md)

**[userPresentableDescription](EOEnterpriseObject.md) (Yellow Box only)

**[willChange](EOEnterpriseObject.md)**************************************************

**[EOFaulting](EOFaulting.md)**

**[clearFault](EOFaulting.md)

**[isFault](EOFaulting.md)

**[turnIntoFault](EOFaulting.md)

**[willRead](EOFaulting.md)********

## Constructors

public __EOCustomObject__ (EOEditingContext _anEOEditingContext_, EOClassDescription _anEOClassDescription_, EOGlobalID _anEOGlobalID_)

You would never create an instance of EOCustomObject; rather, your subclasses can create constructors of this same form. A subclass's constructors should create a new object and initialize it with the arguments provided.

__See also:__ [- __createInstanceWithEditingContext__](EOClassDescription.md)(EOClassDescription)

## Static Methods

---

#### accessInstanceVariablesDirectly

public static boolean __accessInstanceVariablesDirectly__ ()

Subclasses implement this method to return __false__ if the key-value coding methods should never access the corresponding instance variable directly on finding no accessor method for a property. You don't have to implement this method if the default behavior of accessing instance variables directly is correct for your objects.

__See also:__ [__valueForKey__](EOKeyValueCoding.md), [__takeValueForKey__](EOKeyValueCoding.md)

---

#### flushAllKeyBindings

public static void __flushAllKeyBindings__ ()

Invalidates the cached key binding information for all classes (caches are kept of key-to-method or instance variable bindings in order to make key-value coding efficient). This method should be invoked whenever a class is modified in or removed from the run-time system.

__See also:__

---

#### useStoredAccessor

public static boolean __useStoredAccessor__ ()

Subclasses implement this method to return __false__ if the stored value methods ([__storedValueForKey__](EOKeyValueCoding.md)and [__takeStoredValueForKey__](EOKeyValueCoding.md)) should not use private accessor methods in preference to public accessors. Returning __false__ causes the stored value methods to use the same accessor method-instance variable search order as the corresponding basic key-value coding methods ([__valueForKey__](EOKeyValueCoding.md)and [__takeValueForKey__](EOKeyValueCoding.md)). You don't have to implement this method if the default default stored value search order is correct for your objects.

---

[!](EOCooperatingObjectStore.md)
[!](EODataSource.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
