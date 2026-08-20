---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/ClientSideComponents/Applets/Introduction.html
archived_at: '2026-07-15T07:49:27.855101Z'
---
> 导航：[总目录](../../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](CSControls.mif.book.md)
[!Previous Section](CSControls.mif.book.md)

# Introduction

The applets provided by NeXT "wrap" certain graphical user-interface classes in __java.awt.\*__. They also implement the code necessary to interact with an instance of the SimpleAssociation class and thus "push" and "pull" values between the server and the client sides of an application.

A WOApplet dynamic element represents each of these applets on the server side of a WebObjects application. You must initialize this element with the location of the applet's ".class" file, the applet's dimensions, and its association class. You may also initialize any applet-specific key or action. The following is a sample set of assignments made in a declarations (".wod") file:

```
PASSWORD : WOApplet {
    code = "next.wo.client.controls.TextFieldApplet.class";
    codebase = "/WebObjects/Java";
    width = "200";
    height = "20";
    associationClass = "next.wo.client.SimpleAssociation";
    stringValue = nameString;
    echoCharacter = "*";
    action = "validateUser";
    enabled = isNotValidated; // superclass key (AWTApplet)
};
```

In this case, the __stringValue__ and __echoCharacter__ attributes are the keys and __action__ is the action of TextFieldApplet. The variable "nameString" is probably declared in the component in which this dynamic element appears whereas "validateUser" is a method of the component that is invoked when the user presses Return in this text field. (Note that methods should be quoted.) The __echoCharacter__ attribute is assigned a string constant.

Notice, however the __enabled__ attribute. This key is not defined by TextFieldApplet, but by its superclass, AWTApplet, which is also the superclass for all NeXT-provided applets. Through inheritance, these derived applets accept values for the keys defined by AWTApplet.

A WebObjects application downloads initial values to the applets after they're created in the browser. These initial values include constants specified in the ".wod" file and values of variables initialized in the component's __init__ methods. Thereafter the values of applet keys are synchronized twice with the variables they are bound to in the WOApplet declaration, once before the triggering of an action method in the server and once again after the method returns __nil__.

## Superclass Attributes

AWTApplet is the base class for the applet controls provided with WebObjects. AWTApplet has keys for common applet attributes: enabled status, foreground color, and background color. The effect of these keys depends on particular applets and particular browsers. For example, no foreground or background colors for a ButtonApplet (other than gray) are allowed. Some browsers do not support certain colors.

**__enabled__**
: If __enabled__ evaluates to "NO", the applet appears in the page but is not active. The disabled state is manifest differently for each control. For example, a TextFieldApplet will not accept the insertion of a cursor. A disabled button has a grayed-out title and doesn't react to clicks. The default setting is "YES".

**__foregroundColor__**
: The color of the applet foreground. The foreground of an applet depends upon the type of object. The TextFieldApplet, for example, displays typed text in the foreground color. You must specify colors as a string. The string is either the name of a color (see "[Color Names](#apple-kjcumnjxheytc)," below) or it may contain six hexadecimal digits to be interpreted in pairs as RGB values. Colors specified as hexadecimal values may start with the "#" character (although this is not required).

**__backgroundColor__**
: The color of the applet background. The background of an applet depends upon the type of object. The TextFieldApplet, for example, displays the area behind typed text in the background color. You must specify colors as a string. The string is either the name of a color (see "[Color Names](#apple-kjcumnjxheytc)," below) or it may contain six hexadecimal digits to be interpreted in pairs as RGB values. Colors specified as hexadecimal values may start with the "#" character (although this is not required).

### Color Names

The following color names, defined as static class variables by __java.awt.Color__, are acceptable as string values for the __foregroundColor__ and __backgroundColor__ keys:

|  |  |  |  |
| --- | --- | --- | --- |
| black | blue | cyan | darkGray |
| gray | green | lightGray | magenta |
| orange | pink | red | white |
| yellow |

## A Note on Declaration Synopses

The synopses in this section include the keys and values specific to each applet as well as the specific package name for each applet class file. Ellipses suggest that the other assignments are necessary or possible (__codebase__ or superclass keys, for instance). See the section on [standard WOApplet assignments](../../../DevGuide/ClientSide/Integrating3.md), such as __codebase__ and __associationClass__, in the "Java Client-Side Components" chapter of the _WebObjects Developer's Guide_.

[!Table of Contents](CSControls.mif.book.md)
[!Next Section](ButtonApplet.md)
