---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EODisplayGroupDelegate.html
archived_at: '2026-07-18T01:28:47.361169Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EODisplayGroup-2.md)
[!](EOGenericControlAssociation-2.md)

---

# EODisplayGroupDelegate

(informal protocol)

NSObject

__Declared in:__
EOInterface/EODisplayGroup.h

Category Description

The EODisplayGroupDelegate informal protocol defines methods that an EODisplayGroup can invoke in its delegate. Delegates are not required to provide implementations for all of the methods in the informal protocol. Instead, declare and implement any subset of the methods declared in the informal protocol that you need, and use the EODisplayGroup method [`setDelegate:`](../Classes/EODisplayGroup.md#apple-ge2dsmy) method to assign your object as the delegate. A display group can determine if the delegate doesn't implement a delegate method and only attempts to invoke the methods the delegate actually implements.

---

## Method Types

**Fetching objects**

**[- displayGroupShouldFetch:](#apple-gqzdena)

**[- displayGroup:didFetchObjects:](#apple-gqydgoi)

**[- displayGroup:shouldRefetchForInvalidatedAllObjectsNotification:](#apple-gqztimi)******

**Inserting, updating, and deleting objects**

**[- displayGroup:shouldInsertObject:atIndex:](#apple-gqzdkmy)

**[- displayGroup:didInsertObject:](#apple-gqydmoa)

**[- displayGroup:createObjectFailedForDataSource:](#apple-gm4tema)

**[- displayGroup:didSetValue:forObject:key:](#apple-gqydsni)

**[- displayGroup:shouldDeleteObject:](#apple-gqytmmq)

**[- displayGroup:didDeleteObject:](#apple-gqydcnq)************

**Managing the display**

**[- displayGroup:shouldDisplayAlertWithTitle:message:](#apple-gqytsni)

**[- displayGroup:shouldRedisplayForChangesInEditingContext:](#apple-gqzdqmi)

**[- displayGroup:displayArrayForObjects:](#apple-gm4tkma)******

**Managing the selection**

**[- displayGroup:shouldChangeSelectionToIndexes:](#apple-gqytemq)

**[- displayGroupDidChangeSelection:](#apple-gm4tsna)

**[- displayGroupDidChangeSelectedObjects:](#apple-gm4tomq)******

**Changing the data source**

**[- displayGroupDidChangeDataSource:](#apple-gm4dkoa)**

---

## Instance Methods

---

### displayGroup:createObjectFailedForDataSource:

- (void)`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_`createObjectFailedForDataSource:`(EODataSource \*)_aDataSource_

Invoked from `[insertObjectAtIndex:](../Classes/EODisplayGroup.md#apple-gi3tqma)` to inform the delegate that _aDisplayGroup_ has failed to create a new object for _aDataSource_. If the delegate doesn't implement this method, the EODisplayGroup instead runs an alert panel to inform the user of the failure.

---

### displayGroupDidChangeDataSource:

- (void)`displayGroupDidChangeDataSource:`(EODisplayGroup \*)_aDisplayGroup_

Informs the delegate that _aDisplayGroup_'s EODataSource has changed.

---

### displayGroupDidChangeSelectedObjects:

- (void)`displayGroupDidChangeSelectedObjects:`(EODisplayGroup \*)_aDisplayGroup_

Informs the delegate that _aDisplayGroup_'s set of selected objects has changed, regardless of whether the selection indexes have changed.

---

### displayGroupDidChangeSelection:

- (void)`displayGroupDidChangeSelection:`(EODisplayGroup \*)_aDisplayGroup_

Informs the delegate that _aDisplayGroup_'s selection has changed.

---

### displayGroup:didDeleteObject:

- (void)`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_`didDeleteObject:`(id)_anObject_

Informs the delegate that _aDisplayGroup_ has deleted _anObject_.

---

### displayGroup:didFetchObjects:

- (void)`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_`didFetchObjects:`(NSArray \*)_objects_

Informs the delegate that _aDisplayGroup_ has fetched _objects_.

---

### displayGroup:didInsertObject:

- (void)`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_`didInsertObject:`(id)_anObject_

Informs the delegate that _aDisplayGroup_ has inserted _anObject_.

---

### displayGroup:didSetValue:forObject:key:

- (void)`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_`didSetValue:`(id)_value_`forObject:`(id)_anObject_`key:`(NSString \*)_key_

Informs the delegate that _aDisplayGroup_ has altered a property value of _anObject_. _key_ identifies the property, and _value_ is its new value.

---

### displayGroup:displayArrayForObjects:

- (NSArray \*)`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_`displayArrayForObjects:`(NSArray \*)_objects_

Invoked from `[updateDisplayedObjects](../Classes/EODisplayGroup.md#apple-ge2tkny)`, this method allows the delegate to filter and sort _aDisplayGroup_'s array of objects to limit which ones get displayed. _objects_ contains all of _aDisplayGroup_'s objects. The delegate should filter any objects that shouldn't be shown and sort the remainder, returning a new array containing this group of objects. You can use the added NSArray methods `filteredArrayUsingQualifier:` and `sortedArrayUsingKeyOrderArray:` to create the new array.

If the delegate doesn't implement this method, the EODisplayGroup uses its own qualifier and sort ordering to update its displayed objects array.

__See also:__
[- `sortOrderings`](../Classes/EODisplayGroup.md#apple-ge2tkmy), [- `qualifier`](../Classes/EODisplayGroup.md#apple-ge2dema), [- `displayedObjects`](../Classes/EODisplayGroup.md#apple-geztmmi)

---

### displayGroup:shouldChangeSelectionToIndexes:

- (BOOL)`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_`shouldChangeSelectionToIndexes:`(NSArray \*)_newIndexes_

Allows the delegate to prevent a change in selection by _aDisplayGroup_. _newIndexes_ is the proposed new selection, an array of NSNumbers . If the delegate returns YES, the selection changes; if the delegate returns NO, the selection remains as it is.

---

### displayGroup:shouldDeleteObject:

- (BOOL)`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_`shouldDeleteObject:`(id)_anObject_

Allows the delegate to prevent _aDisplayGroup_ from deleting _anObject_. If the delegate returns YES, _anObject_ is deleted; if the delegate returns NO, the deletion is abandoned.

---

### displayGroup:shouldDisplayAlertWithTitle:message:

- (BOOL)`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_`shouldDisplayAlertWithTitle:`(NSString \*)_title_`message:`(NSString \*)_message_

Allows the delegate to prevent _aDisplayGroup_ from displaying an attention panel with _title_ and _message_. The delegate can return YES to allow _aDisplayGroup_ to display the panel, or NO to prevent it from doing so (perhaps displaying a different attention panel).

---

### displayGroupShouldFetch:

- (BOOL)`displayGroupShouldFetch:`(EODisplayGroup \*)_aDisplayGroup_

Allows the delegate to prevent _aDisplayGroup_ from fetching. If the delegate returns YES, _aDisplayGroup_ performs the fetch; if the delegate returns NO, _aDisplayGroup_ abandons the fetch.

---

### displayGroup:shouldInsertObject:atIndex:

- (BOOL)`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_`shouldInsertObject:`(id)_anObject_`atIndex:`(unsigned int)_anIndex_

Allows the delegate to prevent _aDisplayGroup_ from inserting _anObject_ at _anIndex_. If the delegate returns YES, _anObject_ is inserted; if the delegate returns NO, the insertion is abandoned.

---

### displayGroup:shouldRedisplayForChangesInEditingContext:

- (BOOL)`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_ `shouldRedisplayForEditingContextChangeNotification:`(NSNotification \*)_aNotification_

Invoked whenever _aDisplayGroup_ receives an EOObjectsChangedInEditingContextNotification, this method allows the delegate to suppress redisplay based on the nature of the change that has occurred. If the delegate returns YES, _aDisplayGroup_ redisplays; if it returns NO, _aDisplayGroup_ doesn't. _aNotification_ supplies the EOEditingContext that has changed, as well as which objects have changed and how. See the EOEditingContext class specification for information on EOObjectsChangedInEditingContextNotification.

__See also:__
[- `redisplay`](../Classes/EODisplayGroup.md#apple-ge2dena)

---

### displayGroup:shouldRefetchForInvalidatedAllObjectsNotification:

- (BOOL)`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_ `shouldRefetchForInvalidatedAllObjectsNotification:`(NSNotification \*)_aNotification_

Invoked whenever _aDisplayGroup_ receives an EOInvalidatedAllObjectsInStoreNotification, this method allows the delegate to suppress refetching of the invalidated objects. If the delegate returns YES, _aDisplayGroup_ immediately refetches its objects. If the delegate returns NO, _aDisplayGroup_ doesn't immediately fetch, instead delaying until absolutely necessary. _aNotification_ is an NSNotification. See the EOObjectStore and EOEditingContext class specifications for information on this notification.

---

[!](EODisplayGroup-2.md)
[!](EOGenericControlAssociation-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
