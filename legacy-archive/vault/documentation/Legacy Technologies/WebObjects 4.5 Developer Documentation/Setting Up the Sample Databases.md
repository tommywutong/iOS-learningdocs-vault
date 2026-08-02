---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.26.html
archived_at: '2026-07-15T08:09:31.887141Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Post-Installation%20Steps.md) [!](Creating%20Data%20Sources%20and%20Databases.md) [!](Running%20the%20Setup%20Wizard.md)

---

#   Setting Up the Sample Databases

WebObjects includes Enterprise Objects Framework database integration technology. If you've installed WebObjects Developer, several examples demonstrate Enterprise Objects Framework programming techniques. In particular, if you work through the tutorials in the book _Getting Started With WebObjects_
, you'll need two sample databases: Movies, which contains background information on all movies available form a store's distributor, and Rentals, which contains the inventory, customer list, and rental transaction records for the store. In addition, WebObjects ships with an example application named Movies, which uses a database of Movies, their ratings, and principal actors. The section [Verifying the Installation](Verifying%20the%20Installation.md)
uses Movies to verify that the installation is working properly.

> __Warning:__None of the data in the sample databases is intended to be accurate.

All of the examples supplied with this release come pre-built, and are runnable directly from their distribution directories. Those that use the Enterprise Objects Framework run "out of the box" against the supplied OpenBaseLite databases. On Mac OS X Server and Windows NT systems, you can invoke the Setup Wizard to reconfigure the example application models to use another supported database, such as Oracle or Sybase, and to optionally load the database for you. The Setup Wizard copies the examples into a directory of your choosing before modifying them.

For WebObjects 4.5, the Setup Wizard doesn't completely perform all operations necessary to get the examples running. In particular, it doesn't convert the models in the BusinessLogicInheritance framework, and it doesn't load the inheritance model data into a database. However, it does work correctly on the BusinessLogic framework; thus, the simpler examples that don't use inheritance will work correctly with your database after you run the SetupWizard and perform a few additional manual steps.

#### [Running the Setup Wizard](Running%20the%20Setup%20Wizard.md#apple-obtwmslehuytamrsgi)

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Post-Installation%20Steps.md) [!](Creating%20Data%20Sources%20and%20Databases.md) [!](Running%20the%20Setup%20Wizard.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
