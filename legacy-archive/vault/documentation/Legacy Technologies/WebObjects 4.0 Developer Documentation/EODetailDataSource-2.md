---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EODetailDataSource.html
archived_at: '2026-07-18T01:28:35.563677Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EODelayedObserverQueue-4.md)
[!](EOEditingContext-3.md)

---

# EODetailDataSource

__Inherits From:__
[EODataSource](EODataSource-3.md) : NSObject

__Conforms To:__ NSObject (NSObject)

__Declared in:__ EOControl/EODetailDataSource.h

EODetailDataSource defines a data source for use in master-detail configurations, where operations in the detail data source are applied directly to properties of a master object. EODetailDataSource implements the standard __fetchObjects__ , __insertObject:__ , and __deleteObject:__ methods to operate on a relationship property of its master object, so it works for any concrete subclass of EODataSource, including another EODetailDataSource (for a chain of three master and detail data sources).

To set up an EODetailDataSource programmatically, you typically create it by sending a [__dataSourceQualifiedByKey:__](EODataSource-3.md)message to the master data source, then establish the master object with a __qualifyWithRelationshipKey:ofObject:__ message. The latter method records the name of a relationship for a particular object to resolve in __fetchObjects__ and to modify in __insertObject:__ , and __deleteObject:__ . These three methods then manipulate the relationship property of the master object to perform the operations requested. See the individual method descriptions for more information.

**Creating instances**

**- initWithMasterClassDescription:detailKey:

**- initWithMasterDataSource:detailKey:****

**Qualifying instances**

**- qualifyWithRelationshipKey:ofObject:**

**Examining instances**

**- masterDataSource

**- detailKey

**- masterObject******

**Accessing the master class description**

**- masterClassDescription

**- setMasterClassDescription:****

**Accessing the objects**

**- fetchObjects**

**Inserting and deleting objects**

**- insertObject:

**- deleteObject:****

**Accessing the master editing context**

**- editingContext**

---

#### deleteObject:

- (void)__deleteObject:__ (id)_anObject_

Sends a __[removeObject:fromPropertyWithKey:](EORelationshipManipulation-2.md)__ message (defined in the [EORelationshipManipulation](EORelationshipManipulation-2.md) informal protocol) to the master object with _anObject_ and the receiver's detail key as the arguments. Raises an NSInternalInconsistencyException if there's no master object or no detail key set.

---

#### detailKey

__- (NSString \*)detailKey__

Returns the name of the relationship for which the receiver provides objects, as provided to __initWithMasterDataSource:detailKey:__ or as set in __qualifyWithRelationshipKey:ofObject:__ . If none has been set yet, returns __nil__ .

---

#### editingContext

__-__ (EOEditingContext \*)`editingContext`

Returns the EOEditingContext of the master object, or `nil` if there isn't one.

---

#### fetchObjects

- (NSArray \*)__fetchObjects__

Sends [__valueForKey:__](EOKeyValueCoding-3.md)(defined in the [EOKeyValueCoding](EOKeyValueCoding-3.md) informal protocol) to the master object with the receiver's detail key as the argument, constructs an array for the returned object or objects, and returns it. Returns an empty array if there's no master object, or returns an array containing the master object itself if no detail key is set.

---

#### initWithMasterClassDescription:detailKey:

- `initWithMasterClassDescription:`(EOClassDescription \*)_masterClassDescription_`detailKey:`(NSString \*)_relationshipKey_

Initializes a newly allocated EODetailDataSource to provide objects based on a relationship of objects in the master object associated with _masterClassDescription_. Invokes __qualifyWithRelationshipKey:ofObject:__ with _relationshipKey_ specified as the relationship key and `nil` specified as the object. The receiver initially has no master object selected; to select one, use __qualifyWithRelationshipKey:ofObject:__ . This is the designated initializer for the EODetailDataSource class. Returns __self__ .

__See also:__ - __masterClassDescription__ , - __detailKey__

---

#### initWithMasterDataSource:detailKey:

- (id)__initWithMasterDataSource:__ (EODataSource \*)_masterDataSource___detailKey:__ (NSString \*)_relationshipKey_

Initializes a newly allocated EODetailDataSource to provide objects based on a relationship of objects in _masterDataSource_ named by _relationshipKey_. Invokes __initWithMasterClassDescription:detailKey:__ with `nil` specified for the class description and _relationshipKey_ specified as the detail key. The receiver initially has no master object selected; to select one, use __qualifyWithRelationshipKey:ofObject:__ . Returns __self__ .

__See also:__ - __masterDataSource__ , - __detailKey__

---

#### insertObject:

- (void)__insertObject:__ (id)_anObject_

Sends an [__addObject:toBothSidesOfRelationshipWithKey:__](EORelationshipManipulation-2.md)message (defined in the [EORelationshipManipulation](EORelationshipManipulation-2.md) informal protocol) to the master object with _anObject_ and the receiver's detail key as the arguments. Raises an NSInternalInconsistencyException if there's no master object or no detail key set.

---

#### masterClassDescription

- (EOClassDescription \*)`masterClassDescription`

Returns the EOClassDescription of the receiver's master object.

__See also:__ - __setMasterClassDescription:__ , - initWithMasterClassDescription:detailKey:

---

#### masterDataSource

- (EODataSource \*)__masterDataSource__

Returns the receiver's master data source.

__See also:__ - __detailKey__ , - initWithMasterDataSource:detailKey:

---

#### masterObject

- (id)__masterObject__

Returns the object in the master data source for which the receiver provides objects. You can change this with a __qualifyWithRelationshipKey:ofObject:__ message.

__See also:__ - __detailKey__

---

#### qualifyWithRelationshipKey:ofObject:

- (void)__qualifyWithRelationshipKey:__ (NSString \*)_relationshipKey___ofObject:__ (id)_masterObject_

Configures the receiver to provide objects based on the relationship of _masterObject_ named by _relationshipKey_. _relationshipKey_ can be different from the one used with __initWithMasterDataSource:detailKey:__ , which changes the relationship the receiver operates on. If _masterObject_ is __nil__ , this method causes the receiver to return an empty array when sent a __fetchObjects__ message.

__See also:__ - __detailKey__

---

#### setMasterClassDescription:

- (void)`setMasterClassDescription:`(EOClassDescription \*)_classDescription_

Assigns _classDescription_ as the EOClassDescription for the receiver's master object.

__See also:__ - __masterClassDescription__

---

[!](EODelayedObserverQueue-4.md)
[!](EOEditingContext-3.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
