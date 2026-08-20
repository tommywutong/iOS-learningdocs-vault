---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.37.html
archived_at: '2026-07-15T08:09:38.440828Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Problems%20With%20Compiled%20Applications.md) [!](Problem-3.md) [!](Problem-5.md)

---

#  Problem

The Movies application won't run.

#  Checklist

1. 

   Make sure the application was correctly installed and compiled.

   The Movies application must be compiled before you can run it. In addition, you must create the Movies database (scripts are provided) and install the database model file that is compatible with your database server as described in [Setting Up the Sample Databases](Setting%20Up%20the%20Sample%20Databases.md#apple-gmytcnzq)
   .

   Check the Movies directory for an directory named
   Movies.woa
   . This is the WebObjects application wrapper. Check the wrapper for an executable file. If the wrapper or the executable doesn't exist, build the Movies application.

   On Solaris and HP-UX, you need to build Movies with the correct client libraries and adaptor. Before you build, add the appropriate adaptor framework to the
   FRAMEWORKS
   makefile variable. Then uncomment the following line in the
   Makefile.preamble
   to link the appropriate client libraries:

   include $(MAKEFILEDIR)/pdo-eoadaptor-linking.make

   If Movies compiles and runs but can't access data about the various movies, it's probably because the application can't communicate with the database server.

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Problems%20With%20Compiled%20Applications.md) [!](Problem-3.md) [!](Problem-5.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
