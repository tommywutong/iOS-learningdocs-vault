---
title: Auto Layout Guide
apple_id: TP40010853
resource_type: Guide
platform: tvOS|iOS|macOS
topic: User Experience
technology: AppKit
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/ProgrammaticallyCreatingConstraints.html
archived_at: '2026-07-18T02:10:21.535645Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Auto Layout Guide](index.md)



## Programmatically Creating Constraints

Whenever possible, use Interface Builder to set your constraints. Interface Builder provides a wide range of tools to visualize, edit, manage, and debug your constraints. By analyzing your constraints, it also reveals many common errors at design time, letting you find and fix problems before your app even runs.

Interface Builder can manage an ever-growing number of tasks. You can build almost any type of constraint directly in Interface Builder (see [Working with Constraints in Interface Builder](WorkingwithConstraintsinInterfaceBuidler.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmjqfvjvomi)). You can also specify size-class-specific constraints (see [Debugging Auto Layout](TypesofErrors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrsfvjvomi)), and with new tools like stack views, you can even dynamically add or remove views at runtime (see [Dynamic Stack View](LayoutUsingStackViews.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmjrfvjvomjz)). However, some dynamic changes to your view hierarchy can still be managed only in code.

You have three choices when it comes to programmatically creating constraints: You can use layout anchors, you can use the [NSLayoutConstraint](https://developer.apple.com/documentation/uikit/nslayoutconstraint) class, or you can use the Visual Format Language.

### Layout Anchors

The [NSLayoutAnchor](https://developer.apple.com/documentation/appkit/nslayoutanchor) class provides a fluent interface for creating constraints. To use this API, access the anchor properties on the items you want to constrain. For example, the view controller’s top and bottom layout guides have `topAnchor`, `bottomAnchor`, and `heightAnchor` properties. Views, on the other hand, expose anchors for their edges, centers, size, and baselines.

> [!NOTE]
> 

Layout anchors let you create constraints in an easy-to-read, compact format. They expose a number of methods for creating different types of constraints, as shown in Listing 13-1.

__Listing 13-1__Creating layout anchors

1. `// Get the superview's layout`
2. `let margins = view.layoutMarginsGuide`
4. `// Pin the leading edge of myView to the margin's leading edge`
5. `myView.leadingAnchor.constraint(equalTo: margins.leadingAnchor).isActive = true`
7. `// Pin the trailing edge of myView to the margin's trailing edge`
8. `myView.trailingAnchor.constraint(equalTo: margins.trailingAnchor).isActive = true`
10. `// Give myView a 1:2 aspect ratio`
11. `myView.heightAnchor.constraint(equalTo: myView.widthAnchor, multiplier: 2.0).isActive = true`

As described in [Anatomy of a Constraint](AnatomyofaConstraint.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqojnknltc), a constraint is simply a linear equation.

![image: ../Art/view_formula.pdf](attachments/Art/view_formula_2x.png)

The layout anchors have several different methods for creating constraints. Each method includes parameters only for the elements of the equation that affect the results. So in the following line of code:

1. `myView.leadingAnchor.constraint(equalTo: margins.leadingAnchor).isActive = true`

the symbols correspond to the following parts of the equation:

| Equation | Symbol |
| --- | --- |
| Item 1 | myView |
| Attribute 1 | leadingAnchor |
| Relationship | constraintEqualToAnchor |
| Multiplier | None (defaults to 1.0) |
| Item 2 | margins |
| Attribute 2 | leadingAnchor |
| Constant | None (defaults to 0.0) |

The layout anchors also provides additional type safety. The `NSLayoutAnchor` class has a number of subclasses that add type information and subclass-specific methods for creating constraints. This helps prevent the accidental creation of invalid constraints. For example, you can constrain horizontal anchors ([leadingAnchor](https://developer.apple.com/documentation/uikit/uiview/1622520-leadinganchor) or [trailingAnchor](https://developer.apple.com/documentation/uikit/uiview/1622522-trailinganchor)) only with other horizontal anchors. Similarly, you can provide multipliers only for size constraints.

> [!NOTE]
> 

For more information, see _[NSLayoutAnchor Class Reference](https://developer.apple.com/documentation/appkit/nslayoutanchor)_.

### NSLayoutConstraint Class

You can also create constraints directly using the [NSLayoutConstraint](https://developer.apple.com/documentation/uikit/nslayoutconstraint) class’s [constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526954-init) convenience method. This method explicitly converts the constraint equation into code. Each parameter corresponds to a part of the equation (see [The constraint equation](AnatomyofaConstraint.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqojnknlte)).

Unlike the approach taken by the layout anchor API, you must specify a value for each parameter, even if it doesn’t affect the layout. The end result is a considerable amount of boilerplate code, which is usually harder to read. For example, the code in [Listing 13-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmjwfvjvona) code is functionally identical to the code in [Listing 13-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmjwfvjvomy).

__Listing 13-2__Directly Instantiating Constraints

1. `NSLayoutConstraint(item: myView, attribute: .leading, relatedBy: .equal, toItem: view, attribute: .leadingMargin, multiplier: 1.0, constant: 0.0).isActive = true`
3. `NSLayoutConstraint(item: myView, attribute: .trailing, relatedBy: .equal, toItem: view, attribute: .trailingMargin, multiplier: 1.0, constant: 0.0).isActive = true`
5. `NSLayoutConstraint(item: myView, attribute: .height, relatedBy: .equal, toItem: myView, attribute:.width, multiplier: 2.0, constant:0.0).isActive = true`

> [!NOTE]
> 

Unlike the layout anchor API, the convenience method does not highlight the important features of a particular constraint. As a result, it is easier to miss important details when scanning over the code. Additionally, the compiler does not perform any static analysis of the constraint. You can freely create invalid constraints. These constraints then throw an exception at runtime. Therefore, unless you need to support iOS 8 or OS X v10.10 or earlier, consider migrating your code to the newer layout anchor API.

For more information, see _[NSLayoutConstraint Class Reference](https://developer.apple.com/documentation/uikit/nslayoutconstraint)_.

### Visual Format Language

The Visual Format Language lets you use ASCII-art like strings to define your constraints. This provides a visually descriptive representation of the constraints. The Visual Formatting Language has the following advantages and disadvantages:

- Auto Layout prints constraints to the console using the visual format language; for this reason, the debugging messages look very similar to the code used to create the constraints.
- The visual format language lets you create multiple constraints at once, using a very compact expression.
- The visual format language lets you create only valid constraints.
- The notation emphasizes good visualization over completeness. Therefore some constraints (for example, aspect ratios) cannot be created using the visual format language.
- The compiler does not validate the strings in any way. You can discover mistakes through runtime testing only.

In [Listing 13-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmjwfvjvomy), the example has been rewritten using the Visual Format Language:

__Listing 13-3__Creating constraints with the Visual Format Language

1. `let views = ["myView" : myView]`
2. `let formatString = "|-[myView]-|"`
4. `let constraints = NSLayoutConstraint.constraints(withVisualFormat: formatString, options: .alignAllTop, metrics: nil, views: views)`
6. `NSLayoutConstraint.activate(constraints)`

This example creates and activates both the leading and trailing constraints. The visual format language always creates 0-point constraints to the superview’s margins when using the default spacing, so these constraints are identical to the earlier examples. However, [Listing 13-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmjwfvjvomjq) cannot create the aspect ratio constraint.

If you create a more complex view with multiple items on a line, the Visual Format Language specifies both the vertical alignment and the horizontal spacing. As written, the “Align All Top” option does not affect the layout, because the example has only one view (not counting the superview).

To create constraints using the visual format language:

1. Create the `views` dictionary. This dictionary must have strings for the keys and view objects (or other items that can be constrained in Auto Layout, like layout guides) as the values. Use the keys to identify the views in the format string.

   > [!NOTE]
   > 
2. (Optional) Create the `metrics` dictionary. This dictionary must have strings for the keys, and [NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber) objects for the values. Use the keys to represent the constant values in the format string.
3. Create the format string by laying out a single row or column of items.
4. Call the [NSLayoutConstraint](https://developer.apple.com/documentation/uikit/nslayoutconstraint) class’s [constraintsWithVisualFormat:options:metrics:views:](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526944-constraints) method. This method returns an array containing all the constraints.
5. Activate the constraints by calling the `NSLayoutConstraint` class’s [activateConstraints:](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526955-activate) method.

For more information, see the [Visual Format Language](VisualFormatLanguage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrxfvjvomi) appendix.

[Debugging Tricks and Tips](DebuggingTricksandTips.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrrfvjvomi)

[Size-Class-Specific Layout](Size-ClassSpecificLayout.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrwfvjvomi)
