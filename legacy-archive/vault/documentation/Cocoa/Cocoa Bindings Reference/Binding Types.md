---
title: Cocoa Bindings Reference
apple_id: 10000189i
resource_type: Guide
platform: macOS
topic: null
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Reference/CocoaBindingsRef/Concepts/BindingTypes.html
archived_at: '2026-07-15T07:21:59.083548Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Reference](Introduction%20to%20Cocoa%20Bindings%20Reference.md)


[Next](Binding%20Options.md)[Previous](Introduction%20to%20Cocoa%20Bindings%20Reference.md)

# Binding Types

Simple-value bindings are the most common type of binding. A simple-value binding is bound to a single value.

In some cases, simple-value bindings are considered read-only. Changes made to the binding value are observed and reflected in the user interface. Changes made in the user interface, however, are not propagated to the originating attribute.

Multiple-value bindings allow multiple bindings to be created for a single binding. Creating a binding with the first binding automatically causes a second binding to be exposed, and so on.

For example, if you bind to the `enabled` binding, a binding called `enabled2` is exposed. If you bind `enabled2`, the object will expose `enabled3`, and so on. All these binding values are then used together in returning the final value of the binding.

Multiple-value bindings are always read-only.

There are four variations of multiple-value bindings.

Multiple-value Boolean bindings are used to determine if an object is editable, hidden, or enabled. The resulting value of the binding is derived by forming the logical AND or logical OR of the values of the exposed bindings. The logical operation used depends on the specific binding.

The conventional Cocoa target/action mechanism provides the means for a control to invoke a message, passing itself as the sender. Multiple-value argument bindings extend that capability, allowing you to specify a target while passing an arbitrary number of arguments to the action. This mechanism provides significantly greater flexibility.

To set up target and argument bindings, you typically first bind the target binding—often to a controller’s `selection` or `arrangedObjects` key path—and specify the selector name to invoke. For each argument of the selector, you then bind an `argument` binding. When the control is clicked, the action is sent to the target with the specified parameters.

You can specify the selector name for any of the argument bindings, and the change will be propagated throughout.

The multiple-value pattern bindings allow you to assemble the final value of a binding from multiple string values. This pattern is used by the `displayPatternValue` and `displayPatternTitle` bindings.

A common use of pattern bindings is to indicate the size of the selection in an array controller in the form “5 of 34 selected”. To implement this, you’d bind `displayPatternValue1` to the controller with the key path `selection.@count`, and then bind `displayPatternValue2` to the controller with the key path `contentArray.@count`. You then specify the format string by setting the value pattern option to “`%{value1}@ of %{value2}@ selected`”.

In the pattern string, the value of `displayPatternValue1` is represented by “`%{value1}@`”, the value of `displayPatternValue2` by “`%{value2}@`”, and so on. Unlike the other multiple-value bindings, the first pattern binding is always 1.

You can specify the pattern string for any of the display pattern value bindings, and the change will be propagated throughout.

The multiple-value predicate binding allows you to create a search field pop-up menu that is pre populated with menu items that correspond to predicate filters. Each of the predicate bindings correspond to an entry in the search field pop-up menu. This multiple-value binding is used by the `NSSearchField` `predicate` binding.

The display name string is used as the menu item title. The predicate format is string that specifies the predicate for that menu item using the predicate format described in _[Predicate Programming Guide](../Predicate%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoobz)_. Any occurrences of the string `$value` in the predicate format string are replaced with the contents of the search field.

For example, if you have a search field pop-up menu item named “Subject” that will filter message objects in an array controller based on the value of the subject key, you would construct a predicate as follows:

__Table 1__  Example predicate binding

| Binding Field | Value |
| Controller | messageArrayController |
| Model Keypath | filterPredicate |
| Display Name | Subject |
| Predicate Format | `subject contains $value` |

Additional search menu items can be added by binding to the newly exposed bindings, `predicate2`, `predicate3`, etc.

Read-only bindings are bindings that take new values from the observed object, but do not return any changes made to that value.

As an example, the `valuePath` binding of `NSImageView` is a read-only binding. Changing the value of the object that this binding references will result in a different image being displayed. However, changing the image by dragging a new image into the image view does not cause the value to which `valuePath` is bound to change.

[Next](Binding%20Options.md)[Previous](Introduction%20to%20Cocoa%20Bindings%20Reference.md)

