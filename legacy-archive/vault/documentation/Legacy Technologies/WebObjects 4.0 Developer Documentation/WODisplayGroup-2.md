---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WODisplayGroup.html
archived_at: '2026-07-18T01:28:53.841400Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WODirectAction-2.md)
[!](WODynamicElement-2.md)

---

# WODisplayGroup

__Inherits From:__
NSObject

__Conforms To:__
NSCoding
NSObject (NSObject)

__Declared in:__
WebObjects/WODisplayGroup.h

---

## Class Description

A WODisplayGroup is the basic user interface manager for a WebObjects application that accesses a database. It collects objects from an EODataSource (defined in EOControl), filters and sorts them, and maintains a selection in the filtered subset. You bind WebObjects dynamic elements to WODisplayGroup attributes and methods to display information from the database on your web page.

A WODisplayGroup manipulates its EODataSource by sending it __fetchObjects__ , __insertObject:__ , and other messages, and registers itself as an editor and message handler of the EODataSource's EOEditingContext (also defined in EOControl). The EOEditingContext then monitors the WODisplayGroup for changes to objects.

Most of a WODisplayGroup's interactions are with its EODataSource and its EOEditingContext. See the EODataSource, and EOEditingContext class specifications in the _Enterprise Objects Framework Reference_ for more information on these interactions.

---

## The Delegate

