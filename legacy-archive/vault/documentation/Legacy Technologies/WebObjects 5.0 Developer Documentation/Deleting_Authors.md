---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOFRelationships/Deleting_Authors.html
archived_at: '2026-07-15T08:13:06.210600Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Running_the_Application.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Sorting_a_Fetch.md)

## Deleting Authors

When the user deletes an author, she doesn't get a warning
telling her that all the books related to that author are going
to be deleted as well. In this section, you'll add a component
that displays such a warning.

Though conceptually more complex, the design and implementation
of the logic for deleting authors is just as simple as that for
books. The only significant difference is that the application asks
the user for confirmation before deleting the author, because this action
has the side effect of removing additional objects from the object
store that the user may not be aware of.

You'll add a component that displays the author that the
user wants to delete, along with all related books, and asks for
confirmation. If the user changes her mind, she'll be returned
to the Main component. If the user clicks Delete, the author and
related books are deleted from the editing context (the actual delete
transaction takes place when the user clicks Save on the Main page).

### Create the ConfirmAuthorDelete Component

1. Add a new
   component and name it ConfirmAuthorDelete.

   (See ["Defining a New Component"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/ComponentCommunication/iDefining_a_New_Component.html) for
   details.)
2. Open `ConfirmAuthorDelete.wo` in
   WebObjects Builder.
3. Add the following instance variables:
   1. `author` (Author),
      with accessor methods
   2. `bookItem` (Book),
      without accessor methods
4. Add the following actions:
   1. `cancel` (Main)
   2. `deleteAuthor` (Main)
5. Edit the component's content so that it looks similar to [Figure 12-6](#apple-ijbegqscizfeq) and
   make the necessary bindings.

   __Figure 12-6 ConfirmAuthorDelete.wo__

   ![[image: ../Art/confirmauthordeletewo.gif]](../Art/confirmauthordeletewo.gif)
6. Save `ConfirmAuthorDelete.wo`.

### Edit ConfirmAuthorDelete.java

Edit the `deleteAuthor` method
so that it looks like [Listing 12-15](#apple-ijbegqshjfbuo).

__Listing
12-15 The deleteAuthor method in ConfirmAuthorDelete.java__

```
public Main deleteAuthor() {
    Main nextPage = (Main)pageWithName("Main");

    // get session
    Session session = (Session)session();

    session.deleteAuthor(author);

    return nextPage;
}
```


### Modify the Main Component

The Main component needs to display the ConfirmAuthorDelete
component when its `deleteAuthor` action
is invoked. You accomplish that by modifying the `deleteAuthor` method
in Main.java so that it looks like [Listing 12-16](#apple-ijbegqsdinbuq).

__Listing
12-16 The deleteAuthor method in Main.java—returns
ConfirmAuthorDelete component__

```
public ConfirmAuthorDelete deleteAuthor() {
    ConfirmAuthorDelete nextPage =  (ConfirmAuthorDelete)pageWithName("ConfirmAuthorDelete");
    nextPage.setAuthor(authorItem);
    return nextPage;
}
```


### Run the Application

Build and run the application. Create a new author, add several
books, and save your changes. (You can use EOModeler to browse the
tables's contents and confirm that the new information has been
added to the database.) Click Delete on the newly added author.
You should be presented with a confirmation page similar to [Figure 12-7](#apple-ijbegskkivfes).

__Figure
12-7 The ConfirmAuthorDelete component
in action__

![[image: ../Art/confirmauthordeleteie.gif]](../Art/confirmauthordeleteie.gif)

If you click Cancel, you are simply returned to the Main page.
Clicking Delete causes the `deleteAuthor` method
in `ConfirmAuthorDelete.java` to
be invoked. In turn, it invokes the session's `deleteAuthor` method,
which removes the author from the `authorList` array
and adds it to the editing context's list of enterprise objects
to delete.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Running_the_Application.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Sorting_a_Fetch.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
