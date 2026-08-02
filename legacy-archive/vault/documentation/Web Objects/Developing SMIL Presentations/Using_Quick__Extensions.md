---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/CreatingPresentations/Using_Quick__Extensions.html
archived_at: '2026-07-18T02:20:17.536097Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](Linking_Presentations.md) [!](https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/Reference/index.html)

## Using QuickTime SMIL Extensions

QuickTime takes advantage of SMIL's extensibility by adding
tags that you can use to enhance a presentation. To make use of
QuickTime extensions in your presentations, you have to add the
special binding `otherTagString` in
the WOSMILDocument element. Then you must bind it to an instance
variable that provides the appropriate string.

1. Select the
   WOSMILDocument element in your component.
2. In the WOSMILDocument Binding Inspector window, add the `otherTagString` binding.
3. Bind `otherTagString` to
   an instance variable of type String named `qtNameSpace`.
4. In the component class's constructor, initialize `qtNameSpace` to `"xmlns:qt=\"http://www.apple.com/quicktime/resources/smilextensions\""`.

   QuickTime
   does not actually access the URL; it is used only to uniquely identify
   the QuickTime SMIL extensions. For more information, see [http://www.apple.com/quicktime/authoring/qtsmil.html](http://www.apple.com/quicktime/authoring/qtsmil.html).

[!](Linking_Presentations.md) [!](https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/Reference/index.html)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
