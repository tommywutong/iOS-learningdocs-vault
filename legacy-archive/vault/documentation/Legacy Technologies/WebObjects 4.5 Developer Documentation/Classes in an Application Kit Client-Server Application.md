---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/EOFClasses2.html
archived_at: '2026-07-15T08:03:01.733444Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Enterprise%20Objects%20Framework%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](Classes%20in%20a%20Command-Line%20Program.md)

# Classes in an Application Kit Client/Server Application

An Application Kit client/server application uses an architecture similar to that in a command-line program, but it incorporates classes to synchronize values between enterprise objects and the application's user interface. This section describes the roles of those classes and how they fit into the application's architecture.

!

Figure 16. Classes in an Application Kit Application

## User Interface Objects

In a traditional client/server application such as the one described in this chapter, Application Kit user interface objects (such as NSPopUpButtons, NSForms, NSTextFields, and NSTableViews) are used to display the values of enterprise objects. When values are edited in the user interface, these same Application Kit objects are used to communicate the changes back to the enterprise objects. In [Figure 16](#apple-geydgnzq), Application Kit classes are represented by a screen capture of a real application's user interface.

## The Interface Layer

The interface layer in an Application Kit application synchronizes data between the application's user interface (Application Kit objects) and the control layer's graph of enterprise objects. The relationship between user interface objects and enterprise objects is managed by EODisplayGroup objects. More precisely, display groups are used by EOAssociation objects to mediate between enterprise objects and the user interface. EOAssociations link a single user interface object to one or more class properties (keys) of the objects managed by a display group. The properties' values are displayed in the association's user interface object.
In the Interface layer, EOAssociation objects "observe" EODisplayGroups to make sure that the data displayed in the user interface remains consistent with enterprise object data. Display Groups interact with data sources, which supply them with enterprise objects.

## Access and Control Layers

The roles of the access and control layers in an Application Kit application are the same as they are in a command-line application. However, in an Application Kit application, each layer supplies a _data source_ for interacting with the interface layer.
A data source is a subclass of the EODataSource abstract class that presents an EODisplayGroup object with a standard interface to a store of enterprise objects. From the perspective of the EODisplayGroup to which a data source supplies enterprise objects, the actual mechanism used for storing data is of no concern; everything below the data source is effectively a "black box." The interface layer interacts with all data sources in the same way. A data source takes care of communicating with the external data store to fetch, insert, update, and delete objects.
For most database applications, data sources are instances of EODatabaseDataSource or EODetailDataSource (the data source classes supplied with the Framework). EODatabaseDataSource, defined in EOAccess, provides an interface to the Framework's access layer and ultimately, to a relational database. However, the data source can be any object that is a subclass of the abstract class EODataSource. Thus, the user interface layer can be used independently from the access layer for other types of data sources, such as an array of objects constructed by an application, or objects fetched from a flat-file database or a newsfeed.
Data sources can be arranged in master-detail configurations to support master-detail displays. For example, suppose an application displays movie studios in one table and the movies for the selected studio in another table. Selecting a new studio updates the movies table to display the movies for the newly selected studio. To support this user interface, the application has a master data source for Studio objects and a detail data source for Movie objects. Based on a relationship between Studio and Movie (a studio has many movies), the detail data source limits its Movie objects to those associated with the Studio that's selected in the application's user interface.
Most often the master data source is an EODatabaseDataSource, while the detail is an EODetailDataSource. EODetailDataSource is provided by the control layer, and is a general purpose data source for master-detail configurations.

[!Table of Contents](Enterprise%20Objects%20Framework%20Viewed%20Through%20Its%20Classes.md) [!Next Section](Classes%20in%20an%20HTML%20WebObjects%20Application.md)
