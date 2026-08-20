---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Installation/Choosing_What_to_Install.html
archived_at: '2026-07-15T08:12:11.024259Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Installing%20the%20Software.md)[!](Environment_X_Platforms.md)

## Choosing What to Install

When you perform a complete installation of WebObjects Deployment
on a computer, two types of files are copied to its hard disk: adaptor
files and deployment files.

### Adaptor Files

These are the files that allow your Web server to communicate
with WebObjects application instances. The executable files for
the adaptors are placed in the `/System/Library/WebObjects/Adaptors` directory.

The source files for the adaptors are placed in the /Developer/Examples/WebObjects/Source/Adaptors directory.
Also included are HTML files containing instructions for building
and installing each adaptor. The code of the adaptors is open source,
so you can install them anywhere.

### Deployment Files

These files are divided into two groups:

- __Runtime
  environment__ The runtime environment of WebObjects is
  implemented in __framework__ (`.framework`)
  files, whose purpose is similar to dynamically linked library (DLL)
  files in Windows. Framework files are installed in the /System/Library/Frameworks directory.
  These frameworks are used by any WebObjects application, including
  the deployment tools of WebObjects
- __Deployment tools__ WebObjects Deployment
  includes two deployment tools you use to configure and monitor your
  site. The files that make up these tools are placed in the /System/Library/WebObjects/JavaApplications directory. [Table 3-1](#apple-ijbusskiijbei) shows
  the purpose of each tool. For more information on the deployment
  tools, see ["Managing Application Instances"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/DeploymentElements/iManaging_Ap_n_Instances.html)

__Table
3-1 The WebObjects deployment and administration
tools__

__|  |  |  |
| --- | --- | --- |
| Filename | Application name | Purpose |__| `JavaMonitor.woa` | Monitor | Site configuration and administration |
| `wotaskd.woa` | wotaskd | Instance management |

|  |
| --- |
| __Note:__ Installing WebObjects Deployment on a computer requires a WebObjects Deployment license. Please read the license agreement before installing this package. |

### Types of WebObjects Deployment Installations

Depending on the purpose of the computer you're installing
the software on, there are three types of WebObjects Deployment
installations you can perform:

- __Web
  server only__ On a computer that you want to use as the
  Web server computer but on which you do not intend to run application
  instances (including the deployment tools), you need to install
  only the HTTP adaptor files.
- __Application host only__ On computers
  that you intend to use only as application hosts, you need to install
  only the deployment tools. (If you do not plan to run Monitor on that
  machine, you can delete its files.)
- __Web server and application host__ When
  one computer can satisfy all your deployment needs or when you want
  a Web server machine to also run application instances, you need
  to install the adaptor files and the deployment tools.

|  |
| --- |
| __Note:__ On Windows 2000 machines it's not possible to perform tailored WebObjects Deployment installations. |

[!](Installing%20the%20Software.md)[!](Environment_X_Platforms.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
