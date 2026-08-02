---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/ServingWebObjects/Logging.html
archived_at: '2026-07-15T07:49:59.143062Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Previous Section](ManagingProcesses.md)

# Logging and Analyzing Adaptor Activity

If an adaptor sees that a file named __logWebObjects__ exists in the _temporary_ _directory_, it will log its activity in __WebObjects.log__ in that same directory. The temporary directory depends on the platform:

- __/tmp__ on Mach, Solaris, and HPUX
- The directory indicated by the TEMP environment variable on Windows NT

You can analyze the information in the log to find out such things as which applications are being requested, which applications are being autostarted, and what the HTTP headers of requests are. You can also use the log to verify if adaptors are properly configured for load balancing. For example, the following excerpt includes a warning message printed when the adaptor cannot find the __WebObjects.conf__ file in the expected location.

```
  INFO: -- WOServerAdaptor: Load Balancing for Examples/TimeOff
  WARN: -- WOServerAdaptor: "No such file or directory" occured while
  opening the configuration file C:\NETSCAPE\ns-home\httpd-80\config/WebObjects.conf
```

The procedure is:

1. Start a shell program (on NT use the Bourne Shell in the WebObjects program group).
2. Change to the temporary directory (using the __cd__ command).
3. Enter the following command to create the __logWebObjects__ file:

   ```
       touch logWebObjects
   ```
4. Then enter the __tail__ command to print the current activity in the adaptor to standard output (the shell window):

   ```
       tail -f WebObjects.log
   ```

[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Next Section](LoadBalancing.md)
