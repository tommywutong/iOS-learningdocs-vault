---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.b.html
archived_at: '2026-07-15T08:09:48.936195Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Mac%20OS%20X%20Server%20Post-Installation%20Steps.md) [!](Mac%20OS%20X%20Server%20Post-Installation%20Steps.md) [!](Update%20Java%20CLASSPATH%20for%20old%20Swing-AWT%20Applications.md)

---

#  Using woservice on Mac OS X Server

On Mac OS X Server
wotaskd
is started automatically upon boot time under the control of
woservice
, which will restart
wotaskd
in the event that it is killed or crashes for any reason. This is done in
3100_WebObjects
, which is a script within
/etc/startup
.

You can use
woservice
to control Monitor in a similar fashion, thus ensuring that it is always running. You can enter the
woservice
tool on a shell command line (such as provided by
Terminal.app
), start it from a shell script, or configure it to launch Monitor automatically at boot time.

When invoking
woservice
from the command-line, pass as arguments the path to the application you want to be launched followed by any arguments you want to launch it with. So to start
woservice
for Monitor, you might give the following command:
> 
>
> woservice
> /System/Library/WebObjects/Applications/Monitor.woa/Monitor

To have Monitor launched at system boot time, you must add a startup script to
/etc/startup
. The scripts in
/etc/startup
follow a naming convention whereby the first four characters of the script filename are numbers. These numbers signify the order in which the system runs the scripts in
/etc/startup
. You should start Monitor near the end of the boot cycle.

You could add the following script, named
3200_Monitor
, to
/etc/startup
to start
woservice
when the system boots and have it keep Monitor running:
> 
>
> #!/bin/sh
>
> 
>
> #
>
> 
>
> # Start Monitor using woservice for WebObjects Deployment
>
> 
>
> #
>
> 
>
> . /etc/rc.common
>
> 
>
> # the following is one line:
>
> 
>
> /System/Library/WebObjects/Applications/Monitor.woa/woservice
> /System/Library/WebObjects/Applications/Monitor.woa/Monitor &

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Mac%20OS%20X%20Server%20Post-Installation%20Steps.md) [!](Mac%20OS%20X%20Server%20Post-Installation%20Steps.md) [!](Update%20Java%20CLASSPATH%20for%20old%20Swing-AWT%20Applications.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
