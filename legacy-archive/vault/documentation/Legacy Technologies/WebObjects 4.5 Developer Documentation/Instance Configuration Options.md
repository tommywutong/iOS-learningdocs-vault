---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-34.html
archived_at: '2026-07-15T08:04:54.799083Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Monitor%20Option%20Summary.md) [!](Application%20Configuration%20Options.md) [!](Administrative%20Tasks.md)

---

# Instance Configuration Options

With the options of the Instance Configuration page you can override global application settings for particular instances. To display the Instance Configuration page, go to the Detail View for the application and click the Config button next to the desired instance.

#### Application Start-Up / Command Line Arguments

This section allows you to change the command-line arguments that are used when the instance is started. See [Setting Command-Line Arguments in Monitor](Setting%20Command-Line%20Arguments%20in%20Monitor.md#apple-gqydsmrz) for details.

For convenience, the entire set of command-line arguments passed to the instance are displayed in the blue box at the bottom of this section.

#### Adaptor Settings

This section is where you specify default values for individual instances of an applications. These settings override the corresponding settings made for the application and for the host on which the application instance is running.

__Transport__
: The socket API used to contact an instance. "socket" indicates simple, cross platform, unbuffered sockets. "fsocket" specifies sockets buffered using fopen(), fread(), fwrite() & such (valid on Unix only). "winsock" specifies Win32 socket API (valid on NT only). "nssocket" indicates Netscape's NSAPI socket API (NSAPI only).

__Redirection URL__
: If an error occurs during request processing, return a redirect (302) HTTP response with the specified URL as the location.

__Timeout__
: Default for Send Timeout, Receive Timeout, and Connect Timeout.

__Send timeout__
: Timeout, in seconds, before reporting a failed send() to an instance.

__Receive timeout__
: Timeout, in seconds, before reporting a failed recv() from an instance.

__Connect timeout__
: Timeout, in seconds, before reporting a failed connect() to an instance.

__Connection pool size__
: Number of persistent connections to maintain with an instance.

Click Change Adaptor Settings to cause changes in any of these settings to take affect.

#### Graceful Shutdown

This section allows you to change the minimum active session threshold for an instance. This threshold is used when the instance begins refusing new sessions. The default is zero. If your application is usually under heavy traffic, you might not want to wait for all sessions to time-out before terminating the application.

#### Scheduling

This section allows you to configure the scheduling settings for a given instance. Normally you should use the Application level scheduling to create a staggered schedule of starting and stopping instances. Use the instance-specific section to create your own schedule intervals. See [Automatic Scheduling](Automatic%20Scheduling.md#apple-geytgnzt) for the scheduling procedure.

Monitor computes a series of shutdown dates from the desired instance lifespan or from the desired instance downtime. The scheduling algorithm causes the instance to begin refusing new sessions on regular intervals based on these two variables.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Monitor%20Option%20Summary.md) [!](Application%20Configuration%20Options.md) [!](Administrative%20Tasks.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
