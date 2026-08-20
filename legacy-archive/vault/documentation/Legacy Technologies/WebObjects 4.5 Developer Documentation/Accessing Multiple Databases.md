---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/AppConfs5.html
archived_at: '2026-07-15T08:02:49.499468Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Application%20Configurations.md) [!Previous Section](Object%20Store%20Coordinator%20Configurations.md)

# Accessing Multiple Databases

Enterprise Objects Framework applications access multiple databases almost transparently. Simply make different models for each database, and then you can create relationships from an entity in one database to an entity in another. In your application, you can fetch enterprise objects from different databases into the same object graph without any extra work. See the chapter "Using EOModeler" for more information.
However, there are a couple of pitfalls that can occur when you're working with more than one database:

- Enterprise Objects Framework doesn't implement a two-phase commit.
- EODatabaseDataSources with models for different databases can erroneously rendezvous on the same EODatabaseContext.

The following sections describe these problems and what you can do about them.

## Getting By Without Two-Phase Commit

When an EOEditingContext has changes that need to be saved in multiple databases, the editing context's underlying EOObjectStoreCoordinator guides its EOCooperatingObjectStores (usually EODatabaseContexts) through a multi-pass save protocol in which each cooperating store saves its own changes and forwards remaining changes to other cooperating stores.
Although a coordinator manages objects from multiple repositories, it doesn't guarantee consistent updates when saving changes across object stores. If your application requires guaranteed distributed transactions, you can either provide your own solution by creating a subclass of EOObjectStoreCoordinator that integrates with a TP monitor, use a database server with built-in distributed transaction support, or design your application to write to only one object store per save operation (though it may read from multiple object stores). For more discussion of this subject, see the EOObjectStoreCoordinator class specification in the _Enterprise Objects Framework Reference_.

## Preventing Database Context Rendezvousing

As described in ["Database Context Rendezvousing"](Graphical%20User%20Interface%20Applications.md#apple-g43donq), EODatabaseDataSources automatically rendezvous on the same EODatabaseContexts to minimize the number of database connections an application creates. For example, in an application that accesses only one database, all the database data sources share the same database context by default. In an application that accesses two databases, there are two database contexts by default (one for each database); and as shown in [Figure 45](#apple-g4zdqnq), a database data source uses one or the other of the database contexts depending on the database with which its entity is associated.

!

Figure 45. Sharing EODatabaseContexts

Enterprise Objects Framework determines whether or not an database data source should rendezvous with an existing database context based on the data source's model. If the data source's model is _compatible_ with an database context's model, then the database data source can use the database context.
Two models are compatible when their connection dictionaries are equal. Thus, if you don't assign connection information to your models, database data sources can erroneously rendezvous with the same database context. For example, suppose an application uses two databases. The application contains two EODisplayGroups, each representing an entity from a different database. Further suppose that the models for the databases don't contain any connection information because the application requires the user to supply valid login information. In this scenario, the database data sources for each display group rendezvous on the same database context, which causes an error. Here's how it happens:

- The first database data source is unarchived. During unarchiving, it connects a database context using the method __registeredDatabaseContextForModel__ (__registeredDatabaseContextForModel:editingContext:__ in Objective-C). This EODatabaseContext static method (class method in Objective-C) checks to see if a database context that can service the data source's model already exists. Since this is the first database data source to be unarchived, there isn't an database context available at all, so one is created.
- In the process of creating the database context, the adaptor specified in the model is loaded. An EOAdaptor is instantiated, and the new database context is associated with this adaptor.
- The second database data source is unarchived. When __registeredDatabaseContextForModel__ is invoked this time, it returns the existing database context because the models for the two data sources are considered compatible.

At this point, two database data sources share a database context that represents a single database session; but two database contexts are actually needed. When the second data source attempts to interact with its database, it fails because it's using a connection to the wrong database.
The simplest way to prevent rendezvousing is to assign distinct connection dictionaries to your model files. You don't have to assign complete connection dictionaries. The dictionaries associated with different databases simply must differ in one or more entries.
Alternatively, you can programmatically assign complete connection dictionaries to your models before any EODatabaseDataSource objects are created-at application initialization time, for example. The best way to access your models is through the default EOModelGroup. The __models__ method returns an array of all the EOModels used by the application.
[!Table of Contents](Application%20Configurations.md) [!Next Section](Connecting%20to%20a%20Database.md)
