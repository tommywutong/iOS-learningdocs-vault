---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOEnterpriseObject.html
archived_at: '2026-07-18T01:28:41.085704Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOEditors.md)
[!](EOEnterpriseObject-4.md)

---

# EOEnterpriseObject

---

#### (informal protocol)

__Category Of:__ NSObject

__Declared in:__ EOControl/EOClassDescription.h
EOControl/EOEditingContext.h
EOControl/EOKeyValueCoding.h
EOControl/EOObserver.h

## Protocol Description

The EOEnterpriseObject informal protocol identifies basic enterprise object behavior, defining methods for supporting operations common to all enterprise objects. Among these are methods for initializing instances, announcing changes, setting and retrieving property values, and performing validation of state. Some of these methods are for enterprise objects to implement or override, and some are meant to be used as defined by the Framework. Many methods are used internally by the Framework and rarely invoked by application code.

Many of the functional areas are defined in smaller, more specialized informal protocols and incorporated in the overarching EOEnterpriseObject informal protocol:

- [EOKeyValueCoding](EOKeyValueCoding-3.md) defines Enterprise Objects Framework's main data transport mechanism, in which the properties of an object are accessed indirectly by name (or _key_), rather than directly through invocation of an accessor method or as instance variables.
- [EOKeyValueCodingAdditions](EOKeyValueCodingAdditions-2.md) defines extensions to the basic EOKeyValueCoding informal protocol, giving access to groups of properties and to properties across relationships.
- [EORelationshipManipulation](EORelationshipManipulation-2.md) builds on the basic EOKeyValueCoding informal protocol to allow you to modify to-many relationship properties.
- [EOValidation](EOValidation-3.md) defines the way that enterprise objects validate their values.

The remaining methods are introduced in the EOEnterpriseObject informal protocol itself and can be broken down into three functional groups discussed in the following sections:

- [Initialization](EOEnterpriseObject-4.md)
- [Change Notification](EOEnterpriseObject-4.md)
- [Object and Class Metadata Access](EOEnterpriseObject-4.md)
- [Snapshots](EOEnterpriseObject-4.md)

You rarely need to implement the EOEnterpriseObject informal protocol from scratch. The Framework provides default implementations of the methods in categories on NSObject. Use EOGenericRecords to represent enterprise objects that don't require custom behavior, and create subclasses of NSObject to represent enterprise objects that do. The section "[Writing an Enterprise Object Class](EOEnterpriseObject-4.md)" highlights the methods that you typically provide or override in a custom enterprise object class.

# Informal Protocols Incorporated

**[EOKeyValueCoding](EOKeyValueCoding-3.md)**

**[+ accessInstanceVariablesDirectly](EOKeyValueCoding-3.md)

**[+ flushAllKeyBindings](EOKeyValueCoding-3.md)

**[+ useStoredAccessor](EOKeyValueCoding-3.md)

**[- handleQueryWithUnboundKey:](EOKeyValueCoding-3.md)

**[- handleTakeValue:forUnboundKey:](EOKeyValueCoding-3.md)

**[- storedValueForKey:](EOKeyValueCoding-3.md)

**[- takeStoredValue:forKey:](EOKeyValueCoding-3.md)

**[- takeValue:forKey:](EOKeyValueCoding-3.md)

**[- unableToSetNullForKey:](EOKeyValueCoding-3.md)

**[- valueForKey:](EOKeyValueCoding-3.md)********************

**[EOKeyValueCodingAdditions](EOKeyValueCodingAdditions-2.md)**

**[- takeValue:forKeyPath:](EOKeyValueCodingAdditions-2.md)

**[- takeValuesFromDictionary:](EOKeyValueCodingAdditions-2.md)

**[- valueForKeyPath:](EOKeyValueCodingAdditions-2.md)

**[- valuesForKeys:](EOKeyValueCodingAdditions-2.md)********

**[EORelationshipManipulation](EORelationshipManipulation-2.md)**

**[- addObject:toBothSidesOfRelationshipWithKey:](EORelationshipManipulation-2.md)

**[- addObject:toPropertyWithKey:](EORelationshipManipulation-2.md)

**[- removeObject:fromBothSidesOfRelationshipWithKey:](EORelationshipManipulation-2.md)

**[- removeObject:fromPropertyWithKey:](EORelationshipManipulation-2.md)********

**[EOValidation](EOValidation-3.md)**

**[- validateForDelete](EOValidation-3.md)

**[- validateForInsert](EOValidation-3.md)

**[- validateForSave](EOValidation-3.md)

**[- validateForUpdate](EOValidation-3.md)

**[- validateValue:forKey:](EOValidation-3.md)**********

