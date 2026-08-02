---
title: WebObjects Deployment Guide Using JavaMonitor
apple_id: TP30001009
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Deployment/Deploying_Applications/Installation/Installation.html
archived_at: '2026-07-18T02:15:44.813663Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Deployment Guide Using JavaMonitor](Introduction%20to%20WebObjects%20Deployment%20Guide%20Using%20JavaMonitor.md)


[Next](HTTP%20Adaptors.md)[Previous](WebObjects%20Deployment.md)

# Installing Software

This chapter addresses WebObjects Deployment installation issues, including what elements of the software need to be installed on a computer, taking the computer’s purpose into account.

The chapter contains these sections:

- [Choosing What to Install](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydanrrfvbegskhijbeqsq) explains which files need to be installed on a computer, based on the purpose of the computer within a deployment.
- [HTTP Adaptors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydanrrfvbegskejbdukri) covers the various HTTP adaptors that can be used in a deployment. It explains which adaptors are appropriate for your platform as well as how to build an adaptor from the source files included with WebObjects.
- [Data-Store Adaptor Installation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydanrrfvbuuqsfi5auoqy) describes the JDBC and JNDI adaptors that WebObjects applications can use to interact with data stores, such as databases and directory-services servers.

When you perform a complete installation of WebObjects Deployment on a computer, two types of files are copied to its hard disk: adaptor files and deployment files.

HTTP adaptors allow your web server to communicate with WebObjects application instances. The adaptor processes a single transaction, a request and its response, at a time. Normally, the request is forwarded to a single application instance, which, in turn, generates the response. Exceptions include error conditions or a request for an application that does not exist.

Typically an HTTP adaptor performs the following actions for each request:

1. Reads the request from the server, checks the URL, and collects header data and form data.
2. Finds an application to service the request. This is the part of the process that involves load balancing between instances.
3. Uses an existing socket connection to the application or connects a new socket to the application and forwards the request to the application.
4. Waits for and reads the response (status, headers, and content).
5. Returns the connection to the connection pool or—if the connection is transitory—closes the connection.
6. Sends the response to the client through the web server.

The executable files of the HTTP adaptors are placed in `/System/Library/WebObjects/Adaptors`. You can build your own adaptors using the source files for the default adaptors as a starting point. These source files are installed in `/Developer/Examples/WebObjects/Source/Adaptors`.

In addition to the HTTP adaptors, WebObjects applications that access a data store need to have an appropriate adaptor for that data store. Two types of data stores are supported, databases and directory services; these use JDBC and JNDI (Java Naming and Directory Interface), respectively.

Deployment files are divided into two groups:

- __Runtime environment__. The runtime environment of WebObjects is implemented in JAR (Java archive) files contained within _framework_ (`.framework`) bundles. WebObjects frameworks are installed in `/System/Library/Frameworks`. These frameworks are used by any WebObjects application, including the deployment tools of WebObjects.
- __Deployment tools__. WebObjects Deployment includes two deployment tools you use to configure and monitor your site. The files that make up these tools are placed in `/System/Library/WebObjects/JavaApplications`. Table 2-1 shows the purpose of each tool. For more information on the deployment tools, see [Managing Application Instances](Managing%20Application%20Instances.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydanrtfvbecssfijbukri).

  __Table 2-1__  The WebObjects deployment and administration tools

  | Filename | Application name | Purpose |
  | `JavaMonitor.woa` | JavaMonitor | Site configuration and administration |
  | `wotaskd.woa` | wotaskd | Instance management |

Depending on the purpose of the computer you’re installing the software on, there are three types of WebObjects Deployment installations you can perform:

- __Web server only__: On a computer that you want to use as the web server but on which you do not intend to run application instances (including the deployment tools), you need to install only the HTTP adaptor files.
- __Application host only__: On computers that you intend to use only as application hosts, you need to install only the deployment tools. (If you do not plan to run JavaMonitor on that computer, you can delete its files.)
- __Web server and application host__: When one computer can satisfy all your deployment needs or when you want a web server to also run application instances, you need to install the adaptor files and the deployment tools.

WebObjects uses a variety of HTTP adaptors to enable access to applications through a web server. Depending on your deployment platform, particular HTTP adaptors are installed by default.

