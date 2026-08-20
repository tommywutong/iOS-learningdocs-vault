---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/ForceFeedback.html
archived_at: '2026-07-18T02:51:17.638431Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# ForceFeedback Changes for Swift

### ForceFeedback

Removed [FFCUSTOMFORCE.init(cChannels: DWORD, dwSamplePeriod: DWORD, cSamples: DWORD, rglForceData: LPLONG)](https://developer.apple.com/documentation/forcefeedback/ffcustomforce/1403978-init)Removed [FFEFFECT.init(dwSize: DWORD, dwFlags: DWORD, dwDuration: DWORD, dwSamplePeriod: DWORD, dwGain: DWORD, dwTriggerButton: DWORD, dwTriggerRepeatInterval: DWORD, cAxes: DWORD, rgdwAxes: LPDWORD, rglDirection: LPLONG, lpEnvelope: PFFENVELOPE, cbTypeSpecificParams: DWORD, lpvTypeSpecificParams: UnsafeMutablePointer<Void>, dwStartDelay: DWORD)](https://developer.apple.com/documentation/forcefeedback/ffeffect/1403817-init)Removed [FFEFFESCAPE.init(dwSize: DWORD, dwCommand: DWORD, lpvInBuffer: UnsafeMutablePointer<Void>, cbInBuffer: DWORD, lpvOutBuffer: UnsafeMutablePointer<Void>, cbOutBuffer: DWORD)](https://developer.apple.com/documentation/forcefeedback/ffeffescape/1403887-init)Added [FFCUSTOMFORCE.init(cChannels: DWORD, dwSamplePeriod: DWORD, cSamples: DWORD, rglForceData: LPLONG!)](https://developer.apple.com/documentation/forcefeedback/ffcustomforce/1403978-init)Added [FFEFFECT.init(dwSize: DWORD, dwFlags: DWORD, dwDuration: DWORD, dwSamplePeriod: DWORD, dwGain: DWORD, dwTriggerButton: DWORD, dwTriggerRepeatInterval: DWORD, cAxes: DWORD, rgdwAxes: LPDWORD!, rglDirection: LPLONG!, lpEnvelope: PFFENVELOPE!, cbTypeSpecificParams: DWORD, lpvTypeSpecificParams: UnsafeMutableRawPointer!, dwStartDelay: DWORD)](https://developer.apple.com/documentation/forcefeedback/ffeffect/1403817-init)Added [FFEFFESCAPE.init(dwSize: DWORD, dwCommand: DWORD, lpvInBuffer: UnsafeMutableRawPointer!, cbInBuffer: DWORD, lpvOutBuffer: UnsafeMutableRawPointer!, cbOutBuffer: DWORD)](https://developer.apple.com/documentation/forcefeedback/ffeffescape/1403887-init)Added [FF_DOWNLOADSKIPPED](https://developer.apple.com/documentation/forcefeedback/ff_downloadskipped)Added [FF_EFFECTRESTARTED](https://developer.apple.com/documentation/forcefeedback/ff_effectrestarted)Added [FF_FALSE](https://developer.apple.com/documentation/forcefeedback/ff_false)Added [FF_OK](https://developer.apple.com/documentation/forcefeedback/ff_ok)Added [FF_TRUNCATED](https://developer.apple.com/documentation/forcefeedback/ff_truncated)Added [FF_TRUNCATEDANDRESTARTED](https://developer.apple.com/documentation/forcefeedback/ff_truncatedandrestarted)Added [FFERR_GENERIC](https://developer.apple.com/documentation/forcefeedback/fferr_generic)Added [FFERR_INVALIDPARAM](https://developer.apple.com/documentation/forcefeedback/fferr_invalidparam)Added [FFERR_NOINTERFACE](https://developer.apple.com/documentation/forcefeedback/fferr_nointerface)Added [FFERR_OUTOFMEMORY](https://developer.apple.com/documentation/forcefeedback/fferr_outofmemory)Added [FFERR_UNSUPPORTED](https://developer.apple.com/documentation/forcefeedback/fferr_unsupported)Modified [FFCUSTOMFORCE [struct]](https://developer.apple.com/documentation/forcefeedback/ffcustomforce)

|  | Declaration |
| --- | --- |
| From | ``` struct FFCUSTOMFORCE {     var cChannels: DWORD     var dwSamplePeriod: DWORD     var cSamples: DWORD     var rglForceData: LPLONG     init()     init(cChannels cChannels: DWORD, dwSamplePeriod dwSamplePeriod: DWORD, cSamples cSamples: DWORD, rglForceData rglForceData: LPLONG) } ``` |
| To | ``` struct FFCUSTOMFORCE {     var cChannels: DWORD     var dwSamplePeriod: DWORD     var cSamples: DWORD     var rglForceData: LPLONG!     init()     init(cChannels cChannels: DWORD, dwSamplePeriod dwSamplePeriod: DWORD, cSamples cSamples: DWORD, rglForceData rglForceData: LPLONG!) } ``` |

Modified [FFCUSTOMFORCE.rglForceData](https://developer.apple.com/documentation/forcefeedback/ffcustomforce/1403968-rglforcedata)

|  | Declaration |
| --- | --- |
| From | ``` var rglForceData: LPLONG ``` |
| To | ``` var rglForceData: LPLONG! ``` |

Modified [FFEFFECT [struct]](https://developer.apple.com/documentation/forcefeedback/ffeffect)

|  | Declaration |
| --- | --- |
| From | ``` struct FFEFFECT {     var dwSize: DWORD     var dwFlags: DWORD     var dwDuration: DWORD     var dwSamplePeriod: DWORD     var dwGain: DWORD     var dwTriggerButton: DWORD     var dwTriggerRepeatInterval: DWORD     var cAxes: DWORD     var rgdwAxes: LPDWORD     var rglDirection: LPLONG     var lpEnvelope: PFFENVELOPE     var cbTypeSpecificParams: DWORD     var lpvTypeSpecificParams: UnsafeMutablePointer<Void>     var dwStartDelay: DWORD     init()     init(dwSize dwSize: DWORD, dwFlags dwFlags: DWORD, dwDuration dwDuration: DWORD, dwSamplePeriod dwSamplePeriod: DWORD, dwGain dwGain: DWORD, dwTriggerButton dwTriggerButton: DWORD, dwTriggerRepeatInterval dwTriggerRepeatInterval: DWORD, cAxes cAxes: DWORD, rgdwAxes rgdwAxes: LPDWORD, rglDirection rglDirection: LPLONG, lpEnvelope lpEnvelope: PFFENVELOPE, cbTypeSpecificParams cbTypeSpecificParams: DWORD, lpvTypeSpecificParams lpvTypeSpecificParams: UnsafeMutablePointer<Void>, dwStartDelay dwStartDelay: DWORD) } ``` |
| To | ``` struct FFEFFECT {     var dwSize: DWORD     var dwFlags: DWORD     var dwDuration: DWORD     var dwSamplePeriod: DWORD     var dwGain: DWORD     var dwTriggerButton: DWORD     var dwTriggerRepeatInterval: DWORD     var cAxes: DWORD     var rgdwAxes: LPDWORD!     var rglDirection: LPLONG!     var lpEnvelope: PFFENVELOPE!     var cbTypeSpecificParams: DWORD     var lpvTypeSpecificParams: UnsafeMutableRawPointer!     var dwStartDelay: DWORD     init()     init(dwSize dwSize: DWORD, dwFlags dwFlags: DWORD, dwDuration dwDuration: DWORD, dwSamplePeriod dwSamplePeriod: DWORD, dwGain dwGain: DWORD, dwTriggerButton dwTriggerButton: DWORD, dwTriggerRepeatInterval dwTriggerRepeatInterval: DWORD, cAxes cAxes: DWORD, rgdwAxes rgdwAxes: LPDWORD!, rglDirection rglDirection: LPLONG!, lpEnvelope lpEnvelope: PFFENVELOPE!, cbTypeSpecificParams cbTypeSpecificParams: DWORD, lpvTypeSpecificParams lpvTypeSpecificParams: UnsafeMutableRawPointer!, dwStartDelay dwStartDelay: DWORD) } ``` |

Modified [FFEFFECT.lpEnvelope](https://developer.apple.com/documentation/forcefeedback/ffeffect/1403805-lpenvelope)

|  | Declaration |
| --- | --- |
| From | ``` var lpEnvelope: PFFENVELOPE ``` |
| To | ``` var lpEnvelope: PFFENVELOPE! ``` |

Modified [FFEFFECT.lpvTypeSpecificParams](https://developer.apple.com/documentation/forcefeedback/ffeffect/1403964-lpvtypespecificparams)

|  | Declaration |
| --- | --- |
| From | ``` var lpvTypeSpecificParams: UnsafeMutablePointer<Void> ``` |
| To | ``` var lpvTypeSpecificParams: UnsafeMutableRawPointer! ``` |

Modified [FFEFFECT.rgdwAxes](https://developer.apple.com/documentation/forcefeedback/ffeffect/1403691-rgdwaxes)

|  | Declaration |
| --- | --- |
| From | ``` var rgdwAxes: LPDWORD ``` |
| To | ``` var rgdwAxes: LPDWORD! ``` |

Modified [FFEFFECT.rglDirection](https://developer.apple.com/documentation/forcefeedback/ffeffect/1403765-rgldirection)

|  | Declaration |
| --- | --- |
| From | ``` var rglDirection: LPLONG ``` |
| To | ``` var rglDirection: LPLONG! ``` |

Modified [FFEFFESCAPE [struct]](https://developer.apple.com/documentation/forcefeedback/ffeffescape)

|  | Declaration |
| --- | --- |
| From | ``` struct FFEFFESCAPE {     var dwSize: DWORD     var dwCommand: DWORD     var lpvInBuffer: UnsafeMutablePointer<Void>     var cbInBuffer: DWORD     var lpvOutBuffer: UnsafeMutablePointer<Void>     var cbOutBuffer: DWORD     init()     init(dwSize dwSize: DWORD, dwCommand dwCommand: DWORD, lpvInBuffer lpvInBuffer: UnsafeMutablePointer<Void>, cbInBuffer cbInBuffer: DWORD, lpvOutBuffer lpvOutBuffer: UnsafeMutablePointer<Void>, cbOutBuffer cbOutBuffer: DWORD) } ``` |
| To | ``` struct FFEFFESCAPE {     var dwSize: DWORD     var dwCommand: DWORD     var lpvInBuffer: UnsafeMutableRawPointer!     var cbInBuffer: DWORD     var lpvOutBuffer: UnsafeMutableRawPointer!     var cbOutBuffer: DWORD     init()     init(dwSize dwSize: DWORD, dwCommand dwCommand: DWORD, lpvInBuffer lpvInBuffer: UnsafeMutableRawPointer!, cbInBuffer cbInBuffer: DWORD, lpvOutBuffer lpvOutBuffer: UnsafeMutableRawPointer!, cbOutBuffer cbOutBuffer: DWORD) } ``` |

Modified [FFEFFESCAPE.lpvInBuffer](https://developer.apple.com/documentation/forcefeedback/ffeffescape/1403781-lpvinbuffer)

|  | Declaration |
| --- | --- |
| From | ``` var lpvInBuffer: UnsafeMutablePointer<Void> ``` |
| To | ``` var lpvInBuffer: UnsafeMutableRawPointer! ``` |

Modified [FFEFFESCAPE.lpvOutBuffer](https://developer.apple.com/documentation/forcefeedback/ffeffescape/1403803-lpvoutbuffer)

|  | Declaration |
| --- | --- |
| From | ``` var lpvOutBuffer: UnsafeMutablePointer<Void> ``` |
| To | ``` var lpvOutBuffer: UnsafeMutableRawPointer! ``` |

Modified [FFCreateDevice(_: io_service_t, _: UnsafeMutablePointer<FFDeviceObjectReference?>!) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403914-ffcreatedevice)

|  | Declaration |
| --- | --- |
| From | ``` func FFCreateDevice(_ hidDevice: io_service_t, _ pDeviceReference: UnsafeMutablePointer<FFDeviceObjectReference>) -> HRESULT ``` |
| To | ``` func FFCreateDevice(_ hidDevice: io_service_t, _ pDeviceReference: UnsafeMutablePointer<FFDeviceObjectReference?>!) -> HRESULT ``` |

Modified [FFDeviceCreateEffect(_: FFDeviceObjectReference!, _: CFUUID!, _: UnsafeMutablePointer<FFEFFECT>!, _: UnsafeMutablePointer<FFEffectObjectReference?>!) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403757-ffdevicecreateeffect)

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceCreateEffect(_ deviceReference: FFDeviceObjectReference, _ uuidRef: CFUUID!, _ pEffectDefinition: UnsafeMutablePointer<FFEFFECT>, _ pEffectReference: UnsafeMutablePointer<FFEffectObjectReference>) -> HRESULT ``` |
| To | ``` func FFDeviceCreateEffect(_ deviceReference: FFDeviceObjectReference!, _ uuidRef: CFUUID!, _ pEffectDefinition: UnsafeMutablePointer<FFEFFECT>!, _ pEffectReference: UnsafeMutablePointer<FFEffectObjectReference?>!) -> HRESULT ``` |

Modified [FFDeviceEscape(_: FFDeviceObjectReference!, _: UnsafeMutablePointer<FFEFFESCAPE>!) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403853-ffdeviceescape)

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceEscape(_ deviceReference: FFDeviceObjectReference, _ pFFEffectEscape: UnsafeMutablePointer<FFEFFESCAPE>) -> HRESULT ``` |
| To | ``` func FFDeviceEscape(_ deviceReference: FFDeviceObjectReference!, _ pFFEffectEscape: UnsafeMutablePointer<FFEFFESCAPE>!) -> HRESULT ``` |

Modified [FFDeviceGetForceFeedbackCapabilities(_: FFDeviceObjectReference!, _: UnsafeMutablePointer<FFCAPABILITIES>!) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403831-ffdevicegetforcefeedbackcapabili)

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceGetForceFeedbackCapabilities(_ deviceReference: FFDeviceObjectReference, _ pFFCapabilities: UnsafeMutablePointer<FFCAPABILITIES>) -> HRESULT ``` |
| To | ``` func FFDeviceGetForceFeedbackCapabilities(_ deviceReference: FFDeviceObjectReference!, _ pFFCapabilities: UnsafeMutablePointer<FFCAPABILITIES>!) -> HRESULT ``` |

Modified [FFDeviceGetForceFeedbackProperty(_: FFDeviceObjectReference!, _: FFProperty, _: UnsafeMutableRawPointer!, _: IOByteCount) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403881-ffdevicegetforcefeedbackproperty)

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceGetForceFeedbackProperty(_ deviceReference: FFDeviceObjectReference, _ property: FFProperty, _ pValue: UnsafeMutablePointer<Void>, _ valueSize: IOByteCount) -> HRESULT ``` |
| To | ``` func FFDeviceGetForceFeedbackProperty(_ deviceReference: FFDeviceObjectReference!, _ property: FFProperty, _ pValue: UnsafeMutableRawPointer!, _ valueSize: IOByteCount) -> HRESULT ``` |

Modified [FFDeviceGetForceFeedbackState(_: FFDeviceObjectReference!, _: UnsafeMutablePointer<FFState>!) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403950-ffdevicegetforcefeedbackstate)

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceGetForceFeedbackState(_ deviceReference: FFDeviceObjectReference, _ pFFState: UnsafeMutablePointer<FFState>) -> HRESULT ``` |
| To | ``` func FFDeviceGetForceFeedbackState(_ deviceReference: FFDeviceObjectReference!, _ pFFState: UnsafeMutablePointer<FFState>!) -> HRESULT ``` |

Modified [FFDeviceReleaseEffect(_: FFDeviceObjectReference!, _: FFEffectObjectReference!) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403707-ffdevicereleaseeffect)

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceReleaseEffect(_ deviceReference: FFDeviceObjectReference, _ effectReference: FFEffectObjectReference) -> HRESULT ``` |
| To | ``` func FFDeviceReleaseEffect(_ deviceReference: FFDeviceObjectReference!, _ effectReference: FFEffectObjectReference!) -> HRESULT ``` |

Modified [FFDeviceSendForceFeedbackCommand(_: FFDeviceObjectReference!, _: FFCommandFlag) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403731-ffdevicesendforcefeedbackcommand)

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceSendForceFeedbackCommand(_ deviceReference: FFDeviceObjectReference, _ flags: FFCommandFlag) -> HRESULT ``` |
| To | ``` func FFDeviceSendForceFeedbackCommand(_ deviceReference: FFDeviceObjectReference!, _ flags: FFCommandFlag) -> HRESULT ``` |

Modified [FFDeviceSetCooperativeLevel(_: FFDeviceObjectReference!, _: UnsafeMutableRawPointer!, _: FFCooperativeLevelFlag) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403883-ffdevicesetcooperativelevel)

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceSetCooperativeLevel(_ deviceReference: FFDeviceObjectReference, _ taskIdentifier: UnsafeMutablePointer<Void>, _ flags: FFCooperativeLevelFlag) -> HRESULT ``` |
| To | ``` func FFDeviceSetCooperativeLevel(_ deviceReference: FFDeviceObjectReference!, _ taskIdentifier: UnsafeMutableRawPointer!, _ flags: FFCooperativeLevelFlag) -> HRESULT ``` |

Modified [FFDeviceSetForceFeedbackProperty(_: FFDeviceObjectReference!, _: FFProperty, _: UnsafeMutableRawPointer!) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403658-ffdevicesetforcefeedbackproperty)

|  | Declaration |
| --- | --- |
| From | ``` func FFDeviceSetForceFeedbackProperty(_ deviceReference: FFDeviceObjectReference, _ property: FFProperty, _ pValue: UnsafeMutablePointer<Void>) -> HRESULT ``` |
| To | ``` func FFDeviceSetForceFeedbackProperty(_ deviceReference: FFDeviceObjectReference!, _ property: FFProperty, _ pValue: UnsafeMutableRawPointer!) -> HRESULT ``` |

Modified [FFEffectDownload(_: FFEffectObjectReference!) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403791-ffeffectdownload)

|  | Declaration |
| --- | --- |
| From | ``` func FFEffectDownload(_ effectReference: FFEffectObjectReference) -> HRESULT ``` |
| To | ``` func FFEffectDownload(_ effectReference: FFEffectObjectReference!) -> HRESULT ``` |

Modified [FFEffectEscape(_: FFEffectObjectReference!, _: UnsafeMutablePointer<FFEFFESCAPE>!) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403976-ffeffectescape)

|  | Declaration |
| --- | --- |
| From | ``` func FFEffectEscape(_ effectReference: FFEffectObjectReference, _ pFFEffectEscape: UnsafeMutablePointer<FFEFFESCAPE>) -> HRESULT ``` |
| To | ``` func FFEffectEscape(_ effectReference: FFEffectObjectReference!, _ pFFEffectEscape: UnsafeMutablePointer<FFEFFESCAPE>!) -> HRESULT ``` |

Modified [FFEffectGetEffectStatus(_: FFEffectObjectReference!, _: UnsafeMutablePointer<FFEffectStatusFlag>!) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403785-ffeffectgeteffectstatus)

|  | Declaration |
| --- | --- |
| From | ``` func FFEffectGetEffectStatus(_ effectReference: FFEffectObjectReference, _ pFlags: UnsafeMutablePointer<FFEffectStatusFlag>) -> HRESULT ``` |
| To | ``` func FFEffectGetEffectStatus(_ effectReference: FFEffectObjectReference!, _ pFlags: UnsafeMutablePointer<FFEffectStatusFlag>!) -> HRESULT ``` |

Modified [FFEffectGetParameters(_: FFEffectObjectReference!, _: UnsafeMutablePointer<FFEFFECT>!, _: FFEffectParameterFlag) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403602-ffeffectgetparameters)

|  | Declaration |
| --- | --- |
| From | ``` func FFEffectGetParameters(_ effectReference: FFEffectObjectReference, _ pFFEffect: UnsafeMutablePointer<FFEFFECT>, _ flags: FFEffectParameterFlag) -> HRESULT ``` |
| To | ``` func FFEffectGetParameters(_ effectReference: FFEffectObjectReference!, _ pFFEffect: UnsafeMutablePointer<FFEFFECT>!, _ flags: FFEffectParameterFlag) -> HRESULT ``` |

Modified [FFEffectSetParameters(_: FFEffectObjectReference!, _: UnsafeMutablePointer<FFEFFECT>!, _: FFEffectParameterFlag) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403584-ffeffectsetparameters)

|  | Declaration |
| --- | --- |
| From | ``` func FFEffectSetParameters(_ effectReference: FFEffectObjectReference, _ pFFEffect: UnsafeMutablePointer<FFEFFECT>, _ flags: FFEffectParameterFlag) -> HRESULT ``` |
| To | ``` func FFEffectSetParameters(_ effectReference: FFEffectObjectReference!, _ pFFEffect: UnsafeMutablePointer<FFEFFECT>!, _ flags: FFEffectParameterFlag) -> HRESULT ``` |

Modified [FFEffectStart(_: FFEffectObjectReference!, _: UInt32, _: FFEffectStartFlag) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403875-ffeffectstart)

|  | Declaration |
| --- | --- |
| From | ``` func FFEffectStart(_ effectReference: FFEffectObjectReference, _ iterations: UInt32, _ flags: FFEffectStartFlag) -> HRESULT ``` |
| To | ``` func FFEffectStart(_ effectReference: FFEffectObjectReference!, _ iterations: UInt32, _ flags: FFEffectStartFlag) -> HRESULT ``` |

Modified [FFEffectStop(_: FFEffectObjectReference!) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403869-ffeffectstop)

|  | Declaration |
| --- | --- |
| From | ``` func FFEffectStop(_ effectReference: FFEffectObjectReference) -> HRESULT ``` |
| To | ``` func FFEffectStop(_ effectReference: FFEffectObjectReference!) -> HRESULT ``` |

Modified [FFEffectUnload(_: FFEffectObjectReference!) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403618-ffeffectunload)

|  | Declaration |
| --- | --- |
| From | ``` func FFEffectUnload(_ effectReference: FFEffectObjectReference) -> HRESULT ``` |
| To | ``` func FFEffectUnload(_ effectReference: FFEffectObjectReference!) -> HRESULT ``` |

Modified [FFReleaseDevice(_: FFDeviceObjectReference!) -> HRESULT](https://developer.apple.com/documentation/forcefeedback/1403715-ffreleasedevice)

|  | Declaration |
| --- | --- |
| From | ``` func FFReleaseDevice(_ deviceReference: FFDeviceObjectReference) -> HRESULT ``` |
| To | ``` func FFReleaseDevice(_ deviceReference: FFDeviceObjectReference!) -> HRESULT ``` |

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
