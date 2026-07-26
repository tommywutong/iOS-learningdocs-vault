---
title: 10 Things You Need to Know About Cocoa Auto Layout
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/03/things-you-need-to-know-about-cocoa-autolayout/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:afba1f459ec6fd5d'
translated: false
---

> 原文：[10 Things You Need to Know About Cocoa Auto Layout](https://oleb.net/blog/2013/03/things-you-need-to-know-about-cocoa-autolayout/)　·　Ole Begemann

# 10 Things You Need to Know About Cocoa Auto Layout

Working with [Cocoa Auto Layout](https://developer.apple.com/library/ios/#documentation/UserExperience/Conceptual/AutolayoutPG/Articles/Introduction.html) for the first time is very different from the springs and struts model Cocoa developers have known for more than a decade. Despite the complexity of Auto Layout, I have found that you need to understand just a few basic rules to make the concept click. This article is an attempt to list those rules.

# General Auto Layout Concepts

## 1. Rule of Thumb: At Least Two Constraints in Each Dimension

In each dimension (vertical and horizontal), each view’s position and size is defined by three values: leading space, size and trailing space.[1](#fn:1) The leading and trailing spaces can be defined either in terms of a view’s superview or in relation to a sibling in the view hierarchy. Generally speaking, your layout constraints must fix two of these values so that the third one can be calculated. As a result, a standard view needs at least two constraints in each dimension for an unambiguous layout.

## 2. Embrace Intrinsic Size

Some controls, such as labels and buttons, have a so-called intrinsic size. Depending on the control, intrinsic sizes can be valid either horizontally or vertically or in both dimensions. In the absence of explicit width and height constraints, a control’s intrinsic size functions as an implicit constraint. This allows you to create unambiguous layouts with only one explicit constraint per dimension (as opposed to the general rule above) and let the controls resize themselves automatically based on their content. This is the key for creating a layout that looks best in every localization.

# Auto Layout in Interface Builder

**Update March 3, 2014:** When I wrote this, Xcode 4.x was the current version. Meanwhile, Xcode 5 has significantly changed how Auto Layout is handled in Interface Builder, so much of the following is no longer true (especially items 3 and 4). Xcode now allows you to create ambiguous layouts in Interface Builder and will add missing constraints at build time to make a layout unambiguous. This makes prototyping and quick changes during development much easier. Items 5 and 6 still apply to Xcode 5, too, though.

The Auto Layout editor in Interface Builder seems to have a mind of its own. An understanding of why the Xcode engineers designed it this way will make working with it much less frustrating.

![The Delete menu item for a layout constraint in Interface Builder is grayed out](https://oleb.net/media/interface-builder-constraints-editor-context-menu.png)

<sub>IB won't let you delete a constraint if that would lead to an ambiguous layout.</sub>

## 3. IB Will Never Let You Create Ambiguous Layouts

IB’s primary goal is to protect you from yourself. It will never let you create an ambiguous layout. That means that IB automatically creates constraints for you as soon as you place a view in a layout. Try placing your views along IB’s automatic guides to help it guess correctly which layout you want.

## 4. Before You Can Delete An Existing Constraint, You Must Create Another One

Use the Size Inspector to see a list of all constraints for a particular view. When the Delete menu item for a constraint is grayed out, this is IB’s way of telling you that deleting this constraint would create an ambiguous layout and is hence not allowed. You need to create at least one more custom constraint before you can delete this one.

![Interface Builder's UI for creating new layout constraints](https://oleb.net/media/interface-builder-create-constraints-ui.png)

<sub>IB's UI for creating new layout constraints.</sub>

To create a new constraint, select one or more views in your layout and use the three inconspicuous buttons in the bottom right corner of the canvas. These are easy to overlook.

## 5. Don’t Resize Controls Explicitly

Try not to set a control’s size explicitly. As long as you don’t resize them manually, most controls will resize themselves to fit their content and use this intrinsic size to create a perfect, content-sensitive layout. This is especially important for UIs that get localized. Once you (by accident or on purpose) manually resize a control, IB creates an explicit size constraint that is hard to get rid of. To return to intrinsic sizing, use the Editor \> Size to Fit Content command.

## 6. Avoid Premature Optimization

Unfortunately, using Auto Layout with Interface Builder forces you to be careful. For instance, if you find that you need to replace one control with another, deleting the original from your layout can lead IB to automatically create a bunch of new constraints that you then need to modify manually (again) once you have inserted the replacement control. It is probably not a good idea to constantly try to optimize your constraints while your layout is still in a state of flux. Better to do it at a later stage when it is more stable.

# Auto Layout in Code

Working with Auto Layout in Interface Builder can quickly lead to frustration, which is why more and more developers ([Brent Simmons is one example](http://inessential.com/2013/03/06/how_much_or_how_little_i_use_interface)) prefer to write their layouts in code.

## 7. Forget frame

Forget that the `frame` property exists. Never set it directly. A view’s frame is the result of the Auto Layout process, not an input variable. To change the frame, change the constraints. This forces you to change the way you think about your UI. Rather than thinking in positions and sizes, think of the rules that specify a each view’s positioning in relation to its siblings and parents. It’s not unlike CSS.

## 8. Don’t Forget To Disable Autoresizing Masks

For backwards compatibility of your code, the springs and struts model is still the default. For every programmatically created view that you want to use Auto Layout with, call `setTranslatesAutoresizingMaskIntoConstraints:NO`.

## 9. The Debugger Console Is Your Friend

When writing your constraints, keep an eye on the debugger console. I found that the error messages Apple logs for ambiguous or unsatisfiable layouts usually help you pin down the problem very quickly. [Apple’s debugging tips in the Cocoa Auto Layout Guide](https://developer.apple.com/library/ios/documentation/userexperience/conceptual/AutolayoutPG/ResolvingIssues/ResolvingIssues.html#//apple_ref/doc/uid/TP40010853-CH17-SW14) are a great start.

## 10. Animate the Constraints, Not the Frame

Animations also require rethinking under Auto Layout. You cannot simply animate a view’s frame anymore; if you do, the view will snap back to its Auto Layout-calculated position and size as soon as the animation finishes. Instead, you need to animate the layout constraints directly. To do so, either modify the existing constraints (you can create `IBOutlet`s for constraints created in IB) or add new ones, then send `layoutIfNeeded` to your view from within an animation block.

1. In the vertical dimension, leading and trailing spaces are the top and bottom spaces, respectively. In the horizontal dimension, you can choose between two directions: “Leading to Trailing” or “Left to Right”. The difference becomes relevant if your UI is displayed in a right-to-left language. Layout constraints in the “Leading to Trailing” direction now go from right to left (i.e., your layout gets mirrored) while “Left to Right” constraints keep their orientation regardless of the writing direction. In most cases, “Leading to Trailing” is what you want. [↩︎](#fnref:1)
