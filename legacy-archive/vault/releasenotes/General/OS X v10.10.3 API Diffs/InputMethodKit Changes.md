---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/InputMethodKit.html
archived_at: '2026-07-18T02:52:32.600453Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# InputMethodKit Changes

## InputMethodKit

Added IMKCandidates.attachChild(IMKCandidates!, toCandidate: Int, type: IMKStyleType)Added IMKCandidates.attributes() -> [NSObject: AnyObject]!Added IMKCandidates.candidateFrame() -> NSRectAdded IMKCandidates.candidateStringIdentifier(AnyObject!) -> IntAdded IMKCandidates.detachChild(Int)Added IMKCandidates.dismissesAutomatically() -> BoolAdded IMKCandidates.hideChild()Added IMKCandidates.selectCandidate(Int)Added IMKCandidates.selectCandidateWithIdentifier(Int) -> BoolAdded IMKCandidates.selectedCandidate() -> IntAdded IMKCandidates.selectionKeys() -> [AnyObject]!Added IMKCandidates.selectionKeysKeylayout() -> Unmanaged<TISInputSource>!Added IMKCandidates.setAttributes([NSObject: AnyObject]!)Added IMKCandidates.setCandidateData([AnyObject]!)Added IMKCandidates.setCandidateFrameTopLeft(NSPoint)Added IMKCandidates.setDismissesAutomatically(Bool)Added IMKCandidates.setSelectionKeys([AnyObject]!)Added IMKCandidates.setSelectionKeysKeylayout(TISInputSource!)Added IMKCandidates.showCandidates()Added IMKCandidates.showChild()Added NSObject.candidates(AnyObject!) -> [AnyObject]!Added NSObject.commitComposition(AnyObject!)Added NSObject.composedString(AnyObject!) -> AnyObject!Added NSObject.didCommandBySelector(Selector, client: AnyObject!) -> BoolAdded NSObject.handleEvent(NSEvent!, client: AnyObject!) -> BoolAdded NSObject.inputText(String!, client: AnyObject!) -> BoolAdded NSObject.inputText(String!, key: Int, modifiers: Int, client: AnyObject!) -> BoolAdded NSObject.originalString(AnyObject!) -> NSAttributedString!Modified IMKCandidates.candidateIdentifierAtLineNumber(Int) -> Int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IMKCandidates.clearSelection()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IMKCandidates.lineNumberForCandidateWithIdentifier(Int) -> Int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IMKCandidates.init(server: IMKServer!, panelType: IMKCandidatePanelType)

|  | Declaration |
| --- | --- |
| From | ``` init(server server: IMKServer!, panelType panelType: IMKCandidatePanelType) ``` |
| To | ``` init!(server server: IMKServer!, panelType panelType: IMKCandidatePanelType) ``` |

Modified IMKCandidates.init(server: IMKServer!, panelType: IMKCandidatePanelType, styleType: IMKStyleType)

|  | Declaration |
| --- | --- |
| From | ``` init(server server: IMKServer!, panelType panelType: IMKCandidatePanelType, styleType style: IMKStyleType) ``` |
| To | ``` init!(server server: IMKServer!, panelType panelType: IMKCandidatePanelType, styleType style: IMKStyleType) ``` |

Modified IMKInputController.inputControllerWillClose()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IMKInputController.init(server: IMKServer!, delegate: AnyObject!, client: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(server server: IMKServer!, delegate delegate: AnyObject!, client inputClient: AnyObject!) ``` |
| To | ``` init!(server server: IMKServer!, delegate delegate: AnyObject!, client inputClient: AnyObject!) ``` |

Modified IMKMouseHandling.mouseDownOnCharacterIndex(Int, coordinate: NSPoint, withModifier: Int, continueTracking: UnsafeMutablePointer<ObjCBool>, client: AnyObject!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func mouseDownOnCharacterIndex(_ index: Int, coordinate point: NSPoint, withModifier flags: Int, continueTracking keepTracking: UnsafePointer<ObjCBool>, client sender: AnyObject!) -> Bool ``` |
| To | ``` func mouseDownOnCharacterIndex(_ index: Int, coordinate point: NSPoint, withModifier flags: Int, continueTracking keepTracking: UnsafeMutablePointer<ObjCBool>, client sender: AnyObject!) -> Bool ``` |

Modified IMKServer.lastKeyEventWasDeadKey() -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IMKServer.init(name: String!, bundleIdentifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!, bundleIdentifier bundleIdentifier: String!) ``` |
| To | ``` init!(name name: String!, bundleIdentifier bundleIdentifier: String!) ``` |

Modified IMKServer.init(name: String!, controllerClass: AnyClass!, delegateClass: AnyClass!)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!, controllerClass controllerClassID: AnyClass!, delegateClass delegateClassID: AnyClass!) ``` |
| To | ``` init!(name name: String!, controllerClass controllerClassID: AnyClass!, delegateClass delegateClassID: AnyClass!) ``` |

Modified IMKServer.paletteWillTerminate() -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IMKCandidatesOpacityAttributeName

|  | Declaration |
| --- | --- |
| From | ``` var IMKCandidatesOpacityAttributeName: NSString! ``` |
| To | ``` let IMKCandidatesOpacityAttributeName: String ``` |

Modified IMKCandidatesSendServerKeyEventFirst

|  | Declaration |
| --- | --- |
| From | ``` var IMKCandidatesSendServerKeyEventFirst: NSString! ``` |
| To | ``` let IMKCandidatesSendServerKeyEventFirst: String ``` |

Modified IMKControllerClass

|  | Declaration |
| --- | --- |
| From | ``` var IMKControllerClass: NSString! ``` |
| To | ``` let IMKControllerClass: String ``` |

Modified IMKDelegateClass

|  | Declaration |
| --- | --- |
| From | ``` var IMKDelegateClass: NSString! ``` |
| To | ``` let IMKDelegateClass: String ``` |

Modified IMKModeDictionary

|  | Declaration |
| --- | --- |
| From | ``` var IMKModeDictionary: NSString! ``` |
| To | ``` let IMKModeDictionary: String ``` |

Modified kIMKCommandClientName

|  | Declaration |
| --- | --- |
| From | ``` var kIMKCommandClientName: NSString! ``` |
| To | ``` let kIMKCommandClientName: String ``` |

Modified kIMKCommandMenuItemName

|  | Declaration |
| --- | --- |
| From | ``` var kIMKCommandMenuItemName: NSString! ``` |
| To | ``` let kIMKCommandMenuItemName: String ``` |

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
