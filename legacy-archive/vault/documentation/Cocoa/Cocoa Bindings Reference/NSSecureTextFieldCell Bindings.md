---
title: Cocoa Bindings Reference
apple_id: 10000189i
resource_type: Guide
platform: macOS
topic: null
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Reference/CocoaBindingsRef/BindingsText/NSSecureTextFieldCell.html
archived_at: '2026-07-15T07:21:47.572643Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Reference](Introduction%20to%20Cocoa%20Bindings%20Reference.md)


[Next](NSSegmentedCell%20Bindings.md)[Previous](NSSecureTextField%20Bindings.md)

# NSSecureTextFieldCell Bindings

|  |  |
| --- | --- |
| __Related class__ | [NSSecureTextFieldCell](https://developer.apple.com/documentation/appkit/nssecuretextfieldcell) |
| __Availability__ | Available in OS X v10.3 and later. |

A multiple-value binding that determines if the `NSSecureTextFieldCell` is editable in the user interface.

When `editable` is bound, a new binding, `editable2`, is exposed and can be bound. Binding to `editable2` causes `editable3` to be exposed, and so on.

The contents of the `NSSecureTextFieldCell` are editable if a logical AND operation on all the `editable` bindings results in a Boolean value of `YES`.

__Availability:__Available in OS X v10.3 and later.__Binding is Read-Only.__

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

A multiple-value binding that determines if the `NSSecureTextFieldCell` is enabled in the user interface.

When `enabled` is bound, a new binding, `enabled2`, is exposed and can be bound. Binding to `enabled2` causes `enabled3` to be exposed, and so on.

The `NSSecureTextFieldCell` is enabled if a logical AND operation on all the `enabled` bindings results in a Boolean value of `YES`.

__Availability:__Available in OS X v10.3 and later.__Binding is Read-Only.__

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

An NSFont used to display the `NSSecureTextFieldCell`.

If `font` is bound, all other Font category bindings are disabled.

__Availability:__Available in OS X v10.3 and later.__Binding is Read-Only.__

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |

A Boolean value that determines if the NSFont used to display the `NSSecureTextFieldCell` is bold. If `fontBold` evaluates to `YES`, the bold attribute is added to the font.

If `fontBold` is bound, the `font` and `fontName` bindings are disabled.

__Availability:__Available in OS X v10.3 and later.__Binding is Read-Only.__

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

An NSString that specifies the family name of the NSFont used to display the contents of the `NSSecureTextFieldCell`.

If `fontFamilyName` is bound to a key, the `font` and `fontName` bindings are disabled.

__Availability:__Available in OS X v10.3 and later.__Binding is Read-Only.__

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

A Boolean value that determines if the NSFont used to display the `NSSecureTextFieldCell` is italic. If `fontItalic` evaluates to `YES`, the italic attribute is added to the font.

If `fontItalic` is bound, the `font` and `fontName` bindings are disabled.

__Availability:__Available in OS X v10.3 and later.__Binding is Read-Only.__

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

An NSString that specifies the full name of the NSFont that is used to display the contents of the `NSSecureTextFieldCell`. The full font name includes the family and the style of the font — for example, "Helvetica-Bold".

If `fontName` bound to a key, the `font`, `fontBold`, `fontFamilyName` and `fontItalic` bindings are disabled.

__Availability:__Available in OS X v10.3 and later.__Binding is Read-Only.__

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

An integer value that determines the size, in points, of the font used to display the `NSSecureTextFieldCell`.

If `fontSize` is bound, the `font` binding is disabled.

__Availability:__Available in OS X v10.3 and later.__Binding is Read-Only.__

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

An NSColor that specifies the color used to display the text of the `NSSecureTextFieldCell`.

__Availability:__Available in OS X v10.3 and later.__Binding is Read-Only.__

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |

An NSString or NSNumber that is displayed as the content of the `NSSecureTextFieldCell`.

__Availability:__Available in OS X v10.3 and later.

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Allows Editing Multiple Value Selection | [NSAllowsEditingMultipleValuesSelectionBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztinjt) | NSNumber (Boolean) |
| Always Presents Application Modal Alerts. Available in OS X v10.4 and later. | [NSAlwaysPresentsApplicationModalAlertsBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4dknzy) | NSNumber (Boolean) |
| Conditionally Sets Editable | [NSConditionallySetsEditableBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4tcmjt) | NSNumber (Boolean) |
| Conditionally Sets Enabled | [NSConditionallySetsEnabledBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztknjx) | NSNumber (Boolean) |
| Continuously Updates Value | [NSContinuouslyUpdatesValueBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tinby) | NSNumber (Boolean) |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |
| Validates Immediately | [NSValidatesImmediatelyBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkojx) | NSNumber (Boolean) |

Placeholders

| Description | Placeholder constant | Value class |
| --- | --- | --- |
| Multiple Values Placeholder | [NSMultipleValuesPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk4zq) | NSString |
| No Selection Placeholder | [NSNoSelectionPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42a) | NSString |
| Not Applicable Placeholder | [NSNotApplicablePlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42q) | NSString |
| Null Placeholder | [NSNullPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztonzw) | NSString |

A multiple-value binding that specifies a string value that replaces `%{value1}@` in a display pattern string that is used to set the value of the `NSSecureTextFieldCell`.

When `displayPatternValue1` is bound, a new binding, `displayPatternValue2`, is exposed and can be bound. Binding to `displayPatternValue2` causes `displayPatternValue3` to be exposed, and so on.

The Display Pattern binding option is an NSString that is used as the pattern string. The appropriate `displayPatternValueX` binding value is substituted for the `%{valueX}@` pattern in the display string.

As an example, if `displayPatternValue1` evaluates to `22`, `displayPatternValue2` evaluates to `5` and the Display Pattern string is `"%{value2}@ of %{value1}@ rows are selected"`, the resulting value will be "5 of 22 rows are selected".

If `displayPatternValue1` is bound, the `value` binding is not available.

__Availability:__Available in OS X v10.3 and later.__Binding is Read-Only.__

Binding Options

| Option | Binding option constant | Value class |
| --- | --- | --- |
| Raises for Not Applicable Keys | [NSRaisesForNotApplicableKeysBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljrha3tkmrv) | NSNumber (Boolean) |
| Display Pattern | [NSDisplayPatternBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsge4tamjq) | NSString |

Placeholders

| Description | Placeholder constant | Value class |
| --- | --- | --- |
| Multiple Values Placeholder | [NSMultipleValuesPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk4zq) | NSString |
| No Selection Placeholder | [NSNoSelectionPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42a) | NSString |
| Not Applicable Placeholder | [NSNotApplicablePlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42q) | NSString |
| Null Placeholder | [NSNullPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztonzw) | NSString |

[Next](NSSegmentedCell%20Bindings.md)[Previous](NSSecureTextField%20Bindings.md)

