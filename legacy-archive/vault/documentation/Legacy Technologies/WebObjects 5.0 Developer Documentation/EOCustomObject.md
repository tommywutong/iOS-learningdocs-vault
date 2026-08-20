---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOCustomObject.html
archived_at: '2026-07-15T08:13:46.655364Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOCustomObject

> __Inherits from:__ Object
>
> __Implements:__
> EOEnterpriseObject
> EODeferredFaulting (EOEnterpriseObject)
> EOKeyValueCodingAdditions (EOEnterpriseObject)
> EORelationshipManipulation (EOEnterpriseObject)
> EOValidation (EOEnterpriseObject)
> EOFaulting (EODeferredFaulting)
> EOKeyValueCoding (EOKeyValueCodingAdditions)
> NSKeyValueCoding (EOKeyValueCoding)
>
> __Package:__ com.webobjects.eocontrol

---

## Class Description

---

The EOCustomObject class provides a default implementation of the EOEnterpriseObject interface. If you need to create a custom enterprise object class, you can subclass EOCustomObject and inherit the Framework's default implementations. Some of the methods are for subclasses to implement or override, but most are meant to be used as defined by EOCustomObject. For information on which methods you should implement in your subclass, see the EOEnterpriseObject interface specification.

EOCustomObject's method implementations are described in the specification for the interface that declares them. For example, you can find a description of how EOCustomObject implements valueForKey (introduced in the EOKeyValueCoding interface) in the specification for EOKeyValueCoding, and you can find a description of how EOCustomObject implements classDescription (introduced in the EOEnterpriseObject interface) in the specification for EOEnterpriseObject.

The only methods provided in EOCustomObject that aren't defined in the EOEnterpriseObject interface are the following three static methods:

- [canAccessFieldsDirectly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3von2g63kpmjvgky3uf5rwc3sbmnrwk43tizuwk3deoncgs4tfmn2gy6i)
- [shouldUseStoredAccessors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3von2g63kpmjvgky3uf5zwq33vnrsfk43fkn2g64tfmrawgy3fonzw64tt)

You would never invoke these methods, rather, they are provided in EOCustomObject to demonstrate the additional API your custom enterprise objects can implement. Similarly, EOCustomObject's constructors are not meant to be invoked; you would never create an instance of EOCustomObject. Rather, EOCustomObject provides the constructors to demonstrate the constructors your custom enterprise objects should implement.

## Interfaces Implemented

---

> EOKeyValueCoding and NSKeyValueCoding
> storedValueForKey
> takeStoredValueForKey
> takeValueForKeyvalueForKey
>
> EOKeyValueCodingAdditions
> takeValuesFromDictionaryvaluesForKeys
>
> EORelationshipManipulation
> addObjectToBothSidesOfRelationshipWithKey
> addObjectToPropertyWithKey
> removeObjectFromBothSidesOfRelationshipWithKey
> removeObjectFromPropertyWithKeyEOValidation
> validateForDeletevalidateForInsert
> validateForSavevalidateForUpdate
>
> EOEnterpriseObject
> allPropertyKeys
> attributeKeys
> awakeFromFetch
> awakeFromInsertion
> changesFromSnapshot
> classDescription
> classDescriptionForDestinationKey
> clearProperties
> deleteRuleForRelationshipKey
> editingContext
> entityName
> eoDescriptioneoShallowDescription
> inverseForRelationshipKey
> invokeRemoteMethodisToManyKey
> ownsDestinationObjectsForRelationshipKey
> propagateDeleteWithEditingContext
> reapplyChangesFromDictionary
> snapshot
> toManyRelationshipKeys
> toOneRelationshipKeys
> updateFromSnapshot
> userPresentableDescription
> willChangeEOFaulting
> clearFaultfaultHandler
> isFaultturnIntoFaultwillRead

## Constructors

---

### __EOCustomObject__

`public EOCustomObject()`

Description forthcoming.

`public EOCustomObject( EOEditingContext anEOEditingContext, EOClassDescription anEOClassDescription, EOGlobalID anEOGlobalID)`

You would never create an instance of EOCustomObject; rather, your subclasses can create constructors of this same form. A subclass's constructors should create a new object and initialize it with the arguments provided.

__See Also:__ createInstanceWithEditingContext (EOClassDescription)

---

## Static Methods

---

### canAccessFieldsDirectly

`public static boolean canAccessFieldsDirectly()`

Subclasses implement this method to return `false` if the key-value coding methods should never access the corresponding instance variable directly on finding no accessor method for a property. You don't have to implement this method if the default behavior of accessing instance variables directly is correct for your objects.

__See Also:__ valueForKey, takeValueForKey

---

### shouldUseStoredAccessors

`public static boolean shouldUseStoredAccessors()`

Subclasses implement this method to return `false` if the stored value methods (storedValueForKey and takeStoredValueForKey) should not use private accessor methods in preference to public accessors. Returning `false` causes the stored value methods to use the same accessor method-instance variable search order as the corresponding basic key-value coding methods (valueForKey and takeValueForKey). You don't have to implement this method if the default stored value search order is correct for your objects.

---

### usesDeferredFaultCreation

`public static boolean usesDeferredFaultCreation()`

Conformance to EODeferredFaulting.

---

## Instance Methods

---

### addObjectToBothSidesOfRelationshipWithKey

`public void addObjectToBothSidesOfRelationshipWithKey( EORelationshipManipulation anEORelationshipManipulation, String aString)`

Description forthcoming.

---

### addObjectToPropertyWithKey

`public void addObjectToPropertyWithKey( Object anObject, String aString)`

Description forthcoming.

