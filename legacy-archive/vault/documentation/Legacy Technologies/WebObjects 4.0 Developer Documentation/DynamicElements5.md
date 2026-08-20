---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DynamicElements5.html
archived_at: '2026-07-18T01:26:12.737123Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](The%20Object%20Browser.md)

## Creating Variables and Methods in WebObjects Builder

At the bottom of the object browser, there is a pull-down menu called Edit _sourcefile._ It has three items:

- __Add Variable/Method__ allows you to add a key (an instance variable or a method that returns a value) to your source file.
- __Add Action__ allows you to add the template for an action (a method that takes no parameters and returns a component).
- __View Source File__ opens the source file in a Project Builder window.

When you choose Add Variable/Method, the following panel opens:
!
In this panel, you specify:

- The name of the key.
- Its type.

You can choose the type from the pop-up list or type it in directly. You can also use the radio buttons to specify whether the variable is an array.

- How the key is implemented.

The key can be an instance variable whose value is accessed directly, or a method that returns a value (not necessarily associated with an instance variable). You can also create a method that sets the value of an instance variable.

When you click Add, the key's name appears in the object browser (below __application__ and __session__). To see what was added to your source code, choose View Source File from the pop-up menu in the object browser. You'll see something like the following:

!

When you choose Add Action, the following panel appears:

!

When you click Add, the following code is added to your source file:

```
public ThatPage myAction()
{
    ThatPage nextPage = (ThatPage)pageWithName("ThatPage");

    // Initialize your component here

    return nextPage;
}
```


WebObjects Builder provides these ways to add variables and methods for your convenience. Of course, you can add variables and methods directly to your component's code by editing them in Project Builder.
The Add Variable/Method and Add Action menu items apply to the code file that appears in the menu's title, as in "Edit Main.java.". To add variables and methods to the application or session code files, select __application__ or __session__ in the object browser first. Notice that the pull-down menu title changes accordingly. Then choose Add Variable/Method or Add Action from the pull-down menu. Deselect the keys in the object browser to return to the main component (On Mac OS X Server, command-click to deselect, and on Windows NT control-click).
To delete a key or action, you must delete it from the source code in Project Builder.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DynamicElements6-2.md)
