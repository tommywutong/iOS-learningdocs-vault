---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToJavaClient/Tutorial/Configuring_Windows.html
archived_at: '2026-07-15T08:12:21.015093Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](Typical_Workflow.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](Other_Assistant_Settings.md)

## Configuring Windows

After configuring properties and widgets, the bulk of your
Assistant customizations are done. The final change you make to
your application in this tutorial is to change the title of a window.
To do this, you use the Windows tab of the Assistant.

The Windows tab allows you to do things such as

- setting the
  title of windows
- changing the default position and size of a window
- determining whether to save window position and size in user
  defaults
- specifying disposal and reuse behavior to tune performance

### Changing the Title of the Query Window

To change the title of the Query Window to "Find", perform
the following steps.

1. Click the
   Windows tab in the Assistant.
2. Click the Query Window.

   This focuses the Assistant on
   the Query Window, setting the Question to window, setting Task to `queryWindow`,
   and disabling Entity (because the Query Window displays multiple
   entities).
3. In the Label field, type `Find`.
4. Save your changes and restart the application.

   The Query
   Window's title is now "Find".

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](Typical_Workflow.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](Other_Assistant_Settings.md)

© 2001 Apple Computer, Inc.
