---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOCustomObject.html
archived_at: '2026-07-15T08:11:37.400422Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOCustomObject

> **__Inherits
> from:__**
> : (com.apple.client.eocontrol) Object
> (com.apple.yellow.eocontrol) NSObject

> **__Implements:__**
> : EOEnterpriseObject
> : EODeferredFaulting (EOEnterpriseObject)
> : EOKeyValueCodingAdditions (EOEnterpriseObject)
> : EOKeyValueCoding.KeyBindingCreation (EOEnterpriseObject)
> : EORelationshipManipulation (EOEnterpriseObject)
> : EOValidation (EOEnterpriseObject)
> : EOFaulting (EODeferredFaulting)
> : EOKeyValueCoding (EOKeyValueCodingAdditions)
> : (com.apple.client.eocontrol only) NSKeyValueCoding (EOKeyValueCoding)
> : (com.apple.client.eocontrol only) NSInlineObservable

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Class Description

---

The EOCustomObject class provides a default implementation
of the EOEnterpriseObject interface. If you need to create a custom
enterprise object class, you can subclass EOCustomObject and inherit
the Framework's default implementations. Some of the methods are
for subclasses to implement or override, but most are meant to be
used as defined by EOCustomObject. For information on which methods
you should implement in your subclass, see the [EOEnterpriseObject](EOEnterpriseObject.md#apple-ijaueqsdjbfeq) interface
specification.

EOCustomObject's method implementations are described in
the specification for the interface that declares them. For example,
you can find a description of how EOCustomObject implements [valueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) (introduced in the EOKeyValueCoding
interface) in the specification for EOKeyValueCoding, and you can
find a description of how EOCustomObject implements [classDescription](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg3dbonzuizltmnzgs4dunfxw4) (introduced in the
EOEnterpriseObject interface) in the specification for EOEnterpriseObject.

The only methods provided in EOCustomObject that aren't
defined in the EOEnterpriseObject interface are the following three
static methods:

- [accessInstanceVariablesDirectly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3von2g63kpmjvgky3uf5qwgy3fonzus3ttorqw4y3fkzqxe2lbmjwgk42enfzgky3unr4q)
- [flushAllKeyBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3von2g63kpmjvgky3uf5tgy5ltnbawy3clmv4ue2lomruw4z3t)
- [useStoredAccessor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3von2g63kpmjvgky3uf52xgzktorxxezleifrwgzltonxxe)

You would never invoke these methods, rather, they are provided
in EOCustomObject to demonstrate the additional API your custom
enterprise objects can implement. Similarly, EOCustomObject's constructors
are not meant to be invoked; you would never create an instance
of EOCustomObject. Rather, EOCustomObject provides the constructors
to demonstrate the constructors your custom enterprise objects should
implement.

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
> EOEnterpriseObject: [allPropertyKeys](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc3dmkbzg64dfoj2hss3fpfzq)
> : [attributeKeys](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc5duojuwe5lumvfwk6lt)
> : [awakeFromFetch](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvdgk5ddna)
> : [awakeFromInsertion](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvew443foj2gs33o)
> : [changesFromSnapshot](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg2dbnztwk42gojxw2u3omfyhg2dpoq) (com.apple.yellow.eocontrol only)
> : [classDescription](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg3dbonzuizltmnzgs4dunfxw4)
> : [classDescriptionForDestinationKey](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg3dbonzuizltmnzgs4dunfxw4rtpojcgk43unfxgc5djn5xewzlz)
> : [clearProperties](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg3dfmfzfa4tpobsxe5djmvzq)
> : [deleteRuleForRelationshipKey](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwizlmmv2gkutvnrsum33skjswyylunfxw443infyewzlz)
> : [editingContext](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwkzdjoruw4z2dn5xhizlyoq)
> : [entityName](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk3tunf2hsttbnvsq)
> : [eoDescription](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32emvzwg4tjob2gs33o)
> : [eoShallowDescription](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32tnbqwy3dpo5cgk43dojuxa5djn5xa)
> : [inverseForRelationshipKey](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxws3twmvzhgzkgn5zfezlmmf2gs33oonugs4clmv4q)
> : [invokeRemoteMethod](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxws3twn5vwkutfnvxxizknmv2gq33e) (com.apple.client.eocontrol only)
> : [isToManyKey](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxws42un5gwc3tzjnsxs)
> : [ownsDestinationObjectsForRelationshipKey](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxw653ooncgk43unfxgc5djn5xe6ytkmvrxi42gn5zfezlmmf2gs33oonugs4clmv4q)
> : [propagateDeleteWithEditingContext](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxa4tpobqwoylumvcgk3dforsvo2lunbcwi2lunfxgoq3pnz2gk6du)
> : [reapplyChangesFromDictionary](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxezlbobygy6kdnbqw4z3fondhe33niruwg5djn5xgc4tz)
> : [snapshot](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxg3tbobzwq33u)
> : [toManyRelationshipKeys](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y)
> : [toOneRelationshipKeys](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32pnzsvezlmmf2gs33oonugs4clmv4xg)
> : [updateFromSnapshot](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxk4demf2gkrtsn5wvg3tbobzwq33u)
> : [userPresentableDescription](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxk43fojihezltmvxhiylcnrsuizltmnzgs4dunfxw4) (com.apple.yellow.eocontrol only)
> : [willChange](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxo2lmnrbwqylom5sq)
>
> [EOFaulting](EOFaulting.md#apple-ijcuiq2gijdee): [clearFault](EOFaulting.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3dnrswc4sgmf2wy5a)
> : [faultHandler](EOFaulting.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3gmf2wy5cimfxgi3dfoi)
> : [isFault](EOFaulting.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3jondgc5lmoq)
> : [turnIntoFault](EOFaulting.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3uovzg4sloorxumylvnr2a)
> : [willRead](EOFaulting.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3xnfwgyutfmfsa)
>
> NSInlineObservable
> (com.apple.client.eocontrol only): `observerData`
> : `setObserverData`

## Constructors

---

### `EOCustomObject`

`public EOCustomObject(
EOEditingContext anEOEditingContext,
EOClassDescription anEOClassDescription,
EOGlobalID anEOGlobalID)`

You would never create an instance of EOCustomObject;
rather, your subclasses can create constructors of this same form.
A subclass's constructors should create a new object and initialize
it with the arguments provided.

__See Also:__  [createInstanceWithEditingContext](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwg4tfmf2gksloon2gc3tdmvlws5diivsgs5djnztug33oorsxq5a) (EOClassDescription)

---

## Static Methods

---

### accessInstanceVariablesDirectly

`public static boolean accessInstanceVariablesDirectly()`

Subclasses implement this method to return `false` if
the key-value coding methods should never access the corresponding
instance variable directly on finding no accessor method for a property.
You don't have to implement this method if the default behavior
of accessing instance variables directly is correct for your objects.

__See
Also:__  [valueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe), [takeValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz)

---

### flushAllKeyBindings

`public static void flushAllKeyBindings()`

Invalidates the cached key binding information
for all classes (caches are kept of key-to-method or instance variable
bindings in order to make key-value coding efficient). This method
should be invoked whenever a class is modified in or removed from
the run-time system.

__See Also:__

---

### useStoredAccessor

`public static boolean useStoredAccessor()`

Subclasses implement this method to return `false` if
the stored value methods ( [storedValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpon2g64tfmrlgc3dvmvdg64slmv4q) and [takeStoredValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzktorxxezlekzqwy5lfizxxes3fpe)) should not
use private accessor methods in preference to public accessors. Returning `false` causes
the stored value methods to use the same accessor method-instance
variable search order as the corresponding basic key-value coding
methods ( [valueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) and [takeValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz)). You don't have
to implement this method if the default stored value search order
is correct for your objects.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
