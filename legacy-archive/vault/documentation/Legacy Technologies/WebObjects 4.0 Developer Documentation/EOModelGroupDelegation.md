---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOModelGroupDelegate.html
archived_at: '2026-07-18T01:28:24.237891Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOModelGroupClassDelegation.md)
[!](EOPropertyListEncoding-2.md)

---

# EOModelGroupDelegation

__Inherits From:__
NSObject

__Declared in:__
EOAccess/EOModelGroup.h

# Protocol Description

An EOModelGroup object should have a delegate which can influence how it finds and loads models. The EOModelGroup instance delegate can implement the methods below:

- [`entity:relationshipForRow:relationship:`](#apple-gy4dmoi)
- [`subEntityForEntity:primaryKey:isFinal:`](#apple-gy4dmmi)
- [`entity:failedToLookupClassNamed:`](#apple-gizti)
- [`entity:classForObjectWithGlobalID:`](#apple-gy4dooa)

In addition to the delegates you assign to EOModelGroup instances, the EOModelGroup class itself can have a delegate. The class delegate implements a single method-[`defaultModelGroup`](EOModelGroupClassDelegate.md#apple-gizda). For more information, see the [EOModelGroupClassDelegation](EOModelGroupClassDelegation.md).

---

## Instance Methods

---

### entity:classForObjectWithGlobalID:

- (Class)`entity:`(EOEntity \*)_entity_ `classForObjectWithGlobalID:`(EOGlobalID \*)_globalID_

Used to fine-tune inheritance. The delegate can use _globalID_ to determine a subclass to be used in place of the one specified in _entity_.

---

### entity:failedToLookupClassNamed:

- (Class)`entity:`(EOEntity \*)_entity_ `failedToLookupClassNamed:`(NSString \*)_className_

Invoked when the class name specified for _entity_ cannot be found at run-time. The delegate can take action (such as loading a bundle) to provide _entity_ with a class corresponding to _className_. If the delegate cannot provide anything, or if there is no delegate, EOGenericRecord is used.

---

### entity:relationshipForRow:relationship:

- (EORelationship \*)`entity:`(EOEntity \*)_entity_ `relationshipForRow:`(NSDictionary \*)_row_ `relationship:`(EORelationship \*)_relationship_

Invoked when relationships are instantiated for a newly fetched object. The delegate can use the information in _row_ to determine which entity the target enterprise object should be associated with, and replace the relationship appropriately.

---

### modelGroup:entityNamed:

- (EOModel \*)`modelGroup:`(EOModelGroup \*)_group_ `entityNamed:`(NSString \*)_name_

If implemented by the delegate, this method should search the _group_ for the entity named _name_ and return the entity's EOModel. Return `nil` if _name_ is not an entity in _group_.

---

### relationship:failedToLookupDestinationNamed:

- (EOEntity \*)__relationship:__ (EORelationship \*)_relationship_ __failedToLookupDestinationNamed:__ (NSString \*)_entityName_

Invoked when loading _relationship_ and the destination _entityName_ specified in the model file cannot be found in the model group. This most often occurs when a model references entities in another model file that can't be found. If the delegate doesn't implement this method, an exception is raised. If the delegate does implement this method, the method's return value is set as the destination entity. if the delegate returns `nil`, the destination entity is set to `nil`.

---

### subEntityForEntity:primaryKey:isFinal:

- (EOEntity \*)`subEntityForEntity:`(EOEntity \*)_entity_`primaryKey:`(NSDictionary \*)_primaryKey_`isFinal:`(BOOL \*)_flag_

Allows the delegate to fine-tune inheritance by indicating from which sub-entity an object should be fetched based on its _primaryKey_. The entity returned must be a sub-entity of _entity_. If the delegate knows that the object should be fetched from the returned entity and not one of its sub-entities, it should set _flag_ to YES.

---

[!](EOModelGroupClassDelegation.md)
[!](EOPropertyListEncoding-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
