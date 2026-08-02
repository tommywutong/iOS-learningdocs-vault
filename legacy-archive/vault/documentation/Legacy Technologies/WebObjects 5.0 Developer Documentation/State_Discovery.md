---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/WebObjectsAdaptors/State_Discovery.html
archived_at: '2026-07-15T08:12:16.980281Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Types_of_Adaptors.md)[!](The_WebObje_mation_Page.md)

## State Discovery

Your site's state is represented by

- a list of
  application hosts
- a list of running application instances on each host

The HTTP adaptor captures your site's state at regular intervals,
which you set when you configure the adaptor. You define the method
that the adaptor uses to gather state information by configuring
the adaptor itself. For details, see ["Overriding Default Configuration Settings"](Overriding__on_Settings.md#apple-ijbegrchjjduq).

The adaptor can obtain the state of your site using one of
three methods:

- __Multicast
  request__ The adaptor sends a multicast request to find
  out what application hosts are available. After the host list is
  compiled, the adaptor polls each host to get its list of running
  application instances
- __Host list__ This method requires that
  you configure the host list in the adaptor itself. As with the first
  method, the adaptor polls the hosts on the list for their lists
  of running application instances.
- __Configuration file__ The adaptor obtains
  the site's configuration by reading an __XML__ (Extensible
  Markup Language) formatted document.

