---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/Automator.html
archived_at: '2026-07-15T07:34:50.134936Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# Automator Changes

## Automator (Added)

Added AMActionAdded AMAction.activated()Added AMAction.closed()Added AMAction.init(contentsOfURL: NSURL!, error: NSErrorPointer)Added AMAction.init(definition: [NSObject: AnyObject]!, fromArchive: Bool)Added AMAction.finishRunningWithError(NSError!)Added AMAction.ignoresInputAdded AMAction.nameAdded AMAction.opened()Added AMAction.outputAdded AMAction.parametersUpdated()Added AMAction.progressValueAdded AMAction.reset()Added AMAction.runAsynchronouslyWithInput(AnyObject!)Added AMAction.runWithInput(AnyObject!, error: NSErrorPointer) -> AnyObject!Added AMAction.selectedInputTypeAdded AMAction.selectedOutputTypeAdded AMAction.stop()Added AMAction.stoppedAdded AMAction.updateParameters()Added AMAction.willFinishRunning()Added AMAction.writeToDictionary(NSMutableDictionary!)Added AMAppleScriptActionAdded AMAppleScriptAction.scriptAdded AMBundleActionAdded AMBundleAction.awakeFromBundle()Added AMBundleAction.bundleAdded AMBundleAction.init(definition: [NSObject: AnyObject]!, fromArchive: Bool)Added AMBundleAction.hasViewAdded AMBundleAction.parametersAdded AMBundleAction.viewAdded AMLogLevel [enum]Added AMLogLevel.DebugAdded AMLogLevel.ErrorAdded AMLogLevel.InfoAdded AMLogLevel.WarnAdded AMShellScriptActionAdded AMShellScriptAction.inputFieldSeparator() -> String!Added AMShellScriptAction.outputFieldSeparator() -> String!Added AMShellScriptAction.remapLineEndings() -> BoolAdded AMWorkflowAdded AMWorkflow.actionsAdded AMWorkflow.addAction(AMAction!)Added AMWorkflow.init(contentsOfURL: NSURL!, error: NSErrorPointer)Added AMWorkflow.fileURLAdded AMWorkflow.inputAdded AMWorkflow.insertAction(AMAction!, atIndex: Int)Added AMWorkflow.moveActionAtIndex(Int, toIndex: Int)Added AMWorkflow.outputAdded AMWorkflow.removeAction(AMAction!)Added AMWorkflow.runWorkflowAtURL(NSURL!, withInput: AnyObject!, error: NSErrorPointer) -> AnyObject! [class]Added AMWorkflow.setValue(AnyObject!, forVariableWithName: String!) -> BoolAdded AMWorkflow.valueForVariableWithName(String!) -> AnyObject!Added AMWorkflow.writeToURL(NSURL!, error: NSErrorPointer) -> BoolAdded AMWorkflowControllerAdded AMWorkflowController.canRunAdded AMWorkflowController.delegateAdded AMWorkflowController.pause(AnyObject!)Added AMWorkflowController.pausedAdded AMWorkflowController.reset(AnyObject!)Added AMWorkflowController.run(AnyObject!)Added AMWorkflowController.runningAdded AMWorkflowController.step(AnyObject!)Added AMWorkflowController.stop(AnyObject!)Added AMWorkflowController.workflowAdded AMWorkflowController.workflowViewAdded AMWorkflowViewAdded AMWorkflowView.editableAdded AMWorkflowView.workflowControllerAdded NSObject.workflowController(AMWorkflowController!, didError: NSError!)Added NSObject.workflowController(AMWorkflowController!, didRunAction: AMAction!)Added NSObject.workflowController(AMWorkflowController!, willRunAction: AMAction!)Added NSObject.workflowControllerDidRun(AMWorkflowController!)Added NSObject.workflowControllerDidStop(AMWorkflowController!)Added NSObject.workflowControllerWillRun(AMWorkflowController!)Added NSObject.workflowControllerWillStop(AMWorkflowController!)Added AMActionApplicationResourceErrorAdded AMActionApplicationVersionResourceErrorAdded AMActionArchitectureMismatchErrorAdded AMActionErrorKeyAdded AMActionExceptionErrorAdded AMActionExecutionErrorAdded AMActionFailedGatekeeperErrorAdded AMActionFileResourceErrorAdded AMActionInitializationErrorAdded AMActionInsufficientDataErrorAdded AMActionIsDeprecatedErrorAdded AMActionLicenseResourceErrorAdded AMActionLinkErrorAdded AMActionLoadErrorAdded AMActionMalwareErrorAdded AMActionNotLoadableErrorAdded AMActionPropertyListInvalidErrorAdded AMActionQuarantineErrorAdded AMActionRequiredActionResourceErrorAdded AMActionRuntimeMismatchErrorAdded AMActionSignatureCorruptErrorAdded AMActionXProtectErrorAdded AMAutomatorErrorDomainAdded AMConversionFailedErrorAdded AMConversionNoDataErrorAdded AMConversionNotPossibleErrorAdded AMNoSuchActionErrorAdded AMUserCanceledErrorAdded AMWorkflowNewerActionVersionErrorAdded AMWorkflowNewerVersionErrorAdded AMWorkflowOlderActionVersionErrorAdded AMWorkflowPropertyListInvalidError

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
