---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeltaDoc/WebObjects.html
archived_at: '2026-07-15T08:04:35.698037Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
What's New in WebObjects

---

[!](What%27s%20New%20in%20WebObjects%204.5.md)

# What's New in the WebObjects Framework

This chapter describes changes made to the Web Objects
Framework and the Monitor application between release 4.0 and 4.5.
It describes changes made to existing features and describes new
features you may want to start using in your applications.

This chapter is organized into the following sections:

- ["Executive Summary"](#apple-incuqssdivdeg)
- ["Monitor Changes"](#apple-incuqr2kirfeo)
- ["Web Server Adaptor Changes"](#apple-ijbukq2fi5euu)
- ["Configuring the Web Server Adaptor"](#apple-incuqq2bjbcui)
- ["Licensing Changes"](#apple-inbeoqsjivbuk)
- ["Miscellaneous Changes"](#apple-incuqskki5duo)
- ["Supplemental Documentation"](#apple-incuqq2gijfeu)

Between WebObjects 4.0 and 4.5 there have been a number of
changes to the WebObjects Framework APIs. These changes are detailed
in a separate chapter, ["WebObjects Framework API Changes"](WebObjects%20Framework%20API%20Changes.md#apple-ijdumq2gijdek). In addition. WebObjects application
developers will likely be interested in the new Event Logging feature;
see ["Event Logging"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoq2gi5cuk).

## Executive Summary

The changes to the WebObjects Framework for the 4.5 release
of WebObjects can be summed up as follows:

- MonitorProxy has been replaced by `wotaskd`.
- The web server adaptors by default now get their configuration
  information from `wotaskd` via http
  requests, and no longer maintain a temporary configuration file
  in `/tmp`. The web server adaptor can be
  configured to retrieve its configuration information from a file
  on the current or a different web server; see ["Accessing Configuration Information"](#apple-ijbeuq2iijbum) for
  details.
- The web server adaptors are now capable of automatically determining
  which WebObjects application servers are available and which applications
  are running on those servers.
- The web server adaptor configuration file, if used, now uses
  an XML format (see the online document _Deploying WebObjects
  Applications_ for details).
- A number of aspects of WebObjects adaptor operation are now
  configurable at runtime.
- Much of the common functionality between WORequest and WOResponse
  has been abstracted into a new class, WOMessage, that represents
  messages with either HTML or-if your WebObjects application is
  written in Java-XML content. WOMessages allow your WebObjects
  applications to communicate with other WebObjects applications as
  well as with applications that "speak " XML.
- Installed as a part of WebObjects is the `com.ibm.xml.dom` package
  (IBM's alphaWorks), which contains various XML parsers for Java
  written by IBM. The WebObjects Framework uses the DOM parser to
  generate document and document fragment objects from XML data (or
  to manipulate and/or generate XML data from a document object).
  For more information on the alphaWorks parser, including complete documentation,
  point your web browser to
  `http://www.alphaworks.ibm.com` and
  search for "XML Parser for Java".
- Components can now be made stateless. A single instance of
  each stateless component is shared between multiple sessions, reducing
  your application's memory footprint.

To support the above new functionality, there have been various
additions to the WebObjects Framework API's. For a complete list
of changes, see ["WebObjects Framework API Changes"](WebObjects%20Framework%20API%20Changes.md#apple-ijdumq2gijdek).

## Monitor Changes

Monitor and MonitorProxy have changed substantially in WebObjects
4.5. In particular, MonitorProxy has been replaced with a new process
named "`wotaskd`" that's responsible for
all things related to deployment on a particular host. Many of the
responsibilities formerly assumed by the Monitor application are
now handled by `wotaskd` (each
host involved in a WebObjects deployment now runs `wotaskd`).
Monitor now simply changes settings in your deployment environment.

|  |
| --- |
| __Note:__ In theory, you could run multiple `wotaskd`'s on different ports on the same machine and have different web servers talk to the same app servers but see different applications. This has not been tested, however. |

Monitor registration with `wotaskd` no
longer used DO (Distributed Objects).

Monitor has a number of minor UI enhancements throughout,
including:

- the "File Transfer Wizard," which allows
  Monitor users to move files and directories between hosts being
  monitored, and
- the "Path Wizard," which should appear everywhere you're
  required to enter a path in Monitor, allowing you to browse the
  file system on a particular host.

There are new settings that can be altered from within Monitor
that affect the WebObjects adaptors.

## Web Server Adaptor Changes

The WebObjects 4.5 API-based web server adaptor is intended
to be used as a server plug-in where state information can be maintained
from request to request. CGI is supported, but beyond the fact that
it's easier to debug, the CGI adaptor provides no real benefit
over the API-based adaptor.

Among the features which differentiate it from the 4.0 WebObjects
adaptor:

- Many aspects are configurable at runtime, including:

- Load balancing strategy
- Application/adaptor communication transport
- Socket timeouts
- Application URL version (the adaptor supports WebObjects 3.5,
  4.0, and 4.5 application URLs)
- Error redirect URLs

- It supports a new, additional scheduling technique: "Instance
  load-based scheduling."
- It uses an XML-based configuration file format (see the online
  document _Deploying WebObjects Applications_ for
  details).
- Configuration for multiple web servers is simpler and more
  automatic: configuration files are no longer required.
- The web server adaptor by default automatically discovers
  WebObjects-enabled systems.
- Performance has been improved.

For information on installing the adaptor, see the installation
files for CGI, Apache, Microsoft ISAPI, Netscape NSAPI or Netscape
WAI.

|  |
| --- |
| __Note:__ The WebObjects 4.5 NSAPI adaptor won't work with Netscape Enterprise 3.5 servers. If you want to use the NSAPI adaptor, you'll need to upgrade to Netscape Enterprise 3.6, or recompile with 3.5. |

## Configuring the Web Server Adaptor

The web server adaptors by default now get their configuration
information from `wotaskd` via HTTP
requests, and no longer maintain a temporary configuration file
in `/tmp`. This release also includes support
for the automatic discovery of systems running WebObjects by web
server adaptors. This should remove the necessity to administer
the web servers, beyond the initial adaptor installation. This automatic
discovery mechanism is the default; to disable it, you'll need
to change the web server adaptor's configuration file as outlined in ["Accessing Configuration Information"](#apple-ijbeuq2iijbum).

When the web server adaptor starts up, and at intervals determined
by the configuration refresh interval setting, the adaptor sends
out a multicast request in an effort to discover which WebObjects
app servers are available. Each app server's `wotaskd` process
replies with its URL (`http://me.myself.com:1085`).
The adaptor constructs a list of these URLs and then polls each
in turn to get the full site configuration information.

If the configuration refresh interval is 10 seconds, the discovery
broadcast happens every 100 seconds (the discovery broadcast occurs
a factor of 10 less frequently).

### Accessing Configuration Information

Web server adaptor configuration information can now be obtained
in a number of ways. In addition to the default "multicast"
mode, the web server adaptor can be set to retrieve configuration
information from one or more WebObjects application servers running `wotaskd`,
or it can be set to obtain configuration information from a configuration
file, which can be located either on the local machine or on a machine
running a different web server.

By default, the adaptor uses multicast to communicate with
all machines on same subnet that are running `wotaskd`.
From the responses, the adaptor builds up a list of WebObjects application
servers, along with all of the information necessary to allow access
to all of the the WebObjects application instances running on those
machines. Although this is the default mode of operation, you can
explicitly specify that the Web server adaptor obtain its configuration
information this way using an entry similar to the following in
your apache.conf file:

> ```
> # Retrieve configuration information using multicast
> WebObjectsConfig webobjects://239.128.14.2:1085 10
> ```

|  |
| --- |
| __Note:__ For simplicity, only entries in apache.conf are shown. However, the corresponding entries can be made for all other supported web servers (with ISAPI you either need to make an entry in the Windows NT registry as shown in ["Changing the Web Server Adaptor Multicast Address"](#apple-ijbeur2iinbue)or you need to rebuild the adaptor). See the installation instructions for your particular web server-in  $NEXT_ROOT/Developer/Examples/WebObjects/Source/Adaptors-for more information. |

In the above, as in all of the configuration file entries
shown in this section, the final value-10 in this instance-indicates
the configuration refresh interval.

While the multicast mode requires no configuration, in a real
deployment scenario you may wish to limit which application servers
can be accessed from a given web server. For instance, you may have
multiple web servers that each need to access a different set of WebObjects
applications. Or, you may want to prevent end-user access to WebObjects applications
in development or being tested on the same subnet. To explicitly
specify the set of WebObjects application servers that can be accessed
from a given web server, use an entry similar to the following in
your apache.conf file:

> ```
> # Retrieve config file from wotaskd (multiple hosts can be listed)
> WebObjectsConfig http://hostA:1085,http://hostB:1085 10
> ```

Note that `wotaskd` must be running
on each WebObjects application server in order for the above to
work.

You can also have the web server adaptor obtain its configuration
information from a configuration file. Using a configuration file
allows you to further limit what a given web server can access:
in the configuration file you can specify that the web server can
access only specific applications (or even specific instances of
a WebObjects application) on individual WebObjects application servers.
This configuration file now uses an XML format (previously it was
formatted as a property-list) which is fully described in the online
document _Deploying WebObjects Applications_.
Place an entry similar to _one_ of the following
in your `apache.conf` file to have the web
server adaptor obtain its configuration information from a file:

> ```
> # Retrieve config information from a file (XML-formatted config file)
> WebObjectsConfig file:///tmp/WebObjects.xml 10
> ```

or:

> ```
> # Retrieve config information from a file (old plist-style config file)
> WebObjectsConfig file:///tmp/WebObjects.conf 10
> ```

or:

> ```
> #Retrieve config information from a file on a different web server
> WebObjectsConfig http://my.webserver.com/WebObjects.xml 10
> ```

#### Changing the Web Server Adaptor Multicast Address

The adaptor sends discovery requests out on a particular multicast
"channel" (which is a combination of the IP address and the
port). The defaults are:

Default IP Address: `239.128.14.2`

Default port: `1085`

The default multicast address is within the "Adminstratively
Scoped Domain." That is, it's within the range of addresses
intended for internal use inside organizations.

For Apache, place the following in your `apache.conf` (the
final value-10 in this instance-indicates the configuration
refresh interval):

> ```
> WebObjectsConfig webobjects://239.128.14.2:1085 10
> ```

For CGI, either recompile, or set the `WO_CONFIG_URL` environment
variable as above.

|  |
| --- |
| __Note:__ With Apache, you'll need the `SetEnv` command, which comes with the "env" module. Note that Mac OS X Server doesn't switch this module on by default. |

For NSAPI, place something like the following in your `obj.conf`:

_Standard:_

> ```
> Init fn="WebObjects_init" root="/opt/ns-home/docs"      config="http://localhost:1085"
> ```

_Multicast:_

> ```
> Init fn="WebObjects_init" root="/opt/ns-home/docs"      config="webobjects://239.128.14.2:1085"
> ```

For ISAPI, add the following to the registry:

> ```
> \\SOFTWARE\\Apple\\WebObjects\\Configuration\\CONF_URL      webobjects://239.128.14.2:1085
> ```

By default `wotaskd` listens for multicast
discovery requests on IP address `239.128.14.2`.
If you configure the web server adaptor to send such requests to
a different IP address, you must also set the `WOConfigMulticastAddress` user
default on machines running `wotaskd (`you
must to do this as root/administrator). One way to do this is to
modify the startup script to set this user default as follows:

> ```
> defaults write wotaskd WOConfigMulticastAddress 239.128.14.2
> ```

If you don't change the multicast IP address, the above `defaults
write` isn't necessary.

### Disabling or Protecting Administrator Access

In WebObjects 4.5, sending the URL `http://
someHost/cgi-bin/WebObjects/xyzzy` results
in the webserver adaptor displaying information about all available
application instances. As a convenience to the developer, this
functionality is enabled by default. This has certain security implications,
however. For deployment this behavior should either be turned off or
protected with a username and password.

|  |
| --- |
| __Note:__  When `xyzzy` output is password protected, you access the application instance display by supplying a URL of the form: `http://someHost/cgi-bin/WebObjects/xyzzy?username+password` |

You protect the `xyzzy` output
by specifying a username and password. To disable it altogether,
simply specify a username of "disabled". How you do this depends
on which webserver you're using. The following sections detail
how you disable or protect this feature for a number of common webservers.

#### Apache with mod_WebObjects.so

To completely disable `xyzzy` output,
add the line

> ```
> WebObjectsAdminUsername disabled
> ```

to the bottom of the apache.conf file.
To provide username and password protection, add the following two
lines at the bottom of the apache.conf file:

> ```
> WebObjectsAdminUsername someName
> WebObjectsAdminPassword somePassword
> ```

#### NSAPI Adaptors

To completely disable `xyzzy` output,
add the following to your obj.conf file:

> ```
> Init fn=WebObjects_init root="C:/Netscape/Suitespot/docs"
> config="webobjects://239.128.14.2:1085" username="disabled"
> ```

To provide username and password protection, add something
like the following to your obj.conf file (providing
your own username and password as appropriate):

> ```
> Init fn=WebObjects_init root="C:/Netscape/Suitespot/docs"
> config="webobjects://239.128.14.2:1085" username="joe" password="secret"
> ```

#### ISAPI Adaptor

To completely disable `xyzzy` output,
add the following registry entry:

> ```
> \\HKEY_LOCAL_MACHINE\\SOFTWARE\\Apple\\WebObjects\\Configuration\\WOUSERNAME
>     disabled
> ```

To provide username and password protection, add registry
entries similar to the following (providing your own username and
password as appropriate):

> ```
> \\HKEY_LOCAL_MACHINE\\SOFTWARE\\Apple\\WebObjects\\Configuration\\WOUSERNAME
>     joe
> \\HKEY_LOCAL_MACHINE\\SOFTWARE\\Apple\\WebObjects\\Configuration\\WOPASSWORD
>     secret
> ```

#### WAI

To completely disable `xyzzy` output,
add the following to your obj.conf file:

> ```
> Init fn="WebObjectsServiceInit" root="C:/Netscape/Suitespot/docs"  config="webobjects://239.128.14.2:1085" username="disabled"
> ```

To provide username and password protection, add something
similar to the following to your obj.conf file
(provide your own username and password as appropriate):

> ```
> Init fn="WebObjectsServiceInit" root="C:/Netscape/Suitespot/docs"  config="webobjects://239.128.14.2:1085" username="joe" password="secret"
> ```

#### CGI

There are two options for disabling or protecting `xyzzy` output
when using CGI. First, you can uncomment the relevant code (shown
below) in main.c and then recompile the CGI adaptor.

> ```
> /*
>  * SECURITY ALERT
>  *
>  * To disable xyzzy, uncomment the next line.
>  * st_addStatic(options, WOUSERNAME, "disabled");
>  *
>  * To specify an xyzzy username and password, uncomment the next two lines.
>  * st_addStatic(options, WOUSERNAME, "joe");
>  * st_addStatic(options, WOPASSWORD, "secret");
>  *
>  */
> ```

Alternatively, if the webserver is configured to pass environment
variables, the CGI adaptor will read them. For example, configure
Apache to load the module mod_env.so by adding
or uncommenting the lines in apache.conf.

> ```
> LoadModule env_module         /System/Library/Apache/Modules/mod_env.so
> AddModule mod_env.c
> ```

You will also need to add the following System directive in apache.conf:

> ```
> PassEnv WO_XYZZY_USERNAME WO_XYZZY_PASSWORD
> ```

To completely disable `xyzzy` output,
you must then create an environment variable `WO_XYZZY_USERNAME` and
set its value to "disabled".

To provide username and password protection, create two environment
variables, `WO_XYZZY_USERNAME` and `WO_XYZZY_PASSWORD`,
and set them to, for example, "joe" and "secret" respectively.

## Licensing Mechanism

The dynamic licensing mechanism in WebObjects 4.5 has the same goals as in previous releases,
but a different implementation.
However, WebObjects
4.5 changes both the registration mechanism for instances and the
way the configuration is picked up by the webserver adaptors.When
the license is correctly enforced, these changes mean certain usage
that was possible (though not strictly conforming to the license)
with WebObjects 4.0 is no longer possible with 4.5.

Unregistered instances appear with an instance ID of -1. This
is all that is allowed with the restricted license. If an app sees
a URL with a positive instance ID and the license is restricted,
it will generate a "more than one instance detected" error message.
This error simply means that there's an instance out there using
a positive instance ID when only -1 is allowed. In this instance,
it does _not_ literally mean there is more than
one instance running.

Apps now register via a UDP heartbeat with `wotaskd`.
This fixes a large number of problems with the way the old monitoring
scheme worked, but, if `wotaskd` knows about
it, any app that registers with the correct name on a given port
will be given the instance ID assigned for that app name and port
combination. This can mean that your app gets a "deployment"
instance ID when your license does not actually allow that. This
behavior is different from 4.0, since in 4.0 you either built the .conf file
yourself (and thus could do what you liked), or you allowed the
adaptor to pick up the .conf file from /tmp,
in which all instance IDs were set to -1. You can avoid this problem
in WebObjects 4.5 by either picking a different port or removing
the instance from the configuration on that host using Monitor.

WebObjects 4.5 by default performs instance discovery via
multicast. On a large subnet with many machines running WebObjects,
instance discovery could produce a lot of replies. WebObjects 4.5
filters out non-deployment instances that aren't running on the same
machine as the adaptor, so the only ones you wind up seeing are
those you should be able to talk to, and the possibility of name/port
collision in the adaptor is reduced. This filtering basically means
you can't talk to an app instance that isn't "deployed"
if the webserver and adaptor are running on a different machine.
To make this work in WebObjects 4.0 you had to create your own configuration
file (by copying the configuration file in /tmp on
the other machine) and use -1 for the instance IDs. In Webobjects
4.5, you should be able to get this old WebObjects 4.0 behavior
by using a file URL to specify the adaptor configuration file. See ["Accessing Configuration Information"](#apple-ijbeuq2iijbum) for more information on specifying an
adaptor configuration file.

## Miscellaneous Changes

In addition to the numerous major changes listed elsewhere
in this document, a number of smaller changes are important to note:

- Configuration files have moved from $(NEXT_ROOT)/Library/WebObjects/Configuration to $(NEXT_ROOT)/Local/Library/WebObjects/Configuration.
  As with all end-user configurations, /Local is
  reserved for files which you change.
- The `WOMonitorHost` user default (and
  command-line argument) has been deprecated. WOF always tries to
  register with the service named `wotaskd` on `localhost`.
- This release supports a `WORequiresWOF40Compatibility` user
  default that re-enables certain behaviors of the 4.0 release. If
  you're having problems with an application you've ported from
  WebObjects 4.0, set the `WORequiresWOF40Compatibility` user
  default to "YES".
- The WORadioButtonList dynamic element has been deprecated.
  Use WORadioButtonMatrix (defined in the WebObjectsExtensions Framework)
  instead.

## Supplemental Documentation

The following documentation supplements that found in the _WebObjects
Developer's Guide_.

### Direct-Connect Mode

For deployment, a web server should be running to receive
HTTP requests and to forward them through the WebObjects adaptor.
To simplify the development process, though, WebObjects applications
are capable of receiving HTTP requests directly. This is the default;
invoke WOApplication's `setDirectConnectEnabled` method
to disable direct-connect mode.

This feature has several advantages:

- You can debug applications on a machine that
  doesn't have a web server present.
- You don't have to install project directories under the
  web server's document root in order to test them.
- Running without an HTTP server uses less memory on your development
  machine.
- The WebObjects example applications don't need to be installed
  under the web server's document root (they are installed under `Developer/Examples/WebObjects`).

The `WOPort` command-line option
(also settable from Monitor) allows you to specify the number of
the port where the application should listen for requests when operating without
a web server. By default, `WOPort` is
-1, which assigns an arbitrary high port number to the application.
Thus, you aren't required to specify a port number when in direct-connect
mode. However, it's generally a good idea to assign a specific
port number.

Note that if you do want to use a web server to test WebObjects
examples, you can still do so. Before you do, perform a "make
install" (be sure to set `INSTALLDIR_WEBSERVER` in
the makefile preamble) to install the example's web server resources
(such as image files and Java client-side classes) in the web server's
document root, just as you do when installing a WebObjects application.
If you put your application in a directory other than "WebObjects"
under your document root, set the `WOApplicationBaseURL` option
to the `.woa` directory's
path relative to the document root (`WOApplicationBaseURL` is
set to `/WebObjects` by
default). If you don't perform these steps, the web server won't
be able to find web server resources; when you run the application,
you'll see broken images, and client-side classes won't be loaded.

See the following section for more on developing with and
without a web server.

### Rapid Turnaround Mode

WebObjects is largely an interpreted environment. The HTML
templates, declarations files, and WebScript files each represent
interpreted languages. One of the main benefits of an interpreted
environment is that you needn't recompile every time you make
a change to the project. The ability to test your changes without
rebuilding the project is called "rapid turnaround" and, when
using rapid turnaround capability, you're said to be in "rapid
turnaround mode."

WebObjects supports rapid turnaround of `.html`, `.wod`,
and `.wos` files within
application projects, framework projects, and subprojects of either
application or framework projects.

To support rapid turnaround, WebObjects must be able to locate
the resources of your application and its associated frameworks
within your system's projects rather than the built products (the `.woa` or `.framework` wrappers).
To tell WebObjects where to look for your system's projects you
must define the `NSProjectSearchPath` user
default. Set this default to an array of paths where your projects
may be found. (Relative paths are taken relative to the executable
of your project.) The order of the entries in the array defines
the order in which projects will be located. The default `NSProjectSearchPath` is `("../..")`, which
causes WebObjects to look for any other applicable projects in the
directory where your application's project resides. For example,
if your application's executable resides within:

> ```
> c:\web\docroot\WebObjects\Projects\MyProject\MyProject.woa
> ```

then from the executable's directory, `"../.."` would
point to:

> ```
> c:\web\docroot\WebObjects\Projects
> ```

If you've set your project's "Build In" directory
to something other than the default, `"../.."` isn't
likely to be appropriate; you should set your `NSProjectSearchPath` to
point to the directories where you keep your projects while you
work on them.

When your application is starting up, pay close attention
to those log messages which indicate that a given project is found
and will be used instead of the built product. Many problems can
be solved by understanding how to interpret this output. If no such
log message is seen for a given project, it won't be possible
to use rapid turnaround for that project.

Pay close attention when you have several projects with the
same name in the same directory. This often happens when you have
several copies of the same project as backups in your project directory.
For example, you might have:

> ```
> c:\web\docroot\WebObjects\Projects\MyApp
> c:\web\docroot\WebObjects\Projects\Copy of MyApp
> c:\web\docroot\WebObjects\Projects\MyAppOld
> ```

Even though the folders containing the projects have different
names, the `PB.project` files within
them might be identical. WebObjects uses the `PROJECTNAME` attribute
inside your project's `PB.project` file
to determine the name of the project, not the name of the directory for
the project. If this happens with in a WebObjects application, WebObjects
checks the path of the project in question against the path to the
executable (after resolving symbolic links). and chooses the project
whose path matches the initial portion of the executable's path
(thus, in the above example it would choose `MyApp`).
If multiple projects with the same `PROJECTNAME` attribute
reside within a single directory in a framework project, WebObjects chooses
the one who's `PROJECTNAME` matches
the prefix of the framework's project directory.

#### Rapid Turnaround and Direct-Connect Mode

Direct-connect mode allows you to test your application without
involving a web server. This means that you don't have to install
your web server resources under the document root of your web server.
The result is that rapid turnaround is even more convenient when in
direct-connect mode because you needn't rebuild to install web
server resources changes to the document root. See ["Direct-Connect Mode"](#apple-incuqrsgiffeg) for
more information on Direct-Connect Mode.

#### Testing With a Web Server

When you're working in direct-connect mode, few issues arise
with respect to rapid turnaround. If your application has features
which require a web server even for testing, however, there are
a couple of things to know to make rapid turnaround work for you. Specifically,
since you are relying on the web server to locate files within `WebServerResources`,
you must follow these guidelines:

- Your projects must reside somewhere below your
  web server's document root.
- `NSProjectSearchPath` should
  point to all projects of interest.
- For application projects, the `WOApplicationBaseURL` user
  default should specify the directory containing the application
  project. For example, if your application's project folder is:
  > ```
  > c:\web\docroot\WebObjects\MyApp
  > ```

   then
  the `WOApplicationBaseURL` user default
  must be "`/WebObjects`".

- For framework projects, the `WOFrameworksBaseURL` user
  default should specify the directory containing all framework projects
  used by the application. For example, if your application uses `MyFramework.framework` and
  that project resides in:
  > ```
  > c:\web\docroot\WebObjects\Frameworks\MyFramework
  > ```

   then
  the `WOFrameworksBaseURL` user default
  must be "`/WebObjects/Frameworks`".

Conveniently, the two examples above use the default locations
for `WOApplicationBaseURL` and `WOFrameworksBaseURL`;
if your projects reside in these default locations, you need only set `NSProjectSearchPath`.

Also, while it is possible to point `WOApplicationBaseURL` and `WOFrameworksBaseURL` to
other locations, it is not suggested that `WOFrameworksBaseURL` be
moved since all WebObjects applications use `WOExtensions.framework`,
which resides in the default location. If you set `WOFrameworksBaseURL` to
point elsewhere, one side effect will be that the images in the "Raised
Exception" panel will not render.

[!](What%27s%20New%20in%20WebObjects%204.5.md)
