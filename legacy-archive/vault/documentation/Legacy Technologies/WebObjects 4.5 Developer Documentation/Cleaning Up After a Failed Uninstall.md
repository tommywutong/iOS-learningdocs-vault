---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.48.html
archived_at: '2026-07-15T08:09:45.479993Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Uninstalling%20on%20Solaris%20and%20HP-UX.md) [!](Uninstalling%20on%20Solaris%20and%20HP-UX.md)

---

#  Cleaning Up After a Failed Uninstall

If for some reason the uninstall fails or is prematurely aborted, you can perform the following steps to uninstall WebObjects manually.

1. 

   Log in as
   root
   .
2. 

   Remove the contents of the
   NEXT_ROOT
   directory with:

   rm -rf NEXT_ROOT
3. 

   Remove the
   ApplePDOstartup
   scripts from
   /etc
   with:

   cd /etc

   find . -name `\*Apple\*' -print | xargs rm -f

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Uninstalling%20on%20Solaris%20and%20HP-UX.md) [!](Uninstalling%20on%20Solaris%20and%20HP-UX.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
