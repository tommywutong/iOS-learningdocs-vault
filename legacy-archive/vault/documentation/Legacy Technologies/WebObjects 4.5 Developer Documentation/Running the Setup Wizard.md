---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.27.html
archived_at: '2026-07-15T08:09:32.393863Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Setting%20Up%20the%20Sample%20Databases.md) [!](Setting%20Up%20the%20Sample%20Databases.md) [!](Troubleshooting.md)

---

#  Running the Setup Wizard

SetupWizard.app is located in
/System/Developer/Examples/EnterpriseObjects
(on Windows NT systems, _NEXT_ROOT_

\Developer\Examples\EnterpriseObjects
). After you invoke the wizard, you'll be prompted for a directory into which the examples should be installed. _This directory must already exist in order for the wizard to work properly_
.

> __Warning:__
> The wizard will delete any existing contents of the directory you specify.

After advancing to the next screen, follow the prompts through the rest of the wizard. Note that you'll need to select a database adaptor and login to the database twice: once for Movies, and once for Rentals. Finally, the wizard will ask you whether or not you want it to populate the selected databases for you.

The Setup Wizard doesn't set up the inheritance databases; for this, you'll need to perform the steps listed in
ReadMe-Inheritance.html
, which is located in the same directory in which the Setup Wizard is located (
.../Examples/EnterpriseObjects
).

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Setting%20Up%20the%20Sample%20Databases.md) [!](Setting%20Up%20the%20Sample%20Databases.md) [!](Troubleshooting.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
