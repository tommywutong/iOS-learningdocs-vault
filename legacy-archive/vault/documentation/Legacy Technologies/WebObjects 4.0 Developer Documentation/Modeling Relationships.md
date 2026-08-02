---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/EOsII2.html
archived_at: '2026-07-18T01:19:42.922919Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Advanced%20Enterprise%20Object%20Modeling.md) [!Previous Section](Modeling%20Complex%20Attributes.md)

# Modeling Relationships

How you model relationships is perhaps the most complex and interesting part of a database-to-objects mapping. This section describes some of the finer points of relationship modeling.

## Modeling Optional To-One Relationships

A to-one relationship is optional if the relationship's destination object can be __null__ (__nil__ in Objective-C). For example, a Member entity's __creditCard__ relationship is optional if a Member object isn't required to have a CreditCard object.
__Note:__  Occasionally, a mandatory to-one relationship doesn't resolve to a destination object. For example, suppose your application's Movie database contains legacy data for which relational integrity constraints weren't strictly enforced. As a result, some Movies don't have corresponding Studios even though the Movies-to-Studios relationship is mandatory. The techniques for handling these errant to-one relationships are the same as those for handling optional to-one relationships.
You can model an optional to-one relationship many different ways, depending on how you represent the relationship in the database-as a _foreign key to primary key join_ or as a _primary key to primary key join_.
__Note:__  For to-one relationships, Enterprise Objects Framework doesn't support primary key to foreign key joins. The destination join attribute in a to-one relationship must be the destination entity's primary key.
Using a foreign key to primary key join, you include the destination row's primary key in the source row. For example, in the relationship shown in [Figure 24](#apple-ha4dcmq), the __creditCard__ relationship's source table (MEMBER) has a foreign key (CARD_NUMBER) to the destination table (CREDIT_CARD). Using this approach, you can model an optional
to-one relationship as a true to-one relationship just as you would model a mandatory to-one relationship.

!

Figure 24. Storing a Foreign Key in the Source Table

A foreign key to primary key join is the best way to model a to-one relationship for use with Enterprise Objects Framework. If you have control over the design of the database schema, use foreign key to primary key joins for to-one relationships whenever possible.
Alternatively, you can use a primary key to primary key join that includes the source's primary key in the destination table. For example, in the relationship shown in [Figure 25](#apple-heztm), the __talentPhoto__ relationship's destination table (TALENT_PHOTO) has a foreign key (TALENT_ID) to the source table (TALENT). For reasons described below, this arrangement requires special handling.

!

Figure 25. Storing a Foreign Key in the Destination Table