---

### allPropertyKeys

`public NSArray allPropertyKeys()`

Description forthcoming.

---

### attributeKeys

`public NSArray attributeKeys()`

Description forthcoming.

---

### awakeFromClientUpdate

`public void awakeFromClientUpdate(EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### awakeFromFetch

`public void awakeFromFetch(EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### awakeFromInsertion

`public void awakeFromInsertion(EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### changesFromSnapshot

`public NSDictionary changesFromSnapshot(NSDictionary aNSDictionary)`

Description forthcoming.

---

### classDescription

`public EOClassDescription classDescription()`

Description forthcoming.

---

### classDescriptionForDestinationKey

`public EOClassDescription classDescriptionForDestinationKey(String aString)`

Description forthcoming.

---

### clearFault

`public void clearFault()`

Description forthcoming.

---

### clearProperties

`public void clearProperties()`

Description forthcoming.

---

### deleteRuleForRelationshipKey

`public int deleteRuleForRelationshipKey(String aString)`

Description forthcoming.

---

### editingContext

`public EOEditingContext editingContext()`

Description forthcoming.

---

### entityName

`public String entityName()`

Description forthcoming.

---

### eoDescription

`public String eoDescription()`

Description forthcoming.

---

### eoShallowDescription

`public String eoShallowDescription()`

Description forthcoming.

---

### faultHandler

`public EOFaultHandler faultHandler()`

Description forthcoming.

---

### handleQueryWithUnboundKey

`public Object handleQueryWithUnboundKey(String aString)`

Description forthcoming.

---

### handleTakeValueForUnboundKey

`public void handleTakeValueForUnboundKey( Object anObject, String aString)`

Description forthcoming.

---

### inverseForRelationshipKey

`public String inverseForRelationshipKey(String aString)`

Description forthcoming.

---

### invokeRemoteMethod

`public Object invokeRemoteMethod(String methodName, Class[] argumentTypes, Object[] arguments)`

Description forthcoming.

---

### isFault

`public boolean isFault()`

Description forthcoming.

---

### isToManyKey

`public boolean isToManyKey(String aString)`

Description forthcoming.

---

### ownsDestinationObjectsForRelationshipKey

`public boolean ownsDestinationObjectsForRelationshipKey(String aString)`

Description forthcoming.

---

### prepareValuesForClient

`public void prepareValuesForClient()`

Description forthcoming.

---

### propagateDeleteWithEditingContext

`public void propagateDeleteWithEditingContext(EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### readResolve

`protected Object readResolve()`

Description forthcoming.

---

### reapplyChangesFromDictionary

`public void reapplyChangesFromDictionary(NSDictionary aNSDictionary)`

Description forthcoming.

---

### removeObjectFromBothSidesOfRelationshipWithKey

`public void removeObjectFromBothSidesOfRelationshipWithKey( EORelationshipManipulation anEORelationshipManipulation, String aString)`

Description forthcoming.

---

### removeObjectFromPropertyWithKey

`public void removeObjectFromPropertyWithKey( Object anObject, String aString)`

Description forthcoming.

---

### snapshot

`public NSDictionary snapshot()`

Description forthcoming.

---

### storedValueForKey

`public Object storedValueForKey(String aString)`

Description forthcoming.

---

### takeStoredValueForKey

`public void takeStoredValueForKey( Object anObject, String aString)`

Description forthcoming.

---

### takeValueForKey

`public void takeValueForKey( Object anObject, String aString)`

Description forthcoming.

---

### takeValueForKeyPath

`public void takeValueForKeyPath( Object anObject, String aString)`

Description forthcoming.

---

### takeValuesFromDictionary

`public void takeValuesFromDictionary(NSDictionary aNSDictionary)`

Description forthcoming.

---

### toManyRelationshipKeys

`public NSArray toManyRelationshipKeys()`

Description forthcoming.

---

### toOneRelationshipKeys

`public NSArray toOneRelationshipKeys()`

Description forthcoming.

---

### toString

`public String toString()`

Description forthcoming.

---

### turnIntoFault

`public void turnIntoFault(EOFaultHandler anEOFaultHandler)`

Description forthcoming.

---

### unableToSetNullForKey

`public void unableToSetNullForKey(String aString)`

Description forthcoming.

---

### updateFromSnapshot

`public void updateFromSnapshot(NSDictionary aNSDictionary)`

Description forthcoming.

---

### userPresentableDescription

`public String userPresentableDescription()`

Description forthcoming.

---

### validateClientUpdate

`public void validateClientUpdate()`

Description forthcoming.

---

### validateForDelete

`public void validateForDelete()`

Description forthcoming.

---

### validateForInsert

`public void validateForInsert()`

Description forthcoming.

---

### validateForSave

`public void validateForSave()`

Description forthcoming.

---

### validateForUpdate

`public void validateForUpdate()`

Description forthcoming.

---

### validateTakeValueForKeyPath

`public Object validateTakeValueForKeyPath( Object anObject, String aString)`

Description forthcoming.

---

### validateValueForKey

`public Object validateValueForKey( Object anObject, String aString)`

Description forthcoming.

---

### valueForKey

`public Object valueForKey(String aString)`

Description forthcoming.

---

### valueForKeyPath

`public Object valueForKeyPath(String aString)`

Description forthcoming.

---

### valuesForKeys

`public NSDictionary valuesForKeys(NSArray aNSArray)`

Description forthcoming.

---

### willChange

`public void willChange()`

Description forthcoming.

---

### willRead

`public void willRead()`

Description forthcoming.

---

### willReadRelationship

`public Object willReadRelationship(Object object)`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
