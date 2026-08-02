---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies18.html
archived_at: '2026-07-15T07:54:18.197327Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies17.md)

### Bindings in the Editing Part

The text fields in the editing part are all bound to attributes of the __movieDisplayGroup__'s __selectedObject__-the movie on which the user clicked. Typing new values into these fields updates the Movie enterprise object. To actually save the updated values to the database, the user must click the "Save to database" button.!

- Inspect the middle image button.

Its __action__ attribute is bound to the action method __saveChanges__.

- Look in the __Main.java__ class to see how __saveChanges__ is implemented.

The method (shown below with comments omitted) simply saves any changes that have been made to __movieDisplayGroup__'s objects to the database.

```
public void saveChanges() throws Exception {
    try {
        this.session().defaultEditingContext().saveChanges();
    }
    catch (Exception exception) {
        System.err.println("Cannot save changes ");
        throw exception;
    }
}
```


__this.session()__ returns a Session object that represents a connection to the application by a single user. A Session object provides access to an EditingContext object. The expression

```
this.session().defaultEditingContext().saveChanges();
```


sends a __saveChanges__ message to the Session's __defaultEditingContext__. This default EditingContext object manages graphs of objects fetched from the database, and all changes to the database are saved through it. For more information, see the EditingContext class specification in the _Enterprise Objects Framework Reference_.

An EditingContext's __saveChanges__ method uses other Enterprise Objects Framework objects to analyze its network of enterprise objects (Movie objects referenced by the application) for changes and then to perform a set of corresponding operations in the database. If an error occurs during this process, __saveChanges__ throws an exception. __Main.java__'s __saveChanges__ method simply raises the exception, having the effect of returning a diagnostic page. You could return an error page that explains the reason for the save failure instead, but the application in this tutorial uses the default behavior.

- Inspect the first and third image buttons to see what their __action__ attributes are bound to.

They are bound to __movieDisplayGroup.insert__ and __movieDisplayGroup.delete__, respectively. The DisplayGroup __insert__ method creates a new enterprise object, then inserts it into the display group's list of objects just past the current selection. The DisplayGroup __delete__ method deletes the display group's selected object. These changes happen only in memory-not in the database. To actually insert a new row in the database (or delete a row), the user must click the "Save to database" button, invoking __saveChanges__ on the session's EditingContext. The editing context analyzes the enterprise objects in memory; determines if any objects have been added, updated, or deleted; and then executes database operations to sync the database with the application.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies19.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
