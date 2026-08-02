---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOEnterpriseObject.html
archived_at: '2026-07-18T01:28:32.689258Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOEditingContext.Editor.md)
[!](EOEnterpriseObject-2.md)

---

# EOEnterpriseObject

__Implemented By:__
EOCustomObject
EOGenericRecord

__Implements:__
EOFaulting
EOKeyValueCoding (EOKeyValueCodingAdditions)
EOKeyValueCodingAdditions
EORelationshipManipulation
EOValidation

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (WebObjects and Yellow Box)

## Interface Description

The EOEnterpriseObject interface identifies basic enterprise object behavior, defining methods for supporting operations common to all enterprise objects. Among these are methods for initializing instances, announcing changes, setting and retrieving property values, and performing validation of state. Some of these methods are for enterprise objects to implement or override, and some are meant to be used as defined by the Framework. Many methods are used internally by the Framework and rarely invoked by application code.

Many of the functional areas are defined in smaller, more specialized interfaces and incorporated in the overarching EOEnterpriseObject interface:

- [EOKeyValueCoding](EOKeyValueCoding.md) defines Enterprise Objects Framework's main data transport mechanism, in which the properties of an object are accessed indirectly by name (or _key_), rather than directly through invocation of an accessor method or as instance variables.
- [EOKeyValueCodingAdditions](EOKeyValueCodingAdditions.md) defines extensions to the basic EOKeyValueCoding interface, giving access to groups of properties and to properties across relationships.
- [EORelationshipManipulation](EORelationshipManipulation.md) builds on the basic EOKeyValueCoding interface to allow you to modify to-many relationship properties.
- [EOValidation](EOValidation.md) defines the way that enterprise objects validate their values.
- [EOFaulting](EOFaulting.md) forms a general mechanism for postponing an object's initialization until its actually needed.

The remaining methods are introduced in the EOEnterpriseObject interface itself and can be broken down into three functional groups discussed in the following sections:

- [Initialization](EOEnterpriseObject-2.md)
- [Change Notification](EOEnterpriseObject-2.md)
- [Object and Class Metadata Access](EOEnterpriseObject-2.md)
- [Snapshots](EOEnterpriseObject-2.md)

You rarely need to implement the EOEnterpriseObject interface from scratch. The Framework provides default implementations of the methods in EOCustomObject and EOGenericRecord. Use EOGenericRecords to represent enterprise objects that don't require custom behavior, and create subclasses of EOCustomObject to represent enterprise objects that do. The section "[Writing an Enterprise Object Class](EOEnterpriseObject-2.md)" highlights the methods that you typically provide or override in a custom enterprise object class.

## Interfaces Implemented

**[EOKeyValueCoding](EOKeyValueCoding.md)**

**[- handleQueryWithUnboundKey](EOKeyValueCoding.md)

**[- handleTakeValueForUnboundKey](EOKeyValueCoding.md)

**[- storedValueForKey](EOKeyValueCoding.md)

**[- takeStoredValueForKey](EOKeyValueCoding.md)

**[- takeValueForKey](EOKeyValueCoding.md)

**[- unableToSetNullForKey](EOKeyValueCoding.md)

**[- valueForKey](EOKeyValueCoding.md)**************

**[EOKeyValueCodingAdditions](EOKeyValueCodingAdditions.md)**

**[- takeValueForKeyPath](EOKeyValueCodingAdditions.md)

**[- takeValuesFromDictionary](EOKeyValueCodingAdditions.md)

**[- valueForKeyPath](EOKeyValueCodingAdditions.md)

**[- valuesForKeys](EOKeyValueCodingAdditions.md)********

**[EORelationshipManipulation](EORelationshipManipulation.md)**

**[- addObjectToBothSidesOfRelationshipWithKey](EORelationshipManipulation.md)

**[- addObjectToPropertyWithKey](EORelationshipManipulation.md)

**[- removeObjectFromBothSidesOfRelationshipWithKey](EORelationshipManipulation.md)

**[- removeObjectFromPropertyWithKey](EORelationshipManipulation.md)********

**[EOValidation](EOValidation.md)**

**[- validateForDelete](EOValidation.md)

**[- validateForInsert](EOValidation.md)

**[- validateForSave](EOValidation.md)

**[- validateForUpdate](EOValidation.md)

**[- validateValueForKey](EOValidation.md)**********

**[EOFaulting](EOFaulting.md)**

**[clearFault](EOFaulting.md)

**[isFault](EOFaulting.md)

**[turnIntoFault](EOFaulting.md)

**[willRead](EOFaulting.md)********

