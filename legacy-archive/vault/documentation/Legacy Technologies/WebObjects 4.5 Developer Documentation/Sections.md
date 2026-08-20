---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-14.html
archived_at: '2026-07-15T08:04:39.756884Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Web%20Server%20Adaptor%20Configuration%20File%20Format.md) [!](XML%20Format%20in%20Full.md) [!](Attributes-2.md)

---

# Sections

The configuration file is divided into three sections, as follows:

<adaptor>

> In this optional section, specify global default values for applications and instances. Attribute values defined here apply to global adaptor behavior and apply to all applications.

> The "error" attribute is used to redirect requests for which no application can be found.

<application>

> Required attribute: "name".

> Attribute values defined here specify load balancing behavior and default values for instances of this application.

<instance>

> Required attributes: id, port, host

> Attribute values defined here specify communication options for this instance and override anything specified at the application.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Web%20Server%20Adaptor%20Configuration%20File%20Format.md) [!](XML%20Format%20in%20Full.md) [!](Attributes-2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
