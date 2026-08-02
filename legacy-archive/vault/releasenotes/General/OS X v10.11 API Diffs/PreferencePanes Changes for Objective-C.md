---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/PreferencePanes.html
archived_at: '2026-07-18T02:53:11.388390Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# PreferencePanes Changes for Objective-C

### PreferencePanes

#### NSPreferencePane.h

Modified NSPreferencePane.bundle

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSBundle *bundle ``` |
| To | ``` @property(readonly, strong, nonnull) NSBundle *bundle ``` |

Modified NSPreferencePane.firstKeyView

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSView *firstKeyView ``` |
| To | ``` @property(strong, nullable) NSView *firstKeyView ``` |

Modified NSPreferencePane.initialKeyView

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSView *initialKeyView ``` |
| To | ``` @property(strong, nullable) NSView *initialKeyView ``` |

Modified -[NSPreferencePane initWithBundle:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithBundle:(NSBundle *)bundle ``` |
| To | ``` - (instancetype _Nonnull)initWithBundle:(NSBundle * _Nonnull)bundle ``` |

Modified NSPreferencePane.lastKeyView

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSView *lastKeyView ``` |
| To | ``` @property(strong, nullable) NSView *lastKeyView ``` |

Modified -[NSPreferencePane loadMainView]

|  | Declaration |
| --- | --- |
| From | ``` - (NSView *)loadMainView ``` |
| To | ``` - (NSView * _Nonnull)loadMainView ``` |

Modified NSPreferencePane.mainNibName

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSString *mainNibName ``` |
| To | ``` @property(readonly, strong, nonnull) NSString *mainNibName ``` |

Modified NSPreferencePane.mainView

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSView *mainView ``` |
| To | ``` @property(strong, nonnull) NSView *mainView ``` |

Modified -[NSPreferencePane updateHelpMenuWithArray:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)updateHelpMenuWithArray:(NSArray *)inArrayOfMenuItems ``` |
| To | ``` - (void)updateHelpMenuWithArray:(NSArray<NSDictionary<NSString *,NSString *> *> * _Nullable)inArrayOfMenuItems ``` |

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
