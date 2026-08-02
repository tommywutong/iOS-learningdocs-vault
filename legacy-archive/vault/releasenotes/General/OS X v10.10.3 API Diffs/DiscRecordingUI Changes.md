---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/frameworks/DiscRecordingUI.html
archived_at: '2026-07-18T02:51:49.011455Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# DiscRecordingUI Changes

## DiscRecordingUI

DRBurnProgressPanel.hModified -[DRBurnProgressPanel stopBurn:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)stopBurn:(id)sender ``` |
| To | ``` - (IBAction)stopBurn:(id)sender ``` |

DRBurnSetupPanel.hModified -[DRBurnSetupPanel appendable:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)appendable:(id)sender ``` |
| To | ``` - (IBAction)appendable:(id)sender ``` |

Modified -[DRBurnSetupPanel burnSpeed:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)burnSpeed:(id)sender ``` |
| To | ``` - (IBAction)burnSpeed:(id)sender ``` |

Modified -[DRBurnSetupPanel completionAction:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)completionAction:(id)sender ``` |
| To | ``` - (IBAction)completionAction:(id)sender ``` |

Modified -[DRBurnSetupPanel expand:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)expand:(id)sender ``` |
| To | ``` - (IBAction)expand:(id)sender ``` |

Modified -[DRBurnSetupPanel testBurn:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)testBurn:(id)sender ``` |
| To | ``` - (IBAction)testBurn:(id)sender ``` |

Modified -[DRBurnSetupPanel verifyBurn:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)verifyBurn:(id)sender ``` |
| To | ``` - (IBAction)verifyBurn:(id)sender ``` |

DREraseSetupPanel.hModified -[DREraseSetupPanel eraseType:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)eraseType:(id)sender ``` |
| To | ``` - (IBAction)eraseType:(id)sender ``` |

DRSetupPanel.hModified -[DRSetupPanel cancel:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)cancel:(id)sender ``` |
| To | ``` - (IBAction)cancel:(id)sender ``` |

Modified -[DRSetupPanel close:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)close:(id)sender ``` |
| To | ``` - (IBAction)close:(id)sender ``` |

Modified -[DRSetupPanel eject:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)eject:(id)sender ``` |
| To | ``` - (IBAction)eject:(id)sender ``` |

Modified -[DRSetupPanel ok:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)ok:(id)sender ``` |
| To | ``` - (IBAction)ok:(id)sender ``` |

Modified -[DRSetupPanel open:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)open:(id)sender ``` |
| To | ``` - (IBAction)open:(id)sender ``` |

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
