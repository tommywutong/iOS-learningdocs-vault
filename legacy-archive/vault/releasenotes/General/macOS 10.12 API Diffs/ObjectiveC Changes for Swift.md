---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/ObjectiveC.html
archived_at: '2026-07-18T02:51:31.242317Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# ObjectiveC Changes for Swift

### ObjectiveC

Removed NSZone.init()Removed NSZone.init(nilLiteral: ())Removed objc_method_description.init(name: Selector, types: UnsafeMutablePointer<Int8>)Removed objc_property_attribute_t.init(name: UnsafePointer<Int8>, value: UnsafePointer<Int8>)Removed Selector.init()Removed Selector.init(nilLiteral: ())Removed &&(_: T, _: () -> ObjCBool) -> BoolRemoved autoreleasepool(_: () -> Void)Removed objc_assign_global(_: AnyObject!, _: AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject!Removed objc_assign_ivar(_: AnyObject!, _: AnyObject!, _: Int) -> AnyObject!Removed objc_assign_strongCast(_: AnyObject!, _: AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject!Removed [objc_assign_threadlocal(_: AnyObject!, _: AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject!](https://developer.apple.com/documentation/objectivec/1418937-objc_assign_threadlocal)Removed objc_assign_weak(_: AnyObject!, _: AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject!Removed objc_read_weak(_: AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject!Removed ||(_: T, _: () -> ObjCBool) -> BoolAdded objc_method_description.init(name: Selector!, types: UnsafeMutablePointer<Int8>!)Added objc_property_attribute_t.init(name: UnsafePointer<Int8>!, value: UnsafePointer<Int8>!)Added [ObjCBool.customMirror](https://developer.apple.com/documentation/objectivec/objcbool/1642778-custommirror)Added [Selector.customMirror](https://developer.apple.com/documentation/objectivec/selector/1642780-custommirror)Added [autoreleasepool<Result>(invoking: () throws -> Result) rethrows -> Result](https://developer.apple.com/documentation/objectivec/2299644-autoreleasepool)Added objc_collecting_enabled() -> BoolAdded objc_finalizeOnMainThread(_: Swift.AnyClass!)Added OBJC_NO_GCAdded objc_set_collection_ratio(_: Int)Added objc_set_collection_threshold(_: Int)Added objc_start_collector_thread()Added objc_startCollectorThread()Added [object_setIvarWithStrongDefault(_: Any!, _: Ivar!, _: Any!)](https://developer.apple.com/documentation/objectivec/1642779-object_setivarwithstrongdefault)Added [protocol_copyPropertyList2(_: Protocol!, _: UnsafeMutablePointer<UInt32>!, _: Bool, _: Bool) -> UnsafeMutablePointer<objc_property_t?>!](https://developer.apple.com/documentation/objectivec/1642782-protocol_copypropertylist2)Modified [NSObject](https://developer.apple.com/documentation/objectivec/nsobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSObject : NSObjectProtocol {     class func load()     class func initialize()     init()     class func new() -> Self     class func allocWithZone(_ zone: NSZone) -> Self     class func alloc() -> Self     func finalize()     func copy() -> AnyObject     func mutableCopy() -> AnyObject     class func copyWithZone(_ zone: NSZone) -> AnyObject!     class func mutableCopyWithZone(_ zone: NSZone) -> AnyObject!     class func instancesRespondToSelector(_ aSelector: Selector) -> Bool     class func conformsToProtocol(_ protocol: Protocol) -> Bool     func methodForSelector(_ aSelector: Selector) -> IMP     class func instanceMethodForSelector(_ aSelector: Selector) -> IMP     func doesNotRecognizeSelector(_ aSelector: Selector)     func forwardingTargetForSelector(_ aSelector: Selector) -> AnyObject?     func forwardInvocation(_ anInvocation: NSInvocation!)     func methodSignatureForSelector(_ aSelector: Selector) -> NSMethodSignature!     class func instanceMethodSignatureForSelector(_ aSelector: Selector) -> NSMethodSignature!     func allowsWeakReference() -> Bool     func retainWeakReference() -> Bool     class func isSubclassOfClass(_ aClass: AnyClass) -> Bool     class func resolveClassMethod(_ sel: Selector) -> Bool     class func resolveInstanceMethod(_ sel: Selector) -> Bool     class func hash() -> Int     class func superclass() -> AnyClass?     class func `class`() -> AnyClass!     class func description() -> String     class func debugDescription() -> String } extension NSObject {     func actionProperty() -> String!     func titleForPerson(_ person: ABPerson!, identifier identifier: String!) -> String!     func performActionForPerson(_ person: ABPerson!, identifier identifier: String!)     func shouldEnableActionForPerson(_ person: ABPerson!, identifier identifier: String!) -> Bool } extension NSObject {     func accessibilityAttributeNames() -> [AnyObject]     func accessibilityAttributeValue(_ attribute: String) -> AnyObject?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: AnyObject?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [AnyObject]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: AnyObject?) -> AnyObject?     func accessibilityActionNames() -> [AnyObject]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> AnyObject?     var accessibilityFocusedUIElement: AnyObject? { get }     func accessibilityIndexOfChild(_ child: AnyObject) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [AnyObject]     var accessibilityNotifiesWhenDestroyed: Bool { get } } extension NSObject {     func accessibilitySetOverrideValue(_ value: AnyObject?, forAttribute attribute: String) -> Bool } extension NSObject {     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool } extension NSObject {     func changeColor(_ sender: AnyObject?) } extension NSObject {     func controlTextDidBeginEditing(_ obj: NSNotification)     func controlTextDidEndEditing(_ obj: NSNotification)     func controlTextDidChange(_ obj: NSNotification) } extension NSObject {     func namesOfPromisedFilesDroppedAtDestination(_ dropDestination: NSURL) -> [String]?     func draggingSourceOperationMaskForLocal(_ flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool) } extension NSObject {     func fontManager(_ sender: AnyObject, willIncludeFont fontName: String) -> Bool } extension NSObject {     func changeFont(_ sender: AnyObject?) } extension NSObject {     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int } extension NSObject {     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, toObject observable: AnyObject, withKeyPath keyPath: String, options options: [String : AnyObject]?)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : AnyObject]?     func optionDescriptionsForBinding(_ aBinding: String) -> [NSAttributeDescription] } extension NSObject {     class func setDefaultPlaceholder(_ placeholder: AnyObject?, forMarker marker: AnyObject?, withBinding binding: String)     class func defaultPlaceholderForMarker(_ marker: AnyObject?, withBinding binding: String) -> AnyObject? } extension NSObject {     func objectDidBeginEditing(_ editor: AnyObject)     func objectDidEndEditing(_ editor: AnyObject) } extension NSObject {     func discardEditing()     func commitEditing() -> Bool     func commitEditingWithDelegate(_ delegate: AnyObject?, didCommitSelector didCommitSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func commitEditingAndReturnError() throws } extension NSObject {     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool } extension NSObject {     func awakeFromNib()     func prepareForInterfaceBuilder() } extension NSObject {     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard) } extension NSObject {     func panel(_ sender: AnyObject, isValidFilename filename: String) -> Bool     func panel(_ sender: AnyObject, directoryDidChange path: String)     func panel(_ sender: AnyObject, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> NSComparisonResult     func panel(_ sender: AnyObject, shouldShowFilename filename: String) -> Bool } extension NSObject {     func tableView(_ tableView: NSTableView, writeRows rows: [AnyObject], toPasteboard pboard: NSPasteboard) -> Bool } extension NSObject {     func textStorageWillProcessEditing(_ notification: NSNotification)     func textStorageDidProcessEditing(_ notification: NSNotification) } extension NSObject {     func validateToolbarItem(_ theItem: NSToolbarItem) -> Bool } extension NSObject {     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, fromWindow window: NSWindow) -> Bool } extension NSObject {     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutablePointer<Void>) -> String } extension NSObject {     func workflowControllerWillRun(_ controller: AMWorkflowController)     func workflowControllerWillStop(_ controller: AMWorkflowController)     func workflowControllerDidRun(_ controller: AMWorkflowController)     func workflowControllerDidStop(_ controller: AMWorkflowController)     func workflowController(_ controller: AMWorkflowController, willRunAction action: AMAction)     func workflowController(_ controller: AMWorkflowController, didRunAction action: AMAction)     func workflowController(_ controller: AMWorkflowController, didError error: NSError) } extension NSObject {     func provideImageData(_ data: UnsafeMutablePointer<Void>, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: AnyObject?) } extension NSObject {     func burnProgressPanelWillBegin(_ aNotification: NSNotification!)     func burnProgressPanelDidFinish(_ aNotification: NSNotification!)     func burnProgressPanel(_ theBurnPanel: DRBurnProgressPanel!, burnDidFinish burn: DRBurn!) -> Bool } extension NSObject {     func eraseProgressPanelWillBegin(_ aNotification: NSNotification!)     func eraseProgressPanelDidFinish(_ aNotification: NSNotification!)     func eraseProgressPanel(_ theErasePanel: DREraseProgressPanel!, eraseDidFinish erase: DRErase!) -> Bool } extension NSObject {     func setupPanel(_ aPanel: DRSetupPanel!, deviceCouldBeTarget device: DRDevice!) -> Bool     func setupPanel(_ aPanel: DRSetupPanel!, determineBestDeviceOfA deviceA: DRDevice!, orB device: DRDevice!) -> DRDevice!     func setupPanelDeviceSelectionChanged(_ aNotification: NSNotification!)     func setupPanelShouldHandleMediaReservations(_ aPanel: DRSetupPanel!) -> Bool     func setupPanel(_ aPanel: DRSetupPanel!, deviceContainsSuitableMedia device: DRDevice!, promptString prompt: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool } extension NSObject {     func exceptionHandler(_ sender: NSExceptionHandler!, shouldLogException exception: NSException!, mask aMask: Int) -> Bool     func exceptionHandler(_ sender: NSExceptionHandler!, shouldHandleException exception: NSException!, mask aMask: Int) -> Bool } extension NSObject {     var classForArchiver: AnyClass? { get }     func replacementObjectForArchiver(_ archiver: NSArchiver) -> AnyObject? } extension NSObject {     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverseForRelationshipKey(_ relationshipKey: String) -> String? } extension NSObject {     func attemptRecoveryFromError(_ error: NSError, optionIndex recoveryOptionIndex: Int, delegate delegate: AnyObject?, didRecoverSelector didRecoverSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func attemptRecoveryFromError(_ error: NSError, optionIndex recoveryOptionIndex: Int) -> Bool } extension NSObject {     func fileManager(_ fm: NSFileManager, shouldProceedAfterError errorInfo: [NSObject : AnyObject]) -> Bool     func fileManager(_ fm: NSFileManager, willProcessPath path: String) } extension NSObject {     class func accessInstanceVariablesDirectly() -> Bool     func valueForKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValueForKey(_ key: String) -> NSMutableArray     func mutableOrderedSetValueForKey(_ key: String) -> NSMutableOrderedSet     func mutableSetValueForKey(_ key: String) -> NSMutableSet     func valueForKeyPath(_ keyPath: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValueForKeyPath(_ keyPath: String) -> NSMutableArray     func mutableOrderedSetValueForKeyPath(_ keyPath: String) -> NSMutableOrderedSet     func mutableSetValueForKeyPath(_ keyPath: String) -> NSMutableSet     func valueForUndefinedKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValuesForKeys(_ keys: [String]) -> [String : AnyObject]     func setValuesForKeysWithDictionary(_ keyedValues: [String : AnyObject]) } extension NSObject {     class func useStoredAccessor() -> Bool     func storedValueForKey(_ key: String) -> AnyObject?     func takeStoredValue(_ value: AnyObject?, forKey key: String)     func takeValue(_ value: AnyObject?, forKey key: String)     func takeValue(_ value: AnyObject?, forKeyPath keyPath: String)     func handleQueryWithUnboundKey(_ key: String) -> AnyObject?     func handleTakeValue(_ value: AnyObject?, forUnboundKey key: String)     func unableToSetNilForKey(_ key: String)     func valuesForKeys(_ keys: [AnyObject]) -> [NSObject : AnyObject]     func takeValuesFromDictionary(_ properties: [NSObject : AnyObject]) } extension NSObject {     func observeValueForKeyPath(_ keyPath: String?, ofObject object: AnyObject?, change change: [String : AnyObject]?, context context: UnsafeMutablePointer<Void>) } extension NSObject {     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSObject {     func willChangeValueForKey(_ key: String)     func didChangeValueForKey(_ key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAtIndexes indexes: NSIndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAtIndexes indexes: NSIndexSet, forKey key: String)     func willChangeValueForKey(_ key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, usingObjects objects: Set<NSObject>)     func didChangeValueForKey(_ key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, usingObjects objects: Set<NSObject>) } extension NSObject {     class func keyPathsForValuesAffectingValueForKey(_ key: String) -> Set<String>     class func automaticallyNotifiesObserversForKey(_ key: String) -> Bool     var observationInfo: UnsafeMutablePointer<Void> } extension NSObject {     class func setKeys(_ keys: [AnyObject], triggerChangeNotificationsForDependentKey dependentKey: String) } extension NSObject {     var classForKeyedArchiver: AnyClass? { get }     func replacementObjectForKeyedArchiver(_ archiver: NSKeyedArchiver) -> AnyObject?     class func classFallbacksForKeyedArchiver() -> [String] } extension NSObject {     class func classForKeyedUnarchiver() -> AnyClass } extension NSObject {     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObjectForCoder(_ aCoder: NSCoder) -> AnyObject?     func awakeAfterUsingCoder(_ aDecoder: NSCoder) -> AnyObject? } extension NSObject {     class func poseAsClass(_ aClass: AnyClass) } extension NSObject {     var autoContentAccessingProxy: AnyObject { get } } extension NSObject {     func scriptingValueForSpecifier(_ objectSpecifier: NSScriptObjectSpecifier) -> AnyObject?     var scriptingProperties: [String : AnyObject]?     func copyScriptingValue(_ value: AnyObject, forKey key: String, withProperties properties: [String : AnyObject]) -> AnyObject?     func newScriptingObjectOfClass(_ objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: AnyObject?, properties properties: [String : AnyObject]) -> AnyObject? } extension NSObject {     var classForPortCoder: AnyClass { get }     func replacementObjectForPortCoder(_ coder: NSPortCoder) -> AnyObject? } extension NSObject {     func performSelector(_ aSelector: Selector, withObject anArgument: AnyObject?, afterDelay delay: NSTimeInterval, inModes modes: [String])     func performSelector(_ aSelector: Selector, withObject anArgument: AnyObject?, afterDelay delay: NSTimeInterval)     class func cancelPreviousPerformRequestsWithTarget(_ aTarget: AnyObject, selector aSelector: Selector, object anArgument: AnyObject?)     class func cancelPreviousPerformRequestsWithTarget(_ aTarget: AnyObject) } extension NSObject {     var classCode: FourCharCode { get }     var className: String { get } } extension NSObject {     func valueAtIndex(_ index: Int, inPropertyWithKey key: String) -> AnyObject?     func valueWithName(_ name: String, inPropertyWithKey key: String) -> AnyObject?     func valueWithUniqueID(_ uniqueID: AnyObject, inPropertyWithKey key: String) -> AnyObject?     func insertValue(_ value: AnyObject, atIndex index: Int, inPropertyWithKey key: String)     func removeValueAtIndex(_ index: Int, fromPropertyWithKey key: String)     func replaceValueAtIndex(_ index: Int, inPropertyWithKey key: String, withValue value: AnyObject)     func insertValue(_ value: AnyObject, inPropertyWithKey key: String)     func coerceValue(_ value: AnyObject?, forKey key: String) -> AnyObject? } extension NSObject {     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjectsByEvaluatingObjectSpecifier(_ specifier: NSScriptObjectSpecifier) -> [NSNumber]? } extension NSObject {     func isEqualTo(_ object: AnyObject?) -> Bool     func isLessThanOrEqualTo(_ object: AnyObject?) -> Bool     func isLessThan(_ object: AnyObject?) -> Bool     func isGreaterThanOrEqualTo(_ object: AnyObject?) -> Bool     func isGreaterThan(_ object: AnyObject?) -> Bool     func isNotEqualTo(_ object: AnyObject?) -> Bool     func doesContain(_ object: AnyObject) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool } extension NSObject {     func scriptingIsEqualTo(_ object: AnyObject) -> Bool     func scriptingIsLessThanOrEqualTo(_ object: AnyObject) -> Bool     func scriptingIsLessThan(_ object: AnyObject) -> Bool     func scriptingIsGreaterThanOrEqualTo(_ object: AnyObject) -> Bool     func scriptingIsGreaterThan(_ object: AnyObject) -> Bool     func scriptingBeginsWith(_ object: AnyObject) -> Bool     func scriptingEndsWith(_ object: AnyObject) -> Bool     func scriptingContains(_ object: AnyObject) -> Bool } extension NSObject {     func performSelectorOnMainThread(_ aSelector: Selector, withObject arg: AnyObject?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelectorOnMainThread(_ aSelector: Selector, withObject arg: AnyObject?, waitUntilDone wait: Bool)     func performSelector(_ aSelector: Selector, onThread thr: NSThread, withObject arg: AnyObject?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(_ aSelector: Selector, onThread thr: NSThread, withObject arg: AnyObject?, waitUntilDone wait: Bool)     func performSelectorInBackground(_ aSelector: Selector, withObject arg: AnyObject?) } extension NSObject {     func URL(_ sender: NSURL, resourceDataDidBecomeAvailable newBytes: NSData)     func URLResourceDidFinishLoading(_ sender: NSURL)     func URLResourceDidCancelLoading(_ sender: NSURL)     func URL(_ sender: NSURL, resourceDidFailLoadingWithReason reason: String) } extension NSObject : CustomDebugStringConvertible { } extension NSObject : CustomStringConvertible { } extension NSObject {     func readRSSIForDeviceComplete(_ controller: AnyObject!, device device: IOBluetoothDevice!, info info: UnsafeMutablePointer<BluetoothHCIRSSIInfo>, error error: IOReturn)     func readLinkQualityForDeviceComplete(_ controller: AnyObject!, device device: IOBluetoothDevice!, info info: UnsafeMutablePointer<BluetoothHCILinkQualityInfo>, error error: IOReturn) } extension NSObject {     func registerIncomingDataListener(_ listener: IOBluetoothL2CAPChannelIncomingDataListener!, refCon refCon: UnsafeMutablePointer<Void>) -> IOReturn     func write(_ data: UnsafeMutablePointer<Void>, length length: UInt16) -> IOReturn     class func withL2CAPChannelRef(_ l2capChannelRef: IOBluetoothL2CAPChannelRef!) -> IOBluetoothL2CAPChannel!     func getL2CAPChannelRef() -> Unmanaged<IOBluetoothL2CAPChannelRef>! } extension NSObject {     func fileTransferServicesConnectionComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError)     func fileTransferServicesDisconnectionComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError)     func fileTransferServicesAbortComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError)     func fileTransferServicesRemoveItemComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError, removedItem inItemName: String!)     func fileTransferServicesCreateFolderComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError, folder inFolderName: String!)     func fileTransferServicesPathChangeComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError, finalPath inPath: String!)     func fileTransferServicesRetrieveFolderListingComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError, listing inListing: [AnyObject]!)     func fileTransferServicesFilePreparationComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError)     func fileTransferServicesSendFileProgress(_ inServices: OBEXFileTransferServices!, transferProgress inProgressDescription: [NSObject : AnyObject]!)     func fileTransferServicesSendFileComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError)     func fileTransferServicesCopyRemoteFileProgress(_ inServices: OBEXFileTransferServices!, transferProgress inProgressDescription: [NSObject : AnyObject]!)     func fileTransferServicesCopyRemoteFileComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError) } extension NSObject {     func inputText(_ string: String!, key keyCode: Int, modifiers flags: Int, client sender: AnyObject!) -> Bool     func inputText(_ string: String!, client sender: AnyObject!) -> Bool     func handleEvent(_ event: NSEvent!, client sender: AnyObject!) -> Bool     func didCommandBySelector(_ aSelector: Selector, client sender: AnyObject!) -> Bool     func composedString(_ sender: AnyObject!) -> AnyObject!     func originalString(_ sender: AnyObject!) -> NSAttributedString!     func commitComposition(_ sender: AnyObject!)     func candidates(_ sender: AnyObject!) -> [AnyObject]! } extension NSObject : Equatable, Hashable {     var hashValue: Int { get } } extension NSObject : CVarArgType { } extension NSObject : Equatable, Hashable {     var hashValue: Int { get } } extension NSObject : CVarArgType { } extension NSObject {     func feedDidBeginRefresh(_ feed: PSFeed!)     func feedDidEndRefresh(_ feed: PSFeed!)     func feed(_ feed: PSFeed!, didAddEntries entries: [AnyObject]!)     func feed(_ feed: PSFeed!, didRemoveEntriesWithIdentifiers identifiers: [AnyObject]!)     func feed(_ feed: PSFeed!, didUpdateEntries entries: [AnyObject]!)     func feed(_ feed: PSFeed!, didChangeFlagsInEntries entries: [AnyObject]!)     func enclosure(_ enclosure: PSEnclosure!, downloadStateDidChange state: PSEnclosureDownloadState) } extension NSObject {     func numberOfItemsInImageBrowser(_ aBrowser: IKImageBrowserView!) -> Int     func imageBrowser(_ aBrowser: IKImageBrowserView!, itemAtIndex index: Int) -> AnyObject!     func imageBrowser(_ aBrowser: IKImageBrowserView!, removeItemsAtIndexes indexes: NSIndexSet!)     func imageBrowser(_ aBrowser: IKImageBrowserView!, moveItemsAtIndexes indexes: NSIndexSet!, toIndex destinationIndex: Int) -> Bool     func imageBrowser(_ aBrowser: IKImageBrowserView!, writeItemsAtIndexes itemIndexes: NSIndexSet!, toPasteboard pasteboard: NSPasteboard!) -> Int     func numberOfGroupsInImageBrowser(_ aBrowser: IKImageBrowserView!) -> Int     func imageBrowser(_ aBrowser: IKImageBrowserView!, groupAtIndex index: Int) -> [NSObject : AnyObject]! } extension NSObject {     func imageUID() -> String!     func imageRepresentationType() -> String!     func imageRepresentation() -> AnyObject!     func imageVersion() -> Int     func imageTitle() -> String!     func imageSubtitle() -> String!     func isSelectable() -> Bool } extension NSObject {     func imageBrowserSelectionDidChange(_ aBrowser: IKImageBrowserView!)     func imageBrowser(_ aBrowser: IKImageBrowserView!, cellWasDoubleClickedAtIndex index: Int)     func imageBrowser(_ aBrowser: IKImageBrowserView!, cellWasRightClickedAtIndex index: Int, withEvent event: NSEvent!)     func imageBrowser(_ aBrowser: IKImageBrowserView!, backgroundWasRightClickedWithEvent event: NSEvent!) } extension NSObject {     func saveOptions(_ saveOptions: IKSaveOptions!, shouldShowUTType utType: String!) -> Bool } extension NSObject {     func documentDidUnlock(_ notification: NSNotification!)     func documentDidBeginDocumentFind(_ notification: NSNotification!)     func documentDidEndDocumentFind(_ notification: NSNotification!)     func documentDidBeginPageFind(_ notification: NSNotification!)     func documentDidEndPageFind(_ notification: NSNotification!)     func documentDidFindMatch(_ notification: NSNotification!) } extension NSObject {     func didMatchString(_ instance: PDFSelection!)     func classForPage() -> AnyClass!     func classForAnnotationClass(_ annotationClass: AnyClass!) -> AnyClass! } extension NSObject {     func PDFViewWillChangeScaleFactor(_ sender: PDFView!, toScale scale: CGFloat) -> CGFloat     func PDFViewWillClickOnLink(_ sender: PDFView!, withURL url: NSURL!)     func PDFViewPrintJobTitle(_ sender: PDFView!) -> String!     func PDFViewPerformFind(_ sender: PDFView!)     func PDFViewPerformGoToPage(_ sender: PDFView!)     func PDFViewPerformPrint(_ sender: PDFView!)     func PDFViewOpenPDF(_ sender: PDFView!, forRemoteGoToAction action: PDFActionRemoteGoTo!) } extension NSObject {     func compositionParameterView(_ parameterView: QCCompositionParameterView!, shouldDisplayParameterWithKey portKey: String!, attributes portAttributes: [NSObject : AnyObject]!) -> Bool     func compositionParameterView(_ parameterView: QCCompositionParameterView!, didChangeParameterWithKey portKey: String!) } extension NSObject {     func compositionPickerView(_ pickerView: QCCompositionPickerView!, didSelectComposition composition: QCComposition!)     func compositionPickerViewDidStartAnimating(_ pickerView: QCCompositionPickerView!)     func compositionPickerViewWillStopAnimating(_ pickerView: QCCompositionPickerView!) } extension NSObject {     func quartzFilterManager(_ sender: QuartzFilterManager!, didAddFilter filter: QuartzFilter!)     func quartzFilterManager(_ sender: QuartzFilterManager!, didRemoveFilter filter: QuartzFilter!)     func quartzFilterManager(_ sender: QuartzFilterManager!, didModifyFilter filter: QuartzFilter!)     func quartzFilterManager(_ sender: QuartzFilterManager!, didSelectFilter filter: QuartzFilter!) } extension NSObject {     func acceptsPreviewPanelControl(_ panel: QLPreviewPanel!) -> Bool     func beginPreviewPanelControl(_ panel: QLPreviewPanel!)     func endPreviewPanelControl(_ panel: QLPreviewPanel!) } extension NSObject {     func animationDidStart(_ anim: CAAnimation)     func animationDidStop(_ anim: CAAnimation, finished flag: Bool) } extension NSObject {     func preferredSizeOfLayer(_ layer: CALayer) -> CGSize     func invalidateLayoutOfLayer(_ layer: CALayer)     func layoutSublayersOfLayer(_ layer: CALayer) } extension NSObject {     func displayLayer(_ layer: CALayer)     func drawLayer(_ layer: CALayer, inContext ctx: CGContext)     func actionForLayer(_ layer: CALayer, forKey event: String) -> CAAction? } extension NSObject {     func authorizationViewDidAuthorize(_ view: SFAuthorizationView!)     func authorizationViewDidDeauthorize(_ view: SFAuthorizationView!)     func authorizationViewShouldDeauthorize(_ view: SFAuthorizationView!) -> Int8     func authorizationViewCreatedAuthorization(_ view: SFAuthorizationView!)     func authorizationViewReleasedAuthorization(_ view: SFAuthorizationView!)     func authorizationViewDidHide(_ view: SFAuthorizationView!) } extension NSObject {     func certificatePanelShowHelp(_ sender: SFCertificatePanel!) -> Int8 } extension NSObject {     func chooseIdentityPanelShowHelp(_ sender: SFChooseIdentityPanel!) -> Int8 } extension NSObject {     func webView(_ webView: WebView!, shouldBeginEditingInDOMRange range: DOMRange!) -> Bool     func webView(_ webView: WebView!, shouldEndEditingInDOMRange range: DOMRange!) -> Bool     func webView(_ webView: WebView!, shouldInsertNode node: DOMNode!, replacingDOMRange range: DOMRange!, givenAction action: WebViewInsertAction) -> Bool     func webView(_ webView: WebView!, shouldInsertText text: String!, replacingDOMRange range: DOMRange!, givenAction action: WebViewInsertAction) -> Bool     func webView(_ webView: WebView!, shouldDeleteDOMRange range: DOMRange!) -> Bool     func webView(_ webView: WebView!, shouldChangeSelectedDOMRange currentRange: DOMRange!, toDOMRange proposedRange: DOMRange!, affinity selectionAffinity: NSSelectionAffinity, stillSelecting flag: Bool) -> Bool     func webView(_ webView: WebView!, shouldApplyStyle style: DOMCSSStyleDeclaration!, toElementsInDOMRange range: DOMRange!) -> Bool     func webView(_ webView: WebView!, shouldChangeTypingStyle currentStyle: DOMCSSStyleDeclaration!, toStyle proposedStyle: DOMCSSStyleDeclaration!) -> Bool     func webView(_ webView: WebView!, doCommandBySelector selector: Selector) -> Bool     func webViewDidBeginEditing(_ notification: NSNotification!)     func webViewDidChange(_ notification: NSNotification!)     func webViewDidEndEditing(_ notification: NSNotification!)     func webViewDidChangeTypingStyle(_ notification: NSNotification!)     func webViewDidChangeSelection(_ notification: NSNotification!)     func undoManagerForWebView(_ webView: WebView!) -> NSUndoManager! } extension NSObject {     func webPlugInInitialize()     func webPlugInStart()     func webPlugInStop()     func webPlugInDestroy()     func webPlugInSetIsSelected(_ isSelected: Bool)     var objectForWebScript: AnyObject! { get }     func webPlugInMainResourceDidReceiveResponse(_ response: NSURLResponse!)     func webPlugInMainResourceDidReceiveData(_ data: NSData!)     func webPlugInMainResourceDidFailWithError(_ error: NSError!)     func webPlugInMainResourceDidFinishLoading() } extension NSObject {     func webPlugInContainerLoadRequest(_ request: NSURLRequest!, inFrame target: String!)     func webPlugInContainerShowStatus(_ message: String!)     var webPlugInContainerSelectionColor: NSColor! { get }     var webFrame: WebFrame! { get } } extension NSObject {     class func webScriptNameForSelector(_ selector: Selector) -> String!     class func isSelectorExcludedFromWebScript(_ selector: Selector) -> Bool     class func webScriptNameForKey(_ name: UnsafePointer<Int8>) -> String!     class func isKeyExcludedFromWebScript(_ name: UnsafePointer<Int8>) -> Bool     func invokeUndefinedMethodFromWebScript(_ name: String!, withArguments arguments: [AnyObject]!) -> AnyObject!     func invokeDefaultMethodWithArguments(_ arguments: [AnyObject]!) -> AnyObject!     func finalizeForWebScript() } ``` | CVarArgType, CustomDebugStringConvertible, CustomStringConvertible, Equatable, Hashable, NSObjectProtocol |
| To | ``` class NSObject : NSObjectProtocol {     class func load()     class func initialize()     init()     class func new() -> Self     class func alloc(with zone: NSZone!) -> Self     class func alloc() -> Self     func finalize()     func copy() -> Any     func mutableCopy() -> Any     class func copy(with zone: NSZone!) -> Any!     class func mutableCopy(with zone: NSZone!) -> Any!     class func instancesRespond(to aSelector: Selector!) -> Bool     class func conforms(to protocol: Protocol) -> Bool     func method(for aSelector: Selector!) -> IMP!     class func instanceMethod(for aSelector: Selector!) -> IMP!     func doesNotRecognizeSelector(_ aSelector: Selector!)     func forwardingTarget(for aSelector: Selector!) -> Any?     func forwardInvocation(_ anInvocation: NSInvocation!)     func methodSignature(for aSelector: Selector!) -> NSMethodSignature!     class func instanceMethodSignature(for aSelector: Selector!) -> NSMethodSignature!     func allowsWeakReference() -> Bool     func retainWeakReference() -> Bool     class func isSubclass(of aClass: Swift.AnyClass) -> Bool     class func resolveClassMethod(_ sel: Selector!) -> Bool     class func resolveInstanceMethod(_ sel: Selector!) -> Bool     class func hash() -> Int     class func superclass() -> Swift.AnyClass?     class func `class`() -> Swift.AnyClass!     class func description() -> String     class func debugDescription() -> String } extension NSObject {     func actionProperty() -> String!     func title(for person: ABPerson!, identifier identifier: String!) -> String!     func performAction(for person: ABPerson!, identifier identifier: String!)     func shouldEnableAction(for person: ABPerson!, identifier identifier: String!) -> Bool } extension NSObject {     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get } } extension NSObject {     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool } extension NSObject {     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool } extension NSObject {     func changeColor(_ sender: Any?) } extension NSObject {     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification) } extension NSObject {     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool) } extension NSObject {     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool } extension NSObject {     func changeFont(_ sender: Any?) } extension NSObject {     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int } extension NSObject {     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> Swift.AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription] } extension NSObject {     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any? } extension NSObject {     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any) } extension NSObject {     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws } extension NSObject {     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool } extension NSObject {     func awakeFromNib()     func prepareForInterfaceBuilder() } extension NSObject {     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard) } extension NSObject {     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool } extension NSObject {     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool } extension NSObject {     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification) } extension NSObject {     func validateToolbarItem(_ item: NSToolbarItem) -> Bool } extension NSObject {     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool } extension NSObject {     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String } extension NSObject {     func workflowControllerWillRun(_ controller: AMWorkflowController)     func workflowControllerWillStop(_ controller: AMWorkflowController)     func workflowControllerDidRun(_ controller: AMWorkflowController)     func workflowControllerDidStop(_ controller: AMWorkflowController)     func workflowController(_ controller: AMWorkflowController, willRun action: AMAction)     func workflowController(_ controller: AMWorkflowController, didRun action: AMAction)     func workflowController(_ controller: AMWorkflowController, didError error: Error) } extension NSObject {     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension NSObject {     func burnProgressPanelWillBegin(_ aNotification: Notification!)     func burnProgressPanelDidFinish(_ aNotification: Notification!)     func burnProgressPanel(_ theBurnPanel: DRBurnProgressPanel!, burnDidFinish burn: DRBurn!) -> Bool } extension NSObject {     func eraseProgressPanelWillBegin(_ aNotification: Notification!)     func eraseProgressPanelDidFinish(_ aNotification: Notification!)     func eraseProgressPanel(_ theErasePanel: DREraseProgressPanel!, eraseDidFinish erase: DRErase!) -> Bool } extension NSObject {     func setupPanel(_ aPanel: DRSetupPanel!, deviceCouldBeTarget device: DRDevice!) -> Bool     func setupPanel(_ aPanel: DRSetupPanel!, determineBestDeviceOfA deviceA: DRDevice!, orB device: DRDevice!) -> DRDevice!     func setupPanelDeviceSelectionChanged(_ aNotification: Notification!)     func setupPanelShouldHandleMediaReservations(_ aPanel: DRSetupPanel!) -> Bool     func setupPanel(_ aPanel: DRSetupPanel!, deviceContainsSuitableMedia device: DRDevice!, promptString prompt: AutoreleasingUnsafeMutablePointer<NSString?>!) -> Bool } extension NSObject {     func exceptionHandler(_ sender: NSExceptionHandler!, shouldLogException exception: NSException!, mask aMask: Int) -> Bool     func exceptionHandler(_ sender: NSExceptionHandler!, shouldHandle exception: NSException!, mask aMask: Int) -> Bool } extension NSObject {     var classForArchiver: Swift.AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any? } extension NSObject {     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String? } extension NSObject {     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool } extension NSObject {     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String) } extension NSObject {     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any]) } extension NSObject {     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any]) } extension NSObject {     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?) } extension NSObject {     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSObject {     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>) } extension NSObject {     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer? } extension NSObject {     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String) } extension NSObject {     var classForKeyedArchiver: Swift.AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String] } extension NSObject {     class func classForKeyedUnarchiver() -> Swift.AnyClass } extension NSObject {     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: Swift.AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSObject {     class func pose(as aClass: Swift.AnyClass) } extension NSObject {     var autoContentAccessingProxy: Any { get } } extension NSObject {     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: Swift.AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any? } extension NSObject {     var classForPortCoder: Swift.AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any? } extension NSObject {     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any) } extension NSObject {     var classCode: FourCharCode { get }     var className: String { get } } extension NSObject {     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any? } extension NSObject {     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]? } extension NSObject {     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool } extension NSObject {     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool } extension NSObject {     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?) } extension NSObject : CustomStringConvertible { } extension NSObject : CustomDebugStringConvertible { } extension NSObject {     func readRSSI(forDeviceComplete controller: Any!, device device: IOBluetoothDevice!, info info: UnsafeMutablePointer<BluetoothHCIRSSIInfo>!, error error: IOReturn)     func readLinkQuality(forDeviceComplete controller: Any!, device device: IOBluetoothDevice!, info info: UnsafeMutablePointer<BluetoothHCILinkQualityInfo>!, error error: IOReturn) } extension NSObject {     func registerIncomingDataListener(_ listener: IOBluetooth.IOBluetoothL2CAPChannelIncomingDataListener!, refCon refCon: UnsafeMutableRawPointer!) -> IOReturn     func write(_ data: UnsafeMutableRawPointer!, length length: UInt16) -> IOReturn     class func withL2CAPChannelRef(_ l2capChannelRef: IOBluetoothL2CAPChannelRef!) -> IOBluetoothL2CAPChannel!     func getL2CAPChannelRef() -> Unmanaged<IOBluetoothL2CAPChannelRef>! } extension NSObject {     func fileTransferServicesConnectionComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError)     func fileTransferServicesDisconnectionComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError)     func fileTransferServicesAbortComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError)     func fileTransferServicesRemoveItemComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError, removedItem inItemName: String!)     func fileTransferServicesCreateFolderComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError, folder inFolderName: String!)     func fileTransferServicesPathChangeComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError, finalPath inPath: String!)     func fileTransferServicesRetrieveFolderListingComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError, listing inListing: [Any]!)     func fileTransferServicesFilePreparationComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError)     func fileTransferServicesSendFileProgress(_ inServices: OBEXFileTransferServices!, transferProgress inProgressDescription: [AnyHashable : Any]!)     func fileTransferServicesSendFileComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError)     func fileTransferServicesCopyRemoteFileProgress(_ inServices: OBEXFileTransferServices!, transferProgress inProgressDescription: [AnyHashable : Any]!)     func fileTransferServicesCopyRemoteFileComplete(_ inServices: OBEXFileTransferServices!, error inError: OBEXError) } extension NSObject {     func inputText(_ string: String!, key keyCode: Int, modifiers flags: Int, client sender: Any!) -> Bool     func inputText(_ string: String!, client sender: Any!) -> Bool     func handle(_ event: NSEvent!, client sender: Any!) -> Bool     func didCommand(by aSelector: Selector!, client sender: Any!) -> Bool     func composedString(_ sender: Any!) -> Any!     func originalString(_ sender: Any!) -> NSAttributedString!     func commitComposition(_ sender: Any!)     func candidates(_ sender: Any!) -> [Any]! } extension NSObject : CVarArg { } extension NSObject : Equatable, Hashable {     var hashValue: Int { get } } extension NSObject : Equatable, Hashable {     var hashValue: Int { get } } extension NSObject : CVarArg { } extension NSObject {     func numberOfItems(inImageBrowser aBrowser: IKImageBrowserView!) -> Int     func imageBrowser(_ aBrowser: IKImageBrowserView!, itemAt index: Int) -> Any!     func imageBrowser(_ aBrowser: IKImageBrowserView!, removeItemsAt indexes: IndexSet!)     func imageBrowser(_ aBrowser: IKImageBrowserView!, moveItemsAt indexes: IndexSet!, to destinationIndex: Int) -> Bool     func imageBrowser(_ aBrowser: IKImageBrowserView!, writeItemsAt itemIndexes: IndexSet!, to pasteboard: NSPasteboard!) -> Int     func numberOfGroups(inImageBrowser aBrowser: IKImageBrowserView!) -> Int     func imageBrowser(_ aBrowser: IKImageBrowserView!, groupAt index: Int) -> [AnyHashable : Any]! } extension NSObject {     func imageUID() -> String!     func imageRepresentationType() -> String!     func imageRepresentation() -> Any!     func imageVersion() -> Int     func imageTitle() -> String!     func imageSubtitle() -> String!     var isSelectable: Bool { get } } extension NSObject {     func imageBrowserSelectionDidChange(_ aBrowser: IKImageBrowserView!)     func imageBrowser(_ aBrowser: IKImageBrowserView!, cellWasDoubleClickedAt index: Int)     func imageBrowser(_ aBrowser: IKImageBrowserView!, cellWasRightClickedAt index: Int, with event: NSEvent!)     func imageBrowser(_ aBrowser: IKImageBrowserView!, backgroundWasRightClickedWith event: NSEvent!) } extension NSObject {     func saveOptions(_ saveOptions: IKSaveOptions!, shouldShowUTType utType: String!) -> Bool } extension NSObject {     func documentDidUnlock(_ notification: Notification)     func documentDidBeginDocumentFind(_ notification: Notification)     func documentDidEndDocumentFind(_ notification: Notification)     func documentDidBeginPageFind(_ notification: Notification)     func documentDidEndPageFind(_ notification: Notification)     func documentDidFindMatch(_ notification: Notification) } extension NSObject {     func didMatchString(_ instance: PDFSelection)     func classForPage() -> Swift.AnyClass     func `class`(forAnnotationClass annotationClass: Swift.AnyClass) -> Swift.AnyClass } extension NSObject {     func compositionParameterView(_ parameterView: QCCompositionParameterView!, shouldDisplayParameterWithKey portKey: String!, attributes portAttributes: [AnyHashable : Any]! = [:]) -> Bool     func compositionParameterView(_ parameterView: QCCompositionParameterView!, didChangeParameterWithKey portKey: String!) } extension NSObject {     func compositionPickerView(_ pickerView: QCCompositionPickerView!, didSelect composition: QCComposition!)     func compositionPickerViewDidStartAnimating(_ pickerView: QCCompositionPickerView!)     func compositionPickerViewWillStopAnimating(_ pickerView: QCCompositionPickerView!) } extension NSObject {     func quartzFilterManager(_ sender: QuartzFilterManager!, didAdd filter: QuartzFilter!)     func quartzFilterManager(_ sender: QuartzFilterManager!, didRemove filter: QuartzFilter!)     func quartzFilterManager(_ sender: QuartzFilterManager!, didModifyFilter filter: QuartzFilter!)     func quartzFilterManager(_ sender: QuartzFilterManager!, didSelect filter: QuartzFilter!) } extension NSObject {     func acceptsPreviewPanelControl(_ panel: QLPreviewPanel!) -> Bool     func beginPreviewPanelControl(_ panel: QLPreviewPanel!)     func endPreviewPanelControl(_ panel: QLPreviewPanel!) } extension NSObject {     func authorizationViewDidAuthorize(_ view: SFAuthorizationView!)     func authorizationViewDidDeauthorize(_ view: SFAuthorizationView!)     func authorizationViewShouldDeauthorize(_ view: SFAuthorizationView!) -> Int8     func authorizationViewCreatedAuthorization(_ view: SFAuthorizationView!)     func authorizationViewReleasedAuthorization(_ view: SFAuthorizationView!)     func authorizationViewDidHide(_ view: SFAuthorizationView!) } extension NSObject {     func certificatePanelShowHelp(_ sender: SFCertificatePanel!) -> Int8 } extension NSObject {     func chooseIdentityPanelShowHelp(_ sender: SFChooseIdentityPanel!) -> Int8 } extension NSObject {     func webPlugInInitialize()     func webPlugInStart()     func webPlugInStop()     func webPlugInDestroy()     func webPlugInSetIsSelected(_ isSelected: Bool)     var objectForWebScript: Any! { get }     func webPlugInMainResourceDidReceive(_ response: URLResponse!)     func webPlugInMainResourceDidReceive(_ data: Data!)     func webPlugInMainResourceDidFailWithError(_ error: Error!)     func webPlugInMainResourceDidFinishLoading() } extension NSObject {     func webPlugInContainerLoad(_ request: URLRequest!, inFrame target: String!)     func webPlugInContainerShowStatus(_ message: String!)     var webPlugInContainerSelectionColor: NSColor! { get }     var webFrame: WebFrame! { get } } extension NSObject {     class func webScriptName(for selector: Selector!) -> String!     class func isSelectorExcluded(fromWebScript selector: Selector!) -> Bool     class func webScriptName(forKey name: UnsafePointer<Int8>!) -> String!     class func isKeyExcluded(fromWebScript name: UnsafePointer<Int8>!) -> Bool     func invokeUndefinedMethod(fromWebScript name: String!, withArguments arguments: [Any]!) -> Any!     func invokeDefaultMethod(withArguments arguments: [Any]!) -> Any!     func finalizeForWebScript() } ``` | CVarArg, CustomDebugStringConvertible, CustomStringConvertible, Equatable, Hashable, NSObjectProtocol |

Modified [NSObject.conforms(to: Protocol) -> Bool [class]](https://developer.apple.com/documentation/objectivec/nsobject/1418893-conforms)

|  | Declaration |
| --- | --- |
| From | ``` class func conformsToProtocol(_ protocol: Protocol) -> Bool ``` |
| To | ``` class func conforms(to protocol: Protocol) -> Bool ``` |

Modified [NSObject.copy() -> Any](https://developer.apple.com/documentation/objectivec/nsobject/1418807-copy)

|  | Declaration |
| --- | --- |
| From | ``` func copy() -> AnyObject ``` |
| To | ``` func copy() -> Any ``` |

Modified [NSObject.doesNotRecognizeSelector(_: Selector!)](https://developer.apple.com/documentation/objectivec/nsobject/1418637-doesnotrecognizeselector)

|  | Declaration |
| --- | --- |
| From | ``` func doesNotRecognizeSelector(_ aSelector: Selector) ``` |
| To | ``` func doesNotRecognizeSelector(_ aSelector: Selector!) ``` |

Modified [NSObject.finalize()](https://developer.apple.com/documentation/objectivec/nsobject/1418513-finalize)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NSObject.forwardingTarget(for: Selector!) -> Any?](https://developer.apple.com/documentation/objectivec/nsobject/1418855-forwardingtarget)

|  | Declaration |
| --- | --- |
| From | ``` func forwardingTargetForSelector(_ aSelector: Selector) -> AnyObject? ``` |
| To | ``` func forwardingTarget(for aSelector: Selector!) -> Any? ``` |

Modified [NSObject.instanceMethod(for: Selector!) -> IMP! [class]](https://developer.apple.com/documentation/objectivec/nsobject/1418713-instancemethod)

|  | Declaration |
| --- | --- |
| From | ``` class func instanceMethodForSelector(_ aSelector: Selector) -> IMP ``` |
| To | ``` class func instanceMethod(for aSelector: Selector!) -> IMP! ``` |

Modified [NSObject.instancesRespond(to: Selector!) -> Bool [class]](https://developer.apple.com/documentation/objectivec/nsobject/1418555-instancesrespond)

|  | Declaration |
| --- | --- |
| From | ``` class func instancesRespondToSelector(_ aSelector: Selector) -> Bool ``` |
| To | ``` class func instancesRespond(to aSelector: Selector!) -> Bool ``` |

Modified [NSObject.isSubclass(of: Swift.AnyClass) -> Bool [class]](https://developer.apple.com/documentation/objectivec/nsobject/1418669-issubclassofclass)

|  | Declaration |
| --- | --- |
| From | ``` class func isSubclassOfClass(_ aClass: AnyClass) -> Bool ``` |
| To | ``` class func isSubclass(of aClass: Swift.AnyClass) -> Bool ``` |

Modified [NSObject.method(for: Selector!) -> IMP!](https://developer.apple.com/documentation/objectivec/nsobject/1418863-method)

|  | Declaration |
| --- | --- |
| From | ``` func methodForSelector(_ aSelector: Selector) -> IMP ``` |
| To | ``` func method(for aSelector: Selector!) -> IMP! ``` |

Modified [NSObject.mutableCopy() -> Any](https://developer.apple.com/documentation/objectivec/nsobject/1418978-mutablecopy)

|  | Declaration |
| --- | --- |
| From | ``` func mutableCopy() -> AnyObject ``` |
| To | ``` func mutableCopy() -> Any ``` |

Modified [NSObject.resolveClassMethod(_: Selector!) -> Bool [class]](https://developer.apple.com/documentation/objectivec/nsobject/1418889-resolveclassmethod)

|  | Declaration |
| --- | --- |
| From | ``` class func resolveClassMethod(_ sel: Selector) -> Bool ``` |
| To | ``` class func resolveClassMethod(_ sel: Selector!) -> Bool ``` |

Modified [NSObject.resolveInstanceMethod(_: Selector!) -> Bool [class]](https://developer.apple.com/documentation/objectivec/nsobject/1418500-resolveinstancemethod)

|  | Declaration |
| --- | --- |
| From | ``` class func resolveInstanceMethod(_ sel: Selector) -> Bool ``` |
| To | ``` class func resolveInstanceMethod(_ sel: Selector!) -> Bool ``` |

Modified [NSObject.superclass() -> Swift.AnyClass? [class]](https://developer.apple.com/documentation/objectivec/nsobject/1418803-superclass)

|  | Declaration |
| --- | --- |
| From | ``` class func superclass() -> AnyClass? ``` |
| To | ``` class func superclass() -> Swift.AnyClass? ``` |

Modified [NSObjectProtocol](https://developer.apple.com/documentation/objectivec/nsobjectprotocol)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSObjectProtocol {     func isEqual(_ object: AnyObject?) -> Bool     var hash: Int { get }     var superclass: AnyClass? { get }     func `class`() -> AnyClass!     func `self`() -> Self     func performSelector(_ aSelector: Selector) -> Unmanaged<AnyObject>!     func performSelector(_ aSelector: Selector, withObject object: AnyObject!) -> Unmanaged<AnyObject>!     func performSelector(_ aSelector: Selector, withObject object1: AnyObject!, withObject object2: AnyObject!) -> Unmanaged<AnyObject>!     func isProxy() -> Bool     func isKindOfClass(_ aClass: AnyClass) -> Bool     func isMemberOfClass(_ aClass: AnyClass) -> Bool     func conformsToProtocol(_ aProtocol: Protocol) -> Bool     func respondsToSelector(_ aSelector: Selector) -> Bool     func retain() -> Self!     func release()     func autorelease() -> Self!     func retainCount() -> Int     func zone() -> NSZone     var description: String { get }     optional var debugDescription: String { get } } ``` |
| To | ``` protocol NSObjectProtocol {     func isEqual(_ object: Any?) -> Bool     var hash: Int { get }     var superclass: Swift.AnyClass? { get }     func `class`() -> Swift.AnyClass!     func `self`() -> Self     func perform(_ aSelector: Selector!) -> Unmanaged<AnyObject>!     func perform(_ aSelector: Selector!, with object: Any!) -> Unmanaged<AnyObject>!     func perform(_ aSelector: Selector!, with object1: Any!, with object2: Any!) -> Unmanaged<AnyObject>!     func isProxy() -> Bool     func isKind(of aClass: Swift.AnyClass) -> Bool     func isMember(of aClass: Swift.AnyClass) -> Bool     func conforms(to aProtocol: Protocol) -> Bool     func responds(to aSelector: Selector!) -> Bool     func retain() -> Self!     func release()     func autorelease() -> Self!     func retainCount() -> Int     func zone() -> NSZone!     var description: String { get }     optional var debugDescription: String { get } } ``` |

Modified [NSObjectProtocol.conforms(to: Protocol) -> Bool](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418515-conformstoprotocol)

|  | Declaration |
| --- | --- |
| From | ``` func conformsToProtocol(_ aProtocol: Protocol) -> Bool ``` |
| To | ``` func conforms(to aProtocol: Protocol) -> Bool ``` |

Modified [NSObjectProtocol.isEqual(_: Any?) -> Bool](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/1418795-isequal)

|  | Declaration |
| --- | --- |
| From | ``` func isEqual(_ object: AnyObject?) -> Bool ``` |
| To | ``` func isEqual(_ object: Any?) -> Bool ``` |

Modified [NSObjectProtocol.isKind(of: Swift.AnyClass) -> Bool](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/1418511-iskind)

|  | Declaration |
| --- | --- |
| From | ``` func isKindOfClass(_ aClass: AnyClass) -> Bool ``` |
| To | ``` func isKind(of aClass: Swift.AnyClass) -> Bool ``` |

Modified [NSObjectProtocol.isMember(of: Swift.AnyClass) -> Bool](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418766-ismemberofclass)

|  | Declaration |
| --- | --- |
| From | ``` func isMemberOfClass(_ aClass: AnyClass) -> Bool ``` |
| To | ``` func isMember(of aClass: Swift.AnyClass) -> Bool ``` |

Modified [NSObjectProtocol.perform(_: Selector!) -> Unmanaged<AnyObject>!](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/1418867-perform)

|  | Declaration |
| --- | --- |
| From | ``` func performSelector(_ aSelector: Selector) -> Unmanaged<AnyObject>! ``` |
| To | ``` func perform(_ aSelector: Selector!) -> Unmanaged<AnyObject>! ``` |

Modified [NSObjectProtocol.perform(_: Selector!, with: Any!) -> Unmanaged<AnyObject>!](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/1418764-perform)

|  | Declaration |
| --- | --- |
| From | ``` func performSelector(_ aSelector: Selector, withObject object: AnyObject!) -> Unmanaged<AnyObject>! ``` |
| To | ``` func perform(_ aSelector: Selector!, with object: Any!) -> Unmanaged<AnyObject>! ``` |

Modified [NSObjectProtocol.perform(_: Selector!, with: Any!, with: Any!) -> Unmanaged<AnyObject>!](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418667-performselector)

|  | Declaration |
| --- | --- |
| From | ``` func performSelector(_ aSelector: Selector, withObject object1: AnyObject!, withObject object2: AnyObject!) -> Unmanaged<AnyObject>! ``` |
| To | ``` func perform(_ aSelector: Selector!, with object1: Any!, with object2: Any!) -> Unmanaged<AnyObject>! ``` |

Modified [NSObjectProtocol.responds(to: Selector!) -> Bool](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/1418583-responds)

|  | Declaration |
| --- | --- |
| From | ``` func respondsToSelector(_ aSelector: Selector) -> Bool ``` |
| To | ``` func responds(to aSelector: Selector!) -> Bool ``` |

Modified [NSObjectProtocol.superclass](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/1418793-superclass)

|  | Declaration |
| --- | --- |
| From | ``` var superclass: AnyClass? { get } ``` |
| To | ``` var superclass: Swift.AnyClass? { get } ``` |

Modified [NSZone [struct]](https://developer.apple.com/documentation/objectivec/nszone)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSZone : NilLiteralConvertible {     init()     init(nilLiteral nilLiteral: ()) } ``` | NilLiteralConvertible |
| To | ``` struct NSZone { } ``` | -- |

Modified [objc_method_description [struct]](https://developer.apple.com/documentation/objectivec/objc_method_description)

|  | Declaration |
| --- | --- |
| From | ``` struct objc_method_description {     var name: Selector     var types: UnsafeMutablePointer<Int8>     init()     init(name name: Selector, types types: UnsafeMutablePointer<Int8>) } ``` |
| To | ``` struct objc_method_description {     var name: Selector!     var types: UnsafeMutablePointer<Int8>!     init()     init(name name: Selector!, types types: UnsafeMutablePointer<Int8>!) } ``` |

Modified [objc_method_description.name](https://developer.apple.com/documentation/objectivec/objc_method_description/1418493-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: Selector ``` |
| To | ``` var name: Selector! ``` |

Modified [objc_method_description.types](https://developer.apple.com/documentation/objectivec/objc_method_description/1418665-types)

|  | Declaration |
| --- | --- |
| From | ``` var types: UnsafeMutablePointer<Int8> ``` |
| To | ``` var types: UnsafeMutablePointer<Int8>! ``` |

Modified [objc_object [struct]](https://developer.apple.com/documentation/objectivec/id)

|  | Declaration |
| --- | --- |
| From | ``` struct objc_object {     var isa: AnyClass!     init()     init(isa isa: AnyClass!) } ``` |
| To | ``` struct objc_object {     var isa: Swift.AnyClass!     init()     init(isa isa: Swift.AnyClass!) } ``` |

Modified objc_object.init(isa: Swift.AnyClass!)

|  | Declaration |
| --- | --- |
| From | ``` init(isa isa: AnyClass!) ``` |
| To | ``` init(isa isa: Swift.AnyClass!) ``` |

Modified [objc_object.isa](https://developer.apple.com/documentation/objectivec/objc_object/1418809-isa)

|  | Declaration |
| --- | --- |
| From | ``` var isa: AnyClass! ``` |
| To | ``` var isa: Swift.AnyClass! ``` |

Modified [objc_property_attribute_t [struct]](https://developer.apple.com/documentation/objectivec/objc_property_attribute_t)

|  | Declaration |
| --- | --- |
| From | ``` struct objc_property_attribute_t {     var name: UnsafePointer<Int8>     var value: UnsafePointer<Int8>     init()     init(name name: UnsafePointer<Int8>, value value: UnsafePointer<Int8>) } ``` |
| To | ``` struct objc_property_attribute_t {     var name: UnsafePointer<Int8>!     var value: UnsafePointer<Int8>!     init()     init(name name: UnsafePointer<Int8>!, value value: UnsafePointer<Int8>!) } ``` |

Modified [objc_property_attribute_t.name](https://developer.apple.com/documentation/objectivec/objc_property_attribute_t/1418734-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: UnsafePointer<Int8> ``` |
| To | ``` var name: UnsafePointer<Int8>! ``` |

Modified [objc_property_attribute_t.value](https://developer.apple.com/documentation/objectivec/objc_property_attribute_t/1418797-value)

|  | Declaration |
| --- | --- |
| From | ``` var value: UnsafePointer<Int8> ``` |
| To | ``` var value: UnsafePointer<Int8>! ``` |

Modified [objc_super [struct]](https://developer.apple.com/documentation/objectivec/objc_super)

|  | Declaration |
| --- | --- |
| From | ``` struct objc_super {     var receiver: Unmanaged<AnyObject>!     var super_class: AnyClass!     init()     init(receiver receiver: Unmanaged<AnyObject>!, super_class super_class: AnyClass!) } ``` |
| To | ``` struct objc_super {     var receiver: Unmanaged<AnyObject>!     var super_class: Swift.AnyClass!     init()     init(receiver receiver: Unmanaged<AnyObject>!, super_class super_class: Swift.AnyClass!) } ``` |

Modified objc_super.init(receiver: Unmanaged<AnyObject>!, super_class: Swift.AnyClass!)

|  | Declaration |
| --- | --- |
| From | ``` init(receiver receiver: Unmanaged<AnyObject>!, super_class super_class: AnyClass!) ``` |
| To | ``` init(receiver receiver: Unmanaged<AnyObject>!, super_class super_class: Swift.AnyClass!) ``` |

Modified [objc_super.super_class](https://developer.apple.com/documentation/objectivec/objc_super/1418775-super_class)

|  | Declaration |
| --- | --- |
| From | ``` var super_class: AnyClass! ``` |
| To | ``` var super_class: Swift.AnyClass! ``` |

Modified [ObjCBool [struct]](https://developer.apple.com/documentation/objectivec/objcbool)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ObjCBool : BooleanType, BooleanLiteralConvertible {     init(_ value: Bool)     var boolValue: Bool { get }     init(booleanLiteral value: Bool) } extension ObjCBool : _Reflectable { } extension ObjCBool : CustomStringConvertible {     var description: String { get } } ``` | BooleanLiteralConvertible, BooleanType, CustomStringConvertible |
| To | ``` struct ObjCBool : ExpressibleByBooleanLiteral {     init(_ value: Bool)     var boolValue: Bool { get }     init(booleanLiteral value: Bool) } extension ObjCBool : CustomReflectable {     var customMirror: Mirror { get } } extension ObjCBool : CustomStringConvertible {     var description: String { get } } ``` | CustomReflectable, CustomStringConvertible, ExpressibleByBooleanLiteral |

Modified [Selector [struct]](https://developer.apple.com/documentation/objectivec/selector)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Selector : StringLiteralConvertible, NilLiteralConvertible {     init(_ str: String)     init(unicodeScalarLiteral value: String)     init(extendedGraphemeClusterLiteral value: String)     init(stringLiteral value: String)     init()     init(nilLiteral nilLiteral: ()) } extension Selector : Equatable, Hashable {     var hashValue: Int { get } } extension Selector : CustomStringConvertible {     var description: String { get } } extension Selector : _Reflectable { } ``` | CustomStringConvertible, Equatable, Hashable, NilLiteralConvertible, StringLiteralConvertible |
| To | ``` struct Selector : ExpressibleByStringLiteral {     init(_ str: String)     init(unicodeScalarLiteral value: String)     init(extendedGraphemeClusterLiteral value: String)     init(stringLiteral value: String) } extension Selector : CustomStringConvertible {     var description: String { get } } extension Selector : CustomReflectable {     var customMirror: Mirror { get } } extension Selector : Equatable, Hashable {     var hashValue: Int { get } } ``` | CustomReflectable, CustomStringConvertible, Equatable, ExpressibleByStringLiteral, Hashable |

Modified ==(_: Selector, _: Selector) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ==(_ lhs: Selector, _ rhs: Selector) -> Bool ``` |
| To | ``` func ==(_ lhs: Selector, _ rhs: Selector) -> Bool ``` |

Modified ==(_: NSObject, _: NSObject) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ==(_ lhs: NSObject, _ rhs: NSObject) -> Bool ``` |
| To | ``` func ==(_ lhs: NSObject, _ rhs: NSObject) -> Bool ``` |

Modified [Category](https://developer.apple.com/documentation/objectivec/category)

|  | Declaration |
| --- | --- |
| From | ``` typealias Category = COpaquePointer ``` |
| To | ``` typealias Category = OpaquePointer ``` |

Modified [class_addIvar(_: Swift.AnyClass!, _: UnsafePointer<Int8>!, _: Int, _: UInt8, _: UnsafePointer<Int8>!) -> Bool](https://developer.apple.com/documentation/objectivec/1418756-class_addivar)

|  | Declaration |
| --- | --- |
| From | ``` func class_addIvar(_ cls: AnyClass!, _ name: UnsafePointer<Int8>, _ size: Int, _ alignment: UInt8, _ types: UnsafePointer<Int8>) -> Bool ``` |
| To | ``` func class_addIvar(_ cls: Swift.AnyClass!, _ name: UnsafePointer<Int8>!, _ size: Int, _ alignment: UInt8, _ types: UnsafePointer<Int8>!) -> Bool ``` |

Modified [class_addMethod(_: Swift.AnyClass!, _: Selector!, _: IMP!, _: UnsafePointer<Int8>!) -> Bool](https://developer.apple.com/documentation/objectivec/1418901-class_addmethod)

|  | Declaration |
| --- | --- |
| From | ``` func class_addMethod(_ cls: AnyClass!, _ name: Selector, _ imp: IMP, _ types: UnsafePointer<Int8>) -> Bool ``` |
| To | ``` func class_addMethod(_ cls: Swift.AnyClass!, _ name: Selector!, _ imp: IMP!, _ types: UnsafePointer<Int8>!) -> Bool ``` |

Modified [class_addProperty(_: Swift.AnyClass!, _: UnsafePointer<Int8>!, _: UnsafePointer<objc_property_attribute_t>!, _: UInt32) -> Bool](https://developer.apple.com/documentation/objectivec/1418946-class_addproperty)

|  | Declaration |
| --- | --- |
| From | ``` func class_addProperty(_ cls: AnyClass!, _ name: UnsafePointer<Int8>, _ attributes: UnsafePointer<objc_property_attribute_t>, _ attributeCount: UInt32) -> Bool ``` |
| To | ``` func class_addProperty(_ cls: Swift.AnyClass!, _ name: UnsafePointer<Int8>!, _ attributes: UnsafePointer<objc_property_attribute_t>!, _ attributeCount: UInt32) -> Bool ``` |

Modified [class_addProtocol(_: Swift.AnyClass!, _: Protocol!) -> Bool](https://developer.apple.com/documentation/objectivec/1418773-class_addprotocol)

|  | Declaration |
| --- | --- |
| From | ``` func class_addProtocol(_ cls: AnyClass!, _ protocol: Protocol!) -> Bool ``` |
| To | ``` func class_addProtocol(_ cls: Swift.AnyClass!, _ protocol: Protocol!) -> Bool ``` |

Modified [class_conformsToProtocol(_: Swift.AnyClass!, _: Protocol!) -> Bool](https://developer.apple.com/documentation/objectivec/1418685-class_conformstoprotocol)

|  | Declaration |
| --- | --- |
| From | ``` func class_conformsToProtocol(_ cls: AnyClass!, _ protocol: Protocol!) -> Bool ``` |
| To | ``` func class_conformsToProtocol(_ cls: Swift.AnyClass!, _ protocol: Protocol!) -> Bool ``` |

Modified [class_copyIvarList(_: Swift.AnyClass!, _: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<Ivar?>!](https://developer.apple.com/documentation/objectivec/1418910-class_copyivarlist)

|  | Declaration |
| --- | --- |
| From | ``` func class_copyIvarList(_ cls: AnyClass!, _ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<Ivar> ``` |
| To | ``` func class_copyIvarList(_ cls: Swift.AnyClass!, _ outCount: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<Ivar?>! ``` |

Modified [class_copyMethodList(_: Swift.AnyClass!, _: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<Method?>!](https://developer.apple.com/documentation/objectivec/1418490-class_copymethodlist)

|  | Declaration |
| --- | --- |
| From | ``` func class_copyMethodList(_ cls: AnyClass!, _ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<Method> ``` |
| To | ``` func class_copyMethodList(_ cls: Swift.AnyClass!, _ outCount: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<Method?>! ``` |

Modified [class_copyPropertyList(_: Swift.AnyClass!, _: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<objc_property_t?>!](https://developer.apple.com/documentation/objectivec/1418553-class_copypropertylist)

|  | Declaration |
| --- | --- |
| From | ``` func class_copyPropertyList(_ cls: AnyClass!, _ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_property_t> ``` |
| To | ``` func class_copyPropertyList(_ cls: Swift.AnyClass!, _ outCount: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<objc_property_t?>! ``` |

Modified [class_copyProtocolList(_: Swift.AnyClass!, _: UnsafeMutablePointer<UInt32>!) -> AutoreleasingUnsafeMutablePointer<Protocol?>!](https://developer.apple.com/documentation/objectivec/1418883-class_copyprotocollist)

|  | Declaration |
| --- | --- |
| From | ``` func class_copyProtocolList(_ cls: AnyClass!, _ outCount: UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<Protocol?> ``` |
| To | ``` func class_copyProtocolList(_ cls: Swift.AnyClass!, _ outCount: UnsafeMutablePointer<UInt32>!) -> AutoreleasingUnsafeMutablePointer<Protocol?>! ``` |

Modified [class_getClassMethod(_: Swift.AnyClass!, _: Selector!) -> Method!](https://developer.apple.com/documentation/objectivec/1418887-class_getclassmethod)

|  | Declaration |
| --- | --- |
| From | ``` func class_getClassMethod(_ cls: AnyClass!, _ name: Selector) -> Method ``` |
| To | ``` func class_getClassMethod(_ cls: Swift.AnyClass!, _ name: Selector!) -> Method! ``` |

Modified [class_getClassVariable(_: Swift.AnyClass!, _: UnsafePointer<Int8>!) -> Ivar!](https://developer.apple.com/documentation/objectivec/1418487-class_getclassvariable)

|  | Declaration |
| --- | --- |
| From | ``` func class_getClassVariable(_ cls: AnyClass!, _ name: UnsafePointer<Int8>) -> Ivar ``` |
| To | ``` func class_getClassVariable(_ cls: Swift.AnyClass!, _ name: UnsafePointer<Int8>!) -> Ivar! ``` |

Modified [class_getImageName(_: Swift.AnyClass!) -> UnsafePointer<Int8>!](https://developer.apple.com/documentation/objectivec/1418539-class_getimagename)

|  | Declaration |
| --- | --- |
| From | ``` func class_getImageName(_ cls: AnyClass!) -> UnsafePointer<Int8> ``` |
| To | ``` func class_getImageName(_ cls: Swift.AnyClass!) -> UnsafePointer<Int8>! ``` |

Modified [class_getInstanceMethod(_: Swift.AnyClass!, _: Selector!) -> Method!](https://developer.apple.com/documentation/objectivec/1418530-class_getinstancemethod)

|  | Declaration |
| --- | --- |
| From | ``` func class_getInstanceMethod(_ cls: AnyClass!, _ name: Selector) -> Method ``` |
| To | ``` func class_getInstanceMethod(_ cls: Swift.AnyClass!, _ name: Selector!) -> Method! ``` |

Modified [class_getInstanceSize(_: Swift.AnyClass!) -> Int](https://developer.apple.com/documentation/objectivec/1418907-class_getinstancesize)

|  | Declaration |
| --- | --- |
| From | ``` func class_getInstanceSize(_ cls: AnyClass!) -> Int ``` |
| To | ``` func class_getInstanceSize(_ cls: Swift.AnyClass!) -> Int ``` |

Modified [class_getInstanceVariable(_: Swift.AnyClass!, _: UnsafePointer<Int8>!) -> Ivar!](https://developer.apple.com/documentation/objectivec/1418643-class_getinstancevariable)

|  | Declaration |
| --- | --- |
| From | ``` func class_getInstanceVariable(_ cls: AnyClass!, _ name: UnsafePointer<Int8>) -> Ivar ``` |
| To | ``` func class_getInstanceVariable(_ cls: Swift.AnyClass!, _ name: UnsafePointer<Int8>!) -> Ivar! ``` |

Modified [class_getIvarLayout(_: Swift.AnyClass!) -> UnsafePointer<UInt8>!](https://developer.apple.com/documentation/objectivec/1418918-class_getivarlayout)

|  | Declaration |
| --- | --- |
| From | ``` func class_getIvarLayout(_ cls: AnyClass!) -> UnsafePointer<UInt8> ``` |
| To | ``` func class_getIvarLayout(_ cls: Swift.AnyClass!) -> UnsafePointer<UInt8>! ``` |

Modified [class_getMethodImplementation(_: Swift.AnyClass!, _: Selector!) -> IMP!](https://developer.apple.com/documentation/objectivec/1418811-class_getmethodimplementation)

|  | Declaration |
| --- | --- |
| From | ``` func class_getMethodImplementation(_ cls: AnyClass!, _ name: Selector) -> IMP ``` |
| To | ``` func class_getMethodImplementation(_ cls: Swift.AnyClass!, _ name: Selector!) -> IMP! ``` |

Modified [class_getMethodImplementation_stret(_: Swift.AnyClass!, _: Selector!) -> IMP!](https://developer.apple.com/documentation/objectivec/1418771-class_getmethodimplementation_st)

|  | Declaration |
| --- | --- |
| From | ``` func class_getMethodImplementation_stret(_ cls: AnyClass!, _ name: Selector) -> IMP ``` |
| To | ``` func class_getMethodImplementation_stret(_ cls: Swift.AnyClass!, _ name: Selector!) -> IMP! ``` |

Modified [class_getName(_: Swift.AnyClass!) -> UnsafePointer<Int8>!](https://developer.apple.com/documentation/objectivec/1418635-class_getname)

|  | Declaration |
| --- | --- |
| From | ``` func class_getName(_ cls: AnyClass!) -> UnsafePointer<Int8> ``` |
| To | ``` func class_getName(_ cls: Swift.AnyClass!) -> UnsafePointer<Int8>! ``` |

Modified [class_getProperty(_: Swift.AnyClass!, _: UnsafePointer<Int8>!) -> objc_property_t!](https://developer.apple.com/documentation/objectivec/1418597-class_getproperty)

|  | Declaration |
| --- | --- |
| From | ``` func class_getProperty(_ cls: AnyClass!, _ name: UnsafePointer<Int8>) -> objc_property_t ``` |
| To | ``` func class_getProperty(_ cls: Swift.AnyClass!, _ name: UnsafePointer<Int8>!) -> objc_property_t! ``` |

Modified [class_getSuperclass(_: Swift.AnyClass!) -> Swift.AnyClass!](https://developer.apple.com/documentation/objectivec/1418498-class_getsuperclass)

|  | Declaration |
| --- | --- |
| From | ``` func class_getSuperclass(_ cls: AnyClass!) -> AnyClass! ``` |
| To | ``` func class_getSuperclass(_ cls: Swift.AnyClass!) -> Swift.AnyClass! ``` |

Modified [class_getVersion(_: Swift.AnyClass!) -> Int32](https://developer.apple.com/documentation/objectivec/1418537-class_getversion)

|  | Declaration |
| --- | --- |
| From | ``` func class_getVersion(_ cls: AnyClass!) -> Int32 ``` |
| To | ``` func class_getVersion(_ cls: Swift.AnyClass!) -> Int32 ``` |

Modified [class_getWeakIvarLayout(_: Swift.AnyClass!) -> UnsafePointer<UInt8>!](https://developer.apple.com/documentation/objectivec/1418508-class_getweakivarlayout)

|  | Declaration |
| --- | --- |
| From | ``` func class_getWeakIvarLayout(_ cls: AnyClass!) -> UnsafePointer<UInt8> ``` |
| To | ``` func class_getWeakIvarLayout(_ cls: Swift.AnyClass!) -> UnsafePointer<UInt8>! ``` |

Modified [class_isMetaClass(_: Swift.AnyClass!) -> Bool](https://developer.apple.com/documentation/objectivec/1418627-class_ismetaclass)

|  | Declaration |
| --- | --- |
| From | ``` func class_isMetaClass(_ cls: AnyClass!) -> Bool ``` |
| To | ``` func class_isMetaClass(_ cls: Swift.AnyClass!) -> Bool ``` |

Modified [class_replaceMethod(_: Swift.AnyClass!, _: Selector!, _: IMP!, _: UnsafePointer<Int8>!) -> IMP!](https://developer.apple.com/documentation/objectivec/1418677-class_replacemethod)

|  | Declaration |
| --- | --- |
| From | ``` func class_replaceMethod(_ cls: AnyClass!, _ name: Selector, _ imp: IMP, _ types: UnsafePointer<Int8>) -> IMP ``` |
| To | ``` func class_replaceMethod(_ cls: Swift.AnyClass!, _ name: Selector!, _ imp: IMP!, _ types: UnsafePointer<Int8>!) -> IMP! ``` |

Modified [class_replaceProperty(_: Swift.AnyClass!, _: UnsafePointer<Int8>!, _: UnsafePointer<objc_property_attribute_t>!, _: UInt32)](https://developer.apple.com/documentation/objectivec/1418891-class_replaceproperty)

|  | Declaration |
| --- | --- |
| From | ``` func class_replaceProperty(_ cls: AnyClass!, _ name: UnsafePointer<Int8>, _ attributes: UnsafePointer<objc_property_attribute_t>, _ attributeCount: UInt32) ``` |
| To | ``` func class_replaceProperty(_ cls: Swift.AnyClass!, _ name: UnsafePointer<Int8>!, _ attributes: UnsafePointer<objc_property_attribute_t>!, _ attributeCount: UInt32) ``` |

Modified [class_respondsToSelector(_: Swift.AnyClass!, _: Selector!) -> Bool](https://developer.apple.com/documentation/objectivec/1418517-class_respondstoselector)

|  | Declaration |
| --- | --- |
| From | ``` func class_respondsToSelector(_ cls: AnyClass!, _ sel: Selector) -> Bool ``` |
| To | ``` func class_respondsToSelector(_ cls: Swift.AnyClass!, _ sel: Selector!) -> Bool ``` |

Modified [class_setIvarLayout(_: Swift.AnyClass!, _: UnsafePointer<UInt8>!)](https://developer.apple.com/documentation/objectivec/1418749-class_setivarlayout)

|  | Declaration |
| --- | --- |
| From | ``` func class_setIvarLayout(_ cls: AnyClass!, _ layout: UnsafePointer<UInt8>) ``` |
| To | ``` func class_setIvarLayout(_ cls: Swift.AnyClass!, _ layout: UnsafePointer<UInt8>!) ``` |

Modified [class_setVersion(_: Swift.AnyClass!, _: Int32)](https://developer.apple.com/documentation/objectivec/1418492-class_setversion)

|  | Declaration |
| --- | --- |
| From | ``` func class_setVersion(_ cls: AnyClass!, _ version: Int32) ``` |
| To | ``` func class_setVersion(_ cls: Swift.AnyClass!, _ version: Int32) ``` |

Modified [class_setWeakIvarLayout(_: Swift.AnyClass!, _: UnsafePointer<UInt8>!)](https://developer.apple.com/documentation/objectivec/1418852-class_setweakivarlayout)

|  | Declaration |
| --- | --- |
| From | ``` func class_setWeakIvarLayout(_ cls: AnyClass!, _ layout: UnsafePointer<UInt8>) ``` |
| To | ``` func class_setWeakIvarLayout(_ cls: Swift.AnyClass!, _ layout: UnsafePointer<UInt8>!) ``` |

Modified IMP

|  | Declaration |
| --- | --- |
| From | ``` typealias IMP = COpaquePointer ``` |
| To | ``` typealias IMP = OpaquePointer ``` |

Modified [imp_getBlock(_: IMP!) -> Any!](https://developer.apple.com/documentation/objectivec/1418820-imp_getblock)

|  | Declaration |
| --- | --- |
| From | ``` func imp_getBlock(_ anImp: IMP) -> AnyObject! ``` |
| To | ``` func imp_getBlock(_ anImp: IMP!) -> Any! ``` |

Modified [imp_implementationWithBlock(_: Any!) -> IMP!](https://developer.apple.com/documentation/objectivec/1418587-imp_implementationwithblock)

|  | Declaration |
| --- | --- |
| From | ``` func imp_implementationWithBlock(_ block: AnyObject!) -> IMP ``` |
| To | ``` func imp_implementationWithBlock(_ block: Any!) -> IMP! ``` |

Modified [imp_removeBlock(_: IMP!) -> Bool](https://developer.apple.com/documentation/objectivec/1418482-imp_removeblock)

|  | Declaration |
| --- | --- |
| From | ``` func imp_removeBlock(_ anImp: IMP) -> Bool ``` |
| To | ``` func imp_removeBlock(_ anImp: IMP!) -> Bool ``` |

Modified [Ivar](https://developer.apple.com/documentation/objectivec/ivar)

|  | Declaration |
| --- | --- |
| From | ``` typealias Ivar = COpaquePointer ``` |
| To | ``` typealias Ivar = OpaquePointer ``` |

Modified [ivar_getName(_: Ivar!) -> UnsafePointer<Int8>!](https://developer.apple.com/documentation/objectivec/1418922-ivar_getname)

|  | Declaration |
| --- | --- |
| From | ``` func ivar_getName(_ v: Ivar) -> UnsafePointer<Int8> ``` |
| To | ``` func ivar_getName(_ v: Ivar!) -> UnsafePointer<Int8>! ``` |

Modified [ivar_getOffset(_: Ivar!) -> Int](https://developer.apple.com/documentation/objectivec/1418976-ivar_getoffset)

|  | Declaration |
| --- | --- |
| From | ``` func ivar_getOffset(_ v: Ivar) -> Int ``` |
| To | ``` func ivar_getOffset(_ v: Ivar!) -> Int ``` |

Modified [ivar_getTypeEncoding(_: Ivar!) -> UnsafePointer<Int8>!](https://developer.apple.com/documentation/objectivec/1418569-ivar_gettypeencoding)

|  | Declaration |
| --- | --- |
| From | ``` func ivar_getTypeEncoding(_ v: Ivar) -> UnsafePointer<Int8> ``` |
| To | ``` func ivar_getTypeEncoding(_ v: Ivar!) -> UnsafePointer<Int8>! ``` |

Modified marg_list

|  | Declaration |
| --- | --- |
| From | ``` typealias marg_list = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias marg_list = UnsafeMutableRawPointer ``` |

Modified [Method](https://developer.apple.com/documentation/objectivec/method)

|  | Declaration |
| --- | --- |
| From | ``` typealias Method = COpaquePointer ``` |
| To | ``` typealias Method = OpaquePointer ``` |

Modified [method_copyArgumentType(_: Method!, _: UInt32) -> UnsafeMutablePointer<Int8>!](https://developer.apple.com/documentation/objectivec/1418832-method_copyargumenttype)

|  | Declaration |
| --- | --- |
| From | ``` func method_copyArgumentType(_ m: Method, _ index: UInt32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func method_copyArgumentType(_ m: Method!, _ index: UInt32) -> UnsafeMutablePointer<Int8>! ``` |

Modified [method_copyReturnType(_: Method!) -> UnsafeMutablePointer<Int8>!](https://developer.apple.com/documentation/objectivec/1418777-method_copyreturntype)

|  | Declaration |
| --- | --- |
| From | ``` func method_copyReturnType(_ m: Method) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func method_copyReturnType(_ m: Method!) -> UnsafeMutablePointer<Int8>! ``` |

Modified [method_exchangeImplementations(_: Method!, _: Method!)](https://developer.apple.com/documentation/objectivec/1418769-method_exchangeimplementations)

|  | Declaration |
| --- | --- |
| From | ``` func method_exchangeImplementations(_ m1: Method, _ m2: Method) ``` |
| To | ``` func method_exchangeImplementations(_ m1: Method!, _ m2: Method!) ``` |

Modified [method_getArgumentType(_: Method!, _: UInt32, _: UnsafeMutablePointer<Int8>!, _: Int)](https://developer.apple.com/documentation/objectivec/1418607-method_getargumenttype)

|  | Declaration |
| --- | --- |
| From | ``` func method_getArgumentType(_ m: Method, _ index: UInt32, _ dst: UnsafeMutablePointer<Int8>, _ dst_len: Int) ``` |
| To | ``` func method_getArgumentType(_ m: Method!, _ index: UInt32, _ dst: UnsafeMutablePointer<Int8>!, _ dst_len: Int) ``` |

Modified [method_getDescription(_: Method!) -> UnsafeMutablePointer<objc_method_description>!](https://developer.apple.com/documentation/objectivec/1418545-method_getdescription)

|  | Declaration |
| --- | --- |
| From | ``` func method_getDescription(_ m: Method) -> UnsafeMutablePointer<objc_method_description> ``` |
| To | ``` func method_getDescription(_ m: Method!) -> UnsafeMutablePointer<objc_method_description>! ``` |

Modified [method_getImplementation(_: Method!) -> IMP!](https://developer.apple.com/documentation/objectivec/1418551-method_getimplementation)

|  | Declaration |
| --- | --- |
| From | ``` func method_getImplementation(_ m: Method) -> IMP ``` |
| To | ``` func method_getImplementation(_ m: Method!) -> IMP! ``` |

Modified [method_getName(_: Method!) -> Selector!](https://developer.apple.com/documentation/objectivec/1418758-method_getname)

|  | Declaration |
| --- | --- |
| From | ``` func method_getName(_ m: Method) -> Selector ``` |
| To | ``` func method_getName(_ m: Method!) -> Selector! ``` |

Modified [method_getNumberOfArguments(_: Method!) -> UInt32](https://developer.apple.com/documentation/objectivec/1418968-method_getnumberofarguments)

|  | Declaration |
| --- | --- |
| From | ``` func method_getNumberOfArguments(_ m: Method) -> UInt32 ``` |
| To | ``` func method_getNumberOfArguments(_ m: Method!) -> UInt32 ``` |

Modified [method_getReturnType(_: Method!, _: UnsafeMutablePointer<Int8>!, _: Int)](https://developer.apple.com/documentation/objectivec/1418591-method_getreturntype)

|  | Declaration |
| --- | --- |
| From | ``` func method_getReturnType(_ m: Method, _ dst: UnsafeMutablePointer<Int8>, _ dst_len: Int) ``` |
| To | ``` func method_getReturnType(_ m: Method!, _ dst: UnsafeMutablePointer<Int8>!, _ dst_len: Int) ``` |

Modified [method_getTypeEncoding(_: Method!) -> UnsafePointer<Int8>!](https://developer.apple.com/documentation/objectivec/1418488-method_gettypeencoding)

|  | Declaration |
| --- | --- |
| From | ``` func method_getTypeEncoding(_ m: Method) -> UnsafePointer<Int8> ``` |
| To | ``` func method_getTypeEncoding(_ m: Method!) -> UnsafePointer<Int8>! ``` |

Modified [method_setImplementation(_: Method!, _: IMP!) -> IMP!](https://developer.apple.com/documentation/objectivec/1418707-method_setimplementation)

|  | Declaration |
| --- | --- |
| From | ``` func method_setImplementation(_ m: Method, _ imp: IMP) -> IMP ``` |
| To | ``` func method_setImplementation(_ m: Method!, _ imp: IMP!) -> IMP! ``` |

Modified [objc_addExceptionHandler(_: ObjectiveC.objc_exception_handler!, _: UnsafeMutableRawPointer!) -> UInt](https://developer.apple.com/documentation/objectivec/1418605-objc_addexceptionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func objc_addExceptionHandler(_ fn: objc_exception_handler!, _ context: UnsafeMutablePointer<Void>) -> UInt ``` |
| To | ``` func objc_addExceptionHandler(_ fn: ObjectiveC.objc_exception_handler!, _ context: UnsafeMutableRawPointer!) -> UInt ``` |

Modified [objc_allocateClassPair(_: Swift.AnyClass!, _: UnsafePointer<Int8>!, _: Int) -> Swift.AnyClass!](https://developer.apple.com/documentation/objectivec/1418559-objc_allocateclasspair)

|  | Declaration |
| --- | --- |
| From | ``` func objc_allocateClassPair(_ superclass: AnyClass!, _ name: UnsafePointer<Int8>, _ extraBytes: Int) -> AnyClass! ``` |
| To | ``` func objc_allocateClassPair(_ superclass: Swift.AnyClass!, _ name: UnsafePointer<Int8>!, _ extraBytes: Int) -> Swift.AnyClass! ``` |

Modified [objc_allocateProtocol(_: UnsafePointer<Int8>!) -> Protocol!](https://developer.apple.com/documentation/objectivec/1418599-objc_allocateprotocol)

|  | Declaration |
| --- | --- |
| From | ``` func objc_allocateProtocol(_ name: UnsafePointer<Int8>) -> Protocol! ``` |
| To | ``` func objc_allocateProtocol(_ name: UnsafePointer<Int8>!) -> Protocol! ``` |

Modified objc_assertRegisteredThreadWithCollector()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified objc_begin_catch(_: UnsafeMutableRawPointer!) -> Any!

|  | Declaration |
| --- | --- |
| From | ``` func objc_begin_catch(_ exc_buf: UnsafeMutablePointer<Void>) -> AnyObject! ``` |
| To | ``` func objc_begin_catch(_ exc_buf: UnsafeMutableRawPointer!) -> Any! ``` |

Modified objc_clear_stack(_: UInt)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified objc_collect(_: UInt)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [objc_collectableZone() -> UnsafeMutablePointer<malloc_zone_t>!](https://developer.apple.com/documentation/objectivec/1418519-objc_collectablezone)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func objc_collectableZone() -> UnsafeMutablePointer<malloc_zone_t> ``` | -- |
| To | ``` func objc_collectableZone() -> UnsafeMutablePointer<malloc_zone_t>! ``` | OS X 10.12 |

Modified objc_collectingEnabled() -> Bool

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [objc_copyClassList(_: UnsafeMutablePointer<UInt32>!) -> AutoreleasingUnsafeMutablePointer<Swift.AnyClass?>!](https://developer.apple.com/documentation/objectivec/1418762-objc_copyclasslist)

|  | Declaration |
| --- | --- |
| From | ``` func objc_copyClassList(_ outCount: UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<AnyClass?> ``` |
| To | ``` func objc_copyClassList(_ outCount: UnsafeMutablePointer<UInt32>!) -> AutoreleasingUnsafeMutablePointer<Swift.AnyClass?>! ``` |

Modified [objc_copyClassNamesForImage(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<UnsafePointer<Int8>?>!](https://developer.apple.com/documentation/objectivec/1418485-objc_copyclassnamesforimage)

|  | Declaration |
| --- | --- |
| From | ``` func objc_copyClassNamesForImage(_ image: UnsafePointer<Int8>, _ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<UnsafePointer<Int8>> ``` |
| To | ``` func objc_copyClassNamesForImage(_ image: UnsafePointer<Int8>!, _ outCount: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<UnsafePointer<Int8>?>! ``` |

Modified [objc_copyImageNames(_: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<UnsafePointer<Int8>?>!](https://developer.apple.com/documentation/objectivec/1418970-objc_copyimagenames)

|  | Declaration |
| --- | --- |
| From | ``` func objc_copyImageNames(_ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<UnsafePointer<Int8>> ``` |
| To | ``` func objc_copyImageNames(_ outCount: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<UnsafePointer<Int8>?>! ``` |

Modified [objc_copyProtocolList(_: UnsafeMutablePointer<UInt32>!) -> AutoreleasingUnsafeMutablePointer<Protocol?>!](https://developer.apple.com/documentation/objectivec/1418549-objc_copyprotocollist)

|  | Declaration |
| --- | --- |
| From | ``` func objc_copyProtocolList(_ outCount: UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<Protocol?> ``` |
| To | ``` func objc_copyProtocolList(_ outCount: UnsafeMutablePointer<UInt32>!) -> AutoreleasingUnsafeMutablePointer<Protocol?>! ``` |

Modified [objc_disposeClassPair(_: Swift.AnyClass!)](https://developer.apple.com/documentation/objectivec/1418912-objc_disposeclasspair)

|  | Declaration |
| --- | --- |
| From | ``` func objc_disposeClassPair(_ cls: AnyClass!) ``` |
| To | ``` func objc_disposeClassPair(_ cls: Swift.AnyClass!) ``` |

Modified [objc_duplicateClass(_: Swift.AnyClass!, _: UnsafePointer<Int8>!, _: Int) -> Swift.AnyClass!](https://developer.apple.com/documentation/objectivec/1418645-objc_duplicateclass)

|  | Declaration |
| --- | --- |
| From | ``` func objc_duplicateClass(_ original: AnyClass!, _ name: UnsafePointer<Int8>, _ extraBytes: Int) -> AnyClass! ``` |
| To | ``` func objc_duplicateClass(_ original: Swift.AnyClass!, _ name: UnsafePointer<Int8>!, _ extraBytes: Int) -> Swift.AnyClass! ``` |

Modified [objc_enumerationMutation(_: Any!)](https://developer.apple.com/documentation/objectivec/1418744-objc_enumerationmutation)

|  | Declaration |
| --- | --- |
| From | ``` func objc_enumerationMutation(_ obj: AnyObject!) ``` |
| To | ``` func objc_enumerationMutation(_ obj: Any!) ``` |

Modified objc_exception_handler

|  | Declaration |
| --- | --- |
| From | ``` typealias objc_exception_handler = (AnyObject!, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias objc_exception_handler = (Any?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified objc_exception_matcher

|  | Declaration |
| --- | --- |
| From | ``` typealias objc_exception_matcher = (AnyClass!, AnyObject!) -> Int32 ``` |
| To | ``` typealias objc_exception_matcher = (Swift.AnyClass?, Any?) -> Int32 ``` |

Modified objc_exception_preprocessor

|  | Declaration |
| --- | --- |
| From | ``` typealias objc_exception_preprocessor = (AnyObject!) -> AnyObject! ``` |
| To | ``` typealias objc_exception_preprocessor = (Any?) -> Any? ``` |

Modified objc_exception_throw(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` func objc_exception_throw(_ exception: AnyObject!) ``` |
| To | ``` func objc_exception_throw(_ exception: Any!) ``` |

Modified [objc_getAssociatedObject(_: Any!, _: UnsafeRawPointer!) -> Any!](https://developer.apple.com/documentation/objectivec/1418865-objc_getassociatedobject)

|  | Declaration |
| --- | --- |
| From | ``` func objc_getAssociatedObject(_ object: AnyObject!, _ key: UnsafePointer<Void>) -> AnyObject! ``` |
| To | ``` func objc_getAssociatedObject(_ object: Any!, _ key: UnsafeRawPointer!) -> Any! ``` |

Modified [objc_getClass(_: UnsafePointer<Int8>!) -> Any!](https://developer.apple.com/documentation/objectivec/1418952-objc_getclass)

|  | Declaration |
| --- | --- |
| From | ``` func objc_getClass(_ name: UnsafePointer<Int8>) -> AnyObject! ``` |
| To | ``` func objc_getClass(_ name: UnsafePointer<Int8>!) -> Any! ``` |

Modified [objc_getClassList(_: AutoreleasingUnsafeMutablePointer<Swift.AnyClass?>!, _: Int32) -> Int32](https://developer.apple.com/documentation/objectivec/1418579-objc_getclasslist)

|  | Declaration |
| --- | --- |
| From | ``` func objc_getClassList(_ buffer: AutoreleasingUnsafeMutablePointer<AnyClass?>, _ bufferCount: Int32) -> Int32 ``` |
| To | ``` func objc_getClassList(_ buffer: AutoreleasingUnsafeMutablePointer<Swift.AnyClass?>!, _ bufferCount: Int32) -> Int32 ``` |

Modified [objc_getMetaClass(_: UnsafePointer<Int8>!) -> Any!](https://developer.apple.com/documentation/objectivec/1418721-objc_getmetaclass)

|  | Declaration |
| --- | --- |
| From | ``` func objc_getMetaClass(_ name: UnsafePointer<Int8>) -> AnyObject! ``` |
| To | ``` func objc_getMetaClass(_ name: UnsafePointer<Int8>!) -> Any! ``` |

Modified [objc_getProtocol(_: UnsafePointer<Int8>!) -> Protocol!](https://developer.apple.com/documentation/objectivec/1418870-objc_getprotocol)

|  | Declaration |
| --- | --- |
| From | ``` func objc_getProtocol(_ name: UnsafePointer<Int8>) -> Protocol! ``` |
| To | ``` func objc_getProtocol(_ name: UnsafePointer<Int8>!) -> Protocol! ``` |

Modified [objc_getRequiredClass(_: UnsafePointer<Int8>!) -> Swift.AnyClass!](https://developer.apple.com/documentation/objectivec/1418661-objc_getrequiredclass)

|  | Declaration |
| --- | --- |
| From | ``` func objc_getRequiredClass(_ name: UnsafePointer<Int8>) -> AnyClass! ``` |
| To | ``` func objc_getRequiredClass(_ name: UnsafePointer<Int8>!) -> Swift.AnyClass! ``` |

Modified objc_is_finalized(_: UnsafeMutableRawPointer!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func objc_is_finalized(_ ptr: UnsafeMutablePointer<Void>) -> Bool ``` | -- |
| To | ``` func objc_is_finalized(_ ptr: UnsafeMutableRawPointer!) -> Bool ``` | OS X 10.12 |

Modified [objc_loadWeak(_: AutoreleasingUnsafeMutablePointer<AnyObject?>!) -> Any!](https://developer.apple.com/documentation/objectivec/1418693-objc_loadweak)

|  | Declaration |
| --- | --- |
| From | ``` func objc_loadWeak(_ location: AutoreleasingUnsafeMutablePointer<AnyObject?>) -> AnyObject! ``` |
| To | ``` func objc_loadWeak(_ location: AutoreleasingUnsafeMutablePointer<AnyObject?>!) -> Any! ``` |

Modified [objc_lookUpClass(_: UnsafePointer<Int8>!) -> Swift.AnyClass!](https://developer.apple.com/documentation/objectivec/1418760-objc_lookupclass)

|  | Declaration |
| --- | --- |
| From | ``` func objc_lookUpClass(_ name: UnsafePointer<Int8>) -> AnyClass! ``` |
| To | ``` func objc_lookUpClass(_ name: UnsafePointer<Int8>!) -> Swift.AnyClass! ``` |

Modified objc_memmove_collectable(_: UnsafeMutableRawPointer!, _: UnsafeRawPointer!, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func objc_memmove_collectable(_ dst: UnsafeMutablePointer<Void>, _ src: UnsafePointer<Void>, _ size: Int) -> UnsafeMutablePointer<Void> ``` | -- |
| To | ``` func objc_memmove_collectable(_ dst: UnsafeMutableRawPointer!, _ src: UnsafeRawPointer!, _ size: Int) -> UnsafeMutableRawPointer! ``` | OS X 10.12 |

Modified objc_objectptr_t

|  | Declaration |
| --- | --- |
| From | ``` typealias objc_objectptr_t = UnsafePointer<Void> ``` |
| To | ``` typealias objc_objectptr_t = UnsafeRawPointer ``` |

Modified [objc_property_t](https://developer.apple.com/documentation/objectivec/objc_property_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias objc_property_t = COpaquePointer ``` |
| To | ``` typealias objc_property_t = OpaquePointer ``` |

Modified [objc_registerClassPair(_: Swift.AnyClass!)](https://developer.apple.com/documentation/objectivec/1418603-objc_registerclasspair)

|  | Declaration |
| --- | --- |
| From | ``` func objc_registerClassPair(_ cls: AnyClass!) ``` |
| To | ``` func objc_registerClassPair(_ cls: Swift.AnyClass!) ``` |

Modified objc_registerThreadWithCollector()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [objc_removeAssociatedObjects(_: Any!)](https://developer.apple.com/documentation/objectivec/1418683-objc_removeassociatedobjects)

|  | Declaration |
| --- | --- |
| From | ``` func objc_removeAssociatedObjects(_ object: AnyObject!) ``` |
| To | ``` func objc_removeAssociatedObjects(_ object: Any!) ``` |

Modified [objc_setAssociatedObject(_: Any!, _: UnsafeRawPointer!, _: Any!, _: objc_AssociationPolicy)](https://developer.apple.com/documentation/objectivec/1418509-objc_setassociatedobject)

|  | Declaration |
| --- | --- |
| From | ``` func objc_setAssociatedObject(_ object: AnyObject!, _ key: UnsafePointer<Void>, _ value: AnyObject!, _ policy: objc_AssociationPolicy) ``` |
| To | ``` func objc_setAssociatedObject(_ object: Any!, _ key: UnsafeRawPointer!, _ value: Any!, _ policy: objc_AssociationPolicy) ``` |

Modified objc_setCollectionRatio(_: Int)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified objc_setCollectionThreshold(_: Int)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [objc_setEnumerationMutationHandler(_: ( (Any?) -> Swift.Void)!)](https://developer.apple.com/documentation/objectivec/1418751-objc_setenumerationmutationhandl)

|  | Declaration |
| --- | --- |
| From | ``` func objc_setEnumerationMutationHandler(_ handler: ((AnyObject!) -> Void)!) ``` |
| To | ``` func objc_setEnumerationMutationHandler(_ handler: (@escaping (Any?) -> Swift.Void)!) ``` |

Modified objc_setExceptionMatcher(_: ObjectiveC.objc_exception_matcher!) -> ObjectiveC.objc_exception_matcher!

|  | Declaration |
| --- | --- |
| From | ``` func objc_setExceptionMatcher(_ fn: objc_exception_matcher!) -> objc_exception_matcher! ``` |
| To | ``` func objc_setExceptionMatcher(_ fn: ObjectiveC.objc_exception_matcher!) -> ObjectiveC.objc_exception_matcher! ``` |

Modified objc_setExceptionPreprocessor(_: ObjectiveC.objc_exception_preprocessor!) -> ObjectiveC.objc_exception_preprocessor!

|  | Declaration |
| --- | --- |
| From | ``` func objc_setExceptionPreprocessor(_ fn: objc_exception_preprocessor!) -> objc_exception_preprocessor! ``` |
| To | ``` func objc_setExceptionPreprocessor(_ fn: ObjectiveC.objc_exception_preprocessor!) -> ObjectiveC.objc_exception_preprocessor! ``` |

Modified objc_setForwardHandler(_: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func objc_setForwardHandler(_ fwd: UnsafeMutablePointer<Void>, _ fwd_stret: UnsafeMutablePointer<Void>) ``` |
| To | ``` func objc_setForwardHandler(_ fwd: UnsafeMutableRawPointer!, _ fwd_stret: UnsafeMutableRawPointer!) ``` |

Modified objc_setUncaughtExceptionHandler(_: ObjectiveC.objc_uncaught_exception_handler!) -> ObjectiveC.objc_uncaught_exception_handler!

|  | Declaration |
| --- | --- |
| From | ``` func objc_setUncaughtExceptionHandler(_ fn: objc_uncaught_exception_handler!) -> objc_uncaught_exception_handler! ``` |
| To | ``` func objc_setUncaughtExceptionHandler(_ fn: ObjectiveC.objc_uncaught_exception_handler!) -> ObjectiveC.objc_uncaught_exception_handler! ``` |

Modified [objc_storeWeak(_: AutoreleasingUnsafeMutablePointer<AnyObject?>!, _: Any!) -> Any!](https://developer.apple.com/documentation/objectivec/1418791-objc_storeweak)

|  | Declaration |
| --- | --- |
| From | ``` func objc_storeWeak(_ location: AutoreleasingUnsafeMutablePointer<AnyObject?>, _ obj: AnyObject!) -> AnyObject! ``` |
| To | ``` func objc_storeWeak(_ location: AutoreleasingUnsafeMutablePointer<AnyObject?>!, _ obj: Any!) -> Any! ``` |

Modified objc_sync_enter(_: Any!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func objc_sync_enter(_ obj: AnyObject!) -> Int32 ``` |
| To | ``` func objc_sync_enter(_ obj: Any!) -> Int32 ``` |

Modified objc_sync_exit(_: Any!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func objc_sync_exit(_ obj: AnyObject!) -> Int32 ``` |
| To | ``` func objc_sync_exit(_ obj: Any!) -> Int32 ``` |

Modified objc_uncaught_exception_handler

|  | Declaration |
| --- | --- |
| From | ``` typealias objc_uncaught_exception_handler = (AnyObject!) -> Void ``` |
| To | ``` typealias objc_uncaught_exception_handler = (Any?) -> Swift.Void ``` |

Modified objc_unregisterThreadWithCollector()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [object_getClass(_: Any!) -> Swift.AnyClass!](https://developer.apple.com/documentation/objectivec/1418629-object_getclass)

|  | Declaration |
| --- | --- |
| From | ``` func object_getClass(_ obj: AnyObject!) -> AnyClass! ``` |
| To | ``` func object_getClass(_ obj: Any!) -> Swift.AnyClass! ``` |

Modified [object_getClassName(_: Any!) -> UnsafePointer<Int8>!](https://developer.apple.com/documentation/objectivec/1418547-object_getclassname)

|  | Declaration |
| --- | --- |
| From | ``` func object_getClassName(_ obj: AnyObject!) -> UnsafePointer<Int8> ``` |
| To | ``` func object_getClassName(_ obj: Any!) -> UnsafePointer<Int8>! ``` |

Modified [object_getIvar(_: Any!, _: Ivar!) -> Any!](https://developer.apple.com/documentation/objectivec/1418960-object_getivar)

|  | Declaration |
| --- | --- |
| From | ``` func object_getIvar(_ obj: AnyObject!, _ ivar: Ivar) -> AnyObject! ``` |
| To | ``` func object_getIvar(_ obj: Any!, _ ivar: Ivar!) -> Any! ``` |

Modified [object_isClass(_: Any!) -> Bool](https://developer.apple.com/documentation/objectivec/1418659-object_isclass)

|  | Declaration |
| --- | --- |
| From | ``` func object_isClass(_ obj: AnyObject!) -> Bool ``` |
| To | ``` func object_isClass(_ obj: Any!) -> Bool ``` |

Modified [object_setClass(_: Any!, _: Swift.AnyClass!) -> Swift.AnyClass!](https://developer.apple.com/documentation/objectivec/1418905-object_setclass)

|  | Declaration |
| --- | --- |
| From | ``` func object_setClass(_ obj: AnyObject!, _ cls: AnyClass!) -> AnyClass! ``` |
| To | ``` func object_setClass(_ obj: Any!, _ cls: Swift.AnyClass!) -> Swift.AnyClass! ``` |

Modified [object_setIvar(_: Any!, _: Ivar!, _: Any!)](https://developer.apple.com/documentation/objectivec/1418899-object_setivar)

|  | Declaration |
| --- | --- |
| From | ``` func object_setIvar(_ obj: AnyObject!, _ ivar: Ivar, _ value: AnyObject!) ``` |
| To | ``` func object_setIvar(_ obj: Any!, _ ivar: Ivar!, _ value: Any!) ``` |

Modified [property_copyAttributeList(_: objc_property_t!, _: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<objc_property_attribute_t>!](https://developer.apple.com/documentation/objectivec/1418675-property_copyattributelist)

|  | Declaration |
| --- | --- |
| From | ``` func property_copyAttributeList(_ property: objc_property_t, _ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_property_attribute_t> ``` |
| To | ``` func property_copyAttributeList(_ property: objc_property_t!, _ outCount: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<objc_property_attribute_t>! ``` |

Modified [property_copyAttributeValue(_: objc_property_t!, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!](https://developer.apple.com/documentation/objectivec/1418944-property_copyattributevalue)

|  | Declaration |
| --- | --- |
| From | ``` func property_copyAttributeValue(_ property: objc_property_t, _ attributeName: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func property_copyAttributeValue(_ property: objc_property_t!, _ attributeName: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified [property_getAttributes(_: objc_property_t!) -> UnsafePointer<Int8>!](https://developer.apple.com/documentation/objectivec/1418909-property_getattributes)

|  | Declaration |
| --- | --- |
| From | ``` func property_getAttributes(_ property: objc_property_t) -> UnsafePointer<Int8> ``` |
| To | ``` func property_getAttributes(_ property: objc_property_t!) -> UnsafePointer<Int8>! ``` |

Modified [property_getName(_: objc_property_t!) -> UnsafePointer<Int8>!](https://developer.apple.com/documentation/objectivec/1418903-property_getname)

|  | Declaration |
| --- | --- |
| From | ``` func property_getName(_ property: objc_property_t) -> UnsafePointer<Int8> ``` |
| To | ``` func property_getName(_ property: objc_property_t!) -> UnsafePointer<Int8>! ``` |

Modified [protocol_addMethodDescription(_: Protocol!, _: Selector!, _: UnsafePointer<Int8>!, _: Bool, _: Bool)](https://developer.apple.com/documentation/objectivec/1418709-protocol_addmethoddescription)

|  | Declaration |
| --- | --- |
| From | ``` func protocol_addMethodDescription(_ proto: Protocol!, _ name: Selector, _ types: UnsafePointer<Int8>, _ isRequiredMethod: Bool, _ isInstanceMethod: Bool) ``` |
| To | ``` func protocol_addMethodDescription(_ proto: Protocol!, _ name: Selector!, _ types: UnsafePointer<Int8>!, _ isRequiredMethod: Bool, _ isInstanceMethod: Bool) ``` |

Modified [protocol_addProperty(_: Protocol!, _: UnsafePointer<Int8>!, _: UnsafePointer<objc_property_attribute_t>!, _: UInt32, _: Bool, _: Bool)](https://developer.apple.com/documentation/objectivec/1418585-protocol_addproperty)

|  | Declaration |
| --- | --- |
| From | ``` func protocol_addProperty(_ proto: Protocol!, _ name: UnsafePointer<Int8>, _ attributes: UnsafePointer<objc_property_attribute_t>, _ attributeCount: UInt32, _ isRequiredProperty: Bool, _ isInstanceProperty: Bool) ``` |
| To | ``` func protocol_addProperty(_ proto: Protocol!, _ name: UnsafePointer<Int8>!, _ attributes: UnsafePointer<objc_property_attribute_t>!, _ attributeCount: UInt32, _ isRequiredProperty: Bool, _ isInstanceProperty: Bool) ``` |

Modified [protocol_copyMethodDescriptionList(_: Protocol!, _: Bool, _: Bool, _: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<objc_method_description>!](https://developer.apple.com/documentation/objectivec/1418822-protocol_copymethoddescriptionli)

|  | Declaration |
| --- | --- |
| From | ``` func protocol_copyMethodDescriptionList(_ p: Protocol!, _ isRequiredMethod: Bool, _ isInstanceMethod: Bool, _ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_method_description> ``` |
| To | ``` func protocol_copyMethodDescriptionList(_ p: Protocol!, _ isRequiredMethod: Bool, _ isInstanceMethod: Bool, _ outCount: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<objc_method_description>! ``` |

Modified [protocol_copyPropertyList(_: Protocol!, _: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<objc_property_t?>!](https://developer.apple.com/documentation/objectivec/1418689-protocol_copypropertylist)

|  | Declaration |
| --- | --- |
| From | ``` func protocol_copyPropertyList(_ proto: Protocol!, _ outCount: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<objc_property_t> ``` |
| To | ``` func protocol_copyPropertyList(_ proto: Protocol!, _ outCount: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<objc_property_t?>! ``` |

Modified [protocol_copyProtocolList(_: Protocol!, _: UnsafeMutablePointer<UInt32>!) -> AutoreleasingUnsafeMutablePointer<Protocol?>!](https://developer.apple.com/documentation/objectivec/1418717-protocol_copyprotocollist)

|  | Declaration |
| --- | --- |
| From | ``` func protocol_copyProtocolList(_ proto: Protocol!, _ outCount: UnsafeMutablePointer<UInt32>) -> AutoreleasingUnsafeMutablePointer<Protocol?> ``` |
| To | ``` func protocol_copyProtocolList(_ proto: Protocol!, _ outCount: UnsafeMutablePointer<UInt32>!) -> AutoreleasingUnsafeMutablePointer<Protocol?>! ``` |

Modified [protocol_getMethodDescription(_: Protocol!, _: Selector!, _: Bool, _: Bool) -> objc_method_description](https://developer.apple.com/documentation/objectivec/1418830-protocol_getmethoddescription)

|  | Declaration |
| --- | --- |
| From | ``` func protocol_getMethodDescription(_ p: Protocol!, _ aSel: Selector, _ isRequiredMethod: Bool, _ isInstanceMethod: Bool) -> objc_method_description ``` |
| To | ``` func protocol_getMethodDescription(_ p: Protocol!, _ aSel: Selector!, _ isRequiredMethod: Bool, _ isInstanceMethod: Bool) -> objc_method_description ``` |

Modified [protocol_getName(_: Protocol!) -> UnsafePointer<Int8>!](https://developer.apple.com/documentation/objectivec/1418826-protocol_getname)

|  | Declaration |
| --- | --- |
| From | ``` func protocol_getName(_ p: Protocol!) -> UnsafePointer<Int8> ``` |
| To | ``` func protocol_getName(_ p: Protocol!) -> UnsafePointer<Int8>! ``` |

Modified [protocol_getProperty(_: Protocol!, _: UnsafePointer<Int8>!, _: Bool, _: Bool) -> objc_property_t!](https://developer.apple.com/documentation/objectivec/1418740-protocol_getproperty)

|  | Declaration |
| --- | --- |
| From | ``` func protocol_getProperty(_ proto: Protocol!, _ name: UnsafePointer<Int8>, _ isRequiredProperty: Bool, _ isInstanceProperty: Bool) -> objc_property_t ``` |
| To | ``` func protocol_getProperty(_ proto: Protocol!, _ name: UnsafePointer<Int8>!, _ isRequiredProperty: Bool, _ isInstanceProperty: Bool) -> objc_property_t! ``` |

Modified [sel_getName(_: Selector!) -> UnsafePointer<Int8>!](https://developer.apple.com/documentation/objectivec/1418571-sel_getname)

|  | Declaration |
| --- | --- |
| From | ``` func sel_getName(_ sel: Selector) -> UnsafePointer<Int8> ``` |
| To | ``` func sel_getName(_ sel: Selector!) -> UnsafePointer<Int8>! ``` |

Modified [sel_getUid(_: UnsafePointer<Int8>!) -> Selector!](https://developer.apple.com/documentation/objectivec/1418625-sel_getuid)

|  | Declaration |
| --- | --- |
| From | ``` func sel_getUid(_ str: UnsafePointer<Int8>) -> Selector ``` |
| To | ``` func sel_getUid(_ str: UnsafePointer<Int8>!) -> Selector! ``` |

Modified [sel_isEqual(_: Selector!, _: Selector!) -> Bool](https://developer.apple.com/documentation/objectivec/1418736-sel_isequal)

|  | Declaration |
| --- | --- |
| From | ``` func sel_isEqual(_ lhs: Selector, _ rhs: Selector) -> Bool ``` |
| To | ``` func sel_isEqual(_ lhs: Selector!, _ rhs: Selector!) -> Bool ``` |

Modified sel_isMapped(_: Selector!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func sel_isMapped(_ sel: Selector) -> Bool ``` |
| To | ``` func sel_isMapped(_ sel: Selector!) -> Bool ``` |

Modified [sel_registerName(_: UnsafePointer<Int8>!) -> Selector!](https://developer.apple.com/documentation/objectivec/1418557-sel_registername)

|  | Declaration |
| --- | --- |
| From | ``` func sel_registerName(_ str: UnsafePointer<Int8>) -> Selector ``` |
| To | ``` func sel_registerName(_ str: UnsafePointer<Int8>!) -> Selector! ``` |

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
