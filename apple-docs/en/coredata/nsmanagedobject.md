---
title: NSManagedObject
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject.json'
content_hash: 'sha256:64e68f1a812b501f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSManagedObject

<sub>Class</sub>

The base class that all Core Data model objects inherit from.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated class NSManagedObject
```

## Overview

A managed object has an associated entity description ([NSEntityDescription](nsentitydescription.md)) that provides metadata about the object, including the name of the entity that the object represents and the names of its attributes and relationships. A managed object also has an associated managed object context that tracks changes to the object graph.

You can’t use instances of direct subclasses of [NSObject](../objectivec/nsobject-swift.class.md), or any other class that doesn’t inherit from [NSManagedObject](nsmanagedobject.md), with a managed object context. You may create custom subclasses of [NSManagedObject](nsmanagedobject.md), although this isn’t always necessary. If you don’t need custom logic, you can create a complete object graph with [NSManagedObject](nsmanagedobject.md) instances.

If you instantiate a managed object directly, you must call the designated initializer [- initWithEntity:insertIntoManagedObjectContext:](<nsmanagedobject/init(entity_insertinto_).md>).

### Data Storage

In some respects, an `NSManagedObject` acts like a dictionary—it’s a generic container object that provides efficient storage for the properties defined by its associated `NSEntityDescription` instance. `NSManagedObject` supports a range of common types for attribute values, including string, date, and number (see [NSAttributeDescription](nsattributedescription.md) for full details). Therefore, typically you don’t need to define instance variables in subclasses. Sometimes, however, you want to use types that aren’t supported directly, such as colors and C structures. For example, in a graphics application you might want to define a Rectangle entity that has color and bounds attributes that are an instance of `NSColor` and an `NSRect` struct, respectively. For some types you can use a transformable attribute, for others this may require you to create a subclass of `NSManagedObject`.

> [!note] Note
> The default value for [automaticallyNotifiesObservers(forKey:)](<../objectivec/nsobject-swift.class/automaticallynotifiesobservers(forkey_).md>) is `false` for managed properties of a `NSManagedObject`, and `true` for unmanaged properties.

### Faulting

Managed objects typically represent data held in a persistent store. In some situations a managed object may be a _fault_—an object whose property values haven’t yet been loaded from the external data store. When you access persistent property values, the fault “fires” and the data is retrieved from the store automatically. This can be a comparatively expensive process (potentially requiring a round trip to the persistent store), and you may wish to avoid unnecessarily firing a fault. See [Faulting and Uniquing](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/FaultingandUniquing.html#//apple_ref/doc/uid/TP40001075-CH18) for more details on faults.

You can safely invoke the following methods and properties on a fault without causing it to fire: [isEqual(_:)](<../objectivec/nsobjectprotocol/isequal(__).md>), [hash](../objectivec/nsobjectprotocol/hash.md), [superclass](../objectivec/nsobjectprotocol/superclass.md), [class](../objectivec/nsobject-c.protocol/class.md), [self()](<../objectivec/nsobjectprotocol/self().md>), [isProxy()](<../objectivec/nsobjectprotocol/isproxy().md>), [isKind(of:)](<../objectivec/nsobjectprotocol/iskind(of_).md>), [isMember(of:)](<../objectivec/nsobjectprotocol/ismember(of_).md>), [conforms(to:)](<../objectivec/nsobject-swift.class/conforms(to_).md>), [responds(to:)](<../objectivec/nsobjectprotocol/responds(to_).md>), [description](../objectivec/nsobjectprotocol/description.md), [managedObjectContext](nsmanagedobject/managedobjectcontext.md), [entity](nsmanagedobject/entity-swift.property.md), [objectID](nsmanagedobject/objectid.md), [inserted](nsmanagedobject/isinserted.md), [updated](nsmanagedobject/isupdated.md), [deleted](nsmanagedobject/isdeleted.md), [faultingState](nsmanagedobject/faultingstate.md), and [fault](nsmanagedobject/isfault.md). Because `isEqual` and `hash` don’t cause a fault to fire, managed objects can typically be placed in collections without firing a fault. Note, however, that invoking key-value coding methods on the collection object might in turn result in an invocation of `valueForKey:` on a managed object, which would fire the fault.

Although the `description` property doesn’t cause a fault to fire, if you implement a custom `description` that accesses the object’s persistent properties, this does cause a fault to fire. You are strongly discouraged from overriding `description` in this way.

### Subclassing Notes

In combination with the entity description in the managed object model, `NSManagedObject` provides a rich set of default behaviors including support for arbitrary properties and value validation. If you decide to subclass `NSManagedObject` to implement custom features, make sure you don’t disrupt Core Data’s behavior.

#### Methods and Properties You Must Not Override

`NSManagedObject` itself customizes many features of `NSObject` so that managed objects can be properly integrated into the Core Data infrastructure. Core Data relies on the `NSManagedObject` implementation of the following methods and properties, which you therefore absolutely must not override: [- primitiveValueForKey:](<nsmanagedobject/primitivevalue(forkey_).md>), [- setPrimitiveValue:forKey:](<nsmanagedobject/setprimitivevalue(__forkey_).md>), [isEqual(_:)](<../objectivec/nsobjectprotocol/isequal(__).md>), [hash](../objectivec/nsobjectprotocol/hash.md), [superclass](../objectivec/nsobjectprotocol/superclass.md), [class](../objectivec/nsobject-c.protocol/class.md), [self()](<../objectivec/nsobjectprotocol/self().md>), [isProxy()](<../objectivec/nsobjectprotocol/isproxy().md>), [isKind(of:)](<../objectivec/nsobjectprotocol/iskind(of_).md>), [isMember(of:)](<../objectivec/nsobjectprotocol/ismember(of_).md>), [conforms(to:)](<../objectivec/nsobjectprotocol/conforms(to_).md>), [responds(to:)](<../objectivec/nsobjectprotocol/responds(to_).md>), [managedObjectContext](nsmanagedobject/managedobjectcontext.md), [entity](nsmanagedobject/entity-swift.property.md), [objectID](nsmanagedobject/objectid.md), [inserted](nsmanagedobject/isinserted.md), [updated](nsmanagedobject/isupdated.md), [deleted](nsmanagedobject/isdeleted.md), and [fault](nsmanagedobject/isfault.md), [alloc](../objectivec/nsobject-swift.class/alloc.md), [allocWithZone:](../objectivec/nsobject-swift.class/allocwithzone_.md), [new](../objectivec/nsobject-swift.class/new.md),  [instancesRespond(to:)](<../objectivec/nsobject-swift.class/instancesrespond(to_).md>), [instanceMethod(for:)](<../objectivec/nsobject-swift.class/instancemethod(for_).md>), [method(for:)](<../objectivec/nsobject-swift.class/method(for_).md>), [methodSignatureForSelector:](../objectivec/nsobject-swift.class/methodsignatureforselector_.md), [instanceMethodSignatureForSelector:](../objectivec/nsobject-swift.class/instancemethodsignatureforselector_.md), or [isSubclass(of:)](<../objectivec/nsobject-swift.class/issubclass(of_).md>).

#### Methods and Properties You Shouldn’t Override

As with any class, you are strongly discouraged from overriding the key-value observing methods such as [willChangeValue(forKey:)](<../objectivec/nsobject-swift.class/willchangevalue(forkey_).md>) and [didChangeValue(forKey:withSetMutation:using:)](<../objectivec/nsobject-swift.class/didchangevalue(forkey_withsetmutation_using_).md>). Avoid overriding `description`—if this method fires a fault during a debugging operation, the results may be unpredictable. Also avoid overriding [- initWithEntity:insertIntoManagedObjectContext:](<nsmanagedobject/init(entity_insertinto_).md>), or `dealloc`. Changing values in the [- initWithEntity:insertIntoManagedObjectContext:](<nsmanagedobject/init(entity_insertinto_).md>) method won’t be noticed by the context, and if you aren’t careful, those changes may not be saved. Perform most initialization customization in one of the `awake…` methods. If you do override [- initWithEntity:insertIntoManagedObjectContext:](<nsmanagedobject/init(entity_insertinto_).md>), make sure you adhere to the requirements set out in the method description. See [- initWithEntity:insertIntoManagedObjectContext:](<nsmanagedobject/init(entity_insertinto_).md>).

Don’t override `dealloc` because [- didTurnIntoFault](<nsmanagedobject/didturnintofault().md>) is usually a better time to clear values—a managed object may not be reclaimed for some time after it has been turned into a fault. Core Data doesn’t guarantee that `dealloc` will be called in all scenarios (such as when the application quits). Therefore, don’t include required side effects (like saving or changes to the file system, user preferences, and so on) in these methods.

In summary, for [- initWithEntity:insertIntoManagedObjectContext:](<nsmanagedobject/init(entity_insertinto_).md>) and `dealloc`, Core Data reserves exclusive control over the life cycle of the managed object (that is, raw memory management). This is so that the framework can provide features such as uniquing and by consequence, relationship maintenance, as well as much better performance than would be possible otherwise.

#### Additional Override Considerations

The following methods are intended to be fine grained and aren’t suitable for large-scale operations. Don’t fetch or save in these methods. In particular, they shouldn’t have side effects on the managed object context.

- [- initWithEntity:insertIntoManagedObjectContext:](<nsmanagedobject/init(entity_insertinto_).md>)
- [- didTurnIntoFault](<nsmanagedobject/didturnintofault().md>)
- [- willTurnIntoFault](<nsmanagedobject/willturnintofault().md>)
- `dealloc`

In addition, if you plan to override `awakeFromInsert`, `awakeFromFetch`, and validation methods, first invoke `super.method()`, the superclass’s implementation. Don’t modify relationships in [- awakeFromFetch](<nsmanagedobject/awakefromfetch().md>)—see the method description for details.

#### Custom Accessor Methods

Typically, you don’t need to write custom accessor methods for properties that are defined in the entity of a managed object’s corresponding managed object model. If you need to do so, follow the implementation patterns described in Managed Object Accessor Methods in [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075).

Core Data automatically generates accessor methods (and primitive accessor methods) for you. For attributes and to-one relationships, Core Data generates the standard get and set accessor methods; for to-many relationships, Core Data generates the indexed accessor methods as described in [Achieving Basic Key-Value Coding Compliance](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/AccessorConventions.html#//apple_ref/doc/uid/20002174) in [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i). You do however need to declare the accessor methods or use Objective-C properties to suppress compiler warnings. For a full discussion, see Managed Object Accessor Methods in [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075).

#### Custom Instance Variables

By default, `NSManagedObject` stores its properties in an internal structure as objects, and in general Core Data is more efficient working with storage under its own control rather than by using custom instance variables.

`NSManagedObject` provides support for a range of common types for attribute values, including string, date, and number (see [NSAttributeDescription](nsattributedescription.md) for full details). If you want to use types that aren’t supported directly, like colors and C structures, you can either use transformable attributes or create a subclass of `NSManagedObject`.

Sometimes it’s convenient to represent variables as scalars—in drawing applications, for example, where variables represent dimensions and x and y coordinates and are frequently used in calculations. To represent attributes as scalars, you declare instance variables as you do in any other class. You also need to implement suitable accessor methods as described in Managed Object Accessor Methods.

If you define custom instance variables for example to store derived attributes or other transient properties, clean up these variables in [- didTurnIntoFault](<nsmanagedobject/didturnintofault().md>) rather than `dealloc`.

#### Validation Methods

`NSManagedObject` provides consistent hooks for validating property and inter-property values. You typically shouldn’t override [- validateValue:forKey:error:](<nsmanagedobject/validatevalue(__forkey_).md>). Instead implement methods of the form `validate<Key>:error:`, as defined by the NSKeyValueCoding protocol. If you want to validate inter-property values, you can override [- validateForUpdate:](<nsmanagedobject/validateforupdate().md>) and/or related validation methods.

Don’t call `validateValue:forKey:error:` within custom property validation methods—if you do, you create an infinite loop when `validateValue:forKey:error:` is invoked at runtime. If you do implement custom validation methods, don’t call them directly. Instead, call `validateValue:forKey:error:` with the appropriate key. This ensures that any constraints defined in the managed object model are applied.

If you implement custom inter-property validation methods like [- validateForUpdate:](<nsmanagedobject/validateforupdate().md>), call the superclass’s implementation first. This ensures that individual property validation methods are also invoked. If there are multiple validation failures in one operation, collect them in an array and add the array—using the key `NSDetailedErrorsKey`—to the userInfo dictionary in the `NSError` object you return. For an example, see Managed Object Validation.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSFetchRequestResult](nsfetchrequestresult.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [ObservableObject](../combine/observableobject.md)

## Topics

### Creating a Managed Object

- [- initWithEntity:insertIntoManagedObjectContext:](<nsmanagedobject/init(entity_insertinto_).md>) — Initializes a managed object from an entity description and inserts it into the specified managed object context.
- [- initWithContext:](<nsmanagedobject/init(context_).md>) — Initializes a managed object subclass and inserts it into the specified managed object context.

### Getting a Managed Object’s Identity

- [entity](nsmanagedobject/entity-swift.property.md) — The entity description of the managed object.
- [objectID](nsmanagedobject/objectid.md) — The object ID of the managed object.
- [+ entity](<nsmanagedobject/entity().md>) — Returns the entity description that is associated with this subclass.

### Getting State Information

- [managedObjectContext](nsmanagedobject/managedobjectcontext.md) — The managed object context with which the managed object is registered.
- [hasChanges](nsmanagedobject/haschanges.md) — A Boolean value that indicates whether the managed object has been inserted, has been deleted, or has unsaved changes.
- [inserted](nsmanagedobject/isinserted.md) — A Boolean value that indicates whether the managed object has been inserted in a managed object context.
- [updated](nsmanagedobject/isupdated.md) — A Boolean value that indicates whether the managed object has unsaved changes.
- [deleted](nsmanagedobject/isdeleted.md) — A Boolean value that indicates whether the managed object will be deleted during the next save.
- [fault](nsmanagedobject/isfault.md) — A Boolean value that indicates whether the managed object is a fault.
- [faultingState](nsmanagedobject/faultingstate.md) — The faulting state of the managed object.
- [- hasFaultForRelationshipNamed:](<nsmanagedobject/hasfault(forrelationshipnamed_).md>) — Returns a Boolean value that indicates whether the relationship for a given key is a fault.
- [hasPersistentChangedValues](nsmanagedobject/haspersistentchangedvalues.md) — A Boolean value that indicates whether the managed object has persistent changes.

### Managing Change Events

- [contextShouldIgnoreUnmodeledPropertyChanges](nsmanagedobject/contextshouldignoreunmodeledpropertychanges.md) — A Boolean value that indicates whether to mark instances of the class as having changes when an unmodeled property changes.
- [- awakeFromFetch](<nsmanagedobject/awakefromfetch().md>) — Provides an opportunity to add code into the life cycle of the managed object when fufilling it from a fault.
- [- awakeFromInsert](<nsmanagedobject/awakefrominsert().md>) — Provides an opportunity to add code into the life cycle of the managed object when initially creating it.
- [- awakeFromSnapshotEvents:](<nsmanagedobject/awake(fromsnapshotevents_).md>) — Provides an opportunity to add code into the life cycle of the managed object when fulfilling it from a snapshot.
- [- changedValues](<nsmanagedobject/changedvalues().md>) — Returns a dictionary containing the keys and new values of persistent properties with changes since the last fetching or saving of the managed object.
- [- changedValuesForCurrentEvent](<nsmanagedobject/changedvaluesforcurrentevent().md>) — Returns a dictionary containing the keys and new values of persistent properties with changes since the last fetching or saving of the managed object.
- [- committedValuesForKeys:](<nsmanagedobject/committedvalues(forkeys_).md>) — Returns a dictionary of the most recent fetched or saved values of the managed object for the properties of the specified keys.
- [- prepareForDeletion](<nsmanagedobject/preparefordeletion().md>) — Provides an opportunity to add code into the life cycle of the managed object before deleting it.
- [- willSave](<nsmanagedobject/willsave().md>) — Provides an opportunity to add code into the life cycle of the managed object before saving it.
- [- didSave](<nsmanagedobject/didsave().md>) — Provides an opportunity to add code into the life cycle of the managed object after the managed object’s context completes a save operation.
- [- willTurnIntoFault](<nsmanagedobject/willturnintofault().md>) — Provides an opportunity to add code into the life cycle of the managed object before converting it to a fault.
- [- didTurnIntoFault](<nsmanagedobject/didturnintofault().md>) — Provides an opportunity to add code into the life cycle of the managed object after converting it to a fault.
- [fetchRequest()](<nsmanagedobject/fetchrequest().md>) — Returns an initialized fetch request with the entity this subclass represents.

### Supporting Key-Value Coding

- [- valueForKey:](<nsmanagedobject/value(forkey_).md>) — Returns the value for the property specified by `key`.
- [- setValue:forKey:](<nsmanagedobject/setvalue(__forkey_).md>) — Sets the specified property of the managed object to the specified value.
- [- primitiveValueForKey:](<nsmanagedobject/primitivevalue(forkey_).md>) — Returns the value for the specified property from the managed object’s private internal storage .
- [- setPrimitiveValue:forKey:](<nsmanagedobject/setprimitivevalue(__forkey_).md>) — Sets the value of a given property in the managed object’s private internal storage.
- [- objectIDsForRelationshipNamed:](<nsmanagedobject/objectids(forrelationshipnamed_).md>) — Returns the object IDs for all of the managed objects that are in the named relationship.

### Managing Data Validation

- [- validateValue:forKey:error:](<nsmanagedobject/validatevalue(__forkey_).md>) — Validates a property value for a given key.
- [- validateForDelete:](<nsmanagedobject/validatefordelete().md>) — Determines whether the managed object can be deleted in its current state.
- [- validateForInsert:](<nsmanagedobject/validateforinsert().md>) — Determines whether the managed object can be inserted in its current state.
- [- validateForUpdate:](<nsmanagedobject/validateforupdate().md>) — Determines whether the managed object’s current state is valid.
- [Validation error codes](1535452-validation-error-codes.md) — Error codes relating to the validation of managed objects.
- [NSValidationKeyErrorKey](nsvalidationkeyerrorkey.md) — The error key for the attribute that failed to validate.
- [NSValidationObjectErrorKey](nsvalidationobjecterrorkey.md) — The error key for the object that failed to validate.
- [NSValidationPredicateErrorKey](nsvalidationpredicateerrorkey.md) — The error key for the predicate that failed to validate.
- [NSValidationValueErrorKey](nsvalidationvalueerrorkey.md) — The error key for the value that failed to validate.

### Supporting Key-Value Observing

- [- didAccessValueForKey:](<nsmanagedobject/didaccessvalue(forkey_).md>) — Provides support for key-value observing access notification.
- [- observationInfo](<nsmanagedobject/observationinfo().md>) — Returns the observation info of the managed object.
- [- setObservationInfo:](<nsmanagedobject/setobservationinfo(__).md>) — Sets the observation info of the managed object.
- [- willAccessValueForKey:](<nsmanagedobject/willaccessvalue(forkey_).md>) — Provides support for key-value observing access notification.
- [- didChangeValueForKey:](<nsmanagedobject/didchangevalue(forkey_).md>) — Provides an opportunity to respond when a value of a given property has changed.
- [- didChangeValueForKey:withSetMutation:usingObjects:](<nsmanagedobject/didchangevalue(forkey_withsetmutation_using_).md>) — Provides an opportunity to respond when a change was made to a specified to-many relationship.
- [- willChangeValueForKey:](<nsmanagedobject/willchangevalue(forkey_).md>) — Provides an opportunity to respond when a value of a given property is about to change.
- [- willChangeValueForKey:withSetMutation:usingObjects:](<nsmanagedobject/willchangevalue(forkey_withsetmutation_using_).md>) — Provides an opportunity to respond when a change is about to be made to a specified to-many relationship.

### Reinitializing Values

- [NSSnapshotEventType](nssnapshoteventtype.md) — Constants that specify the reason the managed object may need to reinitialize its values.

### Initializers

- [init(entity:insertIntoManagedObjectContext:)](<nsmanagedobject/init(entity_insertintomanagedobjectcontext_).md>)

### Subscripts

- [subscript(_:)](<nsmanagedobject/subscript(__).md>)

## See Also

### Objects and entities

- [NSEntityDescription](nsentitydescription.md) — A description of a Core Data entity.
