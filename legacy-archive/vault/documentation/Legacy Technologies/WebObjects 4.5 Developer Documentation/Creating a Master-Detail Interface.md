---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.28.html
archived_at: '2026-07-15T08:09:03.624946Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Adding%20Relationships.md) [!](Adding%20Movies%20to%20the%20Application.md) [!](Transferring%20Movies%20Between%20Studios.md)

---

#   Creating a Master-Detail Interface

Starting with this exercise, you will create the final user interface of the StudioManager application. This means that you should start off by removing all objects added earlier to your nib file; also, give your application window a title.

1. 

   Prepare the nib file.

   In Interface Builder, delete the table view from the window.

   Delete the Studio EODisplayGroup and the EditingContext from the nib file window.

   Save the nib file.
2. 

   Set the window title.

   Select the window by clicking its title bar.

   Choose Inspector from the Tools menu.

   Enter "Studio Manager" in the TItle field of the Attributes display.

   !

   You can create a master-detail interface by simply dragging a relationship from EOModeler onto your window.
3. 

   Create a master-detail interface.

   Drag Studio's __movies__
   relationship from EOModeler onto the window in Interface Builder.

   Rearrange and resize the tables so that they are next to each other.

   Reconnect the Add and Remove buttons to the new Studio EODisplayGroup

   Reconnect the Save button to File's Owner (the interface controller).

   (See [Adding Action Methods](Adding%20Action%20Methods.md#apple-gi3tsobu)
   for these procedures.)

   !

   This operation creates a master-detail interface. Columns are automatically added for all of the attributes marked as class properties; you can delete any columns you don't want.

   For a Java Client application, the interface controller--represented by the File's Owner icon in the nib file window--is the "controller" object in the Model-View-Controller design scheme. The interface controller comes already connected to its "view" through the component outlet. But you must connect it to its "model" object, the editing context.
4. 

   Connect the interface controller to its editing context and display group.

   Control-drag from File's Owner to the EditingContext icon in the nib file window.

   In the Connections inspector, select the __editingContext__
   outlet.

   Click Connect.

   !

   Control-drag from File's Owner to the Studio icon in the nib file window.

   In the Connections inspector, select the __displayGroup__
   outlet.

   Click Connect.

   In the following figure, you can see the master-detail interface in action. Notice that the table views have been rearranged, and that titles have been added above the Studios and Movies tables.
5. 

   Test your interface.

   Choose File !
   Test Interface.

   !
6. 

   Use Project Builder to build the application.

   To see the effects of your changes, you must compile and run the application. However, before you run the application, there is one last step to perform. The applet providing the running environment for your Java Client application is set to a default size in the WOJavaClientApplet bindings in __Main.wod__. This size could be too small to accommodate your user interface (or too large for it).
7. 

   Learn the size of the window.

   Open __StudioManager.nib.__

   Choose Inspector from the Tools menu.

   Select the Size inspector.

   Write down the __w__
   and__h__
   parameters.

   !

   For example's sake, let's assume the window is 503 pixels high and 700 pixels wide. Transfer these numbers to the WOJavaClientApplet.
8. 

   Set the WOJavaClientApplet size bindings.

   Open __Main.wod.__

   Enter the dimensions of the window in the height and width bindings.

   Save the file.

   Applet: WOJavaClientApplet {

     height = 503; // change this

     width = 700; // and this

     interfaceControllerClassName =
   "studiomanager.client.StudioManager";

     useJavaPlugin = NO;

   }

   Now you are ready to test the application.
9. 

   Run and test the application.

   Choose Tools !
   Launcher !
   Run to launch the server side of the application.

   Start up the client side (see [Running a Java Client Application](Running%20a%20Java%20Client%20Application.md#apple-gmzdmmzz)
   ).

   When you select a studio in the Studios table view, the display changes in the Movies table view to show the selected studio's movies.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Adding%20Relationships.md) [!](Adding%20Movies%20to%20the%20Application.md) [!](Transferring%20Movies%20Between%20Studios.md)
