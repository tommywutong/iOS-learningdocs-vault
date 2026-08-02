---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects26.html
archived_at: '2026-07-18T01:23:44.311516Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects25.md)

### Logging and Analyzing Adaptor Activity

If an adaptor sees that a file named __logWebObjects__ exists in the temporary directory, it will log its activity in __WebObjects.log__ in that same directory. Logging adaptor activity significantly decreases performance. Use this feature only if you suspect something is wrong; do not use it during deployment.
The temporary directory depends on the platform:

- __/tmp__ on Mac OS X Server, Solaris, and HPUX
- The directory indicated by the TEMP environment variable on Windows NT

You can analyze the information in the log to find out such things as which applications are being requested, which applications are being autostarted, and what the HTTP headers of requests are. You can also use the log to verify if adaptors are properly configured for load balancing. For example, the following excerpt includes a warning message printed when the adaptor cannot find the __WebObjects.conf__ file in the expected location.

```
    INFO: -- WOServerAdaptor: Load Balancing for Examples/TimeOff
    WARN: -- WOServerAdaptor: "No such file or directory" occurred while
    opening the configuration file C:\NETSCAPE\ns-home\httpd-
80\config/WebObjects.conf
```


The procedure is:

- Start a command shell window (on NT use the Bourne Shell in the WebObjects program group).
- Change to the temporary directory (using the __cd__ command).
- Enter the following command to create the __logWebObjects__ file:

```
touch logWebObjects
```


On UNIX-based systems, you must have root privileges.

- Enter the __tail__ command to print the current activity in the adaptor to standard output (the shell window):

```
tail -f WebObjects.log
```

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects27.md)
