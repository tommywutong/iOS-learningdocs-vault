---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.6.html
archived_at: '2026-07-15T08:00:23.126123Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Post-Install Guide](About%20This%20Document.md)

[!Table of Contents](About%20This%20Document.md) [!Previous Section](Using%20Microsoft%20Access.md)

#   Setting Up the Sample Databases

WebObjects includes Enterprise Objects Framework database integration technology. If you've installed WebObjects Developer, several examples demonstrate Enterprise Objects Framework programming techniques. In particular, if you work through the tutorials in the book _Getting Started With WebObjects,_ you'll need two sample databases: Movies, which contains background information on all movies available form a store's distributor, and Rentals, which contains the inventory, customer list, and rental transaction records for the store. In addition, WebObjects ships with an example application named Movies, which uses a database of Movies, their ratings, and principal actors. The section _[Verifying the Installation](Verifying%20the%20Installation.md#apple-gu3tsnju)_ uses Movies to verify that the installation is working properly.

> 
>
>
> ---
>
> Warning: None of the data in the sample databases is intended to be accurate.
>
> ---

All of the examples supplied with this release come pre-built, and are runnable directly from their distribution directories. Those that use the Enterprise Objects Framework run "out of the box" against the supplied OpenBaseLite databases. On Mac OS X Server and Windows NT systems, you can invoke the Setup Wizard to reconfigure the example application models to use another supported database, such as Oracle or Sybase, and to optionally load the database for you. The Setup Wizard copies the examples into a directory of your choosing before modifying them.

For WebObjects 4.0, the Setup Wizard doesn't completely perform all operations necessary to get the examples running. In particular, it doesn't convert the models in the BusinessLogicInheritance framework, and it doesn't load the inheritance model data into a database. However, it does work correctly on the BusinessLogic framework; thus, the simpler examples that don't use interitance will work correctly with your database after you run the SetupWizard and perform a few additional manual steps.

##  Running the Setup Wizard

SetupWizard.app is located in __/System/Developer/Examples/EnterpriseObjects__
(on Windows NT systems, _NEXT_ROOT___\Developer\Examples\EnterpriseObjects__
). After you invoke the wizard, you'll be prompted for a directory into which the examples should be installed. _This directory must already exist in order for the wizard to work properly._

> 
>
>
> ---
>
> Warning: The wizard will delete any existing contents of the directory you specify.
>
> ---

After advancing to the next screen, follow the prompts through the rest of the wizard. Note that you `ll need to select a database adaptor and login to the database twice: once for Movies, and once for Rentals. Finally, the wizard will ask you whether or not you want it to populate the selected databases for you.

After running the Setup Wizard, you'll need to perform a couple of additional steps. These steps are outlined in a separate online document, ExampleGuide.rtfd, which is located in the same directory in which the Setup Wizard itself is located (__.../Examples/EnterpriseObjects__).

[!Table of Contents](About%20This%20Document.md) [!Next Section](Verifying%20the%20Installation.md)
