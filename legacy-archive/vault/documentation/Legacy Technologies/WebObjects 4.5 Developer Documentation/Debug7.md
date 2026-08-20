---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Debug7.html
archived_at: '2026-07-15T08:05:15.290471Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Previous Section](Debug6.md)

## Debugging Without a Web Server

WebObjects applications are meant to be used in conjunction with a web server. When you are in development mode, however, you do not have to use a web server to interact with the application. Instead, you simply specify the number of the port where the application should receive requests using the WOPort user default. By default, WOPort is -1, which assigns an arbitrary high port number to the application. Thus, if you specify no port number at all, you can still run your application without a web server. However, it is probably a good idea to assign a specific port number to your application. To do so, use the following command in a command shell window:

```
% defaults write MyWebApp WOPort portNumber
```


When a port number is assigned to an application, you can access it by typing the following URL in the browser (provided the application is already running):

```
http://localhost:portNumber
```

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Next Section](Debug8.md)
