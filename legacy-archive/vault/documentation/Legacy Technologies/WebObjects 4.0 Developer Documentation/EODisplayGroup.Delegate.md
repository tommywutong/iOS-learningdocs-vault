---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EODisplayGroupDelegate.html
archived_at: '2026-07-18T01:28:44.803126Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOViewLayout.md)

---

# EODisplayGroup.Delegate

__Inherits From:__
com.apple.yellow.eointerface

The EODisplayGroup.Delegate interface defines methods that an EODisplayGroup can invoke in its delegate. Delegates are not required to provide implementations for all of the methods in the interface, and you don't have to use the `implements` keyword to specify that the object implements the Delegates interface. Instead, declare and implement any subset of the methods declared in the interface that you need, and use the EODisplayGroup method [`setDelegate`](../Classes/EODisplayGroup.md#apple-ge2dsmy) method to assign your object as the delegate. A display group can determine if the delegate doesn't implement a delegate method and only attempts to invoke the methods the delegate actually implements.

---

## Method Types

**Fetching objects**

**[displayGroupShouldFetch](#apple-gqzdena)

**[displayGroupDidFetchObjects](#apple-gqydgoi)

**[displayGroupShouldRefetch](#apple-gqztimi)******

**Inserting, updating, and deleting objects**

**[displayGroupShouldInsertObject](#apple-gqzdkmy)

**[displayGroupDidInsertObject](#apple-gqydmoa)

**[displayGroupCreateObjectFailed](#apple-gm4tema)

**[displayGroupDidSetValueForObject](#apple-gqydsni)

**[displayGroupShouldDeleteObject](#apple-gqytmmq)

**[displayGroupDidDeleteObject](#apple-gqydcnq)************

**Managing the display**

**[displayGroupShouldDisplayAlert](#apple-gqytsni)

**[displayGroupShouldRedisplay](#apple-gqzdqmi)

**[displayGroupDisplayArrayForObjects](#apple-gm4tkma)******

**Managing the selection**

**[displayGroupShouldChangeSelection](#apple-gqytemq)

**[displayGroupDidChangeSelection](#apple-gm4tsna)

**[displayGroupDidChangeSelectedObjects](#apple-gm4tomq)******

**Changing the data source**

**[displayGroupDidChangeDataSource](#apple-gm4dkoa)**

---

## Instance Methods

---

### displayGroupCreateObjectFailed

public abstract void `displayGroupCreateObjectFailed`(
EODisplayGroup _aDisplayGroup_,
com.apple.yellow.eocontrol.EODataSource _aDataSource_)

Invoked from `[insertNewObjectAtIndex](../Classes/EODisplayGroup.md#apple-gi3tqma)` to inform the delegate that _aDisplayGroup_ has failed to create a new object for _aDataSource_. If the delegate doesn't implement this method, the EODisplayGroup instead runs an alert panel to inform the user of the failure.

---

### displayGroupDidChangeDataSource

public abstract void `displayGroupDidChangeDataSource`(
EODisplayGroup _aDisplayGroup_)

Informs the delegate that _aDisplayGroup_'s EODataSource has changed.

---

### displayGroupDidChangeSelectedObjects

public abstract void `displayGroupDidChangeSelectedObjects`(
EODisplayGroup _aDisplayGroup_)

Informs the delegate that _aDisplayGroup_'s set of selected objects has changed, regardless of whether the selection indexes have changed.

---

### displayGroupDidChangeSelection

public abstract void `displayGroupDidChangeSelection`(
EODisplayGroup _aDisplayGroup_)

Informs the delegate that _aDisplayGroup_'s selection has changed.

---

### displayGroupDidDeleteObject

public abstract void `displayGroupDidDeleteObject`(
EODisplayGroup _aDisplayGroup_,
java.lang.Object _anObject_)

Informs the delegate that _aDisplayGroup_ has deleted _anObject_.

---

### displayGroupDidFetchObjects

public abstract void `displayGroupDidFetchObjects`(
EODisplayGroup _aDisplayGroup_,
com.apple.yellow.foundation.NSArray _objects_)

Informs the delegate that _aDisplayGroup_ has fetched _objects_.

---

### displayGroupDidInsertObject

public abstract void `displayGroupDidInsertObject`(
EODisplayGroup _aDisplayGroup_,
java.lang.Object _anObject_)

Informs the delegate that _aDisplayGroup_ has inserted _anObject_.

---

### displayGroupDidSetValueForObject

public abstract void `displayGroupDidSetValueForObject`(
EODisplayGroup _aDisplayGroup_,
java.lang.Object _value_,
java.lang.Object _anObject_,
java.lang.String _key_)

Informs the delegate that _aDisplayGroup_ has altered a property value of _anObject_. _key_ identifies the property, and _value_ is its new value.

---

### displayGroupDisplayArrayForObjects

public abstract com.apple.yellow.foundation.NSArray `displayGroupDisplayArrayForObjects`(
EODisplayGroup _aDisplayGroup_,
com.apple.yellow.foundation.NSArray _objects_)

Invoked from `[updateDisplayedObjects](../Classes/EODisplayGroup.md#apple-ge2tkny)`, this method allows the delegate to filter and sort _aDisplayGroup_'s array of objects to limit which ones get displayed. _objects_ contains all of _aDisplayGroup_'s objects. The delegate should filter any objects that shouldn't be shown and sort the remainder, returning a new array containing this group of objects. You can use the added NSArray methods `filteredArrayUsingQualifier:` and `sortedArrayUsingKeyOrderArray:` to create the new array.

If the delegate doesn't implement this method, the EODisplayGroup uses its own qualifier and sort ordering to update its displayed objects array.

__See also:__
[`sortOrderings`](../Classes/EODisplayGroup.md#apple-ge2tkmy), [`qualifier`](../Classes/EODisplayGroup.md#apple-ge2dema), [`displayedObjects`](../Classes/EODisplayGroup.md#apple-geztmmi)

---

### displayGroupShouldChangeSelection

public abstract boolean `displayGroupShouldChangeSelection`(
EODisplayGroup _aDisplayGroup_, com.apple.yellow.foundation.NSArray _newIndexes_)

Allows the delegate to prevent a change in selection by _aDisplayGroup_. _newIndexes_ is the proposed new selection, an array of NSNumbers . If the delegate returns `true`, the selection changes; if the delegate returns `false`, the selection remains as it is.

---

### displayGroupShouldDeleteObject

public abstract boolean `displayGroupShouldDeleteObject`(
EODisplayGroup _aDisplayGroup_,
java.lang.Object _anObject_)

Allows the delegate to prevent _aDisplayGroup_ from deleting _anObject_. If the delegate returns `true`, _anObject_ is deleted; if the delegate returns `false`, the deletion is abandoned.

---

### displayGroupShouldDisplayAlert

public abstract boolean `displayGroupShouldDisplayAlert`(
EODisplayGroup _aDisplayGroup_,
java.lang.String _title_,
java.lang.String _message_)

Allows the delegate to prevent _aDisplayGroup_ from displaying an attention panel with _title_ and _message_. The delegate can return `true` to allow _aDisplayGroup_ to display the panel, or `false` to prevent it from doing so (perhaps displaying a different attention panel).

---

### displayGroupShouldFetch

public abstract boolean `displayGroupShouldFetch`(
EODisplayGroup _aDisplayGroup_)

Allows the delegate to prevent _aDisplayGroup_ from fetching. If the delegate returns `true`, _aDisplayGroup_ performs the fetch; if the delegate returns `false`, _aDisplayGroup_ abandons the fetch.

---

### displayGroupShouldInsertObject

public abstract boolean `displayGroupShouldInsertObject`(
EODisplayGroup _aDisplayGroup_,
java.lang.Object _anObject_,
int _anIndex_)

Allows the delegate to prevent _aDisplayGroup_ from inserting _anObject_ at _anIndex_. If the delegate returns `true`, _anObject_ is inserted; if the delegate returns `false`, the insertion is abandoned.

---

### displayGroupShouldRedisplay

public abstract boolean `displayGroupShouldRedisplay`(
EODisplayGroup _aDisplayGroup_,
com.apple.yellow.foundation.NSNotification _aNotification_)

Invoked whenever _aDisplayGroup_ receives an EOObjectsChangedInEditingContextNotification, this method allows the delegate to suppress redisplay based on the nature of the change that has occurred. If the delegate returns `true`, _aDisplayGroup_ redisplays; if it returns `false`, _aDisplayGroup_ doesn't. _aNotification_ supplies the EOEditingContext that has changed, as well as which objects have changed and how. See the EOEditingContext class specification for information on EOObjectsChangedInEditingContextNotification.

__See also:__
[`redisplay`](../Classes/EODisplayGroup.md#apple-ge2dena)

---

### displayGroupShouldRefetch

public abstract boolean `displayGroupShouldRefetch`(
EODisplayGroup _aDisplayGroup_,
com.apple.yellow.foundation.NSNotification _aNotification_)

Invoked whenever _aDisplayGroup_ receives an EOInvalidatedAllObjectsInStoreNotification, this method allows the delegate to suppress refetching of the invalidated objects. If the delegate returns `true`, _aDisplayGroup_ immediately refetches its objects. If the delegate returns `false`, _aDisplayGroup_ doesn't immediately fetch, instead delaying until absolutely necessary. _aNotification_ is an NSNotification. See the EOObjectStore and EOEditingContext class specifications for information on this notification.

---

[!](EOViewLayout.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
