---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/Application__Properties.html
archived_at: '2026-07-15T08:12:15.447664Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Deployment%20Settings%20Reference.md)[!](Command_Line_Arguments.md)

## Application Configuration Properties

There are several settings that Monitor, wotaskd, and application
instances use in a deployment. You can set the value of these properties
in Monitor, in the command line, or in an application's `Properties` file
(which you would have to create and place in the `Contents/Resources` directory
of the application). The following sections describe all the settings
and their function.

### Application Settings

The following sections describe the properties that apply
to all the instances of an application. In Monitor, you set the
value of these properties in the Application Settings section of
the application configuration page.

#### Adaptor

The default adaptor class an instance uses. (This is not the
HTTP adaptor used by the Web server.) You use this if the application
defines a subclass of the WOAdaptor class to be used to create adaptor
objects (instead of using the WOAdaptor class itself).

#### Adaptor Threads

The number of worker threads that the adaptor creates to handle
requests to the application. It applies only to adaptor objects
of the WODefaultAdaptor class in WebObjects 4.5.

#### Listen Queue Size

Determines the depth of the listen queue. While the instance
handles a request, the socket buffer can hold as many additional
requests as this setting indicates before it starts refusing them.
If you expect spikes in the traffic level of a specific application,
consider increasing the value of this property. While it does not
necessarily improve performance, or allow the instance to process
more requests at sustained high loads, it may reduce the number
of times an application's user has to retry to send a particular
request during high-traffic periods.

Keep in mind that if an application instance's listen queue
size becomes full and a request is refused by it, the request does
not get redirected to another instance with space left over in its
queue. The client will have to resend the request.

#### Maximum Adaptor Threads

The maximum number of worker threads the HTTP adaptor creates
to handle requests to the application. It applies only to adaptor
processes of the WODefaultAdaptor class in WebObjects 5. The purpose
of these threads is to process TCP or UDP packets; they have nothing
to do with request processing.

#### Minimum Adaptor Threads

The initial number of worker threads the adaptor creates to
handle requests to the application. It applies only to adaptor processes
of the WODefaultAdaptor class in WebObjects 5.

#### Name

This property is used by the adaptor to implement load balancing.
The adaptor can load-balance only between instances with the same
application name. The property can be used to create groups of instances,
even when the instances share the same executable file. This argument
is set automatically for instances started by wotaskd.

#### Phased Startup

