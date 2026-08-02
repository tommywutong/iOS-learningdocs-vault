---
title: Limiting the component list in SCRequestImageSettings
apple_id: DTS10001614
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-01-12'
source_url: https://developer.apple.com/library/archive/qa/qa1062/_index.html
archived_at: '2026-07-18T02:29:55.057299Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1062

# Limiting the component list in SCRequestImageSettings

## Q:  How can I display a limited set of components in the SCRequestImageSettings dialog? I've been able to select a component and make it the default, but I cannot remove the other components from the list. I tried using `scListEveryCodec` but that didn't seem to help.

A: Although documented in the 'Sound Dialog Selectors' section of the QuickTime API reference, the selector you're looking for is `scCompressionListType`.

Use this selector with `SCSetInfo`. Pass in a pointer to a handle which contains an array of values of type `OSType` indicating the codecs you want presented to the user. Passing in `NULL` will reset the list. See Listing 1.

__Listing 1__  Limiting the codec list.

```
const UInt8 kNumberOfTypes = 4;

Handle    theTypesList = NULL;
OSTypePtr pTypesList = NULL;
SCSpatialSettings theDefaultChoice = { kSorenson3CodecType,
                                       (CodecComponent)kSorenson3CodecType,
                                       32,
                                       codecNormalQuality };

...

// limit the list to four - or however many you want
theTypesList = NewHandle(sizeof(OSType) * kNumberOfTypes);
if (theTypesList) {
   HLock(theTypesList);
   *pTypesList = (OSTypePtr)*theTypesList;

   pTypesList[0] = kH261CodecType;
   pTypesList[1] = kH263CodecType;
   pTypesList[2] = kSorensonCodecType;
   pTypesList[3] = kSorenson3CodecType;

   SCSetInfo(ci, scCompressionListType, &theTypesList);
   DisposeHandle(theTypesList);
}

// set up the default choice
SCSetInfo(ci, scSpatialSettingsType, &theDefaultChoice);

...

SCRequestImageSettings(ci);
```

You shouldn't need to use `scListEveryCodec`, it will show multiple variants for a given codec. For example, if you have your own JPEG codec it will show yours as well as the one built into QuickTime.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-01-12 | editorial |
| 2001-07-24 | New document that describes the scCompressionListType flag, which limits the list of compressors shown in the standard image settings dialog. |

