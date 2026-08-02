---
title: Using the kQTPropertyClass_DRM properties with QuickTime
apple_id: DTS10003924
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-04-11'
source_url: https://developer.apple.com/library/archive/qa/qa1476/_index.html
archived_at: '2026-07-18T02:31:22.763134Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1476

# Using the kQTPropertyClass_DRM properties with QuickTime

## Q:  How can an application determine if some QuickTime media (such as an imported music file) is DRM-protected and if so, find out if the current machine is authorized to play it?

A: QuickTime defines a number of DRM properties in ImageCompression.h. Media Handlers may be queried to determine the value of the `kQTDRMPropertyID_IsProtected` and `kQTDRMPropertyID_IsAuthorized` properties, and may query or set the `kQTDRMPropertyID_InteractWithUser` property.


```
/* DRM properties*/

enum {
    kQTPropertyClass_DRM = 'drm '
};

enum {
    kQTDRMPropertyID_InteractWithUser = 'shui', /* Boolean* */
    kQTDRMPropertyID_IsProtected  = 'prot',     /* Boolean* */
    kQTDRMPropertyID_IsAuthorized = 'auth'      /* Boolean* */
};
```

Applications query a Media Handler Component for properties of the class `kQTPropertyClass_DRM` by calling `QTGetComponentProperty` and passing in a `MediaHandler` (an instance of the media handler component for the media the application is interested in) as the first parameter. Applications may also set the `kQTDRMPropertyID_InteractWithUser` property by calling `QTSetComponentProperty`. See Listing 1.

If the property does not exist a `kQTPropertyNotSupportedErr` (-2195) is returned.

__Listing 1__  Example use of `kQTPropertyClass_DRM` properties.

```
OSStatus CheckSoundMediaIsAuthorized(Movie inMovie,
                                     UInt32 inSoundTrackIndex,
                                     Boolean inInteractWithUser,
                                     Boolean *outIsAuthorized)
{
    Track aTrack;
    Media aMedia;
    MediaHandler mh;
    Boolean isProtected;

    OSStatus err = paramErr;

    // get n sound track
    aTrack = GetMovieIndTrackType(inMovie, inSoundTrackIndex, SoundMediaType,
                                  movieTrackMediaType | movieTrackEnabledOnly);
    if (aTrack) {
        // get the track media
        aMedia = GetTrackMedia(aTrack);
        if (aMedia) {
            // get the media handler we can query
            mh = GetMediaHandler(aMedia);
            if (mh) {
                // is this media protected?
                err = QTGetComponentProperty(mh, kQTPropertyClass_DRM, kQTDRMPropertyID_IsProtected,
                                             sizeof(isProtected), &isProtected, NULL);
                if ((noErr == err) && isProtected) {
                    // if so, is this media authorized on this machine?
                    // user interaction may be turned off so no automatic dialog will pop up
                    // if the machine is not authorized -- an application may therefore choose
                    // to show their own custom UI and direct the user appropriately
                    QTSetComponentProperty(mh, kQTPropertyClass_DRM, kQTDRMPropertyID_InteractWithUser,
                                           sizeof(inInteractWithUser), &inInteractWithUser);

                    err = QTGetComponentProperty(mh, kQTPropertyClass_DRM, kQTDRMPropertyID_IsAuthorized,
                                                 sizeof(*outIsAuthorized), outIsAuthorized, NULL);
                }
            }
        }
    }

    return err;
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-04-11 | New document that explains how to use the kQTPropertyClass_DRM properties with QuickTime media. |