If this option is selected, when a wotaskd process starts
up, the instances that it manages that have [Auto Recover](#apple-ijbusqsgjbceo) selected are started
one-at-a-time instead of all at once. This option is selected by
default. For more information, see ["Auto Recover"](#apple-ijbusqsgjbceo).

#### Starting Port

The first port number to try to assign to a new instance of
the application. If the port is in use by another instance (of any
application), the next nonassigned port number is used.

#### Time Allowed for Startup

The number of seconds Monitor waits for an instance to start
before determining that the instance failed to start.

### Instance Settings

The following sections explain the properties that can be
set in Monitor in the New Instance Defaults section of the application
configuration page and in the Instance Settings section of the instance
configuration page.

#### Additional Arguments

Additional information to send to the instance when it's
started.

In particular, you may want to use the following additional
arguments:

- `WOSessionTimeOut` (For
  details, see ["WOSessionTimeOut"](Command_Line_Arguments.md#apple-ijbegqshi5buu).)
- `WOStatisticsPassword` (For
  details, see ["WOStatisticsPassword"](Command_Line_Arguments.md#apple-ijbegq2iirfem).)

#### Auto-Open In Browser

Determines whether the instance automatically opens a Web
browser window to the application's URL (starting up the browser
if necessary).

#### Auto Recover

Indicates whether instances are restarted automatically whenever
they become unresponsive or are manually shut down.

#### Caching Enabled

Determines whether the instance caches component definitions
instead of parsing HTML code and declaration files each time a request
is processed. (A component is a Web page or a portion of one.)

#### Debugging Enabled

Determines whether application instances print debugging messages
to the standard error stream during startup.

#### ID

The instance's identification number. Must be unique for
the load-balancing process to operate correctly. (This property
is not available in the New Instance Defaults section.)

#### Lifebeat Interval

Determines the interval, in seconds, between lifebeats.

#### Minimum Active Sessions

The minimum number of active sessions an instance must have
before it can be terminated by Monitor. (A session is an object
of the WOSession class that stores user-state information.) See ["Scheduling Settings"](#apple-ijbusrkhjbceq).

#### Output Path

Allows you to redirect the instance's standard output and
standard error streams to the directory specified. The file generated
is named as follows:

```
<application name>-<instance ID>
```


#### Path

Location of the launch script file for the application. For
example, `MyApp` for Mac
OS X and Solaris, and `MyApp.cmd` for
Windows 2000.

#### Port

The port on which the instance runs. (This property is not
available in the New Instance Defaults section.)

### Email Notification Settings

You can tell Monitor to send a message to one of more email
addresses when instances of the application terminate unexpectedly.
(Manual or scheduled instance shut downs are not considered unexpected
terminations.) You specify the value of these settings in the Email Notifications
section of the Site page.

### Load Balancing and Adaptor Settings

The following sections explain the properties related to load
balancing and other adaptor settings. In Monitor, you specify the
value of these settings in the HTTP Adaptor Settings section of
the Site page and in the Load Balancing and Adaptor Settings section
of the application configuration page.

#### Connect Timeout

The length of time, in seconds, before the adaptor gives up
connecting to an instance.

#### Connection Pool Size

The maximum number of simultaneous connections the adaptor
should keep open for each configured instance.

#### Dormant

The number of times the adaptor skips an instance of the application
before trying again.

#### Load-Balancing Scheme

The load-balancing method used by the adaptor for instances
of the application. The options provided by WebObjects are Round-Robin,
Random, and Load Average. You can also use a custom load balancer
by choosing the Custom option and entering the load balancer's
name.

#### Receive Buffer Size

The size, in bytes, of the TCP socket receive buffer that's
used for adaptor-to-instance communication.

#### Receive Timeout

The length of time, in seconds, the adaptor waits for a response
from an instance of the application before giving up.

#### Redirection URL

The URL that the user is redirected to when an instance fails
to respond to a direct request.

#### Retries

The number of times a request is retried (trying several instances)
if a communications failure occurs before an error page is returned
to the Web server.

#### Send Buffer Size

The size, in bytes, of the TCP socket send buffer that's
used for adaptor-to-instance communication.

#### Send Timeout

The length of time, in seconds, the adaptor attempts to send
data to an instance of the application before giving up.

#### URL Version

The WebObjects version to use for URL parsing and formatting.
All WebObjects 4, 4.5, and 5 applications use version 4 URLs by
default.

### Scheduling Settings

These properties determine when Monitor restarts application
instances. Restarting instances regularly helps you deploy highly
reliable sites. You set the values of scheduling properties in the
Scheduling section of the application configuration page.

#### Is Scheduled

Determines whether the schedule defined for a particular instance
is active.

#### Graceful Scheduling

Determines whether an instance is shut down gracefully or
immediately at its scheduled shut-down time. During a graceful shutdown,
the instance does not create sessions for new users (they are automatically
directed to other available instances, if any). Existing sessions remain
active until they time out or the user logs out. When the number
of active sessions drops to the value set for the [Minimum Active Sessions](#apple-ijbusrkgjjeeu),
the instance is restarted. When Graceful Scheduling is not selected
for the instance, it is restarted immediately, terminating active
sessions. See ["Minimum Active Sessions"](#apple-ijbusrkgjjeeu) for more information.

#### Types of Schedule

There are three types of schedule available for instances:
hourly, daily, and weekly.

- __Hourly__ The
  instance is restarted after a certain number of hours from a particular
  hour.
- __Daily__ The instance is restarted at
  a particular hour every day.
- __Weekly__ The instance is restarted a
  particular hour on a specific day of the week.

[!](Deployment%20Settings%20Reference.md)[!](Command_Line_Arguments.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
