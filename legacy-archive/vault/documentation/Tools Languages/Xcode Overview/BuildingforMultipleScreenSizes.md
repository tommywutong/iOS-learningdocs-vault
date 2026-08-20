---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/BuildingforMultipleScreenSizes.html
archived_at: '2026-07-27T06:57:08.022095Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](LookingupObjectDocumentation.md)[Previous](ConnectingObjectstoCode.md)

## Building for Multiple Screen Sizes

iOS and watchOS devices come in multiple screen sizes, and multitasking on iPad with Split View adds even more variations. Design and layout your app for all of these combinations is made easy with three technologies:

- _Stack views_ lay out a collection of views in either a row or column, including other stack views.
- _Size Classes_ let you specify different views or even whole layouts depending on the size category of the vertical and horizontal dimensions of the screen.
- _Auto Layout_ defines relationship _constraints_ between the elements of your user interface that are used to determine the run time sizes.

The combination of these technologies lets you focus on building a user interface instead of writing code to change sizes and orientations.

For information on `UIStackView`, see _[UIStackView Class Reference](https://developer.apple.com/documentation/uikit/uistackview)_.

### Using Size Classes

_Size Classes_ enable you to use one storyboard for all different sizes of screens. You build your interface as it will look on most devices, and then update only the objects that need to change when the available screen size changes.

A size class identifies a relative amount of display space for the height and width. The size can be _compact_ or _regular_ for either height or width. Examples of compact are the width of an iPhone screen in portrait and the height of the screen in landscape. Examples of regular are the height of an iPhone in landscape and both the width and height of an iPad screen. The specific number of points on the screen does not matter, only the relative amount of available space.

Because most of your interface is probably the same for compact or regular, there is an additional size class, _any_. You can lay out most of your interface elements for any width and height, and then lay out any parts of the interface that change for a compact or regular size on either axis.

The size class aware attributes are:

- The constant for a constraint
- A Boolean value indicating whether a constraint is installed in the view hierarchy
- A Boolean value indicating whether a view is installed in the view hierarchy
- The font for a text label, field, text view, or button

Some of the user interface changes enabled by modifying these attributes include:

- Changing the size or position of a view
- Adding or removing views
- Adding or removing sets of constraints
- Changing the font in labels, fields, text views, and buttons

Note that if a view or constraint is not installed in the current size class, it is still allocated. Any reference to that view or constraint returns a valid object. Views will not have a superview. If you uninstall a view, Xcode uninstalls all related constraints.

Enable size classes for your storyboard by selecting the storyboard in the project navigator, showing the File inspector, and selecting the Use Size Classes checkbox. Xcode will ask whether you want to convert the storyboard. Turning on size classes also turns on Auto Layout.

（原归档配图未能恢复：`IB_SizeClassesEnableBefore_2x.png`）

After you enable size classes, Xcode displays all of your top level view controllers on the canvas as squares. There is also a size class control (（原归档配图未能恢复：`IB_SizeClassControl_2x.png`）) at the bottom of the canvas in the center. The control shows the current size class for the width (w) and height (h). In this case, it is any/any.

（原归档配图未能恢复：`IB_SizeClassesEnableAfter_2x.png`）

To change size classes, click the size class control. In the pop-up that appears, move your pointer to the quadrant in the pop-up for the horizontal and vertical size classes you want.

（原归档配图未能恢复：`IB_SizeClassesPicker_2x.png`）

After you choose a new size class, all of the view controllers are resized to reflect the new size class. The bottom bar is shown in blue to remind you that you are no longer editing any/any.

（原归档配图未能恢复：`IB_SizeClassesBlueBar_2x.png`）

Changes you make to constraints, views, and fonts in a specific size class are specific for that class. To uninstall a constraint or view, select the constraint or view and press Command-Delete. When you turn off a view, you usually want to turn off all the constraints attached to that view.

For more help on how to see what is active in a particular size class, and for other ways to work with objects, see [Xcode Help](https://help.apple.com/xcode).

### Using Auto Layout for Automatic Resizing and Positioning

Auto Layout enables your app to adapt to different window sizes, screen sizes, and device orientations. You do this by defining relationship _constraints_ between the elements of your user interface. For example, create a horizontally centered relationship between an image and its container. As the user rotates the iOS device, the image remains horizontally centered in both landscape and portrait orientations of the device.

With Auto Layout constraints governing the layout, the objects in your user interface automatically resize and reposition themselves whenever:

- The user changes the screen orientation of an iOS device
- The user resizes a window in a Mac app
- The iPad enters or leaves Split View mode
- Content dimensions change (for example, when the length of a text string changes in a label or button)

When you Control-drag between two user interface objects, Interface Builder presents you with a list of appropriate constraints. Add constraints to your objects by choosing from this list. The screenshot shows the result of Control-dragging from the main logo image view to the main view of the controller. The pop-up menu shows two constraints between the the image view and its container. "Top Space to Container” is a constraint between the top of the image view and the top of the container. The other horizontally centers the image view in its container.

（原归档配图未能恢复：`AddingConstraint_2x.png`）

To see the constraints for an object, select the object from the outline view in the Interface Builder dock or select the object on the canvas. Constraints are represented by solid blue lines. You can view a list of constraints by selecting the Size inspector (（原归档配图未能恢复：`IB_H_inspector_size_button_2x.png`）).

（原归档配图未能恢复：`IB_Constraints_View_2x.png`）

The top part of the constraints section shows a graphical representation of the types of constraints for the selected object. Each blue horizontal or vertical line indicates that there are one or more constraints of that type. Selecting one or more lines filters the list to constraints that match the selected types.

（原归档配图获取待重试：`IB_Constraints_Filter_2x.png`）

View and edit a constraint in the inspector by selecting the constraint on the canvas or double-clicking the constraint in the Size inspector. You can also double-click a constraint to show a pop-up editor with the most frequently edited attributes.

（原归档配图获取待重试：`IB_Constraints_Edit_2x.png`）

There are more ways to add and edit constraints, including using the buttons along the bottom right of the canvas (（原归档配图获取待重试：`IB_Constraints_Buttons_2x.png`）). For more information on using Auto Layout and constraints, see _[Auto Layout Guide](../../User%20Experience/Auto%20Layout%20Guide/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjt)_ and [Xcode Help](https://help.apple.com/xcode).

[Connecting Objects to Code](ConnectingObjectstoCode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnbufvjvomi)

[Viewing Object Documentation](LookingupObjectDocumentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnbwfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](LookingupObjectDocumentation.md)[Previous](ConnectingObjectstoCode.md)
