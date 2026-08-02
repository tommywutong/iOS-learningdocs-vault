---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.43.html
archived_at: '2026-07-15T08:10:37.116816Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](The%20Object%20Browser.md) [!](The%20Object%20Browser.md) [!](Working%20with%20Application%20and%20Session%20Variables.md)

---

#   Working with Keys in WebObjects Builder

At the bottom of the object browser, there is a pull-down list called Edit Source File_._
It has five items:

- 

  __Add Key__
  allows you to add a key (an instance variable or a method that returns a value) to your source file.
- 

  __Add Action__
  allows you to add the template for an action (a method that takes no parameters and returns a component).
- 

  __Delete Key__
  deletes a key from your source file by deleting its instance variable and accessor methods.
- 

  __Rename Key__
  renames a key in your source file by renaming its instance variable and accessor methods.
- 

  __View Source File__
  opens the source file in a Project Builder window.

When you choose Add Key, the following panel opens:
!

In this panel, you specify:

- 

  The name of the key.
- 

  Its type.

  You can choose the type from the combo box or type it in directly. You can also use the radio buttons to specify whether the variable is an array.
- 

  How the key is implemented.

  The key can be an instance variable whose value is accessed directly, or a method that returns a value (not necessarily associated with an instance variable). You can also create a method that sets the value of an instance variable.

When you click Add, the key's name appears in the object browser (below __application__
and __session__
). To see what was added to your source code, choose View Source File from the Edit Source pull-down list in the object browser. You'll see something like the following:

protected String myVar;

public String myVar() {

   return myVar;

}

public void setMyVar(String newMyVar) {

   myVar = newMyVar;

}

The first line defines the instance variable. The first method returns its value. The second method sets its value.

When you choose Add Action, the following panel appears:

!

When you click Add, the following code is added to your source file:

public ThatPage myAction()
{
   ThatPage nextPage = (ThatPage)pageWithName("ThatPage");

   // Initialize your component here

   return nextPage;
}

WebObjects Builder provides these ways to add variables and methods for your convenience. Of course, you can add variables and methods directly to your component's code by editing them in Project Builder.

To delete a key, select it in the object browser and choose __Delete__
_Key_
from the Edit Source pull-down list. Any variables and methods associated with the key are deleted from the source file. You can restore the deleted key by selecting Undo from the Edit menu.

!

You can also delete the key with its context menu.

1. 

   Control-click the key on Rhapsody or right-click the key on Windows NT
2. 

   Choose Delete _key_
   from the menu that appears.
   !

To rename a variable or method, select its key in the object browser and choose __Rename__
_Key_
from the Edit Source pull-down list. In the panel that appears, enter the new name for the key and click Rename. Any variables and methods associated with the key are renamed.

Alternatively, you can rename the key with its context menu.

1. 

   Control-click the key on Rhapsody or right-click the key on Windows NT.
2. 

   Choose Rename _key_
   from the context menu that appears.
3. 

   Enter the new name in the panel that appears.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](The%20Object%20Browser.md) [!](The%20Object%20Browser.md) [!](Working%20with%20Application%20and%20Session%20Variables.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
