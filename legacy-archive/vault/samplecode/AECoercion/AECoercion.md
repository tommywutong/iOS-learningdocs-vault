---
title: AECoercion
apple_id: DTS10000202
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/AECoercion/Introduction/Intro.html
archived_at: '2026-07-18T02:59:26.606249Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](AECoerceINIT.r.md)

# AECoercion

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-07-22 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

This sample illustrates how to install a system level Apple event Manager type coercion handler at system startup time. The Apple Event Manager installs several type coercion handlers for you that will automatically coerce data types stored in Apple events from one type to another as needed. For example, 'odoc' (open document) Apple events contain a list of file system Alias records. If when reading such a list one requests FSSpec records, the Apple Event Manager's alias-to-FSSpec coercion handler is called automatically to convert the aliases from into FSSpec records without the application having to perform any special conversion operations. In this sample, a type coercion handler is installed for coercing pascal style strings into typeChar (ASCII strings). Requires: System 7.0 Keywords: AppleEvent Manager, coercion

[Next](AECoerceINIT.r.md)

