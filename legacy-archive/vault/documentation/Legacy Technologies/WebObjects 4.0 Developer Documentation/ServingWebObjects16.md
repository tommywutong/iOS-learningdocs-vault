---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects16.html
archived_at: '2026-07-18T01:23:38.436148Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects15.md)

### Application Configuration Options

The Application Configuration page allows you to configure general aspects of an application. It lists the options described below.
__To Access__: Click the Applications button on the Monitor banner, then click the Config button next to any instance.

##### New Instance Default Arguments

In this section you can specify a set of default arguments that Monitor uses when it creates new instances of the application. Most of these arguments are the normal command-line options used to configure an instance of a WebObjects application (see "[Starting Up Applications From the Command Line](ServingWebObjects21.md#apple-gq4timi)" for descriptions of these options). Two options, Auto Recover and Minimum Active Sessions, are not command-line options but are deployment settings that Monitor uses for determining starting and stopping policy.

The "[Setting Command-Line Arguments in Monitor](ServingWebObjects22.md#apple-gy3tmoa)" of this document discusses how to set launch options using Monitor.

These settings all appear in the Instance Configuration page as well.

##### Scheduling Instances

This section enables the administrator to configure an application's pool of instances to conform to a staggered schedule of starting, running for a period of time, begin refusing new sessions, and shutting down when the minimum active session threshold is reached.
See "[Automatic Scheduling](ServingWebObjects30.md#apple-guytana)" for instructions on setting the shutdown and startup schedules for all instances of an application as well as specific instances.

##### E-Mail Notifications

If the SMTP server has been set in Monitor's Global Configuration page (see "[Global Configuration](ServingWebObjects14.md#apple-g44dcni)" ) then an application can specify a list of electronic-mail addresses to send an mail to when an instance fails unexpectedly. This list should be comma delimited (for example, "jdoe@somewhere.com, mpublic@else.com, foo@bar.com").

The mail message contains the application name, host, port, and date and time of the failure.
To turn off the feature, delete all addresses from the text field and click Update.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects17.md)
