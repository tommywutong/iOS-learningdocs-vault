---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies23.html
archived_at: '2026-07-18T01:22:12.984874Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies22.md)

## Setting a Number Format

In addition to a __dateformat__ attribute, text field elements also have a __numberformat__ attribute.

- Inspect the __revenue__ text field.

The __revenue__ text field's __numberformat__ attribute is bound to the string "###.##". This binding tells the text field that it's displaying a number and describes how to format it.

- Change the text field's __numberformat__ binding value to the string (including the quotes): "$ #,##0.00".

Using this number format, the Movies application formats the number 1750000 as $ 1,750,000. For more information on creating number formats, see the NSNumberFormatter class specification in the _Foundation Framework Reference_.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies24.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
