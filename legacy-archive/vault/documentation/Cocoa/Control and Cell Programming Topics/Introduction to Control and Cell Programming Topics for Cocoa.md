---
title: Control and Cell Programming Topics
apple_id: 10000015i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/ControlCell.html
archived_at: '2026-07-15T07:13:45.869176Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Cells%20and%20Controls.md)

# Introduction to Control and Cell Programming Topics for Cocoa

Controls and cells implement user-interface objects, like buttons, text fields, and sliders.

This topic contains these subtopics:

|  |  |
| --- | --- |
| _[Button Programming Topics](../Button%20Programming%20Topics/Introduction%20to%20Buttons.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayts2i)_ | A user interface object that sends an action message to a target when clicked. |
| _[Image View Programming Topics](../Image%20View%20Programming%20Topics/Introduction%20to%20Image%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3te2i)_ | A user interface object that displays a single image in a frame, and optionally allow a user to drag an image to it. |
| _[Slider Programming Topics](../Slider%20Programming%20Topics/Introduction%20to%20Sliders.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazdk2i)_ | A user interface object that displays a range of values and has an indicator, or knob, which indicates the current setting. |
| _Text Fields_ | A user interface object that displays text that the user can select or edit. |
| _[Box Programming Topics](../Box%20Programming%20Topics/Introduction%20to%20Boxes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayto2i)_ | A user interface object that can draw a border around itself and title itself. |
| _[Progress Indicator Programming Topics](../Progress%20Indicator%20Programming%20Topics/Introduction%20to%20Progress%20Indicators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazdi2i)_ | A user interface object that shows that a lengthy task is under way. |
| _[Status Bar Programming Topics](../Status%20Bar%20Programming%20Topics/Introduction%20to%20Status%20Bars.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3tg2i)_ | A user interface object that displays a collection of items that provide interaction with or feedback to the user. |
| _[Browser Programming Topics](../Browser%20Programming%20Topics/Introduction%20to%20Browsers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytq2i)_ | Provides a user interface for displaying and selecting items from a list of data or from hierarchically organized lists of data, such as directory paths. |
| _[Matrix Programming Guide](../Matrix%20Programming%20Guide/Introduction%20to%20Matrices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazde2i)_ | A user interface object used for creating groups of cells that work together in various ways. |
| _[Form Programming Topics](../Form%20Programming%20Topics/Introduction%20to%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazdc2i)_ | A group of related text fields. |
| _[Combo Box Programming Topics](../Combo%20Box%20Programming%20Topics/Introduction%20to%20Combo%20Boxes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazda2i)_ | A user interface object that gives the user two ways to enter a value: entering it directly in a text field, or choosing it from a pop-up list of pre-selected values. |
| _[Table View Programming Guide for Mac](../Table%20View%20Programming%20Guide%20for%20Mac/About%20Table%20Views%20in%20OS%20X%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazdm2i)_ | A user interface object that displays data for a set of related records, with rows representing individual records and columns representing the attributes of those records. |
| _[Tab View Programming Topics](../Tab%20View%20Programming%20Topics/Introduction%20to%20Tab%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3ti2i)_ | A user interface object providing a convenient way to provide information in multiple pages. |
| _[Outline View Programming Topics](../Outline%20View%20Programming%20Topics/Introduction%20to%20Outline%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazdg2i)_ | A type of table which lets the user expand or collapse rows containing hierarchical data. |
| _Text Views_ | Text views are the main user interface objects of the Cocoa text system. |
| _[Stepper Programming Topics](../Stepper%20Programming%20Topics/Introduction%20to%20Steppers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydq2i)_ | A user interface object consisting of two small arrows that can increment and decrement a value that appears beside it, such as a date or time. |
| _[Search Fields](../Search%20Fields/Introduction%20to%20Search%20Fields.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dq2i)_ | A user interface object that provides a standard user interface for searching. |
| _[Segmented Control Programming Guide](../Segmented%20Control%20Programming%20Guide/Introduction%20to%20Segmented%20Controls.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4de2i)_ | A user interface object that has the appearance and behavior of a horizontal button divided into multiple segments. |

Controls and cells implement user-interface objects, like buttons, text fields, and sliders. The control is responsible for

- Displaying itself
- Intercepting user events (such as a clicking a button or moving a slider)
- Sending actions to other objects, usually in response to a user event (such as changing a variable’s value as a slider moves or performing a command when a button is pressed.)

A control usually delegates the first two responsibilities to cells. Splitting these responsibilities off makes it easier to create a control with many identical elements (like a spreadsheet table) or with a few different elements (like a pull-down list that lets you enter a string either in a text field or from a menu of pre-elected strings).

Here are the concepts:

- [About Cells and Controls](About%20Cells%20and%20Controls.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ztclkcijbukqkdivaq) gives basic information on what the NSCell and NSControl classes do.
- [How Controls and Cells Interact](How%20Controls%20and%20Cells%20Interact.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga3dqlkcijbuer2fizba) gives more information on how controls and cells interact and how they operate.
- [Cell States](Cell%20States.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga3dslkcijbukqkdivaq) describes the three states a control can have: on, off, or mixed. Although used primarily by NSButton, states are defined in NSCell so future subclasses can use them.
- [Represented Objects](Represented%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga3dolkcineuercdjfeq) explains how to associate a cell with the object it represents.

Here are the tasks:

- "[Manipulating Cells and Controls](Manipulating%20Cells%20and%20Controls.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmzyfvjvomq)" discusses various tips and techniques for dealing with cells and controls.
- [Changing the Cell for a Control](Changing%20the%20Cell%20for%20a%20Control.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga3telkcineuersbjbea) describes how to change the NSCell subclass that a control uses.
- [Displaying Cell Values](Displaying%20Cell%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga3tclkcijbukqkgincq) describes how some cells format and display their values as strings.
- [Validating Control Entries](Validating%20Control%20Entries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga3talkcineueskkivfa) describes how to validate the contents of some cells, especially cells in a matrix or text field.
- [Using a Continuous Control](Using%20a%20Continuous%20Control.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgi2talkcineuissdi5cq) describes how to set up a control so it sends its action message repeatedly while being pressed.
- [Subclassing NSCell](Subclassing%20NSCell.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4zdqlkcineuersbjbea) and [Subclassing NSControl](Subclassing%20NSControl.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ztalkcineuissdi5cq) describe how to create custom subclasses of NSCell and NSControl.
- [Using the System Control Tint](Using%20the%20System%20Control%20Tint.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge4dalkcineuersbjbea) describes how to use the system-wide control tint in your custom views and control cells.

[Next](About%20Cells%20and%20Controls.md)

