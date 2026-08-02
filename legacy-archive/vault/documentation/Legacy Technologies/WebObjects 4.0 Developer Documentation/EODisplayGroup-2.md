---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EODisplayGroup.html
archived_at: '2026-07-18T01:28:45.822064Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EODetailSelectionAssociation-2.md)
[!](EODisplayGroupDelegate.md)

---

# EODisplayGroup

__Inherits From:__
NSObject

__Conforms To:__
NSCoding
NSObject (NSObject)

__Declared in:__
EOInterface/EODisplayGroup.h

---

## Class At a Glance:

**---

### Purpose**

An EODisplayGroup collects an array of objects from an EODataSource, and works with a group of EOAssociation objects to display and edit the properties of those objects.

**---

### Principal Attributes**

- Array of objects supplied by an EODataSource
- EOQualifier and EOSortOrderings to filter the objects for display
- Array of selection indexes
- Delegate

  **---

  ### Creation**

  **Interface Builder

  **[- init](#apple-guydoobv) Designated initializer.****

  **---

  ### Commonly Used Methods**

  **[- allObjects](#apple-geztcny) Returns all objects in the EODisplayGroup.

  **[- displayedObjects](#apple-geztmmi) Returns the subset of all objects made available for display.

  **[- selectedObjects](#apple-ge2dgmq) Returns the selected objects.

  **[- setQualifier:](#apple-ge2taoi) Sets a filter that limits the objects displayed.

  **[- setSortOrderings:](#apple-ge2teoa) Sets the ordering used to sort the objects.

  **[- updateDisplayedObjects](#apple-ge2tkny) Filters, sorts, and redisplays the objects.

  **[- insertObjectAtIndex:](#apple-gi3tqma) Creates a new object and inserts it into the EODataSource.**************

  ---

  ## Class Description

  An EODisplayGroup is the basic user interface manager for an Enterprise Objects Framework or Java Client application. It collects objects from an EODataSource, filters and sorts them, and maintains a selection in the filtered subset. It interacts with user interface objects and other display objects through EOAssociations, which bind the values of objects to various aspects of the display objects.

  An EODisplayGroup manipulates its EODataSource by sending it `fetchObjects`, `insertObject:`, and other messages, and registers itself as an editor and message handler of the EODataSource's EOEditingContext. The EOEditingContext allows the EODisplayGroup to intercede in certain operations, as described in the EOEditors and EOMessageHandlers informal protocol specifications. EODisplayGroup implements all the methods of these informal protocols; see the descriptions for `[editingContextWillSaveChanges:](#apple-ge2tcmjw)`, `[editorHasChangesForEditingContext:](#apple-ge2tcmry)`, and `[editingContext:presentErrorMessage:](#apple-ge2tcmbv)` (`editingContextPresentException` for Java Client applications) for more information.

  Most of an EODisplayGroup's interactions are with its associations, its EODataSource, and its EOEditingContext. See the EOAssociation, EODataSource, and EOEditingContext class specifications for more information on these interactions.

  ---

  ## Creating an EODisplayGroup

  You create most EODisplayGroups in Interface Builder, by dragging an entity icon from the EOModeler application, which creates an EODisplayGroup with an EODatabaseDataSource (EODistributedDataSource, for Java Client applications), or by dragging an EODisplayGroup with no EODataSource from the EOPalette. EODisplayGroups with EODataSources operate independent of other EODisplayGroups, while those without EODataSources must be set up in a master-detail association with another EODisplayGroup.

  To create an EODisplayGroup programmatically, simply initialize it and set its EODataSource:

  > ```
  > EODataSource *myDataSource;    /* Assume this exists. */EODisplayGroup *myDisplayGroup;myDisplayGroup = [[EODisplayGroup alloc] init];[myDisplayGroup setDataSource:myDataSource];
  > ```

  After creating the EODisplayGroup, you can add associations as described in the EOAssociation class specification.

  ---

  ## Getting Objects

  Since an EODisplayGroup isn't much use without objects to manage, the first thing you do with an EODisplayGroup is send it a fetch message. You can use the basic `[fetch](#apple-ge3dqmy)` method; the `[fetch:](#apple-guydomrx)` action method, which can be invoked by a control in the EODisplayGroup's nib file; or, you can configure the EODisplayGroup in Interface Builder to fetch automatically when its nib file is loaded. These methods all ask the EODisplayGroup's EODataSource to fetch from its persistent store with a `fetchObjects` message.

  ---

  ### Filtering and Sorting

  An EODisplayGroup's fetched objects are available through its `[allObjects](#apple-geztcny)` method. These objects are treated only as candidates for display, however. The array of objects actually displayed is filtered and sorted by the EODisplayGroup's delegate, or by a qualifier and sort ordering array. You set the qualifier and sort orderings using the `[setQualifier:](#apple-ge2taoi)` and `[setSortOrderings:](#apple-ge2teoa)` methods. The `[displayedObjects](#apple-geztmmi)` method returns this filtered and sorted array; index arguments to other EODisplayGroup methods are defined in terms of this array.

  If the EODisplayGroup has a delegate that responds to `[displayGroup:displayArrayForObjects:](../Protocols/EODisplayGroupDelegate.md#apple-gm4tkma)`, it invokes this method rather than using its own qualifier and sort ordering array. The delegate is then responsible for filtering the objects and returning a sorted array. If the delegate only needs to perform one of these steps, it can get the qualifier or sort orderings from the EODisplayGroup and apply either itself using the NSArray methods `filteredArrayUsingQualifier:` and `sortedArrayUsingKeyOrderArray:`, which are added by the control layer.

  If you change the qualifier or sort ordering, or alter the delegate in a way that changes how it filters and sorts the EODisplayGroup's objects, you can send `[updateDisplayedObjects](#apple-ge2tkny)` to the EODisplayGroup to get it to refilter and resort its objects. Note that this doesn't cause the EODisplayGroup to refetch.

  ---

  ## Changing and Examining the Selection

  An EODisplayGroup keeps a selection in terms of indexes into the array of displayed objects. EOAssociations that display values for multiple objects are responsible for updating the selection in their EODisplayGroups according to user actions on their display objects. This is typically done with the `[setSelectionIndexes:](#apple-ge2tcoa)` method. Other methods available for indirect manipulation of the selection are the action methods `[selectNext](#apple-ge2dioa)` and `[selectPrevious](#apple-ge2dmoa)`, as well as `[selectObjectsIdenticalTo:](#apple-ge2dmma)` and `[selectObjectsIdenticalTo:](#apple-ge2dmma)`.

  To get the selection, you can use the `[selectionIndexes](#apple-ge2dina)` method, which returns an array of NSNumbers, or `[selectedObjects](#apple-ge2dgmq)`, which returns an array containing the selected objects themselves. Another method, `[selectedObject](#apple-ge2deoa)`, returns the first selected object if there is one.

  ---

  ## The Delegate

  EODisplayGroup offers a number of methods for its delegate to implement; if the delegate does, it invokes them as appropriate. Besides the aforementioned `[displayGroup:displayArrayForObjects:](../Protocols/EODisplayGroupDelegate.md#apple-gm4tkma)`, there are methods that inform the delegate that the EODisplayGroup has fetched, created an object (or failed to create one), inserted or deleted an object, changed the selection, or set a value for a property. There are also methods that request permission from the delegate to perform most of these same actions. The delegate can return YES to permit the action or NO to deny it. For more information, see each method's description in the [EODisplayGroupDelegate](EODisplayGroupDelegate.md) protocol specification.

  ---

  ## Methods for Use by EOAssociations

  While most of your application code interacts with objects directly, EODisplayGroup also defines methods for its associations to access properties of individual objects without having to know anything about which methods they implement. Accessing properties through the EODisplayGroup offers associations the benefit of automatic validation, as well.

  Associations access objects by index into the displayed objects array, or by object identifier. `[valueForObjectAtIndex:key:](#apple-ge2tony)` returns the value of a named property for the object at a given index, and `[setValue:forObjectAtIndex:key:](#apple-ge2tioi)` sets it. Similarly, `[valueForObject:key:](#apple-ge2tomy)` and `[setValue:forObject:key:](#apple-ge2timy)`access the objects by object identifer. EOAssociations can also get and set values for the first object in the selection using `[selectedObjectValueForKey:](#apple-ge2dgnq)` and `[setSelectedObjectValue:forKey:](#apple-geytqmzq)`.

  ---

  ## Adopted Protocols

  **NSCoding**

  **- encodeWithCoder:

  **- initWithCoder:****

  ---

  ## Method Types

  **Creating instances**

  **[- init](#apple-guydoobv)**

  **Configuring behavior**

  **[- defaultStringMatchFormat](#apple-gmytmna)

  **[- defaultStringMatchOperator](#apple-gmytmoa)

  **[- fetchesOnLoad](#apple-geztsmi)

  **[- queryBindingValues](#apple-gmytqmq)

  **[- queryOperatorValues](#apple-gmytqnq)

  **[- selectsFirstObjectAfterFetch](#apple-ge2dqma)

  **[- setDefaultStringMatchFormat:](#apple-gmytsny)

  **[- setDefaultStringMatchOperator:](#apple-gmzdami)

  **[- setFetchesOnLoad:](#apple-ge2dsny)

  **[- setQueryBindingValues:](#apple-ge4tsnjv)

  **[- setQueryOperatorValues:](#apple-gmzdeny)

  **[- setSelectsFirstObjectAfterFetch:](#apple-ge2temy)

  **[- setUsesOptimisticRefresh:](#apple-ge2tgmy)

  **[- setValidatesChangesImmediately:](#apple-ge2tgoa)

  **[- usesOptimisticRefresh](#apple-ge2tmna)

  **[- validatesChangesImmediately](#apple-ge2tmoi)********************************

  **Setting the data source**

  **[- setDataSource:](#apple-ge2dqni)

  **[- dataSource](#apple-geztima)****

  **Setting the qualifier and sort ordering**

  **[- setQualifier:](#apple-ge2taoi)

  **[- qualifier](#apple-ge2dema)

  **[- setSortOrderings:](#apple-ge2teoa)

  **[- sortOrderings](#apple-ge2tkmy)********

  **Managing queries**

  **[- qualifierFromQueryValues](#apple-geytsny)

  **[- setEqualToQueryValues:](#apple-ge3dsmy)

  **[- equalToQueryValues](#apple-ge3dqoa)

  **[- setGreaterThanQueryValues:](#apple-ge3dsnq)

  **[- greaterThanQueryValues](#apple-ge3dona)

  **[- setLessThanQueryValues:](#apple-ge3tama)

  **[- lessThanQueryValues](#apple-ge3dqni)

  **[- qualifyDisplayGroup](#apple-gqytgnq)

  **[- qualifyDisplayGroup:](#apple-guytamzv)

  **[- qualifyDataSource](#apple-geytsni)

  **[- qualifyDataSource:](#apple-guytamrs)

  **[- enterQueryMode:](#apple-ge3dkny)

  **[- inQueryMode](#apple-ge3dkmy)

  **[- setInQueryMode:](#apple-ge3dkmi)

  **[- enabledToSetSelectedObjectValueForKey:](#apple-ge3dkoi)******************************

  **Fetching objects from the data source**

  **[- fetch](#apple-ge3dqmy)

  **[- fetch:](#apple-guydomrx)****

  **Getting the objects [- allObjects](#apple-geztcny)**

  **[- displayedObjects](#apple-geztmmi)**

  **Updating display of values**

  **[- redisplay](#apple-ge2dena)

  **[- updateDisplayedObjects](#apple-ge2tkny)****

  **Setting the objects**

  **[- setObjectArray:](#apple-ge2tana)**

  **Changing the selection**

  **[- setSelectionIndexes:](#apple-ge2tcoa)

  **[- selectObjectsIdenticalTo:](#apple-ge2dmma)

  **[- selectObjectsIdenticalTo:selectFirstOnNoMatch:](#apple-guytenbv)

  **[- selectObject:](#apple-ge3donq)

  **[- clearSelection](#apple-geztgmy)

  **[- selectNext](#apple-ge2dioa)

  **[- selectNext:](#apple-guytcobq)

  **[- selectPrevious](#apple-ge2dmoa)

  **[- selectPrevious:](#apple-guyteobz)******************

  **Examining the selection**

  **[- selectionIndexes](#apple-ge2dina)

  **[- selectedObject](#apple-ge2deoa)

  **[- selectedObjects](#apple-ge2dgmq)******

  **Inserting and deleting objects**

  **[- delete:](#apple-guydimrz)

  **[- deleteObjectAtIndex:](#apple-gqztcni)

  **[- deleteSelection](#apple-geztkny)

  **[- insert:](#apple-ge4dkobt)

  **[- insertedObjectDefaultValues](#apple-giydcnbu)

  **[- insertObjectAtIndex:](#apple-gi3tqma)

  **[- insertObject:atIndex:](#apple-ge2damy)

  **[- setInsertedObjectDefaultValues:](#apple-he4dkny)****************

  **Adding keys**

  **[- setLocalKeys:](#apple-gezdama)

  **[- localKeys](#apple-ge2dcmq)****

  **Getting the associations**

  **[- observingAssociations](#apple-ge2dcnq)**

  **Setting the delegate**

  **[- setDelegate:](#apple-ge2dsmy)

  **[- delegate](#apple-ge4tonry)****

  **Changing values from associations**

  **[- setSelectedObjectValue:forKey:](#apple-geytqmzq)

  **[- selectedObjectValueForKey:](#apple-ge2dgnq)

  **[- setValue:forObject:key:](#apple-ge2timy)

  **[- valueForObject:key:](#apple-ge2tomy)

  **[- setValue:forObjectAtIndex:key:](#apple-ge2tioi)

  **[- valueForObjectAtIndex:key:](#apple-ge2tony)************

  **Editing by associations**

  **[- associationDidBeginEditing:](#apple-gezteni)

  **[- association:failedToValidateValue:forKey:object:errorDescription:](#apple-gi3dcoa)

  **[- associationDidEndEditing:](#apple-gezteoi)

  **[- editingAssociation](#apple-geztmni)

  **[- endEditing](#apple-ge2tami)**********

  **Querying changes for associations**

  **[- contentsChanged](#apple-geztgnq)

  **[- selectionChanged](#apple-ge2dima)

  **[- updatedObjectIndex](#apple-ge2tmmi)******

  **Interacting with the EOEditingContext**

  **[- editorHasChangesForEditingContext:](#apple-ge2tcmry)

  **[- editingContextWillSaveChanges:](#apple-ge2tcmjw)

  **[- editingContext:presentErrorMessage:](#apple-ge2tcmbv)******

  ---

  ## Instance Methods

  ---

  ### allObjects

  - (NSArray \*)`allObjects`

  Returns all of the objects collected by the receiver.

  __See also:__
  [- `displayedObjects`](#apple-geztmmi), [- `fetch`](#apple-ge3dqmy)

  ---

  ### associationDidBeginEditing:

  - (void)`associationDidBeginEditing:`(EOAssociation \*)_anAssociation_

  Invoked by _anAssociation_ when its display object begins editing to record that EOAssociation as the editing association.

  __See also:__
  [- `editingAssociation`](#apple-geztmni), [- `endEditing`](#apple-ge2tami), [- `association:failedToValidateValue:forKey:object:
  errorDescription:`](#apple-gi3dcoa)

  ---

  ### associationDidEndEditing:

  - (void)`associationDidEndEditing:`(EOAssociation \*)_anAssociation_

  Invoked by _anAssociation_ to clear the editing association. If _anAssociation_ is the receiver's editing association, clears the editing association. Otherwise does nothing.

  __See also:__
  [- `editingAssociation`](#apple-geztmni), [- `endEditing`](#apple-ge2tami), [- `association:failedToValidateValue:forKey:object:
  errorDescription:`](#apple-gi3dcoa)

  ---

  ### association:failedToValidateValue:forKey:object:errorDescription:

  - (BOOL)`association:`(EOAssociation \*)_anAssociation_`failedToValidateValue:`(NSString \*)_value_`forKey:`(NSString \*)_key_`object:`(id)_anObject_`errorDescription:`(NSString \*)_errorDescription_

  Invoked by _anAssociation_ from its `[shouldEndEditingForAspect:invalidInput:errorDescription:index:](EOAssociation.md#apple-gyytk)` method to let the receiver handle a validation error. This method opens an attention panel with _errorDescription_ as the message and returns NO.

  __See also:__
  [- `displayGroup:shouldDisplayAlertWithTitle:message:`](../Protocols/EODisplayGroupDelegate.md#apple-gqytsni) ([EODisplayGroupDelegate](EODisplayGroupDelegate.md))

  ---

  ### clearSelection

  - (BOOL)`clearSelection`

  Invokes [`setSelectionIndexes:`](#apple-ge2tcoa) to clear the selection, returning YES on success and NO on failure.

  ---

  ### contentsChanged

  - (BOOL)`contentsChanged`

  Returns YES if the receiver's array of objects has changed and not all observers have been notified, NO otherwise. EOAssociations use this in their [`subjectChanged`](EOAssociation.md#apple-gyytq) methods to determine what they need to update.

  __See also:__
  [- `selectionChanged`](#apple-ge2dima), [- `updatedObjectIndex`](#apple-ge2tmmi)

  ---

  ### dataSource

  - (EODataSource \*)`dataSource`

  Returns the receiver's EODataSource.

  __See also:__
  [- `setDataSource:`](#apple-ge2dqni)

  ---

  ### defaultStringMatchFormat

  - (NSString \*)`defaultStringMatchFormat`

  Returns the format string that specifies how pattern matching will be performed on string values in the `queryMatch` dictionary. If a key in the `queryMatch` dictionary does not have an associated operator in the [`queryOperatorValues`](#apple-gmytqnq) dictionary, then its value is matched using pattern matching, and the format string returned by this method specifies how it will be matched.

  __See also:__
  [- `defaultStringMatchOperator`](#apple-gmytmoa), [- `setDefaultStringMatchFormat:`](#apple-gmytsny)

  ---

  ### defaultStringMatchOperator

  - (NSString \*)`defaultStringMatchOperator`

  Returns the operator used to perform pattern matching for string values in the `queryMatch` dictionary. If a key in the `queryMatch` dictionary does not have an associated operator in the [`queryOperatorValues`](#apple-gmytqnq) dictionary, then the operator returned by this method is used to perform pattern matching.

  __See also:__
  [- `defaultStringMatchFormat`](#apple-gmytmna), [- `setDefaultStringMatchOperator:`](#apple-gmzdami)

  ---

  ### delegate

  - (id)`delegate`

  Returns the receiver's delegate.

  __See also:__
  [- `setDelegate:`](#apple-ge2dsmy)

  ---

  ### delete:

  - (void)`delete:`(id)_sender_

  This action method invokes [`deleteSelection`](#apple-geztkny).

  ---

  ### deleteObjectAtIndex:

  - (BOOL)`deleteObjectAtIndex:`(unsigned int)_index_

  Attempts to delete the object at _index_, returning YES if successful and NO if not. Checks with the delegate using `[displayGroup:shouldDeleteObject:](../Protocols/EODisplayGroupDelegate.md#apple-gqytmmq)`. If the delegate returns NO, this method fails and returns NO. If successful, sends the delegate a `[displayGroup:didDeleteObject:](../Protocols/EODisplayGroupDelegate.md#apple-gqydcnq)` message.

  This method performs the delete by sending `deleteObject:` to the EODataSource. If that message raises an exception, this method fails and returns NO.

  ---

  ### deleteSelection

  - (BOOL)`deleteSelection`

  Attempts to delete the selected objects, returning YES if successful and NO if not.

  ---

  ### displayedObjects

  - (NSArray \*)`displayedObjects`

  Returns the objects that should be displayed or otherwise made available to the user, as filtered by the receiver's delegate or by its qualifier and sort ordering.

  __See also:__
  [- `allObjects`](#apple-geztcny), [- `updateDisplayedObjects`](#apple-ge2tkny), [- `displayGroup:displayArrayForObjects:`](../Protocols/EODisplayGroupDelegate.md#apple-gm4tkma)
  ([EODisplayGroupDelegate](EODisplayGroupDelegate.md)), [- `qualifier`](#apple-ge2dema), [- `sortOrderings`](#apple-ge2tkmy)

  ---

  ### editingAssociation

  - (EOAssociation \*)`editingAssociation`

  Returns the EOAssociation editing a value if there is one, NO if there isn't.

  __See also:__
  [- `associationDidBeginEditing:`](#apple-gezteni), [- `associationDidEndEditing:`](#apple-gezteoi)

  ---

  ### editingContext:presentErrorMessage:

  - (void)`editingContext:`(EOEditingContext \*)_anEditingContext_`presentErrorMessage:`(NSString \*)_errorMessage_

  Invoked by _anEditingContext_ as part of the EOMessageHandlers informal protocol, this method presents an attention panel with _errorMessage_ as the message to display.

  ---

  ### editingContextWillSaveChanges:

  - (void)`editingContextWillSaveChanges:`(EOEditingContext \*)_anEditingContext_

  Invoked by _anEditingContext_ in its `saveChanges` method as part of the EOEditors informal protocol, this method allows the EODisplayGroup to prohibit a save operation. EODisplayGroup's implementation of this method invokes [`endEditing`](#apple-ge2tami), and raises an NSInternalInconsistencyException if it returns NO. Thus, if there's an association that refuses to end editing, _anEditingContext_ doesn't save changes.

  ---

  ### editorHasChangesForEditingContext:

  - (BOOL)`editorHasChangesForEditingContext`__:__ (EOEditingContext \*)_anEditingContext_

  Invoked by _anEditingContext_ as part of the EOEditors informal protocol, this method returns NO if any association is editing, YESotherwise.

  ---

  ### enabledToSetSelectedObjectValueForKey:

  - (BOOL)`enabledToSetSelectedObjectValueForKey:`(NSString \*)_key_

  Returns YES to indicate that a single value association (such as an EOControlAssociation for a NSTextField) should be enabled for setting _key_, NO otherwise. Normally this is the case if the receiver has a selected object. However, if _key_ is a special query key (for example, "@query=.name"), then the control should be enabled even without a selected object.

  ---

  ### endEditing

  - (BOOL)`endEditing`

  Attempts to end any editing taking place. If there's no editing association or if the editing association responds YES to an `endEditing` message, returns YES. Otherwise returns NO.

  __See also:__
  [- `editingAssociation`](#apple-geztmni)

  ---

  ### enterQueryMode:

  - (void)`enterQueryMode:`(id)_sender_

  This action method invokes [`setInQueryMode:`](#apple-ge3dkmi) with an argument of YES.

  ---

  ### equalToQueryValues

  - (NSDictionary \*)`equalToQueryValues`

  Returns the receiver's dictionary of equalTo query values. This dictionary is typically manipulated by associations bound to keys of the form @query=._propertyName_. The [`qualifierFromQueryValues`](#apple-geytsny) method uses this dictionary along with the lessThan and greaterThan dictionaries to construct qualifiers.

  __See also:__
  [- `setEqualToQueryValues:`](#apple-ge3dsmy), [- `greaterThanQueryValues`](#apple-ge3dona), [- `lessThanQueryValues`](#apple-ge3dqni),

  ---

  ### fetch

  - (BOOL)`fetch`

  Attempts to fetch objects from the EODataSource, returning YES on success and NO on failure.

  Before fetching, invokes [`endEditing`](#apple-ge2tami) and sends `[displayGroupShouldFetch:](../Protocols/EODisplayGroupDelegate.md#apple-gqzdena)` to the delegate, returning NO if either of these methods does. If both return YES, sends a `fetchObjects` message to the receiver's EODataSource to replace the object array, and if successful sends the delegate a `[displayGroup:didFetchObjects:](../Protocols/EODisplayGroupDelegate.md#apple-gqydgoi)` message.

  ---

  ### fetch:

  - (void)`fetch:`(id)_sender_

  This action method invokes [`fetch`](#apple-ge3dqmy).

  ---

  ### fetchesOnLoad

  - (BOOL)`fetchesOnLoad`

  Returns YES if the receiver fetches automatically after being loaded from a nib file, NO if it must be told explicitly to fetch. The default is NO. You can set this behavior in Interface Builder using the Inspector panel.

  __See also:__
  [- `fetch`](#apple-ge3dqmy), [- `setFetchesOnLoad:`](#apple-ge2dsny)

  ---

  ### greaterThanQueryValues

  - (NSDictionary \*)`greaterThanQueryValues`

  Returns the receiver's dictionary of greaterThan query values. This dictionary is typically manipulated by associations bound to keys of the form @query>._propertyName_. The [`qualifierFromQueryValues`](#apple-geytsny) method uses this dictionary along with the lessThan and equalTo dictionaries to construct qualifiers.

  __See also:__
  [- `setGreaterThanQueryValues:`](#apple-ge3dsnq), [- `lessThanQueryValues`](#apple-ge3dqni), [- `equalToQueryValues`](#apple-ge3dqoa)

  ---

  ### init

  - (id)`init`

  Initializes a newly allocated EODisplayGroup. The new display group then needs to have an EODataSource set with [`setDataSource:`](#apple-ge2dqni). This is the designated initializer for the EODisplayGroup class. Returns `self`.

  __See also:__
  [- `bindAspect:displayGroup:key:`](EOAssociation.md#apple-gu2tq) (EOAssociation)

  ---

  ### inQueryMode

  - (BOOL)`inQueryMode`

  Returns YES to indicate that the receiver is in query mode, NO otherwise. In query mode, user interface controls that normally display values become empty, allowing users to type queries directly into them (this is also known as a "Query By Example" interface). In effect, the receiver's "displayedObjects" are replaced with an empty equalTo query values dictionary. When [`qualifyDisplayGroup`](#apple-gqytgnq) or [`qualifyDataSource`](#apple-geytsni) is subsequently invoked, the query is performed and the display reverts to displaying values-this time, the objects returned by the query.

  __See also:__
  [- `setInQueryMode:`](#apple-ge3dkmi), [- `enterQueryMode:`](#apple-ge3dkny)

  ---

  ### insert:

  - (void)`insert:`(id)_sender_

  This action method invokes [`insertObjectAtIndex:`](#apple-gi3tqma) with an index just past the first index in the selection, or 0 if there's no selection.

  ---

  ### insertedObjectDefaultValues

  - (NSDictionary \*)`insertedObjectDefaultValues`

  Returns the default values to be used for newly inserted objects. The keys into the dictionary are the properties of the entity that the display group manages. If the dictionary returned by this method is empty, the `insert...` method adds an object that is initially empty. Because the object is empty, the display group has no value to display on the HTML page for that object, meaning that there is nothing for the user to select and modify. Use the [`setInsertedObjectDefaultValues:`](#apple-he4dkny) method to set up a default value so that there is something to display on the page.

  ---

  ### insertObjectAtIndex:

  - (id)`insertObjectAtIndex:`(unsigned int)_anIndex_

  Asks the receiver's EODataSource to create a new object by sending it a `createObject` message, then inserts the new object using [`insertObject:atIndex:`](#apple-ge2damy). The EODataSource __createObject__  method has the effect of inserting the object into the EOEditingContext.

  If a new object can't be created, this method sends the delegate a [`displayGroup:createObjectFailedForDataSource:`](../Protocols/EODisplayGroupDelegate.md#apple-gm4tema) message or, if the delegate doesn't respond, opens an attention panel to inform the user of the error.

  __See also:__
  [- `insert:`](#apple-ge4dkobt)

  ---

  ### insertObject:atIndex:

  - (void)`insertObject:`(id)_anObject_`atIndex:`(unsigned int)_index_

  Inserts _anObject_ into the receiver's EODataSource and [`displayedObjects`](#apple-geztmmi) array at _index_, if possible. This method checks with the delegate before actually inserting, using `[displayGroup:shouldInsertObject:atIndex:](../Protocols/EODisplayGroupDelegate.md#apple-gqzdkmy)`. If the delegate refuses, _anObject_ isn't inserted. After successfully inserting the object, this method informs the delegate with a `[displayGroup:didInsertObject:](../Protocols/EODisplayGroupDelegate.md#apple-gqydmoa)` message, and selects the newly inserted object. Raises an NSRangeException if _index_ is out of bounds.

  Unlike the [`insertObjectAtIndex:`](#apple-gi3tqma) method, this method does not insert the object into the EOEditingContext. If you use this method, you're responsible for inserting the object into the EOEditingContext yourself.

  __See also:__
  [- `insert:`](#apple-ge4dkobt)

  ---

  ### lessThanQueryValues

  - (NSDictionary \*)`lessThanQueryValues`

  Returns the receiver's dictionary of lessThan query values. This dictionary is typically manipulated by associations bound to keys of the form @query<._propertyName_. The [`qualifierFromQueryValues`](#apple-geytsny) method uses this dictionary along with the greaterThan and equalTo dictionaries to construct qualifiers.

  __See also:__
  [- `setLessThanQueryValues:`](#apple-ge3tama), [- `greaterThanQueryValues`](#apple-ge3dona), [- `equalToQueryValues`](#apple-ge3dqoa)

  ---

  ### localKeys

  - (NSArray \*)`localKeys`

  Returns the additional keys that EOAssociations can be bound to. An EODisplayGroup's basic keys are typically those of the attributes and relationships of its objects, as defined by their EOClassDescription through an EOEntity in the model. Local keys are typically used to form associations with key paths, with arbitrary methods of objects, or with properties of objects not associated with an EOEntity. Interface Builder allows the user to add and remove local keys in the EODisplayGroup Attributes Inspector panel.

  __See also:__
  [- `setLocalKeys:`](#apple-gezdama)

  ---

  ### observingAssociations

  - (NSArray \*)`observingAssociations`

  Returns all EOAssociations that observe the receiver's objects.

  ---

  ### qualifier

  - (EOQualifier \*)`qualifier`

  Returns the receiver's qualifier, which it uses to filter its array of objects for display when the delegate doesn't do so itself.

  __See also:__
  [- `updateDisplayedObjects`](#apple-ge2tkny), [- `displayedObjects`](#apple-geztmmi), [- `setQualifier:`](#apple-ge2taoi)

  ---

  ### qualifierFromQueryValues

  - (EOQualifier \*)`qualifierFromQueryValues`

  Builds a qualifier constructed from entries in the three query dictionaries: equalTo, greaterThan, and lessThan. These, in turn, are typically manipulated by associations bound to keys of the form @query=.firstName, @query>.budget, @query<.budget.

  __See also:__
  [- `qualifyDisplayGroup`](#apple-gqytgnq), [- `qualifyDataSource`](#apple-geytsni)

  ---

  ### qualifyDataSource

  - (void)`qualifyDataSource`

  Takes the result of [`qualifierFromQueryValues`](#apple-geytsny) and applies to the receiver's data source. The receiver then sends itself a [`fetch`](#apple-ge3dqmy) message. If the receiver is in query mode, query mode is exited. This method differs from [`qualifyDisplayGroup`](#apple-gqytgnq) as follows: whereas `qualifyDisplayGroup` performs in-memory filtering of already fetched objects, `qualifyDataSource` triggers a new qualified fetch against the database.

  ---

  ### qualifyDataSource:

  - (void)`qualifyDataSource:`(id)_sender_

  This action method invokes __qualifyDataSource__ .

  ---

  ### qualifyDisplayGroup

  - (void)`qualifyDisplayGroup`

  Takes the result of [`qualifierFromQueryValues`](#apple-geytsny) and applies to the receiver using [`setQualifier:`](#apple-ge2taoi). The method [`updateDisplayedObjects`](#apple-ge2tkny) is invoked to refresh the display. If the receiver is in query mode, query mode is exited.

  __See also:__
  [- `qualifyDataSource`](#apple-geytsni)

  ---

  ### qualifyDisplayGroup:

  - (void)`qualifyDisplayGroup:`(id)_sender_

  This action method invokes __qualifyDisplayGroup:__ .

  ---

  ### queryBindingValues

  - (NSDictionary \*)`queryBindingValues`

  Returns a dictionary containing the actual values that the user wants to query upon. You use this method to perform a query stored in the model file. Bind keys in this dictionary to elements on your component that specify query values, then pass this dictionary to the fetch specification that performs the fetch.

  ---

  ### queryOperatorValues

  - (NSDictionary \*)`queryOperatorValues`

  Returns a dictionary of operators to use on items in the `queryMatch` dictionary. If a key in the `queryMatch` dictionary also exists in `queryOperatorValues`, that operator for that key is used.

  __See also:__
  [- `qualifierFromQueryValues`](#apple-geytsny)

  ---

  ### redisplay

  - (void)`redisplay`

  Notifies all observing associations to redisplay their values.

  __See also:__
  [- `observingAssociations`](#apple-ge2dcnq)

  ---

  ### selectedObject

  - (id)`selectedObject`

  Returns the first selected object in the displayed objects array, or `nil` if there's no such object.

  __See also:__
  [- `displayedObjects`](#apple-geztmmi), [- `selectionIndexes`](#apple-ge2dina)

  ---

  ### selectedObjects

  - (NSArray \*)`selectedObjects`

  Returns the objects selected in the receiver's displayed objects array.

  __See also:__
  [- `displayedObjects`](#apple-geztmmi), [- `selectionIndexes`](#apple-ge2dina)

  ---

  ### selectedObjectValueForKey:

  - (id)`selectedObjectValueForKey:`(NSString \*)_key_

  Returns the value corresponding to _key_ for the first selected object in the receiver's displayed objects array, or `nil` if exactly one object isn't selected.

  __See also:__
  [- `valueForObject:key:`](#apple-ge2tomy)

  ---

  ### selectionChanged

  - (BOOL)`selectionChanged`

  Returns YES if the selection has changed and not all observers have been notified, NO otherwise. EOAssociations use this in their [`subjectChanged`](EOAssociation.md#apple-gyytq) methods to determine what they need to update.

  __See also:__
  [- `contentsChanged`](#apple-geztgnq)

  ---

  ### selectionIndexes

  - (NSArray \*)`selectionIndexes`

  Returns the indexes of the receiver's selected objects as NSNumbers , in terms of its displayed objects array.

  __See also:__
  [- `displayedObjects`](#apple-geztmmi), [- `selectedObjects`](#apple-ge2dgmq), [- `selectedObject`](#apple-ge2deoa), [- `setSelectionIndexes:`](#apple-ge2tcoa)

  ---

  ### selectNext

  - (BOOL)`selectNext`

  Attempts to select the object just after the currently selected one, returning YES if successful and NO if not. The selection is altered in this way:

  - If there are no objects, does nothing and returns NO.
  - If there's no selection, selects the object at index zero and returns YES.
  - If the first selected object is the last object in the displayed objects array, selects the first object and returns YES.
  - Otherwise selects the object after the first selected object.__See also:__
  [- `selectPrevious`](#apple-ge2dmoa), [- `setSelectionIndexes:`](#apple-ge2tcoa)

  ---

  ### selectNext:

  - (void)`selectNext:`(id)_sender_

  This action method invokes `[selectNext](#apple-ge2dioa)`.

  __See also:__
  [- `selectPrevious:`](#apple-guyteobz), [- `setSelectionIndexes:`](#apple-ge2tcoa)

  ---

  ### selectObject:

  - (BOOL)`selectObject:`(id)_anObject_

  Returns YES to indicate that the receiver has found and selected _anObject_, NO if it can't find a match for _anObject_ (in which case it clears the selection). The selection is performed on the receiver's [`displayedObjects`](#apple-geztmmi), not on [`allObjects`](#apple-geztcny).

  ---

  ### selectObjectsIdenticalTo:

  - (BOOL)`selectObjectsIdenticalTo:`(NSArray \*)_objects_

  Attempts to select the objects in the receiver's displayed objects array whose `id`s are equal to those of _objects_, returning YES if successful and NO otherwise.

  __See also:__
  [- `setSelectionIndexes:`](#apple-ge2tcoa)

  ---

  ### selectObjectsIdenticalTo:selectFirstOnNoMatch:

  - (BOOL)`selectObjectsIdenticalTo:`(NSArray \*)_objects_`selectFirstOnNoMatch:`(BOOL)_flag_

  Selects the objects in the receiver's displayed objects array whose `id`s are equal to those of _objects_, returning YES if successful and NO otherwise. If no objects in the displayed objects array match _objects_ and _flag_ is YES, attempts to select the first object in the displayed objects array.

  __See also:__
  [- `setSelectionIndexes:`](#apple-ge2tcoa)

  ---

  ### selectPrevious

  - (BOOL)`selectPrevious`

  Attempts to select the object just before the presently selected one, returning YES if successful and NO if not. The selection is altered in this way:

  - If there are no objects, does nothing and returns NO.
  - If there's no selection, selects the object at index zero and returns YES.
  - If the first selected object is at index zero, selects the last object and returns YES.
  - Otherwise selects the object before the first selected object.__See also:__
  [- `selectNext`](#apple-ge2dioa), [- `redisplay`](#apple-ge2dena)

  ---

  ### selectPrevious:

  - (void)`selectPrevious:`(id)_sender_

  This action method invokes [`selectPrevious`](#apple-ge2dmoa).

  __See also:__
  [- `selectNext:`](#apple-guytcobq), [- `redisplay`](#apple-ge2dena)

  ---

  ### selectsFirstObjectAfterFetch

  - (BOOL)`selectsFirstObjectAfterFetch`

  Returns YES if the receiver automatically selects its first displayed object after a fetch if there was no selection, NO if it leaves an empty selection as-is.

  __See also:__
  [- `displayedObjects`](#apple-geztmmi), [- `fetch`](#apple-ge3dqmy), [- `setSelectsFirstObjectAfterFetch:`](#apple-ge2temy)

  ---

  ### setDataSource:

  - (void)`setDataSource:`(EODataSource \*)_aDataSource_

  Sets the receiver's EODataSource to _aDataSource_. In the process, it performs these actions:

  - Unregisters `self` as an editor and message handler for the previous EODataSource's EOEditingContext, if necessary, and registers `self` with _aDataSource's_ editing context. If the new editing context already has a message handler, however, the receiver doesn't assume that role.
  - Registers `self` for EOObjectsChangedInEditingContextNotification and EOInvalidatedAllObjectsInStoreNotification from the new editing context.
  - Clears the receiver's array of objects.
  - Sends [`displayGroupDidChangeDataSource:`](../Protocols/EODisplayGroupDelegate.md#apple-gm4dkoa) to the delegate if there is one.__See also:__
  [- `dataSource`](#apple-geztima)

  ---

  ### setDefaultStringMatchFormat:

  - (void)`setDefaultStringMatchFormat:`(NSString \*)_format_

  Sets how pattern matching will be performed on NSString values in the `queryMatch` dictionary. This format is used for properties listed in the `queryMatch` dictionary that have NSString values and that do not have an associated entry in the [`queryOperatorValues`](#apple-gmytqnq) dictionary. In these cases, the value is matched using pattern matching and _format_ specifies how it will be matched.

  The default format string for pattern matching is "`%@*`" which means that the string value in the `queryMatch` dictionary is used as a prefix. For example, if the `queryMatch` dictionary contains a value "Jo" for the key "Name", the query returns all records whose name values begin with "Jo".

  __See also:__
  [- `defaultStringMatchFormat`](#apple-gmytmna), [- `setDefaultStringMatchOperator:`](#apple-gmzdami)

  ---

  ### setDefaultStringMatchOperator:

  - (void)`setDefaultStringMatchOperator:`(NSString \*)_operator_

  Sets the operator used to perform pattern matching for NSString values in the `queryMatch` dictionary. This operator is used for properties listed in the `queryMatch` dictionary that have NSString values and that do not have an associated entry in the [`queryOperatorValues`](#apple-gmytqnq) dictionary. In these cases, the operator _operator_ is used to perform pattern matching.

  The default value for the query match operator is `caseInsensitiveLike`, which means that the query does not consider case when matching letters. The other possible value for this operator is `like`, which matches the case of the letters exactly.

  __See also:__
  [- `defaultStringMatchOperator`](#apple-gmytmoa), [- `setDefaultStringMatchFormat:`](#apple-gmytsny)

  ---

  ### setDelegate:

  - (void)`setDelegate:`(id)_anObject_

  Sets the receiver's delegate to _anObject_, without retaining it.

  __See also:__
  [- `delegate`](#apple-ge4tonry)

  ---

  ### setEqualToQueryValues:

  - (void)`setEqualToQueryValues:`(NSDictionary \*)_values_

  Sets to _values_ the receiver's dictionary of equalTo query values. The [`qualifierFromQueryValues`](#apple-geytsny) method uses this dictionary along with the lessThan and greaterThan dictionaries to construct qualifiers.

  __See also:__
  [- `equalToQueryValues`](#apple-ge3dqoa), [- `setLessThanQueryValues:`](#apple-ge3tama), [- `setGreaterThanQueryValues:`](#apple-ge3dsnq)

  ---

  ### setFetchesOnLoad:

  - (void)`setFetchesOnLoad:`(BOOL)_flag_

  Controls whether the receiver automatically fetches its objects after being loaded from a nib file. If _flag_ is YES it does; if _flag_ is NO the receiver must be told explicitly to fetch. The default is NO. You can also set this behavior in Interface Builder using the Inspector panel.

  __See also:__
  [- `fetch`](#apple-ge3dqmy), [- `fetchesOnLoad`](#apple-geztsmi)

  ---

  ### setGreaterThanQueryValues:

  - (void)`setGreaterThanQueryValues:`(NSDictionary \*)_values_

  Sets to _values_ the receiver's dictionary of greaterThan query values. The [`qualifierFromQueryValues`](#apple-geytsny) method uses this dictionary along with the lessThan and equalTo dictionaries to construct qualifiers.

  __See also:__
  [- `greaterThanQueryValues`](#apple-ge3dona), [- `setLessThanQueryValues:`](#apple-ge3tama), [- `setEqualToQueryValues:`](#apple-ge3dsmy)

  ---

  ### setInQueryMode:

  - (void)`setInQueryMode:`(BOOL)_flag_

  Sets according to _flag_ whether the receiver is in query mode.

  __See also:__
  [- `inQueryMode`](#apple-ge3dkmy), [- `enterQueryMode:`](#apple-ge3dkny)

  ---

  ### setInsertedObjectDefaultValues:

  - (void)`setInsertedObjectDefaultValues:`(NSDictionary \*)_defaultValues_

  Sets default values to be used for newly inserted objects. When you use the `insert...` method to add an object, that object is initially empty. Because the object is empty, there is no value to be displayed on the HTML page, meaning there is nothing for the user to select and modify. You use this method to provide at least one field that can be displayed for the newly inserted object. The possible keys into the dictionary are the properties of the entity managed by this display group. For example, a component that displays a list of movie titles and allows the user to insert new movie titles might contain these statements to ensure that all new objects have something to display as a movie title:

  > ```
  > [defaultValues setObject:@"New title" forKey:@"title"];
  > ```

  > ```
  > [movies setInsertedObjectDefaultValues:defaultValues];
  > ```

  __See also:__
  [- `insertedObjectDefaultValues`](#apple-giydcnbu)

  ---

  ### setLessThanQueryValues:

  - (void)`setLessThanQueryValues:`(NSDictionary \*)_values_

  Sets to _values_ the receiver's dictionary of lessThan query values. The [`qualifierFromQueryValues`](#apple-geytsny) method uses this dictionary along with the greaterThan and equalTo dictionaries to construct qualifiers.

  __See also:__
  [- `lessThanQueryValues`](#apple-ge3dqni), [- `setGreaterThanQueryValues:`](#apple-ge3dsnq), [- `setEqualToQueryValues:`](#apple-ge3dsmy)

  ---

  ### setLocalKeys:

  - (void)`setLocalKeys:`(NSArray \*)_keys_

  Sets the additional keys to which EOAssociations can be bound to the strings in _keys_. Instead of invoking this method programmatically, you can use Interface Builder to add and remove local keys in the EODisplayGroup Attributes Inspector panel.

  __See also:__
  `[- localKeys](#apple-ge2dcmq)`

  ---

  ### setObjectArray:

  - (void)`setObjectArray:`(NSArray \*)_objects_

  Sets the receiver's objects to _objects_, regardless of what its EODataSource provides. This method doesn't affect the EODataSource's objects at all; specifically, it results in neither inserts or deletes of objects in the EODataSource. _objects_ should contain objects with the same property names or methods as those accessed by the receiver. This method is used by `[fetch](#apple-ge3dqmy)` to set the array of fetched objects; you should rarely need to invoke it directly.

  After setting the object array, this method restores as much of the original selection as possible by invoking `[selectObjectsIdenticalTo:](#apple-ge2dmma)`. If there's no match and the receiver selects after fetching, then the first object is selected.

  __See also:__
  [- `allObjects`](#apple-geztcny), [- `displayedObjects`](#apple-geztmmi), [- `selectsFirstObjectAfterFetch`](#apple-ge2dqma)

  ---

  ### setQualifier:

  - (void)`setQualifier:`(EOQualifier \*)_aQualifier_

  Sets the receiver's qualifier to _aQualifier_. This qualifier is used to filter the receiver's array of objects for display when the delegate doesn't do so itself. Use [`updateDisplayedObjects`](#apple-ge2tkny) to apply the qualifier.

  If the receiver's delegate responds to `[displayGroup:displayArrayForObjects:](../Protocols/EODisplayGroupDelegate.md#apple-gm4tkma)`, that method is used instead of the qualifier to filter the objects.

  __See also:__
  [- `displayedObjects`](#apple-geztmmi), [- `qualifier`](#apple-ge2dema), [- `qualifierFromQueryValues`](#apple-geytsny)

  ---

  ### setQueryBindingValues:

  - (void)`setQueryBindingValues:`(NSDictionary \*)_values_

  ---

  ### setQueryOperatorValues:

  - (void)`setQueryOperatorValues:`(NSDictionary \*)_values_

  ---

  ### setSelectedObjectValue:forKey:

  - (BOOL)`setSelectedObjectValue:`(id)_value_`forKey:`(NSString \*)_key_

  Invokes `[setValue:forObject:key:](#apple-ge2timy)` with the first selected object, returning YES if successful and NO otherwise. This method should be invoked only by EOAssociation objects to propagate changes from display objects.

  __See also:__
  [- `setValue:forObjectAtIndex:key:`](#apple-ge2tioi), [- `valueForObject:key:`](#apple-ge2tomy)

  ---

  ### setSelectionIndexes:

  - (BOOL)`setSelectionIndexes:`(NSArray \*)_indexes_

  Selects the objects at _indexes_ in the receiver's array if possible, returning YES if successful and NO if not (in which case the selection remains unaltered). _indexes_ is an array of NSNumbers . This method is the primitive method for altering the selection; all other such methods invoke this one to make the change.

  This method invokes [`endEditing`](#apple-ge2tami) to wrap up any changes being made by the user. If `endEditing` returns NO, this method fails and returns NO. This method then checks the delegate with a `[displayGroup:shouldChangeSelectionToIndexes:](../Protocols/EODisplayGroupDelegate.md#apple-gqytemq)` message. If the delegate returns NO, this method also fails and returns NO. If the receiver successfully changes the selection, its observers (typically EOAssociations) each receive a [`subjectChanged`](EOAssociation.md#apple-gyytq) message.

  ---

  ### setSelectsFirstObjectAfterFetch:

  - (void)`setSelectsFirstObjectAfterFetch:`(BOOL)_flag_

  Controls whether the receiver automatically selects its first displayed object after a fetch when there were no selected objects before the fetch. If _flag_ is YES it does; if _flag_ is NO then no objects are selected. By default, display groups select the first object after a fetch when there was no previous selection.

  __See also:__
  [- `displayedObjects`](#apple-geztmmi), [- `fetch`](#apple-ge3dqmy), [- `selectsFirstObjectAfterFetch`](#apple-ge2dqma)

  ---

  ### setSortOrderings:

  - (void)`setSortOrderings:`(NSArray \*)_orderings_

  Sets the EOSortOrdering objects that [`updateDisplayedObjects`](#apple-ge2tkny) uses to sort the displayed objects to _orderings_. Use [`updateDisplayedObjects`](#apple-ge2tkny) to apply the sort orderings.

  If the receiver's delegate responds to `[displayGroup:displayArrayForObjects:](../Protocols/EODisplayGroupDelegate.md#apple-gm4tkma)`, that method is used instead of the sort orderings to order the objects.

  __See also:__
  [- `displayedObjects`](#apple-geztmmi), [- `sortOrderings`](#apple-ge2tkmy)

  ---

  ### setUsesOptimisticRefresh:

  - (void)`setUsesOptimisticRefresh:`(BOOL)_flag_

  Controls how the receiver redisplays on changes to objects. If _flag_ is YES it redisplays only when elements of its displayed objects array change; if _flag_ is NO it redisplays on any change in its EOEditingContext. Because changes to other objects can affect the displayed objects (through flattened attributes or custom methods, for example), EODisplayGroups by default use the more pessimistic refresh technique of redisplaying on any change in the EOEditingContext. If you know that none of the EOAssociations for a particular EODisplayGroup display derived values, you can turn on optimistic refresh to reduce redisplay time.

  The default is NO. You can also change this setting in Interface Builder's Inspector panel using the Refresh All check box.

  __See also:__
  [- `usesOptimisticRefresh`](#apple-ge2tmna)

  ---

  ### setValidatesChangesImmediately:

  - (void)`setValidatesChangesImmediately:`(BOOL)_flag_

  Controls the receiver's behavior on encountering a validation error. Whenever an EODisplayGroup sets a value in an object, it sends the object a `validateValue:forKey:` message, allowing the object to coerce the value's type to a more appropriate one or to return an exception indicating that the value isn't valid. If this method is invoked with a _flag_ of YES, the receiver immediately presents an attention panel indicating the validation error. If this method is invoked with a _flag_ of NO, the receiver leaves validation errors to be handled when changes are saved. By default, display groups don't validate changes immediately.

  __See also:__
  - `saveChanges` (EOEditingContext), [- `validatesChangesImmediately`](#apple-ge2tmoi)

  ---

  ### setValue:forObject:key:

  - (BOOL)`setValue:`(id)_value_`forObject:`(id)_anObject_`key:`(NSString \*)_key_

  Sets a property of _anObject_, identified by _key_, to _value_. Returns YES if successful and NO otherwise. If a new value is set, sends the delegate a `[displayGroup:didSetValue:forObject:key:](../Protocols/EODisplayGroupDelegate.md#apple-gqydsni)` message.

  This method should be invoked only by EOAssociation objects to propagate changes from display objects. Other application code should interact with the objects directly.

  If the receiver validates changes immediately, it sends _anObject_ a `validateValue:forKey:` message, returning NO if the object refuses to validate _value_. Otherwise, validation errors are checked by the EOEditingContext when it attempts to save changes.

  __See also:__
  [- `setValue:forObjectAtIndex:key:`](#apple-ge2tioi), [- `setSelectedObjectValue:forKey:`](#apple-geytqmzq), [- `valueForObject:
  key:`](#apple-ge2tomy), [- `validatesChangesImmediately`](#apple-ge2tmoi)

  ---

  ### setValue:forObjectAtIndex:key:

  - (BOOL)`setValue:`(id)_value_`forObjectAtIndex:`(unsigned int)_index_`key:`(NSString \*)_key_

  Invokes [`setValue:forObject:key:`](#apple-ge2timy) with the object at _index_, returning YES if successful and NO otherwise. This method should be invoked only by EOAssociation objects to propagate changes from display objects.

  __See also:__
  [- `setSelectedObjectValue:forKey:`](#apple-geytqmzq),[- `valueForObjectAtIndex:key:`](#apple-ge2tony)

  ---

  ### sortOrderings

  - (NSArray \*)`sortOrderings`

  Returns an array of EOSortOrdering objects that [`updateDisplayedObjects`](#apple-ge2tkny) uses to sort the displayed objects, as returned by the `[displayedObjects](#apple-geztmmi)` method.

  __See also:__
  [- `setSortOrderings:`](#apple-ge2teoa)

  ---

  ### updateDisplayedObjects

  - (void)`updateDisplayedObjects`

  Recalculates the receiver's displayed objects array and redisplays. If the receiver's delegate responds to `[displayGroup:displayArrayForObjects:](../Protocols/EODisplayGroupDelegate.md#apple-gm4tkma)`, it's sent this message and the returned array is set as the display group's displayed object. Otherwise, the receiver applies its qualifier and sort ordering to its array of objects. In either case, any objects that were selected before remain selected in the new displayed objects array.

  __See also:__
  [- `redisplay`](#apple-ge2dena), [- `displayedObjects`](#apple-geztmmi), [- `selectedObjects`](#apple-ge2dgmq), [- `qualifier`](#apple-ge2dema), [- `sortOrderings`](#apple-ge2tkmy)

  ---

  ### updatedObjectIndex

  - (int)`updatedObjectIndex`

  Returns the index in the displayed objects array of the most recently updated object, or -1 if more than one object has changed. The return value is meaningful only when [`contentsChanged`](#apple-geztgnq) returns YES. EOAssociations can use this method to optimize redisplay of their user interface objects.

  ---

  ### usesOptimisticRefresh

  - (BOOL)`usesOptimisticRefresh`

  Returns YES if the receiver redisplays only when its displayed objects change, NO if it redisplays on any change in its EOEditingContext.

  __See also:__
  [- `setUsesOptimisticRefresh:`](#apple-ge2tgmy)

  ---

  ### validatesChangesImmediately

  - (BOOL)`validatesChangesImmediately`

  Returns YES if the receiver immediately handles validation errors, or NO if it leaves errors for the EOEditingContext to handle when saving changes.

  __See also:__
  [- `setValidatesChangesImmediately:`](#apple-ge2tgoa)

  ---

  ### valueForObject:key:

  - (id)`valueForObject:`(id)_anObject_`key:`(NSString \*)_key_

  Returns _anObject_'s value for the property identified by _key_.

  ---

  ### valueForObjectAtIndex:key:

  - (id)`valueForObjectAtIndex:`(unsigned int)_index_`key:`(NSString \*)_key_

  Returns the value of the object at _index_ for the property identified by _key_.

  ---

  [!](EODetailSelectionAssociation-2.md)
  [!](EODisplayGroupDelegate.md)

  ---

  _Copyright © 1998, Apple Computer, Inc. All rights
  reserved._
