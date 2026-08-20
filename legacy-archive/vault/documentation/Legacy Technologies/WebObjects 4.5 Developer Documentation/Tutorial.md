---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.c.html
archived_at: '2026-07-15T08:09:18.010636Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Creating%20a%20Java%20Client%20WebObjects%20Application.md) [!](Programming%20With%20Java%20Client.md) [!](Requirements.md)

---

#   Tutorial

This tutorial shows you how to create a "Java Client" WebObjects application, which is a distributed Enterprise Objects Framework application that uses a Web browser as its display medium. The application is "distributed" in the sense that business logic can be shared among enterprise objects on the Web client (which are implemented in Java) and enterprise objects on the server (which can be implemented in Java or Objective-C). The steps you take to create a Java Client WebObjects application are remarkably similar to the steps you take to create a typical stand-alone (or "fat client") Enterprise Objects Framework application.

The application you'll be creating in this chapter, StudioManager, is based on the Movies sample database distributed with Enterprise Objects Framework (you must have the sample databases installed to do this tutorial). It centers around three types of enterprise objects: Studio, Movie, and Talent. Studios own movies, and they have a budget for buying new movies. Movies feature actors, or "talent." The StudioManager application lets you transfer movies between studios and buy all of the movies starring a particular actor. It also lets you add, modify, and delete studios.

The StudioManager example project upon which this tutorial is based is installed in _NEXT_ROOT___/Developer/Examples/WebObjects/JavaClient__.

#### [Requirements](Requirements.md#apple-obtwmslehuytambwga4do)

#### [Enterprise Objects and Relational Databases](Enterprise%20Objects%20and%20Relational%20Databases.md#apple-obtwmslehuytambwgeydc)

#### [What Goes Into the StudioManager Application](What%20Goes%20Into%20the%20StudioManager%20Application.md#apple-obtwm3dehuytambwgeyto)

#### [Creating the StudioManager Project](Creating%20the%20StudioManager%20Project.md#apple-obtwmslehuytambwgeztk)

#### [The Ingredients of a Java Client Project](The%20Ingredients%20of%20a%20Java%20Client%20Project.md#apple-obtwmslehuytambwgmztc)

#### [Verifying and Modifying the Model](Verifying%20and%20Modifying%20the%20Model.md#apple-obtwm3dehuytambwgqyti)

#### [Creating the User Interface](Creating%20the%20User%20Interface.md#apple-obtwmslehuytambwguyti)

#### [Building and Testing Your Application](Building%20and%20Testing%20Your%20Application.md#apple-obtwmslehuytambwgy2tk)

#### [Adding Relationships](Adding%20Relationships.md#apple-obtwmslehuytambwg42de)

#### [Transferring Movies Between Studios](Transferring%20Movies%20Between%20Studios.md#apple-obtwmslehuytambwha3te)

#### [Putting the Finishing Touches on Your Model](Putting%20the%20Finishing%20Touches%20on%20Your%20Model.md#apple-obtwm3dehuytambwhezde)

#### [Adding Behavior to Your Enterprise Objects](Adding%20Behavior%20to%20Your%20Enterprise%20Objects-2.md#apple-obtwmslehuytambwhe2tq)

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Creating%20a%20Java%20Client%20WebObjects%20Application.md) [!](Programming%20With%20Java%20Client.md) [!](Requirements.md)
