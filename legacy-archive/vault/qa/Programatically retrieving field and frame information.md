---
title: Programatically retrieving field and frame information
apple_id: DTS10004447
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2007-09-13'
source_url: https://developer.apple.com/library/archive/qa/qa1547/_index.html
archived_at: '2026-07-18T02:32:15.936067Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1547

# Programatically retrieving field and frame information

## Q:  How can I programatically find out if video media in a QuickTime Movie is interlaced or progressive scan?

A: How can I programatically find out if video media in a QuickTime Movie is interlaced or progressive scan?

The Field/Frame information for a Media is stored in the Image Description and may be returned by calling `ICMImageDescriptionGetProperty` using the `kICMImageDescriptionPropertyID_FieldInfo` property ID.

Asking for the `kICMImageDescriptionPropertyID_FieldInfo` property will return the information (if available) in a `FieldInfoImageDescriptionExtension2` structure (see below). The `fields` variable of this structure will be either set to `kQTFieldsProgressiveScan` if the content is progressive, or `kQTFieldsInterlaced` if it is interlaced.


```
/* Field/Frame Info */ struct FieldInfoImageDescriptionExtension2 {   UInt8               fields;   UInt8               detail; };  /* Field Info Values */ enum {   kQTFieldsProgressiveScan  = 1,   kQTFieldsInterlaced       = 2 };  /* Frame Detail Values */ enum {   kQTFieldDetailUnknown                 = 0,   kQTFieldDetailTemporalTopFirst        = 1,   kQTFieldDetailTemporalBottomFirst     = 6,   kQTFieldDetailSpatialFirstLineEarly   = 9,   kQTFieldDetailSpatialFirstLineLate    = 14 };
```

Listing 1 demonstrates using `ICMImageDescriptionGetProperty` to get the Field/Frame info.

__Listing 1__  IsInterlaced function.

```swift
Boolean IsInterlaced(Track inVideoTrack) {     Media aMedia = 0;     Boolean isInterlaced = NO; // assume progressive     FieldInfoImageDescriptionExtension2 *fieldInfo = NULL;     ImageDescriptionHandle desc = NULL;      if (0 == inVideoTrack) goto bail;      // get the tracks media     aMedia = GetTrackMedia(inVideoTrack);     if (0 == aMedia) goto bail;      // grab the image description     desc = (ImageDescriptionHandle)NewHandle(0);     if (NULL == desc) goto bail;     GetMediaSampleDescription(aMedia, 1, (SampleDescriptionHandle)desc);      // get the size of the returned property     ByteCount propertyValueSize = 0;     ComponentValueType propertyType = 0;     UInt32 propertyFlags = 0;      OSStatus status = ICMImageDescriptionGetPropertyInfo(desc,                                                          kQTPropertyClass_ImageDescription,                                                          kICMImageDescriptionPropertyID_FieldInfo,                                                          &propertyType,                                                          &propertyValueSize,                                                          &propertyFlags);    if (noErr != status) goto bail;      // get the FieldInfo property - for more information see ImageCodec.h     fieldInfo = (FieldInfoImageDescriptionExtension2 *)calloc(1, propertyValueSize);      status = ICMImageDescriptionGetProperty(desc,                                             kQTPropertyClass_ImageDescription,                                             kICMImageDescriptionPropertyID_FieldInfo,                                             propertyValueSize,                                             fieldInfo,                                             NULL);     // check the value     if (noErr == status) {         isInterlaced = (fieldInfo->fields == kQTFieldsInterlaced);     }  bail:     if (NULL != desc) DisposeHandle((Handle)desc);     if (NULL != fieldInfo) free(fieldInfo);      return isInterlaced; }
```


- [QuickTime 7 Update Guide](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7UpdateGuide/index.html)
- [Technical Q&A QA1438, 'Using the QuickTime DVCompressor properties'](https://developer.apple.com/qa/qa2005/qa1438.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-09-13 | New document that discusses the use of the kICMImageDescriptionPropertyID_FieldInfo property to retrieve Field/Frame information. |

