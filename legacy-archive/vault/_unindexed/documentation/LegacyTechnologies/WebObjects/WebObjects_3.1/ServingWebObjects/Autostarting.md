---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/ServingWebObjects/Autostarting.html
archived_at: '2026-07-15T07:49:54.230662Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Previous Section](ISAPIConfig.md)

# Autostarting Applications

When applications are autostarted on Windows NT they are, by default, launched under the "LocalSystem" account on Netscape's servers or under "IUSR_machinename" on Internet Information Servers. Both of these accounts take privileges that might prevent you from terminating the autostarted processes. To avoid this problem, you should set these autostart accounts to be the same as yours (or other account with "user" privileges). The procedure for doing this differs between Netscape servers and Internet Information Servers.

## Netscape Servers on Windows NT

1. Log in as a user with "user" privileges.
2. Open the Services control panel.
3. Select the Netscape server (something like "Netscape Httpd-80" or "Netscape Https-foo").
4. Click Startup.
5. In the Services dialog box:
   - Select the Automatic Startup option.
   - Under Log On As, select This Account.
   - Enter your account name and your password; confirm your password
   - Click OK.
6. Restart the server.
7. Repeat steps 3 through 5 for the Netscape Administration server.

## __Internet Information Servers__

Using the Internet Service Manager, access the properties sheet for the WWW service. Set the Anonymous Login to a new user account. Type the password carefully as validation is not done at this point. Finally, stop and start the server to make this change take effect.

## __UNIX-Based Platforms__

To avoid problems with application processes, you should ensure that each process runs as user "nobody". Check your server's configuration documentation for the steps required to specify the user account of application processes.

[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Next Section](SecuringSource.md)
