---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/Script/WODisplayGroupMethods.html
archived_at: '2026-07-15T07:51:07.033090Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Script.book.md)
[!Previous Section](SetUpWODisplayGroup.md)

 Common WODisplayGroup Methods

|  |  |
| --- | --- |
|  | ---  Common WODisplayGroup Methods The WODisplayGroup performs all database accesses for your application. The more commonly used methods are listed below, sorted by the type of operation they perform. Displaying Results These methods give you access to database objects and allow you to display them.  **__allObjects__** : All of the records to be displayed. For example, if your application has a query that results in one hundred records being fetched but you have set up the display group to only display ten at a time, __allObjects__ contains all one hundred records.  **__displayedObjects__** : The records actually being displayed. For example, if your application has a query that results in one hundred records being fetched but you have set up the display group to only display ten at a time, __displayedObjects__ contains those ten records.  **__selectedObjects__** : The records in the current selection.  **__selectedObject__** : A single selected record. Usually, this returns the first record in the __selectedObjects__ array. Managing Batches These methods control the grouping of records into manageable batches to display. (You set the batch size on the WODisplayGroup options panel.)  **__displayPreviousBatch__** : Select the previously-displayed batch of records and then reloads the page.  **__displayNextBatch__** : Selects the next batch of records and then reloads the page.  **__batchCount__** : The number of batches to display. For example, if you're fetching two hundred records and the batch size is ten, __batchCount__ returns twenty (twenty batches of ten records each).  **__batchIndex__** : The number of the batch currently displayed, where 1 is the first batch displayed. For example, if the batch size is ten records and __displayedObjects__ is showing records 11 through 20, the __batchIndex__ is 2. Querying These methods are used in applications that perform queries.  **__executeQuery__** : Builds a qualifier using __inputObjectForQualifier__ and the pattern matching you set on the display group options panel, and then fetches the records that match that qualifier. The qualifier is not preserved.  **__inputObjectForQualifier__** : Returns an entity object that is used to create the qualifier. For example, if you wanted the application to search on movie titles, you would bind a text field to __inputObjectForQualifier.title__. (__title__ comes from the entity that created the WODisplayGroup.)  **__secondObjectForQualifier__** : Used for from-to queries to specify the "to" value. This method must use the same property as __inputObjectForQualifier__. For example, if you wanted to query all movies released between two dates, you would bind the first field __inputObjectForQualifier.dateReleased__ and the second field to __secondObjectForQualifier.dateReleased__. The resulting qualifier would fetch all movies release after the date specified in __inputObjectForQualifier__ but before the date specified in __secondObjectForQualifier__. Modifying the Database These methods modify the database.  **__insert__** : Adds a new empty record. You should provide a dictionary containing default values for the record and use the __setInsertedObjectDefaultValues:__ to specify that the WODisplayGroup should use that dictionary to create all new values. For example, these statements ensure that all new records contain a value for movie title:  ``` [dictionary setObject:@"New title"]              forKey:@"title"]; [movies setInsertedObjectDefaultValues:dictionary]; ```  **__delete__** : Deletes the selected records.  If you're modifying a database, you must explicitly save the changes. Write a method that uses the session's EOEditingContext to save the changes. For example:   ``` [self.session.defaultEditingContext saveChanges];  ```   See the EOEditingContext class description in the _Enterprise Objects Framework Reference_.     --- |

[!Table of Contents](Script.book.md)
[!Next Section](CreateMethods.md)
