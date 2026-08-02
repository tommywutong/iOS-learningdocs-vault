---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-28.html
archived_at: '2026-07-15T08:04:50.817596Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Starting%20and%20Stopping%20an%20Application%20Instance.md) [!](Starting%20and%20Stopping%20an%20Application%20Instance.md) [!](Deploying-29.md)

---

# Setting Command-Line Arguments in Monitor

When you use Monitor to start an instance of an application, it uses a set of arguments to initialize that instance. Most of these arguments are the command-line arguments described in [Starting Up Applications From the Command Line](Deploying-29.md#apple-ge3tkmjv). You can change an applications arguments, even for all instances that are currently configured and running, by doing one of the following:

- __New application__
  : Display the Applications page by clicking the Applications button in the Monitor banner, enter the name of the application in the Add Application field, and then click the Add Application button.
- __Existing application__
  : Display the Application Configuration page for the application by clicking the Config button next to the application in the Application's page (which you can get to by clicking the Applications button in the Monitor banner). Click the arrow next to the New Instance Default Arguments option of the Application Configuration page.

The following form is displayed:

!

1. Specify the command-line options you want your application's instances to have. The most common options, which can be changed by simply clicking checkboxes or entering values in fields, are:

| Field | Option |
| --- | --- |
| Name | The name of the application, which is the WebObjects wrapper name minus the ".woa" extension. |
| Path | The full path to the WebObjects application's executable (including the ".exe" extension on Windows NT). |
| Auto Recover | Specifies whether Monitor should try to restart the instance if the instance fails. |
| Minimum Active Sessions | Specifies the minimum number of active sessions allowed. |
| Caching enabled | Command-line option -WOCachingEnabled. Requests that the application cache component definitions (templates) instead of reparsing HTML and declaration files upon each new HTTP request. |
| Adaptor | Command-line option -WOAdaptor. The WOAdaptor class name. |
| Adaptor threads | Command-line option -WOWorkerThreadCount. The maximum number of worker threads for a multithreaded application. Setting this count to 0 results in single-threaded request dispatch. |
| Listen Queue Size | Command-line option -WOListenQueueSize. The depth of the listen queue If the application is expected to experience "spikes" in its processing load, consider increasing the listen queue depth (althou increasing this setting does not necessarily improve performance or allow the application to server more requests at sustained high loads). |
| Debugging Enabled | Command-line option -WODebuggingEnabled. Controls whether the application prints debugging messages to standard error duing startup. |

> For command-line arguments not included in the above table, enter them as "-_key_
> _value_
> " pairs, separated by spaces, in the Additional Command-line Arguments field. See [Starting Up Applications From the Command Line](Deploying-29.md#apple-ge3tkmjv) for a complete list of command-line arguments.

2. If you want the new settings "pushed" to existing instances, click the checkbox in the gray area next to each option you want pushed, then click the Update for New and Existing Instances button. The existing instances will have to be restarted for new options to take effect. To make the changes effective for new instances only, click the Update for New Instances button instead.

#### Setting Command-Line Arguments for a Specific Instance

The above procedure affects all new or existing instances of a WebObjects application. Monitor also allows you to set the command-arguments for specific instances. To navigate to the form for doing this, go to the Detail View page for an application and click the Config button next to an instance. A list of instance-specific options is displayed; from the list choose "Application Start-Up/Command-line arguments." The following form is exposed:

!

Enter the new arguments and click Save Changes in App Starting. Unlike the previous form, this one allows you to specify a specific port, but it doesn't allow you to set Monitor-specific options (such as auto-recover). Moreover, the changes that you make here do not take effect until the instance is restarted.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Starting%20and%20Stopping%20an%20Application%20Instance.md) [!](Starting%20and%20Stopping%20an%20Application%20Instance.md) [!](Deploying-29.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
