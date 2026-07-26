---
title: 'The Apple Symbols Font: A Great Repository for iPhone Button Icons'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2009/10/apple-symbols-font-repository-for-iphone-icons/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7c193eb8fdde1edc'
translated: false
---

> 原文：[The Apple Symbols Font: A Great Repository for iPhone Button Icons](https://oleb.net/blog/2009/10/apple-symbols-font-repository-for-iphone-icons/)　·　Ole Begemann

# The Apple Symbols Font: A Great Repository for iPhone Button Icons

**Update February 22, 2013:** When I originally wrote this article, the current version of Mac OS X was 10.6. Unfortunately, Apple revised the Character Viewer in OS X 10.7. There is no longer a Glyph View that shows the glyph catalog of a particular font. This makes it much harder to get at the interesting glyphs in the Apple Symbols font. If you are a Mac developer and looking for an app idea, I think an app that made it super easy to create an image file from a font glyph has the potential to be winner.

For iPhone developers looking for icons to use in buttons, toolbars, navigation bars and tab bars, there are a few good resources available, for example Joseph Wain’s excellent (and free!) [collection of 130 icons](http://www.glyphish.com/) and Eddie Wilson’s [set of 160 iPhone UI icons](http://www.eddit.com/shop/iphone_ui_icon_set/) ($69). These are not only beautifully designed but also already have the right sizes and format for use in toolbars and tab bars.

If you are not afraid of making your own PNGs, there is another free and hidden treasure in every Mac OS X installation: the [Apple Symbols](https://en.wikipedia.org/wiki/Apple_Symbols) font. It contains many of the icons Apple uses in the built-in iPhone apps and makes them readily available for your own buttons.

# Background: standard buttons in the iPhone SDK

The set of standard buttons that Apple ships with the iPhone SDK is quite limited in both number and context. For instance, the standard toolbar buttons can only be used inside a `UIBarButtonItem` on a toolbar or navigation bar. Now, this is a good thing, I hear you say, because it enforces consistent UIs. And I agree to a point. Specifically, I urge you to follow Apple’s Human Interface Guidelines and use the system-provided buttons for (and only for) [their documented meanings](http://developer.apple.com/iphone/library/documentation/UserExperience/Conceptual/MobileHIG/SystemProvided/SystemProvided.html#//apple_ref/doc/uid/TP40006556-CH15-SW14) or you risk the rejection of your app.

[![Icons for buttons, toolbars/navigation bars and tab bars shipped with the iPhone SDK](https://oleb.net/media/iphone-toolbar-icons.png)](https://oleb.net/media/iphone-toolbar-icons.png)

<sub>Icons for buttons, toolbars/navigation bars and tab bars shipped with the iPhone SDK.</sub>

# Apple Symbols to the rescue

If the standard buttons do not cover your needs or ff you need to use one of the standard toolbar buttons outside of a toolbar (in a simple `UIButton`, for example), you are out of luck. But the Apple Symbols font contains many more standard icons for your icon-making pleasure. Open the OS X Character Viewer in Glyph View, select the Apple Symbols font and scroll down to the very end of the Glyph Catalog:

[![The Apple Symbols font in Character Viewer](https://oleb.net/media/apple-symbols-font-glyphs-table.png)](https://oleb.net/media/apple-symbols-font-glyphs-table.png)

<sub>The Apple Symbols font in Character Viewer.</sub>

Making a button from one of these glyphs is as simple as inserting it into Photoshop or any other graphics software that can work with fonts, resizing it, and saving it as a transparent PNG. Use about 20⨉20 pixels for toolbar and navbar icons, and about 30⨉30 pixels for tab bar icons and other buttons.

# Am I allowed to do this?

I am not a lawyer but I have not found any restrictions that would forbid the use of these glyphs in your apps. This is what the [Mac OS X license agreement](http://images.apple.com/legal/sla/docs/macosx106.pdf) has to say about fonts:

> D. Fonts. Subject to the terms and conditions of this License, you may use the fonts included with the Apple Software to display and print content while running the Apple Software; however, you may only embed fonts in content if that is permitted by the embedding restrictions accompanying the font in question. These embedding restrictions can be found in the Font Book/Preview/Show Font Info panel.

And Font Book lists no license or embedding restrictions for Apple Symbols:

[![Apple Symbols Font Info](https://oleb.net/media/apple-symbols-font-info.png)](https://oleb.net/media/apple-symbols-font-info.png)

**Updates:**

**January 22, 2010:** Several readers have reported problems with getting the glyphs into Photoshop. It seems Photoshop does not play nicely with Apple’s Character Viewer. I have no solution, other than suggesting to use a different image editor such as Acorn or Pixelmator. If all else fails, you could insert the glyph into text edit, save it as a PDF and open the PDF in Photoshop or Illustrator.

**November 21, 2010:** If you want to use a custom graphic as an image in a `UITabBar` or `UIBarButtonItem`, remember that the image’s alpha channel is the significant indicator whether a pixel is visible or not in the toolbar button. Your PNG file’s alpha channel must contain the brightness of each pixel.
