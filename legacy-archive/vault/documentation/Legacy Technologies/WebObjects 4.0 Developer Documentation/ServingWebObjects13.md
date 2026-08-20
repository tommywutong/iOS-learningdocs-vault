---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects13.html
archived_at: '2026-07-18T01:23:36.816729Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects12.md)

## Creating Application Instances

Each application instance you create adopts the defaults provided in the Application Configuration page for the application. To create an instance,

- Click the button labeled "Detail View" in the upper right corner of the Application Configuration page.

The application's Detail View page is then displayed:

!

- Click the Add Instance button to create a new instance of your application.

A new page appears that gives you a choice of hosts to add your instance to.

!

- Select the host from the pop-up menu.

Unless you previously configured hosts in Monitor, there should only be one item in the pop-up menu.

- Click the Add Instance button.

After clicking this button you are returned to the Detail View page, where you can now see a new row in the table showing the status of the instance you just created. From this page you can start the application instance. See "[Starting and Stopping an Application Instance](ServingWebObjects20.md#apple-gyzdmna)" for details.

When you use Monitor to add an application or an instance, or indeed to change any setting, you are creating or updating the public configuration file _NEXT_ROOT___/Library/WebObjects/Configuration/WebObjects.conf__. The presence of this file tells the adaptor to do load balancing across multiple instances. See "[Configuration Files](ServingWebObjects2.md#apple-gq3dama)" for more information on __WebObjects.conf__.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects14.md)
