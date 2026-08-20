---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Introduction/The_WebObje_yment_Model.html
archived_at: '2026-07-15T08:12:13.948794Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Introduction%20to%20WebObjects%20Deployment.md)[!](The_WebObje_Environment.md)

## The WebObjects Deployment Model

A WebObjects deployment has six major parts:

- __Client__ Web
  browser or Java Client application (A Java Client application).
- __Web server__ application that receives
  HTTP requests from clients and sends responses back to them.
- __HTTP adaptor__ application that serves
  as an interface between your Web server and your application instances.
  The HTTP adaptor routes requests from the Web server to the appropriate
  instance and sends the responses generated back to the Web server. The
  adaptor does this while performing __load balancing__ to
  distribute an application's users among its active instances.
  Load balancing helps to spread the user load of your site evenly
  across your application hosts.
- __Application instances__ individual processes
  that receive requests from the HTTP adaptor and send responses back
  to it. To create a response, an instance can perform calculations,
  or save or retrieve data from a datasource.
- __Datasource adaptor__ interface between
  an application instance and your datasource. WebObjects includes
  a __JDBC__ (Java Database Connectivity) adaptor,
  allowing your applications to connect to any JDBC-compliant database.

  For
  JDBC connectivity, your database needs a JDBC driver, which you
  obtain from your database vendor. WebObjects applications can connect
  to databases that use Type 2 (partly Java) or Type 4 (all Java)
  JDBC drivers. The JDBC adaptor included with WebObjects Deployment
  has been certified to work adequately with Type 4 drivers. Type
  2 drivers may require special configuration for them to work properly
  with the adaptor. If your database provides a Type 2 driver, consult
  with your database vendor to determine how it needs to be configured
  to work properly with a JDBC adaptor.
- __Datasource__ the mechanism that your
  applications use to store persistent data. Consult with your datasource
  vendor to obtain configuration and optimization details.

When an application user sends a request through a Web browser
to your Web server, the server forwards the request to the HTTP
adaptor. The adaptor then determines which application instance
should process the request and forwards the request to it. When
the application instance receives the request, it performs all the
necessary processing to produce a response (a new Web page). The
instance then sends the response page to the adaptor, which forwards
it to the Web server. The Web server then forwards the response page
to the user's Web browser. This process is illustrated in [Figure 2-1](#apple-ijauuq2ijfeui).

__Figure
2-1 WebObjects deployment model__

![[image: ../Art/deploymentmodel.gif]](../Art/deploymentmodel.gif)

Notice that both the application instance and the Web server
contribute to the response page's content. The instance uses templates
and logic to generate the HTML code for dynamic pages, while the
Web server provides the content of images contained in those pages.
The server can also dispense static pages.

The number of instances of your application necessary to support
its users depends on the number of users that connect to your application
concurrently. In some cases a single instance is adequate. When
one instance is not able to process requests in a timely manner, additional
instances can solve the problem. This way, the amount of user-state
information that a single instance stores is reduced. In addition,
with less state to keep track of, an instance can process requests
faster. [Figure 2-2](#apple-ijauussdivduc) shows a site with one host running multiple instances
of an application.

__Figure
2-2 WebObjects deployment model—multiple
instances of an application__

![[image: ../Art/deploymentmodel2.gif]](../Art/deploymentmodel2.gif)

However, adding instances of your application to a host may
not be the most effective solution. Eventually a point of diminishing
returns will be reached, where adding instances actually decreases
your application's performance. In such a case, you should consider
adding additional application hosts that run the extra instances
required to handle the increased traffic to your site. [Figure 2-3](#apple-ijbegr2ki5duc) shows
how a site with two computers, one acting as a Web server and application
host, and the other just as an application host would look.

__Figure
2-3 Deployment using two computers__

![[image: ../Art/twomachines.gif]](../Art/twomachines.gif)

[!](Introduction%20to%20WebObjects%20Deployment.md)[!](The_WebObje_Environment.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
