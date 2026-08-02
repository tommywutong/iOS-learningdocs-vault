---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Glossary/Glossary.html
archived_at: '2026-07-15T08:12:10.981241Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/SpecialDeploymentIssues/iDeploying_W_pplications.html)

# Glossary

**__API-based adaptor__**
: HTTP
adaptor based on APIs specific to a particular Web server. It allows CGI-like
tasks to run as part of the main server process, avoiding the creation
and termination of a process for each request. See __API-based adaptor__; __CGI
adaptor__; __HTTP adaptor__.

**__application host__**
: A computer capable of running application instances.

**__bundle__**
: In Mac OS X systems, a bundle is a directory
in the file system that stores executable code and the software
resources related to that code. The bundle directory, in essence,
groups a set of resources in a discrete package.

**__CGI (Common Gateway Interface)__**
: A standard for communication between external applications
and information servers, such as HTTP servers.

**__CGI adaptor__**
: HTTP adaptor that uses the Common Gateway Interface
(CGI) to translate requests from a Web server into requests to an application
instance, and responses from an application instance to responses
to the Web server. The Web server creates a new CGI process to handle
each request. See __API-based adaptor__; __HTTP
adaptor__.

**__component__**
: An object (of the WOComponent class) that represents
a Web page or a reusable portion of one.

**__datasource adaptor__**
: A mechanism that connects your application
to a particular database server. For each type of server you use, you
need a separate adaptor. WebObjects provides an adaptor for databases
conforming to JDBC. See also __JDBC adaptor__.

**__framework__**
: A type of bundle that packages a dynamic shared
library with the resources that the library requires, including
header files and reference documentation.

**__HTTP__**
: The client-server TCP/IP protocol used on the
Web for the exchange of HTML documents.

**__HTTP adaptor__**
: A process (or a part of one) that connects
WebObjects applications to a Web server. See also __Web server__.

**__Java Client__**
: A WebObjects development approach that allows
you to create graphical user interface applications that run on
the user's computer and communicate with a WebObjects server.

**__JDBC (Java Database Connectivity)__**
: An interface between Java platforms and databases.

**__JDBC adaptor__**
: A datasource adaptor that allows WebObjects
applications to connect to JDBC-compliant database management systems. See __datasource
adaptor__.

**__lifebeat__**
: Status message sent by WebObjects applications
to wotaskd to report their activity. The four types of lifebeat
messages are has started, is alive, will stop, and will crash.

**__load balancing__**
: Technique used to distribute user-load among
the instances of an application. When multiple instances of an application
are running and a new user accesses the application, the WebObjects
adaptor uses one of several algorithms to determine which instance
to forward the request to.

**__loopback__**
: Mechanism that allows you to open a connection
to a machine that does not go over the network.

**__Monitor__**
: A tool used to configure and maintain deployed
WebObjects applications capable of handling multiple applications,
application instances, and applications hosts at the same time.

**__Project Builder__**
: A tool used to manage the development of a
WebObjects application or framework.

**__session__**
: A period during which access to a WebObjects
application and its resources is granted to a particular client
(typically a browser). Also an object (of the WOSession class) representing
a session.

**__SMTP (Simple Mail Transfer
Protocol)__**
: A protocol used to
transfer email between computers, usually over Ethernet.

**__socket__**
: Mechanism for creating a virtual connection
between processes. It interfaces standard I/O with network communication facilities.
A socket address consists of a port number and an IP address.

**__UDP (User Datagram Protocol)__**
: Lightweight and efficient connectionless datagram
transport protocol. Used to send self-routing data throughout a
network.

**__Web server__**
: An application that serves Web pages to Web
browsers using the HTTP protocol. In WebObjects, the Web server
lies between the browser and a WebObjects application. When the
Web server receives a request from a browser, it passes the request
to the WebObjects adaptor, which generates a response and returns it
to the Web server. The Web server then sends the response to the
browser. See also __HTTP adaptor__.

**__WebObjects Deployment__**
: Software package that allows you to deploy
WebObjects applications on an intranet or the Web. You need to install
a WebObjects deployment license on computers on which you want to
install this package. See also __WebObjects Development__.

**__WebObjects Development__**
: Software package that allows you to develop
WebObjects applications. It includes tools to design applications
using an object-oriented approach. You need to install a WebObjects
development license on computers on which you want to develop applications.
See also __WebObjects Deployment__.

**__WOServices__**
: WebObjects service that monitors wotaskd processes.
Its main duty is to monitor wotaskd and restart it if it dies or
when the host is restarted. The implementation of this service is platform-dependent.

**__wotaskd__**
: WebObjects Deployment tool that manages the
instances on an application host. It's used by Monitor to propagate
site configuration changes throughout the site's application hosts.
See also __Monitor__.

[!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/SpecialDeploymentIssues/iDeploying_W_pplications.html)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
