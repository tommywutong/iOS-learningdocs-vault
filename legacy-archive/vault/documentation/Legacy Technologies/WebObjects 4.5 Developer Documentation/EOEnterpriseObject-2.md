---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/More/EOEnterpriseObject.html
archived_at: '2026-07-15T08:11:39.071319Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)

# EOEnterpriseObject

## Initialization

The Framework creates enterprise objects with a constructor
of the following form:

> ```
> public MyClass(
> EOEditingContext anEditingContext,
> EOClassDescription classDescription,
> EOGlobalID globalID)
> ```

This constructor should create a new instance of your enterprise
object class with the provided arguments and it can perform any
custom initialization that you require. Enterprise objects created
in a Java client (with Java Client) and enterprise objects created
on the server (with Yellow Box) require this constructor.

After an enterprise object is created, it receives an `awake...` message.
The particular message depends on whether the object has been fetched
from a database or created anew in the application. In the former case,
it receives an [awakeFromFetch](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvdgk5ddna) message. In the latter,
it receives an [awakeFromInsertion](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvew443foj2gs33o) message. The receiver
can override either method to perform extra initialization-such
as setting default values-based on how it was created.

## Change Notification

For the Framework to keep all areas of an application synchronized,
enterprise objects must notify their observers when their state
changes. Objects do this by invoking [willChange](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxo2lmnrbwqylom5sq) before altering any instance variable
or other kind of state. This method informs all observers that the
invoker is about to change. See the [EOObserverCenter](EOObserverCenter.md#apple-ivhu6yttmvzhmzlsinsw45dfoi) class specification
for more information on change notification.

The primary observer of changes in an object is the object's
EOEditingContext. EOEditingContext is a subclass of EOObjectStore
that manages collections of objects in memory, tracking inserts,
deletes, and updates, and propagating changes to the persistent
store as needed. You can get the EOEditingContext that contains
an object by sending the object an [editingContext](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwkzdjoruw4z2dn5xhizlyoq) message.

## Object and Class Metadata Access

One of the larger groups of methods in the EOEnterpriseObject
interface provides information about an object's properties. Most
of these methods consult an EOClassDescription to provide their
answers. An object's [classDescription](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg3dbonzuizltmnzgs4dunfxw4) method returns it's
class description. See the [EOClassDescription](EOClassDescription.md#apple-ivhug3dbonzuizltmnzgs4dunfxw4) class specification
for the methods it implements. Methods you can send directly to
an enterprise object include [entityName](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk3tunf2hsttbnvsq), which provides the name
of the entity mapped to the receiver's class; [allPropertyKeys](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc3dmkbzg64dfoj2hss3fpfzq), which returns the
names of all the receiver's class properties, attributes and relationships
alike; and [attributeKeys](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc5duojuwe5lumvfwk6lt), which returns just
the names of the attributes.

Some methods return information about relationships. [toOneRelationshipKeys](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32pnzsvezlmmf2gs33oonugs4clmv4xg) and [toManyRelationshipKeys](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y) return the
names of the receiver's relationships, while [isToManyKey](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxws42un5gwc3tzjnsxs) tells which kind a particular
relationship is. [deleteRuleForRelationshipKey](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwizlmmv2gkutvnrsum33skjswyylunfxw443infyewzlz) indicates
what should happen to the receiver's relationships when it's
deleted. Similarly, [ownsDestinationObjectsForRelationshipKey](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxw653ooncgk43unfxgc5djn5xe6ytkmvrxi42gn5zfezlmmf2gs33oonugs4clmv4q) indicates
what should happen when another object is added to or removed from
the receiver's relationship. Another method, [classDescriptionForDestinationKey](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg3dbonzuizltmnzgs4dunfxw4rtpojcgk43unfxgc5djn5xewzlz),
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
the necessary conversions for proper behavior. [snapshot](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxg3tbobzwq33u) returns a dictionary containing
all the receiver's properties, and [updateFromSnapshot](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxk4demf2gkrtsn5wvg3tbobzwq33u) sets properties
of the receiver to the values in a snapshot.

A special kind of snapshot is also used to merge an object's
uncommitted changes with changes that have been committed to the
external store since the object was fetched (in Yellow Box only).
These methods are [changesFromSnapshot](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg2dbnztwk42gojxw2u3omfyhg2dpoq) and [reapplyChangesFromDictionary](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxezlbobygy6kdnbqw4z3fondhe33niruwg5djn5xgc4tz).

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
| `MyClass ( EOEditingContext, EOClassDescription, EOGlobalID)` | The framework creates enterprise objects with this method if it exists. Yellow Box resorts to the empty constructor if this constructor doesn't exist, but Java Client requires this constructor. |
| [awakeFromFetch](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvdgk5ddna) | Performs additional initialization after the object is fetched. |
| [awakeFromInsertion](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvew443foj2gs33o) | Performs additional initialization after the object is created in memory. |

|  |
| --- |
| __Key-Value Coding: Accessing Properties and Relationships__ |
| `set Key` | Sets the value for the property named _key._ |
| `key` | Retrieves the value for the property named _key._ |
| `addTo Key` | Adds an object to a relationship property named _key._ |
| `removeFrom Key` | Removes an object from the property named _key._ |
| [handleTakeValueForUnboundKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvkgc23fkzqwy5lfizxxevlomjxxk3tejnsxs) | Handles a failure of [takeValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) to find a property. |
| [handleQueryWithUnboundKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvixkzlspflws5dikvxge33vnzsewzlz) | Handles a failure of [valueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) to find a property. |
| [unableToSetNullForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpovxgcytmmvkg6u3forhhk3dmizxxes3fpe) | Handles an attempt to set a non-object property's value to `null`. |

|  |
| --- |
| __Validation__ |
| `validate Key` | Validates a value for the property named _key._ |
| [validateForDelete](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zeizlmmv2gk) | Validates all properties before deleting the receiver. |
| [validateForInsert](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zes3ttmvzhi) | Validates all properties before inserting the receiver. |
| [validateForSave](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zfgylwmu) | Validates all properties before saving the receiver. |
| [validateForUpdate](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zfk4demf2gk) | Validates all properties before updating the receiver. |

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)
