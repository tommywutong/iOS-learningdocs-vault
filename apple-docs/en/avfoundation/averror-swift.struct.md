---
title: AVError
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/averror-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/averror-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/averror-swift.struct.json'
content_hash: 'sha256:bcfdce18661bec82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVError

<sub>Structure</sub>

A structure that defines the errors that framework operations can generate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVError
```

## Relationships

- **Conforms To**: [CustomNSError](../foundation/customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Error domain

- [errorDomain](averror-swift.struct/errordomain.md)

### Error codes

- [Code](averror-swift.struct/code.md) — An enumeration that defines the errors that framework operations can generate.
- [airPlayControllerRequiresInternet](averror-swift.struct/airplaycontrollerrequiresinternet.md) — The AirPlay controller requires an internet connection to function.
- [airPlayReceiverRequiresInternet](averror-swift.struct/airplayreceiverrequiresinternet.md) — The AirPlay receiver requires an internet connection to function.
- [airPlayReceiverTemporarilyUnavailable](averror-swift.struct/airplayreceivertemporarilyunavailable.md) — An AirPlay receiver is temporarily unavailable.
- [applicationIsNotAuthorizedToUseDevice](averror-swift.struct/applicationisnotauthorizedtousedevice.md) — The user denied this app permission to capture media.
- [applicationIsNotAuthorized](averror-swift.struct/applicationisnotauthorized.md) — The app isn’t authorized to play media.
- [autoWhiteBalanceNotLocked](averror-swift.struct/autowhitebalancenotlocked.md)
- [compositionTrackSegmentsNotContiguous](averror-swift.struct/compositiontracksegmentsnotcontiguous.md) — The composition can’t add the source media because it contains gaps.
- [contentIsNotAuthorized](averror-swift.struct/contentisnotauthorized.md) — The user isn’t authorized to play the media.
- [contentIsProtected](averror-swift.struct/contentisprotected.md) — The app isn’t authorized to open the media.
- [contentIsUnavailable](averror-swift.struct/contentisunavailable.md) — The captured content is unavailable.
- [contentKeyRequestCancelled](averror-swift.struct/contentkeyrequestcancelled.md) — The app canceled a request to retrieve a content key.
- [contentNotUpdated](averror-swift.struct/contentnotupdated.md) — The system couldn’t update the captured content.
- [createContentKeyRequestFailed](averror-swift.struct/createcontentkeyrequestfailed.md) — The app couldn’t create a content key request.
- [decodeFailed](averror-swift.struct/decodefailed.md) — The system failed to decode the media.
- [decoderNotFound](averror-swift.struct/decodernotfound.md) — The system can’t find a suitable decoder for the media.
- [decoderTemporarilyUnavailable](averror-swift.struct/decodertemporarilyunavailable.md) — A suitable decoder for the media is temporarily available.
- [deviceAlreadyUsedByAnotherSession](averror-swift.struct/devicealreadyusedbyanothersession.md) — Your app can’t access the device because another session is currently using it.
- [deviceInUseByAnotherApplication](averror-swift.struct/deviceinusebyanotherapplication.md) — Your app can’t access the device because another app is currently using it.
- [deviceLockedForConfigurationByAnotherProcess](averror-swift.struct/devicelockedforconfigurationbyanotherprocess.md) — Your app can’t change device settings because another process currently controls the device.
- [deviceNotConnected](averror-swift.struct/devicenotconnected.md) — You app can’t access the device because it isn’t connected.
- [deviceWasDisconnected](averror-swift.struct/devicewasdisconnected.md) — A previously connected device is no longer accessible.
- [diskFull](averror-swift.struct/diskfull.md) — Recording stopped because the disk is full.
- [displayWasDisabled](averror-swift.struct/displaywasdisabled.md) — Screen capture failed because the display was inactive.
- [encodeFailed](averror-swift.struct/encodefailed.md) — The system couldn’t encode the media data.
- [encoderNotFound](averror-swift.struct/encodernotfound.md) — The requested encoder isn’t found.
- [encoderTemporarilyUnavailable](averror-swift.struct/encodertemporarilyunavailable.md) — An appropriate encoder isn’t currently available.
- [exportFailed](averror-swift.struct/exportfailed.md) — The requested export operation failed.
- [externalPlaybackNotSupportedForAsset](averror-swift.struct/externalplaybacknotsupportedforasset.md) — The current asset doesn’t support playback.
- [failedToLoadMediaData](averror-swift.struct/failedtoloadmediadata.md) — The system can’t load the requested media data.
- [failedToLoadSampleData](averror-swift.struct/failedtoloadsampledata.md) — The system can’t load the requested sample data.
- [failedToParse](averror-swift.struct/failedtoparse.md) — The system can’t parse the media.
- [fileAlreadyExists](averror-swift.struct/filealreadyexists.md) — A file with the same name exists at the location and you can’t overwrite it.
- [fileFailedToParse](averror-swift.struct/filefailedtoparse.md) — The file is corrupt or in an unrecognized format.
- [fileFormatNotRecognized](averror-swift.struct/fileformatnotrecognized.md) — The system can’t open the file because it’s in an unrecognized format.
- [fileTypeDoesNotSupportSampleReferences](averror-swift.struct/filetypedoesnotsupportsamplereferences.md) — The file type doesn’t support sample references.
- [followExternalSyncDeviceTimedOut](averror-swift.struct/followexternalsyncdevicetimedout.md)
- [formatUnsupported](averror-swift.struct/formatunsupported.md) — The current asset format isn’t supported.
- [incompatibleAsset](averror-swift.struct/incompatibleasset.md) — You can’t display the media because the device isn’t capable of playing the content.
- [incorrectlyConfigured](averror-swift.struct/incorrectlyconfigured.md) — The system is incorrectly configured for the requested operation.
- [invalidCompositionTrackSegmentDuration](averror-swift.struct/invalidcompositiontracksegmentduration.md) — You can’t add the source media because its duration in the destination is invalid.
- [invalidCompositionTrackSegmentSourceDuration](averror-swift.struct/invalidcompositiontracksegmentsourceduration.md) — You can’t add the source media because it has no duration.
- [invalidCompositionTrackSegmentSourceStartTime](averror-swift.struct/invalidcompositiontracksegmentsourcestarttime.md) — You can’t add the source media because its start time in the destination is invalid.
- [invalidOutputURLPathExtension](averror-swift.struct/invalidoutputurlpathextension.md) — The path extension of the output URL is invalid.
- [invalidSampleCursor](averror-swift.struct/invalidsamplecursor.md) — An invalid sample cursor produced an error.
- [invalidSourceMedia](averror-swift.struct/invalidsourcemedia.md) — The system couldn’t read the source media.
- [invalidVideoComposition](averror-swift.struct/invalidvideocomposition.md) — You attempted to present an unsupported video composition.
- [malformedDepth](averror-swift.struct/malformeddepth.md) — The depth data isn’t properly structured.
- [maximumDurationReached](averror-swift.struct/maximumdurationreached.md) — The recording stopped because it reached the file’s maximum duration.
- [maximumFileSizeReached](averror-swift.struct/maximumfilesizereached.md) — The recording stopped because it reached the file’s maximum size.
- [maximumNumberOfSamplesForFileFormatReached](averror-swift.struct/maximumnumberofsamplesforfileformatreached.md) — The recording stopped because it reached the file’s maximum number of samples.
- [maximumStillImageCaptureRequestsExceeded](averror-swift.struct/maximumstillimagecapturerequestsexceeded.md) — Your app can’t take a photo because there are too many unfinished photo capture requests.
- [mediaChanged](averror-swift.struct/mediachanged.md) — Recording stopped because the format of the source media changed.
- [mediaDiscontinuity](averror-swift.struct/mediadiscontinuity.md) — Recording stopped because there was an interruption in the input media.
- [mediaExtensionConflict](averror-swift.struct/mediaextensionconflict.md)
- [mediaExtensionDisabled](averror-swift.struct/mediaextensiondisabled.md)
- [mediaServicesWereReset](averror-swift.struct/mediaserviceswerereset.md) — The system couldn’t perform the operation because media services were unavailable.
- [noCompatibleAlternatesForExternalDisplay](averror-swift.struct/nocompatiblealternatesforexternaldisplay.md) — The system found no compatible external displays.
- [noDataCaptured](averror-swift.struct/nodatacaptured.md) — The recording failed because the system received no data.
- [noImageAtTime](averror-swift.struct/noimageattime.md) — No image is available in the media at the indicated time.
- [noLongerPlayable](averror-swift.struct/nolongerplayable.md) — The asset is no longer playable.
- [noSmartFramingsEnabled](averror-swift.struct/nosmartframingsenabled.md)
- [noSourceTrack](averror-swift.struct/nosourcetrack.md) — The asset doesn’t contain a source track.
- [operationCancelled](averror-swift.struct/operationcancelled.md) — The asset handled a request to cancel loading a property value asynchronously.
- [operationInterrupted](averror-swift.struct/operationinterrupted.md) — An interruption occurred while performing a reading or writing operation.
- [operationNotAllowed](averror-swift.struct/operationnotallowed.md) — The requested operation isn’t allowed.
- [operationNotSupportedForAsset](averror-swift.struct/operationnotsupportedforasset.md) — Your app attempted to perform an unsupported operation with the asset.
- [operationNotSupportedForPreset](averror-swift.struct/operationnotsupportedforpreset.md) — Your app attempted to perform an unsupported operation for the current preset.
- [outOfMemory](averror-swift.struct/outofmemory.md) — The operation couldn’t finish because there isn’t enough memory available to process the media.
- [recordingAlreadyInProgress](averror-swift.struct/recordingalreadyinprogress.md) — Your app attempted to start recording a movie file while an existing recording is underway.
- [referenceForbiddenByReferencePolicy](averror-swift.struct/referenceforbiddenbyreferencepolicy.md) — The current reference restrictions prevent the system from loading referenced media.
- [rosettaNotInstalled](averror-swift.struct/rosettanotinstalled.md) — The system doesn’t have Rosetta installed and can’t perform the requested operation.
- [sandboxExtensionDenied](averror-swift.struct/sandboxextensiondenied.md) — The system denied issuing the sandbox extension.
- [screenCaptureFailed](averror-swift.struct/screencapturefailed.md) — An unexpected problem occurred that prevented screen capture.
- [segmentStartedWithNonSyncSample](averror-swift.struct/segmentstartedwithnonsyncsample.md) — The operation attempted to write a new MPEG-4 segment that didn’t start with a sync sample.
- [serverIncorrectlyConfigured](averror-swift.struct/serverincorrectlyconfigured.md) — The configuration of the HTTP server that streams the media resource isn’t correct.
- [sessionConfigurationChanged](averror-swift.struct/sessionconfigurationchanged.md) — Recording stopped because the configuration of media sources and destinations changed.
- [sessionHardwareCostOverage](averror-swift.struct/sessionhardwarecostoverage.md) — Your app requested too many camera hardware resources.
- [sessionNotRunning](averror-swift.struct/sessionnotrunning.md) — The recording couldn’t start because the session isn’t running.
- [sessionWasInterrupted](averror-swift.struct/sessionwasinterrupted.md) — The recording stopped because the system interrupted the audio session.
- [toneMappingFailed](averror-swift.struct/tonemappingfailed.md) — The requested tone mapping failed.
- [torchLevelUnavailable](averror-swift.struct/torchlevelunavailable.md) — The specified torch level is valid but currently unavailable, possibly due to overheating.
- [undecodableMediaData](averror-swift.struct/undecodablemediadata.md) — The system couldn’t decode the media data.
- [unknown](averror-swift.struct/unknown.md) — An unknown error occurred.
- [unsupportedDeviceActiveFormat](averror-swift.struct/unsupporteddeviceactiveformat.md) — The capture session doesn’t support the camera device’s active format.
- [unsupportedOutputSettings](averror-swift.struct/unsupportedoutputsettings.md) — Your app requested unsupported output settings.
- [videoCompositorFailed](averror-swift.struct/videocompositorfailed.md) — The compositor couldn’t composite video frames.
- [deviceIsNotAvailableInBackground](averror-swift.struct/deviceisnotavailableinbackground.md) — You attempted to start a capture session in the background, which isn’t allowed in iOS. _(deprecated)_

### Error properties

- [device](averror-swift.struct/device-5iio4.md) — The capture device in use.
- [device](averror-swift.struct/device-1qfzr.md)
- [fileSize](averror-swift.struct/filesize.md) — The asset file size.
- [fileType](averror-swift.struct/filetype.md) — The asset file type.
- [mediaSubtypes](averror-swift.struct/mediasubtypes.md) — An array of media subtypes.
- [mediaType](averror-swift.struct/mediatype-7ksjb.md) — The asset media type.
- [mediaType](averror-swift.struct/mediatype-5d8ie.md) — The media type.
- [persistentTrackID](averror-swift.struct/persistenttrackid.md) — The persistent track ID, if the track exists.
- [presentationTimeStamp](averror-swift.struct/presentationtimestamp.md) — The presentation time stamp.
- [processID](averror-swift.struct/processid.md) — The process ID.
- [recordingSuccessfullyFinished](averror-swift.struct/recordingsuccessfullyfinished.md) — A Boolean value that indicates whether recording finished successfully.
- [time](averror-swift.struct/time.md) — The time duration of the error.

### User info keys

- [AVErrorDeviceKey](averrordevicekey.md) — The user information key to retrieve the device name.
- [AVErrorDiscontinuityFlagsKey](averrordiscontinuityflagskey.md) — The user information key to retrieve discontinuity flags.
- [AVErrorFileSizeKey](averrorfilesizekey.md) — The user information key to retrieve the file size in bytes.
- [AVErrorFileTypeKey](averrorfiletypekey.md) — The user information key to retrieve the file type.
- [AVErrorMediaTypeKey](averrormediatypekey.md) — The user information key to retrieve the media type.
- [AVErrorMediaSubTypeKey](averrormediasubtypekey.md) — The user information key to retrieve the media subtype.
- [AVErrorPersistentTrackIDKey](averrorpersistenttrackidkey.md) — The user information key to retrieve the track’s persistent identifier.
- [AVErrorPIDKey](averrorpidkey.md) — The user information key to retrieve the process ID value.
- [AVErrorPresentationTimeStampKey](averrorpresentationtimestampkey.md) — The user information key to retrieve the presentation time stamp.
- [AVErrorRecordingSuccessfullyFinishedKey](averrorrecordingsuccessfullyfinishedkey.md) — The user information key to retrieve a Boolean value that indicates whether recording finished successfully.
- [AVErrorTimeKey](averrortimekey.md) — The user information key to retrieve the error time.

### Type Properties

- [externalSyncDeviceFrequencyHigherThanSpecified](averror-swift.struct/externalsyncdevicefrequencyhigherthanspecified.md) _(beta)_
- [externalSyncDeviceFrequencyLowerThanSpecified](averror-swift.struct/externalsyncdevicefrequencylowerthanspecified.md) _(beta)_
- [followExternalSyncFailed](averror-swift.struct/followexternalsyncfailed.md) _(beta)_
- [notEnoughSpaceForProVideoStorageReplenishment](averror-swift.struct/notenoughspaceforprovideostoragereplenishment.md) _(beta)_

## See Also

### Errors

- [AVFoundationErrorDomain](avfoundationerrordomain.md) — The error domain of AVFoundation errors.
