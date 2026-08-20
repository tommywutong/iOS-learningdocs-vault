---
title: Java Application Server Guide
apple_id: TP40002323
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Conceptual/J2EE_JavaAppServerGuide/Glossary/Glossary.html
archived_at: '2026-07-18T02:14:23.171779Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Java Application Server Guide](Introduction%20to%20Java%20Application%20Server%20Guide.md)


[Previous](Document%20Revision%20History.md)

# Glossary

- __application server__

  JBoss instance, which is started through Server Admin.

- __CMP (container-managed persistence)__

  Enterprise bean persistence model in which the J2EE container is responsible for persisting enterprise-bean instances to a data store and populating the fields of enterprise-bean instances when they are retrieved.

- __deployment tool__

  HTML-based application through which J2EE application or component archives can be configured or assembled in preparation for deployment in OS X Server.

- __EJB (Enterprise JavaBeans)__

  Specification that provides an infrastructure through which data-based components can be developed and deployed in a variety of platforms.

- __J2EE (Java 2, Enterprise Edition)__

  Specification that defines a platform for the development and deployment of Web applications. It describes an environment under which enterprise beans, servlets, and JSP pages can share resources and work together.

- __JBoss__

  Java-based open-source application server capable of deploying J2EE-based applications. JBoss provides many useful features in addition those defined in the J2EE standard, including support for clustering, session replication, mail, and security.

- __JMS (Java Message Service)__

  Java-based programming interface that implements an asynchronous message-exchange system. It facilitates the development of message-based applications. JMS is part of the J2EE platform.

- __management tool__

  HTML-based application through which an application-server configuration can be modified. It also allows for the viewing of statistics of resources and services deployed on application servers, starting and stopping services, and adding topics, queues, and data sources.

- __Pet Store__

  Pet Store is a sample J2EE application from Sun Microsystems, which showcases the power and flexibility of the J2EE platform.

- __queue__

  A queue is a JMS construct that allows for point-to-point messaging between applications. A message sent to a queue can be received by only one application. When several applications are subscribed to the queue, the messages are load balanced between the subscribers.

- __server__

  Computer running OS X Server.

- __topic__

  Topics are one of the message distribution center types for J2EE-based applications. Message senders send messages only to topics instead of specific applications, while only the applications interested in receiving messages sent to a particular topic subscribe to the topic and, therefore, receive the messages sent to it. A topic can have one or more subscribers. Any message sent to the topic is broadcasted to all the topic’s subscribers.

[Previous](Document%20Revision%20History.md)

