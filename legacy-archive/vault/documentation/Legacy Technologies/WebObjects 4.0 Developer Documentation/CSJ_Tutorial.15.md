---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.15.html
archived_at: '2026-07-15T07:59:25.932706Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.14.md) | [Back Up One Level](CSJ_Tutorial.13.md) | [Next](CSJ_Tutorial.16.md)

###   Adding Action  Methods

You can add basic behavior to your application, such as giving it the ability to add, delete, and save objects, without writing a line of code. This is possible because the EODisplayGroup, EOEditingContext, and EOInterfaceController objects in Interface Builder have predefined action methods that you can use to trigger operations in your application. An action method is a method that's invoked when the user clicks a button or another control object.

__7.

Add action methods.__

> Add three buttons to your window and label them "Add," "Remove," and "Save."
>
> ###### 
>
> !
>
> 
>
> These buttons will be used to insert new studios, delete existing studios, and save changes.
>
> 
>
> > Control-drag from the Add button to the Studio EODisplayGroup.
> >
> > 
> >
> > In the Inspector, select Outlets from the pop-up list at the top of the left column.
> >
> > 
> >
> > Select __target__
> > in the left column.
> >
> > 
> >
> > Double-click __insert:__
> > in the right column.
> >
> > 
> >
> > Using the same process, connect the Remove button to the __delete:__
> > method.
> >
> > 
> >
> > To connect the Save button, control-drag from the button to the File's Owner object in the nib file window.
> >
> > 
> >
> > In the Inspector, select __target__
> > in the left column.
> >
> > 
> >
> > Double-click __save:__
> > in the right column.
>
> ###### 
>
> !
>
> 
>
> The File's Owner icon represents the object that "owns" the nib file, or the nib file's root object. In a Java Client WebObjects application, this object is an instance of a custom subclass of EOInterfaceController that is automatically created for you (__StudioManager.java__
> , in this case). EOInterfaceController defines the __save__
> method and implements it to commit changes to the database.
>
> 
>
> __Note:__ The EOEditingContext object in the nib file ("EditingContext") also defines a method--__saveChanges__
> --that also commits changes to the database. However, EOInterfaceController's method is preferable because it catches exceptions that might arise from this operation.
>
> ---
>
> \xA9 1999 Apple Computer, Inc.
>
> [Previous](CSJ_Tutorial.14.md) | [Back Up One Level](CSJ_Tutorial.13.md) | [Next](CSJ_Tutorial.16.md)
>
> 
>
> Copyright © 2016 Apple Inc. All rights reserved.
>
> - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
> - [Privacy Policy](http://www.apple.com/privacy/)