The method that requires the least administration on your
part is the multicast request. If an application host goes down,
the adaptor automatically removes the application instances running
on it from its list of active instances. When the host is brought
back up, the adaptor adds the instances back to its list. You should
use this method if your site has many application hosts. See ["Using a Multicast Request"](#apple-ijbegrshjbdek) for
more information.

The second method, defining a host list for your adaptor,
eliminates the multicast request. Use this method if you do not
want the adaptor to send regular multicast requests out on your
network or if you seldom add or remove application hosts from your
site. This is the method that is active by default. However, the
host list contains only one host, `localhost`. For
details, see ["Using a Defined Host List"](#apple-ijbegskfizcee).

In the third method, using a configuration file, the HTTP
adaptor obtains your site's configuration by reading a file. This
file can be static or it can be dynamically updated as you configure
your site with Monitor. For details, see ["Using a Configuration File"](#apple-ijbegq2iifdee).

You can write the adaptor configuration file in one of two
ways:

- __Manually__ The
  information in the configuration file is stored in a structured
  document using the XML format. For details, see ["The HTTP Adaptor Configuration File"](#apple-ijbegscci5deu).
- __Using Monitor and wotaskd__ After configuring
  your site to your liking using Monitor, you can have a file created
  for you or you can copy and paste the information. See ["Creating the HTTP Adaptor Configuration File"](#apple-ijbegr2ci5fec) for more information.

### Using a Multicast Request

When you configure an adaptor to obtain your site's state
using a multicast discovery request, the adaptor obtains the list
of active application hosts by broadcasting a message to which each
computer configured as a WebObjects application host responds. After
the adaptor compiles the list of available hosts, it polls each
one to obtain its state (the list of running application instances).

There are drawbacks to using the multicast method:

- It increases
  network traffic. By default, the HTTP adaptor send a multicast request every
  100 seconds
- A host may become unavailable between discovery requests if
  the multicast request or a wotaskd process's response is lost
  (multicast is an inherently unreliable protocol).
- Normally, multicast broadcasts are limited to a subnet. However,
  you can configure your routers to pass on the multicast request
  to other subnets if you wish.

By default, wotaskd does not respond to multicast requests.
To be able to use the multicast request method, you must configure
wotaskd processes in your application hosts to respond to multicast
requests.

#### Multicast Request

To discover available hosts, the adaptor sends a host discovery
request on the multicast channel (a nonrouting IP address and a
port number), which is set to IP address `239.128.14.2` and
port `1085` by default.
The frequency of each multicast request is ten times as long as
the adaptor's configuration refresh interval. For details on how
to change the multicast channel, see ["Setting the Multicast Address and Port"](Overriding__on_Settings.md#apple-ijbegq2dizdes), ["WOPort"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iCommand_Line_Arguments.html), ["WOMulticastAddress"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iCommand_Line_Arguments.html), and ["WORespondsToMulticastQuery"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iCommand_Line_Arguments.html).
When a wotaskd process starts, it creates a UDP (User Datagram Protocol)
socket that listens to the multicast channel through which it receives
multicast requests.

|  |
| --- |
| __Note:__ If you change the address and port that adaptors use to send multicast requests, you must also change the address and port that wotaskd processes use to receive multicast requests. |

When each wotaskd process receives the multicast request,
it replies with its URL, such as `http://host1.site.com:1085`.
The adaptor in turn compiles a list of these URLs.

Sending a multicast request on an entire subnet is an expensive
procedure. If your available hosts never change, consider using
a defined host list instead.

#### Host Polling

After the HTTP adaptor constructs the host list, it polls
each application host on the list for information on the active
application instances running on it. Each wotaskd process, in turn,
sends its state information using the format in [Listing 4-2](#apple-ijbegqsfijceu). Host
polling to obtain information on active instances occurs at the
interval indicated in the configuration refresh interval setting
for the HTTP adaptor. [Figure 4-4](#apple-ijbegrscjfdum) illustrates the process used to determine the configuration
of the site in [Figure 4-3](Adaptors_Ap_s_and_Hosts.md#apple-ijbegr2ki5duc).

__Figure
4-4 Dynamic site configuration using multicast
request and polling__

![[image: ../Art/configadaptor_auto.gif]](../Art/configadaptor_auto.gif)

### Using a Defined Host List

This method is similar to the one described in ["Using a Multicast Request"](#apple-ijbegrshjbdek).
The only difference is that the HTTP adaptor skips the first part,
the multicast request. The host polling process occurs at the interval
set in the adaptor's configuration refresh interval setting.

You must explicitly define a host list for each adaptor. See ["Setting the Host List"](Overriding__on_Settings.md#apple-ijbegq2hirdec) for details
on defining the host list for each of the adaptors provided.

### Using a Configuration File

Using an HTTP adaptor configuration file is useful when you
want to have a static site configuration (one in which application
instances are not stopped after they are started) or if you want
to use Monitor to configure your site and have the adaptor read
your configuration changes immediately. (The adaptor reads the configuration
file every 10 seconds to determine which application instances are
active.)

This method also provides a way of having more than one configuration
of your site available. You can switch among different configurations
by placing the appropriate configuration file in the configuration
directory.

["The HTTP Adaptor Configuration File"](#apple-ijbegscci5deu) explains how the file
is structured and lists the properties that it defines. For instructions
on creating the configuration file and configuring the HTTP adaptor
to use it, see ["Creating the HTTP Adaptor Configuration File"](#apple-ijbegr2ci5fec).

#### The HTTP Adaptor Configuration File

You can set up the HTTP adaptor to get your site's configuration
by reading an HTTP adaptor configuration file (called `WOConfig.xml` by
default) in the configuration directory (/Library/WebObjects/Configuration by
default). You should have only one adaptor configuration file per
Web server so that it can perform load balancing effectively. (See ["Load Balancing"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iLoad_Balancing.html) for details.)
In addition, in a site with multiple Web servers, if two servers
share the configuration file, instead of deploying two sites you
would be deploying the same site twice. [Listing 4-1](#apple-krifqusfiyytamq) shows a configuration
file that defines a site with two application hosts (`ebruce.apple.com` and `ejays.apple.com`),
each running two application instances, one of the Payroll application
and the other of the HR application.

__Listing
4-1 A WebObjects adaptor configuration file__

```xml
<?xml version="1.0" encoding="ASCII"?>
<adaptor>
  <application name="Payroll" urlVersion="4">
    <instance id="1" port="2002" host="ebruce.apple.com"/>
    <instance id="2" port="2001" host="ejays.apple.com"/>
  </application>
  <application name="HR" urlVersion="4">
    <instance id="1" port="2001" host="ebruce.apple.com"/>
    <instance id="2" port="2002" host="ejays.apple.com"/>
  </application>
</adaptor>
```

The HTTP adaptor configuration file provides the HTTP adaptor
with information about your site's registered application instances.
The format of the configuration file is provided in [Listing 4-2](#apple-ijbegqsfijceu) (you
can also view it by opening the `woadaptor.dtd` file,
located in the /Developer/Examples/WebObjects/Source/Adaptors directory).
For information on the properties defined in the configuration file,
consult [Table 4-2](#apple-krifqusfiyytanq).

__Listing
4-2 Format of the HTTP adaptor configuration
file__

```xml
<?xml version="1.0" encoding="ASCII"?>

<!DOCTYPE WebObjectsAdaptorConfiguration SYSTEM "woadaptor.dtd">

<adaptor>
    <application name=STRING
            retries=NUMBER
            scheduler=["RANDOM"|"ROUNDROBIN"|"LOADAVERAGE"]
            dormant=NUMBER
            protocol="http"
            redir=URL
            poolSize=NUMBER
            urlVersion=["3"|"4"]
            additionalArgs="unspecified"
        >
        <instance    id=NUMBER  port=NUMBER  host=STRING
            sendTimeout=NUMBER
            recvTimeout=NUMBER
            cnctTimeout=NUMBER
            sendBufSize=NUMBER
            recvBufSize=NUMBER
            additionalArgs="unspecified"
        >
        </instance>
    </application>
</adaptor>
```


__Table
4-2 The properties of the HTTP adaptor
configuration file__

__|  |  |
| --- | --- |
| Attribute |  |__| `name` | This property is used by the adaptor to implement load balancing. The adaptor can load-balance only between instances with the same application name. The property can be used to create groups of instances, even when the instances share the same executable file. This argument is set automatically for instances started by wotaskd. |
| `retries` | The number of times a request is retried (trying several instances) if a communications failure occurs before an error page is returned to the Web server. |
| `scheduler` | The load-balancing scheme used by the adaptor for instances of the application. The options provided by WebObjects are Round-Robin, Random, and Load Average. You can also use a custom load balancer by choosing the Custom option and entering the load balancer's name. |
| `dormant` | The number of times the adaptor skips an instance of the application before trying again. |
| `redir` | The URL that the user is redirected to when an instance fails to respond to a direct request. |
| `poolSize` | The maximum number of simultaneous connections the adaptor should keep open for each configured instance. |
| `urlVersion` | The WebObjects version to use for URL parsing and formatting. All WebObjects 4, 4.5, and 5 applications use version 4 URLs by default. |
| `additionalArgs` | Additional information to send to the instance when it's started. |
| `id` | The instance's identification number. Must be unique for the load-balancing process to operate correctly. |
| `port` | The port on which the instance runs. |
| `host` | Specifies the network interface that an instance binds to. This argument should only be used on hosts with multiple network interfaces (IP addresses). |
| `sendTimeout` | The length of time, in seconds, that the adaptor attempts to send data to an instance of the application before giving up. |
| `recvTimeout` | The length of time, in seconds, that the adaptor waits for a response from an instance of the application before giving up. |
| `cnctTimeout` | The length of time, in seconds, before the adaptor gives up connecting to an instance. |
| `sendBufSize` | The size, in bytes, of the TCP/IP socket send buffer that's used for adaptor-to-instance communication. |
| `recvBufSize` | The size, in bytes, of the TCP/IP socket receive buffer that's used for adaptor-to-instance communication. |

#### Creating the HTTP Adaptor Configuration File

You can define your site's configuration by writing the
HTTP adaptor configuration file by hand. However, Monitor provides
you with an easy-to-use interface that facilitates that task.

["Deployment Tasks"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iDeployment_Tasks.html) shows you
how to configure your site using Monitor. When you are satisfied
with your configuration, you can save your settings into a configuration
file by copying and pasting or by telling wotaskd to write the file.

To use the copy-and-paste method, follow these steps:

1. In Monitor,
   display the Hosts page.
2. Click YES for any host.

   The host configuration page is
   displayed in a new Web browser window.
3. Copy the contents of the section "Adaptor Config as written
   to disk—All Registered Applications and Instances," as shown
   in [Figure 4-5](#apple-ijbegrcbjjdec).

   __Figure
   4-5 Copying the information that makes
   up the HTTP adaptor configuration file__

   ![[image: ../Art/woconfigxmlcopy.gif]](../Art/woconfigxmlcopy.gif)
4. Using a text editor, create a new file and paste the contents
   of the clipboard into it.
5. Save the file as `WOConfig.xml` (or
   any other name you choose) in the configuration directory.

   __Figure
   4-6 Creating and saving the HTTP adaptor
   configuration file__

   ![[image: ../Art/woconfigxmlpaste.gif]](../Art/woconfigxmlpaste.gif)

If instead of copying and pasting you want wotaskd to create
the configuration file for you, you can start a wotaskd process
specifically to create the file or you can tell wotaskd to continually
maintain the configuration file.

To start a wotaskd process specifically to create the file,
you must first stop the process that corresponds to the site you
configured if it's already running on the Web server computer.

To start a wotaskd process that writes the configuration file
to the default location, execute the following two commands using
your command shell editor:

```
cd /System/Library/WebObjects/JavaApplications/wotaskd.woa
./wotaskd -WOPort <port> -WOSavesAdaptorConfiguration true
```

To specify a different location for the HTTP adaptor configuration
file, follow the instructions in ["WODeploymentConfigurationDirectory"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iCommand_Line_Arguments.html).
If you want to give the file a different name, ["Setting the HTTP Adaptor Configuration File"](Overriding__on_Settings.md#apple-ijbegq2fizdui) shows
you how.

To tell wotaskd to maintain the configuration file on a permanent
basis, add the following to the WOServices script line that starts
the wotaskd process:

```
-WOSavesAdaptorConfiguration true
```

When you restart your Web server, the HTTP adaptor configuration
file is updated every time you make a change to your site's configuration
through Monitor. The changes are picked up by the HTTP adaptor the
next time it reads the configuration file.

To configure the HTTP adaptor to read the configuration file
instead of using a multicast request or a host list, follow the
instructions in ["Setting the HTTP Adaptor Configuration File"](Overriding__on_Settings.md#apple-ijbegq2fizdui).

[!](Types_of_Adaptors.md)[!](The_WebObje_mation_Page.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
