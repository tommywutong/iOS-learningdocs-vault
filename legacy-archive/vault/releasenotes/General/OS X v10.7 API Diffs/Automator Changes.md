---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/Automator.html
archived_at: '2026-07-18T02:54:26.325705Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# Automator Changes

## Automator

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

AMAction.hAdded [-[AMAction finishRunningWithError:]](https://developer.apple.com/documentation/automator/amaction/1419677-finishrunningwitherror)Added [-[AMAction isStopped]](https://developer.apple.com/documentation/automator/amaction/1419600-stopped)Added [-[AMAction logMessageWithLevel:format:]](https://developer.apple.com/documentation/automator/amaction/1438359-logmessagewithlevel)Added [-[AMAction runWithInput:error:]](https://developer.apple.com/documentation/automator/amaction/1419624-run)Added [AMLogLevel](https://developer.apple.com/documentation/automator/amloglevel)Added [AMLogLevelDebug](https://developer.apple.com/documentation/automator/amloglevel/debug)Added [AMLogLevelError](https://developer.apple.com/documentation/automator/amloglevel/error)Added [AMLogLevelInfo](https://developer.apple.com/documentation/automator/amloglevel/info)Added [AMLogLevelWarn](https://developer.apple.com/documentation/automator/amloglevel/amloglevelwarn)Modified [-[AMAction didFinishRunningWithError:]](https://developer.apple.com/documentation/automator/amaction/1438357-didfinishrunningwitherror)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.5 |

Modified [-[AMAction runWithInput:fromAction:error:]](https://developer.apple.com/documentation/automator/amaction/1438363-runwithinput)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.4 |

AMAttributesForAnalyzer.hAdded #def AM_RETURNS_NONRETAINED_FOR_ANALYZERAdded #def AM_RETURNS_RETAINED_FOR_ANALYZERAdded #def AM_UNUSED_FOR_ANALYZERAMWorkflow.hRemoved [-[AMWorkflow actions]](https://developer.apple.com/documentation/automator/amworkflow/1419646-actions)Removed [-[AMWorkflow fileURL]](https://developer.apple.com/documentation/automator/amworkflow/1419726-fileurl)Removed [-[AMWorkflow input]](https://developer.apple.com/documentation/automator/amworkflow/1419587-input)Removed [-[AMWorkflow output]](https://developer.apple.com/documentation/automator/amworkflow/1419626-output)Removed [-[AMWorkflow setInput:]](https://developer.apple.com/documentation/automator/amworkflow/1419587-input)Added [AMWorkflow.actions](https://developer.apple.com/documentation/automator/amworkflow/1419646-actions)Added [AMWorkflow.fileURL](https://developer.apple.com/documentation/automator/amworkflow/1419726-fileurl)Added [AMWorkflow.input](https://developer.apple.com/documentation/automator/amworkflow/1419587-input)Added [AMWorkflow.output](https://developer.apple.com/documentation/automator/amworkflow/1419626-output)AMWorkflowController.hAdded [-[AMWorkflowController isPaused]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419746-paused)Added [-[AMWorkflowController pause:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419659-pause)Added [-[AMWorkflowController reset:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419748-reset)Added [-[AMWorkflowController step:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419740-step)

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
