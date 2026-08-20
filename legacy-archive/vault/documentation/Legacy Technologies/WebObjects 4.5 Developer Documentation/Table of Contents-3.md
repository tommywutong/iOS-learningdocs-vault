---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-1.html
archived_at: '2026-07-15T08:04:35.745476Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Deploying%20WebObjects%20Applications.md) [!](Deploying%20WebObjects%20Applications.md) [!](Introduction-5.md)

---

# Table of Contents

- [Introduction](Introduction-5.md#apple-obtwmslefu2diojz)

- [Related Documentation](Related%20Documentation.md#apple-obtwmslefu2dknzy)

- [WebObjects HTTP Adaptors](WebObjects%20HTTP%20Adaptors.md#apple-obtwmslefu2dkobv)

- [CGI Adaptors](CGI%20Adaptors.md#apple-obtwmslefu4tmnbr)
- [API-based Adaptors](API-based%20Adaptors.md#apple-obtwmslefu4tmnbs)
- [Installable HTTP Adaptors](Installable%20HTTP%20Adaptors.md#apple-obtwmslefu4tonbs)
- [Configuration Files](Configuration%20Files.md#apple-obtwmslefu2dmmbq)
- [Automatic Discovery of WebObjects App Servers](Automatic%20Discovery%20of%20WebObjects%20App%20Servers.md#apple-obtwmslefuytanjrgi)

- [Web Server Adaptor](Web%20Server%20Adaptor.md#apple-obtwmslefuytanjvgi)
- [wotaskd](wotaskd.md#apple-obtwmslefuytanrzgm)

- [Web Server Adaptor Configuration File Format](Web%20Server%20Adaptor%20Configuration%20File%20Format.md#apple-obtwmslefu4tqmrz)

- [XML Format in Full](XML%20Format%20in%20Full.md#apple-obtwmslefu4tqnbs)
- [Sections](Sections.md#apple-obtwmslefu4tsojq)
- [Attributes](Attributes-2.md#apple-obtwmslefuytambwgu)
- [Sample Configuration File](Sample%20Configuration%20File.md#apple-obtwmslefuytamzwga)
- [Configuration File DTD](Configuration%20File%20DTD.md)

- [Installing Applications](Installing%20Applications-2.md#apple-obtwmslefu4tmnbt)
- [Deploying With Monitor](Deploying%20With%20Monitor.md)

- [Setting Up the Monitor Application](Setting%20Up%20the%20Monitor%20Application.md#apple-obtwmslefu2tsmzr)
- [Starting Up Monitor](Starting%20Up%20Monitor.md#apple-obtwmslefu2dmobz)
- [Setting Up Monitor](Setting%20Up%20Monitor.md#apple-obtwmslefu2dombr)
- [Deploying on Multiple Hosts](Deploying%20on%20Multiple%20Hosts.md#apple-obtwmslefu3damby)

- [Adding a Host to Monitor](Adding%20a%20Host%20to%20Monitor.md#apple-obtwmslefu3danjy)

- [Adding and Configuring an Application](Adding%20and%20Configuring%20an%20Application.md#apple-obtwmslefu3dcobu)
- [Creating Application Instances](Creating%20Application%20Instances.md#apple-obtwmslefu3dcojv)
- [Starting and Stopping an Application Instance](Starting%20and%20Stopping%20an%20Application%20Instance.md#apple-obtwmslefu4tmnjt)

- [Setting Command-Line Arguments in Monitor](Setting%20Command-Line%20Arguments%20in%20Monitor.md#apple-obtwmslefu4tonru)
- [Starting Up Applications From the Command Line](Deploying-29.md#apple-obtwmslefu4tqnbz)

- [Monitor Option Summary](Monitor%20Option%20Summary.md#apple-obtwmslefu4dsnzr)

- [Global Configuration](Global%20Configuration.md#apple-obtwmslefu3tqmjv)
- [Host Configuration](Host%20Configuration.md#apple-obtwmslefu3tqmzs)
- [Application Configuration Options](Application%20Configuration%20Options.md#apple-obtwmslefu3tqmzy)
- [Instance Configuration Options](Instance%20Configuration%20Options.md#apple-obtwmslefu3tqnjw)

- [Administrative Tasks](Administrative%20Tasks.md#apple-obtwmslefu2dqmzv)

- [Monitoring Application Activity](Monitoring%20Application%20Activity.md#apple-obtwmslefu2dsobu)

- [Obtaining Information From Monitor](Obtaining%20Information%20From%20Monitor.md#apple-obtwmslefu2dsobw)
- [Logging and Analyzing Application Activity](Logging%20and%20Analyzing%20Application%20Activity.md#apple-obtwmslefu3tkmbu)
- [Logging and Analyzing Adaptor Activity](Logging%20and%20Analyzing%20Adaptor%20Activity.md#apple-obtwmslefu2tambu)
- [Accessing the Application Statistics Page](Accessing%20the%20Application%20Statistics%20Page.md#apple-obtwmslefu2tamjy)

- [Performance Testing](Performance%20Testing.md#apple-obtwmslefu2tamzs)

- [Recording a Session](Recording%20a%20Session.md#apple-obtwmslefu4tanjt)
- [Playing Back a Session](Playing%20Back%20a%20Session.md#apple-obtwmslefu4tanrs)

- [Improving Performance](Improving%20Performance.md#apple-obtwmslefu2tanrz)
- [Automatic Scheduling](Automatic%20Scheduling.md#apple-obtwmslefu2tcmbu)
- [Load Balancing](Load%20Balancing.md#apple-obtwmslefu2tcmru)
- [Increasing the Listen Queue Depth](Increasing%20the%20Listen%20Queue%20Depth.md#apple-obtwmslefu2tcnrz)
- [Making Monitor and wotaskd Fail-safe](Making%20Monitor%20and%20wotaskd%20Fail-safe.md#apple-obtwmslefu4dcobv)

- [Starting Monitor and wotaskd on Windows NT](Starting%20Monitor%20and%20wotaskd%20on%20Windows%20NT.md#apple-obtwmslefu4dcobz)
- [Using woservice on Mac OS X Server](Using%20woservice%20on%20Mac%20OS%20X%20Server-2.md#apple-obtwmslefu4tsmjy)

- [The WebObjects Application URL](Deploying-51.md#apple-obtwmslefuytanbzga)

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Deploying%20WebObjects%20Applications.md) [!](Deploying%20WebObjects%20Applications.md) [!](Introduction-5.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
