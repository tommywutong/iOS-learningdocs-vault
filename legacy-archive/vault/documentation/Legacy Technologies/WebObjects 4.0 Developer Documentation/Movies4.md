---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies4.html
archived_at: '2026-07-18T01:22:56.797836Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies3.md)

## Choosing an Adaptor

An _adaptor_ is a mechanism that connects your application to a particular database server. For each type of server you use, you need a separate adaptor. WebObjects provides adaptors for OpenBase Lite, Informix, Oracle, and Sybase servers. If you're working on a Windows platform, WebObjects also provides an ODBC adaptor for use with ODBC-compliant database sources.

- In the wizard panel, choose the adaptor for your database.
- Click Next.

A login panel for the selected adaptor opens. Different databases require different login information, so each database's login panel looks different. Shown below are the login panels for the OpenBase Lite, Oracle and ODBC adaptors.

!

!

!

- Complete the login panel.

If you are using the preinstalled OpenBase Lite database, click "Set Path", browse to the __\Apple\Local\Library\Databases\__ directory, and click Open. "Movies" will now appear in the Database pop-up list. Click Login.

If you are not using OpenBase Lite, specify the connection information you provided when you created and populated the Movies database. _Post-Installation Instructions_ provides more information.

- Click OK.

When you use the wizard to create a model file, the wizard uses the adaptor you specify to connect to your database. With the information you specified in the adaptor's login panel, the adaptor logs in, reads the database's schema information, and creates a model. The wizard uses your answers to the questions in the next several pages to configure that model.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies5.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
