---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/CallKit.html
archived_at: '2026-07-18T02:54:53.756936Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# CallKit Changes for Objective-C

### CallKit (Added)

#### CXAction.h (Added)

Added [CXAction](https://developer.apple.com/documentation/callkit/cxaction)Added [CXAction.complete](https://developer.apple.com/documentation/callkit/cxaction/1649007-complete)Added [-[CXAction fail]](https://developer.apple.com/documentation/callkit/cxaction/1930708-fail)Added [-[CXAction fulfill]](https://developer.apple.com/documentation/callkit/cxaction/1648982-fulfill)Added [-[CXAction init]](https://developer.apple.com/documentation/callkit/cxaction/1648990-init)Added [-[CXAction initWithCoder:]](https://developer.apple.com/documentation/callkit/cxaction/1648978-init)Added [CXAction.timeoutDate](https://developer.apple.com/documentation/callkit/cxaction/1771728-timeoutdate)Added [CXAction.UUID](https://developer.apple.com/documentation/callkit/cxaction/1648989-uuid)

#### CXAnswerCallAction.h (Added)

Added [CXAnswerCallAction](https://developer.apple.com/documentation/callkit/cxanswercallaction)Added [-[CXAnswerCallAction fulfillWithDateConnected:]](https://developer.apple.com/documentation/callkit/cxanswercallaction/1771456-fulfillwithdateconnected)

#### CXBase.h (Added)

Added #def CX_CLASS_AVAILABLEAdded #def CX_EXTERNAdded #def CXBundleIdentifierAdded #def CXBundleIdentifierLowercase

#### CXCall.h (Added)

Added [CXCall](https://developer.apple.com/documentation/callkit/cxcall)Added [CXCall.hasConnected](https://developer.apple.com/documentation/callkit/cxcall/1649013-hasconnected)Added [CXCall.hasEnded](https://developer.apple.com/documentation/callkit/cxcall/1648977-hasended)Added [-[CXCall isEqualToCall:]](https://developer.apple.com/documentation/callkit/cxcall/2102240-isequaltocall)Added [CXCall.onHold](https://developer.apple.com/documentation/callkit/cxcall/1648996-onhold)Added [CXCall.outgoing](https://developer.apple.com/documentation/callkit/cxcall/1648994-isoutgoing)Added [CXCall.UUID](https://developer.apple.com/documentation/callkit/cxcall/1648975-uuid)

#### CXCallAction.h (Added)

Added [CXCallAction](https://developer.apple.com/documentation/callkit/cxcallaction)Added [CXCallAction.callUUID](https://developer.apple.com/documentation/callkit/cxcallaction/1648089-calluuid)Added [-[CXCallAction initWithCallUUID:]](https://developer.apple.com/documentation/callkit/cxcallaction/1648088-init)Added [-[CXCallAction initWithCoder:]](https://developer.apple.com/documentation/callkit/cxcallaction/1648087-init)

#### CXCallController.h (Added)

Added [CXCallController](https://developer.apple.com/documentation/callkit/cxcallcontroller)Added [CXCallController.callObserver](https://developer.apple.com/documentation/callkit/cxcallcontroller/1648119-callobserver)Added [-[CXCallController init]](https://developer.apple.com/documentation/callkit/cxcallcontroller/1648117-init)Added [-[CXCallController initWithQueue:]](https://developer.apple.com/documentation/callkit/cxcallcontroller/1648120-init)Added [-[CXCallController requestTransaction:completion:]](https://developer.apple.com/documentation/callkit/cxcallcontroller/1648116-requesttransaction)

#### CXCallDirectory.h (Added)

Added [CXCallDirectoryPhoneNumber](https://developer.apple.com/documentation/callkit/cxcalldirectoryphonenumber)Added [CXCallDirectoryPhoneNumberMax](https://developer.apple.com/documentation/callkit/cxcalldirectoryphonenumbermax)

#### CXCallDirectoryExtensionContext.h (Added)

Added [CXCallDirectoryExtensionContext](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext)Added [-[CXCallDirectoryExtensionContext addBlockingEntryWithNextSequentialPhoneNumber:]](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/1779571-addblockingentry)Added [-[CXCallDirectoryExtensionContext addIdentificationEntryWithNextSequentialPhoneNumber:label:]](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/1779572-addidentificationentry)Added [-[CXCallDirectoryExtensionContext completeRequestWithCompletionHandler:]](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/1779570-completerequest)Added [CXCallDirectoryExtensionContext.delegate](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/2305438-delegate)Added [CXCallDirectoryExtensionContextDelegate](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontextdelegate)Added [-[CXCallDirectoryExtensionContextDelegate requestFailedForExtensionContext:withError:]](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontextdelegate/2305467-requestfailed)

#### CXCallDirectoryManager.h (Added)

Added [CXCallDirectoryManager](https://developer.apple.com/documentation/callkit/cxcalldirectorymanager)Added [-[CXCallDirectoryManager getEnabledStatusForExtensionWithIdentifier:completionHandler:]](https://developer.apple.com/documentation/callkit/cxcalldirectorymanager/1779567-getenabledstatusforextension)Added [-[CXCallDirectoryManager reloadExtensionWithIdentifier:completionHandler:]](https://developer.apple.com/documentation/callkit/cxcalldirectorymanager/1649012-reloadextensionwithidentifier)Added [+[CXCallDirectoryManager sharedInstance]](https://developer.apple.com/documentation/callkit/cxcalldirectorymanager/1648997-sharedinstance)Added [CXCallDirectoryManager.sharedInstance](https://developer.apple.com/documentation/callkit/cxcalldirectorymanager/1648997-sharedinstance)Added [CXCallDirectoryEnabledStatus](https://developer.apple.com/documentation/callkit/cxcalldirectorymanager/enabledstatus)Added [CXCallDirectoryEnabledStatusDisabled](https://developer.apple.com/documentation/callkit/cxcalldirectoryenabledstatus/cxcalldirectoryenabledstatusdisabled)Added [CXCallDirectoryEnabledStatusEnabled](https://developer.apple.com/documentation/callkit/cxcalldirectoryenabledstatus/cxcalldirectoryenabledstatusenabled)Added [CXCallDirectoryEnabledStatusUnknown](https://developer.apple.com/documentation/callkit/cxcalldirectorymanager/enabledstatus/unknown)

#### CXCallDirectoryProvider.h (Added)

Added [CXCallDirectoryProvider](https://developer.apple.com/documentation/callkit/cxcalldirectoryprovider)Added [-[CXCallDirectoryProvider beginRequestWithExtensionContext:]](https://developer.apple.com/documentation/callkit/cxcalldirectoryprovider/1779582-beginrequestwithextensioncontext)

#### CXCallObserver.h (Added)

Added [CXCallObserver](https://developer.apple.com/documentation/callkit/cxcallobserver)Added [CXCallObserver.calls](https://developer.apple.com/documentation/callkit/cxcallobserver/1648973-calls)Added [-[CXCallObserver setDelegate:queue:]](https://developer.apple.com/documentation/callkit/cxcallobserver/1648998-setdelegate)Added [CXCallObserverDelegate](https://developer.apple.com/documentation/callkit/cxcallobserverdelegate)Added [-[CXCallObserverDelegate callObserver:callChanged:]](https://developer.apple.com/documentation/callkit/cxcallobserverdelegate/1649009-callobserver)

#### CXCallUpdate.h (Added)

Added [CXCallUpdate](https://developer.apple.com/documentation/callkit/cxcallupdate)Added [CXCallUpdate.hasVideo](https://developer.apple.com/documentation/callkit/cxcallupdate/2212625-hasvideo)Added [CXCallUpdate.localizedCallerName](https://developer.apple.com/documentation/callkit/cxcallupdate/1648584-localizedcallername)Added [CXCallUpdate.remoteHandle](https://developer.apple.com/documentation/callkit/cxcallupdate/2102405-remotehandle)Added [CXCallUpdate.supportsDTMF](https://developer.apple.com/documentation/callkit/cxcallupdate/1648585-supportsdtmf)Added [CXCallUpdate.supportsGrouping](https://developer.apple.com/documentation/callkit/cxcallupdate/1648587-supportsgrouping)Added [CXCallUpdate.supportsHolding](https://developer.apple.com/documentation/callkit/cxcallupdate/1648586-supportsholding)Added [CXCallUpdate.supportsUngrouping](https://developer.apple.com/documentation/callkit/cxcallupdate/1648589-supportsungrouping)

#### CXEndCallAction.h (Added)

Added [CXEndCallAction](https://developer.apple.com/documentation/callkit/cxendcallaction)Added [-[CXEndCallAction fulfillWithDateEnded:]](https://developer.apple.com/documentation/callkit/cxendcallaction/1771760-fulfill)

#### CXError.h (Added)

Added [CXErrorCode](https://developer.apple.com/documentation/callkit/cxerrorcode)Added [CXErrorCodeCallDirectoryManagerError](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror/code)Added [CXErrorCodeCallDirectoryManagerErrorDuplicateEntries](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror/code/duplicateentries)Added [CXErrorCodeCallDirectoryManagerErrorEntriesOutOfOrder](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror/code/entriesoutoforder)Added [CXErrorCodeCallDirectoryManagerErrorExtensionDisabled](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror/code/extensiondisabled)Added [CXErrorCodeCallDirectoryManagerErrorLoadingInterrupted](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror/code/loadinginterrupted)Added [CXErrorCodeCallDirectoryManagerErrorMaximumEntriesExceeded](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror/cxerrorcodecalldirectorymanagererrormaximumentriesexceeded)Added [CXErrorCodeCallDirectoryManagerErrorNoExtensionFound](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror/code/noextensionfound)Added [CXErrorCodeCallDirectoryManagerErrorUnknown](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror/cxerrorcodecalldirectorymanagererrorunknown)Added [CXErrorCodeIncomingCallError](https://developer.apple.com/documentation/callkit/cxerrorcodeincomingcallerror/code)Added [CXErrorCodeIncomingCallErrorCallUUIDAlreadyExists](https://developer.apple.com/documentation/callkit/cxerrorcodeincomingcallerror/cxerrorcodeincomingcallerrorcalluuidalreadyexists)Added [CXErrorCodeIncomingCallErrorFilteredByBlockList](https://developer.apple.com/documentation/callkit/cxerrorcodeincomingcallerror/code/filteredbyblocklist)Added [CXErrorCodeIncomingCallErrorFilteredByDoNotDisturb](https://developer.apple.com/documentation/callkit/cxerrorcodeincomingcallerror/cxerrorcodeincomingcallerrorfilteredbydonotdisturb)Added [CXErrorCodeIncomingCallErrorUnentitled](https://developer.apple.com/documentation/callkit/cxerrorcodeincomingcallerror/code/unentitled)Added [CXErrorCodeIncomingCallErrorUnknown](https://developer.apple.com/documentation/callkit/cxerrorcodeincomingcallerror/cxerrorcodeincomingcallerrorunknown)Added [CXErrorCodeRequestTransactionError](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror/code)Added [CXErrorCodeRequestTransactionErrorCallUUIDAlreadyExists](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror/cxerrorcoderequesttransactionerrorcalluuidalreadyexists)Added [CXErrorCodeRequestTransactionErrorEmptyTransaction](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror/cxerrorcoderequesttransactionerroremptytransaction)Added [CXErrorCodeRequestTransactionErrorInvalidAction](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror/code/invalidaction)Added [CXErrorCodeRequestTransactionErrorMaximumCallGroupsReached](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror/cxerrorcoderequesttransactionerrormaximumcallgroupsreached)Added [CXErrorCodeRequestTransactionErrorUnentitled](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror/cxerrorcoderequesttransactionerrorunentitled)Added [CXErrorCodeRequestTransactionErrorUnknown](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror/cxerrorcoderequesttransactionerrorunknown)Added [CXErrorCodeRequestTransactionErrorUnknownCallProvider](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror/code/unknowncallprovider)Added [CXErrorCodeRequestTransactionErrorUnknownCallUUID](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror/code/unknowncalluuid)Added [CXErrorCodeUnknownError](https://developer.apple.com/documentation/callkit/cxerrorcode/cxerrorcodeunknownerror)Added [CXErrorDomain](https://developer.apple.com/documentation/callkit/cxerrordomain)Added [CXErrorDomainCallDirectoryManager](https://developer.apple.com/documentation/callkit/cxerrordomaincalldirectorymanager)Added [CXErrorDomainIncomingCall](https://developer.apple.com/documentation/callkit/cxerrordomainincomingcall)Added [CXErrorDomainRequestTransaction](https://developer.apple.com/documentation/callkit/cxerrordomainrequesttransaction)

#### CXHandle.h (Added)

Added [CXHandle](https://developer.apple.com/documentation/callkit/cxhandle)Added [-[CXHandle initWithType:value:]](https://developer.apple.com/documentation/callkit/cxhandle/2102570-init)Added [-[CXHandle isEqualToHandle:]](https://developer.apple.com/documentation/callkit/cxhandle/2102564-isequaltohandle)Added [CXHandle.type](https://developer.apple.com/documentation/callkit/cxhandle/2102566-type)Added [CXHandle.value](https://developer.apple.com/documentation/callkit/cxhandle/2102565-value)Added [CXHandleType](https://developer.apple.com/documentation/callkit/cxhandletype)Added [CXHandleTypeEmailAddress](https://developer.apple.com/documentation/callkit/cxhandle/handletype/emailaddress)Added [CXHandleTypeGeneric](https://developer.apple.com/documentation/callkit/cxhandletype/cxhandletypegeneric)Added [CXHandleTypePhoneNumber](https://developer.apple.com/documentation/callkit/cxhandletype/cxhandletypephonenumber)

#### CXPlayDTMFCallAction.h (Added)

Added [CXPlayDTMFCallAction](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction)Added [CXPlayDTMFCallAction.digits](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction/1649003-digits)Added [-[CXPlayDTMFCallAction initWithCallUUID:digits:type:]](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction/2147857-initwithcalluuid)Added [-[CXPlayDTMFCallAction initWithCoder:]](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction/2147859-init)Added [CXPlayDTMFCallAction.type](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction/1648980-type)Added [CXPlayDTMFCallActionType](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction/actiontype)Added [CXPlayDTMFCallActionTypeHardPause](https://developer.apple.com/documentation/callkit/cxplaydtmfcallactiontype/cxplaydtmfcallactiontypehardpause)Added [CXPlayDTMFCallActionTypeSingleTone](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction/actiontype/singletone)Added [CXPlayDTMFCallActionTypeSoftPause](https://developer.apple.com/documentation/callkit/cxplaydtmfcallactiontype/cxplaydtmfcallactiontypesoftpause)

#### CXProvider.h (Added)

Added [CXProvider](https://developer.apple.com/documentation/callkit/cxprovider)Added [CXProvider.configuration](https://developer.apple.com/documentation/callkit/cxprovider/1648253-configuration)Added [-[CXProvider initWithConfiguration:]](https://developer.apple.com/documentation/callkit/cxprovider/1648267-initwithconfiguration)Added [-[CXProvider invalidate]](https://developer.apple.com/documentation/callkit/cxprovider/1930697-invalidate)Added [-[CXProvider pendingCallActionsOfClass:withCallUUID:]](https://developer.apple.com/documentation/callkit/cxprovider/1648252-pendingcallactionsofclass)Added [CXProvider.pendingTransactions](https://developer.apple.com/documentation/callkit/cxprovider/1648251-pendingtransactions)Added [-[CXProvider reportCallWithUUID:endedAtDate:reason:]](https://developer.apple.com/documentation/callkit/cxprovider/1930701-reportcall)Added [-[CXProvider reportCallWithUUID:updated:]](https://developer.apple.com/documentation/callkit/cxprovider/1930703-reportcall)Added [-[CXProvider reportNewIncomingCallWithUUID:update:completion:]](https://developer.apple.com/documentation/callkit/cxprovider/1930694-reportnewincomingcall)Added [-[CXProvider reportOutgoingCallWithUUID:connectedAtDate:]](https://developer.apple.com/documentation/callkit/cxprovider/1930695-reportoutgoingcall)Added [-[CXProvider reportOutgoingCallWithUUID:startedConnectingAtDate:]](https://developer.apple.com/documentation/callkit/cxprovider/1930696-reportoutgoingcall)Added [-[CXProvider setDelegate:queue:]](https://developer.apple.com/documentation/callkit/cxprovider/1648274-setdelegate)Added [CXProviderDelegate](https://developer.apple.com/documentation/callkit/cxproviderdelegate)Added [-[CXProviderDelegate provider:didActivateAudioSession:]](https://developer.apple.com/documentation/callkit/cxproviderdelegate/1833281-provider)Added [-[CXProviderDelegate provider:didDeactivateAudioSession:]](https://developer.apple.com/documentation/callkit/cxproviderdelegate/1833280-provider)Added [-[CXProviderDelegate provider:executeTransaction:]](https://developer.apple.com/documentation/callkit/cxproviderdelegate/1648257-provider)Added [-[CXProviderDelegate provider:performAnswerCallAction:]](https://developer.apple.com/documentation/callkit/cxproviderdelegate/1648270-provider)Added [-[CXProviderDelegate provider:performEndCallAction:]](https://developer.apple.com/documentation/callkit/cxproviderdelegate/1648264-provider)Added [-[CXProviderDelegate provider:performPlayDTMFCallAction:]](https://developer.apple.com/documentation/callkit/cxproviderdelegate/1648261-provider)Added [-[CXProviderDelegate provider:performSetGroupCallAction:]](https://developer.apple.com/documentation/callkit/cxproviderdelegate/1648265-provider)Added [-[CXProviderDelegate provider:performSetHeldCallAction:]](https://developer.apple.com/documentation/callkit/cxproviderdelegate/1648256-provider)Added [-[CXProviderDelegate provider:performSetMutedCallAction:]](https://developer.apple.com/documentation/callkit/cxproviderdelegate/1648269-provider)Added [-[CXProviderDelegate provider:performStartCallAction:]](https://developer.apple.com/documentation/callkit/cxproviderdelegate/1648260-provider)Added [-[CXProviderDelegate provider:timedOutPerformingAction:]](https://developer.apple.com/documentation/callkit/cxproviderdelegate/1771738-provider)Added [-[CXProviderDelegate providerDidBegin:]](https://developer.apple.com/documentation/callkit/cxproviderdelegate/1648262-providerdidbegin)Added [-[CXProviderDelegate providerDidReset:]](https://developer.apple.com/documentation/callkit/cxproviderdelegate/1771739-providerdidreset)Added [CXCallEndedReason](https://developer.apple.com/documentation/callkit/cxcallendedreason)Added [CXCallEndedReasonAnsweredElsewhere](https://developer.apple.com/documentation/callkit/cxcallendedreason/cxcallendedreasonansweredelsewhere)Added [CXCallEndedReasonDeclinedElsewhere](https://developer.apple.com/documentation/callkit/cxcallendedreason/declinedelsewhere)Added [CXCallEndedReasonFailed](https://developer.apple.com/documentation/callkit/cxcallendedreason/failed)Added [CXCallEndedReasonRemoteEnded](https://developer.apple.com/documentation/callkit/cxcallendedreason/remoteended)Added [CXCallEndedReasonUnanswered](https://developer.apple.com/documentation/callkit/cxcallendedreason/cxcallendedreasonunanswered)

#### CXProviderConfiguration.h (Added)

Added [CXProviderConfiguration](https://developer.apple.com/documentation/callkit/cxproviderconfiguration)Added [CXProviderConfiguration.iconTemplateImageData](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/2274376-icontemplateimagedata)Added [-[CXProviderConfiguration initWithLocalizedName:]](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/1648349-init)Added [CXProviderConfiguration.localizedName](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/1648347-localizedname)Added [CXProviderConfiguration.maximumCallGroups](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/1648348-maximumcallgroups)Added [CXProviderConfiguration.maximumCallsPerCallGroup](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/1648351-maximumcallspercallgroup)Added [CXProviderConfiguration.ringtoneSound](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/1648350-ringtonesound)Added [CXProviderConfiguration.supportedHandleTypes](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/2102473-supportedhandletypes)Added [CXProviderConfiguration.supportsVideo](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/1779574-supportsvideo)

#### CXSetGroupCallAction.h (Added)

Added [CXSetGroupCallAction](https://developer.apple.com/documentation/callkit/cxsetgroupcallaction)Added [CXSetGroupCallAction.callUUIDToGroupWith](https://developer.apple.com/documentation/callkit/cxsetgroupcallaction/1648993-calluuidtogroupwith)Added [-[CXSetGroupCallAction initWithCallUUID:callUUIDToGroupWith:]](https://developer.apple.com/documentation/callkit/cxsetgroupcallaction/2143177-initwithcalluuid)Added [-[CXSetGroupCallAction initWithCoder:]](https://developer.apple.com/documentation/callkit/cxsetgroupcallaction/2143178-initwithcoder)

#### CXSetHeldCallAction.h (Added)

Added [CXSetHeldCallAction](https://developer.apple.com/documentation/callkit/cxsetheldcallaction)Added [-[CXSetHeldCallAction initWithCallUUID:onHold:]](https://developer.apple.com/documentation/callkit/cxsetheldcallaction/2143182-init)Added [-[CXSetHeldCallAction initWithCoder:]](https://developer.apple.com/documentation/callkit/cxsetheldcallaction/2143183-init)Added [CXSetHeldCallAction.onHold](https://developer.apple.com/documentation/callkit/cxsetheldcallaction/1649005-isonhold)

#### CXSetMutedCallAction.h (Added)

Added [CXSetMutedCallAction](https://developer.apple.com/documentation/callkit/cxsetmutedcallaction)Added [-[CXSetMutedCallAction initWithCallUUID:muted:]](https://developer.apple.com/documentation/callkit/cxsetmutedcallaction/2143165-initwithcalluuid)Added [-[CXSetMutedCallAction initWithCoder:]](https://developer.apple.com/documentation/callkit/cxsetmutedcallaction/2143164-init)Added [CXSetMutedCallAction.muted](https://developer.apple.com/documentation/callkit/cxsetmutedcallaction/1648995-muted)

#### CXStartCallAction.h (Added)

Added [CXStartCallAction](https://developer.apple.com/documentation/callkit/cxstartcallaction)Added [CXStartCallAction.contactIdentifier](https://developer.apple.com/documentation/callkit/cxstartcallaction/1648074-contactidentifier)Added [-[CXStartCallAction fulfillWithDateStarted:]](https://developer.apple.com/documentation/callkit/cxstartcallaction/1771732-fulfillwithdatestarted)Added [CXStartCallAction.handle](https://developer.apple.com/documentation/callkit/cxstartcallaction/2102276-handle)Added [-[CXStartCallAction initWithCallUUID:handle:]](https://developer.apple.com/documentation/callkit/cxstartcallaction/2143298-init)Added [-[CXStartCallAction initWithCoder:]](https://developer.apple.com/documentation/callkit/cxstartcallaction/2143299-init)Added [CXStartCallAction.video](https://developer.apple.com/documentation/callkit/cxstartcallaction/2274632-video)

#### CXTransaction.h (Added)

Added [CXTransaction](https://developer.apple.com/documentation/callkit/cxtransaction)Added [CXTransaction.actions](https://developer.apple.com/documentation/callkit/cxtransaction/1648158-actions)Added [-[CXTransaction addAction:]](https://developer.apple.com/documentation/callkit/cxtransaction/1648154-addaction)Added [CXTransaction.complete](https://developer.apple.com/documentation/callkit/cxtransaction/1648155-complete)Added [-[CXTransaction initWithAction:]](https://developer.apple.com/documentation/callkit/cxtransaction/2274391-initwithaction)Added [-[CXTransaction initWithActions:]](https://developer.apple.com/documentation/callkit/cxtransaction/2274392-initwithactions)Added [CXTransaction.UUID](https://developer.apple.com/documentation/callkit/cxtransaction/1648157-uuid)

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
