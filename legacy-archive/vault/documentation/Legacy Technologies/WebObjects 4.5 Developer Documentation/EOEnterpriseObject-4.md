---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/More/EOEnterpriseObject.html
archived_at: '2026-07-15T08:11:43.603232Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)

# EOEnterpriseObject

## Initialization

Enterprise objects are initialized using [initWithEditingContext:classDescription:globalID:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5uw42luk5uxi2cfmruxi2lom5bw63tumv4hiotdnrqxg42emvzwg4tjob2gs33ohjtwy33cmfwesrb2),
which by default simply invokes init. You can place your custom
initialization code in __init__, or you can
override __initWithEditingContext:classDescription:globalID:__ to
take advantage of the extra information available with this method.

After an enterprise object is created, it receives an __awake...__ message.
The particular message depends on whether the object has been fetched
from a database or created anew in the application. In the former case,
it receives an [awakeFromFetchInEditingContext:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxoyllmvdhe33nizsxiy3ijfxekzdjoruw4z2dn5xhizlyoq5a) message.
In the latter, it receives an [awakeFromInsertionInEditingContext:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxoyllmvdhe33njfxhgzlsoruw63sjnzcwi2lunfxgoq3pnz2gk6duhi) message.
The receiver can override either method to perform extra initialization-such
as setting default values-based on how it was created.

## Change Notification

For the Framework to keep all areas of an application synchronized,
enterprise objects must notify their observers when their state
changes. Objects do this by invoking [willChange](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf53ws3dminugc3thmu) before altering any instance variable
or other kind of state. This method informs all observers that the
invoker is about to change. See the [EOObserverCenter](EOObserverCenter-2.md#apple-ivhu6yttmvzhmzlsinsw45dfoi) class specification
for more information on change notification.

The primary observer of changes in an object is the object's
EOEditingContext. EOEditingContext is a subclass of EOObjectStore
that manages collections of objects in memory, tracking inserts,
deletes, and updates, and propagating changes to the persistent
store as needed. You can get the EOEditingContext that contains
an object by sending the object an [editingContext](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5swi2lunfxgoq3pnz2gk6du) message.

## Object and Class Metadata Access

One of the larger groups of methods in the EOEnterpriseObject
interface provides information about an object's properties. Most
of these methods consult an EOClassDescription to provide their
answers. An object's [classDescription](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5rwyyltoncgk43dojuxa5djn5xa) method returns it's
class description. See the [EOClassDescription](EOClassDescription-3.md#apple-ivhug3dbonzuizltmnzgs4dunfxw4) class specification
for the methods it implements. Methods you can send directly to
an enterprise object include [entityName](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5sw45djor4u4ylnmu), which provides the name
of the entity mapped to the receiver's class; [allPropertyKeys](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qwy3cqojxxazlsor4uwzlzom), which returns the
names of all the receiver's class properties, attributes and relationships
alike; and [attributeKeys](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxi5dsnfrhk5dfjnsxs4y), which returns just
the names of the attributes.

Some methods return information about relationships. [toOneRelationshipKeys](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52g6t3omvjgk3dboruw63ttnbuxas3fpfzq) and [toManyRelationshipKeys](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52g6tlbnz4vezlmmf2gs33oonugs4clmv4xg) return the
names of the receiver's relationships, while [isToManyKey:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5uxgvdpjvqw46klmv4tu) tells which kind a particular
relationship is. [deleteRuleForRelationshipKey:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5sgk3dforsve5lmmvdg64ssmvwgc5djn5xhg2djobfwk6j2) indicates
what should happen to the receiver's relationships when it's
deleted. Similarly, [ownsDestinationObjectsForRelationshipKey:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5xxo3ttirsxg5djnzqxi2lpnzhwe2tfmn2hgrtpojjgk3dboruw63ttnbuxas3fpe5a) indicates
what should happen when another object is added to or removed from
the receiver's relationship. Another method, [classDescriptionForDestinationKey:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5rwyyltoncgk43dojuxa5djn5xem33sirsxg5djnzqxi2lpnzfwk6j2),
returns the EOClassDescription for the objects at the destination
of a relationship.

## Snapshots

The key-value coding methods define a general mechanism for
accessing an object's properties, but you first have to know what
those properties are. Sometimes, however, the Framework needs to
preserve an object's entire state for later use, whether to undo
changes to the object, compare the values that have changed, or
just keep a record of the changes. The snapshotting methods provide
this service, extracting or setting all properties at once and performing
the necessary conversions for proper behavior. [snapshot](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5zw4ylqonug65a) returns a dictionary containing
all the receiver's properties, and [updateFromSnapshot:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52xazdborsum4tpnvjw4ylqonug65b2) sets properties
of the receiver to the values in a snapshot.

A special kind of snapshot is also used to merge an object's
uncommitted changes with changes that have been committed to the
external store since the object was fetched. These methods are [changesFromSnapshot](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5rwqylom5sxgrtsn5wvg3tbobzwq33u) and [reapplyChangesFromDictionary:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5zgkylqobwhsq3imfxgozltizzg63kenfrxi2lpnzqxe6j2).

## Writing an Enterprise Object Class

Some of the EOEnterpriseObject methods are for enterprise
objects to implement or override, and some are meant to be used
as defined by the Framework. Many methods are used internally by
the Framework and rarely invoked by application code. The tables
in this section highlight the methods that you typically override
or implement in a custom enterprise object.

|  |
| --- |
| __Creation__ |
| __- init__ | Designated initializer. |
| [- initWithEditingContext:classDescription:globalID:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5uw42luk5uxi2cfmruxi2lom5bw63tumv4hiotdnrqxg42emvzwg4tjob2gs33ohjtwy33cmfwesrb2) | Optional initializer. |
| [- awakeFromFetchInEditingContext:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxoyllmvdhe33nizsxiy3ijfxekzdjoruw4z2dn5xhizlyoq5a) | Performs additional initialization after the object is fetched. |
| [- awakeFromInsertionInEditingContext:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxoyllmvdhe33njfxhgzlsoruw63sjnzcwi2lunfxgoq3pnz2gk6duhi) | Performs additional initialization after the object is created in memory. |

|  |
| --- |
| __Key-Value Coding: Accessing Properties and Relationships__ |
| `- setKey:` | Sets the value for the property named _key_. |
| `- key` | Retrieves the value for the property named _key_. |
| `- addToKey:` | Adds an object to a relationship property named _key_. |
| `- removeFromKey:` | Removes an object from the property named _key_. |
| [- handleTakeValue:forUnboundKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkrqwwzkwmfwhkzj2mzxxevlomjxxk3tejnsxsoq) | Handles a failure of [takeValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi) to find a property. |
| [- handleQueryWithUnboundKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkf2wk4tzk5uxi2cvnzrg65lomrfwk6j2) | Handles a failure of [valueForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi) to find a property. |
| [- unableToSetNullForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3vnzqwe3dfkrxvgzlujz2wy3cgn5zewzlzhi) | Handles an attempt to set a non-object property's value to __nil__. |

|  |
| --- |
| __Validation__ |
| `- validateKey:` | Validates a value for the property named _key_. |
| [- validateForDelete](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojcgk3dforsq) | Validates all properties before deleting the receiver. |
| [- validateForInsert](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojew443foj2a) | Validates all properties before inserting the receiver. |
| [- validateForSave](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojjwc5tf) | Validates all properties before saving the receiver. |
| [- validateForUpdate](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojkxazdborsq) | Validates all properties before updating the receiver. |

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)
