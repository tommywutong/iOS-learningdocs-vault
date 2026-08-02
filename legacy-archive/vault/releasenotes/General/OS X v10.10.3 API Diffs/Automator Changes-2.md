---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/Automator.html
archived_at: '2026-07-18T02:52:06.780229Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Automator Changes

## Automator

Added NSObject.workflowController(AMWorkflowController!, didError: NSError!)Added NSObject.workflowController(AMWorkflowController!, didRunAction: AMAction!)Added NSObject.workflowController(AMWorkflowController!, willRunAction: AMAction!)Added NSObject.workflowControllerDidRun(AMWorkflowController!)Added NSObject.workflowControllerDidStop(AMWorkflowController!)Added NSObject.workflowControllerWillRun(AMWorkflowController!)Added NSObject.workflowControllerWillStop(AMWorkflowController!)Modified AMAction.closed()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AMAction.init(contentsOfURL: NSURL!, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(contentsOfURL fileURL: NSURL!, error outError: NSErrorPointer) ``` | OS X 10.10 |
| To | ``` init!(contentsOfURL fileURL: NSURL!, error outError: NSErrorPointer) ``` | OS X 10.5 |

Modified AMAction.init(definition: [NSObject: AnyObject]!, fromArchive: Bool)

|  | Declaration |
| --- | --- |
| From | ``` init(definition dict: [NSObject : AnyObject]!, fromArchive archived: Bool) ``` |
| To | ``` init!(definition dict: [NSObject : AnyObject]!, fromArchive archived: Bool) ``` |

Modified AMAction.finishRunningWithError(NSError!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AMAction.ignoresInput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AMAction.name

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AMAction.output

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AMAction.progressValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified AMAction.runAsynchronouslyWithInput(AnyObject!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AMAction.runWithInput(AnyObject!, error: NSErrorPointer) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AMAction.selectedInputType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified AMAction.selectedOutputType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified AMAction.willFinishRunning()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AMBundleAction.init(definition: [NSObject: AnyObject]!, fromArchive: Bool)

|  | Declaration |
| --- | --- |
| From | ``` init(definition dict: [NSObject : AnyObject]!, fromArchive archived: Bool) ``` |
| To | ``` init!(definition dict: [NSObject : AnyObject]!, fromArchive archived: Bool) ``` |

Modified AMWorkflow.init(contentsOfURL: NSURL!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL fileURL: NSURL!, error outError: NSErrorPointer) ``` |
| To | ``` init!(contentsOfURL fileURL: NSURL!, error outError: NSErrorPointer) ``` |

Modified AMWorkflow.fileURL

|  | Declaration |
| --- | --- |
| From | ``` var fileURL: NSURL! { get } ``` |
| To | ``` @NSCopying var fileURL: NSURL! { get } ``` |

Modified AMWorkflow.output

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified AMWorkflowController.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AnyObject! ``` |
| To | ``` unowned(unsafe) var delegate: AnyObject! ``` |

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
