---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOFRelationships/Completing__thors_Model.html
archived_at: '2026-07-15T08:13:02.721885Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Working_Wit_lationships.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Using_Relat_n_Your_Code.md)

## Completing the Authors Model

To complete the Authors model, you'll add the Book entity
to it. After defining the entity's attributes, you'll add the
BOOK table to the Authors database. Then you'll add the relationships
between Author and Book.

### Define the Book Entity

In this section you'll create the Book entity and define
its attributes, including its primary and foreign keys.

1. Open `Authors.eomodeld` in
   EOModeler.
2. Create a new entity.
   1. Choose Property >
      Add Entity.
   2. Choose Tools > Inspector.
   3. Enter `Book` in the
      Name and Class text fields.
   4. Enter `BOOK` in the
      Table Name text field.
       ![[image: ../Art/entitybookadd.gif]](../Art/entitybookadd.gif)
3. Add and configure Book's attributes.

   The Book entity
   has one major attribute, `title`,
   which stores a book's title. It also needs a primary key attribute, `bookId`,
   to ensure that all the rows in the BOOK table are unique. Finally,
   it requires an additional attribute, a foreign key, which is used
   to link a book to its author. This last attribute is named `authorId`.

   Add
   the `title` attribute by
   following these steps:

   1. Make sure the Book
      entity is selected in entity list.
   2. Add a new attribute and name it `title`.
   3. Enter `TITLE` as
      the column name.
   4. Enter `char` as the
      external type.
   5. Choose String as the internal data type.
   6. Enter `50` in the
      External Width text field.
   7. Select the Allow Null Value option in the Advanced Attribute
      Inspector.
       ![[image: ../Art/authortitle.gif]](../Art/authortitle.gif)

   Add
   the `bookId` attribute:

   1. Add a new attribute
      and name it `bookId`.
   2. Enter `BOOK_ID` as
      the column name.
   3. Enter `int` as the
      external data type.
   4. Choose Integer as the internal data type.
   5. Make sure the Allow Null Value option is not selected.
      ![[image: ../Art/bookbookid.gif]](../Art/bookbookid.gif)

   Add
   the `authorId` attribute
   (this is the foreign key that relates a book to its author):

   1. Add a new attribute
      and name it `authorId`.
   2. Enter `AUTHOR_ID` as
      the column name.
   3. Enter `int` as the
      external type.
   4. Choose Integer as the internal data type.
   5. Make sure the Allow Null Value option is not selected.
4. Select the primary key attribute for the Book entity.
   1. In the `bookId` row
      of the Book Attributes list, click in the column with a key as its heading
      so that a key appears in the row.
   2. Click in the diamond column of the `bookId` row
      so that the diamond disappears (the value of the `bookId` attribute
      is not relevant to the application).
5. Make `authorId` a
   hidden attribute.

   For the same reason that `bookId` is
   irrelevant, the value of `authorId` is
   of no interest to the application.

   Click in the diamond
   column of the `authorId` row
   in the Book Attributes list, so that the diamond disappears.

### Create the BOOK Table

In this section, you'll create the BOOK table, just like
you created the AUTHOR table in ["Creating the AUTHOR Table"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOMBasics/iThe_Authors_Application.html).

1. Select the
   Book entity from the entity list.
2. Choose Property > Generate SQL.
3. Make sure that only the Create Tables option is selected.
   ![[image: ../Art/booktablecreate.gif]](../Art/booktablecreate.gif)
4. Click Execute SQL.

### Define the Model's Relationships

Now that the Book entity is defined, you will relate it to
the Author entity.

The relationship between Author and Book is bidirectional.
Each author can have many books, while each book has only one author.

Create the relationships by following these steps:

1. Choose Tools
   > Diagram View.
2. Control-drag from `Author.authorId` to `Book.authorId`.

   This
   creates two relationships: a to-many relationship from Author to
   Book, using `authorId` as
   the linking attribute; and a to-one relationship from Book to Author,
   again using `authorId` as
   the linking attribute.

   [Figure 12-1](#apple-ijbegrsji5fes) graphically depicts
   the two relationships. Book is linked to Author by a single-headed
   arrow, meaning that a book can have one author. Whereas Author is linked
   to Book by a double-headed arrow, meaning that an author can have
   more than one book.

   __Figure 12-1 Relationships
   in the Authors model__

   ![[image: ../Art/authorseomodelddiagram2.gif]](../Art/authorseomodelddiagram2.gif)

Deletion can become complex due to the relationships between
entities. For example, if you delete an Author object, what should
happen to the Book objects associated with it? You can define the
behavior you desire by using delete rules in your model.

#### What Are Delete Rules?

Each relationship has a __delete rule__ that
tells Enterprise Objects what to do when you try to delete the source
object. The following are the possible behaviors:

- __Nullify__ Delete
  the object and nullify any relationships that point back to it from
  other entities. (The value of the foreign key property in target
  objects is set to `null`.)
- __No action__ Delete the object and perform
  no other action.
- __Cascade__ Delete the object and all the
  objects that are targets of the relationship (child objects).
- __Deny__ Do not delete the object if child
  objects exist. This rule is typically used when child-object deletion
  should receive special processing before the parent is deleted.

#### Delete Rules in the Authors Model

In the case of deletion of a book, it makes the most sense
to delete the book and remove it from the Author entity's `books` relationship.
This is an example of the Nullify delete rule. If you examine the `author` relationship
of the Book entity, you'll see that it is already configured with
the Nullify delete rule selected. Therefore, you don't need to
alter it. However, that default is not appropriate when an author
is deleted.

Follow these steps to configure the `books` relationship
of the Authors entity so that all of an author's books are deleted
when the author is removed from the database:

1. Select the `books` relationship
   of the Author entity.
    ![[image: ../Art/authorsentities.gif]](../Art/authorsentities.gif)
2. Open the Inspector.
3. Display the Advanced Relationship Inspector.
4. Select Cascade as the delete rule.
5. Select the Owns Destination option.
    ![[image: ../Art/deleterule.gif]](../Art/deleterule.gif)
6. Save `Books.eomodeld`.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Working_Wit_lationships.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Using_Relat_n_Your_Code.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
