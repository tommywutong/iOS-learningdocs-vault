---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.10.html
archived_at: '2026-07-15T08:09:20.866254Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Solaris%20Post-Installation%20Steps.md) [!](Set%20the%20Time%20Zone.md) [!](Rebuild%20the%20Executable%20WODefaultApp.md)

---

#   Install the Java Native Threads Pack

If you are running Solaris 2.5.1 (with patches 103566, 103600, and 103640), you must install the Java Native Threads Pack. You can download the Native Threads Pack from JavaSoft's Java Development Kit website.

Be aware that the Native Threads patch for JDK 1.1.8 uses the green threads implementation by default, even if the native threads patch is in place. To get native threads you must do at least one of the following:

- 

  Have an environment variable named THREADS_FLAG that is set to "native".
- 

  Pass "-native" to each executable in the JDK whenever you call it (for instance, "javac -native myProg.java"). This is for _all executables_
  in the JDK, including the compiler, the JVM and AppletViewer.
- 

  Modify java_wrapper, changing the script so that DEFAULT_THREADS_FGLAG is set to "native".

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Solaris%20Post-Installation%20Steps.md) [!](Set%20the%20Time%20Zone.md) [!](Rebuild%20the%20Executable%20WODefaultApp.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
