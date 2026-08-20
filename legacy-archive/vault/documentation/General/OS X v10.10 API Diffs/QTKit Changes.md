---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/QTKit.html
archived_at: '2026-07-15T07:34:47.096143Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# QTKit Changes

## QTKit

QTExportSession.hModified -[QTExportSessionDelegate exportSession:didFailWithError:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[QTExportSessionDelegate exportSession:didReachProgress:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[QTExportSessionDelegate exportSessionDidSucceed:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[QTExportSessionDelegate exportSessionWasCancelled:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

QTMovieView.hModified -[QTMovieView add:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)add:(id)sender ``` |
| To | ``` - (IBAction)add:(id)sender ``` |

Modified -[QTMovieView addScaled:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)addScaled:(id)sender ``` |
| To | ``` - (IBAction)addScaled:(id)sender ``` |

Modified -[QTMovieView copy:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)copy:(id)sender ``` |
| To | ``` - (IBAction)copy:(id)sender ``` |

Modified -[QTMovieView cut:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)cut:(id)sender ``` |
| To | ``` - (IBAction)cut:(id)sender ``` |

Modified -[QTMovieView delete:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)delete:(id)sender ``` |
| To | ``` - (IBAction)delete:(id)sender ``` |

Modified -[QTMovieView gotoBeginning:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)gotoBeginning:(id)sender ``` |
| To | ``` - (IBAction)gotoBeginning:(id)sender ``` |

Modified -[QTMovieView gotoEnd:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)gotoEnd:(id)sender ``` |
| To | ``` - (IBAction)gotoEnd:(id)sender ``` |

Modified -[QTMovieView gotoNextSelectionPoint:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)gotoNextSelectionPoint:(id)sender ``` |
| To | ``` - (IBAction)gotoNextSelectionPoint:(id)sender ``` |

Modified -[QTMovieView gotoPosterFrame:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)gotoPosterFrame:(id)sender ``` |
| To | ``` - (IBAction)gotoPosterFrame:(id)sender ``` |

Modified -[QTMovieView gotoPreviousSelectionPoint:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)gotoPreviousSelectionPoint:(id)sender ``` |
| To | ``` - (IBAction)gotoPreviousSelectionPoint:(id)sender ``` |

Modified -[QTMovieView paste:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)paste:(id)sender ``` |
| To | ``` - (IBAction)paste:(id)sender ``` |

Modified -[QTMovieView pause:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)pause:(id)sender ``` |
| To | ``` - (IBAction)pause:(id)sender ``` |

Modified -[QTMovieView play:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)play:(id)sender ``` |
| To | ``` - (IBAction)play:(id)sender ``` |

Modified -[QTMovieView replace:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)replace:(id)sender ``` |
| To | ``` - (IBAction)replace:(id)sender ``` |

Modified -[QTMovieView selectAll:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectAll:(id)sender ``` |
| To | ``` - (IBAction)selectAll:(id)sender ``` |

Modified -[QTMovieView selectNone:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectNone:(id)sender ``` |
| To | ``` - (IBAction)selectNone:(id)sender ``` |

Modified -[QTMovieView stepBackward:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)stepBackward:(id)sender ``` |
| To | ``` - (IBAction)stepBackward:(id)sender ``` |

Modified -[QTMovieView stepForward:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)stepForward:(id)sender ``` |
| To | ``` - (IBAction)stepForward:(id)sender ``` |

Modified -[QTMovieView trim:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)trim:(id)sender ``` |
| To | ``` - (IBAction)trim:(id)sender ``` |

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
