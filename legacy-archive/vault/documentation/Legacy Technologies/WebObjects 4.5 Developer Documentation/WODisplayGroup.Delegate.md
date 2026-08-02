---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Protocols/WODisplayGroup.html
archived_at: '2026-07-15T08:11:47.268320Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WODisplayGroup.Delegate

> __Implemented by:__
> WODisplayGroup delegate objects

> __Package:__
> com.apple.yellow.webobjects

## Interface Description

---

WODisplayGroup offers a number of methods for its delegate
to implement; if the delegate does implement them, the WODisplayGroup
instances invoke them as appropriate. There are methods that inform
the delegate that the EODisplayGroup has fetched, created an object
(or failed to create one), inserted or deleted an object, changed
the selection, or set a value for a property. There are also methods that
request permission from the delegate to perform most of these same
actions. The delegate can return true to permit the action or false to
deny it. See each method's description for more information.

## Instance Methods

---

### displayGroupCreateObjectFailedForDataSource

`public abstract void displayGroupCreateObjectFailedForDataSource(
WODisplayGroup aDisplayGroup,
Object aDataSource)`

Invoked from [insertNewObjectAtIndex](WODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62loonsxe5comv3u6ytkmvrxiqlujfxgizly) to
inform the delegate that _aDisplayGroup_ has
failed to create a new object for _aDataSource_.
If the delegate doesn't implement this method, the WODisplayGroup
fails silently.

---

### displayGroupDidChangeDataSource

`public abstract void displayGroupDidChangeDataSource(WODisplayGroup aDisplayGroup)`

Informs the delegate that _aDisplayGroup_'s
EODataSource (defined in the EOControl framework) has changed.

---

### displayGroupDidChangeSelectedObjects

`public abstract void displayGroupDidChangeSelectedObjects(WODisplayGroup aDisplayGroup)`

Informs the delegate that _aDisplayGroup_'s
selected objects have changed, regardless of whether the selection
indexes have changed.

---

### displayGroupDidChangeSelection

`public abstract void displayGroupDidChangeSelection(WODisplayGroup aDisplayGroup)`

Informs the delegate that _aDisplayGroup_'s
selection has changed.

---

### displayGroupDidDeleteObject

`public abstract void displayGroupDidDeleteObject(
WODisplayGroup aDisplayGroup,
Object anObject)`

Informs the delegate that _aDisplayGroup_ has
deleted _anObject_.

---

### displayGroupDidFetchObjects

`public abstract void displayGroupDidFetchObjects(
WODisplayGroup aDisplayGroup,
NSArray objects)`

Informs the delegate that _aDisplayGroup_ has
fetched _objects_.

---

### displayGroupDidInsertObject

`public abstract void displayGroupDidInsertObject(
WODisplayGroup aDisplayGroup,
Object anObject)`

Informs the delegate that _aDisplayGroup_ has
inserted _anObject_.

---

### displayGroupDidSetValue

`public abstract void displayGroupDidSetValue(
WODisplayGroup aDisplayGroup,
Object value,
Object anObject,
String key)`

Informs the delegate that _aDisplayGroup_ has
altered a property value of _anObject_. _key_ identifies
the property, and _value_ is its new
value.

---

### displayGroupDisplayArrayForObjects

`public abstract NSArray displayGroupDisplayArrayForObjects(
WODisplayGroup aDisplayGroup,
NSArray objects)`

Invoked from [updateDisplayedObjects](WODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt),
this method allows the delegate to filter and sort _aDisplayGroup_'s
array of objects to limit which ones get displayed. _objects_ contains
all of aDisplayGroup's objects. The delegate should filter any
objects that shouldn't be shown and sort the remainder, returning
a new array containing this group of objects. You can use the NSArray
methods filteredArrayUsingQualifier and sortedArrayUsingKeyOrderingArray to
create the new array.

If the delegate doesn't implement this method, the WODisplayGroup
uses its own qualifier and sort ordering to update the displayed
objects array.

__See Also:__
[displayedObjects](WODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [qualifier](WODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztjmvza), [sortOrderings](WODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643poj2e64temvzgs3thom)

---

### displayGroupShouldChangeSelectionToIndexes

`public abstract boolean displayGroupShouldChangeSelectionToIndexes(
WODisplayGroup aDisplayGroup,
NSArray newIndexes)`

Allows the delegate to prevent a change in selection
by _aDisplayGroup_. _newIndexes_ is
the proposed new selection. If the delegate returns true, the selection
changes; if the delegate returns false, the selection remains as
it is.

---

### displayGroupShouldDeleteObject

`public abstract boolean displayGroupShouldDeleteObject(
WODisplayGroup aDisplayGroup,
Object anObject)`

Allows the delegate to prevent _aDisplayGroup_ from
deleting _anObject_. If the delegate
returns true, _anObject_ is deleted;
if the delegate returns false, the deletion is abandoned.

---

### displayGroupShouldFetch

`public abstract boolean displayGroupShouldFetch(WODisplayGroup aDisplayGroup)`

Allows the delegate to prevent _aDisplayGroup_ from
fetching. If the delegate returns true, _aDisplayGroup_ performs
the fetch; if the delegate returns false, _aDisplayGroup_ abandons
the fetch.

---

### displayGroupShouldInsertObject

`public abstract boolean displayGroupShouldInsertObject(
WODisplayGroup aDisplayGroup,
Object anObject,
int anIndex)`

Allows the delegate to prevent [redisplay](WODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64tfmruxg4dmmf4q) from inserting _anObject_ at _anIndex_.
If the delegate returns true, _anObject_ is
inserted; if the delegate returns false, the insertion is abandoned.

---

### displayGroupShouldRedisplayForChangesInEditingContext

`public abstract boolean displayGroupShouldRedisplayForChangesInEditingContext(
WODisplayGroup aDisplayGroup,
NSNotification aNotification)`

Invoked whenever _aDisplayGroup_ receives
an EOObjectsChangedInEditingContextNotification, this method allows
the delegate to suppress redisplay based on the nature of the change
that has occurred. If the delegate returns true, _aDisplayGroup_ redisplays;
if it returns false, _aDisplayGroup_ doesn't.

__See Also:__
[redisplay](WODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64tfmruxg4dmmf4q)

---

### displayGroupShouldRefetchForInvalidatedAllObjectsNotification

`public abstract boolean displayGroupShouldRefetchForInvalidatedAllObjects(
WODisplayGroup aDisplayGroup,
NSNotification aNotification)`

Invoked whenever _aDisplayGroup_ receives
an EOInvalidatedAllObjectsInStoreNotification, this method allows
the delegate to suppress the refetching of the invalidated objects.
If the delegate returns true, _aDisplayGroup_ immediately
fetches its objects. If the delegate returns false, _aDisplayGroup_ doesn't immediately
fetch, instead delaying until absolutely necessary.

__See Also:__
[redisplay](WODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64tfmruxg4dmmf4q)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
