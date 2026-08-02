---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.1d.html
archived_at: '2026-07-15T07:59:34.222340Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.1c.md) | [Back Up One Level](CSJ_Tutorial.1b.md) | [Next](CSJ_Tutorial.1e.md)

###   Creating a Master-Detail Interface

Starting with this exercise, you will create the final user interface of the StudioManager application. This means that you should start off by removing all objects added earlier to your nib file; also, give your application window a title.

__2. Prepare the nib file.__
> 
>
> In Interface Builder, delete the table view from the window.
>
> 
>
> Delete the Studio EODisplayGroup and the EditingContext from the nib file window.
>
> 
>
> Save the nib file.

__3. Set the window title.__

> Select the window by clicking its title bar.
>
> 
>
> Choose Inspector from the Tools menu.
>
> 
>
> Enter "Studio Manager" in the TItle field of the Attributes display.
>
> ###### 
>
> !
>
> 
>
> You can create a master-detail interface by simply dragging a relationship from EOModeler onto your window.

__4. Create a master-detail interface.__

> Drag Studio's __movies__
> relationship from EOModeler onto the window in Interface Builder.
>
> 
>
> Rearrange and resize the tables so that they are next to each other.
>
> 
>
> Reconnect the Add and Remove buttons to the new Studio EODisplayGroup
>
> 
>
> Reconnect the Save button to File's Owner (the interface controller).
>
> 
>
> (See [Adding Action Methods](CSJ_Tutorial.15.md#apple-gi3tsobu)
> for these procedures.)
>
> ###### 
>
> !
>
> 
>
> This operation creates a master-detail interface. Columns are automatically added for all of the attributes marked as class properties; you can delete any columns you don't want.
>
> 
>
> For a Java Client application, the interface controller--represented by the File's Owner icon in the nib file window--is the "controller" object in the Model-View-Controller design scheme. The interface controller comes already connected to its "view" through the component outlet. But you must connect it to its "model" object, the editing context.

__5. Connect the interface controller to its editing context and display group.__

> Control-drag from File's Owner to the EditingContext icon in the nib file window.
>
> 
>
> In the Connections inspector, select the __editingContext__
> outlet.
>
> 
>
> Click Connect.
>
> ###### 
>
> !
>
> 
>
> Control-drag from File's Owner to the Studio icon in the nib file window.
>
> 
>
> In the Connections inspector, select the __MasterDisplayGroup__
> outlet.
>
> 
>
> Click Connect.
>
> 
>
> In the following figure, you can see the master-detail interface in action. Notice that the table views have been rearranged, and that titles have been added above the Studios and Movies tables.

__6. Test your interface.__

> Choose File !
> Test Interface.
>
> ###### 
>
> !

__7. Use Project Builder to build the application.__

To see the effects of your changes, you must compile and run the application. However, before you run the application, there is one last step to perform. The providing the running environment for your Java Client application is set to a default size in the WOJavaClientApplet bindings in __Main.wod__
. This size could be too small to accommodate your user interface (or too large for it).

__8. Learn the size of the window.__
> 
>
> Open __StudioManager.nib.__
>
> 
>
> Choose Inspector from the Tools menu.
>
> 
>
> Select the Size inspector.
>
> 
>
> Write down the __w__
> and__h__
> parameters.
>
> ###### 
>
> !
>
> 
>
> For example's sake, let's assume the window is 503 pixels high and 700 pixels wide. Transfer these numbers to the WOJavaClientApplet.

__9. Set the WOJavaClientApplet size bindings.__

> Open __Main.wod.__
>
> 
>
> Enter the dimensions of the window in the height and width bindings.
>
> 
>
> Save the file.
>
> 
>
> `Applet: WOJavaClientApplet {
> 
>
>    height = 503; // change this
> 
>
>    width = 700; // and this
> 
>
>    interfaceControllerClassName = "studiomanager.client.StudioManager";
> 
>
>    useJavaPlugin = NO;
> 
>
> }`
>
> 

Now you are ready to test the application.

__10. Run and test the application.__

> Choose Tools !
> Launcher !
> Run to launch the server side of the application.
>
> 
>
> Start up the client side (see [Running a Java Client Application](CSJ_Tutorial.19.md#apple-gmzdmmzz)
> ).
>
> 

When you select a studio in the Studios table view, the display changes in the Movies table view to show the selected studio's movies.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.1c.md) | [Back Up One Level](CSJ_Tutorial.1b.md) | [Next](CSJ_Tutorial.1e.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
