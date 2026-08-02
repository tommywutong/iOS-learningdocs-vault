---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Protocols/WODisplayGroup.html
archived_at: '2026-07-15T08:11:47.910782Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WODisplayGroup Delegate

> __Adopted by:__
> WODisplayGroup delegate objects

> __Declared in:__  WebObjects/WODisplayGroup.h

## Protocol Description

---

WODisplayGroup offers a number of methods for its delegate
to implement; if the delegate does implement them, the WODisplayGroup
instances invoke them as appropriate. There are methods that inform
the delegate that the EODisplayGroup has fetched, created an object
(or failed to create one), inserted or deleted an object, changed
the selection, or set a value for a property. There are also methods that
request permission from the delegate to perform most of these same
actions. The delegate can return YES to permit the action or NO to
deny it. See each method's description for more information.

## Instance Methods

---

### displayGroup:createObjectFailedForDataSource:

`- (void)displayGroup:(WODisplayGroup
*)aDisplayGroup
createObjectFailedForDataSource:(id)aDataSource`

Invoked from [insertObjectAtIndex:](WODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3ttmvzhit3cnjswg5cborew4zdfpa5a) to
inform the delegate that _aDisplayGroup_ has
failed to create a new object for _aDataSource_.
If the delegate doesn't implement this method, the WODisplayGroup
fails silently.

---

### displayGroupDidChangeDataSource:

`- (void)displayGroupDidChangeDataSource:(WODisplayGroup
*)aDisplayGroup`

Informs the delegate that _aDisplayGroup_'s
EODataSource (defined in the EOControl framework) has changed.

---

### displayGroupDidChangeSelectedObjects:

`- (void)displayGroupDidChangeSelectedObjects:(WODisplayGroup
*)aDisplayGroup`

Informs the delegate that _aDisplayGroup_'s
selected objects have changed, regardless of whether the selection
indexes have changed.

---

### displayGroupDidChangeSelection:

`- (void)displayGroupDidChangeSelection:(WODisplayGroup
*)aDisplayGroup`

Informs the delegate that _aDisplayGroup_'s
selection has changed.

---

### displayGroup:didDeleteObject:

`- (void)displayGroup:(WODisplayGroup
*)aDisplayGroup
didDeleteObject:(id)anObject`

Informs the delegate that _aDisplayGroup_ has
deleted _anObject_.

---

### displayGroup:didFetchObjects:

`- (void)displayGroup:(WODisplayGroup
*)aDisplayGroup
didFetchObjects:(NSArray *)objects`

Informs the delegate that _aDisplayGroup_ has
fetched _objects_.

---

### displayGroup:didInsertObject:

`- (void)displayGroup:(WODisplayGroup
*)aDisplayGroup
didInsertObject:(id)anObject`

Informs the delegate that _aDisplayGroup_ has
inserted _anObject_.

---

### displayGroup:didSetValue:forObject:key:

`- (void)displayGroup:(WODisplayGroup
*)aDisplayGroup
didSetValue:(id)value
forObject:(id)anObject
key:(NSString *)key`

Informs the delegate that _aDisplayGroup_ has
altered a property value of _anObject_. _key_ identifies
the property, and _value_ is its new
value.

---

### displayGroup:displayArrayForObjects:

`- (NSArray *)displayGroup:(WODisplayGroup
*)aDisplayGroup
displayArrayForObjects:(NSArray
*)objects`

Invoked from [updateDisplayedObjects](WODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y),
this method allows the delegate to filter and sort _aDisplayGroup_'s
array of objects to limit which ones get displayed. _objects_ contains
all of aDisplayGroup's objects. The delegate should filter any
objects that shouldn't be shown and sort the remainder, returning
a new array containing this group of objects. You can use the NSArray
methods filteredArrayUsingQualifier: and sortedArrayUsingKeyOrderingArray: to
create the new array.

If the delegate doesn't implement this method, the WODisplayGroup
uses its own qualifier and sort ordering to update the displayed
objects array.

__See Also:__
[- displayedObjects](WODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- qualifier](WODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfoi), [- sortOrderings](WODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxg33sorhxezdfojuw4z3t)

---

### displayGroup:shouldChangeSelectionToIndexes:

`- (BOOL)displayGroup:(WODisplayGroup
*)aDisplayGroup
shouldChangeSelectionToIndexes:(NSArray
*)newIndexes`

Allows the delegate to prevent a change in selection
by _aDisplayGroup_. _newIndexes_ is
the proposed new selection. If the delegate returns YES, the selection
changes; if the delegate returns NO, the selection remains as it
is.

---

### displayGroup:shouldDeleteObject:

`- (BOOL)displayGroup:(WODisplayGroup
*)aDisplayGroup
shouldDeleteObject:(id)anObject`

Allows the delegate to prevent _aDisplayGroup_ from
deleting _anObject_. If the delegate
returns YES, _anObject_ is deleted;
if the delegate returns NO, the deletion is abandoned.

---

### displayGroupShouldFetch:

`- (BOOL)displayGroupShouldFetch:(WODisplayGroup
*)aDisplayGroup`

Allows the delegate to prevent _aDisplayGroup_ from
fetching. If the delegate returns YES, _aDisplayGroup_ performs
the fetch; if the delegate returns NO, _aDisplayGroup_ abandons
the fetch.

---

### displayGroup:shouldInsertObject:atIndex:

`- (BOOL)displayGroup:(WODisplayGroup
*)aDisplayGroup
shouldInsertObject:(id)anObject
atIndex:(unsigned int)anIndex`

Allows the delegate to prevent [redisplay](WODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxezlenfzxa3dbpe) from inserting _anObject_ at _anIndex_.
If the delegate returns YES, _anObject_ is
inserted; if the delegate returns NO, the insertion is abandoned.

---

### displayGroup:shouldRedisplayForChangesInEditingContext:

`- (BOOL)displayGroup:(WODisplayGroup
*)aDisplayGroup
shouldRedisplayForEditingContextChangeNotification:(NSNotification
*)aNotification`

Invoked whenever _aDisplayGroup_ receives
an EOObjectsChangedInEditingContextNotification, this method allows
the delegate to suppress redisplay based on the nature of the change
that has occurred. If the delegate returns YES, _aDisplayGroup_ redisplays;
if it returns NO, _aDisplayGroup_ doesn't.

__See Also:__
[- redisplay](WODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxezlenfzxa3dbpe)

---

### displayGroup:shouldRefetchForInvalidatedAllObjectsNotification:

`- (BOOL)displayGroup:(WODisplayGroup
*)aDisplayGroup
shouldRefetchForInvalidatedAllObjectsNotification:(NSNotification
*)aNotification`

Invoked whenever _aDisplayGroup_ receives
an EOInvalidatedAllObjectsInStoreNotification, this method allows
the delegate to suppress the refetching of the invalidated objects.
If the delegate returns YES, _aDisplayGroup_ immediately
fetches its objects. If the delegate returns NO, _aDisplayGroup_ doesn't immediately
fetch, instead delaying until absolutely necessary.

__See Also:__
[- redisplay](WODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxezlenfzxa3dbpe)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
