---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/Command_Line_Arguments.html
archived_at: '2026-07-15T08:12:15.466882Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Application__Properties.md)[!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/SpecialDeploymentIssues/index.html)

## Command-Line Arguments

The following sections describe the command-line options available
to fine-tune your deployment. You specify command-line options using
the following format:

```
<appName> -<optionName> <value> -<optionName> <value> ...
```

There are three types of command-line options: general, wotaskd
and Monitor specific, and wotaskd specific.

### General Command-Line Arguments

The sections below describe the command-line options that
apply to Monitor processes, wotaskd processes, and application instances.

#### WOApplicationName

- __Value
  format__ _string_.
- __Default value__ Name of executable file.
- __Description__ This setting is used by
  the adaptor to implement load balancing. The adaptor can load-balance
  only between instances with the same application name. This setting
  can be used to create groups of instances, even when the instances
  share the same executable file. This argument is set automatically
  for instances started by wotaskd.

#### WOHost

- __Value
  format__ _string_.
- __Default value__ None.
- __Description__ Specifies the network interface
  that an instance binds to. This argument should only be used on
  hosts with multiple network interfaces (IP addresses).

#### WOLifebeatDestinationPort

- __Value
  format__ _number_.
- __Default value__ `1085`.
- __Description__ Determines the port that
  instances send lifebeats to (should be the port that the wotaskd
  process that overlooks the instance runs on). The value of this
  property on an application instance must be the same as the value
  of the property for the Monitor process used to manage the instance.
  The wotaskd process sets this argument to the value of its `WOPort` for
  instances that it starts.
- __See__ ["WOPort"](#apple-ijbusskfivfei).

#### WOLifebeatEnabled

- __Value
  format__ {`true`, `false`}.
- __Default value__ `true`.
- __Description__ Determines whether the
  instance sends lifebeats.

#### WOLifebeatInterval

- __Value
  format__ _number_.
- __Default value__ `30`.
- __Description__ Determines the interval,
  in seconds, between lifebeats.

#### WONoPause

- __Value
  format__ {`true`, `false`}.
- __Default value__ `false`.
- __Description__ In Windows 2000 launch
  scripts, if an error occurs during script execution, the process
  idles because the message "Press any key..." is displayed on
  the console and the system awaits a keypress. To avoid this behavior,
  set this property to `true`.

#### WOOutputPath

- __Value
  format__ _path_.
- __Default value__ /dev/null.
- __Description__ Allows you to redirect
  the instance's standard output and standard error streams to the
  directory specified. The file generated is named as follows:

  ```
  <application name>-<instance ID>
  ```

#### WOPort

- __Value
  format__ _integer_.
- __Default value__ `1085`.
- __Description__ The port that the instance
  runs on.
- __See__ ["WOLifebeatDestinationPort"](#apple-ijbusrsfjbdek).

#### WORecordingPath

- __Value
  format__ _path_.
- __Default value__ None.
- __Description__ Specifies the path for
  the file that stores each request and response made in a session.

#### WOSessionTimeOut

- __Value
  format__ _number_.
- __Default value__ `3600`.
- __Description__ Specifies the time, in
  seconds, that passes after the last request is processed before
  the session times out.

#### WOStatisticsPassword

- __Value
  format__ _text_.
- __Default value__ None.
- __Description__ Specifies the password
  that must be entered to gain access to the instance statistics (WOStats)
  page of an application instance.

### Monitor and wotaskd Command-Line Arguments

There's one command-line option that applies to both Monitor
and wotaskd processes but not to application instances.

#### WODeploymentConfigurationDirectory

- __Value
  format__ _path_.
- __Default value__ /Library/WebObjects/Configuration.
- __Description__ Each wotaskd process writes
  its configuration to a file called `SiteConfig.xml` in
  the directory specified here. (The HTTP adaptor configuration file
  is also written to this directory.) This argument, in conjunction
  with `WOLifebeatDestinationPort`,
  allows you to run multiple wotaskd processes on a single machine.
- __See__ ["WOLifebeatDestinationPort"](#apple-ijbusrsfjbdek).

### wotaskd Command-Line Arguments

These are command-line arguments that apply only to wotaskd
processes.

#### WOAssumeApplicationIsDeadMultiplier

- __Value
  format__ _integer_.
- __Default value__ `4`.
- __Description__ Used to determine the number
  of seconds that the wotaskd process waits without receiving a status
  message from an instance before considering it dead. It species a
  multiplier against `WOLifebeatInterval`.
  If `WOLifebeatInterval` is `30`,
  a wotaskd process waits 120 seconds from the last status message
  before determining that an instance is dead.

#### WOMulticastAddress

- __Value
  format__ _ip-address_.
- __Default value__ `239.128.14.2`.
- __Description__ Sets the IP address that
  the wotaskd process listens to for multicast requests from the HTTP
  adaptor.

#### WORespondsToMulticastQuery

- __Value
  format__ {`true`, `false`}.
- __Default value__ `false`.
- __Description__ Determines whether the
  wotaskd process responds to multicast queries from the HTTP adaptor.

#### WOSavesAdaptorConfiguration

- __Value
  format__ {`true`, `false`}.
- __Default value__ `false`.
- __Description__ Determines whether the
  wotaskd process generates an HTTP adaptor configuration file.

[!](Application__Properties.md)[!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/SpecialDeploymentIssues/index.html)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
