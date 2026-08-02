---
title: Obtaining and Using Icons With Icon Services
apple_id: TP40000916
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2003-02-01'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Icon_Service_nd_Utilities/02concepts/concepts.html
archived_at: '2026-07-15T05:23:11.740769Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Obtaining and Using Icons With Icon Services](Introduction%20to%20Obtaining%20and%20Using%20Icons%20With%20Icon%20Services.md)


[Next](Icon%20Services%20Tasks.md)[Previous](Introduction%20to%20Obtaining%20and%20Using%20Icons%20With%20Icon%20Services.md)

# Icon Services Concepts

Icon Services provides icon data to multiple Mac OS clients, including the Finder, extensions and applications. Using Icon Services to obtain icon data means you can provide efficient icon caching and release memory when you don’t need icon data any longer. Icon Services provides the appropriate icon for any file object (file, folder, or volume), as well as other commonly used icons such as caution, note, or help icons in alert boxes, for example. The icons provided by Icon Services support a much larger palette of colors: up to 24 bits per pixel and an eight-bit mask. Icons are Appearance-compliant and appropriate to the active theme.

The basic data type used by Icon Services is the `IconRef`, a 32-bit opaque value. You obtain an `IconRef` by calling one of the `GetIconRef` functions described in [Obtaining and Releasing IconRefs](Icon%20Services%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjwfuzs2qscineekr2biq). Two or more files that have the same file type and creator and do not provide custom icons will use the same `IconRef`. Files with custom icons have their own `IconRef`.

`IconRef` values are reference counted, so that the icon data represented by a particular `IconRef` can be shared by several clients simultaneously. Each client that uses a particular `IconRef` increments that `IconRef`’s reference count. When there are no more clients using a particular `IconRef`, the icon data associated with it is disposed of.

The `'icns'` resource is a means of providing a single source for icon data, as opposed to the variety of icon resources represented by `‘ICN#’`, `‘icl8’` and other familiar resource types. Combining all icon data into a single resource type speeds up icon fetching and simplifies resource management.

The `'icns'` resource provides for 32-bit-deep icon data.

Icons provided through the `'icns'` resource feature deep masks, meaning an icon mask can have 256 different levels of transparency.

The `'icns'` resource adds “huge” icons, which are 48 pixels by 48 pixels, as well as providing the sizes contained in other icon resources. For more information, see `'icns'`.

[Next](Icon%20Services%20Tasks.md)[Previous](Introduction%20to%20Obtaining%20and%20Using%20Icons%20With%20Icon%20Services.md)

