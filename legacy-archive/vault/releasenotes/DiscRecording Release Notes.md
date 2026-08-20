---
title: DiscRecording Release Notes
apple_id: TP40001002
resource_type: Release Note
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: DiscRecording
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/MusicAudio/RN-DiscRecording/index.html
archived_at: '2026-07-18T02:58:59.045434Z'
---
> 导航：[总目录](../README.md) · [releasenotes](../_indexes/releasenotes.md)



# Disc Recording Release Notes for OS X v10.5

This release note describes changes to the Disc Recording frameworks from OS X version 10.4

#### Contents:

- [64 Bit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambsfvcg63tujruw422fnrsw2zlooreuixzr)
- [Garbage Collection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambsfvcg63tujruw422fnrsw2zlooreuixzs)
- [UDF 2.0](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambsfvcg63tujruw422fnrsw2zlooreuixzt)
- [R-W Subchannel Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambsfvcg63tujruw422fnrsw2zlooreuixzu)
- [DVD-R DL Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambsfvcg63tujruw422fnrsw2zlooreuixzv)
- [Localization API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambsfvcg63tujruw422fnrsw2zlooreuixzw)
- [CD Text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambsfvcg63tujruw422fnrsw2zlooreuixzx)
- [Disk Image handling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambsfvcg63tujruw422fnrsw2zlooreuixzy)

### 64 Bit

In OS X v10.5, the Disc Recording frameworks are 64-bit, enabling building and running applications using it as 64-bit.

There are a significant number of API changes in Cocoa and Disc Recording to accomodate and enable 64-bit. Please refer to the
_[Foundation Release Notes for macOS 10.13 and iOS 11](Foundation/Foundation%20Release%20Notes%20for%20macOS%2010.13%20and%20iOS%2011.md)_ for more information on 64-bit for Cocoa.

### Garbage Collection

The Disc Recording frameworks have been updated to support garbage collection when used from Objective C.

### UDF 2.0

The Disc Recording content creation engine now supports writing UDF 2.0 discs in addition to UDF 1.02 and 1.5

### R-W Subchannel Support

Disc Recording now allows clients to specify the R-W subchannel information written to discs. This allows applications to create CDs containing custom graphics data (CD+G) or other application specific uses. R-W subchannel writing is controlled by the`kDRSubchannelDataFormKey`

### DVD-R DL Support

DVD-R Dual Layer burning support has been added as API.

### Localization API

`DRCopyLocalizedStringForValue` is a new API that assists applications using Disc Recording in presenting the correct localized strings to the user for various media types, status and support levels.

### CD Text

Several problems having to do with accented characters in CD Text packs have been resolved. Disc Recording now uses the proper Red Book Encoding - ISO Latin 1 Music CD Variant.

Reading and writing CD Text has been generally improved to handle more combinations of languages and character sets.

### Disk Image handling

A resource leak that would leave a disk image file open and un-deletable if burned using -[
`DRBurn layoutForImageFile:`] has been fixed.
