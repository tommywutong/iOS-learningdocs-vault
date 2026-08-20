---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOEnterpriseObject.html
archived_at: '2026-07-15T08:11:38.875475Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOEnterpriseObject

> __Implemented by:__ : EOCustomObject
> : EOGenericRecord

> **__Implements:__**
> : EODeferredFaulting
> : EOKeyValueCodingAdditions
> : EOKeyValueCoding.KeyBindingCreation
> : EORelationshipManipulation
> : EOValidation
> : EOFaulting (EODeferredFaulting)
> : EOKeyValueCoding (EOKeyValueCodingAdditions)

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Interface Description

---

The EOEnterpriseObject interface identifies basic enterprise
object behavior, defining methods for supporting operations common
to all enterprise objects. Among these are methods for initializing instances,
announcing changes, setting and retrieving property values, and
performing validation of state. Some of these methods are for enterprise
objects to implement or override, and some are meant to be used
as defined by the Framework. Many methods are used internally by
the Framework and rarely invoked by application code.

Many of the functional areas are defined in smaller, more
specialized interfaces and incorporated in the over arching EOEnterpriseObject interface:

- [EOKeyValueCoding](EOKeyValueCoding.md#apple-ineucq2iizduu) defines
  Enterprise Objects Framework's main data transport mechanism,
  in which the properties of an object are accessed indirectly by
  name (or "key"), rather than directly through invocation of
  an accessor method or as instance variables.
- EOKeyValueCoding.KeyBindingCreation defines a mechanism for
  binding class/key pairs with a method for accessing the key, which
  maximizes the performance of EOKeyValueCoding.
- [EOKeyValueCodingAdditions](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOKeyValueCodingAdd.html#CBFDAIAA) defines
  extensions to the basic EOKeyValueCoding interface, giving access
  to groups of properties and to properties across relationships.
- [EORelationshipManipulation](EORelationshipManipulation.md#apple-infemqsfireei) builds
  on the basic EOKeyValueCoding interface to allow you to modify to-many
  relationship properties.
- [EOValidation](EOValidation.md#apple-infemqsfifcui) defines
  the way that enterprise objects validate their values.
- [EOFaulting](EOFaulting.md#apple-ijcuiq2gijdee) and EODeferredFaulting
  define mechanisms for postponing an object's initialization until
  its actually needed.

The remaining methods are introduced in the EOEnterpriseObject interface itself
and can be broken down into three functional groups discussed in
the following sections:

- ["Initialization"](EOEnterpriseObject-2.md#apple-ijaueq2iizcem)
- ["Change Notification"](EOEnterpriseObject-2.md#apple-ijaueqsijbauu)
- ["Object and Class Metadata Access"](EOEnterpriseObject-2.md#apple-ijauerccjbaui)
- ["Snapshots"](EOEnterpriseObject-2.md#apple-ijauercbijauc)

You rarely need to implement the EOEnterpriseObject interface from
scratch. The Framework provides default implementations of the methods
in EOCustomObject and EOGenericRecord. Use EOGenericRecords to represent
enterprise objects that don't require custom behavior, and create subclasses
of EOCustomObject to represent enterprise objects that do. The section ["Writing an Enterprise Object Class"](EOEnterpriseObject-2.md#apple-ijaueqsijjfeg) highlights the methods that you typically provide
or override in a custom enterprise object class.

## Interfaces Implemented

---

> [EOKeyValueCoding](EOKeyValueCoding.md#apple-ineucq2iizduu): [handleQueryWithUnboundKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvixkzlspflws5dikvxge33vnzsewzlz)
> : [handleTakeValueForUnboundKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvkgc23fkzqwy5lfizxxevlomjxxk3tejnsxs)
> : [storedValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpon2g64tfmrlgc3dvmvdg64slmv4q)
> : [takeStoredValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzktorxxezlekzqwy5lfizxxes3fpe)
> : [takeValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz)
> : [unableToSetNullForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpovxgcytmmvkg6u3forhhk3dmizxxes3fpe)
> : [valueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe)
>
> [EOKeyValueCodingAdditions](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOKeyValueCodingAdd.html#CBFDAIAA): [takeValueForKeyPath](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOKeyValueCodingAdd.html#//apple_ref/java/intfm/EOKeyValueCodingAdditions/takeValueForKeyPath)
> : [takeValuesFromDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOKeyValueCodingAdd.html#//apple_ref/java/intfm/EOKeyValueCodingAdditions/takeValuesFromDictionary)
> : [valueForKeyPath](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOKeyValueCodingAdd.html#//apple_ref/java/intfm/EOKeyValueCodingAdditions/valueForKeyPath)
> : [valuesForKeys](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOKeyValueCodingAdd.html#//apple_ref/java/intfm/EOKeyValueCodingAdditions/valuesForKeys)
>
> [EORelationshipManipulation](EORelationshipManipulation.md#apple-infemqsfireei): [addObjectToBothSidesOfRelationshipWithKey](EORelationshipManipulation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkjswyylunfxw443infye2ylonfyhk3dboruw63rpmfsgit3cnjswg5cun5bg65diknuwizltj5tfezlmmf2gs33oonugs4cxnf2gqs3fpe)
> : [addObjectToPropertyWithKey](EORelationshipManipulation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkjswyylunfxw443infye2ylonfyhk3dboruw63rpmfsgit3cnjswg5cun5ihe33qmvzhi6kxnf2gqs3fpe)
> : [removeObjectFromBothSidesOfRelationshipWithKey](EORelationshipManipulation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkjswyylunfxw443infye2ylonfyhk3dboruw63rpojsw233wmvhwe2tfmn2em4tpnvbg65diknuwizltj5tfezlmmf2gs33oonugs4cxnf2gqs3fpe)
> : [removeObjectFromPropertyWithKey](EORelationshipManipulation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkjswyylunfxw443infye2ylonfyhk3dboruw63rpojsw233wmvhwe2tfmn2em4tpnvihe33qmvzhi6kxnf2gqs3fpe)
>
> [EOValidation](EOValidation.md#apple-infemqsfifcui): [validateForDelete](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zeizlmmv2gk)
> : [validateForInsert](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zes3ttmvzhi)
> : [validateForSave](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zfgylwmu)
> : [validateForUpdate](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zfk4demf2gk)
> : [validateValueForKey](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkwmfwhkzkgn5zewzlz)
>
> [EOFaulting](EOFaulting.md#apple-ijcuiq2gijdee): [clearFault](EOFaulting.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3dnrswc4sgmf2wy5a)
> : [faultHandler](EOFaulting.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3gmf2wy5cimfxgi3dfoi)
> : [isFault](EOFaulting.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3jondgc5lmoq)
> : [turnIntoFault](EOFaulting.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3uovzg4sloorxumylvnr2a)
> : [willRead](EOFaulting.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3xnfwgyutfmfsa)

## Method Types

---

> **Initializing enterprise
> objects**
> : [awakeFromFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvdgk5ddna)
> : [awakeFromInsertion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvew443foj2gs33o)
>
> **Announcing changes**
> : [willChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxo2lmnrbwqylom5sq)
>
> **Getting an object's
> EOEditingContext**
> : [editingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwkzdjoruw4z2dn5xhizlyoq)
>
> **Getting class description
> information**
> : [allPropertyKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc3dmkbzg64dfoj2hss3fpfzq)
> : [attributeKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc5duojuwe5lumvfwk6lt)
> : [classDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg3dbonzuizltmnzgs4dunfxw4)
> : [classDescriptionForDestinationKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg3dbonzuizltmnzgs4dunfxw4rtpojcgk43unfxgc5djn5xewzlz)
> : [deleteRuleForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwizlmmv2gkutvnrsum33skjswyylunfxw443infyewzlz)
> : [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk3tunf2hsttbnvsq)
> : [inverseForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxws3twmvzhgzkgn5zfezlmmf2gs33oonugs4clmv4q)
> : [isToManyKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxws42un5gwc3tzjnsxs)
> : [ownsDestinationObjectsForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxw653ooncgk43unfxgc5djn5xe6ytkmvrxi42gn5zfezlmmf2gs33oonugs4clmv4q)
> : [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y)
> : [toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32pnzsvezlmmf2gs33oonugs4clmv4xg)
>
> **Modifying relationships**
> : [propagateDeleteWithEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxa4tpobqwoylumvcgk3dforsvo2lunbcwi2lunfxgoq3pnz2gk6du)
> : [clearProperties](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg3dfmfzfa4tpobsxe5djmvzq)
>
> **Working with snapshots**
> : [snapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxg3tbobzwq33u)
> : [updateFromSnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxk4demf2gkrtsn5wvg3tbobzwq33u)
>
> **Merging values**
> : [changesFromSnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg2dbnztwk42gojxw2u3omfyhg2dpoq)
> : [reapplyChangesFromDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxezlbobygy6kdnbqw4z3fondhe33niruwg5djn5xgc4tz)
>
> **Invoking behavior on
> the server (com.apple.client.eocontrol only)**
> : [invokeRemoteMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxws3twn5vwkutfnvxxizknmv2gq33e)
>
> **Getting descriptions**
> : [eoDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32emvzwg4tjob2gs33o)
> : [eoShallowDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32tnbqwy3dpo5cgk43dojuxa5djn5xa)
> : [userPresentableDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxk43fojihezltmvxhiylcnrsuizltmnzgs4dunfxw4)

## Instance Methods

---

### allPropertyKeys

`public abstract NSArray allPropertyKeys()`

Returns all of the receiver's property keys. EOCustomObject's
implementation returns the union of the keys returned by [attributeKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc5duojuwe5lumvfwk6lt), [toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32pnzsvezlmmf2gs33oonugs4clmv4xg),
and [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y).

---

### attributeKeys

`public abstract NSArray attributeKeys()`

Returns the names of the receiver's attributes
(not relationship properties). EOCustomObject's implementation
simply invokes [attributeKeys](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwc5duojuwe5lumvfwk6lt) in the object's EOClassDescription
and returns the results. You might wish to override this method
to add keys for attributes not defined by the EOClassDescription.
The access layer's subclass of EOClassDescription, EOEntityClassDescription, returns
the names of attributes designated as class properties.

__See Also:__
[toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32pnzsvezlmmf2gs33oonugs4clmv4xg), [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y)

---

### awakeFromFetch

`public abstract void awakeFromFetch(EOEditingContext anEditingContext)`

Overridden by subclasses to perform additional
initialization on the receiver upon its being fetched from the external
repository into _anEditingContext._ EOCustomObject's
implementation merely sends an [awakeObjectFromFetch](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwc53bnnsu6ytkmvrxirtsn5wumzlumnua) to
the receiver's EOClassDescription. Subclasses should invoke `super`'s implementation
before performing their own initialization.

---

### awakeFromInsertion

`public abstract void awakeFromInsertion(EOEditingContext anEditingContext)`

Overridden by subclasses to perform additional
initialization on the receiver upon its being inserted into _anEditingContext._
This is commonly used to assign default values or record the time
of insertion. EOCustomObject's implementation merely sends an [awakeObjectFromInsertion](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwc53bnnsu6ytkmvrxirtsn5wus3ttmvzhi2lpny) to
the receiver's EOClassDescription. Subclasses should invoke `super`'s
implementation before performing their own initialization.

---

### changesFromSnapshot

`public abstract NSDictionary changesFromSnapshot(NSDictionary snapshot)`

Returns a dictionary whose keys correspond
to the receiver's properties with uncommitted changes relative
to _snapshot,_ and whose values are
the uncommitted values. In both _snapshot_ and
the returned dictionary, where a key represents a to-many relationship,
the corresponding value is an NSArray containing two other NSArrays:
the first is an array of objects to be added to the relationship
property, and the second is an array of objects to be removed.

__See Also:__
[reapplyChangesFromDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxezlbobygy6kdnbqw4z3fondhe33niruwg5djn5xgc4tz)

---

### classDescription

`public abstract EOClassDescription classDescription()`

Returns the EOClassDescription registered for
the receiver's class.EOCustomObject's implementation invokes
the EOClassDescription static method a [classDescriptionForClass](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rpmnwgc43tirsxgy3snfyhi2lpnzdg64sdnrqxg4y).

---

### classDescriptionForDestinationKey

`public abstract EOClassDescription classDescriptionForDestinationKey(String key)`

Returns the EOClassDescription for the destination
objects of the relationship identified by _key._ EOCustomObject's
implementation sends a [classDescriptionForDestinationKey](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwg3dbonzuizltmnzgs4dunfxw4rtpojcgk43unfxgc5djn5xewzlz) message
to the receiver's EOClassDescription.

---

### clearProperties

`public abstract void clearProperties()`

Sets all of the receiver's to-one and to-many
relationships to null. EOEditingContexts use this method to break
cyclic references among objects when they're finalized. EOCustomObject's
implementation should be sufficient for all purposes. If your enterprise
object maintains references to other objects and these references
are not to-one or to-many keys, then you should probably subclass
this method ensure unused objects can be finalized.

---

### deleteRuleForRelationshipKey

`public abstract int deleteRuleForRelationshipKey(String relationshipKey)`

Returns a rule indicating how to handle the
destination of the receiver's relationship named by _relationshipKey_ when
the receiver is deleted. The delete rule is one of:

- [DeleteRuleNullify](EOClassDescription.md#apple-ijaucq2ei5bek)
- [DeleteRuleCascade](EOClassDescription.md#apple-ijaucrccirbuo)
- [DeleteRuleDeny](EOClassDescription.md#apple-ijaucrchivdeo)
- [DeleteRuleNoAction](EOClassDescription.md#apple-ijaucrchjjfem)

For example, an Invoice object might return `DeleteRuleNullify` for
the relationship named "lineItems", since when an invoice is
deleted, its line items should be deleted as well. For more information
on the delete rules, see the method description for EOClassDescription's [deleteRuleForRelationshipKey](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwizlmmv2gkutvnrsum33skjswyylunfxw443infyewzlz) in
the class specification for EOClassDescription, the class in which
they're defined.

EOCustomObject's implementation of this method simply sends
a [deleteRuleForRelationshipKey](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwizlmmv2gkutvnrsum33skjswyylunfxw443infyewzlz) message
to the receiver's EOClassDescription.

__See Also:__
[propagateDeleteWithEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxa4tpobqwoylumvcgk3dforsvo2lunbcwi2lunfxgoq3pnz2gk6du), [validateForDelete](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zeizlmmv2gk) (EOValidation)

---

### editingContext

`public abstract EOEditingContext editingContext()`

Returns the EOEditingContext that holds the
receiver.

---

### entityName

`public abstract String entityName()`

Returns the name of the receiver's entity,
or null if it doesn't have one. EOCustomObject's implementation
simply sends an [entityName](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwk3tunf2hsttbnvsq) message to the receiver's
EOClassDescription.

---

### eoDescription

`public abstract String eoDescription()`

Returns a string that describes the receiver. EOCustomObject's
implementation returns a full description of the receiver's property
values by extracting them using the key-value coding methods. An
object referenced through relationships is listed with the results
of an [eoShallowDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32tnbqwy3dpo5cgk43dojuxa5djn5xa) message
(to avoid infinite recursion through cyclical relationships).

This method is useful for debugging. You can implement a `toString` method
that invokes this one, and the debugger's print-object command
(`po` on the command line) automatically
displays this description. You can also invoke this method directly
on the command line of the debugger.

__See Also:__
[userPresentableDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxk43fojihezltmvxhiylcnrsuizltmnzgs4dunfxw4)

---

### eoShallowDescription

`public abstract String eoShallowDescription()`

Similar to [eoDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32emvzwg4tjob2gs33o), but doesn't descend
into relationships. `eoDescription` invokes
this method for relationship destinations to avoid infinite recursion
through cyclical relationships. EOCustomObject's implementation
simply returns a string containing the receiver's class and entity
names.

__See Also:__
[userPresentableDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxk43fojihezltmvxhiylcnrsuizltmnzgs4dunfxw4)

---

### inverseForRelationshipKey

`public abstract String inverseForRelationshipKey(String relationshipKey)`

Returns the name of the relationship pointing
back to the receiver's class or entity from that named by _relationshipKey,_
or null if there isn't one. With the access layer's EOEntity
and EORelationship, for example, reciprocality is determined by
the join attributes of the two EORelationships. EOCustomObject's
implementation simply sends an [inverseForRelationshipKey](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxws3twmvzhgzkgn5zfezlmmf2gs33oonugs4clmv4q) message
to the receiver's EOClassDescription.

You might override this method for reciprocal relationships
that aren't defined using the same join attributes. For example,
if a Member object has a relationship to CreditCard based on the
card number, but a CreditCard has a relationship to Member based
on the Member's primary key, both classes need to override this
method. This is how Member might implement it:

> ```
> public String inverseForRelationshipKey(String relationshipKey) {
>     if (relationshipKey.equals("creditCard"))
>         return "member";
>     else
>         return super.inverseForRelationshipKey(relationshipKey);
> }
> ```

---

### invokeRemoteMethod

`public abstract Object invokeRemoteMethod(
String methodName,
Object[] arguments)`

(com.apple.client.eocontrol only) Invokes _methodName_ using _arguments._
To pass an enterprise object as an argument, use its global ID.
This method has the side effect of saving all the changes from the
receiver's editing context all the way down to the editing context
in the server session.

---

### isToManyKey

`public abstract boolean isToManyKey(String key)`

Returns true if the receiver has a to-many relationship
identified by _key,_ false otherwise. EOCustomObject's
implementation of this method simply checks its [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y) array for _key._

---

### ownsDestinationObjectsForRelationshipKey

`public abstract boolean ownsDestinationObjectsForRelationshipKey(String key)`

Returns true if the receiver has a relationship
identified by _key_ that owns its destination, false otherwise.
If an object owns the destination for a relationship, then when
that destination object is removed from the relationship, it's
automatically deleted. Ownership of a relationship thus contrasts with
a delete rule, in that the first applies when the destination is
removed and the second applies when the source is deleted. EOCustomObject's
implementation of this method simply sends an [ownsDestinationObjectsForRelationshipKey](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxw653ooncgk43unfxgc5djn5xe6ytkmvrxi42gn5zfezlmmf2gs33oonugs4clmv4q) message
to the receiver's EOClassDescription.

__See Also:__
[deleteRuleForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwizlmmv2gkutvnrsum33skjswyylunfxw443infyewzlz), `ownsDestination` (EOAccess'
EORelationship)

---

### propagateDeleteWithEditingContext

`public abstract void propagateDeleteWithEditingContext(EOEditingContext anEditingContext)`

Deletes the destination objects of the receiver's
relationships according to the delete rule for each relationship. EOCustomObject's
implementation simply sends a [propagateDeleteForObject](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxa4tpobqwoylumvcgk3dforsum33sj5rguzldoq) message
to the receiver's EOClassDescription. For more information on
delete rules, see the method description for [deleteRuleForRelationshipKey](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwizlmmv2gkutvnrsum33skjswyylunfxw443infyewzlz) in
the EOClassDescription class specification.

__See Also:__
[deleteRuleForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwizlmmv2gkutvnrsum33skjswyylunfxw443infyewzlz)

---

### reapplyChangesFromDictionary

`public abstract void reapplyChangesFromDictionary(NSDictionary changes)`

Similar to [takeValuesFromDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOKeyValueCodingAdd.html#//apple_ref/java/intfm/EOKeyValueCodingAdditions/takeValuesFromDictionary), but the _changes_ dictionary
can contain arrays for to-many relationships. Where a key represents
a to-many relationship, the dictionary's value is an NSArray containing
two other NSArrays: the first is an array of objects to be added
to the relationship property, and the second is an array of objects
to be removed. EOCustomObject's implementation should be sufficient
for all purposes; you shouldn't have to override this method.

__See Also:__
[changesFromSnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg2dbnztwk42gojxw2u3omfyhg2dpoq)

---

### snapshot

`public abstract NSDictionary snapshot()`

Returns a dictionary whose keys are those of
the receiver's attributes, to-one relationships, and to-many relationships,
and whose values are the values of those properties, with EONullValue substituted
for null. For to-many relationships, the dictionary contains shallow
copies of the arrays. EOCustomObject's implementation should be
sufficient for all purposes; you shouldn't have to override this
method.

__See Also:__
[updateFromSnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxk4demf2gkrtsn5wvg3tbobzwq33u)

---

### toManyRelationshipKeys

`public abstract NSArray toManyRelationshipKeys()`

Returns the names of the receiver's to-many
relationships. EOCustomObject's implementation simply invokes [toManyRelationshipKeys](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y) in
the object's EOClassDescription and returns the results. You might wish
to override this method to add keys for relationships not defined
by the EOClassDescription, but it's rarely necessary: The access
layer's subclass of EOClassDescription, EOEntityClassDescription, returns
the names of to-many relationships designated as class properties.

__See Also:__
[attributeKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc5duojuwe5lumvfwk6lt), [toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32pnzsvezlmmf2gs33oonugs4clmv4xg)

---

### toOneRelationshipKeys

`public abstract NSArray toOneRelationshipKeys()`

Returns the names of the receiver's to-one
relationships. EOCustomObject's implementation simply invokes [toOneRelationshipKeys](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxi32pnzsvezlmmf2gs33oonugs4clmv4xg) in
the object's EOClassDescription and returns the results. You might wish
to override this method to add keys for relationships not defined
by the EOClassDescription, but it's rarely necessary: The access
layer's subclass of EOClassDescription, EOEntityClassDescription, returns
the names of to-one relationships designated as class properties.

__See Also:__
[attributeKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc5duojuwe5lumvfwk6lt), [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y)

---

### updateFromSnapshot

`public abstract void updateFromSnapshot(NSDictionary aSnapshot)`

Takes the values from _aSnapshot,_
and sets the receiver's properties to them. EOCustomObject's implementation
sets each one using [takeStoredValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzktorxxezlekzqwy5lfizxxes3fpe). In the process, EONullValues are converted
to null, and array values are set as shallow mutable copies.

__See Also:__
[snapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxg3tbobzwq33u)

---

### userPresentableDescription

`public abstract String userPresentableDescription()`

Returns a short (no longer than 60 characters)
description of an enterprise object based on its data. EOCustomObject's
implementation enumerates the object's [attributeKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc5duojuwe5lumvfwk6lt) and returns the values
of all of its properties, separated by commas (applying the default
formatter for numbers and dates).

__See Also:__
[eoDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32emvzwg4tjob2gs33o), [eoShallowDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32tnbqwy3dpo5cgk43dojuxa5djn5xa)

---

### willChange

`public abstract void willChange()`

Notifies any observers that the receiver's
state is about to change, by sending each an [objectWillChange](EOObserving.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpj5rhgzlsozuw4zzpn5rguzldorlws3dminugc3thmu) message
(see the [EOObserverCenter](EOObserverCenter.md#apple-ivhu6yttmvzhmzlsinsw45dfoi) class specification
for more information). A subclass should not override this method,
but should invoke it prior to altering the subclass's state, most
typically in "set" methods such as the following:
> ```
> public void setRoleName(String value) {
>     willChange();
>     roleName = value;
> }
> ```

In com.apple.client.eocontrol, this method invokes [willRead](EOFaulting.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3xnfwgyutfmfsa).

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
