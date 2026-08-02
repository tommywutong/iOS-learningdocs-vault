---
title: WebObjects Application Properties Reference
apple_id: TP30001020
resource_type: Guide
platform: macOS
topic: null
technology: WebObjects
published: '2007-07-11'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/WOAppProperties/Articles/JavaMonitorProperties.html
archived_at: '2026-07-18T02:21:55.894435Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Application Properties Reference](Introduction%20to%20WebObjects%20Application%20Properties%20Reference.md)


[Next](wotaskd%20Properties.md)[Previous](Application%20Properties.md)

# JavaMonitor Properties

This chapter describes the properties you can configure when launching JavaMonitor. Currently there is only one JavaMonitor property.

Usually you set these properties on the command line using Java-style command-line arguments with the following format:

```
<appName> -D<optionName>=<value> -D<optionName>=<value> ...
```

Read _[WebObjects Deployment Guide Using JavaMonitor](../WebObjects%20Deployment%20Guide%20Using%20JavaMonitor/Introduction%20to%20WebObjects%20Deployment%20Guide%20Using%20JavaMonitor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambz)_ for examples on when to use these properties.

__Table 1__  JavaMonitor properties

| Property | Type | Description |
| `WODeploymentConfigurationDirectory` | string | Location of the site configuration file.  Each wotaskd process writes its configuration to a file called `SiteConfig.xml` in the directory specified by this property. (The HTTP adaptor configuration file is also located in this directory.) This property, in conjunction the `WOLifebeatDestinationPort` property, allows you to run multiple wotaskd processes on a single computer.  The default value is `/Library/WebObjects/Configuration`. |

[Next](wotaskd%20Properties.md)[Previous](Application%20Properties.md)

