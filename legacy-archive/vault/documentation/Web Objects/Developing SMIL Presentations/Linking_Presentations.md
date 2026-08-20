---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/CreatingPresentations/Linking_Presentations.html
archived_at: '2026-07-18T02:20:17.478126Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](Creating_a_1resentation.md) [!](Using_Quick__Extensions.md)

## Linking Presentations

In this section you learn how to link presentations. You'll
modify `Hello.wo` so that
when the user clicks the iPod image, the Hello presentation is replaced
with the Movies presentation.

For the media-object element that displays the iPod image
to behave like a hyperlink, you have to surround it with the WOSMILActiveLink
element.

1. Open `Hello.wo` in
   WebObjects Builder, if it's not already open.
2. Put a WOSMILActiveLink element below the first WOSMILMediaObject
   element.
   1. Enter `"Movies"` for
      the `pageName` binding.
   2. Enter `"replace"` for
      the `show` binding.
3. Select the second WOSMILMediaObject element and choose Edit
   > Cut.
4. Put the cursor inside the WOSMILActiveLink element and choose
   Edit > Paste.

Save `Hello.wo` and
connect to the application's Hello component in QuickTime Player. When
you click the iPod image, the Hello presentation is replaced by
the Movies presentation.

[!](Creating_a_1resentation.md) [!](Using_Quick__Extensions.md)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
