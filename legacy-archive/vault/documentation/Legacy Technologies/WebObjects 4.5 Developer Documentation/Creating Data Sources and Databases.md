---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.25.html
archived_at: '2026-07-15T08:09:31.383382Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Using%20Microsoft%20Access.md) [!](What%20You%20Need.md) [!](Setting%20Up%20the%20Sample%20Databases.md)

---

#  Creating Data Sources and Databases

After you've installed an ODBC driver for Access, you'll need to create databases and corresponding data sources for them. A data source simply stores the information needed to connect to your database. The easiest way to create an Access database and a corresponding data source from scratch is to create them both at the same time with the ODBC Data Source Administrator:

1. 

   Choose the ODBC option in the Control Panel.

   An ODBC Data Source Administrator panel opens.
2. 

   Click the System DSN tab.

   System data sources are accessible to all users, including NT services. It's important to create system data sources instead of user data sources, especially for use with WebObjects, because autolaunched applications aren't able to access user data sources.
3. 

   Click Add.

   The Create New Data Source panel opens.
4. 

   Select the Microsoft Access Driver.
5. 

   Click Finish.

   The ODBC Microsoft Access Setup panel opens.
6. 

   Type a name for your data source in the Data Source Name field (Movies, for example).

   Remember the name you provide because later you'll it to login to your database.
7. 

   In the Database section of the panel, click Create.

   A New Database panel opens. You'll use this panel to create a new, empty database.
8. 

   Type a name for your database in the Database Name field (Movies.mdb, for example).
9. 

   Choose a directory where you want the database located.
10. 

    Click OK.

    A panel opens telling you that the database was successfully created.
11. 

    In the ODBC Microsoft Access Setup panel, click OK.

Your database and data source are now ready to use. If you want to populate the new database with one of the sample databases that come with WebObjects, you've completed the first step: setting up the database accounts. To find out what to do next, see "[Setting Up the Sample Databases](Setting%20Up%20the%20Sample%20Databases.md#apple-gmytcnzq)
."

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Using%20Microsoft%20Access.md) [!](What%20You%20Need.md) [!](Setting%20Up%20the%20Sample%20Databases.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
