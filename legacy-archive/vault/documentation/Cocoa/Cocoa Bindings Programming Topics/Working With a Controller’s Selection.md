---
title: Cocoa Bindings Programming Topics
apple_id: 10000167i
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/Concepts/CntrlSelection.html
archived_at: '2026-07-15T07:12:00.996794Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Programming Topics](Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md)


[Next](Bindings%20Message%20Flow.md)[Previous](Providing%20Controller%20Content.md)

# Working With a Controller’s Selection

NSObjectController and its subclasses NSArrayController and NSTreeController support tracking of the currently selected object or objects. This article explains how to get a controller’s current selection, change the current selection, and fine-tune the selection behaviors.

There are two methods that are commonly used to access the objects that are currently selected: `selection` and `selectedObjects`.

NSObjectController and its subclasses implement the `selection` method. This method returns a proxy object that represents the receiver’s current selection. The proxy is fully key-value-coding compliant.

When you request a key’s value from the selection proxy it returns the value, or a _selection marker_. Placeholder markers provide additional information about the selection. There are three placeholder markers defined in the `NSPlaceholders` informal protocol:

- NSNoSelectionMarker

  The NSNoSelectionMarker indicates that there are no items selected in the controller.
- NSNotApplicableMarker

  The NSNotApplicableMarker indicates that the underlying object is not key-value-coding compliant for the requested key.
- NSMultipleValuesMarker

  The NSMultipleValuesMarker indicates that more than one object is selected in the controller and the values for the requested key aren’t the same.

  By default controllers return the NSMultipleValuesMarker only when the values for the requested key differ. For example, if the value for `selection.name` returns an array containing three strings—”Tony”, “Tony”, “Tony”—the string “Tony” is returned instead of the NSMultipleValuesMarker.

  A collection controller can be configured—either programmatically using the method `setAlwaysUsesMultipleValuesMarker:` or by checking the “Always uses multiple values marker” checkbox in Interface Builder—such that it always returns NSMultipleValuesMarker when multiple items are selected, even if the values are equal.

Some bindings, such as NSTextField’s `value` binding, allow you to replace selection markers with custom values that are treated as placeholder values by the controls. These replacement values are specified in the Bindings inspector in Interface Builder. Bindings established programmatically can provide values for the `NSNoSelectionPlaceholderBindingOption`, `NSNotApplicablePlaceholderBindingOption`, `NSNullPlaceholderBindingOption` or `NSRaisesForNotApplicableKeysBindingOption` keys, defined in the NSKeyValueBindingCreation informal protocol, in the options dictionary passed to `bind:toObject:withKeyPath:options:`. The NSPlaceholders protocol also provides two class methods `setDefaultPlaceholder:forMarker:withBinding:` and `defaultPlaceholderForMarker:withBinding:` that allow you to provide default placeholders for the specified selection markers for a binding.

Often you need to directly access the objects currently selected by the controller, rather than the proxy object returned by `selection`. NSObjectController and its subclasses provide the `selectedObjects` method to allow you to do just that. This method returns an array containing the objects that are currently selected by the receiver. NSObjectController’s implementation returns an array containing a single object, the content object.

The collection controllers provide methods that allow you to modify the current selection by adding and removing objects, or replacing the selection entirely.

All the methods that change a controller’s selection return a boolean value that indicates if the selection was successfully changed. This is because an attempt to change the selection may cause a `commitEditing` message to be sent which may fail or be denied, perhaps due to a value failing validation. If the selection is changed successfully, these methods return `YES`, otherwise they return `NO`.

NSArrayController provides the following methods for replacing the controller’s selection completely or adding and removing objects from the current selection:

```objc
- (BOOL)addSelectedObjects:(NSArray *)objects;
- (BOOL)removeSelectedObjects:(NSArray *)objects;
- (BOOL)setSelectedObjects:(NSArray *)objects;
```

All three methods require that you pass an array containing the objects as the parameter.

The collection controller classes provide additional methods to get the current selection as a set of indexes to the objects in the collection.

NSArrayController provides the following methods for getting and setting the selection by index:

```objc
- (unsigned int)selectionIndex;
- (BOOL)setSelectionIndex:(unsigned int)index;

- (NSIndexSet *)selectionIndexes;
- (BOOL)setSelectionIndexes:(NSIndexSet *)indexes;
- (BOOL)addSelectionIndexes:(NSIndexSet *)indexes;
- (BOOL)removeSelectionIndexes:(NSIndexSet *)indexes;
```

The `selectionIndexes` method returns an NSIndexSet that specifies the indexes of all the selected objects. The convenience method `selectionIndex` returns the index of the first selected object as an unsigned integer.

You can explicitly set the selection of the controller using the `setSelectionIndexes:` method, passing an NSIndexSet that specifies the indexes of the items that should become the selection. The `setSelectionIndex:` method is a convenience method that lets you set the selection to a single index. If the selection is changed successfully, these methods return `YES`.

The `addSelectionIndexes:` method attempts to add objects specified in the NSIndexSet parameter to the current selection. Similarly, the `removeSelectionIndexes:` attempts to remove the objects specified by index in the NSIndexSet parameter from the selection. If the selection is changed successfully, the methods return `YES`.

