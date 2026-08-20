---
title: Cocoa Bindings Reference
apple_id: 10000189i
resource_type: Guide
platform: macOS
topic: null
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Reference/CocoaBindingsRef/BindingsText/NSTreeController.html
archived_at: '2026-07-15T07:21:56.584760Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Reference](Introduction%20to%20Cocoa%20Bindings%20Reference.md)


[Next](NSView%20Bindings.md)[Previous](NSToolbarItem%20Bindings.md)

# NSTreeController Bindings

|  |  |
| --- | --- |
| __Related class__ | [NSTreeController](https://developer.apple.com/documentation/appkit/nstreecontroller) |
| __Availability__ | Available in OS X v10.4 and later. |

A multiple-value binding that determines if the `NSTreeController` is editable in the user interface.

When `editable` is bound, a new binding, `editable2`, is exposed and can be bound. Binding to `editable2` causes `editable3` to be exposed, and so on.

The contents of the `NSTreeController` are editable if a logical AND operation on all the `editable` bindings results in a Boolean value of `YES`.

__Availability:__Available in OS X v10.4 and later.__Binding is Read-Only.__

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |

Placeholders

| Description | Placeholder constant | Value class |
| --- | --- | --- |
| Multiple Values Placeholder | [NSMultipleValuesPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk4zq) | NSNumber (Boolean) or NSNull |
| No Selection Placeholder | [NSNoSelectionPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42a) | NSNumber (Boolean) or NSNull |
| Not Applicable Placeholder | [NSNotApplicablePlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42q) | NSNumber (Boolean) or NSNull |
| Null Placeholder | [NSNullPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztonzw) | NSNumber (Boolean) or NSNull |

An indexed collection that specifies the content of the `NSTreeController`.

The indexed collection is an NSArray instance or subclass, a property that is accessible using the key-value-coding indexed accessor methods, or is accessible through `mutableArrayValueForKey:`.

You should use the `contentSet` binding for Core Data to-many relationships.

__Availability:__Available in OS X v10.4 and later.

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Always Presents Application Modal Alerts. Available in OS X v10.4 and later. | [NSAlwaysPresentsApplicationModalAlertsBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4dknzy) | NSNumber (Boolean) |
| Conditionally Sets Editable | [NSConditionallySetsEditableBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4tcmjt) | NSNumber (Boolean) |
|  | [NSDeletesObjectsOnRemoveBindingsOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4dmnjr) | NSNumber (Boolean) |
| Handles Content As Compound Value | [NSHandlesContentAsCompoundValueBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztomjz) | NSNumber (Boolean) |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |
| Validates Immediately | [NSValidatesImmediatelyBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkojx) | NSNumber (Boolean) |

An indexed collection specifying the items that the `NSTreeController` treats as its content objects when the `contentArray` or `contentObject` binding returns the multiple selection marker.

The indexed collection is an NSArray instance or subclass, a property that is accessible using the key-value-coding indexed accessor methods, or is accessible through `mutableArrayValueForKey:`.

This binding is used when the `NSTreeController` displays the detail objects in a master-detail relationship, and the master controller allows multiple selection. Typically when multiple items are selected in the master controller, the detail controller bindings return the values set as the multiple values placeholder. When `contentArrayForMultipleSelection` is bound, the items in that array are used instead.

This binding is useful when combined with array operators. For example, `contentArray` is bound to the "selection.employees' keypath of `companyArrayController` and, `contentArrayForMultipleSelection` is bound to the "selection.@distinctUnionOfArrays.employees" keypath of `companyArrayController`. When a single company is selected in `companyArrayController`, the employees of that company are used as the content. When multiple companies are selected, the employees from all the selected companies are used as content.

__Availability:__Available in OS X v10.4 and later.__Binding is Read-Only.__

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Conditionally Sets Editable | [NSConditionallySetsEditableBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4tcmjt) | NSNumber (Boolean) |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |

An object that the `NSTreeController` treats as its content.

This is bound when the object is the detail controller in a master-detail configuration. The binding is typically created with the selection key path in the master array controller that represents an attribute or to-one relationship. When the master array controller's selection returns the multiple selection marker, the `contentArrayForMultipleSelection` binding is used as the content of the `NSTreeController`.

__Availability:__Available in OS X v10.4 and later.

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Always Presents Application Modal Alerts. Available in OS X v10.4 and later. | [NSAlwaysPresentsApplicationModalAlertsBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4dknzy) | NSNumber (Boolean) |
| Conditionally Sets Editable | [NSConditionallySetsEditableBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4tcmjt) | NSNumber (Boolean) |
|  | [NSDeletesObjectsOnRemoveBindingsOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4dmnjr) | NSNumber (Boolean) |
| Handles Content As Compound Value | [NSHandlesContentAsCompoundValueBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztomjz) | NSNumber (Boolean) |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |
| Validates Immediately | [NSValidatesImmediatelyBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkojx) | NSNumber (Boolean) |

An NSSet that specifies the content of the `NSTreeController`.

__Availability:__Available in OS X v10.4 and later.

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Always Presents Application Modal Alerts. Available in OS X v10.4 and later. | [NSAlwaysPresentsApplicationModalAlertsBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4dknzy) | NSNumber (Boolean) |
| Conditionally Sets Editable | [NSConditionallySetsEditableBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4tcmjt) | NSNumber (Boolean) |
|  | [NSDeletesObjectsOnRemoveBindingsOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4dmnjr) | NSNumber (Boolean) |
| Handles Content As Compound Value | [NSHandlesContentAsCompoundValueBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztomjz) | NSNumber (Boolean) |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |
| Validates Immediately | [NSValidatesImmediatelyBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkojx) | NSNumber (Boolean) |

An array of NSIndexPath instances that specify the current selection in the `NSTreeController`.

__Availability:__Available in OS X v10.4 and later.

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Always Presents Application Modal Alerts. Available in OS X v10.4 and later. | [NSAlwaysPresentsApplicationModalAlertsBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4dknzy) | NSNumber (Boolean) |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |
| Validates Immediately | [NSValidatesImmediatelyBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkojx) | NSNumber (Boolean) |

An indexed collection of NSSortDescriptor instances that specify the sort ordering of the contents of the `NSTreeController`.

The indexed collection is an NSArray instance or subclass, or a property that is accessible using the key-value-coding indexed accessor methods.

__Availability:__Available in OS X v10.4 and later.

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Always Presents Application Modal Alerts. Available in OS X v10.4 and later. | [NSAlwaysPresentsApplicationModalAlertsBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4dknzy) | NSNumber (Boolean) |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |
| Validates Immediately | [NSValidatesImmediatelyBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkojx) | NSNumber (Boolean) |

The NSManagedObjectContext instance that the `NSTreeController` is registered with.

__Availability:__Available in OS X v10.4 and later.__Binding is Read-Only.__

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |

[Next](NSView%20Bindings.md)[Previous](NSToolbarItem%20Bindings.md)

