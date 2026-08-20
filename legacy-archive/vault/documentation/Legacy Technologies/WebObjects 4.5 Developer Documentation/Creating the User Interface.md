---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.1e.html
archived_at: '2026-07-15T08:08:56.196856Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Tutorial.md) [!](Removing%20Primary%20and%20Foreign%20Keys%20as%20Class%20Properties.md) [!](Formatting%20Currency%20Values%20and%20Dates.md)

---

#   Creating the User Interface

When you create a Java Client WebObjects application project, Project Builder puts a nib file in the Interfaces suitcase of the ClientSideJava subproject. A nib file is primarily a description of a user interface (or part of a user interface); it is created by the Interface Builder application and it can be archived along with other resources of your application. The nib file in the ClientSideJava subproject, however, is quite unlike the nib files in typical applications. When the EOJavaClient palette is loaded and you construct a user interface, the objects that a nib file contains are derived from the Yellow Box frameworks _and_ the Java Foundation Classes (JFC), or Swing. They thus can be downloaded to Java Client applets that live on the client.

1. 

   Open the StudioManager.nib file.

   In the project browser navigate to Subprojects !
   ClientSideJava !
   Interfaces !
   English.

   Select __StudioManager.nib__
   .

   Double-click to open.

   !

   By default, a blank window appears when Interface Builder is launched. This is the window you'll use to create your user interface.

   The Interface Builder application is located in the WebObjects program group. The icon for the application is this:

   !

   In Interface Builder you typically construct a user interface by dragging objects from a palette and dropping them into the window. Java Client WebObjects applications require that two special palettes be loaded into Interface Builder:
   - 

     __EOPalette.palette__ includes two 

     objects: EODisplayGroup and EOEditingContext.
   - 

     __EOJavaClientPalette.palette__ has no visible objects but contains the code that creates Swing objects equivalent to the Yellow Box objects on the standard palettes.

   If these palettes are not loaded, you must load them.
2. 

   Load the required palettes.

   In Interface Builder, choose Tools !
   Palettes !
   Open.

   In the Open Palette panel, navigate to __NEXT_ROOT/Developer/Palettes.__

   Double-click __EOPalette.palette__
   .

   Perform the same sequence of steps, but this time load __EOJavaClientPalette.palette__
   .

   !

   You'll be dragging objects off of the palette later. For now, however, you can construct a basic interface for a Java Client WebObjects application by simply dragging icons from EOModeler into Interface Builder.
3. 

   Drag the Studio entity from EOModeler into the window.

   !

   The following figure shows the results of dragging an entity into your window. In the nib file window, there's a new EODisplayGroup that's named "Studio" after the entity you dragged in. Note that the nib file window also includes an EOEditingContext object. An EOEditingContext object is added to your application along with the first entity you drag into Interface Builder. Because a document typically only needs one EOEditingContext, this object is only added once.
   __Related Concepts:__

   [What are EODisplayGroups and EOEditingContexts?](What%20are%20EODisplayGroups%20and%20EOEditingContexts.md#apple-obtwmslehuytambwgezto)
   
   !

   An 

   entity EODisplayGroup has keys that correspond to the properties in its associated entity. You can examine these keys in the EODisplayGroup Inspector.
4. 

   Examine the EODisplayGroup in the Inspector.

   Select the Studio EODisplayGroup in the nib file window.

   Choose Tools !
   Inspector.

   Make sure that the 

   "Fetch on load" checkbox is checked.

   !

   The "Fetch on load" option is important because it allows data to be fetched from the database when you start your application.

   The interface that was created when you dragged an entity into the window is already a functional (if simple) application. You can test it.
5. 

   Test the interface.

   On Mac OS X Server, choose Document !
   Test Interface. Click !
   in the menu bar to exit the test.

   On Windows NT, choose File !
   Test Interface. Choose File !
   Exit to exit the test.

   !

   Note that because the "Fetch on load" option was enabled for the Studio EODisplayGroup in the Inspector, the data is automatically fetched when you test your interface.

#### [Formatting Currency Values and Dates](Formatting%20Currency%20Values%20and%20Dates.md#apple-obtwm3dehuytambwgyyti)

#### [Adding Action Methods](Adding%20Action%20Methods.md#apple-obtwmslehuytambwgyztc)

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Tutorial.md) [!](Removing%20Primary%20and%20Foreign%20Keys%20as%20Class%20Properties.md) [!](Formatting%20Currency%20Values%20and%20Dates.md)