NSTreeController treats data as an array of dictionaries of arrays, so a simple index of the selection isn’t sufficient. Instead NSTreeController uses an NSIndexPath to specify the location of an object in the tree. An NSIndexPath specifies the “path” to the selection as a series of indexes into the arrays, for example “1.4.2.3”.

NSTreeController provides the following methods for getting and setting the selection by index path:

```objc
-(NSIndexPath *)selectionIndexPath
-(NSArray *)selectionIndexPaths

-(BOOL)setSelectionIndexPath:(NSIndexPath *)indexPath
-(BOOL)setSelectionIndexPaths:(NSArray *)indexPaths

-(BOOL)addSelectionIndexPaths:(NSArray *)indexPaths
-(BOOL)removeSelectionIndexPaths:(NSArray *)indexPaths
```

The `selectionIndexPaths:` method returns an array of NSIndexPath objects that represent each of the currently selected objects. The convenience method `selectionIndexPath` returns the first selected object as an NSIndexPath.

You explicitly set the current selection using the `setSelectionIndexPaths:` method, passing an NSArray of NSIndexPath objects as the parameter. The convenience method `setSelectionIndexPath:` sets the selection to the single object specified by the NSIndexPath parameter.

The methods `addSelectionIndexPaths:` and `removeSelectionIndexPaths:` add or remove the objects at the index paths specified in the array from the selection. As with the other selection modifying methods they return a boolean value of `YES` if the selection was successfully changed.

The collection controllers provide several methods that allow you to fine-tune how selection is maintained by a controller, and how values are returned by the `selection` method.

Often it is desirable to attempt to always have at least one item in a collection selected after an action such as removing an item. This is the default behavior of the collection controllers.

You can modify this behavior using the method `setAvoidsEmptySelection:` passing `NO` as the parameter. This allows the controller to have an empty selection, even if there are objects in the content. You can query the current behavior using the method `avoidsEmptySelection`.

Interface Builder allows you to change this behavior for a collection controller by unchecking the “Avoids empty selection” checkbox in the controller’s inspector panel.

By default a collection controller automatically selects objects as they are inserted. While this is often the correct behavior, if you are inserting many objects into the collection it is inefficient and can degrade performance.

You can turn off this behavior using the `setSelectsInsertedObjects:` method. Passing `YES` as the parameter causes all newly inserted objects to be selected. If `NO` is passed as the parameter, the current selection is unchanged as objects are inserted. The method `selectsInsertedObjects` returns a boolean indicating if newly inserted objects will be selected.

You can also change this setting in Interface Builder by unchecking the “Selects inserted objects” checkbox in the controller’s inspector panel.

The NSMultipleValuesMarker indicates that more than one object is selected in the controller and the values for the requested key aren’t the same. If the values are the same the value is returned rather than the selection marker. While this allows editing of that common value across all the selected objects, it may not be the desired result.

You can force all multiple selections to always return the NSMultipleValuesMarker using the method `setAlwaysUsesMultipleValuesMarker:`, passing `YES` as the parameter. You query the state of this setting using the method `alwaysUsesMultipleValuesMarker`.

This setting can also be changed in Interface Builder by checking the “Always use multiple values marker” checkbox.

With large selections, enabling this option can improve performance.

When the content of a collection controller changes, the default behavior is to attempt to find matching objects for the current selection in the new content. Figure 1 shows a master-detail interface in which the selected object in the detail NSTableView is automatically selected when the user selects a different activity in the master NSTableView.

__Figure 1__  Preserves selection example

!!

This behavior can be disabled by calling the `setPreservesSelection:` method, passing `NO` as the parameter. The current state is queried using the `preservesSelection` method which returns a boolean. You can also change this setting in Interface Builder by unchecking the “Preserves selection” option in the controller’s inspector.

While the default behavior is often appropriate, there can be performance implications. When the content changes, the current selection must first be cached, and then the new content collection must be searched for matching objects. This can become costly when dealing with large collections and multiple selections.

There is a per-binding option that allows you further control over the selection when using an NSArrayController.

The `NSSelectsAllWhenSettingContentBindingOption` causes the array controller to automatically select all the items in the array when the application changes the `contentArray`, `contentSet`, `contentObject` or `contentArrayForMultipleSelection` value of the controller.

__Figure 2__  Selects all when setting content example

!!

Figure 2 shows an application with a master-detail interface. The detail NSTableView displays a single member selection “Daniel”. When the user selects the “Swim Team” item in the master NSTableView all the members are selected automatically.

This option is set either in the Bindings inspector in Interface Builder, or by setting an NSNumber object with a boolean value of `YES` as the `NSSelectsAllWhenSettingContentBindingOption` value in the options dictionary passed to `bind:toObject:withKeyPath:options:`.

The “Selects All When Setting Content” option is also useful when creating inspectors for master-detail interfaces that allow multiple selections to occur in the master interface. The selection that is to be inspected is predetermined by the master array controller. The inspector array controller is bound to the master array controller's `selectedObjects` binding, specifying the “Selects All When Setting Content” option. This ensures that all items in the master controller's current selection are always selected in the inspector. In an NSDocument-based application, the detail array controller's `contentArray` binding is typically bound to the NSApplication instance using the `mainWindow.windowController.document.<yourmastercontroller>` key path, substituting the master array controller's key for the final key in the key path.

[Next](Bindings%20Message%20Flow.md)[Previous](Providing%20Controller%20Content.md)

