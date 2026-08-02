---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.46.html
archived_at: '2026-07-15T08:09:44.422342Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Uninstalling%20WebObjects.md) [!](Cleaning%20Up%20After%20a%20Failed%20Installation.md) [!](Uninstalling%20on%20Solaris%20and%20HP-UX.md)

---

#  Uninstalling on Mac OS X Server

Uninstalling WebObjects on a computer running Mac OS X Server is simply a matter of double-clicking the installed packages in the
/Local/Library/Receipts
directory (which opens the packages in the Installer application) and clicking the Delete button (note that you must be logged in as
root
in order to uninstall WebObjects). If you did a Custom install you'll need to remove those packages that you selected. If you did a Complete install, you'll need to remove the following:

__WebObjects Developer__

- 

  WebObjectsLicense.pkg
- 

  DeveloperDoc.pkg
- 

  DeveloperTools.pkg
- 

  ProfileLibs.pkg
- 

  Emaces.pkg
- 

  Source.pkg
- 

  EOUser.pkg
- 

  WebObjectsAdaptors.pkg
- 

  WebObjectsDeployment.pkg
- 

  EODeveloper.pkg
- 

  LDAPEOAdaptor.pkg
- 

  OracleEOAdaptor.pkg
- 

  OpenBaseLiteAdaptor.pkg
- 

  WebObjectsExamples.pkg
- 

  WebObjectsDeveloper.pkg

__WebObjects Deployment__

- 

  WebObjectsLicense.pkg
- 

  EOUser.pkg
- 

  WebObjectsAdaptors.pkg
- 

  WebObjectsDeployment.pkg
- 

  LDAPEOAdaptor.pkg
- 

  OracleEOAdaptor.pkg

Note that a Complete install of either WebObjects Developer or Deployment installs the MacOSXServer1.0-2.pkg; this package is a system software patch for Mac OS X Server and shouldn't be removed along with the WebObjects packages listed above.

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Uninstalling%20WebObjects.md) [!](Cleaning%20Up%20After%20a%20Failed%20Installation.md) [!](Uninstalling%20on%20Solaris%20and%20HP-UX.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
