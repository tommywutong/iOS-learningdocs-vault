---
title: Cocoa Bindings Reference
apple_id: 10000189i
resource_type: Guide
platform: macOS
topic: null
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Reference/CocoaBindingsRef/Concepts/BindingsOptions.html
archived_at: '2026-07-15T07:21:59.589844Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Reference](Introduction%20to%20Cocoa%20Bindings%20Reference.md)


[Next](AMPathPopUpButton%20Bindings.md)[Previous](Binding%20Types.md)

# Binding Options

Many bindings allow you to specify additional options that modify their default behavior. This can be done both in Interface Builder and programmatically.

When creating a binding in Interface Builder, the Bindings pane of the inspector displays the available options for the binding. Bindings created programmatically pass an `NSDictionary` containing the option keys and corresponding values.

A Boolean value that determines if the binding allows editing when the value represents a multiple selection.

If `YES`, the content is editable and any edits will be applied to all the selected values. If the option is `NO`, editing of the content is disabled.

| Constant | Value class |
| --- | --- |
| `NSAllowsEditingMultipleValuesSelection` | NSNumber (Boolean) |

A Boolean value that determines if the argument binding allows passing argument values of Null.

If `YES`, then Null arguments are allowed, otherwise they are prohibited.

| Constant | Value class |
| --- | --- |
| `NSAllowsNullArgumentBindingOption` | NSNumber (Boolean) |

A Boolean value that determines if validation and error alert panels displayed as a result of this binding are displayed as application modal alerts.

If `YES`, then the alerts are displayed application modal, otherwise they are displayed as sheets.

| Constant | Value class |
| --- | --- |
| `NSAlwaysPresentsApplicationModalAlertsBindingOption` | NSNumber (Boolean) |

A Boolean value that determines if the editable state of the user interface item is automatically configured based on the controller's selection.

If `YES`, the item's editable state is configured automatically. The user interface item will not be editable when the value represents a multiple selection, unless the selected objects are considered equal.

| Constant | Value class |
| --- | --- |
| `NSConditionallySetsEditableBindingOption` | NSNumber (Boolean) |

A Boolean value that determines if the enabled state of the user interface item is automatically configured based on the controller's selection.

If `YES`, the item's enabled state is configured automatically. The user interface item is disabled for editing when the value represents a multiple selection unless the selected objects are considered equal.

| Constant | Value class |
| --- | --- |
| `NSConditionallySetsEnabledBindingOption` | NSNumber (Boolean) |

A Boolean value that determines if the hidden state of the user interface item is automatically configured based on the controller's selection.

If `YES`, the item's hidden state is configured automatically. The user interface item is hidden when the value represents a multiple selection unless the selected objects are considered equal.

| Constant | Value class |
| --- | --- |
| `NSConditionallySetsHiddenBindingOption` | NSNumber (Boolean) |

An integer value that specifies where the menu content provided by the binding will be inserted in the bound menu. For example, setting the content placement tag to a value of six will result in the bounds menu items being inserted in place of the menu item with the tag ID 6. This allows a menu to have both static menu items and dynamically bound menu items.

| Constant | Value class |
| --- | --- |
| `NSContentPlacementTagBindingOption` | NSNumber (Integer) |

A Boolean value that determines whether the value of the binding is updated as edits are made to the user interface item or is updated only when the user interface item resigns as the responder.

If `YES`, the bound object is updated continuously; otherwise the update is made only when the user interface item resigns as the responder.

| Constant | Value class |
| --- | --- |
| `NSContinuouslyUpdatesValueBindingOption` | NSNumber (Boolean) |

A Boolean value that determines if NSTableColumn can be sorted by clicking on the column’s header cell.

If `YES`, the table column will sort when the user clicks in the column header cell; otherwise the column remains unsorted.

| Constant | Value class |
| --- | --- |
| `NSCreatesSortDescriptorBindingOption` | NSNumber (Boolean) |

A Boolean value that determines whether objects removed from the controller are removed just from the relationship, or from the relationship and the object graph. This option is only relevant when the contentSet of the controller is a to-many relationship.

If `YES`, objects removed from the controller are removed from the relationship and the object graph; otherwise the objects are removed from the relationship only.

| Constant | Value class |
| --- | --- |
| `NSDeletesObjectsOnRemoveBindingOption` | NSNumber (Boolean) |

An NSString that is used as the content of the search field pop-up menu item corresponding to the multi-value predicate binding. See [Predicate Binding](Binding%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydkljsge3dsobv) for further information.

| Constant | Value class |
| --- | --- |
| `NSDisplayNameBindingOption` | NSString |

