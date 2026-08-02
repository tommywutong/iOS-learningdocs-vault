---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Movies/0_Intro.html
archived_at: '2026-07-15T07:48:50.917245Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Movies.book.md) [!Previous Section](Movies.book.md)

# The Movies Application

The application has three pages: "Browse Movies," "Movie Search," and "Movie Details." The Browse Movies and Movie Search pages of the Movies application let you browse the movies that are in a database and search for movies that match user-specified criteria. For example, you can search for all comedies starting with the letter "T" that have an R rating. You can also use these pages to insert, update, and delete movie records.
!
Movies also has a Movie Details page that displays the actors who star in a selected movie and the roles that the actors play. From this page, you can add new roles to a movie, change the name of a role, and assign a different actor to a role.!
In this tutorial, you'll learn the basic things you must do to create a WebObjects application that uses Enterprise Objects Framework. You'll discover how to use WebObjects Builder to create web pages that access a database and how to work with models in EOModeler.

# Enterprise Objects and the Movies Database

Enterprise Objects Framework manages the interaction between the database and objects in the Movies application. Its primary responsibility is to fetch data from relational databases into _enterprise objects_. The Movies application centers around three enterprise objects: Movie, MovieRole, and Talent. A movie has many roles; actors, or _talent_, play those roles.
An enterprise object is like any other object in that it couples data with methods for operating on that data. However, an enterprise object class has certain characteristics that distinguish it from other classes:

- It has properties that map to stored data; an enterprise object instance typically corresponds to a single row or record in a database.
- It knows how to interact with WebObjects Framework and Enterprise Objects Framework to give and receive values for its properties.

The ingredients that make up an enterprise object are its class definition and the data values from the database row or record with which the object is instantiated.
The Movie, MovieRole, and Talent enterprise objects in the Movies application correspond to tables in a relational database. For example, the Talent enterprise object corresponds to the TALENT table in the database, which has LAST_NAME and FIRST_NAME columns. The Talent enterprise object class in turn has __lastName__ and __firstName__ instance variables, or class properties. (Instance variables based on database data are called class properties.) In an application, Talent objects are instantiated using the data from a corresponding database row, as shown in the following figure:!

[!Table of Contents](Movies.book.md) [!Next Section](1_Main.md)
