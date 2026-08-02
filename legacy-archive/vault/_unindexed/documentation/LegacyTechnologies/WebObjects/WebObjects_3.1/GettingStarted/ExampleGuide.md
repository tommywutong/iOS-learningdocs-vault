---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/ExampleGuide.html
archived_at: '2026-07-15T07:48:31.980994Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


# Enterprise Objects Framework Example Guide

_For WebObjects Release 3.x_

WebObjects includes Enterprise Objects Framework database integration technology and several examples that demonstrate Enterprise Objects Framework programming techniques. The Enterprise Objects Framework examples are built around the idea of a video rental store. The rental store uses two separate databases. The first database, Movies, contains background information on all movies available from the store's distributor. The second database, Rentals, contains the inventory, customer list, and rental transaction records for the store. __Disclaimer:__ __none of the data in the Movies database is guaranteed to be accurate.__

The Enterprise Objects Framework examples are located in: ___NEXT_ROOT_/NextDeveloper/Examples/EnterpriseObjects__

This guide describes:

[Installing the Sample Databases](#apple-irqxiylcmfzwk)
[The Examples](#apple-iv4gc3lqnrsxg)
[Building the Examples](#apple-ij2ws3denfxgo)

## Installing the Sample Databases

Before you can run the examples, you must set up the Movies and Rentals databases on your system. Installing the sample databases involves the following four steps:

1. __Setting up Database Accounts__

   The multi-database support in EOF 2.0 makes it possible for you to install the sample databases in three different configurations:

   - both sets of tables together in a single user/database
   - each set of tables in its own user/database on the same database server
   - each set of tables on its own database server (e.g. Movies on Informix, Rentals on Oracle).

   Depending on your desired set up, you use the tools available with your database server to set up one or two new user/databases. For example. on Sybase you might create a new database on your server called "Movies" and login with the user "sa". On Oracle you might create a new user with the name "Movies". Once you have set up these accounts, you are ready to install the examples.
2. __Copying the Example Directory__

   The database installation scripts make modifications to some of the example files based on your database set up, so you should copy the example directory to a directory that you can write in.
3. __Configuring the Example Models__

   The model files used by the examples must be configured to use your database and its adaptor. To configure the model files, simply run the __configure_examples__ program in a command shell. (To open a shell on NT, choose Sh in the OPENSTEP program group.) __cd__ to your copy of the examples directory, and run __configure_examples__. It asks you for the name of the adaptor you want to use (Informix, ODBC, Oracle, or Sybase) and for the login information for your database. It then modifies the example models to work with your server.
4. __Populating the Databases__

   To fill your example databases with sample data, use the __install_database__ program. in the DatabaseSetUp directory. In your command shell, __cd__ to the __DatabaseSetUp__ directory, and run __install_database__. It connects to your databases, adds the example tables, and fills them with data. If you later wish to remove the data, run the __drop_database__ program.

## The Examples

None of the examples in this directory are web-based. In fact, many of them require OpenStep Enterprise. Unless you have OpenStep Enterprise, you won't be able to build the following examples:

AssociationPalette
AssociationsApp
Customers
EOExtensions
Inventory
ModelerBundle
Movie
PointOfSale
Studios

However, the remaining examples may be useful to you as examples of how to program with Enterprise Objects Framework.

BusinessLogic
FlatFileAdaptor
ODBCAdaptor (NT only)
SimpleFetch
UsingStoredProcedures

For more information on these examples, see the __ExampleGuide.rtfd__ file in the EnterpriseObjects examples directory.

## Building the Enterprise Objects Examples

Building the examples requires two steps:

1. __Configuring Your Machine__

   __Window's Users:__ to install and run the examples your executable path environment variable must include:

   .;C:\NeXT\LocalDeveloper\Executables(The above assumes that __C:\NeXT__ is the root of your OpenStep installation). To check your path variable, use the System Control Panel. If the above isn't included, add it.

   __Mach Users:__ to install and run the examples you must create the directory __/LocalDeveloper/Frameworks__. This directory must be set to be writable by the user installing the examples.
2. __Building the Example Programs__

   With your example projects installed and your database filled with data, you are ready to build and run the examples. In a command shell, __cd__ to the example you want to build and type __make__.
