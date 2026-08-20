---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/Deployment_Tasks.html
archived_at: '2026-07-15T08:12:00.334448Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/DeploymentElements/iStarting_We_ts_Services.html)[!](Setting_Up_Hosts.md)

# Deployment Tasks

Now that you are acquainted with the deployment
tools of WebObjects, you are ready to put that knowledge to work
by deploying your applications.

This chapter explains how Monitor allows you to perform most
of the tasks required to maintain a WebObjects application site
with point-and-click ease. The sections below guide you through
the process of adding and configuring hosts, applications, and instances.
Also explained is the load-balancing mechanism used by the HTTP
adaptor, which performs load balancing among the instances of an
application (which can be distributed across more than one host)
and how to set up email notifications so that you and your colleagues
are notified when problems arise.

This chapter addresses the following subjects:

- ["Setting Up Hosts"](Setting_Up_Hosts.md#apple-krifqusfiyytcma) explains
  how you add and configure hosts for application deployment. Note
  that this is different from configuring hosts in the HTTP adaptor.
- ["Installing Applications"](Installing_Applications.md#apple-ijbusrcjjfcei) shows you where to place application
  files and Web server resources on an application host before deployment.
- ["Setting Up Applications"](Setting_Up_Applications.md#apple-krifqusfiyytcmy) details the ways you can customize
  a deployment. These include choosing a load-balancing algorithm
  and scheduling instances to restart at regular intervals.
- ["Configuring Sites"](Configuring_Sites.md#apple-ijbusrkijjcuq) describes the site-wide properties available.
  These include configuring Monitor to use your SMTP (Simple Mail
  Transfer Protocol) server to send email notifications.
- ["Setting Monitor Preferences"](Setting_Mon_Preferences.md#apple-ijbusrsgjjdue) shows you the Monitor-specific
  preferences you can use to tailor the tool's behavior.
- ["Load Balancing"](Load_Balancing.md#apple-ijbusskjijcue) explains how load balancing distributes
  user load among the running instances of an application in your
  site.
- ["Deploying Multiple Sites"](Deploying_Multiple_Sites.md#apple-ijbusrsiinbee) shows how you can maintain multiple
  sites on one set of computers.

[!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/DeploymentElements/iStarting_We_ts_Services.html)[!](Setting_Up_Hosts.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
