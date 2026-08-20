---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/InstallerPlugins.html
archived_at: '2026-07-15T07:34:46.327390Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# InstallerPlugins Changes

## InstallerPlugins

InstallerPane.hRemoved -[InstallerPane gotoNextPane]Removed -[InstallerPane gotoPreviousPane]Removed -[InstallerPane nextEnabled]Removed -[InstallerPane previousEnabled]Removed -[InstallerPane section]Removed -[InstallerPane setNextEnabled:]Removed -[InstallerPane setPreviousEnabled:]Removed -[InstallerPane title]Added InstallerPane.gotoNextPaneAdded InstallerPane.gotoPreviousPaneAdded InstallerPane.nextEnabledAdded InstallerPane.previousEnabledAdded InstallerPane.sectionAdded InstallerPane.titleModified InstallerPane.contentView

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSView *contentView ``` |
| To | ``` @property(nonatomic, retain) IBOutlet NSView *contentView ``` |

Modified InstallerPane.firstKeyView

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSView *firstKeyView ``` |
| To | ``` @property(nonatomic, retain) IBOutlet NSView *firstKeyView ``` |

Modified -[InstallerPane initWithSection:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSection:(id)parent ``` |
| To | ``` - (instancetype)initWithSection:(id)parent ``` |

Modified InstallerPane.initialKeyView

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSView *initialKeyView ``` |
| To | ``` @property(nonatomic, retain) IBOutlet NSView *initialKeyView ``` |

Modified InstallerPane.lastKeyView

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSView *lastKeyView ``` |
| To | ``` @property(nonatomic, retain) IBOutlet NSView *lastKeyView ``` |

Modified InstallerPane.nextPane

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) InstallerPane *nextPane ``` |
| To | ``` @property(nonatomic, retain) IBOutlet InstallerPane *nextPane ``` |

InstallerSection.hRemoved -[InstallerSection activePane]Removed -[InstallerSection bundle]Removed -[InstallerSection firstPane]Removed -[InstallerSection installerState]Removed -[InstallerSection shouldLoad]Removed -[InstallerSection title]Added InstallerSection.activePaneAdded InstallerSection.bundleAdded InstallerSection.firstPaneAdded InstallerSection.installerStateAdded InstallerSection.shouldLoadAdded InstallerSection.titleInstallerState.hRemoved -[InstallerState choiceDictionaries]Removed -[InstallerState installStarted]Removed -[InstallerState installSucceeded]Removed -[InstallerState licenseAgreed]Removed -[InstallerState licenseAgreedLanguage]Removed -[InstallerState targetPath]Removed -[InstallerState targetVolumePath]Added InstallerState.choiceDictionariesAdded InstallerState.installStartedAdded InstallerState.installSucceededAdded InstallerState.licenseAgreedAdded InstallerState.licenseAgreedLanguageAdded InstallerState.targetPathAdded InstallerState.targetVolumePath

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
