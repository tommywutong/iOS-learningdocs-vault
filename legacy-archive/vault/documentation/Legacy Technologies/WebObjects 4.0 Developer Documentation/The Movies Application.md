---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies1.html
archived_at: '2026-07-18T01:21:46.242193Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Creating%20a%20WebObjects%20Database%20Application.md)

# The Movies Application

The Movies application has two pages, each of which allows you to access information from the database in different ways:

- _MovieSearch_ (the main page) lets you search for movies that match user-specified criteria. For example, you can search for all comedies starting with the letter "A". Once you find the movie you're looking for, you can make changes to its data or delete it. You can also use this page to insert new movies into the database.
- _MovieDetails_ displays the actors who star in a selected movie and the roles those actors play. You can add new roles, change the name of a role, and assign a different actor to a role.

!

## Enterprise Objects and the Movies Database

Enterprise Objects Framework manages the interaction between the database and objects in the Movies application. Its primary responsibility is to fetch data from relational databases into _enterprise objects_. An enterprise object, like any other object, couples data with methods for operating on that data. In addition, an enterprise object has properties that map to stored data. Enterprise object classes typically correspond to database tables_._ An enterprise object instance corresponds to a single row or record in a database table.
The Movies application centers around three kinds of enterprise objects: Movies, MovieRoles, and Talents. A movie has many roles, and talents (or actors) play those roles.
The Movie, MovieRole, and Talent enterprise objects in the Movies application correspond to tables in a relational database. For example, the Talent enterprise object corresponds to the TALENT table in the database, which has LAST_NAME and FIRST_NAME columns. The Talent enterprise object class in turn has __lastName__ and __firstName__ instance variables. In an application, Talent objects are instantiated using the data from a corresponding database row, as shown in the following figure:

!

## Enterprise Objects and Relationships

Relational databases model not just individual entities, but entities' relationships to one another. For example, a movie has zero, one, or more roles. This is modeled in the database by both the MOVIE table and MOVIE_ROLE table having a MOVIE_ID column. In the MOVIE table, MOVIE_ID is a _primary key_, while in MOVIE_ROLE it's a _foreign_ _key_.
A _primary key_ is a column or combination of columns whose values are guaranteed to uniquely identify each row in that table. For example, each row in the MOVIE table has a different value in the MOVIE_ID column, which uniquely identifies that row. Two movies could have the same name but still be distinguished from each other by their MOVIE_IDs.
A _foreign key_ matches the value of a primary key in another table. The purpose of a foreign key is to identify a relationship from a source table to a destination table. In the following diagram, notice that the value in the MOVIE_ID column for both MOVIE_ROLE rows is 501. This matches the value in the MOVIE_ID column of the "Alien" MOVIE row. In other words, "Ripley" and "Ash" are both roles in the movie "Alien."

!

Suppose you fetch a Movie object. Enterprise Objects Framework takes the value for the movie's MOVIE_ID attribute and looks up movie roles with the corresponding MOVIE_ID foreign key. The framework then assembles a network of enterprise objects that connects a Movie object with its MovieRole objects. As shown below, a Movie object has an array of its MovieRoles, and the MovieRoles each have a Movie.

!

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Designing%20the%20Main%20Page.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