**Initializing enterprise objects**

**- initWithEditingContext:classDescription:globalID:

**- awakeFromFetchInEditingContext:

**- awakeFromInsertionInEditingContext:******

**Announcing changes**

**- willChange**

**Getting an object's EOEditingContext**

**- editingContext**

**Getting class description information**

**- allPropertyKeys

**- attributeKeys

**- classDescription

**- classDescriptionForDestinationKey:

**- deleteRuleForRelationshipKey:

**- entityName

**- inverseForRelationshipKey:

**- isToManyKey:

**- ownsDestinationObjectsForRelationshipKey:

**- toManyRelationshipKeys

**- toOneRelationshipKeys**********************

**Modifying relationships**

**- propagateDeleteWithEditingContext:

**- clearProperties****

**Working with snapshots**

**- snapshot

**- updateFromSnapshot:****

**Merging values**

**- changesFromSnapshot

**- reapplyChangesFromDictionary:****

**Getting descriptions**

**- eoDescription

**- eoShallowDescription

**- userPresentableDescription******

---

#### allPropertyKeys

- (NSArray \*)__allPropertyKeys__

Returns all of the receiver's property keys. NSObject's implementation returns the union of the keys returned by __attributeKeys__ , __toOneRelationshipKeys__ , and __toManyRelationshipKeys__ .

---

#### attributeKeys

- (NSArray \*)__attributeKeys__

Returns the names of the receiver's attributes (not relationship properties). NSObject's implementation simply invokes [__attributeKeys__](EOClassDescription-3.md)in the object's EOClassDescription and returns the results. You might wish to override this method to add keys for attributes not defined by the EOClassDescription. The access layer's subclass of EOClassDescription, EOEntityClassDescription, returns the names of attributes designated as class properties.

__See also:__ - __toOneRelationshipKeys__ , - __toManyRelationshipKeys__

---

#### awakeFromFetchInEditingContext:

- (void)__awakeFromFetchInEditingContext:__ (EOEditingContext \*)_anEditingContext_

Overridden by subclasses to perform additional initialization on the receiver upon its being fetched from the external repository into _anEditingContext_. NSObject's implementation merely sends an [__awakeObject:fromFetchInEditingContext:__](EOClassDescription-3.md)to the receiver's EOClassDescription. Subclasses should invoke __super__ 's implementation before performing their own initialization.

---

#### awakeFromInsertionInEditingContext:

- (void)__awakeFromInsertionInEditingContext:__ (EOEditingContext \*)_anEditingContext_

Overridden by subclasses to perform additional initialization on the receiver upon its being inserted into _anEditingContext_. This is commonly used to assign default values or record the time of insertion. NSObject's implementation merely sends an [__awakeObject:fromInsertionInEditingContext:__](EOClassDescription-3.md)to the receiver's EOClassDescription. Subclasses should invoke __super__ 's implementation before performing their own initialization.

---

#### changesFromSnapshot

- (NSDictionary \*)__changesFromSnapshot:__ (NSDictionary \*)_snapshot_

Returns a dictionary whose keys correspond to the receiver's properties with uncommitted changes relative to _snapshot_, and whose values are the uncommitted values. In both _snapshot_ and the returned dictionary, where a key represents a to-many relationship, the corresponding value is an NSArray containing two other NSArrays: the first is an array of objects to be added to the relationship property, and the second is an array of objects to be removed.

__See also:__ - __reapplyChangesFromDictionary:__

---

#### classDescription

- (EOClassDescription \*)__classDescription__

Returns the EOClassDescription registered for the receiver's class.NSObject's implementation invokes the EOClassDescription class method a [__classDescriptionForClass:__](EOClassDescription-3.md).

---

#### classDescriptionForDestinationKey:

- (EOClassDescription \*)__classDescriptionForDestinationKey:__ (NSString \*)_key_

Returns the EOClassDescription for the destination objects of the relationship identified by _key_. NSObject's implementation sends a [__classDescriptionForDestinationKey:__](EOClassDescription-3.md)message to the receiver's EOClassDescription.

---

#### clearProperties

- (void)__clearProperties__

Sets all of the receiver's to-one and to-many relationships to __nil__ . EOEditingContexts use this method to break cyclic references among objects when they're deallocated. NSObject's implementation should be sufficient for all purposes. If your enterprise object maintains references to other objects and these references are not to-one or to-many keys, then you should probably subclass this method ensure unused objects can be deallocated.

---

#### deleteRuleForRelationshipKey:

- (EODeleteRule)__deleteRuleForRelationshipKey:__ (NSString \*)_relationshipKey_

