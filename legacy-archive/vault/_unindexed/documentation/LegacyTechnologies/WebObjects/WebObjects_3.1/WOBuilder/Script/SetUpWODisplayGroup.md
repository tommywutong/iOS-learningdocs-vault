---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/Script/SetUpWODisplayGroup.html
archived_at: '2026-07-15T07:51:04.562615Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Script.book.md)
[!Previous Section](Enterprise.md)

Setting Up a WODisplayGroup

# Setting Up a WODisplayGroup

Select the WODisplayGroup variable.

Click the checkmark button in the object browser.

!

!

A WODisplayGroup performs certain database-related operations: it can display records, organize results into batches, fetch records from the database, as well as query the database. You use the options panel to set up how the WODisplayGroup performs these operations.

#### Displaying

The Entries per batch field specifies the number of records displayed at a time. For example, suppose you are displaying one hundred records. Instead of displaying all of these at once, you can set the batch size so that the page displays a more manageable number (for example, 10). If you set a batch size, the component should have buttons that will return the next batch of records and the previous batch of records. (Bind the buttons to the WODisplayGroup methods __displayNextBatch__ and __displayPreviousBatch__.) If you don't want records displayed as batches, set the size to 0.

#### Sorting

The Sort order options specify how the records are sorted. The pop-up list shows all of the class properties for the WODisplayGroup's entity. Select the class property that the results should be sorted upon and then specify the sort order.

#### Fetching

If you're creating a component that is simply going to list a set of records from the database, you probably want the Fetches on Load check box checked. If checked, the WODisplayGroup performs a fetch when the application starts up. If you're creating a query-based application, you probably want this check box turned off so that the user controls when the fetch is performed.

#### Querying

Qualification Mode sets how the pattern matching works. When a user enters a string in a text field to search the database for that string, the qualification mode sets which part of the string must be matched.

- Prefix means that the text starts with the string the user enters in the search field. (For example, suppose you are searching a database of movies and you enter "the" in the search for title text field. Prefix mode returns all of the movies that begin with "the.")
- Contains means the string can be anywhere in the entry. (For example, it returns all movies that contain the string "the" anywhere in the title.)
- Suffix means the entry ends with the string the user typed in the field. (For example, it returns all movies that end with the string "the").

[!Table of Contents](Script.book.md)
[!Next Section](WODisplayGroupMethods.md)
