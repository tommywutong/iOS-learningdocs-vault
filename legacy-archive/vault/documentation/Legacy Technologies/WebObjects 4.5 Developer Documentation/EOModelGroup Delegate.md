---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Protocols/EOModelGroupDelegate.html
archived_at: '2026-07-15T08:11:36.045284Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOModelGroup Delegate

> __Declared in:__  EOAccess/EOModelGroup.h

## Protocol Description

---

An EOModelGroup object should have a delegate which can influence
how it finds and loads models. The EOModelGroup instance delegate
can implement the methods below:

- [entity:relationshipForRow:relationship:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bairswyzlhmf2gkl3fnz2gs5dzhjzgk3dboruw63ttnbuxartpojjg65z2ojswyylunfxw443infydu)
- [subEntityForEntity:primaryKey:isFinal:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bairswyzlhmf2gkl3tovrek3tunf2hsrtpojcw45djor4tu4dsnfwwc4tzjnsxsotjondgs3tbnq5a)
- [entity:failedToLookupClassNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bairswyzlhmf2gkl3fnz2gs5dzhjtgc2lmmvsfi32mn5xww5lqinwgc43tjzqw2zlehi)
- [entity:classForObjectWithGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bairswyzlhmf2gkl3fnz2gs5dzhjrwyyltondg64spmjvgky3uk5uxi2chnrxweylmjfcdu)

In addition to the delegates you assign to EOModelGroup instances,
the EOModelGroup class itself can have a delegate. The class delegate
implements a single method- [defaultModelGroup](EOModelGroup%20Class%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bainwgc43tebcgk3dfm5qxizjpmrswmylvnr2e233emvweo4tpovya).
For more information, see the [EOModelGroup Class Delegate](EOModelGroup%20Class%20Delegate.md#apple-indeerckizduo) protocol description.

## Instance Methods

---

### entity:classForObjectWithGlobalID:

`- (Class)entity:(EOEntity
*)entity
classForObjectWithGlobalID:(EOGlobalID
*)globalID`

Used to fine-tune inheritance. The delegate
can use _globalID_ to determine a subclass
to be used in place of the one specified in entity.

---

### entity:failedToLookupClassNamed:

`- (Class)entity:(EOEntity
*)entity
failedToLookupClassNamed:(NSString
*)className`

Invoked when the class name specified for entity
cannot be found at run-time. The delegate can take action (such
as loading a bundle) to provide entity with a class corresponding
to _className_. If the delegate cannot
provide anything, or if there is no delegate, EOGenericRecord is
used.

---

### entity:relationshipForRow:relationship:

`- (EORelationship *)entity:(EOEntity
*)entity
relationshipForRow:(NSDictionary
*)row
relationship:(EORelationship *)relationship`

Invoked when relationships are instantiated
for a newly fetched object. The delegate can use the information
in row to determine which entity the target enterprise object should
be associated with, and replace the relationship appropriately.

---

### modelGroup:entityNamed:

`- (EOModel *)modelGroup:(EOModelGroup
*)group
entityNamed:(NSString *)name`

If implemented by the delegate, this method
should search the _group_ for the entity
named _name_ and return the entity's
EOModel. Return nil if _name_ is not
an entity in _group_.

---

### relationship:failedToLookupDestinationNamed:

`- (EOEntity *)relationship:(EORelationship
*)relationship
failedToLookupDestinationNamed:(NSString
*)entityName`

Invoked when loading relationship and the destination
entityName specified in the model file cannot be found in the model
group. This most often occurs when a model references entities in
another model file that can't be found. If the delegate doesn't
implement this method, an exception is raised. If the delegate does
implement this method, the method's return value is set as the
destination entity. if the delegate returns nil, the destination
entity is set to nil.

---

### subEntityForEntity:primaryKey:isFinal:

`- (EOEntity *)subEntityForEntity:(EOEntity
*)entity
primaryKey:(NSDictionary *)primaryKey
isFinal:(BOOL *)flag`

Allows the delegate to fine-tune inheritance
by indicating from which sub-entity an object should be fetched
based on its primaryKey. The entity returned must be a sub-entity
of _entity_. If the delegate knows
that the object should be fetched from the returned entity and not
one of its sub-entities, it should set _flag_ to
YES.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
