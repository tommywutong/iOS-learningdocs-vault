---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOEnterpriseObject.html
archived_at: '2026-07-15T08:11:42.959896Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOEnterpriseObject

> __(informal protocol)__

> __Declared in:__ : EOControl/EOClassDescription.h
> : EOControl/EOEditingContext.h
> : EOControl/EOKeyValueCoding.h
> : EOControl/EOObserver.h

---

## Protocol Description

---

The EOEnterpriseObject informal protocol identifies basic
enterprise object behavior, defining methods for supporting operations
common to all enterprise objects. Among these are methods for initializing instances,
announcing changes, setting and retrieving property values, and
performing validation of state. Some of these methods are for enterprise
objects to implement or override, and some are meant to be used
as defined by the Framework. Many methods are used internally by
the Framework and rarely invoked by application code.

Many of the functional areas are defined in smaller, more
specialized informal protocols and incorporated in the over arching
EOEnterpriseObject informal protocol:

- [EOKeyValueCoding](EOKeyValueCoding-3.md#apple-ineucq2iizduu) defines
  Enterprise Objects Framework's main data transport mechanism,
  in which the properties of an object are accessed indirectly by
  name (or "key"), rather than directly through invocation of
  an accessor method or as instance variables.
- EOKeyBindingCreation defines a mechanism for binding class/key
  pairs with a method for accessing the key, which maximizes the performance
  of EOKeyValueCoding.
- [EOKeyValueCodingAdditions](EOKeyValueCodingAdditions.md#apple-inbemrcbjfauc) defines
  extensions to the basic EOKeyValueCoding informal protocol, giving
  access to groups of properties and to properties across relationships.
- [EORelationshipManipulation](EORelationshipManipulation-2.md#apple-infemqsfireei) builds
  on the basic EOKeyValueCoding informal protocol to allow you to
  modify to-many relationship properties.
- [EOValidation](EOValidation-3.md#apple-infemqsfifcui) defines
  the way that enterprise objects validate their values.

The remaining methods are introduced in the EOEnterpriseObject informal
protocol itself and can be broken down into three functional groups
discussed in the following sections:

- ["Initialization"](EOEnterpriseObject-4.md#apple-ijaueq2iizcem)
- ["Change Notification"](EOEnterpriseObject-4.md#apple-ijaueqsijbauu)
- ["Object and Class Metadata Access"](EOEnterpriseObject-4.md#apple-ijauerccjbaui)
- ["Snapshots"](EOEnterpriseObject-4.md#apple-ijauercbijauc)

You rarely need to implement the EOEnterpriseObject informal
protocol from scratch. The Framework provides default implementations
of the methods in categories on NSObject. Use EOGenericRecords to represent
enterprise objects that don't require custom behavior, and create
subclasses of NSObject to represent enterprise objects that do.
The section ["Writing an Enterprise Object Class"](EOEnterpriseObject-4.md#apple-ijaueqsijjfeg) highlights
the methods that you typically provide or override in a custom enterprise
object class.

## Adopted Protocols

---

> [EOKeyValueCoding](EOKeyValueCoding-3.md#apple-ineucq2iizduu): [+ accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/accessInstanceVariablesDirectly)
> : [+ flushAllKeyBindings](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/flushAllKeyBindings)
> : [+ useStoredAccessor](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/useStoredAccessor)
> : [- handleQueryWithUnboundKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkf2wk4tzk5uxi2cvnzrg65lomrfwk6j2)
> : [- handleTakeValue:forUnboundKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkrqwwzkwmfwhkzj2mzxxevlomjxxk3tejnsxsoq)
> : [- storedValueForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3torxxezlekzqwy5lfizxxes3fpe5a)
> : [- takeStoredValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwku3un5zgkzcwmfwhkzj2mzxxes3fpe5a)
> : [- takeValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi)
> : [- unableToSetNullForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3vnzqwe3dfkrxvgzlujz2wy3cgn5zewzlzhi)
> : [- valueForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi)
>
> [EOKeyValueCodingAdditions](EOKeyValueCodingAdditions.md#apple-inbemrcbjfauc): [- takeValue:forKeyPath:](EOKeyValueCodingAdditions.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgoqlemruxi2lpnzzs65dbnnsvmylmovstuztpojfwk6kqmf2gqoq)
> : [- takeValuesFromDictionary:](EOKeyValueCodingAdditions.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgoqlemruxi2lpnzzs65dbnnsvmylmovsxgrtsn5wui2ldoruw63tboj4tu)
> : [- valueForKeyPath:](EOKeyValueCodingAdditions.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgoqlemruxi2lpnzzs65tbnr2wkrtpojfwk6kqmf2gqoq)
> : [- valuesForKeys:](EOKeyValueCodingAdditions.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgoqlemruxi2lpnzzs65tbnr2wk42gn5zewzlzom5a)
>
> [EORelationshipManipulation](EORelationshipManipulation-2.md#apple-infemqsfireei): [- addObject:toBothSidesOfRelationshipWithKey:](EORelationshipManipulation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2smvwgc5djn5xhg2djobgwc3tjob2wyylunfxw4l3bmrse6ytkmvrxiotun5bg65diknuwizltj5tfezlmmf2gs33oonugs4cxnf2gqs3fpe5a)
> : [- addObject:toPropertyWithKey:](EORelationshipManipulation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2smvwgc5djn5xhg2djobgwc3tjob2wyylunfxw4l3bmrse6ytkmvrxiotun5ihe33qmvzhi6kxnf2gqs3fpe5a)
> : [- removeObject:fromBothSidesOfRelationshipWithKey:](EORelationshipManipulation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2smvwgc5djn5xhg2djobgwc3tjob2wyylunfxw4l3smvww65tfj5rguzldoq5gm4tpnvbg65diknuwizltj5tfezlmmf2gs33oonugs4cxnf2gqs3fpe5a)
> : [- removeObject:fromPropertyWithKey:](EORelationshipManipulation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2smvwgc5djn5xhg2djobgwc3tjob2wyylunfxw4l3smvww65tfj5rguzldoq5gm4tpnvihe33qmvzhi6kxnf2gqs3fpe5a)
>
> [EOValidation](EOValidation-3.md#apple-infemqsfifcui): [- validateForDelete](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojcgk3dforsq)
> : [- validateForInsert](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojew443foj2a)
> : [- validateForSave](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojjwc5tf)
> : [- validateForUpdate](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojkxazdborsq)
> : [- validateValue:forKey:](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkvtbnr2wkotgn5zewzlzhi)

## Method Types

---

> **Initializing enterprise
> objects**
> : [- initWithEditingContext:classDescription:globalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5uw42luk5uxi2cfmruxi2lom5bw63tumv4hiotdnrqxg42emvzwg4tjob2gs33ohjtwy33cmfwesrb2)
> : [- awakeFromFetchInEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxoyllmvdhe33nizsxiy3ijfxekzdjoruw4z2dn5xhizlyoq5a)
> : [- awakeFromInsertionInEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxoyllmvdhe33njfxhgzlsoruw63sjnzcwi2lunfxgoq3pnz2gk6duhi)
>
> **Announcing changes**
> : [- willChange](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf53ws3dminugc3thmu)
>
> **Getting an object's
> EOEditingContext**
> : [- editingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5swi2lunfxgoq3pnz2gk6du)
>
> **Getting class description
> information**
> : [- allPropertyKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qwy3cqojxxazlsor4uwzlzom)
> : [- attributeKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxi5dsnfrhk5dfjnsxs4y)
> : [- classDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5rwyyltoncgk43dojuxa5djn5xa)
> : [- classDescriptionForDestinationKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5rwyyltoncgk43dojuxa5djn5xem33sirsxg5djnzqxi2lpnzfwk6j2)
> : [- deleteRuleForRelationshipKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5sgk3dforsve5lmmvdg64ssmvwgc5djn5xhg2djobfwk6j2)
> : [- entityName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5sw45djor4u4ylnmu)
> : [- inverseForRelationshipKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5uw45tfojzwkrtpojjgk3dboruw63ttnbuxas3fpe5a)
> : [- isToManyKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5uxgvdpjvqw46klmv4tu)
> : [- ownsDestinationObjectsForRelationshipKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5xxo3ttirsxg5djnzqxi2lpnzhwe2tfmn2hgrtpojjgk3dboruw63ttnbuxas3fpe5a)
> : [- toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52g6tlbnz4vezlmmf2gs33oonugs4clmv4xg)
> : [- toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52g6t3omvjgk3dboruw63ttnbuxas3fpfzq)
>
> **Modifying relationships**
> : [- propagateDeleteWithEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5yhe33qmftwc5dfirswyzlumvlws5diivsgs5djnztug33oorsxq5b2)
> : [- clearProperties](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5rwyzlbojihe33qmvzhi2lfom)
>
> **Working with snapshots**
> : [- snapshot](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5zw4ylqonug65a)
> : [- updateFromSnapshot:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52xazdborsum4tpnvjw4ylqonug65b2)
>
> **Merging values**
> : [- changesFromSnapshot](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5rwqylom5sxgrtsn5wvg3tbobzwq33u)
> : [- reapplyChangesFromDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5zgkylqobwhsq3imfxgozltizzg63kenfrxi2lpnzqxe6j2)
>
> **Getting descriptions**
> : [- eoDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5sw6rdfonrxe2lqoruw63q)
> : [- eoShallowDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5sw6u3imfwgy33xirsxgy3snfyhi2lpny)
> : [- userPresentableDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52xgzlskbzgk43fnz2gcytmmvcgk43dojuxa5djn5xa)

## Instance Methods

---

### allPropertyKeys

`- (NSArray *)allPropertyKeys`

Returns all of the receiver's property keys. NSObject's
implementation returns the union of the keys returned by [attributeKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxi5dsnfrhk5dfjnsxs4y), [toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52g6t3omvjgk3dboruw63ttnbuxas3fpfzq),
and [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52g6tlbnz4vezlmmf2gs33oonugs4clmv4xg).

---

### attributeKeys

`- (NSArray *)attributeKeys`

Returns the names of the receiver's attributes
(not relationship properties). NSObject's implementation simply
invokes [attributeKeys](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5qxi5dsnfrhk5dfjnsxs4y) in the object's EOClassDescription
and returns the results. You might wish to override this method
to add keys for attributes not defined by the EOClassDescription.
The access layer's subclass of EOClassDescription, EOEntityClassDescription,
returns the names of attributes designated as class properties.

__See Also:__
[- toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52g6t3omvjgk3dboruw63ttnbuxas3fpfzq), [- toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52g6tlbnz4vezlmmf2gs33oonugs4clmv4xg)

---

### awakeFromFetchInEditingContext:

`- (void)awakeFromFetchInEditingContext:(EOEditingContext
*)anEditingContext`

Overridden by subclasses to perform additional
initialization on the receiver upon its being fetched from the external
repository into _anEditingContext_. NSObject's
implementation merely sends an [awakeObject:fromFetchInEditingContext:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5qxoyllmvhwe2tfmn2duztsn5wumzlumnues3sfmruxi2lom5bw63tumv4hioq) to
the receiver's EOClassDescription. Subclasses should invoke __super__'s
implementation before performing their own initialization.

---

### awakeFromInsertionInEditingContext:

`- (void)awakeFromInsertionInEditingContext:(EOEditingContext
*)anEditingContext`

Overridden by subclasses to perform additional
initialization on the receiver upon its being inserted into _anEditingContext_.
This is commonly used to assign default values or record the time
of insertion. NSObject's implementation merely sends an [awakeObject:fromInsertionInEditingContext:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5qxoyllmvhwe2tfmn2duztsn5wus3ttmvzhi2lpnzew4rlenf2gs3thinxw45dfpb2du) to
the receiver's EOClassDescription. Subclasses should invoke __super__'s
implementation before performing their own initialization.

---

### changesFromSnapshot

`- (NSDictionary *)changesFromSnapshot:(NSDictionary
*)snapshot`

Returns a dictionary whose keys correspond
to the receiver's properties with uncommitted changes relative
to _snapshot_, and whose values are
the uncommitted values. In both _snapshot_ and
the returned dictionary, where a key represents a to-many relationship,
the corresponding value is an NSArray containing two other NSArrays:
the first is an array of objects to be added to the relationship
property, and the second is an array of objects to be removed.

__See Also:__
[- reapplyChangesFromDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5zgkylqobwhsq3imfxgozltizzg63kenfrxi2lpnzqxe6j2)

---

### classDescription

`- (EOClassDescription *)classDescription`

Returns the EOClassDescription registered for
the receiver's class.NSObject's implementation invokes the EOClassDescription class method
a [classDescriptionForClass:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3dnrqxg42emvzwg4tjob2gs33oizxxeq3mmfzxgoq).

---

### classDescriptionForDestinationKey:

`- (EOClassDescription *)classDescriptionForDestinationKey:(NSString
*)key`

Returns the EOClassDescription for the destination
objects of the relationship identified by _key_. NSObject's
implementation sends a [classDescriptionForDestinationKey:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5rwyyltoncgk43dojuxa5djn5xem33sirsxg5djnzqxi2lpnzfwk6j2) message
to the receiver's EOClassDescription.

---

### clearProperties

`- (void)clearProperties`

Sets all of the receiver's to-one and to-many
relationships to nil. EOEditingContexts use this method to break
cyclic references among objects when they're deallocated. NSObject's
implementation should be sufficient for all purposes. If your enterprise
object maintains references to other objects and these references
are not to-one or to-many keys, then you should probably subclass
this method ensure unused objects can be deallocated.

---

### deleteRuleForRelationshipKey:

`- (EODeleteRule)deleteRuleForRelationshipKey:(NSString
*)relationshipKey`

Returns a rule indicating how to handle the
destination of the receiver's relationship named by _relationshipKey_ when
the receiver is deleted. The delete rule is one of:

- [EODeleteRuleNullify](EOClassDescription-3.md#apple-ijaucq2ei5bek)
- [EODeleteRuleCascade](EOClassDescription-3.md#apple-ijaucrccirbuo)
- [EODeleteRuleDeny](EOClassDescription-3.md#apple-ijaucrchivdeo)
- [EODeleteRuleNoAction](EOClassDescription-3.md#apple-ijaucrchjjfem)

For example, an Invoice object might return `EODeleteRuleNullify` for
the relationship named "lineItems", since when an invoice is
deleted, its line items should be deleted as well. For more information
on the delete rules, see the method description for EOClassDescription's [deleteRuleForRelationshipKey:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5sgk3dforsve5lmmvdg64ssmvwgc5djn5xhg2djobfwk6j2) in
the class specification for EOClassDescription.

NSObject's implementation of this method simply sends a [deleteRuleForRelationshipKey:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5sgk3dforsve5lmmvdg64ssmvwgc5djn5xhg2djobfwk6j2) message
to the receiver's EOClassDescription.

__See Also:__
[- propagateDeleteWithEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5yhe33qmftwc5dfirswyzlumvlws5diivsgs5djnztug33oorsxq5b2), [- validateForDelete](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojcgk3dforsq) (EOValidation)

---

### editingContext

`- (EOEditingContext *)editingContext`

Returns the EOEditingContext that holds the
receiver.

---

### entityName

`- (NSString *)entityName`

Returns the name of the receiver's entity,
or nil if it doesn't have one. NSObject's implementation simply
sends an [entityName](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5sw45djor4u4ylnmu) message to the receiver's
EOClassDescription.

---

### eoDescription

`- (NSString *)eoDescription`

Returns a string that describes the receiver. NSObject's
implementation returns a full description of the receiver's property
values by extracting them using the key-value coding methods. An
object referenced through relationships is listed with the results
of an [eoShallowDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5sw6u3imfwgy33xirsxgy3snfyhi2lpny) message
(to avoid infinite recursion through cyclical relationships).

This method is useful for debugging. You can implement a __description__ method
that invokes this one, and the debugger's print-object command
(__po__ on the command line) automatically
displays this description. You can also invoke this method directly
on the command line of the debugger.

__See Also:__
[- userPresentableDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52xgzlskbzgk43fnz2gcytmmvcgk43dojuxa5djn5xa)

---

### eoShallowDescription

`- (NSString *)eoShallowDescription`

Similar to [eoDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5sw6rdfonrxe2lqoruw63q), but doesn't descend
into relationships. __eoDescription__ invokes
this method for relationship destinations to avoid infinite recursion
through cyclical relationships. NSObject's implementation simply
returns a string containing the receiver's class and entity names,
along with the memory address of its `id`.

__See Also:__
[- userPresentableDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52xgzlskbzgk43fnz2gcytmmvcgk43dojuxa5djn5xa)

---

### initWithEditingContext:classDescription:globalID:

`- initWithEditingContext:(EOEditingContext
*)anEditingContext classDescription:(EOClassDescription
*)aClassDescription
globalID:(EOGlobalID *)globalID`

Initializes the receiver with the arguments
provided. NSObject's implementation simply invokes __init__, and
ignores _anEditingContext_.

__See Also:__
[- createInstanceWithEditingContext:globalID:zone:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5rxezlborsus3ttorqw4y3fk5uxi2cfmruxi2lom5bw63tumv4hiothnrxweylmjfcdu6tpnzstu) (EOClassDescription)

---

### inverseForRelationshipKey:

`- (NSString *)inverseForRelationshipKey:(NSString
*)relationshipKey`

Returns the name of the relationship pointing
back to the receiver's class or entity from that named by _relationshipKey_,
or nil if there isn't one. With the access layer's EOEntity
and EORelationship, for example, reciprocality is determined by
the join attributes of the two EORelationships. NSObject's implementation
simply sends an [inverseForRelationshipKey:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5uw45tfojzwkrtpojjgk3dboruw63ttnbuxas3fpe5a) message
to the receiver's EOClassDescription.

You might override this method for reciprocal relationships
that aren't defined using the same join attributes. For example,
if a Member object has a relationship to CreditCard based on the
card number, but a CreditCard has a relationship to Member based
on the Member's primary key, both classes need to override this
method. This is how Member might implement it:

> ```
> - (NSString *)inverseForRelationshipKey:(NSString *)relationshipKey
> {
>     if ([relationshipKey isEqual:@"creditCard"]) return @"member";
>     return [super inverseForRelationshipKey:relationshipKey];
> }
> ```

---

### isToManyKey:

`- (BOOL)isToManyKey:(NSString
*)key`

Returns YES if the receiver has a to-many relationship
identified by _key_, NO otherwise. NSObject's implementation
of this method simply checks its [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52g6tlbnz4vezlmmf2gs33oonugs4clmv4xg) array for _key_.

---

### ownsDestinationObjectsForRelationshipKey:

`- (BOOL)ownsDestinationObjectsForRelationshipKey:(NSString
*)key`

Returns YES if the receiver has a relationship
identified by _key_ that owns its destination, NO otherwise.
If an object owns the destination for a relationship, then when
that destination object is removed from the relationship, it's
automatically deleted. Ownership of a relationship thus contrasts
with a delete rule, in that the first applies when the destination
is removed and the second applies when the source is deleted. NSObject's
implementation of this method simply sends an [ownsDestinationObjectsForRelationshipKey:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5xxo3ttirsxg5djnzqxi2lpnzhwe2tfmn2hgrtpojjgk3dboruw63ttnbuxas3fpe5a) message
to the receiver's EOClassDescription.

__See Also:__
[- deleteRuleForRelationshipKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5sgk3dforsve5lmmvdg64ssmvwgc5djn5xhg2djobfwk6j2), __- ownsDestination__ (EOAccess'
EORelationship)

---

### propagateDeleteWithEditingContext:

`- (void)propagateDeleteWithEditingContext:(EOEditingContext
*)anEditingContext`

Deletes the destination objects of the receiver's
relationships according to the delete rule for each relationship. NSObject's
implementation simply sends a [propagateDeleteForObject:editingContext:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5yhe33qmftwc5dfirswyzlumvdg64spmjvgky3uhjswi2lunfxgoq3pnz2gk6duhi) message
to the receiver's EOClassDescription. For more information on
delete rules, see the method description for [deleteRuleForRelationshipKey:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5sgk3dforsve5lmmvdg64ssmvwgc5djn5xhg2djobfwk6j2) in
the EOClassDescription class specification.

__See Also:__
[- deleteRuleForRelationshipKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5sgk3dforsve5lmmvdg64ssmvwgc5djn5xhg2djobfwk6j2)

---

### reapplyChangesFromDictionary:

`- (void)reapplyChangesFromDictionary:(NSDictionary
*)changes`

Similar to [takeValuesFromDictionary:](EOKeyValueCodingAdditions.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgoqlemruxi2lpnzzs65dbnnsvmylmovsxgrtsn5wui2ldoruw63tboj4tu), but the _changes_ dictionary
can contain arrays for to-many relationships. Where a key represents
a to-many relationship, the dictionary's value is an NSArray containing
two other NSArrays: the first is an array of objects to be added
to the relationship property, and the second is an array of objects
to be removed. NSObject's implementation should be sufficient
for all purposes; you shouldn't have to override this method.

__See Also:__
[- changesFromSnapshot](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5rwqylom5sxgrtsn5wvg3tbobzwq33u)

---

### snapshot

`- (NSDictionary *)snapshot`

Returns a dictionary whose keys are those of
the receiver's attributes, to-one relationships, and to-many relationships,
and whose values are the values of those properties, with EONull substituted
for nil. For to-many relationships, the dictionary contains shallow
copies of the arrays to preserve the ids of the contents. NSObject's
implementation should be sufficient for all purposes; you shouldn't
have to override this method.

__See Also:__
[- updateFromSnapshot:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52xazdborsum4tpnvjw4ylqonug65b2)

---

### toManyRelationshipKeys

`- (NSArray *)toManyRelationshipKeys`

Returns the names of the receiver's to-many
relationships. NSObject's implementation simply invokes [toManyRelationshipKeys](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of52g6tlbnz4vezlmmf2gs33oonugs4clmv4xg) in
the object's EOClassDescription and returns the results. You might
wish to override this method to add keys for relationships not defined
by the EOClassDescription, but it's rarely necessary: The access
layer's subclass of EOClassDescription, EOEntityClassDescription,
returns the names of to-many relationships designated as class properties.

__See Also:__
[- attributeKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxi5dsnfrhk5dfjnsxs4y), [- toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52g6t3omvjgk3dboruw63ttnbuxas3fpfzq)

---

### toOneRelationshipKeys

`- (NSArray *)toOneRelationshipKeys`

Returns the names of the receiver's to-one
relationships. NSObject's implementation simply invokes [toOneRelationshipKeys](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of52g6t3omvjgk3dboruw63ttnbuxas3fpfzq) in
the object's EOClassDescription and returns the results. You might
wish to override this method to add keys for relationships not defined
by the EOClassDescription, but it's rarely necessary: The access
layer's subclass of EOClassDescription, EOEntityClassDescription,
returns the names of to-one relationships designated as class properties.

__See Also:__
[- attributeKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxi5dsnfrhk5dfjnsxs4y), [- toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52g6tlbnz4vezlmmf2gs33oonugs4clmv4xg)

---

### updateFromSnapshot:

`- (void)updateFromSnapshot:(NSDictionary
*)aSnapshot`

Takes the values from _aSnapshot_,
and sets the receiver's properties to them. NSObject's implementation sets
each one using [takeStoredValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwku3un5zgkzcwmfwhkzj2mzxxes3fpe5a). In the process, EONull
values are converted to nil, and array values are set as shallow
mutable copies to preserve the ids of the contents.

__See Also:__
[- snapshot](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5zw4ylqonug65a)

---

### userPresentableDescription

`- (NSString *)userPresentableDescription`

Returns a short (no longer than 60 characters)
description of an enterprise object based on its data. NSObject's
implementation enumerates the object's [attributeKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxi5dsnfrhk5dfjnsxs4y) and returns the values
of all of its properties, separated by commas (applying the default
formatter for numbers and dates).

__See Also:__
[- eoDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5sw6rdfonrxe2lqoruw63q), [- eoShallowDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5sw6u3imfwgy33xirsxgy3snfyhi2lpny)

---

### willChange

`- (void)willChange`

Notifies any observers that the receiver's
state is about to change, by sending each an [objectWillChange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOObserving.html#//apple_ref/occ/intfm/EOObserving/objectWillChange:) message
(see the [EOObserverCenter](EOObserverCenter-2.md#apple-ivhu6yttmvzhmzlsinsw45dfoi) class specification
for more information). A subclass should not override this method,
but should invoke it prior to altering the subclass's state, most
typically in "set" methods such as the following:
> ```
> - (void)setRoleName:(NSString *)value {
>     [self willChange];
>     [roleName autorelease];
>     roleName = [value retain];
> }
> ```

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
