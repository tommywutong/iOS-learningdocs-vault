---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Installation/Confirming__d_Is_Active.html
archived_at: '2026-07-15T08:12:11.042198Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Environment_X_Platforms.md)[!](Default_Ada_nstallation.md)

## Confirming That wotaskd Is Active

After the installation is complete (and if you chose to start __WOServices__ in
Solaris), a wotaskd process should be running on your computer.
(WOServices ensures that wotaskd is running at all times.) To confirm
that wotaskd is running, launch a Web browser and enter this address: `http://localhost:1085`.
You should see a page like the one in [Figure 3-1](#apple-ijbusrkbjjcue). For more information,
see ["Viewing a Host's Configuration"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iSetting_Up_Hosts.html).

__Figure
3-1 The configuration page of a wotaskd
process__

![[image: ../Art/wotaskdpage.gif]](../Art/wotaskdpage.gif)

If a wotaskd process isn't running, these are possible reasons:

- The version
  of J2SE is not 1.3 or later.

  Upgrade to J2SE 1.3 (version 1.3.1
  on Windows 2000).
- Port `1085` is already
  in use.

  Change the port of the process that's using port `1085`.
- The `NEXT_ROOT` environment
  variable is not set.

  In platforms other than Mac OS X Server
  and Windows 2000, make sure that the `NEXT_ROOT` environment
  variable is set for the user under which you're trying to run wotaskd.
  This also applies to application instances.

[!](Environment_X_Platforms.md)[!](Default_Ada_nstallation.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
