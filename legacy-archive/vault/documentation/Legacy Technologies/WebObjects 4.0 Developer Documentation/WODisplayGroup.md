---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/WODisplayGroup.html
archived_at: '2026-07-18T01:28:51.592089Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](WODirectAction.md)
[!](WODynamicElement.md)

---

# WODisplayGroup

__Inherits From:__
NSObject

NSCoding

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

A WODisplayGroup is the basic user interface manager for a WebObjects application that accesses a database. It collects objects from an EODataSource (defined in EOControl), filters and sorts them, and maintains a selection in the filtered subset. You bind WebObjects dynamic elements to WODisplayGroup attributes and methods to display information from the database on your web page.

A WODisplayGroup manipulates its EODataSource by sending it
fetchObjects
,
insertObject:
, and other messages, and registers itself as an editor and message handler of the EODataSource's EOEditingContext (also defined in EOControl). The EOEditingContext then monitors the WODisplayGroup for changes to objects.

Most of a WODisplayGroup's interactions are with its EODataSource and its EOEditingContext. See the EODataSource, and EOEditingContext class specifications in the _Enterprise Objects Framework Reference_ for more information on these interactions.

---

## The Delegate

The WODisplayGroup delegate offers a number of methods, and WODisplayGroup invokes them as appropriate. Besides [`displayArrayForObjects`](../Protocols/WODisplayGroup.Delegate.md#apple-geztima), there are methods that inform the delegate that the WODisplayGroup has fetched, created an object (or failed to create one), inserted or deleted an object, changed the selection, or set a value for a property. There are also methods that request permission from the delegate to perform most of these same actions. The delegate can return `true` to permit the action or `false` to deny it. See each method's description in the WODisplayGroup.Delegates interface specification for more information.

---

## Method Types

**Constructor**

**[WODisplayGroup](#apple-gq3tgnjt)**

**Configuring behavior**

**[setFetchesOnLoad](#apple-gi3tk)

**[fetchesOnLoad](#apple-geytk)

**[setSelectsFirstObjectAfterFetch](#apple-gmytc)

**[selectsFirstObjectAfterFetch](#apple-gi2do)

**[setValidatesChangesImmediately](#apple-gyzdemy)

**[validatesChangesImmediately](#apple-gmztc)************

**Setting the data source**

**[setDataSource](#apple-gi2tk)

**[dataSource](#apple-gyzq)****

**Setting the qualifier and sort ordering**

**[setQualifier](#apple-gmydg)

**[qualifier](#apple-gm3dimq)

**[setSortOrderings](#apple-gmytk)

**[sortOrderings](#apple-gmzdg)********

**Managing queries**

**[qualifierFromQueryValues](#apple-ge3tk)

**[queryMatch](#apple-ge4tc)

**[queryMax](#apple-ge4tk)

**[queryMin](#apple-ge4ts)

**[queryOperator](#apple-giydg)

**[allQualifierOperators](#apple-gq3q)

**[relationalQualifierOperators](#apple-giytc)

**[setDefaultStringMatchFormat](#apple-gi2ts)

**[defaultStringMatchFormat](#apple-gy3q)

**[setDefaultStringMatchOperator](#apple-gi3dg)

**[defaultStringMatchOperator](#apple-g4yq)

**[qualifyDisplayGroup](#apple-ge4dg)

**[qualifyDataSource](#apple-ge3ts)

**[inQueryMode](#apple-geztsnrq)

**[setInQueryMode](#apple-gm4doni)******************************

**Fetching objects from the data source**

**[fetch](#apple-geytc)**

**Getting the objects**

**[allObjects](#apple-gqzq)

**[displayedObjects](#apple-geztsmry)****

**Batching the results**

**[setNumberOfObjectsPerBatch](#apple-gi4tk)

**[numberOfObjectsPerBatch](#apple-ge3do)

**[hasMultipleBatches](#apple-gezdg)

**[displayNextBatch](#apple-giydqmq)

**[displayPreviousBatch](#apple-geydg)

**[batchCount](#apple-guyq)

**[setCurrentBatchIndex](#apple-gi2tc)

**[currentBatchIndex](#apple-gu4q)

**[indexOfFirstDisplayedObject](#apple-gezdenby)

**[indexOfLastDisplayedObject](#apple-gezdenju)

**[displayBatchContainingSelectedObject](#apple-he2q)**********************

**Updating display of values**

**[redisplay](#apple-giydo)

**[updateDisplayedObjects](#apple-gmzdo)****

**Setting the objects**

**[setObjectArray](#apple-gi4ts)**

**Changing the selection**

**[setSelectionIndexes](#apple-gm4tkmy)

**[selectObjectsIdenticalTo](#apple-ge2danjz)

**[selectObjectsIdenticalToAndSelectFirstOnNoMatch](#apple-ge2danzt)

**[selectObject](#apple-ge2danbv)

**[clearSelection](#apple-gu2q)

**[selectNext](#apple-ge2damrw)

**[selectPrevious](#apple-ge2daobx)**************

**Examining the selection**

**[selectionIndexes](#apple-gi2dg)

**[selectedObject](#apple-giztk)

**[selectedObjects](#apple-gizts)******

**Inserting and deleting objects**

**[insertNewObjectAtIndex](#apple-ge2dambt)

**[insert](#apple-ge2dg)

**[setInsertedObjectDefaultValues](#apple-gi4dg)

**[insertedObjectDefaultValues](#apple-geztsobv)

**[deleteObjectAtIndex](#apple-hazq)

**[deleteSelection](#apple-gm2domq)

**[delete](#apple-g44q)**************

**Setting up a detail display group**

**[hasDetailDataSource](#apple-geyts)

**[setMasterObject](#apple-gi4tc)

**[masterObject](#apple-ge3dg)

**[setDetailKey](#apple-gi3tc)

**[detailKey](#apple-heyq)**********

**Working with named fetch specifications**

**[queryBindings](#apple-gezdgnry)**

**Setting the delegate**

**[setDelegate](#apple-gi3do)

**[delegate](#apple-g42q)****

---

## Constructors

---

### WODisplayGroup

public `WODisplayGroup`()

Creates and returns a new WODisplayGroup. The WODisplayGroup then needs to have an EODataSource (defined in EOControl) set with [`setDataSource`](#apple-gi2tk).

---

## Instance Methods

---

### allObjects

public NSArray `allObjects`()

Returns all of the objects collected by the receiver.

__See also:__
[`displayedObjects`](#apple-geztsmry), [`fetch`](#apple-geytc)

---

### allQualifierOperators

public NSArray `allQualifierOperators`()

Returns an array containing all of the relational operators supported by EOControl's EOQualifier: =, !=, <, <=, >, >=, "`like`" and "`caseInsensitiveLike`".

__See also:__
[`queryOperator`](#apple-giydg), [`relationalQualifierOperators`](#apple-giytc)

---

### batchCount

public int `batchCount`()

The number of batches to display. For example, if the displayed objects array contains two hundred records and the batch size is ten, `batchCount` returns twenty (twenty batches of ten records each).

__See also:__
[`currentBatchIndex`](#apple-gu4q), [`displayNextBatch`](#apple-giydqmq), [`displayPreviousBatch`](#apple-geydg), [`hasMultipleBatches`](#apple-gezdg),
[`numberOfObjectsPerBatch`](#apple-ge3do)

---

### clearSelection

public boolean `clearSelection`()

Invokes [`setSelectionIndexes`](#apple-gm4tkmy) to clear the selection, returning `true` on success and `false` on failure.

---

### currentBatchIndex

public int `currentBatchIndex`()

Returns the index of the batch currently being displayed. The total batch count equals the number of displayed objects divided by the batch size. For example, if the WODisplayGroup has one hundred objects to display and the batch size is twenty, there are five batches. The first batch has a batch index of 1.

__See also:__
[`batchCount`](#apple-guyq), [`numberOfObjectsPerBatch`](#apple-ge3do), [`setCurrentBatchIndex`](#apple-gi2tc)

---

### dataSource

public com.apple.yellow.eocontrol.EODataSource `dataSource`()

Returns the receiver's EODataSource (defined in the EOControl framework).

__See also:__
[`hasDetailDataSource`](#apple-geyts), [`setDataSource`](#apple-gi2tk)

---

### defaultStringMatchFormat

public java.lang.String `defaultStringMatchFormat`()

Returns the format string that specifies how pattern matching will be performed on string values in the [`queryMatch`](#apple-ge4tc) dictionary. If a key in the `queryMatch` dictionary does not have an associated operator in the [`queryOperator`](#apple-giydg) dictionary, then its value is matched using pattern matching, and the format string returned by this method specifies how it will be matched.

__See also:__
[`defaultStringMatchOperator`](#apple-g4yq), [`setDefaultStringMatchFormat`](#apple-gi2ts)

---

### defaultStringMatchOperator

public java.lang.String `defaultStringMatchOperator`()

Returns the operator used to perform pattern matching for string values in the [`queryMatch`](#apple-ge4tc) dictionary. If a key in the `queryMatch` dictionary does not have an associated operator in the [`queryOperator`](#apple-giydg) dictionary, then the operator returned by this method is used to perform pattern matching. Unless the default is changed, this method returns caseInsensitiveLike.

__See also:__
[`defaultStringMatchFormat`](#apple-gy3q), [`setDefaultStringMatchOperator`](#apple-gi3dg)

---

### delegate

public java.lang.Object `delegate`()

Returns the receiver's delegate.

__See also:__
[`setDelegate`](#apple-gi3do)

---

### delete

public java.lang.Object `delete`()

Uses [`deleteSelection`](#apple-gm2domq) to attempt to delete the selected objects and then causes the page to reload. Returns `null` to force reloading of the web page.

__See also:__
[`deleteObjectAtIndex`](#apple-hazq)

---

### deleteObjectAtIndex

public boolean `deleteObjectAtIndex`(int _index_)

Attempts to delete the object at _index_, returning `true` if successful and `false` if not. Checks with the delegate using the method [`shouldDeleteObject`](../Protocols/WODisplayGroup.Delegate.md#apple-geztonq). If the delegate returns `false`, this method fails and returns `false`. If successful, it sends the delegate a [`didDeleteObject`](../Protocols/WODisplayGroup.Delegate.md#apple-geztama) message.

This method performs the delete by sending
deleteObject
to the EODataSource (defined in the EOControl framework). If that message raises an exception, this method fails and returns `false`.

__See also:__
[`delete`](#apple-g44q), [`deleteSelection`](#apple-gm2domq)

---

### deleteSelection

public boolean `deleteSelection`()

Attempts to delete the selected objects, returning `true` if successful and `false` if not.

__See also:__
[`delete`](#apple-g44q), [`deleteObjectAtIndex`](#apple-hazq)

---

### detailKey

public java.lang.String `detailKey`()

For detail display groups, returns the key to the master object that specifies what this detail display group represents. That is, if you send the object returned by the [`masterObject`](#apple-ge3dg) method a
valueForKey:
message with this key, you obtain the objects controlled by this display group.

This method returns `null` if the receiver is not a detail display group or if the detail key has not yet been set. You typically create a detail display group by dragging a to-many relationship from EOModeler to an open component in WebObjects Builder.

__See also:__
[`hasDetailDataSource`](#apple-geyts), [`masterObject`](#apple-ge3dg), [`setDetailKey`](#apple-gi3tc)

---

### displayBatchContainingSelectedObject

public java.lang.Object `displayBatchContainingSelectedObject`()

Displays the batch containing the selection and sets the current batch index to that batch's index. Returns `null` to force the page to reload.

__See also:__
: [`displayNextBatch`](#apple-giydqmq), [`displayPreviousBatch`](#apple-geydg), [`setCurrentBatchIndex`](#apple-gi2tc)

---

### displayedObjects

public NSArray `displayedObjects`()

Returns the objects that should be displayed or otherwise made available to the user, as filtered by the receiver's delegate, by the receiver's qualifier and sort ordering.

If batching is in effect, `displayedObjects` returns the current batch of objects.

__See also:__
[`allObjects`](#apple-gqzq), [`updateDisplayedObjects`](#apple-gmzdo), [`qualifier`](#apple-gm3dimq), [`setSortOrderings`](#apple-gmytk), [`displayArrayForObjects`](../Protocols/WODisplayGroup.Delegate.md#apple-geztima)
(delegate method)

---

### displayNextBatch

public java.lang.Object `displayNextBatch`()

Increments the current batch index, displays that batch of objects, and clears the selection. If the batch currently being displayed is the last batch, this method displays the first batch of objects. Returns `null` to force the page to reload.

__See also:__
[`batchCount`](#apple-guyq), [`currentBatchIndex`](#apple-gu4q), [`displayBatchContainingSelectedObject`](#apple-he2q),
[`displayPreviousBatch`](#apple-geydg)

---

### displayPreviousBatch

public java.lang.Object `displayPreviousBatch`()

Decrements the current batch index, displays that batch of objects, and clears the selection. If the batch currently being displayed is the first batch, this method displays the last batch of objects. Returns `null` to force the page to reload.

__See also:__
[`batchCount`](#apple-guyq), [`currentBatchIndex`](#apple-gu4q), [`displayBatchContainingSelectedObject`](#apple-he2q), [`displayNextBatch`](#apple-giydqmq)

---

### fetch

public java.lang.Object `fetch`()

Attempts to fetch objects from the EODataSource (defined in the EOControl framework).

Before fetching, this method sends [`displayGroupShouldFetch`](../Protocols/WODisplayGroup.Delegate.md#apple-ge2dkmq) to the delegate. If this method was successful, it then sends a `fetchObjects` message to the receiver's EODataSource to replace the object array, and if successful sends the delegate a [`didFetchObjects`](../Protocols/WODisplayGroup.Delegate.md#apple-geztaoi) message.

This method returns `null` to force the page to reload.

__See also:__
[`allObjects`](#apple-gqzq), [`updateDisplayedObjects`](#apple-gmzdo)

---

### fetchesOnLoad

public boolean `fetchesOnLoad`()

Returns `true` if the receiver fetches automatically after the component that contains it is loaded, `false` if it must be told explicitly to fetch. The default is `true`. You can set this behavior in WebObjects Builder using the Display Group Options panel. Note that if the display group fetches on load, it performs the fetch each time the component is loaded into the web browser.

__See also:__
[`fetch`](#apple-geytc), [`setFetchesOnLoad`](#apple-gi3tk)

---

### hasDetailDataSource

public boolean `hasDetailDataSource`()

Returns `true` if the display group's data source is an EODetailDataSource (defined in the EOControl framework), and `false` otherwise. If you drag a to-many relationship from EOModeler to an open component in WebObjects Builder, you create a display group that has an EODetailDataSource. You can also set this up using the Display Group Options panel in WebObjects Builder.

__See also:__
[`detailKey`](#apple-heyq), [`masterObject`](#apple-ge3dg)

---

### hasMultipleBatches

public boolean `hasMultipleBatches`()

Returns `true` if the batch count is greater than 1. A display group displays its objects in batches if the [`numberOfObjectsPerBatch`](#apple-ge3do) method returns a number that is less than the number of objects in the [`displayedObjects`](#apple-geztsmry) array.

__See also:__
[`batchCount`](#apple-guyq), [`setNumberOfObjectsPerBatch`](#apple-gi4tk)

---

### indexOfFirstDisplayedObject

public int `indexOfFirstDisplayedObject`()

Returns the index of the first object displayed by the current batch. For example, if the current batch is displaying items 11 through 20, this method returns 11.

__See also:__
[`indexOfLastDisplayedObject`](#apple-gezdenju)

---

### indexOfLastDisplayedObject

public int `indexOfLastDisplayedObject`()

Returns the index of the last object display by the current batch. For example, if the current batch is displaying items 11 through 20, this method returns 20.

__See also:__
[`indexOfFirstDisplayedObject`](#apple-gezdenby)

---

### inQueryMode

public boolean `inQueryMode`()

Returns `true` to indicate that the receiver is in query mode, `false` otherwise. In query mode, controls in the user interface that normally display values become empty, allowing users to type queries directly into them (this is also known as a "Query by Example" interface). In effect, the receiver's "displayedObjects" are replaced with an empty [`queryMatch`](#apple-ge4tc) dictionary. When [`qualifyDisplayGroup`](#apple-ge4dg) or [`qualifyDataSource`](#apple-ge3ts) is subsequently invoked, the query is performed and the display reverts to displaying values-this time, the objects returned by the query.

__See also:__
[`setInQueryMode`](#apple-gm4doni)

---

### insert

public java.lang.Object `insert`()

Invokes [`insertNewObjectAtIndex`](#apple-ge2dambt) with an index just past the first index in the selection, or at the end if there's no selection.

This method returns `null` to force the page to reload.

---

### insertedObjectDefaultValues

public NSDictionary `insertedObjectDefaultValues`()

Returns the default values to be used for newly inserted objects. The keys into the dictionary are the properties of the entity that the display group manages. If the dictionary returned by this method is empty, the [`insert`](#apple-ge2dg) method adds an object that is initially empty. Because the object is empty, the display group has no value to display on the HTML page for that object, meaning that there is nothing for the user to select and modify. Use the [`setInsertedObjectDefaultValues`](#apple-gi4dg) method to set up a default value so that there is something to display on the page.

---

### insertNewObjectAtIndex

public java.lang.Object `insertNewObjectAtIndex`(int _index_)

Asks the receiver's EODataSource (defined in the EOControl framework) to create a new object by sending it a
createObject
message, then inserts the new object . If a new object can't be created, this method sends the delegate a [`createObjectFailedForDataSource`](../Protocols/WODisplayGroup.Delegate.md#apple-gi2dgnq) message.

If the object is successfully created, this method then sets the default values specified by [`insertedObjectDefaultValues`](#apple-geztsobv).

__See also:__
[`insert`](#apple-ge2dg)

---

### masterObject

public java.lang.Object `masterObject`()

Returns the master object for a detail display group (a display group that represents a detail in a master-detail relationship). A detail display group is one that uses an EODetailDataSource (defined in the EOControl framework). You create a detail display group by dragging a to-many relationship from EOModeler to an open component in WebObjects Builder. If the display group is not a detail display group or does not have a master object set, this method returns `null`.

__See also:__
[`detailKey`](#apple-heyq), [`hasDetailDataSource`](#apple-geyts), [`setMasterObject`](#apple-gi4tc)

---

### numberOfObjectsPerBatch

public int `numberOfObjectsPerBatch`()

Returns the batch size. You can set the batch size using [`setNumberOfObjectsPerBatch`](#apple-gi4tk) or using WebObjects Builder's Display Group Options panel.

---

### qualifier

public com.apple.yellow.eocontrol.EOQualifier `qualifier`()

Returns the receiver's qualifier, which it uses to filter its array of objects for display when the delegate doesn't do so itself.

__See also:__
[`displayedObjects`](#apple-geztsmry), [`setQualifier`](#apple-gmydg):,[`updateDisplayedObjects`](#apple-gmzdo)

---

### qualifierFromQueryValues

public com.apple.yellow.eocontrol.EOQualifier `qualifierFromQueryValues`()

Builds a qualifier constructed from entries in these query dictionaries: [`queryMatch`](#apple-ge4tc), [`queryMax`](#apple-ge4tk), [`queryMin`](#apple-ge4ts), and [`queryOperator`](#apple-giydg).

__See also:__
[`qualifyDataSource`](#apple-ge3ts), [`qualifyDisplayGroup`](#apple-ge4dg)

---

### qualifyDataSource

public void `qualifyDataSource`()

Takes the result of [`qualifierFromQueryValues`](#apple-ge3tk) and applies to the receiver's data source. The receiver then sends itself a [`fetch`](#apple-geytc) message. If the receiver is in query mode, query mode is exited. This method differs from [`qualifyDisplayGroup`](#apple-ge4dg) as follows: whereas `qualifyDisplayGroup` performs in-memory filtering of already fetched objects, `qualifyDataSource` triggers a new qualified fetch against the database.

__See also:__
[`queryMatch`](#apple-ge4tc), [`queryMax`](#apple-ge4tk),, [`queryMin`](#apple-ge4ts),[`queryOperator`](#apple-giydg)

---

### qualifyDisplayGroup

public void `qualifyDisplayGroup`()

Takes the result of the [`qualifierFromQueryValues`](#apple-ge3tk) and applies to the receiver using [`setQualifier`](#apple-gmydg). The method [`updateDisplayedObjects`](#apple-gmzdo) is invoked to refresh the display. If the receiver is in query mode, query mode is exited.

__See also:__
[`qualifyDataSource`](#apple-ge3ts), [`queryMatch`](#apple-ge4tc), [`queryMax`](#apple-ge4tk), -[`queryMin`](#apple-ge4ts), [`queryOperator`](#apple-giydg)

---

### queryBindings

public NSMutableDictionary `queryBindings`()

Returns a dictionary containing the actual values that the user wants to query upon. You use this method to perform a query stored in the model file. Bind keys in this dictionary to elements on your component that specify query values, then pass this dictionary to the fetch specification that performs the fetch.

---

### queryMatch

public NSMutableDictionary `queryMatch`()

Returns a dictionary of query values to match. The [`qualifierFromQueryValues`](#apple-ge3tk) method uses this dictionary along with the [`queryMax`](#apple-ge4tk) and [`queryMin`](#apple-ge4ts) dictionaries to construct qualifiers.

Use the [`queryOperator`](#apple-giydg) dictionary to specify the type of matching (=, <, >, `like`, and so on) for each key in the `queryMatch` dictionary.

If the `queryOperator` dictionary does not contain a key contained in the `queryMatch` dictionary, the default is to match the value exactly (=) if the value is a number or a date and to perform pattern matching if the value is a String. In the case of string values, the [`defaultStringMatchFormat`](#apple-gy3q) and [`defaultStringMatchOperator`](#apple-g4yq) specify exactly how the pattern matching will be performed.

__See also:__
[`allQualifierOperators`](#apple-gq3q), [`qualifyDataSource`](#apple-ge3ts), [`qualifyDisplayGroup`](#apple-ge4dg),
[`relationalQualifierOperators`](#apple-giytc)

---

### queryMax

public NSMutableDictionary `queryMax`()

Returns a dictionary of "less than" query values. The [`qualifierFromQueryValues`](#apple-ge3tk) method uses this dictionary along with the [`queryMatch`](#apple-ge4tc) and [`queryMin`](#apple-ge4ts) dictionaries to construct qualifiers.

__See also:__
[`qualifyDataSource`](#apple-ge3ts), [`qualifyDisplayGroup`](#apple-ge4dg), [`queryOperator`](#apple-giydg)

---

### queryMin

public NSMutableDictionary `queryMin`()

Returns a dictionary of "greater than" query values. The [`qualifierFromQueryValues`](#apple-ge3tk) method uses this dictionary along with the [`queryMatch`](#apple-ge4tc) and `queryMin` dictionaries to construct qualifiers.

__See also:__
[`qualifyDataSource`](#apple-ge3ts), [`qualifyDisplayGroup`](#apple-ge4dg), [`queryOperator`](#apple-giydg)

---

### queryOperator

public NSMutableDictionary `queryOperator`()

Returns a dictionary of operators to use on items in the [`queryMatch`](#apple-ge4tc) dictionary. If a key in the `queryMatch` dictionary also exists in `queryOperator`, that operator for that key is used. The [`allQualifierOperators`](#apple-gq3q) method returns the operator strings you can use as values in this dictionary.

__See also:__
[`qualifierFromQueryValues`](#apple-ge3tk), [`queryMax`](#apple-ge4tk), [`queryMin`](#apple-ge4ts), [`relationalQualifierOperators`](#apple-giytc)

---

### redisplay

public void `redisplay`()

Sends out a contents changed notification.

---

### relationalQualifierOperators

public NSArray `relationalQualifierOperators`()

Returns an array containing all of the relational operators supported by EOControl's EOQualifier: =, !=, <, <=, >, and >=. In other words, returns all of the EOQualifier operators except for the ones that work exclusively on strings: "`like`" and "`caseInsensitiveLike`".

__See also:__
[`allQualifierOperators`](#apple-gq3q), [`queryOperator`](#apple-giydg)

---

### selectedObject

public java.lang.Object `selectedObject`()

Returns the first selected object in the displayed objects array, or `null` if there's no such object.

__See also:__
[`displayedObjects`](#apple-geztsmry), [`selectionIndexes`](#apple-gi2dg), [`selectedObjects`](#apple-gizts)

---

### selectedObjects

public NSArray `selectedObjects`()

Returns the objects selected in the receiver's displayed objects array.

__See also:__
[`displayedObjects`](#apple-geztsmry), [`selectionIndexes`](#apple-gi2dg), [`selectedObject`](#apple-giztk)

---

### selectionIndexes

public NSArray `selectionIndexes`()

Returns the selection as an array of integers. The integers are indexes into the array returned by [`displayedObjects`](#apple-geztsmry).

__See also:__
[`selectedObject`](#apple-giztk), [`selectedObjects`](#apple-gizts), [`setSelectionIndexes`](#apple-gm4tkmy)

---

### selectNext

public java.lang.Object `selectNext`()

Attempts to select the object just after the currently selected one. The selection is altered in this way:

- If there are no objects, does nothing.
- If there's no selection, selects the object at index zero.
- If the first selected object is the last object in the displayed objects array, selects the first object.
- Otherwise selects the object after the first selected object.

This method returns `null` to force the page to reload.

__See also:__
[`selectPrevious`](#apple-ge2daobx), [`setSelectionIndexes`](#apple-gm4tkmy)

---

### selectObject

public boolean `selectObject`(java.lang.Object _anObject_)

Attempts to select the object equal to _anObject_ in the receiver's displayed objects array, returning `true` if successful and `false` otherwise. _anObject_ is equal to an object in the displayed objects array if its address is the same as the object in the array.

__See also:__
[`selectNext`](#apple-ge2damrw), [`selectPrevious`](#apple-ge2daobx)

---

### selectObjectsIdenticalTo

public boolean `selectObjectsIdenticalTo`(NSArray _objectSelection_)

Attempts to select the objects in the receiver's displayed objects array whose addresses are equal to those of objects, returning `true` if successful and `false` otherwise.

__See also:__
[`setSelectionIndexes`](#apple-gm4tkmy), [`selectObjectsIdenticalToAndSelectFirstOnNoMatch`](#apple-ge2danzt)

---

### selectObjectsIdenticalToAndSelectFirstOnNoMatch

public boolean `selectObjectsIdenticalToAndSelectFirstOnNoMatch`(NSArray _objects_, boolean _flag_)

Selects the objects in the receiver's displayed objects array whose addresses are equal to those of _objects_, returning `true` if successful and `false` otherwise. If no objects in the displayed objects array match objects and _flag_ is `true`, attempts to select the first object in the displayed objects array.

__See also:__
[`setSelectionIndexes`](#apple-gm4tkmy), [`selectObjectsIdenticalTo`](#apple-ge2danjz)

---

### selectPrevious

public java.lang.Object `selectPrevious`()

Attempts to select the object just before the presently selected one. The selection is altered in this way:

- If there are no objects, does nothing.
- If there's no selection, selects the object at index zero.
- If the first selected object is at index zero, selects the last object.
- Otherwise selects the object before the first selected object.

This method returns `null` to force the page to reload.

__See also:__
[`selectNext`](#apple-ge2damrw), [`redisplay`](#apple-giydo)

---

### selectsFirstObjectAfterFetch

public boolean `selectsFirstObjectAfterFetch`()

Returns `true` if the receiver automatically selects its first displayed object after a fetch if there was no selection, `false` if it leaves an empty selection as-is.

WODisplayGroups by default do select the first object after a fetch when there was no previous selection.

__See also:__
[`displayedObjects`](#apple-geztsmry), [`fetch`](#apple-geytc), [`setSelectsFirstObjectAfterFetch`](#apple-gmytc)

---

### setCurrentBatchIndex

public void `setCurrentBatchIndex`(int _anInt_)

Displays the _anInt_ batch of objects. The total batch count equals the number of displayed objects divided by the batch size. For example, if the WODisplayGroup has one hundred objects to display and the batch size is twenty, there are five batches. The first batch has a batch index of 1. `setCurrentBatchIndex(3)` would display the third batch of objects (objects 41 to 60 in this example).

If _anInt_ is greater than the number of batches, this method displays the first batch.

__See also:__
[`batchCount`](#apple-guyq), [`currentBatchIndex`](#apple-gu4q), [`displayBatchContainingSelectedObject`](#apple-he2q),[`displayNextBatch`](#apple-giydqmq), [`displayPreviousBatch`](#apple-geydg),[`numberOfObjectsPerBatch`](#apple-ge3do)

---

### setDataSource

public void `setDataSource`(com.apple.yellow.eocontrol.EODataSource _aDataSource_)

Sets the receiver's EODataSource (defined in the EOControl framework) to _aDataSource_. In the process, it performs these actions:

Unregisters itself as an editor and message handler for the previous EODataSource's EOEditingContext (also defined in EOControl), if necessary, and registers itself with _aDataSource_'s EOEditingContext. If the new EOEditingContext already has a message handler, however, the receiver doesn't assume that role.

Clears the receiver's array of objects.

Sends [`displayGroupDidChangeDataSource`](../Protocols/WODisplayGroup.Delegate.md#apple-ge2demy) to the delegate if there is one.

__See also:__
[`dataSource`](#apple-gyzq)

---

### setDefaultStringMatchFormat

public void `setDefaultStringMatchFormat`(java.lang.String _format_)

Sets how pattern matching will be performed on String values in the [`queryMatch`](#apple-ge4tc) dictionary. This format is used for properties listed in the `queryMatch` dictionary that have String values and that do not have an associated entry in the [`queryOperator`](#apple-giydg) dictionary. In these cases, the value is matched using pattern matching and _format_ specifies how it will be matched.

The default format string for pattern matching is "`%@*`" which means that the string value in the `queryMatch` dictionary is used as a prefix. For example, if the `queryMatch` dictionary contains a value "Jo" for the key "Name", the query returns all records whose name values begin with "Jo".

__See also:__
[`defaultStringMatchFormat`](#apple-gy3q), [`setDefaultStringMatchOperator`](#apple-gi3dg)

---

### setDefaultStringMatchOperator

public void `setDefaultStringMatchOperator`(java.lang.String _operator_)

Sets the operator used to perform pattern matching for String values in the [`queryMatch`](#apple-ge4tc) dictionary. This operator is used for properties listed in the `queryMatch` dictionary that have String values and that do not have an associated entry in the [`queryOperator`](#apple-giydg) dictionary. In these cases, the operator _operator_ is used to perform pattern matching.

The default value for the query match operator is `caseInsensitiveLike`, which means that the query does not consider case when matching letters. The other possible value for this operator is `like`, which matches the case of the letters exactly.

__See also:__
[`allQualifierOperators`](#apple-gq3q), [`defaultStringMatchOperator`](#apple-g4yq), [`relationalQualifierOperators`](#apple-giytc),
[`setDefaultStringMatchFormat`](#apple-gi2ts)

---

### setDelegate

public void `setDelegate`(java.lang.Object _anObject_)

Sets the receiver's delegate to _anObject_.

__See also:__
[`delegate`](#apple-g42q), [WODisplayGroup.Delegate](WODisplayGroup.Delegate.md)

---

### setDetailKey

public void `setDetailKey`(java.lang.String _detailKey_)

Sets the detail key to _detailKey_ for a detail display group. The detail key is the key that retrieves from the master object the objects that this display group manages. You must set a detail key before you set a master object.

If the receiver is not a detail display group, this method has no effect. A display group is a detail display group if its data source is an EODetailDataSource (defined in the EOControl framework). You typically create a detail display group by dragging a to-many relationship from EOModeler to an open component in WebObjects Builder. Doing so sets the detail key and master object, so you rarely need to use this method.

__See also:__
[`hasDetailDataSource`](#apple-geyts), [`detailKey`](#apple-heyq), [`setMasterObject`](#apple-gi4tc)

---

### setFetchesOnLoad

public void `setFetchesOnLoad`(boolean _flag_)

Controls whether the receiver automatically fetches its objects after being loaded. If _flag_ is `true` it does; if _flag_ is `false` the receiver must be told explicitly to fetch. The default is `false`. You can also set this behavior in WebObjects Builder in the Display Group Options panel.

__See also:__
[`fetch`](#apple-geytc), [`fetchesOnLoad`](#apple-geytk)

---

### setInQueryMode

public void `setInQueryMode`(boolean _flag_)

Sets according to _flag_ whether the receiver is in query mode. In query mode, controls in the user interface that normally display values become empty, allowing users to type queries directly into them (this is also known as a "Query by Example" interface). In effect, the receiver's "displayedObjects" are replaced with an empty [`queryMatch`](#apple-ge4tc) dictionary. When [`qualifyDisplayGroup`](#apple-ge4dg) or [`qualifyDataSource`](#apple-ge3ts) is subsequently invoked, the query is performed and the display reverts to displaying values-this time, the objects returned by the query.

__See also:__
[`inQueryMode`](#apple-geztsnrq)

---

### setInsertedObjectDefaultValues

public void `setInsertedObjectDefaultValues`(NSDictionary _defaultValues_)

Sets default values to be used for newly inserted objects. When you use the [`insert`](#apple-ge2dg) method to add an object, that object is initially empty. Because the object is empty, there is no value to be displayed on the HTML page, meaning there is nothing for the user to select and modify. You use this method to provide at least one field that can be displayed for the newly inserted object. The possible keys into the dictionary are the properties of the entity managed by this display group. For example, a component that displays a list of movie titles and allows the user to insert new movie titles might contain these statements to ensure that all new objects have something to display as a movie title:

> ```
> [defaultValues setObject:@"New title" forKey:@"title"];
> ```

> ```
> [movies setInsertedObjectDefaultValues:defaultValues];
> ```

__See also:__
[`insertedObjectDefaultValues`](#apple-geztsobv)

---

### setMasterObject

public void `setMasterObject`(java.lang.Object _masterObject_)

Sets the master object to _masterObject_ for detail display groups and then performs a fetch if the display group is set to fetch on load. The master object owns the objects controlled by this display group.

Before you use this method, you should use the [`setDetailKey`](#apple-gi3tc) to set the key to this relationship. You typically create a detail display group by dragging a to-Many relationship from EOModeler to an open component in WebObjects Builder. Doing so sets the master object and detail key, so you typically do not have to use this method.

If the receiver is not a detail display group, this method has no effect.

__See also:__
[`hasDetailDataSource`](#apple-geyts), [`masterObject`](#apple-ge3dg)

---

### setNumberOfObjectsPerBatch

public void `setNumberOfObjectsPerBatch`(int _count_)

Sets the number of objects the receiver displays at a time. For example, suppose you are displaying one hundred records. Instead of displaying all of these at once, you can set the batch size so that the page displays a more manageable number (for example, 10). WebObjects Builder allows you to set the number of objects per batch on the Display Group Options panel.

__See also:__
[`batchCount`](#apple-guyq), [`displayNextBatch`](#apple-giydqmq), [`displayPreviousBatch`](#apple-geydg), [`numberOfObjectsPerBatch`](#apple-ge3do)

---

### setObjectArray

public void `setObjectArray`(NSArray _objects_)

Sets the receiver's objects to _objects_, regardless of what its EODataSource (defined in the EOControl framework) provides. This method doesn't affect the EODataSource's objects at all; specifically, it results in neither inserts nor deletes of objects in the EODataSource. _objects_ should contain objects with the same property names or methods as those accessed by the receiver. This method is used by `fetch` to set the array of fetched objects; you should rarely need to invoke it directly.

After setting the object array, this method restores as much of the original selection as possible. If there's no match and the receiver selects after fetching, then the first object is selected.

__See also:__
[`allObjects`](#apple-gqzq), [`displayedObjects`](#apple-geztsmry), [`fetch`](#apple-geytc), [`selectsFirstObjectAfterFetch`](#apple-gi2do)

---

### setQualifier

public void `setQualifier`(com.apple.yellow.eocontrol.EOQualifier _aQualifier_)

Sets the receiver's qualifier to _aQualifier_. This qualifier is used to filter the receiver's array of objects for display. Use [`updateDisplayedObjects`](#apple-gmzdo) to apply the qualifier.

If the receiver's delegate responds to [`displayArrayForObjects`](../Protocols/WODisplayGroup.Delegate.md#apple-geztima), that method is used instead of the qualifier to filter the objects.

__See also:__
[`displayedObjects`](#apple-geztsmry), [`qualifier`](#apple-gm3dimq)

---

### setSelectionIndexes

public boolean `setSelectionIndexes`(NSArray _selection_)

Selects the objects at _selection_ in the receiver's array if possible, returning `true` if successful and `false` if not (in which case the selection remains unaltered). _selection_ is an array of java.lang.Integers. This method is the primitive method for altering the selection; all other such methods invoke this one to make the change.

This method checks the delegate with a [`shouldChangeSelectionToIndexes`](../Protocols/WODisplayGroup.Delegate.md#apple-geztmmy) message. If the delegate returns `false`, this method also fails and returns `false`. If the receiver successfully changes the selection, its observers each receive a `subjectChanged` message and, if necessary, a [`displayGroupDidChangeSelectedObjects`](../Protocols/WODisplayGroup.Delegate.md#apple-ge2dgna) message.

__Note:__
The selection set here is only a programmatic selection; the objects on the screen are not highlighted
in any way.

__See also:__
[`allObjects`](#apple-gqzq)

---

### setSelectsFirstObjectAfterFetch

public void `setSelectsFirstObjectAfterFetch`(boolean _flag_)

Controls whether the receiver automatically selects its first displayed object after a fetch when there were no selected objects before the fetch. If _flag_ is `true` it does; if _flag_ is `false` then no objects are selected.

WODisplayGroups by default do select the first object after a fetch when there was no previous selection.

__See also:__
[`displayedObjects`](#apple-geztsmry), [`fetch`](#apple-geytc), [`selectsFirstObjectAfterFetch`](#apple-gi2do)

---

### setSortOrderings

public void `setSortOrderings`(NSArray _keySortOrderArray_)

Sets the EOSortOrdering objects (defined in the EOControl framework) that [`updateDisplayedObjects`](#apple-gmzdo) uses to sort the displayed objects to orderings. Use `updateDisplayedObjects` to apply the sort orderings.You can also set this value using the WebObjects Builder Display Group Options panel.

If the receiver's delegate responds to `displayGroup:displayArrayForObjects:`, that method is used instead of the sort orderings to order the objects.

__See also:__
[`displayedObjects`](#apple-geztsmry), [`sortOrderings`](#apple-gmzdg), [`updateDisplayedObjects`](#apple-gmzdo)

---

### setValidatesChangesImmediately

public void `setValidatesChangesImmediately`(boolean _flag_)

Controls the receiver's behavior on encountering a validation error. In the Web context, this method has no effect.

WODisplayGroups by default don't validate changes immediately.

__See also:__
-
saveChanges
(in EOControl's EOEditingContext), - tryToSaveChanges (EOEditingContext
Additions), [`validatesChangesImmediately`](#apple-gmztc)

---

### sortOrderings

public NSArray `sortOrderings`()

Returns an array of EOSortOrdering objects (defined in the EOControl framework) that [`updateDisplayedObjects`](#apple-gmzdo) uses to sort the displayed objects, as returned by the [`displayedObjects`](#apple-geztsmry) method.

__See also:__
[`setSortOrderings`](#apple-gmytk)

---

### updateDisplayedObjects

public void `updateDisplayedObjects`()

Recalculates the receiver's displayed objects arrays and redisplays. If the delegate responds to [`displayArrayForObjects`](../Protocols/WODisplayGroup.Delegate.md#apple-geztima), it's sent this message and the returned array is set as the WODisplayGroup's displayed objects. Otherwise, the receiver applies its qualifier and sort ordering to its array of objects. In either case, any objects that were selected before remain selected in the new displayed object's array.

__See also:__
[`redisplay`](#apple-giydo), [`allObjects`](#apple-gqzq), [`displayedObjects`](#apple-geztsmry), [`qualifier`](#apple-gm3dimq), [`selectedObjects`](#apple-gizts), [`sortOrderings`](#apple-gmzdg)

---

### validatesChangesImmediately

public boolean `validatesChangesImmediately`()

Returns `true` if the receiver immediately handles validation errors, or leaves them for the EOEditingContext (defined in the EOControl framework) to handle when saving changes.

By default, WODisplayGroups don't validate changes immediately.

__See also:__
[`setValidatesChangesImmediately`](#apple-gyzdemy)

****

---

[!](WODirectAction.md)
[!](WODynamicElement.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
