---
title: Auto Layout Guide
apple_id: TP40010853
resource_type: Guide
platform: tvOS|iOS|macOS
topic: User Experience
technology: AppKit
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/ModifyingConstraints.html
archived_at: '2026-07-18T02:10:20.975609Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Auto Layout Guide](index.md)



## Changing Constraints

A constraint change is anything that alters the underlying mathematical expression of a constraint (see Figure 17-1). You can learn more about constraint equations in [Anatomy of a Constraint](AnatomyofaConstraint.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqojnknltc).

__Figure 17-1__The constraint equation
![image: ../Art/view_formula_2x.png](attachments/Art/view_formula_2x.png)

All of the following actions change one or more constraints:

- Activating or deactivating a constraint
- Changing the constraint’s constant value
- Changing the constraint’s priority
- Removing a view from the view hierarchy

Other changes, like setting a control’s property, or modifying the view hierarchy, can also change constraints. When a change occurs, the system schedules a deferred layout pass (see [The Deferred Layout Pass](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrzfvjvomy)).

In general, you can make these changes at any time. Ideally, most constraints should be set up in Interface Builder, or programatically created by the view controller during the controller’s initial setup (for example, in [viewDidLoad](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621495-viewdidload)). If you need to dynamically change constraints at runtime, it’s usually best to change them when the application’s state changes. For example, if you want to change a constraint in response to a button tap, make that change directly in the button’s action method.

Occasionally, you may need to batch a set of changes for performance reasons. For more information, see [Batching Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrzfvjvomq).

### The Deferred Layout Pass

Instead of immediately updating the affected views’ frames, Auto Layout schedules a layout pass for the near future. This deferred pass updates the layout’s constraints and then calculates the frames for all the views in the view hierarchy.

You can schedule your own deferred layout pass by calling the [setNeedsLayout](https://developer.apple.com/documentation/uikit/uiview/1622601-setneedslayout) method or the [setNeedsUpdateConstraints](https://developer.apple.com/documentation/uikit/uiview/1622450-setneedsupdateconstraints) method.

The deferred layout pass actually involves two passes through the view hierarchy:

1. The update pass updates the constraints, as necessary
2. The layout pass repositions the view’s frames, as necessary

### Update Pass

The system traverses the view hierarchy and calls the [updateViewConstraints](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621379-updateviewconstraints) method on all view controllers, and the [updateConstraints](https://developer.apple.com/documentation/uikit/uiview/1622512-updateconstraints) method on all views. You can override these methods to optimize changes to your constraints (see [Batching Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrzfvjvomq)).

### Layout Pass

The system traverses the view hierarchy again and calls [viewWillLayoutSubviews](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621437-viewwilllayoutsubviews) on all view controllers, and [layoutSubviews](https://developer.apple.com/documentation/uikit/uiview/1622482-layoutsubviews) ([layout](https://developer.apple.com/documentation/appkit/nsview/1526146-layout) in OS X) on all views. By default, the [layoutSubviews](https://developer.apple.com/documentation/uikit/uiview/1622482-layoutsubviews) method updates the frame of each subview with the rectangle calculated by the Auto Layout engine. You can override these methods to modify the layout (see [Custom Layouts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrzfvjvona)).

### Batching Changes

It is almost always cleaner and easier to update a constraint immediately after the affecting change has occurred. Deferring these changes to a later method makes the code more complex and harder to understand.

However, there are times when you may want to batch changes for performance reasons. This should only be done when changing the constraints in place is too slow, or when a view is making a number of redundant changes.

To batch a change, instead of making the change directly, call the [setNeedsUpdateConstraints](https://developer.apple.com/documentation/uikit/uiview/1622450-setneedsupdateconstraints) method on the view holding the constraint. Then, override the view’s [updateConstraints](https://developer.apple.com/documentation/uikit/uiview/1622512-updateconstraints) method to modify the affected constraints.

> [!NOTE]
> 

Always call the superclasses implementation as the last step of your [updateConstraints](https://developer.apple.com/documentation/uikit/uiview/1622512-updateconstraints) method’s implementation.

Do not call [setNeedsUpdateConstraints](https://developer.apple.com/documentation/uikit/uiview/1622450-setneedsupdateconstraints) inside your [updateConstraints](https://developer.apple.com/documentation/uikit/uiview/1622512-updateconstraints) method. Calling [setNeedsUpdateConstraints](https://developer.apple.com/documentation/uikit/uiview/1622450-setneedsupdateconstraints) schedules another update pass, creating a feedback loop.

### Custom Layouts

Override the [viewWillLayoutSubviews](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621437-viewwilllayoutsubviews) or [layoutSubviews](https://developer.apple.com/documentation/uikit/uiview/1622482-layoutsubviews) methods to modify the results returned by the layout engine.

> [!IMPORTANT]
> 

When overriding these methods, the layout is in an inconsistent state. Some views have already been laid out. Others have not. You need to be very careful about how you modify the view hierarchy, or you can create feedback loops. The following rules should help you avoid feedback loops:

- You must call the superclass’s implementation somewhere in your method.
- You can safely invalidate the layout of views in your subtree; however, you must do this before you call the superclass’s implementation.
- Don’t invalidate the layout of any views outside your subtree. This could create a feedback loop.
- Don’t call [setNeedsUpdateConstraints](https://developer.apple.com/documentation/uikit/uiview/1622450-setneedsupdateconstraints). You have just completed an update pass. Calling this method creates a feedback loop.
- Don’t call [setNeedsLayout](https://developer.apple.com/documentation/uikit/uiview/1622601-setneedslayout). Calling this method creates a feedback loop.
- Be careful about changing constraints. You don’t want to accidentally invalidate the layout of any views outside your subtree.

[Working with Self-Sizing Table View Cells](WorkingwithSelf-SizingTableViewCells.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrvfvjvomi)

[Visual Format Language](VisualFormatLanguage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrxfvjvomi)
