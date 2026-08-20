---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/ForceFeedback.html
archived_at: '2026-07-15T07:34:54.375898Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# ForceFeedback Changes

## ForceFeedback (Added)

Added FFCAPABILITIES [struct]Added FFCAPABILITIES.driverVerAdded FFCAPABILITIES.emulatedEffectsAdded FFCAPABILITIES.ffAxesAdded FFCAPABILITIES.ffSpecVerAdded FFCAPABILITIES.firmwareVerAdded FFCAPABILITIES.hardwareVerAdded FFCAPABILITIES.numFfAxesAdded FFCAPABILITIES.playbackCapacityAdded FFCAPABILITIES.storageCapacityAdded FFCAPABILITIES.subTypeAdded FFCAPABILITIES.supportedEffectsAdded FFCONDITION [struct]Added FFCONDITION.dwNegativeSaturationAdded FFCONDITION.dwPositiveSaturationAdded FFCONDITION.lDeadBandAdded FFCONDITION.lNegativeCoefficientAdded FFCONDITION.lOffsetAdded FFCONDITION.lPositiveCoefficientAdded FFCONSTANTFORCE [struct]Added FFCONSTANTFORCE.lMagnitudeAdded FFCUSTOMFORCE [struct]Added FFCUSTOMFORCE.cChannelsAdded FFCUSTOMFORCE.cSamplesAdded FFCUSTOMFORCE.dwSamplePeriodAdded FFCUSTOMFORCE.rglForceDataAdded FFEFFECT [struct]Added FFEFFECT.cAxesAdded FFEFFECT.cbTypeSpecificParamsAdded FFEFFECT.dwDurationAdded FFEFFECT.dwFlagsAdded FFEFFECT.dwGainAdded FFEFFECT.dwSamplePeriodAdded FFEFFECT.dwSizeAdded FFEFFECT.dwStartDelayAdded FFEFFECT.dwTriggerButtonAdded FFEFFECT.dwTriggerRepeatIntervalAdded FFEFFECT.lpEnvelopeAdded FFEFFECT.lpvTypeSpecificParamsAdded FFEFFECT.rgdwAxesAdded FFEFFECT.rglDirectionAdded FFEFFESCAPE [struct]Added FFEFFESCAPE.cbInBufferAdded FFEFFESCAPE.cbOutBufferAdded FFEFFESCAPE.dwCommandAdded FFEFFESCAPE.dwSizeAdded FFEFFESCAPE.lpvInBufferAdded FFEFFESCAPE.lpvOutBufferAdded FFENVELOPE [struct]Added FFENVELOPE.dwAttackLevelAdded FFENVELOPE.dwAttackTimeAdded FFENVELOPE.dwFadeLevelAdded FFENVELOPE.dwFadeTimeAdded FFENVELOPE.dwSizeAdded FFPERIODIC [struct]Added FFPERIODIC.dwMagnitudeAdded FFPERIODIC.dwPeriodAdded FFPERIODIC.dwPhaseAdded FFPERIODIC.lOffsetAdded FFRAMPFORCE [struct]Added FFRAMPFORCE.lEndAdded FFRAMPFORCE.lStartAdded DWORDAdded E_PENDINGAdded FFCAP_ET_CONSTANTFORCEAdded FFCAP_ET_CUSTOMFORCEAdded FFCAP_ET_DAMPERAdded FFCAP_ET_FRICTIONAdded FFCAP_ET_INERTIAAdded FFCAP_ET_RAMPFORCEAdded FFCAP_ET_SAWTOOTHDOWNAdded FFCAP_ET_SAWTOOTHUPAdded FFCAP_ET_SINEAdded FFCAP_ET_SPRINGAdded FFCAP_ET_SQUAREAdded FFCAP_ET_TRIANGLEAdded FFCAP_ST_KINESTHETICAdded FFCAP_ST_VIBRATIONAdded FFCapabilitiesEffectSubTypeAdded FFCapabilitiesEffectTypeAdded FFCommandFlagAdded FFCooperativeLevelFlagAdded FFCoordinateSystemFlagAdded FFCreateDevice(io_service_t, UnsafeMutablePointer<FFDeviceObjectReference>) -> HRESULTAdded FFDeviceCreateEffect(FFDeviceObjectReference, CFUUID!, UnsafeMutablePointer<FFEFFECT>, UnsafeMutablePointer<FFEffectObjectReference>) -> HRESULTAdded FFDeviceEscape(FFDeviceObjectReference, UnsafeMutablePointer<FFEFFESCAPE>) -> HRESULTAdded FFDeviceGetForceFeedbackCapabilities(FFDeviceObjectReference, UnsafeMutablePointer<FFCAPABILITIES>) -> HRESULTAdded FFDeviceGetForceFeedbackProperty(FFDeviceObjectReference, FFProperty, UnsafeMutablePointer<Void>, IOByteCount) -> HRESULTAdded FFDeviceGetForceFeedbackState(FFDeviceObjectReference, UnsafeMutablePointer<FFState>) -> HRESULTAdded FFDeviceObjectReferenceAdded FFDeviceReleaseEffect(FFDeviceObjectReference, FFEffectObjectReference) -> HRESULTAdded FFDeviceSendForceFeedbackCommand(FFDeviceObjectReference, FFCommandFlag) -> HRESULTAdded FFDeviceSetCooperativeLevel(FFDeviceObjectReference, UnsafeMutablePointer<Void>, FFCooperativeLevelFlag) -> HRESULTAdded FFDeviceSetForceFeedbackProperty(FFDeviceObjectReference, FFProperty, UnsafeMutablePointer<Void>) -> HRESULTAdded FFEB_NOTRIGGERAdded FFEFF_CARTESIANAdded FFEFF_OBJECTOFFSETSAdded FFEFF_POLARAdded FFEFF_SPHERICALAdded FFEGES_EMULATEDAdded FFEGES_NOTPLAYINGAdded FFEGES_PLAYINGAdded FFEP_ALLPARAMSAdded FFEP_AXESAdded FFEP_DIRECTIONAdded FFEP_DURATIONAdded FFEP_ENVELOPEAdded FFEP_GAINAdded FFEP_NODOWNLOADAdded FFEP_NORESTARTAdded FFEP_SAMPLEPERIODAdded FFEP_STARTAdded FFEP_STARTDELAYAdded FFEP_TRIGGERBUTTONAdded FFEP_TRIGGERREPEATINTERVALAdded FFEP_TYPESPECIFICPARAMSAdded FFERR_DEVICEFULLAdded FFERR_DEVICEPAUSEDAdded FFERR_DEVICERELEASEDAdded FFERR_EFFECTPLAYINGAdded FFERR_EFFECTTYPEMISMATCHAdded FFERR_EFFECTTYPENOTSUPPORTEDAdded FFERR_HASEFFECTSAdded FFERR_INCOMPLETEEFFECTAdded FFERR_INTERNALAdded FFERR_INVALIDDOWNLOADIDAdded FFERR_MOREDATAAdded FFERR_NOTDOWNLOADEDAdded FFERR_NOTINITIALIZEDAdded FFERR_UNPLUGGEDAdded FFERR_UNSUPPORTEDAXISAdded FFES_NODOWNLOADAdded FFES_SOLOAdded FFEffectDownload(FFEffectObjectReference) -> HRESULTAdded FFEffectEscape(FFEffectObjectReference, UnsafeMutablePointer<FFEFFESCAPE>) -> HRESULTAdded FFEffectGetEffectStatus(FFEffectObjectReference, UnsafeMutablePointer<FFEffectStatusFlag>) -> HRESULTAdded FFEffectGetParameters(FFEffectObjectReference, UnsafeMutablePointer<FFEFFECT>, FFEffectParameterFlag) -> HRESULTAdded FFEffectObjectReferenceAdded FFEffectParameterFlagAdded FFEffectSetParameters(FFEffectObjectReference, UnsafeMutablePointer<FFEFFECT>, FFEffectParameterFlag) -> HRESULTAdded FFEffectStart(FFEffectObjectReference, UInt32, FFEffectStartFlag) -> HRESULTAdded FFEffectStartFlagAdded FFEffectStatusFlagAdded FFEffectStop(FFEffectObjectReference) -> HRESULTAdded FFEffectUnload(FFEffectObjectReference) -> HRESULTAdded FFGFFS_ACTUATORSOFFAdded FFGFFS_ACTUATORSONAdded FFGFFS_DEVICELOSTAdded FFGFFS_EMPTYAdded FFGFFS_PAUSEDAdded FFGFFS_POWEROFFAdded FFGFFS_POWERONAdded FFGFFS_SAFETYSWITCHOFFAdded FFGFFS_SAFETYSWITCHONAdded FFGFFS_STOPPEDAdded FFGFFS_USERFFSWITCHOFFAdded FFGFFS_USERFFSWITCHONAdded FFIsForceFeedback(io_service_t) -> HRESULTAdded FFJOFS_RXAdded FFJOFS_RYAdded FFJOFS_RZAdded FFJOFS_XAdded FFJOFS_YAdded FFJOFS_ZAdded FFPROP_AUTOCENTERAdded FFPROP_FFGAINAdded FFPropertyAdded FFReleaseDevice(FFDeviceObjectReference) -> HRESULTAdded FFSCL_BACKGROUNDAdded FFSCL_EXCLUSIVEAdded FFSCL_FOREGROUNDAdded FFSCL_NONEXCLUSIVEAdded FFSFFC_CONTINUEAdded FFSFFC_PAUSEAdded FFSFFC_RESETAdded FFSFFC_SETACTUATORSOFFAdded FFSFFC_SETACTUATORSONAdded FFSFFC_STOPALLAdded FFStateAdded FF_DEGREESAdded FF_FFNOMINALMAXAdded FF_INFINITEAdded FF_SECONDSAdded LONGAdded LPDWORDAdded LPLONGAdded PFFCAPABILITIESAdded PFFCONDITIONAdded PFFCONSTANTFORCEAdded PFFCUSTOMFORCEAdded PFFEFFECTAdded PFFEFFESCAPEAdded PFFENVELOPEAdded PFFPERIODICAdded PFFRAMPFORCEAdded kFFAPIMajorRevAdded kFFAPIMinorAndBugRevAdded kFFAPINonRelRevAdded kFFAPIStage

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
