---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects22.html
archived_at: '2026-07-18T01:23:39.557968Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects21.md)

### Setting Command-Line Arguments in Monitor

When you use Monitor to start an instance of an application, it uses a set of arguments to initialize that instance. Most of these arguments are the command-line arguments described in "[Starting Up Applications From the Command Line](ServingWebObjects21.md#apple-gq4timi)". You can change an applications arguments, even for all instances that are currently configured and running, by doing the following:

- Display the Application Configuration page for an application. You can get to this form using one of two approaches:

- Existing applications: Click the Config button next to an instance in the Applications page (which you can get by clicking Applications in the Monitor banner).
- New applications: In the Applications page, enter the name of an application in the Add Application field and click the Add Application button.

- Click the arrow next to the New Instance Default Arguments option of the Application Configuration page. (This step is not necessary if you are configuring a new application.)

The following form is exposed:

!

- Specify the command-line options you want your application's instances to have. For the most common options, simply specify the value (not the key). These options are:

  |  Field |  Option |
  |  Auto Recover |  Internal flag. Specifies whether Monitor should try to restart the instance if the instance fails. |
  |  Minimum Active Sessions |  Internal flag. Specifies the minimum number of active sessions allowed. |
  |  Caching enabled |  Command-line option -WOCachingEnabled |
  |  Adaptor |  Command-line option -WOAdaptor |
  |  Adaptor threads |  Command-line option -WOWorkerThreadCount |
  |  Listen Queue Size |  Command-line option -WOListenQueueSize |

```
```


For command-line arguments not included in the above table, enter them as "-_key_ _value_" pairs, separated by spaces, in the Additional Command-line Arguments field.

- If you want the new settings "pushed" to existing instances, click the checkbox in the gray area next to each option, then click the Update for New and Existing Instances button. The existing instances will have to be restarted for new options to take effect.

You can also set the command-arguments for specific instances. To navigate to the form for doing this, go to the Detail View page for an application and click the Config button next to an instance. A list of instance-specific options is displayed; from the list choose "Application Start-Up/Command-line arguments." The following form is exposed:

!

Enter the new arguments and click Save Changes in App Starting. Unlike the previous form, this one allows you to specify a specific port, but it doesn't allow you to set Monitor-specific options (such as auto-recover). Moreover, the changes that you make here do not take effect until the instance is restarted.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects23.md)
