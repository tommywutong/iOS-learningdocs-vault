---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Protocols/EOModelGroupDelegate.html
archived_at: '2026-07-15T08:13:42.045186Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOModelGroup.Delegate

> **__Package:__**
> : com.webobjects.eoaccess

---

## Interface Description

---

An EOModelGroup object should have a delegate which can influence how it finds and loads models. The EOModelGroup instance delegate can implement the methods below:

- entityRelationshipForRow
- subEntityForEntity
- entityFailedToLookupClassNamed
- classForObjectWithGlobalID

In addition to the delegates you assign to EOModelGroup instances, the EOModelGroup class itself can have a delegate. The class delegate implements a single method-defaultModelGroup. For more information, see the EOModelGroup.ClassDelegate interface description.

## Instance Methods

---

### classForObjectWithGlobalID

`public abstract Class classForObjectWithGlobalID( EOEntity entity, com.webobjects.eocontrol.EOGlobalID globalID)`

Used to fine-tune inheritance. The delegate can use _globalID_ to determine a subclass to be used in place of the one specified in entity.

---

### entityFailedToLookupClassNamed

`public abstract Class entityFailedToLookupClassNamed( EOEntity entity, String className)`

Invoked when the class name specified for entity cannot be found at run-time. The delegate can take action (such as loading a bundle) to provide entity with a class corresponding to _className_. If the delegate cannot provide anything, or if there is no delegate, EOGenericRecord is used.

---

### entityRelationshipForRow

`public abstract EORelationship entityRelationshipForRow( EOEntity entity, NSDictionary row, EORelationship relationship)`

Invoked when relationships are instantiated for a newly fetched object. The delegate can use the information in row to determine which entity the target enterprise object should be associated with, and replace the relationship appropriately.

---

### modelGroupEntityWithName

`public abstract EOModel modelGroupEntityWithName( EOModelGroup group, String name)`

If implemented by the delegate, this method should search the _group_ for the entity named _name_ and return the entity's EOModel. Returns `null` if _name_ is not an entity in _group_.

---

### relationshipFailedToLookupDestinationWithName

`public abstract EOEntity relationshipFailedToLookupDestinationWithName( EORelationship relationship, String entityName)`

Invoked when loading relationship and the destination entityName specified in the model file cannot be found in the model group. This most often occurs when a model references entities in another model file that can't be found. If the delegate doesn't implement this method, an exception is raised. If the delegate does implement this method, the method's return value is set as the destination entity. if the delegate returns `null`, the destination entity is set to `null`.

---

### subEntityForEntity

`public abstract EOEntity subEntityForEntity( EOEntity entity, NSDictionary primaryKey)`

Allows the delegate to fine-tune inheritance by indicating from which sub-entity an object should be fetched based on its primaryKey. The entity returned must be a sub-entity of _entity_.

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
