---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/Setting_Mon_Preferences.html
archived_at: '2026-07-15T08:12:00.442673Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Configuring_Sites.md)[!](Load_Balancing.md)

## Setting Monitor Preferences

When you click the Preferences tab in Monitor, the page in [Figure 6-18](#apple-ijbusrkii5dec) is
displayed. It contains two sections: Monitor Password and Detail
View Refresh Settings.

__Figure
6-18 The Preferences page of Monitor__

![[image: ../Art/preferences.gif]](../Art/preferences.gif)

### Monitor Password

You can restrict access to Monitor by requiring its users
to enter a password before they can use it. When a site is protected
this way, the site's wotaskd processes are also protected; that
is, you cannot directly obtain a wotaskd process's information
by connecting to its port, as described in ["Confirming That wotaskd Is Active"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Installation/iConfirming__d_Is_Active.html).

[Figure 6-19](#apple-krifqusfiyytkna) shows the login page that Monitor displays after
you password-protect your site.

__Figure
6-19 Login page displayed by Monitor on
a password-protected site__

![[image: ../Art/monitorlogin.gif]](../Art/monitorlogin.gif)

When you try to view the configuration of an application host
on a site that you've password-protected by connecting to the
appropriate wotaskd process's port, you'll see a page similar
to the one shown in [Figure 6-20](#apple-ijbegscfjjbei) (the page's content varies according to your deployment
platform).

__Figure
6-20 Page returned by wotaskd when the
site is password-protected__

![[image: ../Art/wotaskdprotected.gif]](../Art/wotaskdprotected.gif)

On password-protected sites, you'll have to use Monitor
to view an application host's configuration.

### Detail View Refresh Settings

This section allows you to tell Monitor if you want it to
refresh the application detail page and how often to do it.

[!](Configuring_Sites.md)[!](Load_Balancing.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
