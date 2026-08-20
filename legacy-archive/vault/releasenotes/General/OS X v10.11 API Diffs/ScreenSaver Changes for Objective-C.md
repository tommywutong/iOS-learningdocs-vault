---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/ScreenSaver.html
archived_at: '2026-07-18T02:53:13.009085Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# ScreenSaver Changes for Objective-C

### ScreenSaver

#### ScreenSaverDefaults.h

Modified [+[ScreenSaverDefaults defaultsForModuleWithName:]](https://developer.apple.com/documentation/screensaver/screensaverdefaults/1512473-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)defaultsForModuleWithName:(NSString *)inModuleName ``` |
| To | ``` + (instancetype _Nullable)defaultsForModuleWithName:(NSString * _Nonnull)inModuleName ``` |

#### ScreenSaverView.h

Removed -[ScreenSaverView isAnimating]Removed -[ScreenSaverView isPreview]Removed [-[ScreenSaverView setAnimationTimeInterval:]](https://developer.apple.com/documentation/screensaver/screensaverview/1512484-animationtimeinterval)Added [ScreenSaverView.animating](https://developer.apple.com/documentation/screensaver/screensaverview/1512467-animating)Added [ScreenSaverView.preview](https://developer.apple.com/documentation/screensaver/screensaverview/1512504-preview)Modified [ScreenSaverView.animationTimeInterval](https://developer.apple.com/documentation/screensaver/screensaverview/1512484-animationtimeinterval)

|  | Declaration |
| --- | --- |
| From | ``` - (NSTimeInterval)animationTimeInterval ``` |
| To | ``` @property(atomic) NSTimeInterval animationTimeInterval ``` |

Modified [-[ScreenSaverView configureSheet]](https://developer.apple.com/documentation/screensaver/screensaverview/1512486-configuresheet)

|  | Declaration |
| --- | --- |
| From | ``` - (NSWindow *)configureSheet ``` |
| To | ``` - (NSWindow * _Nullable)configureSheet ``` |

Modified -[ScreenSaverView initWithFrame:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(NSRect)frame ``` |
| To | ``` - (instancetype _Nullable)initWithFrame:(NSRect)frame ``` |

Modified [-[ScreenSaverView initWithFrame:isPreview:]](https://developer.apple.com/documentation/screensaver/screensaverview/1512475-initwithframe)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithFrame:(NSRect)frame isPreview:(BOOL)isPreview ``` | -- |
| To | ``` - (instancetype _Nullable)initWithFrame:(NSRect)frame isPreview:(BOOL)isPreview ``` | yes |

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
