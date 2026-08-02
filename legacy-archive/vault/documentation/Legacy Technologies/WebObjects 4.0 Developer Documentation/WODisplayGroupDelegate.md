---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/WODisplayGroup.Delegate.html
archived_at: '2026-07-18T01:28:54.912431Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WOActionResults-2.md)

---

# WODisplayGroupDelegate

__Adopted By:__
WODisplayGroup delegate objects

__Declared in:__
WebObjects/WODisplayGroup.h

# Protocol Description

WODisplayGroup offers a number of methods for its delegate to implement; if the delegate does implement them, the WODisplayGroup instances invoke them as appropriate. There are methods that inform the delegate that the EODisplayGroup has fetched, created an object (or failed to create one), inserted or deleted an object, changed the selection, or set a value for a property. There are also methods that request permission from the delegate to perform most of these same actions. The delegate can return YES to permit the action or NO to deny it. See each method's description for more information.

---

## Instance Methods

---

### displayGroup:createObjectFailedForDataSource:

- (void)__displayGroup:__ (WODisplayGroup \*)_aDisplayGroup_
__createObjectFailedForDataSource:__ (id)_aDataSource_

Invoked from [__insertObject: atIndex:__](WODisplayGroup-2.md#apple-gqztimzz) to inform the delegate that _aDisplayGroup_ has failed to create a new object for _aDataSource_. If the delegate doesn't implement this method, the WODisplayGroup fails silently.

---

### displayGroup:didDeleteObject:

- (void)__displayGroup:__ (WODisplayGroup \*)_aDisplayGroup_ __didDeleteObject:__ (id)_anObject_

Informs the delegate that _aDisplayGroup_ has deleted _anObject_.

---

### displayGroup:didFetchObjects:

- (void)__displayGroup:__ (WODisplayGroup \*)_aDisplayGroup_ __didFetchObjects:__ (NSArray \*)_objects_

Informs the delegate that _aDisplayGroup_ has fetched _objects_.

---

### displayGroup:didInsertObject:

- (void)__displayGroup:__ (WODisplayGroup \*)_aDisplayGroup_ __didInsertObject:__ (id)_anObject_

Informs the delegate that _aDisplayGroup_ has inserted _anObject_.

---

### displayGroup:didSetValue:forObject:key:

- (void)__displayGroup:__ (WODisplayGroup \*)_aDisplayGroup___didSetValue:__ (id)_value___forObject:__ (id)_anObject___key:__ (NSString \*)_key_

Informs the delegate that _aDisplayGroup_ has altered a property value of _anObject_. _key_ identifies the property, and _value_ is its new value.

---

### displayGroup:displayArrayForObjects:

- (NSArray \*)__displayGroup:__ (WODisplayGroup \*)_aDisplayGroup___displayArrayForObjects:__ (NSArray \*)_objects_

Invoked from [__updateDisplayedObjects__](WODisplayGroup-2.md#apple-gmzdo), this method allows the delegate to filter and sort _aDisplayGroup_'s array of objects to limit which ones get displayed. _objects_ contains all of _aDisplayGroup_'s objects. The delegate should filter any objects that shouldn't be shown and sort the remainder, returning a new array containing this group of objects. You can use the NSArray methods __filteredArrayUsingQualifier:__  and __sortedArrayUsingKeyOrderingArray:__  to create the new array.

If the delegate doesn't implement this method, the WODisplayGroup uses its own qualifier and sort ordering to update the displayed objects array.

__See also:__
[- __displayedObjects__](WODisplayGroup-2.md#apple-geztsmry), [- __qualifier__](WODisplayGroup-2.md#apple-gm3dimq), [- __sortOrderings__](WODisplayGroup-2.md#apple-gmzdg)

---

### displayGroupDidChangeDataSource:

- (void)__displayGroupDidChangeDataSource:__ (WODisplayGroup \*)_aDisplayGroup_

Informs the delegate that _aDisplayGroup_'s EODataSource (defined in the EOControl framework) has changed.

---

### displayGroupDidChangeSelectedObjects:

- (void)`displayGroupDidChangeSelectedObjects:`(WODisplayGroup \*)_aDisplayGroup_

Informs the delegate that _aDisplayGroup_'s selected objects have changed, regardless of whether the selection indexes have changed.

---

### displayGroupDidChangeSelection:

- (void)__displayGroupDidChangeSelection:__ (WODisplayGroup \*)_aDisplayGroup_

Informs the delegate that _aDisplayGroup_'s selection has changed.

---

### displayGroupShouldFetch:

- (BOOL)__displayGroupShouldFetch:__ (WODisplayGroup \*)_aDisplayGroup_

Allows the delegate to prevent _aDisplayGroup_ from fetching. If the delegate returns YES, _aDisplayGroup_ performs the fetch; if the delegate returns NO, _aDisplayGroup_ abandons the fetch.

---

### displayGroup:shouldChangeSelectionToIndexes:

- (BOOL)__displayGroup:__ (WODisplayGroup \*)_aDisplayGroup_
__shouldChangeSelectionToIndexes:__ (NSArray \*)_newIndexes_

Allows the delegate to prevent a change in selection by _aDisplayGroup_. _newIndexes_ is the proposed new selection. If the delegate returns YES, the selection changes; if the delegate returns NO, the selection remains as it is.

---

### displayGroup:shouldDeleteObject:

- (BOOL)__displayGroup:__ (WODisplayGroup \*)_aDisplayGroup_ __shouldDeleteObject:__ _anObject_

Allows the delegate to prevent _aDisplayGroup_ from deleting _anObject_. If the delegate returns YES, _anObject_ is deleted; if the delegate returns NO, the deletion is abandoned.

---

### displayGroup:shouldInsertObject:atIndex:

- (BOOL)__displayGroup:__ (WODisplayGroup \*)_aDisplayGroup___shouldInsertObject:__ _anObject___atIndex:__ (unsigned int)_anIndex_

Allows the delegate to prevent [__redisplay__](WODisplayGroup-2.md#apple-giydo) from inserting _anObject_ at _anIndex_. If the delegate returns YES, _anObject_ is inserted; if the delegate returns NO, the insertion is abandoned.

---

### displayGroup:shouldRedisplayForChangesInEditingContext:

- (BOOL)__displayGroup:__ (WODisplayGroup \*)_aDisplayGroup_ __shouldRedisplayForEditingContextChangeNotification:__ (NSNotification \*)_aNotification_

Invoked whenever _aDisplayGroup_ receives an EOObjectsChangedInEditingContextNotification, this method allows the delegate to suppress redisplay based on the nature of the change that has occurred. If the delegate returns YES, _aDisplayGroup_ redisplays; if it returns NO, _aDisplayGroup_ doesn't.

__See also:__
[- __redisplay__](WODisplayGroup-2.md#apple-giydo)

---

### displayGroup:shouldRefetchForInvalidatedAllObjectsNotification:

- (BOOL)__displayGroup:__ (WODisplayGroup \*)_aDisplayGroup_ __shouldRefetchForInvalidatedAllObjectsNotification:__ (NSNotification \*)_aNotification_

Invoked whenever _aDisplayGroup_ receives an EOInvalidatedAllObjectsInStoreNotification, this method allows the delegate to suppress the refetching of the invalidated objects. If the delegate returns YES, _aDisplayGroup_ immediately fetches its objects. If the delegate returns NO, _aDisplayGroup_ doesn't immediately fetch, instead delaying until absolutely necessary.

__See also:__
[- __redisplay__](WODisplayGroup-2.md#apple-giydo)

****

---

[!](WOActionResults-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