## Method Types

**Initializing enterprise objects**

**- awakeFromFetch

**- awakeFromInsertion****

**Announcing changes**

**- willChange**

**Getting an object's EOEditingContext**

**- editingContext**

**Getting class description information**

**- allPropertyKeys

**- attributeKeys

**- classDescription

**- classDescriptionForDestinationKey

**- deleteRuleForRelationshipKey

**- entityName

**- inverseForRelationshipKey

**- isToManyKey

**- ownsDestinationObjectsForRelationshipKey

**- toManyRelationshipKeys

**- toOneRelationshipKeys**********************

**Modifying relationships**

**- propagateDeleteWithEditingContext

**- clearProperties****

**Working with snapshots**

**- snapshot

**- updateFromSnapshot****

**Merging values (Yellow Box only)**

**- changesFromSnapshot (Yellow Box only)

**- reapplyChangesFromDictionary (Yellow Box only)****

**Invoking behavior on the server (Java Client only)**

**invokeRemoteMethod (Java Client only)**

**Getting descriptions**

**- eoDescription

**- eoShallowDescription

**- userPresentableDescription (Yellow Box only)******

## Instance Methods

---

#### allPropertyKeys

public abstract NSArray __allPropertyKeys__ ()

Returns all of the receiver's property keys. EOCustomObject's implementation returns the union of the keys returned by __attributeKeys__ , __toOneRelationshipKeys__ , and __toManyRelationshipKeys__ .

---

#### attributeKeys

public abstract NSArray __attributeKeys__ ()

Returns the names of the receiver's attributes (not relationship properties). EOCustomObject's implementation simply invokes [__attributeKeys__](EOClassDescription.md)in the object's EOClassDescription and returns the results. You might wish to override this method to add keys for attributes not defined by the EOClassDescription. The access layer's subclass of EOClassDescription, EOEntityClassDescription, returns the names of attributes designated as class properties.

__See also:__ - __toOneRelationshipKeys__ , - __toManyRelationshipKeys__

---

#### awakeFromFetch

public abstract void __awakeFromFetch__ (EOEditingContext _anEditingContext_)

Overridden by subclasses to perform additional initialization on the receiver upon its being fetched from the external repository into _anEditingContext_. EOCustomObject's implementation merely sends an [__awakeObjectFromFetch__](EOClassDescription.md)to the receiver's EOClassDescription. Subclasses should invoke __super__ 's implementation before performing their own initialization.

---

#### awakeFromInsertion

public abstract void __awakeFromInsertion__ (EOEditingContext _anEditingContext_)

Overridden by subclasses to perform additional initialization on the receiver upon its being inserted into _anEditingContext_. This is commonly used to assign default values or record the time of insertion. EOCustomObject's implementation merely sends an [__awakeObjectFromInsertion__](EOClassDescription.md)to the receiver's EOClassDescription. Subclasses should invoke __super__ 's implementation before performing their own initialization.

---

#### changesFromSnapshot

public abstract NSDictionary __changesFromSnapshot__ (NSDictionary _snapshot_)

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Returns a dictionary whose keys correspond to the receiver's properties with uncommitted changes relative to _snapshot_, and whose values are the uncommitted values. In both _snapshot_ and the returned dictionary, where a key represents a to-many relationship, the corresponding value is an NSArray containing two other NSArrays: the first is an array of objects to be added to the relationship property, and the second is an array of objects to be removed.

__See also:__ - __reapplyChangesFromDictionary__

---

#### classDescription

public abstract EOClassDescription __classDescription__ ()

Returns the EOClassDescription registered for the receiver's class.EOCustomObject's implementation invokes the EOClassDescription static method a [__classDescriptionForClass__](EOClassDescription.md).

---

#### classDescriptionForDestinationKey

public abstract EOClassDescription __classDescriptionForDestinationKey__ (java.lang.String _key_)

Returns the EOClassDescription for the destination objects of the relationship identified by _key_. EOCustomObject's implementation sends a [__classDescriptionForDestinationKey__](EOClassDescription.md)message to the receiver's EOClassDescription.

---

#### clearProperties

public abstract void __clearProperties__ ()

Sets all of the receiver's to-one and to-many relationships to __null__ . EOEditingContexts use this method to break cyclic references among objects when they're finalized. EOCustomObject's implementation should be sufficient for all purposes. If your enterprise object maintains references to other objects and these references are not to-one or to-many keys, then you should probably subclass this method ensure unused objects can be finalized.

---

#### deleteRuleForRelationshipKey

public abstract int __deleteRuleForRelationshipKey__ (java.lang.String _relationshipKey_)

