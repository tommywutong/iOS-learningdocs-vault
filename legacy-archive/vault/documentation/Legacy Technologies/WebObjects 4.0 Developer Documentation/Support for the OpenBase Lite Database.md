---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/DeltaDoc/NewInEOF3.05.html
archived_at: '2026-07-15T07:58:01.134857Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in EOF 3.0](Table%20of%20Contents-2.md)

[!Table of Contents](Table%20of%20Contents-2.md) [!Previous Section](Deprecated%20API.md)

# Support for the OpenBase Lite Database

Enterprise Objects Framework 3.0 adds support for a new database, OpenBase Lite, which ships with Enterprise Objects Framework 3.0 as an unsupported demo.
If you install OpenBase Lite, it installs the following two frameworks in __Local/Library/Frameworks__:

- OpenBaseLiteAPI.framework, the proprietary database implementation
- OpenBaseLiteEOAdaptor.framework, the OpenBase Lite adaptor

On NT, OpenBase Lite also installs the following DLLs in __Local/Library/Executables__:

- OpenBaseLiteAPI.dll
- OpenBaseLiteEOAdaptor.dll

Additionally, a preloaded OpenBase Lite database for the Movies and Rentals models is provided as a part of the installation process. All of the examples run against this database out-of-the-box (without any configuration).
OpenBase Lite is intended to be used as a single-user, single-machine database convenient for development, not as a deployment database. Only one process can access an OpenBase Lite database at a time (other processes are locked out until the first process releases the OpenBase Lite database). For more information on OpenBase Lite or if you are interested in the full-featured, client-server OpenBase database (as opposed to the bundled "Lite" version), contact OpenBase International:
OPENBASE INTERNATIONAL LTD.
58 Greenfield Road
Francestown, NH 03043 USA
TEL: (603) 547-8404
FAX: (603) 547-2423
e-mail: info@openbase.com
http://www.openbase.com

[!Table of Contents](Table%20of%20Contents-2.md) [!Next Section](New%20Convenience%20API.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
