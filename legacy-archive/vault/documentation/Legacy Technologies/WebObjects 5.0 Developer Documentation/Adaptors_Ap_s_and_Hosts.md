---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/WebObjectsAdaptors/Adaptors_Ap_s_and_Hosts.html
archived_at: '2026-07-15T08:12:15.574370Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](HTTP%20Adaptors.md)[!](Types_of_Adaptors.md)

## Adaptors, Applications, and Hosts

A WebObjects adaptor forwards requests from a Web server to
application instances and returns responses from instances back
to the server. You may need to have more than one instance of a
given application to support a large number of concurrent users. [Figure 4-1](#apple-ijbegssiivbeo) illustrates
a simple site, implemented with one computer. It serves two applications,
with two instances for each application.

__Figure
4-1 Deployment on one computer, using
one adaptor__

![[image: ../Art/onemachine.gif]](../Art/onemachine.gif)

Although the WebObjects installation provides several adaptors,
only one is active by default (see ["Default Adaptor Installation"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Installation/iDefault_Ada_nstallation.html) for
details). However, an application can communicate with an adaptor
other than the active adaptor.

[Figure 4-2](#apple-ijbegr2hircec) depicts an application site running on one machine,
using two adaptors.

__Figure
4-2 Deployment on one computer using two
adaptors__

![[image: ../Art/onemachinetwoadaptors.gif]](../Art/onemachinetwoadaptors.gif)

Most sites require multiple computers to ensure that an instance
of a particular application is always available. In this kind of
deployment, usually one computer runs the Web server and the WebObjects
adaptor, while one or more additional machines serve as application hosts. [Figure 4-3](#apple-ijbegr2ki5duc) illustrates
an application site using three computers, one running the Web server
and the adaptor, and the other two running application instances.

__Figure
4-3 Deployment using three machines using
one adaptor__

![[image: ../Art/multiplemachines.gif]](../Art/multiplemachines.gif)

The HTTP adaptor needs to periodically determine your site's
state—which application instances are running. There are two ways
in which the adaptor can obtain this information:

- __Dynamically__ The
  adaptor determines your site's state by asking each application
  host for its state. The adaptor can use a multicast request to find
  out which hosts are available or you can define a host list for
  it. Using this method, you avoid having to configure new hosts as
  you add them to your site.
- __Statically__ An adaptor configuration
  file contains host and application information about your site;
  it includes information about every application instance you want
  to run. After the adaptor reads the file, it has all the information
  it needs to communicate with the application instances you want
  to run. Using this kind of configuration avoids multicast requests
  and host polling. However, when you add new hosts, you'll have
  to update the configuration file. For more information on the adaptor
  configuration file, see ["Using a Configuration File"](State_Discovery.md#apple-ijbegq2iifdee).

You configure your site using Monitor, a Web-browser–based
tool.

[!](HTTP%20Adaptors.md)[!](Types_of_Adaptors.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
