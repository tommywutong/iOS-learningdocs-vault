---
title: TwoColumn LDEF
apple_id: DTS10000622
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/TwoColumn_LDEF/Introduction/Intro.html
archived_at: '2026-07-18T03:27:24.257062Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](TwoColLDEF.c.md)

# TwoColumn LDEF

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-30 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

Two-column LDEF code resource looks for a comma in the text of each cell and draws the text that follows the comma half-way across the cell so a cell containing the text +--------------+ | abc,def | +--------------+ will instead appear as +--------------+ | abc def | +--------------+ To see this LDEF in action, paste it into the ModalList sample program and recompile the program so that the LNew call uses the definition procedure 128 rather than 0

[Next](TwoColLDEF.c.md)