The WODisplayGroup delegate offers a number of methods, and WODisplayGroup invokes them as appropriate. Besides [__displayGroup:displayArrayForObjects:__](WODisplayGroupDelegate.md#apple-geztima), there are methods that inform the delegate that the WODisplayGroup has fetched, created an object (or failed to create one), inserted or deleted an object, changed the selection, or set a value for a property. There are also methods that request permission from the delegate to perform most of these same actions. The delegate can return YES to permit the action or NO to deny it. See each method's description in the WODisplayGroup.Delegates protocol specification for more information.

---

# Adopted Protocols

**NSCoding

**- encodeWithCoder:

**- initWithCoder:******

---

## Method Types

**Creating instances**

**[- init](#apple-gqzteobt)**

**Configuring behavior**

**[- setFetchesOnLoad:](#apple-gi3tk)

**[- fetchesOnLoad](#apple-geytk)

**[- setSelectsFirstObjectAfterFetch:](#apple-gmytc)

**[- selectsFirstObjectAfterFetch](#apple-gi2do)

**[- setValidatesChangesImmediately:](#apple-gyzdemy)

**[- validatesChangesImmediately](#apple-gmztc)************

**Setting the data source**

**[- setDataSource:](#apple-gi2tk)

**[- dataSource](#apple-gyzq)****

**Setting the qualifier and sort ordering**

**[- setQualifier:](#apple-gmydg)

**[- qualifier](#apple-gm3dimq)

**[- setSortOrderings:](#apple-gmytk)

**[- sortOrderings](#apple-gmzdg)********

**Managing queries**

**[- qualifierFromQueryValues](#apple-ge3tk)

**[- queryMatch](#apple-ge4tc)

**[- queryMax](#apple-ge4tk)

**[- queryMin](#apple-ge4ts)

**[- queryOperator](#apple-giydg)

**[- allQualifierOperators](#apple-gq3q)

**[- relationalQualifierOperators](#apple-giytc)

**[- setDefaultStringMatchFormat:](#apple-gi2ts)

**[- defaultStringMatchFormat](#apple-gy3q)

**[- setDefaultStringMatchOperator:](#apple-gi3dg)

**[- defaultStringMatchOperator](#apple-g4yq)

**[- qualifyDisplayGroup](#apple-ge4dg)

**[- qualifyDataSource](#apple-ge3ts)

**[- inQueryMode](#apple-geztsnrq)

**[- setInQueryMode:](#apple-gm4doni)******************************

**Fetching objects from the data source**

**[- fetch](#apple-geytc)**

**Getting the objects**

**[- allObjects](#apple-gqzq)

**[- displayedObjects](#apple-geztsmry)****

**Batching the results**

**[- setNumberOfObjectsPerBatch:](#apple-gi4tk)

**[- numberOfObjectsPerBatch](#apple-ge3do)

**[- hasMultipleBatches](#apple-gezdg)

**[- displayNextBatch](#apple-giydqmq)

**[- displayPreviousBatch](#apple-geydg)

**[- batchCount](#apple-guyq)

**[- setCurrentBatchIndex:](#apple-gi2tc)

**[- currentBatchIndex](#apple-gu4q)

**[- indexOfFirstDisplayedObject](#apple-gezdenby)

**[- indexOfLastDisplayedObject](#apple-gezdenju)

**[- displayBatchContainingSelectedObject](#apple-he2q)**********************

**Updating display of values**

**[- redisplay](#apple-giydo)

**[- updateDisplayedObjects](#apple-gmzdo)****

**Setting the objects**

**[- setObjectArray:](#apple-gi4ts)**

**Changing the selection**

**[- setSelectionIndexes:](#apple-gm4tkmy)

**[- selectObjectsIdenticalTo:](#apple-ge2danjz)

**[- selectObjectsIdenticalTo:selectFirstOnNoMatch:](#apple-ge2danzt)

**[- selectObject:](#apple-ge2danbv)

**[- clearSelection](#apple-gu2q)

**[- selectNext](#apple-ge2damrw)

**[- selectPrevious](#apple-ge2daobx)**************

**Examining the selection**

**[- selectionIndexes](#apple-gi2dg)

**[- selectedObject](#apple-giztk)

**[- selectedObjects](#apple-gizts)******

**Inserting and deleting objects**

**[- insertObject: atIndex:](#apple-gqztimzz)

**[- insertObjectAtIndex:](#apple-ge2dambt)

**[- insert](#apple-ge2dg)

**[- setInsertedObjectDefaultValues:](#apple-gi4dg)

**[- insertedObjectDefaultValues](#apple-geztsobv)

**[- deleteObjectAtIndex:](#apple-hazq)

**[- deleteSelection](#apple-gm2domq)

**[- delete](#apple-g44q)****************

**Setting up a detail display group**

**[- hasDetailDataSource](#apple-geyts)

**[- setMasterObject:](#apple-gi4tc)

**[- masterObject](#apple-ge3dg)

**[- setDetailKey:](#apple-gi3tc)

**[- detailKey](#apple-heyq)**********

**Working with named fetch specifications**

**[- queryBindings](#apple-gezdgnry)**

**Setting the delegate**

**[- setDelegate:](#apple-gi3do)

**[- delegate](#apple-g42q)****

---

## Instance Methods

---

### allObjects

- (NSArray \*)__allObjects__

Returns all of the objects collected by the receiver.

__See also:__
[- __displayedObjects__](#apple-geztsmry), [- __fetch__](#apple-geytc)

---

### allQualifierOperators

- (NSArray \*)__allQualifierOperators__

Returns an array containing all of the relational operators supported by EOControl's EOQualifier: =, !=, <, <=, >, >=, "__like__ " and "__caseInsensitiveLike__ ".

__See also:__
[- __queryOperator__](#apple-giydg), [- __relationalQualifierOperators__](#apple-giytc)

---

### batchCount

- (unsigned)__batchCount__

The number of batches to display. For example, if the displayed objects array contains two hundred records and the batch size is ten, __batchCount__  returns twenty (twenty batches of ten records each).

__See also:__
[- __currentBatchIndex__](#apple-gu4q), [- __displayNextBatch__](#apple-giydqmq), [- __displayPreviousBatch__](#apple-geydg), [- __hasMultipleBatches__](#apple-gezdg),
[- __numberOfObjectsPerBatch__](#apple-ge3do)

---

### clearSelection

- (BOOL)__clearSelection__

Invokes [__setSelectionIndexes:__](#apple-gm4tkmy) to clear the selection, returning YES on success and NO on failure.

---

### currentBatchIndex

- (unsigned)__currentBatchIndex__

Returns the index of the batch currently being displayed. The total batch count equals the number of displayed objects divided by the batch size. For example, if the WODisplayGroup has one hundred objects to display and the batch size is twenty, there are five batches. The first batch has a batch index of 1.

__See also:__
[- __batchCount__](#apple-guyq), [- __numberOfObjectsPerBatch__](#apple-ge3do), [- __setCurrentBatchIndex:__](#apple-gi2tc)

---

### dataSource

- (EODataSource \*)__dataSource__

Returns the receiver's EODataSource (defined in the EOControl framework).

__See also:__
[- __hasDetailDataSource__](#apple-geyts), [- __setDataSource:__](#apple-gi2tk)

---

### defaultStringMatchFormat

- (NSString \*)__defaultStringMatchFormat__

Returns the format string that specifies how pattern matching will be performed on string values in the [__queryMatch__](#apple-ge4tc) dictionary. If a key in the __queryMatch__  dictionary does not have an associated operator in the [__queryOperator__](#apple-giydg) dictionary, then its value is matched using pattern matching, and the format string returned by this method specifies how it will be matched.

__See also:__
[- __defaultStringMatchOperator__](#apple-g4yq), [- __setDefaultStringMatchFormat:__](#apple-gi2ts)

---

### defaultStringMatchOperator

- (NSString \*)__defaultStringMatchOperator__

Returns the operator used to perform pattern matching for string values in the [__queryMatch__](#apple-ge4tc) dictionary. If a key in the __queryMatch__  dictionary does not have an associated operator in the [__queryOperator__](#apple-giydg) dictionary, then the operator returned by this method is used to perform pattern matching. Unless the default is changed, this method returns caseInsensitiveLike.

__See also:__
[- __defaultStringMatchFormat__](#apple-gy3q), [- __setDefaultStringMatchOperator:__](#apple-gi3dg)

---

### delegate

- (id)__delegate__

Returns the receiver's delegate.

__See also:__
[- __setDelegate:__](#apple-gi3do)

---

### delete

- (id)__delete__

Uses [__deleteSelection__](#apple-gm2domq) to attempt to delete the selected objects and then causes the page to reload. Returns __nil__  to force reloading of the web page.

__See also:__
[- __deleteObjectAtIndex:__](#apple-hazq)

---

### deleteObjectAtIndex:

- (BOOL)__deleteObjectAtIndex:__ (unsigned)_index_

Attempts to delete the object at _index_, returning YES if successful and NO if not. Checks with the delegate using the method [__displayGroup:shouldDeleteObject:__](WODisplayGroupDelegate.md#apple-geztonq). If the delegate returns NO, this method fails and returns NO. If successful, it sends the delegate a [__displayGroup:didDeleteObject:__](WODisplayGroupDelegate.md#apple-geztama) message.

This method performs the delete by sending __deleteObject__  to the EODataSource (defined in the EOControl framework). If that message raises an exception, this method fails and returns NO.

__See also:__
[- __delete__](#apple-g44q), [- __deleteSelection__](#apple-gm2domq)

---

### deleteSelection

- (BOOL)__deleteSelection__

Attempts to delete the selected objects, returning YES if successful and NO if not.

__See also:__
[- __delete__](#apple-g44q), [- __deleteObjectAtIndex:__](#apple-hazq)

---

### detailKey

- (NSString \*)__detailKey__

For detail display groups, returns the key to the master object that specifies what this detail display group represents. That is, if you send the object returned by the [__masterObject__](#apple-ge3dg) method a __valueForKey:__  message with this key, you obtain the objects controlled by this display group.

This method returns __nil__  if the receiver is not a detail display group or if the detail key has not yet been set. You typically create a detail display group by dragging a to-many relationship from EOModeler to an open component in WebObjects Builder.

__See also:__
[- __hasDetailDataSource__](#apple-geyts), [- __masterObject__](#apple-ge3dg), [- __setDetailKey:__](#apple-gi3tc)

---

### displayBatchContainingSelectedObject

- (id)__displayBatchContainingSelectedObject__

Displays the batch containing the selection and sets the current batch index to that batch's index. Returns __nil__  to force the page to reload.

__See also:__
: [- __displayNextBatch__](#apple-giydqmq), [- __displayPreviousBatch__](#apple-geydg), [- __setCurrentBatchIndex:__](#apple-gi2tc)

---

### displayedObjects

- (NSArray \*)__displayedObjects__

Returns the objects that should be displayed or otherwise made available to the user, as filtered by the receiver's delegate, by the receiver's qualifier and sort ordering.

If batching is in effect, __displayedObjects__  returns the current batch of objects.

__See also:__
[- __allObjects__](#apple-gqzq), [- __updateDisplayedObjects__](#apple-gmzdo), [- __qualifier__](#apple-gm3dimq), [- __setSortOrderings:__](#apple-gmytk), [- __displayGroup:
displayArrayForObjects:__](../Protocols/WODisplayGroup.Delegate.md#apple-geztima) (delegate method)

---

### displayNextBatch

- (id)__displayNextBatch__

Increments the current batch index, displays that batch of objects, and clears the selection. If the batch currently being displayed is the last batch, this method displays the first batch of objects. Returns __nil__  to force the page to reload.

__See also:__
[- __batchCount__](#apple-guyq), [- __currentBatchIndex__](#apple-gu4q), [- __displayBatchContainingSelectedObject__](#apple-he2q),
[- __displayPreviousBatch__](#apple-geydg)

---

### displayPreviousBatch

- (id)__displayPreviousBatch__

Decrements the current batch index, displays that batch of objects, and clears the selection. If the batch currently being displayed is the first batch, this method displays the last batch of objects. Returns __nil__  to force the page to reload.

__See also:__
[- __batchCount__](#apple-guyq), [- __currentBatchIndex__](#apple-gu4q), [- __displayBatchContainingSelectedObject__](#apple-he2q),
[- __displayNextBatch__](#apple-giydqmq)

---

### fetch

- (id)__fetch__

Attempts to fetch objects from the EODataSource (defined in the EOControl framework).

Before fetching, this method sends [__displayGroupShouldFetch:__](WODisplayGroupDelegate.md#apple-ge2dkmq) to the delegate. If this method was successful, it then sends a __fetchObjects__  message to the receiver's EODataSource to replace the object array, and if successful sends the delegate a [__displayGroup:didFetchObjects:__](WODisplayGroupDelegate.md#apple-geztaoi) message.

This method returns __nil__  to force the page to reload.

__See also:__
[- __allObjects__](#apple-gqzq), [- __updateDisplayedObjects__](#apple-gmzdo)

---

### fetchesOnLoad

- (BOOL)__fetchesOnLoad__

Returns YES if the receiver fetches automatically after the component that contains it is loaded, NO if it must be told explicitly to fetch. The default is YES. You can set this behavior in WebObjects Builder using the Display Group Options panel. Note that if the display group fetches on load, it performs the fetch each time the component is loaded into the web browser.

__See also:__
[- __fetch__](#apple-geytc), [- __setFetchesOnLoad:__](#apple-gi3tk)

---

### hasDetailDataSource

- (BOOL)__hasDetailDataSource__

Returns YES if the display group's data source is an EODetailDataSource (defined in the EOControl framework), and NO otherwise. If you drag a to-many relationship from EOModeler to an open component in WebObjects Builder, you create a display group that has an EODetailDataSource. You can also set this up using the Display Group Options panel in WebObjects Builder.

__See also:__
[- __detailKey__](#apple-heyq), [- __masterObject__](#apple-ge3dg)

---

### hasMultipleBatches

- (BOOL)__hasMultipleBatches__

Returns YES if the batch count is greater than 1. A display group displays its objects in batches if the [__numberOfObjectsPerBatch__](#apple-ge3do) method returns a number that is less than the number of objects in the [__displayedObjects__](#apple-geztsmry) array.

__See also:__
[- __batchCount__](#apple-guyq), [- __setNumberOfObjectsPerBatch:__](#apple-gi4tk)

---

### indexOfFirstDisplayedObject

- (unsigned)__indexOfFirstDisplayedObject__

Returns the index of the first object displayed by the current batch. For example, if the current batch is displaying items 11 through 20, this method returns 11.

__See also:__
[- __indexOfLastDisplayedObject__](#apple-gezdenju)

---

### indexOfLastDisplayedObject

- (unsigned)__indexOfLastDisplayedObject__

Returns the index of the last object display by the current batch. For example, if the current batch is displaying items 11 through 20, this method returns 20.

__See also:__
[- __indexOfFirstDisplayedObject__](#apple-gezdenby)

---

### init

- __init__

Initializes the WODisplayGroup. The WODisplayGroup then needs to have an EODataSource set with [__setDataSource:__](#apple-gi2tk).

---

### inQueryMode

- (BOOL)__inQueryMode__

Returns YES to indicate that the receiver is in query mode, NO otherwise. In query mode, controls in the user interface that normally display values become empty, allowing users to type queries directly into them (this is also known as a "Query by Example" interface). In effect, the receiver's "displayedObjects" are replaced with an empty [__queryMatch__](#apple-ge4tc) dictionary. When [__qualifyDisplayGroup__](#apple-ge4dg) or [__qualifyDataSource__](#apple-ge3ts) is subsequently invoked, the query is performed and the display reverts to displaying values-this time, the objects returned by the query.

__See also:__
[- __setInQueryMode:__](#apple-gm4doni)

---

### insert

- (id)__insert__

Invokes [__insertObjectAtIndex:__](#apple-ge2dambt) with an index just past the first index in the selection, or at the end if there's no selection.

This method returns __nil__  to force the page to reload.

---

### insertedObjectDefaultValues

- (NSDictionary \*)__insertedObjectDefaultValues__

Returns the default values to be used for newly inserted objects. The keys into the dictionary are the properties of the entity that the display group manages. If the dictionary returned by this method is empty, the [__insert__](#apple-ge2dg) method adds an object that is initially empty. Because the object is empty, the display group has no value to display on the HTML page for that object, meaning that there is nothing for the user to select and modify. Use the [__setInsertedObjectDefaultValues:__](#apple-gi4dg) method to set up a default value so that there is something to display on the page.

---

### insertObjectAtIndex:

- (id)__insertObjectAtIndex:__ (unsigned)_index_

Asks the receiver's EODataSource (defined in the EOControl framework) to create a new object by sending it a __createObject__  message, then inserts the new object using [__insertObject: atIndex:__](#apple-gqztimzz). If a new object can't be created, this method sends the delegate a [__displayGroup:createObjectFailedForDataSource:__](WODisplayGroupDelegate.md#apple-gi2dgnq) message.

If the object is successfully created, this method then sets the default values specified by [__insertedObjectDefaultValues__](#apple-geztsobv).

__See also:__
[- __insert__](#apple-ge2dg)

---

### insertObject: atIndex:

- (void)__insertObject:__ _anObject___atIndex:__ (unsigned)_index_

Inserts _anObject_ into the receiver's EODataSource and displayed objects at _index_, if possible. This method checks with the delegate before actually inserting, using [__displayGroup:shouldInsertObject:atIndex:__](WODisplayGroupDelegate.md#apple-geztqni). If the delegate refuses, _anObject_ isn't inserted. After successfully inserting the object, this method informs the delegate with a [__displayGroup:didInsertObject:__](WODisplayGroupDelegate.md#apple-geztemq) message, and selects the newly inserted object.

Raises an NSRangeException if index is out of bounds.

__See also:__
[- __insertObjectAtIndex:__](#apple-ge2dambt), [- __insert__](#apple-ge2dg)

---

### masterObject

- (id)__masterObject__

Returns the master object for a detail display group (a display group that represents a detail in a master-detail relationship). A detail display group is one that uses an EODetailDataSource (defined in the EOControl framework). You create a detail display group by dragging a to-many relationship from EOModeler to an open component in WebObjects Builder. If the display group is not a detail display group or does not have a master object set, this method returns __nil__ .

__See also:__
[- __detailKey__](#apple-heyq), [- __hasDetailDataSource__](#apple-geyts), [- __setMasterObject:__](#apple-gi4tc)

---

### numberOfObjectsPerBatch

- (unsigned)__numberOfObjectsPerBatch__

Returns the batch size. You can set the batch size using [__setNumberOfObjectsPerBatch:__](#apple-gi4tk) or using WebObjects Builder's Display Group Options panel.

---

### qualifier

- (EOQualifier \*)__qualifier__

Returns the receiver's qualifier, which it uses to filter its array of objects for display when the delegate doesn't do so itself.

__See also:__
[- __displayedObjects__](#apple-geztsmry), [- __setQualifier:__](#apple-gmydg):,[- __updateDisplayedObjects__](#apple-gmzdo)

---

### qualifierFromQueryValues

- (EOQualifier \*)__qualifierFromQueryValues__

Builds a qualifier constructed from entries in these query dictionaries: [__queryMatch__](#apple-ge4tc), [__queryMax__](#apple-ge4tk), [__queryMin__](#apple-ge4ts), and [__queryOperator__](#apple-giydg).

__See also:__
[- __qualifyDataSource__](#apple-ge3ts), [- __qualifyDisplayGroup__](#apple-ge4dg)

---

### qualifyDataSource

- (void)__qualifyDataSource__

Takes the result of [__qualifierFromQueryValues__](#apple-ge3tk) and applies to the receiver's data source. The receiver then sends itself a [__fetch__](#apple-geytc) message. If the receiver is in query mode, query mode is exited. This method differs from [__qualifyDisplayGroup__](#apple-ge4dg) as follows: whereas __qualifyDisplayGroup__  performs in-memory filtering of already fetched objects, __qualifyDataSource__  triggers a new qualified fetch against the database.

__See also:__
[- __queryMatch__](#apple-ge4tc), [- __queryMax__](#apple-ge4tk),, [- __queryMin__](#apple-ge4ts),[- __queryOperator__](#apple-giydg)

---

### qualifyDisplayGroup

- (void)__qualifyDisplayGroup__

Takes the result of the [__qualifierFromQueryValues__](#apple-ge3tk) and applies to the receiver using [__setQualifier:__](#apple-gmydg). The method [__updateDisplayedObjects__](#apple-gmzdo) is invoked to refresh the display. If the receiver is in query mode, query mode is exited.

__See also:__
[- __qualifyDataSource__](#apple-ge3ts), [- __queryMatch__](#apple-ge4tc), [- __queryMax__](#apple-ge4tk), -[- __queryMin__](#apple-ge4ts), [- __queryOperator__](#apple-giydg)

---

### queryBindings

- (NSMutableDictionary \*)__queryBindings__

Returns a dictionary containing the actual values that the user wants to query upon. You use this method to perform a query stored in the model file. Bind keys in this dictionary to elements on your component that specify query values, then pass this dictionary to the fetch specification that performs the fetch. <<revisit>>

---

### queryMatch

- (NSMutableDictionary \*)__queryMatch__

Returns a dictionary of query values to match. The [__qualifierFromQueryValues__](#apple-ge3tk) method uses this dictionary along with the [__queryMax__](#apple-ge4tk) and [__queryMin__](#apple-ge4ts) dictionaries to construct qualifiers.

Use the [__queryOperator__](#apple-giydg) dictionary to specify the type of matching (=, <, >, __like__ , and so on) for each key in the __queryMatch__  dictionary.

If the __queryOperator__  dictionary does not contain a key contained in the __queryMatch__  dictionary, the default is to match the value exactly (=) if the value is a number or a date and to perform pattern matching if the value is an NSString. In the case of string values, the [__defaultStringMatchFormat__](#apple-gy3q) and [__defaultStringMatchOperator__](#apple-g4yq) specify exactly how the pattern matching will be performed.

__See also:__
[- __allQualifierOperators__](#apple-gq3q), [- __qualifyDataSource__](#apple-ge3ts), [- __qualifyDisplayGroup__](#apple-ge4dg),
[- __relationalQualifierOperators__](#apple-giytc)

---

### queryMax

- (NSMutableDictionary \*)__queryMax__

Returns a dictionary of "less than" query values. The [__qualifierFromQueryValues__](#apple-ge3tk) method uses this dictionary along with the [__queryMatch__](#apple-ge4tc) and [__queryMin__](#apple-ge4ts) dictionaries to construct qualifiers.

__See also:__
[- __qualifyDataSource__](#apple-ge3ts), [- __qualifyDisplayGroup__](#apple-ge4dg), [- __queryOperator__](#apple-giydg)

---

### queryMin

- (NSMutableDictionary \*)__queryMin__

Returns a dictionary of "greater than" query values. The [__qualifierFromQueryValues__](#apple-ge3tk) method uses this dictionary along with the [__queryMatch__](#apple-ge4tc) and __queryMin__  dictionaries to construct qualifiers.

__See also:__
[- __qualifyDataSource__](#apple-ge3ts), [- __qualifyDisplayGroup__](#apple-ge4dg), [- __queryOperator__](#apple-giydg)

---

### queryOperator

- (NSMutableDictionary \*)__queryOperator__

Returns a dictionary of operators to use on items in the [__queryMatch__](#apple-ge4tc) dictionary. If a key in the __queryMatch__  dictionary also exists in __queryOperator__ , that operator for that key is used. The [__allQualifierOperators__](#apple-gq3q) method returns the operator strings you can use as values in this dictionary.

__See also:__
[- __qualifierFromQueryValues__](#apple-ge3tk), [- __queryMax__](#apple-ge4tk), [- __queryMin__](#apple-ge4ts), [- __relationalQualifierOperators__](#apple-giytc)

---

### redisplay

- (void)__redisplay__

Sends out a contents changed notification.

---

### relationalQualifierOperators

- (NSArray \*)__relationalQualifierOperators__

Returns an array containing all of the relational operators supported by EOControl's EOQualifier: =, !=, <, <=, >, and >=. In other words, returns all of the EOQualifier operators except for the ones that work exclusively on strings: "__like__ " and "__caseInsensitiveLike__ ".

__See also:__
[- __allQualifierOperators__](#apple-gq3q), [- __queryOperator__](#apple-giydg)

---

### selectedObject

- (id)__selectedObject__

Returns the first selected object in the displayed objects array, or __nil__  if there's no such object.

__See also:__
[- __displayedObjects__](#apple-geztsmry), [- __selectionIndexes__](#apple-gi2dg), [- __selectedObjects__](#apple-gizts)

---

### selectedObjects

- (NSArray \*)__selectedObjects__

Returns the objects selected in the receiver's displayed objects array.

__See also:__
[- __displayedObjects__](#apple-geztsmry), [- __selectionIndexes__](#apple-gi2dg), [- __selectedObject__](#apple-giztk)

---

### selectionIndexes

- (NSArray \*)__selectionIndexes__

Returns the selection as an array of NSNumbers. The NSNumbers are indexes into the array returned by [__displayedObjects__](#apple-geztsmry).

__See also:__
[- __selectedObject__](#apple-giztk), [- __selectedObjects__](#apple-gizts), [- __setSelectionIndexes:__](#apple-gm4tkmy)

---

### selectNext

- (id)__selectNext__

Attempts to select the object just after the currently selected one. The selection is altered in this way:

- If there are no objects, does nothing.
- If there's no selection, selects the object at index zero.
- If the first selected object is the last object in the displayed objects array, selects the first object.
- Otherwise selects the object after the first selected object.

This method returns __nil__  to force the page to reload.

__See also:__
[- __selectPrevious__](#apple-ge2daobx), [- __setSelectionIndexes:__](#apple-gm4tkmy)

---

### selectObject:

- (BOOL)__selectObject:__ (id)_anObject_

Attempts to select the object equal to _anObject_ in the receiver's displayed objects array, returning YES if successful and NO otherwise. _anObject_ is equal to an object in the displayed objects array if its address is the same as the object in the array.

__See also:__
[- __selectNext__](#apple-ge2damrw), [- __selectPrevious__](#apple-ge2daobx)

---

### selectObjectsIdenticalTo:

- (BOOL)__selectObjectsIdenticalTo:__ (NSArray \*)_objectSelection_

Attempts to select the objects in the receiver's displayed objects array whose __id__ s are equal to those of objects, returning YES if successful and NO otherwise.

__See also:__
[- __setSelectionIndexes:__](#apple-gm4tkmy), [- __selectObjectsIdenticalTo:selectFirstOnNoMatch:__](#apple-ge2danzt)

---

### selectObjectsIdenticalTo:selectFirstOnNoMatch:

- (BOOL)__selectObjectsIdenticalTo:__ (NSArray \*)_objects___selectFirstOnNoMatch:__ (BOOL)_flag_

Selects the objects in the receiver's displayed objects array whose __id__ s are equal to those of _objects_, returning YES if successful and NO otherwise. If no objects in the displayed objects array match objects and _flag_ is YES, attempts to select the first object in the displayed objects array.

__See also:__
[- __setSelectionIndexes:__](#apple-gm4tkmy), [- __selectObjectsIdenticalTo:__](#apple-ge2danjz)

---

### selectPrevious

- (id)__selectPrevious__

Attempts to select the object just before the presently selected one. The selection is altered in this way:

- If there are no objects, does nothing.
- If there's no selection, selects the object at index zero.
- If the first selected object is at index zero, selects the last object.
- Otherwise selects the object before the first selected object.

This method returns __nil__  to force the page to reload.

__See also:__
[- __selectNext__](#apple-ge2damrw), [- __redisplay__](#apple-giydo)

---

### selectsFirstObjectAfterFetch

- (BOOL)__selectsFirstObjectAfterFetch__

Returns YES YES if the receiver automatically selects its first displayed object after a fetch if there was no selection, NO if it leaves an empty selection as-is.

WODisplayGroups by default do select the first object after a fetch when there was no previous selection.

__See also:__
[- __displayedObjects__](#apple-geztsmry), [- __fetch__](#apple-geytc), [- __setSelectsFirstObjectAfterFetch:__](#apple-gmytc)

---

### setCurrentBatchIndex:

- (void)__setCurrentBatchIndex:__ (unsigned)_anInt_

Displays the _anInt_ batch of objects. The total batch count equals the number of displayed objects divided by the batch size. For example, if the WODisplayGroup has one hundred objects to display and the batch size is twenty, there are five batches. The first batch has a batch index of 1. __setCurrentBatchIndex:3__  would display the third batch of objects (objects 41 to 60 in this example).

If _anInt_ is greater than the number of batches, this method displays the first batch.

__See also:__
[- __batchCount__](#apple-guyq), [- __currentBatchIndex__](#apple-gu4q),
[- __displayBatchContainingSelectedObject__](#apple-he2q),[- __displayNextBatch__](#apple-giydqmq), [- __displayPreviousBatch__](#apple-geydg),[- __numberOfObjectsPerBatch__](#apple-ge3do)

---

### setDataSource:

- (void)__setDataSource:__ (EODataSource \*)_aDataSource_

Sets the receiver's EODataSource (defined in the EOControl framework) to _aDataSource_. In the process, it performs these actions:

Unregisters itself as an editor and message handler for the previous EODataSource's EOEditingContext (also defined in EOControl), if necessary, and registers itself with _aDataSource_'s EOEditingContext. If the new EOEditingContext already has a message handler, however, the receiver doesn't assume that role.

Clears the receiver's array of objects.

Sends [__displayGroupDidChangeDataSource:__](WODisplayGroupDelegate.md#apple-ge2demy) to the delegate if there is one.

__See also:__
[- __dataSource__](#apple-gyzq)

---

### setDefaultStringMatchFormat:

- (void)__setDefaultStringMatchFormat:__ (NSString \*)_format_

Sets how pattern matching will be performed on NSString values in the [__queryMatch__](#apple-ge4tc) dictionary. This format is used for properties listed in the __queryMatch__  dictionary that have NSString values and that do not have an associated entry in the [__queryOperator__](#apple-giydg) dictionary. In these cases, the value is matched using pattern matching and _format_ specifies how it will be matched.

The default format string for pattern matching is "__%@\*__ " which means that the string value in the __queryMatch__  dictionary is used as a prefix. For example, if the __queryMatch__  dictionary contains a value "Jo" for the key "Name", the query returns all records whose name values begin with "Jo".

__See also:__
[- __defaultStringMatchFormat__](#apple-gy3q), [- __setDefaultStringMatchOperator:__](#apple-gi3dg)

---

### setDefaultStringMatchOperator:

- (void)__setDefaultStringMatchOperator:__ (NSString \*)_operator_

Sets the operator used to perform pattern matching for NSString values in the [__queryMatch__](#apple-ge4tc) dictionary. This operator is used for properties listed in the __queryMatch__  dictionary that have NSString values and that do not have an associated entry in the [__queryOperator__](#apple-giydg) dictionary. In these cases, the operator _operator_ is used to perform pattern matching.

The default value for the query match operator is __caseInsensitiveLike__ , which means that the query does not consider case when matching letters. The other possible value for this operator is __like__ , which matches the case of the letters exactly.

__See also:__
[- __allQualifierOperators__](#apple-gq3q), [- __defaultStringMatchOperator__](#apple-g4yq), [- __relationalQualifierOperators__](#apple-giytc),
[- __setDefaultStringMatchFormat:__](#apple-gi2ts)

---

### setDelegate:

- (void)__setDelegate:__ (id)_anObject_

Sets the receiver's delegate to _anObject_, without retaining it.

__See also:__
[- __delegate__](#apple-g42q), [WODisplayGroupDelegate](WODisplayGroupDelegate.md)

---

### setDetailKey:

- (void)__setDetailKey:__ (NSString \*)_detailKey_

Sets the detail key to _detailKey_ for a detail display group. The detail key is the key that retrieves from the master object the objects that this display group manages. You must set a detail key before you set a master object.

If the receiver is not a detail display group, this method has no effect. A display group is a detail display group if its data source is an EODetailDataSource (defined in the EOControl framework). You typically create a detail display group by dragging a to-many relationship from EOModeler to an open component in WebObjects Builder. Doing so sets the detail key and master object, so you rarely need to use this method.

__See also:__
[- __hasDetailDataSource__](#apple-geyts), [- __detailKey__](#apple-heyq), [- __setMasterObject:__](#apple-gi4tc)

---

### setFetchesOnLoad:

- (void)__setFetchesOnLoad:__ (BOOL)_flag_

Controls whether the receiver automatically fetches its objects after being loaded. If _flag_ is YES it does; if _flag_ is NO the receiver must be told explicitly to fetch. The default is NO. You can also set this behavior in WebObjects Builder in the Display Group Options panel.

__See also:__
[- __fetch__](#apple-geytc), [- __fetchesOnLoad__](#apple-geytk)

---

### setInQueryMode:

- (void)__setInQueryMode:__ (BOOL)_flag_

Sets according to _flag_ whether the receiver is in query mode. In query mode, controls in the user interface that normally display values become empty, allowing users to type queries directly into them (this is also known as a "Query by Example" interface). In effect, the receiver's "displayedObjects" are replaced with an empty [__queryMatch__](#apple-ge4tc) dictionary. When [__qualifyDisplayGroup__](#apple-ge4dg) or [__qualifyDataSource__](#apple-ge3ts) is subsequently invoked, the query is performed and the display reverts to displaying values-this time, the objects returned by the query.

__See also:__
[- __inQueryMode__](#apple-geztsnrq)

---

### setInsertedObjectDefaultValues:

- (void)__setInsertedObjectDefaultValues:__ (NSDictionary \*)_defaultValues_

Sets default values to be used for newly inserted objects. When you use the [__insert__](#apple-ge2dg) method to add an object, that object is initially empty. Because the object is empty, there is no value to be displayed on the HTML page, meaning there is nothing for the user to select and modify. You use this method to provide at least one field that can be displayed for the newly inserted object. The possible keys into the dictionary are the properties of the entity managed by this display group. For example, a component that displays a list of movie titles and allows the user to insert new movie titles might contain these statements to ensure that all new objects have something to display as a movie title:

> ```
> [defaultValues setObject:@"New title" forKey:@"title"];
> ```

> ```
> [movies setInsertedObjectDefaultValues:defaultValues];
> ```

__See also:__
[- __insertedObjectDefaultValues__](#apple-geztsobv)

---

### setMasterObject:

- (void)__setMasterObject:__ (id)_masterObject_

Sets the master object to _masterObject_ for detail display groups and then performs a fetch if the display group is set to fetch on load. The master object owns the objects controlled by this display group.

Before you use this method, you should use the [__setDetailKey:__](#apple-gi3tc) to set the key to this relationship. You typically create a detail display group by dragging a to-Many relationship from EOModeler to an open component in WebObjects Builder. Doing so sets the master object and detail key, so you typically do not have to use this method.

If the receiver is not a detail display group, this method has no effect.

__See also:__
[- __hasDetailDataSource__](#apple-geyts), [- __masterObject__](#apple-ge3dg)

---

### setNumberOfObjectsPerBatch:

- (void)__setNumberOfObjectsPerBatch:__ (unsigned)_count_

Sets the number of objects the receiver displays at a time. For example, suppose you are displaying one hundred records. Instead of displaying all of these at once, you can set the batch size so that the page displays a more manageable number (for example, 10). WebObjects Builder allows you to set the number of objects per batch on the Display Group Options panel.

__See also:__
[- __batchCount__](#apple-guyq), [- __displayNextBatch__](#apple-giydqmq), [- __displayPreviousBatch__](#apple-geydg), [- __numberOfObjectsPerBatch__](#apple-ge3do)

---

### setObjectArray:

- (void)__setObjectArray:__ (NSArray \*)_objects_

Sets the receiver's objects to _objects_, regardless of what its EODataSource (defined in the EOControl framework) provides. This method doesn't affect the EODataSource's objects at all; specifically, it results in neither inserts nor deletes of objects in the EODataSource. _objects_ should contain objects with the same property names or methods as those accessed by the receiver. This method is used by __fetch__  to set the array of fetched objects; you should rarely need to invoke it directly.

After setting the object array, this method restores as much of the original selection as possible. If there's no match and the receiver selects after fetching, then the first object is selected.

__See also:__
[- __allObjects__](#apple-gqzq), [- __displayedObjects__](#apple-geztsmry), [- __fetch__](#apple-geytc), [- __selectsFirstObjectAfterFetch__](#apple-gi2do)

---

### setQualifier:

- (void)__setQualifier:__ (EOQualifier \*)_aQualifier_

Sets the receiver's qualifier to _aQualifier_. This qualifier is used to filter the receiver's array of objects for display. Use [__updateDisplayedObjects__](#apple-gmzdo) to apply the qualifier.

If the receiver's delegate responds to [__displayGroup:displayArrayForObjects:__](WODisplayGroupDelegate.md#apple-geztima), that method is used instead of the qualifier to filter the objects.

__See also:__
[- __displayedObjects__](#apple-geztsmry), [- __qualifier__](#apple-gm3dimq)

---

### setSelectionIndexes:

- (BOOL)__setSelectionIndexes:__ (NSArray \*)_selection_

Selects the objects at _selection_ in the receiver's array if possible, returning YES if successful and NO if not (in which case the selection remains unaltered). This method is the primitive method for altering the selection; all other such methods invoke this one to make the change.

This method checks the delegate with a [__displayGroup:shouldChangeSelectionToIndexes:__](WODisplayGroupDelegate.md#apple-geztmmy) message. If the delegate returns NO, this method also fails and returns NO. If the receiver successfully changes the selection, its observers each receive a [__displayGroupDidChangeSelection:__](WODisplayGroupDelegate.md#apple-ge2dimy) message and, if necessary, a [__displayGroupDidChangeSelectedObjects:__](WODisplayGroupDelegate.md#apple-ge2dgna) message.

__Note:__
The selection set here is only a programmatic selection; the objects on the screen are not highlighted
in any way.

__See also:__
[- __allObjects__](#apple-gqzq)

---

### setSelectsFirstObjectAfterFetch:

- (void)__setSelectsFirstObjectAfterFetch:__ (BOOL)_flag_

Controls whether the receiver automatically selects its first displayed object after a fetch when there were no selected objects before the fetch. If _flag_ is YES it does; if _flag_ is NO then no objects are selected.

WODisplayGroups by default do select the first object after a fetch when there was no previous selection.

__See also:__
[- __displayedObjects__](#apple-geztsmry), [- __fetch__](#apple-geytc), [- __selectsFirstObjectAfterFetch__](#apple-gi2do)

---

### setSortOrderings:

- (void)__setSortOrderings:__ (NSArray \*)_keySortOrderArray_

Sets the EOSortOrdering objects (defined in the EOControl framework) that [__updateDisplayedObjects__](#apple-gmzdo) uses to sort the displayed objects to orderings. Use __updateDisplayedObjects__  to apply the sort orderings.You can also set this value using the WebObjects Builder Display Group Options panel.

If the receiver's delegate responds to __displayGroup:displayArrayForObjects:__ , that method is used instead of the sort orderings to order the objects.

__See also:__
[- __displayedObjects__](#apple-geztsmry), [- __sortOrderings__](#apple-gmzdg), [- __updateDisplayedObjects__](#apple-gmzdo)

---

### setValidatesChangesImmediately:

- (void)__setValidatesChangesImmediately:__ (BOOL)_flag_

Controls the receiver's behavior on encountering a validation error. In the Web context, this method has no effect.

WODisplayGroups by default don't validate changes immediately.

__See also:__
- __saveChanges__  (in EOControl's EOEditingContext), - tryToSaveChanges (EOEditingContext
Additions), [- __validatesChangesImmediately__](#apple-gmztc)

---

### sortOrderings

- (NSArray \*)__sortOrderings__

Returns an array of EOSortOrdering objects (defined in the EOControl framework) that [__updateDisplayedObjects__](#apple-gmzdo) uses to sort the displayed objects, as returned by the [__displayedObjects__](#apple-geztsmry) method.

__See also:__
[- __setSortOrderings:__](#apple-gmytk)

---

### updateDisplayedObjects

- (void)__updateDisplayedObjects__

Recalculates the receiver's displayed objects arrays and redisplays. If the delegate responds to [__displayGroup:displayArrayForObjects:__](WODisplayGroupDelegate.md#apple-geztima), it's sent this message and the returned array is set as the WODisplayGroup's displayed objects. Otherwise, the receiver applies its qualifier and sort ordering to its array of objects. In either case, any objects that were selected before remain selected in the new displayed object's array.

__See also:__
[- __redisplay__](#apple-giydo), [- __allObjects__](#apple-gqzq), [- __displayedObjects__](#apple-geztsmry), [- __qualifier__](#apple-gm3dimq), [- __selectedObjects__](#apple-gizts), [- __sortOrderings__](#apple-gmzdg)

---

### validatesChangesImmediately

- (BOOL)__validatesChangesImmediately__

Returns YES if the receiver immediately handles validation errors, or leaves them for the EOEditingContext (defined in the EOControl framework) to handle when saving changes.

By default, WODisplayGroups don't validate changes immediately.

__See also:__
[- __setValidatesChangesImmediately:__](#apple-gyzdemy)

****

---

[!](WODirectAction-2.md)
[!](WODynamicElement-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
