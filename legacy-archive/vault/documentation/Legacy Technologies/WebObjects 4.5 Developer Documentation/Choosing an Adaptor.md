---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.2a.html
archived_at: '2026-07-15T08:07:31.681822Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Designing%20the%20Main%20Page.md) [!](Specifying%20a%20Model%20File.md) [!](Choosing%20What%20to%20Include%20in%20Your%20Model.md)

---

#  Choosing an Adaptor

An _adaptor_ is a mechanism that connects your application to a particular database server. For each type of server you use, you need a separate adaptor. WebObjects provides adaptors for OpenBase Lite, Informix, Oracle, and Sybase servers. If you're working on a Windows platform, WebObjects also provides an ODBC adaptor for use with ODBC-compliant database sources.

1. 

   In the wizard panel, choose the adaptor for your database.
2. 

   Click Next.

   A login panel for the selected adaptor opens. Different databases require different login information, so each database's login panel looks different. Shown below are the login panels for the OpenBase Lite, Oracle, and ODBC adaptors.

   !!!
3. 

   Complete the login panel.

   If you are using the preinstalled OpenBase Lite database, click "Browse", browse to the __/Local/Library/Databases/Movies.db__ file (__\Apple\Local\Library\Databases\Movies.db__ in Windows NT) and click Open. The filename now appears in the Database field.

   If you are not using OpenBase Lite, specify the connection information you provided when you created and populated the Movies database. _Post-Installation Instructions_ provides more information.
4. 

   Click OK.

When you use the wizard to create a model file, the wizard uses the adaptor you specify to connect to your database. With the information you specified in the adaptor's login panel, the adaptor logs in, reads the database's schema information, and creates a model. The wizard uses your answers to the questions in the next several pages to configure that model.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Designing%20the%20Main%20Page.md) [!](Specifying%20a%20Model%20File.md) [!](Choosing%20What%20to%20Include%20in%20Your%20Model.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
