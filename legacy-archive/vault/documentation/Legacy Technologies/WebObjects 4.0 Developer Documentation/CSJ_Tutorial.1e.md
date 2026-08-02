---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.1e.html
archived_at: '2026-07-15T07:59:37.081514Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.1d.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.1f.md)

##   Transferring Movies Between Studios

One of the primary functions of the StudioManager application is to allow one studio to purchase movies from another. To make this possible, you'll now add a pop-up list to the user interface.

The pop-up list displays a list of all of the studio titles. When you select a new studio in the pop-up list, you cause that studio to purchase the movie that's selected in the table view.

__1. Add a pop-up list.__

> Drag a pop-up list (labeled "Item" on the Views palette) into the window.
>
> 
>
> Control-drag from the pop-up list to the Studio EODisplayGroup.
>
> 
>
> In the Inspector, select 
>
> EOPopupAssoc from the pop-up list at the top of the left column.
>
> 
>
> Select __titles__
> in the left column. The __titles__
> aspect is bound to the class key whose values you want to display in the pop-up list.
>
> 
>
> Select __name__
> in the right column (since you want to display Studio names in the pop-up list).
>
> ###### 
>
> !
>
> 
>
> Put the pop-up list directly below the Studio table view and leave some space between it and the row of buttons. Later you will be adding fields between the pop-up list and the buttons. For a guide, see the figure associated with step 2, "Test your interface and try out the new pop-up list."
>
> 
>
> Now you have to add another binding to the EOPopupAssociation so that when you change the selected studio title, it sets the corresponding __studio__
> relationship property in the selected Movie object.
>
> 
>
> > Control-drag from the pop-up list to the movies EODisplayGroup.
> >
> > 
> >
> > In the Inspector, select EOPopupAssoc from the pop-up list at the top of the left column.
> >
> > 
> >
> > Select __selectedObject__
> > in the left column.
> >
> > 
> >
> > Select __studio__
> > in the right column.
>
> ###### 
>
> !
>
> 
>
> The __selectedObject__
> aspect is bound to the relationship property (in this example, Movie's __studio__
> property) that corresponds to the object bound to the __titles__
> aspect (Studio).

__2. Test your interface and try out the new pop-up list.__

> Choose File !
> Test Interface.
>
> ###### 
>
> !
>
> __3. Build and test-run the application.__
>
> 
>
> > (See "[Building and Testing Your Application](CSJ_Tutorial.16.md#apple-geytimjt)
> > " for details.)
> >
> > ###### 
> >
> > 
> >
> > You can now test the behavior of the pop-up list. For example, suppose you want to transfer the movie "Alien" from the 20th Century Fox studio to MGM. First select 20th Century Fox to display its movies. Then select "Alien" in the list of movies. Finally, use the pop-up list to change the selected studio from 20th Century Fox to MGM. This has the effect of removing "Alien" from 20th Century Fox's __movies__
> > relationship array and adding it to the __movies__
> > relationship array of MGM. It also sets the "Alien" Movie object's __studio__
> > relationship property to point to the new studio, MGM. When you use the pop-up list to transfer a movie, you'll notice that the movie disappears from the original studio's movie list and reappears in the movie list of the new studio.
> >
> > 
> >
> > These changes aren't committed to the database until you click Save. At that time Enterprise Objects Framework translates the changes you made in the object graph into the appropriate database changes. For example, it sets the foreign key __studioID__
> > in the transferred Movie object to have the same value as the __studioID__
> > primary key of its new studio.
> >
> > 
> >
> > Note that Enterprise Objects Framework manages all of this for you without requiring you to write any code.
>
> __Related Concepts:__ 
>
> [What is an Association?](CSJ_Tutorial.2e.md#apple-gqytcnbr)
> [See What is an Association?](CSJ_Tutorial.2e.md#apple-gqytcnbr)
>
> ---
>
> \xA9 1999 Apple Computer, Inc.
>
> [Previous](CSJ_Tutorial.1d.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.1f.md)
>
> 
>
> Copyright © 2016 Apple Inc. All rights reserved.
>
> - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
> - [Privacy Policy](http://www.apple.com/privacy/)
