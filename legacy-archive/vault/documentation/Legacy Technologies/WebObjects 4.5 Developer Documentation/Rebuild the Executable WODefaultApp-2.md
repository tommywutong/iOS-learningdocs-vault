---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.1c.html
archived_at: '2026-07-15T08:09:26.900414Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](HP-UX%20Post-Installation%20Steps.md) [!](Change%20the%20UID%20for%20User%20nobody.md) [!](Obtain%20and%20Install%20Database%20Client%20Libraries-3.md)

---

#   Rebuild the Executable WODefaultApp

On HP-UX, the Enterprise Objects Framework cannot automatically load your database's client library and its adaptor, as it can on other platforms. Because of this, you must rebuild the
WODefaultApp
executable, which is installed with WebObjects and is used to run purely scripted applications. If you don't rebuild this executable, any purely scripted applications you run with
WODefaultApp
won't be able to access the database.

If you answered "y" to all questions you were asked during installation, the
WODefaultApp
executable has already been rebuilt by the installation process. If you answered "n" to the question about building
WODefaultApp
or you have installed new client libraries afterwards, you should rebuild
WODefaultApp
before testing your installation.

To rebuild
WODefaultApp
, run the
RebuildWODefaultApp
script located in
$NEXT_ROOT/Developer/Examples/WebObjects/Source/WODefaultApp
.

Each time you create a new project, you'll need to set it up so that it statically links the database's client library and adaptor. To do so, add the appropriate adaptor framework to the FRAMEWORKS makefile variable definition, and uncomment this line in the
Makefile.preamble
.

include $(MAKEFILEDIR)/pdo-eoadaptor-linking.make

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](HP-UX%20Post-Installation%20Steps.md) [!](Change%20the%20UID%20for%20User%20nobody.md) [!](Obtain%20and%20Install%20Database%20Client%20Libraries-3.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
