---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/Automator.html
archived_at: '2026-07-15T07:34:44.855421Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# Automator Changes

## Automator

AMAction.hRemoved [-[AMAction ignoresInput]](https://developer.apple.com/documentation/automator/amaction/1419752-ignoresinput)Removed [-[AMAction isStopped]](https://developer.apple.com/documentation/automator/amaction/1419600-stopped)Removed [-[AMAction name]](https://developer.apple.com/documentation/automator/amaction/1419648-name)Removed [-[AMAction output]](https://developer.apple.com/documentation/automator/amaction/1419786-output)Removed [-[AMAction progressValue]](https://developer.apple.com/documentation/automator/amaction/1419710-progressvalue)Removed [-[AMAction selectedInputType]](https://developer.apple.com/documentation/automator/amaction/1419756-selectedinputtype)Removed [-[AMAction selectedOutputType]](https://developer.apple.com/documentation/automator/amaction/1419661-selectedoutputtype)Removed [-[AMAction setOutput:]](https://developer.apple.com/documentation/automator/amaction/1419786-output)Removed [-[AMAction setProgressValue:]](https://developer.apple.com/documentation/automator/amaction/1419710-progressvalue)Removed [-[AMAction setSelectedInputType:]](https://developer.apple.com/documentation/automator/amaction/1419756-selectedinputtype)Removed [-[AMAction setSelectedOutputType:]](https://developer.apple.com/documentation/automator/amaction/1419661-selectedoutputtype)Added [AMAction.ignoresInput](https://developer.apple.com/documentation/automator/amaction/1419752-ignoresinput)Added [AMAction.name](https://developer.apple.com/documentation/automator/amaction/1419648-name)Added [AMAction.output](https://developer.apple.com/documentation/automator/amaction/1419786-output)Added [AMAction.progressValue](https://developer.apple.com/documentation/automator/amaction/1419710-progressvalue)Added [AMAction.selectedInputType](https://developer.apple.com/documentation/automator/amaction/1419756-selectedinputtype)Added [AMAction.selectedOutputType](https://developer.apple.com/documentation/automator/amaction/1419661-selectedoutputtype)Added [AMAction.stopped](https://developer.apple.com/documentation/automator/amaction/1419600-isstopped)Modified [-[AMAction initWithContentsOfURL:error:]](https://developer.apple.com/documentation/automator/amaction/1419742-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)fileURL error:(NSError **)outError ``` |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)fileURL error:(NSError **)outError ``` |

Modified [-[AMAction initWithDefinition:fromArchive:]](https://developer.apple.com/documentation/automator/amaction/1419574-initwithdefinition)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDefinition:(NSDictionary *)dict fromArchive:(BOOL)archived ``` |
| To | ``` - (instancetype)initWithDefinition:(NSDictionary *)dict fromArchive:(BOOL)archived ``` |

AMAppleScriptAction.hRemoved [-[AMAppleScriptAction script]](https://developer.apple.com/documentation/automator/amapplescriptaction/1419700-script)Removed -[AMAppleScriptAction setScript:]Added [AMAppleScriptAction.script](https://developer.apple.com/documentation/automator/amapplescriptaction/1419700-script)AMBundleAction.hRemoved [-[AMBundleAction bundle]](https://developer.apple.com/documentation/automator/ambundleaction/1419572-bundle)Removed [-[AMBundleAction hasView]](https://developer.apple.com/documentation/automator/ambundleaction/1419792-hasview)Removed [-[AMBundleAction parameters]](https://developer.apple.com/documentation/automator/ambundleaction/1419634-parameters)Removed [-[AMBundleAction setParameters:]](https://developer.apple.com/documentation/automator/ambundleaction/1419634-parameters)Removed [-[AMBundleAction view]](https://developer.apple.com/documentation/automator/ambundleaction/1419665-view)Added [AMBundleAction.bundle](https://developer.apple.com/documentation/automator/ambundleaction/1419572-bundle)Added [AMBundleAction.hasView](https://developer.apple.com/documentation/automator/ambundleaction/1419792-hasview)Added [AMBundleAction.parameters](https://developer.apple.com/documentation/automator/ambundleaction/1419634-parameters)Added [AMBundleAction.view](https://developer.apple.com/documentation/automator/ambundleaction/1419665-view)Modified [-[AMBundleAction initWithDefinition:fromArchive:]](https://developer.apple.com/documentation/automator/ambundleaction/1807582-initwithdefinition)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDefinition:(NSDictionary *)dict fromArchive:(BOOL)archived ``` |
| To | ``` - (instancetype)initWithDefinition:(NSDictionary *)dict fromArchive:(BOOL)archived ``` |

AMWorkflow.hModified [-[AMWorkflow initWithContentsOfURL:error:]](https://developer.apple.com/documentation/automator/amworkflow/1419774-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)fileURL error:(NSError **)outError ``` |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)fileURL error:(NSError **)outError ``` |

AMWorkflowController.hRemoved [-[AMWorkflowController canRun]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419679-canrun)Removed [-[AMWorkflowController delegate]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419724-delegate)Removed [-[AMWorkflowController isPaused]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419746-paused)Removed [-[AMWorkflowController isRunning]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419694-running)Removed [-[AMWorkflowController setDelegate:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419724-delegate)Removed [-[AMWorkflowController setWorkflow:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419620-workflow)Removed [-[AMWorkflowController setWorkflowView:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419614-workflowview)Removed [-[AMWorkflowController workflow]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419620-workflow)Removed [-[AMWorkflowController workflowView]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419614-workflowview)Added [AMWorkflowController.canRun](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419679-canrun)Added [AMWorkflowController.delegate](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419724-delegate)Added [AMWorkflowController.paused](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419746-paused)Added [AMWorkflowController.running](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419694-isrunning)Added [AMWorkflowController.workflow](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419620-workflow)Added [AMWorkflowController.workflowView](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419614-workflowview)Modified [-[AMWorkflowController pause:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419659-pause)

|  | Declaration |
| --- | --- |
| From | ``` - (void)pause:(id)sender ``` |
| To | ``` - (IBAction)pause:(id)sender ``` |

Modified [-[AMWorkflowController reset:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419748-reset)

|  | Declaration |
| --- | --- |
| From | ``` - (void)reset:(id)sender ``` |
| To | ``` - (IBAction)reset:(id)sender ``` |

Modified [-[AMWorkflowController run:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419780-run)

|  | Declaration |
| --- | --- |
| From | ``` - (void)run:(id)sender ``` |
| To | ``` - (IBAction)run:(id)sender ``` |

Modified [-[AMWorkflowController step:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419740-step)

|  | Declaration |
| --- | --- |
| From | ``` - (void)step:(id)sender ``` |
| To | ``` - (IBAction)step:(id)sender ``` |

Modified [-[AMWorkflowController stop:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419712-stop)

|  | Declaration |
| --- | --- |
| From | ``` - (void)stop:(id)sender ``` |
| To | ``` - (IBAction)stop:(id)sender ``` |

AMWorkflowView.hRemoved [-[AMWorkflowView isEditable]](https://developer.apple.com/documentation/automator/amworkflowview/1419702-editable)Removed [-[AMWorkflowView setEditable:]](https://developer.apple.com/documentation/automator/amworkflowview/1419702-editable)Removed [-[AMWorkflowView setWorkflowController:]](https://developer.apple.com/documentation/automator/amworkflowview/1419790-workflowcontroller)Removed [-[AMWorkflowView workflowController]](https://developer.apple.com/documentation/automator/amworkflowview/1419790-workflowcontroller)Added [AMWorkflowView.editable](https://developer.apple.com/documentation/automator/amworkflowview/1419702-editable)Added [AMWorkflowView.workflowController](https://developer.apple.com/documentation/automator/amworkflowview/1419790-workflowcontroller)AutomatorErrors.hAdded [AMActionFailedGatekeeperError](https://developer.apple.com/documentation/automator/amerror/code/actionfailedgatekeepererror)Added [AMActionMalwareError](https://developer.apple.com/documentation/automator/amerror/code/actionmalwareerror)Added [AMActionQuarantineError](https://developer.apple.com/documentation/automator/amerrorcode/amactionquarantineerror)Added [AMActionSignatureCorruptError](https://developer.apple.com/documentation/automator/amerror/code/actionsignaturecorrupterror)Added [AMActionXProtectError](https://developer.apple.com/documentation/automator/amerror/code/actionxprotecterror)

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
