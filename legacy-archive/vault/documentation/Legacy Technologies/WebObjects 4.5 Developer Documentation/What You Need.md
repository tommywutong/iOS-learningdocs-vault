---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.24.html
archived_at: '2026-07-15T08:09:30.893873Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Using%20Microsoft%20Access.md) [!](Using%20Microsoft%20Access.md) [!](Creating%20Data%20Sources%20and%20Databases.md)

---

#  What You Need

Enterprise Objects Framework uses ODBC (a standard API developed by Microsoft for accessing database management systems) to interact with Access databases, so you'll need an Access-specific ODBC driver if you don't have one already.

To determine if you've already got an ODBC driver installed, open the Control panel. If there isn't an ODBC option listed, then you don't have any ODBC drivers installed. The latest ODBC manager and drivers for Windows NT are available from Microsoft. See
http://www.microsoft.com/data/
.

Some bugs in old versions of the ODBCJT32.DLL (used by the Enterprise Objects Framework to communicate with Microsoft Access) can cause problems with primary key generation in the ODBC Adaptor (the ODBC manager reports an invalid SQL statement when updating the EO_PK_TABLE). ODBCJT32.DLL version 3.40.2728 causes this problem, but the more recent ODBCJT32.DLL version 3.51.1029 works correctly. To verify that you don't have the older version of the ODBC drivers, open the ODBC Control Panel and click on the tab labeled "ODBC Drivers".

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Using%20Microsoft%20Access.md) [!](Using%20Microsoft%20Access.md) [!](Creating%20Data%20Sources%20and%20Databases.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
