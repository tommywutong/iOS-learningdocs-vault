---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies3.html
archived_at: '2026-07-15T07:54:35.231376Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies2.md)

## Choosing an Adaptor

An _adaptor_ is a mechanism that connects your application to a particular database server. For each type of server you use, you need a separate adaptor. WebObjects provides adaptors for Informix, Oracle, and Sybase servers. If you're working on a Windows platform, WebObjects also provides an ODBC adaptor for use with ODBC-compliant database sources.

- In the wizard panel, choose the adaptor for your database.
- Click Next.

A login panel for the selected adaptor opens. Different databases require different login information, so each database's login panel looks different. Shown below are the login panels for the ODBC and Oracle adaptors, for use with ODBC-compliant database servers (such as Microsoft Access) and Oracle database servers, respectively.

!- Complete the login panel.

Specify the connection information you provided when you created and populated the Movies database. _Post-Installation Instructions_ provides more information.

- Click OK.

When you use the wizard to create a model file, the wizard uses the adaptor you specify to connect to your database. With the information you specified in the adaptor's login panel, the adaptor logs in, reads the database's schema information, and creates a model. The wizard uses your answers to the questions in the next several pages to configure that model.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies4.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