Mac OS X Server supports Apache and CGI. The Apache adaptor is active by default. Requests in the form `http://.../cgi-bin/WebObjects/` are handled by the Apache adaptor. If you disable the Apache module, such requests are handled by the CGI adaptor.

If you want to use an HTTP adaptor other than the one installed by default on your platform, you need to build it and install it. This section discusses building HTTP adaptors from the source code in `/Developer/Examples/WebObjects/Source/Adaptors`.

Before building an adaptor, make sure that you have the following installed:

- WebObjects Deployment
- ANSI-C compliant compiler—for example, `gcc` version 2.7.2 or later
- `gnumake` version 3.74 or later
- Web server software

Follow these steps to build your adaptor:

1. Select the platform you want to build on by editing the `ADAPTOR_OS` variable in `make.config`.
2. Select the adaptor that you want to build by editing the `ADAPTORS` variable in `make.config`. You can build multiple adaptors for different web servers at the same time.
3. Modify the appropriate compile-time parameters in `Adaptor/config.h`. Most features can be configured at initialization time. Some, however, are determined during compilation; you change these by editing `config.h`.
4. Depending on the adaptor you want to build, you may need to make additional changes:

   - For Apache, modify the `APXS` variable in `make.config`. The default settings should work for Mac OS X Server.
   - For CGI, you might need to customize `CFLAGS` or `LDFLAGS` in `CGI/Makefile`. For example, you don’t need to define `-nopdolib` when you are not using the Apple PDO C compiler.
5. Set the `CC` variable in `make.config` to point at the compiler you want to use. The compiler must be an ANSI C compiler. The `CC` variable is set to `gcc` by default.
6. Type `make` in the `NEXT_ROOT/Developer/Examples/WebObjects/Source/Adaptors` folder.

In case you need to modify the default adaptors, Table 2-2 identifies the purpose of the source files in `/Developer/Examples/WebObjects/Source/Adaptors/`.

__Table 2-2__  Adaptor source description

| Source file | Description |
| `Apache/mod_WebObjects.c` | Interface modules that interact directly with the web server. |
| `CGI/WebObjects.c` | Interface modules that interact directly with the web server. |
| `Adaptor/config.h` | Configuration-parameters file. |
| `Adaptor/config.c` | Operating system–specific configuration items. |
| `Adaptor/transaction.c` | Implements request/response processing. |
| `Adaptor/request.c` | Structures and routines to collect headers and form data. Also function support for sending requests to applications. |
| `Adaptor/response.c` | Structures and routines to collect response headers and content. |
| `Adaptor/hostlookup.c` | Gets `hostent` structure for an application host using `gethostbyname` and caches the result. |
| `Adaptor/transport.h` | Declaration of application IPC API. |
| `Adaptor/nbsocket.c` | Transport is implemented with nonblocking sockets. This file provides timeouts and user-space buffering. |
| `Adaptor/loadbalancing.h` | Declaration of functions to provide load balancing. Load-balancing implementations need to define these functions. |
| `Adaptor/random.c` | Load-balancing routine that randomly selects any available application instance. |
| `Adaptor/roundrobin.c` | Load-balancing routine that selects an instance using a round-robin algorithm. |
| `Adaptor/loadaverage.c` | Load-balancing routine that selects an instance using the load average returned by each instance in its headers. |
| `Adaptor/log.c` | `printf` style logging to `/tmp/WebObjects.log`. Checks for the existence of `/tmp/logWebObjects`, an empty file that must be owned by root on UNIX platforms. This file should not be present in deployment mode. |
| `Adaptor/xmlparse.c` | Parses the configuration information supplied in an XML document. This is either supplied from wotaskd, a URL, or a file. |
| `Adaptor/WOURLCUtilities.c` | WebObjects URL-parsing routines. |
| `Adaptor/MoreURLCUtilities.c` | Additional utility functions to augment `WOURLCUtilities.c`. |
| `Adaptor/strdict.c` | String key–based dictionary. |
| `Adaptor/strtbl.c` | String key/value lookup data structure. |
| `Adaptor/list.c` | Data structure used to collect pointers. |

