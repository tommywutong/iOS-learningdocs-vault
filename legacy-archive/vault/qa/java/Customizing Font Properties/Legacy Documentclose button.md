---
title: Customizing Font Properties
apple_id: DTS10001385
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-17'
source_url: https://developer.apple.com/library/archive/qa/java/java10.html
archived_at: '2026-07-18T02:29:41.234563Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA10Customizing Font Properties |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ---   Q: On other platforms, there is a `font.properties` file that Java uses to determine which fonts to use for different categories of objects. I cannot find that file on the Mac and want to know how to customize my application's font properties.  The fonts that I am using on other platforms do not look good on the Mac, and I would like to experiment with some different fonts to see if I can get a better-looking display.  A: MRJ does not use the `font.properties` approach for several reasons, but there are still several ways to customize font usage, depending on the way fonts are being used in the application.  If you are designing your application with fonts in mind, the most straightforward and flexible way to provide customization is to explicitly set all fonts based on platform-specific resource bundles or system properties. See `java.awt.Font.getFont` in [Chan & Lee The Java Class Libraries Vol. 2](http://www.amazon.com/exec/obidos/ASIN/0201310031/qid=923695186/002-9950660-4614657) for documentation on retrieving a font from a system property. To set the custom system property in MRJ, use the properties panel in JBindery (part of the [MRJ SDK](https://developer.apple.com/java/text/download.html#sdk)).  For example, if you set the property "`appname.component.font`" to "`arial-bold-9`", and your component's code has something like:   |  | | --- | | ``` setFont(Font.getFont("appname.component.font", kDefaultFont)); ``` |   The font for your component will be set to arial, style bold, 9 point. Note that you can take advantage of the fact that font settings are inherited by components from their containers to minimize the number of places you need to make these settings.  If your application was not designed from the beginning to support font customization, then you will need to do one of the following:   - Re-specify the defaults used when no font is set in the code.   In MRJ 2.1, you can set properties for the default fonts used for Windows and Dialogs. To do this, specify the font or logical font to use as the default in windows or dialogs by setting the property in JBindery to something similar to this:   |  | | --- | | ``` awt.font.macwindowdefault = SmallSystem // Appearance dependent. awt.font.macdialogdefault = Times ``` |    - Set properties for mapping logical font names to fonts.   This also allows you to reset any of the standard mappings. For example, use the properties panel in JBindery to set the property `awt.font.dialog` to Courier, and you'll see that text that previously used Dialog font will now show up in Courier:   |  | | --- | | ``` awt.font.dialog = courier awt.font.serif = New Century Schlbk ``` |    (Note: only the logical font name mappings are case sensitive.)   - Map explicit font names.   You can map one font to another font or logical font. Below, the first example is mapping the Arial font to the logical font `Application`, and the second example is mapping the Times font to use the Courier font instead:   |  | | --- | | ``` awt.font.arial = Application awt.font.times = courier ``` |    For the three cases above, properties can be set to real, installed, font names, such as Courier, or they can be set to logical font names. Valid cross-platform logical font names are `Serif`, `SansSerif`, `Monospaced`, `Dialog`, and `DialogInput`. There are also three MRJ-specific logical font names, which are `System`, `Application`, and `SmallSystem`. These MRJ-specific fonts will be dependent on the settings of the Mac OS Appearance Manager. All of the logical font names are case-sensitive, unlike explicit font names which are case insensitive.  If you are using Swing, be aware that it uses a separate set of system properties for its fonts, at least some of which MRJ sets in its font peer if they haven't been set at startup. These properties set the font name, style, and size.  For example:   |  | | --- | | ``` swing.plaf.metal.controlFont = arial-bold-14 swing.plaf.metal.smallFont = SmallSystem--9 and so forth. ``` |   Swing has more such properties that can be set; consult the Swing documentation. |

#### [May 17 1999]

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
