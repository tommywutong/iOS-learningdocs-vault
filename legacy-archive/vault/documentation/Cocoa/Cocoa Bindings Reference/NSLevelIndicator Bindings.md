---
title: Cocoa Bindings Reference
apple_id: 10000189i
resource_type: Guide
platform: macOS
topic: null
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Reference/CocoaBindingsRef/BindingsText/NSLevelIndicator.html
archived_at: '2026-07-15T07:21:39.020699Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Reference](Introduction%20to%20Cocoa%20Bindings%20Reference.md)


[Next](NSLevelIndicatorCell%20Bindings.md)[Previous](NSImageView%20Bindings.md)

# NSLevelIndicator Bindings

|  |  |
| --- | --- |
| __Related class__ | [NSLevelIndicator](https://developer.apple.com/documentation/appkit/nslevelindicator) |
| __Availability__ | Available in OS X v10.4 and later. |

A multiple-value binding that determines if the `NSLevelIndicator` is enabled in the user interface.

When `enabled` is bound, a new binding, `enabled2`, is exposed and can be bound. Binding to `enabled2` causes `enabled3` to be exposed, and so on.

The `NSLevelIndicator` is enabled if a logical AND operation on all the `enabled` bindings results in a Boolean value of `YES`.

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

A multiple-value binding that determines if the `NSLevelIndicator` is displayed in the user interface.

When `hidden` is bound, a new binding, `hidden2`, is exposed and can be bound. Binding to `hidden2` causes `hidden3` to be exposed, and so on.

The `NSLevelIndicator` is hidden if a logical OR operation on all the `hidden` bindings results in a Boolean value of `YES`.

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

A `float` value that indicates the critical value of the `NSLevelIndicator`.

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

An NSString that contains the tool tip to display for this `NSLevelIndicator`.

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

A `float` value that indicates the warning value of the `NSLevelIndicator`.

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

A `double` value that specifies the maximum value allowed by the `NSLevelIndicator`.

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

A `double` value that specifies the minimum value allowed by the `NSLevelIndicator`.

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

A `float` value that specifies the current value of the `NSLevelIndicator`.

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
| Multiple Values Placeholder | [NSMultipleValuesPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk4zq) | NSNumber |
| No Selection Placeholder | [NSNoSelectionPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42a) | NSNumber |
| Not Applicable Placeholder | [NSNotApplicablePlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydilktk42q) | NSNumber |
| Null Placeholder | [NSNullPlaceholderBindingOption](Binding%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydiljsgaztonzw) | NSNumber |

[Next](NSLevelIndicatorCell%20Bindings.md)[Previous](NSImageView%20Bindings.md)

