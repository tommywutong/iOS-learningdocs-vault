---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.1b.html
archived_at: '2026-07-15T08:09:26.382132Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](HP-UX%20Post-Installation%20Steps.md) [!](Set%20the%20Time%20Zone-2.md) [!](Rebuild%20the%20Executable%20WODefaultApp-2.md)

---

#   Change the UID for User nobody

If you're using the Apache web server you'll need to change the UID of the user nobody, which is used to launch CGI processes. By default, the UID is -2, which causes setuid to complain about an invalid argument.

Change the nobody UID and nogroup group ID in
/etc/passwd
and
/etc/group
to positive numbers.

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](HP-UX%20Post-Installation%20Steps.md) [!](Set%20the%20Time%20Zone-2.md) [!](Rebuild%20the%20Executable%20WODefaultApp-2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
