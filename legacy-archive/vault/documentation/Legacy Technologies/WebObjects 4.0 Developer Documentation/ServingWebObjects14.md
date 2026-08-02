---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects14.html
archived_at: '2026-07-18T01:23:38.264586Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects13.md)

## Monitor Option Reference

Many of Monitor's options are listed on pages with triangles to the left of them. Clicking the triangle causes a section (a form with fields, buttons, and so on) to be displayed.

### Global Configuration

The Global Configuration page allows you to configure aspects of Monitor and your site that are not specific to an application. It lists the options described below.
__To Access__: Click the Configure button in the Monitor banner.

##### Monitor Password

In this section specify a password that is required to access Monitor. Monitor does not have a password set by default. After you set a password Monitor prompts users for it each time they access the application.

##### HTTP Server and WebObjects Adaptor

You use this section primarily to specify the URL that points to the adaptor on your deployment's web server. Monitor uses this URL to construct more URLs that direct the administrator to running instances, the WOStats page, and other destinations.
Also configurable is the paths to which Monitor writes new versions of the __WebObjects.conf__ file used by the adaptor for load balancing. You can specify multiple locations for Monitor to write this file in case you have a customized adaptor or if your web server is on a different machine and you need to have the file written to a network-mounted drive.

##### Auto-Recover Settings

This configuration option allows you to have an additional level of recovery outside the per-instance Auto-Recover feature. This feature restarts application instances after they fail. When Monitor is notified that an instance has crashed, it checks the instance's auto-recover setting to see if it should start a new instance. With the global auto-recover option, when Monitor is started (perhaps when a machine is booted) it can locate all instances configured to be auto-recovered and start them if they are not running. This allows you to have a machine that has failed to boot up, start Monitor, and then have Monitor start all the appropriate applications.
When this setting is on, Monitor perform this check on regular intervals. If Monitor fails or you change an instance's Auto-Recover setting, Monitor launches the appropriate instances within 45 seconds.

##### E-Mail Notification

In this section you specify an SMTP server that Monitor uses to send e-mail to a set of addresses when application instances fail unexpectedly. In order for Monitor to send e-mail it requires the name or IP Address of an SMTP server.

##### Statistics Gathering

Periodically Monitor gathers statistical information from each running instance of an application and uses it to refresh the Detail View. If you have many instances of an application, collecting this information on every refresh of the Detail View can be too time consuming. This section allows you to set how long Monitor waits before refetching the statistical information from each instance. The more instances you have the higher this number should probably be. The fewer instances you have the lower this number can be.

##### Detail View

In this section you can set the interval at which the Detail View page is automatically refreshed.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects15.md)
