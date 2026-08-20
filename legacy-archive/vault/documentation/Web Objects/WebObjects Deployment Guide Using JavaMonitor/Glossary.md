---
title: WebObjects Deployment Guide Using JavaMonitor
apple_id: TP30001009
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Deployment/Deploying_Applications/Glossary/Glossary.html
archived_at: '2026-07-18T02:15:44.758380Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Deployment Guide Using JavaMonitor](Introduction%20to%20WebObjects%20Deployment%20Guide%20Using%20JavaMonitor.md)


[Next](Document%20Revision%20History.md)[Previous](Deployment%20Issues%20with%20Java%20Client.md)

# Glossary

- __API-based adaptor__

  HTTP adaptor based on a programming interface specific to a particular web server. It allows CGI-like tasks to run as part of the main server process, avoiding the creation and termination of a process for each request.

- __application host__

  A computer capable of running application instances.

- __bundle__

  In Mac OS X systems, a bundle is a directory in the file system that stores executable code and the software resources related to that code. The bundle directory, in essence, groups a set of resources in a discrete package.

- __CGI (Common Gateway Interface)__

  A standard for communication between external applications and information servers, such as web servers.

- __CGI adaptor__

  HTTP adaptor that uses the Common Gateway Interface (CGI) to translate requests from an web server into requests to an application instance, and responses from an application instance to responses to the web server. The web server creates a CGI process to handle each request.

- __data-source adaptor__

  A mechanism that connects your application to a particular database server. For each type of server you use, you need a separate adaptor. WebObjects provides an adaptor for databases conforming to JDBC.

- __framework__

  A type of bundle that packages a dynamic shared library with the resources that the library requires, including header files and reference documentation.

- __HTTP (Hypertext Transfer Protocol)__

  The client-server TCP/IP protocol used on the web for the exchange of HTML documents.

- __HTTP adaptor__

  A process (or a part of one) that connects WebObjects applications to an web server.

- __Java Client__

  A WebObjects development approach that allows you to create graphical user interface applications that run on the user’s computer and communicate with a WebObjects server application.

- __JDBC__

  An interface between Java platforms and databases.

- __JDBC adaptor__

  A datasource adaptor that allows WebObjects applications to connect to JDBC-compliant database management systems.

- __lifebeat__

  Status message sent by WebObjects applications to wotaskd to report their activity. The four types of lifebeat messages are has started, is alive, will stop, and will crash.

- __load balancing__

  Technique used to distribute user-load among the instances of an application. When multiple instances of an application are running and a new user accesses the application, the WebObjects adaptor uses one of several algorithms to determine which instance to forward the request to.

- __loopback__

  Mechanism that allows you to open a connection to a computer that does not go over the network.

- __JavaMonitor__

  A tool used to configure and maintain deployed WebObjects applications capable of handling multiple applications, application instances, and applications hosts at the same time.

- __session__

  A period during which access to a WebObjects application and its resources is granted to a particular client (typically a browser). Also an object (of the WOSession class) representing a session.

- __SMTP (Simple Mail Transfer Protocol)__

  A protocol used to transfer email between computers, usually over Ethernet.

- __socket__

  Mechanism for creating a virtual connection between processes. It interfaces standard I/O with network communication facilities. A socket address consists of a port number and an IP address.

- __UDP (User Datagram Protocol)__

  Lightweight and efficient connectionless datagram transport protocol. Used to send self-routing data throughout a network.

- __Web component__

  An object (of the WOComponent class) that represents a webpage or a reusable portion of one.

- __Web server__

  An application that serves webpages to web browsers using the HTTP protocol. In WebObjects, the web server lies between the browser and a WebObjects application. When the web server receives a request from a browser, it passes the request to the WebObjects adaptor, which generates a response and returns it to the web server. The web server then sends the response to the browser.

- __WebObjects Deployment__

  Software package that allows you to deploy WebObjects applications on an intranet or the web. You need to install a WebObjects deployment license on computers on which you want to install this package.

- __WebObjects Development__

  Software package that allows you to develop WebObjects applications. It includes tools to design applications using an object-oriented approach. You need to install a WebObjects development license on computers on which you want to develop applications.

- __WOServices__

  WebObjects service that monitors wotaskd processes. Its main duty is to monitor wotaskd and restart it if it dies or when the host is restarted. The implementation of this service is platform-dependent.

- __wotaskd (WebObjects task daemon)__

  WebObjects Deployment tool that manages the instances on an application host. It’s used by Monitor to propagate site configuration changes throughout the site’s application hosts.

- __Xcode__

  A tool used to manage the development of a WebObjects application or framework.

[Next](Document%20Revision%20History.md)[Previous](Deployment%20Issues%20with%20Java%20Client.md)

