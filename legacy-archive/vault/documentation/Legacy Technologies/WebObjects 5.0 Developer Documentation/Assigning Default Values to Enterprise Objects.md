---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.21.html
archived_at: '2026-07-15T08:14:52.364651Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.20.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.22.md)

#   Assigning Default Values to Enterprise Objects

##  Synopsis

Describes how to assign default values to new enterprise objects.

##  Discussion

When you create new enterprise objects in your application, you often need to assign default values to attributes of the objects. For example, if you are inserting a new movie into a Movies database, you should assign a default value for the title attribute so that the new movie is not displayed as a blank line when movies are listed.

You can assign default values in one of four ways:

- 

  Assignment immediately after object is created and inserted into the editing context
- 

  A custom action method bound to a display group's insert button
- 

  Specification of default values using a display group

Although you can assign default values in an enterprise object's constructor (or, in the case of Objective-C, an enterprise object's initializer), it is not recommended that you do so. Because such initialization happens during a fetch, it can create much useless data and thus slow down the fetch.

###  Assignment After Insertion Into the Editing Context

If default values are intrinsic to an enterprise object, you could assign them immediately after the objects are inserted into the editing context. As an example, say your video rental application's VideoRental class has a
dateCheckedOut
property. You probably want to assign the current date automatically to
dateCheckedOut
instead of requiring the user to supply the value.

A custom enterprise object is sent certain messages when it is created, and one of these is of particular significance for assigning default values. After a custom enterprise object is created and inserted into an editing context, it receives the
awakeFromInsertionInEditingContext
method (which is invoked by the
insertObjectWithGlobalID
method which, in turn, is invoked by the
insertObject
method). Your enterprise object can implement the
awakeFromInsertionInEditingContext
method to assign default values to the attributes of the enterprise object.

```

public void awakeFromInsertionInEditingContext(EOEditingContext context) {    super.awakeFromInsertionInEditingContext(context);    dateCheckedOut = new CalendarDate();}
```


Use
awakeFromInsertionInEditingContext
method for assigning default values if you are creating objects that did not previously exist in the database. If, on the other hand, you are creating new enterprise objects from existing data in the database, you should use the
awakeFromFetchInEditingContext
method, which is sent to an enterprise object just created from a database row and initialized with database values. In this scenario, you must be careful about sending messages to other enterprise objects, however, because faulting may occur because the database channel might still be open while the fetching continues. Read the topics on faults for more information.

###  Assignment in an Action Method

If you're using a WODisplayGroup, you can implement a custom action method for the "Insert" button of your application instead of binding that control directly to the display group's
insert
method. In your implementation of the action method, you might create a new enterprise object, assign default values to it, and then insert the new object into the display group.

```

public void insertBook() {    EOEditingContext ec = session().defaultEditingContext();    NSDate dateCheckedOut = new NSDate();    // create new book    Book book = new Book (ec, null, null);    book.setDateCheckedOut(dateCheckedOut);    // assume display group already exists    bookDisplayGroup.insertObject(book);}
```

###  Assignment Through Default Values Per Display Group

If the default values are specific to an application or to a particular user interface, you might explicitly initialize the object in code, or specify the default values using a display group. In a Movies application, for example, your user interface may require you to provide a default value so that users can tell when they have selected a newly inserted record. In another situation, you might not want a new movie to have a default title; you might instead want the new movie's title to be blank.

To specify default values for newly created Movie objects using the display group, (
moviesDisplayGroup
in the example below), you might write the following constructor for the movie page WOComponent:

```

public MoviePage() {
    super();
    NSMutableDictionary defaultValues = new NSMutableDictionary();
    defaultValues.setObjectForKey("New Movie Title", "title");
    movieDisplayGroup.setInsertedObjectDefaultValues(defaultValues);
}
```


This method assigns the value "New Movie Title" as the default value for a new movie's
title
attribute. When
movieDisplayGroup
inserts a new movie, it creates a new "movie" enterprise object and assigns this default title to that movie.

##  See Also

- 

  [Creating a New Enterprise Object](Creating%20a%20New%20Enterprise%20Object.md#apple-ge3dsmzu)

##  Questions

- 

  How do I set data in the columns of newly inserted rows?
- 

  How do I ensure that default values go into my new rows?

##  Keywords

- 

  Editing
- 

  Context
- 

  Display
- 

  Group
- 

  Action
- 

  Initialization
- 

  Default

##  Revision History

24 July, 1998. Virginia McCulloh. First Draft.

18 November, 1998. Terry Donoghue. Second Draft.

16 March, 1998. Clif Liu. Corrections.

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.20.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.22.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
