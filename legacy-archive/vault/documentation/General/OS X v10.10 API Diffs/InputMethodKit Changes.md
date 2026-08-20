---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/InputMethodKit.html
archived_at: '2026-07-15T07:34:55.652211Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# InputMethodKit Changes

## InputMethodKit (Added)

Added IMKCandidatesAdded IMKCandidates.candidateIdentifierAtLineNumber(Int) -> IntAdded IMKCandidates.clearSelection()Added IMKCandidates.hide()Added IMKCandidates.isVisible() -> BoolAdded IMKCandidates.lineNumberForCandidateWithIdentifier(Int) -> IntAdded IMKCandidates.panelType() -> IMKCandidatePanelTypeAdded IMKCandidates.selectedCandidateString() -> NSAttributedString!Added IMKCandidates.init(server: IMKServer!, panelType: IMKCandidatePanelType)Added IMKCandidates.init(server: IMKServer!, panelType: IMKCandidatePanelType, styleType: IMKStyleType)Added IMKCandidates.setPanelType(IMKCandidatePanelType)Added IMKCandidates.show(IMKCandidatesLocationHint)Added IMKCandidates.showAnnotation(NSAttributedString!)Added IMKCandidates.showSublist([AnyObject]!, subListDelegate: AnyObject!)Added IMKCandidates.updateCandidates()Added IMKInputControllerAdded IMKInputController.annotationSelected(NSAttributedString!, forCandidate: NSAttributedString!)Added IMKInputController.cancelComposition()Added IMKInputController.candidateSelected(NSAttributedString!)Added IMKInputController.candidateSelectionChanged(NSAttributedString!)Added IMKInputController.client() -> protocol<IMKTextInput, NSObjectProtocol>!Added IMKInputController.compositionAttributesAtRange(NSRange) -> NSMutableDictionary!Added IMKInputController.delegate() -> AnyObject!Added IMKInputController.doCommandBySelector(Selector, commandDictionary:[NSObject: AnyObject]!)Added IMKInputController.hidePalettes()Added IMKInputController.inputControllerWillClose()Added IMKInputController.markForStyle(Int, atRange: NSRange) -> [NSObject: AnyObject]!Added IMKInputController.menu() -> NSMenu!Added IMKInputController.replacementRange() -> NSRangeAdded IMKInputController.selectionRange() -> NSRangeAdded IMKInputController.server() -> IMKServer!Added IMKInputController.init(server: IMKServer!, delegate: AnyObject!, client: AnyObject!)Added IMKInputController.setDelegate(AnyObject!)Added IMKInputController.updateComposition()Added IMKMouseHandlingAdded IMKMouseHandling.mouseDownOnCharacterIndex(Int, coordinate: NSPoint, withModifier: Int, continueTracking: UnsafeMutablePointer<ObjCBool>, client: AnyObject!) -> BoolAdded IMKMouseHandling.mouseMovedOnCharacterIndex(Int, coordinate: NSPoint, withModifier: Int, client: AnyObject!) -> BoolAdded IMKMouseHandling.mouseUpOnCharacterIndex(Int, coordinate: NSPoint, withModifier: Int, client: AnyObject!) -> BoolAdded IMKServerAdded IMKServer.bundle() -> NSBundle!Added IMKServer.lastKeyEventWasDeadKey() -> BoolAdded IMKServer.init(name: String!, bundleIdentifier: String!)Added IMKServer.init(name: String!, controllerClass: AnyClass!, delegateClass: AnyClass!)Added IMKServer.paletteWillTerminate() -> BoolAdded IMKStateSettingAdded IMKStateSetting.activateServer(AnyObject!)Added IMKStateSetting.deactivateServer(AnyObject!)Added IMKStateSetting.modes(AnyObject!) -> [NSObject: AnyObject]!Added IMKStateSetting.recognizedEvents(AnyObject!) -> IntAdded IMKStateSetting.setValue(AnyObject!, forTag: Int, client: AnyObject!)Added IMKStateSetting.showPreferences(AnyObject!)Added IMKStateSetting.valueForTag(Int, client: AnyObject!) -> AnyObject!Added NSObject.candidates(AnyObject!) -> [AnyObject]!Added NSObject.commitComposition(AnyObject!)Added NSObject.composedString(AnyObject!) -> AnyObject!Added NSObject.didCommandBySelector(Selector, client: AnyObject!) -> BoolAdded NSObject.handleEvent(NSEvent!, client: AnyObject!) -> BoolAdded NSObject.inputText(String!, client: AnyObject!) -> BoolAdded NSObject.inputText(String!, key: Int, modifiers: Int, client: AnyObject!) -> BoolAdded NSObject.originalString(AnyObject!) -> NSAttributedString!Added IMKCandidatePanelTypeAdded IMKCandidatesLocationHintAdded IMKCandidatesOpacityAttributeNameAdded IMKCandidatesSendServerKeyEventFirstAdded IMKControllerClassAdded IMKDelegateClassAdded IMKModeDictionaryAdded IMKStyleTypeAdded kIMKAnnotationAdded kIMKCommandClientNameAdded kIMKCommandMenuItemNameAdded kIMKLocateCandidatesAboveHintAdded kIMKLocateCandidatesBelowHintAdded kIMKLocateCandidatesLeftHintAdded kIMKLocateCandidatesRightHintAdded kIMKMainAdded kIMKScrollingGridCandidatePanelAdded kIMKSingleColumnScrollingCandidatePanelAdded kIMKSingleRowSteppingCandidatePanelAdded kIMKSubList

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
