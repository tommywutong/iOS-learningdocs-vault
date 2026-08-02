---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/Concepts/EOEnterpriseObjectConcept.html
archived_at: '2026-07-15T08:13:47.520788Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Protocols/Art/up.gif)](../../EOControlTOC.md)

# EOEnterpriseObject.Concepts

## Initialization

The Framework creates enterprise objects with a constructor of the following form:

```
public MyClass(
EOEditingContext anEditingContext,
EOClassDescription classDescription,
EOGlobalID globalID)
```

This constructor should create a new instance of your enterprise object class with the provided arguments and it can perform any custom initialization that you require. Enterprise objects created in a Java client and enterprise objects created on the server require this constructor.

After an enterprise object is created, it receives an __awake...__ message. The particular message depends on whether the object has been fetched from a database or created anew in the application. In the former case, it receives an awakeFromFetch message. In the latter, it receives an awakeFromInsertion message. The receiver can override either method to perform extra initialization-such as setting default values-based on how it was created.

## Change Notification

For the Framework to keep all areas of an application synchronized, enterprise objects must notify their observers when their state changes. Objects do this by invoking willChange before altering any instance variable or other kind of state. This method informs all observers that the invoker is about to change. See the EOObserverCenter class specification for more information on change notification.

The primary observer of changes in an object is the object's EOEditingContext. EOEditingContext is a subclass of EOObjectStore that manages collections of objects in memory, tracking inserts, deletes, and updates, and propagating changes to the persistent store as needed. You can get the EOEditingContext that contains an object by sending the object an editingContext message.

## Object and Class Metadata Access

One of the larger groups of methods in the EOEnterpriseObject interface provides information about an object's properties. Most of these methods consult an EOClassDescription to provide their answers. An object's classDescription method returns it's class description. See the EOClassDescription class specification for the methods it implements. Methods you can send directly to an enterprise object include entityName, which provides the name of the entity mapped to the receiver's class; allPropertyKeys, which returns the names of all the receiver's class properties, attributes and relationships alike; and attributeKeys, which returns just the names of the attributes.

Some methods return information about relationships. toOneRelationshipKeys and toManyRelationshipKeys return the names of the receiver's relationships, while isToManyKey: tells which kind a particular relationship is. deleteRuleForRelationshipKey indicates what should happen to the receiver's relationships when it's deleted. Similarly, ownsDestinationObjectsForRelationshipKey indicates what should happen when another object is added to or removed from the receiver's relationship. Another method, classDescriptionForDestinationKey, returns the EOClassDescription for the objects at the destination of a relationship.

## Snapshots

The key-value coding methods define a general mechanism for accessing an object's properties, but you first have to know what those properties are. Sometimes, however, the Framework needs to preserve an object's entire state for later use, whether to undo changes to the object, compare the values that have changed, or just keep a record of the changes. The snapshotting methods provide this service, extracting or setting all properties at once and performing the necessary conversions for proper behavior. snapshot returns a dictionary containing all the receiver's properties, and updateFromSnapshot sets properties of the receiver to the values in a snapshot.

A special kind of snapshot is also used to merge an object's uncommitted changes with changes that have been committed to the external store since the object was fetched. These methods are changesFromSnapshot and reapplyChangesFromDictionary.

## Writing an Enterprise Object Class

Some of the EOEnterpriseObject methods are for enterprise objects to implement or override, and some are meant to be used as defined by the Framework. Many methods are used internally by the Framework and rarely invoked by application code. The tables in this section highlight the methods that you typically override or implement in a custom enterprise object.

|  |  |
| --- | --- |
| __Creation__ |  |
| _MyClass_( `EOEditingContext`, `EOClassDescription`, `EOGlobalID`) | The framework creates enterprise objects with this method if it exists. |
| awakeFromFetch | Performs additional initialization after the object is fetched. |
| awakeFromInsertion | Performs additional initialization after the object is created in memory. |

|  |  |
| --- | --- |
| __Key-Value Coding: Accessing Properties and Relationships__ |  |
| _setKey_ | Sets the value for the property named _key_. |
| _key_ | Retrieves the value for the property named _key_. |
| _addToKey_ | Adds an object to a relationship property named _key_. |
| _removeFromKey_ | Removes an object from the property named _key_. |
| handleTakeValueForUnboundKey | Handles a failure of takeValueForKey to find a property. |
| handleQueryWithUnboundKey | Handles a failure of valueForKey to find a property. |
| unableToSetNullForKey | Handles an attempt to set a non-object property's value to __null__. |

|  |  |
| --- | --- |
| __Validation__ |  |
| _validateKey_ | Validates a value for the property named _key_. |
| validateForDelete | Validates all properties before deleting the receiver. |
| validateForInsert | Validates all properties before inserting the receiver. |
| validateForSave | Validates all properties before saving the receiver. |
| validateForUpdate | Validates all properties before updating the receiver. |

© 2001 Apple Computer, Inc. (Last Published April 23, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Protocols/Art/up.gif)](../../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
