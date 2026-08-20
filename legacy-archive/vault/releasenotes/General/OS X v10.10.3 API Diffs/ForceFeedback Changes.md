---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/ForceFeedback.html
archived_at: '2026-07-18T02:52:24.604335Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# ForceFeedback Changes

## ForceFeedback

Added FFCAPABILITIES.init()Added FFCAPABILITIES.init(ffSpecVer: NumVersion, supportedEffects: UInt32, emulatedEffects: UInt32, subType: UInt32, numFfAxes: UInt32, ffAxes:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), storageCapacity: UInt32, playbackCapacity: UInt32, firmwareVer: NumVersion, hardwareVer: NumVersion, driverVer: NumVersion)Added FFCONDITION.init()Added FFCONDITION.init(lOffset: LONG, lPositiveCoefficient: LONG, lNegativeCoefficient: LONG, dwPositiveSaturation: DWORD, dwNegativeSaturation: DWORD, lDeadBand: LONG)Added FFCONSTANTFORCE.init()Added FFCONSTANTFORCE.init(lMagnitude: LONG)Added FFCUSTOMFORCE.init()Added FFCUSTOMFORCE.init(cChannels: DWORD, dwSamplePeriod: DWORD, cSamples: DWORD, rglForceData: LPLONG)Added FFEFFECT.init()Added FFEFFECT.init(dwSize: DWORD, dwFlags: DWORD, dwDuration: DWORD, dwSamplePeriod: DWORD, dwGain: DWORD, dwTriggerButton: DWORD, dwTriggerRepeatInterval: DWORD, cAxes: DWORD, rgdwAxes: LPDWORD, rglDirection: LPLONG, lpEnvelope: PFFENVELOPE, cbTypeSpecificParams: DWORD, lpvTypeSpecificParams: UnsafeMutablePointer<Void>, dwStartDelay: DWORD)Added FFEFFESCAPE.init()Added FFEFFESCAPE.init(dwSize: DWORD, dwCommand: DWORD, lpvInBuffer: UnsafeMutablePointer<Void>, cbInBuffer: DWORD, lpvOutBuffer: UnsafeMutablePointer<Void>, cbOutBuffer: DWORD)Added FFENVELOPE.init()Added FFENVELOPE.init(dwSize: DWORD, dwAttackLevel: DWORD, dwAttackTime: DWORD, dwFadeLevel: DWORD, dwFadeTime: DWORD)Added FFPERIODIC.init()Added FFPERIODIC.init(dwMagnitude: DWORD, lOffset: LONG, dwPhase: DWORD, dwPeriod: DWORD)Added FFRAMPFORCE.init()Added FFRAMPFORCE.init(lStart: LONG, lEnd: LONG)Modified FFCAPABILITIES [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FFCAPABILITIES {     var ffSpecVer: NumVersion     var supportedEffects: UInt32     var emulatedEffects: UInt32     var subType: UInt32     var numFfAxes: UInt32     var ffAxes: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var storageCapacity: UInt32     var playbackCapacity: UInt32     var firmwareVer: NumVersion     var hardwareVer: NumVersion     var driverVer: NumVersion } ``` |
| To | ``` struct FFCAPABILITIES {     var ffSpecVer: NumVersion     var supportedEffects: UInt32     var emulatedEffects: UInt32     var subType: UInt32     var numFfAxes: UInt32     var ffAxes: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var storageCapacity: UInt32     var playbackCapacity: UInt32     var firmwareVer: NumVersion     var hardwareVer: NumVersion     var driverVer: NumVersion     init()     init(ffSpecVer ffSpecVer: NumVersion, supportedEffects supportedEffects: UInt32, emulatedEffects emulatedEffects: UInt32, subType subType: UInt32, numFfAxes numFfAxes: UInt32, ffAxes ffAxes: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), storageCapacity storageCapacity: UInt32, playbackCapacity playbackCapacity: UInt32, firmwareVer firmwareVer: NumVersion, hardwareVer hardwareVer: NumVersion, driverVer driverVer: NumVersion) } ``` |

Modified FFCONDITION [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FFCONDITION {     var lOffset: LONG     var lPositiveCoefficient: LONG     var lNegativeCoefficient: LONG     var dwPositiveSaturation: DWORD     var dwNegativeSaturation: DWORD     var lDeadBand: LONG } ``` |
| To | ``` struct FFCONDITION {     var lOffset: LONG     var lPositiveCoefficient: LONG     var lNegativeCoefficient: LONG     var dwPositiveSaturation: DWORD     var dwNegativeSaturation: DWORD     var lDeadBand: LONG     init()     init(lOffset lOffset: LONG, lPositiveCoefficient lPositiveCoefficient: LONG, lNegativeCoefficient lNegativeCoefficient: LONG, dwPositiveSaturation dwPositiveSaturation: DWORD, dwNegativeSaturation dwNegativeSaturation: DWORD, lDeadBand lDeadBand: LONG) } ``` |

