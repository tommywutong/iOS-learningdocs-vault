---
title: Cocoa Bindings Reference
apple_id: 10000189i
resource_type: Guide
platform: macOS
topic: null
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Reference/CocoaBindingsRef/BindingsText/NSDatePicker.html
archived_at: '2026-07-15T07:21:35.022755Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Reference](Introduction%20to%20Cocoa%20Bindings%20Reference.md)


[Next](NSDatePickerCell%20Bindings.md)[Previous](NSComboBoxCell%20Bindings.md)

# NSDatePicker Bindings

|  |  |
| --- | --- |
| __Related class__ | [NSDatePicker](https://developer.apple.com/documentation/appkit/nsdatepicker) |
| __Availability__ | Available in OS X v10.4 and later. |

A multiple-value binding that determines if the `NSDatePicker` is enabled in the user interface.

When `enabled` is bound, a new binding, `enabled2`, is exposed and can be bound. Binding to `enabled2` causes `enabled3` to be exposed, and so on.

The `NSDatePicker` is enabled if a logical AND operation on all the `enabled` bindings results in a Boolean value of `YES`.

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

A multiple-value binding that determines if the `NSDatePicker` is displayed in the user interface.

When `hidden` is bound, a new binding, `hidden2`, is exposed and can be bound. Binding to `hidden2` causes `hidden3` to be exposed, and so on.

The `NSDatePicker` is hidden if a logical OR operation on all the `hidden` bindings results in a Boolean value of `YES`.

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

An NSFont used to display the `NSDatePicker`.

If `font` is bound, all other Font category bindings are disabled.

__Availability:__Available in OS X v10.4 and later.__Binding is Read-Only.__

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |

A Boolean value that determines if the NSFont used to display the `NSDatePicker` is bold. If `fontBold` evaluates to `YES`, the bold attribute is added to the font.

If `fontBold` is bound, the `font` and `fontName` bindings are disabled.

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

An NSString that specifies the family name of the NSFont used to display the contents of the `NSDatePicker`.

If `fontFamilyName` is bound to a key, the `font` and `fontName` bindings are disabled.

__Availability:__Available in OS X v10.4 and later.__Binding is Read-Only.__

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |

Placeholders

| Description | Placeholder constant | Value class |
| --- | --- | --- |
| Multiple Values Placeholder | [NSMultipleValuesPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk4zq) | NSString |
| No Selection Placeholder | [NSNoSelectionPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42a) | NSString |
| Not Applicable Placeholder | [NSNotApplicablePlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42q) | NSString |
| Null Placeholder | [NSNullPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztonzw) | NSString |

A Boolean value that determines if the NSFont used to display the `NSDatePicker` is italic. If `fontItalic` evaluates to `YES`, the italic attribute is added to the font.

If `fontItalic` is bound, the `font` and `fontName` bindings are disabled.

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

An NSString that specifies the full name of the NSFont that is used to display the contents of the `NSDatePicker`. The full font name includes the family and the style of the font — for example, "Helvetica-Bold".

If `fontName` bound to a key, the `font`, `fontBold`, `fontFamilyName` and `fontItalic` bindings are disabled.

__Availability:__Available in OS X v10.4 and later.__Binding is Read-Only.__

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |

Placeholders

| Description | Placeholder constant | Value class |
| --- | --- | --- |
| Multiple Values Placeholder | [NSMultipleValuesPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk4zq) | NSString |
| No Selection Placeholder | [NSNoSelectionPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42a) | NSString |
| Not Applicable Placeholder | [NSNotApplicablePlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42q) | NSString |
| Null Placeholder | [NSNullPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztonzw) | NSString |

An integer value that determines the size, in points, of the font used to display the `NSDatePicker`.

If `fontSize` is bound, the `font` binding is disabled.

__Availability:__Available in OS X v10.4 and later.__Binding is Read-Only.__

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |

Placeholders

| Description | Placeholder constant | Value class |
| --- | --- | --- |
| Multiple Values Placeholder | [NSMultipleValuesPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk4zq) | NSNumber |
| No Selection Placeholder | [NSNoSelectionPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42a) | NSNumber |
| Not Applicable Placeholder | [NSNotApplicablePlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42q) | NSNumber |
| Null Placeholder | [NSNullPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztonzw) | NSNumber |

An NSString that contains the tool tip to display for this `NSDatePicker`.

__Availability:__Available in OS X v10.4 and later.__Binding is Read-Only.__

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |

Placeholders

| Description | Placeholder constant | Value class |
| --- | --- | --- |
| Multiple Values Placeholder | [NSMultipleValuesPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk4zq) | NSString |
| No Selection Placeholder | [NSNoSelectionPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42a) | NSString |
| Not Applicable Placeholder | [NSNotApplicablePlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42q) | NSString |
| Null Placeholder | [NSNullPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztonzw) | NSString |

An NSColor that specifies the color used to display the text of the `NSDatePicker`.

__Availability:__Available in OS X v10.4 and later.__Binding is Read-Only.__

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |

An NSDate instance that specifies the maximum date value allowed by the `NSDatePicker`.

__Availability:__Available in OS X v10.4 and later.__Binding is Read-Only.__

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |

Placeholders

| Description | Placeholder constant | Value class |
| --- | --- | --- |
| Multiple Values Placeholder | [NSMultipleValuesPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk4zq) | NSDate |
| No Selection Placeholder | [NSNoSelectionPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42a) | NSDate |
| Not Applicable Placeholder | [NSNotApplicablePlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42q) | NSDate |
| Null Placeholder | [NSNullPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztonzw) | NSDate |

An NSDate instance that specifies the minimum date value allowed by the `NSDatePicker`.

__Availability:__Available in OS X v10.4 and later.__Binding is Read-Only.__

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |

Placeholders

| Description | Placeholder constant | Value class |
| --- | --- | --- |
| Multiple Values Placeholder | [NSMultipleValuesPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk4zq) | NSDate |
| No Selection Placeholder | [NSNoSelectionPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42a) | NSDate |
| Not Applicable Placeholder | [NSNotApplicablePlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42q) | NSDate |
| Null Placeholder | [NSNullPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztonzw) | NSDate |

An NSDate instance to be displayed in the `NSDatePicker`.

__Availability:__Available in OS X v10.4 and later.

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Allows Editing Multiple Value Selection | [NSAllowsEditingMultipleValuesSelectionBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztinjt) | NSNumber (Boolean) |
| Always Presents Application Modal Alerts. Available in OS X v10.4 and later. | [NSAlwaysPresentsApplicationModalAlertsBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4dknzy) | NSNumber (Boolean) |
| Conditionally Sets Enabled | [NSConditionallySetsEnabledBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztknjx) | NSNumber (Boolean) |
| Conditionally Sets Hidden | [NSConditionallySetsHiddenBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztmnrx) | NSNumber (Boolean) |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |
| Validates Immediately | [NSValidatesImmediatelyBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkojx) | NSNumber (Boolean) |

Placeholders

| Description | Placeholder constant | Value class |
| --- | --- | --- |
| Multiple Values Placeholder | [NSMultipleValuesPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk4zq) | NSDate |
| No Selection Placeholder | [NSNoSelectionPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42a) | NSDate |
| Not Applicable Placeholder | [NSNotApplicablePlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42q) | NSDate |
| Null Placeholder | [NSNullPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztonzw) | NSDate |

[Next](NSDatePickerCell%20Bindings.md)[Previous](NSComboBoxCell%20Bindings.md)

