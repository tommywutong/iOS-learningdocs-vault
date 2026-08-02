---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/Carbon.html
archived_at: '2026-07-18T02:58:42.374005Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# Carbon Changes

## Carbon

Appearance.hAdded kThemeMenuItemAlignRightModified DrawThemeChasingArrows()

|  | Declaration |
| --- | --- |
| Old | OSStatus DrawThemeChasingArrows ( const Rect \*bounds, UInt32 index, ThemeDrawState state, ThemeEraseUPP eraseProc, URefCon eraseData); |
| New | OSStatus DrawThemeChasingArrows ( const Rect \*bounds, UInt32 theIndex, ThemeDrawState state, ThemeEraseUPP eraseProc, URefCon eraseData); |

CarbonEvents.hAdded kEventClassGestureAdded kEventGestureEndedAdded kEventGestureMagnifyAdded kEventGestureRotateAdded kEventGestureStartedAdded kEventGestureSwipeAdded kEventParamMagnificationAmountAdded kEventParamRotationAmountAdded kEventParamSwipeDirectionAdded kEventWindowRestoreFromDockEvents.hModified EventAvail()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified KeyTranslate()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified GetNextEvent()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified PostEvent()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified WaitNextEvent()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified IsCmdChar()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified FlushEvents()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified Button()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

IMKInputSession.hAdded -[IMKTextInput supportsProperty:]KeychainHI.hModified kcunlock()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified kcaddgenericpassword()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified KCAddInternetPasswordWithPath()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified KCCreateKeychain()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified kcaddinternetpassword()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified kcaddapplesharepassword()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified KCAddInternetPassword()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified KCUnlock()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified KCAddGenericPassword()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified kcaddinternetpasswordwithpath()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified KCAddItem()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified kccreatekeychain()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified KCAddAppleSharePassword()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified KCChangeSettings()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