Returns a rule indicating how to handle the destination of the receiver's relationship named by _relationshipKey_ when the receiver is deleted. The delete rule is one of:

- [DeleteRuleNullify](EOClassDescription.md)
- [DeleteRuleNullify](EOClassDescription.md)
- [DeleteRuleNullify](EOClassDescription.md)
- [DeleteRuleNullify](EOClassDescription.md)

For example, an Invoice object might return [DeleteRuleNullify](EOClassDescription.md) for the relationship named "lineItems", since when an invoice is deleted, its line items should be deleted as well. For more information on the delete rules, see the method description for EOClassDescription's [__deleteRuleForRelationshipKey__](EOClassDescription.md)in the class specification for EOClassDescription, the class in which they're defined.

EOCustomObject's implementation of this method simply sends a [__deleteRuleForRelationshipKey__](EOClassDescription.md)message to the receiver's EOClassDescription.

__See also:__ - __propagateDeleteWithEditingContext__ , [- __validateForDelete__](EOValidation.md)(EOValidation)

---

#### editingContext

public abstract EOEditingContext __editingContext__ ()

Returns the EOEditingContext that holds the receiver.

---

#### entityName

public abstract java.lang.String __entityName__ ()

Returns the name of the receiver's entity, or __null__ if it doesn't have one. EOCustomObject's implementation simply sends an [__entityName__](EOClassDescription.md)message to the receiver's EOClassDescription.

---

#### eoDescription

public abstract java.lang.String __eoDescription__ ()

Returns a string that describes the receiver. EOCustomObject's implementation returns a full description of the receiver's property values by extracting them using the key-value coding methods. An object referenced through relationships is listed with the results of an __eoShallowDescription__ message (to avoid infinite recursion through cyclical relationships).

This method is useful for debugging. You can implement a __toString__ method that invokes this one, and the debugger's print-object command (__po__ on the command line) automatically displays this description. You can also invoke this method directly on the command line of the debugger.

__See also:__ - __userPresentableDescription__

---

#### eoShallowDescription

public abstract java.lang.String __eoShallowDescription__ ()

Similar to __eoDescription__ , but doesn't descend into relationships. __eoDescription__ invokes this method for relationship destinations to avoid infinite recursion through cyclical relationships. EOCustomObject's implementation simply returns a string containing the receiver's class and entity names.

__See also:__ - __userPresentableDescription__

---

#### inverseForRelationshipKey

public abstract java.lang.String __inverseForRelationshipKey__ (java.lang.String _relationshipKey_)

Returns the name of the relationship pointing back to the receiver's class or entity from that named by _relationshipKey_, or __null__ if there isn't one. With the access layer's EOEntity and EORelationship, for example, reciprocality is determined by the join attributes of the two EORelationships. EOCustomObject's implementation simply sends an [__inverseForRelationshipKey__](EOClassDescription.md)message to the receiver's EOClassDescription.

You might override this method for reciprocal relationships that aren't defined using the same join attributes. For example, if a Member object has a relationship to CreditCard based on the card number, but a CreditCard has a relationship to Member based on the Member's primary key, both classes need to override this method. This is how Member might implement it:

> ```
> public String inverseForRelationshipKey(java.lang.String relationshipKey) {
>     if (relationshipKey.equals("creditCard"))
>         return "member";
>     else
>         return super.inverseForRelationshipKey(relationshipKey);
> }
> ```

---

#### invokeRemoteMethod

public abstract java.lang.Object __invokeRemoteMethod__ (
java.lang.String _methodName_,
java.lang.Object[] _arguments_)

This method is available for Java Client applications only; there is no Yellow Box equivalent.

Invokes _methodName_ using _arguments_. To pass an enterprise object as an argument, use its global ID. This method has the side effect of saving all the changes from the receiver's editing context all the way down to the editing context in the server session.

---

#### isToManyKey

public abstract boolean __isToManyKey__ (java.lang.String _key_)

Returns __true__ if the receiver has a to-many relationship identified by _key_, __false__ otherwise. EOCustomObject's implementation of this method simply checks its __toManyRelationshipKeys__ array for _key_.

---

#### ownsDestinationObjectsForRelationshipKey

public abstract boolean __ownsDestinationObjectsForRelationshipKey__ (java.lang.String _key_)

Returns __true__ if the receiver has a relationship identified by _key_ that owns its destination, __false__ otherwise. If an object owns the destination for a relationship, then when that destination object is removed from the relationship, it's automatically deleted. Ownership of a relationship thus contrasts with a delete rule, in that the first applies when the destination is removed and the second applies when the source is deleted. EOCustomObject's implementation of this method simply sends an [__ownsDestinationObjectsForRelationshipKey__](EOClassDescription.md)message to the receiver's EOClassDescription.

