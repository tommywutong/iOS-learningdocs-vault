---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.16.html
archived_at: '2026-07-15T08:09:23.882952Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Obtain%20and%20Install%20Database%20Client%20Libraries-2.md) [!](Sybase-2.md) [!](Build%20the%20Examples.md)

---

#  Linking Against the Adaptor

On Solaris applications must explicitly link against the adaptor framework and the client libraries. New makefiles look for adaptor frameworks and automatically add in the right linker arguments. Simply add the adaptor framework to your project, make sure that LD_LIBRARY_PATH contains the client library directory, and set the requisite environment variable specifying where the client libraries are installed. For Oracle set ORACLE_HOME and, optionally, ORACLE_REL in the makefile preamble. (The ORACLE_REL flag controls which set of libraries are used. It uses the Oracle 7.3 static link libraries by default, but you can also specify "8.0-static" or "7.3-dynamic.") For Sybase set SYBASE_HOME. For Informix set INFORMIX_HOME, INFORMIXDIR, and INFORMIXSERVER.

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Obtain%20and%20Install%20Database%20Client%20Libraries-2.md) [!](Sybase-2.md) [!](Build%20the%20Examples.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
