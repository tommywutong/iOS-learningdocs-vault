---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.c.html
archived_at: '2026-07-15T08:09:49.456348Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Mac%20OS%20X%20Server%20Post-Installation%20Steps.md) [!](Using%20woservice%20on%20Mac%20OS%20X%20Server.md) [!](Solaris%20Post-Installation%20Steps.md)

---

#  Update Java CLASSPATH for old Swing/AWT Applications

Between Swing 1.0 and Swing 1.1, Sun changed the Swing package path from
com.sun.java
to
javax
. WebObjects 4.5 installs the new versions of of
Swing.jar
and
AWT.jar
in
/System/Library/Frameworks/JavaVM.framework/Classes
(AWT depends on Swing). Note that this is where the old
.jar
files were located; in order to allow applications that were using the older versions of the Swing and AWT packages to continue to function, the WebObjects 4.5 installer doesn't overwrite the old
.jar
files but instead renames them to
Swing.old.jar
and
AWT.old.jar
. Thus, to use the old
.jar
files you need only alter your runtime CLASSPATH to point to the new locations of the old versions of AWT and Swing.

This change needs to be made only for non-WebObjects projects that use the old version of Swing. WebObjects projects that use the old version of Swing should be modified to use the new version.

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Mac%20OS%20X%20Server%20Post-Installation%20Steps.md) [!](Using%20woservice%20on%20Mac%20OS%20X%20Server.md) [!](Solaris%20Post-Installation%20Steps.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