__See also:__ - __deleteRuleForRelationshipKey__ , - __ownsDestination__ (the access layer's EORelationship)

---

#### propagateDeleteWithEditingContext

public abstract void __propagateDeleteWithEditingContext__ (EOEditingContext _anEditingContext_)

Deletes the destination objects of the receiver's relationships according to the delete rule for each relationship. EOCustomObject's implementation simply sends a [__propagateDeleteForObject__](EOClassDescription.md)message to the receiver's EOClassDescription. For more information on delete rules, see the method description for [__deleteRuleForRelationshipKey__](EOClassDescription.md)in the EOClassDescription class specification.

__See also:__ - __deleteRuleForRelationshipKey__

---

#### reapplyChangesFromDictionary

public abstract void __reapplyChangesFromDictionary__ (NSDictionary _changes_)

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Similar to [__takeValuesFromDictionary__](EOKeyValueCodingAdditions.md), but the _changes_ dictionary can contain arrays for to-many relationships. Where a key represents a to-many relationship, the dictionary's value is an NSArray containing two other NSArrays: the first is an array of objects to be added to the relationship property, and the second is an array of objects to be removed. EOCustomObject's implementation should be sufficient for all purposes; you shouldn't have to override this method.

__See also:__ - __changesFromSnapshot__

---

#### snapshot

public abstract NSDictionary __snapshot__ ()

Returns a dictionary whose keys are those of the receiver's attributes, to-one relationships, and to-many relationships, and whose values are the values of those properties, with EONullValue substituted for __null__ . For to-many relationships, the dictionary contains shallow copies of the arrays. EOCustomObject's implementation should be sufficient for all purposes; you shouldn't have to override this method.

__See also:__ - __updateFromSnapshot__

---

#### toManyRelationshipKeys

public abstract NSArray __toManyRelationshipKeys__ ()

Returns the names of the receiver's to-many relationships. EOCustomObject's implementation simply invokes [__toManyRelationshipKeys__](EOClassDescription.md)in the object's EOClassDescription and returns the results. You might wish to override this method to add keys for relationships not defined by the EOClassDescription, but it's rarely necessary: The access layer's subclass of EOClassDescription, EOEntityClassDescription, returns the names of to-many relationships designated as class properties.

__See also:__ - __attributeKeys__ , - __toOneRelationshipKeys__

---

#### toOneRelationshipKeys

public abstract NSArray __toOneRelationshipKeys__ ()

Returns the names of the receiver's to-one relationships. EOCustomObject's implementation simply invokes [__toOneRelationshipKeys__](EOClassDescription.md)in the object's EOClassDescription and returns the results. You might wish to override this method to add keys for relationships not defined by the EOClassDescription, but it's rarely necessary: The access layer's subclass of EOClassDescription, EOEntityClassDescription, returns the names of to-one relationships designated as class properties.

__See also:__ - __attributeKeys__ , - __toManyRelationshipKeys__

---

#### updateFromSnapshot

public abstract void __updateFromSnapshot__ (NSDictionary _aSnapshot_)

Takes the values from _aSnapshot_, and sets the receiver's properties to them. EOCustomObject's implementation sets each one using __[takeStoredValueForKey](EOKeyValueCoding.md)__ . In the process, EONullValues are converted to __null__ , and array values are set as shallow mutable copies.

__See also:__ - __snapshot__

---

#### userPresentableDescription

public abstract java.lang.String __userPresentableDescription__ ()

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Returns a short (no longer than 60 characters) description of an enterprise object based on its data. EOCustomObject's implementation enumerates the object's __attributeKeys__ and returns the values of all of its properties, separated by commas (applying the default formatter for numbers and dates).

__See also:__ - __eoDescription__ , - __eoShallowDescription__

---

#### willChange

public abstract void __willChange__ ()

Notifies any observers that the receiver's state is about to change, by sending each an [__objectWillChange__](EOObserving.md)message (see the [EOObserverCenter](EOObserverCenter.md) class specification for more information). A subclass should not override this method, but should invoke it prior to altering the subclass's state, most typically in "set" methods such as the following:

> ```
> public void setRoleName(String value) {
>     willChange();
>     roleName = value;
> }
> ```

In Java Client, this method invokes __willRead:__ .

---

[[TOC]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html) [[Prev]](EOEditors.md) [[Next]](More/EOEnterpriseObject_m.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
