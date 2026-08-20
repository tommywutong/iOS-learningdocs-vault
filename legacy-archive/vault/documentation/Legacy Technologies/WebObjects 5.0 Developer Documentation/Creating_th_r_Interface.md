---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Creating/Creating_th_r_Interface.html
archived_at: '2026-07-15T08:14:04.585277Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](The_Ingredi_ent_Project.md)[![Next](attachments/JavaClient/Images/next.gif)](Building_an_Application.md)

## Creating the User Interface

When you create a Java Client application using the Project
Builder Assistant, Project Builder puts a nib file in the Interfaces
group of the project. A nib file is primarily a description of a
user interface (or part of a user interface). It resides in the
Interfaces group of the project, is edited by the Interface Builder
application and can be archived along with other resources of your
application. This interface file is just like the interface files
in typical applications, which are defined using Cocoa objects.
The Enterprise Objects palette translates the Cocoa objects into
Swing objects that Java Client uses to generate the user-interface
on the client.

You typically construct a user interface using Interface Builder,
by dragging objects from a palette and dropping them into the content
window. Java Client WebObjects applications require that the Enterprise
Objects palette be loaded into Interface Builder. This palette includes
two objects: EOEditingContext and EODisplayGroup.

### Adding the EnterpriseObjects Palette

Before you can create the user-interface for a Java Client
application, you have to make sure that Interface Builder has the
EnterpriseObjects palette loaded. To do this you need to launch
Interface Builder and examine its Preferences window.

1. Start Interface
   Builder.

   Navigate to `/Developer/Applications` and
   launch Interface Builder.

   ![[image: ../Art/interfacebuildericon.gif]](../Art/interfacebuildericon.gif)
2. Load the required palettes.

   In Interface Builder, choose
   Interface Builder > Preferences.

   Click the Palettes
   tab.

   ![[image: ../Art/ibpreferences.gif]](../Art/ibpreferences.gif)

   If
   you don't see the EnterpriseObjects option, you add it by performing
   these steps:

   1. Click Add.
   2. In the Open Palette dialog, Navigate to the /Developer/Palettes directory.
   3. Double-click `EnterpriseObjects.palette`.

   Make
   sure that EnterpriseObjects is selected.

   Close the Interface
   Builder Preferences window.
3. Quit Interface Builder.

   Choose Interface Builder >
   Quit Interface Builder.

### Laying Out the User-Interface Elements

You can construct a basic interface for a Java Client WebObjects
application by simply dragging icons from EOModeler into the content
window in Interface Builder

