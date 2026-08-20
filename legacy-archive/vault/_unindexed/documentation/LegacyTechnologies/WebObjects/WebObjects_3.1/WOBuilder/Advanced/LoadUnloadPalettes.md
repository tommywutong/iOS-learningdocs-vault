---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/Advanced/LoadUnloadPalettes.html
archived_at: '2026-07-15T07:50:06.313821Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Advanced.book.md)
[!Previous Section](CreatePalette.md)

Loading and Unloading Palettes

# Loading and Unloading Palettes

- Choose Tools->Palettes->Open to load a palette.
- Choose Tools->Palettes->Close to unload a palette.

The palette window always displays the standard palettes (Static Elements, Form Elements, and Abstract Elements). It can also display your custom palettes or palettes that others have created. For example, the palette ___NeXT_Root___/NextDeveloper/Palettes/ClientSideComponents.wbpalette contains _client-side components_, components that are written in Java and execute on the client. Even though this palette is distributed with the WebObjects product, it's not loaded until you specifically request it.

If you want the palette window to display a nonstandard palette, choose Tools->Palettes->Open and select the __.wbpalette__ file to open. Once you have opened a palette, WebObjects Builder always displays it unless you specifically tell it not to. That is, if you quit WebObjects Builder and restart it, the nonstandard palette is opened at launch time.

If you don't want WebObjects Builder to display a palette any more, select the palette in the palette window and choose Tools->Palettes->Close. After you close a palette file, WebObjects Builder assumes you never want it opened. If you quit WebObjects Builder and restart it, it no longer opens that palette.
