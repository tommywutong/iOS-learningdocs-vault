---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Introduction/Keeping_Your_Site_Secure.html
archived_at: '2026-07-15T08:12:11.550356Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](The_WebObje_Environment.md)[!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Installation/index.html)

## Keeping Your Site Secure

In a WebObjects deployment, you have several features at your
disposal to enhance the security of your site:

- split-installation
  of applications (application files and Web server resources). By installing
  application-related files in two locations, you can put sensitive
  information (such as business logic) into protected locations. Nonsensitive
  resources (such as image files) can be installed on the Web server's `Document
  Root` directory. For more information, see ["Installing Applications"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iInstalling_Applications.html).
- restricted access to deployment tools. ["Monitor Password"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iSetting_Mon_Preferences.html) explains
  how you can password-protect access to Monitor and wotaskd through
  a single page.
- restricted access to development application instances. If
  your computing environment supports both the development and deployment
  of applications through the same Web server, access of development
  instances is restricted by the HTTP adaptor. See ["Viewing a Host's Configuration"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iSetting_Up_Hosts.html) for details
- restricted access to application instance statistics. Agents
  external to your organization can use the statistics that your application
  instances produce to get privileged information. To avoid this,
  access to the instance statistics page is restricted. See ["Setting a Password for the Instance Statistics Page"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iSetting_Up_Applications.html) for details.

[!](The_WebObje_Environment.md)[!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Installation/index.html)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
