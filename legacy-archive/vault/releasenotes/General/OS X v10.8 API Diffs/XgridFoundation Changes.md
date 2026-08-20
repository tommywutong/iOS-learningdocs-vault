---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/XgridFoundation.html
archived_at: '2026-07-18T02:54:07.060606Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# XgridFoundation Changes

## XgridFoundation

XGActionMonitor.hRemoved XGActionMonitorRemoved -[XGActionMonitor action]Removed -[XGActionMonitor actionDidFail]Removed -[XGActionMonitor actionDidSucceed]Removed +[XGActionMonitor actionMonitorWithResource:action:]Removed +[XGActionMonitor actionMonitorWithResource:action:parameters:]Removed -[XGActionMonitor error]Removed -[XGActionMonitor initWithResource:action:parameters:]Removed -[XGActionMonitor outcome]Removed -[XGActionMonitor parameters]Removed -[XGActionMonitor performAction]Removed -[XGActionMonitor resource]Removed -[XGActionMonitor results]Removed XGActionMonitorOutcomeRemoved XGActionMonitorOutcomeFailureRemoved XGActionMonitorOutcomeNoneRemoved XGActionMonitorOutcomeSuccessRemoved XGActionMonitorResultsOutputFilesKeyRemoved XGActionMonitorResultsOutputStreamsKeyRemoved XGResourceActionRemoved XGResourceActionDeleteRemoved XGResourceActionGetOutputFilesRemoved XGResourceActionGetOutputStreamsRemoved XGResourceActionGetSpecificationRemoved XGResourceActionMakeDefaultRemoved XGResourceActionNoneRemoved XGResourceActionRenameRemoved XGResourceActionRestartRemoved XGResourceActionResumeRemoved XGResourceActionStopRemoved XGResourceActionSubmitJobRemoved XGResourceActionSuspendXGAuthenticator.hRemoved -[NSObject authenticatorDidAuthenticate:]Removed -[NSObject authenticatorDidNotAuthenticate:]Removed XGAuthenticatorRemoved -[XGAuthenticator beginAuthentication:]Removed -[XGAuthenticator delegate]Removed -[XGAuthenticator error]Removed -[XGAuthenticator failWithError:]Removed -[XGAuthenticator finishAuthentication]Removed -[XGAuthenticator piggyback]Removed +[XGAuthenticator profileURI]Removed -[XGAuthenticator receiveData:]Removed -[XGAuthenticator sendData:]Removed -[XGAuthenticator setDelegate:]Removed -[XGAuthenticator state]Removed NSObject(XGAuthenticatorDelegate)Removed XGAuthenticatorStateRemoved XGAuthenticatorStateAuthenticatedRemoved XGAuthenticatorStateAuthenticatingRemoved XGAuthenticatorStateFailedRemoved XGAuthenticatorStateUnauthenticatedXGConnection.hRemoved -[NSObject connectionDidClose:]Removed -[NSObject connectionDidNotOpen:withError:]Removed -[NSObject connectionDidOpen:]Removed XGConnectionRemoved -[XGConnection authenticator]Removed -[XGConnection close]Removed -[XGConnection delegate]Removed -[XGConnection error]Removed -[XGConnection hostname]Removed -[XGConnection initWithHostname:portnumber:]Removed -[XGConnection initWithNetService:]Removed -[XGConnection isClosed]Removed -[XGConnection isOpened]Removed -[XGConnection name]Removed -[XGConnection netService]Removed -[XGConnection open]Removed -[XGConnection portnumber]Removed -[XGConnection servicePrincipal]Removed -[XGConnection setAuthenticator:]Removed -[XGConnection setDelegate:]Removed -[XGConnection state]Removed NSObject(XGConnectionDelegate)Removed XGConnectionKeyIsClosedRemoved XGConnectionKeyIsOpenedRemoved XGConnectionKeyStateRemoved XGConnectionStateRemoved XGConnectionStateClosedRemoved XGConnectionStateClosingRemoved XGConnectionStateOpenRemoved XGConnectionStateOpeningXGController.hRemoved XGControllerRemoved +[XGController controllerWithHostname:portnumber:]Removed +[XGController controllerWithNetService:]Removed +[XGController defaultController]Removed -[XGController defaultGrid]Removed -[XGController gridForIdentifier:]Removed -[XGController grids]Removed -[XGController initWithConnection:]Removed -[XGController jobsPredicateString]Removed -[XGController performSubmitJobActionWithJobSpecification:gridIdentifier:]Removed +[XGController privateController]Removed -[XGController setJobsPredicateString:]Removed XGController(XGControllerCreation)Removed XGControllerWillDeallocNotificationXGFile.hRemoved XGFileRemoved -[XGFile job]Removed -[XGFile path]Removed -[XGFile taskIdentifier]Removed -[XGFile type]Removed XGFileStandardErrorPathRemoved XGFileStandardOutputPathRemoved XGFileTypeRemoved XGFileTypeNoneRemoved XGFileTypeRegularRemoved XGFileTypeStreamXGFileDownload.hRemoved -[NSObject fileDownload:decideDestinationWithSuggestedPath:]Removed -[NSObject fileDownload:didCreateDestination:]Removed -[NSObject fileDownload:didFailWithError:]Removed -[NSObject fileDownload:didReceiveAttributes:]Removed -[NSObject fileDownload:didReceiveData:]Removed -[NSObject fileDownloadDidBegin:]Removed -[NSObject fileDownloadDidFinish:]Removed XGFileDownloadRemoved -[XGFileDownload cancel]Removed -[XGFileDownload delegate]Removed -[XGFileDownload destination]Removed -[XGFileDownload file]Removed -[XGFileDownload initWithFile:delegate:]Removed -[XGFileDownload setDestination:allowOverwrite:]Removed NSObject(XGFileDownloadDelegate)XGGSSAuthenticator.hRemoved XGGSSAuthenticatorRemoved -[XGGSSAuthenticator servicePrincipal]Removed -[XGGSSAuthenticator setServicePrincipal:]XGGrid.hRemoved XGGridRemoved -[XGGrid isDefault]Removed -[XGGrid jobForIdentifier:]Removed -[XGGrid jobs]Removed -[XGGrid name]XGJob.hRemoved XGJobRemoved -[XGJob activeCPUPower]Removed -[XGJob applicationIdentifier]Removed -[XGJob applicationInfo]Removed -[XGJob completedTaskCount]Removed -[XGJob dateStarted]Removed -[XGJob dateStopped]Removed -[XGJob dateSubmitted]Removed -[XGJob name]Removed -[XGJob percentDone]Removed -[XGJob performDeleteAction]Removed -[XGJob performGetOutputFilesAction]Removed -[XGJob performGetOutputStreamsAction]Removed -[XGJob performGetSpecificationAction]Removed -[XGJob performRestartAction]Removed -[XGJob performResumeAction]Removed -[XGJob performStopAction]Removed -[XGJob performSuspendAction]Removed -[XGJob taskCount]Removed XGJobSpecificationARTConditionsKeyRemoved XGJobSpecificationARTDataKeyRemoved XGJobSpecificationARTEqualKeyRemoved XGJobSpecificationARTMaximumKeyRemoved XGJobSpecificationARTMinimumKeyRemoved XGJobSpecificationARTSpecificationsKeyRemoved XGJobSpecificationApplicationIdentifierKeyRemoved XGJobSpecificationArgumentTypeKeyRemoved XGJobSpecificationArgumentsKeyRemoved XGJobSpecificationCommandKeyRemoved XGJobSpecificationDependsOnJobsKeyRemoved XGJobSpecificationDependsOnTasksKeyRemoved XGJobSpecificationEnvironmentKeyRemoved XGJobSpecificationFileDataKeyRemoved XGJobSpecificationGridIdentifierKeyRemoved XGJobSpecificationInputFileMapKeyRemoved XGJobSpecificationInputFilesKeyRemoved XGJobSpecificationInputStreamKeyRemoved XGJobSpecificationIsExecutableKeyRemoved XGJobSpecificationNameKeyRemoved XGJobSpecificationNotificationEmailKeyRemoved XGJobSpecificationPathIdentifierKeyRemoved XGJobSpecificationSchedulerHintsKeyRemoved XGJobSpecificationSchedulerParametersKeyRemoved XGJobSpecificationSubmissionIdentifierKeyRemoved XGJobSpecificationTaskPrototypeIdentifierKeyRemoved XGJobSpecificationTaskPrototypesKeyRemoved XGJobSpecificationTaskSpecificationsKeyRemoved XGJobSpecificationTypeKeyRemoved XGJobSpecificationTypeTaskListValueXGResource.hRemoved XGResourceRemoved -[XGResource actionMonitors]Removed -[XGResource connection]Removed -[XGResource controller]Removed -[XGResource identifier]Removed -[XGResource isUpdated]Removed -[XGResource isUpdating]Removed -[XGResource performAction:withParameters:]Removed -[XGResource state]Removed XGResourceStateRemoved XGResourceStateAvailableRemoved XGResourceStateCanceledRemoved XGResourceStateConnectingRemoved XGResourceStateFailedRemoved XGResourceStateFinishedRemoved XGResourceStateOfflineRemoved XGResourceStatePendingRemoved XGResourceStateRunningRemoved XGResourceStateStagingInRemoved XGResourceStateStagingOutRemoved XGResourceStateStartingRemoved XGResourceStateSuspendedRemoved XGResourceStateUnavailableRemoved XGResourceStateUninitializedRemoved XGResourceStateWorkingXGTwoWayRandomAuthenticator.hRemoved XGTwoWayRandomAuthenticatorRemoved -[XGTwoWayRandomAuthenticator setPassword:]Removed -[XGTwoWayRandomAuthenticator setUsername:]Removed -[XGTwoWayRandomAuthenticator username]

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
