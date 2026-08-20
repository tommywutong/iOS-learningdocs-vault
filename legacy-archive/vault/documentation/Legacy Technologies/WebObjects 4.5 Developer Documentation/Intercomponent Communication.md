---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/ReusableComponents3.html
archived_at: '2026-07-15T08:06:02.678128Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Creating%20Reusable%20Components.md) [!Previous Section](ReusableComponents2.md)

# Intercomponent Communication

Reusable components can vary widely in scope, from as extensive as an entire HTML page to as limited as a single character or graphic in a page. They can even serve as building blocks for other reusable components. When a reusable component is nested within another component, be it a page or something smaller, the containing component is known as the _parent component_, and the contained component is known as the _child component_. This section examines the interaction between parent and child components.
In the AlertPanel example shown in [Figure 32](ReusableComponents2.md#apple-he4tg), you saw how the parent component, in its declarations file, sets the attributes of the child component:

```
ALERT: AlertPanel {
        alertString = alertTitle;
        alertFontColor = "#A00000";
        alertFontSize = 6;
        infoString = alertDescription;
        infoFontSize = 4;
        infoFontColor = "#500000";
        tableWidth = "50%";
};
```


Each of the AlertPanel component's attributes is set either statically (to a constant value) or dynamically (by binding the attribute's value to a variable or method invocation in the parent's code). Communication from the parent to the child is quite straightforward.
For reusable components to be truly versatile, there must also be a mechanism for the child component to interact with the parent, either by setting the parent's variables or invoking its methods, or both. This mechanism must be flexible enough that a given child component can be reused by various parent components without having to be modified in any way. WebObjects provides just such a mechanism, as illustrated by the following example.
Consider an AlertPanel component like the one described above, but with the added ability to accept user input and relay that input to a parent component. The panel might look like the one in [Figure 33](#apple-g42dq).

!

Figure 33. An Alert Panel That Allows User Input

As in the earlier example, you use this component by simply declaring its position within the HTML page:
_Parent's Template File_

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
_Parent's Declarations File (excerpt)_

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


The __parentAction__ attribute identifies a _callback method_, one that the child component invokes in the parent when the user clicks the Yes or No link. The __exitStatus__ attribute identifies a variable that the parent can check to discover which of the two links was clicked. This attribute passes state information from the child to the parent. A reusable component can have any number of callback and state attributes, and they can have any name you choose.
Now let's look at the revised child component. The template file for the AlertPanel component has to declare the positions of the added Yes and No hyperlinks. (Only excerpts of the implementation files are shown here.)
_Child Component's Template File (excerpt)_

```
<TD>
    <WEBOBJECT name=NOCHOICE></WEBOBJECT>
</TD>
<TD>
    <WEBOBJECT name=YESCHOICE></WEBOBJECT>
</TD>
```


The corresponding declarations file binds these declarations to scripted methods:
_Child Component's Declarations File (excerpt)_

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


And the script file contains the implementations of the __rejectChoice__ and __acceptChoice__ methods:
_Child Component's Script File (excerpt)_

```
id exitStatus;
id parentAction;

- rejectChoice {
    exitStatus = NO;
    return [self performParentAction:parentAction];
}

- acceptChoice {
    exitStatus = YES;
    return [self performParentAction:parentAction];
}
```


Note that __exitStatus__ and __parentAction__ are simply component variables. Depending on the method invoked, __exitStatus__ can have the values YES or NO. The __parentAction__ variable stores the name of the method in the parent component that will be invoked by the child. In this example __parentAction__ identifies the parent method named __"respondToAlert"__, as specified in the parent's declarations file.
__Note:__ You must enclose the name of the parent's action method in quotes.
Now, looking at the __rejectChoice__ and __acceptChoice__ method implementations, you can see that they are identical except for the assignment to __exitStatus__. Note that after a value is assigned to __exitStatus__, the child component sends a message to itself to invoke the parent's action method, causing the parent's __respondToAlert__ method to be invoked. Since the parent's __usersChoice__ variable is bound to the value of the child's __exitStatus__ variable, the parent code can determine which of the two links was clicked and respond accordingly. [Figure 34](#apple-ha3dk) illustrates the connections between the child and parent components.

!

Figure 34. Parent and Child Component Interconnections

The child component's __parentAction__ attribute provides a separation between a user action (such as clicking a hyperlink) within a reusable component and the method it ultimately invokes in the parent. Because of this separation, the same child component can be used by multiple parents, invoking different methods in each of them:
_Parent1's Declarations File (excerpt)_

```
ALERT: AlertPanel {
        ...
        parentAction = "respondToAlert";
        exitStatus = usersChoice;
};
```


_Parent2's Declarations File (excerpt)_

```
ALERT: AlertPanel {
        ...
        parentAction = "okCancel";
        exitStatus = result;
};
```


_Parent3's Declarations File (excerpt)_

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
- Binding an attribute to the value of a variable declared in the parent's code
- Binding an attribute to the return value of a method defined in the parent's code

A child component can communicate actions and values to a parent component by:

- Invoking the parent's callback method
- Setting variables that are bound to variables in the parent, as specified in the parent's declarations file

[!Table of Contents](Creating%20Reusable%20Components.md) [!Next Section](ReusableComponents4.md)
