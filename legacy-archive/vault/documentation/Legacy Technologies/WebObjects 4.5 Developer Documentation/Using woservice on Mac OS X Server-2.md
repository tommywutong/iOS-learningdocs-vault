---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-50.html
archived_at: '2026-07-15T08:05:06.338226Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Making%20Monitor%20and%20wotaskd%20Fail-safe.md) [!](Starting%20Monitor%20and%20wotaskd%20on%20Windows%20NT.md) [!](Deploying-51.md)

---

# Using woservice on Mac OS X Server

On Mac OS X Server __wotaskd__
is started automatically upon boot time under the control of __woservice__
, which will restart __wotaskd__
in the event that it is killed or crashes for any reason. This is done in __3100_WebObjects__
, which is a script within __/etc/startup__
.

You can use __woservice__
to control Monitor in a similar fashion, thus ensuring that it is always running. You can enter the __woservice__
tool on a shell command line (such as provided by __Terminal.app__
), start it from a shell script, or configure it to launch Monitor automatically at boot time.

When invoking __woservice__
from the command-line, pass as arguments the path to the application you want to be launched followed by any arguments you want to launch it with. So to start __woservice__
for Monitor, you might give the following command:

`woservice /System/Library/WebObjects/Applications/Monitor.woa/Monitor`

To have Monitor launched at system boot time, you must add a startup script to __/etc/startup__
. The scripts in __/etc/startup__
follow a naming convention whereby the first four characters of the script filename are numbers. These numbers signify the order in which the system runs the scripts in __/etc/startup__
. You should start Monitor near the end of the boot cycle.

You could add the following script, named __3200_Monitor__
, to __/etc/startup__
to start __woservice__
when the system boots and have it keep Monitor running:

`#!/bin/sh`

`#`

`# Start Monitor using woservice for WebObjects Deployment`

`#`

`. /etc/rc.common`
`# the following is one line:`
`/System/Library/WebObjects/Applications/Monitor.woa/woservice /System/Library/WebObjects/Applications/Monitor.woa/Monitor &`

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Making%20Monitor%20and%20wotaskd%20Fail-safe.md) [!](Starting%20Monitor%20and%20wotaskd%20on%20Windows%20NT.md) [!](Deploying-51.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
