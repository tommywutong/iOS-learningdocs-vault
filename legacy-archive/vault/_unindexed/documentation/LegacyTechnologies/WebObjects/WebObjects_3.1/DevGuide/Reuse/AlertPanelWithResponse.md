---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Reuse/AlertPanelWithResponse.html
archived_at: '2026-07-15T07:47:14.713279Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Reuse.book.md)
[!Previous Section](Intercom.md)

# Alert Panel Allowing User Input

Consider an AlertPanel component like the one described previously, but with the added ability to accept user input and relay that input to a parent component. The panel might look like this:

!
 ____Figure 1.__  Alert Panel That Allows User Input__

As in the earlier example, you use this component by simply declaring its position within the HTML page:

__Parent's Template File__

---

```
<HTML>
<HEAD>
    <TITLE>Alert</TITLE>
</HEAD>
<BODY>
<WEBOBJECT NAME = "ALERT"></WEBOBJECT>
</BODY>
</HTML>
```

The corresponding declarations file reveals two new attributes (indicated in bold):

__Parent's Declarations File (excerpt)__

---

```
ALERT: AlertPanel {
    infoString = message;
    infoFontSize = 4;
    infoFontColor = "#500000";
    alertString = "New Release";
    alertFontColor = "#A00000";
    alertFontSize = 6;
    tableWidth = "50%";
    parentAction = "respondToAlert";
    exitStatus = usersChoice;
};
```

The __parentAction__ attribute identifies a _callback_ method, one that the child component invokes in the parent when the user clicks the Yes or No link. The __exitStatus__ attribute identifies a variable that the parent can check to discover which of the two links was clicked. This attribute passes state information from the child to the parent. A reusable component can have any number of callback and state attributes , and they can have any name you choose.

Now let's look at the revised child component. The template file for the AlertPanel component has to declare the positions of the added Yes and No hyperlinks. (Only excerpts of the implementation files are shown here.)

__Child Component's Template File (excerpt)__

---

```
  <TD>
    <WEBOBJECT name=NOCHOICE></WEBOBJECT>
  </TD>
  <TD>
    <WEBOBJECT name=YESCHOICE></WEBOBJECT>
  </TD>
```

The corresponding declarations file binds these declarations to scripted methods:

__Child Component's Declarations File (excerpt)__

---

```
NOCHOICE: WOHyperlink {
    action = rejectChoice;
    string = "No";
};
YESCHOICE: WOHyperlink {
    action = acceptChoice;
    string = "Yes";
};
```

And the script file reveals the implementation the __rejectChoice__ and __acceptChoice__ methods:

__Child Component's Script File (excerpt)__

---

```
id exitStatus;
id parentAction;
- rejectChoice
{
    exitStatus = NO;
    return [self performParentAction:parentAction];
}

- acceptChoice
{
    exitStatus = YES;
    return [self performParentAction:parentAction];
}
```

Note that __exitStatus__ and __parentAction__ are simply component variables. Depending on the method invoked, __exitStatus__ can have the values YES or NO. The __parentAction__ variable stores the name of the method in the parent component that will be invoked by the child. In this example __parentAction__ identifies the parent method named __"respondToAlert__", as specified in the parent's declarations file. __Note:__ You must enclose the name of the parent's action method in quotes, as in the example above.

Now, looking at the __rejectChoice__ and __acceptChoice__ method implementations, you can see that they are identical except for the assignment to __exitStatus__. Note that after a value is assigned to __exitStatus__, the child component sends a message to itself to invoke the parent's action method, causing the parent's __respondToAlert__ method to be invoked. Since the parent's __usersChoice__ variable is bound to the value of the child's __exitStatus__ variable (see the parent's declaration file above), the parent script can determine which of the two links was clicked and respond accordingly. The following diagram illustrates the connections between the child and parent components.

!
 ____Figure 2.__  Parent and Child Component Interconnections__

The child component's __parentAction__ attribute provides a separation between a user action (such as a click on a hyperlink) within a reusable component and the method it ultimately invokes in the parent. Because of this separation, the same child component can be used by multiple parents, invoking different methods in each of them:

__Parent1's Declarations File (excerpt)__

---

```
ALERT: AlertPanel {
    ...
    parentAction = "respondToAlert";
    exitStatus = usersChoice;
};
```

__Parent2's Declarations File (excerpt)__

---

```
ALERT: AlertPanel {
    ...
    parentAction = "okCancel";
    exitStatus = result;
};
```

__Parent3's Declarations File (excerpt)__

---

```
ALERT: AlertPanel {
    ...
    parentAction = "alertAction";
    exitStatus = choice;
};
```

In summary, parent and child components communicate in these ways:

A parent component can, in its declarations file, set child component attributes by:

- Assigning constant values
- Binding an attribute to the value of a variable declared in the parent's script file
- Binding an attribute to the return value of a method defined in the parent's script file

A child component can communicate actions and values to a parent component by:

- Invoking the parent's callback method
- Setting variables that are bound to variables in the parent, as specified in the parent's declarations file

[!Table of Contents](Reuse.book.md)
[!Next Section](Synchronize.md)
