---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOEntityClassDescription.html
archived_at: '2026-07-15T08:13:41.571043Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOEntityClassDescription

> **__Inherits from:__**
> : com.webobjects.eocontrol.EOClassDescription

> **__Package:__**
> : com.webobjects.eoaccess

---

## Class Description

---

EOEntityClassDescription is the subclass of the control layer's EOClassDescription. The EOClassDescription class provides a mechanism for extending classes by giving them access to metadata not available in the run-time system. EOEntityClassDescription extends the behavior of enterprise objects by deriving information about them (such as NULL constraints and referential integrity rules) from an associated EOModel. For detailed information on the methods, see the EOClassDescription class specification.

In the typical scenario in which an enterprise object has a corresponding model file, the first time a particular operation is performed on a class (such as validating a value), an `ClassDescriptionNeeded...` notification (either an `ClassDescriptionNeededForClassNotification` or an `ClassDescriptionNeededForEntityNameNotification`) is broadcast. When an EOModel object receives this notification it registers the metadata (class description) for the EOEntity on which the enterprise object is based. This class description is used from that point on.

## Constructors

---

### EOEntityClassDescription

`public EOEntityClassDescription(EOEntity entity)`

Creates a new EOEntityClassDescription and assigns _entity_ to it.

__See Also:__ [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbwyyltoncgk43dojuxa5djn5xc6zlooruxi6i)

---

## Instance Methods

---

### allAttributeKeys

`public NSArray allAttributeKeys()`

Description forthcoming.

---

### allPropertyKeys

`public NSArray allPropertyKeys()`

Description forthcoming.

---

### allToManyRelationshipKeys

`public NSArray allToManyRelationshipKeys()`

Description forthcoming.

---

### allToOneRelationshipKeys

`public NSArray allToOneRelationshipKeys()`

Description forthcoming.

---

### attributeKeys

`public NSArray attributeKeys()`

Description forthcoming.

---

### awakeObjectFromInsertion

`public void awakeObjectFromInsertion( com.webobjects.eocontrol.EOEnterpriseObject anEOEnterpriseObject, com.webobjects.eocontrol.EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### classDescriptionForDestinationKey

`public com.webobjects.eocontrol.EOClassDescription classDescriptionForDestinationKey(String aString)`

Description forthcoming.

---

### clientAttributeKeys

`public NSArray clientAttributeKeys()`

Description forthcoming.

---

### clientToManyRelationshipKeys

`public NSArray clientToManyRelationshipKeys()`

Description forthcoming.

---

### clientToOneRelationshipKeys

`public NSArray clientToOneRelationshipKeys()`

Description forthcoming.

---

### createInstanceWithEditingContext

`public com.webobjects.eocontrol.EOEnterpriseObject createInstanceWithEditingContext( com.webobjects.eocontrol.EOEditingContext anEOEditingContext, com.webobjects.eocontrol.EOGlobalID anEOGlobalID)`

Description forthcoming.

---

### defaultFormatterForKey

`public java.text.Format defaultFormatterForKey(String aString)`

Description forthcoming.

---

### deleteRuleForRelationshipKey

`public int deleteRuleForRelationshipKey(String aString)`

Description forthcoming.

---

### entity

`public EOEntity entity()`

Returns the entity associated with the receiver.

__See Also:__ [EOEntityClassDescription](#apple-ineegrccizeum)

---

## Instance Methods

---

### allAttributeKeys

`public NSArray allAttributeKeys()`

Description forthcoming.

---

### allPropertyKeys

`public NSArray allPropertyKeys()`

Description forthcoming.

---

### allToManyRelationshipKeys

`public NSArray allToManyRelationshipKeys()`

Description forthcoming.

---

### allToOneRelationshipKeys

`public NSArray allToOneRelationshipKeys()`

Description forthcoming.

---

### attributeKeys

`public NSArray attributeKeys()`

Description forthcoming.

---

### awakeObjectFromInsertion

`public void awakeObjectFromInsertion( com.webobjects.eocontrol.EOEnterpriseObject anEOEnterpriseObject, com.webobjects.eocontrol.EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### classDescriptionForDestinationKey

`public com.webobjects.eocontrol.EOClassDescription classDescriptionForDestinationKey(String aString)`

Description forthcoming.

---

### clientAttributeKeys

`public NSArray clientAttributeKeys()`

Description forthcoming.

---

### clientToManyRelationshipKeys

`public NSArray clientToManyRelationshipKeys()`

Description forthcoming.

---

### clientToOneRelationshipKeys

`public NSArray clientToOneRelationshipKeys()`

Description forthcoming.

---

### createInstanceWithEditingContext

`public com.webobjects.eocontrol.EOEnterpriseObject createInstanceWithEditingContext( com.webobjects.eocontrol.EOEditingContext anEOEditingContext, com.webobjects.eocontrol.EOGlobalID anEOGlobalID)`

Description forthcoming.

---

### defaultFormatterForKey

`public java.text.Format defaultFormatterForKey(String aString)`

Description forthcoming.

---

### deleteRuleForRelationshipKey

`public int deleteRuleForRelationshipKey(String aString)`

Description forthcoming.

---

### entity

`public EOEntity entity()`

Description forthcoming.

---

### entityName

`public String entityName()`

Description forthcoming.

---

### fetchSpecificationNamed

`public com.webobjects.eocontrol.EOFetchSpecification fetchSpecificationNamed(String aString)`

Description forthcoming.

---

### inverseForRelationshipKey

`public String inverseForRelationshipKey(String aString)`

Description forthcoming.

---

### ownsDestinationObjectsForRelationshipKey

`public boolean ownsDestinationObjectsForRelationshipKey(String aString)`

Description forthcoming.

---

### readResolve

`protected Object readResolve()`

Description forthcoming.

---

### superClassDescription

`public com.webobjects.eocontrol.EOClassDescription superClassDescription()`

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

### validateObjectForDelete

`public void validateObjectForDelete(com.webobjects.eocontrol.EOEnterpriseObject anEOEnterpriseObject)`

Description forthcoming.

---

### validateObjectForSave

`public Exception validateObjectForSave(Object anObject)`

Description forthcoming.

---

### validateValueForKey

`public Object validateValueForKey( Object anObject, String aString)`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
