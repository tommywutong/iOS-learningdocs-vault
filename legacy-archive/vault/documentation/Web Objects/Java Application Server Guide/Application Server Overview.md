---
title: Java Application Server Guide
apple_id: TP40002323
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Conceptual/J2EE_JavaAppServerGuide/Overview/Overview.html
archived_at: '2026-07-18T02:14:24.156974Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Java Application Server Guide](Introduction%20to%20Java%20Application%20Server%20Guide.md)


[Next](Configuring%20Applications.md)[Previous](Introduction%20to%20Java%20Application%20Server%20Guide.md)

# Application Server Overview

JBoss is an open-source highly popular Java-based application server. Based on the Java 2, Enterprise Edition (J2EE) platform, JBoss provides an affordable delivery system for enterprise applications. Applications that follow the J2EE standard can be deployed on other application servers, such as WebLogic, WebSphere, and JRun, with little or no modification. JBoss provides many useful features in addition those defined in the J2EE standard, including support for clustering, session replication, mail, and security.

OS X Server includes two easy-to-use, HTML-based tools that facilitate the configuration of J2EE applications for deployment: The deployment tool and the management tool. The deployment tool allows you to open application or component archives (EAR files, WAR files, JAR files, SAR files, and so on) without having to manually decompress the archives. The application lets you view or change the values of settings specified in the `META-INF` and `WEB-INF` directories of the archives. See [Configuring Applications](Configuring%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmrtfvbuqmrrguwueqkkiveesr2e) for more information.

The management tool allows you to manage application servers (JBoss instances) running on one or more computers. This application lets you start and stop services provided by individual application servers, configure services, and create data sources, queues, and topics. See [Administering Application Servers](Administering%20Application%20Servers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmrtfvbuqmrrg4wugsscindeessh) for details.

This chapter provides an overview of JBoss for OS X Server.

OS X Server version 10.3 includes JBoss version 3.2.2RC2. To provide a high level of availability, OS X Server includes a “watchdog” process that ensures that the application server is always running (if you turn on the application server in Server Admin). If the application server freezes or crashes, the daemon restarts it automatically.

In addition, OS X Server offers load balancing and session failover through Apache and JBoss:

- Apache, coupled with the `mod_jk` plug-in, provides HTTP load balancing with session affinity (sticky sessions) and connects to JBoss instances through AJP connectors.
- JBoss offers session failover through HTTP session state replication in the cluster configuration.
- JBoss also provides load balancing for enterprise beans, including failover for stateful session beans, and support for session affinity.

In OS X Server, JBoss is configured to use Tomcat (using the AJP connector) as its web server and servlet container. In addition, HTTP and HTTPS (through port `8443`) are enabled by default.

You can manage the application server from the Server Admin application. This provides you with a simple way to start, stop, and monitor the application server. You can use the command line, if you prefer.

OS X Server includes two applications that allow you to deploy applications on JBoss and monitor their performance. They are the JBoss deployment tool and the JBoss management tool.

The deployment tool allows you to configure an application or an application component so that, for example, it accesses the appropriate data sources and database tables when it’s run. This is how application developers decouple business logic from the database engine that is used to persist data. That way, you can use the database engine that meets your needs and not the one the developer used while developing the application. For details on the deployment tool, see [Configuring Applications](Configuring%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmrtfvbuqmrrguwueqkkiveesr2e).

The management tool lets you administer the local (running on the computer you are logged in to) application server, and monitor local and remote (running on a computer in the local network) application servers. As part of administering an application server, you may start and stop services, configure services, deploy applications, and add data sources, queues, and topics. When monitoring an application server, the management tool lets you access the statistics provided by the resources and services running on it. For example, a service may indicate its name, its purpose, and when it was started. For more information on the management tool, see [Administering Application Servers](Administering%20Application%20Servers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmrtfvbuqmrrg4wugsscindeessh).

In OS X Server, all the JBoss configurable settings are set up for maximum J2EE compliance. There are three standard deployment configurations in JBoss for OS X Server:

- The development configuration offers increased logging and also consults schema documents. As a result, an application is not deployed when the configuration files do not adhere to their respective schemas.
- The standalone configuration is set up for high performance on a single server.
- The cluster configuration is optimized for high performance on a cluster of servers. This includes load balancing as well as session replication among stateful session beans and HTTP sessions.

[Next](Configuring%20Applications.md)[Previous](Introduction%20to%20Java%20Application%20Server%20Guide.md)

