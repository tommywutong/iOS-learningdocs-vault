---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Movies/6_MasDet.html
archived_at: '2026-07-15T07:49:14.111198Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Movies.book.md) [!Previous Section](5_Actors.md)

# Add a detail display group to the details page

In the previous section, you navigated relationships to access attributes in other entities. Using the __movieRoles__ relationship in the Movies entity, you were able to display attributes of a movie's roles. Similarly, you displayed the names of the actors who played a role by navigating two relationships: __movieRoles__ to get from a movie to one of its roles and __talent__ to get from the role to the actor who played it. Traversing the object graph this way works very well in read-only scenarios where you only want to display information in a related object. However, it doesn't work completely in scenarios where you want to be able to make changes to the related objects.
In the next section, you'll give the application the ability to insert, update, and delete movie roles for the selected movie. This read-write scenario requires a slight modification to the way you access movie role information. To be able to insert new movie roles for a movie, you need a WODisplayGroup for managing MovieRole objects.

## Disconnect the bindings

- Inspect the repetition.
- Disconnect the __list__ binding.
- Disconnect the __item__ binding.
!- Similarly, disconnect the __value__ bindings for each of the three string elements.

## Delete the movieRole variable

- Select the __movieRole__ variable in the object browser.
- Click the delete button.
!

Recall that the __movieRole__ variable was created automatically when you bound __movies__ ! __movieRoles__ to the repetition's __list__ attribute. Since you disconnected the __list__ and __item__ bindings, you don't need the __movieRole__ variable anymore.

## Create a second WODisplayGroup

- Drag the MovieRole entity from your model file into the MovieDetails component window.

WebObjects Builder creates a variable named __movieroles__ in the MovieDetails component. __movieroles__ is a WODisplayGroup that manages MovieRole objects.

## Set up a master-detail relationship

As is, the __movieroles__ display group manages _all_ the movie roles in the database, but it should manage only the MovieRole objects that are related to the selected movie. To restrict the objects that __movieroles__ manages, you need to set up a _master-detail_ relationship between the __movieroles__ and __movies__ display groups.

- Add the following __init__ method to MovieDetails' script:

```
    - init {
        [super init];
        [movieroles setDataSource:[[movies dataSource]
            dataSourceQualifiedByKey:@"movieRoles"]];
        return self;
    }
```


The first line of this __init__ method invokes any initialization performed by the object's superclass. Whenever you implement an __init__ method, include a call to the super class's __init__ method. If you omit the call to __super__, your objects won't be fully initialized.
The second line of this method assigns a new data source to the __movieroles__ display group. A data source-an instance of an EODataSource subclass-is an object that defines a basic interface for providing enterprise objects. It exists primarily as a simple means for a WODisplayGroup or other higher-level class to access a store of objects. For example, when you tell a display group to fetch, it does so by telling its data source to fetch.
To restrict the objects that __movieroles__ displays, you need to replace __movieroles__' data source with a _detail data source_. A detail data source is a data source that qualifies (restricts) its set of enterprise objects to an object that's selected in a _master data source_. A detail data source is set up to provide objects for the destination entity of a particular relationship.
The following expression:

```
[[movies dataSource] dataSourceQualifiedByKey:@"movieRoles"]
```


gets the data source from the __movies__ display group and asks it to provide a detail data source. The data source returned by __dataSourceQualifiedByKey:__ is set up to provide MovieRole objects that are related to one of __movies__' enterprise objects through the __movieRoles__ relationship.

## Qualify the detail data source

In a master-detail setup, changes to the detail apply to the objects in the master; for example, adding an object to the detail also adds it to the relationship of the _master object_. Once you have a detail data source, you can set the master object by sending the detail a __qualifyWithRelationshipKey:ofObject:__ message. The detail then uses the master object in evaluating the relationship and applies inserts and deletes to that master object. In the MovieDetails page, this plays out as follows: If you insert a new MovieRole object in the __movieroles__ display group, it is also added to the __movieRoles__ array of the selected Movie object.

- Modify the __setMovie:__ method to look like this:

```
    - setMovie:aMovie {
        if (aMovie)
            [movies setObjectArray:[NSArray
                arrayWithObject:aMovie]];
        else
            [movies setObjectArray:nil];
        [movies selectObject:aMovie];

        // Add the following lines.
        [[movieroles dataSource]
                qualifyWithRelationshipKey:@"movieRoles"
                ofObject:aMovie];
        [movieroles fetch];
    }
```


## Create the repetition bindings

- Bind the __movieroles__ ! __displayedObjects__ method to the repetition's __list__ attribute.

WebObjects Builder adds the __movieRole__ variable back and automatically binds it to the repetition's __item__ attribute.

__movieRole__'s __displayedObjects__ method returns an array of roles in the selected movie. In general, WODisplayGroup's __displayedObjects__ method returns the list of objects that you want to display.

Typically, a display group's object array contains more objects than the display group makes available for display. Most display groups fetch all of the objects in the database, and you usually do not want to display all of the objects in the database. To display fewer objects, you associate a qualifier with the display group. After the display group has performed the fetch, it applies the qualifier to the fetched objects. __displayedObjects__ returns an array that either contains the entire array of objects after the qualifier has been applied, or if the batch size is greater than 0, it returns the objects in the current batch.

For example, suppose there are one thousand records in the database. A typical display group would fetch all one thousand records. Then suppose the display group had a qualifier that narrows the list down to one hundred objects that should eventually be displayed. If the batch size is 0 (indicating that the display is not being batched), __displayedObjects__ returns all one hundred objects that should be displayed. If the batch size is ten, __displayedObjects__ returns the ten objects out of those one hundred that currently should be displayed. When the page is loaded, __displayedObjects__ returns the first ten objects. When the Next Page button is clicked, __displayedObjects__ returns the next ten objects, and so on.

- Bind __movieRole__ ! __talent__ ! __firstName__ to the first string element.
- Bind __movieRole__ ! __talent__ ! __lastName__ to the second string element.
- Bind __movieRole__ ! __roleName__ to the last string element.

[!Table of Contents](Movies.book.md) [!Next Section](7_InUpDe.md)
