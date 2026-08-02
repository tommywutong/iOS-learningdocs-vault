---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.d.html
archived_at: '2026-07-15T05:24:02.051530Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.2.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.c.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.e.md)

---

#   Appearance Manager Versions

A number of 

versions of the Appearance Manager are currently available. [Table 2-1](#apple-gmytsmbu)
specifies

- 

  the version of the Appearance Manager that must or may be installed on a given version of the Mac OS
- 

  the version of the API provided by that Appearance Manager version
- 

  the version number produced by passing
  gestaltAppearanceVersion
  to the
  Gestalt
  function

__Table 2-1__  

Appearance Manager versions

|   System version |   Appearance Manager version |   API version |   gestaltAppearanceVersion |
| --- | --- | --- | --- |
|   System 7.1 through Mac OS 7.6.1 |   must install 1.0.2 or 1.0.3 |   1.0.1 |   1.0.1 |
|   Mac OS 8 |   1.0 (bundled) |   1.0 |   none |
|   Mac OS 8.1 |   1.0.1 (bundled) |   1.0.1 |   1.0.1 |
|   Mac OS 8 and Mac OS 8.1 |   may install 1.0.2 or 1.0.3 |   1.0.1 |   1.0.1 |
|   Mac OS 8.5 |   1.1 (built into the System file) |   1.1 |   1.1.0 |

Version 1.0 of the Appearance Manager does not advertise its version via
Gestalt
; if the
gestaltAppearanceVersion
selector is not present but the
gestaltAppearanceAttr
selector is present, you can assume version 1.0 of the API is available.

Appearance Manager 1.0.2 uses
Gestalt
to advertise version 1.0.1 of the API. The only differences between Appearance Manager 1.0.1 and 1.0.2 are that 1.0.2 contains extra code for backward compatibility and the ".Keyboard" font, which you can detect by calling the Font Manager function
GetFNum

Appearance Manager 1.0.3 uses
Gestalt
to advertise version 1.0.1 of the API. The only difference between Appearance Manager 1.0.2 and 1.0.3 is that 1.0.3 no longer contains the ".Keyboard" font. In the 1.0.3 SDK, the font is delivered as a separate suitcase that should be installed into the Fonts folder. The font can still be detected with the function
GetFNum
.

Do not attempt to install a version of the Appearance Manager bundled with the Mac OS onto any other version of the Mac OS. Apple has not tested such configurations and does not recommend or support such configurations.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.2.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.c.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.e.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
