---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/Speech.html
archived_at: '2026-07-18T02:54:58.952892Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# Speech Changes for Objective-C

### Speech (Added)

#### SFSpeechRecognitionRequest.h (Added)

Added [SFSpeechAudioBufferRecognitionRequest](https://developer.apple.com/documentation/speech/sfspeechaudiobufferrecognitionrequest)Added [-[SFSpeechAudioBufferRecognitionRequest appendAudioPCMBuffer:]](https://developer.apple.com/documentation/speech/sfspeechaudiobufferrecognitionrequest/1649389-appendaudiopcmbuffer)Added [-[SFSpeechAudioBufferRecognitionRequest appendAudioSampleBuffer:]](https://developer.apple.com/documentation/speech/sfspeechaudiobufferrecognitionrequest/1649395-appendaudiosamplebuffer)Added [-[SFSpeechAudioBufferRecognitionRequest endAudio]](https://developer.apple.com/documentation/speech/sfspeechaudiobufferrecognitionrequest/1649388-endaudio)Added [SFSpeechAudioBufferRecognitionRequest.nativeAudioFormat](https://developer.apple.com/documentation/speech/sfspeechaudiobufferrecognitionrequest/1649387-nativeaudioformat)Added [SFSpeechRecognitionRequest](https://developer.apple.com/documentation/speech/sfspeechrecognitionrequest)Added [SFSpeechRecognitionRequest.contextualStrings](https://developer.apple.com/documentation/speech/sfspeechrecognitionrequest/1649391-contextualstrings)Added [SFSpeechRecognitionRequest.interactionIdentifier](https://developer.apple.com/documentation/speech/sfspeechrecognitionrequest/1649384-interactionidentifier)Added [SFSpeechRecognitionRequest.shouldReportPartialResults](https://developer.apple.com/documentation/speech/sfspeechrecognitionrequest/1649392-shouldreportpartialresults)Added [SFSpeechRecognitionRequest.taskHint](https://developer.apple.com/documentation/speech/sfspeechrecognitionrequest/1649386-taskhint)Added [SFSpeechURLRecognitionRequest](https://developer.apple.com/documentation/speech/sfspeechurlrecognitionrequest)Added [-[SFSpeechURLRecognitionRequest initWithURL:]](https://developer.apple.com/documentation/speech/sfspeechurlrecognitionrequest/1649390-init)Added [SFSpeechURLRecognitionRequest.URL](https://developer.apple.com/documentation/speech/sfspeechurlrecognitionrequest/1649394-url)

#### SFSpeechRecognitionResult.h (Added)

Added [SFSpeechRecognitionResult](https://developer.apple.com/documentation/speech/sfspeechrecognitionresult)Added [SFSpeechRecognitionResult.bestTranscription](https://developer.apple.com/documentation/speech/sfspeechrecognitionresult/1648280-besttranscription)Added [SFSpeechRecognitionResult.final](https://developer.apple.com/documentation/speech/sfspeechrecognitionresult/1648281-final)Added [SFSpeechRecognitionResult.transcriptions](https://developer.apple.com/documentation/speech/sfspeechrecognitionresult/1648282-transcriptions)

#### SFSpeechRecognitionTask.h (Added)

Added [SFSpeechRecognitionTask](https://developer.apple.com/documentation/speech/sfspeechrecognitiontask)Added [-[SFSpeechRecognitionTask cancel]](https://developer.apple.com/documentation/speech/sfspeechrecognitiontask/1649204-cancel)Added [SFSpeechRecognitionTask.cancelled](https://developer.apple.com/documentation/speech/sfspeechrecognitiontask/1649208-iscancelled)Added [SFSpeechRecognitionTask.error](https://developer.apple.com/documentation/speech/sfspeechrecognitiontask/1649201-error)Added [-[SFSpeechRecognitionTask finish]](https://developer.apple.com/documentation/speech/sfspeechrecognitiontask/1649198-finish)Added [SFSpeechRecognitionTask.finishing](https://developer.apple.com/documentation/speech/sfspeechrecognitiontask/1649213-isfinishing)Added [SFSpeechRecognitionTask.state](https://developer.apple.com/documentation/speech/sfspeechrecognitiontask/1649196-state)Added [SFSpeechRecognitionTaskDelegate](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate)Added [-[SFSpeechRecognitionTaskDelegate speechRecognitionDidDetectSpeech:]](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/1649206-speechrecognitiondiddetectspeech)Added [-[SFSpeechRecognitionTaskDelegate speechRecognitionTask:didFinishRecognition:]](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/1649214-speechrecognitiontask)Added [-[SFSpeechRecognitionTaskDelegate speechRecognitionTask:didFinishSuccessfully:]](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/1649215-speechrecognitiontask)Added [-[SFSpeechRecognitionTaskDelegate speechRecognitionTask:didHypothesizeTranscription:]](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/1649210-speechrecognitiontask)Added [-[SFSpeechRecognitionTaskDelegate speechRecognitionTaskFinishedReadingAudio:]](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/1649193-speechrecognitiontaskfinishedrea)Added [-[SFSpeechRecognitionTaskDelegate speechRecognitionTaskWasCancelled:]](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/1649200-speechrecognitiontaskwascancelle)Added [SFSpeechRecognitionTaskState](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskstate)Added [SFSpeechRecognitionTaskStateCanceling](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskstate/sfspeechrecognitiontaskstatecanceling)Added [SFSpeechRecognitionTaskStateCompleted](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskstate/sfspeechrecognitiontaskstatecompleted)Added [SFSpeechRecognitionTaskStateFinishing](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskstate/finishing)Added [SFSpeechRecognitionTaskStateRunning](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskstate/sfspeechrecognitiontaskstaterunning)Added [SFSpeechRecognitionTaskStateStarting](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskstate/starting)

#### SFSpeechRecognitionTaskHint.h (Added)

Added [SFSpeechRecognitionTaskHint](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskhint)Added [SFSpeechRecognitionTaskHintConfirmation](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskhint/sfspeechrecognitiontaskhintconfirmation)Added [SFSpeechRecognitionTaskHintDictation](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskhint/dictation)Added [SFSpeechRecognitionTaskHintSearch](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskhint/search)Added [SFSpeechRecognitionTaskHintUnspecified](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskhint/unspecified)

#### SFSpeechRecognizer.h (Added)

Added [SFSpeechRecognizer](https://developer.apple.com/documentation/speech/sfspeechrecognizer)Added [+[SFSpeechRecognizer authorizationStatus]](https://developer.apple.com/documentation/speech/sfspeechrecognizer/1649884-authorizationstatus)Added [SFSpeechRecognizer.available](https://developer.apple.com/documentation/speech/sfspeechrecognizer/1649885-available)Added [SFSpeechRecognizer.defaultTaskHint](https://developer.apple.com/documentation/speech/sfspeechrecognizer/1649896-defaulttaskhint)Added [SFSpeechRecognizer.delegate](https://developer.apple.com/documentation/speech/sfspeechrecognizer/1649893-delegate)Added [-[SFSpeechRecognizer init]](https://developer.apple.com/documentation/speech/sfspeechrecognizer/1649878-init)Added [-[SFSpeechRecognizer initWithLocale:]](https://developer.apple.com/documentation/speech/sfspeechrecognizer/1649877-initwithlocale)Added [SFSpeechRecognizer.locale](https://developer.apple.com/documentation/speech/sfspeechrecognizer/1649882-locale)Added [SFSpeechRecognizer.queue](https://developer.apple.com/documentation/speech/sfspeechrecognizer/1649881-queue)Added [-[SFSpeechRecognizer recognitionTaskWithRequest:delegate:]](https://developer.apple.com/documentation/speech/sfspeechrecognizer/1649894-recognitiontask)Added [-[SFSpeechRecognizer recognitionTaskWithRequest:resultHandler:]](https://developer.apple.com/documentation/speech/sfspeechrecognizer/1649883-recognitiontaskwithrequest)Added [+[SFSpeechRecognizer requestAuthorization:]](https://developer.apple.com/documentation/speech/sfspeechrecognizer/1649892-requestauthorization)Added [+[SFSpeechRecognizer supportedLocales]](https://developer.apple.com/documentation/speech/sfspeechrecognizer/1649889-supportedlocales)Added [SFSpeechRecognizerDelegate](https://developer.apple.com/documentation/speech/sfspeechrecognizerdelegate)Added [-[SFSpeechRecognizerDelegate speechRecognizer:availabilityDidChange:]](https://developer.apple.com/documentation/speech/sfspeechrecognizerdelegate/1649879-speechrecognizer)Added [SFSpeechRecognizerAuthorizationStatus](https://developer.apple.com/documentation/speech/sfspeechrecognizerauthorizationstatus)Added [SFSpeechRecognizerAuthorizationStatusAuthorized](https://developer.apple.com/documentation/speech/sfspeechrecognizerauthorizationstatus/authorized)Added [SFSpeechRecognizerAuthorizationStatusDenied](https://developer.apple.com/documentation/speech/sfspeechrecognizerauthorizationstatus/denied)Added [SFSpeechRecognizerAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/speech/sfspeechrecognizerauthorizationstatus/sfspeechrecognizerauthorizationstatusnotdetermined)Added [SFSpeechRecognizerAuthorizationStatusRestricted](https://developer.apple.com/documentation/speech/sfspeechrecognizerauthorizationstatus/sfspeechrecognizerauthorizationstatusrestricted)

#### SFTranscription.h (Added)

Added [SFTranscription](https://developer.apple.com/documentation/speech/sftranscription)Added [SFTranscription.formattedString](https://developer.apple.com/documentation/speech/sftranscription/1648774-formattedstring)Added [SFTranscription.segments](https://developer.apple.com/documentation/speech/sftranscription/1648773-segments)

#### SFTranscriptionSegment.h (Added)

Added [SFTranscriptionSegment](https://developer.apple.com/documentation/speech/sftranscriptionsegment)Added [SFTranscriptionSegment.alternativeSubstrings](https://developer.apple.com/documentation/speech/sftranscriptionsegment/1649528-alternativesubstrings)Added [SFTranscriptionSegment.confidence](https://developer.apple.com/documentation/speech/sftranscriptionsegment/1649534-confidence)Added [SFTranscriptionSegment.duration](https://developer.apple.com/documentation/speech/sftranscriptionsegment/1649531-duration)Added [SFTranscriptionSegment.substring](https://developer.apple.com/documentation/speech/sftranscriptionsegment/1649532-substring)Added [SFTranscriptionSegment.substringRange](https://developer.apple.com/documentation/speech/sftranscriptionsegment/1649529-substringrange)Added [SFTranscriptionSegment.timestamp](https://developer.apple.com/documentation/speech/sftranscriptionsegment/1649533-timestamp)

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