A successful build of the Apache adaptor yields a file named `mod_WebObjects.so`. This file should be copied into `/System/Library/WebObjects/Adaptors/Apache` on Mac OS X and `NEXT_ROOT/Library/WebObjects/Adaptors/Apache` on other platforms. In order for the adaptor to work, Apache must be configured to accept Dynamic Shared Objects (DSOs). Refer to the Apache web server documentation available at [http://www.apache.org](http://www.apache.org/) for more information on building Apache to accept DSOs. If the adaptor fails to build, it is probably because Apache is not built to accept DSOs.

Once you have built the adaptor and server, you need to configure the web server to handle WebObjects requests. See [Customizing HTTP Adaptors](HTTP%20Adaptors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydanrsfvbeeq2ei5feosa) for more information on configuring Apache.

After you have built and configured the server with the linked adaptor, you should start it and confirm that it’s working by moving aside the WebObjects CGI adaptor in the `cgi-bin` directory and making a few requests. You can determine whether the CGI or Apache adaptor is handling requests by turning on the logging feature of the adaptor as follows:

1. As root, execute the following command:

```
touch /tmp/logWebObjects
```
2. Make a request to a WebObjects application to initialize the log file.
3. Execute the following command:

```
tail -f /tmp/WebObjects.log
```
4. If the Apache web server is configured to use the CGI adaptor, each request is logged as

```
Info: <CGI> new request: /cgi-bin/WebObjects/MyApp
```
5. If the Apache web server is configured to use the WebObjects Apache module, each request is logged as

```
Info: <WebObjects Apache Module> new request: /cgi-bin/WebObjects/MyApp
```


The default CGI adaptor is a generic CGI adaptor designed to be used with all web servers that support CGI. There is a performance disadvantage when using CGI adaptors; therefore, you should consider using a server plug-in adaptor whenever possible.

To install this adaptor, copy the file `WebObjects` to your web server’s `cgi-bin` or `scripts` directory. This is done for you if you install WebObjects on a system with a web server installed.

It is possible to configure the CGI adaptor to contact the instance of wotaskd on localhost for adaptor configuration information including the list of instances. For deployment you normally want to use a different mechanism that is less expensive. Set up the CGI adaptor to use either a static file on the web server or a static URL for this information. For examples of this, see [Customizing HTTP Adaptors](HTTP%20Adaptors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydanrsfvbeeq2ei5feosa).

If there are problems executing the CGI adaptor on MacOS X, do the following:

- Make sure that the `WebObjects` CGI executable is installed in `/Library/WebServer/CGI-Executables/`.
- Verify that it is owned by root:admin.
- Make it executable by everyone.

Although generally not the best for production-level deployment, there is a good reason to use the CGI adaptor. It is useful for exercising the underlying request handler and debugging any customizations you may have made to the source code. Since all input to any CGI program is provided in the environment variables and `stdin`, the WebObjects CGI program can be conveniently run under a debugger.

To do this, set the following environment variables and values as shown in Table 2-3.

__Table 2-3__  CGI debugging variable settings

| Environment variable | Value |
| `REQUEST_METHOD` | `GET` |
| `SERVER_PROTOCOL` | `HTTP/1.0` |
| `QUERY_STRING` | `\?foo=bar` |
| `SCRIPT_NAME` | `/cgi-bin/WebObjects` |
| `PATH_INFO` | `/MyApps/MyCoolApp` |

If you want to include form data, set a `CONTENT_LENGTH` header and type the form as `stdin`. An alternative is to edit and execute the `TestCGI.sh` or `Env.csh` files provided in `/Developer/Examples/WebObjects/Source/Adaptors/CGI`.

This section provides resources that help you obtain and install the two types of data-store adaptors that WebObjects applications may require: database adaptors and adaptors for directory-services servers.

To ensure that your JDBC driver works with your database, you should get the latest JDBC driver that matches the version of your database and the version of Java JDK installed on your machine.

WebObjects provides access to directory services through the use of the JNDI adaptor in conjunction with a service provider. WebObjects has been tested with connections to the following Lightweight Directory Access Protocol (LDAP) servers:

- OpenLDAP Directory Server

To use this LDAP JNDI adaptor, you need to have the JNDI class libraries and the LDAP service provider from Sun Microsystems installed. These are both available from [http://java.sun.com/products/jndi](http://java.sun.com/products/jndi). On Mac OS X these are installed by default.

[Next](HTTP%20Adaptors.md)[Previous](WebObjects%20Deployment.md)

