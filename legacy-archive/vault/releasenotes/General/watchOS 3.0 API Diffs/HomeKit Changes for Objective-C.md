---
title: watchOS 3.0 API Diffs
apple_id: TP40017328
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS30APIDiffs/Objective-C/HomeKit.html
archived_at: '2026-07-18T02:58:14.741253Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.0 API Diffs](watchOS%202.2%20to%20watchOS%203.0%20API%20Differences.md)


# HomeKit Changes for Objective-C

### HomeKit

#### HMAccessory+Camera.h (Added)

Added [HMAccessory.cameraProfiles](https://developer.apple.com/documentation/homekit/hmaccessory/1650056-cameraprofiles)Added HMAccessory(Camera)

#### HMAccessoryCategoryTypes.h

Added [HMAccessoryCategoryTypeIPCamera](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypeipcamera)Added [HMAccessoryCategoryTypeVideoDoorbell](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypevideodoorbell)

#### HMAccessoryProfile.h (Added)

Added [HMAccessoryProfile](https://developer.apple.com/documentation/homekit/hmaccessoryprofile)Added [HMAccessoryProfile.accessory](https://developer.apple.com/documentation/homekit/hmaccessoryprofile/1649077-accessory)Added [HMAccessoryProfile.services](https://developer.apple.com/documentation/homekit/hmaccessoryprofile/1649075-services)Added [HMAccessoryProfile.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmaccessoryprofile/1649076-uniqueidentifier)

#### HMActionSet.h

Added [HMActionSet.lastExecutionDate](https://developer.apple.com/documentation/homekit/hmactionset/1649437-lastexecutiondate)Added [HMActionSetTypeTriggerOwned](https://developer.apple.com/documentation/homekit/hmactionsettypetriggerowned)

#### HMCameraAudioControl.h (Added)

Added [HMCameraAudioControl](https://developer.apple.com/documentation/homekit/hmcameraaudiocontrol)Added [HMCameraAudioControl.mute](https://developer.apple.com/documentation/homekit/hmcameraaudiocontrol/1649451-mute)Added [HMCameraAudioControl.volume](https://developer.apple.com/documentation/homekit/hmcameraaudiocontrol/1649444-volume)

#### HMCameraControl.h (Added)

Added [HMCameraControl](https://developer.apple.com/documentation/homekit/hmcameracontrol)

#### HMCameraDefines.h (Added)

Added [HMCameraAudioStreamSetting](https://developer.apple.com/documentation/homekit/hmcameraaudiostreamsetting)Added [HMCameraAudioStreamSettingBidirectionalAudioAllowed](https://developer.apple.com/documentation/homekit/hmcameraaudiostreamsetting/hmcameraaudiostreamsettingbidirectionalaudioallowed)Added [HMCameraAudioStreamSettingIncomingAudioAllowed](https://developer.apple.com/documentation/homekit/hmcameraaudiostreamsetting/hmcameraaudiostreamsettingincomingaudioallowed)Added [HMCameraAudioStreamSettingMuted](https://developer.apple.com/documentation/homekit/hmcameraaudiostreamsetting/hmcameraaudiostreamsettingmuted)Added [HMCameraStreamState](https://developer.apple.com/documentation/homekit/hmcamerastreamstate)Added [HMCameraStreamStateNotStreaming](https://developer.apple.com/documentation/homekit/hmcamerastreamstate/notstreaming)Added [HMCameraStreamStateStarting](https://developer.apple.com/documentation/homekit/hmcamerastreamstate/hmcamerastreamstatestarting)Added [HMCameraStreamStateStopping](https://developer.apple.com/documentation/homekit/hmcamerastreamstate/hmcamerastreamstatestopping)Added [HMCameraStreamStateStreaming](https://developer.apple.com/documentation/homekit/hmcamerastreamstate/hmcamerastreamstatestreaming)

#### HMCameraProfile.h (Added)

Added [HMCameraProfile](https://developer.apple.com/documentation/homekit/hmcameraprofile)Added [HMCameraProfile.microphoneControl](https://developer.apple.com/documentation/homekit/hmcameraprofile/1649316-microphonecontrol)Added [HMCameraProfile.settingsControl](https://developer.apple.com/documentation/homekit/hmcameraprofile/1649313-settingscontrol)Added [HMCameraProfile.snapshotControl](https://developer.apple.com/documentation/homekit/hmcameraprofile/1833282-snapshotcontrol)Added [HMCameraProfile.speakerControl](https://developer.apple.com/documentation/homekit/hmcameraprofile/1649318-speakercontrol)Added [HMCameraProfile.streamControl](https://developer.apple.com/documentation/homekit/hmcameraprofile/1649314-streamcontrol)

#### HMCameraSettingsControl.h (Added)

Added [HMCameraSettingsControl](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol)Added [HMCameraSettingsControl.currentHorizontalTilt](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1829447-currenthorizontaltilt)Added [HMCameraSettingsControl.currentVerticalTilt](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1829448-currentverticaltilt)Added [HMCameraSettingsControl.digitalZoom](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1649954-digitalzoom)Added [HMCameraSettingsControl.imageMirroring](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1649935-imagemirroring)Added [HMCameraSettingsControl.imageRotation](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1649955-imagerotation)Added [HMCameraSettingsControl.nightVision](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1649936-nightvision)Added [HMCameraSettingsControl.opticalZoom](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1649946-opticalzoom)Added [HMCameraSettingsControl.targetHorizontalTilt](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1829450-targethorizontaltilt)Added [HMCameraSettingsControl.targetVerticalTilt](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1829449-targetverticaltilt)

#### HMCameraSnapshot.h (Added)

Added [HMCameraSnapshot](https://developer.apple.com/documentation/homekit/hmcamerasnapshot)Added [HMCameraSnapshot.captureDate](https://developer.apple.com/documentation/homekit/hmcamerasnapshot/1833285-capturedate)

#### HMCameraSnapshotControl.h (Added)

Added [HMCameraSnapshotControl](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontrol)Added [HMCameraSnapshotControl.delegate](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontrol/1833267-delegate)Added [HMCameraSnapshotControl.mostRecentSnapshot](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontrol/1833272-mostrecentsnapshot)Added [-[HMCameraSnapshotControl takeSnapshot]](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontrol/1833270-takesnapshot)Added [HMCameraSnapshotControlDelegate](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontroldelegate)Added [-[HMCameraSnapshotControlDelegate cameraSnapshotControl:didTakeSnapshot:error:]](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontroldelegate/1833265-camerasnapshotcontrol)

#### HMCameraSource.h (Added)

Added [HMCameraSource](https://developer.apple.com/documentation/homekit/hmcamerasource)

#### HMCameraStream.h (Added)

Added [HMCameraStream](https://developer.apple.com/documentation/homekit/hmcamerastream)Added [HMCameraStream.audioStreamSetting](https://developer.apple.com/documentation/homekit/hmcamerastream/1833317-audiostreamsetting)Added [-[HMCameraStream setAudioStreamSetting:]](https://developer.apple.com/documentation/homekit/hmcamerastream/2143155-setaudiostreamsetting)Added [-[HMCameraStream updateAudioStreamSetting:completionHandler:]](https://developer.apple.com/documentation/homekit/hmcamerastream/2143154-updateaudiostreamsetting)

#### HMCameraStreamControl.h (Added)

Added [HMCameraStreamControl](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol)Added [HMCameraStreamControl.cameraStream](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol/1833307-camerastream)Added [HMCameraStreamControl.delegate](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol/1649676-delegate)Added [-[HMCameraStreamControl startStream]](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol/1833311-startstream)Added [-[HMCameraStreamControl stopStream]](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol/1833308-stopstream)Added [HMCameraStreamControl.streamState](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol/1649686-streamstate)Added [HMCameraStreamControlDelegate](https://developer.apple.com/documentation/homekit/hmcamerastreamcontroldelegate)Added [-[HMCameraStreamControlDelegate cameraStreamControl:didStopStreamWithError:]](https://developer.apple.com/documentation/homekit/hmcamerastreamcontroldelegate/1833309-camerastreamcontrol)Added [-[HMCameraStreamControlDelegate cameraStreamControlDidStartStream:]](https://developer.apple.com/documentation/homekit/hmcamerastreamcontroldelegate/1833310-camerastreamcontroldidstartstrea)

#### HMCharacteristicDefines.h

Added [HMCharacteristicValueBatteryStatus](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluebatterystatus)Added [HMCharacteristicValueBatteryStatusLow](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluebatterystatus/hmcharacteristicvaluebatterystatuslow)Added [HMCharacteristicValueBatteryStatusNormal](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluebatterystatus/hmcharacteristicvaluebatterystatusnormal)Added [HMCharacteristicValueCarbonDioxideDetectionStatus](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecarbondioxidedetectionstatus)Added [HMCharacteristicValueCarbonDioxideDetectionStatusDetected](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecarbondioxidedetectionstatus/detected)Added [HMCharacteristicValueCarbonDioxideDetectionStatusNotDetected](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecarbondioxidedetectionstatus/hmcharacteristicvaluecarbondioxidedetectionstatusnotdetected)Added [HMCharacteristicValueCarbonMonoxideDetectionStatus](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecarbonmonoxidedetectionstatus)Added [HMCharacteristicValueCarbonMonoxideDetectionStatusDetected](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecarbonmonoxidedetectionstatus/hmcharacteristicvaluecarbonmonoxidedetectionstatusdetected)Added [HMCharacteristicValueCarbonMonoxideDetectionStatusNotDetected](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecarbonmonoxidedetectionstatus/hmcharacteristicvaluecarbonmonoxidedetectionstatusnotdetected)Added [HMCharacteristicValueChargingState](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluechargingstate)Added [HMCharacteristicValueChargingStateInProgress](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluechargingstate/hmcharacteristicvaluechargingstateinprogress)Added [HMCharacteristicValueChargingStateNone](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluechargingstate/none)Added [HMCharacteristicValueContactState](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecontactstate)Added [HMCharacteristicValueContactStateDetected](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecontactstate/detected)Added [HMCharacteristicValueContactStateNone](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecontactstate/none)Added [HMCharacteristicValueJammedStatus](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluejammedstatus)Added [HMCharacteristicValueJammedStatusJammed](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluejammedstatus/jammed)Added [HMCharacteristicValueJammedStatusNone](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluejammedstatus/none)Added [HMCharacteristicValueLeakStatus](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueleakstatus)Added [HMCharacteristicValueLeakStatusDetected](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueleakstatus/detected)Added [HMCharacteristicValueLeakStatusNone](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueleakstatus/hmcharacteristicvalueleakstatusnone)Added [HMCharacteristicValueOccupancyStatus](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueoccupancystatus)Added [HMCharacteristicValueOccupancyStatusNotOccupied](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueoccupancystatus/notoccupied)Added [HMCharacteristicValueOccupancyStatusOccupied](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueoccupancystatus/occupied)Added [HMCharacteristicValueSecuritySystemAlarmType](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluesecuritysystemalarmtype)Added [HMCharacteristicValueSecuritySystemAlarmTypeNoAlarm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluesecuritysystemalarmtype/hmcharacteristicvaluesecuritysystemalarmtypenoalarm)Added [HMCharacteristicValueSecuritySystemAlarmTypeUnknown](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluesecuritysystemalarmtype/unknown)Added [HMCharacteristicValueSmokeDetectionStatus](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluesmokedetectionstatus)Added [HMCharacteristicValueSmokeDetectionStatusDetected](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluesmokedetectionstatus/hmcharacteristicvaluesmokedetectionstatusdetected)Added [HMCharacteristicValueSmokeDetectionStatusNone](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluesmokedetectionstatus/none)Added [HMCharacteristicValueStatusFault](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluestatusfault)Added [HMCharacteristicValueStatusFaultGeneralFault](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluestatusfault/hmcharacteristicvaluestatusfaultgeneralfault)Added [HMCharacteristicValueStatusFaultNoFault](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluestatusfault/hmcharacteristicvaluestatusfaultnofault)Added [HMCharacteristicValueTamperedStatus](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetamperedstatus)Added [HMCharacteristicValueTamperedStatusNone](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetamperedstatus/hmcharacteristicvaluetamperedstatusnone)Added [HMCharacteristicValueTamperedStatusTampered](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetamperedstatus/hmcharacteristicvaluetamperedstatustampered)

#### HMCharacteristicMetadata.h

Added [HMCharacteristicMetadata.validValues](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata/1649244-validvalues)Added [HMCharacteristicMetadataUnitsMicrogramsPerCubicMeter](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadataunitsmicrogramspercubicmeter)Added [HMCharacteristicMetadataUnitsPartsPerMillion](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadataunitspartspermillion)

#### HMCharacteristicTypes.h

Added [HMCharacteristicTypeDigitalZoom](https://developer.apple.com/documentation/homekit/hmcharacteristictypedigitalzoom)Added [HMCharacteristicTypeImageMirroring](https://developer.apple.com/documentation/homekit/hmcharacteristictypeimagemirroring)Added [HMCharacteristicTypeImageRotation](https://developer.apple.com/documentation/homekit/hmcharacteristictypeimagerotation)Added [HMCharacteristicTypeMute](https://developer.apple.com/documentation/homekit/hmcharacteristictypemute)Added [HMCharacteristicTypeNightVision](https://developer.apple.com/documentation/homekit/hmcharacteristictypenightvision)Added [HMCharacteristicTypeOpticalZoom](https://developer.apple.com/documentation/homekit/hmcharacteristictypeopticalzoom)Added [HMCharacteristicTypeSelectedStreamConfiguration](https://developer.apple.com/documentation/homekit/hmcharacteristictypeselectedstreamconfiguration)Added [HMCharacteristicTypeSetupStreamEndpoint](https://developer.apple.com/documentation/homekit/hmcharacteristictypesetupstreamendpoint)Added [HMCharacteristicTypeStreamingStatus](https://developer.apple.com/documentation/homekit/hmcharacteristictypestreamingstatus)Added [HMCharacteristicTypeSupportedAudioStreamConfiguration](https://developer.apple.com/documentation/homekit/hmcharacteristictypesupportedaudiostreamconfiguration)Added [HMCharacteristicTypeSupportedRTPConfiguration](https://developer.apple.com/documentation/homekit/hmcharacteristictypesupportedrtpconfiguration)Added [HMCharacteristicTypeSupportedVideoStreamConfiguration](https://developer.apple.com/documentation/homekit/hmcharacteristictypesupportedvideostreamconfiguration)Added [HMCharacteristicTypeVolume](https://developer.apple.com/documentation/homekit/hmcharacteristictypevolume)

#### HMError.h

Added [HMErrorCodeBridgedAccessoryNotReachable](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodebridgedaccessorynotreachable)Added [HMErrorCodeInvalidOrMissingAuthorizationData](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeinvalidormissingauthorizationdata)Added [HMErrorCodeNotAuthorizedForMicrophoneAccess](https://developer.apple.com/documentation/homekit/hmerror/code/notauthorizedformicrophoneaccess)

#### HMEventTrigger.h

Modified [HMSignificantEventSunrise](https://developer.apple.com/documentation/homekit/hmsignificantevent/1624412-sunrise)

|  | Header |
| --- | --- |
| From | HomeKit/HMEventTrigger.h |
| To | HomeKit/HMSignificantEvents.h |

Modified [HMSignificantEventSunset](https://developer.apple.com/documentation/homekit/hmsignificantevent/1624417-sunset)

|  | Header |
| --- | --- |
| From | HomeKit/HMEventTrigger.h |
| To | HomeKit/HMSignificantEvents.h |

#### HMService.h

Added [HMService.linkedServices](https://developer.apple.com/documentation/homekit/hmservice/1650058-linkedservices)Added [HMService.primaryService](https://developer.apple.com/documentation/homekit/hmservice/1650059-primaryservice)

#### HMServiceTypes.h

Added [HMServiceTypeCameraControl](https://developer.apple.com/documentation/homekit/hmservicetypecameracontrol)Added [HMServiceTypeCameraRTPStreamManagement](https://developer.apple.com/documentation/homekit/hmservicetypecamerartpstreammanagement)Added [HMServiceTypeDoorbell](https://developer.apple.com/documentation/homekit/hmservicetypedoorbell)Added [HMServiceTypeMicrophone](https://developer.apple.com/documentation/homekit/hmservicetypemicrophone)Added [HMServiceTypeSpeaker](https://developer.apple.com/documentation/homekit/hmservicetypespeaker)

#### HMSignificantEvents.h (Added)

Modified [HMSignificantEventSunrise](https://developer.apple.com/documentation/homekit/hmsignificantevent/1624412-sunrise)

|  | Header |
| --- | --- |
| From | HomeKit/HMEventTrigger.h |
| To | HomeKit/HMSignificantEvents.h |

Modified [HMSignificantEventSunset](https://developer.apple.com/documentation/homekit/hmsignificantevent/1624417-sunset)

|  | Header |
| --- | --- |
| From | HomeKit/HMEventTrigger.h |
| To | HomeKit/HMSignificantEvents.h |

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
