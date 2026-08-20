---
title: WebObjects Application Properties Reference
apple_id: TP30001020
resource_type: Guide
platform: macOS
topic: null
technology: WebObjects
published: '2007-07-11'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/WOAppProperties/Articles/WotaskdProperties.html
archived_at: '2026-07-18T02:21:55.927555Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Application Properties Reference](Introduction%20to%20WebObjects%20Application%20Properties%20Reference.md)


[Next](Document%20Revision%20History.md)[Previous](JavaMonitor%20Properties.md)

# wotaskd Properties

This chapter describes the properties you can configure when launching wotaskd.

The wotaskd properties are described in Table 1. Note that the `WODeploymentConfigurationDirectory` property is also used by the JavaMonitor tool. The other properties listed in Table 1 are unique to wotaskd.

Usually you set these properties on the command line using Java-style command-line arguments with the following format:

```
<appName> -D<optionName>=<value> -D<optionName>=<value> ...
```

Read _[WebObjects Deployment Guide Using JavaMonitor](../WebObjects%20Deployment%20Guide%20Using%20JavaMonitor/Introduction%20to%20WebObjects%20Deployment%20Guide%20Using%20JavaMonitor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambz)_ for examples on when to use these properties.

__Table 1__  wotaskd Properties

| Property | Type | Description |
| `WODeploymentConfigurationDirectory` | string | Location of the site configuration file.  Each wotaskd process writes its configuration to a file called `SiteConfig.xml` in the directory specified by this property. (The HTTP adaptor configuration file is also located in this directory.) This property, in conjunction the `WOLifebeatDestinationPort` property, allows you to run multiple wotaskd processes on a single computer.  The default value is `/Library/WebObjects/Configuration`. |
| `WOAssumeApplicationIsDeadMultiplier` | integer | A multiplier used to calculate the number of seconds that the wotaskd process waits without receiving a status message from an instance before considering it dead.  This property is multiplied by the `WOLifebeatInterval` property to calculate the total number of seconds wotaskd waits. For example, if `WOLifebeatInterval` is `30`, a wotaskd process waits 120 seconds from the last status message before concluding that an instance is dead.  The default value is `4`. |
| `WOMulticastAddress` | string | The IP address that the wotaskd process listens to for multicast requests from the HTTP adaptor.  The default value is `239.128.14.2`. |
| `WORespondsToMulticastQuery` | Boolean | A Boolean value of `true` or `false` that determines whether the wotaskd process responds to multicast queries from the HTTP adaptor.  The default value is `false`. |
| `WOSavesAdaptorConfiguration` | Boolean | A Boolean value of `true` or `false` that determines whether the wotaskd process generates an HTTP adaptor configuration file.  The default value is `false`. |

[Next](Document%20Revision%20History.md)[Previous](JavaMonitor%20Properties.md)

