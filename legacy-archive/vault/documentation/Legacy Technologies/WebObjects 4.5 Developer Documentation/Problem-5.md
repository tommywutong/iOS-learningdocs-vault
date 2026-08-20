---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.39.html
archived_at: '2026-07-15T08:09:38.960613Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Problems%20With%20Compiled%20Applications.md) [!](Problem-4.md) [!](Converting%20Projects%20From%20Earlier%20Releases.md)

---

#  Problem

A WebObjects application won't connect to the database server.

#  Checklist

1. 

   Check that your database server itself is operating correctly.

   Check that the client libraries for your database server are correctly installed on your machine. If so, you can, for example, use the tools supplied with the database server (
   isql
   for Sybase,
   sqlplus
   for Oracle, and
   dbaccess
   for Informix) to test that you can connect to the server and execute simple SQL commands.
2. 

   Make sure that the database model file is accessible to your application.

   The model file should be in the
   Resources
   directory under the application's
   .woa
   directory. Taking the Movies application for example, the directory structure would look like this:

    Movies.woa/

       Movies (the executable file)

       Resources/Movies.eomodeld (the model file)

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Problems%20With%20Compiled%20Applications.md) [!](Problem-4.md) [!](Converting%20Projects%20From%20Earlier%20Releases.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