When Enterprise Objects Framework fetches an enterprise object, it attempts to assign destination objects to any of the object's to-one relationships. If a destination object hasn't already been fetched, Enterprise Objects Framework creates a fault to stand in for the destination object until it is actually needed. (For more information on faulting, see the chapter["Behind the Scenes"](Behind%20the%20Scenes.md#apple-ha2tqni).)

The exception to this is when the relationship is based on a foreign key to primary key join and the relationship's source object doesn't have a corresponding destination. Instead of creating a fault, Enterprise Objects Framework assigns __null__ (or __nil__ in Objective-C) to the source object's relationship property. For example, if a Member doesn't have a corresponding CreditCard, the corresponding MEMBER record's CARD_NUMBER value is NULL. When Enterprise Objects Framework sees the null-valued CARD_NUMBER attribute, it sets the Member's __creditCard__ property to __null__.
On the other hand, Enterprise Objects Framework can't detect that a primary key to primary key relationship doesn't have a destination. For example, Enterprise Objects Framework can't tell that a TALENT record doesn't have a corresponding TALENT_PHOTO record until it tries to fetch a TALENT_PHOTO with the same TALENT_ID value and fails. Consequently, in a primary key to primary key relationship, Enterprise Objects Framework always assigns a fault if a corresponding destination object hasn't been fetched. If no such destination exists, Enterprise Objects Framework throws an exception when it tries to resolve the fault.
An optional primary key to primary key relationship (such as __talentPhoto__) can be handled in a number of ways:

- _Model the relationship as a mandatory to-one, but allow the destination entity to have_ __null___-valued attributes._ For example, assume that a relationship between Customers and Addresses is optional. To model the relationship as a mandatory to-one, Customers who don't provide their Addresses have corresponding Address objects with __null__-valued __streetAddress__, __city__, __state__, and __zip__ attributes. The Customers also have Address rows in the database, but the Address rows contain NULLs in all the columns except the primary key column (whose value matches that of the corresponding Customer).

This approach is a good choice when the destination object contains what are conceptually attributes of the source object. For example, conceptually __photo__ is an attribute of a Talent object. It's implemented using a to-one relationship for performance reasons. (Photo data is very large, and isn't fetched unless-and until-it's needed.)

- _Model the relationship as a to-many._ This approach is useful when you think that a to-one relationship may evolve into a to-many relationship in the future. For example, current requirements for a Movie application specify that a Talent object may only have one photo. However, the requirements for the next version of the application mention a Talent's portfolio.
- _Handle the exception thrown by faults that don't correspond to a destination object._ This approach is probably the best for handling optional to-one relationships based on primary key to primary key joins.
- I_mplement the delegate method_ __databaseContextFailedToFetchObject__ (__databaseContext:failedToFetchObject:globalID:__ in Objective-C). This approach is best for handling mandatory to-one relationships with errant data (source rows that don't have corresponding destinations).

The following sections describe each approach.

### Use a Mandatory To-One Relationship

This approach is used for the Movies database to model Talent's __talentPhoto__ relationship. Although a Talent object doesn't have to have a photo, it does have to have a corresponding TalentPhoto object. As shown in [Figure 26](#apple-guzdm), a Talent object that doesn't have a photo has a TalentPhoto object whose __photo__ attribute is __null__ (__nil__ in Objective-C).

!

Figure 26. A Destination Object with null-Valued Attributes

This approach doesn't require any code. In the Advanced Relationship Inspector for the Talent entity's __talentPhoto__ relationship, you simply set the relationship to _propagate primary key_. Propagate primary key tells Enterprise Objects Framework to propagate the primary key of the source entity into newly inserted objects in the destination entity (instead of generating a primary key value for the destination). With this configuration, Enterprise Objects Framework inserts a new Talent object, it inserts a corresponding TalentPhoto object if the Talent object doesn't already have one assigned to it.

### Use a To-Many Relationship

To-many relationships use a different faulting mechanism than to-ones. A fault for a to-many relationship replaces itself with an NSArray of corresponding destination objects, and it doesn't throw an exception if it doesn't find any. If you use a to-many relationship to model an optional to-one and no destination object exists, the array is simply empty. If the relationship does have a destination object, it's the first and only object in the array.
You can design your enterprise object's API to hide the to-many implementation. For example, suppose that Talent's __talentPhoto__ relationship was modeled as a to-many. To design a Talent enterprise object that acts as if its __talentPhoto__ relationship is an optional to-one, you could name the to-many relationship (and the corresponding instance variable) "_talentPhotoArray" and implement the following two accessor methods:
In Java:

```
public void setTalentPhoto(TalentPhoto talentPhoto)
{
    willChange();
    _talentPhotoArray.removeAllObjects();
    if (talentPhoto != null)
        _talentPhotoArray.addObject(talentPhoto);
}

public TalentPhoto talentPhoto()
{
    willRead();
    if (_talentPhotoArray.count() > 0)
        return _talentPhotoArray.objectAtIndex(0);
    return null;
}
```


In Objective-C:

```objc
- (void)setTalentPhoto:(TalentPhoto *)talentPhoto
{
    [self willChange];
    [_talentPhotoArray removeAllObjects];
    if (_talentPhotoArray)
        [_talentPhotoArray addObject:talentPhoto];
}

- (id)talentPhoto
{
    if ([_talentPhotoArray count])
        return [_talentPhotoArray objectAtIndex:0];
    return nil;
}
```


### Handle the Exception

You can use a to-one relationship if you handle any exceptions that are thrown when a fault doesn't resolve to a destination object. For example, in the Talent enterprise object, you would implement the __talentPhoto__ relationship "get" method as follows:
In Java:

```
public TalentPhoto talentPhoto()
{
    try {
        // If the receiver is a fault, sending it a willRead
        // message attempts to resolve it.  If the
        // corresponding row doesn't exist in the database,
        // an exception is thrown.
        talentPhoto.willRead();
    } catch (NSException e) {
        talentPhoto = null;
    }

    return talentPhoto;
}
```


In Objective-C:

```objc
- (TalentPhoto *)talentPhoto
{
    NS_DURING
        // If the receiver is a fault, sending it a self
        // message attempts to resolve it.  If the
        // corresponding row doesn't exist in the database,
        // an exception is raised.
        [talentPhoto self];
    NS_HANDLER
        [talentPhoto autorelease];
        talentPhoto = nil;
    NS_ENDHANDLER

    return talentPhoto;
}
```


Sending __willRead__ (or __self__ in Objective-C) to a fault triggers it to fetch its corresponding enterprise object. If a Talent instance doesn't have a corresponding TalentPhoto, sending __willRead__ to the __talentPhoto__ property throws an exception. In the __talentPhoto__ method above, the exception handler simply sets the property to __null__ (first autoreleasing the __talentPhoto__ fault in Objective-C).

### Implement databaseContextFailedToFetchObject

With the EODatabaseContext delegate method __databaseContextFailedToFetchObject__ (__databaseContext:failedToFetchObject:globalID:__ in Objective-C), you can prevent an exception from being thrown when a fault doesn't resolve to a destination object. This method is invoked when a fault for a to-one relationship can't find its corresponding object in the database. By returning __false__ (NO in Objective-C), you can prevent the EODatabaseContext from raising an exception.
For example, to handle mandatory to-one relationships with errant data (source rows that don't have corresponding destinations), you could implement the delegate method to insert the empty object, thereby supplying the missing destination object:
In Java:

```
public boolean databaseContextFailedToFetchObject(
    EODatabaseContext context,
    Object object,
    EOGlobalID gid)
{
    // Perform a check to determine whether to intervene
    if (...) {
        // Set values in your object (if necesssary).
        object.editingContext().insertObject(object);
        return false;
    }
    return true;
}
```


In Objective-C:

```objc
- (BOOL)databaseContext:(EODatabaseContext *)context
    failedToFetchObject:(id)object
    globalID:(EOGlobalID *)gid
{
    // Perform a check to determine whether to intervene
    if (...) {
        // Set values in your object (if necesssary).
        [[object editingContext] insertObject:object];
        return NO;
    }
    return YES;
}
```


In the above implementations, the delegate method first checks to see if it should intervene. For example, the method might check to see if __object__ is an instance of the TalentPhoto class. If the delegate determines that __object__ represents a destination object that's missing from the database, the delegate queues __object__ for insertion into the database by inserting it into its editing context. It returns __false__ (NO in Objective-C) indicating that the delegate has handled the error and that the EODatabaseContext shouldn't throw an exception.

## Modeling Many-To-Many Relationships

To model a many-to-many relationship between objects is simple: each object manages a collection of the other kind. For example, consider the many-to-many relationship between employees and projects. To model this relationship in objects, an Employee has an NSArray, __projects__, of all the projects he or she works on; and a Project class has an NSArray, __employees__, of all its members.
To model a many-to-many relationship in a database, you have to create an intermediate table (also known as a _correlation_ or _join_ table). For example, the database for employees and projects might have EMPLOYEE, PROJECT, and EMP_PROJ tables, where EMP_PROJ is the correlation table. The appendix "Entity-Relationship Modeling" provides more information on the tables behind a many-to-many relationship.
Given the relational database representation of a many-to-many, how do you get the object model you want? You don't want to see evidence of the correlation table in your object model, and you don't want to write code to maintain database correlation rows. With Enterprise Objects Framework, you don't have to. Simply use flattened relationships as described in the chapter "Using EOModeler" to hide your correlation tables.
A model with the following features has the effect of hiding the EMP_PROJ correlation table from its object model altogether:

- Employee and Project entities whose to-many relationships to the EmpProj entity (__toEmpProj__) are not class properties.
- The flattened relationships __projects__ and __employees__ in Employee and Project, respectively, are class properties.

Consequently, EmpProj enterprise objects are never created, Employees have an array of related Projects, and Projects have an array of related Employees. Furthermore, Enterprise Objects Framework automatically manages rows in the EMP_PROJ correlation table.
However, what do you do when a correlation table contains extra attributes that are interesting? For example, the MOVIE_ROLE table in the sample Movies database is a correlation table between movies and the actors who star in them. In addition to foreign keys for MOVIE and TALENT, the MOVIE_ROLE table also contains the name of the role the actor plays in the film. In this case, MovieRole enterprise objects actually have a place in the object model even though they're fetched from a correlation table.
If you want to programmatically access both a Movie's roles and its actors directly from the Movie object, you should do the following:

- Create a __movieRole__ relationship from Movie to MovieRole and set it to be a class property.
- Create a __talent__ relationship from MovieRole to Talent.
- Define an __actors__ method in the Movie class that returns the Talent objects by getting them from the corresponding MovieRoles.

Because MovieRole corresponds to a data-bearing correlation table, you shouldn't create a flattened relationship from Movie to Talent. If your application fetches correlation records as enterprise objects, consistency problems can arise if it also manages a flattened relationship. For example, suppose you did flatten the __talent__ relationship into the Movie entity. Movie objects would then have an array of MovieRole objects and an array of Talent objects. If your application adds a new MovieRole to a Movie's __roles__ array, the corresponding __actors__ array doesn't reflect the addition until the new MovieRole is saved to the database and the Movie is refetched.
Instead, if you create an __actors__ method that traverses the object graph through the Movie's MovieRole objects, you avoid any consistency problems.
For display purposes, you don't even need an accessor method to bypass a correlation object. Instead, you can use key paths. For example, you can use the key path __roles.talent__ to access a Movie's Talent objects in a master-detail configuration between a Movie EODisplayGroup and a Talent EODisplayGroup.

[!Table of Contents](Advanced%20Enterprise%20Object%20Modeling.md) [!Next Section](Modeling%20Inheritance.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
