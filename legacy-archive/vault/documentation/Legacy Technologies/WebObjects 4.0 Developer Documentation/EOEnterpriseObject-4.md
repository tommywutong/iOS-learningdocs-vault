---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/More/EOEnterpriseObject_m.html
archived_at: '2026-07-18T01:28:41.960809Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOEnterpriseObject-3.md)
[!](EOKeyValueCoding-3.md)

---

# EOEnterpriseObject

---

### Initialization

Enterprise objects are initialized using __initWithEditingContext:classDescription:globalID:__ , which by default simply invokes __init__ . You can place your custom initialization code in __init__ , or you can override __initWithEditingContext:classDescription:globalID:__ to take advantage of the extra information available with this method.

After an enterprise object is created, it receives an __awake...__ message. The particular message depends on whether the object has been fetched from a database or created anew in the application. In the former case, it receives an [__awakeFromFetchInEditingContext:__](EOEnterpriseObject-3.md)message. In the latter, it receives an [__awakeFromInsertionInEditingContext:__](EOEnterpriseObject-3.md)message. The receiver can override either method to perform extra initialization-such as setting default values-based on how it was created.

---

### Change Notification

For the Framework to keep all areas of an application synchronized, enterprise objects must notify their observers when their state changes. Objects do this by invoking [__willChange__](EOEnterpriseObject-3.md)before altering any instance variable or other kind of state. This method informs all observers that the invoker is about to change. See the [EOObserverCenter](EOObserverCenter-2.md) class specification for more information on change notification.

The primary observer of changes in an object is the object's EOEditingContext. EOEditingContext is a subclass of EOObjectStore that manages collections of objects in memory, tracking inserts, deletes, and updates, and propagating changes to the persistent store as needed. You can get the EOEditingContext that contains an object by sending the object an [__editingContext__](EOEnterpriseObject-3.md)message.

---

### Object and Class Metadata Access

One of the larger groups of methods in the EOEnterpriseObject interface provides information about an object's properties. Most of these methods consult an EOClassDescription to provide their answers. An object's [__classDescription__](EOEnterpriseObject-3.md)method returns it's class description. See the [EOClassDescription](EOClassDescription-3.md) class specification for the methods it implements. Methods you can send directly to an enterprise object include [__entityName__](EOEnterpriseObject-3.md), which provides the name of the entity mapped to the receiver's class; [__allPropertyKeys__](EOEnterpriseObject-3.md), which returns the names of all the receiver's class properties, attributes and relationships alike; and [__attributeKeys__](EOEnterpriseObject-3.md), which returns just the names of the attributes.

Some methods return information about relationships. [__toOneRelationshipKeys__](EOEnterpriseObject-3.md)and [__toManyRelationshipKeys__](EOEnterpriseObject-3.md)return the names of the receiver's relationships, while [__isToManyKey:__](EOEnterpriseObject-3.md)tells which kind a particular relationship is. [__deleteRuleForRelationshipKey:__](EOEnterpriseObject-3.md)indicates what should happen to the receiver's relationships when it's deleted. Similarly, [__ownsDestinationObjectsForRelationshipKey:__](EOEnterpriseObject-3.md)indicates what should happen when another object is added to or removed from the receiver's relationship. Another method, [__classDescriptionForDestinationKey:__](EOEnterpriseObject-3.md), returns the EOClassDescription for the objects at the destination of a relationship.

---

### Snapshots

The key-value coding methods define a general mechanism for accessing an object's properties, but you first have to know what those properties are. Sometimes, however, the Framework needs to preserve an object's entire state for later use, whether to undo changes to the object, compare the values that have changed, or just keep a record of the changes. The snapshotting methods provide this service, extracting or setting all properties at once and performing the necessary conversions for proper behavior. __[snapshot](EOEnterpriseObject-3.md)__ returns a dictionary containing all the receiver's properties, and __[updateFromSnapshot:](EOEnterpriseObject-3.md)__ sets properties of the receiver to the values in a snapshot.

A special kind of snapshot is also used to merge an object's uncommitted changes with changes that have been committed to the external store since the object was fetched. These methods are [__changesFromSnapshot__](EOEnterpriseObject-3.md)and [__reapplyChangesFromDictionary:__](EOEnterpriseObject-3.md).

---

### Writing an Enterprise Object Class

Some of the EOEnterpriseObject methods are for enterprise objects to implement or override, and some are meant to be used as defined by the Framework. Many methods are used internally by the Framework and rarely invoked by application code. The tables in this section highlight the methods that you typically override or implement in a custom enterprise object.

| __Creation__ | __Creation__ |
| - init | Designated initializer. |
| - initWithEditingContext:classDescription:globalID: | Optional initializer. |
| [- awakeFromFetchInEditingContext:](EOEnterpriseObject-3.md) | Performs additional initialization after the object is fetched. |
| [- awakeFromInsertionInEditingContext:](EOEnterpriseObject-3.md) | Performs additional initialization after the object is created in memory. |

```
```

| __Key-Value Coding: Accessing Properties and Relationships__ | __Key-Value Coding: Accessing Properties and Relationships__ |
| - set_Key_: | Sets the value for the property named _key_. |
| - _key_ | Retrieves the value for the property named _key_. |
| - addTo_Key_: | Adds an object to a relationship property named _key_. |
| - removeFrom_Key_: | Removes an object from the property named _key_. |
| [- handleTakeValue:forUnboundKey:](EOKeyValueCoding-3.md) | Handles a failure of __[takeValue:forKey:](EOKeyValueCoding-3.md)__ to find a property. |
| [- handleQueryWithUnboundKey:](EOKeyValueCoding-3.md) | Handles a failure of __[valueForKey:](EOKeyValueCoding-3.md)__ to find a property. |
| [- unableToSetNullForKey:](EOKeyValueCoding-3.md) | Handles an attempt to set a non-object property's value to __nil__ . |

```
```

| __Validation__ | __Validation__ |
| - validate_Key_: | Validates a value for the property named _key_. |
| [- validateForDelete](EOValidation-3.md) | Validates all properties before deleting the receiver. |
| [- validateForInsert](EOValidation-3.md) | Validates all properties before inserting the receiver. |
| [- validateForSave](EOValidation-3.md) | Validates all properties before saving the receiver. |
| [- validateForUpdate](EOValidation-3.md) | Validates all properties before updating the receiver. |

```
```

---

[!](EOEnterpriseObject-3.md)
[!](EOKeyValueCoding-3.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
