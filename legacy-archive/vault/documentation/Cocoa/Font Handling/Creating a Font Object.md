---
title: Font Handling
apple_id: 10000093i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontHandling/Tasks/CreatingAFontObject.html
archived_at: '2026-07-15T07:15:46.940443Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Handling](Introduction%20to%20Font%20Handling.md)


[Next](Getting%20Font%20Metrics.md)[Previous](Introduction%20to%20Font%20Handling.md)

# Creating a Font Object

You don’t create font objects using the `alloc` and `init` methods
(or with constructors in Java), instead, you use either `fontWithName:matrix:` or `fontWithName:size:` to
look up an available font and alter its size or matrix to your needs. These
methods check for an existing font object with the specified characteristics,
returning it if there is one. Otherwise, they look up the font data
requested and create the appropriate object.

NSFont also defines a number of methods for specifying standard
system fonts, such
as `systemFontOfSize:`, `userFontOfSize:`,
and `messageFontOfSize:`.
To request the default size for these standard fonts,
pass `0` or a negative
number as the font size. The standard system font methods are listed
in [Querying Aqua Font Variations](Querying%20Aqua%20Font%20Variations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg44dqlkdjjbeqqsdi5ba).

[Next](Getting%20Font%20Metrics.md)[Previous](Introduction%20to%20Font%20Handling.md)

