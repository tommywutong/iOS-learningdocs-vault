---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/InputMethodKit.html
archived_at: '2026-07-18T02:51:27.401074Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# InputMethodKit Changes for Swift

### InputMethodKit

Modified [IMKCandidates](https://developer.apple.com/documentation/inputmethodkit/imkcandidates)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class IMKCandidates : NSResponder {     init!(server server: IMKServer!, panelType panelType: IMKCandidatePanelType)     init!(server server: IMKServer!, panelType panelType: IMKCandidatePanelType, styleType style: IMKStyleType)     func panelType() -> IMKCandidatePanelType     func setPanelType(_ panelType: IMKCandidatePanelType)     func show(_ locationHint: IMKCandidatesLocationHint)     func hide()     func isVisible() -> Bool     func updateCandidates()     func showAnnotation(_ annotationString: NSAttributedString!)     func showSublist(_ candidates: [AnyObject]!, subListDelegate delegate: AnyObject!)     func selectedCandidateString() -> NSAttributedString!     func setCandidateFrameTopLeft(_ point: NSPoint)     func candidateFrame() -> NSRect     func setSelectionKeys(_ keyCodes: [AnyObject]!)     func selectionKeys() -> [AnyObject]!     func setSelectionKeysKeylayout(_ layout: TISInputSource!)     func selectionKeysKeylayout() -> Unmanaged<TISInputSource>!     func setAttributes(_ attributes: [NSObject : AnyObject]!)     func attributes() -> [NSObject : AnyObject]!     func setDismissesAutomatically(_ flag: Bool)     func dismissesAutomatically() -> Bool     func selectedCandidate() -> Int     func showChild()     func hideChild()     func attachChild(_ child: IMKCandidates!, toCandidate candidateIdentifier: Int, type theType: IMKStyleType)     func detachChild(_ candidateIdentifier: Int)     func setCandidateData(_ candidatesArray: [AnyObject]!)     func selectCandidateWithIdentifier(_ candidateIdentifier: Int) -> Bool     func selectCandidate(_ candidateIdentifier: Int)     func showCandidates()     func candidateStringIdentifier(_ candidateString: AnyObject!) -> Int     func candidateIdentifierAtLineNumber(_ lineNumber: Int) -> Int     func lineNumberForCandidateWithIdentifier(_ candidateIdentifier: Int) -> Int     func clearSelection() } ``` | -- |
| To | ``` class IMKCandidates : NSResponder {     init!(server server: IMKServer!, panelType panelType: IMKCandidatePanelType)     init!(server server: IMKServer!, panelType panelType: IMKCandidatePanelType, styleType style: IMKStyleType)     func panelType() -> IMKCandidatePanelType     func setPanelType(_ panelType: IMKCandidatePanelType)     func show(_ locationHint: IMKCandidatesLocationHint)     func hide()     func isVisible() -> Bool     func update()     func showAnnotation(_ annotationString: NSAttributedString!)     func showSublist(_ candidates: [Any]!, subListDelegate delegate: Any!)     func selectedCandidateString() -> NSAttributedString!     func setCandidateFrameTopLeft(_ point: NSPoint)     func candidateFrame() -> NSRect     func setSelectionKeys(_ keyCodes: [Any]!)     func selectionKeys() -> [Any]!     func setSelectionKeysKeylayout(_ layout: TISInputSource!)     func selectionKeysKeylayout() -> Unmanaged<TISInputSource>!     func setAttributes(_ attributes: [AnyHashable : Any]!)     func attributes() -> [AnyHashable : Any]!     func setDismissesAutomatically(_ flag: Bool)     func dismissesAutomatically() -> Bool     func selectedCandidate() -> Int     func showChild()     func hideChild()     func attachChild(_ child: IMKCandidates!, toCandidate candidateIdentifier: Int, type theType: IMKStyleType)     func detachChild(_ candidateIdentifier: Int)     func setCandidateData(_ candidatesArray: [Any]!)     func selectCandidate(withIdentifier candidateIdentifier: Int) -> Bool     func selectCandidate(_ candidateIdentifier: Int)     func show()     func candidateStringIdentifier(_ candidateString: Any!) -> Int     func candidateIdentifier(atLineNumber lineNumber: Int) -> Int     func lineNumberForCandidate(withIdentifier candidateIdentifier: Int) -> Int     func clearSelection()     func encodeRestorableState(with coder: NSCoder)     func restoreState(with coder: NSCoder)     func invalidateRestorableState()     class func restorableStateKeyPaths() -> [String]     func interfaceStyle() -> Int     func setInterfaceStyle(_ interfaceStyle: Int)     var userActivity: NSUserActivity?     func updateUserActivityState(_ userActivity: NSUserActivity)     func restoreUserActivityState(_ userActivity: NSUserActivity)     func performMnemonic(_ string: String) -> Bool     @IBAction func newWindowForTab(_ sender: Any?)     func performTextFinderAction(_ sender: Any?)     func presentError(_ error: Error, modalFor window: NSWindow, delegate delegate: Any?, didPresent didPresentSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func presentError(_ error: Error) -> Bool     func willPresentError(_ error: Error) -> Error     func validateProposedFirstResponder(_ responder: NSResponder, for event: NSEvent?) -> Bool     var undoManager: UndoManager? { get }     func insertText(_ insertString: Any)     func doCommand(by selector: Selector)     func moveForward(_ sender: Any?)     func moveRight(_ sender: Any?)     func moveBackward(_ sender: Any?)     func moveLeft(_ sender: Any?)     func moveUp(_ sender: Any?)     func moveDown(_ sender: Any?)     func moveWordForward(_ sender: Any?)     func moveWordBackward(_ sender: Any?)     func moveToBeginningOfLine(_ sender: Any?)     func moveToEndOfLine(_ sender: Any?)     func moveToBeginningOfParagraph(_ sender: Any?)     func moveToEndOfParagraph(_ sender: Any?)     func moveToEndOfDocument(_ sender: Any?)     func moveToBeginningOfDocument(_ sender: Any?)     func pageDown(_ sender: Any?)     func pageUp(_ sender: Any?)     func centerSelectionInVisibleArea(_ sender: Any?)     func moveBackwardAndModifySelection(_ sender: Any?)     func moveForwardAndModifySelection(_ sender: Any?)     func moveWordForwardAndModifySelection(_ sender: Any?)     func moveWordBackwardAndModifySelection(_ sender: Any?)     func moveUpAndModifySelection(_ sender: Any?)     func moveDownAndModifySelection(_ sender: Any?)     func moveToBeginningOfLineAndModifySelection(_ sender: Any?)     func moveToEndOfLineAndModifySelection(_ sender: Any?)     func moveToBeginningOfParagraphAndModifySelection(_ sender: Any?)     func moveToEndOfParagraphAndModifySelection(_ sender: Any?)     func moveToEndOfDocumentAndModifySelection(_ sender: Any?)     func moveToBeginningOfDocumentAndModifySelection(_ sender: Any?)     func pageDownAndModifySelection(_ sender: Any?)     func pageUpAndModifySelection(_ sender: Any?)     func moveParagraphForwardAndModifySelection(_ sender: Any?)     func moveParagraphBackwardAndModifySelection(_ sender: Any?)     func moveWordRight(_ sender: Any?)     func moveWordLeft(_ sender: Any?)     func moveRightAndModifySelection(_ sender: Any?)     func moveLeftAndModifySelection(_ sender: Any?)     func moveWordRightAndModifySelection(_ sender: Any?)     func moveWordLeftAndModifySelection(_ sender: Any?)     func moveToLeftEndOfLine(_ sender: Any?)     func moveToRightEndOfLine(_ sender: Any?)     func moveToLeftEndOfLineAndModifySelection(_ sender: Any?)     func moveToRightEndOfLineAndModifySelection(_ sender: Any?)     func scrollPageUp(_ sender: Any?)     func scrollPageDown(_ sender: Any?)     func scrollLineUp(_ sender: Any?)     func scrollLineDown(_ sender: Any?)     func scrollToBeginningOfDocument(_ sender: Any?)     func scrollToEndOfDocument(_ sender: Any?)     func transpose(_ sender: Any?)     func transposeWords(_ sender: Any?)     func selectAll(_ sender: Any?)     func selectParagraph(_ sender: Any?)     func selectLine(_ sender: Any?)     func selectWord(_ sender: Any?)     func indent(_ sender: Any?)     func insertTab(_ sender: Any?)     func insertBacktab(_ sender: Any?)     func insertNewline(_ sender: Any?)     func insertParagraphSeparator(_ sender: Any?)     func insertNewlineIgnoringFieldEditor(_ sender: Any?)     func insertTabIgnoringFieldEditor(_ sender: Any?)     func insertLineBreak(_ sender: Any?)     func insertContainerBreak(_ sender: Any?)     func insertSingleQuoteIgnoringSubstitution(_ sender: Any?)     func insertDoubleQuoteIgnoringSubstitution(_ sender: Any?)     func changeCaseOfLetter(_ sender: Any?)     func uppercaseWord(_ sender: Any?)     func lowercaseWord(_ sender: Any?)     func capitalizeWord(_ sender: Any?)     func deleteForward(_ sender: Any?)     func deleteBackward(_ sender: Any?)     func deleteBackwardByDecomposingPreviousCharacter(_ sender: Any?)     func deleteWordForward(_ sender: Any?)     func deleteWordBackward(_ sender: Any?)     func deleteToBeginningOfLine(_ sender: Any?)     func deleteToEndOfLine(_ sender: Any?)     func deleteToBeginningOfParagraph(_ sender: Any?)     func deleteToEndOfParagraph(_ sender: Any?)     func yank(_ sender: Any?)     func complete(_ sender: Any?)     func setMark(_ sender: Any?)     func deleteToMark(_ sender: Any?)     func selectToMark(_ sender: Any?)     func swapWithMark(_ sender: Any?)     func cancelOperation(_ sender: Any?)     func makeBaseWritingDirectionNatural(_ sender: Any?)     func makeBaseWritingDirectionLeftToRight(_ sender: Any?)     func makeBaseWritingDirectionRightToLeft(_ sender: Any?)     func makeTextWritingDirectionNatural(_ sender: Any?)     func makeTextWritingDirectionLeftToRight(_ sender: Any?)     func makeTextWritingDirectionRightToLeft(_ sender: Any?)     func quickLookPreviewItems(_ sender: Any?)     func inputText(_ string: String!, key keyCode: Int, modifiers flags: Int, client sender: Any!) -> Bool     func inputText(_ string: String!, client sender: Any!) -> Bool     func handle(_ event: NSEvent!, client sender: Any!) -> Bool     func didCommand(by aSelector: Selector!, client sender: Any!) -> Bool     func composedString(_ sender: Any!) -> Any!     func originalString(_ sender: Any!) -> NSAttributedString!     func commitComposition(_ sender: Any!)     func candidates(_ sender: Any!) -> [Any]!     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any)     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any?     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription]     func validateToolbarItem(_ item: NSToolbarItem) -> Bool     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification)     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func changeColor(_ sender: Any?)     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard)     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int     func changeFont(_ sender: Any?)     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification)     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool)     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get }     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension IMKCandidates : CVarArg { } extension IMKCandidates : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [IMKCandidates.attributes() -> [AnyHashable : Any]!](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385440-attributes)

|  | Declaration |
| --- | --- |
| From | ``` func attributes() -> [NSObject : AnyObject]! ``` |
| To | ``` func attributes() -> [AnyHashable : Any]! ``` |

Modified [IMKCandidates.candidateIdentifier(atLineNumber: Int) -> Int](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385471-candidateidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func candidateIdentifierAtLineNumber(_ lineNumber: Int) -> Int ``` |
| To | ``` func candidateIdentifier(atLineNumber lineNumber: Int) -> Int ``` |

Modified [IMKCandidates.candidateStringIdentifier(_: Any!) -> Int](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385512-candidatestringidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func candidateStringIdentifier(_ candidateString: AnyObject!) -> Int ``` |
| To | ``` func candidateStringIdentifier(_ candidateString: Any!) -> Int ``` |

Modified [IMKCandidates.lineNumberForCandidate(withIdentifier: Int) -> Int](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385488-linenumberforcandidatewithidenti)

|  | Declaration |
| --- | --- |
| From | ``` func lineNumberForCandidateWithIdentifier(_ candidateIdentifier: Int) -> Int ``` |
| To | ``` func lineNumberForCandidate(withIdentifier candidateIdentifier: Int) -> Int ``` |

Modified [IMKCandidates.selectCandidate(withIdentifier: Int) -> Bool](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385559-selectcandidate)

|  | Declaration |
| --- | --- |
| From | ``` func selectCandidateWithIdentifier(_ candidateIdentifier: Int) -> Bool ``` |
| To | ``` func selectCandidate(withIdentifier candidateIdentifier: Int) -> Bool ``` |

Modified [IMKCandidates.selectionKeys() -> [Any]!](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385537-selectionkeys)

|  | Declaration |
| --- | --- |
| From | ``` func selectionKeys() -> [AnyObject]! ``` |
| To | ``` func selectionKeys() -> [Any]! ``` |

Modified [IMKCandidates.setAttributes(_: [AnyHashable : Any]!)](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385465-setattributes)

|  | Declaration |
| --- | --- |
| From | ``` func setAttributes(_ attributes: [NSObject : AnyObject]!) ``` |
| To | ``` func setAttributes(_ attributes: [AnyHashable : Any]!) ``` |

Modified [IMKCandidates.setCandidateData(_: [Any]!)](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385508-setcandidatedata)

|  | Declaration |
| --- | --- |
| From | ``` func setCandidateData(_ candidatesArray: [AnyObject]!) ``` |
| To | ``` func setCandidateData(_ candidatesArray: [Any]!) ``` |

Modified [IMKCandidates.setSelectionKeys(_: [Any]!)](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385522-setselectionkeys)

|  | Declaration |
| --- | --- |
| From | ``` func setSelectionKeys(_ keyCodes: [AnyObject]!) ``` |
| To | ``` func setSelectionKeys(_ keyCodes: [Any]!) ``` |

Modified [IMKCandidates.show()](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385404-show)

|  | Declaration |
| --- | --- |
| From | ``` func showCandidates() ``` |
| To | ``` func show() ``` |

Modified [IMKCandidates.showSublist(_: [Any]!, subListDelegate: Any!)](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385492-showsublist)

|  | Declaration |
| --- | --- |
| From | ``` func showSublist(_ candidates: [AnyObject]!, subListDelegate delegate: AnyObject!) ``` |
| To | ``` func showSublist(_ candidates: [Any]!, subListDelegate delegate: Any!) ``` |

Modified [IMKCandidates.update()](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385516-updatecandidates)

|  | Declaration |
| --- | --- |
| From | ``` func updateCandidates() ``` |
| To | ``` func update() ``` |

Modified [IMKInputController](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class IMKInputController : NSObject, IMKStateSetting, IMKMouseHandling {     init!(server server: IMKServer!, delegate delegate: AnyObject!, client inputClient: AnyObject!)     func updateComposition()     func cancelComposition()     func compositionAttributesAtRange(_ range: NSRange) -> NSMutableDictionary!     func selectionRange() -> NSRange     func replacementRange() -> NSRange     func markForStyle(_ style: Int, atRange range: NSRange) -> [NSObject : AnyObject]!     func doCommandBySelector(_ aSelector: Selector, commandDictionary infoDictionary: [NSObject : AnyObject]!)     func hidePalettes()     func menu() -> NSMenu!     func delegate() -> AnyObject!     func setDelegate(_ newDelegate: AnyObject!)     func server() -> IMKServer!     func client() -> protocol<IMKTextInput, NSObjectProtocol>!     func inputControllerWillClose()     func annotationSelected(_ annotationString: NSAttributedString!, forCandidate candidateString: NSAttributedString!)     func candidateSelectionChanged(_ candidateString: NSAttributedString!)     func candidateSelected(_ candidateString: NSAttributedString!) } ``` | IMKMouseHandling, IMKStateSetting |
| To | ``` class IMKInputController : NSObject, IMKStateSetting, IMKMouseHandling {     init!(server server: IMKServer!, delegate delegate: Any!, client inputClient: Any!)     func updateComposition()     func cancelComposition()     func compositionAttributes(at range: NSRange) -> NSMutableDictionary!     func selectionRange() -> NSRange     func replacementRange() -> NSRange     func mark(forStyle style: Int, at range: NSRange) -> [AnyHashable : Any]!     func doCommand(by aSelector: Selector!, command infoDictionary: [AnyHashable : Any]!)     func hidePalettes()     func menu() -> NSMenu!     func delegate() -> Any!     func setDelegate(_ newDelegate: Any!)     func server() -> IMKServer!     func client() -> (IMKTextInput & NSObjectProtocol)!     func inputControllerWillClose()     func annotationSelected(_ annotationString: NSAttributedString!, forCandidate candidateString: NSAttributedString!)     func candidateSelectionChanged(_ candidateString: NSAttributedString!)     func candidateSelected(_ candidateString: NSAttributedString!)     func inputText(_ string: String!, key keyCode: Int, modifiers flags: Int, client sender: Any!) -> Bool     func inputText(_ string: String!, client sender: Any!) -> Bool     func handle(_ event: NSEvent!, client sender: Any!) -> Bool     func didCommand(by aSelector: Selector!, client sender: Any!) -> Bool     func composedString(_ sender: Any!) -> Any!     func originalString(_ sender: Any!) -> NSAttributedString!     func commitComposition(_ sender: Any!)     func candidates(_ sender: Any!) -> [Any]!     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any)     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any?     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription]     func validateToolbarItem(_ item: NSToolbarItem) -> Bool     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification)     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func changeColor(_ sender: Any?)     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard)     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int     func changeFont(_ sender: Any?)     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification)     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool)     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get }     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension IMKInputController : CVarArg { } extension IMKInputController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, IMKMouseHandling, IMKStateSetting |

Modified [IMKInputController.client() -> (IMKTextInput & NSObjectProtocol)!](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/1385490-client)

|  | Declaration |
| --- | --- |
| From | ``` func client() -> protocol<IMKTextInput, NSObjectProtocol>! ``` |
| To | ``` func client() -> (IMKTextInput & NSObjectProtocol)! ``` |

Modified [IMKInputController.compositionAttributes(at: NSRange) -> NSMutableDictionary!](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/1385453-compositionattributes)

|  | Declaration |
| --- | --- |
| From | ``` func compositionAttributesAtRange(_ range: NSRange) -> NSMutableDictionary! ``` |
| To | ``` func compositionAttributes(at range: NSRange) -> NSMutableDictionary! ``` |

Modified [IMKInputController.delegate() -> Any!](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/1385555-delegate)

|  | Declaration |
| --- | --- |
| From | ``` func delegate() -> AnyObject! ``` |
| To | ``` func delegate() -> Any! ``` |

Modified [IMKInputController.doCommand(by: Selector!, command: [AnyHashable : Any]!)](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/1385553-docommand)

|  | Declaration |
| --- | --- |
| From | ``` func doCommandBySelector(_ aSelector: Selector, commandDictionary infoDictionary: [NSObject : AnyObject]!) ``` |
| To | ``` func doCommand(by aSelector: Selector!, command infoDictionary: [AnyHashable : Any]!) ``` |

Modified [IMKInputController.init(server: IMKServer!, delegate: Any!, client: Any!)](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/1385385-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(server server: IMKServer!, delegate delegate: AnyObject!, client inputClient: AnyObject!) ``` |
| To | ``` init!(server server: IMKServer!, delegate delegate: Any!, client inputClient: Any!) ``` |

Modified [IMKInputController.mark(forStyle: Int, at: NSRange) -> [AnyHashable : Any]!](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/1385381-mark)

|  | Declaration |
| --- | --- |
| From | ``` func markForStyle(_ style: Int, atRange range: NSRange) -> [NSObject : AnyObject]! ``` |
| To | ``` func mark(forStyle style: Int, at range: NSRange) -> [AnyHashable : Any]! ``` |

Modified [IMKInputController.setDelegate(_: Any!)](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/1385557-setdelegate)

|  | Declaration |
| --- | --- |
| From | ``` func setDelegate(_ newDelegate: AnyObject!) ``` |
| To | ``` func setDelegate(_ newDelegate: Any!) ``` |

Modified [IMKMouseHandling](https://developer.apple.com/documentation/inputmethodkit/imkmousehandling)

|  | Declaration |
| --- | --- |
| From | ``` protocol IMKMouseHandling {     func mouseDownOnCharacterIndex(_ index: Int, coordinate point: NSPoint, withModifier flags: Int, continueTracking keepTracking: UnsafeMutablePointer<ObjCBool>, client sender: AnyObject!) -> Bool     func mouseUpOnCharacterIndex(_ index: Int, coordinate point: NSPoint, withModifier flags: Int, client sender: AnyObject!) -> Bool     func mouseMovedOnCharacterIndex(_ index: Int, coordinate point: NSPoint, withModifier flags: Int, client sender: AnyObject!) -> Bool } ``` |
| To | ``` protocol IMKMouseHandling {     func mouseDown(onCharacterIndex index: Int, coordinate point: NSPoint, withModifier flags: Int, continueTracking keepTracking: UnsafeMutablePointer<ObjCBool>!, client sender: Any!) -> Bool     func mouseUp(onCharacterIndex index: Int, coordinate point: NSPoint, withModifier flags: Int, client sender: Any!) -> Bool     func mouseMoved(onCharacterIndex index: Int, coordinate point: NSPoint, withModifier flags: Int, client sender: Any!) -> Bool } ``` |

Modified [IMKMouseHandling.mouseDown(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, continueTracking: UnsafeMutablePointer<ObjCBool>!, client: Any!) -> Bool](https://developer.apple.com/documentation/inputmethodkit/imkmousehandling/1385444-mousedown)

|  | Declaration |
| --- | --- |
| From | ``` func mouseDownOnCharacterIndex(_ index: Int, coordinate point: NSPoint, withModifier flags: Int, continueTracking keepTracking: UnsafeMutablePointer<ObjCBool>, client sender: AnyObject!) -> Bool ``` |
| To | ``` func mouseDown(onCharacterIndex index: Int, coordinate point: NSPoint, withModifier flags: Int, continueTracking keepTracking: UnsafeMutablePointer<ObjCBool>!, client sender: Any!) -> Bool ``` |

Modified [IMKMouseHandling.mouseMoved(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, client: Any!) -> Bool](https://developer.apple.com/documentation/inputmethodkit/imkmousehandling/1385551-mousemoved)

|  | Declaration |
| --- | --- |
| From | ``` func mouseMovedOnCharacterIndex(_ index: Int, coordinate point: NSPoint, withModifier flags: Int, client sender: AnyObject!) -> Bool ``` |
| To | ``` func mouseMoved(onCharacterIndex index: Int, coordinate point: NSPoint, withModifier flags: Int, client sender: Any!) -> Bool ``` |

Modified [IMKMouseHandling.mouseUp(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, client: Any!) -> Bool](https://developer.apple.com/documentation/inputmethodkit/imkmousehandling/1385410-mouseuponcharacterindex)

|  | Declaration |
| --- | --- |
| From | ``` func mouseUpOnCharacterIndex(_ index: Int, coordinate point: NSPoint, withModifier flags: Int, client sender: AnyObject!) -> Bool ``` |
| To | ``` func mouseUp(onCharacterIndex index: Int, coordinate point: NSPoint, withModifier flags: Int, client sender: Any!) -> Bool ``` |

Modified [IMKServer](https://developer.apple.com/documentation/inputmethodkit/imkserver)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class IMKServer : NSObject {     init!(name name: String!, bundleIdentifier bundleIdentifier: String!)     init!(name name: String!, controllerClass controllerClassID: AnyClass!, delegateClass delegateClassID: AnyClass!)     func bundle() -> NSBundle!     func paletteWillTerminate() -> Bool     func lastKeyEventWasDeadKey() -> Bool } ``` | -- |
| To | ``` class IMKServer : NSObject {     init!(name name: String!, bundleIdentifier bundleIdentifier: String!)     init!(name name: String!, controllerClass controllerClassID: Swift.AnyClass!, delegateClass delegateClassID: Swift.AnyClass!)     func bundle() -> Bundle!     func paletteWillTerminate() -> Bool     func lastKeyEventWasDeadKey() -> Bool     func inputText(_ string: String!, key keyCode: Int, modifiers flags: Int, client sender: Any!) -> Bool     func inputText(_ string: String!, client sender: Any!) -> Bool     func handle(_ event: NSEvent!, client sender: Any!) -> Bool     func didCommand(by aSelector: Selector!, client sender: Any!) -> Bool     func composedString(_ sender: Any!) -> Any!     func originalString(_ sender: Any!) -> NSAttributedString!     func commitComposition(_ sender: Any!)     func candidates(_ sender: Any!) -> [Any]!     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any)     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any?     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription]     func validateToolbarItem(_ item: NSToolbarItem) -> Bool     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification)     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func changeColor(_ sender: Any?)     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard)     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int     func changeFont(_ sender: Any?)     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification)     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool)     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get }     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension IMKServer : CVarArg { } extension IMKServer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [IMKServer.bundle() -> Bundle!](https://developer.apple.com/documentation/inputmethodkit/imkserver/1385387-bundle)

|  | Declaration |
| --- | --- |
| From | ``` func bundle() -> NSBundle! ``` |
| To | ``` func bundle() -> Bundle! ``` |

Modified [IMKServer.init(name: String!, controllerClass: Swift.AnyClass!, delegateClass: Swift.AnyClass!)](https://developer.apple.com/documentation/inputmethodkit/imkserver/1385520-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!, controllerClass controllerClassID: AnyClass!, delegateClass delegateClassID: AnyClass!) ``` |
| To | ``` init!(name name: String!, controllerClass controllerClassID: Swift.AnyClass!, delegateClass delegateClassID: Swift.AnyClass!) ``` |

Modified [IMKStateSetting](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting)

|  | Declaration |
| --- | --- |
| From | ``` protocol IMKStateSetting {     func activateServer(_ sender: AnyObject!)     func deactivateServer(_ sender: AnyObject!)     func valueForTag(_ tag: Int, client sender: AnyObject!) -> AnyObject!     func setValue(_ value: AnyObject!, forTag tag: Int, client sender: AnyObject!)     func modes(_ sender: AnyObject!) -> [NSObject : AnyObject]!     func recognizedEvents(_ sender: AnyObject!) -> Int     func showPreferences(_ sender: AnyObject!) } ``` |
| To | ``` protocol IMKStateSetting {     func activateServer(_ sender: Any!)     func deactivateServer(_ sender: Any!)     func value(forTag tag: Int, client sender: Any!) -> Any!     func setValue(_ value: Any!, forTag tag: Int, client sender: Any!)     func modes(_ sender: Any!) -> [AnyHashable : Any]!     func recognizedEvents(_ sender: Any!) -> Int     func showPreferences(_ sender: Any!) } ``` |

Modified [IMKStateSetting.activateServer(_: Any!)](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting/1385434-activateserver)

|  | Declaration |
| --- | --- |
| From | ``` func activateServer(_ sender: AnyObject!) ``` |
| To | ``` func activateServer(_ sender: Any!) ``` |

Modified [IMKStateSetting.deactivateServer(_: Any!)](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting/1385424-deactivateserver)

|  | Declaration |
| --- | --- |
| From | ``` func deactivateServer(_ sender: AnyObject!) ``` |
| To | ``` func deactivateServer(_ sender: Any!) ``` |

Modified [IMKStateSetting.modes(_: Any!) -> [AnyHashable : Any]!](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting/1385461-modes)

|  | Declaration |
| --- | --- |
| From | ``` func modes(_ sender: AnyObject!) -> [NSObject : AnyObject]! ``` |
| To | ``` func modes(_ sender: Any!) -> [AnyHashable : Any]! ``` |

Modified [IMKStateSetting.recognizedEvents(_: Any!) -> Int](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting/1385535-recognizedevents)

|  | Declaration |
| --- | --- |
| From | ``` func recognizedEvents(_ sender: AnyObject!) -> Int ``` |
| To | ``` func recognizedEvents(_ sender: Any!) -> Int ``` |

Modified [IMKStateSetting.setValue(_: Any!, forTag: Int, client: Any!)](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting/1385412-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ value: AnyObject!, forTag tag: Int, client sender: AnyObject!) ``` |
| To | ``` func setValue(_ value: Any!, forTag tag: Int, client sender: Any!) ``` |

Modified [IMKStateSetting.showPreferences(_: Any!)](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting/1385549-showpreferences)

|  | Declaration |
| --- | --- |
| From | ``` func showPreferences(_ sender: AnyObject!) ``` |
| To | ``` func showPreferences(_ sender: Any!) ``` |

Modified [IMKStateSetting.value(forTag: Int, client: Any!) -> Any!](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting/1385547-value)

|  | Declaration |
| --- | --- |
| From | ``` func valueForTag(_ tag: Int, client sender: AnyObject!) -> AnyObject! ``` |
| To | ``` func value(forTag tag: Int, client sender: Any!) -> Any! ``` |

Modified [NSObject.candidates(_: Any!) -> [Any]!](https://developer.apple.com/documentation/objectivec/nsobject/1385360-candidates)

|  | Declaration |
| --- | --- |
| From | ``` func candidates(_ sender: AnyObject!) -> [AnyObject]! ``` |
| To | ``` func candidates(_ sender: Any!) -> [Any]! ``` |

Modified [NSObject.commitComposition(_: Any!)](https://developer.apple.com/documentation/objectivec/nsobject/1385539-commitcomposition)

|  | Declaration |
| --- | --- |
| From | ``` func commitComposition(_ sender: AnyObject!) ``` |
| To | ``` func commitComposition(_ sender: Any!) ``` |

Modified [NSObject.composedString(_: Any!) -> Any!](https://developer.apple.com/documentation/objectivec/nsobject/1385416-composedstring)

|  | Declaration |
| --- | --- |
| From | ``` func composedString(_ sender: AnyObject!) -> AnyObject! ``` |
| To | ``` func composedString(_ sender: Any!) -> Any! ``` |

Modified [NSObject.didCommand(by: Selector!, client: Any!) -> Bool](https://developer.apple.com/documentation/objectivec/nsobject/1385394-didcommand)

|  | Declaration |
| --- | --- |
| From | ``` func didCommandBySelector(_ aSelector: Selector, client sender: AnyObject!) -> Bool ``` |
| To | ``` func didCommand(by aSelector: Selector!, client sender: Any!) -> Bool ``` |

Modified [NSObject.handle(_: NSEvent!, client: Any!) -> Bool](https://developer.apple.com/documentation/objectivec/nsobject/1385363-handleevent)

|  | Declaration |
| --- | --- |
| From | ``` func handleEvent(_ event: NSEvent!, client sender: AnyObject!) -> Bool ``` |
| To | ``` func handle(_ event: NSEvent!, client sender: Any!) -> Bool ``` |

Modified [NSObject.inputText(_: String!, client: Any!) -> Bool](https://developer.apple.com/documentation/objectivec/nsobject/1385446-inputtext)

|  | Declaration |
| --- | --- |
| From | ``` func inputText(_ string: String!, client sender: AnyObject!) -> Bool ``` |
| To | ``` func inputText(_ string: String!, client sender: Any!) -> Bool ``` |

Modified [NSObject.inputText(_: String!, key: Int, modifiers: Int, client: Any!) -> Bool](https://developer.apple.com/documentation/objectivec/nsobject/1385436-inputtext)

|  | Declaration |
| --- | --- |
| From | ``` func inputText(_ string: String!, key keyCode: Int, modifiers flags: Int, client sender: AnyObject!) -> Bool ``` |
| To | ``` func inputText(_ string: String!, key keyCode: Int, modifiers flags: Int, client sender: Any!) -> Bool ``` |

Modified [NSObject.originalString(_: Any!) -> NSAttributedString!](https://developer.apple.com/documentation/objectivec/nsobject/1385400-originalstring)

|  | Declaration |
| --- | --- |
| From | ``` func originalString(_ sender: AnyObject!) -> NSAttributedString! ``` |
| To | ``` func originalString(_ sender: Any!) -> NSAttributedString! ``` |

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
