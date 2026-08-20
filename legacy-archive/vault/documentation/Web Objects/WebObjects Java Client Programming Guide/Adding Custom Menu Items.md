---
title: WebObjects Java Client Programming Guide
apple_id: TP30001017
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-08-11'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/DesktopApplications/T4CustomMenuItems/T4CustomMenuItems.html
archived_at: '2026-07-18T02:19:04.389692Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Java Client Programming Guide](Introduction%20to%20WebObjects%20Java%20Client%20Programming%20Guide.md)


[Next](Adding%20Custom%20Actions%20to%20Controllers.md)[Previous](Generating%20Controllers%20With%20the%20Controller%20Factory.md)

# Adding Custom Menu Items

There are many ways to add custom menu items to a Direct to Java Client application. This chapter describes the most common mechanisms.Para

Before learning how to add actions to your application, you should understand the different kinds of actions in Direct to Java Client applications. If you consult [Controllers and Actions Reference](Controllers%20and%20Actions%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzsgmwviubr), you’ll find a number of types of available actions. Whereas the appendix simply lists the XML tags and attributes of each action, this section describes the differences between each type of action and what each attribute represents.

**`APPLICATIONACTION`**
: These actions are added to the menu specified by the `descriptionPath` parameter. They invoke a method in the application object specified by the `actionName` parameter.

**`CONTROLLERHIERARCHYACTION`**
: These actions are added to the menu specified by the `descriptionPath` parameter. They invoke a method in the controller hierarchy specified by the `actionName` parameter. This means that the menu items for these types of actions are available only if the action method is defined in the controller hierarchy whose top level controller is active in the application.

**`HELPWINDOWACTION`**
: These actions are added to the Help menu. They invoke rule system tasks specified by the `task` parameter.

**`TOOLWINDOWACTION`**
: These actions are added to the Tools menu. They invoke rule system tasks specified by the `task` parameter.

**`WINDOWACTION`**
: These actions are added to the menu specified by the `descriptionPath` parameter. They invoke rule system tasks specified by the `task` parameter.

The default actions in a Direct to Java Client application are defined in the `com.webobjects.eoapplication` package. As described in [Restricting Access to an Application](Restricting%20Access%20to%20an%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqhawviubr), you can take control of the actions in menus by overriding the `actions` key in the rule system.

You write a rule whose right-hand side key is `actions` and right-hand side value is the name of a D2WComponent in the application that specifies the custom actions.

The following sections describe how to add the different types of actions to your application. Since they all require a D2WComponent, the task for adding one to an application is given first.

_Problem:_ You want to add a D2WComponent to your project to hold custom actions (or for other customization purposes).

_Solution:_ Add a WOComponent to your project and make it a D2WComponent.

The first step in adding custom actions is to create a new D2WComponent in which to define them. In a Direct to Java Client project, add a new WebObjects component to the Application Server target. Call it UserActions. This creates a new component of type `com.webobjects.appserver.WOComponent`. However, you need a D2WComponent, so add an import statement for the `com.webobjects.directtoweb` package and change the superclass of UserActions to D2WComponent, as shown in [Listing 13-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgawuer2civbuirkj).

__Listing 13-1__  Changing the superclass of UserActions

```
import com.webobjects.appserver.*;
import com.webobjects.foundation.*;
import com.webobjects.directtoweb.*; // add this

public class UserActions extends D2WComponent { //change superclass to this

    public UserActions(WOContext context) {
        super(context);
    }
}
```

Now you can add actions to this component to provide custom menu items to your application as described in the following sections.

_Problem:_ You want to add a new menu item that is always available in the client application. The menu item invokes an action method.

_Solution:_ Use `APPLICATIONACTION`.

Suppose your application has a main window that provides access to the application’s primary functions. It’s conceivable that this window might become hidden underneath other windows as users use the application. So, you can provide a custom menu item that brings this window forward.

You specify the method an `APPLICATIONACTION` object invokes with the `actionName` parameter. The rule system looks for the method in subclasses of the client’s principal class, EODynamicApplication (direct project types) or EOApplication (nondirect project types). If the method cannot be found, the menu item is still displayed but it is disabled (grayed out).

In the HTML file of the D2WComponent that contains your application’s custom menu items (`UserActions.html` in the UserActions component created with the steps described in [New D2WComponent](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgawugrkhivceussi)), the XML description for an `APPLICATIONACTION` object that invokes a method called `bringForwardMainWindow` looks like this:

```
<APPLICATIONACTION actionName="bringForwardMainWindow" menuAccelerator="shift B" descriptionPath="Window/Main Window"/>
```

This description specifies a custom action that is displayed in the Window menu as the menu item Main Window with the keyboard equivalent Shift-B. It invokes a method called `bringForwardMainWindow` on the client application’s principal class. `APPLICATIONACTION` XML descriptions can include other parameters. The possible parameters for XML descriptions of actions are listed in [EOActions XML Descriptions](Controllers%20and%20Actions%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzsgmwviucykjcummjqge).

_Problem:_ You want to add a new menu item that is always available in the client application and that invokes a task defined in the rule system. The menu item appears in either the Help menu or the Tools menu.

_Solution:_ Use `HELPWINDOWACTION` or `TOOLWINDOWACTION`.

Suppose your application includes a frozen XML component containing help for the application. The HTML file of the D2WComponent containing your custom rules would include this XML description:

```
<HELPWINDOWACTION task="help" menuAccelerator="shift T" descriptionPath="Window/Main Window"/>
```

If the frozen XML component containing the help file is named HelpWindow, the rule to load it is as follows:

**Left-Hand Side:**
: `(task='help')`

**Key:**
: `window`

**Value:**
: `"HelpWindow"`

**Priority:**
: `50`

This defines a new task that opens the frozen XML component specified in the right-hand side value.

To add a menu item to the Tools menu, follow the steps for adding an item to the Help menu, changing `HELPWINDOWACTION` to `TOOLWINDOWACTION` in the XML description.

_Problem:_ You want to add a new menu item that is available only in the client application for a particular controller hierarchy. The menu item invokes an action in a particular controller hierarchy.

_Solution:_ Use a `CONTROLLERHIERARCHYACTION`.

Sometimes you want a menu item to be available only while a particular task or user interface component is active. For example, in [Enhancing the Application](Enhancing%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgmwviubr), a custom action is added to the application to send a report of a student’s information. In the tutorial, the custom action is added only to form windows for the Student entity, but this would also be a good action to add as a menu item.

However, this menu item should be available only if a student record is in the frontmost window. So `CONTROLLERHIERARCHYACTION` is the appropriate type of action. These actions are enabled only if the action method is in a class that is part of the controller hierarchy represented in the frontmost window of an application.The HTML file of the D2WComponent containing your custom rules would include this XML description:

```
<CONTROLLERHIERARCHYACTION actionName="activateMainWindow" menuAccelerator="shift A" descriptionPath="Window/Main Window"/>
```

This invokes a method called `activateMainWindow` in a class that is part of the frontmost controller hierarchy.

[Next](Adding%20Custom%20Actions%20to%20Controllers.md)[Previous](Generating%20Controllers%20With%20the%20Controller%20Factory.md)

