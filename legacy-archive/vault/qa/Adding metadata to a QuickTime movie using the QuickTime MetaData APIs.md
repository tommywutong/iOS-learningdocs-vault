---
title: Adding metadata to a QuickTime movie using the QuickTime MetaData APIs
apple_id: DTS10004227
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2010-04-28'
source_url: https://developer.apple.com/library/archive/qa/qa1515/_index.html
archived_at: '2026-07-18T02:32:04.936920Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1515

# Adding metadata to a QuickTime movie using the QuickTime MetaData APIs

## Q:  How do I add metadata (such as album art, artist name, and so on) to a QuickTime movie file using the QuickTime MetaData APIs? I'm not sure which parameters to pass to `QTMetaDataAddItem` for the various metadata items. Please help.

A: Listing 1 shows how to add the album art (`kQTMetaDataCommonKeyArtwork`) metadata item to a movie using QTKit and the QuickTime Metadata APIs.

You must first get the movie’s metadata object using the `QTCopyMovieMetaData` function, and then pass this metadata object to the `QTMetaDataAddItem` function to add the actual item.

Here's a short description of the parameters that are passed to `QTMetaDataAddItem`:

The actual album art file data is passed in the `inValuePtr` parameter as an `NSData` object reference, and the size of the data is passed in the `inValueSize` parameter.

Since the album art file in this case is a JPEG file you must specify `kQTMetaDataTypeJPEGImage` for the `inDataType` parameter.

The album art items are being added as QuickTime native metadata format items so you must pass `kQTMetaDataStorageFormatQuickTime` for the `inMetaDataFormat` storage format parameter. And to allow unified access across the different QuickTime metadata container formats for your metadata item specify the `kQTMetaDataKeyFormatCommon` key format for the `inKeyFormat` parameter.

You get the movie's metadata object using the `QTCopyMovieMetaData` as described above. This value is passed in the `inMetaData` parameter.

Use `kQTMetaDataCommonKeyArtwork` to specify the album art metadata key in the `inKeyPtr` parameter.

Also, it is also a good idea to assign locale information to your metadata (using the `kQTMetaDataItemPropertyID_Locale` identifier property). The locale information designates a particular language or country, in case your file is opened on a system which is using a different language than yours. Use the `QTMetaDataSetItemProperty` function to set the metadata item locale property.

Lastly, call the `updateMovieFile` method to save your changes to the `QTMovie`.

__Listing 1__  Adding the artwork metadata item to a movie.

```objc
// Add the artwork metadata item to a movie file
-(void) addMovieJPEGArtworkMetaData:(QTMovie *)aQTMovie
                        artworkFile:(NSString *)filePath
{
    QTMetaDataRef   metaDataRef;
    Movie           theMovie;
    OSStatus        status;

    theMovie = [aQTMovie quickTimeMovie];
    status = QTCopyMovieMetaData (theMovie, &metaDataRef );
    NSAssert(status == noErr,@"QTCopyMovieMetaData failed!");

    if (status == noErr)
    {
        NSFileManager *fileMgr = [NSFileManager defaultManager];
        NSData *artworkData = [fileMgr contentsAtPath:filePath];
        NSAssert(artworkData != NULL,@"contentsAtPath failed!");

        if (artworkData)
        {
            OSType key = kQTMetaDataCommonKeyArtwork;
            QTMetaDataItem outItem;
            status = QTMetaDataAddItem(metaDataRef,
                                      kQTMetaDataStorageFormatQuickTime,
                                      kQTMetaDataKeyFormatCommon,
                                      (const UInt8 *)&key,
                                      sizeof(key),
                                      (const UInt8 *)[artworkData bytes],
                                      [artworkData length],
                                      kQTMetaDataTypeJPEGImage, // jpeg data
                                      &outItem);
            NSAssert(status == noErr,@"QTMetaDataAddItem failed!");

            const char *langCodeStr = [self langCode];
            status = QTMetaDataSetItemProperty(
                                              metaDataRef,
                                              outItem,
                                              kPropertyClass_MetaDataItem,
                                              kQTMetaDataItemPropertyID_Locale,
                                              strlen(langCodeStr) + 1,
                                              langCodeStr);
            NSAssert(status == noErr,@"QTMetaDataSetItemProperty failed!");

            if (status == noErr)
            {
                // we must update the movie file to save the
                // metadata items that were added
                BOOL success = [aQTMovie updateMovieFile];
                NSAssert(success == YES,@"updateMovieFile failed!");
            }

        }

        QTMetaDataRelease(metaDataRef);
    }
}

// Return the default language set by the user
// in the language tab of the International preference
// pane.
-(const char *)langCode
{
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    NSAssert(defaults != NULL,@"standardUserDefaults failed!");

    NSArray *languages = [defaults objectForKey:@"AppleLanguages"];
    NSAssert(languages != NULL,@"objectForKey failed!");

    NSString *langStr = [languages objectAtIndex:0];

    return ([langStr cStringUsingEncoding:NSMacOSRomanStringEncoding]);
}
```

