---
title: watchOS 3.0 API Diffs
apple_id: TP40017328
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS30APIDiffs/Swift/HomeKit.html
archived_at: '2026-07-18T02:58:30.645859Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.0 API Diffs](watchOS%202.2%20to%20watchOS%203.0%20API%20Differences.md)


# HomeKit Changes for Swift

### HomeKit

Added [HMAccessory.cameraProfiles](https://developer.apple.com/documentation/homekit/hmaccessory/1650056-cameraprofiles)Added [HMAccessoryProfile](https://developer.apple.com/documentation/homekit/hmaccessoryprofile)Added [HMAccessoryProfile.accessory](https://developer.apple.com/documentation/homekit/hmaccessoryprofile/1649077-accessory)Added [HMAccessoryProfile.services](https://developer.apple.com/documentation/homekit/hmaccessoryprofile/1649075-services)Added [HMAccessoryProfile.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmaccessoryprofile/1649076-uniqueidentifier)Added [HMActionSet.lastExecutionDate](https://developer.apple.com/documentation/homekit/hmactionset/1649437-lastexecutiondate)Added [HMCameraAudioControl](https://developer.apple.com/documentation/homekit/hmcameraaudiocontrol)Added [HMCameraAudioControl.mute](https://developer.apple.com/documentation/homekit/hmcameraaudiocontrol/1649451-mute)Added [HMCameraAudioControl.volume](https://developer.apple.com/documentation/homekit/hmcameraaudiocontrol/1649444-volume)Added [HMCameraAudioStreamSetting [enum]](https://developer.apple.com/documentation/homekit/hmcameraaudiostreamsetting)Added [HMCameraAudioStreamSetting.bidirectionalAudioAllowed](https://developer.apple.com/documentation/homekit/hmcameraaudiostreamsetting/bidirectionalaudioallowed)Added [HMCameraAudioStreamSetting.incomingAudioAllowed](https://developer.apple.com/documentation/homekit/hmcameraaudiostreamsetting/incomingaudioallowed)Added [HMCameraAudioStreamSetting.muted](https://developer.apple.com/documentation/homekit/hmcameraaudiostreamsetting/muted)Added [HMCameraControl](https://developer.apple.com/documentation/homekit/hmcameracontrol)Added [HMCameraProfile](https://developer.apple.com/documentation/homekit/hmcameraprofile)Added [HMCameraProfile.microphoneControl](https://developer.apple.com/documentation/homekit/hmcameraprofile/1649316-microphonecontrol)Added [HMCameraProfile.settingsControl](https://developer.apple.com/documentation/homekit/hmcameraprofile/1649313-settingscontrol)Added [HMCameraProfile.snapshotControl](https://developer.apple.com/documentation/homekit/hmcameraprofile/1833282-snapshotcontrol)Added [HMCameraProfile.speakerControl](https://developer.apple.com/documentation/homekit/hmcameraprofile/1649318-speakercontrol)Added [HMCameraProfile.streamControl](https://developer.apple.com/documentation/homekit/hmcameraprofile/1649314-streamcontrol)Added [HMCameraSettingsControl](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol)Added [HMCameraSettingsControl.currentHorizontalTilt](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1829447-currenthorizontaltilt)Added [HMCameraSettingsControl.currentVerticalTilt](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1829448-currentverticaltilt)Added [HMCameraSettingsControl.digitalZoom](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1649954-digitalzoom)Added [HMCameraSettingsControl.imageMirroring](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1649935-imagemirroring)Added [HMCameraSettingsControl.imageRotation](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1649955-imagerotation)Added [HMCameraSettingsControl.nightVision](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1649936-nightvision)Added [HMCameraSettingsControl.opticalZoom](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1649946-opticalzoom)Added [HMCameraSettingsControl.targetHorizontalTilt](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1829450-targethorizontaltilt)Added [HMCameraSettingsControl.targetVerticalTilt](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/1829449-targetverticaltilt)Added [HMCameraSnapshot](https://developer.apple.com/documentation/homekit/hmcamerasnapshot)Added [HMCameraSnapshot.captureDate](https://developer.apple.com/documentation/homekit/hmcamerasnapshot/1833285-capturedate)Added [HMCameraSnapshotControl](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontrol)Added [HMCameraSnapshotControl.delegate](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontrol/1833267-delegate)Added [HMCameraSnapshotControl.mostRecentSnapshot](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontrol/1833272-mostrecentsnapshot)Added [HMCameraSnapshotControl.takeSnapshot()](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontrol/1833270-takesnapshot)Added [HMCameraSnapshotControlDelegate](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontroldelegate)Added [HMCameraSnapshotControlDelegate.cameraSnapshotControl(_: HMCameraSnapshotControl, didTake: HMCameraSnapshot?, error: Error?)](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontroldelegate/1833265-camerasnapshotcontrol)Added [HMCameraSource](https://developer.apple.com/documentation/homekit/hmcamerasource)Added [HMCameraStream](https://developer.apple.com/documentation/homekit/hmcamerastream)Added [HMCameraStream.audioStreamSetting](https://developer.apple.com/documentation/homekit/hmcamerastream/1833317-audiostreamsetting)Added [HMCameraStream.setAudioStreamSetting(_: HMCameraAudioStreamSetting)](https://developer.apple.com/documentation/homekit/hmcamerastream/2143155-setaudiostreamsetting)Added [HMCameraStream.updateAudioStreamSetting(_: HMCameraAudioStreamSetting, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/homekit/hmcamerastream/2143154-updateaudiostreamsetting)Added [HMCameraStreamControl](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol)Added [HMCameraStreamControl.cameraStream](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol/1833307-camerastream)Added [HMCameraStreamControl.delegate](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol/1649676-delegate)Added [HMCameraStreamControl.startStream()](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol/1833311-startstream)Added [HMCameraStreamControl.stopStream()](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol/1833308-stopstream)Added [HMCameraStreamControl.streamState](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol/1649686-streamstate)Added [HMCameraStreamControlDelegate](https://developer.apple.com/documentation/homekit/hmcamerastreamcontroldelegate)Added [HMCameraStreamControlDelegate.cameraStreamControl(_: HMCameraStreamControl, didStopStreamWithError: Error?)](https://developer.apple.com/documentation/homekit/hmcamerastreamcontroldelegate/1833309-camerastreamcontrol)Added [HMCameraStreamControlDelegate.cameraStreamControlDidStartStream(_: HMCameraStreamControl)](https://developer.apple.com/documentation/homekit/hmcamerastreamcontroldelegate/1833310-camerastreamcontroldidstartstrea)Added [HMCameraStreamState [enum]](https://developer.apple.com/documentation/homekit/hmcamerastreamstate)Added [HMCameraStreamState.notStreaming](https://developer.apple.com/documentation/homekit/hmcamerastreamstate/notstreaming)Added [HMCameraStreamState.starting](https://developer.apple.com/documentation/homekit/hmcamerastreamstate/starting)Added [HMCameraStreamState.stopping](https://developer.apple.com/documentation/homekit/hmcamerastreamstate/hmcamerastreamstatestopping)Added [HMCameraStreamState.streaming](https://developer.apple.com/documentation/homekit/hmcamerastreamstate/hmcamerastreamstatestreaming)Added [HMCharacteristicMetadata.validValues](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata/1649244-validvalues)Added [HMCharacteristicValueBatteryStatus [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluebatterystatus)Added [HMCharacteristicValueBatteryStatus.low](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluebatterystatus/hmcharacteristicvaluebatterystatuslow)Added [HMCharacteristicValueBatteryStatus.normal](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluebatterystatus/hmcharacteristicvaluebatterystatusnormal)Added [HMCharacteristicValueCarbonDioxideDetectionStatus [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecarbondioxidedetectionstatus)Added [HMCharacteristicValueCarbonDioxideDetectionStatus.detected](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecarbondioxidedetectionstatus/hmcharacteristicvaluecarbondioxidedetectionstatusdetected)Added [HMCharacteristicValueCarbonDioxideDetectionStatus.notDetected](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecarbondioxidedetectionstatus/hmcharacteristicvaluecarbondioxidedetectionstatusnotdetected)Added [HMCharacteristicValueCarbonMonoxideDetectionStatus [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecarbonmonoxidedetectionstatus)Added [HMCharacteristicValueCarbonMonoxideDetectionStatus.detected](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecarbonmonoxidedetectionstatus/hmcharacteristicvaluecarbonmonoxidedetectionstatusdetected)Added [HMCharacteristicValueCarbonMonoxideDetectionStatus.notDetected](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecarbonmonoxidedetectionstatus/notdetected)Added [HMCharacteristicValueChargingState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluechargingstate)Added [HMCharacteristicValueChargingState.inProgress](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluechargingstate/inprogress)Added [HMCharacteristicValueChargingState.none](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluechargingstate/none)Added [HMCharacteristicValueContactState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecontactstate)Added [HMCharacteristicValueContactState.detected](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecontactstate/detected)Added [HMCharacteristicValueContactState.none](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecontactstate/none)Added [HMCharacteristicValueJammedStatus [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluejammedstatus)Added [HMCharacteristicValueJammedStatus.jammed](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluejammedstatus/hmcharacteristicvaluejammedstatusjammed)Added [HMCharacteristicValueJammedStatus.none](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluejammedstatus/hmcharacteristicvaluejammedstatusnone)Added [HMCharacteristicValueLeakStatus [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueleakstatus)Added [HMCharacteristicValueLeakStatus.detected](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueleakstatus/detected)Added [HMCharacteristicValueLeakStatus.none](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueleakstatus/hmcharacteristicvalueleakstatusnone)Added [HMCharacteristicValueOccupancyStatus [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueoccupancystatus)Added [HMCharacteristicValueOccupancyStatus.notOccupied](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueoccupancystatus/hmcharacteristicvalueoccupancystatusnotoccupied)Added [HMCharacteristicValueOccupancyStatus.occupied](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueoccupancystatus/hmcharacteristicvalueoccupancystatusoccupied)Added [HMCharacteristicValueSecuritySystemAlarmType [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluesecuritysystemalarmtype)Added [HMCharacteristicValueSecuritySystemAlarmType.noAlarm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluesecuritysystemalarmtype/hmcharacteristicvaluesecuritysystemalarmtypenoalarm)Added [HMCharacteristicValueSecuritySystemAlarmType.unknown](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluesecuritysystemalarmtype/unknown)Added [HMCharacteristicValueSmokeDetectionStatus [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluesmokedetectionstatus)Added [HMCharacteristicValueSmokeDetectionStatus.detected](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluesmokedetectionstatus/hmcharacteristicvaluesmokedetectionstatusdetected)Added [HMCharacteristicValueSmokeDetectionStatus.none](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluesmokedetectionstatus/none)Added [HMCharacteristicValueStatusFault [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluestatusfault)Added [HMCharacteristicValueStatusFault.generalFault](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluestatusfault/hmcharacteristicvaluestatusfaultgeneralfault)Added [HMCharacteristicValueStatusFault.noFault](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluestatusfault/nofault)Added [HMCharacteristicValueTamperedStatus [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetamperedstatus)Added [HMCharacteristicValueTamperedStatus.none](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetamperedstatus/none)Added [HMCharacteristicValueTamperedStatus.tampered](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetamperedstatus/hmcharacteristicvaluetamperedstatustampered)Added [HMError [struct]](https://developer.apple.com/documentation/homekit/hmerror)Added [HMError.accessDenied](https://developer.apple.com/documentation/homekit/hmerror/2325613-accessdenied)Added [HMError.accessoryDiscoveryFailed](https://developer.apple.com/documentation/homekit/hmerror/2325654-accessorydiscoveryfailed)Added [HMError.accessoryIsBlocked](https://developer.apple.com/documentation/homekit/hmerror/2325580-accessoryisblocked)Added [HMError.accessoryIsBusy](https://developer.apple.com/documentation/homekit/hmerror/2325633-accessoryisbusy)Added [HMError.accessoryNotReachable](https://developer.apple.com/documentation/homekit/hmerror/2325615-accessorynotreachable)Added [HMError.accessoryOutOfCompliance](https://developer.apple.com/documentation/homekit/hmerror/2325658-accessoryoutofcompliance)Added [HMError.accessoryOutOfResources](https://developer.apple.com/documentation/homekit/hmerror/2325583-accessoryoutofresources)Added [HMError.accessoryPairingFailed](https://developer.apple.com/documentation/homekit/hmerror/2325626-accessorypairingfailed)Added [HMError.accessoryPoweredOff](https://developer.apple.com/documentation/homekit/hmerror/2325591-accessorypoweredoff)Added [HMError.accessoryResponseError](https://developer.apple.com/documentation/homekit/hmerror/2325659-accessoryresponseerror)Added [HMError.accessorySentInvalidResponse](https://developer.apple.com/documentation/homekit/hmerror/2325601-accessorysentinvalidresponse)Added [HMError.actionInAnotherActionSet](https://developer.apple.com/documentation/homekit/hmerror/2325611-actioninanotheractionset)Added [HMError.actionSetExecutionFailed](https://developer.apple.com/documentation/homekit/hmerror/2325637-actionsetexecutionfailed)Added [HMError.actionSetExecutionInProgress](https://developer.apple.com/documentation/homekit/hmerror/2325666-actionsetexecutioninprogress)Added [HMError.actionSetExecutionPartialSuccess](https://developer.apple.com/documentation/homekit/hmerror/2325623-actionsetexecutionpartialsuccess)Added [HMError.addAccessoryFailed](https://developer.apple.com/documentation/homekit/hmerror/2325587-addaccessoryfailed)Added [HMError.alreadyExists](https://developer.apple.com/documentation/homekit/hmerror/2325609-alreadyexists)Added [HMError.bridgedAccessoryNotReachable](https://developer.apple.com/documentation/homekit/hmerror/2325608-bridgedaccessorynotreachable)Added [HMError.cannotActivateTriggerTooFarInFuture](https://developer.apple.com/documentation/homekit/hmerror/2325621-cannotactivatetriggertoofarinfut)Added [HMError.cannotRemoveBuiltinActionSet](https://developer.apple.com/documentation/homekit/hmerror/2325634-cannotremovebuiltinactionset)Added [HMError.cannotRemoveNonBridgeAccessory](https://developer.apple.com/documentation/homekit/hmerror/2325593-cannotremovenonbridgeaccessory)Added [HMError.cannotUnblockNonBridgeAccessory](https://developer.apple.com/documentation/homekit/hmerror/2325649-cannotunblocknonbridgeaccessory)Added [HMError.clientRequestError](https://developer.apple.com/documentation/homekit/hmerror/2325640-clientrequesterror)Added [HMError.cloudDataSyncInProgress](https://developer.apple.com/documentation/homekit/hmerror/2325630-clouddatasyncinprogress)Added [HMError.communicationFailure](https://developer.apple.com/documentation/homekit/hmerror/2325605-communicationfailure)Added [HMError.dataResetFailure](https://developer.apple.com/documentation/homekit/hmerror/2325597-dataresetfailure)Added [HMError.dateMustBeOnSpecifiedBoundaries](https://developer.apple.com/documentation/homekit/hmerror/2325620-datemustbeonspecifiedboundaries)Added [HMError.deviceLocked](https://developer.apple.com/documentation/homekit/hmerror/2325604-devicelocked)Added [HMError.fireDateInPast](https://developer.apple.com/documentation/homekit/hmerror/2325584-firedateinpast)Added [HMError.genericError](https://developer.apple.com/documentation/homekit/hmerror/2325603-genericerror)Added [HMError.homeAccessNotAuthorized](https://developer.apple.com/documentation/homekit/hmerror/2325650-homeaccessnotauthorized)Added [HMError.homeWithSimilarNameExists](https://developer.apple.com/documentation/homekit/hmerror/2325641-homewithsimilarnameexists)Added HMError.init(_nsError: NSError)Added [HMError.insufficientPrivileges](https://developer.apple.com/documentation/homekit/hmerror/2325642-insufficientprivileges)Added [HMError.invalidAssociatedServiceType](https://developer.apple.com/documentation/homekit/hmerror/2325598-invalidassociatedservicetype)Added [HMError.invalidClass](https://developer.apple.com/documentation/homekit/hmerror/2325661-invalidclass)Added [HMError.invalidDataFormatSpecified](https://developer.apple.com/documentation/homekit/hmerror/2325594-invaliddataformatspecified)Added [HMError.invalidMessageSize](https://developer.apple.com/documentation/homekit/hmerror/2325663-invalidmessagesize)Added [HMError.invalidOrMissingAuthorizationData](https://developer.apple.com/documentation/homekit/hmerror/2325639-invalidormissingauthorizationdat)Added [HMError.invalidParameter](https://developer.apple.com/documentation/homekit/hmerror/2325602-invalidparameter)Added [HMError.invalidValueType](https://developer.apple.com/documentation/homekit/hmerror/2325595-invalidvaluetype)Added [HMError.keychainSyncNotEnabled](https://developer.apple.com/documentation/homekit/hmerror/2325610-keychainsyncnotenabled)Added [HMError.locationForHomeDisabled](https://developer.apple.com/documentation/homekit/hmerror/2325643-locationforhomedisabled)Added [HMError.maximumObjectLimitReached](https://developer.apple.com/documentation/homekit/hmerror/2325599-maximumobjectlimitreached)Added [HMError.messageAuthenticationFailed](https://developer.apple.com/documentation/homekit/hmerror/2325582-messageauthenticationfailed)Added [HMError.missingEntitlement](https://developer.apple.com/documentation/homekit/hmerror/2325638-missingentitlement)Added [HMError.missingParameter](https://developer.apple.com/documentation/homekit/hmerror/2325651-missingparameter)Added [HMError.nameContainsProhibitedCharacters](https://developer.apple.com/documentation/homekit/hmerror/2325646-namecontainsprohibitedcharacters)Added [HMError.nameDoesNotEndWithValidCharacters](https://developer.apple.com/documentation/homekit/hmerror/2325655-namedoesnotendwithvalidcharacter)Added [HMError.nameDoesNotStartWithValidCharacters](https://developer.apple.com/documentation/homekit/hmerror/2325656-namedoesnotstartwithvalidcharact)Added [HMError.networkUnavailable](https://developer.apple.com/documentation/homekit/hmerror/2325622-networkunavailable)Added [HMError.nilParameter](https://developer.apple.com/documentation/homekit/hmerror/2325625-nilparameter)Added [HMError.noActionsInActionSet](https://developer.apple.com/documentation/homekit/hmerror/2325606-noactionsinactionset)Added [HMError.noRegisteredActionSets](https://developer.apple.com/documentation/homekit/hmerror/2325657-noregisteredactionsets)Added [HMError.notAuthorizedForLocationServices](https://developer.apple.com/documentation/homekit/hmerror/2325590-notauthorizedforlocationservices)Added [HMError.notAuthorizedForMicrophoneAccess](https://developer.apple.com/documentation/homekit/hmerror/2325624-notauthorizedformicrophoneaccess)Added [HMError.notFound](https://developer.apple.com/documentation/homekit/hmerror/2325645-notfound)Added [HMError.notificationAlreadyEnabled](https://developer.apple.com/documentation/homekit/hmerror/2325665-notificationalreadyenabled)Added [HMError.notificationNotSupported](https://developer.apple.com/documentation/homekit/hmerror/2325648-notificationnotsupported)Added [HMError.notSignedIntoiCloud](https://developer.apple.com/documentation/homekit/hmerror/2325588-notsignedintoicloud)Added [HMError.objectAlreadyAssociatedToHome](https://developer.apple.com/documentation/homekit/hmerror/2325662-objectalreadyassociatedtohome)Added [HMError.objectAssociatedToAnotherHome](https://developer.apple.com/documentation/homekit/hmerror/2325589-objectassociatedtoanotherhome)Added [HMError.objectNotAssociatedToAnyHome](https://developer.apple.com/documentation/homekit/hmerror/2325632-objectnotassociatedtoanyhome)Added [HMError.objectWithSimilarNameExistsInHome](https://developer.apple.com/documentation/homekit/hmerror/2325586-objectwithsimilarnameexistsinhom)Added [HMError.operationCancelled](https://developer.apple.com/documentation/homekit/hmerror/2325617-operationcancelled)Added [HMError.operationInProgress](https://developer.apple.com/documentation/homekit/hmerror/2325631-operationinprogress)Added [HMError.operationNotSupported](https://developer.apple.com/documentation/homekit/hmerror/2325635-operationnotsupported)Added [HMError.operationTimedOut](https://developer.apple.com/documentation/homekit/hmerror/2325664-operationtimedout)Added [HMError.readOnlyCharacteristic](https://developer.apple.com/documentation/homekit/hmerror/2325667-readonlycharacteristic)Added [HMError.readWriteFailure](https://developer.apple.com/documentation/homekit/hmerror/2325636-readwritefailure)Added [HMError.readWritePartialSuccess](https://developer.apple.com/documentation/homekit/hmerror/2325653-readwritepartialsuccess)Added [HMError.recurrenceMustBeOnSpecifiedBoundaries](https://developer.apple.com/documentation/homekit/hmerror/2325629-recurrencemustbeonspecifiedbound)Added [HMError.recurrenceTooLarge](https://developer.apple.com/documentation/homekit/hmerror/2325585-recurrencetoolarge)Added [HMError.recurrenceTooSmall](https://developer.apple.com/documentation/homekit/hmerror/2325616-recurrencetoosmall)Added [HMError.referToUserManual](https://developer.apple.com/documentation/homekit/hmerror/2325600-refertousermanual)Added [HMError.renameWithSimilarName](https://developer.apple.com/documentation/homekit/hmerror/2325592-renamewithsimilarname)Added [HMError.roomForHomeCannotBeInZone](https://developer.apple.com/documentation/homekit/hmerror/2325614-roomforhomecannotbeinzone)Added [HMError.roomForHomeCannotBeUpdated](https://developer.apple.com/documentation/homekit/hmerror/2325668-roomforhomecannotbeupdated)Added [HMError.securityFailure](https://developer.apple.com/documentation/homekit/hmerror/2325627-securityfailure)Added [HMError.stringLongerThanMaximum](https://developer.apple.com/documentation/homekit/hmerror/2325652-stringlongerthanmaximum)Added [HMError.stringShorterThanMinimum](https://developer.apple.com/documentation/homekit/hmerror/2325618-stringshorterthanminimum)Added [HMError.unconfiguredParameter](https://developer.apple.com/documentation/homekit/hmerror/2325619-unconfiguredparameter)Added [HMError.userDeclinedAddingUser](https://developer.apple.com/documentation/homekit/hmerror/2325612-userdeclinedaddinguser)Added [HMError.userDeclinedInvite](https://developer.apple.com/documentation/homekit/hmerror/2325596-userdeclinedinvite)Added [HMError.userDeclinedRemovingUser](https://developer.apple.com/documentation/homekit/hmerror/2325660-userdeclinedremovinguser)Added [HMError.userIDNotEmailAddress](https://developer.apple.com/documentation/homekit/hmerror/2325628-useridnotemailaddress)Added [HMError.userManagementFailed](https://developer.apple.com/documentation/homekit/hmerror/2325607-usermanagementfailed)Added [HMError.valueHigherThanMaximum](https://developer.apple.com/documentation/homekit/hmerror/2325644-valuehigherthanmaximum)Added [HMError.valueLowerThanMinimum](https://developer.apple.com/documentation/homekit/hmerror/2325647-valuelowerthanminimum)Added [HMError.writeOnlyCharacteristic](https://developer.apple.com/documentation/homekit/hmerror/2325581-writeonlycharacteristic)Added [HMError.Code.bridgedAccessoryNotReachable](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodebridgedaccessorynotreachable)Added [HMError.Code.invalidOrMissingAuthorizationData](https://developer.apple.com/documentation/homekit/hmerror/code/invalidormissingauthorizationdata)Added [HMError.Code.notAuthorizedForMicrophoneAccess](https://developer.apple.com/documentation/homekit/hmerror/code/notauthorizedformicrophoneaccess)Added [HMService.isPrimaryService](https://developer.apple.com/documentation/homekit/hmservice/1650059-primaryservice)Added [HMService.linkedServices](https://developer.apple.com/documentation/homekit/hmservice/1650058-linkedservices)Added [HMAccessoryCategoryTypeIPCamera](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypeipcamera)Added [HMAccessoryCategoryTypeVideoDoorbell](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypevideodoorbell)Added [HMActionSetTypeTriggerOwned](https://developer.apple.com/documentation/homekit/hmactionsettypetriggerowned)Added [HMCharacteristicMetadataUnitsMicrogramsPerCubicMeter](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadataunitsmicrogramspercubicmeter)Added [HMCharacteristicMetadataUnitsPartsPerMillion](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadataunitspartspermillion)Added [HMCharacteristicPropertySupportsEventNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1616329-hmcharacteristicpropertysupports)Added [HMCharacteristicTypeDigitalZoom](https://developer.apple.com/documentation/homekit/hmcharacteristictypedigitalzoom)Added [HMCharacteristicTypeImageMirroring](https://developer.apple.com/documentation/homekit/hmcharacteristictypeimagemirroring)Added [HMCharacteristicTypeImageRotation](https://developer.apple.com/documentation/homekit/hmcharacteristictypeimagerotation)Added [HMCharacteristicTypeMute](https://developer.apple.com/documentation/homekit/hmcharacteristictypemute)Added [HMCharacteristicTypeNightVision](https://developer.apple.com/documentation/homekit/hmcharacteristictypenightvision)Added [HMCharacteristicTypeOpticalZoom](https://developer.apple.com/documentation/homekit/hmcharacteristictypeopticalzoom)Added [HMCharacteristicTypeSelectedStreamConfiguration](https://developer.apple.com/documentation/homekit/hmcharacteristictypeselectedstreamconfiguration)Added [HMCharacteristicTypeSetupStreamEndpoint](https://developer.apple.com/documentation/homekit/hmcharacteristictypesetupstreamendpoint)Added [HMCharacteristicTypeStreamingStatus](https://developer.apple.com/documentation/homekit/hmcharacteristictypestreamingstatus)Added [HMCharacteristicTypeSupportedAudioStreamConfiguration](https://developer.apple.com/documentation/homekit/hmcharacteristictypesupportedaudiostreamconfiguration)Added [HMCharacteristicTypeSupportedRTPConfiguration](https://developer.apple.com/documentation/homekit/hmcharacteristictypesupportedrtpconfiguration)Added [HMCharacteristicTypeSupportedVideoStreamConfiguration](https://developer.apple.com/documentation/homekit/hmcharacteristictypesupportedvideostreamconfiguration)Added [HMCharacteristicTypeVolume](https://developer.apple.com/documentation/homekit/hmcharacteristictypevolume)Added [HMServiceTypeCameraControl](https://developer.apple.com/documentation/homekit/hmservicetypecameracontrol)Added [HMServiceTypeCameraRTPStreamManagement](https://developer.apple.com/documentation/homekit/hmservicetypecamerartpstreammanagement)Added [HMServiceTypeDoorbell](https://developer.apple.com/documentation/homekit/hmservicetypedoorbell)Added [HMServiceTypeMicrophone](https://developer.apple.com/documentation/homekit/hmservicetypemicrophone)Added [HMServiceTypeSpeaker](https://developer.apple.com/documentation/homekit/hmservicetypespeaker)Modified [HMAccessory](https://developer.apple.com/documentation/homekit/hmaccessory)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMAccessory : NSObject {     var name: String { get }     @NSCopying var identifier: NSUUID { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     weak var delegate: HMAccessoryDelegate?     var reachable: Bool { get }     var bridged: Bool { get }     var identifiersForBridgedAccessories: [NSUUID]? { get }     var uniqueIdentifiersForBridgedAccessories: [NSUUID]? { get }     var category: HMAccessoryCategory { get }     weak var room: HMRoom? { get }     var services: [HMService] { get }     var blocked: Bool { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void)     func identifyWithCompletionHandler(_ completion: (NSError?) -> Void) } ``` | -- |
| To | ``` class HMAccessory : NSObject {     var name: String { get }     var identifier: UUID { get }     var uniqueIdentifier: UUID { get }     weak var delegate: HMAccessoryDelegate?     var isReachable: Bool { get }     var isBridged: Bool { get }     var identifiersForBridgedAccessories: [UUID]? { get }     var uniqueIdentifiersForBridgedAccessories: [UUID]? { get }     var category: HMAccessoryCategory { get }     weak var room: HMRoom? { get }     var services: [HMService] { get }     var isBlocked: Bool { get }     func updateName(_ name: String, completionHandler completion: @escaping (Error?) -> Swift.Void)     func identify(completionHandler completion: @escaping (Error?) -> Swift.Void)     var cameraProfiles: [HMCameraProfile]? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMAccessory : CVarArg { } extension HMAccessory : Equatable, Hashable {     var hashValue: Int { get } } extension HMAccessory {     var cameraProfiles: [HMCameraProfile]? { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMAccessory.identify(completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/homekit/hmaccessory/1615259-identify)

|  | Declaration |
| --- | --- |
| From | ``` func identifyWithCompletionHandler(_ completion: (NSError?) -> Void) ``` |
| To | ``` func identify(completionHandler completion: @escaping (Error?) -> Swift.Void) ``` |

Modified [HMAccessory.isBlocked](https://developer.apple.com/documentation/homekit/hmaccessory/1615288-isblocked)

|  | Declaration |
| --- | --- |
| From | ``` var blocked: Bool { get } ``` |
| To | ``` var isBlocked: Bool { get } ``` |

Modified [HMAccessory.isBridged](https://developer.apple.com/documentation/homekit/hmaccessory/1615251-isbridged)

|  | Declaration |
| --- | --- |
| From | ``` var bridged: Bool { get } ``` |
| To | ``` var isBridged: Bool { get } ``` |

Modified [HMAccessory.isReachable](https://developer.apple.com/documentation/homekit/hmaccessory/1615257-reachable)

|  | Declaration |
| --- | --- |
| From | ``` var reachable: Bool { get } ``` |
| To | ``` var isReachable: Bool { get } ``` |

Modified [HMAccessory.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmaccessory/1615261-uniqueidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var uniqueIdentifier: NSUUID { get } ``` |
| To | ``` var uniqueIdentifier: UUID { get } ``` |

Modified [HMAccessory.uniqueIdentifiersForBridgedAccessories](https://developer.apple.com/documentation/homekit/hmaccessory/1615278-uniqueidentifiersforbridgedacces)

|  | Declaration |
| --- | --- |
| From | ``` var uniqueIdentifiersForBridgedAccessories: [NSUUID]? { get } ``` |
| To | ``` var uniqueIdentifiersForBridgedAccessories: [UUID]? { get } ``` |

Modified [HMAccessoryCategory](https://developer.apple.com/documentation/homekit/hmaccessorycategory)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMAccessoryCategory : NSObject {     var categoryType: String { get }     var localizedDescription: String { get } } ``` | -- |
| To | ``` class HMAccessoryCategory : NSObject {     var categoryType: String { get }     var localizedDescription: String { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMAccessoryCategory : CVarArg { } extension HMAccessoryCategory : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMAccessoryDelegate](https://developer.apple.com/documentation/homekit/hmaccessorydelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol HMAccessoryDelegate : NSObjectProtocol {     optional func accessoryDidUpdateName(_ accessory: HMAccessory)     optional func accessory(_ accessory: HMAccessory, didUpdateNameForService service: HMService)     optional func accessory(_ accessory: HMAccessory, didUpdateAssociatedServiceTypeForService service: HMService)     optional func accessoryDidUpdateServices(_ accessory: HMAccessory)     optional func accessoryDidUpdateReachability(_ accessory: HMAccessory)     optional func accessory(_ accessory: HMAccessory, service service: HMService, didUpdateValueForCharacteristic characteristic: HMCharacteristic) } ``` |
| To | ``` protocol HMAccessoryDelegate : NSObjectProtocol {     optional func accessoryDidUpdateName(_ accessory: HMAccessory)     optional func accessory(_ accessory: HMAccessory, didUpdateNameFor service: HMService)     optional func accessory(_ accessory: HMAccessory, didUpdateAssociatedServiceTypeFor service: HMService)     optional func accessoryDidUpdateServices(_ accessory: HMAccessory)     optional func accessoryDidUpdateReachability(_ accessory: HMAccessory)     optional func accessory(_ accessory: HMAccessory, service service: HMService, didUpdateValueFor characteristic: HMCharacteristic) } ``` |

Modified [HMAccessoryDelegate.accessory(_: HMAccessory, didUpdateAssociatedServiceTypeFor: HMService)](https://developer.apple.com/documentation/homekit/hmaccessorydelegate/1615267-accessory)

|  | Declaration |
| --- | --- |
| From | ``` optional func accessory(_ accessory: HMAccessory, didUpdateAssociatedServiceTypeForService service: HMService) ``` |
| To | ``` optional func accessory(_ accessory: HMAccessory, didUpdateAssociatedServiceTypeFor service: HMService) ``` |

Modified [HMAccessoryDelegate.accessory(_: HMAccessory, didUpdateNameFor: HMService)](https://developer.apple.com/documentation/homekit/hmaccessorydelegate/1615263-accessory)

|  | Declaration |
| --- | --- |
| From | ``` optional func accessory(_ accessory: HMAccessory, didUpdateNameForService service: HMService) ``` |
| To | ``` optional func accessory(_ accessory: HMAccessory, didUpdateNameFor service: HMService) ``` |

Modified [HMAccessoryDelegate.accessory(_: HMAccessory, service: HMService, didUpdateValueFor: HMCharacteristic)](https://developer.apple.com/documentation/homekit/hmaccessorydelegate/1615286-accessory)

|  | Declaration |
| --- | --- |
| From | ``` optional func accessory(_ accessory: HMAccessory, service service: HMService, didUpdateValueForCharacteristic characteristic: HMCharacteristic) ``` |
| To | ``` optional func accessory(_ accessory: HMAccessory, service service: HMService, didUpdateValueFor characteristic: HMCharacteristic) ``` |

Modified [HMAction](https://developer.apple.com/documentation/homekit/hmaction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMAction : NSObject {     @NSCopying var uniqueIdentifier: NSUUID { get } } ``` | -- |
| To | ``` class HMAction : NSObject {     var uniqueIdentifier: UUID { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMAction : CVarArg { } extension HMAction : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMAction.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmaction/1624923-uniqueidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var uniqueIdentifier: NSUUID { get } ``` |
| To | ``` var uniqueIdentifier: UUID { get } ``` |

Modified [HMActionSet](https://developer.apple.com/documentation/homekit/hmactionset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMActionSet : NSObject {     init()     var name: String { get }     var actions: Set<HMAction> { get }     var executing: Bool { get }     var actionSetType: String { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void)     func addAction(_ action: HMAction, completionHandler completion: (NSError?) -> Void)     func removeAction(_ action: HMAction, completionHandler completion: (NSError?) -> Void) } ``` | -- |
| To | ``` class HMActionSet : NSObject {     init()     var name: String { get }     var actions: Set<HMAction> { get }     var isExecuting: Bool { get }     var actionSetType: String { get }     var uniqueIdentifier: UUID { get }     var lastExecutionDate: Date { get }     func updateName(_ name: String, completionHandler completion: @escaping (Error?) -> Swift.Void)     func addAction(_ action: HMAction, completionHandler completion: @escaping (Error?) -> Swift.Void)     func removeAction(_ action: HMAction, completionHandler completion: @escaping (Error?) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMActionSet : CVarArg { } extension HMActionSet : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMActionSet.isExecuting](https://developer.apple.com/documentation/homekit/hmactionset/1616792-executing)

|  | Declaration |
| --- | --- |
| From | ``` var executing: Bool { get } ``` |
| To | ``` var isExecuting: Bool { get } ``` |

Modified [HMActionSet.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmactionset/1616789-uniqueidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var uniqueIdentifier: NSUUID { get } ``` |
| To | ``` var uniqueIdentifier: UUID { get } ``` |

Modified [HMCharacteristic](https://developer.apple.com/documentation/homekit/hmcharacteristic)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMCharacteristic : NSObject {     var characteristicType: String { get }     var localizedDescription: String { get }     weak var service: HMService? { get }     var properties: [String] { get }     var metadata: HMCharacteristicMetadata? { get }     @NSCopying var value: AnyObject? { get }     var notificationEnabled: Bool { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     func writeValue(_ value: AnyObject?, completionHandler completion: (NSError?) -> Void)     func readValueWithCompletionHandler(_ completion: (NSError?) -> Void)     func enableNotification(_ enable: Bool, completionHandler completion: (NSError?) -> Void)     func updateAuthorizationData(_ data: NSData?, completionHandler completion: (NSError?) -> Void) } ``` | -- |
| To | ``` class HMCharacteristic : NSObject {     var characteristicType: String { get }     var localizedDescription: String { get }     weak var service: HMService? { get }     var properties: [String] { get }     var metadata: HMCharacteristicMetadata? { get }     var value: Any? { get }     var isNotificationEnabled: Bool { get }     var uniqueIdentifier: UUID { get }     func writeValue(_ value: Any?, completionHandler completion: @escaping (Error?) -> Swift.Void)     func readValue(completionHandler completion: @escaping (Error?) -> Swift.Void)     func enableNotification(_ enable: Bool, completionHandler completion: @escaping (Error?) -> Swift.Void)     func updateAuthorizationData(_ data: Data?, completionHandler completion: @escaping (Error?) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMCharacteristic : CVarArg { } extension HMCharacteristic : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMCharacteristic.enableNotification(_: Bool, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624189-enablenotification)

|  | Declaration |
| --- | --- |
| From | ``` func enableNotification(_ enable: Bool, completionHandler completion: (NSError?) -> Void) ``` |
| To | ``` func enableNotification(_ enable: Bool, completionHandler completion: @escaping (Error?) -> Swift.Void) ``` |

Modified [HMCharacteristic.isNotificationEnabled](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624190-notificationenabled)

|  | Declaration |
| --- | --- |
| From | ``` var notificationEnabled: Bool { get } ``` |
| To | ``` var isNotificationEnabled: Bool { get } ``` |

Modified [HMCharacteristic.readValue(completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624188-readvaluewithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func readValueWithCompletionHandler(_ completion: (NSError?) -> Void) ``` |
| To | ``` func readValue(completionHandler completion: @escaping (Error?) -> Swift.Void) ``` |

Modified [HMCharacteristic.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624187-uniqueidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var uniqueIdentifier: NSUUID { get } ``` |
| To | ``` var uniqueIdentifier: UUID { get } ``` |

Modified [HMCharacteristic.value](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624195-value)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var value: AnyObject? { get } ``` |
| To | ``` var value: Any? { get } ``` |

Modified [HMCharacteristic.writeValue(_: Any?, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624191-writevalue)

|  | Declaration |
| --- | --- |
| From | ``` func writeValue(_ value: AnyObject?, completionHandler completion: (NSError?) -> Void) ``` |
| To | ``` func writeValue(_ value: Any?, completionHandler completion: @escaping (Error?) -> Swift.Void) ``` |

Modified [HMCharacteristicEvent](https://developer.apple.com/documentation/homekit/hmcharacteristicevent)

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` class HMCharacteristicEvent : HMEvent {     init()     init(characteristic characteristic: HMCharacteristic, triggerValue triggerValue: NSCopying?)     var characteristic: HMCharacteristic { get }     @NSCopying var triggerValue: NSCopying? { get }     func updateTriggerValue(_ triggerValue: NSCopying?, completionHandler completion: (NSError?) -> Void) } ``` | ```  ``` | -- |
| To | ``` class HMCharacteristicEvent<TriggerValueType : NSCopying> : HMEvent {     init()     init(characteristic characteristic: HMCharacteristic, triggerValue triggerValue: TriggerValueType?)     var characteristic: HMCharacteristic { get }     @NSCopying var triggerValue: TriggerValueType? { get }     func updateTriggerValue(_ triggerValue: TriggerValueType?, completionHandler completion: @escaping (Error?) -> Swift.Void) } ``` | ``` TriggerValueType : NSCopying ``` | TriggerValueType |

Modified [HMCharacteristicEvent.triggerValue](https://developer.apple.com/documentation/homekit/hmcharacteristicevent/1617200-triggervalue)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var triggerValue: NSCopying? { get } ``` |
| To | ``` @NSCopying var triggerValue: TriggerValueType? { get } ``` |

Modified [HMCharacteristicMetadata](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMCharacteristicMetadata : NSObject {     var minimumValue: NSNumber? { get }     var maximumValue: NSNumber? { get }     var stepValue: NSNumber? { get }     var maxLength: NSNumber? { get }     var format: String? { get }     var units: String? { get }     var manufacturerDescription: String? { get } } ``` | -- |
| To | ``` class HMCharacteristicMetadata : NSObject {     var minimumValue: NSNumber? { get }     var maximumValue: NSNumber? { get }     var stepValue: NSNumber? { get }     var maxLength: NSNumber? { get }     var format: String? { get }     var units: String? { get }     var manufacturerDescription: String? { get }     var validValues: [NSNumber]? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMCharacteristicMetadata : CVarArg { } extension HMCharacteristicMetadata : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMCharacteristicValueAirParticulateSize [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairparticulatesize)

|  | Declaration |
| --- | --- |
| From | ``` enum HMCharacteristicValueAirParticulateSize : Int {     case Size2_5     case Size10 } ``` |
| To | ``` enum HMCharacteristicValueAirParticulateSize : Int {     case size2_5     case size10 } ``` |

Modified [HMCharacteristicValueAirParticulateSize.size10](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairparticulatesize/size10)

|  | Declaration |
| --- | --- |
| From | ``` case Size10 ``` |
| To | ``` case size10 ``` |

Modified [HMCharacteristicValueAirParticulateSize.size2_5](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairparticulatesize/hmcharacteristicvalueairparticulatesize2_5)

|  | Declaration |
| --- | --- |
| From | ``` case Size2_5 ``` |
| To | ``` case size2_5 ``` |

Modified [HMCharacteristicValueAirQuality [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality)

|  | Declaration |
| --- | --- |
| From | ``` enum HMCharacteristicValueAirQuality : Int {     case Unknown     case Excellent     case Good     case Fair     case Inferior     case Poor } ``` |
| To | ``` enum HMCharacteristicValueAirQuality : Int {     case unknown     case excellent     case good     case fair     case inferior     case poor } ``` |

Modified [HMCharacteristicValueAirQuality.excellent](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/excellent)

|  | Declaration |
| --- | --- |
| From | ``` case Excellent ``` |
| To | ``` case excellent ``` |

Modified [HMCharacteristicValueAirQuality.fair](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/hmcharacteristicvalueairqualityfair)

|  | Declaration |
| --- | --- |
| From | ``` case Fair ``` |
| To | ``` case fair ``` |

Modified [HMCharacteristicValueAirQuality.good](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/good)

|  | Declaration |
| --- | --- |
| From | ``` case Good ``` |
| To | ``` case good ``` |

Modified [HMCharacteristicValueAirQuality.inferior](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/hmcharacteristicvalueairqualityinferior)

|  | Declaration |
| --- | --- |
| From | ``` case Inferior ``` |
| To | ``` case inferior ``` |

Modified [HMCharacteristicValueAirQuality.poor](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/poor)

|  | Declaration |
| --- | --- |
| From | ``` case Poor ``` |
| To | ``` case poor ``` |

Modified [HMCharacteristicValueAirQuality.unknown](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [HMCharacteristicValueCurrentSecuritySystemState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate)

|  | Declaration |
| --- | --- |
| From | ``` enum HMCharacteristicValueCurrentSecuritySystemState : Int {     case StayArm     case AwayArm     case NightArm     case Disarmed     case Triggered } ``` |
| To | ``` enum HMCharacteristicValueCurrentSecuritySystemState : Int {     case stayArm     case awayArm     case nightArm     case disarmed     case triggered } ``` |

Modified [HMCharacteristicValueCurrentSecuritySystemState.awayArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/hmcharacteristicvaluecurrentsecuritysystemstateawayarm)

|  | Declaration |
| --- | --- |
| From | ``` case AwayArm ``` |
| To | ``` case awayArm ``` |

Modified [HMCharacteristicValueCurrentSecuritySystemState.disarmed](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/disarmed)

|  | Declaration |
| --- | --- |
| From | ``` case Disarmed ``` |
| To | ``` case disarmed ``` |

Modified [HMCharacteristicValueCurrentSecuritySystemState.nightArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/nightarm)

|  | Declaration |
| --- | --- |
| From | ``` case NightArm ``` |
| To | ``` case nightArm ``` |

Modified [HMCharacteristicValueCurrentSecuritySystemState.stayArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/hmcharacteristicvaluecurrentsecuritysystemstatestayarm)

|  | Declaration |
| --- | --- |
| From | ``` case StayArm ``` |
| To | ``` case stayArm ``` |

Modified [HMCharacteristicValueCurrentSecuritySystemState.triggered](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/triggered)

|  | Declaration |
| --- | --- |
| From | ``` case Triggered ``` |
| To | ``` case triggered ``` |

Modified [HMCharacteristicValueDoorState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluedoorstate)

|  | Declaration |
| --- | --- |
| From | ``` enum HMCharacteristicValueDoorState : Int {     case Open     case Closed     case Opening     case Closing     case Stopped } ``` |
| To | ``` enum HMCharacteristicValueDoorState : Int {     case open     case closed     case opening     case closing     case stopped } ``` |

Modified [HMCharacteristicValueDoorState.closed](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluedoorstate/hmcharacteristicvaluedoorstateclosed)

|  | Declaration |
| --- | --- |
| From | ``` case Closed ``` |
| To | ``` case closed ``` |

Modified [HMCharacteristicValueDoorState.closing](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluedoorstate/hmcharacteristicvaluedoorstateclosing)

|  | Declaration |
| --- | --- |
| From | ``` case Closing ``` |
| To | ``` case closing ``` |

Modified [HMCharacteristicValueDoorState.open](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluedoorstate/hmcharacteristicvaluedoorstateopen)

|  | Declaration |
| --- | --- |
| From | ``` case Open ``` |
| To | ``` case open ``` |

Modified [HMCharacteristicValueDoorState.opening](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluedoorstate/opening)

|  | Declaration |
| --- | --- |
| From | ``` case Opening ``` |
| To | ``` case opening ``` |

Modified [HMCharacteristicValueDoorState.stopped](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluedoorstate/hmcharacteristicvaluedoorstatestopped)

|  | Declaration |
| --- | --- |
| From | ``` case Stopped ``` |
| To | ``` case stopped ``` |

Modified [HMCharacteristicValueHeatingCooling [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueheatingcooling)

|  | Declaration |
| --- | --- |
| From | ``` enum HMCharacteristicValueHeatingCooling : Int {     case Off     case Heat     case Cool     case Auto } ``` |
| To | ``` enum HMCharacteristicValueHeatingCooling : Int {     case off     case heat     case cool     case auto } ``` |

Modified [HMCharacteristicValueHeatingCooling.auto](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueheatingcooling/auto)

|  | Declaration |
| --- | --- |
| From | ``` case Auto ``` |
| To | ``` case auto ``` |

Modified [HMCharacteristicValueHeatingCooling.cool](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueheatingcooling/hmcharacteristicvalueheatingcoolingcool)

|  | Declaration |
| --- | --- |
| From | ``` case Cool ``` |
| To | ``` case cool ``` |

Modified [HMCharacteristicValueHeatingCooling.heat](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueheatingcooling/hmcharacteristicvalueheatingcoolingheat)

|  | Declaration |
| --- | --- |
| From | ``` case Heat ``` |
| To | ``` case heat ``` |

Modified [HMCharacteristicValueHeatingCooling.off](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueheatingcooling/off)

|  | Declaration |
| --- | --- |
| From | ``` case Off ``` |
| To | ``` case off ``` |

Modified [HMCharacteristicValueLockMechanismLastKnownAction [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismlastknownaction)

|  | Declaration |
| --- | --- |
| From | ``` enum HMCharacteristicValueLockMechanismLastKnownAction : Int {     case SecuredUsingPhysicalMovementInterior     case UnsecuredUsingPhysicalMovementInterior     case SecuredUsingPhysicalMovementExterior     case UnsecuredUsingPhysicalMovementExterior     case SecuredWithKeypad     case UnsecuredWithKeypad     case SecuredRemotely     case UnsecuredRemotely     case SecuredWithAutomaticSecureTimeout     case SecuredUsingPhysicalMovement     case UnsecuredUsingPhysicalMovement } ``` |
| To | ``` enum HMCharacteristicValueLockMechanismLastKnownAction : Int {     case securedUsingPhysicalMovementInterior     case unsecuredUsingPhysicalMovementInterior     case securedUsingPhysicalMovementExterior     case unsecuredUsingPhysicalMovementExterior     case securedWithKeypad     case unsecuredWithKeypad     case securedRemotely     case unsecuredRemotely     case securedWithAutomaticSecureTimeout     case securedUsingPhysicalMovement     case unsecuredUsingPhysicalMovement } ``` |

Modified [HMCharacteristicValueLockMechanismLastKnownAction.securedRemotely](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismlastknownaction/securedremotely)

|  | Declaration |
| --- | --- |
| From | ``` case SecuredRemotely ``` |
| To | ``` case securedRemotely ``` |

Modified [HMCharacteristicValueLockMechanismLastKnownAction.securedUsingPhysicalMovement](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismlastknownaction/securedusingphysicalmovement)

|  | Declaration |
| --- | --- |
| From | ``` case SecuredUsingPhysicalMovement ``` |
| To | ``` case securedUsingPhysicalMovement ``` |

Modified [HMCharacteristicValueLockMechanismLastKnownAction.securedUsingPhysicalMovementExterior](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismlastknownaction/hmcharacteristicvaluelockmechanismlastknownactionsecuredusingphysicalmovementexterior)

|  | Declaration |
| --- | --- |
| From | ``` case SecuredUsingPhysicalMovementExterior ``` |
| To | ``` case securedUsingPhysicalMovementExterior ``` |

Modified [HMCharacteristicValueLockMechanismLastKnownAction.securedUsingPhysicalMovementInterior](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismlastknownaction/hmcharacteristicvaluelockmechanismlastknownactionsecuredusingphysicalmovementinterior)

|  | Declaration |
| --- | --- |
| From | ``` case SecuredUsingPhysicalMovementInterior ``` |
| To | ``` case securedUsingPhysicalMovementInterior ``` |

Modified [HMCharacteristicValueLockMechanismLastKnownAction.securedWithAutomaticSecureTimeout](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismlastknownaction/hmcharacteristicvaluelockmechanismlastknownactionsecuredwithautomaticsecuretimeout)

|  | Declaration |
| --- | --- |
| From | ``` case SecuredWithAutomaticSecureTimeout ``` |
| To | ``` case securedWithAutomaticSecureTimeout ``` |

Modified [HMCharacteristicValueLockMechanismLastKnownAction.securedWithKeypad](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismlastknownaction/securedwithkeypad)

|  | Declaration |
| --- | --- |
| From | ``` case SecuredWithKeypad ``` |
| To | ``` case securedWithKeypad ``` |

Modified [HMCharacteristicValueLockMechanismLastKnownAction.unsecuredRemotely](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismlastknownaction/hmcharacteristicvaluelockmechanismlastknownactionunsecuredremotely)

|  | Declaration |
| --- | --- |
| From | ``` case UnsecuredRemotely ``` |
| To | ``` case unsecuredRemotely ``` |

Modified [HMCharacteristicValueLockMechanismLastKnownAction.unsecuredUsingPhysicalMovement](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismlastknownaction/unsecuredusingphysicalmovement)

|  | Declaration |
| --- | --- |
| From | ``` case UnsecuredUsingPhysicalMovement ``` |
| To | ``` case unsecuredUsingPhysicalMovement ``` |

Modified [HMCharacteristicValueLockMechanismLastKnownAction.unsecuredUsingPhysicalMovementExterior](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismlastknownaction/hmcharacteristicvaluelockmechanismlastknownactionunsecuredusingphysicalmovementexterior)

|  | Declaration |
| --- | --- |
| From | ``` case UnsecuredUsingPhysicalMovementExterior ``` |
| To | ``` case unsecuredUsingPhysicalMovementExterior ``` |

Modified [HMCharacteristicValueLockMechanismLastKnownAction.unsecuredUsingPhysicalMovementInterior](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismlastknownaction/hmcharacteristicvaluelockmechanismlastknownactionunsecuredusingphysicalmovementinterior)

|  | Declaration |
| --- | --- |
| From | ``` case UnsecuredUsingPhysicalMovementInterior ``` |
| To | ``` case unsecuredUsingPhysicalMovementInterior ``` |

Modified [HMCharacteristicValueLockMechanismLastKnownAction.unsecuredWithKeypad](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismlastknownaction/unsecuredwithkeypad)

|  | Declaration |
| --- | --- |
| From | ``` case UnsecuredWithKeypad ``` |
| To | ``` case unsecuredWithKeypad ``` |

Modified [HMCharacteristicValueLockMechanismState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismstate)

|  | Declaration |
| --- | --- |
| From | ``` enum HMCharacteristicValueLockMechanismState : Int {     case Unsecured     case Secured     case Jammed     case Unknown } ``` |
| To | ``` enum HMCharacteristicValueLockMechanismState : Int {     case unsecured     case secured     case jammed     case unknown } ``` |

Modified [HMCharacteristicValueLockMechanismState.jammed](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismstate/jammed)

|  | Declaration |
| --- | --- |
| From | ``` case Jammed ``` |
| To | ``` case jammed ``` |

Modified [HMCharacteristicValueLockMechanismState.secured](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismstate/secured)

|  | Declaration |
| --- | --- |
| From | ``` case Secured ``` |
| To | ``` case secured ``` |

Modified [HMCharacteristicValueLockMechanismState.unknown](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismstate/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [HMCharacteristicValueLockMechanismState.unsecured](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismstate/hmcharacteristicvaluelockmechanismstateunsecured)

|  | Declaration |
| --- | --- |
| From | ``` case Unsecured ``` |
| To | ``` case unsecured ``` |

Modified [HMCharacteristicValuePositionState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluepositionstate)

|  | Declaration |
| --- | --- |
| From | ``` enum HMCharacteristicValuePositionState : Int {     case Closing     case Opening     case Stopped } ``` |
| To | ``` enum HMCharacteristicValuePositionState : Int {     case closing     case opening     case stopped } ``` |

Modified [HMCharacteristicValuePositionState.closing](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluepositionstate/hmcharacteristicvaluepositionstateclosing)

|  | Declaration |
| --- | --- |
| From | ``` case Closing ``` |
| To | ``` case closing ``` |

Modified [HMCharacteristicValuePositionState.opening](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluepositionstate/opening)

|  | Declaration |
| --- | --- |
| From | ``` case Opening ``` |
| To | ``` case opening ``` |

Modified [HMCharacteristicValuePositionState.stopped](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluepositionstate/hmcharacteristicvaluepositionstatestopped)

|  | Declaration |
| --- | --- |
| From | ``` case Stopped ``` |
| To | ``` case stopped ``` |

Modified [HMCharacteristicValueRotationDirection [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluerotationdirection)

|  | Declaration |
| --- | --- |
| From | ``` enum HMCharacteristicValueRotationDirection : Int {     case Clockwise     case CounterClockwise } ``` |
| To | ``` enum HMCharacteristicValueRotationDirection : Int {     case clockwise     case counterClockwise } ``` |

Modified [HMCharacteristicValueRotationDirection.clockwise](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluerotationdirection/clockwise)

|  | Declaration |
| --- | --- |
| From | ``` case Clockwise ``` |
| To | ``` case clockwise ``` |

Modified [HMCharacteristicValueRotationDirection.counterClockwise](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluerotationdirection/hmcharacteristicvaluerotationdirectioncounterclockwise)

|  | Declaration |
| --- | --- |
| From | ``` case CounterClockwise ``` |
| To | ``` case counterClockwise ``` |

Modified [HMCharacteristicValueTargetSecuritySystemState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate)

|  | Declaration |
| --- | --- |
| From | ``` enum HMCharacteristicValueTargetSecuritySystemState : Int {     case StayArm     case AwayArm     case NightArm     case Disarm } ``` |
| To | ``` enum HMCharacteristicValueTargetSecuritySystemState : Int {     case stayArm     case awayArm     case nightArm     case disarm } ``` |

Modified [HMCharacteristicValueTargetSecuritySystemState.awayArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate/awayarm)

|  | Declaration |
| --- | --- |
| From | ``` case AwayArm ``` |
| To | ``` case awayArm ``` |

Modified [HMCharacteristicValueTargetSecuritySystemState.disarm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate/hmcharacteristicvaluetargetsecuritysystemstatedisarm)

|  | Declaration |
| --- | --- |
| From | ``` case Disarm ``` |
| To | ``` case disarm ``` |

Modified [HMCharacteristicValueTargetSecuritySystemState.nightArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate/hmcharacteristicvaluetargetsecuritysystemstatenightarm)

|  | Declaration |
| --- | --- |
| From | ``` case NightArm ``` |
| To | ``` case nightArm ``` |

Modified [HMCharacteristicValueTargetSecuritySystemState.stayArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate/hmcharacteristicvaluetargetsecuritysystemstatestayarm)

|  | Declaration |
| --- | --- |
| From | ``` case StayArm ``` |
| To | ``` case stayArm ``` |

Modified [HMCharacteristicValueTemperatureUnit [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetemperatureunit)

|  | Declaration |
| --- | --- |
| From | ``` enum HMCharacteristicValueTemperatureUnit : Int {     case Celsius     case Fahrenheit } ``` |
| To | ``` enum HMCharacteristicValueTemperatureUnit : Int {     case celsius     case fahrenheit } ``` |

Modified [HMCharacteristicValueTemperatureUnit.celsius](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetemperatureunit/celsius)

|  | Declaration |
| --- | --- |
| From | ``` case Celsius ``` |
| To | ``` case celsius ``` |

Modified [HMCharacteristicValueTemperatureUnit.fahrenheit](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetemperatureunit/hmcharacteristicvaluetemperatureunitfahrenheit)

|  | Declaration |
| --- | --- |
| From | ``` case Fahrenheit ``` |
| To | ``` case fahrenheit ``` |

Modified [HMCharacteristicWriteAction](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction)

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` class HMCharacteristicWriteAction : HMAction {     convenience init()     init(characteristic characteristic: HMCharacteristic, targetValue targetValue: NSCopying)     var characteristic: HMCharacteristic { get }     @NSCopying var targetValue: NSCopying { get }     func updateTargetValue(_ targetValue: NSCopying, completionHandler completion: (NSError?) -> Void) } ``` | ```  ``` | -- |
| To | ``` class HMCharacteristicWriteAction<TargetValueType : NSCopying> : HMAction {     convenience init()     init(characteristic characteristic: HMCharacteristic, targetValue targetValue: TargetValueType)     var characteristic: HMCharacteristic { get }     @NSCopying var targetValue: TargetValueType { get }     func updateTargetValue(_ targetValue: TargetValueType, completionHandler completion: @escaping (Error?) -> Swift.Void) } ``` | ``` TargetValueType : NSCopying ``` | TargetValueType |

Modified [HMCharacteristicWriteAction.targetValue](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/1621973-targetvalue)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var targetValue: NSCopying { get } ``` |
| To | ``` @NSCopying var targetValue: TargetValueType { get } ``` |

Modified [HMError.Code [enum]](https://developer.apple.com/documentation/homekit/hmerror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum HMErrorCode : Int {     case AlreadyExists     case NotFound     case InvalidParameter     case AccessoryNotReachable     case ReadOnlyCharacteristic     case WriteOnlyCharacteristic     case NotificationNotSupported     case OperationTimedOut     case AccessoryPoweredOff     case AccessDenied     case ObjectAssociatedToAnotherHome     case ObjectNotAssociatedToAnyHome     case ObjectAlreadyAssociatedToHome     case AccessoryIsBusy     case OperationInProgress     case AccessoryOutOfResources     case InsufficientPrivileges     case AccessoryPairingFailed     case InvalidDataFormatSpecified     case NilParameter     case UnconfiguredParameter     case InvalidClass     case OperationCancelled     case RoomForHomeCannotBeInZone     case NoActionsInActionSet     case NoRegisteredActionSets     case MissingParameter     case FireDateInPast     case RoomForHomeCannotBeUpdated     case ActionInAnotherActionSet     case ObjectWithSimilarNameExistsInHome     case HomeWithSimilarNameExists     case RenameWithSimilarName     case CannotRemoveNonBridgeAccessory     case NameContainsProhibitedCharacters     case NameDoesNotStartWithValidCharacters     case UserIDNotEmailAddress     case UserDeclinedAddingUser     case UserDeclinedRemovingUser     case UserDeclinedInvite     case UserManagementFailed     case RecurrenceTooSmall     case InvalidValueType     case ValueLowerThanMinimum     case ValueHigherThanMaximum     case StringLongerThanMaximum     case HomeAccessNotAuthorized     case OperationNotSupported     case MaximumObjectLimitReached     case AccessorySentInvalidResponse     case StringShorterThanMinimum     case GenericError     case SecurityFailure     case CommunicationFailure     case MessageAuthenticationFailed     case InvalidMessageSize     case AccessoryDiscoveryFailed     case ClientRequestError     case AccessoryResponseError     case NameDoesNotEndWithValidCharacters     case AccessoryIsBlocked     case InvalidAssociatedServiceType     case ActionSetExecutionFailed     case ActionSetExecutionPartialSuccess     case ActionSetExecutionInProgress     case AccessoryOutOfCompliance     case DataResetFailure     case NotificationAlreadyEnabled     case RecurrenceMustBeOnSpecifiedBoundaries     case DateMustBeOnSpecifiedBoundaries     case CannotActivateTriggerTooFarInFuture     case RecurrenceTooLarge     case ReadWritePartialSuccess     case ReadWriteFailure     case NotSignedIntoiCloud     case KeychainSyncNotEnabled     case CloudDataSyncInProgress     case NetworkUnavailable     case AddAccessoryFailed     case MissingEntitlement     case CannotUnblockNonBridgeAccessory     case DeviceLocked     case CannotRemoveBuiltinActionSet     case LocationForHomeDisabled     case NotAuthorizedForLocationServices     case ReferToUserManual } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = HMError         case alreadyExists         case notFound         case invalidParameter         case accessoryNotReachable         case readOnlyCharacteristic         case writeOnlyCharacteristic         case notificationNotSupported         case operationTimedOut         case accessoryPoweredOff         case accessDenied         case objectAssociatedToAnotherHome         case objectNotAssociatedToAnyHome         case objectAlreadyAssociatedToHome         case accessoryIsBusy         case operationInProgress         case accessoryOutOfResources         case insufficientPrivileges         case accessoryPairingFailed         case invalidDataFormatSpecified         case nilParameter         case unconfiguredParameter         case invalidClass         case operationCancelled         case roomForHomeCannotBeInZone         case noActionsInActionSet         case noRegisteredActionSets         case missingParameter         case fireDateInPast         case roomForHomeCannotBeUpdated         case actionInAnotherActionSet         case objectWithSimilarNameExistsInHome         case homeWithSimilarNameExists         case renameWithSimilarName         case cannotRemoveNonBridgeAccessory         case nameContainsProhibitedCharacters         case nameDoesNotStartWithValidCharacters         case userIDNotEmailAddress         case userDeclinedAddingUser         case userDeclinedRemovingUser         case userDeclinedInvite         case userManagementFailed         case recurrenceTooSmall         case invalidValueType         case valueLowerThanMinimum         case valueHigherThanMaximum         case stringLongerThanMaximum         case homeAccessNotAuthorized         case operationNotSupported         case maximumObjectLimitReached         case accessorySentInvalidResponse         case stringShorterThanMinimum         case genericError         case securityFailure         case communicationFailure         case messageAuthenticationFailed         case invalidMessageSize         case accessoryDiscoveryFailed         case clientRequestError         case accessoryResponseError         case nameDoesNotEndWithValidCharacters         case accessoryIsBlocked         case invalidAssociatedServiceType         case actionSetExecutionFailed         case actionSetExecutionPartialSuccess         case actionSetExecutionInProgress         case accessoryOutOfCompliance         case dataResetFailure         case notificationAlreadyEnabled         case recurrenceMustBeOnSpecifiedBoundaries         case dateMustBeOnSpecifiedBoundaries         case cannotActivateTriggerTooFarInFuture         case recurrenceTooLarge         case readWritePartialSuccess         case readWriteFailure         case notSignedIntoiCloud         case keychainSyncNotEnabled         case cloudDataSyncInProgress         case networkUnavailable         case addAccessoryFailed         case missingEntitlement         case cannotUnblockNonBridgeAccessory         case deviceLocked         case cannotRemoveBuiltinActionSet         case locationForHomeDisabled         case notAuthorizedForLocationServices         case referToUserManual         case invalidOrMissingAuthorizationData         case bridgedAccessoryNotReachable         case notAuthorizedForMicrophoneAccess     } ``` |

Modified [HMError.Code.accessDenied](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeaccessdenied)

|  | Declaration |
| --- | --- |
| From | ``` case AccessDenied ``` |
| To | ``` case accessDenied ``` |

Modified [HMError.Code.accessoryDiscoveryFailed](https://developer.apple.com/documentation/homekit/hmerror/code/accessorydiscoveryfailed)

|  | Declaration |
| --- | --- |
| From | ``` case AccessoryDiscoveryFailed ``` |
| To | ``` case accessoryDiscoveryFailed ``` |

Modified [HMError.Code.accessoryIsBlocked](https://developer.apple.com/documentation/homekit/hmerror/code/accessoryisblocked)

|  | Declaration |
| --- | --- |
| From | ``` case AccessoryIsBlocked ``` |
| To | ``` case accessoryIsBlocked ``` |

Modified [HMError.Code.accessoryIsBusy](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeaccessoryisbusy)

|  | Declaration |
| --- | --- |
| From | ``` case AccessoryIsBusy ``` |
| To | ``` case accessoryIsBusy ``` |

Modified [HMError.Code.accessoryNotReachable](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeaccessorynotreachable)

|  | Declaration |
| --- | --- |
| From | ``` case AccessoryNotReachable ``` |
| To | ``` case accessoryNotReachable ``` |

Modified [HMError.Code.accessoryOutOfCompliance](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeaccessoryoutofcompliance)

|  | Declaration |
| --- | --- |
| From | ``` case AccessoryOutOfCompliance ``` |
| To | ``` case accessoryOutOfCompliance ``` |

Modified [HMError.Code.accessoryOutOfResources](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeaccessoryoutofresources)

|  | Declaration |
| --- | --- |
| From | ``` case AccessoryOutOfResources ``` |
| To | ``` case accessoryOutOfResources ``` |

Modified [HMError.Code.accessoryPairingFailed](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeaccessorypairingfailed)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case AccessoryPairingFailed ``` | watchOS 2.0 |
| To | ``` case accessoryPairingFailed ``` | watchOS 3.0 |

Modified [HMError.Code.accessoryPoweredOff](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeaccessorypoweredoff)

|  | Declaration |
| --- | --- |
| From | ``` case AccessoryPoweredOff ``` |
| To | ``` case accessoryPoweredOff ``` |

Modified [HMError.Code.accessoryResponseError](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeaccessoryresponseerror)

|  | Declaration |
| --- | --- |
| From | ``` case AccessoryResponseError ``` |
| To | ``` case accessoryResponseError ``` |

Modified [HMError.Code.accessorySentInvalidResponse](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeaccessorysentinvalidresponse)

|  | Declaration |
| --- | --- |
| From | ``` case AccessorySentInvalidResponse ``` |
| To | ``` case accessorySentInvalidResponse ``` |

Modified [HMError.Code.actionInAnotherActionSet](https://developer.apple.com/documentation/homekit/hmerror/code/actioninanotheractionset)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case ActionInAnotherActionSet ``` | watchOS 2.0 |
| To | ``` case actionInAnotherActionSet ``` | watchOS 3.0 |

Modified [HMError.Code.actionSetExecutionFailed](https://developer.apple.com/documentation/homekit/hmerror/code/actionsetexecutionfailed)

|  | Declaration |
| --- | --- |
| From | ``` case ActionSetExecutionFailed ``` |
| To | ``` case actionSetExecutionFailed ``` |

Modified [HMError.Code.actionSetExecutionInProgress](https://developer.apple.com/documentation/homekit/hmerror/code/actionsetexecutioninprogress)

|  | Declaration |
| --- | --- |
| From | ``` case ActionSetExecutionInProgress ``` |
| To | ``` case actionSetExecutionInProgress ``` |

Modified [HMError.Code.actionSetExecutionPartialSuccess](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeactionsetexecutionpartialsuccess)

|  | Declaration |
| --- | --- |
| From | ``` case ActionSetExecutionPartialSuccess ``` |
| To | ``` case actionSetExecutionPartialSuccess ``` |

Modified [HMError.Code.addAccessoryFailed](https://developer.apple.com/documentation/homekit/hmerror/code/addaccessoryfailed)

|  | Declaration |
| --- | --- |
| From | ``` case AddAccessoryFailed ``` |
| To | ``` case addAccessoryFailed ``` |

Modified [HMError.Code.alreadyExists](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodealreadyexists)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case AlreadyExists ``` | watchOS 2.0 |
| To | ``` case alreadyExists ``` | watchOS 3.0 |

Modified [HMError.Code.cannotActivateTriggerTooFarInFuture](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodecannotactivatetriggertoofarinfuture)

|  | Declaration |
| --- | --- |
| From | ``` case CannotActivateTriggerTooFarInFuture ``` |
| To | ``` case cannotActivateTriggerTooFarInFuture ``` |

Modified [HMError.Code.cannotRemoveBuiltinActionSet](https://developer.apple.com/documentation/homekit/hmerror/code/cannotremovebuiltinactionset)

|  | Declaration |
| --- | --- |
| From | ``` case CannotRemoveBuiltinActionSet ``` |
| To | ``` case cannotRemoveBuiltinActionSet ``` |

Modified [HMError.Code.cannotRemoveNonBridgeAccessory](https://developer.apple.com/documentation/homekit/hmerror/code/cannotremovenonbridgeaccessory)

|  | Declaration |
| --- | --- |
| From | ``` case CannotRemoveNonBridgeAccessory ``` |
| To | ``` case cannotRemoveNonBridgeAccessory ``` |

Modified [HMError.Code.cannotUnblockNonBridgeAccessory](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodecannotunblocknonbridgeaccessory)

|  | Declaration |
| --- | --- |
| From | ``` case CannotUnblockNonBridgeAccessory ``` |
| To | ``` case cannotUnblockNonBridgeAccessory ``` |

Modified [HMError.Code.clientRequestError](https://developer.apple.com/documentation/homekit/hmerror/code/clientrequesterror)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case ClientRequestError ``` | watchOS 2.0 |
| To | ``` case clientRequestError ``` | watchOS 3.0 |

Modified [HMError.Code.cloudDataSyncInProgress](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeclouddatasyncinprogress)

|  | Declaration |
| --- | --- |
| From | ``` case CloudDataSyncInProgress ``` |
| To | ``` case cloudDataSyncInProgress ``` |

Modified [HMError.Code.communicationFailure](https://developer.apple.com/documentation/homekit/hmerror/code/communicationfailure)

|  | Declaration |
| --- | --- |
| From | ``` case CommunicationFailure ``` |
| To | ``` case communicationFailure ``` |

Modified [HMError.Code.dataResetFailure](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodedataresetfailure)

|  | Declaration |
| --- | --- |
| From | ``` case DataResetFailure ``` |
| To | ``` case dataResetFailure ``` |

Modified [HMError.Code.dateMustBeOnSpecifiedBoundaries](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodedatemustbeonspecifiedboundaries)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case DateMustBeOnSpecifiedBoundaries ``` | watchOS 2.0 |
| To | ``` case dateMustBeOnSpecifiedBoundaries ``` | watchOS 3.0 |

Modified [HMError.Code.deviceLocked](https://developer.apple.com/documentation/homekit/hmerror/code/devicelocked)

|  | Declaration |
| --- | --- |
| From | ``` case DeviceLocked ``` |
| To | ``` case deviceLocked ``` |

Modified [HMError.Code.fireDateInPast](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodefiredateinpast)

|  | Declaration |
| --- | --- |
| From | ``` case FireDateInPast ``` |
| To | ``` case fireDateInPast ``` |

Modified [HMError.Code.genericError](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodegenericerror)

|  | Declaration |
| --- | --- |
| From | ``` case GenericError ``` |
| To | ``` case genericError ``` |

Modified [HMError.Code.homeAccessNotAuthorized](https://developer.apple.com/documentation/homekit/hmerror/code/homeaccessnotauthorized)

|  | Declaration |
| --- | --- |
| From | ``` case HomeAccessNotAuthorized ``` |
| To | ``` case homeAccessNotAuthorized ``` |

Modified [HMError.Code.homeWithSimilarNameExists](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodehomewithsimilarnameexists)

|  | Declaration |
| --- | --- |
| From | ``` case HomeWithSimilarNameExists ``` |
| To | ``` case homeWithSimilarNameExists ``` |

Modified [HMError.Code.insufficientPrivileges](https://developer.apple.com/documentation/homekit/hmerror/code/insufficientprivileges)

|  | Declaration |
| --- | --- |
| From | ``` case InsufficientPrivileges ``` |
| To | ``` case insufficientPrivileges ``` |

Modified [HMError.Code.invalidAssociatedServiceType](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeinvalidassociatedservicetype)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidAssociatedServiceType ``` |
| To | ``` case invalidAssociatedServiceType ``` |

Modified [HMError.Code.invalidClass](https://developer.apple.com/documentation/homekit/hmerror/code/invalidclass)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case InvalidClass ``` | watchOS 2.0 |
| To | ``` case invalidClass ``` | watchOS 3.0 |

Modified [HMError.Code.invalidDataFormatSpecified](https://developer.apple.com/documentation/homekit/hmerror/code/invaliddataformatspecified)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidDataFormatSpecified ``` |
| To | ``` case invalidDataFormatSpecified ``` |

Modified [HMError.Code.invalidMessageSize](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeinvalidmessagesize)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidMessageSize ``` |
| To | ``` case invalidMessageSize ``` |

Modified [HMError.Code.invalidParameter](https://developer.apple.com/documentation/homekit/hmerror/code/invalidparameter)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidParameter ``` |
| To | ``` case invalidParameter ``` |

Modified [HMError.Code.invalidValueType](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeinvalidvaluetype)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidValueType ``` |
| To | ``` case invalidValueType ``` |

Modified [HMError.Code.keychainSyncNotEnabled](https://developer.apple.com/documentation/homekit/hmerror/code/keychainsyncnotenabled)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case KeychainSyncNotEnabled ``` | watchOS 2.0 |
| To | ``` case keychainSyncNotEnabled ``` | watchOS 3.0 |

Modified [HMError.Code.locationForHomeDisabled](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodelocationforhomedisabled)

|  | Declaration |
| --- | --- |
| From | ``` case LocationForHomeDisabled ``` |
| To | ``` case locationForHomeDisabled ``` |

Modified [HMError.Code.maximumObjectLimitReached](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodemaximumobjectlimitreached)

|  | Declaration |
| --- | --- |
| From | ``` case MaximumObjectLimitReached ``` |
| To | ``` case maximumObjectLimitReached ``` |

Modified [HMError.Code.messageAuthenticationFailed](https://developer.apple.com/documentation/homekit/hmerror/code/messageauthenticationfailed)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case MessageAuthenticationFailed ``` | watchOS 2.0 |
| To | ``` case messageAuthenticationFailed ``` | watchOS 3.0 |

Modified [HMError.Code.missingEntitlement](https://developer.apple.com/documentation/homekit/hmerror/code/missingentitlement)

|  | Declaration |
| --- | --- |
| From | ``` case MissingEntitlement ``` |
| To | ``` case missingEntitlement ``` |

Modified [HMError.Code.missingParameter](https://developer.apple.com/documentation/homekit/hmerror/code/missingparameter)

|  | Declaration |
| --- | --- |
| From | ``` case MissingParameter ``` |
| To | ``` case missingParameter ``` |

Modified [HMError.Code.nameContainsProhibitedCharacters](https://developer.apple.com/documentation/homekit/hmerror/code/namecontainsprohibitedcharacters)

|  | Declaration |
| --- | --- |
| From | ``` case NameContainsProhibitedCharacters ``` |
| To | ``` case nameContainsProhibitedCharacters ``` |

Modified [HMError.Code.nameDoesNotEndWithValidCharacters](https://developer.apple.com/documentation/homekit/hmerror/code/namedoesnotendwithvalidcharacters)

|  | Declaration |
| --- | --- |
| From | ``` case NameDoesNotEndWithValidCharacters ``` |
| To | ``` case nameDoesNotEndWithValidCharacters ``` |

Modified [HMError.Code.nameDoesNotStartWithValidCharacters](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodenamedoesnotstartwithvalidcharacters)

|  | Declaration |
| --- | --- |
| From | ``` case NameDoesNotStartWithValidCharacters ``` |
| To | ``` case nameDoesNotStartWithValidCharacters ``` |

Modified [HMError.Code.networkUnavailable](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodenetworkunavailable)

|  | Declaration |
| --- | --- |
| From | ``` case NetworkUnavailable ``` |
| To | ``` case networkUnavailable ``` |

Modified [HMError.Code.nilParameter](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodenilparameter)

|  | Declaration |
| --- | --- |
| From | ``` case NilParameter ``` |
| To | ``` case nilParameter ``` |

Modified [HMError.Code.noActionsInActionSet](https://developer.apple.com/documentation/homekit/hmerror/code/noactionsinactionset)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case NoActionsInActionSet ``` | watchOS 2.0 |
| To | ``` case noActionsInActionSet ``` | watchOS 3.0 |

Modified [HMError.Code.noRegisteredActionSets](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodenoregisteredactionsets)

|  | Declaration |
| --- | --- |
| From | ``` case NoRegisteredActionSets ``` |
| To | ``` case noRegisteredActionSets ``` |

Modified [HMError.Code.notAuthorizedForLocationServices](https://developer.apple.com/documentation/homekit/hmerror/code/notauthorizedforlocationservices)

|  | Declaration |
| --- | --- |
| From | ``` case NotAuthorizedForLocationServices ``` |
| To | ``` case notAuthorizedForLocationServices ``` |

Modified [HMError.Code.notFound](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodenotfound)

|  | Declaration |
| --- | --- |
| From | ``` case NotFound ``` |
| To | ``` case notFound ``` |

Modified [HMError.Code.notificationAlreadyEnabled](https://developer.apple.com/documentation/homekit/hmerror/code/notificationalreadyenabled)

|  | Declaration |
| --- | --- |
| From | ``` case NotificationAlreadyEnabled ``` |
| To | ``` case notificationAlreadyEnabled ``` |

Modified [HMError.Code.notificationNotSupported](https://developer.apple.com/documentation/homekit/hmerror/code/notificationnotsupported)

|  | Declaration |
| --- | --- |
| From | ``` case NotificationNotSupported ``` |
| To | ``` case notificationNotSupported ``` |

Modified [HMError.Code.notSignedIntoiCloud](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodenotsignedintoicloud)

|  | Declaration |
| --- | --- |
| From | ``` case NotSignedIntoiCloud ``` |
| To | ``` case notSignedIntoiCloud ``` |

Modified [HMError.Code.objectAlreadyAssociatedToHome](https://developer.apple.com/documentation/homekit/hmerror/code/objectalreadyassociatedtohome)

|  | Declaration |
| --- | --- |
| From | ``` case ObjectAlreadyAssociatedToHome ``` |
| To | ``` case objectAlreadyAssociatedToHome ``` |

Modified [HMError.Code.objectAssociatedToAnotherHome](https://developer.apple.com/documentation/homekit/hmerror/code/objectassociatedtoanotherhome)

|  | Declaration |
| --- | --- |
| From | ``` case ObjectAssociatedToAnotherHome ``` |
| To | ``` case objectAssociatedToAnotherHome ``` |

Modified [HMError.Code.objectNotAssociatedToAnyHome](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeobjectnotassociatedtoanyhome)

|  | Declaration |
| --- | --- |
| From | ``` case ObjectNotAssociatedToAnyHome ``` |
| To | ``` case objectNotAssociatedToAnyHome ``` |

Modified [HMError.Code.objectWithSimilarNameExistsInHome](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeobjectwithsimilarnameexistsinhome)

|  | Declaration |
| --- | --- |
| From | ``` case ObjectWithSimilarNameExistsInHome ``` |
| To | ``` case objectWithSimilarNameExistsInHome ``` |

Modified [HMError.Code.operationCancelled](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeoperationcancelled)

|  | Declaration |
| --- | --- |
| From | ``` case OperationCancelled ``` |
| To | ``` case operationCancelled ``` |

Modified [HMError.Code.operationInProgress](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeoperationinprogress)

|  | Declaration |
| --- | --- |
| From | ``` case OperationInProgress ``` |
| To | ``` case operationInProgress ``` |

Modified [HMError.Code.operationNotSupported](https://developer.apple.com/documentation/homekit/hmerror/code/operationnotsupported)

|  | Declaration |
| --- | --- |
| From | ``` case OperationNotSupported ``` |
| To | ``` case operationNotSupported ``` |

Modified [HMError.Code.operationTimedOut](https://developer.apple.com/documentation/homekit/hmerror/code/operationtimedout)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case OperationTimedOut ``` | watchOS 2.0 |
| To | ``` case operationTimedOut ``` | watchOS 3.0 |

Modified [HMError.Code.readOnlyCharacteristic](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodereadonlycharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` case ReadOnlyCharacteristic ``` |
| To | ``` case readOnlyCharacteristic ``` |

Modified [HMError.Code.readWriteFailure](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodereadwritefailure)

|  | Declaration |
| --- | --- |
| From | ``` case ReadWriteFailure ``` |
| To | ``` case readWriteFailure ``` |

Modified [HMError.Code.readWritePartialSuccess](https://developer.apple.com/documentation/homekit/hmerror/code/readwritepartialsuccess)

|  | Declaration |
| --- | --- |
| From | ``` case ReadWritePartialSuccess ``` |
| To | ``` case readWritePartialSuccess ``` |

Modified [HMError.Code.recurrenceMustBeOnSpecifiedBoundaries](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcoderecurrencemustbeonspecifiedboundaries)

|  | Declaration |
| --- | --- |
| From | ``` case RecurrenceMustBeOnSpecifiedBoundaries ``` |
| To | ``` case recurrenceMustBeOnSpecifiedBoundaries ``` |

Modified [HMError.Code.recurrenceTooLarge](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcoderecurrencetoolarge)

|  | Declaration |
| --- | --- |
| From | ``` case RecurrenceTooLarge ``` |
| To | ``` case recurrenceTooLarge ``` |

Modified [HMError.Code.recurrenceTooSmall](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcoderecurrencetoosmall)

|  | Declaration |
| --- | --- |
| From | ``` case RecurrenceTooSmall ``` |
| To | ``` case recurrenceTooSmall ``` |

Modified [HMError.Code.referToUserManual](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcoderefertousermanual)

|  | Declaration |
| --- | --- |
| From | ``` case ReferToUserManual ``` |
| To | ``` case referToUserManual ``` |

Modified [HMError.Code.renameWithSimilarName](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcoderenamewithsimilarname)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case RenameWithSimilarName ``` | watchOS 2.0 |
| To | ``` case renameWithSimilarName ``` | watchOS 3.0 |

Modified [HMError.Code.roomForHomeCannotBeInZone](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcoderoomforhomecannotbeinzone)

|  | Declaration |
| --- | --- |
| From | ``` case RoomForHomeCannotBeInZone ``` |
| To | ``` case roomForHomeCannotBeInZone ``` |

Modified [HMError.Code.roomForHomeCannotBeUpdated](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcoderoomforhomecannotbeupdated)

|  | Declaration |
| --- | --- |
| From | ``` case RoomForHomeCannotBeUpdated ``` |
| To | ``` case roomForHomeCannotBeUpdated ``` |

Modified [HMError.Code.securityFailure](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodesecurityfailure)

|  | Declaration |
| --- | --- |
| From | ``` case SecurityFailure ``` |
| To | ``` case securityFailure ``` |

Modified [HMError.Code.stringLongerThanMaximum](https://developer.apple.com/documentation/homekit/hmerror/code/stringlongerthanmaximum)

|  | Declaration |
| --- | --- |
| From | ``` case StringLongerThanMaximum ``` |
| To | ``` case stringLongerThanMaximum ``` |

Modified [HMError.Code.stringShorterThanMinimum](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodestringshorterthanminimum)

|  | Declaration |
| --- | --- |
| From | ``` case StringShorterThanMinimum ``` |
| To | ``` case stringShorterThanMinimum ``` |

Modified [HMError.Code.unconfiguredParameter](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeunconfiguredparameter)

|  | Declaration |
| --- | --- |
| From | ``` case UnconfiguredParameter ``` |
| To | ``` case unconfiguredParameter ``` |

Modified [HMError.Code.userDeclinedAddingUser](https://developer.apple.com/documentation/homekit/hmerror/code/userdeclinedaddinguser)

|  | Declaration |
| --- | --- |
| From | ``` case UserDeclinedAddingUser ``` |
| To | ``` case userDeclinedAddingUser ``` |

Modified [HMError.Code.userDeclinedInvite](https://developer.apple.com/documentation/homekit/hmerror/code/userdeclinedinvite)

|  | Declaration |
| --- | --- |
| From | ``` case UserDeclinedInvite ``` |
| To | ``` case userDeclinedInvite ``` |

Modified [HMError.Code.userDeclinedRemovingUser](https://developer.apple.com/documentation/homekit/hmerror/code/userdeclinedremovinguser)

|  | Declaration |
| --- | --- |
| From | ``` case UserDeclinedRemovingUser ``` |
| To | ``` case userDeclinedRemovingUser ``` |

Modified [HMError.Code.userIDNotEmailAddress](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeuseridnotemailaddress)

|  | Declaration |
| --- | --- |
| From | ``` case UserIDNotEmailAddress ``` |
| To | ``` case userIDNotEmailAddress ``` |

Modified [HMError.Code.userManagementFailed](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeusermanagementfailed)

|  | Declaration |
| --- | --- |
| From | ``` case UserManagementFailed ``` |
| To | ``` case userManagementFailed ``` |

Modified [HMError.Code.valueHigherThanMaximum](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodevaluehigherthanmaximum)

|  | Declaration |
| --- | --- |
| From | ``` case ValueHigherThanMaximum ``` |
| To | ``` case valueHigherThanMaximum ``` |

Modified [HMError.Code.valueLowerThanMinimum](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodevaluelowerthanminimum)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case ValueLowerThanMinimum ``` | watchOS 2.0 |
| To | ``` case valueLowerThanMinimum ``` | watchOS 3.0 |

Modified [HMError.Code.writeOnlyCharacteristic](https://developer.apple.com/documentation/homekit/hmerror/code/writeonlycharacteristic)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case WriteOnlyCharacteristic ``` | watchOS 2.0 |
| To | ``` case writeOnlyCharacteristic ``` | watchOS 3.0 |

Modified [HMEvent](https://developer.apple.com/documentation/homekit/hmevent)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMEvent : NSObject {     @NSCopying var uniqueIdentifier: NSUUID { get } } ``` | -- |
| To | ``` class HMEvent : NSObject {     var uniqueIdentifier: UUID { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMEvent : CVarArg { } extension HMEvent : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMEvent.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmevent/1619881-uniqueidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var uniqueIdentifier: NSUUID { get } ``` |
| To | ``` var uniqueIdentifier: UUID { get } ``` |

Modified [HMEventTrigger](https://developer.apple.com/documentation/homekit/hmeventtrigger)

|  | Declaration |
| --- | --- |
| From | ``` class HMEventTrigger : HMTrigger {     convenience init()     init(name name: String, events events: [HMEvent], predicate predicate: NSPredicate?)     var events: [HMEvent] { get }     @NSCopying var predicate: NSPredicate? { get }     class func predicateForEvaluatingTriggerOccurringBeforeSignificantEvent(_ significantEvent: String, applyingOffset offset: NSDateComponents?) -> NSPredicate     class func predicateForEvaluatingTriggerOccurringAfterSignificantEvent(_ significantEvent: String, applyingOffset offset: NSDateComponents?) -> NSPredicate     class func predicateForEvaluatingTriggerOccurringBeforeDateWithComponents(_ dateComponents: NSDateComponents) -> NSPredicate     class func predicateForEvaluatingTriggerOccurringOnDateWithComponents(_ dateComponents: NSDateComponents) -> NSPredicate     class func predicateForEvaluatingTriggerOccurringAfterDateWithComponents(_ dateComponents: NSDateComponents) -> NSPredicate     class func predicateForEvaluatingTriggerWithCharacteristic(_ characteristic: HMCharacteristic, relatedBy operatorType: NSPredicateOperatorType, toValue value: AnyObject) -> NSPredicate     func addEvent(_ event: HMEvent, completionHandler completion: (NSError?) -> Void)     func removeEvent(_ event: HMEvent, completionHandler completion: (NSError?) -> Void)     func updatePredicate(_ predicate: NSPredicate?, completionHandler completion: (NSError?) -> Void) } ``` |
| To | ``` class HMEventTrigger : HMTrigger {     init()     init(name name: String, events events: [HMEvent], predicate predicate: NSPredicate?)     var events: [HMEvent] { get }     @NSCopying var predicate: NSPredicate? { get }     class func predicateForEvaluatingTrigger(occurringBefore significantEvent: String, applyingOffset offset: DateComponents?) -> NSPredicate     class func predicateForEvaluatingTrigger(occurringAfter significantEvent: String, applyingOffset offset: DateComponents?) -> NSPredicate     class func predicateForEvaluatingTrigger(occurringBefore dateComponents: DateComponents) -> NSPredicate     class func predicateForEvaluatingTrigger(occurringOn dateComponents: DateComponents) -> NSPredicate     class func predicateForEvaluatingTrigger(occurringAfter dateComponents: DateComponents) -> NSPredicate     class func predicateForEvaluatingTrigger(_ characteristic: HMCharacteristic, relatedBy operatorType: NSComparisonPredicate.Operator, toValue value: Any) -> NSPredicate     func addEvent(_ event: HMEvent, completionHandler completion: @escaping (Error?) -> Swift.Void)     func removeEvent(_ event: HMEvent, completionHandler completion: @escaping (Error?) -> Swift.Void)     func updatePredicate(_ predicate: NSPredicate?, completionHandler completion: @escaping (Error?) -> Swift.Void) } ``` |

Modified [HMEventTrigger.predicateForEvaluatingTrigger(_: HMCharacteristic, relatedBy: NSComparisonPredicate.Operator, toValue: Any) -> NSPredicate [class]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624409-predicateforevaluatingtrigger)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForEvaluatingTriggerWithCharacteristic(_ characteristic: HMCharacteristic, relatedBy operatorType: NSPredicateOperatorType, toValue value: AnyObject) -> NSPredicate ``` |
| To | ``` class func predicateForEvaluatingTrigger(_ characteristic: HMCharacteristic, relatedBy operatorType: NSComparisonPredicate.Operator, toValue value: Any) -> NSPredicate ``` |

Modified [HMEventTrigger.predicateForEvaluatingTrigger(occurringAfter: DateComponents) -> NSPredicate [class]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624414-predicateforevaluatingtriggerocc)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForEvaluatingTriggerOccurringAfterDateWithComponents(_ dateComponents: NSDateComponents) -> NSPredicate ``` |
| To | ``` class func predicateForEvaluatingTrigger(occurringAfter dateComponents: DateComponents) -> NSPredicate ``` |

Modified [HMEventTrigger.predicateForEvaluatingTrigger(occurringAfter: String, applyingOffset: DateComponents?) -> NSPredicate [class]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624406-predicateforevaluatingtriggerocc)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForEvaluatingTriggerOccurringAfterSignificantEvent(_ significantEvent: String, applyingOffset offset: NSDateComponents?) -> NSPredicate ``` |
| To | ``` class func predicateForEvaluatingTrigger(occurringAfter significantEvent: String, applyingOffset offset: DateComponents?) -> NSPredicate ``` |

Modified [HMEventTrigger.predicateForEvaluatingTrigger(occurringBefore: DateComponents) -> NSPredicate [class]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624408-predicateforevaluatingtriggerocc)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForEvaluatingTriggerOccurringBeforeDateWithComponents(_ dateComponents: NSDateComponents) -> NSPredicate ``` |
| To | ``` class func predicateForEvaluatingTrigger(occurringBefore dateComponents: DateComponents) -> NSPredicate ``` |

Modified [HMEventTrigger.predicateForEvaluatingTrigger(occurringBefore: String, applyingOffset: DateComponents?) -> NSPredicate [class]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624401-predicateforevaluatingtrigger)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForEvaluatingTriggerOccurringBeforeSignificantEvent(_ significantEvent: String, applyingOffset offset: NSDateComponents?) -> NSPredicate ``` |
| To | ``` class func predicateForEvaluatingTrigger(occurringBefore significantEvent: String, applyingOffset offset: DateComponents?) -> NSPredicate ``` |

Modified [HMEventTrigger.predicateForEvaluatingTrigger(occurringOn: DateComponents) -> NSPredicate [class]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624407-predicateforevaluatingtriggerocc)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForEvaluatingTriggerOccurringOnDateWithComponents(_ dateComponents: NSDateComponents) -> NSPredicate ``` |
| To | ``` class func predicateForEvaluatingTrigger(occurringOn dateComponents: DateComponents) -> NSPredicate ``` |

Modified [HMHome](https://developer.apple.com/documentation/homekit/hmhome)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMHome : NSObject {     init()     weak var delegate: HMHomeDelegate?     var name: String { get }     var primary: Bool { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void) } extension HMHome {     var accessories: [HMAccessory] { get }     func addAccessory(_ accessory: HMAccessory, completionHandler completion: (NSError?) -> Void)     func removeAccessory(_ accessory: HMAccessory, completionHandler completion: (NSError?) -> Void)     func assignAccessory(_ accessory: HMAccessory, toRoom room: HMRoom, completionHandler completion: (NSError?) -> Void)     func servicesWithTypes(_ serviceTypes: [String]) -> [HMService]?     func unblockAccessory(_ accessory: HMAccessory, completionHandler completion: (NSError?) -> Void) } extension HMHome {     var currentUser: HMUser { get }     var users: [HMUser] { get }     func manageUsersWithCompletionHandler(_ completion: (NSError?) -> Void)     func addUserWithCompletionHandler(_ completion: (HMUser?, NSError?) -> Void)     func removeUser(_ user: HMUser, completionHandler completion: (NSError?) -> Void)     func homeAccessControlForUser(_ user: HMUser) -> HMHomeAccessControl } extension HMHome {     var rooms: [HMRoom] { get }     func addRoomWithName(_ roomName: String, completionHandler completion: (HMRoom?, NSError?) -> Void)     func removeRoom(_ room: HMRoom, completionHandler completion: (NSError?) -> Void)     func roomForEntireHome() -> HMRoom } extension HMHome {     var zones: [HMZone] { get }     func addZoneWithName(_ zoneName: String, completionHandler completion: (HMZone?, NSError?) -> Void)     func removeZone(_ zone: HMZone, completionHandler completion: (NSError?) -> Void) } extension HMHome {     var serviceGroups: [HMServiceGroup] { get }     func addServiceGroupWithName(_ serviceGroupName: String, completionHandler completion: (HMServiceGroup?, NSError?) -> Void)     func removeServiceGroup(_ group: HMServiceGroup, completionHandler completion: (NSError?) -> Void) } extension HMHome {     var actionSets: [HMActionSet] { get }     func addActionSetWithName(_ actionSetName: String, completionHandler completion: (HMActionSet?, NSError?) -> Void)     func removeActionSet(_ actionSet: HMActionSet, completionHandler completion: (NSError?) -> Void)     func executeActionSet(_ actionSet: HMActionSet, completionHandler completion: (NSError?) -> Void)     func builtinActionSetOfType(_ actionSetType: String) -> HMActionSet? } extension HMHome {     var triggers: [HMTrigger] { get }     func addTrigger(_ trigger: HMTrigger, completionHandler completion: (NSError?) -> Void)     func removeTrigger(_ trigger: HMTrigger, completionHandler completion: (NSError?) -> Void) } ``` | -- |
| To | ``` class HMHome : NSObject {     init()     weak var delegate: HMHomeDelegate?     var name: String { get }     var isPrimary: Bool { get }     var uniqueIdentifier: UUID { get }     func updateName(_ name: String, completionHandler completion: @escaping (Error?) -> Swift.Void)     var triggers: [HMTrigger] { get }     func addTrigger(_ trigger: HMTrigger, completionHandler completion: @escaping (Error?) -> Swift.Void)     func removeTrigger(_ trigger: HMTrigger, completionHandler completion: @escaping (Error?) -> Swift.Void)     var actionSets: [HMActionSet] { get }     func addActionSet(withName actionSetName: String, completionHandler completion: @escaping (HMActionSet?, Error?) -> Swift.Void)     func removeActionSet(_ actionSet: HMActionSet, completionHandler completion: @escaping (Error?) -> Swift.Void)     func executeActionSet(_ actionSet: HMActionSet, completionHandler completion: @escaping (Error?) -> Swift.Void)     func builtinActionSet(ofType actionSetType: String) -> HMActionSet?     var serviceGroups: [HMServiceGroup] { get }     func addServiceGroup(withName serviceGroupName: String, completionHandler completion: @escaping (HMServiceGroup?, Error?) -> Swift.Void)     func removeServiceGroup(_ group: HMServiceGroup, completionHandler completion: @escaping (Error?) -> Swift.Void)     var zones: [HMZone] { get }     func addZone(withName zoneName: String, completionHandler completion: @escaping (HMZone?, Error?) -> Swift.Void)     func removeZone(_ zone: HMZone, completionHandler completion: @escaping (Error?) -> Swift.Void)     var rooms: [HMRoom] { get }     func addRoom(withName roomName: String, completionHandler completion: @escaping (HMRoom?, Error?) -> Swift.Void)     func removeRoom(_ room: HMRoom, completionHandler completion: @escaping (Error?) -> Swift.Void)     func roomForEntireHome() -> HMRoom     var currentUser: HMUser { get }     var users: [HMUser] { get }     func manageUsers(completionHandler completion: @escaping (Error?) -> Swift.Void)     func addUser(completionHandler completion: @escaping (HMUser?, Error?) -> Swift.Void)     func removeUser(_ user: HMUser, completionHandler completion: @escaping (Error?) -> Swift.Void)     func homeAccessControl(for user: HMUser) -> HMHomeAccessControl     var accessories: [HMAccessory] { get }     func addAccessory(_ accessory: HMAccessory, completionHandler completion: @escaping (Error?) -> Swift.Void)     func removeAccessory(_ accessory: HMAccessory, completionHandler completion: @escaping (Error?) -> Swift.Void)     func assignAccessory(_ accessory: HMAccessory, to room: HMRoom, completionHandler completion: @escaping (Error?) -> Swift.Void)     func servicesWithTypes(_ serviceTypes: [String]) -> [HMService]?     func unblockAccessory(_ accessory: HMAccessory, completionHandler completion: @escaping (Error?) -> Swift.Void)     func addAndSetupAccessories(completionHandler completion: @escaping (Error?) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMHome : CVarArg { } extension HMHome : Equatable, Hashable {     var hashValue: Int { get } } extension HMHome {     var accessories: [HMAccessory] { get }     func addAccessory(_ accessory: HMAccessory, completionHandler completion: @escaping (Error?) -> Swift.Void)     func removeAccessory(_ accessory: HMAccessory, completionHandler completion: @escaping (Error?) -> Swift.Void)     func assignAccessory(_ accessory: HMAccessory, to room: HMRoom, completionHandler completion: @escaping (Error?) -> Swift.Void)     func servicesWithTypes(_ serviceTypes: [String]) -> [HMService]?     func unblockAccessory(_ accessory: HMAccessory, completionHandler completion: @escaping (Error?) -> Swift.Void)     func addAndSetupAccessories(completionHandler completion: @escaping (Error?) -> Swift.Void) } extension HMHome {     var currentUser: HMUser { get }     var users: [HMUser] { get }     func manageUsers(completionHandler completion: @escaping (Error?) -> Swift.Void)     func addUser(completionHandler completion: @escaping (HMUser?, Error?) -> Swift.Void)     func removeUser(_ user: HMUser, completionHandler completion: @escaping (Error?) -> Swift.Void)     func homeAccessControl(for user: HMUser) -> HMHomeAccessControl } extension HMHome {     var rooms: [HMRoom] { get }     func addRoom(withName roomName: String, completionHandler completion: @escaping (HMRoom?, Error?) -> Swift.Void)     func removeRoom(_ room: HMRoom, completionHandler completion: @escaping (Error?) -> Swift.Void)     func roomForEntireHome() -> HMRoom } extension HMHome {     var zones: [HMZone] { get }     func addZone(withName zoneName: String, completionHandler completion: @escaping (HMZone?, Error?) -> Swift.Void)     func removeZone(_ zone: HMZone, completionHandler completion: @escaping (Error?) -> Swift.Void) } extension HMHome {     var serviceGroups: [HMServiceGroup] { get }     func addServiceGroup(withName serviceGroupName: String, completionHandler completion: @escaping (HMServiceGroup?, Error?) -> Swift.Void)     func removeServiceGroup(_ group: HMServiceGroup, completionHandler completion: @escaping (Error?) -> Swift.Void) } extension HMHome {     var actionSets: [HMActionSet] { get }     func addActionSet(withName actionSetName: String, completionHandler completion: @escaping (HMActionSet?, Error?) -> Swift.Void)     func removeActionSet(_ actionSet: HMActionSet, completionHandler completion: @escaping (Error?) -> Swift.Void)     func executeActionSet(_ actionSet: HMActionSet, completionHandler completion: @escaping (Error?) -> Swift.Void)     func builtinActionSet(ofType actionSetType: String) -> HMActionSet? } extension HMHome {     var triggers: [HMTrigger] { get }     func addTrigger(_ trigger: HMTrigger, completionHandler completion: @escaping (Error?) -> Swift.Void)     func removeTrigger(_ trigger: HMTrigger, completionHandler completion: @escaping (Error?) -> Swift.Void) } ``` | CVarArg, Equatable, Hashable |

Modified [HMHome.builtinActionSet(ofType: String) -> HMActionSet?](https://developer.apple.com/documentation/homekit/hmhome/1620238-builtinactionsetoftype)

|  | Declaration |
| --- | --- |
| From | ``` func builtinActionSetOfType(_ actionSetType: String) -> HMActionSet? ``` |
| To | ``` func builtinActionSet(ofType actionSetType: String) -> HMActionSet? ``` |

Modified [HMHome.executeActionSet(_: HMActionSet, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/homekit/hmhome/1620256-executeactionset)

|  | Declaration |
| --- | --- |
| From | ``` func executeActionSet(_ actionSet: HMActionSet, completionHandler completion: (NSError?) -> Void) ``` |
| To | ``` func executeActionSet(_ actionSet: HMActionSet, completionHandler completion: @escaping (Error?) -> Swift.Void) ``` |

Modified [HMHome.homeAccessControl(for: HMUser) -> HMHomeAccessControl](https://developer.apple.com/documentation/homekit/hmhome/1620214-homeaccesscontrolforuser)

|  | Declaration |
| --- | --- |
| From | ``` func homeAccessControlForUser(_ user: HMUser) -> HMHomeAccessControl ``` |
| To | ``` func homeAccessControl(for user: HMUser) -> HMHomeAccessControl ``` |

Modified [HMHome.isPrimary](https://developer.apple.com/documentation/homekit/hmhome/1620261-isprimary)

|  | Declaration |
| --- | --- |
| From | ``` var primary: Bool { get } ``` |
| To | ``` var isPrimary: Bool { get } ``` |

Modified [HMHome.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmhome/1620243-uniqueidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var uniqueIdentifier: NSUUID { get } ``` |
| To | ``` var uniqueIdentifier: UUID { get } ``` |

Modified [HMHomeAccessControl](https://developer.apple.com/documentation/homekit/hmhomeaccesscontrol)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMHomeAccessControl : NSObject {     init()     var administrator: Bool { get } } ``` | -- |
| To | ``` class HMHomeAccessControl : NSObject {     init()     var isAdministrator: Bool { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMHomeAccessControl : CVarArg { } extension HMHomeAccessControl : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMHomeAccessControl.isAdministrator](https://developer.apple.com/documentation/homekit/hmhomeaccesscontrol/1624331-administrator)

|  | Declaration |
| --- | --- |
| From | ``` var administrator: Bool { get } ``` |
| To | ``` var isAdministrator: Bool { get } ``` |

Modified [HMHomeDelegate](https://developer.apple.com/documentation/homekit/hmhomedelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol HMHomeDelegate : NSObjectProtocol {     optional func homeDidUpdateName(_ home: HMHome)     optional func home(_ home: HMHome, didAddAccessory accessory: HMAccessory)     optional func home(_ home: HMHome, didRemoveAccessory accessory: HMAccessory)     optional func home(_ home: HMHome, didAddUser user: HMUser)     optional func home(_ home: HMHome, didRemoveUser user: HMUser)     optional func home(_ home: HMHome, didUpdateRoom room: HMRoom, forAccessory accessory: HMAccessory)     optional func home(_ home: HMHome, didAddRoom room: HMRoom)     optional func home(_ home: HMHome, didRemoveRoom room: HMRoom)     optional func home(_ home: HMHome, didUpdateNameForRoom room: HMRoom)     optional func home(_ home: HMHome, didAddZone zone: HMZone)     optional func home(_ home: HMHome, didRemoveZone zone: HMZone)     optional func home(_ home: HMHome, didUpdateNameForZone zone: HMZone)     optional func home(_ home: HMHome, didAddRoom room: HMRoom, toZone zone: HMZone)     optional func home(_ home: HMHome, didRemoveRoom room: HMRoom, fromZone zone: HMZone)     optional func home(_ home: HMHome, didAddServiceGroup group: HMServiceGroup)     optional func home(_ home: HMHome, didRemoveServiceGroup group: HMServiceGroup)     optional func home(_ home: HMHome, didUpdateNameForServiceGroup group: HMServiceGroup)     optional func home(_ home: HMHome, didAddService service: HMService, toServiceGroup group: HMServiceGroup)     optional func home(_ home: HMHome, didRemoveService service: HMService, fromServiceGroup group: HMServiceGroup)     optional func home(_ home: HMHome, didAddActionSet actionSet: HMActionSet)     optional func home(_ home: HMHome, didRemoveActionSet actionSet: HMActionSet)     optional func home(_ home: HMHome, didUpdateNameForActionSet actionSet: HMActionSet)     optional func home(_ home: HMHome, didUpdateActionsForActionSet actionSet: HMActionSet)     optional func home(_ home: HMHome, didAddTrigger trigger: HMTrigger)     optional func home(_ home: HMHome, didRemoveTrigger trigger: HMTrigger)     optional func home(_ home: HMHome, didUpdateNameForTrigger trigger: HMTrigger)     optional func home(_ home: HMHome, didUpdateTrigger trigger: HMTrigger)     optional func home(_ home: HMHome, didUnblockAccessory accessory: HMAccessory)     optional func home(_ home: HMHome, didEncounterError error: NSError, forAccessory accessory: HMAccessory) } ``` |
| To | ``` protocol HMHomeDelegate : NSObjectProtocol {     optional func homeDidUpdateName(_ home: HMHome)     optional func home(_ home: HMHome, didAdd accessory: HMAccessory)     optional func home(_ home: HMHome, didRemove accessory: HMAccessory)     optional func home(_ home: HMHome, didAdd user: HMUser)     optional func home(_ home: HMHome, didRemove user: HMUser)     optional func home(_ home: HMHome, didUpdate room: HMRoom, for accessory: HMAccessory)     optional func home(_ home: HMHome, didAdd room: HMRoom)     optional func home(_ home: HMHome, didRemove room: HMRoom)     optional func home(_ home: HMHome, didUpdateNameFor room: HMRoom)     optional func home(_ home: HMHome, didAdd zone: HMZone)     optional func home(_ home: HMHome, didRemove zone: HMZone)     optional func home(_ home: HMHome, didUpdateNameFor zone: HMZone)     optional func home(_ home: HMHome, didAdd room: HMRoom, to zone: HMZone)     optional func home(_ home: HMHome, didRemove room: HMRoom, from zone: HMZone)     optional func home(_ home: HMHome, didAdd group: HMServiceGroup)     optional func home(_ home: HMHome, didRemove group: HMServiceGroup)     optional func home(_ home: HMHome, didUpdateNameFor group: HMServiceGroup)     optional func home(_ home: HMHome, didAdd service: HMService, to group: HMServiceGroup)     optional func home(_ home: HMHome, didRemove service: HMService, from group: HMServiceGroup)     optional func home(_ home: HMHome, didAdd actionSet: HMActionSet)     optional func home(_ home: HMHome, didRemove actionSet: HMActionSet)     optional func home(_ home: HMHome, didUpdateNameFor actionSet: HMActionSet)     optional func home(_ home: HMHome, didUpdateActionsFor actionSet: HMActionSet)     optional func home(_ home: HMHome, didAdd trigger: HMTrigger)     optional func home(_ home: HMHome, didRemove trigger: HMTrigger)     optional func home(_ home: HMHome, didUpdateNameFor trigger: HMTrigger)     optional func home(_ home: HMHome, didUpdate trigger: HMTrigger)     optional func home(_ home: HMHome, didUnblockAccessory accessory: HMAccessory)     optional func home(_ home: HMHome, didEncounterError error: Error, for accessory: HMAccessory) } ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAdd: HMUser)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620217-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddUser user: HMUser) ``` |
| To | ``` optional func home(_ home: HMHome, didAdd user: HMUser) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAdd: HMRoom)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620244-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddRoom room: HMRoom) ``` |
| To | ``` optional func home(_ home: HMHome, didAdd room: HMRoom) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAdd: HMTrigger)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620258-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddTrigger trigger: HMTrigger) ``` |
| To | ``` optional func home(_ home: HMHome, didAdd trigger: HMTrigger) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAdd: HMActionSet)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620277-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddActionSet actionSet: HMActionSet) ``` |
| To | ``` optional func home(_ home: HMHome, didAdd actionSet: HMActionSet) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAdd: HMAccessory)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620215-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddAccessory accessory: HMAccessory) ``` |
| To | ``` optional func home(_ home: HMHome, didAdd accessory: HMAccessory) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAdd: HMZone)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620249-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddZone zone: HMZone) ``` |
| To | ``` optional func home(_ home: HMHome, didAdd zone: HMZone) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAdd: HMServiceGroup)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620211-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddServiceGroup group: HMServiceGroup) ``` |
| To | ``` optional func home(_ home: HMHome, didAdd group: HMServiceGroup) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAdd: HMService, to: HMServiceGroup)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620274-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddService service: HMService, toServiceGroup group: HMServiceGroup) ``` |
| To | ``` optional func home(_ home: HMHome, didAdd service: HMService, to group: HMServiceGroup) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAdd: HMRoom, to: HMZone)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620241-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddRoom room: HMRoom, toZone zone: HMZone) ``` |
| To | ``` optional func home(_ home: HMHome, didAdd room: HMRoom, to zone: HMZone) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didEncounterError: Error, for: HMAccessory)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620247-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didEncounterError error: NSError, forAccessory accessory: HMAccessory) ``` |
| To | ``` optional func home(_ home: HMHome, didEncounterError error: Error, for accessory: HMAccessory) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemove: HMTrigger)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620262-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveTrigger trigger: HMTrigger) ``` |
| To | ``` optional func home(_ home: HMHome, didRemove trigger: HMTrigger) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemove: HMUser)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620232-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveUser user: HMUser) ``` |
| To | ``` optional func home(_ home: HMHome, didRemove user: HMUser) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemove: HMServiceGroup)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620226-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveServiceGroup group: HMServiceGroup) ``` |
| To | ``` optional func home(_ home: HMHome, didRemove group: HMServiceGroup) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemove: HMZone)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620221-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveZone zone: HMZone) ``` |
| To | ``` optional func home(_ home: HMHome, didRemove zone: HMZone) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemove: HMRoom)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620270-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveRoom room: HMRoom) ``` |
| To | ``` optional func home(_ home: HMHome, didRemove room: HMRoom) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemove: HMAccessory)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620263-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveAccessory accessory: HMAccessory) ``` |
| To | ``` optional func home(_ home: HMHome, didRemove accessory: HMAccessory) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemove: HMActionSet)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620267-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveActionSet actionSet: HMActionSet) ``` |
| To | ``` optional func home(_ home: HMHome, didRemove actionSet: HMActionSet) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemove: HMService, from: HMServiceGroup)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620242-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveService service: HMService, fromServiceGroup group: HMServiceGroup) ``` |
| To | ``` optional func home(_ home: HMHome, didRemove service: HMService, from group: HMServiceGroup) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemove: HMRoom, from: HMZone)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620222-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveRoom room: HMRoom, fromZone zone: HMZone) ``` |
| To | ``` optional func home(_ home: HMHome, didRemove room: HMRoom, from zone: HMZone) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdate: HMTrigger)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620219-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateTrigger trigger: HMTrigger) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdate trigger: HMTrigger) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdate: HMRoom, for: HMAccessory)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620237-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateRoom room: HMRoom, forAccessory accessory: HMAccessory) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdate room: HMRoom, for accessory: HMAccessory) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdateActionsFor: HMActionSet)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620259-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateActionsForActionSet actionSet: HMActionSet) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdateActionsFor actionSet: HMActionSet) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdateNameFor: HMActionSet)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620248-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateNameForActionSet actionSet: HMActionSet) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdateNameFor actionSet: HMActionSet) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdateNameFor: HMRoom)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620272-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateNameForRoom room: HMRoom) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdateNameFor room: HMRoom) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdateNameFor: HMZone)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620228-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateNameForZone zone: HMZone) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdateNameFor zone: HMZone) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdateNameFor: HMServiceGroup)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620253-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateNameForServiceGroup group: HMServiceGroup) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdateNameFor group: HMServiceGroup) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdateNameFor: HMTrigger)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620239-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateNameForTrigger trigger: HMTrigger) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdateNameFor trigger: HMTrigger) ``` |

Modified [HMHomeManager](https://developer.apple.com/documentation/homekit/hmhomemanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMHomeManager : NSObject {     weak var delegate: HMHomeManagerDelegate?     var primaryHome: HMHome? { get }     var homes: [HMHome] { get }     func updatePrimaryHome(_ home: HMHome, completionHandler completion: (NSError?) -> Void)     func addHomeWithName(_ homeName: String, completionHandler completion: (HMHome?, NSError?) -> Void)     func removeHome(_ home: HMHome, completionHandler completion: (NSError?) -> Void) } ``` | -- |
| To | ``` class HMHomeManager : NSObject {     weak var delegate: HMHomeManagerDelegate?     var primaryHome: HMHome? { get }     var homes: [HMHome] { get }     func updatePrimaryHome(_ home: HMHome, completionHandler completion: @escaping (Error?) -> Swift.Void)     func addHome(withName homeName: String, completionHandler completion: @escaping (HMHome?, Error?) -> Swift.Void)     func removeHome(_ home: HMHome, completionHandler completion: @escaping (Error?) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMHomeManager : CVarArg { } extension HMHomeManager : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMHomeManagerDelegate](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol HMHomeManagerDelegate : NSObjectProtocol {     optional func homeManagerDidUpdateHomes(_ manager: HMHomeManager)     optional func homeManagerDidUpdatePrimaryHome(_ manager: HMHomeManager)     optional func homeManager(_ manager: HMHomeManager, didAddHome home: HMHome)     optional func homeManager(_ manager: HMHomeManager, didRemoveHome home: HMHome) } ``` |
| To | ``` protocol HMHomeManagerDelegate : NSObjectProtocol {     optional func homeManagerDidUpdateHomes(_ manager: HMHomeManager)     optional func homeManagerDidUpdatePrimaryHome(_ manager: HMHomeManager)     optional func homeManager(_ manager: HMHomeManager, didAdd home: HMHome)     optional func homeManager(_ manager: HMHomeManager, didRemove home: HMHome) } ``` |

Modified [HMHomeManagerDelegate.homeManager(_: HMHomeManager, didAdd: HMHome)](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/1616755-homemanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func homeManager(_ manager: HMHomeManager, didAddHome home: HMHome) ``` |
| To | ``` optional func homeManager(_ manager: HMHomeManager, didAdd home: HMHome) ``` |

Modified [HMHomeManagerDelegate.homeManager(_: HMHomeManager, didRemove: HMHome)](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/1616753-homemanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func homeManager(_ manager: HMHomeManager, didRemoveHome home: HMHome) ``` |
| To | ``` optional func homeManager(_ manager: HMHomeManager, didRemove home: HMHome) ``` |

Modified [HMLocationEvent](https://developer.apple.com/documentation/homekit/hmlocationevent)

|  | Declaration |
| --- | --- |
| From | ``` class HMLocationEvent : HMEvent {     init()     init(region region: CLRegion)     var region: CLRegion? { get }     func updateRegion(_ region: CLRegion, completionHandler completion: (NSError?) -> Void) } ``` |
| To | ``` class HMLocationEvent : HMEvent {     init()     init(region region: CLRegion)     var region: CLRegion? { get }     func updateRegion(_ region: CLRegion, completionHandler completion: @escaping (Error?) -> Swift.Void) } ``` |

Modified [HMRoom](https://developer.apple.com/documentation/homekit/hmroom)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMRoom : NSObject {     init()     var name: String { get }     var accessories: [HMAccessory] { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void) } ``` | -- |
| To | ``` class HMRoom : NSObject {     init()     var name: String { get }     var accessories: [HMAccessory] { get }     var uniqueIdentifier: UUID { get }     func updateName(_ name: String, completionHandler completion: @escaping (Error?) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMRoom : CVarArg { } extension HMRoom : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMRoom.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmroom/1618291-uniqueidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var uniqueIdentifier: NSUUID { get } ``` |
| To | ``` var uniqueIdentifier: UUID { get } ``` |

Modified [HMService](https://developer.apple.com/documentation/homekit/hmservice)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMService : NSObject {     weak var accessory: HMAccessory? { get }     var serviceType: String { get }     var localizedDescription: String { get }     var name: String { get }     var associatedServiceType: String? { get }     var characteristics: [HMCharacteristic] { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     var userInteractive: Bool { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void)     func updateAssociatedServiceType(_ serviceType: String?, completionHandler completion: (NSError?) -> Void) } ``` | -- |
| To | ``` class HMService : NSObject {     weak var accessory: HMAccessory? { get }     var serviceType: String { get }     var localizedDescription: String { get }     var name: String { get }     var associatedServiceType: String? { get }     var characteristics: [HMCharacteristic] { get }     var uniqueIdentifier: UUID { get }     var isUserInteractive: Bool { get }     var isPrimaryService: Bool { get }     var linkedServices: [HMService]? { get }     func updateName(_ name: String, completionHandler completion: @escaping (Error?) -> Swift.Void)     func updateAssociatedServiceType(_ serviceType: String?, completionHandler completion: @escaping (Error?) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMService : CVarArg { } extension HMService : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMService.isUserInteractive](https://developer.apple.com/documentation/homekit/hmservice/1615891-userinteractive)

|  | Declaration |
| --- | --- |
| From | ``` var userInteractive: Bool { get } ``` |
| To | ``` var isUserInteractive: Bool { get } ``` |

Modified [HMService.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmservice/1615883-uniqueidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var uniqueIdentifier: NSUUID { get } ``` |
| To | ``` var uniqueIdentifier: UUID { get } ``` |

Modified [HMServiceGroup](https://developer.apple.com/documentation/homekit/hmservicegroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMServiceGroup : NSObject {     init()     var name: String { get }     var services: [HMService] { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void)     func addService(_ service: HMService, completionHandler completion: (NSError?) -> Void)     func removeService(_ service: HMService, completionHandler completion: (NSError?) -> Void) } ``` | -- |
| To | ``` class HMServiceGroup : NSObject {     init()     var name: String { get }     var services: [HMService] { get }     var uniqueIdentifier: UUID { get }     func updateName(_ name: String, completionHandler completion: @escaping (Error?) -> Swift.Void)     func addService(_ service: HMService, completionHandler completion: @escaping (Error?) -> Swift.Void)     func removeService(_ service: HMService, completionHandler completion: @escaping (Error?) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMServiceGroup : CVarArg { } extension HMServiceGroup : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMServiceGroup.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmservicegroup/1616991-uniqueidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var uniqueIdentifier: NSUUID { get } ``` |
| To | ``` var uniqueIdentifier: UUID { get } ``` |

Modified [HMTimerTrigger](https://developer.apple.com/documentation/homekit/hmtimertrigger)

|  | Declaration |
| --- | --- |
| From | ``` class HMTimerTrigger : HMTrigger {     convenience init()     init(name name: String, fireDate fireDate: NSDate, timeZone timeZone: NSTimeZone?, recurrence recurrence: NSDateComponents?, recurrenceCalendar recurrenceCalendar: NSCalendar?)     @NSCopying var fireDate: NSDate { get }     @NSCopying var timeZone: NSTimeZone? { get }     @NSCopying var recurrence: NSDateComponents? { get }     @NSCopying var recurrenceCalendar: NSCalendar? { get }     func updateFireDate(_ fireDate: NSDate, completionHandler completion: (NSError?) -> Void)     func updateTimeZone(_ timeZone: NSTimeZone?, completionHandler completion: (NSError?) -> Void)     func updateRecurrence(_ recurrence: NSDateComponents?, completionHandler completion: (NSError?) -> Void) } ``` |
| To | ``` class HMTimerTrigger : HMTrigger {     convenience init()     init(name name: String, fireDate fireDate: Date, timeZone timeZone: TimeZone?, recurrence recurrence: DateComponents?, recurrenceCalendar recurrenceCalendar: Calendar?)     var fireDate: Date { get }     var timeZone: TimeZone? { get }     var recurrence: DateComponents? { get }     var recurrenceCalendar: Calendar? { get }     func updateFireDate(_ fireDate: Date, completionHandler completion: @escaping (Error?) -> Swift.Void)     func updateTimeZone(_ timeZone: TimeZone?, completionHandler completion: @escaping (Error?) -> Swift.Void)     func updateRecurrence(_ recurrence: DateComponents?, completionHandler completion: @escaping (Error?) -> Swift.Void) } ``` |

Modified [HMTimerTrigger.fireDate](https://developer.apple.com/documentation/homekit/hmtimertrigger/1616261-firedate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var fireDate: NSDate { get } ``` |
| To | ``` var fireDate: Date { get } ``` |

Modified [HMTimerTrigger.recurrence](https://developer.apple.com/documentation/homekit/hmtimertrigger/1616260-recurrence)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var recurrence: NSDateComponents? { get } ``` |
| To | ``` var recurrence: DateComponents? { get } ``` |

Modified [HMTimerTrigger.recurrenceCalendar](https://developer.apple.com/documentation/homekit/hmtimertrigger/1616264-recurrencecalendar)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var recurrenceCalendar: NSCalendar? { get } ``` |
| To | ``` var recurrenceCalendar: Calendar? { get } ``` |

Modified [HMTimerTrigger.timeZone](https://developer.apple.com/documentation/homekit/hmtimertrigger/1616268-timezone)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var timeZone: NSTimeZone? { get } ``` |
| To | ``` var timeZone: TimeZone? { get } ``` |

Modified [HMTrigger](https://developer.apple.com/documentation/homekit/hmtrigger)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMTrigger : NSObject {     init()     var name: String { get }     var enabled: Bool { get }     var actionSets: [HMActionSet] { get }     @NSCopying var lastFireDate: NSDate? { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void)     func addActionSet(_ actionSet: HMActionSet, completionHandler completion: (NSError?) -> Void)     func removeActionSet(_ actionSet: HMActionSet, completionHandler completion: (NSError?) -> Void)     func enable(_ enable: Bool, completionHandler completion: (NSError?) -> Void) } ``` | -- |
| To | ``` class HMTrigger : NSObject {     init()     var name: String { get }     var isEnabled: Bool { get }     var actionSets: [HMActionSet] { get }     var lastFireDate: Date? { get }     var uniqueIdentifier: UUID { get }     func updateName(_ name: String, completionHandler completion: @escaping (Error?) -> Swift.Void)     func addActionSet(_ actionSet: HMActionSet, completionHandler completion: @escaping (Error?) -> Swift.Void)     func removeActionSet(_ actionSet: HMActionSet, completionHandler completion: @escaping (Error?) -> Swift.Void)     func enable(_ enable: Bool, completionHandler completion: @escaping (Error?) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMTrigger : CVarArg { } extension HMTrigger : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMTrigger.isEnabled](https://developer.apple.com/documentation/homekit/hmtrigger/1620713-isenabled)

|  | Declaration |
| --- | --- |
| From | ``` var enabled: Bool { get } ``` |
| To | ``` var isEnabled: Bool { get } ``` |

Modified [HMTrigger.lastFireDate](https://developer.apple.com/documentation/homekit/hmtrigger/1620715-lastfiredate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var lastFireDate: NSDate? { get } ``` |
| To | ``` var lastFireDate: Date? { get } ``` |

Modified [HMTrigger.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmtrigger/1620720-uniqueidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var uniqueIdentifier: NSUUID { get } ``` |
| To | ``` var uniqueIdentifier: UUID { get } ``` |

Modified [HMUser](https://developer.apple.com/documentation/homekit/hmuser)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMUser : NSObject {     init()     var name: String { get }     @NSCopying var uniqueIdentifier: NSUUID { get } } ``` | -- |
| To | ``` class HMUser : NSObject {     init()     var name: String { get }     var uniqueIdentifier: UUID { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMUser : CVarArg { } extension HMUser : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMUser.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmuser/1620013-uniqueidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var uniqueIdentifier: NSUUID { get } ``` |
| To | ``` var uniqueIdentifier: UUID { get } ``` |

Modified [HMZone](https://developer.apple.com/documentation/homekit/hmzone)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HMZone : NSObject {     init()     var name: String { get }     var rooms: [HMRoom] { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void)     func addRoom(_ room: HMRoom, completionHandler completion: (NSError?) -> Void)     func removeRoom(_ room: HMRoom, completionHandler completion: (NSError?) -> Void) } ``` | -- |
| To | ``` class HMZone : NSObject {     init()     var name: String { get }     var rooms: [HMRoom] { get }     var uniqueIdentifier: UUID { get }     func updateName(_ name: String, completionHandler completion: @escaping (Error?) -> Swift.Void)     func addRoom(_ room: HMRoom, completionHandler completion: @escaping (Error?) -> Swift.Void)     func removeRoom(_ room: HMRoom, completionHandler completion: @escaping (Error?) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension HMZone : CVarArg { } extension HMZone : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [HMZone.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmzone/1624766-uniqueidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var uniqueIdentifier: NSUUID { get } ``` |
| To | ``` var uniqueIdentifier: UUID { get } ``` |

Modified [NSNotification.Name.HMCharacteristicPropertySupportsEvent](https://developer.apple.com/documentation/foundation/nsnotification/name/1616329-hmcharacteristicpropertysupports)

|  | Name | Declaration |
| --- | --- | --- |
| From | HMCharacteristicPropertySupportsEventNotification | ``` let HMCharacteristicPropertySupportsEventNotification: String ``` |
| To | HMCharacteristicPropertySupportsEvent | ``` static let HMCharacteristicPropertySupportsEvent: NSNotification.Name ``` |

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
