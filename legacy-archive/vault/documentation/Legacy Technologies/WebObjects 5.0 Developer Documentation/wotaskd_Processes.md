---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/DeploymentElements/wotaskd_Processes.html
archived_at: '2026-07-15T08:12:10.964311Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Lifebeats.md)[!](Starting_We_ts_Services.md)

## wotaskd Processes

WebObjects Deployment uses wotaskd to manage the application
instances running on your application hosts. Its main task is to
start up instances when hosts are restarted. To accomplish this,
wotaskd itself has to be restarted when the host starts up. This
is done by configuring wotaskd as a service started when the computer
boots. By default, a wotaskd process running on port `1085` is
configured as a service on all supported platforms. The implementation
of this feature is platform-specific. See ["Starting WebObjects Services"](Starting_We_ts_Services.md#apple-ijbusr2ei5cum) for details.

You need to run a wotaskd process on every machine that you
want to use as an application host. These processes constantly receive
lifebeats from the application instances they manage. Lifebeats
communicate the instance's state and allow wostaskd to determine
the state of the instances it oversees. A wotaskd process assumes
that an application instance is dead if it does not receive a lifebeat
within a certain period. For details, see ["WOAssumeApplicationIsDeadMultiplier"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iCommand_Line_Arguments.html).

When you restrict access to Monitor with a password, wotaskd
processes running on hosts configured in Monitor are also protected:
They do not respond to `http://<hostname>:<wotaskd-port>`,
as described in ["Confirming That wotaskd Is Active"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Installation/iConfirming__d_Is_Active.html).

To access the state information of a particular wotaskd process,
you use Monitor's Host page. See ["Viewing a Host's Configuration"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iSetting_Up_Hosts.html) for more information.

[!](Lifebeats.md)[!](Starting_We_ts_Services.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