Similarly, Listing 2 shows how to add the artist name (`kQTMetaDataCommonKeyArtist`) metadata item to a movie using QTKit and the Metadata APIs. The code for adding the artist name metadata is quite similar to the code in Listing 1 for adding the album art -- except the artist name metadata is specified as a C-string.

__Listing 2__  Adding the artist name metadata item to a movie.

```objc
// Add the artist name metadata item to a movie file
-(void) addMovieArtistMetaData:(QTMovie *)aQTMovie artistName:(NSString *)aNameStr
{
    QTMetaDataRef   metaDataRef;
    Movie           theMovie;
    OSStatus        status;

    theMovie = [aQTMovie quickTimeMovie];
    status = QTCopyMovieMetaData (theMovie, &metaDataRef );
    NSAssert(status == noErr,@"QTCopyMovieMetaData failed!");

    if (status == noErr)
    {
        const char *nameCStringPtr = [aNameStr UTF8String];
        NSAssert(nameCStringPtr != nil,@"UTF8String failed!");

        if (nameCStringPtr)
        {
            OSType key = kQTMetaDataCommonKeyArtist;
            QTMetaDataItem outItem;
            status = QTMetaDataAddItem(metaDataRef,
                                        kQTMetaDataStorageFormatQuickTime,
                                        kQTMetaDataKeyFormatCommon,
                                        (const UInt8 *)&key,
                                        sizeof(key),
                                        (const UInt8 *)nameCStringPtr,
                                        strlen(nameCStringPtr),
                                        kQTMetaDataTypeUTF8,
                                        &outItem);
            NSAssert(status == noErr,@"QTMetaDataAddItem failed!");

            // it is also recommended you set the locale identifier
            const char *langCodeStr = [self langCode];
            status = QTMetaDataSetItemProperty(
                                              metaDataRef,
                                              outItem,
                                              kPropertyClass_MetaDataItem,
                                              kQTMetaDataItemPropertyID_Locale,
                                              strlen(langCodeStr) + 1,
                                              langCodeStr);

            if (status == noErr)
            {
                // we must update the movie file to save the
                // metadata items that were added
                BOOL success = [aQTMovie updateMovieFile];
                NSAssert(success == YES,@"updateMovieFile failed!");
            }
        }

        QTMetaDataRelease(metaDataRef);
    }
}

// Return the default language set by the user
// in the language tab of the International preference
// pane.
-(const char *)langCode
{
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    NSAssert(defaults != NULL,@"standardUserDefaults failed!");

    NSArray *languages = [defaults objectForKey:@"AppleLanguages"];
    NSAssert(languages != NULL,@"objectForKey failed!");

    NSString *langStr = [languages objectAtIndex:0];

    return ([langStr cStringUsingEncoding:NSMacOSRomanStringEncoding]);
}
```


- [QuickTime 7 Update Guide](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7UpdateGuide/index.html)
- [QuickTime Movies Properties Reference](https://developer.apple.com/mac/library/documentation/QuickTime/Reference/QTRef_MovieProperties/Reference/reference.html)
- [QTMetadataEditor sample code](https://developer.apple.com/samplecode/QTMetadataEditor/index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-04-28 | Fixed minor bug in code Listing 1. |
| 2008-08-08 | Miscellaneous code fixes. |
| 2007-02-08 | New document that adding metadata to a QuickTime movie using the QuickTime MetaData APIs |