Returns a rule indicating how to handle the destination of the receiver's relationship named by _relationshipKey_ when the receiver is deleted. The delete rule is one of:

- [EODeleteRuleNullify](EOClassDescription-3.md)
- [EODeleteRuleNullify](EOClassDescription-3.md)
- [EODeleteRuleNullify](EOClassDescription-3.md)
- [EODeleteRuleNullify](EOClassDescription-3.md)

For example, an Invoice object might return [EODeleteRuleNullify](EOClassDescription-3.md) for the relationship named "lineItems", since when an invoice is deleted, its line items should be deleted as well. For more information on the delete rules, see the method description for EOClassDescription's [__deleteRuleForRelationshipKey:__](EOClassDescription-3.md)in the class specification for EOClassDescription.

NSObject's implementation of this method simply sends a [__deleteRuleForRelationshipKey:__](EOClassDescription-3.md)message to the receiver's EOClassDescription.

__See also:__ - __propagateDeleteWithEditingContext:__ , [- __validateForDelete__](EOValidation-3.md)(EOValidation)

---

#### editingContext

- (EOEditingContext \*)__editingContext__

Returns the EOEditingContext that holds the receiver.

---

#### entityName

- (NSString \*)__entityName__

Returns the name of the receiver's entity, or __nil__ if it doesn't have one. NSObject's implementation simply sends an [__entityName__](EOClassDescription-3.md)message to the receiver's EOClassDescription.

---

#### eoDescription

- (NSString \*)__eoDescription__

Returns a string that describes the receiver. NSObject's implementation returns a full description of the receiver's property values by extracting them using the key-value coding methods. An object referenced through relationships is listed with the results of an __eoShallowDescription__ message (to avoid infinite recursion through cyclical relationships).

This method is useful for debugging. You can implement a __description__ method that invokes this one, and the debugger's print-object command (__po__ on the command line) automatically displays this description. You can also invoke this method directly on the command line of the debugger.

__See also:__ - __userPresentableDescription__

---

#### eoShallowDescription

- (NSString \*)__eoShallowDescription__

Similar to __eoDescription__ , but doesn't descend into relationships. __eoDescription__ invokes this method for relationship destinations to avoid infinite recursion through cyclical relationships. NSObject's implementation simply returns a string containing the receiver's class and entity names, along with the memory address of its __id__ .

__See also:__ - __userPresentableDescription__

---

#### initWithEditingContext:classDescription:globalID:

- __initWithEditingContext:__ (EOEditingContext \*)_anEditingContext___classDescription:__ (EOClassDescription \*)_aClassDescription___globalID:__ (EOGlobalID \*)_globalID_

Initializes the receiver with the arguments provided. NSObject's implementation simply invokes __init__ , and ingores _anEditingContext_.

__See also:__ [- __createInstanceWithEditingContext:globalID:zone:__](EOClassDescription-3.md)(EOClassDescription)

---

#### inverseForRelationshipKey:

- (NSString \*)__inverseForRelationshipKey:__ (NSString \*)_relationshipKey_

Returns the name of the relationship pointing back to the receiver's class or entity from that named by _relationshipKey_, or __nil__ if there isn't one. With the access layer's EOEntity and EORelationship, for example, reciprocality is determined by the join attributes of the two EORelationships. NSObject's implementation simply sends an [__inverseForRelationshipKey:__](EOClassDescription-3.md)message to the receiver's EOClassDescription.

You might override this method for reciprocal relationships that aren't defined using the same join attributes. For example, if a Member object has a relationship to CreditCard based on the card number, but a CreditCard has a relationship to Member based on the Member's primary key, both classes need to override this method. This is how Member might implement it:

> ```
> public String inverseForRelationshipKey(java.lang.String relationshipKey) {
>     if (relationshipKey.equals("creditCard"))
> - (NSString *)inverseForRelationshipKey:(NSString *)relationshipKey
> {
>     if ([relationshipKey isEqual:@"creditCard"]) return @"member";
>     return [super inverseForRelationshipKey:relationshipKey];
> }
> ```

---

#### isToManyKey:

- (BOOL)__isToManyKey:__ (NSString \*)_key_

Returns YES if the receiver has a to-many relationship identified by _key_, NO otherwise. NSObject's implementation of this method simply checks its __toManyRelationshipKeys__ array for _key_.

---

#### ownsDestinationObjectsForRelationshipKey:

- (BOOL)__ownsDestinationObjectsForRelationshipKey:__ (NSString \*)_key_

