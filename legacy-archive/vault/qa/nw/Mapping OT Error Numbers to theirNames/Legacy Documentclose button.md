---
title: Mapping OT Error Numbers to theirNames
apple_id: DTS10001447
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-06-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw35.html
archived_at: '2026-07-18T02:29:46.086645Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW35Mapping OT Error Numbers to theirNames |

|  |  |
| --- | --- |
| ---   Q: How do I map Open Transport error numbers to their names?  A: There are two ways to do this. The first is the "OTErr" MacsBug '`dcmd`' that ships with the debugging version of OT. This '`dcmd`' allows you to quickly map an error number to a (sometimes) meaningful error name. Once you install it in your Debugger Prefs file, you can type, for example, "oterr -3271" in MacsBug and get the name for that error.  The second solution is the Open Transport Errors Decoder, included here as a public service.   |  | | --- | | ``` Name                      Number kOTNoError                     0 kOTOutOfMemoryErr          -3211 kOTNotFoundErr             -3201 kOTDuplicateFoundErr       -3216 kOTBadAddressErr           -3150 kOTBadOptionErr            -3151 kOTAccessErr               -3152 kOTBadReferenceErr         -3153 kOTNoAddressErr            -3154 kOTOutStateErr             -3155 kOTBadSequenceErr          -3156 kOTSysErrorErr             -3157 kOTLookErr                 -3158 kOTBadDataErr              -3159 kOTBufferOverflowErr       -3160 kOTFlowErr                 -3161 kOTNoDataErr               -3162 kOTNoDisconnectErr         -3163 kOTNoUDErrErr              -3164 kOTBadFlagErr              -3165 kOTNoReleaseErr            -3166 kOTNotSupportedErr         -3167 kOTStateChangeErr          -3168 kOTNoStructureTypeErr      -3169 kOTBadNameErr              -3170 kOTBadQLenErr              -3171 kOTAddressBusyErr          -3172 kOTIndOutErr               -3173 kOTProviderMismatchErr     -3174 kOTResQLenErr              -3175 kOTResAddressErr           -3176 kOTQFullErr                -3177 kOTProtocolErr             -3178 kOTBadSyncErr              -3179 kOTCanceledErr             -3180 kEPERMErr                  -3200 kENOENTErr                 -3201 kENORSRCErr                -3202 kEINTRErr                  -3203 kEIOErr                    -3204 kENXIOErr                  -3205 kEBADFErr                  -3208 kEAGAINErr                 -3210 kENOMEMErr                 -3211 kEACCESErr                 -3212 kEFAULTErr                 -3213 kEBUSYErr                  -3215 kEEXISTErr                 -3216 kENODEVErr                 -3218 kEINVALErr                 -3221 kENOTTYErr                 -3224 kEPIPEErr                  -3231 kERANGEErr                 -3233 kEWOULDBLOCKErr            -3234 kEDEADLKErr                -3234 kEALREADYErr               -3236 kENOTSOCKErr               -3237 kEDESTADDRREQErr           -3238 kEMSGSIZEErr               -3239 kEPROTOTYPEErr             -3240 kENOPROTOOPTErr            -3241 kEPROTONOSUPPORTErr        -3242 kESOCKTNOSUPPORTErr        -3243 kEOPNOTSUPPErr             -3244 kEADDRINUSEErr             -3247 kEADDRNOTAVAILErr          -3248 kENETDOWNErr               -3249 kENETUNREACHErr            -3250 kENETRESETErr              -3251 kECONNABORTEDErr           -3252 kECONNRESETErr             -3253 kENOBUFSErr                -3254 kEISCONNErr                -3255 kENOTCONNErr               -3256 kESHUTDOWNErr              -3257 kETOOMANYREFSErr           -3258 kETIMEDOUTErr              -3259 kECONNREFUSEDErr           -3260 kEHOSTDOWNErr              -3263 kEHOSTUNREACHErr           -3264 kEPROTOErr                 -3269 kETIMEErr                  -3270 kENOSRErr                  -3271 kEBADMSGErr                -3272 kECANCELErr                -3273 kENOSTRErr                 -3274 kENODATAErr                -3275 kEINPROGRESSErr            -3276 kESRCHErr                  -3277 kENOMSGErr                 -3278 kOTClientNotInittedErr     -3279 kOTPortHasDiedErr          -3280 kOTPortWasEjectedErr       -3281 kOTBadConfigurationErr     -3282 kOTConfigurationChangedErr -3283 kOTUserRequestedErr        -3284 kOTPortLostConnection      -3285 ``` | |

#### [Jun 01 1996]

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

---