1. Open the
   StudioManager nib file.

   In the Groups & Files list of the
   Project Builder main window, open the Interfaces group.

   Double-click `StudioManagerInterfaceController.nib`.

   A
   blank window (the content window), a nib file window, and a palette
   window appear when Interface Builder is launched. In [Figure 2-3](#apple-ijauercdindeo) you
   can see the windows you'll use to create your application's
   user interface.

   __Figure
   2-3 The Interface Builder environment__

   ![[image: ../Art/iblaunch.gif]](../Art/iblaunch.gif)

   If you don't
   see the EnterpriseObjects palette, which contains the EOEditingContext and
   EODisplayGroup elements, you need to add it. For details on how
   to perform this task, see ["Adding the EnterpriseObjects Palette"](#apple-ijauer2eijbuo).
2. Open the model file.

   In the Groups & Files list,
   open the Resources group.

   Double-click `Movies.eomodeld`.

|  |
| --- |
| __Note:__ This is a duplicate of the model file you created in ["Creating the Movies Model"](Creating_the_Movies_Model.md#apple-krifqusfiyytkmy). The original model file will not be touched in the remaining of this tutorial. |
3. Drag the Studio entity from EOModeler into the content window
   in Interface Builder. ![[image: ../Art/eomstudiodrag.gif]](../Art/eomstudiodrag.gif)

   In
   the nib file window, there's a new EODisplayGroup named "Studio",
   after the entity you dragged in. Note that the nib file window also
   includes an EOEditingContext object. An EOEditingContext object
   is added to your application along with the first entity you drag
   into Interface Builder. Because a document typically only needs
   one EOEditingContext, this object is only added once.

   ![[image: ../Art/ibstudiodisplaygroup.gif]](../Art/ibstudiodisplaygroup.gif)

   (See ["What Are EODisplayGroups and EOEditingContexts?"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Concepts/iWhat_Are_EO_ngContexts_.html) for more on display groups and editing contexts.)

   An
   entity EODisplayGroup has keys that correspond to the properties
   in its associated entity. You can examine these keys in the EODisplayGroup
   Info window.
4. Examine the EODisplayGroup in the Info window.

   Select
   the Studio EODisplayGroup in the nib file window.

   ![[image: ../Art/studiodisplaygroupicon.gif]](../Art/studiodisplaygroupicon.gif)

   Choose
   Tools > Show Info.

   Display the Attributes pane by
   choosing it from the pop-up menu below the Info window's title
   bar.

   Make sure that "Fetch on load" is selected.

   ![[image: ../Art/ibstudiodisplaygroupinfo.gif]](../Art/ibstudiodisplaygroupinfo.gif)

   The "Fetch on load" option
   is important because it allows data to be fetched from the database
   when you start your application.

   The keys listed correspond
   to the class properties specified for the entity in EOModeler. You
   can add other keys that are not class properties, such as methods
   defined in the associated enterprise object class.

   The
   interface that was created when you dragged an entity into the window
   is already a functional (if simple) application. You can test it.
5. Save the interface.
6. Test the interface.

   Choose File > Test Interface.

   ![[image: ../Art/ibinterfacetest.gif]](../Art/ibinterfacetest.gif)

   Click
   ![[image: ../Art/ibinterfacetesticon.gif]](../Art/ibinterfacetesticon.gif)
   in the menu
   bar to end the test.

   Note that because the "Fetch on load" option was
   enabled for the Studio EODisplayGroup in its Info window, the data
   is automatically fetched when you test your interface.

### Formatting Currency Values

Notice that the Budget column displays the budget amount for
each studio as an unformatted number. You can make the value for
the budget attribute display using currency formatting.

To set formatting, follow these steps:

1. Select the
   Budget column head in the table view. You accomplish this by first double-clicking
   the table and then clicking the column header.
2. Choose Tools > Show Info.
3. Display the Formatter pane of the Info window.
4. Select a standard currency format.

   Do not set the format
   to show negative values in red. Colored text is not currently implemented
   in J2SE.

![[image: ../Art/ibnstablecolumninfo.gif]](../Art/ibnstablecolumninfo.gif)

### Adding Action Methods

You can add basic behavior to your application, such as giving
it the ability to add, delete, and save objects, without writing
a line of code. This is possible because the EODisplayGroup, EOEditingContext,
and EOInterfaceController objects in Interface Builder have predefined
action methods that you can use to trigger operations in your application.
An action method is a method that's invoked when the user clicks
a button or another control object.

Perform these steps to add action methods to your user-interface:

1. Add the interface
   elements.

   Add three buttons to your window and label them "Add",
   "Remove", and "Save".

   These buttons will be
   used to insert new studios, delete existing studios, and save changes.
2. Connect the Add and Remove buttons to the `insert:` and `deleteSelection:` methods.

   Control-drag
   from the Add button to the Studio EODisplayGroup.

   ![[image: ../Art/ibbuttonconnectiondrag.gif]](../Art/ibbuttonconnectiondrag.gif)

   In the NSButton
   Info window, choose Outlets from the pop-up menu at the top of the left
   column.

   Select `target` in
   the left column.

   Select `insert:` in
   the right column and click Connect.

   ![[image: ../Art/ibaddbuttonconnectioninfo.gif]](../Art/ibaddbuttonconnectioninfo.gif)

   Using the same
   process, connect the Remove button to the `deleteSelection:` method.
3. Connect the Save button to the owner's `save()` method

   To
   connect the Save button, Control-drag from the button to the File's
   Owner object in the nib file window. ![[image: ../Art/filesownericon.gif]](../Art/filesownericon.gif)

   In
   the Info window of the Save button, choose Outlets in the pop-up
   menu at the top of the left column.

   Select target in
   the left column.

   Double-click `save()` in
   the right column.

The File's Owner icon represents the object that "owns"
the nib file, or the nib file's root object. In a Java Client
WebObjects application, this object is an instance of a custom subclass
of EOInterfaceController that is automatically created for you (`StudioManager.java`,
in this case). EOInterfaceController defines the `save` method
and implements it to commit changes to the database.

|  |
| --- |
| __Note:__ The EOEditingContext object in the nib file ("EditingContext") also defines a method-`saveChanges`-that commits changes to the database. However, EOInterfaceController's method is preferable because it catches exceptions that might arise from this operation. |

[![Previous](attachments/JavaClient/Images/previous.gif)](The_Ingredi_ent_Project.md)[![Next](attachments/JavaClient/Images/next.gif)](Building_an_Application.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
