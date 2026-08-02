---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/WODisplayGroup.Delegate.html
archived_at: '2026-07-18T01:28:52.925473Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](WOActionResults.md)

---

# WODisplayGroup.Delegate

WODisplayGroup delegate objects

__Inherits From:__
com.apple.yellow.webobjects

WODisplayGroup offers a number of methods for its delegate to implement; if the delegate does implement them, the WODisplayGroup instances invoke them as appropriate. There are methods that inform the delegate that the EODisplayGroup has fetched, created an object (or failed to create one), inserted or deleted an object, changed the selection, or set a value for a property. There are also methods that request permission from the delegate to perform most of these same actions. The delegate can return true to permit the action or false to deny it. See each method's description for more information.

---

## Instance Methods

---

### createObjectFailedForDataSource

public abstract void `createObjectFailedForDataSource`(
WODisplayGroup _aDisplayGroup_,
java.lang.Object _aDataSource_)

Invoked from [`insertNewObjectAtIndex`](../Classes/WODisplayGroup.md#apple-ge2dambt) to inform the delegate that _aDisplayGroup_ has failed to create a new object for _aDataSource_. If the delegate doesn't implement this method, the WODisplayGroup fails silently.

---

### didDeleteObject

public abstract void `didDeleteObject`(
WODisplayGroup _aDisplayGroup_,
java.lang.Object _anObject_)

Informs the delegate that _aDisplayGroup_ has deleted _anObject_.

---

### didFetchObjects

public abstract void `didFetchObjects`(
WODisplayGroup _aDisplayGroup_,
NSArray _objects_)

Informs the delegate that _aDisplayGroup_ has fetched _objects_.

---

### didInsertObject

public abstract void `didInsertObject`(
WODisplayGroup _aDisplayGroup_,
java.lang.Object _anObject_)

Informs the delegate that _aDisplayGroup_ has inserted _anObject_.

---

### didSetValueForObjectWithKey

public abstract void `didSetValueForObjectWithKey`(
WODisplayGroup _aDisplayGroup_,
java.lang.Object _value_,
java.lang.Object _anObject_,
java.lang.String _key_)

Informs the delegate that _aDisplayGroup_ has altered a property value of _anObject_. _key_ identifies the property, and _value_ is its new value.

---

### displayArrayForObjects

public abstract NSArray `displayArrayForObjects`(
WODisplayGroup _aDisplayGroup_,
NSArray _objects_)

Invoked from [`updateDisplayedObjects`](../Classes/WODisplayGroup.md#apple-gmzdo), this method allows the delegate to filter and sort _aDisplayGroup_'s array of objects to limit which ones get displayed. _objects_ contains all of _aDisplayGroup_'s objects. The delegate should filter any objects that shouldn't be shown and sort the remainder, returning a new array containing this group of objects. You can use the NSArray methods __filteredArrayUsingQualifier__
and __sortedArrayUsingKeyOrderingArray__
to create the new array.

If the delegate doesn't implement this method, the WODisplayGroup uses its own qualifier and sort ordering to update the displayed objects array.

__See also:__
[`displayedObjects`](../Classes/WODisplayGroup.md#apple-geztsmry), [`qualifier`](../Classes/WODisplayGroup.md#apple-gm3dimq), [`sortOrderings`](../Classes/WODisplayGroup.md#apple-gmzdg)

---

### displayGroupDidChangeDataSource

public abstract void `displayGroupDidChangeDataSource`(
WODisplayGroup _aDisplayGroup_)

Informs the delegate that _aDisplayGroup_'s EODataSource (defined in the EOControl framework) has changed.

---

### displayGroupDidChangeSelectedObjects

public abstract void `displayGroupDidChangeSelectedObjects`(WODisplayGroup _aDisplayGroup_)

Informs the delegate that _aDisplayGroup_'s selected objects have changed, regardless of whether the selection indexes have changed.

---

### displayGroupDidChangeSelection

public abstract void `displayGroupDidChangeSelection`(WODisplayGroup _aDisplayGroup_)

Informs the delegate that _aDisplayGroup_'s selection has changed.

---

### displayGroupShouldFetch

public abstract boolean `displayGroupShouldFetch`(WODisplayGroup _aDisplayGroup_)

Allows the delegate to prevent _aDisplayGroup_ from fetching. If the delegate returns true, _aDisplayGroup_ performs the fetch; if the delegate returns false, _aDisplayGroup_ abandons the fetch.

---

### shouldChangeSelectionToIndexes

public abstract boolean `shouldChangeSelectionToIndexes`(
WODisplayGroup _aDisplayGroup_,
NSArray _newIndexes_)

Allows the delegate to prevent a change in selection by _aDisplayGroup_. _newIndexes_ is the proposed new selection. If the delegate returns true, the selection changes; if the delegate returns false, the selection remains as it is.

---

### shouldDeleteObject

public abstract boolean `shouldDeleteObject`(
WODisplayGroup _aDisplayGroup_,
java.lang.Object _anObject_)

Allows the delegate to prevent _aDisplayGroup_ from deleting _anObject_. If the delegate returns true, _anObject_ is deleted; if the delegate returns false, the deletion is abandoned.

---

### shouldInsertObject

public abstract boolean `shouldInsertObject`(
WODisplayGroup _aDisplayGroup_,
java.lang.Object _anObject_,
int _anIndex_)

Allows the delegate to prevent [`redisplay`](../Classes/WODisplayGroup.md#apple-giydo) from inserting _anObject_ at _anIndex_. If the delegate returns true, _anObject_ is inserted; if the delegate returns false, the insertion is abandoned.

---

### shouldRedisplayForChangesInEditingContext

public abstract boolean `shouldRedisplayForChangesInEditingContext`(
WODisplayGroup _aDisplayGroup_,
NSNotification _aNotification_)

Invoked whenever _aDisplayGroup_ receives an EOObjectsChangedInEditingContextNotification, this method allows the delegate to suppress redisplay based on the nature of the change that has occurred. If the delegate returns true, _aDisplayGroup_ redisplays; if it returns false, _aDisplayGroup_ doesn't.

__See also:__
[`redisplay`](../Classes/WODisplayGroup.md#apple-giydo)

---

### shouldRefetchForInvalidatedAllObjectsNotification

public abstract boolean `shouldRefetchForInvalidatedAllObjects`(
WODisplayGroup _aDisplayGroup_,
NSNotification _aNotification_)

Invoked whenever _aDisplayGroup_ receives an EOInvalidatedAllObjectsInStoreNotification, this method allows the delegate to suppress the refetching of the invalidated objects. If the delegate returns true, _aDisplayGroup_ immediately fetches its objects. If the delegate returns false, _aDisplayGroup_ doesn't immediately fetch, instead delaying until absolutely necessary.

__See also:__
[`redisplay`](../Classes/WODisplayGroup.md#apple-giydo)

****

---

[!](WOActionResults.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
