---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/ConnectingObjectstoCode.html
archived_at: '2026-07-27T06:57:08.011377Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](BuildingforMultipleScreenSizes.md)[Previous](DesigningwithStoryboards.md)

## Connecting Objects to Code

You write the code that implements the behavior of your user interface objects. Your code communicates with user interface objects through action and outlet connections.

Create an _action connection_ when you need to send a message from a control to your code. A _control_ is a user interface object that causes instant actions or visible results when the user manipulates the object. For example, clicking a button sends an action message telling your code to update data. Text fields, sliders, and switches are examples of commonly used controls in iOS; checkboxes, scroll bars, and text fields are commonly used controls in Mac OS.

Create an _outlet connection_ when you need to send a message from your code to a user interface object. The object can be a control or any other object defined in your storyboard or xib file, such as a label, progress indicator, or map view. For example, when your app needs to update the status of a download your code sends a message through an outlet to a progress bar.

The connections are instantiated after the view controller is instantiated but before it has appeared. For more information, see Resource Management in View Controllers and [Target-Action](https://developer.apple.com/library/archive/documentation/General/Devpedia-CocoaApp-MOSX/TargetAction.html#//apple_ref/doc/uid/TP40009448-CH3).

For more help making connections and establishing cocoa bindings, see [Xcode Help](https://help.apple.com/xcode).

> [!NOTE]
>
> As of iOS 8.0, connections are no longer guaranteed to be instantiated after completing the call to `awakeFromNib`.

### Sending Action Messages from a Control to Your Code

Whenever the user activates a control, such as by tapping it, the control should send a message instructing your code to perform some action. The easiest way to configure a control to send an action message to your code is by Control-dragging from the control in Interface Builder to your object’s implementation file.

With Interface Builder open in the standard editor pane, select the control you want to configure, and click the Assistant Editor button (（原归档配图未能恢复：`XC_O_editor_buttons_assistant_2x.png`）) in the workspace toolbar. The assistant editor opens your object’s implementation file.

Control-drag from the control in Interface Builder to the implementation file. (In the screenshot, the assistant editor displays the implementation file of the view controller for the Warrior button.) Xcode indicates where you can insert an action method in your code.

（原归档配图未能恢复：`insert_action_2x.png`）

Release the Control-drag. The assistant editor displays a Connection menu. In this menu, type the name of the action method (`chooseWarrior` in the screenshot below), and click Connect.

（原归档配图未能恢复：`name_the_action_method_2x.png`）

In the implementation file, Xcode inserts a skeletal definition for the new method, as shown below. The `IBAction` return type is a special keyword indicating that this instance method can be connected to your storyboard or xib file. Xcode also configures the control to call the method when the selected event occurs. As a result, the method gets invoked whenever the control receives an action message.

（原归档配图未能恢复：`XC_O_skeletal_action_method_2x.png`）

To this skeletal definition, add the source code that implements the action method. Whereas activation of the control is implemented by the system, you implement the control’s behavior. In the screenshot below, an action method starts a new game when the user clicks the Warrior button.

（原归档配图未能恢复：`implement_action_method_2x.png`）

For detailed step-by-step instructions, see Creating an Action Connection.

### Sending Messages to a User Interface Object Through an Outlet

To enable your code to send messages to a user interface object (telling a label to display a text string, for example, or telling a button to appear or disappear), connect the user interface object to an outlet in your code. The easiest way to make an outlet connection is to Control-click and drag from a user interface object on the canvas to the implementation or header file. For example, to create an outlet in your view controller and connect a button to that outlet, Control-drag from the button in Interface Builder to the view controller’s implementation file in the assistant editor. Xcode indicates where you can insert an outlet declaration in your code.

（原归档配图未能恢复：`insert_outlet_2x.png`）

Release the Control-drag. The assistant editor displays a Connection menu. From this menu, choose Outlet, type the name of the outlet (`warriorButton` in the screenshot below), and click Connect.

（原归档配图未能恢复：`name_the_outlet_2x.png`）

Interface Builder adds the declaration for the outlet to the class. (Outlets are defined as `IBOutlet` properties. The `IBOutlet` keyword tells Xcode that this property can be connected to your storyboard or xib file.)

（原归档配图未能恢复：`property_defined_2x.png`）

For detailed step-by-step instructions, see Creating an Action Connection.

[Designing with Storyboards](DesigningwithStoryboards.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnbtfvjvomi)

[Building for Multiple Screen Sizes](BuildingforMultipleScreenSizes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnbvfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](BuildingforMultipleScreenSizes.md)[Previous](DesigningwithStoryboards.md)