Modified FFCONSTANTFORCE [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FFCONSTANTFORCE {     var lMagnitude: LONG } ``` |
| To | ``` struct FFCONSTANTFORCE {     var lMagnitude: LONG     init()     init(lMagnitude lMagnitude: LONG) } ``` |

Modified FFCUSTOMFORCE [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FFCUSTOMFORCE {     var cChannels: DWORD     var dwSamplePeriod: DWORD     var cSamples: DWORD     var rglForceData: LPLONG } ``` |
| To | ``` struct FFCUSTOMFORCE {     var cChannels: DWORD     var dwSamplePeriod: DWORD     var cSamples: DWORD     var rglForceData: LPLONG     init()     init(cChannels cChannels: DWORD, dwSamplePeriod dwSamplePeriod: DWORD, cSamples cSamples: DWORD, rglForceData rglForceData: LPLONG) } ``` |

Modified FFEFFECT [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FFEFFECT {     var dwSize: DWORD     var dwFlags: DWORD     var dwDuration: DWORD     var dwSamplePeriod: DWORD     var dwGain: DWORD     var dwTriggerButton: DWORD     var dwTriggerRepeatInterval: DWORD     var cAxes: DWORD     var rgdwAxes: LPDWORD     var rglDirection: LPLONG     var lpEnvelope: PFFENVELOPE     var cbTypeSpecificParams: DWORD     var lpvTypeSpecificParams: UnsafePointer<()>     var dwStartDelay: DWORD } ``` |
| To | ``` struct FFEFFECT {     var dwSize: DWORD     var dwFlags: DWORD     var dwDuration: DWORD     var dwSamplePeriod: DWORD     var dwGain: DWORD     var dwTriggerButton: DWORD     var dwTriggerRepeatInterval: DWORD     var cAxes: DWORD     var rgdwAxes: LPDWORD     var rglDirection: LPLONG     var lpEnvelope: PFFENVELOPE     var cbTypeSpecificParams: DWORD     var lpvTypeSpecificParams: UnsafeMutablePointer<Void>     var dwStartDelay: DWORD     init()     init(dwSize dwSize: DWORD, dwFlags dwFlags: DWORD, dwDuration dwDuration: DWORD, dwSamplePeriod dwSamplePeriod: DWORD, dwGain dwGain: DWORD, dwTriggerButton dwTriggerButton: DWORD, dwTriggerRepeatInterval dwTriggerRepeatInterval: DWORD, cAxes cAxes: DWORD, rgdwAxes rgdwAxes: LPDWORD, rglDirection rglDirection: LPLONG, lpEnvelope lpEnvelope: PFFENVELOPE, cbTypeSpecificParams cbTypeSpecificParams: DWORD, lpvTypeSpecificParams lpvTypeSpecificParams: UnsafeMutablePointer<Void>, dwStartDelay dwStartDelay: DWORD) } ``` |

Modified FFEFFECT.lpvTypeSpecificParams

|  | Declaration |
| --- | --- |
| From | ``` var lpvTypeSpecificParams: UnsafePointer<()> ``` |
| To | ``` var lpvTypeSpecificParams: UnsafeMutablePointer<Void> ``` |

Modified FFEFFESCAPE [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FFEFFESCAPE {     var dwSize: DWORD     var dwCommand: DWORD     var lpvInBuffer: UnsafePointer<()>     var cbInBuffer: DWORD     var lpvOutBuffer: UnsafePointer<()>     var cbOutBuffer: DWORD } ``` |
| To | ``` struct FFEFFESCAPE {     var dwSize: DWORD     var dwCommand: DWORD     var lpvInBuffer: UnsafeMutablePointer<Void>     var cbInBuffer: DWORD     var lpvOutBuffer: UnsafeMutablePointer<Void>     var cbOutBuffer: DWORD     init()     init(dwSize dwSize: DWORD, dwCommand dwCommand: DWORD, lpvInBuffer lpvInBuffer: UnsafeMutablePointer<Void>, cbInBuffer cbInBuffer: DWORD, lpvOutBuffer lpvOutBuffer: UnsafeMutablePointer<Void>, cbOutBuffer cbOutBuffer: DWORD) } ``` |

Modified FFEFFESCAPE.lpvInBuffer

|  | Declaration |
| --- | --- |
| From | ``` var lpvInBuffer: UnsafePointer<()> ``` |
| To | ``` var lpvInBuffer: UnsafeMutablePointer<Void> ``` |

Modified FFEFFESCAPE.lpvOutBuffer

|  | Declaration |
| --- | --- |
| From | ``` var lpvOutBuffer: UnsafePointer<()> ``` |
| To | ``` var lpvOutBuffer: UnsafeMutablePointer<Void> ``` |

Modified FFENVELOPE [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FFENVELOPE {     var dwSize: DWORD     var dwAttackLevel: DWORD     var dwAttackTime: DWORD     var dwFadeLevel: DWORD     var dwFadeTime: DWORD } ``` |
| To | ``` struct FFENVELOPE {     var dwSize: DWORD     var dwAttackLevel: DWORD     var dwAttackTime: DWORD     var dwFadeLevel: DWORD     var dwFadeTime: DWORD     init()     init(dwSize dwSize: DWORD, dwAttackLevel dwAttackLevel: DWORD, dwAttackTime dwAttackTime: DWORD, dwFadeLevel dwFadeLevel: DWORD, dwFadeTime dwFadeTime: DWORD) } ``` |

Modified FFPERIODIC [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FFPERIODIC {     var dwMagnitude: DWORD     var lOffset: LONG     var dwPhase: DWORD     var dwPeriod: DWORD } ``` |
| To | ``` struct FFPERIODIC {     var dwMagnitude: DWORD     var lOffset: LONG     var dwPhase: DWORD     var dwPeriod: DWORD     init()     init(dwMagnitude dwMagnitude: DWORD, lOffset lOffset: LONG, dwPhase dwPhase: DWORD, dwPeriod dwPeriod: DWORD) } ``` |

Modified FFRAMPFORCE [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FFRAMPFORCE {     var lStart: LONG     var lEnd: LONG } ``` |
| To | ``` struct FFRAMPFORCE {     var lStart: LONG     var lEnd: LONG     init()     init(lStart lStart: LONG, lEnd lEnd: LONG) } ``` |

Modified FFCreateDevice(io_service_t, UnsafeMutablePointer<FFDeviceObjectReference>) -> HRESULT

|  | Declaration |
| --- | --- |
| From | ``` func FFCreateDevice(_ hidDevice: io_service_t, _ pDeviceReference: UnsafePointer<FFDeviceObjectReference>) -> HRESULT ``` |
| To | ``` func FFCreateDevice(_ hidDevice: io_service_t, _ pDeviceReference: UnsafeMutablePointer<FFDeviceObjectReference>) -> HRESULT ``` |

Modified FFDeviceCreateEffect(FFDeviceObjectReference, CFUUID!, UnsafeMutablePointer<FFEFFECT>, UnsafeMutablePointer<FFEffectObjectReference>) -> HRESULT

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceCreateEffect(_ deviceReference: FFDeviceObjectReference, _ uuidRef: CFUUID!, _ pEffectDefinition: UnsafePointer<FFEFFECT>, _ pEffectReference: UnsafePointer<FFEffectObjectReference>) -> HRESULT ``` |
| To | ``` func FFDeviceCreateEffect(_ deviceReference: FFDeviceObjectReference, _ uuidRef: CFUUID!, _ pEffectDefinition: UnsafeMutablePointer<FFEFFECT>, _ pEffectReference: UnsafeMutablePointer<FFEffectObjectReference>) -> HRESULT ``` |

Modified FFDeviceEscape(FFDeviceObjectReference, UnsafeMutablePointer<FFEFFESCAPE>) -> HRESULT

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceEscape(_ deviceReference: FFDeviceObjectReference, _ pFFEffectEscape: UnsafePointer<FFEFFESCAPE>) -> HRESULT ``` |
| To | ``` func FFDeviceEscape(_ deviceReference: FFDeviceObjectReference, _ pFFEffectEscape: UnsafeMutablePointer<FFEFFESCAPE>) -> HRESULT ``` |

Modified FFDeviceGetForceFeedbackCapabilities(FFDeviceObjectReference, UnsafeMutablePointer<FFCAPABILITIES>) -> HRESULT

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceGetForceFeedbackCapabilities(_ deviceReference: FFDeviceObjectReference, _ pFFCapabilities: UnsafePointer<FFCAPABILITIES>) -> HRESULT ``` |
| To | ``` func FFDeviceGetForceFeedbackCapabilities(_ deviceReference: FFDeviceObjectReference, _ pFFCapabilities: UnsafeMutablePointer<FFCAPABILITIES>) -> HRESULT ``` |

Modified FFDeviceGetForceFeedbackProperty(FFDeviceObjectReference, FFProperty, UnsafeMutablePointer<Void>, IOByteCount) -> HRESULT

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceGetForceFeedbackProperty(_ deviceReference: FFDeviceObjectReference, _ property: FFProperty, _ pValue: UnsafePointer<()>, _ valueSize: IOByteCount) -> HRESULT ``` |
| To | ``` func FFDeviceGetForceFeedbackProperty(_ deviceReference: FFDeviceObjectReference, _ property: FFProperty, _ pValue: UnsafeMutablePointer<Void>, _ valueSize: IOByteCount) -> HRESULT ``` |

Modified FFDeviceGetForceFeedbackState(FFDeviceObjectReference, UnsafeMutablePointer<FFState>) -> HRESULT

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceGetForceFeedbackState(_ deviceReference: FFDeviceObjectReference, _ pFFState: UnsafePointer<FFState>) -> HRESULT ``` |
| To | ``` func FFDeviceGetForceFeedbackState(_ deviceReference: FFDeviceObjectReference, _ pFFState: UnsafeMutablePointer<FFState>) -> HRESULT ``` |

Modified FFDeviceObjectReference

|  | Declaration |
| --- | --- |
| From | ``` typealias FFDeviceObjectReference = UnsafePointer<__FFDHIDDEN> ``` |
| To | ``` typealias FFDeviceObjectReference = UnsafeMutablePointer<__FFDHIDDEN> ``` |

Modified FFDeviceSetCooperativeLevel(FFDeviceObjectReference, UnsafeMutablePointer<Void>, FFCooperativeLevelFlag) -> HRESULT

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceSetCooperativeLevel(_ deviceReference: FFDeviceObjectReference, _ taskIdentifier: UnsafePointer<()>, _ flags: FFCooperativeLevelFlag) -> HRESULT ``` |
| To | ``` func FFDeviceSetCooperativeLevel(_ deviceReference: FFDeviceObjectReference, _ taskIdentifier: UnsafeMutablePointer<Void>, _ flags: FFCooperativeLevelFlag) -> HRESULT ``` |

Modified FFDeviceSetForceFeedbackProperty(FFDeviceObjectReference, FFProperty, UnsafeMutablePointer<Void>) -> HRESULT

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceSetForceFeedbackProperty(_ deviceReference: FFDeviceObjectReference, _ property: FFProperty, _ pValue: UnsafePointer<()>) -> HRESULT ``` |
| To | ``` func FFDeviceSetForceFeedbackProperty(_ deviceReference: FFDeviceObjectReference, _ property: FFProperty, _ pValue: UnsafeMutablePointer<Void>) -> HRESULT ``` |

Modified FFEffectEscape(FFEffectObjectReference, UnsafeMutablePointer<FFEFFESCAPE>) -> HRESULT

|  | Declaration |
| --- | --- |
| From | ``` func FFEffectEscape(_ effectReference: FFEffectObjectReference, _ pFFEffectEscape: UnsafePointer<FFEFFESCAPE>) -> HRESULT ``` |
| To | ``` func FFEffectEscape(_ effectReference: FFEffectObjectReference, _ pFFEffectEscape: UnsafeMutablePointer<FFEFFESCAPE>) -> HRESULT ``` |

Modified FFEffectGetEffectStatus(FFEffectObjectReference, UnsafeMutablePointer<FFEffectStatusFlag>) -> HRESULT

|  | Declaration |
| --- | --- |
| From | ``` func FFEffectGetEffectStatus(_ effectReference: FFEffectObjectReference, _ pFlags: UnsafePointer<FFEffectStatusFlag>) -> HRESULT ``` |
| To | ``` func FFEffectGetEffectStatus(_ effectReference: FFEffectObjectReference, _ pFlags: UnsafeMutablePointer<FFEffectStatusFlag>) -> HRESULT ``` |

Modified FFEffectGetParameters(FFEffectObjectReference, UnsafeMutablePointer<FFEFFECT>, FFEffectParameterFlag) -> HRESULT

|  | Declaration |
| --- | --- |
| From | ``` func FFEffectGetParameters(_ effectReference: FFEffectObjectReference, _ pFFEffect: UnsafePointer<FFEFFECT>, _ flags: FFEffectParameterFlag) -> HRESULT ``` |
| To | ``` func FFEffectGetParameters(_ effectReference: FFEffectObjectReference, _ pFFEffect: UnsafeMutablePointer<FFEFFECT>, _ flags: FFEffectParameterFlag) -> HRESULT ``` |

Modified FFEffectObjectReference

|  | Declaration |
| --- | --- |
| From | ``` typealias FFEffectObjectReference = UnsafePointer<__FFEHIDDEN> ``` |
| To | ``` typealias FFEffectObjectReference = UnsafeMutablePointer<__FFEHIDDEN> ``` |

Modified FFEffectSetParameters(FFEffectObjectReference, UnsafeMutablePointer<FFEFFECT>, FFEffectParameterFlag) -> HRESULT

|  | Declaration |
| --- | --- |
| From | ``` func FFEffectSetParameters(_ effectReference: FFEffectObjectReference, _ pFFEffect: UnsafePointer<FFEFFECT>, _ flags: FFEffectParameterFlag) -> HRESULT ``` |
| To | ``` func FFEffectSetParameters(_ effectReference: FFEffectObjectReference, _ pFFEffect: UnsafeMutablePointer<FFEFFECT>, _ flags: FFEffectParameterFlag) -> HRESULT ``` |

Modified LPDWORD

|  | Declaration |
| --- | --- |
| From | ``` typealias LPDWORD = UnsafePointer<DWORD> ``` |
| To | ``` typealias LPDWORD = UnsafeMutablePointer<DWORD> ``` |

Modified LPLONG

|  | Declaration |
| --- | --- |
| From | ``` typealias LPLONG = UnsafePointer<LONG> ``` |
| To | ``` typealias LPLONG = UnsafeMutablePointer<LONG> ``` |

Modified PFFCAPABILITIES

|  | Declaration |
| --- | --- |
| From | ``` typealias PFFCAPABILITIES = UnsafePointer<FFCAPABILITIES> ``` |
| To | ``` typealias PFFCAPABILITIES = UnsafeMutablePointer<FFCAPABILITIES> ``` |

Modified PFFCONDITION

|  | Declaration |
| --- | --- |
| From | ``` typealias PFFCONDITION = UnsafePointer<FFCONDITION> ``` |
| To | ``` typealias PFFCONDITION = UnsafeMutablePointer<FFCONDITION> ``` |

Modified PFFCONSTANTFORCE

|  | Declaration |
| --- | --- |
| From | ``` typealias PFFCONSTANTFORCE = UnsafePointer<FFCONSTANTFORCE> ``` |
| To | ``` typealias PFFCONSTANTFORCE = UnsafeMutablePointer<FFCONSTANTFORCE> ``` |

Modified PFFCUSTOMFORCE

|  | Declaration |
| --- | --- |
| From | ``` typealias PFFCUSTOMFORCE = UnsafePointer<FFCUSTOMFORCE> ``` |
| To | ``` typealias PFFCUSTOMFORCE = UnsafeMutablePointer<FFCUSTOMFORCE> ``` |

Modified PFFEFFECT

|  | Declaration |
| --- | --- |
| From | ``` typealias PFFEFFECT = UnsafePointer<FFEFFECT> ``` |
| To | ``` typealias PFFEFFECT = UnsafeMutablePointer<FFEFFECT> ``` |

Modified PFFEFFESCAPE

|  | Declaration |
| --- | --- |
| From | ``` typealias PFFEFFESCAPE = UnsafePointer<FFEFFESCAPE> ``` |
| To | ``` typealias PFFEFFESCAPE = UnsafeMutablePointer<FFEFFESCAPE> ``` |

Modified PFFENVELOPE

|  | Declaration |
| --- | --- |
| From | ``` typealias PFFENVELOPE = UnsafePointer<FFENVELOPE> ``` |
| To | ``` typealias PFFENVELOPE = UnsafeMutablePointer<FFENVELOPE> ``` |

Modified PFFPERIODIC

|  | Declaration |
| --- | --- |
| From | ``` typealias PFFPERIODIC = UnsafePointer<FFPERIODIC> ``` |
| To | ``` typealias PFFPERIODIC = UnsafeMutablePointer<FFPERIODIC> ``` |

Modified PFFRAMPFORCE

|  | Declaration |
| --- | --- |
| From | ``` typealias PFFRAMPFORCE = UnsafePointer<FFRAMPFORCE> ``` |
| To | ``` typealias PFFRAMPFORCE = UnsafeMutablePointer<FFRAMPFORCE> ``` |

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
