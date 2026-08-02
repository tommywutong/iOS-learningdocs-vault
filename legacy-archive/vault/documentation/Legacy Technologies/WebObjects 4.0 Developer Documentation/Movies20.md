---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies20.html
archived_at: '2026-07-18T01:22:10.084169Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Refining%20Main.wo.md)

## Specifying a Sort Order

You can change your application to sort movies alphabetically without writing any code. Display groups manage sorting behavior, and WebObjects Builder provides a Display Group Options panel for configuring this and other characteristics of display groups.

- Double-click the __movieDisplayGroup__ variable in the object browser.

The Display Group Options panel opens for configuring __movieDisplayGroup__.

!

- Select the __title__ attribute in the Sorting pop-up list.
- Select Ascending.
- Click OK.

WebObjects Builder stores your settings in an archive that specifies how to create and configure __movieDisplayGroup__ at run time. The archive is stored inside your Main component in a file named __Main.woo__. You can't see the file from Project Builder because you're not meant to edit it directly, but WebObjects Builder's object browser shows you which of your component's variables are initialized from the archive (or __woo__ file) so you don't have to view its contents directly.

!

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies21.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
