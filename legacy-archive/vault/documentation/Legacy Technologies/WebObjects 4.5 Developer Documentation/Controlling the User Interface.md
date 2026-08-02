---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.34.html
archived_at: '2026-07-15T08:09:14.346047Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md) [!](Invoking%20Server%20Methods%20Remotely.md) [!](Advanced%20Tasks.md)

---

#  Controlling the User Interface

In Java Client applications you can give the interface controller (implemented in this project in __StudioManager.java__ on the client) a _controller display group._ By creating associations between the controller display group and aspects of user-interface objects, you can use the interface controller to manage various facets of the user interface. In the following steps, you add a method as a property of the controller display group and bind this method to the __enabled__ aspect of the Revenue field through an EOControlAssociation; since this method simply returns __false__, the field is disabled.

1. 

   Add a display group to the nib file.

   Drag a display group from the EOPalette to the nib file window.

   Double click the title of the display group to select it.

   Give the display group the name "Controller".

   !

   As mentioned earlier, the owner of the nib file (File's Owner) is an instance of the custom EOInterfaceController automatically created by Project Builder. EOIntefaceController has a __controllerDisplayGroup__ outlet; in the following step, connect the interface controller to this outlet.
2. Connect the interface controller to its display group.

   Control-drag from File\xCDs Owner to the Controller icon.

   In the Connections inspector, select controllerDisplayGroup.

   Click Connect.

   !

   Next add the neverEnabled method as a property of the controller display group.
3. Add a property to the controller display group.

   Select the Controller display group in the nib file.

   In the Attributes inspector, enter \xF1neverEnabled\xEE in the field.

   Click Add.

   !

   Now hook up the field to the display group using an EOControlAssocation to bind its enabled aspect to the neverEnabled method.
4. Connect the field\xCDs enabled aspect to the display group property.

   Control-drag from the Revenue field to the Controller display group.

   In the Connections inspector, select EOControlAssoc from the pop-up list at the top of the left column.

   Select enabled in the left column.

   Select neverEnabled in the right column.

   Click OK.

   !
5. Implement the neverEnabled method.

   Now that the interface controller, the controller display group, and the Revenue field are interconnected via their outlets and associations, you can implement the method bound to the enabled aspect (in StudioManager.Java on the client).

   public boolean neverEnabled() {
         return false;
   }
6. Build, run, and test the application.

   Build the project and test the application. The Revenue field has a gray background and cannot be written into.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md) [!](Invoking%20Server%20Methods%20Remotely.md) [!](Advanced%20Tasks.md)
