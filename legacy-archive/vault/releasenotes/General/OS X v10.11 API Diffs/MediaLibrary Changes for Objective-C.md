---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/MediaLibrary.html
archived_at: '2026-07-18T02:53:09.962135Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# MediaLibrary Changes for Objective-C

### MediaLibrary

#### MLMediaGroup.h

Modified [MLMediaGroup.attributes](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419125-attributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *attributes ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,id> *attributes ``` |

Modified [MLMediaGroup.childGroups](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1418990-childgroups)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *childGroups ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<MLMediaGroup *> *childGroups ``` |

Modified [MLMediaGroup.iconImage](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419172-iconimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSImage *iconImage ``` |
| To | ``` @property(readonly, copy, nullable) NSImage *iconImage ``` |

Modified [MLMediaGroup.identifier](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419339-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *identifier ``` |
| To | ``` @property(readonly, copy, nonnull) NSString *identifier ``` |

Modified [MLMediaGroup.mediaLibrary](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419261-medialibrary)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) MLMediaLibrary *mediaLibrary ``` |
| To | ``` @property(readonly, assign, nullable) MLMediaLibrary *mediaLibrary ``` |

Modified [MLMediaGroup.mediaObjects](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1418982-mediaobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *mediaObjects ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<MLMediaObject *> *mediaObjects ``` |

Modified [MLMediaGroup.mediaSourceIdentifier](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419322-mediasourceidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *mediaSourceIdentifier ``` |
| To | ``` @property(readonly, copy, nonnull) NSString *mediaSourceIdentifier ``` |

Modified [MLMediaGroup.modificationDate](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419335-modificationdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDate *modificationDate ``` |
| To | ``` @property(readonly, copy, nullable) NSDate *modificationDate ``` |

Modified [MLMediaGroup.name](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419121-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *name ``` |
| To | ``` @property(readonly, copy, nullable) NSString *name ``` |

Modified [MLMediaGroup.parent](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419333-parent)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) MLMediaGroup *parent ``` |
| To | ``` @property(readonly, assign, nullable) MLMediaGroup *parent ``` |

Modified [MLMediaGroup.typeIdentifier](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419155-typeidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *typeIdentifier ``` |
| To | ``` @property(readonly, copy, nonnull) NSString *typeIdentifier ``` |

Modified [MLMediaGroup.URL](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419079-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSURL *URL ``` |
| To | ``` @property(readonly, copy, nullable) NSURL *URL ``` |

#### MLMediaLibrary.h

Modified [-[MLMediaLibrary initWithOptions:]](https://developer.apple.com/documentation/medialibrary/mlmedialibrary/1418988-initwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithOptions:(NSDictionary *)options ``` |
| To | ``` - (instancetype _Nonnull)initWithOptions:(NSDictionary<NSString *,id> * _Nonnull)options ``` |

Modified [MLMediaLibrary.mediaSources](https://developer.apple.com/documentation/medialibrary/mlmedialibrary/1419219-mediasources)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *mediaSources ``` |
| To | ``` @property(readonly, copy, nullable) NSDictionary<NSString *,MLMediaSource *> *mediaSources ``` |

#### MLMediaObject.h

Modified [MLMediaObject.artworkImage](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416701-artworkimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSImage *artworkImage ``` |
| To | ``` @property(readonly, copy, nullable) NSImage *artworkImage ``` |

Modified [MLMediaObject.attributes](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416715-attributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *attributes ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,id> *attributes ``` |

Modified [MLMediaObject.contentType](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416722-contenttype)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *contentType ``` |
| To | ``` @property(readonly, copy, nullable) NSString *contentType ``` |

Modified [MLMediaObject.identifier](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416716-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *identifier ``` |
| To | ``` @property(readonly, copy, nonnull) NSString *identifier ``` |

Modified [MLMediaObject.mediaLibrary](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416699-medialibrary)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) MLMediaLibrary *mediaLibrary ``` |
| To | ``` @property(readonly, assign, nullable) MLMediaLibrary *mediaLibrary ``` |

Modified [MLMediaObject.mediaSourceIdentifier](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416711-mediasourceidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *mediaSourceIdentifier ``` |
| To | ``` @property(readonly, copy, nonnull) NSString *mediaSourceIdentifier ``` |

Modified [MLMediaObject.modificationDate](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416705-modificationdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDate *modificationDate ``` |
| To | ``` @property(readonly, copy, nullable) NSDate *modificationDate ``` |

Modified [MLMediaObject.name](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416720-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *name ``` |
| To | ``` @property(readonly, copy, nullable) NSString *name ``` |

Modified [MLMediaObject.originalURL](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416703-originalurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSURL *originalURL ``` |
| To | ``` @property(readonly, copy, nullable) NSURL *originalURL ``` |

Modified [MLMediaObject.thumbnailURL](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416708-thumbnailurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSURL *thumbnailURL ``` |
| To | ``` @property(readonly, copy, nullable) NSURL *thumbnailURL ``` |

Modified [MLMediaObject.URL](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416718-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSURL *URL ``` |
| To | ``` @property(readonly, copy, nullable) NSURL *URL ``` |

#### MLMediaSource.h

Modified [MLMediaSource.attributes](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419157-attributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *attributes ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,id> *attributes ``` |

Modified [-[MLMediaSource mediaGroupForIdentifier:]](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419283-mediagroup)

|  | Declaration |
| --- | --- |
| From | ``` - (MLMediaGroup *)mediaGroupForIdentifier:(NSString *)mediaGroupIdentifier ``` |
| To | ``` - (MLMediaGroup * _Nullable)mediaGroupForIdentifier:(NSString * _Nonnull)mediaGroupIdentifier ``` |

Modified [-[MLMediaSource mediaGroupsForIdentifiers:]](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419337-mediagroupsforidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)mediaGroupsForIdentifiers:(NSArray *)mediaGroupIdentifiers ``` |
| To | ``` - (NSDictionary<NSString *,MLMediaGroup *> * _Nonnull)mediaGroupsForIdentifiers:(NSArray<NSString *> * _Nonnull)mediaGroupIdentifiers ``` |

Modified [MLMediaSource.mediaLibrary](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419004-medialibrary)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) MLMediaLibrary *mediaLibrary ``` |
| To | ``` @property(readonly, assign, nullable) MLMediaLibrary *mediaLibrary ``` |

Modified [-[MLMediaSource mediaObjectForIdentifier:]](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419209-mediaobject)

|  | Declaration |
| --- | --- |
| From | ``` - (MLMediaObject *)mediaObjectForIdentifier:(NSString *)mediaObjectIdentifier ``` |
| To | ``` - (MLMediaObject * _Nullable)mediaObjectForIdentifier:(NSString * _Nonnull)mediaObjectIdentifier ``` |

Modified [-[MLMediaSource mediaObjectsForIdentifiers:]](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419123-mediaobjectsforidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)mediaObjectsForIdentifiers:(NSArray *)mediaObjectIdentifiers ``` |
| To | ``` - (NSDictionary<NSString *,MLMediaObject *> * _Nonnull)mediaObjectsForIdentifiers:(NSArray<NSString *> * _Nonnull)mediaObjectIdentifiers ``` |

Modified [MLMediaSource.mediaSourceIdentifier](https://developer.apple.com/documentation/medialibrary/mlmediasource/1418986-mediasourceidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *mediaSourceIdentifier ``` |
| To | ``` @property(readonly, copy, nonnull) NSString *mediaSourceIdentifier ``` |

Modified [MLMediaSource.rootMediaGroup](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419255-rootmediagroup)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) MLMediaGroup *rootMediaGroup ``` |
| To | ``` @property(readonly, retain, nullable) MLMediaGroup *rootMediaGroup ``` |

#### MLMediaTypes.h

Added [MLPhotosFrontCameraGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosfrontcameragrouptypeidentifier)Added [MLPhotosScreenshotGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosscreenshotgrouptypeidentifier)

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
