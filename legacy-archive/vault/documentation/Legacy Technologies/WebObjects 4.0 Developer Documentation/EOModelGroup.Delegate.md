---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOModelGroupDelegate.html
archived_at: '2026-07-18T01:28:14.796005Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOModelGroup.ClassDelegate.md)
[!](EOPropertyListEncoding.md)

---

# EOModelGroup.Delegate

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.eoaccess

- An EOModelGroup object should have a delegate which can influence how it finds and loads models. The EOModelGroup instance delegate can implement the methods below:`entityRelationshipForRowpublic abstract EORelationship entityRelationshipForRow(EOEntity entity, NSDictionary row, EORelationship relationship)`
- `subEntityForEntity:primaryKey:isFinal:`
- `entityFailedToLookupClassNamedpublic abstract java.lang.Class entityFailedToLookupClassNamed(EOEntity entity, java.lang.String className)`
- `entity:classForObjectWithGlobalID:`

In addition to the delegates you assign to EOModelGroup instances, the EOModelGroup class itself can have a delegate. The class delegate implements a single method-[`defaultModelGroup`](EOModelGroupClassDelegate.md#apple-gizda). For more information, see the [EOModelGroup.ClassDelegate](EOModelGroup.ClassDelegate.md).

---

## Instance Methods

---

### classForObjectWithGlobalID

public abstract java.lang.Class `classForObjectWithGlobalID`(EOEntity _entity_,
com.apple.yellow.eocontrol.EOGlobalID _globalID_)

Used to fine-tune inheritance. The delegate can use _globalID_ to determine a subclass to be used in place of the one specified in _entity_.

__entityFailedToLookupClassNamed__ public abstract java.lang.Class `entityFailedToLookupClassNamed`(EOEntity _entity_,
java.lang.String _className_)

Invoked when the class name specified for _entity_ cannot be found at run-time. The delegate can take action (such as loading a bundle) to provide _entity_ with a class corresponding to _className_. If the delegate cannot provide anything, or if there is no delegate, EOGenericRecord is used.

__entityRelationshipForRow__ public abstract EORelationship `entityRelationshipForRow`(EOEntity _entity_,
NSDictionary _row_,
EORelationship _relationship_)

Invoked when relationships are instantiated for a newly fetched object. The delegate can use the information in _row_ to determine which entity the target enterprise object should be associated with, and replace the relationship appropriately.

---

### modelGroupEntityWithName

public abstract EOModel `modelGroupEntityWithName`(EOModelGroup _group_,
java.lang.String _name_)

If implemented by the delegate, this method should search the _group_ for the entity named _name_ and return the entity's EOModel. Return `null` if _name_ is not an entity in _group_.

__relationshipFailedToLookupDestinationWithName__ public abstract EOEntity `relationshipFailedToLookupDestinationWithName`(
EORelationship _relationship_,
java.lang.String _entityName_)

Invoked when loading _relationship_ and the destination _entityName_ specified in the model file cannot be found in the model group. This most often occurs when a model references entities in another model file that can't be found. If the delegate doesn't implement this method, an exception is raised. If the delegate does implement this method, the method's return value is set as the destination entity. if the delegate returns `null`, the destination entity is set to `null`.

---

[!](EOModelGroup.ClassDelegate.md)
[!](EOPropertyListEncoding.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
