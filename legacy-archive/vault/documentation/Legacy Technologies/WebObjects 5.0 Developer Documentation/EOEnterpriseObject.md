---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/EOEnterpriseObject.html
archived_at: '2026-07-15T08:13:47.895949Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOEnterpriseObject

> __(informal interface)__
>
> __Implemented by:__
> EOCustomObject
> EOGenericRecord
>
> __Implements:__
> EOKeyValueCodingAdditions
> EORelationshipManipulation
> EOValidation
> EODeferredFaultingSerializable
>
> __Package:__ com.webobjects.eocontrol

---

## Interface Description

---

The EOEnterpriseObject interface identifies basic enterprise object behavior, defining methods for supporting operations common to all enterprise objects. Among these are methods for initializing instances, announcing changes, setting and retrieving property values, and performing validation of state. Some of these methods are for enterprise objects to implement or override, and some are meant to be used as defined by the Framework. Many methods are used internally by the Framework and rarely invoked by application code.

Many of the functional areas are defined in smaller, more specialized interfaces and incorporated in the over arching EOEnterpriseObject interface:

- EOKeyValueCoding defines Enterprise Objects Framework's main data transport mechanism, in which the properties of an object are accessed indirectly by name (or "key"), rather than directly through invocation of an accessor method or as instance variables.
- EOKeyValueCodingAdditions defines extensions to the basic EOKeyValueCoding interface, giving access to groups of properties and to properties across relationships.
- EORelationshipManipulation builds on the basic EOKeyValueCoding interface to allow you to modify to-many relationship properties.
- EOValidation defines the way that enterprise objects validate their values.
- EOFaulting and EODeferredFaulting define mechanisms for postponing an object's initialization until its actually needed.

The remaining methods are introduced in the EOEnterpriseObject interface itself and can be broken down into three functional groups discussed in the following sections:

- ["Initialization" (page 363)](EOEnterpriseObject.Concepts.md#apple-ijaueq2iizcem)
- ["Change Notification" (page 364)](EOEnterpriseObject.Concepts.md#apple-ijaueqsijbauu)
- ["Object and Class Metadata Access" (page 364)](EOEnterpriseObject.Concepts.md#apple-ijauerccjbaui)
- ["Snapshots" (page 365)](EOEnterpriseObject.Concepts.md#apple-ijauercbijauc)

You rarely need to implement the EOEnterpriseObject interface from scratch. The Framework provides default implementations of the methods in EOCustomObject and EOGenericRecord. Use EOGenericRecords to represent enterprise objects that don't require custom behavior, and create subclasses of EOCustomObject to represent enterprise objects that do. The section ["Writing an Enterprise Object Class" (page 366)](EOEnterpriseObject.Concepts.md#apple-ijaueqsijjfeg) highlights the methods that you typically provide or override in a custom enterprise object class.

## Method Types

---

> Initializing enterprise objects
> [awakeFromFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvdgk5ddna)[awakeFromInsertion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvew443foj2gs33o)
>
> Announcing changes
> [willChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxo2lmnrbwqylom5sq)
>
> Getting an object's EOEditingContext
> [editingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwkzdjoruw4z2dn5xhizlyoq)
>
> Getting class description information
> [allPropertyKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc3dmkbzg64dfoj2hss3fpfzq)
> [attributeKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc5duojuwe5lumvfwk6lt)
> [classDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg3dbonzuizltmnzgs4dunfxw4)
> [classDescriptionForDestinationKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg3dbonzuizltmnzgs4dunfxw4rtpojcgk43unfxgc5djn5xewzlz)
> [deleteRuleForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwizlmmv2gkutvnrsum33skjswyylunfxw443infyewzlz)
> [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk3tunf2hsttbnvsq)
> [inverseForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxws3twmvzhgzkgn5zfezlmmf2gs33oonugs4clmv4q)
> [isToManyKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxws42un5gwc3tzjnsxsoq)
> [ownsDestinationObjectsForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxw653ooncgk43unfxgc5djn5xe6ytkmvrxi42gn5zfezlmmf2gs33oonugs4clmv4q)
> [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y)
> [toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32pnzsvezlmmf2gs33oonugs4clmv4xg)
>
> Modifying relationships
> [propagateDeleteWithEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxa4tpobqwoylumvcgk3dforsvo2lunbcwi2lunfxgoq3pnz2gk6du)
> [clearProperties](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg3dfmfzfa4tpobsxe5djmvzq)
>
> Working with snapshots
> [snapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxg3tbobzwq33u)
> [updateFromSnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxk4demf2gkrtsn5wvg3tbobzwq33u)
>
> Merging values
> [changesFromSnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg2dbnztwk42gojxw2u3omfyhg2dpoq)
> [reapplyChangesFromDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxezlbobygy6kdnbqw4z3fondhe33niruwg5djn5xgc4tz)
>
> Invoking behavior on the server
> [invokeRemoteMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxws3twn5vwkutfnvxxizknmv2gq33e)
>
> Getting descriptions
> [eoDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32emvzwg4tjob2gs33o)
> [eoShallowDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32tnbqwy3dpo5cgk43dojuxa5djn5xa)
> [userPresentableDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxk43fojihezltmvxhiylcnrsuizltmnzgs4dunfxw4)

## Instance Methods

---

### allPropertyKeys

`public abstract NSArray allPropertyKeys()`

Returns all of the receiver's property keys. EOCustomObject's implementation returns the union of the keys returned by [attributeKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc5duojuwe5lumvfwk6lt), [toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32pnzsvezlmmf2gs33oonugs4clmv4xg), and [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y).

---

### attributeKeys

`public abstract NSArray attributeKeys()`

Returns the names of the receiver's attributes (not relationship properties). EOCustomObject's implementation simply invokes attributeKeys in the object's EOClassDescription and returns the results. You might wish to override this method to add keys for attributes not defined by the EOClassDescription. The access layer's subclass of EOClassDescription, EOEntityClassDescription, returns the names of attributes designated as class properties.

__See Also:__ [toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32pnzsvezlmmf2gs33oonugs4clmv4xg), [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y)

---

### __awakeFromClientUpdate__

`public abstract void awakeFromClientUpdate(EOEditingContext anEditingContext)`

Description forthcoming.

---

### awakeFromFetch

`public abstract void awakeFromFetch(EOEditingContext anEditingContext)`

Overridden by subclasses to perform additional initialization on the receiver upon its being fetched from the external repository into _anEditingContext_. EOCustomObject's implementation merely sends an awakeObjectFromFetch to the receiver's EOClassDescription. Subclasses should invoke __super__'s implementation before performing their own initialization.

---

### awakeFromInsertion

`public abstract void awakeFromInsertion(EOEditingContext anEditingContext)`

Overridden by subclasses to perform additional initialization on the receiver upon its being inserted into _anEditingContext_. This is commonly used to assign default values or record the time of insertion. EOCustomObject's implementation merely sends an awakeObjectFromInsertion to the receiver's EOClassDescription. Subclasses should invoke __super__'s implementation before performing their own initialization.

---

### changesFromSnapshot

`public abstract NSDictionary changesFromSnapshot(NSDictionary snapshot)`

Returns a dictionary whose keys correspond to the receiver's properties with uncommitted changes relative to _snapshot_, and whose values are the uncommitted values. In both _snapshot_ and the returned dictionary, where a key represents a to-many relationship, the corresponding value is an NSArray containing two other NSArrays: the first is an array of objects to be added to the relationship property, and the second is an array of objects to be removed.

__See Also:__ [reapplyChangesFromDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxezlbobygy6kdnbqw4z3fondhe33niruwg5djn5xgc4tz)

---

### classDescription

`public abstract EOClassDescription classDescription()`

Returns the EOClassDescription registered for the receiver's class.EOCustomObject's implementation invokes the EOClassDescription static method a classDescriptionForClass.

---

### classDescriptionForDestinationKey

`public abstract EOClassDescription classDescriptionForDestinationKey(String key)`

Returns the EOClassDescription for the destination objects of the relationship identified by _key_. EOCustomObject's implementation sends a classDescriptionForDestinationKey message to the receiver's EOClassDescription.

---

### clearProperties

`public abstract void clearProperties()`

Sets all of the receiver's to-one and to-many relationships to null. EOEditingContexts use this method to break cyclic references among objects when they're finalized. EOCustomObject's implementation should be sufficient for all purposes. If your enterprise object maintains references to other objects and these references are not to-one or to-many keys, then you should probably subclass this method ensure unused objects can be finalized.

---

### deleteRuleForRelationshipKey

`public abstract int deleteRuleForRelationshipKey(String relationshipKey)`

Returns a rule indicating how to handle the destination of the receiver's relationship named by _relationshipKey_ when the receiver is deleted. The delete rule is one of:

- DeleteRuleNullify
- DeleteRuleCascade
- DeleteRuleDeny
- DeleteRuleNoAction

For example, an Invoice object might return `DeleteRuleNullify` for the relationship named "lineItems", since when an invoice is deleted, its line items should be deleted as well. For more information on the delete rules, see the method description for EOClassDescription's deleteRuleForRelationshipKey in the class specification for EOClassDescription, the class in which they're defined.

EOCustomObject's implementation of this method simply sends a deleteRuleForRelationshipKey message to the receiver's EOClassDescription.

__See Also:__ [propagateDeleteWithEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxa4tpobqwoylumvcgk3dforsvo2lunbcwi2lunfxgoq3pnz2gk6du), validateForDelete (EOValidation)

---

### editingContext

`public abstract EOEditingContext editingContext()`

Returns the EOEditingContext that holds the receiver.

---

### entityName

`public abstract String entityName()`

Returns the name of the receiver's entity, or null if it doesn't have one. EOCustomObject's implementation simply sends an entityName message to the receiver's EOClassDescription.

---

### eoDescription

`public abstract String eoDescription()`

Returns a string that describes the receiver. EOCustomObject's implementation returns a full description of the receiver's property values by extracting them using the key-value coding methods. An object referenced through relationships is listed with the results of an [eoShallowDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32tnbqwy3dpo5cgk43dojuxa5djn5xa) message (to avoid infinite recursion through cyclical relationships).

This method is useful for debugging. You can implement a __toString__ method that invokes this one, and the debugger's print-object command (__po__ on the command line) automatically displays this description. You can also invoke this method directly on the command line of the debugger.

__See Also:__ [userPresentableDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxk43fojihezltmvxhiylcnrsuizltmnzgs4dunfxw4)

---

### eoShallowDescription

`public abstract String eoShallowDescription()`

Similar to [eoDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32emvzwg4tjob2gs33o), but doesn't descend into relationships. __eoDescription__ invokes this method for relationship destinations to avoid infinite recursion through cyclical relationships. EOCustomObject's implementation simply returns a string containing the receiver's class and entity names.

__See Also:__ [userPresentableDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxk43fojihezltmvxhiylcnrsuizltmnzgs4dunfxw4)

---

### inverseForRelationshipKey

`public abstract String inverseForRelationshipKey(String relationshipKey)`

Returns the name of the relationship pointing back to the receiver's class or entity from that named by _relationshipKey_, or null if there isn't one. With the access layer's EOEntity and EORelationship, for example, reciprocality is determined by the join attributes of the two EORelationships. EOCustomObject's implementation simply sends an inverseForRelationshipKey message to the receiver's EOClassDescription.

You might override this method for reciprocal relationships that aren't defined using the same join attributes. For example, if a Member object has a relationship to CreditCard based on the card number, but a CreditCard has a relationship to Member based on the Member's primary key, both classes need to override this method. This is how Member might implement it:

```
public String inverseForRelationshipKey(String relationshipKey) {
    if (relationshipKey.equals("creditCard"))
        return "member";
    else
        return super.inverseForRelationshipKey(relationshipKey);
}
```

---

### invokeRemoteMethod

`public abstract Object invokeRemoteMethod( String methodName, Class[] argumentTypes Object[] arguments)`

Invokes _methodName_ using _arguments_. To pass an enterprise object as an argument, use its global ID. This method has the side effect of saving all the changes from the receiver's editing context all the way down to the editing context in the server session.

---

### isToManyKey:

`public abstract boolean isToManyKey(String key)`

Returns true if the receiver has a to-many relationship identified by _key_, false otherwise. EOCustomObject's implementation of this method simply checks its [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y) array for _key_.

---

### ownsDestinationObjectsForRelationshipKey

`public abstract boolean ownsDestinationObjectsForRelationshipKey(String key)`

Returns true if the receiver has a relationship identified by _key_ that owns its destination, false otherwise. If an object owns the destination for a relationship, then when that destination object is removed from the relationship, it's automatically deleted. Ownership of a relationship thus contrasts with a delete rule, in that the first applies when the destination is removed and the second applies when the source is deleted. EOCustomObject's implementation of this method simply sends an ownsDestinationObjectsForRelationshipKey message to the receiver's EOClassDescription.

__See Also:__ [deleteRuleForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwizlmmv2gkutvnrsum33skjswyylunfxw443infyewzlz), __- ownsDestination__ (EOAccess' EORelationship)

---

### __prepareValuesForClient__

`public abstract void prepareValuesForClient()`

Description forthcoming.

---

### propagateDeleteWithEditingContext

`public abstract void propagateDeleteWithEditingContext(EOEditingContext anEditingContext)`

Deletes the destination objects of the receiver's relationships according to the delete rule for each relationship. EOCustomObject's implementation simply sends a propagateDeleteForObject message to the receiver's EOClassDescription. For more information on delete rules, see the method description for deleteRuleForRelationshipKey in the EOClassDescription class specification.

__See Also:__ [deleteRuleForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwizlmmv2gkutvnrsum33skjswyylunfxw443infyewzlz)

---

### reapplyChangesFromDictionary

`public abstract void reapplyChangesFromDictionary(NSDictionary changes)`

Similar to takeValuesFromDictionary, but the _changes_ dictionary can contain arrays for to-many relationships. Where a key represents a to-many relationship, the dictionary's value is an NSArray containing two other NSArrays: the first is an array of objects to be added to the relationship property, and the second is an array of objects to be removed. EOCustomObject's implementation should be sufficient for all purposes; you shouldn't have to override this method.

__See Also:__ [changesFromSnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg2dbnztwk42gojxw2u3omfyhg2dpoq)

---

### snapshot

`public abstract NSDictionary snapshot()`

Returns a dictionary whose keys are those of the receiver's attributes, to-one relationships, and to-many relationships, and whose values are the values of those properties, with EONullValue substituted for null. For to-many relationships, the dictionary contains shallow copies of the arrays. EOCustomObject's implementation should be sufficient for all purposes; you shouldn't have to override this method.

__See Also:__ [updateFromSnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxk4demf2gkrtsn5wvg3tbobzwq33u)

---

### toManyRelationshipKeys

`public abstract NSArray toManyRelationshipKeys()`

Returns the names of the receiver's to-many relationships. EOCustomObject's implementation simply invokes toManyRelationshipKeys in the object's EOClassDescription and returns the results. You might wish to override this method to add keys for relationships not defined by the EOClassDescription, but it's rarely necessary: The access layer's subclass of EOClassDescription, EOEntityClassDescription, returns the names of to-many relationships designated as class properties.

__See Also:__ [attributeKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc5duojuwe5lumvfwk6lt), [toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32pnzsvezlmmf2gs33oonugs4clmv4xg)

---

### toOneRelationshipKeys

`public abstract NSArray toOneRelationshipKeys()`

Returns the names of the receiver's to-one relationships. EOCustomObject's implementation simply invokes toOneRelationshipKeys in the object's EOClassDescription and returns the results. You might wish to override this method to add keys for relationships not defined by the EOClassDescription, but it's rarely necessary: The access layer's subclass of EOClassDescription, EOEntityClassDescription, returns the names of to-one relationships designated as class properties.

__See Also:__ [attributeKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc5duojuwe5lumvfwk6lt), [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y)

---

### updateFromSnapshot

`public abstract void updateFromSnapshot(NSDictionary aSnapshot)`

Takes the values from _aSnapshot_, and sets the receiver's properties to them. EOCustomObject's implementation sets each one using takeStoredValueForKey. In the process, EONullValues are converted to null, and array values are set as shallow mutable copies.

__See Also:__ [snapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxg3tbobzwq33u)

---

### userPresentableDescription

`public abstract String userPresentableDescription()`

Returns a short (no longer than 60 characters) description of an enterprise object based on its data. EOCustomObject's implementation enumerates the object's [attributeKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc5duojuwe5lumvfwk6lt) and returns the values of all of its properties, separated by commas (applying the default formatter for numbers and dates).

__See Also:__ [eoDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32emvzwg4tjob2gs33o), [eoShallowDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32tnbqwy3dpo5cgk43dojuxa5djn5xa)

---

### willChange

`public abstract void willChange()`

Notifies any observers that the receiver's state is about to change, by sending each an objectWillChange message (see the EOObserverCenter class specification for more information). A subclass should not override this method, but should invoke it prior to altering the subclass's state, most typically in "set" methods such as the following:

```
public void setRoleName(String value) {
    willChange();
    roleName = value;
}
```

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
