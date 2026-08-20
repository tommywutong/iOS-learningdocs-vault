---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.19.html
archived_at: '2026-07-15T08:09:25.375585Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](HP-UX%20Post-Installation%20Steps.md) [!](HP-UX%20Post-Installation%20Steps.md) [!](Set%20the%20Time%20Zone-2.md)

---

#   Setting the LPATH and SHLIB_PATH Environment Variables

Set the LPATH environment variable to an appropriate value for your installation, with the following prepended to it (enter the following all on one line):

$NEXT_ROOT/Local/Developer/Libraries:$NEXT_ROOT/
Developer/Libraries:$NEXT_ROOT/Local/Library/
Executables:$NEXT_ROOT/Library/Executables:$NEXT_ROOT/
Library/JDK/lib

Also set the SHLIB_PATH to the value of LPATH with:

setenv SHLIB_PATH "$LPATH"

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](HP-UX%20Post-Installation%20Steps.md) [!](HP-UX%20Post-Installation%20Steps.md) [!](Set%20the%20Time%20Zone-2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
