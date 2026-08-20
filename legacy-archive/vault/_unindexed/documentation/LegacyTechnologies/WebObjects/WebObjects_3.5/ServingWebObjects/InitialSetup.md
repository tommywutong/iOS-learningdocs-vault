---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/InitialSetup.html
archived_at: '2026-07-15T07:55:54.995562Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.md) [!Previous Section](StartMonitor.md)

## Initial Monitor Setup

In normal operation, when you start up Monitor, all of the WebObjects applications on your site are displayed under the Declared Apps heading, and the right frame shows information about the application you select. (Or if you set it up properly, you'll see a login panel and after you log in you'll see all of your WebObjects applications.) However, the first time you've started the Monitor, no applications are displayed. You need to configure the Monitor for use on your site.!
To configure the Monitor application, do the following:

- Click the Options button.

The right frame shows configuration information.

- Look at the first section of the Configuration options. They should look like this:
!

Make sure each option has the appropriate setting as described below:

**Local host name**
: The name of the server Monitor is running on.

**Admin user name**
: Protects the Monitor from being used by all users except the one specified here. If you enter a user name in this field and that user's password in the "Admin password" and "Admin password again" fields, Monitor runs in a protected mode. When you restart Monitor, it displays a login page instead of the typical first page.

**Admin password**
: If you entered an administrator name, enter the administrator account's password here.

**Admin password again**
: Repeat the administrator password here.

The second set of options affects the configuration file. Make sure each option has the appropriate setting as described below:

!

**Primary WebObjects.conf path**
: The location of the public configuration file. Most of the time, this should be set to _NeXT_ROOT___/NextLibrary/WOAdaptors/Configuration__. (You only need to change this if you move the configuration file.)

**Additional public paths**
: If you have more than one server and each server has its own public configuration file, click the Add Path button and specify the location of the other configuration file(s). Servers can share the configuration file in _NeXT_ROOT___/NextLibrary/WOAdaptors/Configuration__, so usually this setting is not necessary.

**Dedicated Monitor WebObjects.conf path**
: The location of a configuration file used only by Monitor. This file is used only if you want to start multiple instances of Monitor, which is rare. See "[Starting Up Multiple Monitor Instances](MultipleMonitors.md#apple-guzdeni)."

The third set of options displays default setting for each application that you'll add to the Monitor. Make sure each option has the appropriate setting as described below:

!

**WebObjects executable name**
: The executable that you want to use as the default executable for all applications you add to Monitor. By default, this is set to __WODefaultApp__ or __WODefaultApp.exe__.

**Path to executable**
: The path to the executable name you specified in the field above.

**Application cycling**
: Default settings for the periodic shutdown of applications. For more information, see "[Periodically Shutting Down the Application](AppShutdown.md#apple-guytana)" in this guide.

The fourth set of options you rarely have to change. They are used to build the WebObjects application URLs that you use when you click an application's hyperlink to access one of its running instances.

!

**HTTP server host**
: The host name of your HTTP server.

**Adaptor key**
: The name of your WebObjects adaptor. Usually, this is __WebObjects__ or __WebObjects.exe__. If you use the NSAPI adaptor or ISAPI adaptor, you may have to change the name here.

**Protocol name**
: Should normally be set to __http__.

- Click the Save Changes button at the bottom of the page to record your changes.
- In the Main Menu area, click the Add button.
!

The right frame displays the Add Application Panel, which looks like this:

!- For each application that you want to administer using Monitor, do the following:

- Type the application's name in the Application Name field. The application name is the path to the application relative to _<DocRoot>___/WebObjects__.
- Type the path to the application executable in the Application Path field (for example __C:\Next\NextLibrary\WOApps\MyApp.woa__)
- Type the host name of the machine where the application is located in the Host name field.
- Click the Add to Declared Apps button.

Monitor updates the port number and instance number fields for you.

When you use the Add Application panel, you are creating the public configuration file _NeXT_ROOT___/NextLibrary/WOAdaptors/Configuration/WebObjects.conf__. This has a few implications that might not be immediately apparent:

- Autostarting is disabled.

Recall that when the public configuration file exists, autostarting is disabled. You can still start applications manually from the command line, but applications won't autostart when you type a URL in the browser.

- You won't get an application listing if you enter `http://localhost/cgi-bin/WebObjects/` or if you make a typo in an application URL.

This feature depends on autostarting, so it is disabled when autostarting is disabled.

- If you start an application from the command line, you must use the __-n__ option to specify an instance number.

Monitor associates an instance number with all applications that you declare in it, instead of just applications that perform load balancing among multiple instances. If you manually start an application and you want it to connect to the Monitor, you must specify the instance number that Monitor set up for you. For more information, see "[Starting Up Applications From the Command Line](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/ManualStarting.html#4941)" in this guide.

[!Table of Contents](ServingWebObjectsTOC.md) [!Next Section](AdminTasks.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
