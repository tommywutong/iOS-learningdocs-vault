---
title: 'Managing Fonts: QuickDraw'
apple_id: TP30000982
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Managing_FontManager/fm_intro/fmintro.html
archived_at: '2026-07-15T05:23:29.988957Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Managing%20Fonts-%20QuickDraw%20Concepts.md)

# Introduction to Managing Fonts: QuickDraw

The Font Manager is a QuickDraw-based collection of routines and data structures that you can use to manage the fonts your application uses to display and print text. The Font Manager reads font data from the font files on the system’s hard disk and other locations (such as from a PDF, the network, and CD-ROM discs) and creates the bitmap images used to display text. You can use the Font Manager to determine the characteristics of a font, change certain font settings, favor outline fonts over bitmapped fonts, and manipulate fonts in memory. With Mac OS 9 and CarbonLib, additions to the Font Manager API now allow support of more comprehensive font management including: listing, installing, activating, and deactivating font files and retrieving information from the repository of font data.

Font management consists of two tasks: managing font files (installing, activating, and deactivating), and maintaining a repository of font data. In the past, font management relied upon the Finder and the Fonts folder along with specialized code in the Font Manager and Resource Manager to populate and manage the font database. Because the Resource Manager was not designed to handle the sizeable data storage and retrieval needs of professional-level font collections, third-party font management utilities were created to address the limitations inherent in the System suitcase model. Font management utilities have had to manipulate directly system font data, a practice that is not supported in Mac OS X.

Font management capabilities in Mac OS 8 and 9 increased dramatically with the addition of Apple Type Services for Unicode Imaging (ATSUI). ATSUI introduced a text rendering engine and font management model to address the data storage and retrieval needs of professional-level font collections. ATSUI is designed to handle multiple font technologies and file formats. In addition, the Font Manager and QuickDraw have been rewritten to integrate the glyph data cache and font data management system. Developers no longer need to depend upon the Resource Manager to access and modify the font collection. Instead, CarbonLib provides a new Font Management API as part of the Font Manager.

The revised Font Manager supports for the following tasks:

- Enumerating fonts and font families.
- Accessing information on font families, such as name, character encoding, and member fonts.
- Accessing information on fonts, such as font technology, format, name, foundry, and version.
- Accessing font data.
- Creating and managing a Font menu.

[Next](Managing%20Fonts-%20QuickDraw%20Concepts.md)

