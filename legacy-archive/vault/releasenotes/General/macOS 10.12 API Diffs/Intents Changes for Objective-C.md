---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/Intents.html
archived_at: '2026-07-18T02:50:39.902217Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# Intents Changes for Objective-C

### Intents (Added)

#### CLPlacemark+IntentsAdditions.h (Added)

Added CLPlacemark(INIntentsAdditions)

#### INCallCapabilityOptions.h (Added)

Added [INCallCapabilityOptionAudioCall](https://developer.apple.com/documentation/sirikit/incallcapabilityoptions/1902345-audiocall)Added [INCallCapabilityOptions](https://developer.apple.com/documentation/sirikit/incallcapabilityoptions)Added #def INCallCapabilityOptions_hAdded [INCallCapabilityOptionVideoCall](https://developer.apple.com/documentation/sirikit/incallcapabilityoptions/incallcapabilityoptionvideocall)

#### INCallRecordType.h (Added)

Added [INCallRecordType](https://developer.apple.com/documentation/sirikit/incallrecordtype)Added #def INCallRecordType_hAdded [INCallRecordTypeMissed](https://developer.apple.com/documentation/sirikit/incallrecordtype/incallrecordtypemissed)Added [INCallRecordTypeOutgoing](https://developer.apple.com/documentation/sirikit/incallrecordtype/outgoing)Added [INCallRecordTypeReceived](https://developer.apple.com/documentation/sirikit/incallrecordtype/incallrecordtypereceived)Added [INCallRecordTypeUnknown](https://developer.apple.com/documentation/sirikit/incallrecordtype/incallrecordtypeunknown)

#### INCallRecordTypeResolutionResult.h (Added)

Added [INCallRecordTypeResolutionResult](https://developer.apple.com/documentation/sirikit/incallrecordtyperesolutionresult)Added [+[INCallRecordTypeResolutionResult confirmationRequiredWithValueToConfirm:]](https://developer.apple.com/documentation/sirikit/incallrecordtyperesolutionresult/2933971-confirmationrequiredwithvaluetoc)Added [+[INCallRecordTypeResolutionResult successWithResolvedValue:]](https://developer.apple.com/documentation/sirikit/incallrecordtyperesolutionresult/2933972-successwithresolvedvalue)

#### INConditionalOperator.h (Added)

Added [INConditionalOperator](https://developer.apple.com/documentation/sirikit/inconditionaloperator)Added #def INConditionalOperator_hAdded [INConditionalOperatorAll](https://developer.apple.com/documentation/sirikit/inconditionaloperator/all)Added [INConditionalOperatorAny](https://developer.apple.com/documentation/sirikit/inconditionaloperator/any)Added [INConditionalOperatorNone](https://developer.apple.com/documentation/sirikit/inconditionaloperator/inconditionaloperatornone)

#### INDateComponentsRange.h (Added)

Added [INDateComponentsRange](https://developer.apple.com/documentation/sirikit/indatecomponentsrange)Added [INDateComponentsRange.endDateComponents](https://developer.apple.com/documentation/sirikit/indatecomponentsrange/1639237-enddatecomponents)Added [-[INDateComponentsRange initWithStartDateComponents:endDateComponents:]](https://developer.apple.com/documentation/sirikit/indatecomponentsrange/1639081-init)Added [INDateComponentsRange.startDateComponents](https://developer.apple.com/documentation/sirikit/indatecomponentsrange/1639214-startdatecomponents)

#### INDateComponentsRangeResolutionResult.h (Added)

Added [INDateComponentsRangeResolutionResult](https://developer.apple.com/documentation/sirikit/indatecomponentsrangeresolutionresult)Added [+[INDateComponentsRangeResolutionResult confirmationRequiredWithDateComponentsRangeToConfirm:]](https://developer.apple.com/documentation/sirikit/indatecomponentsrangeresolutionresult/1906923-confirmationrequired)Added [+[INDateComponentsRangeResolutionResult disambiguationWithDateComponentsRangesToDisambiguate:]](https://developer.apple.com/documentation/sirikit/indatecomponentsrangeresolutionresult/1906922-disambiguationwithdatecomponents)Added [+[INDateComponentsRangeResolutionResult successWithResolvedDateComponentsRange:]](https://developer.apple.com/documentation/sirikit/indatecomponentsrangeresolutionresult/1906920-successwithresolveddatecomponent)

#### INImage.h (Added)

Added [INImage](https://developer.apple.com/documentation/sirikit/inimage)Added [+[INImage imageNamed:]](https://developer.apple.com/documentation/sirikit/inimage/1778402-imagenamed)Added [+[INImage imageWithImageData:]](https://developer.apple.com/documentation/sirikit/inimage/1639328-init)Added [+[INImage imageWithURL:]](https://developer.apple.com/documentation/sirikit/inimage/1638698-init)

#### INIntent.h (Added)

Added [INIntent](https://developer.apple.com/documentation/sirikit/inintent)Added [INIntent.identifier](https://developer.apple.com/documentation/sirikit/inintent/1639000-identifier)

#### INIntentErrors.h (Added)

Added [INIntentErrorCode](https://developer.apple.com/documentation/sirikit/inintenterror/code)Added [INIntentErrorDeletingAllInteractions](https://developer.apple.com/documentation/sirikit/inintenterrorcode/inintenterrordeletingallinteractions)Added [INIntentErrorDeletingInteractionWithGroupIdentifier](https://developer.apple.com/documentation/sirikit/inintenterrorcode/inintenterrordeletinginteractionwithgroupidentifier)Added [INIntentErrorDeletingInteractionWithIdentifiers](https://developer.apple.com/documentation/sirikit/inintenterrorcode/inintenterrordeletinginteractionwithidentifiers)Added [INIntentErrorDomain](https://developer.apple.com/documentation/sirikit/inintenterrordomain)Added [INIntentErrorDonatingInteraction](https://developer.apple.com/documentation/sirikit/inintenterrorcode/inintenterrordonatinginteraction)Added [INIntentErrorIntentSupportedByMultipleExtension](https://developer.apple.com/documentation/sirikit/inintenterror/code/intentsupportedbymultipleextension)Added [INIntentErrorInteractionOperationNotSupported](https://developer.apple.com/documentation/sirikit/inintenterrorcode/inintenterrorinteractionoperationnotsupported)Added [INIntentErrorInvalidIntentName](https://developer.apple.com/documentation/sirikit/inintenterrorcode/inintenterrorinvalidintentname)Added [INIntentErrorInvalidUserVocabularyFileLocation](https://developer.apple.com/documentation/sirikit/inintenterrorcode/inintenterrorinvaliduservocabularyfilelocation)Added [INIntentErrorNoHandlerProvidedForIntent](https://developer.apple.com/documentation/sirikit/inintenterror/code/nohandlerprovidedforintent)Added [INIntentErrorRequestTimedOut](https://developer.apple.com/documentation/sirikit/inintenterror/code/requesttimedout)Added [INIntentErrorRestrictedIntentsNotSupportedByExtension](https://developer.apple.com/documentation/sirikit/inintenterror/code/restrictedintentsnotsupportedbyextension)

#### INIntentResolutionResult.h (Added)

Added [INIntentResolutionResult](https://developer.apple.com/documentation/sirikit/inintentresolutionresult)Added [+[INIntentResolutionResult needsValue]](https://developer.apple.com/documentation/sirikit/inintentresolutionresult/1902446-needsvalue)Added [+[INIntentResolutionResult notRequired]](https://developer.apple.com/documentation/sirikit/inintentresolutionresult/1902445-notrequired)Added [+[INIntentResolutionResult unsupported]](https://developer.apple.com/documentation/sirikit/inintentresolutionresult/2138302-unsupported)

#### INIntentResponse.h (Added)

Added [INIntentResponse](https://developer.apple.com/documentation/sirikit/inintentresponse)Added [INIntentResponse.userActivity](https://developer.apple.com/documentation/sirikit/inintentresponse/1639469-useractivity)

#### INInteraction.h (Added)

Added [INInteraction](https://developer.apple.com/documentation/sirikit/ininteraction)Added [INInteraction.dateInterval](https://developer.apple.com/documentation/sirikit/ininteraction/1638853-dateinterval)Added [+[INInteraction deleteAllInteractionsWithCompletion:]](https://developer.apple.com/documentation/sirikit/ininteraction/1690389-deleteall)Added [+[INInteraction deleteInteractionsWithGroupIdentifier:completion:]](https://developer.apple.com/documentation/sirikit/ininteraction/1690364-deleteinteractionswithgroupident)Added [+[INInteraction deleteInteractionsWithIdentifiers:completion:]](https://developer.apple.com/documentation/sirikit/ininteraction/1690400-deleteinteractionswithidentifier)Added [INInteraction.direction](https://developer.apple.com/documentation/sirikit/ininteraction/1639368-direction)Added [-[INInteraction donateInteractionWithCompletion:]](https://developer.apple.com/documentation/sirikit/ininteraction/1690386-donateinteractionwithcompletion)Added [INInteraction.groupIdentifier](https://developer.apple.com/documentation/sirikit/ininteraction/1638832-groupidentifier)Added [INInteraction.identifier](https://developer.apple.com/documentation/sirikit/ininteraction/1638924-identifier)Added [-[INInteraction initWithIntent:response:]](https://developer.apple.com/documentation/sirikit/ininteraction/1639259-initwithintent)Added [INInteraction.intent](https://developer.apple.com/documentation/sirikit/ininteraction/1638928-intent)Added [INInteraction.intentHandlingStatus](https://developer.apple.com/documentation/sirikit/ininteraction/1638740-intenthandlingstatus)Added [INInteraction.intentResponse](https://developer.apple.com/documentation/sirikit/ininteraction/1638817-intentresponse)Added [INIntentHandlingStatus](https://developer.apple.com/documentation/sirikit/inintenthandlingstatus)Added [INIntentHandlingStatusDeferredToApplication](https://developer.apple.com/documentation/sirikit/inintenthandlingstatus/inintenthandlingstatusdeferredtoapplication)Added [INIntentHandlingStatusFailure](https://developer.apple.com/documentation/sirikit/inintenthandlingstatus/inintenthandlingstatusfailure)Added [INIntentHandlingStatusInProgress](https://developer.apple.com/documentation/sirikit/inintenthandlingstatus/inintenthandlingstatusinprogress)Added [INIntentHandlingStatusReady](https://developer.apple.com/documentation/sirikit/inintenthandlingstatus/ready)Added [INIntentHandlingStatusSuccess](https://developer.apple.com/documentation/sirikit/inintenthandlingstatus/success)Added [INIntentHandlingStatusUnspecified](https://developer.apple.com/documentation/sirikit/inintenthandlingstatus/unspecified)Added [INInteractionDirection](https://developer.apple.com/documentation/sirikit/ininteractiondirection)Added [INInteractionDirectionIncoming](https://developer.apple.com/documentation/sirikit/ininteractiondirection/ininteractiondirectionincoming)Added [INInteractionDirectionOutgoing](https://developer.apple.com/documentation/sirikit/ininteractiondirection/ininteractiondirectionoutgoing)Added [INInteractionDirectionUnspecified](https://developer.apple.com/documentation/sirikit/ininteractiondirection/ininteractiondirectionunspecified)

#### INMessage.h (Added)

Added [INMessage](https://developer.apple.com/documentation/sirikit/inmessage)Added [INMessage.content](https://developer.apple.com/documentation/sirikit/inmessage/1638554-content)Added [INMessage.dateSent](https://developer.apple.com/documentation/sirikit/inmessage/1639255-datesent)Added [INMessage.identifier](https://developer.apple.com/documentation/sirikit/inmessage/1638230-identifier)Added [-[INMessage initWithIdentifier:content:dateSent:sender:recipients:]](https://developer.apple.com/documentation/sirikit/inmessage/1687606-init)Added [INMessage.recipients](https://developer.apple.com/documentation/sirikit/inmessage/1638938-recipients)Added [INMessage.sender](https://developer.apple.com/documentation/sirikit/inmessage/1638778-sender)

#### INMessageAttributeOptions.h (Added)

Added [INMessageAttributeOptionFlagged](https://developer.apple.com/documentation/sirikit/inmessageattributeoptions/inmessageattributeoptionflagged)Added [INMessageAttributeOptionRead](https://developer.apple.com/documentation/sirikit/inmessageattributeoptions/inmessageattributeoptionread)Added [INMessageAttributeOptions](https://developer.apple.com/documentation/sirikit/inmessageattributeoptions)Added #def INMessageAttributeOptions_hAdded [INMessageAttributeOptionUnflagged](https://developer.apple.com/documentation/sirikit/inmessageattributeoptions/inmessageattributeoptionunflagged)Added [INMessageAttributeOptionUnread](https://developer.apple.com/documentation/sirikit/inmessageattributeoptions/1902413-unread)

#### INMessageAttributeOptionsResolutionResult.h (Added)

Added [INMessageAttributeOptionsResolutionResult](https://developer.apple.com/documentation/sirikit/inmessageattributeoptionsresolutionresult)Added [+[INMessageAttributeOptionsResolutionResult confirmationRequiredWithValueToConfirm:]](https://developer.apple.com/documentation/sirikit/inmessageattributeoptionsresolutionresult/2933991-confirmationrequiredwithvaluetoc)Added [+[INMessageAttributeOptionsResolutionResult successWithResolvedValue:]](https://developer.apple.com/documentation/sirikit/inmessageattributeoptionsresolutionresult/2933992-successwithresolvedvalue)

#### INPerson.h (Added)

Added [INPerson](https://developer.apple.com/documentation/sirikit/inperson)Added [INPerson.aliases](https://developer.apple.com/documentation/sirikit/inperson/2138316-aliases)Added [INPerson.contactIdentifier](https://developer.apple.com/documentation/sirikit/inperson/1638320-contactidentifier)Added [INPerson.customIdentifier](https://developer.apple.com/documentation/sirikit/inperson/2138295-customidentifier)Added [INPerson.displayName](https://developer.apple.com/documentation/sirikit/inperson/1638921-displayname)Added [INPerson.handle](https://developer.apple.com/documentation/sirikit/inperson/1639190-handle)Added [INPerson.image](https://developer.apple.com/documentation/sirikit/inperson/1639130-image)Added [-[INPerson initWithHandle:displayName:contactIdentifier:]](https://developer.apple.com/documentation/sirikit/inperson/1638494-initwithhandle)Added [-[INPerson initWithHandle:nameComponents:contactIdentifier:]](https://developer.apple.com/documentation/sirikit/inperson/1639010-initwithhandle)Added [-[INPerson initWithHandle:nameComponents:displayName:image:contactIdentifier:]](https://developer.apple.com/documentation/sirikit/inperson/1638508-initwithhandle)Added [-[INPerson initWithPersonHandle:nameComponents:displayName:image:contactIdentifier:customIdentifier:]](https://developer.apple.com/documentation/sirikit/inperson/2138319-init)Added [-[INPerson initWithPersonHandle:nameComponents:displayName:image:contactIdentifier:customIdentifier:aliases:suggestionType:]](https://developer.apple.com/documentation/sirikit/inperson/2138310-initwithpersonhandle)Added [INPerson.nameComponents](https://developer.apple.com/documentation/sirikit/inperson/1638822-namecomponents)Added [INPerson.personHandle](https://developer.apple.com/documentation/sirikit/inperson/2138314-personhandle)Added [INPerson.suggestionType](https://developer.apple.com/documentation/sirikit/inperson/2138313-suggestiontype)Added INPerson(INInteraction)Added INPerson(INPersonCreation)Added [INPersonSuggestionType](https://developer.apple.com/documentation/sirikit/inpersonsuggestiontype)Added [INPersonSuggestionTypeInstantMessageAddress](https://developer.apple.com/documentation/sirikit/inpersonsuggestiontype/inpersonsuggestiontypeinstantmessageaddress)Added [INPersonSuggestionTypeSocialProfile](https://developer.apple.com/documentation/sirikit/inpersonsuggestiontype/inpersonsuggestiontypesocialprofile)

#### INPersonHandle.h (Added)

Added [INPersonHandle](https://developer.apple.com/documentation/sirikit/inpersonhandle)Added [-[INPersonHandle initWithValue:type:]](https://developer.apple.com/documentation/sirikit/inpersonhandle/2138303-init)Added [INPersonHandle.type](https://developer.apple.com/documentation/sirikit/inpersonhandle/2138309-type)Added [INPersonHandle.value](https://developer.apple.com/documentation/sirikit/inpersonhandle/2138297-value)Added [INPersonHandleType](https://developer.apple.com/documentation/sirikit/inpersonhandletype)Added [INPersonHandleTypeEmailAddress](https://developer.apple.com/documentation/sirikit/inpersonhandletype/inpersonhandletypeemailaddress)Added [INPersonHandleTypePhoneNumber](https://developer.apple.com/documentation/sirikit/inpersonhandletype/phonenumber)Added [INPersonHandleTypeUnknown](https://developer.apple.com/documentation/sirikit/inpersonhandletype/inpersonhandletypeunknown)

#### INPersonResolutionResult.h (Added)

Added [INPersonResolutionResult](https://developer.apple.com/documentation/sirikit/inpersonresolutionresult)Added [+[INPersonResolutionResult confirmationRequiredWithPersonToConfirm:]](https://developer.apple.com/documentation/sirikit/inpersonresolutionresult/1902496-confirmationrequired)Added [+[INPersonResolutionResult disambiguationWithPeopleToDisambiguate:]](https://developer.apple.com/documentation/sirikit/inpersonresolutionresult/1902497-disambiguationwithpeopletodisamb)Added [+[INPersonResolutionResult successWithResolvedPerson:]](https://developer.apple.com/documentation/sirikit/inpersonresolutionresult/1902499-successwithresolvedperson)

#### INPlacemarkResolutionResult.h (Added)

Added [INPlacemarkResolutionResult](https://developer.apple.com/documentation/sirikit/inplacemarkresolutionresult)Added [+[INPlacemarkResolutionResult confirmationRequiredWithPlacemarkToConfirm:]](https://developer.apple.com/documentation/sirikit/inplacemarkresolutionresult/1902453-confirmationrequiredwithplacemar)Added [+[INPlacemarkResolutionResult disambiguationWithPlacemarksToDisambiguate:]](https://developer.apple.com/documentation/sirikit/inplacemarkresolutionresult/1902456-disambiguationwithplacemarkstodi)Added [+[INPlacemarkResolutionResult successWithResolvedPlacemark:]](https://developer.apple.com/documentation/sirikit/inplacemarkresolutionresult/1902457-successwithresolvedplacemark)

#### INSearchCallHistoryIntent.h (Added)

Added [INSearchCallHistoryIntent](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintent)Added [INSearchCallHistoryIntent.callCapabilities](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintent/1639273-callcapabilities)Added [INSearchCallHistoryIntent.callType](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintent/1638944-calltype)Added [INSearchCallHistoryIntent.dateCreated](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintent/1638678-datecreated)Added [-[INSearchCallHistoryIntent initWithCallType:dateCreated:recipient:callCapabilities:]](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintent/1902451-init)Added [INSearchCallHistoryIntent.recipient](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintent/1638907-recipient)Added [INSearchCallHistoryIntentHandling](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintenthandling)Added [-[INSearchCallHistoryIntentHandling confirmSearchCallHistory:completion:]](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintenthandling/1639070-confirm)Added [-[INSearchCallHistoryIntentHandling handleSearchCallHistory:completion:]](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintenthandling/1638471-handle)Added [-[INSearchCallHistoryIntentHandling resolveCallTypeForSearchCallHistory:withCompletion:]](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintenthandling/1902447-resolvecalltype)Added [-[INSearchCallHistoryIntentHandling resolveDateCreatedForSearchCallHistory:withCompletion:]](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintenthandling/1902448-resolvedatecreatedforsearchcallh)Added [-[INSearchCallHistoryIntentHandling resolveRecipientForSearchCallHistory:withCompletion:]](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintenthandling/1902450-resolverecipient)

#### INSearchCallHistoryIntentResponse.h (Added)

Added [INSearchCallHistoryIntentResponse](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintentresponse)Added [INSearchCallHistoryIntentResponse.code](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintentresponse/1823492-code)Added [-[INSearchCallHistoryIntentResponse initWithCode:userActivity:]](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintentresponse/1638691-initwithcode)Added [INSearchCallHistoryIntentResponseCode](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintentresponsecode)Added [INSearchCallHistoryIntentResponseCodeContinueInApp](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintentresponsecode/continueinapp)Added [INSearchCallHistoryIntentResponseCodeFailure](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintentresponsecode/failure)Added [INSearchCallHistoryIntentResponseCodeFailureRequiringAppLaunch](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintentresponsecode/insearchcallhistoryintentresponsecodefailurerequiringapplaunch)Added [INSearchCallHistoryIntentResponseCodeReady](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintentresponsecode/ready)Added [INSearchCallHistoryIntentResponseCodeUnspecified](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintentresponsecode/insearchcallhistoryintentresponsecodeunspecified)

#### INSearchForMessagesIntent.h (Added)

Added [INSearchForMessagesIntent](https://developer.apple.com/documentation/sirikit/insearchformessagesintent)Added [INSearchForMessagesIntent.attributes](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1639482-attributes)Added [INSearchForMessagesIntent.dateTimeRange](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1638192-datetimerange)Added [INSearchForMessagesIntent.groupNames](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1778236-groupnames)Added [INSearchForMessagesIntent.groupNamesOperator](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1778193-groupnamesoperator)Added [INSearchForMessagesIntent.identifiers](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1638976-identifiers)Added [INSearchForMessagesIntent.identifiersOperator](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1638746-identifiersoperator)Added [-[INSearchForMessagesIntent initWithRecipients:senders:searchTerms:attributes:dateTimeRange:identifiers:notificationIdentifiers:groupNames:]](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1902435-init)Added [INSearchForMessagesIntent.notificationIdentifiers](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1639365-notificationidentifiers)Added [INSearchForMessagesIntent.notificationIdentifiersOperator](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1639253-notificationidentifiersoperator)Added [INSearchForMessagesIntent.recipients](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1638455-recipients)Added [INSearchForMessagesIntent.recipientsOperator](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1638624-recipientsoperator)Added [INSearchForMessagesIntent.searchTerms](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1639353-searchterms)Added [INSearchForMessagesIntent.searchTermsOperator](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1639002-searchtermsoperator)Added [INSearchForMessagesIntent.senders](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1638436-senders)Added [INSearchForMessagesIntent.sendersOperator](https://developer.apple.com/documentation/sirikit/insearchformessagesintent/1639394-sendersoperator)Added [INSearchForMessagesIntentHandling](https://developer.apple.com/documentation/sirikit/insearchformessagesintenthandling)Added [-[INSearchForMessagesIntentHandling confirmSearchForMessages:completion:]](https://developer.apple.com/documentation/sirikit/insearchformessagesintenthandling/1638410-confirmsearchformessages)Added [-[INSearchForMessagesIntentHandling handleSearchForMessages:completion:]](https://developer.apple.com/documentation/sirikit/insearchformessagesintenthandling/1638324-handle)Added [-[INSearchForMessagesIntentHandling resolveAttributesForSearchForMessages:withCompletion:]](https://developer.apple.com/documentation/sirikit/insearchformessagesintenthandling/1902440-resolveattributesforsearchformes)Added [-[INSearchForMessagesIntentHandling resolveDateTimeRangeForSearchForMessages:withCompletion:]](https://developer.apple.com/documentation/sirikit/insearchformessagesintenthandling/1902436-resolvedatetimerangeforsearchfor)Added [-[INSearchForMessagesIntentHandling resolveGroupNamesForSearchForMessages:withCompletion:]](https://developer.apple.com/documentation/sirikit/insearchformessagesintenthandling/1902438-resolvegroupnames)Added [-[INSearchForMessagesIntentHandling resolveRecipientsForSearchForMessages:withCompletion:]](https://developer.apple.com/documentation/sirikit/insearchformessagesintenthandling/1902441-resolverecipientsforsearchformes)Added [-[INSearchForMessagesIntentHandling resolveSendersForSearchForMessages:withCompletion:]](https://developer.apple.com/documentation/sirikit/insearchformessagesintenthandling/1902439-resolvesendersforsearchformessag)

#### INSearchForMessagesIntentResponse.h (Added)

Added [INSearchForMessagesIntentResponse](https://developer.apple.com/documentation/sirikit/insearchformessagesintentresponse)Added [INSearchForMessagesIntentResponse.code](https://developer.apple.com/documentation/sirikit/insearchformessagesintentresponse/1823496-code)Added [-[INSearchForMessagesIntentResponse initWithCode:userActivity:]](https://developer.apple.com/documentation/sirikit/insearchformessagesintentresponse/1638285-init)Added [INSearchForMessagesIntentResponse.messages](https://developer.apple.com/documentation/sirikit/insearchformessagesintentresponse/1639421-messages)Added [INSearchForMessagesIntentResponseCode](https://developer.apple.com/documentation/sirikit/insearchformessagesintentresponsecode)Added [INSearchForMessagesIntentResponseCodeFailure](https://developer.apple.com/documentation/sirikit/insearchformessagesintentresponsecode/insearchformessagesintentresponsecodefailure)Added [INSearchForMessagesIntentResponseCodeFailureMessageServiceNotAvailable](https://developer.apple.com/documentation/sirikit/insearchformessagesintentresponsecode/failuremessageservicenotavailable)Added [INSearchForMessagesIntentResponseCodeFailureRequiringAppLaunch](https://developer.apple.com/documentation/sirikit/insearchformessagesintentresponsecode/insearchformessagesintentresponsecodefailurerequiringapplaunch)Added [INSearchForMessagesIntentResponseCodeInProgress](https://developer.apple.com/documentation/sirikit/insearchformessagesintentresponsecode/insearchformessagesintentresponsecodeinprogress)Added [INSearchForMessagesIntentResponseCodeReady](https://developer.apple.com/documentation/sirikit/insearchformessagesintentresponsecode/ready)Added [INSearchForMessagesIntentResponseCodeSuccess](https://developer.apple.com/documentation/sirikit/insearchformessagesintentresponsecode/insearchformessagesintentresponsecodesuccess)Added [INSearchForMessagesIntentResponseCodeUnspecified](https://developer.apple.com/documentation/sirikit/insearchformessagesintentresponsecode/unspecified)

#### INSendMessageIntent.h (Added)

Added [INSendMessageIntent](https://developer.apple.com/documentation/sirikit/insendmessageintent)Added [INSendMessageIntent.content](https://developer.apple.com/documentation/sirikit/insendmessageintent/1639106-content)Added [INSendMessageIntent.groupName](https://developer.apple.com/documentation/sirikit/insendmessageintent/1778199-groupname)Added [-[INSendMessageIntent initWithRecipients:content:groupName:serviceName:sender:]](https://developer.apple.com/documentation/sirikit/insendmessageintent/1778238-init)Added [INSendMessageIntent.recipients](https://developer.apple.com/documentation/sirikit/insendmessageintent/1639316-recipients)Added [INSendMessageIntent.sender](https://developer.apple.com/documentation/sirikit/insendmessageintent/1639248-sender)Added [INSendMessageIntent.serviceName](https://developer.apple.com/documentation/sirikit/insendmessageintent/1639342-servicename)Added [INSendMessageIntentHandling](https://developer.apple.com/documentation/sirikit/insendmessageintenthandling)Added [-[INSendMessageIntentHandling confirmSendMessage:completion:]](https://developer.apple.com/documentation/sirikit/insendmessageintenthandling/1639459-confirmsendmessage)Added [-[INSendMessageIntentHandling handleSendMessage:completion:]](https://developer.apple.com/documentation/sirikit/insendmessageintenthandling/1639338-handle)Added [-[INSendMessageIntentHandling resolveContentForSendMessage:withCompletion:]](https://developer.apple.com/documentation/sirikit/insendmessageintenthandling/1902359-resolvecontentforsendmessage)Added [-[INSendMessageIntentHandling resolveGroupNameForSendMessage:withCompletion:]](https://developer.apple.com/documentation/sirikit/insendmessageintenthandling/1902358-resolvegroupname)Added [-[INSendMessageIntentHandling resolveRecipientsForSendMessage:withCompletion:]](https://developer.apple.com/documentation/sirikit/insendmessageintenthandling/1902356-resolverecipients)

#### INSendMessageIntentResponse.h (Added)

Added [INSendMessageIntentResponse](https://developer.apple.com/documentation/sirikit/insendmessageintentresponse)Added [INSendMessageIntentResponse.code](https://developer.apple.com/documentation/sirikit/insendmessageintentresponse/1823491-code)Added [-[INSendMessageIntentResponse initWithCode:userActivity:]](https://developer.apple.com/documentation/sirikit/insendmessageintentresponse/1638961-init)Added [INSendMessageIntentResponseCode](https://developer.apple.com/documentation/sirikit/insendmessageintentresponsecode)Added [INSendMessageIntentResponseCodeFailure](https://developer.apple.com/documentation/sirikit/insendmessageintentresponsecode/insendmessageintentresponsecodefailure)Added [INSendMessageIntentResponseCodeFailureMessageServiceNotAvailable](https://developer.apple.com/documentation/sirikit/insendmessageintentresponsecode/insendmessageintentresponsecodefailuremessageservicenotavailable)Added [INSendMessageIntentResponseCodeFailureRequiringAppLaunch](https://developer.apple.com/documentation/sirikit/insendmessageintentresponsecode/failurerequiringapplaunch)Added [INSendMessageIntentResponseCodeInProgress](https://developer.apple.com/documentation/sirikit/insendmessageintentresponsecode/insendmessageintentresponsecodeinprogress)Added [INSendMessageIntentResponseCodeReady](https://developer.apple.com/documentation/sirikit/insendmessageintentresponsecode/insendmessageintentresponsecodeready)Added [INSendMessageIntentResponseCodeSuccess](https://developer.apple.com/documentation/sirikit/insendmessageintentresponsecode/success)Added [INSendMessageIntentResponseCodeUnspecified](https://developer.apple.com/documentation/sirikit/insendmessageintentresponsecode/unspecified)

#### INSpeakable.h (Added)

Added [INSpeakable](https://developer.apple.com/documentation/sirikit/inspeakable)Added [INSpeakable.identifier](https://developer.apple.com/documentation/sirikit/inspeakable/2092308-identifier)Added [INSpeakable.pronunciationHint](https://developer.apple.com/documentation/sirikit/inspeakable/2092309-pronunciationhint)Added [INSpeakable.spokenPhrase](https://developer.apple.com/documentation/sirikit/inspeakable/2092306-spokenphrase)

#### INSpeakableString.h (Added)

Added [INSpeakableString](https://developer.apple.com/documentation/sirikit/inspeakablestring)Added [-[INSpeakableString initWithIdentifier:spokenPhrase:pronunciationHint:]](https://developer.apple.com/documentation/sirikit/inspeakablestring/2118338-init)

#### INSpeakableStringResolutionResult.h (Added)

Added [INSpeakableStringResolutionResult](https://developer.apple.com/documentation/sirikit/inspeakablestringresolutionresult)Added [+[INSpeakableStringResolutionResult confirmationRequiredWithStringToConfirm:]](https://developer.apple.com/documentation/sirikit/inspeakablestringresolutionresult/2092307-confirmationrequiredwithstringto)Added [+[INSpeakableStringResolutionResult disambiguationWithStringsToDisambiguate:]](https://developer.apple.com/documentation/sirikit/inspeakablestringresolutionresult/2092305-disambiguationwithstringstodisam)Added [+[INSpeakableStringResolutionResult successWithResolvedString:]](https://developer.apple.com/documentation/sirikit/inspeakablestringresolutionresult/2092304-success)

#### INStartAudioCallIntent.h (Added)

Added [INStartAudioCallIntent](https://developer.apple.com/documentation/sirikit/instartaudiocallintent)Added [INStartAudioCallIntent.contacts](https://developer.apple.com/documentation/sirikit/instartaudiocallintent/1638516-contacts)Added [-[INStartAudioCallIntent initWithContacts:]](https://developer.apple.com/documentation/sirikit/instartaudiocallintent/1638231-init)Added [INStartAudioCallIntentHandling](https://developer.apple.com/documentation/sirikit/instartaudiocallintenthandling)Added [-[INStartAudioCallIntentHandling confirmStartAudioCall:completion:]](https://developer.apple.com/documentation/sirikit/instartaudiocallintenthandling/1638634-confirmstartaudiocall)Added [-[INStartAudioCallIntentHandling handleStartAudioCall:completion:]](https://developer.apple.com/documentation/sirikit/instartaudiocallintenthandling/1639088-handle)Added [-[INStartAudioCallIntentHandling resolveContactsForStartAudioCall:withCompletion:]](https://developer.apple.com/documentation/sirikit/instartaudiocallintenthandling/1902341-resolvecontactsforstartaudiocall)

#### INStartAudioCallIntentResponse.h (Added)

Added [INStartAudioCallIntentResponse](https://developer.apple.com/documentation/sirikit/instartaudiocallintentresponse)Added [INStartAudioCallIntentResponse.code](https://developer.apple.com/documentation/sirikit/instartaudiocallintentresponse/1823483-code)Added [-[INStartAudioCallIntentResponse initWithCode:userActivity:]](https://developer.apple.com/documentation/sirikit/instartaudiocallintentresponse/1638718-initwithcode)Added [INStartAudioCallIntentResponseCode](https://developer.apple.com/documentation/sirikit/instartaudiocallintentresponsecode)Added [INStartAudioCallIntentResponseCodeContinueInApp](https://developer.apple.com/documentation/sirikit/instartaudiocallintentresponsecode/instartaudiocallintentresponsecodecontinueinapp)Added [INStartAudioCallIntentResponseCodeFailure](https://developer.apple.com/documentation/sirikit/instartaudiocallintentresponsecode/instartaudiocallintentresponsecodefailure)Added [INStartAudioCallIntentResponseCodeFailureRequiringAppLaunch](https://developer.apple.com/documentation/sirikit/instartaudiocallintentresponsecode/instartaudiocallintentresponsecodefailurerequiringapplaunch)Added [INStartAudioCallIntentResponseCodeReady](https://developer.apple.com/documentation/sirikit/instartaudiocallintentresponsecode/instartaudiocallintentresponsecodeready)Added [INStartAudioCallIntentResponseCodeUnspecified](https://developer.apple.com/documentation/sirikit/instartaudiocallintentresponsecode/instartaudiocallintentresponsecodeunspecified)

#### INStartVideoCallIntent.h (Added)

Added [INStartVideoCallIntent](https://developer.apple.com/documentation/sirikit/instartvideocallintent)Added [INStartVideoCallIntent.contacts](https://developer.apple.com/documentation/sirikit/instartvideocallintent/1639126-contacts)Added [-[INStartVideoCallIntent initWithContacts:]](https://developer.apple.com/documentation/sirikit/instartvideocallintent/1638541-init)Added [INStartVideoCallIntentHandling](https://developer.apple.com/documentation/sirikit/instartvideocallintenthandling)Added [-[INStartVideoCallIntentHandling confirmStartVideoCall:completion:]](https://developer.apple.com/documentation/sirikit/instartvideocallintenthandling/1639163-confirmstartvideocall)Added [-[INStartVideoCallIntentHandling handleStartVideoCall:completion:]](https://developer.apple.com/documentation/sirikit/instartvideocallintenthandling/1639069-handle)Added [-[INStartVideoCallIntentHandling resolveContactsForStartVideoCall:withCompletion:]](https://developer.apple.com/documentation/sirikit/instartvideocallintenthandling/1902444-resolvecontacts)

#### INStartVideoCallIntentResponse.h (Added)

Added [INStartVideoCallIntentResponse](https://developer.apple.com/documentation/sirikit/instartvideocallintentresponse)Added [INStartVideoCallIntentResponse.code](https://developer.apple.com/documentation/sirikit/instartvideocallintentresponse/1823493-code)Added [-[INStartVideoCallIntentResponse initWithCode:userActivity:]](https://developer.apple.com/documentation/sirikit/instartvideocallintentresponse/1639246-initwithcode)Added [INStartVideoCallIntentResponseCode](https://developer.apple.com/documentation/sirikit/instartvideocallintentresponsecode)Added [INStartVideoCallIntentResponseCodeContinueInApp](https://developer.apple.com/documentation/sirikit/instartvideocallintentresponsecode/continueinapp)Added [INStartVideoCallIntentResponseCodeFailure](https://developer.apple.com/documentation/sirikit/instartvideocallintentresponsecode/failure)Added [INStartVideoCallIntentResponseCodeFailureRequiringAppLaunch](https://developer.apple.com/documentation/sirikit/instartvideocallintentresponsecode/failurerequiringapplaunch)Added [INStartVideoCallIntentResponseCodeReady](https://developer.apple.com/documentation/sirikit/instartvideocallintentresponsecode/instartvideocallintentresponsecodeready)Added [INStartVideoCallIntentResponseCodeUnspecified](https://developer.apple.com/documentation/sirikit/instartvideocallintentresponsecode/instartvideocallintentresponsecodeunspecified)

#### INStringResolutionResult.h (Added)

Added [INStringResolutionResult](https://developer.apple.com/documentation/sirikit/instringresolutionresult)Added [+[INStringResolutionResult confirmationRequiredWithStringToConfirm:]](https://developer.apple.com/documentation/sirikit/instringresolutionresult/1902375-confirmationrequired)Added [+[INStringResolutionResult disambiguationWithStringsToDisambiguate:]](https://developer.apple.com/documentation/sirikit/instringresolutionresult/1902378-disambiguation)Added [+[INStringResolutionResult successWithResolvedString:]](https://developer.apple.com/documentation/sirikit/instringresolutionresult/1902377-successwithresolvedstring)

#### Intents.h (Added)

Added [IntentsVersionNumber](https://developer.apple.com/documentation/sirikit/intentsversionnumber)Added [IntentsVersionString](https://developer.apple.com/documentation/sirikit/intentsversionstring)

#### IntentsDefines.h (Added)

Added #def INTENTS_EXTERN

#### NSUserActivity+IntentsAdditions.h (Added)

Added [NSUserActivity.interaction](https://developer.apple.com/documentation/foundation/nsuseractivity/1690346-interaction)Added NSUserActivity(IntentsAdditions)

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
