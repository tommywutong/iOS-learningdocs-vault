---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.19.html
archived_at: '2026-07-15T08:09:57.536248Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Manipulating%20Selections%20in%20a%20WODisplayGroup.md) [!](Fetching%20with%20an%20Editing%20Context.md)

#   Working with Unnormalized Tables

##  Synopsis

Describes how to set up an EOModel to work with a database with unnormalized tables.

##  Discussion

A normalized table contains no columns with duplicate data. Any column with duplicate data is replaced with a column of foreign keys into a new table containing unique data. For example, suppose you are creating a movie database. Every movie has a category such as "action", "drama", or "comedy". An unnormalized Movies table may be designed with a category column containing string data. All comedies would contain the string "comedy" in the category column.

This table can be normalized by creating a Category table having a unique set of category strings, the string "comedy" appearing exactly once in this table. Each movie in the Movie table now has a key to the row in the Category table corresponding to the movie's category. All comedies contain the key to the comedy row duplicated in the category column.

Fetches on unnormalized tables don't require the extra joins to the unique tables and are consequently faster than fetches on normalized tables. However, they are harder to maintain. For example, every action movie must have the string "action" in the category column. If an action movie has the misspelled string "actio", or the synonymous string "adventure" in the category column, an query for action movies will overlook this movie.

Suppose you are working with the unnormalized Movies table where the category column contains string data, and you want to present the user with a pick list of all the movie categories. You can't just read all of the categories from the Category table because the database doesn't contain one. However, you can use EOF to pretend your database is normalized by creating extra entities to the same database tables. These extra entities have a subset of the database table's columns. EOF makes objects unique by entity and primary keys, so records fetched from these different entities are indeed different objects. The "faked-out" entities that are not complete records from the database table should be marked as read-only because it makes no sense to insert a sparse Movie record with only the Category set when attempting to create a new Category.

The following steps in EOModeler simulate a Movies database with a Category table when the category data is actually embedded within the Movies table.

Create a new read-only entity in the EOModeler called Category.

1. 

   Set the new Category entity's table name to "Movie."
2. 

   Add one attribute called "category" to the Category entity.
3. 

   Make the category attribute the primary key.
4. 

   Create a to-many relationship from the Category entity to the Movie entity joined by the category attribute in each table. This allows to you get all the movies for a given category.

When you fetch the Category entity, you must remember to invoke
setUsesDistinct:YES
on the fetch specification. Otherwise, you will get duplicates since you are really just fetching one column from the Movie table.

####  Java Code

```

public NSArray fetchCategories() {
    EOEditingContext ec=session().defaultEditingContext();
    EOFetchSpecification fs=new EOFetchSpecification("Category", null, null);
    fs.setUsesDistinct(true);
    return ec.objectsWithFetchSpecification(fs);
}
```

####  Objective-C Code

```objc

- (NSArray *) fetchCategories {
    EOEditingContext *ec=[[self session] defaultEditingContext];
    EOFetchSpecification *fs=[EOFetchSpecification
        fetchSpecificationWithEntityName: @"Category"
        qualifier: nil sortOrderings: nil];
    [fs setUsesDistinct: YES];
    return [ec objectsWithFetchSpecification: fs];
}
```

##  See Also

- 

  [Fetching Distinct Results](Fetching%20Distinct%20Results.md#apple-giytqmru)
- 

  [Creating Fetch Specifications Programmatically](Creating%20Fetch%20Specifications%20Programmatically.md#apple-gm4tsmjz)
- 

  [Fetching with an Editing Context](Fetching%20with%20an%20Editing%20Context.md#apple-ge2tsmzt)

##  Questions

- 

  How do I set up an EOModel to be more normalized than the actual database?
- 

  How do I fetch pick lists when the rows are not normalized into a separate table?

##  Keywords

- 

  Unnormalized
- 

  Distinct

##  Revision History

21 July, 1998. David Scheck. First Draft.
19 November 1998. Clif Liu. Second Draft.

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Manipulating%20Selections%20in%20a%20WODisplayGroup.md) [!](Fetching%20with%20an%20Editing%20Context.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
