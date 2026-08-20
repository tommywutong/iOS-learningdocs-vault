---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.25.html
archived_at: '2026-07-15T08:09:02.618750Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Building%20and%20Testing%20Your%20Application.md) [!](Running%20a%20Java%20Client%20Application.md) [!](Adding%20Relationships.md)

---

#  What if It Doesn't Work?

What if you test-run the application in Interface Builder, or if you build and run it, and it doesn't work?

- 

  If no data appears in the table view, look in the Interface Builder Inspector to make sure that you have "Fetch on load" enabled for the Studio EODisplayGroup.
- 

  If the buttons don't have the desired effect, check to see that they're connected to the appropriate action method in the appropriate object.
- 

  If you get database errors when you try to add and delete studios or save changes, make sure that your model is properly specified. In particular, check that all of your entities have primary keys. Finally, choose Check Consistency from the Model menu in EOModeler to confirm that there are no problems in your model.

####  Optional Exercise

Enterprise Objects Framework provides additional action methods that you can use in connections: __fetch__ (EODisplayGroup) and __refetch__ (EOEditingContext). Try adding controls (such as buttons or menu items) to the application and connecting them to some of these action methods.

Until now you have still not written a single line of code. However, because of the built-in features of Enterprise Objects Framework, all of the following have been provided for you:

- 

  Automatic 

  primary key generation when you insert a new object

  As described in the section[Assigning Primary Keys](Assigning%20Primary%20Keys.md#apple-geytombu)
  , every row in a database is uniquely identified by its primary key value. When you create a new object in your application and save it to the database, you're adding a new row to a database table, and this row needs a primary key (that is, it needs to have a unique value for the primary key attribute you set in EOModeler). Enterprise Objects Framework handles generating this unique value for you.
- 

  Formatting of money and dates
- 

  Coordinating the user interface with your data

  Enterprise Objects Framework keeps all parts of an application synchronized with the current view of the data. For example, if you have two windows in an application that are displaying the same data and you change the values in one window, the other will automatically be updated to reflect the changes.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Building%20and%20Testing%20Your%20Application.md) [!](Running%20a%20Java%20Client%20Application.md) [!](Adding%20Relationships.md)
