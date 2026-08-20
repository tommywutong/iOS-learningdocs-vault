---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-39.html
archived_at: '2026-07-15T08:04:57.761299Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Monitoring%20Application%20Activity.md) [!](Logging%20and%20Analyzing%20Application%20Activity.md) [!](Accessing%20the%20Application%20Statistics%20Page.md)

---

# Logging and Analyzing Adaptor Activity

If an adaptor sees that a file named __logWebObjects__
exists in the temporary directory, it will log its activity in __WebObjects.log__
in that same directory. Logging adaptor activity significantly decreases performance. Use this feature only if you suspect something is wrong; do not use it during deployment.

The temporary directory depends on the platform:

- __/tmp__
  on Mac OS X Server, Solaris, and HPUX
- The directory indicated by the TEMP environment variable on Windows NT

You can analyze the information in the log to find out such things as which applications are being requested, which applications are being autostarted, and what the HTTP headers of requests are. You can also use the log to verify if adaptors are properly configured for load balancing.

The following excerpt includes an error message indicating that ThinkMovies wasn't running when a request for it came in:

`Info: <CGI> new request: /cgi-bin/WebObjects/ThinkMovies`
`Info: V4 URL: /cgi-bin/WebObjects/ThinkMovies`
`Error: Request handling error: The requested application was not found on this server`

After ThinkMovies was started, the same request produces the following log file entries:

`Info: <CGI> new request: /cgi-bin/WebObjects/ThinkMovies`

`Info: V4 URL: /cgi-bin/WebObjects/ThinkMovies`

`Info: Selecting new app instance`

`` Debug: Composed URL to `/cgi-bin/WebObjects/ThinkMovies.woa/1' ``

`Info: New request is GET /cgi-bin/WebObjects/ThinkMovies.woa/1 HTTP/1.0`

``

`Info: Trying to contact ThinkMovies:1 on (2001)`

`Info: attempting to connect to myhost.apple.com on port 2001`

`Info: Created new transient connection to myhost.apple.com:2001`

`Info: ThinkMovies:1 on (2001) connected [pooled: No]`

`Info: Request GET /cgi-bin/WebObjects/ThinkMovies.woa/1 HTTP/1.0 sent, awaiting response [1 pending]`

`Info: New response: HTTP/1.0 200 Apple WebObjects`

`Info: received ->200 Apple`

__Creating the Log File__

To cause the log file to be generated, simply create the logWebObjects file in your server's temp directory. The following procedure shows you how to do this:

1. Start a command shell window (on NT use the Bourne Shell in the WebObjects program group).
2. Change to the temporary directory (using the __cd__
   command).
3. Enter the following command to create the __logWebObjects__
   file:
`
touch logWebObjects`
> On UNIX-based systems, you must have root privileges.

Use the __tail__
command to print the current activity in the adaptor to standard output (the shell window):

`
tail -f WebObjects.log`

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Monitoring%20Application%20Activity.md) [!](Logging%20and%20Analyzing%20Application%20Activity.md) [!](Accessing%20the%20Application%20Statistics%20Page.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
