---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.5.html
archived_at: '2026-07-15T08:00:22.691770Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Post-Install Guide](About%20This%20Document.md)

[!Table of Contents](About%20This%20Document.md) [!Previous Section](HP-UX%20Post-Installation%20Steps.md)

#   Using Microsoft Access

Read this section if you want to use Enterprise Objects Framework to connect to a Microsoft Access database. The information in this section describes what you need to do before you can install the sample databases or create your own custom databases.

##  What You Need

Enterprise Objects Framework uses ODBC (a standard API developed by Microsoft for accessing database management systems) to interact with Access databases, so you'll need an Access-specific ODBC driver if you don't have one already.

To determine if you've already got an ODBC driver installed, open the Control panel. If there isn't an ODBC option listed, then you don't have any ODBC drivers installed. The latest ODBC manager and drivers for Windows NT are available from Microsoft. See __http://www.microsoft.com/data/mdac15.htm__
.

Some bugs in old versions of the ODBCJT32.DLL (used by the Enterprise Objects Framework to communicate with Microsoft Access) can cause problems with primary key generation in the ODBC Adaptor (the ODBC manager reports an invalid SQL statement when updating the EO_PK_TABLE). ODBCJT32.DLL version 3.40.2728 causes this problem, but the more recent ODBCJT32.DLL version 3.51.1029 works correctly. To verify that you don't have the older version of the ODBC drivers, open the ODBC Control Panel and click on the tab labeled "ODBC Drivers".

##  Creating Data Sources and Databases

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

The ODBC Microsoft Access 97 Setup panel opens.

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

    In the ODBC Microsoft Access 97 Setup panel, click OK.

Your database and data source are now ready to use. If you want to populate the new database with one of the sample databases that come with WebObjects, you've completed the first step: setting up the database accounts. To find out what to do next, see "[Setting Up the Sample Databases](Setting%20Up%20the%20Sample%20Databases.md#apple-gmytcnzq)
."

[!Table of Contents](About%20This%20Document.md) [!Next Section](Setting%20Up%20the%20Sample%20Databases.md)