An NSString that specifies a format string used to construct the final value of a string.

The value of the `displayPatternValue` bindings replaces the corresponding `%{valueX}@` pattern in the display pattern string. See [Value With Pattern Bindings](Binding%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydkljsge3dqojx) for further information.

| Constant | Value class |
| --- | --- |
| `NSDisplayPatternBindingOption` | NSString |

A Boolean value that determines if the content is treated as a compound value.

Model objects can store relationship-like data in "compound" values and it may be necessary to use a reversible value transformer to translate those compound values temporarily into smaller pieces, that can be displayed and edited individually. See “[Bindings Message Flow](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/Concepts/MessageFlow.html#//apple_ref/doc/uid/TP40002149)” in “_[Cocoa Bindings Programming Topics](../Cocoa%20Bindings%20Programming%20Topics/Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3do2i)_” for more information.

If `YES`, the content of a controller is treated as a compound value and—by using a reversible value transformer—will apply changes as a single value to the master model object if anything changes (edits, additions, removals).

| Constant | Value class |
| --- | --- |
| `NSHandlesContentAsCompoundValueBindingOption` | NSNumber (Boolean) |

A Boolean value that determines if an additional item which represents Null is inserted into a matrix or pop-up menu before the items in the content array.

If `YES`, an additional item is inserted into the matrix or pop-up menu—before the items in the content array—that returns Null as the `selectedObject` or `selectedValue`. The item is labeled using the null placeholder specified for the `content` binding or the `contentValue` binding.

| Constant | Value class |
| --- | --- |
| `NSInsertsNullPlaceholderBindingOption` | NSNumber (Boolean) |

A Boolean value that determines whether the specified selector is invoked with the array as the argument or is invoked repeatedly with each array item as an argument.

If `YES`, clicking the user interface item causes the specified selector to be invoked for every item in the array, passing each item in turn as the argument. Otherwise, the selector is invoked once, passing the array instance as the argument.

| Constant | Value class |
| --- | --- |
| `NSInvokesSeparatelyWithArrayObjectsBindingOption` | NSNumber (Boolean) |

An object that is used as a placeholder when the key path of the bound controller returns the `NSMultipleValuesMarker` marker for a binding.

| Constant | Value class |
| --- | --- |
| `NSMultipleValuesPlaceholderBindingOption` | The value class is dependent on the particular binding. |

An object that is used as a placeholder when the key path of the bound controller returns the `NSNoSelectionMarker` marker for a binding.

| Constant | Value class |
| --- | --- |
| `NSNoSelectionPlaceholderBindingOption` | The value class is dependent on the particular binding. |

An object that is used as a placeholder when the key path of the bound controller returns the `NSNotApplicableMarker` marker for a binding.

| Constant | Value class |
| --- | --- |
| `NSNotApplicablePlaceholderBindingOption` | The value class is dependent on the particular binding. |

An object that is used as a placeholder when the key path of the bound controller returns `NULL` for a binding.

| Constant | Value class |
| --- | --- |
| `NSNullPlaceholderBindingOption` | The value class is dependent on the particular binding. |

An NSString that is used as the predicate search string of the search field pop-up menu item corresponding to the multi-value predicate binding. See [Predicate Binding](Binding%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydkljsge3dsobv) for further information.

| Constant | Value class |
| --- | --- |
| `NSPredicateFormatBindingOption` | NSString |

A Boolean value that specifies if an exception is raised when a binding is bound to a key that does not exist.

If `YES`, an exception is raised when the bound key is not applicable, otherwise the NSNotApplicableMarker is returned..

| Constant | Value class |
| --- | --- |
| `NSRaisesForNotApplicableKeysBindingOption` | NSNumber (Boolean) |

An NSString that specifies the method selector invoked by the `target` binding when the user interface item is clicked.

| Constant | Value class |
| --- | --- |
| `NSSelectorNameBindingOption` | NSString |

A Boolean value that specifies if all the items in the array controller are selected when the content is set.

If `YES`, all the items are selected when the `contentObject` or `contentArray` binding is set.

| Constant | Value class |
| --- | --- |
| `NSSelectsAllWhenSettingContentBindingOption` | NSNumber (Boolean) |

A Boolean value that determines if the contents of the binding are validated immediately.

If `YES`, the value is validated as it is entered. Otherwise, the content is validated only when the user interface item attempts to resign as the responder.

| Constant | Value class |
| --- | --- |
| `NSValidatesImmediatelyBindingOption` | NSNumber (Boolean) |

[Next](AMPathPopUpButton%20Bindings.md)[Previous](Binding%20Types.md)