Returns YES if the receiver has a relationship identified by _key_ that owns its destination, NO otherwise. If an object owns the destination for a relationship, then when that destination object is removed from the relationship, it's automatically deleted. Ownership of a relationship thus contrasts with a delete rule, in that the first applies when the destination is removed and the second applies when the source is deleted. NSObject's implementation of this method simply sends an [__ownsDestinationObjectsForRelationshipKey:__](EOClassDescription-3.md)message to the receiver's EOClassDescription.

__See also:__ - __deleteRuleForRelationshipKey:__ , - __ownsDestination__ (the access layer's EORelationship)

---

#### propagateDeleteWithEditingContext:

- (void)__propagateDeleteWithEditingContext:__ (EOEditingContext \*)_anEditingContext_

Deletes the destination objects of the receiver's relationships according to the delete rule for each relationship. NSObject's implementation simply sends a [__propagateDeleteForObject:editingContext:__](EOClassDescription-3.md)message to the receiver's EOClassDescription. For more information on delete rules, see the method description for [__deleteRuleForRelationshipKey:__](EOClassDescription-3.md)in the EOClassDescription class specification.

__See also:__ - __deleteRuleForRelationshipKey:__

---

#### reapplyChangesFromDictionary:

- (void)__reapplyChangesFromDictionary:__ (NSDictionary \*)_changes_

Similar to [__takeValuesFromDictionary:__](EOKeyValueCodingAdditions-2.md), but the _changes_ dictionary can contain arrays for to-many relationships. Where a key represents a to-many relationship, the dictionary's value is an NSArray containing two other NSArrays: the first is an array of objects to be added to the relationship property, and the second is an array of objects to be removed. NSObject's implementation should be sufficient for all purposes; you shouldn't have to override this method.

__See also:__ - __changesFromSnapshot__

---

#### snapshot

- (NSDictionary \*)__snapshot__

Returns a dictionary whose keys are those of the receiver's attributes, to-one relationships, and to-many relationships, and whose values are the values of those properties, with EONull substituted for __nil__ . For to-many relationships, the dictionary contains shallow copies of the arrays to preserve the __id__ s of the contents. NSObject's implementation should be sufficient for all purposes; you shouldn't have to override this method.

__See also:__ - __updateFromSnapshot:__

---

#### toManyRelationshipKeys

- (NSArray \*)__toManyRelationshipKeys__

Returns the names of the receiver's to-many relationships. NSObject's implementation simply invokes [__toManyRelationshipKeys__](EOClassDescription-3.md)in the object's EOClassDescription and returns the results. You might wish to override this method to add keys for relationships not defined by the EOClassDescription, but it's rarely necessary: The access layer's subclass of EOClassDescription, EOEntityClassDescription, returns the names of to-many relationships designated as class properties.

__See also:__ - __attributeKeys__ , - __toOneRelationshipKeys__

---

#### toOneRelationshipKeys

- (NSArray \*)__toOneRelationshipKeys__

Returns the names of the receiver's to-one relationships. NSObject's implementation simply invokes [__toOneRelationshipKeys__](EOClassDescription-3.md)in the object's EOClassDescription and returns the results. You might wish to override this method to add keys for relationships not defined by the EOClassDescription, but it's rarely necessary: The access layer's subclass of EOClassDescription, EOEntityClassDescription, returns the names of to-one relationships designated as class properties.

__See also:__ - __attributeKeys__ , - __toManyRelationshipKeys__

---

#### updateFromSnapshot:

- (void)__updateFromSnapshot:__ (NSDictionary \*)_aSnapshot_

Takes the values from _aSnapshot_, and sets the receiver's properties to them. NSObject's implementation sets each one using __[takeStoredValue:forKey:](EOKeyValueCoding-3.md)__ . In the process, EONull values are converted to __nil__ , and array values are set as shallow mutable copies to preserve the __id__ s of the contents.

__See also:__ - __snapshot__

---

#### userPresentableDescription

- (NSString \*)`userPresentableDescription`

Returns a short (no longer than 60 characters) description of an enterprise object based on its data. NSObject's implementation enumerates the object's __attributeKeys__ and returns the values of all of its properties, separated by commas (applying the default formatter for numbers and dates).

__See also:__ - __eoDescription__ , - __eoShallowDescription__

---

#### willChange

- (void)__willChange__

Notifies any observers that the receiver's state is about to change, by sending each an [__objectWillChange:__](EOObserving-2.md)message (see the [EOObserverCenter](EOObserverCenter-2.md) class specification for more information). A subclass should not override this method, but should invoke it prior to altering the subclass's state, most typically in "set" methods such as the following:

> ```
> - (void)setRoleName:(NSString *)value {
>     [self willChange];
>     [roleName autorelease];
>     roleName = [value retain];
> }
> ```

---

[!](EOEditors.md)
[!](EOEnterpriseObject-4.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