OSA.hAdded OSACopyScript()PDEPluginInterface.hRemoved [-[NSObject PDEPanelsForType:withHostInfo:]](https://developer.apple.com/documentation/objectivec/nsobject/1494234-pdepanelsfortype)Removed [-[NSObject PMPrinter]](https://developer.apple.com/documentation/objectivec/nsobject/1494230-pmprinter)Removed [-[NSObject PPDOptionKeyValueDidChange:ppdChoice:]](https://developer.apple.com/documentation/objectivec/nsobject/1494202-ppdoptionkeyvaluedidchange)Removed [-[NSObject initWithBundle:]](https://developer.apple.com/documentation/objectivec/nsobject/1494220-initwithbundle)Removed -[NSObject jobTemplate]Removed [-[NSObject pageFormat]](https://developer.apple.com/documentation/objectivec/nsobject/1494209-pageformat)Removed [-[NSObject panelKind]](https://developer.apple.com/documentation/objectivec/nsobject/1494208-panelkind)Removed [-[NSObject panelName]](https://developer.apple.com/documentation/objectivec/nsobject/1494224-panelname)Removed [-[NSObject panelView]](https://developer.apple.com/documentation/objectivec/nsobject/1494214-panelview)Removed -[NSObject panelViewDidResize]Removed [-[NSObject ppdFile]](https://developer.apple.com/documentation/objectivec/nsobject/1494226-ppdfile)Removed [-[NSObject printSession]](https://developer.apple.com/documentation/objectivec/nsobject/1494218-printsession)Removed [-[NSObject printSettings]](https://developer.apple.com/documentation/objectivec/nsobject/1494206-printsettings)Removed -[NSObject printerInfoTicket]Removed [-[NSObject restoreValuesAndReturnError:]](https://developer.apple.com/documentation/objectivec/nsobject/1494216-restorevaluesandreturnerror)Removed [-[NSObject saveValuesAndReturnError:]](https://developer.apple.com/documentation/objectivec/nsobject/1494222-savevaluesandreturnerror)Removed [-[NSObject shouldHide]](https://developer.apple.com/documentation/objectivec/nsobject/1494210-shouldhide)Removed [-[NSObject summaryInfo]](https://developer.apple.com/documentation/objectivec/nsobject/1494212-summaryinfo)Removed [-[NSObject supportedPPDOptionKeys]](https://developer.apple.com/documentation/objectivec/nsobject/1494232-supportedppdoptionkeys)Removed [-[NSObject willChangePPDOptionKeyValue:ppdChoice:]](https://developer.apple.com/documentation/objectivec/nsobject/1494235-willchangeppdoptionkeyvalue)Removed [-[NSObject willShow]](https://developer.apple.com/documentation/objectivec/nsobject/1494204-willshow)Removed NSObject(PDEPanel)Removed NSObject(PDEPlugIn)Removed NSObject(PDEPlugInCallbackProtocol)PMPrinterBrowsers.hRemoved PMInterfaceAPIVersionRemoved PMInterfaceAPIVersionHdlRemoved PMInterfaceAPIVersionPtrRemoved PMInterfacePrBrowserRemoved PMInterfacePrBrowserHdlRemoved PMInterfacePrBrowserPtrRemoved PMPrBrowserAPIVersionProcPtrRemoved PMPrBrowserCallbackHdlRemoved PMPrBrowserCallbacksRemoved PMPrBrowserCallbacksPtrRemoved PMPrBrowserContextRemoved PMPrBrowserFlagsRemoved PMPrBrowserGetLookupSpecProcPtrRemoved PMPrBrowserGetSelectedPrintersProcPtrRemoved PMPrBrowserInitializeProcPtrRemoved PMPrBrowserPrologueProcPtrRemoved PMPrBrowserRefRemoved PMPrBrowserResizeProcPtrRemoved PMPrBrowserSelectionStatusProcPtrRemoved PMPrBrowserSyncProcPtrRemoved PMPrBrowserSyncRequestProcPtrRemoved PMPrBrowserTerminateProcPtrRemoved PMPrBrowserWorksetPrintersProcPtrRemoved addNow (no architecture available)Removed callbacks (no architecture available)Removed frameRect (no architecture available)Removed #def kPMInterfaceAPIVersionRemoved #def kPMInterfacePrBrowserRemoved #def kPMPrBrowserAPIVersionRemoved #def kPMPrBrowserInvalidRefRemoved #def kPMPrBrowserLookupRefKeyRemoved #def kPMPrBrowserLookupRefStrRemoved kPMPrBrowserPCAllFlagsRemoved #def kPMPrBrowserPCCreatorRemoved kPMPrBrowserPCGetTitleRemoved kPMPrBrowserPCNoFlagsRemoved kPMPrBrowserPCNoUIRemoved #def kPMPrBrowserPlugInTypeRemoved #def kPMPrBrowserSelectAddrKeyRemoved #def kPMPrBrowserSelectAddrStrRemoved #def kPMPrBrowserSelectKindKeyRemoved #def kPMPrBrowserSelectKindStrRemoved #def kPMPrBrowserSelectNameKeyRemoved #def kPMPrBrowserSelectNameStrRemoved #def kPMPrBrowserSelectRefKeyRemoved #def kPMPrBrowserSelectRefStrRemoved #def kPMPrBrowserUnknownPrinterIconTypeRemoved #def kPMPrBrowserWorksetPrinterIconTypeRemoved lookupSpec (no architecture available)Removed maxH (no architecture available)Removed maxV (no architecture available)Removed minH (no architecture available)Removed minV (no architecture available)Removed numLookupSpecs (no architecture available)Removed pbUserPaneCtlHdl (no architecture available)Removed printers (no architecture available)Removed prologueFlags (no architecture available)Removed ref (no architecture available)Removed selected (no architecture available)Removed specIndex (no architecture available)Removed status (no architecture available)Removed title (no architecture available)PMPrintingDialogExtensions.hRemoved #def SUMMARY_DISPLAY_ORDERRemoved #def kAppPageSetupDialogTypeIDStrRemoved #def kAppPrintDialogTypeIDStrRemoved #def kAppPrintThumbnailTypeIDStrRemoved #def kDialogExtensionIntfIDStrRemoved #def kGeneralPageSetupDialogTypeIDStrRemoved #def kGeneralPrintDialogTypeIDStrRemoved #def kPMColorMatchingPDEKindIDRemoved #def kPMColorPDEKindIDRemoved #def kPMCopiesAndPagesPDEKindIDRemoved #def kPMCoverPagePDEKindIDRemoved #def kPMCustomPaperSizePDEKindIDRemoved #def kPMDuplexPDEKindIDRemoved #def kPMErrorHandlingPDEKindIDRemoved #def kPMFaxCoverPagePDEKindIDRemoved #def kPMFaxModemPDEKindIDRemoved #def kPMImagingOptionsPDEKindIDRemoved #def kPMInkPDEKindIDRemoved #def kPMLayoutPDEKindIDRemoved #def kPMOutputOptionsPDEKindIDRemoved #def kPMPageAttributesKindIDRemoved #def kPMPaperFeedPDEKindIDRemoved #def kPMPaperHandlingPDEKindIDRemoved #def kPMPaperSourcePDEKindIDRemoved #def kPMPrinterFeaturesPDEKindIDRemoved #def kPMPriorityPDEKindIDRemoved #def kPMQualityMediaPDEKindIDRemoved #def kPMRotationScalingPDEKindIDRemoved #def kPMSchedulerPDEKindIDRemoved #def kPMSummaryPanelKindIDRemoved #def kPrinterModuleTypeIDStrPMPrintingDialogExtensionsDeprecated.hRemoved CloseProcPtrRemoved GetSummaryTextProcPtrRemoved InitializeProcPtrRemoved OpenProcPtrRemoved PMCreateLocalizedPaperSizeCFString()Removed PMCreatePaperSizeCFString()Removed PMPDEContextRemoved PMPDEFlagsRemoved PMPDERefRemoved PMUpdatePrintButton()Removed PlugInIntfRemoved PlugInIntfVTableRemoved PrologueProcPtrRemoved SyncProcPtrRemoved TerminateProcPtrRemoved creator (no architecture available)Removed embedderUserPane (no architecture available)Removed flags (no architecture available)Removed kEventClassPrintingRemoved kEventParamPDEHeightRemoved kEventPrintingPDEResizeRemoved kEventUpdatePrintButtonRemoved #def kPDEBaseVersionMajorRemoved #def kPDEBaseVersionMinorRemoved #def kPDEBuildVersionMajorRemoved #def kPDEBuildVersionMinorRemoved #def kPDE_PMJobTemplateRefRemoved #def kPDE_PMPageFormatRefRemoved #def kPDE_PMPrintSettingsRefRemoved #def kPDE_PMPrinterInfoRefRemoved kPMPDEAllFlagsRemoved kPMPDENoFlagsRemoved kPMPDENoSummaryRemoved kPMSyncPaneFromTicketRemoved kPMSyncTicketFromPaneRemoved printSession (no architecture available)Removed reinitializePlugIn (no architecture available)Removed summaryArray (no architecture available)Removed titleArray (no architecture available)Removed userOptionKind (no architecture available)

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
