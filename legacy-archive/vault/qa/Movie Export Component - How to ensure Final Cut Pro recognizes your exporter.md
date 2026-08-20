---
title: Movie Export Component - How to ensure Final Cut Pro recognizes your exporter
apple_id: DTS10003515
resource_type: QA
platform: macOS
topic: Apple Applications
technology: null
published: '2005-03-08'
source_url: https://developer.apple.com/library/archive/qa/qa1415/_index.html
archived_at: '2026-07-18T02:30:34.513342Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1415

# Movie Export Component - How to ensure Final Cut Pro recognizes your exporter

## Q:  My QuickTime movie export component works with QuickTime Player and iMovie but doesn't show up in Final Cut Pro's Export->Using QuickTime Conversion..." menu. What can I do to make it show up?

A: Final Cut Pro requires that your export component include a `kQTMovieExportSourceInfoResourceType` ( '`src#`' ) entry with the ID `2` in its component public resource list ( '`thnr`' ). This entry should be mapped to the '`trk#`' resource which indicates the number of tracks of a given type that can be exported. See Listing 1.

Final Cut Pro has this requirement so it can optimize the export operation based on what an export component can actually do. This avoids forcing the end user to render material which would be wasted if the export component would not be using this media during export.

It is good practice to include this public resource list entry in all cases as other QuickTime applications may also make use of this information.

__Listing 1__

```
// Component public resource list
resource 'thnr' (129) {
    {
        'src#', 1, 0,
        'src#', 129, 0,

        'src#', 2, 0,    // src# ID 2
        'trk#', 129, 0,  // mapped to trk#

        .
        .
        .
    }
};

// The 'trk#' resource is meant to indicate the number of tracks of the given types that can be exported.
// The resource is identical to the resource for data sources. The difference is that the flags will have one
// of two values:
//  isMediaType - A media type such as 'vide' for video tracks or 'soun' for sound tracks.
//  isMediaCharacteristic - Indicates that mediaType corresponds to a media characteristic such a 'eyes'
//                                       for visual tracks or 'ears' for tracks with sound.
resource 'trk#' (129) {
    {
        'eyes', 1, 65535, isMediaCharacteristic,
        'soun', 1, 65535, isMediaType
    }
};
```


[Electric Image Component](https://developer.apple.com/samplecode/ElectricImageComponent/ElectricImageComponent.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-03-08 | New document that explains how to make sure Final Cut Pro will recognizes a custom QuickTime movie export component. |

