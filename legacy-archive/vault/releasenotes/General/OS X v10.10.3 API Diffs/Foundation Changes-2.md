---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/Foundation.html
archived_at: '2026-07-18T02:52:24.663788Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Foundation Changes

## Foundation

Removed NSActivityOptions.valueRemoved NSAlignmentOptions.valueRemoved NSAppleEventDescriptor.init(descriptorType: DescType, data: NSData!)Removed NSArray.init(array: [AnyObject]!)Removed NSArray.init(contentsOfFile: String!)Removed NSArray.init(contentsOfURL: NSURL!)Removed NSArray.convertFromArrayLiteral(AnyObject) -> Self [class]Removed NSArray.getMirror() -> MirrorRemoved NSArray.makeObjectsPerformSelector(Selector)Removed NSArray.makeObjectsPerformSelector(Selector, withObject: AnyObject!)Removed NSArray.objectAtIndexedSubscript(Int) -> AnyObject!Removed NSAttributedStringEnumerationOptions.valueRemoved NSBinarySearchingOptions.valueRemoved NSBundle.init(URL: NSURL!)Removed NSBundle.init(path: String!)Removed NSByteCountFormatterUnits.valueRemoved NSCalendarDateRemoved NSCalendarDate.calendarDate() -> AnyObject! [class]Removed NSCalendarDate.calendarFormat() -> String!Removed NSCalendarDate.dateByAddingYears(Int, months: Int, days: Int, hours: Int, minutes: Int, seconds: Int) -> NSCalendarDate!Removed NSCalendarDate.dateWithString(String!, calendarFormat: String!) -> AnyObject! [class]Removed NSCalendarDate.dateWithString(String!, calendarFormat: String!, locale: AnyObject!) -> AnyObject! [class]Removed NSCalendarDate.dateWithYear(Int, month: Int, day: Int, hour: Int, minute: Int, second: Int, timeZone: NSTimeZone!) -> AnyObject! [class]Removed NSCalendarDate.dayOfCommonEra() -> IntRemoved NSCalendarDate.dayOfMonth() -> IntRemoved NSCalendarDate.dayOfWeek() -> IntRemoved NSCalendarDate.dayOfYear() -> IntRemoved NSCalendarDate.descriptionWithCalendarFormat(String!) -> String!Removed NSCalendarDate.descriptionWithCalendarFormat(String!, locale: AnyObject!) -> String!Removed NSCalendarDate.descriptionWithLocale(AnyObject!) -> String!Removed NSCalendarDate.hourOfDay() -> IntRemoved NSCalendarDate.minuteOfHour() -> IntRemoved NSCalendarDate.monthOfYear() -> IntRemoved NSCalendarDate.secondOfMinute() -> IntRemoved NSCalendarDate.setCalendarFormat(String!)Removed NSCalendarDate.setTimeZone(NSTimeZone!)Removed NSCalendarDate.init(string: String!)Removed NSCalendarDate.init(string: String!, calendarFormat: String!)Removed NSCalendarDate.init(string: String!, calendarFormat: String!, locale: AnyObject!)Removed NSCalendarDate.timeZone() -> NSTimeZone!Removed NSCalendarDate.init(year: Int, month: Int, day: Int, hour: Int, minute: Int, second: Int, timeZone: NSTimeZone!)Removed NSCalendarDate.yearOfCommonEra() -> IntRemoved NSCalendarDate.years(UnsafePointer<Int>, months: UnsafePointer<Int>, days: UnsafePointer<Int>, hours: UnsafePointer<Int>, minutes: UnsafePointer<Int>, seconds: UnsafePointer<Int>, sinceDate: NSCalendarDate!)Removed NSCalendarOptions.valueRemoved NSCalendarUnit.valueRemoved NSComparisonPredicate.init(leftExpression: NSExpression!, rightExpression: NSExpression!, customSelector: Selector)Removed NSComparisonPredicate.init(leftExpression: NSExpression!, rightExpression: NSExpression!, modifier: NSComparisonPredicateModifier, type: NSPredicateOperatorType, options: NSComparisonPredicateOptions)Removed NSComparisonPredicateOptions.valueRemoved NSConnectionRemoved NSConnection.addRequestMode(String!)Removed NSConnection.addRunLoop(NSRunLoop!)Removed NSConnection.allConnections() -> [AnyObject]! [class]Removed NSConnection.currentConversation() -> AnyObject! [class]Removed NSConnection.delegateRemoved NSConnection.dispatchWithComponents([AnyObject]!)Removed NSConnection.enableMultipleThreads()Removed NSConnection.independentConversationQueueingRemoved NSConnection.invalidate()Removed NSConnection.localObjectsRemoved NSConnection.multipleThreadsEnabledRemoved NSConnection.receivePortRemoved NSConnection.init(receivePort: NSPort!, sendPort: NSPort!)Removed NSConnection.registerName(String!) -> BoolRemoved NSConnection.registerName(String!, withNameServer: NSPortNameServer!) -> BoolRemoved NSConnection.init(registeredName: String!, host: String!)Removed NSConnection.init(registeredName: String!, host: String!, usingNameServer: NSPortNameServer!)Removed NSConnection.remoteObjectsRemoved NSConnection.removeRequestMode(String!)Removed NSConnection.removeRunLoop(NSRunLoop!)Removed NSConnection.replyTimeoutRemoved NSConnection.requestModesRemoved NSConnection.requestTimeoutRemoved NSConnection.rootObjectRemoved NSConnection.rootProxyRemoved NSConnection.rootProxyForConnectionWithRegisteredName(String!, host: String!) -> NSDistantObject! [class]Removed NSConnection.rootProxyForConnectionWithRegisteredName(String!, host: String!, usingNameServer: NSPortNameServer!) -> NSDistantObject! [class]Removed NSConnection.runInNewThread()Removed NSConnection.sendPortRemoved NSConnection.serviceConnectionWithName(String!, rootObject: AnyObject!) -> Self! [class]Removed NSConnection.serviceConnectionWithName(String!, rootObject: AnyObject!, usingNameServer: NSPortNameServer!) -> Self! [class]Removed NSConnection.statisticsRemoved NSConnection.validRemoved NSConnectionDelegateRemoved NSConnectionDelegate.authenticateComponents([AnyObject]!, withData: NSData!) -> BoolRemoved NSConnectionDelegate.authenticationDataForComponents([AnyObject]!) -> NSData!Removed NSConnectionDelegate.connection(NSConnection!, handleRequest: NSDistantObjectRequest!) -> BoolRemoved NSConnectionDelegate.connection(NSConnection!, shouldMakeNewConnection: NSConnection!) -> BoolRemoved NSConnectionDelegate.createConversationForConnection(NSConnection!) -> AnyObject!Removed NSConnectionDelegate.makeNewConnection(NSConnection!, sender: NSConnection!) -> BoolRemoved NSData.init(contentsOfFile: String!)Removed NSData.init(contentsOfURL: NSURL!)Removed NSData.dataWithContentsOfFile(String!, options: NSDataReadingOptions, error: NSErrorPointer) -> Self! [class]Removed NSData.dataWithContentsOfURL(NSURL!, options: NSDataReadingOptions, error: NSErrorPointer) -> Self! [class]Removed NSData.dataWithData(NSData!) -> Self! [class]Removed NSDataBase64DecodingOptions.valueRemoved NSDataBase64EncodingOptions.valueRemoved NSDataDetector.dataDetectorWithTypes(NSTextCheckingTypes, error: NSErrorPointer) -> NSDataDetector! [class]Removed NSDataReadingOptions.valueRemoved NSDataSearchOptions.valueRemoved NSDataWritingOptions.DataWritingFileProtectionCompleteRemoved NSDataWritingOptions.DataWritingFileProtectionCompleteUnlessOpenRemoved NSDataWritingOptions.DataWritingFileProtectionCompleteUntilFirstUserAuthenticationRemoved NSDataWritingOptions.DataWritingFileProtectionMaskRemoved NSDataWritingOptions.DataWritingFileProtectionNoneRemoved NSDataWritingOptions.valueRemoved NSDate.date() -> Self! [class]Removed NSDate.dateWithTimeIntervalSinceReferenceDate(NSTimeInterval) -> Self! [class]Removed NSDate.getMirror() -> MirrorRemoved NSDate.init(timeInterval: NSTimeInterval, sinceDate: NSDate!)Removed NSDateComponentsFormatterZeroFormattingBehavior.valueRemoved NSDecimalNumber.decimalNumberWithMantissa(UInt64, exponent: Int16, isNegative: Bool) -> NSDecimalNumber! [class]Removed NSDecimalNumber.decimalNumberWithString(String!) -> NSDecimalNumber! [class]Removed NSDecimalNumber.decimalNumberWithString(String!, locale: AnyObject!) -> NSDecimalNumber! [class]Removed NSDecimalNumberHandler.decimalNumberHandlerWithRoundingMode(NSRoundingMode, scale: Int16, raiseOnExactness: Bool, raiseOnOverflow: Bool, raiseOnUnderflow: Bool, raiseOnDivideByZero: Bool) -> Self! [class]Removed NSDictionary.init(contentsOfFile: String!)Removed NSDictionary.init(contentsOfURL: NSURL!)Removed NSDictionary.convertFromDictionaryLiteral((NSCopying, AnyObject)) -> Self [class]Removed NSDictionary.init(dictionary: [NSObject: AnyObject]!)Removed NSDictionary.generate() -> NSDictionaryGeneratorRemoved NSDictionary.getMirror() -> MirrorRemoved NSDictionary.objectForKeyedSubscript(NSCopying!) -> AnyObject!Removed NSDictionary.init(objects: [AnyObject]!, forKeys:[AnyObject]!)Removed NSDictionaryGeneratorRemoved NSDictionaryGenerator.init(_: NSDictionary)Removed NSDictionaryGenerator.dictionaryRemoved NSDictionaryGenerator.fastGeneratorRemoved NSDictionaryGenerator.next() -> (key: AnyObject, value: AnyObject)?Removed NSDirectoryEnumerationOptions.valueRemoved NSDistantObjectRemoved NSDistantObject.init(coder: NSCoder!)Removed NSDistantObject.connectionForProxyRemoved NSDistantObject.init(local: AnyObject!, connection: NSConnection!)Removed NSDistantObject.proxyWithLocal(AnyObject!, connection: NSConnection!) -> AnyObject! [class]Removed NSDistantObject.proxyWithTarget(AnyObject!, connection: NSConnection!) -> AnyObject! [class]Removed NSDistantObject.setProtocolForProxy(Protocol!)Removed NSDistantObject.init(target: AnyObject!, connection: NSConnection!)Removed NSDistantObjectRequestRemoved NSDistantObjectRequest.connectionRemoved NSDistantObjectRequest.conversationRemoved NSDistantObjectRequest.invocationRemoved NSDistantObjectRequest.replyWithException(NSException!)Removed NSDistributedLock.init(path: String!)Removed NSEnumerationOptions.valueRemoved NSError.errorWithDomain(String!, code: Int, userInfo:[NSObject: AnyObject]!) -> Self! [class]Removed NSException.init(name: String!, reason: String!, userInfo:[NSObject: AnyObject]!)Removed NSExpression.init(format: String, _: CVarArg)Removed NSFileCoordinatorReadingOptions.valueRemoved NSFileCoordinatorWritingOptions.valueRemoved NSFileManagerItemReplacementOptions.valueRemoved NSFileVersionAddingOptions.valueRemoved NSFileVersionReplacingOptions.valueRemoved NSFileWrapperReadingOptions.valueRemoved NSFileWrapperWritingOptions.valueRemoved NSHTTPCookie.cookieWithProperties([NSObject: AnyObject]!) -> NSHTTPCookie! [class]Removed NSInputStream.init(URL: NSURL!)Removed NSInputStream.init(data: NSData!)Removed NSInputStream.inputStreamWithFileAtPath(String!) -> Self! [class]Removed NSInvocationOperationRemoved NSInvocationOperation.invocationRemoved NSInvocationOperation.init(invocation: NSInvocation!)Removed NSInvocationOperation.resultRemoved NSInvocationOperation.init(target: AnyObject!, selector: Selector, object: AnyObject!)Removed NSJSONReadingOptions.valueRemoved NSJSONWritingOptions.valueRemoved NSKeyValueObservingOptions.valueRemoved NSLinguisticTaggerOptions.valueRemoved NSLocale.init(localeIdentifier: String!)Removed NSMachBootstrapServerRemoved NSMachBootstrapServer.portForName(String!) -> NSPort!Removed NSMachBootstrapServer.portForName(String!, host: String!) -> NSPort!Removed NSMachBootstrapServer.registerPort(NSPort!, name: String!) -> BoolRemoved NSMachBootstrapServer.servicePortWithName(String!) -> NSPort!Removed NSMachBootstrapServer.sharedInstance() -> AnyObject! [class]Removed NSMatchingFlags.valueRemoved NSMatchingOptions.valueRemoved NSMessagePortNameServerRemoved NSMessagePortNameServer.portForName(String!) -> NSPort!Removed NSMessagePortNameServer.portForName(String!, host: String!) -> NSPort!Removed NSMessagePortNameServer.sharedInstance() -> AnyObject! [class]Removed NSMethodSignatureRemoved NSMethodSignature.frameLengthRemoved NSMethodSignature.getArgumentTypeAtIndex(Int) -> ConstUnsafePointer<Int8>Removed NSMethodSignature.isOneway() -> BoolRemoved NSMethodSignature.methodReturnLengthRemoved NSMethodSignature.methodReturnTypeRemoved NSMethodSignature.numberOfArgumentsRemoved NSMethodSignature.init(objCTypes: ConstUnsafePointer<Int8>)Removed NSMutableArray.init(contentsOfFile: String!)Removed NSMutableArray.init(contentsOfURL: NSURL!)Removed NSMutableArray.setObject(AnyObject!, atIndexedSubscript: Int)Removed NSMutableDictionary.init(contentsOfFile: String!)Removed NSMutableDictionary.init(contentsOfURL: NSURL!)Removed NSMutableDictionary.setObject(AnyObject!, forKeyedSubscript: NSCopying!)Removed NSMutableOrderedSet.setObject(AnyObject!, atIndexedSubscript: Int)Removed NSMutableString.appendFormat(NSString, _: CVarArg)Removed NSMutableString.stringWithCapacity(Int) -> NSMutableString! [class]Removed NSNetServiceOptions.valueRemoved NSNotification.init(name: String!, object: AnyObject!, userInfo:[NSObject: AnyObject]!)Removed NSNumber.convertFromBooleanLiteral(Bool) -> NSNumber [class]Removed NSNumber.convertFromFloatLiteral(Double) -> NSNumber [class]Removed NSNumber.convertFromIntegerLiteral(Int) -> NSNumber [class]Removed NSNumber.numberWithBool(Bool) -> NSNumber! [class]Removed NSNumber.numberWithChar(Int8) -> NSNumber! [class]Removed NSNumber.numberWithDouble(Double) -> NSNumber! [class]Removed NSNumber.numberWithFloat(Float) -> NSNumber! [class]Removed NSNumber.numberWithInt(Int32) -> NSNumber! [class]Removed NSNumber.numberWithInteger(Int) -> NSNumber! [class]Removed NSNumber.numberWithLong(Int) -> NSNumber! [class]Removed NSNumber.numberWithLongLong(Int64) -> NSNumber! [class]Removed NSNumber.numberWithShort(Int16) -> NSNumber! [class]Removed NSNumber.numberWithUnsignedChar(UInt8) -> NSNumber! [class]Removed NSNumber.numberWithUnsignedInt(UInt32) -> NSNumber! [class]Removed NSNumber.numberWithUnsignedInteger(Int) -> NSNumber! [class]Removed NSNumber.numberWithUnsignedLong(UInt) -> NSNumber! [class]Removed NSNumber.numberWithUnsignedLongLong(UInt64) -> NSNumber! [class]Removed NSNumber.numberWithUnsignedShort(UInt16) -> NSNumber! [class]Removed NSOrderedSet.init(array: [AnyObject]!)Removed NSOrderedSet.init(array: [AnyObject]!, range: NSRange, copyItems: Bool)Removed NSOrderedSet.init(object: AnyObject!)Removed NSOrderedSet.objectAtIndexedSubscript(Int) -> AnyObject!Removed NSOrderedSet.init(orderedSet: NSOrderedSet!, range: NSRange, copyItems: Bool)Removed NSOrthography.init(dominantScript: String!, languageMap:[NSObject: AnyObject]!)Removed NSOutputStream.init(URL: NSURL!, append: Bool)Removed NSOutputStream.outputStreamToFileAtPath(String!, append: Bool) -> Self! [class]Removed NSPointerArray.pointerArrayWithOptions(NSPointerFunctionsOptions) -> NSPointerArray! [class]Removed NSPointerArray.pointerArrayWithPointerFunctions(NSPointerFunctions!) -> NSPointerArray! [class]Removed NSPointerFunctions.pointerFunctionsWithOptions(NSPointerFunctionsOptions) -> NSPointerFunctions! [class]Removed NSPort.addConnection(NSConnection!, toRunLoop: NSRunLoop!, forMode: String!)Removed NSPort.removeConnection(NSConnection!, fromRunLoop: NSRunLoop!, forMode: String!)Removed NSPortCoderRemoved NSPortCoder.decodePortObject() -> NSPort!Removed NSPortCoder.encodePortObject(NSPort!)Removed NSPortCoder.isBycopy() -> BoolRemoved NSPortCoder.isByref() -> BoolRemoved NSPortNameServerRemoved NSPortNameServer.portForName(String!) -> NSPort!Removed NSPortNameServer.portForName(String!, host: String!) -> NSPort!Removed NSPortNameServer.registerPort(NSPort!, name: String!) -> BoolRemoved NSPortNameServer.removePortForName(String!) -> BoolRemoved NSPortNameServer.systemDefaultPortNameServer() -> NSPortNameServer! [class]Removed NSPredicate.init(format: String, _: CVarArg)Removed NSPropertyListMutabilityOptions.valueRemoved NSProtocolChecker.init(target: NSObject!, protocol: Protocol!)Removed NSProxy.methodSignatureForSelector(Selector) -> NSMethodSignature!Removed NSRange.bridgeFromObjectiveC(NSValue) -> NSRange [static]Removed NSRange.bridgeToObjectiveC() -> NSValueRemoved NSRange.getMirror() -> MirrorRemoved NSRange.getObjectiveCType() -> Any.Type [static]Removed NSRegularExpression.regularExpressionWithPattern(String!, options: NSRegularExpressionOptions, error: NSErrorPointer) -> NSRegularExpression! [class]Removed NSRegularExpressionOptions.valueRemoved NSScanner.init(string: String!)Removed NSSearchPathDomainMask.valueRemoved NSSet.init(array: [AnyObject]!)Removed NSSet.getMirror() -> MirrorRemoved NSSet.makeObjectsPerformSelector(Selector)Removed NSSet.makeObjectsPerformSelector(Selector, withObject: AnyObject!)Removed NSSet.init(set: NSSet!)Removed NSSocketPortNameServerRemoved NSSocketPortNameServer.defaultNameServerPortNumberRemoved NSSocketPortNameServer.portForName(String!) -> NSPort!Removed NSSocketPortNameServer.portForName(String!, host: String!) -> NSPort!Removed NSSocketPortNameServer.portForName(String!, host: String!, nameServerPortNumber: UInt16) -> NSPort!Removed NSSocketPortNameServer.registerPort(NSPort!, name: String!) -> BoolRemoved NSSocketPortNameServer.registerPort(NSPort!, name: String!, nameServerPortNumber: UInt16) -> BoolRemoved NSSocketPortNameServer.removePortForName(String!) -> BoolRemoved NSSocketPortNameServer.sharedInstance() -> AnyObject! [class]Removed NSSortDescriptor.init(key: String!, ascending: Bool)Removed NSSortDescriptor.init(key: String!, ascending: Bool, comparator: NSComparator!)Removed NSSortDescriptor.init(key: String!, ascending: Bool, selector: Selector)Removed NSSortOptions.valueRemoved NSStreamEvent.valueRemoved NSString.convertFromExtendedGraphemeClusterLiteral(StaticString) -> Self [class]Removed NSString.convertFromStringLiteral(StaticString) -> Self [class]Removed NSString.init(format: NSString, _: CVarArg)Removed NSString.init(format: NSString, locale: NSLocale?, _: CVarArg)Removed NSString.getMirror() -> MirrorRemoved NSString.localizedStringWithFormat(NSString, _: CVarArg) -> NSString [class]Removed NSString.stringByAppendingFormat(NSString, _: CVarArg) -> NSStringRemoved NSString.stringWithCString(ConstUnsafePointer<Int8>, encoding: UInt) -> Self! [class]Removed NSString.stringWithCharacters(ConstUnsafePointer<unichar>, length: Int) -> Self! [class]Removed NSString.stringWithContentsOfFile(String!, encoding: UInt, error: NSErrorPointer) -> Self! [class]Removed NSString.stringWithContentsOfFile(String!, usedEncoding: UnsafePointer<UInt>, error: NSErrorPointer) -> Self! [class]Removed NSString.stringWithContentsOfURL(NSURL!, encoding: UInt, error: NSErrorPointer) -> Self! [class]Removed NSString.stringWithContentsOfURL(NSURL!, usedEncoding: UnsafePointer<UInt>, error: NSErrorPointer) -> Self! [class]Removed NSString.stringWithString(String!) -> Self! [class]Removed NSString.stringWithUTF8String(ConstUnsafePointer<Int8>) -> Self! [class]Removed NSStringCompareOptions.valueRemoved NSStringEncodingConversionOptions.valueRemoved NSStringEnumerationOptions.valueRemoved NSTextCheckingType.valueRemoved NSTimeZone.init(name: String!)Removed NSTimeZone.init(name: String!, data: NSData!)Removed NSURL.URLByResolvingBookmarkData(NSData!, options: NSURLBookmarkResolutionOptions, relativeToURL: NSURL!, bookmarkDataIsStale: UnsafePointer<ObjCBool>, error: NSErrorPointer) -> Self! [class]Removed NSURL.URLWithString(String!) -> Self! [class]Removed NSURL.URLWithString(String!, relativeToURL: NSURL!) -> Self! [class]Removed NSURL.getMirror() -> MirrorRemoved NSURLBookmarkCreationOptions.PreferFileIDResolutionRemoved NSURLBookmarkCreationOptions.valueRemoved NSURLBookmarkResolutionOptions.valueRemoved NSURLComponents.componentsWithString(String!) -> Self! [class]Removed NSURLComponents.componentsWithURL(NSURL!, resolvingAgainstBaseURL: Bool) -> Self! [class]Removed NSURLConnection.connectionWithRequest(NSURLRequest!, delegate: AnyObject!) -> NSURLConnection! [class]Removed NSURLCredential.credentialWithIdentity(SecIdentity!, certificates:[AnyObject]!, persistence: NSURLCredentialPersistence) -> NSURLCredential! [class]Removed NSURLCredential.credentialWithUser(String!, password: String!, persistence: NSURLCredentialPersistence) -> NSURLCredential! [class]Removed NSURLQueryItem.queryItemWithName(String!, value: String!) -> Self! [class]Removed NSUUID.UUID() -> Self! [class]Removed NSUndoManager.prepareWithInvocationTarget(T) -> TRemoved NSValue.valueWithBytes(ConstUnsafePointer<()>, objCType: ConstUnsafePointer<Int8>) -> NSValue! [class]Removed NSVolumeEnumerationOptions.valueRemoved NSXPCConnectionOptions.valueRemoved NSZone.convertFromNilLiteral() -> NSZone [static]Removed NSConnectionDidDieNotificationRemoved NSConnectionDidInitializeNotificationRemoved NSConnectionReplyModeRemoved NSCreateZone(Int, Int, Bool) -> NSZoneRemoved NSExtensionBackgroundTaskIdentifierRemoved NSExtensionJavaScriptFinalizeArgumentKeyRemoved NSFailedAuthenticationExceptionRemoved NSLog(String, CVarArg)Removed NSRecycleZone(NSZone)Removed NSSetZoneName(NSZone, String!)Removed NSZoneCalloc(NSZone, Int, Int) -> UnsafePointer<()>Removed NSZoneFree(NSZone, UnsafePointer<()>)Removed NSZoneFromPointer(UnsafePointer<()>) -> NSZoneRemoved NSZoneMalloc(NSZone, Int) -> UnsafePointer<()>Removed NSZoneName(NSZone) -> String!Removed NSZoneRealloc(NSZone, UnsafePointer<()>, Int) -> UnsafePointer<()>Added Array.init(_fromNSArray: NSArray, noCopy: Bool)Added Bool.init(_: NSNumber)Added CGFloat.init(_: NSNumber)Added Double.init(_: NSNumber)Added Float.init(_: NSNumber)Added Index.init(_: Int)Added Index.advancedBy(Int) -> String.UTF16View.IndexAdded Index.distanceTo(String.UTF16View.Index) -> IntAdded Int.init(_: NSNumber)Added NSActivityOptions.init(rawValue: UInt64)Added NSAffineTransformStruct.init()Added NSAffineTransformStruct.init(m11: CGFloat, m12: CGFloat, m21: CGFloat, m22: CGFloat, tX: CGFloat, tY: CGFloat)Added NSAlignmentOptions.init(rawValue: UInt64)Added NSAppleEventDescriptor.init(descriptorType: DescType, data: NSData)Added NSArray.init(array: NSArray)Added NSArray.init(array: [AnyObject])Added NSArray.init(arrayLiteral: AnyObject)Added NSArray.init(contentsOfFile: String)Added NSArray.init(contentsOfURL: NSURL)Added NSArray.getMirror() -> MirrorTypeAdded NSAttributedStringEnumerationOptions.init(rawValue: UInt)Added NSBinarySearchingOptions.init(rawValue: UInt)Added NSBundle.init(URL: NSURL)Added NSBundle.init(path: String)Added NSByteCountFormatterUnits.init(rawValue: UInt)Added NSCalendarOptions.init(rawValue: UInt)Added NSCalendarUnit.init(rawValue: UInt)Added NSComparisonPredicate.init(leftExpression: NSExpression, rightExpression: NSExpression, customSelector: Selector)Added NSComparisonPredicate.init(leftExpression: NSExpression, rightExpression: NSExpression, modifier: NSComparisonPredicateModifier, type: NSPredicateOperatorType, options: NSComparisonPredicateOptions)Added NSComparisonPredicateOptions.init(rawValue: UInt)Added NSData.init(contentsOfFile: String)Added NSData.init(contentsOfURL: NSURL)Added NSDataBase64DecodingOptions.init(rawValue: UInt)Added NSDataBase64EncodingOptions.init(rawValue: UInt)Added NSDataReadingOptions.init(rawValue: UInt)Added NSDataSearchOptions.init(rawValue: UInt)Added NSDataWritingOptions.init(rawValue: UInt)Added NSDate.getMirror() -> MirrorTypeAdded NSDate.init(timeInterval: NSTimeInterval, sinceDate: NSDate)Added NSDateComponentsFormatterZeroFormattingBehavior.init(rawValue: UInt)Added NSDecimal [struct]Added NSDecimal.init()Added NSDecimalNumber.init(decimal: NSDecimal)Added NSDecimalNumber.decimalValueAdded NSDictionary.init(contentsOfFile: String)Added NSDictionary.init(contentsOfURL: NSURL)Added NSDictionary.init(dictionary: NSDictionary)Added NSDictionary.init(dictionary: [NSObject: AnyObject])Added NSDictionary.init(dictionaryLiteral: (NSCopying, AnyObject))Added NSDictionary.generate() -> NSDictionary.GeneratorAdded NSDictionary.getMirror() -> MirrorTypeAdded NSDictionary.init(objects: [AnyObject], forKeys:[AnyObject])Added NSDictionary.GeneratorAdded NSDictionary.Generator.next() -> (key: AnyObject, value: AnyObject)?Added NSDirectoryEnumerationOptions.init(rawValue: UInt)Added NSDistributedLock.init(path: String)Added NSEdgeInsets.init()Added NSEdgeInsets.init(top: CGFloat, left: CGFloat, bottom: CGFloat, right: CGFloat)Added NSEnumerationOptions.init(rawValue: UInt)Added NSEnumerator.generate() -> NSFastGeneratorAdded NSException.init(name: String, reason: String?, userInfo:[NSObject: AnyObject]?)Added NSExpression.init(format: String, _: CVarArgType)Added NSFastEnumerationState.init(state: UInt, itemsPtr: AutoreleasingUnsafeMutablePointer<AnyObject?>, mutationsPtr: UnsafeMutablePointer<UInt>, extra:(UInt, UInt, UInt, UInt, UInt))Added NSFileCoordinatorReadingOptions.init(rawValue: UInt)Added NSFileCoordinatorWritingOptions.init(rawValue: UInt)Added NSFileManagerItemReplacementOptions.init(rawValue: UInt)Added NSFileVersionAddingOptions.init(rawValue: UInt)Added NSFileVersionReplacingOptions.init(rawValue: UInt)Added NSFileWrapperReadingOptions.init(rawValue: UInt)Added NSFileWrapperWritingOptions.init(rawValue: UInt)Added NSHashEnumerator.init()Added NSHashEnumerator.init(_pi: Int, _si: Int, _bs: UnsafeMutablePointer<Void>)Added NSHashTableCallBacks.init()Added NSHashTableCallBacks.init(hash: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>) -> Int)>, isEqual: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>, UnsafePointer<Void>) -> Bool)>, retain: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>) -> Void)>, release: CFunctionPointer<((NSHashTable!, UnsafeMutablePointer<Void>) -> Void)>, describe: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>) -> String!)>)Added NSIndexSet.generate() -> NSIndexSetGeneratorAdded NSIndexSetGenerator [struct]Added NSIndexSetGenerator.next() -> Int?Added NSIndexSetGenerator.init(set: NSIndexSet)Added NSInputStream.init(URL: NSURL)Added NSInputStream.init(data: NSData)Added NSJSONReadingOptions.init(rawValue: UInt)Added NSJSONWritingOptions.init(rawValue: UInt)Added NSKeyValueObservingOptions.init(rawValue: UInt)Added NSLinguisticTaggerOptions.init(rawValue: UInt)Added NSLocale.init(localeIdentifier: String)Added NSMapEnumerator.init()Added NSMapEnumerator.init(_pi: Int, _si: Int, _bs: UnsafeMutablePointer<Void>)Added NSMapTableKeyCallBacks.init()Added NSMapTableKeyCallBacks.init(hash: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> Int)>, isEqual: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>, UnsafePointer<Void>) -> Bool)>, retain: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> Void)>, release: CFunctionPointer<((NSMapTable!, UnsafeMutablePointer<Void>) -> Void)>, describe: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> String!)>, notAKeyMarker: UnsafePointer<Void>)Added NSMapTableValueCallBacks.init()Added NSMapTableValueCallBacks.init(retain: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> Void)>, release: CFunctionPointer<((NSMapTable!, UnsafeMutablePointer<Void>) -> Void)>, describe: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> String!)>)Added NSMatchingFlags.init(rawValue: UInt)Added NSMatchingOptions.init(rawValue: UInt)Added NSMutableArray.init(contentsOfFile: String)Added NSMutableArray.init(contentsOfURL: NSURL)Added NSMutableDictionary.init(contentsOfFile: String)Added NSMutableDictionary.init(contentsOfURL: NSURL)Added NSMutableString.appendFormat(NSString, _: CVarArgType)Added NSNetServiceOptions.init(rawValue: UInt)Added NSNotification.init(name: String, object: AnyObject?, userInfo:[NSObject: AnyObject]?)Added NSNumber.init(booleanLiteral: Bool)Added NSNumber.decimalValueAdded NSNumber.init(floatLiteral: Double)Added NSNumber.init(integerLiteral: Int)Added NSObject.accessInstanceVariablesDirectly() -> Bool [class]Added NSObject.addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutablePointer<Void>)Added NSObject.attemptRecoveryFromError(NSError!, optionIndex: Int) -> BoolAdded NSObject.attemptRecoveryFromError(NSError!, optionIndex: Int, delegate: AnyObject!, didRecoverSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)Added NSObject.attributeKeysAdded NSObject.autoContentAccessingProxyAdded NSObject.automaticallyNotifiesObserversForKey(String) -> Bool [class]Added NSObject.awakeAfterUsingCoder(NSCoder) -> AnyObject?Added NSObject.cancelPreviousPerformRequestsWithTarget(AnyObject) [class]Added NSObject.cancelPreviousPerformRequestsWithTarget(AnyObject, selector: Selector, object: AnyObject?) [class]Added NSObject.classCodeAdded NSObject.classDescriptionAdded NSObject.classFallbacksForKeyedArchiver() -> [AnyObject] [class]Added NSObject.classForArchiverAdded NSObject.classForCoderAdded NSObject.classForKeyedArchiverAdded NSObject.classForKeyedUnarchiver() -> AnyClass [class]Added NSObject.classNameAdded NSObject.coerceValue(AnyObject!, forKey: String!) -> AnyObject!Added NSObject.copyScriptingValue(AnyObject!, forKey: String, withProperties:[NSObject: AnyObject]!) -> AnyObject?Added NSObject.dictionaryWithValuesForKeys([AnyObject]) -> [NSObject: AnyObject]Added NSObject.didChange(NSKeyValueChange, valuesAtIndexes: NSIndexSet, forKey: String)Added NSObject.didChangeValueForKey(String)Added NSObject.didChangeValueForKey(String, withSetMutation: NSKeyValueSetMutationKind, usingObjects: Set<NSObject>)Added NSObject.doesContain(AnyObject) -> BoolAdded NSObject.encode() -> [Word]Added NSObject.hashValueAdded NSObject.indicesOfObjectsByEvaluatingObjectSpecifier(NSScriptObjectSpecifier) -> [AnyObject]?Added NSObject.insertValue(AnyObject!, inPropertyWithKey: String!)Added NSObject.insertValue(AnyObject, atIndex: Int, inPropertyWithKey: String)Added NSObject.inverseForRelationshipKey(String!) -> String!Added NSObject.isCaseInsensitiveLike(String!) -> BoolAdded NSObject.isEqualTo(AnyObject?) -> BoolAdded NSObject.isGreaterThan(AnyObject!) -> BoolAdded NSObject.isGreaterThanOrEqualTo(AnyObject!) -> BoolAdded NSObject.isLessThan(AnyObject!) -> BoolAdded NSObject.isLessThanOrEqualTo(AnyObject!) -> BoolAdded NSObject.isLike(String!) -> BoolAdded NSObject.isNotEqualTo(AnyObject!) -> BoolAdded NSObject.keyPathsForValuesAffectingValueForKey(String) -> Set<NSObject> [class]Added NSObject.mutableArrayValueForKey(String) -> NSMutableArrayAdded NSObject.mutableArrayValueForKeyPath(String) -> NSMutableArrayAdded NSObject.mutableOrderedSetValueForKey(String) -> NSMutableOrderedSetAdded NSObject.mutableOrderedSetValueForKeyPath(String) -> NSMutableOrderedSetAdded NSObject.mutableSetValueForKey(String) -> NSMutableSetAdded NSObject.mutableSetValueForKeyPath(String) -> NSMutableSetAdded NSObject.newScriptingObjectOfClass(AnyClass!, forValueForKey: String, withContentsValue: AnyObject?, properties:[NSObject: AnyObject]!) -> AnyObject?Added NSObject.objectSpecifierAdded NSObject.observationInfoAdded NSObject.observeValueForKeyPath(String, ofObject: AnyObject, change:[NSObject: AnyObject], context: UnsafeMutablePointer<Void>)Added NSObject.removeObserver(NSObject, forKeyPath: String)Added NSObject.removeObserver(NSObject, forKeyPath: String, context: UnsafeMutablePointer<Void>)Added NSObject.removeValueAtIndex(Int, fromPropertyWithKey: String)Added NSObject.replaceValueAtIndex(Int, inPropertyWithKey: String, withValue: AnyObject!)Added NSObject.replacementObjectForArchiver(NSArchiver) -> AnyObject?Added NSObject.replacementObjectForCoder(NSCoder) -> AnyObject?Added NSObject.replacementObjectForKeyedArchiver(NSKeyedArchiver) -> AnyObject?Added NSObject.scriptingBeginsWith(AnyObject!) -> BoolAdded NSObject.scriptingContains(AnyObject!) -> BoolAdded NSObject.scriptingEndsWith(AnyObject!) -> BoolAdded NSObject.scriptingIsEqualTo(AnyObject!) -> BoolAdded NSObject.scriptingIsGreaterThan(AnyObject!) -> BoolAdded NSObject.scriptingIsGreaterThanOrEqualTo(AnyObject!) -> BoolAdded NSObject.scriptingIsLessThan(AnyObject!) -> BoolAdded NSObject.scriptingIsLessThanOrEqualTo(AnyObject!) -> BoolAdded NSObject.scriptingPropertiesAdded NSObject.scriptingValueForSpecifier(NSScriptObjectSpecifier!) -> AnyObject!Added NSObject.setNilValueForKey(String)Added NSObject.setValue(AnyObject?, forKey: String)Added NSObject.setValue(AnyObject?, forKeyPath: String)Added NSObject.setValue(AnyObject?, forUndefinedKey: String)Added NSObject.setValuesForKeysWithDictionary([NSObject: AnyObject])Added NSObject.setVersion(Int) [class]Added NSObject.toManyRelationshipKeysAdded NSObject.toOneRelationshipKeysAdded NSObject.validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String, error: NSErrorPointer) -> BoolAdded NSObject.validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath: String, error: NSErrorPointer) -> BoolAdded NSObject.valueAtIndex(Int, inPropertyWithKey: String) -> AnyObject?Added NSObject.valueForKey(String) -> AnyObject?Added NSObject.valueForKeyPath(String) -> AnyObject?Added NSObject.valueForUndefinedKey(String) -> AnyObject?Added NSObject.valueWithName(String!, inPropertyWithKey: String!) -> AnyObject!Added NSObject.valueWithUniqueID(AnyObject!, inPropertyWithKey: String!) -> AnyObject!Added NSObject.version() -> Int [class]Added NSObject.willChange(NSKeyValueChange, valuesAtIndexes: NSIndexSet, forKey: String)Added NSObject.willChangeValueForKey(String)Added NSObject.willChangeValueForKey(String, withSetMutation: NSKeyValueSetMutationKind, usingObjects: Set<NSObject>)Added NSOperatingSystemVersion.init()Added NSOperatingSystemVersion.init(majorVersion: Int, minorVersion: Int, patchVersion: Int)Added NSOrderedSet.init(array: [AnyObject])Added NSOrderedSet.init(array: [AnyObject], range: NSRange, copyItems: Bool)Added NSOrderedSet.init(arrayLiteral: AnyObject)Added NSOrderedSet.generate() -> NSFastGeneratorAdded NSOrderedSet.init(object: AnyObject)Added NSOrderedSet.init(orderedSet: NSOrderedSet)Added NSOrderedSet.init(orderedSet: NSOrderedSet, range: NSRange, copyItems: Bool)Added NSOrderedSet.init(set: Set<NSObject>)Added NSOrderedSet.init(set: Set<NSObject>, copyItems: Bool)Added NSOrthography.init(dominantScript: String, languageMap:[NSObject: AnyObject])Added NSOutputStream.init(URL: NSURL, append: Bool)Added NSPredicate.init(format: String, _: CVarArgType)Added NSProcessInfo.thermalStateAdded NSProcessInfoThermalState [enum]Added NSProcessInfoThermalState.CriticalAdded NSProcessInfoThermalState.FairAdded NSProcessInfoThermalState.NominalAdded NSProcessInfoThermalState.SeriousAdded NSPropertyListMutabilityOptions.init(rawValue: UInt)Added NSProtocolChecker.init(target: NSObject, protocol: Protocol)Added NSRange.getMirror() -> MirrorTypeAdded NSRegularExpressionOptions.init(rawValue: UInt)Added NSScanner.init(string: String)Added NSSearchPathDomainMask.init(rawValue: UInt)Added NSSet.init(array: [AnyObject])Added NSSet.init(arrayLiteral: AnyObject)Added NSSet.getMirror() -> MirrorTypeAdded NSSet.init(set: NSSet)Added NSSet.init(set: Set<NSObject>)Added NSSortDescriptor.init(key: String, ascending: Bool)Added NSSortDescriptor.init(key: String, ascending: Bool, comparator: NSComparator)Added NSSortDescriptor.init(key: String, ascending: Bool, selector: Selector)Added NSSortOptions.init(rawValue: UInt)Added NSStreamEvent.init(rawValue: UInt)Added NSString.init(extendedGraphemeClusterLiteral: StaticString)Added NSString.init(format: NSString, _: CVarArgType)Added NSString.init(format: NSString, locale: NSLocale?, _: CVarArgType)Added NSString.getMirror() -> MirrorTypeAdded NSString.localizedStringWithFormat(NSString, _: CVarArgType) -> Self [class]Added NSString.init(string: NSString)Added NSString.stringByAppendingFormat(NSString, _: CVarArgType) -> NSStringAdded NSString.init(stringLiteral: StaticString)Added NSString.init(unicodeScalarLiteral: StaticString)Added NSStringCompareOptions.init(rawValue: UInt)Added NSStringEncodingConversionOptions.init(rawValue: UInt)Added NSStringEnumerationOptions.init(rawValue: UInt)Added NSSwappedDouble.init()Added NSSwappedDouble.init(v: UInt64)Added NSSwappedFloat.init()Added NSSwappedFloat.init(v: UInt32)Added NSTextCheckingType.init(rawValue: UInt64)Added NSTimeZone.init(name: String)Added NSTimeZone.init(name: String, data: NSData?)Added NSURL.getMirror() -> MirrorTypeAdded NSURLBookmarkCreationOptions.init(rawValue: UInt)Added NSURLBookmarkResolutionOptions.init(rawValue: UInt)Added NSUserNotification.contentImageAdded NSValue.init(edgeInsets: NSEdgeInsets)Added NSValue.edgeInsetsValueAdded NSVolumeEnumerationOptions.init(rawValue: UInt)Added NSXMLParser.allowedExternalEntityURLsAdded NSXMLParser.externalEntityResolvingPolicyAdded NSXMLParserExternalEntityResolvingPolicy [enum]Added NSXMLParserExternalEntityResolvingPolicy.ResolveExternalEntitiesAlwaysAdded NSXMLParserExternalEntityResolvingPolicy.ResolveExternalEntitiesNeverAdded NSXMLParserExternalEntityResolvingPolicy.ResolveExternalEntitiesNoNetworkAdded NSXMLParserExternalEntityResolvingPolicy.ResolveExternalEntitiesSameOriginOnlyAdded NSXPCConnectionOptions.init(rawValue: UInt)Added String.init(CString: UnsafePointer<CChar>, encoding: NSStringEncoding)Added String.init(UTF8String: UnsafePointer<CChar>)Added String.init(_: NSString)Added String.availableStringEncodings() -> [NSStringEncoding] [static]Added String.init(bytes: S, encoding: NSStringEncoding)Added String.init(bytesNoCopy: UnsafeMutablePointer<Void>, length: Int, encoding: NSStringEncoding, freeWhenDone: Bool)Added String.cStringUsingEncoding(NSStringEncoding) -> [CChar]?Added String.canBeConvertedToEncoding(NSStringEncoding) -> BoolAdded String.capitalizedStringAdded String.capitalizedStringWithLocale(NSLocale?) -> StringAdded String.caseInsensitiveCompare(String) -> NSComparisonResultAdded String.commonPrefixWithString(String, options: NSStringCompareOptions) -> StringAdded String.compare(String, options: NSStringCompareOptions, range: Range<String.Index>?, locale: NSLocale?) -> NSComparisonResultAdded String.completePathIntoString(UnsafeMutablePointer<String>, caseSensitive: Bool, matchesIntoArray: UnsafeMutablePointer<[String]>, filterTypes:[String]?) -> IntAdded String.componentsSeparatedByCharactersInSet(NSCharacterSet) -> [String]Added String.componentsSeparatedByString(String) -> [String]Added String.init(contentsOfFile: String, encoding: NSStringEncoding, error: NSErrorPointer)Added String.init(contentsOfFile: String, usedEncoding: UnsafeMutablePointer<NSStringEncoding>, error: NSErrorPointer)Added String.init(contentsOfURL: NSURL, encoding: NSStringEncoding, error: NSErrorPointer)Added String.init(contentsOfURL: NSURL, usedEncoding: UnsafeMutablePointer<NSStringEncoding>, error: NSErrorPointer)Added String.dataUsingEncoding(NSStringEncoding, allowLossyConversion: Bool) -> NSData?Added String.decomposedStringWithCanonicalMappingAdded String.decomposedStringWithCompatibilityMappingAdded String.defaultCStringEncoding() -> NSStringEncoding [static]Added String.enumerateLines((line: String, inoutstop: Bool) -> ())Added String.enumerateLinguisticTagsInRange(Range<String.Index>, scheme: String, options: NSLinguisticTaggerOptions, orthography: NSOrthography?, _:(String, Range<String.Index>, Range<String.Index>, inoutBool) -> ())Added String.enumerateSubstringsInRange(Range<String.Index>, options: NSStringEnumerationOptions, _:(substring: String, substringRange: Range<String.Index>, enclosingRange: Range<String.Index>, inoutBool) -> ())Added String.fastestEncodingAdded String.fileSystemRepresentation() -> [CChar]Added String.init(format: String, _: CVarArgType)Added String.init(format: String, arguments:[CVarArgType])Added String.init(format: String, locale: NSLocale?, _: CVarArgType)Added String.init(format: String, locale: NSLocale?, arguments:[CVarArgType])Added String.getBytes([UInt8], maxLength: Int, usedLength: UnsafeMutablePointer<Int>, encoding: NSStringEncoding, options: NSStringEncodingConversionOptions, range: Range<String.Index>, remainingRange: UnsafeMutablePointer<Range<String.Index>>) -> BoolAdded String.getCString([CChar], maxLength: Int, encoding: NSStringEncoding) -> BoolAdded String.getFileSystemRepresentation([CChar], maxLength: Int) -> BoolAdded String.getLineStart(UnsafeMutablePointer<String.Index>, end: UnsafeMutablePointer<String.Index>, contentsEnd: UnsafeMutablePointer<String.Index>, forRange: Range<String.Index>)Added String.getParagraphStart(UnsafeMutablePointer<String.Index>, end: UnsafeMutablePointer<String.Index>, contentsEnd: UnsafeMutablePointer<String.Index>, forRange: Range<String.Index>)Added String.hashAdded String.lastPathComponentAdded String.lengthOfBytesUsingEncoding(NSStringEncoding) -> IntAdded String.lineRangeForRange(Range<String.Index>) -> Range<String.Index>Added String.linguisticTagsInRange(Range<String.Index>, scheme: String, options: NSLinguisticTaggerOptions, orthography: NSOrthography?, tokenRanges: UnsafeMutablePointer<[Range<String.Index>]>) -> [String]Added String.localizedCaseInsensitiveCompare(String) -> NSComparisonResultAdded String.localizedCompare(String) -> NSComparisonResultAdded String.localizedNameOfStringEncoding(NSStringEncoding) -> String [static]Added String.localizedStandardCompare(String) -> NSComparisonResultAdded String.localizedStringWithFormat(String, _: CVarArgType) -> String [static]Added String.lowercaseStringWithLocale(NSLocale) -> StringAdded String.maximumLengthOfBytesUsingEncoding(NSStringEncoding) -> IntAdded String.paragraphRangeForRange(Range<String.Index>) -> Range<String.Index>Added String.pathComponentsAdded String.pathExtensionAdded String.pathWithComponents([String]) -> String [static]Added String.precomposedStringWithCanonicalMappingAdded String.precomposedStringWithCompatibilityMappingAdded String.propertyList() -> AnyObjectAdded String.propertyListFromStringsFileFormat() -> [String: String]Added String.rangeOfCharacterFromSet(NSCharacterSet, options: NSStringCompareOptions, range: Range<String.Index>?) -> Range<String.Index>?Added String.rangeOfComposedCharacterSequenceAtIndex(String.Index) -> Range<String.Index>Added String.rangeOfComposedCharacterSequencesForRange(Range<String.Index>) -> Range<String.Index>Added String.rangeOfString(String, options: NSStringCompareOptions, range: Range<String.Index>?, locale: NSLocale?) -> Range<String.Index>?Added String.smallestEncodingAdded String.stringByAbbreviatingWithTildeInPathAdded String.stringByAddingPercentEncodingWithAllowedCharacters(NSCharacterSet) -> String?Added String.stringByAddingPercentEscapesUsingEncoding(NSStringEncoding) -> String?Added String.stringByAppendingFormat(String, _: CVarArgType) -> StringAdded String.stringByAppendingPathComponent(String) -> StringAdded String.stringByAppendingPathExtension(String) -> String?Added String.stringByAppendingString(String) -> StringAdded String.stringByDeletingLastPathComponentAdded String.stringByDeletingPathExtensionAdded String.stringByExpandingTildeInPathAdded String.stringByFoldingWithOptions(NSStringCompareOptions, locale: NSLocale) -> StringAdded String.stringByPaddingToLength(Int, withString: String, startingAtIndex: Int) -> StringAdded String.stringByRemovingPercentEncodingAdded String.stringByReplacingCharactersInRange(Range<String.Index>, withString: String) -> StringAdded String.stringByReplacingOccurrencesOfString(String, withString: String, options: NSStringCompareOptions, range: Range<String.Index>?) -> StringAdded String.stringByReplacingPercentEscapesUsingEncoding(NSStringEncoding) -> String?Added String.stringByResolvingSymlinksInPathAdded String.stringByStandardizingPathAdded String.stringByTrimmingCharactersInSet(NSCharacterSet) -> StringAdded String.stringsByAppendingPaths([String]) -> [String]Added String.substringFromIndex(String.Index) -> StringAdded String.substringToIndex(String.Index) -> StringAdded String.substringWithRange(Range<String.Index>) -> StringAdded String.uppercaseStringWithLocale(NSLocale) -> StringAdded String.init(utf16CodeUnits: UnsafePointer<unichar>, count: Int)Added String.init(utf16CodeUnitsNoCopy: UnsafePointer<unichar>, count: Int, freeWhenDone: Bool)Added String.writeToFile(String, atomically: Bool, encoding: NSStringEncoding, error: NSErrorPointer) -> BoolAdded String.writeToURL(NSURL, atomically: Bool, encoding: NSStringEncoding, error: NSErrorPointer) -> BoolAdded UInt.init(_: NSNumber)Added NSEDGEINSETS_DEFINEDAdded NSEdgeInsetsEqual(NSEdgeInsets, NSEdgeInsets) -> BoolAdded NSEdgeInsetsZeroAdded NSIndexSetGenerator.ElementAdded NSLog(String, CVarArgType)Added NSMaxXEdgeAdded NSMaxYEdgeAdded NSMinXEdgeAdded NSMinYEdgeAdded NSProcessInfoThermalStateDidChangeNotificationAdded NSUserActivityConnectionUnavailableErrorAdded NSUserActivityErrorMaximumAdded NSUserActivityErrorMinimumAdded NSUserActivityHandoffFailedErrorAdded NSUserActivityHandoffUserInfoTooLargeErrorAdded NSUserActivityRemoteApplicationTimedOutErrorModified NSActivityOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct NSActivityOptions : RawOptionSet {     init(_ value: UInt64)     var value: UInt64     static var IdleDisplaySleepDisabled: NSActivityOptions { get }     static var IdleSystemSleepDisabled: NSActivityOptions { get }     static var SuddenTerminationDisabled: NSActivityOptions { get }     static var AutomaticTerminationDisabled: NSActivityOptions { get }     static var UserInitiated: NSActivityOptions { get }     static var UserInitiatedAllowingIdleSystemSleep: NSActivityOptions { get }     static var Background: NSActivityOptions { get }     static var LatencyCritical: NSActivityOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct NSActivityOptions : RawOptionSetType {     init(_ rawValue: UInt64)     init(rawValue rawValue: UInt64)     static var IdleDisplaySleepDisabled: NSActivityOptions { get }     static var IdleSystemSleepDisabled: NSActivityOptions { get }     static var SuddenTerminationDisabled: NSActivityOptions { get }     static var AutomaticTerminationDisabled: NSActivityOptions { get }     static var UserInitiated: NSActivityOptions { get }     static var UserInitiatedAllowingIdleSystemSleep: NSActivityOptions { get }     static var Background: NSActivityOptions { get }     static var LatencyCritical: NSActivityOptions { get } } ``` | RawOptionSetType | OS X 10.9 |

Modified NSActivityOptions.init(_: UInt64)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt64) ``` |
| To | ``` init(_ rawValue: UInt64) ``` |

Modified NSAffineTransform.appendTransform(NSAffineTransform)

|  | Declaration |
| --- | --- |
| From | ``` func appendTransform(_ transform: NSAffineTransform!) ``` |
| To | ``` func appendTransform(_ transform: NSAffineTransform) ``` |

Modified NSAffineTransform.prependTransform(NSAffineTransform)

|  | Declaration |
| --- | --- |
| From | ``` func prependTransform(_ transform: NSAffineTransform!) ``` |
| To | ``` func prependTransform(_ transform: NSAffineTransform) ``` |

Modified NSAffineTransform.init(transform: NSAffineTransform)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(transform transform: NSAffineTransform!) ``` |
| To | ``` convenience init(transform transform: NSAffineTransform) ``` |

Modified NSAffineTransformStruct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSAffineTransformStruct {     var m11: CGFloat     var m12: CGFloat     var m21: CGFloat     var m22: CGFloat     var tX: CGFloat     var tY: CGFloat } ``` |
| To | ``` struct NSAffineTransformStruct {     var m11: CGFloat     var m12: CGFloat     var m21: CGFloat     var m22: CGFloat     var tX: CGFloat     var tY: CGFloat     init()     init(m11 m11: CGFloat, m12 m12: CGFloat, m21 m21: CGFloat, m22 m22: CGFloat, tX tX: CGFloat, tY tY: CGFloat) } ``` |

Modified NSAlignmentOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSAlignmentOptions : RawOptionSet {     init(_ value: UInt64)     var value: UInt64     static var AlignMinXInward: NSAlignmentOptions { get }     static var AlignMinYInward: NSAlignmentOptions { get }     static var AlignMaxXInward: NSAlignmentOptions { get }     static var AlignMaxYInward: NSAlignmentOptions { get }     static var AlignWidthInward: NSAlignmentOptions { get }     static var AlignHeightInward: NSAlignmentOptions { get }     static var AlignMinXOutward: NSAlignmentOptions { get }     static var AlignMinYOutward: NSAlignmentOptions { get }     static var AlignMaxXOutward: NSAlignmentOptions { get }     static var AlignMaxYOutward: NSAlignmentOptions { get }     static var AlignWidthOutward: NSAlignmentOptions { get }     static var AlignHeightOutward: NSAlignmentOptions { get }     static var AlignMinXNearest: NSAlignmentOptions { get }     static var AlignMinYNearest: NSAlignmentOptions { get }     static var AlignMaxXNearest: NSAlignmentOptions { get }     static var AlignMaxYNearest: NSAlignmentOptions { get }     static var AlignWidthNearest: NSAlignmentOptions { get }     static var AlignHeightNearest: NSAlignmentOptions { get }     static var AlignRectFlipped: NSAlignmentOptions { get }     static var AlignAllEdgesInward: NSAlignmentOptions { get }     static var AlignAllEdgesOutward: NSAlignmentOptions { get }     static var AlignAllEdgesNearest: NSAlignmentOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSAlignmentOptions : RawOptionSetType {     init(_ rawValue: UInt64)     init(rawValue rawValue: UInt64)     static var AlignMinXInward: NSAlignmentOptions { get }     static var AlignMinYInward: NSAlignmentOptions { get }     static var AlignMaxXInward: NSAlignmentOptions { get }     static var AlignMaxYInward: NSAlignmentOptions { get }     static var AlignWidthInward: NSAlignmentOptions { get }     static var AlignHeightInward: NSAlignmentOptions { get }     static var AlignMinXOutward: NSAlignmentOptions { get }     static var AlignMinYOutward: NSAlignmentOptions { get }     static var AlignMaxXOutward: NSAlignmentOptions { get }     static var AlignMaxYOutward: NSAlignmentOptions { get }     static var AlignWidthOutward: NSAlignmentOptions { get }     static var AlignHeightOutward: NSAlignmentOptions { get }     static var AlignMinXNearest: NSAlignmentOptions { get }     static var AlignMinYNearest: NSAlignmentOptions { get }     static var AlignMaxXNearest: NSAlignmentOptions { get }     static var AlignMaxYNearest: NSAlignmentOptions { get }     static var AlignWidthNearest: NSAlignmentOptions { get }     static var AlignHeightNearest: NSAlignmentOptions { get }     static var AlignRectFlipped: NSAlignmentOptions { get }     static var AlignAllEdgesInward: NSAlignmentOptions { get }     static var AlignAllEdgesOutward: NSAlignmentOptions { get }     static var AlignAllEdgesNearest: NSAlignmentOptions { get } } ``` | RawOptionSetType |

Modified NSAlignmentOptions.init(_: UInt64)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt64) ``` |
| To | ``` init(_ rawValue: UInt64) ``` |

Modified NSAppleEventDescriptor.init(AEDescNoCopy: UnsafePointer<AEDesc>)

|  | Declaration |
| --- | --- |
| From | ``` init(AEDescNoCopy aeDesc: ConstUnsafePointer<AEDesc>) ``` |
| To | ``` init(AEDescNoCopy aeDesc: UnsafePointer<AEDesc>) ``` |

Modified NSAppleEventDescriptor.aeDesc

|  | Declaration |
| --- | --- |
| From | ``` var aeDesc: ConstUnsafePointer<AEDesc> { get } ``` |
| To | ``` var aeDesc: UnsafePointer<AEDesc> { get } ``` |

Modified NSAppleEventDescriptor.appleEventWithEventClass(AEEventClass, eventID: AEEventID, targetDescriptor: NSAppleEventDescriptor?, returnID: AEReturnID, transactionID: AETransactionID) -> NSAppleEventDescriptor? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func appleEventWithEventClass(_ eventClass: AEEventClass, eventID eventID: AEEventID, targetDescriptor targetDescriptor: NSAppleEventDescriptor!, returnID returnID: AEReturnID, transactionID transactionID: AETransactionID) -> NSAppleEventDescriptor! ``` |
| To | ``` class func appleEventWithEventClass(_ eventClass: AEEventClass, eventID eventID: AEEventID, targetDescriptor targetDescriptor: NSAppleEventDescriptor?, returnID returnID: AEReturnID, transactionID transactionID: AETransactionID) -> NSAppleEventDescriptor? ``` |

Modified NSAppleEventDescriptor.attributeDescriptorForKeyword(AEKeyword) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func attributeDescriptorForKeyword(_ keyword: AEKeyword) -> NSAppleEventDescriptor! ``` |
| To | ``` func attributeDescriptorForKeyword(_ keyword: AEKeyword) -> NSAppleEventDescriptor? ``` |

Modified NSAppleEventDescriptor.init(boolean: Boolean)

|  | Declaration |
| --- | --- |
| From | ``` init(boolean boolean: Boolean) -> NSAppleEventDescriptor ``` |
| To | ``` init?(boolean boolean: Boolean) -> NSAppleEventDescriptor ``` |

Modified NSAppleEventDescriptor.coerceToDescriptorType(DescType) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func coerceToDescriptorType(_ descriptorType: DescType) -> NSAppleEventDescriptor! ``` |
| To | ``` func coerceToDescriptorType(_ descriptorType: DescType) -> NSAppleEventDescriptor? ``` |

Modified NSAppleEventDescriptor.data

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData! { get } ``` |
| To | ``` @NSCopying var data: NSData { get } ``` |

Modified NSAppleEventDescriptor.descriptorAtIndex(Int) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func descriptorAtIndex(_ index: Int) -> NSAppleEventDescriptor! ``` |
| To | ``` func descriptorAtIndex(_ index: Int) -> NSAppleEventDescriptor? ``` |

Modified NSAppleEventDescriptor.descriptorForKeyword(AEKeyword) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func descriptorForKeyword(_ keyword: AEKeyword) -> NSAppleEventDescriptor! ``` |
| To | ``` func descriptorForKeyword(_ keyword: AEKeyword) -> NSAppleEventDescriptor? ``` |

Modified NSAppleEventDescriptor.init(descriptorType: DescType, bytes: UnsafePointer<Void>, length: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(descriptorType descriptorType: DescType, bytes bytes: ConstUnsafePointer<()>, length byteCount: Int) ``` |
| To | ``` convenience init?(descriptorType descriptorType: DescType, bytes bytes: UnsafePointer<Void>, length byteCount: Int) ``` |

Modified NSAppleEventDescriptor.init(enumCode: OSType)

|  | Declaration |
| --- | --- |
| From | ``` init(enumCode enumerator: OSType) -> NSAppleEventDescriptor ``` |
| To | ``` init?(enumCode enumerator: OSType) -> NSAppleEventDescriptor ``` |

Modified NSAppleEventDescriptor.init(eventClass: AEEventClass, eventID: AEEventID, targetDescriptor: NSAppleEventDescriptor?, returnID: AEReturnID, transactionID: AETransactionID)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(eventClass eventClass: AEEventClass, eventID eventID: AEEventID, targetDescriptor targetDescriptor: NSAppleEventDescriptor!, returnID returnID: AEReturnID, transactionID transactionID: AETransactionID) ``` |
| To | ``` convenience init?(eventClass eventClass: AEEventClass, eventID eventID: AEEventID, targetDescriptor targetDescriptor: NSAppleEventDescriptor?, returnID returnID: AEReturnID, transactionID transactionID: AETransactionID) ``` |

Modified NSAppleEventDescriptor.insertDescriptor(NSAppleEventDescriptor, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insertDescriptor(_ descriptor: NSAppleEventDescriptor!, atIndex index: Int) ``` |
| To | ``` func insertDescriptor(_ descriptor: NSAppleEventDescriptor, atIndex index: Int) ``` |

Modified NSAppleEventDescriptor.init(int32: Int32)

|  | Declaration |
| --- | --- |
| From | ``` init(int32 signedInt: Int32) -> NSAppleEventDescriptor ``` |
| To | ``` init?(int32 signedInt: Int32) -> NSAppleEventDescriptor ``` |

Modified NSAppleEventDescriptor.init(listDescriptor: ())

|  | Declaration |
| --- | --- |
| From | ``` convenience init(listDescriptor listDescriptor: ()) ``` |
| To | ``` convenience init?(listDescriptor listDescriptor: ()) ``` |

Modified NSAppleEventDescriptor.listDescriptor() -> NSAppleEventDescriptor? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func listDescriptor() -> NSAppleEventDescriptor! ``` |
| To | ``` class func listDescriptor() -> NSAppleEventDescriptor? ``` |

Modified NSAppleEventDescriptor.nullDescriptor() -> NSAppleEventDescriptor? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func nullDescriptor() -> NSAppleEventDescriptor! ``` |
| To | ``` class func nullDescriptor() -> NSAppleEventDescriptor? ``` |

Modified NSAppleEventDescriptor.paramDescriptorForKeyword(AEKeyword) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func paramDescriptorForKeyword(_ keyword: AEKeyword) -> NSAppleEventDescriptor! ``` |
| To | ``` func paramDescriptorForKeyword(_ keyword: AEKeyword) -> NSAppleEventDescriptor? ``` |

Modified NSAppleEventDescriptor.init(recordDescriptor: ())

|  | Declaration |
| --- | --- |
| From | ``` convenience init(recordDescriptor recordDescriptor: ()) ``` |
| To | ``` convenience init?(recordDescriptor recordDescriptor: ()) ``` |

Modified NSAppleEventDescriptor.recordDescriptor() -> NSAppleEventDescriptor? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func recordDescriptor() -> NSAppleEventDescriptor! ``` |
| To | ``` class func recordDescriptor() -> NSAppleEventDescriptor? ``` |

Modified NSAppleEventDescriptor.setAttributeDescriptor(NSAppleEventDescriptor, forKeyword: AEKeyword)

|  | Declaration |
| --- | --- |
| From | ``` func setAttributeDescriptor(_ descriptor: NSAppleEventDescriptor!, forKeyword keyword: AEKeyword) ``` |
| To | ``` func setAttributeDescriptor(_ descriptor: NSAppleEventDescriptor, forKeyword keyword: AEKeyword) ``` |

Modified NSAppleEventDescriptor.setDescriptor(NSAppleEventDescriptor, forKeyword: AEKeyword)

|  | Declaration |
| --- | --- |
| From | ``` func setDescriptor(_ descriptor: NSAppleEventDescriptor!, forKeyword keyword: AEKeyword) ``` |
| To | ``` func setDescriptor(_ descriptor: NSAppleEventDescriptor, forKeyword keyword: AEKeyword) ``` |

Modified NSAppleEventDescriptor.setParamDescriptor(NSAppleEventDescriptor, forKeyword: AEKeyword)

|  | Declaration |
| --- | --- |
| From | ``` func setParamDescriptor(_ descriptor: NSAppleEventDescriptor!, forKeyword keyword: AEKeyword) ``` |
| To | ``` func setParamDescriptor(_ descriptor: NSAppleEventDescriptor, forKeyword keyword: AEKeyword) ``` |

Modified NSAppleEventDescriptor.init(string: String)

|  | Declaration |
| --- | --- |
| From | ``` init(string string: String!) -> NSAppleEventDescriptor ``` |
| To | ``` init?(string string: String) -> NSAppleEventDescriptor ``` |

Modified NSAppleEventDescriptor.stringValue

|  | Declaration |
| --- | --- |
| From | ``` var stringValue: String! { get } ``` |
| To | ``` var stringValue: String? { get } ``` |

Modified NSAppleEventDescriptor.init(typeCode: OSType)

|  | Declaration |
| --- | --- |
| From | ``` init(typeCode typeCode: OSType) -> NSAppleEventDescriptor ``` |
| To | ``` init?(typeCode typeCode: OSType) -> NSAppleEventDescriptor ``` |

Modified NSAppleEventManager.appleEventForSuspensionID(NSAppleEventManagerSuspensionID) -> NSAppleEventDescriptor

|  | Declaration |
| --- | --- |
| From | ``` func appleEventForSuspensionID(_ suspensionID: NSAppleEventManagerSuspensionID) -> NSAppleEventDescriptor! ``` |
| To | ``` func appleEventForSuspensionID(_ suspensionID: NSAppleEventManagerSuspensionID) -> NSAppleEventDescriptor ``` |

Modified NSAppleEventManager.currentAppleEvent

|  | Declaration |
| --- | --- |
| From | ``` var currentAppleEvent: NSAppleEventDescriptor! { get } ``` |
| To | ``` var currentAppleEvent: NSAppleEventDescriptor? { get } ``` |

Modified NSAppleEventManager.currentReplyAppleEvent

|  | Declaration |
| --- | --- |
| From | ``` var currentReplyAppleEvent: NSAppleEventDescriptor! { get } ``` |
| To | ``` var currentReplyAppleEvent: NSAppleEventDescriptor? { get } ``` |

Modified NSAppleEventManager.dispatchRawAppleEvent(UnsafePointer<AppleEvent>, withRawReply: UnsafeMutablePointer<AppleEvent>, handlerRefCon: SRefCon) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func dispatchRawAppleEvent(_ theAppleEvent: ConstUnsafePointer<AppleEvent>, withRawReply theReply: UnsafePointer<AppleEvent>, handlerRefCon handlerRefCon: SRefCon) -> OSErr ``` |
| To | ``` func dispatchRawAppleEvent(_ theAppleEvent: UnsafePointer<AppleEvent>, withRawReply theReply: UnsafeMutablePointer<AppleEvent>, handlerRefCon handlerRefCon: SRefCon) -> OSErr ``` |

Modified NSAppleEventManager.replyAppleEventForSuspensionID(NSAppleEventManagerSuspensionID) -> NSAppleEventDescriptor

|  | Declaration |
| --- | --- |
| From | ``` func replyAppleEventForSuspensionID(_ suspensionID: NSAppleEventManagerSuspensionID) -> NSAppleEventDescriptor! ``` |
| To | ``` func replyAppleEventForSuspensionID(_ suspensionID: NSAppleEventManagerSuspensionID) -> NSAppleEventDescriptor ``` |

Modified NSAppleEventManager.setEventHandler(AnyObject, andSelector: Selector, forEventClass: AEEventClass, andEventID: AEEventID)

|  | Declaration |
| --- | --- |
| From | ``` func setEventHandler(_ handler: AnyObject!, andSelector handleEventSelector: Selector, forEventClass eventClass: AEEventClass, andEventID eventID: AEEventID) ``` |
| To | ``` func setEventHandler(_ handler: AnyObject, andSelector handleEventSelector: Selector, forEventClass eventClass: AEEventClass, andEventID eventID: AEEventID) ``` |

Modified NSAppleEventManager.sharedAppleEventManager() -> NSAppleEventManager [class]

|  | Declaration |
| --- | --- |
| From | ``` class func sharedAppleEventManager() -> NSAppleEventManager! ``` |
| To | ``` class func sharedAppleEventManager() -> NSAppleEventManager ``` |

Modified NSAppleScript.compileAndReturnError(AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func compileAndReturnError(_ errorInfo: AutoreleasingUnsafePointer<NSDictionary?>) -> Bool ``` |
| To | ``` func compileAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool ``` |

Modified NSAppleScript.init(contentsOfURL: NSURL, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL url: NSURL!, error errorInfo: AutoreleasingUnsafePointer<NSDictionary?>) ``` |
| To | ``` init?(contentsOfURL url: NSURL, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) ``` |

Modified NSAppleScript.executeAndReturnError(AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func executeAndReturnError(_ errorInfo: AutoreleasingUnsafePointer<NSDictionary?>) -> NSAppleEventDescriptor! ``` |
| To | ``` func executeAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor? ``` |

Modified NSAppleScript.executeAppleEvent(NSAppleEventDescriptor, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func executeAppleEvent(_ event: NSAppleEventDescriptor!, error errorInfo: AutoreleasingUnsafePointer<NSDictionary?>) -> NSAppleEventDescriptor! ``` |
| To | ``` func executeAppleEvent(_ event: NSAppleEventDescriptor, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor? ``` |

Modified NSAppleScript.source

|  | Declaration |
| --- | --- |
| From | ``` var source: String! { get } ``` |
| To | ``` var source: String? { get } ``` |

Modified NSAppleScript.init(source: String)

|  | Declaration |
| --- | --- |
| From | ``` init(source source: String!) ``` |
| To | ``` init?(source source: String) ``` |

Modified NSArchiver.archiveRootObject(AnyObject, toFile: String) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func archiveRootObject(_ rootObject: AnyObject!, toFile path: String!) -> Bool ``` |
| To | ``` class func archiveRootObject(_ rootObject: AnyObject, toFile path: String) -> Bool ``` |

Modified NSArchiver.archivedDataWithRootObject(AnyObject) -> NSData [class]

|  | Declaration |
| --- | --- |
| From | ``` class func archivedDataWithRootObject(_ rootObject: AnyObject!) -> NSData! ``` |
| To | ``` class func archivedDataWithRootObject(_ rootObject: AnyObject) -> NSData ``` |

Modified NSArchiver.archiverData

|  | Declaration |
| --- | --- |
| From | ``` var archiverData: NSMutableData! { get } ``` |
| To | ``` var archiverData: NSMutableData { get } ``` |

Modified NSArchiver.classNameEncodedForTrueClassName(String) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func classNameEncodedForTrueClassName(_ trueName: String!) -> String! ``` |
| To | ``` func classNameEncodedForTrueClassName(_ trueName: String) -> String? ``` |

Modified NSArchiver.encodeClassName(String, intoClassName: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeClassName(_ trueName: String!, intoClassName inArchiveName: String!) ``` |
| To | ``` func encodeClassName(_ trueName: String, intoClassName inArchiveName: String) ``` |

Modified NSArchiver.encodeConditionalObject(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func encodeConditionalObject(_ object: AnyObject!) ``` |
| To | ``` func encodeConditionalObject(_ object: AnyObject?) ``` |

Modified NSArchiver.encodeRootObject(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func encodeRootObject(_ rootObject: AnyObject!) ``` |
| To | ``` func encodeRootObject(_ rootObject: AnyObject) ``` |

Modified NSArchiver.init(forWritingWithMutableData: NSMutableData)

|  | Declaration |
| --- | --- |
| From | ``` init(forWritingWithMutableData mdata: NSMutableData!) ``` |
| To | ``` init(forWritingWithMutableData mdata: NSMutableData) ``` |

Modified NSArchiver.replaceObject(AnyObject, withObject: AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func replaceObject(_ object: AnyObject!, withObject newObject: AnyObject!) ``` |
| To | ``` func replaceObject(_ object: AnyObject, withObject newObject: AnyObject) ``` |

Modified NSArray

|  | Protocols |
| --- | --- |
| From | AnyObject, ArrayLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, Reflectable, Sequence |
| To | AnyObject, ArrayLiteralConvertible, CKRecordValue, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSObjectProtocol, NSSecureCoding, Reflectable, SequenceType |

Modified NSArray.addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func addObserver(_ observer: NSObject!, forKeyPath keyPath: String!, options options: NSKeyValueObservingOptions, context context: UnsafePointer<()>) ``` |
| To | ``` func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>) ``` |

Modified NSArray.addObserver(NSObject, toObjectsAtIndexes: NSIndexSet, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func addObserver(_ observer: NSObject!, toObjectsAtIndexes indexes: NSIndexSet!, forKeyPath keyPath: String!, options options: NSKeyValueObservingOptions, context context: UnsafePointer<()>) ``` |
| To | ``` func addObserver(_ observer: NSObject, toObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>) ``` |

Modified NSArray.init(array: [AnyObject], copyItems: Bool)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(array array: [AnyObject]!, copyItems flag: Bool) ``` |
| To | ``` convenience init(array array: [AnyObject], copyItems flag: Bool) ``` |

Modified NSArray.arrayByAddingObject(AnyObject) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func arrayByAddingObject(_ anObject: AnyObject!) -> [AnyObject]! ``` |
| To | ``` func arrayByAddingObject(_ anObject: AnyObject) -> [AnyObject] ``` |

Modified NSArray.arrayByAddingObjectsFromArray([AnyObject]) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func arrayByAddingObjectsFromArray(_ otherArray: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func arrayByAddingObjectsFromArray(_ otherArray: [AnyObject]) -> [AnyObject] ``` |

Modified NSArray.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init(coder aDecoder: NSCoder) ``` |

Modified NSArray.componentsJoinedByString(String) -> String

|  | Declaration |
| --- | --- |
| From | ``` func componentsJoinedByString(_ separator: String!) -> String! ``` |
| To | ``` func componentsJoinedByString(_ separator: String) -> String ``` |

Modified NSArray.containsObject(AnyObject) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func containsObject(_ anObject: AnyObject!) -> Bool ``` |
| To | ``` func containsObject(_ anObject: AnyObject) -> Bool ``` |

Modified NSArray.description

|  | Declaration |
| --- | --- |
| From | ``` var description: String! { get } ``` |
| To | ``` var description: String { get } ``` |

Modified NSArray.descriptionWithLocale(AnyObject?) -> String

|  | Declaration |
| --- | --- |
| From | ``` func descriptionWithLocale(_ locale: AnyObject!) -> String! ``` |
| To | ``` func descriptionWithLocale(_ locale: AnyObject?) -> String ``` |

Modified NSArray.descriptionWithLocale(AnyObject?, indent: Int) -> String

|  | Declaration |
| --- | --- |
| From | ``` func descriptionWithLocale(_ locale: AnyObject!, indent level: Int) -> String! ``` |
| To | ``` func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String ``` |

Modified NSArray.enumerateObjectsAtIndexes(NSIndexSet, options: NSEnumerationOptions, usingBlock:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateObjectsAtIndexes(_ s: NSIndexSet!, options opts: NSEnumerationOptions, usingBlock block: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.6 |

Modified NSArray.enumerateObjectsUsingBlock((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateObjectsUsingBlock(_ block: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateObjectsUsingBlock(_ block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.6 |

Modified NSArray.enumerateObjectsWithOptions(NSEnumerationOptions, usingBlock:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.6 |

Modified NSArray.filteredArrayUsingPredicate(NSPredicate) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func filteredArrayUsingPredicate(_ predicate: NSPredicate!) -> [AnyObject]! ``` |
| To | ``` func filteredArrayUsingPredicate(_ predicate: NSPredicate) -> [AnyObject] ``` |

Modified NSArray.firstObject

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var firstObject: AnyObject! { get } ``` | OS X 10.10 |
| To | ``` var firstObject: AnyObject? { get } ``` | OS X 10.6 |

Modified NSArray.firstObjectCommonWithArray([AnyObject]) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func firstObjectCommonWithArray(_ otherArray: [AnyObject]!) -> AnyObject! ``` |
| To | ``` func firstObjectCommonWithArray(_ otherArray: [AnyObject]) -> AnyObject? ``` |

Modified NSArray.getObjects(AutoreleasingUnsafeMutablePointer<AnyObject?>)

|  | Declaration |
| --- | --- |
| From | ``` func getObjects(_ objects: AutoreleasingUnsafePointer<AnyObject?>) ``` |
| To | ``` func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>) ``` |

Modified NSArray.getObjects(AutoreleasingUnsafeMutablePointer<AnyObject?>, range: NSRange)

|  | Declaration |
| --- | --- |
| From | ``` func getObjects(_ objects: AutoreleasingUnsafePointer<AnyObject?>, range range: NSRange) ``` |
| To | ``` func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, range range: NSRange) ``` |

Modified NSArray.indexOfObject(AnyObject) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObject(_ anObject: AnyObject!) -> Int ``` |
| To | ``` func indexOfObject(_ anObject: AnyObject) -> Int ``` |

Modified NSArray.indexOfObject(AnyObject, inRange: NSRange) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObject(_ anObject: AnyObject!, inRange range: NSRange) -> Int ``` |
| To | ``` func indexOfObject(_ anObject: AnyObject, inRange range: NSRange) -> Int ``` |

Modified NSArray.indexOfObject(AnyObject, inSortedRange: NSRange, options: NSBinarySearchingOptions, usingComparator: NSComparator) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexOfObject(_ obj: AnyObject!, inSortedRange r: NSRange, options opts: NSBinarySearchingOptions, usingComparator cmp: NSComparator!) -> Int ``` | OS X 10.10 |
| To | ``` func indexOfObject(_ obj: AnyObject, inSortedRange r: NSRange, options opts: NSBinarySearchingOptions, usingComparator cmp: NSComparator) -> Int ``` | OS X 10.6 |

Modified NSArray.indexOfObjectAtIndexes(NSIndexSet, options: NSEnumerationOptions, passingTest:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexOfObjectAtIndexes(_ s: NSIndexSet!, options opts: NSEnumerationOptions, passingTest predicate: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Bool)!) -> Int ``` | OS X 10.10 |
| To | ``` func indexOfObjectAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` | OS X 10.6 |

Modified NSArray.indexOfObjectIdenticalTo(AnyObject) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObjectIdenticalTo(_ anObject: AnyObject!) -> Int ``` |
| To | ``` func indexOfObjectIdenticalTo(_ anObject: AnyObject) -> Int ``` |

Modified NSArray.indexOfObjectIdenticalTo(AnyObject, inRange: NSRange) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObjectIdenticalTo(_ anObject: AnyObject!, inRange range: NSRange) -> Int ``` |
| To | ``` func indexOfObjectIdenticalTo(_ anObject: AnyObject, inRange range: NSRange) -> Int ``` |

Modified NSArray.indexOfObjectPassingTest((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexOfObjectPassingTest(_ predicate: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Bool)!) -> Int ``` | OS X 10.10 |
| To | ``` func indexOfObjectPassingTest(_ predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` | OS X 10.6 |

Modified NSArray.indexOfObjectWithOptions(NSEnumerationOptions, passingTest:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Bool)!) -> Int ``` | OS X 10.10 |
| To | ``` func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` | OS X 10.6 |

Modified NSArray.indexesOfObjectsAtIndexes(NSIndexSet, options: NSEnumerationOptions, passingTest:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexesOfObjectsAtIndexes(_ s: NSIndexSet!, options opts: NSEnumerationOptions, passingTest predicate: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Bool)!) -> NSIndexSet! ``` | OS X 10.10 |
| To | ``` func indexesOfObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` | OS X 10.6 |

Modified NSArray.indexesOfObjectsPassingTest((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexesOfObjectsPassingTest(_ predicate: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Bool)!) -> NSIndexSet! ``` | OS X 10.10 |
| To | ``` func indexesOfObjectsPassingTest(_ predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` | OS X 10.6 |

Modified NSArray.indexesOfObjectsWithOptions(NSEnumerationOptions, passingTest:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Bool)!) -> NSIndexSet! ``` | OS X 10.10 |
| To | ``` func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` | OS X 10.6 |

Modified NSArray.isEqualToArray([AnyObject]) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToArray(_ otherArray: [AnyObject]!) -> Bool ``` |
| To | ``` func isEqualToArray(_ otherArray: [AnyObject]) -> Bool ``` |

Modified NSArray.lastObject

|  | Declaration |
| --- | --- |
| From | ``` var lastObject: AnyObject! { get } ``` |
| To | ``` var lastObject: AnyObject? { get } ``` |

Modified NSArray.init(object: AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(object anObject: AnyObject!) ``` |
| To | ``` convenience init(object anObject: AnyObject) ``` |

Modified NSArray.objectAtIndex(Int) -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func objectAtIndex(_ index: Int) -> AnyObject! ``` |
| To | ``` func objectAtIndex(_ index: Int) -> AnyObject ``` |

Modified NSArray.objectEnumerator() -> NSEnumerator

|  | Declaration |
| --- | --- |
| From | ``` func objectEnumerator() -> NSEnumerator! ``` |
| To | ``` func objectEnumerator() -> NSEnumerator ``` |

Modified NSArray.init(objects: UnsafePointer<AnyObject?>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(objects objects: ConstUnsafePointer<AnyObject?>, count cnt: Int) ``` |
| To | ``` init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int) ``` |

Modified NSArray.objectsAtIndexes(NSIndexSet) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func objectsAtIndexes(_ indexes: NSIndexSet!) -> [AnyObject]! ``` |
| To | ``` func objectsAtIndexes(_ indexes: NSIndexSet) -> [AnyObject] ``` |

Modified NSArray.pathsMatchingExtensions([AnyObject]) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func pathsMatchingExtensions(_ filterTypes: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func pathsMatchingExtensions(_ filterTypes: [AnyObject]) -> [AnyObject] ``` |

Modified NSArray.removeObserver(NSObject, forKeyPath: String)

|  | Declaration |
| --- | --- |
| From | ``` func removeObserver(_ observer: NSObject!, forKeyPath keyPath: String!) ``` |
| To | ``` func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) ``` |

Modified NSArray.removeObserver(NSObject, forKeyPath: String, context: UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func removeObserver(_ observer: NSObject!, forKeyPath keyPath: String!, context context: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>) ``` | OS X 10.7 |

Modified NSArray.removeObserver(NSObject, fromObjectsAtIndexes: NSIndexSet, forKeyPath: String)

|  | Declaration |
| --- | --- |
| From | ``` func removeObserver(_ observer: NSObject!, fromObjectsAtIndexes indexes: NSIndexSet!, forKeyPath keyPath: String!) ``` |
| To | ``` func removeObserver(_ observer: NSObject, fromObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String) ``` |

Modified NSArray.removeObserver(NSObject, fromObjectsAtIndexes: NSIndexSet, forKeyPath: String, context: UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func removeObserver(_ observer: NSObject!, fromObjectsAtIndexes indexes: NSIndexSet!, forKeyPath keyPath: String!, context context: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func removeObserver(_ observer: NSObject, fromObjectsAtIndexes indexes: NSIndexSet, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>) ``` | OS X 10.7 |

Modified NSArray.reverseObjectEnumerator() -> NSEnumerator

|  | Declaration |
| --- | --- |
| From | ``` func reverseObjectEnumerator() -> NSEnumerator! ``` |
| To | ``` func reverseObjectEnumerator() -> NSEnumerator ``` |

Modified NSArray.setValue(AnyObject?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ value: AnyObject!, forKey key: String!) ``` |
| To | ``` func setValue(_ value: AnyObject?, forKey key: String) ``` |

Modified NSArray.sortedArrayHint

|  | Declaration |
| --- | --- |
| From | ``` var sortedArrayHint: NSData! { get } ``` |
| To | ``` @NSCopying var sortedArrayHint: NSData { get } ``` |

Modified NSArray.sortedArrayUsingComparator(NSComparator) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sortedArrayUsingComparator(_ cmptr: NSComparator!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func sortedArrayUsingComparator(_ cmptr: NSComparator) -> [AnyObject] ``` | OS X 10.6 |

Modified NSArray.sortedArrayUsingDescriptors([AnyObject]) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func sortedArrayUsingDescriptors(_ sortDescriptors: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func sortedArrayUsingDescriptors(_ sortDescriptors: [AnyObject]) -> [AnyObject] ``` |

Modified NSArray.sortedArrayUsingFunction(CFunctionPointer<((AnyObject!, AnyObject!, UnsafeMutablePointer<Void>) -> Int)>, context: UnsafeMutablePointer<Void>) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func sortedArrayUsingFunction(_ comparator: CFunctionPointer<((AnyObject!, AnyObject!, UnsafePointer<()>) -> Int)>, context context: UnsafePointer<()>) -> [AnyObject]! ``` |
| To | ``` func sortedArrayUsingFunction(_ comparator: CFunctionPointer<((AnyObject!, AnyObject!, UnsafeMutablePointer<Void>) -> Int)>, context context: UnsafeMutablePointer<Void>) -> [AnyObject] ``` |

Modified NSArray.sortedArrayUsingFunction(CFunctionPointer<((AnyObject!, AnyObject!, UnsafeMutablePointer<Void>) -> Int)>, context: UnsafeMutablePointer<Void>, hint: NSData?) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func sortedArrayUsingFunction(_ comparator: CFunctionPointer<((AnyObject!, AnyObject!, UnsafePointer<()>) -> Int)>, context context: UnsafePointer<()>, hint hint: NSData!) -> [AnyObject]! ``` |
| To | ``` func sortedArrayUsingFunction(_ comparator: CFunctionPointer<((AnyObject!, AnyObject!, UnsafeMutablePointer<Void>) -> Int)>, context context: UnsafeMutablePointer<Void>, hint hint: NSData?) -> [AnyObject] ``` |

Modified NSArray.sortedArrayUsingSelector(Selector) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func sortedArrayUsingSelector(_ comparator: Selector) -> [AnyObject]! ``` |
| To | ``` func sortedArrayUsingSelector(_ comparator: Selector) -> [AnyObject] ``` |

Modified NSArray.sortedArrayWithOptions(NSSortOptions, usingComparator: NSComparator) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sortedArrayWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func sortedArrayWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject] ``` | OS X 10.6 |

Modified NSArray.subarrayWithRange(NSRange) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func subarrayWithRange(_ range: NSRange) -> [AnyObject]! ``` |
| To | ``` func subarrayWithRange(_ range: NSRange) -> [AnyObject] ``` |

Modified NSArray.valueForKey(String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func valueForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` func valueForKey(_ key: String) -> AnyObject? ``` |

Modified NSArray.writeToFile(String, atomically: Bool) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToFile(_ path: String!, atomically useAuxiliaryFile: Bool) -> Bool ``` |
| To | ``` func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool ``` |

Modified NSArray.writeToURL(NSURL, atomically: Bool) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ url: NSURL!, atomically atomically: Bool) -> Bool ``` |
| To | ``` func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool ``` |

Modified NSAssertionHandler.currentHandler() -> NSAssertionHandler [class]

|  | Declaration |
| --- | --- |
| From | ``` class func currentHandler() -> NSAssertionHandler! ``` |
| To | ``` class func currentHandler() -> NSAssertionHandler ``` |

Modified NSAttributedString

|  | Protocols | Introduction |
| --- | --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding | OS X 10.10 |
| To | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSObjectProtocol, NSPasteboardReading, NSPasteboardWriting, NSSecureCoding | OS X 10.0 |

Modified NSAttributedString.attribute(String, atIndex: Int, effectiveRange: NSRangePointer) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func attribute(_ attrName: String!, atIndex location: Int, effectiveRange range: NSRangePointer) -> AnyObject! ``` |
| To | ``` func attribute(_ attrName: String, atIndex location: Int, effectiveRange range: NSRangePointer) -> AnyObject? ``` |

Modified NSAttributedString.attribute(String, atIndex: Int, longestEffectiveRange: NSRangePointer, inRange: NSRange) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func attribute(_ attrName: String!, atIndex location: Int, longestEffectiveRange range: NSRangePointer, inRange rangeLimit: NSRange) -> AnyObject! ``` |
| To | ``` func attribute(_ attrName: String, atIndex location: Int, longestEffectiveRange range: NSRangePointer, inRange rangeLimit: NSRange) -> AnyObject? ``` |

Modified NSAttributedString.init(attributedString: NSAttributedString)

|  | Declaration |
| --- | --- |
| From | ``` init(attributedString attrStr: NSAttributedString!) ``` |
| To | ``` init(attributedString attrStr: NSAttributedString) ``` |

Modified NSAttributedString.attributedSubstringFromRange(NSRange) -> NSAttributedString

|  | Declaration |
| --- | --- |
| From | ``` func attributedSubstringFromRange(_ range: NSRange) -> NSAttributedString! ``` |
| To | ``` func attributedSubstringFromRange(_ range: NSRange) -> NSAttributedString ``` |

Modified NSAttributedString.attributesAtIndex(Int, effectiveRange: NSRangePointer) -> [NSObject: AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func attributesAtIndex(_ location: Int, effectiveRange range: NSRangePointer) -> [NSObject : AnyObject]! ``` |
| To | ``` func attributesAtIndex(_ location: Int, effectiveRange range: NSRangePointer) -> [NSObject : AnyObject] ``` |

Modified NSAttributedString.attributesAtIndex(Int, longestEffectiveRange: NSRangePointer, inRange: NSRange) -> [NSObject: AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func attributesAtIndex(_ location: Int, longestEffectiveRange range: NSRangePointer, inRange rangeLimit: NSRange) -> [NSObject : AnyObject]! ``` |
| To | ``` func attributesAtIndex(_ location: Int, longestEffectiveRange range: NSRangePointer, inRange rangeLimit: NSRange) -> [NSObject : AnyObject] ``` |

Modified NSAttributedString.enumerateAttribute(String, inRange: NSRange, options: NSAttributedStringEnumerationOptions, usingBlock:(AnyObject!, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateAttribute(_ attrName: String!, inRange enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: ((AnyObject!, NSRange, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateAttribute(_ attrName: String, inRange enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: (AnyObject!, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.6 |

Modified NSAttributedString.enumerateAttributesInRange(NSRange, options: NSAttributedStringEnumerationOptions, usingBlock:([NSObject: AnyObject]!, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateAttributesInRange(_ enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: (([NSObject : AnyObject]!, NSRange, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateAttributesInRange(_ enumerationRange: NSRange, options opts: NSAttributedStringEnumerationOptions, usingBlock block: ([NSObject : AnyObject]!, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.6 |

Modified NSAttributedString.isEqualToAttributedString(NSAttributedString) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToAttributedString(_ other: NSAttributedString!) -> Bool ``` |
| To | ``` func isEqualToAttributedString(_ other: NSAttributedString) -> Bool ``` |

Modified NSAttributedString.string

|  | Declaration |
| --- | --- |
| From | ``` var string: String! { get } ``` |
| To | ``` var string: String { get } ``` |

Modified NSAttributedString.init(string: String)

|  | Declaration |
| --- | --- |
| From | ``` init(string str: String!) ``` |
| To | ``` init(string str: String) ``` |

Modified NSAttributedString.init(string: String, attributes:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(string str: String!, attributes attrs: [NSObject : AnyObject]!) ``` |
| To | ``` init(string str: String, attributes attrs: [NSObject : AnyObject]?) ``` |

Modified NSAttributedStringEnumerationOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSAttributedStringEnumerationOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Reverse: NSAttributedStringEnumerationOptions { get }     static var LongestEffectiveRangeNotRequired: NSAttributedStringEnumerationOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSAttributedStringEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Reverse: NSAttributedStringEnumerationOptions { get }     static var LongestEffectiveRangeNotRequired: NSAttributedStringEnumerationOptions { get } } ``` | RawOptionSetType |

Modified NSAttributedStringEnumerationOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSBackgroundActivityScheduler.identifier

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` var identifier: String { get } ``` |

Modified NSBackgroundActivityScheduler.init(identifier: String)

|  | Declaration |
| --- | --- |
| From | ``` init(identifier identifier: String!) ``` |
| To | ``` init(identifier identifier: String) ``` |

Modified NSBackgroundActivityScheduler.scheduleWithBlock((NSBackgroundActivityCompletionHandler!) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleWithBlock(_ block: ((NSBackgroundActivityCompletionHandler!) -> Void)!) ``` |
| To | ``` func scheduleWithBlock(_ block: (NSBackgroundActivityCompletionHandler!) -> Void) ``` |

Modified NSBinarySearchingOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSBinarySearchingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var FirstEqual: NSBinarySearchingOptions { get }     static var LastEqual: NSBinarySearchingOptions { get }     static var InsertionIndex: NSBinarySearchingOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSBinarySearchingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var FirstEqual: NSBinarySearchingOptions { get }     static var LastEqual: NSBinarySearchingOptions { get }     static var InsertionIndex: NSBinarySearchingOptions { get } } ``` | RawOptionSetType |

Modified NSBinarySearchingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSBlockOperation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSBlockOperation.addExecutionBlock(() -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func addExecutionBlock(_ block: (() -> Void)!) ``` |
| To | ``` func addExecutionBlock(_ block: () -> Void) ``` |

Modified NSBlockOperation.init(block: () -> Void)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(block block: (() -> Void)!) ``` |
| To | ``` convenience init(block block: () -> Void) ``` |

Modified NSBlockOperation.executionBlocks

|  | Declaration |
| --- | --- |
| From | ``` var executionBlocks: [AnyObject]! { get } ``` |
| To | ``` var executionBlocks: [AnyObject] { get } ``` |

Modified NSBundle.URLForAuxiliaryExecutable(String) -> NSURL?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URLForAuxiliaryExecutable(_ executableName: String!) -> NSURL! ``` | OS X 10.10 |
| To | ``` func URLForAuxiliaryExecutable(_ executableName: String) -> NSURL? ``` | OS X 10.6 |

Modified NSBundle.URLForResource(String, withExtension: String?) -> NSURL?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URLForResource(_ name: String!, withExtension ext: String!) -> NSURL! ``` | OS X 10.10 |
| To | ``` func URLForResource(_ name: String, withExtension ext: String?) -> NSURL? ``` | OS X 10.6 |

Modified NSBundle.URLForResource(String, withExtension: String?, subdirectory: String?) -> NSURL?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URLForResource(_ name: String!, withExtension ext: String!, subdirectory subpath: String!) -> NSURL! ``` | OS X 10.10 |
| To | ``` func URLForResource(_ name: String, withExtension ext: String?, subdirectory subpath: String?) -> NSURL? ``` | OS X 10.6 |

Modified NSBundle.URLForResource(String, withExtension: String?, subdirectory: String?, inBundleWithURL: NSURL) -> NSURL? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func URLForResource(_ name: String!, withExtension ext: String!, subdirectory subpath: String!, inBundleWithURL bundleURL: NSURL!) -> NSURL! ``` | OS X 10.10 |
| To | ``` class func URLForResource(_ name: String, withExtension ext: String?, subdirectory subpath: String?, inBundleWithURL bundleURL: NSURL) -> NSURL? ``` | OS X 10.6 |

Modified NSBundle.URLForResource(String, withExtension: String?, subdirectory: String?, localization: String?) -> NSURL?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URLForResource(_ name: String!, withExtension ext: String!, subdirectory subpath: String!, localization localizationName: String!) -> NSURL! ``` | OS X 10.10 |
| To | ``` func URLForResource(_ name: String, withExtension ext: String?, subdirectory subpath: String?, localization localizationName: String?) -> NSURL? ``` | OS X 10.6 |

Modified NSBundle.URLsForResourcesWithExtension(String?, subdirectory: String?) -> [AnyObject]?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URLsForResourcesWithExtension(_ ext: String!, subdirectory subpath: String!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?) -> [AnyObject]? ``` | OS X 10.6 |

Modified NSBundle.URLsForResourcesWithExtension(String?, subdirectory: String?, inBundleWithURL: NSURL) -> [AnyObject]? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func URLsForResourcesWithExtension(_ ext: String!, subdirectory subpath: String!, inBundleWithURL bundleURL: NSURL!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` class func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?, inBundleWithURL bundleURL: NSURL) -> [AnyObject]? ``` | OS X 10.6 |

Modified NSBundle.URLsForResourcesWithExtension(String?, subdirectory: String?, localization: String?) -> [AnyObject]?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URLsForResourcesWithExtension(_ ext: String!, subdirectory subpath: String!, localization localizationName: String!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func URLsForResourcesWithExtension(_ ext: String?, subdirectory subpath: String?, localization localizationName: String?) -> [AnyObject]? ``` | OS X 10.6 |

Modified NSBundle.allBundles() -> [AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func allBundles() -> [AnyObject]! ``` |
| To | ``` class func allBundles() -> [AnyObject] ``` |

Modified NSBundle.allFrameworks() -> [AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func allFrameworks() -> [AnyObject]! ``` |
| To | ``` class func allFrameworks() -> [AnyObject] ``` |

Modified NSBundle.appStoreReceiptURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var appStoreReceiptURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var appStoreReceiptURL: NSURL? { get } ``` | OS X 10.7 |

Modified NSBundle.builtInPlugInsPath

|  | Declaration |
| --- | --- |
| From | ``` var builtInPlugInsPath: String! { get } ``` |
| To | ``` var builtInPlugInsPath: String? { get } ``` |

Modified NSBundle.builtInPlugInsURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var builtInPlugInsURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var builtInPlugInsURL: NSURL? { get } ``` | OS X 10.6 |

Modified NSBundle.bundleIdentifier

|  | Declaration |
| --- | --- |
| From | ``` var bundleIdentifier: String! { get } ``` |
| To | ``` var bundleIdentifier: String? { get } ``` |

Modified NSBundle.bundlePath

|  | Declaration |
| --- | --- |
| From | ``` var bundlePath: String! { get } ``` |
| To | ``` var bundlePath: String { get } ``` |

Modified NSBundle.bundleURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var bundleURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var bundleURL: NSURL { get } ``` | OS X 10.6 |

Modified NSBundle.classNamed(String) -> AnyClass?

|  | Declaration |
| --- | --- |
| From | ``` func classNamed(_ className: String!) -> AnyClass! ``` |
| To | ``` func classNamed(_ className: String) -> AnyClass? ``` |

Modified NSBundle.developmentLocalization

|  | Declaration |
| --- | --- |
| From | ``` var developmentLocalization: String! { get } ``` |
| To | ``` var developmentLocalization: String? { get } ``` |

Modified NSBundle.executableArchitectures

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var executableArchitectures: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var executableArchitectures: [AnyObject]? { get } ``` | OS X 10.5 |

Modified NSBundle.executablePath

|  | Declaration |
| --- | --- |
| From | ``` var executablePath: String! { get } ``` |
| To | ``` var executablePath: String? { get } ``` |

Modified NSBundle.executableURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var executableURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var executableURL: NSURL? { get } ``` | OS X 10.6 |

Modified NSBundle.init(forClass: AnyClass)

|  | Declaration |
| --- | --- |
| From | ``` init(forClass aClass: AnyClass!) -> NSBundle ``` |
| To | ``` init(forClass aClass: AnyClass) -> NSBundle ``` |

Modified NSBundle.init(identifier: String)

|  | Declaration |
| --- | --- |
| From | ``` init(identifier identifier: String!) -> NSBundle ``` |
| To | ``` init?(identifier identifier: String) -> NSBundle ``` |

Modified NSBundle.infoDictionary

|  | Declaration |
| --- | --- |
| From | ``` var infoDictionary: [NSObject : AnyObject]! { get } ``` |
| To | ``` var infoDictionary: [NSObject : AnyObject]? { get } ``` |

Modified NSBundle.loadAndReturnError(NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSBundle.localizations

|  | Declaration |
| --- | --- |
| From | ``` var localizations: [AnyObject]! { get } ``` |
| To | ``` var localizations: [AnyObject]? { get } ``` |

Modified NSBundle.localizedInfoDictionary

|  | Declaration |
| --- | --- |
| From | ``` var localizedInfoDictionary: [NSObject : AnyObject]! { get } ``` |
| To | ``` var localizedInfoDictionary: [NSObject : AnyObject]? { get } ``` |

Modified NSBundle.localizedStringForKey(String, value: String?, table: String?) -> String

|  | Declaration |
| --- | --- |
| From | ``` func localizedStringForKey(_ key: String!, value value: String!, table tableName: String!) -> String! ``` |
| To | ``` func localizedStringForKey(_ key: String, value value: String?, table tableName: String?) -> String ``` |

Modified NSBundle.mainBundle() -> NSBundle [class]

|  | Declaration |
| --- | --- |
| From | ``` class func mainBundle() -> NSBundle! ``` |
| To | ``` class func mainBundle() -> NSBundle ``` |

Modified NSBundle.objectForInfoDictionaryKey(String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func objectForInfoDictionaryKey(_ key: String!) -> AnyObject! ``` |
| To | ``` func objectForInfoDictionaryKey(_ key: String) -> AnyObject? ``` |

Modified NSBundle.pathForAuxiliaryExecutable(String) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func pathForAuxiliaryExecutable(_ executableName: String!) -> String! ``` |
| To | ``` func pathForAuxiliaryExecutable(_ executableName: String) -> String? ``` |

Modified NSBundle.pathForResource(String?, ofType: String?) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func pathForResource(_ name: String!, ofType ext: String!) -> String! ``` |
| To | ``` func pathForResource(_ name: String?, ofType ext: String?) -> String? ``` |

Modified NSBundle.pathForResource(String?, ofType: String?, inDirectory: String) -> String? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func pathForResource(_ name: String!, ofType ext: String!, inDirectory bundlePath: String!) -> String! ``` |
| To | ``` class func pathForResource(_ name: String?, ofType ext: String?, inDirectory bundlePath: String) -> String? ``` |

Modified NSBundle.pathForResource(String?, ofType: String?, inDirectory: String?) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func pathForResource(_ name: String!, ofType ext: String!, inDirectory subpath: String!) -> String! ``` |
| To | ``` func pathForResource(_ name: String?, ofType ext: String?, inDirectory subpath: String?) -> String? ``` |

Modified NSBundle.pathForResource(String?, ofType: String?, inDirectory: String?, forLocalization: String?) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func pathForResource(_ name: String!, ofType ext: String!, inDirectory subpath: String!, forLocalization localizationName: String!) -> String! ``` |
| To | ``` func pathForResource(_ name: String?, ofType ext: String?, inDirectory subpath: String?, forLocalization localizationName: String?) -> String? ``` |

Modified NSBundle.pathsForResourcesOfType(String?, inDirectory: String) -> [AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func pathsForResourcesOfType(_ ext: String!, inDirectory bundlePath: String!) -> [AnyObject]! ``` |
| To | ``` class func pathsForResourcesOfType(_ ext: String?, inDirectory bundlePath: String) -> [AnyObject] ``` |

Modified NSBundle.pathsForResourcesOfType(String?, inDirectory: String?) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func pathsForResourcesOfType(_ ext: String!, inDirectory subpath: String!) -> [AnyObject]! ``` |
| To | ``` func pathsForResourcesOfType(_ ext: String?, inDirectory subpath: String?) -> [AnyObject] ``` |

Modified NSBundle.pathsForResourcesOfType(String?, inDirectory: String?, forLocalization: String?) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func pathsForResourcesOfType(_ ext: String!, inDirectory subpath: String!, forLocalization localizationName: String!) -> [AnyObject]! ``` |
| To | ``` func pathsForResourcesOfType(_ ext: String?, inDirectory subpath: String?, forLocalization localizationName: String?) -> [AnyObject] ``` |

Modified NSBundle.preferredLocalizations

|  | Declaration |
| --- | --- |
| From | ``` var preferredLocalizations: [AnyObject]! { get } ``` |
| To | ``` var preferredLocalizations: [AnyObject] { get } ``` |

Modified NSBundle.preferredLocalizationsFromArray([AnyObject]) -> [AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func preferredLocalizationsFromArray(_ localizationsArray: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` class func preferredLocalizationsFromArray(_ localizationsArray: [AnyObject]) -> [AnyObject] ``` |

Modified NSBundle.preferredLocalizationsFromArray([AnyObject], forPreferences:[AnyObject]?) -> [AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func preferredLocalizationsFromArray(_ localizationsArray: [AnyObject]!, forPreferences preferencesArray: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` class func preferredLocalizationsFromArray(_ localizationsArray: [AnyObject], forPreferences preferencesArray: [AnyObject]?) -> [AnyObject] ``` |

Modified NSBundle.preflightAndReturnError(NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSBundle.principalClass

|  | Declaration |
| --- | --- |
| From | ``` var principalClass: AnyClass! { get } ``` |
| To | ``` var principalClass: AnyClass? { get } ``` |

Modified NSBundle.privateFrameworksPath

|  | Declaration |
| --- | --- |
| From | ``` var privateFrameworksPath: String! { get } ``` |
| To | ``` var privateFrameworksPath: String? { get } ``` |

Modified NSBundle.privateFrameworksURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var privateFrameworksURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var privateFrameworksURL: NSURL? { get } ``` | OS X 10.6 |

Modified NSBundle.resourcePath

|  | Declaration |
| --- | --- |
| From | ``` var resourcePath: String! { get } ``` |
| To | ``` var resourcePath: String? { get } ``` |

Modified NSBundle.resourceURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var resourceURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var resourceURL: NSURL? { get } ``` | OS X 10.6 |

Modified NSBundle.sharedFrameworksPath

|  | Declaration |
| --- | --- |
| From | ``` var sharedFrameworksPath: String! { get } ``` |
| To | ``` var sharedFrameworksPath: String? { get } ``` |

Modified NSBundle.sharedFrameworksURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var sharedFrameworksURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var sharedFrameworksURL: NSURL? { get } ``` | OS X 10.6 |

Modified NSBundle.sharedSupportPath

|  | Declaration |
| --- | --- |
| From | ``` var sharedSupportPath: String! { get } ``` |
| To | ``` var sharedSupportPath: String? { get } ``` |

Modified NSBundle.sharedSupportURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var sharedSupportURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var sharedSupportURL: NSURL? { get } ``` | OS X 10.6 |

Modified NSByteCountFormatter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSByteCountFormatter.stringFromByteCount(Int64) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringFromByteCount(_ byteCount: Int64) -> String! ``` |
| To | ``` func stringFromByteCount(_ byteCount: Int64) -> String ``` |

Modified NSByteCountFormatter.stringFromByteCount(Int64, countStyle: NSByteCountFormatterCountStyle) -> String [class]

|  | Declaration |
| --- | --- |
| From | ``` class func stringFromByteCount(_ byteCount: Int64, countStyle countStyle: NSByteCountFormatterCountStyle) -> String! ``` |
| To | ``` class func stringFromByteCount(_ byteCount: Int64, countStyle countStyle: NSByteCountFormatterCountStyle) -> String ``` |

Modified NSByteCountFormatterUnits [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSByteCountFormatterUnits : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var UseDefault: NSByteCountFormatterUnits { get }     static var UseBytes: NSByteCountFormatterUnits { get }     static var UseKB: NSByteCountFormatterUnits { get }     static var UseMB: NSByteCountFormatterUnits { get }     static var UseGB: NSByteCountFormatterUnits { get }     static var UseTB: NSByteCountFormatterUnits { get }     static var UsePB: NSByteCountFormatterUnits { get }     static var UseEB: NSByteCountFormatterUnits { get }     static var UseZB: NSByteCountFormatterUnits { get }     static var UseYBOrHigher: NSByteCountFormatterUnits { get }     static var UseAll: NSByteCountFormatterUnits { get } } ``` | RawOptionSet |
| To | ``` struct NSByteCountFormatterUnits : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var UseDefault: NSByteCountFormatterUnits { get }     static var UseBytes: NSByteCountFormatterUnits { get }     static var UseKB: NSByteCountFormatterUnits { get }     static var UseMB: NSByteCountFormatterUnits { get }     static var UseGB: NSByteCountFormatterUnits { get }     static var UseTB: NSByteCountFormatterUnits { get }     static var UsePB: NSByteCountFormatterUnits { get }     static var UseEB: NSByteCountFormatterUnits { get }     static var UseZB: NSByteCountFormatterUnits { get }     static var UseYBOrHigher: NSByteCountFormatterUnits { get }     static var UseAll: NSByteCountFormatterUnits { get } } ``` | RawOptionSetType |

Modified NSByteCountFormatterUnits.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSCache

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSCache.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: NSCacheDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: NSCacheDelegate? ``` |

Modified NSCache.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String ``` |

Modified NSCache.objectForKey(AnyObject) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func objectForKey(_ key: AnyObject!) -> AnyObject! ``` |
| To | ``` func objectForKey(_ key: AnyObject) -> AnyObject? ``` |

Modified NSCache.removeObjectForKey(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func removeObjectForKey(_ key: AnyObject!) ``` |
| To | ``` func removeObjectForKey(_ key: AnyObject) ``` |

Modified NSCache.setObject(AnyObject, forKey: AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ obj: AnyObject!, forKey key: AnyObject!) ``` |
| To | ``` func setObject(_ obj: AnyObject, forKey key: AnyObject) ``` |

Modified NSCache.setObject(AnyObject, forKey: AnyObject, cost: Int)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ obj: AnyObject!, forKey key: AnyObject!, cost g: Int) ``` |
| To | ``` func setObject(_ obj: AnyObject, forKey key: AnyObject, cost g: Int) ``` |

Modified NSCacheDelegate.cache(NSCache, willEvictObject: AnyObject)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func cache(_ cache: NSCache!, willEvictObject obj: AnyObject!) ``` | -- |
| To | ``` optional func cache(_ cache: NSCache, willEvictObject obj: AnyObject) ``` | yes |

Modified NSCachedURLResponse.data

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData! { get } ``` |
| To | ``` @NSCopying var data: NSData { get } ``` |

Modified NSCachedURLResponse.response

|  | Declaration |
| --- | --- |
| From | ``` var response: NSURLResponse! { get } ``` |
| To | ``` @NSCopying var response: NSURLResponse { get } ``` |

Modified NSCachedURLResponse.init(response: NSURLResponse, data: NSData)

|  | Declaration |
| --- | --- |
| From | ``` init(response response: NSURLResponse!, data data: NSData!) ``` |
| To | ``` init(response response: NSURLResponse, data data: NSData) ``` |

Modified NSCachedURLResponse.init(response: NSURLResponse, data: NSData, userInfo:[NSObject: AnyObject]?, storagePolicy: NSURLCacheStoragePolicy)

|  | Declaration |
| --- | --- |
| From | ``` init(response response: NSURLResponse!, data data: NSData!, userInfo userInfo: [NSObject : AnyObject]!, storagePolicy storagePolicy: NSURLCacheStoragePolicy) ``` |
| To | ``` init(response response: NSURLResponse, data data: NSData, userInfo userInfo: [NSObject : AnyObject]?, storagePolicy storagePolicy: NSURLCacheStoragePolicy) ``` |

Modified NSCachedURLResponse.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! { get } ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? { get } ``` |

Modified NSCalendar.AMSymbol

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var AMSymbol: String! { get } ``` | OS X 10.10 |
| To | ``` var AMSymbol: String { get } ``` | OS X 10.7 |

Modified NSCalendar.PMSymbol

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var PMSymbol: String! { get } ``` | OS X 10.10 |
| To | ``` var PMSymbol: String { get } ``` | OS X 10.7 |

Modified NSCalendar.autoupdatingCurrentCalendar() -> NSCalendar [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func autoupdatingCurrentCalendar() -> NSCalendar! ``` | OS X 10.10 |
| To | ``` class func autoupdatingCurrentCalendar() -> NSCalendar ``` | OS X 10.5 |

Modified NSCalendar.calendarIdentifier

|  | Declaration |
| --- | --- |
| From | ``` var calendarIdentifier: String! { get } ``` |
| To | ``` var calendarIdentifier: String { get } ``` |

Modified NSCalendar.init(calendarIdentifier: String)

|  | Declaration |
| --- | --- |
| From | ``` init(calendarIdentifier ident: String!) ``` |
| To | ``` init?(calendarIdentifier ident: String) ``` |

Modified NSCalendar.compareDate(NSDate, toDate: NSDate, toUnitGranularity: NSCalendarUnit) -> NSComparisonResult

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func compareDate(_ date1: NSDate!, toDate date2: NSDate!, toUnitGranularity unit: NSCalendarUnit) -> NSComparisonResult ``` | OS X 10.10 |
| To | ``` func compareDate(_ date1: NSDate, toDate date2: NSDate, toUnitGranularity unit: NSCalendarUnit) -> NSComparisonResult ``` | OS X 10.9 |

Modified NSCalendar.component(NSCalendarUnit, fromDate: NSDate) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func component(_ unit: NSCalendarUnit, fromDate date: NSDate!) -> Int ``` | OS X 10.10 |
| To | ``` func component(_ unit: NSCalendarUnit, fromDate date: NSDate) -> Int ``` | OS X 10.9 |

Modified NSCalendar.components(NSCalendarUnit, fromDate: NSDate) -> NSDateComponents

|  | Declaration |
| --- | --- |
| From | ``` func components(_ unitFlags: NSCalendarUnit, fromDate date: NSDate!) -> NSDateComponents! ``` |
| To | ``` func components(_ unitFlags: NSCalendarUnit, fromDate date: NSDate) -> NSDateComponents ``` |

Modified NSCalendar.components(NSCalendarUnit, fromDate: NSDate, toDate: NSDate, options: NSCalendarOptions) -> NSDateComponents

|  | Declaration |
| --- | --- |
| From | ``` func components(_ unitFlags: NSCalendarUnit, fromDate startingDate: NSDate!, toDate resultDate: NSDate!, options opts: NSCalendarOptions) -> NSDateComponents! ``` |
| To | ``` func components(_ unitFlags: NSCalendarUnit, fromDate startingDate: NSDate, toDate resultDate: NSDate, options opts: NSCalendarOptions) -> NSDateComponents ``` |

Modified NSCalendar.components(NSCalendarUnit, fromDateComponents: NSDateComponents, toDateComponents: NSDateComponents, options: NSCalendarOptions) -> NSDateComponents

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func components(_ unitFlags: NSCalendarUnit, fromDateComponents startingDateComp: NSDateComponents!, toDateComponents resultDateComp: NSDateComponents!, options options: NSCalendarOptions) -> NSDateComponents! ``` | OS X 10.10 |
| To | ``` func components(_ unitFlags: NSCalendarUnit, fromDateComponents startingDateComp: NSDateComponents, toDateComponents resultDateComp: NSDateComponents, options options: NSCalendarOptions) -> NSDateComponents ``` | OS X 10.9 |

Modified NSCalendar.componentsInTimeZone(NSTimeZone, fromDate: NSDate) -> NSDateComponents

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func componentsInTimeZone(_ timezone: NSTimeZone!, fromDate date: NSDate!) -> NSDateComponents! ``` | OS X 10.10 |
| To | ``` func componentsInTimeZone(_ timezone: NSTimeZone, fromDate date: NSDate) -> NSDateComponents ``` | OS X 10.9 |

Modified NSCalendar.currentCalendar() -> NSCalendar [class]

|  | Declaration |
| --- | --- |
| From | ``` class func currentCalendar() -> NSCalendar! ``` |
| To | ``` class func currentCalendar() -> NSCalendar ``` |

Modified NSCalendar.date(NSDate, matchesComponents: NSDateComponents) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func date(_ date: NSDate!, matchesComponents components: NSDateComponents!) -> Bool ``` | OS X 10.10 |
| To | ``` func date(_ date: NSDate, matchesComponents components: NSDateComponents) -> Bool ``` | OS X 10.9 |

Modified NSCalendar.dateByAddingComponents(NSDateComponents, toDate: NSDate, options: NSCalendarOptions) -> NSDate?

|  | Declaration |
| --- | --- |
| From | ``` func dateByAddingComponents(_ comps: NSDateComponents!, toDate date: NSDate!, options opts: NSCalendarOptions) -> NSDate! ``` |
| To | ``` func dateByAddingComponents(_ comps: NSDateComponents, toDate date: NSDate, options opts: NSCalendarOptions) -> NSDate? ``` |

Modified NSCalendar.dateByAddingUnit(NSCalendarUnit, value: Int, toDate: NSDate, options: NSCalendarOptions) -> NSDate?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func dateByAddingUnit(_ unit: NSCalendarUnit, value value: Int, toDate date: NSDate!, options options: NSCalendarOptions) -> NSDate! ``` | OS X 10.10 |
| To | ``` func dateByAddingUnit(_ unit: NSCalendarUnit, value value: Int, toDate date: NSDate, options options: NSCalendarOptions) -> NSDate? ``` | OS X 10.9 |

Modified NSCalendar.dateBySettingHour(Int, minute: Int, second: Int, ofDate: NSDate, options: NSCalendarOptions) -> NSDate?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func dateBySettingHour(_ h: Int, minute m: Int, second s: Int, ofDate date: NSDate!, options opts: NSCalendarOptions) -> NSDate! ``` | OS X 10.10 |
| To | ``` func dateBySettingHour(_ h: Int, minute m: Int, second s: Int, ofDate date: NSDate, options opts: NSCalendarOptions) -> NSDate? ``` | OS X 10.9 |

Modified NSCalendar.dateBySettingUnit(NSCalendarUnit, value: Int, ofDate: NSDate, options: NSCalendarOptions) -> NSDate?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func dateBySettingUnit(_ unit: NSCalendarUnit, value v: Int, ofDate date: NSDate!, options opts: NSCalendarOptions) -> NSDate! ``` | OS X 10.10 |
| To | ``` func dateBySettingUnit(_ unit: NSCalendarUnit, value v: Int, ofDate date: NSDate, options opts: NSCalendarOptions) -> NSDate? ``` | OS X 10.9 |

Modified NSCalendar.dateFromComponents(NSDateComponents) -> NSDate?

|  | Declaration |
| --- | --- |
| From | ``` func dateFromComponents(_ comps: NSDateComponents!) -> NSDate! ``` |
| To | ``` func dateFromComponents(_ comps: NSDateComponents) -> NSDate? ``` |

Modified NSCalendar.dateWithEra(Int, year: Int, month: Int, day: Int, hour: Int, minute: Int, second: Int, nanosecond: Int) -> NSDate?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func dateWithEra(_ eraValue: Int, year yearValue: Int, month monthValue: Int, day dayValue: Int, hour hourValue: Int, minute minuteValue: Int, second secondValue: Int, nanosecond nanosecondValue: Int) -> NSDate! ``` | OS X 10.10 |
| To | ``` func dateWithEra(_ eraValue: Int, year yearValue: Int, month monthValue: Int, day dayValue: Int, hour hourValue: Int, minute minuteValue: Int, second secondValue: Int, nanosecond nanosecondValue: Int) -> NSDate? ``` | OS X 10.9 |

Modified NSCalendar.dateWithEra(Int, yearForWeekOfYear: Int, weekOfYear: Int, weekday: Int, hour: Int, minute: Int, second: Int, nanosecond: Int) -> NSDate?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func dateWithEra(_ eraValue: Int, yearForWeekOfYear yearValue: Int, weekOfYear weekValue: Int, weekday weekdayValue: Int, hour hourValue: Int, minute minuteValue: Int, second secondValue: Int, nanosecond nanosecondValue: Int) -> NSDate! ``` | OS X 10.10 |
| To | ``` func dateWithEra(_ eraValue: Int, yearForWeekOfYear yearValue: Int, weekOfYear weekValue: Int, weekday weekdayValue: Int, hour hourValue: Int, minute minuteValue: Int, second secondValue: Int, nanosecond nanosecondValue: Int) -> NSDate? ``` | OS X 10.9 |

Modified NSCalendar.enumerateDatesStartingAfterDate(NSDate, matchingComponents: NSDateComponents, options: NSCalendarOptions, usingBlock:(NSDate!, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateDatesStartingAfterDate(_ start: NSDate!, matchingComponents comps: NSDateComponents!, options opts: NSCalendarOptions, usingBlock block: ((NSDate!, Bool, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateDatesStartingAfterDate(_ start: NSDate, matchingComponents comps: NSDateComponents, options opts: NSCalendarOptions, usingBlock block: (NSDate!, Bool, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.9 |

Modified NSCalendar.eraSymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var eraSymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var eraSymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.getEra(UnsafeMutablePointer<Int>, year: UnsafeMutablePointer<Int>, month: UnsafeMutablePointer<Int>, day: UnsafeMutablePointer<Int>, fromDate: NSDate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getEra(_ eraValuePointer: UnsafePointer<Int>, year yearValuePointer: UnsafePointer<Int>, month monthValuePointer: UnsafePointer<Int>, day dayValuePointer: UnsafePointer<Int>, fromDate date: NSDate!) ``` | OS X 10.10 |
| To | ``` func getEra(_ eraValuePointer: UnsafeMutablePointer<Int>, year yearValuePointer: UnsafeMutablePointer<Int>, month monthValuePointer: UnsafeMutablePointer<Int>, day dayValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate) ``` | OS X 10.9 |

Modified NSCalendar.getEra(UnsafeMutablePointer<Int>, yearForWeekOfYear: UnsafeMutablePointer<Int>, weekOfYear: UnsafeMutablePointer<Int>, weekday: UnsafeMutablePointer<Int>, fromDate: NSDate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getEra(_ eraValuePointer: UnsafePointer<Int>, yearForWeekOfYear yearValuePointer: UnsafePointer<Int>, weekOfYear weekValuePointer: UnsafePointer<Int>, weekday weekdayValuePointer: UnsafePointer<Int>, fromDate date: NSDate!) ``` | OS X 10.10 |
| To | ``` func getEra(_ eraValuePointer: UnsafeMutablePointer<Int>, yearForWeekOfYear yearValuePointer: UnsafeMutablePointer<Int>, weekOfYear weekValuePointer: UnsafeMutablePointer<Int>, weekday weekdayValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate) ``` | OS X 10.9 |

Modified NSCalendar.getHour(UnsafeMutablePointer<Int>, minute: UnsafeMutablePointer<Int>, second: UnsafeMutablePointer<Int>, nanosecond: UnsafeMutablePointer<Int>, fromDate: NSDate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getHour(_ hourValuePointer: UnsafePointer<Int>, minute minuteValuePointer: UnsafePointer<Int>, second secondValuePointer: UnsafePointer<Int>, nanosecond nanosecondValuePointer: UnsafePointer<Int>, fromDate date: NSDate!) ``` | OS X 10.10 |
| To | ``` func getHour(_ hourValuePointer: UnsafeMutablePointer<Int>, minute minuteValuePointer: UnsafeMutablePointer<Int>, second secondValuePointer: UnsafeMutablePointer<Int>, nanosecond nanosecondValuePointer: UnsafeMutablePointer<Int>, fromDate date: NSDate) ``` | OS X 10.9 |

Modified NSCalendar.init(identifier: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(identifier calendarIdentifierConstant: String!) -> NSCalendar ``` | OS X 10.10 |
| To | ``` init?(identifier calendarIdentifierConstant: String) -> NSCalendar ``` | OS X 10.9 |

Modified NSCalendar.isDate(NSDate, equalToDate: NSDate, toUnitGranularity: NSCalendarUnit) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isDate(_ date1: NSDate!, equalToDate date2: NSDate!, toUnitGranularity unit: NSCalendarUnit) -> Bool ``` | OS X 10.10 |
| To | ``` func isDate(_ date1: NSDate, equalToDate date2: NSDate, toUnitGranularity unit: NSCalendarUnit) -> Bool ``` | OS X 10.9 |

Modified NSCalendar.isDate(NSDate, inSameDayAsDate: NSDate) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isDate(_ date1: NSDate!, inSameDayAsDate date2: NSDate!) -> Bool ``` | OS X 10.10 |
| To | ``` func isDate(_ date1: NSDate, inSameDayAsDate date2: NSDate) -> Bool ``` | OS X 10.9 |

Modified NSCalendar.isDateInToday(NSDate) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isDateInToday(_ date: NSDate!) -> Bool ``` | OS X 10.10 |
| To | ``` func isDateInToday(_ date: NSDate) -> Bool ``` | OS X 10.9 |

Modified NSCalendar.isDateInTomorrow(NSDate) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isDateInTomorrow(_ date: NSDate!) -> Bool ``` | OS X 10.10 |
| To | ``` func isDateInTomorrow(_ date: NSDate) -> Bool ``` | OS X 10.9 |

Modified NSCalendar.isDateInWeekend(NSDate) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isDateInWeekend(_ date: NSDate!) -> Bool ``` | OS X 10.10 |
| To | ``` func isDateInWeekend(_ date: NSDate) -> Bool ``` | OS X 10.9 |

Modified NSCalendar.isDateInYesterday(NSDate) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isDateInYesterday(_ date: NSDate!) -> Bool ``` | OS X 10.10 |
| To | ``` func isDateInYesterday(_ date: NSDate) -> Bool ``` | OS X 10.9 |

Modified NSCalendar.locale

|  | Declaration |
| --- | --- |
| From | ``` var locale: NSLocale! ``` |
| To | ``` @NSCopying var locale: NSLocale? ``` |

Modified NSCalendar.longEraSymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var longEraSymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var longEraSymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.monthSymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var monthSymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var monthSymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.nextDateAfterDate(NSDate, matchingComponents: NSDateComponents, options: NSCalendarOptions) -> NSDate?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func nextDateAfterDate(_ date: NSDate!, matchingComponents comps: NSDateComponents!, options options: NSCalendarOptions) -> NSDate! ``` | OS X 10.10 |
| To | ``` func nextDateAfterDate(_ date: NSDate, matchingComponents comps: NSDateComponents, options options: NSCalendarOptions) -> NSDate? ``` | OS X 10.9 |

Modified NSCalendar.nextDateAfterDate(NSDate, matchingHour: Int, minute: Int, second: Int, options: NSCalendarOptions) -> NSDate?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func nextDateAfterDate(_ date: NSDate!, matchingHour hourValue: Int, minute minuteValue: Int, second secondValue: Int, options options: NSCalendarOptions) -> NSDate! ``` | OS X 10.10 |
| To | ``` func nextDateAfterDate(_ date: NSDate, matchingHour hourValue: Int, minute minuteValue: Int, second secondValue: Int, options options: NSCalendarOptions) -> NSDate? ``` | OS X 10.9 |

Modified NSCalendar.nextDateAfterDate(NSDate, matchingUnit: NSCalendarUnit, value: Int, options: NSCalendarOptions) -> NSDate?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func nextDateAfterDate(_ date: NSDate!, matchingUnit unit: NSCalendarUnit, value value: Int, options options: NSCalendarOptions) -> NSDate! ``` | OS X 10.10 |
| To | ``` func nextDateAfterDate(_ date: NSDate, matchingUnit unit: NSCalendarUnit, value value: Int, options options: NSCalendarOptions) -> NSDate? ``` | OS X 10.9 |

Modified NSCalendar.nextWeekendStartDate(AutoreleasingUnsafeMutablePointer<NSDate?>, interval: UnsafeMutablePointer<NSTimeInterval>, options: NSCalendarOptions, afterDate: NSDate) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func nextWeekendStartDate(_ datep: AutoreleasingUnsafePointer<NSDate?>, interval tip: UnsafePointer<NSTimeInterval>, options options: NSCalendarOptions, afterDate date: NSDate!) -> Bool ``` | OS X 10.10 |
| To | ``` func nextWeekendStartDate(_ datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, options options: NSCalendarOptions, afterDate date: NSDate) -> Bool ``` | OS X 10.9 |

Modified NSCalendar.ordinalityOfUnit(NSCalendarUnit, inUnit: NSCalendarUnit, forDate: NSDate) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func ordinalityOfUnit(_ smaller: NSCalendarUnit, inUnit larger: NSCalendarUnit, forDate date: NSDate!) -> Int ``` |
| To | ``` func ordinalityOfUnit(_ smaller: NSCalendarUnit, inUnit larger: NSCalendarUnit, forDate date: NSDate) -> Int ``` |

Modified NSCalendar.quarterSymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var quarterSymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var quarterSymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.rangeOfUnit(NSCalendarUnit, inUnit: NSCalendarUnit, forDate: NSDate) -> NSRange

|  | Declaration |
| --- | --- |
| From | ``` func rangeOfUnit(_ smaller: NSCalendarUnit, inUnit larger: NSCalendarUnit, forDate date: NSDate!) -> NSRange ``` |
| To | ``` func rangeOfUnit(_ smaller: NSCalendarUnit, inUnit larger: NSCalendarUnit, forDate date: NSDate) -> NSRange ``` |

Modified NSCalendar.rangeOfUnit(NSCalendarUnit, startDate: AutoreleasingUnsafeMutablePointer<NSDate?>, interval: UnsafeMutablePointer<NSTimeInterval>, forDate: NSDate) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func rangeOfUnit(_ unit: NSCalendarUnit, startDate datep: AutoreleasingUnsafePointer<NSDate?>, interval tip: UnsafePointer<NSTimeInterval>, forDate date: NSDate!) -> Bool ``` | OS X 10.10 |
| To | ``` func rangeOfUnit(_ unit: NSCalendarUnit, startDate datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, forDate date: NSDate) -> Bool ``` | OS X 10.5 |

Modified NSCalendar.rangeOfWeekendStartDate(AutoreleasingUnsafeMutablePointer<NSDate?>, interval: UnsafeMutablePointer<NSTimeInterval>, containingDate: NSDate) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func rangeOfWeekendStartDate(_ datep: AutoreleasingUnsafePointer<NSDate?>, interval tip: UnsafePointer<NSTimeInterval>, containingDate date: NSDate!) -> Bool ``` | OS X 10.10 |
| To | ``` func rangeOfWeekendStartDate(_ datep: AutoreleasingUnsafeMutablePointer<NSDate?>, interval tip: UnsafeMutablePointer<NSTimeInterval>, containingDate date: NSDate) -> Bool ``` | OS X 10.9 |

Modified NSCalendar.shortMonthSymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var shortMonthSymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var shortMonthSymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.shortQuarterSymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var shortQuarterSymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var shortQuarterSymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.shortStandaloneMonthSymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var shortStandaloneMonthSymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var shortStandaloneMonthSymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.shortStandaloneQuarterSymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var shortStandaloneQuarterSymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var shortStandaloneQuarterSymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.shortStandaloneWeekdaySymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var shortStandaloneWeekdaySymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var shortStandaloneWeekdaySymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.shortWeekdaySymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var shortWeekdaySymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var shortWeekdaySymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.standaloneMonthSymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var standaloneMonthSymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var standaloneMonthSymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.standaloneQuarterSymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var standaloneQuarterSymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var standaloneQuarterSymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.standaloneWeekdaySymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var standaloneWeekdaySymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var standaloneWeekdaySymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.startOfDayForDate(NSDate) -> NSDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func startOfDayForDate(_ date: NSDate!) -> NSDate! ``` | OS X 10.10 |
| To | ``` func startOfDayForDate(_ date: NSDate) -> NSDate ``` | OS X 10.9 |

Modified NSCalendar.timeZone

|  | Declaration |
| --- | --- |
| From | ``` var timeZone: NSTimeZone! ``` |
| To | ``` @NSCopying var timeZone: NSTimeZone ``` |

Modified NSCalendar.veryShortMonthSymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var veryShortMonthSymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var veryShortMonthSymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.veryShortStandaloneMonthSymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var veryShortStandaloneMonthSymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var veryShortStandaloneMonthSymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.veryShortStandaloneWeekdaySymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var veryShortStandaloneWeekdaySymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var veryShortStandaloneWeekdaySymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.veryShortWeekdaySymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var veryShortWeekdaySymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var veryShortWeekdaySymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendar.weekdaySymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var weekdaySymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var weekdaySymbols: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSCalendarOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSCalendarOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var WrapComponents: NSCalendarOptions { get }     static var MatchStrictly: NSCalendarOptions { get }     static var SearchBackwards: NSCalendarOptions { get }     static var MatchPreviousTimePreservingSmallerUnits: NSCalendarOptions { get }     static var MatchNextTimePreservingSmallerUnits: NSCalendarOptions { get }     static var MatchNextTime: NSCalendarOptions { get }     static var MatchFirst: NSCalendarOptions { get }     static var MatchLast: NSCalendarOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSCalendarOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var WrapComponents: NSCalendarOptions { get }     static var MatchStrictly: NSCalendarOptions { get }     static var SearchBackwards: NSCalendarOptions { get }     static var MatchPreviousTimePreservingSmallerUnits: NSCalendarOptions { get }     static var MatchNextTimePreservingSmallerUnits: NSCalendarOptions { get }     static var MatchNextTime: NSCalendarOptions { get }     static var MatchFirst: NSCalendarOptions { get }     static var MatchLast: NSCalendarOptions { get } } ``` | RawOptionSetType |

Modified NSCalendarOptions.MatchFirst

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSCalendarOptions.MatchLast

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSCalendarOptions.MatchNextTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSCalendarOptions.MatchNextTimePreservingSmallerUnits

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSCalendarOptions.MatchPreviousTimePreservingSmallerUnits

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSCalendarOptions.MatchStrictly

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSCalendarOptions.SearchBackwards

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSCalendarOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSCalendarUnit [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSCalendarUnit : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var CalendarUnitEra: NSCalendarUnit { get }     static var CalendarUnitYear: NSCalendarUnit { get }     static var CalendarUnitMonth: NSCalendarUnit { get }     static var CalendarUnitDay: NSCalendarUnit { get }     static var CalendarUnitHour: NSCalendarUnit { get }     static var CalendarUnitMinute: NSCalendarUnit { get }     static var CalendarUnitSecond: NSCalendarUnit { get }     static var CalendarUnitWeekday: NSCalendarUnit { get }     static var CalendarUnitWeekdayOrdinal: NSCalendarUnit { get }     static var CalendarUnitQuarter: NSCalendarUnit { get }     static var CalendarUnitWeekOfMonth: NSCalendarUnit { get }     static var CalendarUnitWeekOfYear: NSCalendarUnit { get }     static var CalendarUnitYearForWeekOfYear: NSCalendarUnit { get }     static var CalendarUnitNanosecond: NSCalendarUnit { get }     static var CalendarUnitCalendar: NSCalendarUnit { get }     static var CalendarUnitTimeZone: NSCalendarUnit { get }     static var EraCalendarUnit: NSCalendarUnit { get }     static var YearCalendarUnit: NSCalendarUnit { get }     static var MonthCalendarUnit: NSCalendarUnit { get }     static var DayCalendarUnit: NSCalendarUnit { get }     static var HourCalendarUnit: NSCalendarUnit { get }     static var MinuteCalendarUnit: NSCalendarUnit { get }     static var SecondCalendarUnit: NSCalendarUnit { get }     static var WeekCalendarUnit: NSCalendarUnit { get }     static var WeekdayCalendarUnit: NSCalendarUnit { get }     static var WeekdayOrdinalCalendarUnit: NSCalendarUnit { get }     static var QuarterCalendarUnit: NSCalendarUnit { get }     static var WeekOfMonthCalendarUnit: NSCalendarUnit { get }     static var WeekOfYearCalendarUnit: NSCalendarUnit { get }     static var YearForWeekOfYearCalendarUnit: NSCalendarUnit { get }     static var CalendarCalendarUnit: NSCalendarUnit { get }     static var TimeZoneCalendarUnit: NSCalendarUnit { get } } ``` | RawOptionSet |
| To | ``` struct NSCalendarUnit : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var CalendarUnitEra: NSCalendarUnit { get }     static var CalendarUnitYear: NSCalendarUnit { get }     static var CalendarUnitMonth: NSCalendarUnit { get }     static var CalendarUnitDay: NSCalendarUnit { get }     static var CalendarUnitHour: NSCalendarUnit { get }     static var CalendarUnitMinute: NSCalendarUnit { get }     static var CalendarUnitSecond: NSCalendarUnit { get }     static var CalendarUnitWeekday: NSCalendarUnit { get }     static var CalendarUnitWeekdayOrdinal: NSCalendarUnit { get }     static var CalendarUnitQuarter: NSCalendarUnit { get }     static var CalendarUnitWeekOfMonth: NSCalendarUnit { get }     static var CalendarUnitWeekOfYear: NSCalendarUnit { get }     static var CalendarUnitYearForWeekOfYear: NSCalendarUnit { get }     static var CalendarUnitNanosecond: NSCalendarUnit { get }     static var CalendarUnitCalendar: NSCalendarUnit { get }     static var CalendarUnitTimeZone: NSCalendarUnit { get }     static var EraCalendarUnit: NSCalendarUnit { get }     static var YearCalendarUnit: NSCalendarUnit { get }     static var MonthCalendarUnit: NSCalendarUnit { get }     static var DayCalendarUnit: NSCalendarUnit { get }     static var HourCalendarUnit: NSCalendarUnit { get }     static var MinuteCalendarUnit: NSCalendarUnit { get }     static var SecondCalendarUnit: NSCalendarUnit { get }     static var WeekCalendarUnit: NSCalendarUnit { get }     static var WeekdayCalendarUnit: NSCalendarUnit { get }     static var WeekdayOrdinalCalendarUnit: NSCalendarUnit { get }     static var QuarterCalendarUnit: NSCalendarUnit { get }     static var WeekOfMonthCalendarUnit: NSCalendarUnit { get }     static var WeekOfYearCalendarUnit: NSCalendarUnit { get }     static var YearForWeekOfYearCalendarUnit: NSCalendarUnit { get }     static var CalendarCalendarUnit: NSCalendarUnit { get }     static var TimeZoneCalendarUnit: NSCalendarUnit { get } } ``` | RawOptionSetType |

Modified NSCalendarUnit.CalendarCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | OS X 10.10 |

Modified NSCalendarUnit.CalendarUnitCalendar

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSCalendarUnit.CalendarUnitNanosecond

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSCalendarUnit.CalendarUnitQuarter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSCalendarUnit.CalendarUnitTimeZone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSCalendarUnit.CalendarUnitWeekOfMonth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSCalendarUnit.CalendarUnitWeekOfYear

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSCalendarUnit.CalendarUnitYearForWeekOfYear

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSCalendarUnit.DayCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSCalendarUnit.EraCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSCalendarUnit.HourCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSCalendarUnit.MinuteCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSCalendarUnit.MonthCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSCalendarUnit.QuarterCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.6 | OS X 10.10 |

Modified NSCalendarUnit.SecondCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSCalendarUnit.TimeZoneCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | OS X 10.10 |

Modified NSCalendarUnit.WeekCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSCalendarUnit.WeekOfMonthCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | OS X 10.10 |

Modified NSCalendarUnit.WeekOfYearCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | OS X 10.10 |

Modified NSCalendarUnit.WeekdayCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSCalendarUnit.WeekdayOrdinalCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSCalendarUnit.YearCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSCalendarUnit.YearForWeekOfYearCalendarUnit

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | OS X 10.10 |

Modified NSCalendarUnit.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSCharacterSet.URLFragmentAllowedCharacterSet() -> NSCharacterSet [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func URLFragmentAllowedCharacterSet() -> NSCharacterSet! ``` | OS X 10.10 |
| To | ``` class func URLFragmentAllowedCharacterSet() -> NSCharacterSet ``` | OS X 10.9 |

Modified NSCharacterSet.URLHostAllowedCharacterSet() -> NSCharacterSet [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func URLHostAllowedCharacterSet() -> NSCharacterSet! ``` | OS X 10.10 |
| To | ``` class func URLHostAllowedCharacterSet() -> NSCharacterSet ``` | OS X 10.9 |

Modified NSCharacterSet.URLPasswordAllowedCharacterSet() -> NSCharacterSet [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func URLPasswordAllowedCharacterSet() -> NSCharacterSet! ``` | OS X 10.10 |
| To | ``` class func URLPasswordAllowedCharacterSet() -> NSCharacterSet ``` | OS X 10.9 |

Modified NSCharacterSet.URLPathAllowedCharacterSet() -> NSCharacterSet [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func URLPathAllowedCharacterSet() -> NSCharacterSet! ``` | OS X 10.10 |
| To | ``` class func URLPathAllowedCharacterSet() -> NSCharacterSet ``` | OS X 10.9 |

Modified NSCharacterSet.URLQueryAllowedCharacterSet() -> NSCharacterSet [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func URLQueryAllowedCharacterSet() -> NSCharacterSet! ``` | OS X 10.10 |
| To | ``` class func URLQueryAllowedCharacterSet() -> NSCharacterSet ``` | OS X 10.9 |

Modified NSCharacterSet.URLUserAllowedCharacterSet() -> NSCharacterSet [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func URLUserAllowedCharacterSet() -> NSCharacterSet! ``` | OS X 10.10 |
| To | ``` class func URLUserAllowedCharacterSet() -> NSCharacterSet ``` | OS X 10.9 |

Modified NSCharacterSet.alphanumericCharacterSet() -> NSCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func alphanumericCharacterSet() -> NSCharacterSet! ``` |
| To | ``` class func alphanumericCharacterSet() -> NSCharacterSet ``` |

Modified NSCharacterSet.bitmapRepresentation

|  | Declaration |
| --- | --- |
| From | ``` var bitmapRepresentation: NSData! { get } ``` |
| To | ``` @NSCopying var bitmapRepresentation: NSData { get } ``` |

Modified NSCharacterSet.init(bitmapRepresentation: NSData)

|  | Declaration |
| --- | --- |
| From | ``` init(bitmapRepresentation data: NSData!) -> NSCharacterSet ``` |
| To | ``` init(bitmapRepresentation data: NSData) -> NSCharacterSet ``` |

Modified NSCharacterSet.capitalizedLetterCharacterSet() -> NSCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func capitalizedLetterCharacterSet() -> NSCharacterSet! ``` |
| To | ``` class func capitalizedLetterCharacterSet() -> NSCharacterSet ``` |

Modified NSCharacterSet.init(charactersInString: String)

|  | Declaration |
| --- | --- |
| From | ``` init(charactersInString aString: String!) -> NSCharacterSet ``` |
| To | ``` init(charactersInString aString: String) -> NSCharacterSet ``` |

Modified NSCharacterSet.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init(coder aDecoder: NSCoder) ``` |

Modified NSCharacterSet.init(contentsOfFile: String)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfFile fName: String!) -> NSCharacterSet ``` |
| To | ``` init?(contentsOfFile fName: String) -> NSCharacterSet ``` |

Modified NSCharacterSet.controlCharacterSet() -> NSCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func controlCharacterSet() -> NSCharacterSet! ``` |
| To | ``` class func controlCharacterSet() -> NSCharacterSet ``` |

Modified NSCharacterSet.decimalDigitCharacterSet() -> NSCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func decimalDigitCharacterSet() -> NSCharacterSet! ``` |
| To | ``` class func decimalDigitCharacterSet() -> NSCharacterSet ``` |

Modified NSCharacterSet.decomposableCharacterSet() -> NSCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func decomposableCharacterSet() -> NSCharacterSet! ``` |
| To | ``` class func decomposableCharacterSet() -> NSCharacterSet ``` |

Modified NSCharacterSet.illegalCharacterSet() -> NSCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func illegalCharacterSet() -> NSCharacterSet! ``` |
| To | ``` class func illegalCharacterSet() -> NSCharacterSet ``` |

Modified NSCharacterSet.invertedSet

|  | Declaration |
| --- | --- |
| From | ``` var invertedSet: NSCharacterSet! { get } ``` |
| To | ``` @NSCopying var invertedSet: NSCharacterSet { get } ``` |

Modified NSCharacterSet.isSupersetOfSet(NSCharacterSet) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isSupersetOfSet(_ theOtherSet: NSCharacterSet!) -> Bool ``` |
| To | ``` func isSupersetOfSet(_ theOtherSet: NSCharacterSet) -> Bool ``` |

Modified NSCharacterSet.letterCharacterSet() -> NSCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func letterCharacterSet() -> NSCharacterSet! ``` |
| To | ``` class func letterCharacterSet() -> NSCharacterSet ``` |

Modified NSCharacterSet.lowercaseLetterCharacterSet() -> NSCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func lowercaseLetterCharacterSet() -> NSCharacterSet! ``` |
| To | ``` class func lowercaseLetterCharacterSet() -> NSCharacterSet ``` |

Modified NSCharacterSet.newlineCharacterSet() -> NSCharacterSet [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func newlineCharacterSet() -> NSCharacterSet! ``` | OS X 10.10 |
| To | ``` class func newlineCharacterSet() -> NSCharacterSet ``` | OS X 10.5 |

Modified NSCharacterSet.nonBaseCharacterSet() -> NSCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func nonBaseCharacterSet() -> NSCharacterSet! ``` |
| To | ``` class func nonBaseCharacterSet() -> NSCharacterSet ``` |

Modified NSCharacterSet.punctuationCharacterSet() -> NSCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func punctuationCharacterSet() -> NSCharacterSet! ``` |
| To | ``` class func punctuationCharacterSet() -> NSCharacterSet ``` |

Modified NSCharacterSet.symbolCharacterSet() -> NSCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func symbolCharacterSet() -> NSCharacterSet! ``` |
| To | ``` class func symbolCharacterSet() -> NSCharacterSet ``` |

Modified NSCharacterSet.uppercaseLetterCharacterSet() -> NSCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func uppercaseLetterCharacterSet() -> NSCharacterSet! ``` |
| To | ``` class func uppercaseLetterCharacterSet() -> NSCharacterSet ``` |

Modified NSCharacterSet.whitespaceAndNewlineCharacterSet() -> NSCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func whitespaceAndNewlineCharacterSet() -> NSCharacterSet! ``` |
| To | ``` class func whitespaceAndNewlineCharacterSet() -> NSCharacterSet ``` |

Modified NSCharacterSet.whitespaceCharacterSet() -> NSCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func whitespaceCharacterSet() -> NSCharacterSet! ``` |
| To | ``` class func whitespaceCharacterSet() -> NSCharacterSet ``` |

Modified NSClassDescription.attributeKeys

|  | Declaration |
| --- | --- |
| From | ``` var attributeKeys: [AnyObject]! { get } ``` |
| To | ``` var attributeKeys: [AnyObject] { get } ``` |

Modified NSClassDescription.init(forClass: AnyClass!)

|  | Declaration |
| --- | --- |
| From | ``` init(forClass aClass: AnyClass!) -> NSClassDescription ``` |
| To | ``` init?(forClass aClass: AnyClass!) -> NSClassDescription ``` |

Modified NSClassDescription.inverseForRelationshipKey(String) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func inverseForRelationshipKey(_ relationshipKey: String!) -> String! ``` |
| To | ``` func inverseForRelationshipKey(_ relationshipKey: String) -> String? ``` |

Modified NSClassDescription.registerClassDescription(NSClassDescription, forClass: AnyClass) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func registerClassDescription(_ description: NSClassDescription!, forClass aClass: AnyClass!) ``` |
| To | ``` class func registerClassDescription(_ description: NSClassDescription, forClass aClass: AnyClass) ``` |

Modified NSClassDescription.toManyRelationshipKeys

|  | Declaration |
| --- | --- |
| From | ``` var toManyRelationshipKeys: [AnyObject]! { get } ``` |
| To | ``` var toManyRelationshipKeys: [AnyObject] { get } ``` |

Modified NSClassDescription.toOneRelationshipKeys

|  | Declaration |
| --- | --- |
| From | ``` var toOneRelationshipKeys: [AnyObject]! { get } ``` |
| To | ``` var toOneRelationshipKeys: [AnyObject] { get } ``` |

Modified NSCloneCommand.setReceiversSpecifier(NSScriptObjectSpecifier)

|  | Declaration |
| --- | --- |
| From | ``` func setReceiversSpecifier(_ receiversRef: NSScriptObjectSpecifier!) ``` |
| To | ``` func setReceiversSpecifier(_ receiversRef: NSScriptObjectSpecifier) ``` |

Modified NSCoder.allowedClasses

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var allowedClasses: NSSet! { get } ``` | OS X 10.10 |
| To | ``` var allowedClasses: Set<NSObject>? { get } ``` | OS X 10.8 |

Modified NSCoder.containsValueForKey(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func containsValueForKey(_ key: String!) -> Bool ``` |
| To | ``` func containsValueForKey(_ key: String) -> Bool ``` |

Modified NSCoder.decodeArrayOfObjCType(UnsafePointer<Int8>, count: Int, at: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func decodeArrayOfObjCType(_ itemType: ConstUnsafePointer<Int8>, count count: Int, at array: UnsafePointer<()>) ``` |
| To | ``` func decodeArrayOfObjCType(_ itemType: UnsafePointer<Int8>, count count: Int, at array: UnsafeMutablePointer<Void>) ``` |

Modified NSCoder.decodeBoolForKey(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func decodeBoolForKey(_ key: String!) -> Bool ``` |
| To | ``` func decodeBoolForKey(_ key: String) -> Bool ``` |

Modified NSCoder.decodeBytesForKey(String, returnedLength: UnsafeMutablePointer<Int>) -> UnsafePointer<UInt8>

|  | Declaration |
| --- | --- |
| From | ``` func decodeBytesForKey(_ key: String!, returnedLength lengthp: UnsafePointer<Int>) -> ConstUnsafePointer<UInt8> ``` |
| To | ``` func decodeBytesForKey(_ key: String, returnedLength lengthp: UnsafeMutablePointer<Int>) -> UnsafePointer<UInt8> ``` |

Modified NSCoder.decodeBytesWithReturnedLength(UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func decodeBytesWithReturnedLength(_ lengthp: UnsafePointer<Int>) -> UnsafePointer<()> ``` |
| To | ``` func decodeBytesWithReturnedLength(_ lengthp: UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<Void> ``` |

Modified NSCoder.decodeDataObject() -> NSData?

|  | Declaration |
| --- | --- |
| From | ``` func decodeDataObject() -> NSData! ``` |
| To | ``` func decodeDataObject() -> NSData? ``` |

Modified NSCoder.decodeDoubleForKey(String) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func decodeDoubleForKey(_ key: String!) -> Double ``` |
| To | ``` func decodeDoubleForKey(_ key: String) -> Double ``` |

Modified NSCoder.decodeFloatForKey(String) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func decodeFloatForKey(_ key: String!) -> Float ``` |
| To | ``` func decodeFloatForKey(_ key: String) -> Float ``` |

Modified NSCoder.decodeInt32ForKey(String) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func decodeInt32ForKey(_ key: String!) -> Int32 ``` |
| To | ``` func decodeInt32ForKey(_ key: String) -> Int32 ``` |

Modified NSCoder.decodeInt64ForKey(String) -> Int64

|  | Declaration |
| --- | --- |
| From | ``` func decodeInt64ForKey(_ key: String!) -> Int64 ``` |
| To | ``` func decodeInt64ForKey(_ key: String) -> Int64 ``` |

Modified NSCoder.decodeIntForKey(String) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func decodeIntForKey(_ key: String!) -> Int32 ``` |
| To | ``` func decodeIntForKey(_ key: String) -> Int32 ``` |

Modified NSCoder.decodeIntegerForKey(String) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func decodeIntegerForKey(_ key: String!) -> Int ``` | OS X 10.10 |
| To | ``` func decodeIntegerForKey(_ key: String) -> Int ``` | OS X 10.5 |

Modified NSCoder.decodeObject() -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func decodeObject() -> AnyObject! ``` |
| To | ``` func decodeObject() -> AnyObject? ``` |

Modified NSCoder.decodeObjectForKey(String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func decodeObjectForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` func decodeObjectForKey(_ key: String) -> AnyObject? ``` |

Modified NSCoder.decodeObjectOfClass(AnyClass, forKey: String) -> AnyObject?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func decodeObjectOfClass(_ aClass: AnyClass!, forKey key: String!) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func decodeObjectOfClass(_ aClass: AnyClass, forKey key: String) -> AnyObject? ``` | OS X 10.8 |

Modified NSCoder.decodeObjectOfClasses(Set<NSObject>, forKey: String) -> AnyObject?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func decodeObjectOfClasses(_ classes: NSSet!, forKey key: String!) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func decodeObjectOfClasses(_ classes: Set<NSObject>, forKey key: String) -> AnyObject? ``` | OS X 10.8 |

Modified NSCoder.decodePointForKey(String) -> NSPoint

|  | Declaration |
| --- | --- |
| From | ``` func decodePointForKey(_ key: String!) -> NSPoint ``` |
| To | ``` func decodePointForKey(_ key: String) -> NSPoint ``` |

Modified NSCoder.decodePropertyList() -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func decodePropertyList() -> AnyObject! ``` |
| To | ``` func decodePropertyList() -> AnyObject? ``` |

Modified NSCoder.decodePropertyListForKey(String) -> AnyObject?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func decodePropertyListForKey(_ key: String!) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func decodePropertyListForKey(_ key: String) -> AnyObject? ``` | OS X 10.8 |

Modified NSCoder.decodeRectForKey(String) -> NSRect

|  | Declaration |
| --- | --- |
| From | ``` func decodeRectForKey(_ key: String!) -> NSRect ``` |
| To | ``` func decodeRectForKey(_ key: String) -> NSRect ``` |

Modified NSCoder.decodeSizeForKey(String) -> NSSize

|  | Declaration |
| --- | --- |
| From | ``` func decodeSizeForKey(_ key: String!) -> NSSize ``` |
| To | ``` func decodeSizeForKey(_ key: String) -> NSSize ``` |

Modified NSCoder.decodeValueOfObjCType(UnsafePointer<Int8>, at: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func decodeValueOfObjCType(_ type: ConstUnsafePointer<Int8>, at data: UnsafePointer<()>) ``` |
| To | ``` func decodeValueOfObjCType(_ type: UnsafePointer<Int8>, at data: UnsafeMutablePointer<Void>) ``` |

Modified NSCoder.encodeArrayOfObjCType(UnsafePointer<Int8>, count: Int, at: UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func encodeArrayOfObjCType(_ type: ConstUnsafePointer<Int8>, count count: Int, at array: ConstUnsafePointer<()>) ``` |
| To | ``` func encodeArrayOfObjCType(_ type: UnsafePointer<Int8>, count count: Int, at array: UnsafePointer<Void>) ``` |

Modified NSCoder.encodeBool(Bool, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeBool(_ boolv: Bool, forKey key: String!) ``` |
| To | ``` func encodeBool(_ boolv: Bool, forKey key: String) ``` |

Modified NSCoder.encodeBycopyObject(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func encodeBycopyObject(_ anObject: AnyObject!) ``` |
| To | ``` func encodeBycopyObject(_ anObject: AnyObject?) ``` |

Modified NSCoder.encodeByrefObject(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func encodeByrefObject(_ anObject: AnyObject!) ``` |
| To | ``` func encodeByrefObject(_ anObject: AnyObject?) ``` |

Modified NSCoder.encodeBytes(UnsafePointer<UInt8>, length: Int, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeBytes(_ bytesp: ConstUnsafePointer<UInt8>, length lenv: Int, forKey key: String!) ``` |
| To | ``` func encodeBytes(_ bytesp: UnsafePointer<UInt8>, length lenv: Int, forKey key: String) ``` |

Modified NSCoder.encodeBytes(UnsafePointer<Void>, length: Int)

|  | Declaration |
| --- | --- |
| From | ``` func encodeBytes(_ byteaddr: ConstUnsafePointer<()>, length length: Int) ``` |
| To | ``` func encodeBytes(_ byteaddr: UnsafePointer<Void>, length length: Int) ``` |

Modified NSCoder.encodeConditionalObject(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func encodeConditionalObject(_ object: AnyObject!) ``` |
| To | ``` func encodeConditionalObject(_ object: AnyObject?) ``` |

Modified NSCoder.encodeConditionalObject(AnyObject?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeConditionalObject(_ objv: AnyObject!, forKey key: String!) ``` |
| To | ``` func encodeConditionalObject(_ objv: AnyObject?, forKey key: String) ``` |

Modified NSCoder.encodeDataObject(NSData)

|  | Declaration |
| --- | --- |
| From | ``` func encodeDataObject(_ data: NSData!) ``` |
| To | ``` func encodeDataObject(_ data: NSData) ``` |

Modified NSCoder.encodeDouble(Double, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeDouble(_ realv: Double, forKey key: String!) ``` |
| To | ``` func encodeDouble(_ realv: Double, forKey key: String) ``` |

Modified NSCoder.encodeFloat(Float, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeFloat(_ realv: Float, forKey key: String!) ``` |
| To | ``` func encodeFloat(_ realv: Float, forKey key: String) ``` |

Modified NSCoder.encodeInt(Int32, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeInt(_ intv: Int32, forKey key: String!) ``` |
| To | ``` func encodeInt(_ intv: Int32, forKey key: String) ``` |

Modified NSCoder.encodeInt32(Int32, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeInt32(_ intv: Int32, forKey key: String!) ``` |
| To | ``` func encodeInt32(_ intv: Int32, forKey key: String) ``` |

Modified NSCoder.encodeInt64(Int64, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeInt64(_ intv: Int64, forKey key: String!) ``` |
| To | ``` func encodeInt64(_ intv: Int64, forKey key: String) ``` |

Modified NSCoder.encodeInteger(Int, forKey: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func encodeInteger(_ intv: Int, forKey key: String!) ``` | OS X 10.10 |
| To | ``` func encodeInteger(_ intv: Int, forKey key: String) ``` | OS X 10.5 |

Modified NSCoder.encodeObject(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func encodeObject(_ object: AnyObject!) ``` |
| To | ``` func encodeObject(_ object: AnyObject?) ``` |

Modified NSCoder.encodeObject(AnyObject?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeObject(_ objv: AnyObject!, forKey key: String!) ``` |
| To | ``` func encodeObject(_ objv: AnyObject?, forKey key: String) ``` |

Modified NSCoder.encodePoint(NSPoint, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodePoint(_ point: NSPoint, forKey key: String!) ``` |
| To | ``` func encodePoint(_ point: NSPoint, forKey key: String) ``` |

Modified NSCoder.encodePropertyList(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func encodePropertyList(_ aPropertyList: AnyObject!) ``` |
| To | ``` func encodePropertyList(_ aPropertyList: AnyObject) ``` |

Modified NSCoder.encodeRect(NSRect, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeRect(_ rect: NSRect, forKey key: String!) ``` |
| To | ``` func encodeRect(_ rect: NSRect, forKey key: String) ``` |

Modified NSCoder.encodeRootObject(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func encodeRootObject(_ rootObject: AnyObject!) ``` |
| To | ``` func encodeRootObject(_ rootObject: AnyObject) ``` |

Modified NSCoder.encodeSize(NSSize, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeSize(_ size: NSSize, forKey key: String!) ``` |
| To | ``` func encodeSize(_ size: NSSize, forKey key: String) ``` |

Modified NSCoder.encodeValueOfObjCType(UnsafePointer<Int8>, at: UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func encodeValueOfObjCType(_ type: ConstUnsafePointer<Int8>, at addr: ConstUnsafePointer<()>) ``` |
| To | ``` func encodeValueOfObjCType(_ type: UnsafePointer<Int8>, at addr: UnsafePointer<Void>) ``` |

Modified NSCoder.requiresSecureCoding

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSCoder.versionForClassName(String) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func versionForClassName(_ className: String!) -> Int ``` |
| To | ``` func versionForClassName(_ className: String) -> Int ``` |

Modified NSCoding.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init(coder aDecoder: NSCoder) ``` |

Modified NSCoding.encodeWithCoder(NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` func encodeWithCoder(_ aCoder: NSCoder!) ``` |
| To | ``` func encodeWithCoder(_ aCoder: NSCoder) ``` |

Modified NSComparisonPredicate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSComparisonPredicate.leftExpression

|  | Declaration |
| --- | --- |
| From | ``` var leftExpression: NSExpression! { get } ``` |
| To | ``` var leftExpression: NSExpression { get } ``` |

Modified NSComparisonPredicate.rightExpression

|  | Declaration |
| --- | --- |
| From | ``` var rightExpression: NSExpression! { get } ``` |
| To | ``` var rightExpression: NSExpression { get } ``` |

Modified NSComparisonPredicateOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSComparisonPredicateOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var CaseInsensitivePredicateOption: NSComparisonPredicateOptions { get }     static var DiacriticInsensitivePredicateOption: NSComparisonPredicateOptions { get }     static var NormalizedPredicateOption: NSComparisonPredicateOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSComparisonPredicateOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var CaseInsensitivePredicateOption: NSComparisonPredicateOptions { get }     static var DiacriticInsensitivePredicateOption: NSComparisonPredicateOptions { get }     static var NormalizedPredicateOption: NSComparisonPredicateOptions { get } } ``` | RawOptionSetType |

Modified NSComparisonPredicateOptions.NormalizedPredicateOption

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSComparisonPredicateOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSCompoundPredicate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSCompoundPredicate.andPredicateWithSubpredicates([AnyObject]) -> NSCompoundPredicate [class]

|  | Declaration |
| --- | --- |
| From | ``` class func andPredicateWithSubpredicates(_ subpredicates: [AnyObject]!) -> NSCompoundPredicate! ``` |
| To | ``` class func andPredicateWithSubpredicates(_ subpredicates: [AnyObject]) -> NSCompoundPredicate ``` |

Modified NSCompoundPredicate.notPredicateWithSubpredicate(NSPredicate) -> NSCompoundPredicate [class]

|  | Declaration |
| --- | --- |
| From | ``` class func notPredicateWithSubpredicate(_ predicate: NSPredicate!) -> NSCompoundPredicate! ``` |
| To | ``` class func notPredicateWithSubpredicate(_ predicate: NSPredicate) -> NSCompoundPredicate ``` |

Modified NSCompoundPredicate.orPredicateWithSubpredicates([AnyObject]) -> NSCompoundPredicate [class]

|  | Declaration |
| --- | --- |
| From | ``` class func orPredicateWithSubpredicates(_ subpredicates: [AnyObject]!) -> NSCompoundPredicate! ``` |
| To | ``` class func orPredicateWithSubpredicates(_ subpredicates: [AnyObject]) -> NSCompoundPredicate ``` |

Modified NSCompoundPredicate.subpredicates

|  | Declaration |
| --- | --- |
| From | ``` var subpredicates: [AnyObject]! { get } ``` |
| To | ``` var subpredicates: [AnyObject] { get } ``` |

Modified NSCondition

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSCondition.name

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var name: String! ``` | OS X 10.10 |
| To | ``` var name: String? ``` | OS X 10.5 |

Modified NSCondition.waitUntilDate(NSDate) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func waitUntilDate(_ limit: NSDate!) -> Bool ``` |
| To | ``` func waitUntilDate(_ limit: NSDate) -> Bool ``` |

Modified NSConditionLock.lockBeforeDate(NSDate) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func lockBeforeDate(_ limit: NSDate!) -> Bool ``` |
| To | ``` func lockBeforeDate(_ limit: NSDate) -> Bool ``` |

Modified NSConditionLock.lockWhenCondition(Int, beforeDate: NSDate) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func lockWhenCondition(_ condition: Int, beforeDate limit: NSDate!) -> Bool ``` |
| To | ``` func lockWhenCondition(_ condition: Int, beforeDate limit: NSDate) -> Bool ``` |

Modified NSConditionLock.name

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var name: String! ``` | OS X 10.10 |
| To | ``` var name: String? ``` | OS X 10.5 |

Modified NSCopying.copyWithZone(NSZone) -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func copyWithZone(_ zone: NSZone) -> AnyObject! ``` |
| To | ``` func copyWithZone(_ zone: NSZone) -> AnyObject ``` |

Modified NSCountedSet.addObject(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func addObject(_ object: AnyObject!) ``` |
| To | ``` func addObject(_ object: AnyObject) ``` |

Modified NSCountedSet.init(array: [AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` convenience init(array array: [AnyObject]!) ``` |
| To | ``` convenience init(array array: [AnyObject]) ``` |

Modified NSCountedSet.countForObject(AnyObject) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func countForObject(_ object: AnyObject!) -> Int ``` |
| To | ``` func countForObject(_ object: AnyObject) -> Int ``` |

Modified NSCountedSet.objectEnumerator() -> NSEnumerator

|  | Declaration |
| --- | --- |
| From | ``` func objectEnumerator() -> NSEnumerator! ``` |
| To | ``` func objectEnumerator() -> NSEnumerator ``` |

Modified NSCountedSet.removeObject(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func removeObject(_ object: AnyObject!) ``` |
| To | ``` func removeObject(_ object: AnyObject) ``` |

Modified NSCountedSet.init(set: Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(set set: NSSet!) ``` | OS X 10.10 |
| To | ``` convenience init(set set: Set<NSObject>) ``` | OS X 10.10.3 |

Modified NSCreateCommand.createClassDescription

|  | Declaration |
| --- | --- |
| From | ``` var createClassDescription: NSScriptClassDescription! { get } ``` |
| To | ``` var createClassDescription: NSScriptClassDescription { get } ``` |

Modified NSCreateCommand.resolvedKeyDictionary

|  | Declaration |
| --- | --- |
| From | ``` var resolvedKeyDictionary: [NSObject : AnyObject]! { get } ``` |
| To | ``` var resolvedKeyDictionary: [NSObject : AnyObject] { get } ``` |

Modified NSData

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | AnyObject, CKRecordValue, NSCoding, NSCopying, NSMutableCopying, NSObjectProtocol, NSSecureCoding |

Modified NSData.init(base64EncodedData: NSData, options: NSDataBase64DecodingOptions)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(base64EncodedData base64Data: NSData!, options options: NSDataBase64DecodingOptions) ``` | OS X 10.10 |
| To | ``` init?(base64EncodedData base64Data: NSData, options options: NSDataBase64DecodingOptions) ``` | OS X 10.9 |

Modified NSData.base64EncodedDataWithOptions(NSDataBase64EncodingOptions) -> NSData

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func base64EncodedDataWithOptions(_ options: NSDataBase64EncodingOptions) -> NSData! ``` | OS X 10.10 |
| To | ``` func base64EncodedDataWithOptions(_ options: NSDataBase64EncodingOptions) -> NSData ``` | OS X 10.9 |

Modified NSData.init(base64EncodedString: String, options: NSDataBase64DecodingOptions)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(base64EncodedString base64String: String!, options options: NSDataBase64DecodingOptions) ``` | OS X 10.10 |
| To | ``` init?(base64EncodedString base64String: String, options options: NSDataBase64DecodingOptions) ``` | OS X 10.9 |

Modified NSData.base64EncodedStringWithOptions(NSDataBase64EncodingOptions) -> String

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func base64EncodedStringWithOptions(_ options: NSDataBase64EncodingOptions) -> String! ``` | OS X 10.10 |
| To | ``` func base64EncodedStringWithOptions(_ options: NSDataBase64EncodingOptions) -> String ``` | OS X 10.9 |

Modified NSData.bytes

|  | Declaration |
| --- | --- |
| From | ``` var bytes: ConstUnsafePointer<()> { get } ``` |
| To | ``` var bytes: UnsafePointer<Void> { get } ``` |

Modified NSData.init(bytes: UnsafePointer<Void>, length: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(bytes bytes: ConstUnsafePointer<()>, length length: Int) ``` |
| To | ``` init(bytes bytes: UnsafePointer<Void>, length length: Int) ``` |

Modified NSData.init(bytesNoCopy: UnsafeMutablePointer<Void>, length: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(bytesNoCopy bytes: UnsafePointer<()>, length length: Int) ``` |
| To | ``` init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int) ``` |

Modified NSData.init(bytesNoCopy: UnsafeMutablePointer<Void>, length: Int, deallocator:((UnsafeMutablePointer<Void>, Int) -> Void)?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(bytesNoCopy bytes: UnsafePointer<()>, length length: Int, deallocator deallocator: ((UnsafePointer<()>, Int) -> Void)!) ``` | OS X 10.10 |
| To | ``` init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, deallocator deallocator: ((UnsafeMutablePointer<Void>, Int) -> Void)?) ``` | OS X 10.9 |

Modified NSData.init(bytesNoCopy: UnsafeMutablePointer<Void>, length: Int, freeWhenDone: Bool)

|  | Declaration |
| --- | --- |
| From | ``` init(bytesNoCopy bytes: UnsafePointer<()>, length length: Int, freeWhenDone b: Bool) ``` |
| To | ``` init(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, freeWhenDone b: Bool) ``` |

Modified NSData.init(contentsOfFile: String, options: NSDataReadingOptions, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfFile path: String!, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer) ``` |
| To | ``` init?(contentsOfFile path: String, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer) ``` |

Modified NSData.init(contentsOfMappedFile: String)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(contentsOfMappedFile path: String!) ``` | OS X 10.10 | -- |
| To | ``` init?(contentsOfMappedFile path: String) ``` | OS X 10.0 | OS X 10.10 |

Modified NSData.init(contentsOfURL: NSURL, options: NSDataReadingOptions, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL url: NSURL!, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer) ``` |
| To | ``` init?(contentsOfURL url: NSURL, options readOptionsMask: NSDataReadingOptions, error errorPtr: NSErrorPointer) ``` |

Modified NSData.init(data: NSData)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData!) ``` |
| To | ``` init(data data: NSData) ``` |

Modified NSData.dataWithContentsOfMappedFile(String) -> AnyObject? [class]

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` class func dataWithContentsOfMappedFile(_ path: String!) -> AnyObject! ``` | OS X 10.10 | -- |
| To | ``` class func dataWithContentsOfMappedFile(_ path: String) -> AnyObject? ``` | OS X 10.0 | OS X 10.10 |

Modified NSData.description

|  | Declaration |
| --- | --- |
| From | ``` var description: String! { get } ``` |
| To | ``` var description: String { get } ``` |

Modified NSData.enumerateByteRangesUsingBlock((UnsafePointer<Void>, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateByteRangesUsingBlock(_ block: ((ConstUnsafePointer<()>, NSRange, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateByteRangesUsingBlock(_ block: (UnsafePointer<Void>, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.9 |

Modified NSData.getBytes(UnsafeMutablePointer<Void>)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func getBytes(_ buffer: UnsafePointer<()>) ``` | OS X 10.10 | -- |
| To | ``` func getBytes(_ buffer: UnsafeMutablePointer<Void>) ``` | OS X 10.0 | OS X 10.10 |

Modified NSData.getBytes(UnsafeMutablePointer<Void>, length: Int)

|  | Declaration |
| --- | --- |
| From | ``` func getBytes(_ buffer: UnsafePointer<()>, length length: Int) ``` |
| To | ``` func getBytes(_ buffer: UnsafeMutablePointer<Void>, length length: Int) ``` |

Modified NSData.getBytes(UnsafeMutablePointer<Void>, range: NSRange)

|  | Declaration |
| --- | --- |
| From | ``` func getBytes(_ buffer: UnsafePointer<()>, range range: NSRange) ``` |
| To | ``` func getBytes(_ buffer: UnsafeMutablePointer<Void>, range range: NSRange) ``` |

Modified NSData.isEqualToData(NSData) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToData(_ other: NSData!) -> Bool ``` |
| To | ``` func isEqualToData(_ other: NSData) -> Bool ``` |

Modified NSData.rangeOfData(NSData, options: NSDataSearchOptions, range: NSRange) -> NSRange

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func rangeOfData(_ dataToFind: NSData!, options mask: NSDataSearchOptions, range searchRange: NSRange) -> NSRange ``` | OS X 10.10 |
| To | ``` func rangeOfData(_ dataToFind: NSData, options mask: NSDataSearchOptions, range searchRange: NSRange) -> NSRange ``` | OS X 10.6 |

Modified NSData.subdataWithRange(NSRange) -> NSData

|  | Declaration |
| --- | --- |
| From | ``` func subdataWithRange(_ range: NSRange) -> NSData! ``` |
| To | ``` func subdataWithRange(_ range: NSRange) -> NSData ``` |

Modified NSData.writeToFile(String, atomically: Bool) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToFile(_ path: String!, atomically useAuxiliaryFile: Bool) -> Bool ``` |
| To | ``` func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool ``` |

Modified NSData.writeToFile(String, options: NSDataWritingOptions, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToFile(_ path: String!, options writeOptionsMask: NSDataWritingOptions, error errorPtr: NSErrorPointer) -> Bool ``` |
| To | ``` func writeToFile(_ path: String, options writeOptionsMask: NSDataWritingOptions, error errorPtr: NSErrorPointer) -> Bool ``` |

Modified NSData.writeToURL(NSURL, atomically: Bool) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ url: NSURL!, atomically atomically: Bool) -> Bool ``` |
| To | ``` func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool ``` |

Modified NSData.writeToURL(NSURL, options: NSDataWritingOptions, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ url: NSURL!, options writeOptionsMask: NSDataWritingOptions, error errorPtr: NSErrorPointer) -> Bool ``` |
| To | ``` func writeToURL(_ url: NSURL, options writeOptionsMask: NSDataWritingOptions, error errorPtr: NSErrorPointer) -> Bool ``` |

Modified NSDataBase64DecodingOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct NSDataBase64DecodingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var IgnoreUnknownCharacters: NSDataBase64DecodingOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct NSDataBase64DecodingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var IgnoreUnknownCharacters: NSDataBase64DecodingOptions { get } } ``` | RawOptionSetType | OS X 10.9 |

Modified NSDataBase64DecodingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSDataBase64EncodingOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct NSDataBase64EncodingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Encoding64CharacterLineLength: NSDataBase64EncodingOptions { get }     static var Encoding76CharacterLineLength: NSDataBase64EncodingOptions { get }     static var EncodingEndLineWithCarriageReturn: NSDataBase64EncodingOptions { get }     static var EncodingEndLineWithLineFeed: NSDataBase64EncodingOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct NSDataBase64EncodingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Encoding64CharacterLineLength: NSDataBase64EncodingOptions { get }     static var Encoding76CharacterLineLength: NSDataBase64EncodingOptions { get }     static var EncodingEndLineWithCarriageReturn: NSDataBase64EncodingOptions { get }     static var EncodingEndLineWithLineFeed: NSDataBase64EncodingOptions { get } } ``` | RawOptionSetType | OS X 10.9 |

Modified NSDataBase64EncodingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSDataDetector

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSDataDetector.init(types: NSTextCheckingTypes, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(types checkingTypes: NSTextCheckingTypes, error error: NSErrorPointer) ``` |
| To | ``` init?(types checkingTypes: NSTextCheckingTypes, error error: NSErrorPointer) ``` |

Modified NSDataReadingOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSDataReadingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var DataReadingMappedIfSafe: NSDataReadingOptions { get }     static var DataReadingUncached: NSDataReadingOptions { get }     static var DataReadingMappedAlways: NSDataReadingOptions { get }     static var DataReadingMapped: NSDataReadingOptions { get }     static var MappedRead: NSDataReadingOptions { get }     static var UncachedRead: NSDataReadingOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSDataReadingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var DataReadingMappedIfSafe: NSDataReadingOptions { get }     static var DataReadingUncached: NSDataReadingOptions { get }     static var DataReadingMappedAlways: NSDataReadingOptions { get }     static var DataReadingMapped: NSDataReadingOptions { get }     static var MappedRead: NSDataReadingOptions { get }     static var UncachedRead: NSDataReadingOptions { get } } ``` | RawOptionSetType |

Modified NSDataReadingOptions.DataReadingMappedAlways

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSDataReadingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSDataSearchOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct NSDataSearchOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Backwards: NSDataSearchOptions { get }     static var Anchored: NSDataSearchOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct NSDataSearchOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Backwards: NSDataSearchOptions { get }     static var Anchored: NSDataSearchOptions { get } } ``` | RawOptionSetType | OS X 10.6 |

Modified NSDataSearchOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSDataWritingOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSDataWritingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var DataWritingAtomic: NSDataWritingOptions { get }     static var DataWritingWithoutOverwriting: NSDataWritingOptions { get }     static var DataWritingFileProtectionNone: NSDataWritingOptions { get }     static var DataWritingFileProtectionComplete: NSDataWritingOptions { get }     static var DataWritingFileProtectionCompleteUnlessOpen: NSDataWritingOptions { get }     static var DataWritingFileProtectionCompleteUntilFirstUserAuthentication: NSDataWritingOptions { get }     static var DataWritingFileProtectionMask: NSDataWritingOptions { get }     static var AtomicWrite: NSDataWritingOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSDataWritingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var DataWritingAtomic: NSDataWritingOptions { get }     static var DataWritingWithoutOverwriting: NSDataWritingOptions { get }     static var DataWritingFileProtectionNone: NSDataWritingOptions { get }     static var DataWritingFileProtectionComplete: NSDataWritingOptions { get }     static var DataWritingFileProtectionCompleteUnlessOpen: NSDataWritingOptions { get }     static var DataWritingFileProtectionCompleteUntilFirstUserAuthentication: NSDataWritingOptions { get }     static var DataWritingFileProtectionMask: NSDataWritingOptions { get }     static var AtomicWrite: NSDataWritingOptions { get } } ``` | RawOptionSetType |

Modified NSDataWritingOptions.DataWritingWithoutOverwriting

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSDataWritingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSDate

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSSecureCoding, Reflectable |
| To | AnyObject, CKRecordValue, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding, Reflectable |

Modified NSDate.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init(coder aDecoder: NSCoder) ``` |

Modified NSDate.compare(NSDate) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func compare(_ other: NSDate!) -> NSComparisonResult ``` |
| To | ``` func compare(_ other: NSDate) -> NSComparisonResult ``` |

Modified NSDate.dateByAddingTimeInterval(NSTimeInterval) -> Self

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func dateByAddingTimeInterval(_ ti: NSTimeInterval) -> Self! ``` | OS X 10.10 |
| To | ``` func dateByAddingTimeInterval(_ ti: NSTimeInterval) -> Self ``` | OS X 10.6 |

Modified NSDate.dateWithCalendarFormat(String?, timeZone: NSTimeZone?) -> NSCalendarDate

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func dateWithCalendarFormat(_ format: String!, timeZone aTimeZone: NSTimeZone!) -> NSCalendarDate! ``` | OS X 10.10 | -- |
| To | ``` func dateWithCalendarFormat(_ format: String?, timeZone aTimeZone: NSTimeZone?) -> NSCalendarDate ``` | OS X 10.4 | OS X 10.10 |

Modified NSDate.dateWithNaturalLanguageString(String) -> AnyObject? [class]

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` class func dateWithNaturalLanguageString(_ string: String!) -> AnyObject! ``` | OS X 10.10 | -- |
| To | ``` class func dateWithNaturalLanguageString(_ string: String) -> AnyObject? ``` | OS X 10.4 | OS X 10.10 |

Modified NSDate.dateWithNaturalLanguageString(String, locale: AnyObject?) -> AnyObject? [class]

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` class func dateWithNaturalLanguageString(_ string: String!, locale locale: AnyObject!) -> AnyObject! ``` | OS X 10.10 | -- |
| To | ``` class func dateWithNaturalLanguageString(_ string: String, locale locale: AnyObject?) -> AnyObject? ``` | OS X 10.4 | OS X 10.10 |

Modified NSDate.dateWithString(String) -> AnyObject [class]

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` class func dateWithString(_ aString: String!) -> AnyObject! ``` | OS X 10.10 | -- |
| To | ``` class func dateWithString(_ aString: String) -> AnyObject ``` | OS X 10.4 | OS X 10.10 |

Modified NSDate.description

|  | Declaration |
| --- | --- |
| From | ``` var description: String! { get } ``` |
| To | ``` var description: String { get } ``` |

Modified NSDate.descriptionWithCalendarFormat(String?, timeZone: NSTimeZone?, locale: AnyObject?) -> String?

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func descriptionWithCalendarFormat(_ format: String!, timeZone aTimeZone: NSTimeZone!, locale locale: AnyObject!) -> String! ``` | OS X 10.10 | -- |
| To | ``` func descriptionWithCalendarFormat(_ format: String?, timeZone aTimeZone: NSTimeZone?, locale locale: AnyObject?) -> String? ``` | OS X 10.4 | OS X 10.10 |

Modified NSDate.descriptionWithLocale(AnyObject?) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func descriptionWithLocale(_ locale: AnyObject!) -> String! ``` |
| To | ``` func descriptionWithLocale(_ locale: AnyObject?) -> String? ``` |

Modified NSDate.distantFuture() -> AnyObject [class]

|  | Declaration |
| --- | --- |
| From | ``` class func distantFuture() -> AnyObject! ``` |
| To | ``` class func distantFuture() -> AnyObject ``` |

Modified NSDate.distantPast() -> AnyObject [class]

|  | Declaration |
| --- | --- |
| From | ``` class func distantPast() -> AnyObject! ``` |
| To | ``` class func distantPast() -> AnyObject ``` |

Modified NSDate.earlierDate(NSDate) -> NSDate

|  | Declaration |
| --- | --- |
| From | ``` func earlierDate(_ anotherDate: NSDate!) -> NSDate! ``` |
| To | ``` func earlierDate(_ anotherDate: NSDate) -> NSDate ``` |

Modified NSDate.isEqualToDate(NSDate) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToDate(_ otherDate: NSDate!) -> Bool ``` |
| To | ``` func isEqualToDate(_ otherDate: NSDate) -> Bool ``` |

Modified NSDate.laterDate(NSDate) -> NSDate

|  | Declaration |
| --- | --- |
| From | ``` func laterDate(_ anotherDate: NSDate!) -> NSDate! ``` |
| To | ``` func laterDate(_ anotherDate: NSDate) -> NSDate ``` |

Modified NSDate.init(string: String)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` convenience init(string description: String!) ``` | OS X 10.10 | -- |
| To | ``` convenience init?(string description: String) ``` | OS X 10.4 | OS X 10.10 |

Modified NSDate.timeIntervalSinceDate(NSDate) -> NSTimeInterval

|  | Declaration |
| --- | --- |
| From | ``` func timeIntervalSinceDate(_ anotherDate: NSDate!) -> NSTimeInterval ``` |
| To | ``` func timeIntervalSinceDate(_ anotherDate: NSDate) -> NSTimeInterval ``` |

Modified NSDateComponents.calendar

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var calendar: NSCalendar! ``` | OS X 10.10 |
| To | ``` @NSCopying var calendar: NSCalendar? ``` | OS X 10.7 |

Modified NSDateComponents.date

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var date: NSDate! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var date: NSDate? { get } ``` | OS X 10.7 |

Modified NSDateComponents.isValidDateInCalendar(NSCalendar) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isValidDateInCalendar(_ calendar: NSCalendar!) -> Bool ``` | OS X 10.10 |
| To | ``` func isValidDateInCalendar(_ calendar: NSCalendar) -> Bool ``` | OS X 10.9 |

Modified NSDateComponents.leapMonth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSDateComponents.nanosecond

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSDateComponents.quarter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSDateComponents.setValue(Int, forComponent: NSCalendarUnit)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSDateComponents.timeZone

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var timeZone: NSTimeZone! ``` | OS X 10.10 |
| To | ``` @NSCopying var timeZone: NSTimeZone? ``` | OS X 10.7 |

Modified NSDateComponents.validDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSDateComponents.valueForComponent(NSCalendarUnit) -> Int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSDateComponents.weekOfMonth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSDateComponents.weekOfYear

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSDateComponents.yearForWeekOfYear

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSDateComponentsFormatter.calendar

|  | Declaration |
| --- | --- |
| From | ``` var calendar: NSCalendar! ``` |
| To | ``` @NSCopying var calendar: NSCalendar? ``` |

Modified NSDateComponentsFormatter.getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forString: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getObjectValue(_ obj: AutoreleasingUnsafePointer<AnyObject?>, forString string: String!, errorDescription error: AutoreleasingUnsafePointer<NSString?>) -> Bool ``` |
| To | ``` func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool ``` |

Modified NSDateComponentsFormatter.localizedStringFromDateComponents(NSDateComponents, unitsStyle: NSDateComponentsFormatterUnitsStyle) -> String? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func localizedStringFromDateComponents(_ components: NSDateComponents!, unitsStyle unitsStyle: NSDateComponentsFormatterUnitsStyle) -> String! ``` |
| To | ``` class func localizedStringFromDateComponents(_ components: NSDateComponents, unitsStyle unitsStyle: NSDateComponentsFormatterUnitsStyle) -> String? ``` |

Modified NSDateComponentsFormatter.stringForObjectValue(AnyObject) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func stringForObjectValue(_ obj: AnyObject!) -> String! ``` |
| To | ``` func stringForObjectValue(_ obj: AnyObject) -> String? ``` |

Modified NSDateComponentsFormatter.stringFromDate(NSDate, toDate: NSDate) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func stringFromDate(_ startDate: NSDate!, toDate endDate: NSDate!) -> String! ``` |
| To | ``` func stringFromDate(_ startDate: NSDate, toDate endDate: NSDate) -> String? ``` |

Modified NSDateComponentsFormatter.stringFromDateComponents(NSDateComponents) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func stringFromDateComponents(_ components: NSDateComponents!) -> String! ``` |
| To | ``` func stringFromDateComponents(_ components: NSDateComponents) -> String? ``` |

Modified NSDateComponentsFormatter.stringFromTimeInterval(NSTimeInterval) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func stringFromTimeInterval(_ ti: NSTimeInterval) -> String! ``` |
| To | ``` func stringFromTimeInterval(_ ti: NSTimeInterval) -> String? ``` |

Modified NSDateComponentsFormatterZeroFormattingBehavior [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSDateComponentsFormatterZeroFormattingBehavior : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var None: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var Default: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropLeading: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropMiddle: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropTrailing: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropAll: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var Pad: NSDateComponentsFormatterZeroFormattingBehavior { get } } ``` | RawOptionSet |
| To | ``` struct NSDateComponentsFormatterZeroFormattingBehavior : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var Default: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropLeading: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropMiddle: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropTrailing: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var DropAll: NSDateComponentsFormatterZeroFormattingBehavior { get }     static var Pad: NSDateComponentsFormatterZeroFormattingBehavior { get } } ``` | RawOptionSetType |

Modified NSDateComponentsFormatterZeroFormattingBehavior.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSDateFormatter.calendar

|  | Declaration |
| --- | --- |
| From | ``` var calendar: NSCalendar! ``` |
| To | ``` @NSCopying var calendar: NSCalendar! ``` |

Modified NSDateFormatter.dateFormatFromTemplate(String, options: Int, locale: NSLocale) -> String? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func dateFormatFromTemplate(_ tmplate: String!, options opts: Int, locale locale: NSLocale!) -> String! ``` | OS X 10.10 |
| To | ``` class func dateFormatFromTemplate(_ tmplate: String, options opts: Int, locale locale: NSLocale) -> String? ``` | OS X 10.6 |

Modified NSDateFormatter.dateFromString(String) -> NSDate?

|  | Declaration |
| --- | --- |
| From | ``` func dateFromString(_ string: String!) -> NSDate! ``` |
| To | ``` func dateFromString(_ string: String) -> NSDate? ``` |

Modified NSDateFormatter.defaultDate

|  | Declaration |
| --- | --- |
| From | ``` var defaultDate: NSDate! ``` |
| To | ``` @NSCopying var defaultDate: NSDate? ``` |

Modified NSDateFormatter.doesRelativeDateFormatting

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSDateFormatter.getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forString: String, range: UnsafeMutablePointer<NSRange>, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getObjectValue(_ obj: AutoreleasingUnsafePointer<AnyObject?>, forString string: String!, range rangep: UnsafePointer<NSRange>, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, range rangep: UnsafeMutablePointer<NSRange>, error error: NSErrorPointer) -> Bool ``` |

Modified NSDateFormatter.gregorianStartDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var gregorianStartDate: NSDate! ``` | OS X 10.10 |
| To | ``` @NSCopying var gregorianStartDate: NSDate! ``` | OS X 10.5 |

Modified NSDateFormatter.locale

|  | Declaration |
| --- | --- |
| From | ``` var locale: NSLocale! ``` |
| To | ``` @NSCopying var locale: NSLocale! ``` |

Modified NSDateFormatter.localizedStringFromDate(NSDate, dateStyle: NSDateFormatterStyle, timeStyle: NSDateFormatterStyle) -> String [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func localizedStringFromDate(_ date: NSDate!, dateStyle dstyle: NSDateFormatterStyle, timeStyle tstyle: NSDateFormatterStyle) -> String! ``` | OS X 10.10 |
| To | ``` class func localizedStringFromDate(_ date: NSDate, dateStyle dstyle: NSDateFormatterStyle, timeStyle tstyle: NSDateFormatterStyle) -> String ``` | OS X 10.6 |

Modified NSDateFormatter.longEraSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSDateFormatter.quarterSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSDateFormatter.setLocalizedDateFormatFromTemplate(String)

|  | Declaration |
| --- | --- |
| From | ``` func setLocalizedDateFormatFromTemplate(_ dateFormatTemplate: String!) ``` |
| To | ``` func setLocalizedDateFormatFromTemplate(_ dateFormatTemplate: String) ``` |

Modified NSDateFormatter.shortQuarterSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSDateFormatter.shortStandaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSDateFormatter.shortStandaloneQuarterSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSDateFormatter.shortStandaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSDateFormatter.standaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSDateFormatter.standaloneQuarterSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSDateFormatter.standaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSDateFormatter.stringFromDate(NSDate) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringFromDate(_ date: NSDate!) -> String! ``` |
| To | ``` func stringFromDate(_ date: NSDate) -> String ``` |

Modified NSDateFormatter.timeZone

|  | Declaration |
| --- | --- |
| From | ``` var timeZone: NSTimeZone! ``` |
| To | ``` @NSCopying var timeZone: NSTimeZone! ``` |

Modified NSDateFormatter.twoDigitStartDate

|  | Declaration |
| --- | --- |
| From | ``` var twoDigitStartDate: NSDate! ``` |
| To | ``` @NSCopying var twoDigitStartDate: NSDate! ``` |

Modified NSDateFormatter.veryShortMonthSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSDateFormatter.veryShortStandaloneMonthSymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSDateFormatter.veryShortStandaloneWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSDateFormatter.veryShortWeekdaySymbols

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSDateIntervalFormatter.calendar

|  | Declaration |
| --- | --- |
| From | ``` var calendar: NSCalendar! ``` |
| To | ``` @NSCopying var calendar: NSCalendar? ``` |

Modified NSDateIntervalFormatter.dateTemplate

|  | Declaration |
| --- | --- |
| From | ``` var dateTemplate: String! ``` |
| To | ``` var dateTemplate: String? ``` |

Modified NSDateIntervalFormatter.locale

|  | Declaration |
| --- | --- |
| From | ``` var locale: NSLocale! ``` |
| To | ``` @NSCopying var locale: NSLocale? ``` |

Modified NSDateIntervalFormatter.stringFromDate(NSDate, toDate: NSDate) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringFromDate(_ fromDate: NSDate!, toDate toDate: NSDate!) -> String! ``` |
| To | ``` func stringFromDate(_ fromDate: NSDate, toDate toDate: NSDate) -> String ``` |

Modified NSDateIntervalFormatter.timeZone

|  | Declaration |
| --- | --- |
| From | ``` var timeZone: NSTimeZone! ``` |
| To | ``` @NSCopying var timeZone: NSTimeZone? ``` |

Modified NSDecimalNumber.compare(NSNumber) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func compare(_ decimalNumber: NSNumber!) -> NSComparisonResult ``` |
| To | ``` func compare(_ decimalNumber: NSNumber) -> NSComparisonResult ``` |

Modified NSDecimalNumber.decimalNumberByAdding(NSDecimalNumber) -> NSDecimalNumber

|  | Declaration |
| --- | --- |
| From | ``` func decimalNumberByAdding(_ decimalNumber: NSDecimalNumber!) -> NSDecimalNumber! ``` |
| To | ``` func decimalNumberByAdding(_ decimalNumber: NSDecimalNumber) -> NSDecimalNumber ``` |

Modified NSDecimalNumber.decimalNumberByAdding(NSDecimalNumber, withBehavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber

|  | Declaration |
| --- | --- |
| From | ``` func decimalNumberByAdding(_ decimalNumber: NSDecimalNumber!, withBehavior behavior: NSDecimalNumberBehaviors!) -> NSDecimalNumber! ``` |
| To | ``` func decimalNumberByAdding(_ decimalNumber: NSDecimalNumber, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber ``` |

Modified NSDecimalNumber.decimalNumberByDividingBy(NSDecimalNumber) -> NSDecimalNumber

|  | Declaration |
| --- | --- |
| From | ``` func decimalNumberByDividingBy(_ decimalNumber: NSDecimalNumber!) -> NSDecimalNumber! ``` |
| To | ``` func decimalNumberByDividingBy(_ decimalNumber: NSDecimalNumber) -> NSDecimalNumber ``` |

Modified NSDecimalNumber.decimalNumberByDividingBy(NSDecimalNumber, withBehavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber

|  | Declaration |
| --- | --- |
| From | ``` func decimalNumberByDividingBy(_ decimalNumber: NSDecimalNumber!, withBehavior behavior: NSDecimalNumberBehaviors!) -> NSDecimalNumber! ``` |
| To | ``` func decimalNumberByDividingBy(_ decimalNumber: NSDecimalNumber, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber ``` |

Modified NSDecimalNumber.decimalNumberByMultiplyingBy(NSDecimalNumber) -> NSDecimalNumber

|  | Declaration |
| --- | --- |
| From | ``` func decimalNumberByMultiplyingBy(_ decimalNumber: NSDecimalNumber!) -> NSDecimalNumber! ``` |
| To | ``` func decimalNumberByMultiplyingBy(_ decimalNumber: NSDecimalNumber) -> NSDecimalNumber ``` |

Modified NSDecimalNumber.decimalNumberByMultiplyingBy(NSDecimalNumber, withBehavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber

|  | Declaration |
| --- | --- |
| From | ``` func decimalNumberByMultiplyingBy(_ decimalNumber: NSDecimalNumber!, withBehavior behavior: NSDecimalNumberBehaviors!) -> NSDecimalNumber! ``` |
| To | ``` func decimalNumberByMultiplyingBy(_ decimalNumber: NSDecimalNumber, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber ``` |

Modified NSDecimalNumber.decimalNumberByMultiplyingByPowerOf10(Int16) -> NSDecimalNumber

|  | Declaration |
| --- | --- |
| From | ``` func decimalNumberByMultiplyingByPowerOf10(_ power: Int16) -> NSDecimalNumber! ``` |
| To | ``` func decimalNumberByMultiplyingByPowerOf10(_ power: Int16) -> NSDecimalNumber ``` |

Modified NSDecimalNumber.decimalNumberByMultiplyingByPowerOf10(Int16, withBehavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber

|  | Declaration |
| --- | --- |
| From | ``` func decimalNumberByMultiplyingByPowerOf10(_ power: Int16, withBehavior behavior: NSDecimalNumberBehaviors!) -> NSDecimalNumber! ``` |
| To | ``` func decimalNumberByMultiplyingByPowerOf10(_ power: Int16, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber ``` |

Modified NSDecimalNumber.decimalNumberByRaisingToPower(Int) -> NSDecimalNumber

|  | Declaration |
| --- | --- |
| From | ``` func decimalNumberByRaisingToPower(_ power: Int) -> NSDecimalNumber! ``` |
| To | ``` func decimalNumberByRaisingToPower(_ power: Int) -> NSDecimalNumber ``` |

Modified NSDecimalNumber.decimalNumberByRaisingToPower(Int, withBehavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber

|  | Declaration |
| --- | --- |
| From | ``` func decimalNumberByRaisingToPower(_ power: Int, withBehavior behavior: NSDecimalNumberBehaviors!) -> NSDecimalNumber! ``` |
| To | ``` func decimalNumberByRaisingToPower(_ power: Int, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber ``` |

Modified NSDecimalNumber.decimalNumberByRoundingAccordingToBehavior(NSDecimalNumberBehaviors?) -> NSDecimalNumber

|  | Declaration |
| --- | --- |
| From | ``` func decimalNumberByRoundingAccordingToBehavior(_ behavior: NSDecimalNumberBehaviors!) -> NSDecimalNumber! ``` |
| To | ``` func decimalNumberByRoundingAccordingToBehavior(_ behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber ``` |

Modified NSDecimalNumber.decimalNumberBySubtracting(NSDecimalNumber) -> NSDecimalNumber

|  | Declaration |
| --- | --- |
| From | ``` func decimalNumberBySubtracting(_ decimalNumber: NSDecimalNumber!) -> NSDecimalNumber! ``` |
| To | ``` func decimalNumberBySubtracting(_ decimalNumber: NSDecimalNumber) -> NSDecimalNumber ``` |

Modified NSDecimalNumber.decimalNumberBySubtracting(NSDecimalNumber, withBehavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber

|  | Declaration |
| --- | --- |
| From | ``` func decimalNumberBySubtracting(_ decimalNumber: NSDecimalNumber!, withBehavior behavior: NSDecimalNumberBehaviors!) -> NSDecimalNumber! ``` |
| To | ``` func decimalNumberBySubtracting(_ decimalNumber: NSDecimalNumber, withBehavior behavior: NSDecimalNumberBehaviors?) -> NSDecimalNumber ``` |

Modified NSDecimalNumber.defaultBehavior() -> NSDecimalNumberBehaviors [class]

|  | Declaration |
| --- | --- |
| From | ``` class func defaultBehavior() -> NSDecimalNumberBehaviors! ``` |
| To | ``` class func defaultBehavior() -> NSDecimalNumberBehaviors ``` |

Modified NSDecimalNumber.descriptionWithLocale(AnyObject?) -> String

|  | Declaration |
| --- | --- |
| From | ``` func descriptionWithLocale(_ locale: AnyObject!) -> String! ``` |
| To | ``` func descriptionWithLocale(_ locale: AnyObject?) -> String ``` |

Modified NSDecimalNumber.maximumDecimalNumber() -> NSDecimalNumber [class]

|  | Declaration |
| --- | --- |
| From | ``` class func maximumDecimalNumber() -> NSDecimalNumber! ``` |
| To | ``` class func maximumDecimalNumber() -> NSDecimalNumber ``` |

Modified NSDecimalNumber.minimumDecimalNumber() -> NSDecimalNumber [class]

|  | Declaration |
| --- | --- |
| From | ``` class func minimumDecimalNumber() -> NSDecimalNumber! ``` |
| To | ``` class func minimumDecimalNumber() -> NSDecimalNumber ``` |

Modified NSDecimalNumber.notANumber() -> NSDecimalNumber [class]

|  | Declaration |
| --- | --- |
| From | ``` class func notANumber() -> NSDecimalNumber! ``` |
| To | ``` class func notANumber() -> NSDecimalNumber ``` |

Modified NSDecimalNumber.objCType

|  | Declaration |
| --- | --- |
| From | ``` var objCType: ConstUnsafePointer<Int8> { get } ``` |
| To | ``` var objCType: UnsafePointer<Int8> { get } ``` |

Modified NSDecimalNumber.one() -> NSDecimalNumber [class]

|  | Declaration |
| --- | --- |
| From | ``` class func one() -> NSDecimalNumber! ``` |
| To | ``` class func one() -> NSDecimalNumber ``` |

Modified NSDecimalNumber.setDefaultBehavior(NSDecimalNumberBehaviors) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setDefaultBehavior(_ behavior: NSDecimalNumberBehaviors!) ``` |
| To | ``` class func setDefaultBehavior(_ behavior: NSDecimalNumberBehaviors) ``` |

Modified NSDecimalNumber.init(string: String?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(string numberValue: String!) ``` |
| To | ``` convenience init(string numberValue: String?) ``` |

Modified NSDecimalNumber.init(string: String?, locale: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(string numberValue: String!, locale locale: AnyObject!) ``` |
| To | ``` convenience init(string numberValue: String?, locale locale: AnyObject?) ``` |

Modified NSDecimalNumber.zero() -> NSDecimalNumber [class]

|  | Declaration |
| --- | --- |
| From | ``` class func zero() -> NSDecimalNumber! ``` |
| To | ``` class func zero() -> NSDecimalNumber ``` |

Modified NSDecimalNumberBehaviors.exceptionDuringOperation(Selector, error: NSCalculationError, leftOperand: NSDecimalNumber, rightOperand: NSDecimalNumber) -> NSDecimalNumber?

|  | Declaration |
| --- | --- |
| From | ``` func exceptionDuringOperation(_ operation: Selector, error error: NSCalculationError, leftOperand leftOperand: NSDecimalNumber!, rightOperand rightOperand: NSDecimalNumber!) -> NSDecimalNumber! ``` |
| To | ``` func exceptionDuringOperation(_ operation: Selector, error error: NSCalculationError, leftOperand leftOperand: NSDecimalNumber, rightOperand rightOperand: NSDecimalNumber) -> NSDecimalNumber? ``` |

Modified NSDecimalNumberHandler.defaultDecimalNumberHandler() -> NSDecimalNumberHandler [class]

|  | Declaration |
| --- | --- |
| From | ``` class func defaultDecimalNumberHandler() -> NSDecimalNumberHandler! ``` |
| To | ``` class func defaultDecimalNumberHandler() -> NSDecimalNumberHandler ``` |

Modified NSDeleteCommand.setReceiversSpecifier(NSScriptObjectSpecifier)

|  | Declaration |
| --- | --- |
| From | ``` func setReceiversSpecifier(_ receiversRef: NSScriptObjectSpecifier!) ``` |
| To | ``` func setReceiversSpecifier(_ receiversRef: NSScriptObjectSpecifier) ``` |

Modified NSDictionary

|  | Protocols |
| --- | --- |
| From | AnyObject, DictionaryLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, Reflectable, Sequence |
| To | AnyObject, DictionaryLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, Reflectable, SequenceType |

Modified NSDictionary.allKeys

|  | Declaration |
| --- | --- |
| From | ``` var allKeys: [AnyObject]! { get } ``` |
| To | ``` var allKeys: [AnyObject] { get } ``` |

Modified NSDictionary.allKeysForObject(AnyObject) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func allKeysForObject(_ anObject: AnyObject!) -> [AnyObject]! ``` |
| To | ``` func allKeysForObject(_ anObject: AnyObject) -> [AnyObject] ``` |

Modified NSDictionary.allValues

|  | Declaration |
| --- | --- |
| From | ``` var allValues: [AnyObject]! { get } ``` |
| To | ``` var allValues: [AnyObject] { get } ``` |

Modified NSDictionary.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init(coder aDecoder: NSCoder) ``` |

Modified NSDictionary.description

|  | Declaration |
| --- | --- |
| From | ``` var description: String! { get } ``` |
| To | ``` var description: String { get } ``` |

Modified NSDictionary.descriptionInStringsFileFormat

|  | Declaration |
| --- | --- |
| From | ``` var descriptionInStringsFileFormat: String! { get } ``` |
| To | ``` var descriptionInStringsFileFormat: String { get } ``` |

Modified NSDictionary.descriptionWithLocale(AnyObject?) -> String

|  | Declaration |
| --- | --- |
| From | ``` func descriptionWithLocale(_ locale: AnyObject!) -> String! ``` |
| To | ``` func descriptionWithLocale(_ locale: AnyObject?) -> String ``` |

Modified NSDictionary.descriptionWithLocale(AnyObject?, indent: Int) -> String

|  | Declaration |
| --- | --- |
| From | ``` func descriptionWithLocale(_ locale: AnyObject!, indent level: Int) -> String! ``` |
| To | ``` func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String ``` |

Modified NSDictionary.init(dictionary: [NSObject: AnyObject], copyItems: Bool)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(dictionary otherDictionary: [NSObject : AnyObject]!, copyItems flag: Bool) ``` |
| To | ``` convenience init(dictionary otherDictionary: [NSObject : AnyObject], copyItems flag: Bool) ``` |

Modified NSDictionary.enumerateKeysAndObjectsUsingBlock((AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateKeysAndObjectsUsingBlock(_ block: ((AnyObject!, AnyObject!, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateKeysAndObjectsUsingBlock(_ block: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.6 |

Modified NSDictionary.enumerateKeysAndObjectsWithOptions(NSEnumerationOptions, usingBlock:(AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateKeysAndObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: ((AnyObject!, AnyObject!, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateKeysAndObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.6 |

Modified NSDictionary.fileCreationDate() -> NSDate?

|  | Declaration |
| --- | --- |
| From | ``` func fileCreationDate() -> NSDate! ``` |
| To | ``` func fileCreationDate() -> NSDate? ``` |

Modified NSDictionary.fileGroupOwnerAccountID() -> NSNumber?

|  | Declaration |
| --- | --- |
| From | ``` func fileGroupOwnerAccountID() -> NSNumber! ``` |
| To | ``` func fileGroupOwnerAccountID() -> NSNumber? ``` |

Modified NSDictionary.fileGroupOwnerAccountName() -> String?

|  | Declaration |
| --- | --- |
| From | ``` func fileGroupOwnerAccountName() -> String! ``` |
| To | ``` func fileGroupOwnerAccountName() -> String? ``` |

Modified NSDictionary.fileModificationDate() -> NSDate?

|  | Declaration |
| --- | --- |
| From | ``` func fileModificationDate() -> NSDate! ``` |
| To | ``` func fileModificationDate() -> NSDate? ``` |

Modified NSDictionary.fileOwnerAccountID() -> NSNumber?

|  | Declaration |
| --- | --- |
| From | ``` func fileOwnerAccountID() -> NSNumber! ``` |
| To | ``` func fileOwnerAccountID() -> NSNumber? ``` |

Modified NSDictionary.fileOwnerAccountName() -> String?

|  | Declaration |
| --- | --- |
| From | ``` func fileOwnerAccountName() -> String! ``` |
| To | ``` func fileOwnerAccountName() -> String? ``` |

Modified NSDictionary.fileType() -> String?

|  | Declaration |
| --- | --- |
| From | ``` func fileType() -> String! ``` |
| To | ``` func fileType() -> String? ``` |

Modified NSDictionary.getObjects(AutoreleasingUnsafeMutablePointer<AnyObject?>, andKeys: AutoreleasingUnsafeMutablePointer<AnyObject?>)

|  | Declaration |
| --- | --- |
| From | ``` func getObjects(_ objects: AutoreleasingUnsafePointer<AnyObject?>, andKeys keys: AutoreleasingUnsafePointer<AnyObject?>) ``` |
| To | ``` func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, andKeys keys: AutoreleasingUnsafeMutablePointer<AnyObject?>) ``` |

Modified NSDictionary.isEqualToDictionary([NSObject: AnyObject]) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToDictionary(_ otherDictionary: [NSObject : AnyObject]!) -> Bool ``` |
| To | ``` func isEqualToDictionary(_ otherDictionary: [NSObject : AnyObject]) -> Bool ``` |

Modified NSDictionary.keyEnumerator() -> NSEnumerator

|  | Declaration |
| --- | --- |
| From | ``` func keyEnumerator() -> NSEnumerator! ``` |
| To | ``` func keyEnumerator() -> NSEnumerator ``` |

Modified NSDictionary.keysOfEntriesPassingTest((AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func keysOfEntriesPassingTest(_ predicate: ((AnyObject!, AnyObject!, UnsafePointer<ObjCBool>) -> Bool)!) -> NSSet! ``` | OS X 10.10 |
| To | ``` func keysOfEntriesPassingTest(_ predicate: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` | OS X 10.6 |

Modified NSDictionary.keysOfEntriesWithOptions(NSEnumerationOptions, passingTest:(AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func keysOfEntriesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: ((AnyObject!, AnyObject!, UnsafePointer<ObjCBool>) -> Bool)!) -> NSSet! ``` | OS X 10.10 |
| To | ``` func keysOfEntriesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` | OS X 10.6 |

Modified NSDictionary.keysSortedByValueUsingComparator(NSComparator) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func keysSortedByValueUsingComparator(_ cmptr: NSComparator!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func keysSortedByValueUsingComparator(_ cmptr: NSComparator) -> [AnyObject] ``` | OS X 10.6 |

Modified NSDictionary.keysSortedByValueUsingSelector(Selector) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func keysSortedByValueUsingSelector(_ comparator: Selector) -> [AnyObject]! ``` |
| To | ``` func keysSortedByValueUsingSelector(_ comparator: Selector) -> [AnyObject] ``` |

Modified NSDictionary.keysSortedByValueWithOptions(NSSortOptions, usingComparator: NSComparator) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func keysSortedByValueWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func keysSortedByValueWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject] ``` | OS X 10.6 |

Modified NSDictionary.init(object: AnyObject, forKey: NSCopying)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(object object: AnyObject!, forKey key: NSCopying!) ``` |
| To | ``` convenience init(object object: AnyObject, forKey key: NSCopying) ``` |

Modified NSDictionary.objectEnumerator() -> NSEnumerator

|  | Declaration |
| --- | --- |
| From | ``` func objectEnumerator() -> NSEnumerator! ``` |
| To | ``` func objectEnumerator() -> NSEnumerator ``` |

Modified NSDictionary.objectForKey(AnyObject) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func objectForKey(_ aKey: AnyObject!) -> AnyObject! ``` |
| To | ``` func objectForKey(_ aKey: AnyObject) -> AnyObject? ``` |

Modified NSDictionary.init(objects: UnsafePointer<AnyObject?>, forKeys: UnsafePointer<NSCopying?>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(objects objects: ConstUnsafePointer<AnyObject?>, forKeys keys: ConstUnsafePointer<NSCopying?>, count cnt: Int) ``` |
| To | ``` init(objects objects: UnsafePointer<AnyObject?>, forKeys keys: UnsafePointer<NSCopying?>, count cnt: Int) ``` |

Modified NSDictionary.objectsForKeys([AnyObject], notFoundMarker: AnyObject) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func objectsForKeys(_ keys: [AnyObject]!, notFoundMarker marker: AnyObject!) -> [AnyObject]! ``` |
| To | ``` func objectsForKeys(_ keys: [AnyObject], notFoundMarker marker: AnyObject) -> [AnyObject] ``` |

Modified NSDictionary.sharedKeySetForKeys([AnyObject]) -> AnyObject [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func sharedKeySetForKeys(_ keys: [AnyObject]!) -> AnyObject! ``` | OS X 10.10 |
| To | ``` class func sharedKeySetForKeys(_ keys: [AnyObject]) -> AnyObject ``` | OS X 10.8 |

Modified NSDictionary.valueForKey(String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func valueForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` func valueForKey(_ key: String) -> AnyObject? ``` |

Modified NSDictionary.writeToFile(String, atomically: Bool) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToFile(_ path: String!, atomically useAuxiliaryFile: Bool) -> Bool ``` |
| To | ``` func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool) -> Bool ``` |

Modified NSDictionary.writeToURL(NSURL, atomically: Bool) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ url: NSURL!, atomically atomically: Bool) -> Bool ``` |
| To | ``` func writeToURL(_ url: NSURL, atomically atomically: Bool) -> Bool ``` |

Modified NSDirectoryEnumerationOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct NSDirectoryEnumerationOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var SkipsSubdirectoryDescendants: NSDirectoryEnumerationOptions { get }     static var SkipsPackageDescendants: NSDirectoryEnumerationOptions { get }     static var SkipsHiddenFiles: NSDirectoryEnumerationOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct NSDirectoryEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var SkipsSubdirectoryDescendants: NSDirectoryEnumerationOptions { get }     static var SkipsPackageDescendants: NSDirectoryEnumerationOptions { get }     static var SkipsHiddenFiles: NSDirectoryEnumerationOptions { get } } ``` | RawOptionSetType | OS X 10.6 |

Modified NSDirectoryEnumerationOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSDirectoryEnumerator.directoryAttributes

|  | Declaration |
| --- | --- |
| From | ``` var directoryAttributes: [NSObject : AnyObject]! { get } ``` |
| To | ``` var directoryAttributes: [NSObject : AnyObject]? { get } ``` |

Modified NSDirectoryEnumerator.fileAttributes

|  | Declaration |
| --- | --- |
| From | ``` var fileAttributes: [NSObject : AnyObject]! { get } ``` |
| To | ``` var fileAttributes: [NSObject : AnyObject]? { get } ``` |

Modified NSDirectoryEnumerator.level

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSDirectoryEnumerator.skipDescendants()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSDistributedLock.lockDate

|  | Declaration |
| --- | --- |
| From | ``` var lockDate: NSDate! { get } ``` |
| To | ``` @NSCopying var lockDate: NSDate { get } ``` |

Modified NSDistributedNotificationCenter.addObserver(AnyObject, selector: Selector, name: String?, object: String?)

|  | Declaration |
| --- | --- |
| From | ``` func addObserver(_ observer: AnyObject!, selector aSelector: Selector, name aName: String!, object anObject: String!) ``` |
| To | ``` func addObserver(_ observer: AnyObject, selector aSelector: Selector, name aName: String?, object anObject: String?) ``` |

Modified NSDistributedNotificationCenter.addObserver(AnyObject, selector: Selector, name: String?, object: String?, suspensionBehavior: NSNotificationSuspensionBehavior)

|  | Declaration |
| --- | --- |
| From | ``` func addObserver(_ observer: AnyObject!, selector selector: Selector, name name: String!, object object: String!, suspensionBehavior suspensionBehavior: NSNotificationSuspensionBehavior) ``` |
| To | ``` func addObserver(_ observer: AnyObject, selector selector: Selector, name name: String?, object object: String?, suspensionBehavior suspensionBehavior: NSNotificationSuspensionBehavior) ``` |

Modified NSDistributedNotificationCenter.defaultCenter() -> NSDistributedNotificationCenter [class]

|  | Declaration |
| --- | --- |
| From | ``` class func defaultCenter() -> NSDistributedNotificationCenter! ``` |
| To | ``` class func defaultCenter() -> NSDistributedNotificationCenter ``` |

Modified NSDistributedNotificationCenter.notificationCenterForType(String) -> NSDistributedNotificationCenter [class]

|  | Declaration |
| --- | --- |
| From | ``` class func notificationCenterForType(_ notificationCenterType: String!) -> NSDistributedNotificationCenter! ``` |
| To | ``` class func notificationCenterForType(_ notificationCenterType: String) -> NSDistributedNotificationCenter ``` |

Modified NSDistributedNotificationCenter.postNotificationName(String, object: String?)

|  | Declaration |
| --- | --- |
| From | ``` func postNotificationName(_ aName: String!, object anObject: String!) ``` |
| To | ``` func postNotificationName(_ aName: String, object anObject: String?) ``` |

Modified NSDistributedNotificationCenter.postNotificationName(String, object: String?, userInfo:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` func postNotificationName(_ aName: String!, object anObject: String!, userInfo aUserInfo: [NSObject : AnyObject]!) ``` |
| To | ``` func postNotificationName(_ aName: String, object anObject: String?, userInfo aUserInfo: [NSObject : AnyObject]?) ``` |

Modified NSDistributedNotificationCenter.postNotificationName(String, object: String?, userInfo:[NSObject: AnyObject]?, deliverImmediately: Bool)

|  | Declaration |
| --- | --- |
| From | ``` func postNotificationName(_ name: String!, object object: String!, userInfo userInfo: [NSObject : AnyObject]!, deliverImmediately deliverImmediately: Bool) ``` |
| To | ``` func postNotificationName(_ name: String, object object: String?, userInfo userInfo: [NSObject : AnyObject]?, deliverImmediately deliverImmediately: Bool) ``` |

Modified NSDistributedNotificationCenter.postNotificationName(String, object: String?, userInfo:[NSObject: AnyObject]?, options: Int)

|  | Declaration |
| --- | --- |
| From | ``` func postNotificationName(_ name: String!, object object: String!, userInfo userInfo: [NSObject : AnyObject]!, options options: Int) ``` |
| To | ``` func postNotificationName(_ name: String, object object: String?, userInfo userInfo: [NSObject : AnyObject]?, options options: Int) ``` |

Modified NSDistributedNotificationCenter.removeObserver(AnyObject?, name: String?, object: String?)

|  | Declaration |
| --- | --- |
| From | ``` func removeObserver(_ observer: AnyObject!, name aName: String!, object anObject: String!) ``` |
| To | ``` func removeObserver(_ observer: AnyObject?, name aName: String?, object anObject: String?) ``` |

Modified NSEdgeInsets [struct]

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct NSEdgeInsets {     var top: CGFloat     var left: CGFloat     var bottom: CGFloat     var right: CGFloat } ``` | AppKit |
| To | ``` struct NSEdgeInsets {     var top: CGFloat     var left: CGFloat     var bottom: CGFloat     var right: CGFloat     init()     init(top top: CGFloat, left left: CGFloat, bottom bottom: CGFloat, right right: CGFloat) } ``` | Foundation |

Modified NSEdgeInsets.bottom

|  | Module |
| --- | --- |
| From | AppKit |
| To | Foundation |

Modified NSEdgeInsets.left

|  | Module |
| --- | --- |
| From | AppKit |
| To | Foundation |

Modified NSEdgeInsets.right

|  | Module |
| --- | --- |
| From | AppKit |
| To | Foundation |

Modified NSEdgeInsets.top

|  | Module |
| --- | --- |
| From | AppKit |
| To | Foundation |

Modified NSEnergyFormatter.getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forString: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getObjectValue(_ obj: AutoreleasingUnsafePointer<AnyObject?>, forString string: String!, errorDescription error: AutoreleasingUnsafePointer<NSString?>) -> Bool ``` |
| To | ``` func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool ``` |

Modified NSEnergyFormatter.numberFormatter

|  | Declaration |
| --- | --- |
| From | ``` var numberFormatter: NSNumberFormatter! ``` |
| To | ``` @NSCopying var numberFormatter: NSNumberFormatter ``` |

Modified NSEnergyFormatter.stringFromJoules(Double) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringFromJoules(_ numberInJoules: Double) -> String! ``` |
| To | ``` func stringFromJoules(_ numberInJoules: Double) -> String ``` |

Modified NSEnergyFormatter.stringFromValue(Double, unit: NSEnergyFormatterUnit) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringFromValue(_ value: Double, unit unit: NSEnergyFormatterUnit) -> String! ``` |
| To | ``` func stringFromValue(_ value: Double, unit unit: NSEnergyFormatterUnit) -> String ``` |

Modified NSEnergyFormatter.unitStringFromJoules(Double, usedUnit: UnsafeMutablePointer<NSEnergyFormatterUnit>) -> String

|  | Declaration |
| --- | --- |
| From | ``` func unitStringFromJoules(_ numberInJoules: Double, usedUnit unitp: UnsafePointer<NSEnergyFormatterUnit>) -> String! ``` |
| To | ``` func unitStringFromJoules(_ numberInJoules: Double, usedUnit unitp: UnsafeMutablePointer<NSEnergyFormatterUnit>) -> String ``` |

Modified NSEnergyFormatter.unitStringFromValue(Double, unit: NSEnergyFormatterUnit) -> String

|  | Declaration |
| --- | --- |
| From | ``` func unitStringFromValue(_ value: Double, unit unit: NSEnergyFormatterUnit) -> String! ``` |
| To | ``` func unitStringFromValue(_ value: Double, unit unit: NSEnergyFormatterUnit) -> String ``` |

Modified NSEnumerationOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSEnumerationOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Concurrent: NSEnumerationOptions { get }     static var Reverse: NSEnumerationOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Concurrent: NSEnumerationOptions { get }     static var Reverse: NSEnumerationOptions { get } } ``` | RawOptionSetType |

Modified NSEnumerationOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSEnumerator

|  | Protocols |
| --- | --- |
| From | AnyObject, NSFastEnumeration |
| To | AnyObject, NSFastEnumeration, SequenceType |

Modified NSEnumerator.allObjects

|  | Declaration |
| --- | --- |
| From | ``` var allObjects: [AnyObject]! { get } ``` |
| To | ``` var allObjects: [AnyObject] { get } ``` |

Modified NSEnumerator.nextObject() -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func nextObject() -> AnyObject! ``` |
| To | ``` func nextObject() -> AnyObject? ``` |

Modified NSError.domain

|  | Declaration |
| --- | --- |
| From | ``` var domain: String! { get } ``` |
| To | ``` var domain: String { get } ``` |

Modified NSError.init(domain: String, code: Int, userInfo:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(domain domain: String!, code code: Int, userInfo dict: [NSObject : AnyObject]!) ``` |
| To | ``` init(domain domain: String, code code: Int, userInfo dict: [NSObject : AnyObject]?) ``` |

Modified NSError.helpAnchor

|  | Declaration |
| --- | --- |
| From | ``` var helpAnchor: String! { get } ``` |
| To | ``` var helpAnchor: String? { get } ``` |

Modified NSError.localizedDescription

|  | Declaration |
| --- | --- |
| From | ``` var localizedDescription: String! { get } ``` |
| To | ``` var localizedDescription: String { get } ``` |

Modified NSError.localizedFailureReason

|  | Declaration |
| --- | --- |
| From | ``` var localizedFailureReason: String! { get } ``` |
| To | ``` var localizedFailureReason: String? { get } ``` |

Modified NSError.localizedRecoveryOptions

|  | Declaration |
| --- | --- |
| From | ``` var localizedRecoveryOptions: [AnyObject]! { get } ``` |
| To | ``` var localizedRecoveryOptions: [AnyObject]? { get } ``` |

Modified NSError.localizedRecoverySuggestion

|  | Declaration |
| --- | --- |
| From | ``` var localizedRecoverySuggestion: String! { get } ``` |
| To | ``` var localizedRecoverySuggestion: String? { get } ``` |

Modified NSError.recoveryAttempter

|  | Declaration |
| --- | --- |
| From | ``` var recoveryAttempter: AnyObject! { get } ``` |
| To | ``` var recoveryAttempter: AnyObject? { get } ``` |

Modified NSError.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! { get } ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? { get } ``` |

Modified NSException.callStackReturnAddresses

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var callStackReturnAddresses: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var callStackReturnAddresses: [AnyObject] { get } ``` | OS X 10.5 |

Modified NSException.callStackSymbols

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var callStackSymbols: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var callStackSymbols: [AnyObject] { get } ``` | OS X 10.6 |

Modified NSException.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified NSException.raise(String, format: String, arguments: CVaListPointer) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func raise(_ name: String!, format format: String!, arguments argList: CVaListPointer) ``` |
| To | ``` class func raise(_ name: String, format format: String, arguments argList: CVaListPointer) ``` |

Modified NSException.reason

|  | Declaration |
| --- | --- |
| From | ``` var reason: String! { get } ``` |
| To | ``` var reason: String? { get } ``` |

Modified NSException.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! { get } ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? { get } ``` |

Modified NSExpression

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSExpression.allowEvaluation()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSExpression.arguments

|  | Declaration |
| --- | --- |
| From | ``` var arguments: [AnyObject]! { get } ``` |
| To | ``` var arguments: [AnyObject] { get } ``` |

Modified NSExpression.collection

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var collection: AnyObject! { get } ``` | OS X 10.10 |
| To | ``` var collection: AnyObject { get } ``` | OS X 10.5 |

Modified NSExpression.constantValue

|  | Declaration |
| --- | --- |
| From | ``` var constantValue: AnyObject! { get } ``` |
| To | ``` var constantValue: AnyObject { get } ``` |

Modified NSExpression.expressionBlock

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var expressionBlock: ((AnyObject!, [AnyObject]!, NSMutableDictionary!) -> AnyObject!)! { get } ``` | OS X 10.10 |
| To | ``` var expressionBlock: (AnyObject!, [AnyObject]!, NSMutableDictionary!) -> AnyObject! { get } ``` | OS X 10.6 |

Modified NSExpression.expressionForAnyKey() -> NSExpression [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func expressionForAnyKey() -> NSExpression! ``` | OS X 10.10 |
| To | ``` class func expressionForAnyKey() -> NSExpression ``` | OS X 10.9 |

Modified NSExpression.expressionForEvaluatedObject() -> NSExpression [class]

|  | Declaration |
| --- | --- |
| From | ``` class func expressionForEvaluatedObject() -> NSExpression! ``` |
| To | ``` class func expressionForEvaluatedObject() -> NSExpression ``` |

Modified NSExpression.expressionValueWithObject(AnyObject?, context: NSMutableDictionary?) -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func expressionValueWithObject(_ object: AnyObject!, context context: NSMutableDictionary!) -> AnyObject! ``` |
| To | ``` func expressionValueWithObject(_ object: AnyObject?, context context: NSMutableDictionary?) -> AnyObject ``` |

Modified NSExpression.init(forAggregate: [AnyObject])

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(forAggregate subexpressions: [AnyObject]!) -> NSExpression ``` | OS X 10.10 |
| To | ``` init(forAggregate subexpressions: [AnyObject]) -> NSExpression ``` | OS X 10.5 |

Modified NSExpression.init(forBlock: (AnyObject!,[AnyObject]!, NSMutableDictionary!) -> AnyObject!, arguments:[AnyObject])

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(forBlock block: ((AnyObject!, [AnyObject]!, NSMutableDictionary!) -> AnyObject!)!, arguments arguments: [AnyObject]!) -> NSExpression ``` | OS X 10.10 |
| To | ``` init(forBlock block: (AnyObject!, [AnyObject]!, NSMutableDictionary!) -> AnyObject!, arguments arguments: [AnyObject]) -> NSExpression ``` | OS X 10.6 |

Modified NSExpression.init(forConstantValue: AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` init(forConstantValue obj: AnyObject!) -> NSExpression ``` |
| To | ``` init(forConstantValue obj: AnyObject) -> NSExpression ``` |

Modified NSExpression.init(forFunction: NSExpression, selectorName: String, arguments:[AnyObject])

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(forFunction target: NSExpression!, selectorName name: String!, arguments parameters: [AnyObject]!) -> NSExpression ``` | OS X 10.10 |
| To | ``` init(forFunction target: NSExpression, selectorName name: String, arguments parameters: [AnyObject]) -> NSExpression ``` | OS X 10.5 |

Modified NSExpression.init(forFunction: String, arguments:[AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` init(forFunction name: String!, arguments parameters: [AnyObject]!) -> NSExpression ``` |
| To | ``` init(forFunction name: String, arguments parameters: [AnyObject]) -> NSExpression ``` |

Modified NSExpression.init(forIntersectSet: NSExpression, with: NSExpression)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(forIntersectSet left: NSExpression!, with right: NSExpression!) -> NSExpression ``` | OS X 10.10 |
| To | ``` init(forIntersectSet left: NSExpression, with right: NSExpression) -> NSExpression ``` | OS X 10.5 |

Modified NSExpression.init(forKeyPath: String)

|  | Declaration |
| --- | --- |
| From | ``` init(forKeyPath keyPath: String!) -> NSExpression ``` |
| To | ``` init(forKeyPath keyPath: String) -> NSExpression ``` |

Modified NSExpression.init(forMinusSet: NSExpression, with: NSExpression)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(forMinusSet left: NSExpression!, with right: NSExpression!) -> NSExpression ``` | OS X 10.10 |
| To | ``` init(forMinusSet left: NSExpression, with right: NSExpression) -> NSExpression ``` | OS X 10.5 |

Modified NSExpression.init(forSubquery: NSExpression, usingIteratorVariable: String, predicate: AnyObject)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(forSubquery expression: NSExpression!, usingIteratorVariable variable: String!, predicate predicate: AnyObject!) -> NSExpression ``` | OS X 10.10 |
| To | ``` init(forSubquery expression: NSExpression, usingIteratorVariable variable: String, predicate predicate: AnyObject) -> NSExpression ``` | OS X 10.5 |

Modified NSExpression.init(forUnionSet: NSExpression, with: NSExpression)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(forUnionSet left: NSExpression!, with right: NSExpression!) -> NSExpression ``` | OS X 10.10 |
| To | ``` init(forUnionSet left: NSExpression, with right: NSExpression) -> NSExpression ``` | OS X 10.5 |

Modified NSExpression.init(forVariable: String)

|  | Declaration |
| --- | --- |
| From | ``` init(forVariable string: String!) -> NSExpression ``` |
| To | ``` init(forVariable string: String) -> NSExpression ``` |

Modified NSExpression.init(format: String, argumentArray:[AnyObject])

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(format expressionFormat: String!, argumentArray arguments: [AnyObject]!) -> NSExpression ``` | OS X 10.10 |
| To | ``` init(format expressionFormat: String, argumentArray arguments: [AnyObject]) -> NSExpression ``` | OS X 10.6 |

Modified NSExpression.init(format: String, arguments: CVaListPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(format expressionFormat: String!, arguments argList: CVaListPointer) -> NSExpression ``` | OS X 10.10 |
| To | ``` init(format expressionFormat: String, arguments argList: CVaListPointer) -> NSExpression ``` | OS X 10.6 |

Modified NSExpression.function

|  | Declaration |
| --- | --- |
| From | ``` var function: String! { get } ``` |
| To | ``` var function: String { get } ``` |

Modified NSExpression.keyPath

|  | Declaration |
| --- | --- |
| From | ``` var keyPath: String! { get } ``` |
| To | ``` var keyPath: String { get } ``` |

Modified NSExpression.leftExpression

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var leftExpression: NSExpression! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var leftExpression: NSExpression { get } ``` | OS X 10.5 |

Modified NSExpression.operand

|  | Declaration |
| --- | --- |
| From | ``` var operand: NSExpression! { get } ``` |
| To | ``` @NSCopying var operand: NSExpression { get } ``` |

Modified NSExpression.predicate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var predicate: NSPredicate! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var predicate: NSPredicate { get } ``` | OS X 10.5 |

Modified NSExpression.rightExpression

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var rightExpression: NSExpression! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var rightExpression: NSExpression { get } ``` | OS X 10.5 |

Modified NSExpression.variable

|  | Declaration |
| --- | --- |
| From | ``` var variable: String! { get } ``` |
| To | ``` var variable: String { get } ``` |

Modified NSExpressionType.AggregateExpressionType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSExpressionType.AnyKeyExpressionType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSExpressionType.IntersectSetExpressionType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSExpressionType.MinusSetExpressionType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSExpressionType.SubqueryExpressionType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSExpressionType.UnionSetExpressionType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSExtensionContext.cancelRequestWithError(NSError)

|  | Declaration |
| --- | --- |
| From | ``` func cancelRequestWithError(_ error: NSError!) ``` |
| To | ``` func cancelRequestWithError(_ error: NSError) ``` |

Modified NSExtensionContext.completeRequestReturningItems([AnyObject]?, completionHandler:((Bool) -> Void)?)

|  | Declaration |
| --- | --- |
| From | ``` func completeRequestReturningItems(_ items: [AnyObject]!, completionHandler completionHandler: ((Bool) -> Void)!) ``` |
| To | ``` func completeRequestReturningItems(_ items: [AnyObject]?, completionHandler completionHandler: ((Bool) -> Void)?) ``` |

Modified NSExtensionContext.inputItems

|  | Declaration |
| --- | --- |
| From | ``` var inputItems: [AnyObject]! { get } ``` |
| To | ``` var inputItems: [AnyObject] { get } ``` |

Modified NSExtensionContext.openURL(NSURL, completionHandler:((Bool) -> Void)?)

|  | Declaration |
| --- | --- |
| From | ``` func openURL(_ URL: NSURL!, completionHandler completionHandler: ((Bool) -> Void)!) ``` |
| To | ``` func openURL(_ URL: NSURL, completionHandler completionHandler: ((Bool) -> Void)?) ``` |

Modified NSExtensionItem.attachments

|  | Declaration |
| --- | --- |
| From | ``` var attachments: [AnyObject]! ``` |
| To | ``` var attachments: [AnyObject]? ``` |

Modified NSExtensionItem.attributedContentText

|  | Declaration |
| --- | --- |
| From | ``` var attributedContentText: NSAttributedString! ``` |
| To | ``` @NSCopying var attributedContentText: NSAttributedString? ``` |

Modified NSExtensionItem.attributedTitle

|  | Declaration |
| --- | --- |
| From | ``` var attributedTitle: NSAttributedString! ``` |
| To | ``` @NSCopying var attributedTitle: NSAttributedString? ``` |

Modified NSExtensionItem.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? ``` |

Modified NSExtensionRequestHandling.beginRequestWithExtensionContext(NSExtensionContext)

|  | Declaration |
| --- | --- |
| From | ``` func beginRequestWithExtensionContext(_ context: NSExtensionContext!) ``` |
| To | ``` func beginRequestWithExtensionContext(_ context: NSExtensionContext) ``` |

Modified NSFastEnumeration.countByEnumeratingWithState(UnsafeMutablePointer<NSFastEnumerationState>, objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, count: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func countByEnumeratingWithState(_ state: UnsafePointer<NSFastEnumerationState>, objects buffer: AutoreleasingUnsafePointer<AnyObject?>, count len: Int) -> Int ``` |
| To | ``` func countByEnumeratingWithState(_ state: UnsafeMutablePointer<NSFastEnumerationState>, objects buffer: AutoreleasingUnsafeMutablePointer<AnyObject?>, count len: Int) -> Int ``` |

Modified NSFastEnumerationState [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSFastEnumerationState {     var state: UInt     var itemsPtr: AutoreleasingUnsafePointer<AnyObject?>     var mutationsPtr: UnsafePointer<UInt>     var extra: (UInt, UInt, UInt, UInt, UInt) } ``` |
| To | ``` struct NSFastEnumerationState {     var state: UInt     var itemsPtr: AutoreleasingUnsafeMutablePointer<AnyObject?>     var mutationsPtr: UnsafeMutablePointer<UInt>     var extra: (UInt, UInt, UInt, UInt, UInt)     init()     init(state state: UInt, itemsPtr itemsPtr: AutoreleasingUnsafeMutablePointer<AnyObject?>, mutationsPtr mutationsPtr: UnsafeMutablePointer<UInt>, extra extra: (UInt, UInt, UInt, UInt, UInt)) } ``` |

Modified NSFastEnumerationState.itemsPtr

|  | Declaration |
| --- | --- |
| From | ``` var itemsPtr: AutoreleasingUnsafePointer<AnyObject?> ``` |
| To | ``` var itemsPtr: AutoreleasingUnsafeMutablePointer<AnyObject?> ``` |

Modified NSFastEnumerationState.mutationsPtr

|  | Declaration |
| --- | --- |
| From | ``` var mutationsPtr: UnsafePointer<UInt> ``` |
| To | ``` var mutationsPtr: UnsafeMutablePointer<UInt> ``` |

Modified NSFastGenerator

|  | Protocols |
| --- | --- |
| From | AnyObject, Generator |
| To | AnyObject, GeneratorType |

Modified NSFileAccessIntent.URL

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL { get } ``` |

Modified NSFileAccessIntent.readingIntentWithURL(NSURL, options: NSFileCoordinatorReadingOptions) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func readingIntentWithURL(_ url: NSURL!, options options: NSFileCoordinatorReadingOptions) -> Self! ``` | OS X 10.10 |
| To | ``` class func readingIntentWithURL(_ url: NSURL, options options: NSFileCoordinatorReadingOptions) -> Self ``` | OS X 10.10.3 |

Modified NSFileAccessIntent.writingIntentWithURL(NSURL, options: NSFileCoordinatorWritingOptions) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func writingIntentWithURL(_ url: NSURL!, options options: NSFileCoordinatorWritingOptions) -> Self! ``` | OS X 10.10 |
| To | ``` class func writingIntentWithURL(_ url: NSURL, options options: NSFileCoordinatorWritingOptions) -> Self ``` | OS X 10.10.3 |

Modified NSFileCoordinator

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSFileCoordinator.addFilePresenter(NSFilePresenter) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func addFilePresenter(_ filePresenter: NSFilePresenter!) ``` |
| To | ``` class func addFilePresenter(_ filePresenter: NSFilePresenter) ``` |

Modified NSFileCoordinator.coordinateAccessWithIntents([AnyObject], queue: NSOperationQueue, byAccessor:(NSError!) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func coordinateAccessWithIntents(_ intents: [AnyObject]!, queue queue: NSOperationQueue!, byAccessor accessor: ((NSError!) -> Void)!) ``` |
| To | ``` func coordinateAccessWithIntents(_ intents: [AnyObject], queue queue: NSOperationQueue, byAccessor accessor: (NSError!) -> Void) ``` |

Modified NSFileCoordinator.coordinateReadingItemAtURL(NSURL, options: NSFileCoordinatorReadingOptions, error: NSErrorPointer, byAccessor:(NSURL!) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func coordinateReadingItemAtURL(_ url: NSURL!, options options: NSFileCoordinatorReadingOptions, error outError: NSErrorPointer, byAccessor reader: ((NSURL!) -> Void)!) ``` |
| To | ``` func coordinateReadingItemAtURL(_ url: NSURL, options options: NSFileCoordinatorReadingOptions, error outError: NSErrorPointer, byAccessor reader: (NSURL!) -> Void) ``` |

Modified NSFileCoordinator.coordinateReadingItemAtURL(NSURL, options: NSFileCoordinatorReadingOptions, writingItemAtURL: NSURL, options: NSFileCoordinatorWritingOptions, error: NSErrorPointer, byAccessor:(NSURL!, NSURL!) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func coordinateReadingItemAtURL(_ readingURL: NSURL!, options readingOptions: NSFileCoordinatorReadingOptions, writingItemAtURL writingURL: NSURL!, options writingOptions: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor readerWriter: ((NSURL!, NSURL!) -> Void)!) ``` |
| To | ``` func coordinateReadingItemAtURL(_ readingURL: NSURL, options readingOptions: NSFileCoordinatorReadingOptions, writingItemAtURL writingURL: NSURL, options writingOptions: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor readerWriter: (NSURL!, NSURL!) -> Void) ``` |

Modified NSFileCoordinator.coordinateWritingItemAtURL(NSURL, options: NSFileCoordinatorWritingOptions, error: NSErrorPointer, byAccessor:(NSURL!) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func coordinateWritingItemAtURL(_ url: NSURL!, options options: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor writer: ((NSURL!) -> Void)!) ``` |
| To | ``` func coordinateWritingItemAtURL(_ url: NSURL, options options: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor writer: (NSURL!) -> Void) ``` |

Modified NSFileCoordinator.coordinateWritingItemAtURL(NSURL, options: NSFileCoordinatorWritingOptions, writingItemAtURL: NSURL, options: NSFileCoordinatorWritingOptions, error: NSErrorPointer, byAccessor:(NSURL!, NSURL!) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func coordinateWritingItemAtURL(_ url1: NSURL!, options options1: NSFileCoordinatorWritingOptions, writingItemAtURL url2: NSURL!, options options2: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor writer: ((NSURL!, NSURL!) -> Void)!) ``` |
| To | ``` func coordinateWritingItemAtURL(_ url1: NSURL, options options1: NSFileCoordinatorWritingOptions, writingItemAtURL url2: NSURL, options options2: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor writer: (NSURL!, NSURL!) -> Void) ``` |

Modified NSFileCoordinator.init(filePresenter: NSFilePresenter?)

|  | Declaration |
| --- | --- |
| From | ``` init(filePresenter filePresenterOrNil: NSFilePresenter!) ``` |
| To | ``` init(filePresenter filePresenterOrNil: NSFilePresenter?) ``` |

Modified NSFileCoordinator.filePresenters() -> [AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func filePresenters() -> [AnyObject]! ``` |
| To | ``` class func filePresenters() -> [AnyObject] ``` |

Modified NSFileCoordinator.itemAtURL(NSURL, didMoveToURL: NSURL)

|  | Declaration |
| --- | --- |
| From | ``` func itemAtURL(_ oldURL: NSURL!, didMoveToURL newURL: NSURL!) ``` |
| To | ``` func itemAtURL(_ oldURL: NSURL, didMoveToURL newURL: NSURL) ``` |

Modified NSFileCoordinator.itemAtURL(NSURL, willMoveToURL: NSURL)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func itemAtURL(_ oldURL: NSURL!, willMoveToURL newURL: NSURL!) ``` | OS X 10.10 |
| To | ``` func itemAtURL(_ oldURL: NSURL, willMoveToURL newURL: NSURL) ``` | OS X 10.8 |

Modified NSFileCoordinator.prepareForReadingItemsAtURLs([AnyObject], options: NSFileCoordinatorReadingOptions, writingItemsAtURLs:[AnyObject], options: NSFileCoordinatorWritingOptions, error: NSErrorPointer, byAccessor:((() -> Void)!) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func prepareForReadingItemsAtURLs(_ readingURLs: [AnyObject]!, options readingOptions: NSFileCoordinatorReadingOptions, writingItemsAtURLs writingURLs: [AnyObject]!, options writingOptions: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor batchAccessor: (((() -> Void)!) -> Void)!) ``` |
| To | ``` func prepareForReadingItemsAtURLs(_ readingURLs: [AnyObject], options readingOptions: NSFileCoordinatorReadingOptions, writingItemsAtURLs writingURLs: [AnyObject], options writingOptions: NSFileCoordinatorWritingOptions, error outError: NSErrorPointer, byAccessor batchAccessor: ((() -> Void)!) -> Void) ``` |

Modified NSFileCoordinator.purposeIdentifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var purposeIdentifier: String! ``` | OS X 10.10 |
| To | ``` var purposeIdentifier: String ``` | OS X 10.7 |

Modified NSFileCoordinator.removeFilePresenter(NSFilePresenter) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func removeFilePresenter(_ filePresenter: NSFilePresenter!) ``` |
| To | ``` class func removeFilePresenter(_ filePresenter: NSFilePresenter) ``` |

Modified NSFileCoordinatorReadingOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSFileCoordinatorReadingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var WithoutChanges: NSFileCoordinatorReadingOptions { get }     static var ResolvesSymbolicLink: NSFileCoordinatorReadingOptions { get }     static var ImmediatelyAvailableMetadataOnly: NSFileCoordinatorReadingOptions { get }     static var ForUploading: NSFileCoordinatorReadingOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSFileCoordinatorReadingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var WithoutChanges: NSFileCoordinatorReadingOptions { get }     static var ResolvesSymbolicLink: NSFileCoordinatorReadingOptions { get }     static var ImmediatelyAvailableMetadataOnly: NSFileCoordinatorReadingOptions { get }     static var ForUploading: NSFileCoordinatorReadingOptions { get } } ``` | RawOptionSetType |

Modified NSFileCoordinatorReadingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFileCoordinatorWritingOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSFileCoordinatorWritingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var ForDeleting: NSFileCoordinatorWritingOptions { get }     static var ForMoving: NSFileCoordinatorWritingOptions { get }     static var ForMerging: NSFileCoordinatorWritingOptions { get }     static var ForReplacing: NSFileCoordinatorWritingOptions { get }     static var ContentIndependentMetadataOnly: NSFileCoordinatorWritingOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSFileCoordinatorWritingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ForDeleting: NSFileCoordinatorWritingOptions { get }     static var ForMoving: NSFileCoordinatorWritingOptions { get }     static var ForMerging: NSFileCoordinatorWritingOptions { get }     static var ForReplacing: NSFileCoordinatorWritingOptions { get }     static var ContentIndependentMetadataOnly: NSFileCoordinatorWritingOptions { get } } ``` | RawOptionSetType |

Modified NSFileCoordinatorWritingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFileHandle.acceptConnectionInBackgroundAndNotifyForModes([AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func acceptConnectionInBackgroundAndNotifyForModes(_ modes: [AnyObject]!) ``` |
| To | ``` func acceptConnectionInBackgroundAndNotifyForModes(_ modes: [AnyObject]) ``` |

Modified NSFileHandle.availableData

|  | Declaration |
| --- | --- |
| From | ``` var availableData: NSData! { get } ``` |
| To | ``` @NSCopying var availableData: NSData { get } ``` |

Modified NSFileHandle.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder coder: NSCoder!) ``` |
| To | ``` init?(coder coder: NSCoder) ``` |

Modified NSFileHandle.fileHandleWithNullDevice() -> NSFileHandle [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fileHandleWithNullDevice() -> NSFileHandle! ``` |
| To | ``` class func fileHandleWithNullDevice() -> NSFileHandle ``` |

Modified NSFileHandle.fileHandleWithStandardError() -> NSFileHandle [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fileHandleWithStandardError() -> NSFileHandle! ``` |
| To | ``` class func fileHandleWithStandardError() -> NSFileHandle ``` |

Modified NSFileHandle.fileHandleWithStandardInput() -> NSFileHandle [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fileHandleWithStandardInput() -> NSFileHandle! ``` |
| To | ``` class func fileHandleWithStandardInput() -> NSFileHandle ``` |

Modified NSFileHandle.fileHandleWithStandardOutput() -> NSFileHandle [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fileHandleWithStandardOutput() -> NSFileHandle! ``` |
| To | ``` class func fileHandleWithStandardOutput() -> NSFileHandle ``` |

Modified NSFileHandle.init(forReadingAtPath: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(forReadingAtPath path: String!) ``` |
| To | ``` convenience init?(forReadingAtPath path: String) ``` |

Modified NSFileHandle.init(forReadingFromURL: NSURL, error: NSErrorPointer)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | fileHandleForReadingFromURL(_:error:) | ``` class func fileHandleForReadingFromURL(_ url: NSURL!, error error: NSErrorPointer) -> Self! ``` | OS X 10.10 |
| To | init(forReadingFromURL:error:) | ``` convenience init?(forReadingFromURL url: NSURL, error error: NSErrorPointer) ``` | OS X 10.6 |

Modified NSFileHandle.init(forUpdatingAtPath: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(forUpdatingAtPath path: String!) ``` |
| To | ``` convenience init?(forUpdatingAtPath path: String) ``` |

Modified NSFileHandle.init(forUpdatingURL: NSURL, error: NSErrorPointer)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | fileHandleForUpdatingURL(_:error:) | ``` class func fileHandleForUpdatingURL(_ url: NSURL!, error error: NSErrorPointer) -> Self! ``` | OS X 10.10 |
| To | init(forUpdatingURL:error:) | ``` convenience init?(forUpdatingURL url: NSURL, error error: NSErrorPointer) ``` | OS X 10.6 |

Modified NSFileHandle.init(forWritingAtPath: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(forWritingAtPath path: String!) ``` |
| To | ``` convenience init?(forWritingAtPath path: String) ``` |

Modified NSFileHandle.init(forWritingToURL: NSURL, error: NSErrorPointer)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | fileHandleForWritingToURL(_:error:) | ``` class func fileHandleForWritingToURL(_ url: NSURL!, error error: NSErrorPointer) -> Self! ``` | OS X 10.10 |
| To | init(forWritingToURL:error:) | ``` convenience init?(forWritingToURL url: NSURL, error error: NSErrorPointer) ``` | OS X 10.6 |

Modified NSFileHandle.readDataOfLength(Int) -> NSData

|  | Declaration |
| --- | --- |
| From | ``` func readDataOfLength(_ length: Int) -> NSData! ``` |
| To | ``` func readDataOfLength(_ length: Int) -> NSData ``` |

Modified NSFileHandle.readDataToEndOfFile() -> NSData

|  | Declaration |
| --- | --- |
| From | ``` func readDataToEndOfFile() -> NSData! ``` |
| To | ``` func readDataToEndOfFile() -> NSData ``` |

Modified NSFileHandle.readInBackgroundAndNotifyForModes([AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func readInBackgroundAndNotifyForModes(_ modes: [AnyObject]!) ``` |
| To | ``` func readInBackgroundAndNotifyForModes(_ modes: [AnyObject]) ``` |

Modified NSFileHandle.readToEndOfFileInBackgroundAndNotifyForModes([AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func readToEndOfFileInBackgroundAndNotifyForModes(_ modes: [AnyObject]!) ``` |
| To | ``` func readToEndOfFileInBackgroundAndNotifyForModes(_ modes: [AnyObject]) ``` |

Modified NSFileHandle.readabilityHandler

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var readabilityHandler: ((NSFileHandle!) -> Void)! ``` | OS X 10.10 |
| To | ``` var readabilityHandler: ((NSFileHandle!) -> Void)? ``` | OS X 10.7 |

Modified NSFileHandle.waitForDataInBackgroundAndNotifyForModes([AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func waitForDataInBackgroundAndNotifyForModes(_ modes: [AnyObject]!) ``` |
| To | ``` func waitForDataInBackgroundAndNotifyForModes(_ modes: [AnyObject]) ``` |

Modified NSFileHandle.writeData(NSData)

|  | Declaration |
| --- | --- |
| From | ``` func writeData(_ data: NSData!) ``` |
| To | ``` func writeData(_ data: NSData) ``` |

Modified NSFileHandle.writeabilityHandler

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var writeabilityHandler: ((NSFileHandle!) -> Void)! ``` | OS X 10.10 |
| To | ``` var writeabilityHandler: ((NSFileHandle!) -> Void)? ``` | OS X 10.7 |

Modified NSFileManager.URLForDirectory(NSSearchPathDirectory, inDomain: NSSearchPathDomainMask, appropriateForURL: NSURL?, create: Bool, error: NSErrorPointer) -> NSURL?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URLForDirectory(_ directory: NSSearchPathDirectory, inDomain domain: NSSearchPathDomainMask, appropriateForURL url: NSURL!, create shouldCreate: Bool, error error: NSErrorPointer) -> NSURL! ``` | OS X 10.10 |
| To | ``` func URLForDirectory(_ directory: NSSearchPathDirectory, inDomain domain: NSSearchPathDomainMask, appropriateForURL url: NSURL?, create shouldCreate: Bool, error error: NSErrorPointer) -> NSURL? ``` | OS X 10.6 |

Modified NSFileManager.URLForPublishingUbiquitousItemAtURL(NSURL, expirationDate: AutoreleasingUnsafeMutablePointer<NSDate?>, error: NSErrorPointer) -> NSURL?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URLForPublishingUbiquitousItemAtURL(_ url: NSURL!, expirationDate outDate: AutoreleasingUnsafePointer<NSDate?>, error error: NSErrorPointer) -> NSURL! ``` | OS X 10.10 |
| To | ``` func URLForPublishingUbiquitousItemAtURL(_ url: NSURL, expirationDate outDate: AutoreleasingUnsafeMutablePointer<NSDate?>, error error: NSErrorPointer) -> NSURL? ``` | OS X 10.7 |

Modified NSFileManager.URLForUbiquityContainerIdentifier(String?) -> NSURL?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URLForUbiquityContainerIdentifier(_ containerIdentifier: String!) -> NSURL! ``` | OS X 10.10 |
| To | ``` func URLForUbiquityContainerIdentifier(_ containerIdentifier: String?) -> NSURL? ``` | OS X 10.7 |

Modified NSFileManager.URLsForDirectory(NSSearchPathDirectory, inDomains: NSSearchPathDomainMask) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URLsForDirectory(_ directory: NSSearchPathDirectory, inDomains domainMask: NSSearchPathDomainMask) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func URLsForDirectory(_ directory: NSSearchPathDirectory, inDomains domainMask: NSSearchPathDomainMask) -> [AnyObject] ``` | OS X 10.6 |

Modified NSFileManager.attributesOfFileSystemForPath(String, error: NSErrorPointer) -> [NSObject: AnyObject]?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func attributesOfFileSystemForPath(_ path: String!, error error: NSErrorPointer) -> [NSObject : AnyObject]! ``` | OS X 10.10 |
| To | ``` func attributesOfFileSystemForPath(_ path: String, error error: NSErrorPointer) -> [NSObject : AnyObject]? ``` | OS X 10.5 |

Modified NSFileManager.attributesOfItemAtPath(String, error: NSErrorPointer) -> [NSObject: AnyObject]?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func attributesOfItemAtPath(_ path: String!, error error: NSErrorPointer) -> [NSObject : AnyObject]! ``` | OS X 10.10 |
| To | ``` func attributesOfItemAtPath(_ path: String, error error: NSErrorPointer) -> [NSObject : AnyObject]? ``` | OS X 10.5 |

Modified NSFileManager.changeCurrentDirectoryPath(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func changeCurrentDirectoryPath(_ path: String!) -> Bool ``` |
| To | ``` func changeCurrentDirectoryPath(_ path: String) -> Bool ``` |

Modified NSFileManager.componentsToDisplayForPath(String) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func componentsToDisplayForPath(_ path: String!) -> [AnyObject]! ``` |
| To | ``` func componentsToDisplayForPath(_ path: String) -> [AnyObject]? ``` |

Modified NSFileManager.containerURLForSecurityApplicationGroupIdentifier(String) -> NSURL?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func containerURLForSecurityApplicationGroupIdentifier(_ groupIdentifier: String!) -> NSURL! ``` | OS X 10.10 |
| To | ``` func containerURLForSecurityApplicationGroupIdentifier(_ groupIdentifier: String) -> NSURL? ``` | OS X 10.8 |

Modified NSFileManager.contentsAtPath(String) -> NSData?

|  | Declaration |
| --- | --- |
| From | ``` func contentsAtPath(_ path: String!) -> NSData! ``` |
| To | ``` func contentsAtPath(_ path: String) -> NSData? ``` |

Modified NSFileManager.contentsEqualAtPath(String, andPath: String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func contentsEqualAtPath(_ path1: String!, andPath path2: String!) -> Bool ``` |
| To | ``` func contentsEqualAtPath(_ path1: String, andPath path2: String) -> Bool ``` |

Modified NSFileManager.contentsOfDirectoryAtPath(String, error: NSErrorPointer) -> [AnyObject]?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func contentsOfDirectoryAtPath(_ path: String!, error error: NSErrorPointer) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func contentsOfDirectoryAtPath(_ path: String, error error: NSErrorPointer) -> [AnyObject]? ``` | OS X 10.5 |

Modified NSFileManager.contentsOfDirectoryAtURL(NSURL, includingPropertiesForKeys:[AnyObject]?, options: NSDirectoryEnumerationOptions, error: NSErrorPointer) -> [AnyObject]?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func contentsOfDirectoryAtURL(_ url: NSURL!, includingPropertiesForKeys keys: [AnyObject]!, options mask: NSDirectoryEnumerationOptions, error error: NSErrorPointer) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func contentsOfDirectoryAtURL(_ url: NSURL, includingPropertiesForKeys keys: [AnyObject]?, options mask: NSDirectoryEnumerationOptions, error error: NSErrorPointer) -> [AnyObject]? ``` | OS X 10.6 |

Modified NSFileManager.copyItemAtPath(String, toPath: String, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func copyItemAtPath(_ srcPath: String!, toPath dstPath: String!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func copyItemAtPath(_ srcPath: String, toPath dstPath: String, error error: NSErrorPointer) -> Bool ``` | OS X 10.5 |

Modified NSFileManager.copyItemAtURL(NSURL, toURL: NSURL, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func copyItemAtURL(_ srcURL: NSURL!, toURL dstURL: NSURL!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func copyItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL, error error: NSErrorPointer) -> Bool ``` | OS X 10.6 |

Modified NSFileManager.createDirectoryAtPath(String, withIntermediateDirectories: Bool, attributes:[NSObject: AnyObject]?, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func createDirectoryAtPath(_ path: String!, withIntermediateDirectories createIntermediates: Bool, attributes attributes: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func createDirectoryAtPath(_ path: String, withIntermediateDirectories createIntermediates: Bool, attributes attributes: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool ``` | OS X 10.5 |

Modified NSFileManager.createDirectoryAtURL(NSURL, withIntermediateDirectories: Bool, attributes:[NSObject: AnyObject]?, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func createDirectoryAtURL(_ url: NSURL!, withIntermediateDirectories createIntermediates: Bool, attributes attributes: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func createDirectoryAtURL(_ url: NSURL, withIntermediateDirectories createIntermediates: Bool, attributes attributes: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool ``` | OS X 10.7 |

Modified NSFileManager.createFileAtPath(String, contents: NSData?, attributes:[NSObject: AnyObject]?) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func createFileAtPath(_ path: String!, contents data: NSData!, attributes attr: [NSObject : AnyObject]!) -> Bool ``` |
| To | ``` func createFileAtPath(_ path: String, contents data: NSData?, attributes attr: [NSObject : AnyObject]?) -> Bool ``` |

Modified NSFileManager.createSymbolicLinkAtPath(String, withDestinationPath: String, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func createSymbolicLinkAtPath(_ path: String!, withDestinationPath destPath: String!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func createSymbolicLinkAtPath(_ path: String, withDestinationPath destPath: String, error error: NSErrorPointer) -> Bool ``` | OS X 10.5 |

Modified NSFileManager.createSymbolicLinkAtURL(NSURL, withDestinationURL: NSURL, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func createSymbolicLinkAtURL(_ url: NSURL!, withDestinationURL destURL: NSURL!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func createSymbolicLinkAtURL(_ url: NSURL, withDestinationURL destURL: NSURL, error error: NSErrorPointer) -> Bool ``` | OS X 10.7 |

Modified NSFileManager.currentDirectoryPath

|  | Declaration |
| --- | --- |
| From | ``` var currentDirectoryPath: String! { get } ``` |
| To | ``` var currentDirectoryPath: String { get } ``` |

Modified NSFileManager.defaultManager() -> NSFileManager [class]

|  | Declaration |
| --- | --- |
| From | ``` class func defaultManager() -> NSFileManager! ``` |
| To | ``` class func defaultManager() -> NSFileManager ``` |

Modified NSFileManager.delegate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var delegate: NSFileManagerDelegate! ``` | OS X 10.10 |
| To | ``` unowned(unsafe) var delegate: NSFileManagerDelegate? ``` | OS X 10.5 |

Modified NSFileManager.destinationOfSymbolicLinkAtPath(String, error: NSErrorPointer) -> String?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func destinationOfSymbolicLinkAtPath(_ path: String!, error error: NSErrorPointer) -> String! ``` | OS X 10.10 |
| To | ``` func destinationOfSymbolicLinkAtPath(_ path: String, error error: NSErrorPointer) -> String? ``` | OS X 10.5 |

Modified NSFileManager.displayNameAtPath(String) -> String

|  | Declaration |
| --- | --- |
| From | ``` func displayNameAtPath(_ path: String!) -> String! ``` |
| To | ``` func displayNameAtPath(_ path: String) -> String ``` |

Modified NSFileManager.enumeratorAtPath(String) -> NSDirectoryEnumerator?

|  | Declaration |
| --- | --- |
| From | ``` func enumeratorAtPath(_ path: String!) -> NSDirectoryEnumerator! ``` |
| To | ``` func enumeratorAtPath(_ path: String) -> NSDirectoryEnumerator? ``` |

Modified NSFileManager.enumeratorAtURL(NSURL, includingPropertiesForKeys:[AnyObject]?, options: NSDirectoryEnumerationOptions, errorHandler:((NSURL!, NSError!) -> Bool)?) -> NSDirectoryEnumerator?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumeratorAtURL(_ url: NSURL!, includingPropertiesForKeys keys: [AnyObject]!, options mask: NSDirectoryEnumerationOptions, errorHandler handler: ((NSURL!, NSError!) -> Bool)!) -> NSDirectoryEnumerator! ``` | OS X 10.10 |
| To | ``` func enumeratorAtURL(_ url: NSURL, includingPropertiesForKeys keys: [AnyObject]?, options mask: NSDirectoryEnumerationOptions, errorHandler handler: ((NSURL!, NSError!) -> Bool)?) -> NSDirectoryEnumerator? ``` | OS X 10.6 |

Modified NSFileManager.evictUbiquitousItemAtURL(NSURL, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func evictUbiquitousItemAtURL(_ url: NSURL!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func evictUbiquitousItemAtURL(_ url: NSURL, error error: NSErrorPointer) -> Bool ``` | OS X 10.7 |

Modified NSFileManager.fileExistsAtPath(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func fileExistsAtPath(_ path: String!) -> Bool ``` |
| To | ``` func fileExistsAtPath(_ path: String) -> Bool ``` |

Modified NSFileManager.fileExistsAtPath(String, isDirectory: UnsafeMutablePointer<ObjCBool>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func fileExistsAtPath(_ path: String!, isDirectory isDirectory: UnsafePointer<ObjCBool>) -> Bool ``` |
| To | ``` func fileExistsAtPath(_ path: String, isDirectory isDirectory: UnsafeMutablePointer<ObjCBool>) -> Bool ``` |

Modified NSFileManager.fileSystemRepresentationWithPath(String) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func fileSystemRepresentationWithPath(_ path: String!) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func fileSystemRepresentationWithPath(_ path: String) -> UnsafePointer<Int8> ``` |

Modified NSFileManager.getRelationship(UnsafeMutablePointer<NSURLRelationship>, ofDirectory: NSSearchPathDirectory, inDomain: NSSearchPathDomainMask, toItemAtURL: NSURL, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getRelationship(_ outRelationship: UnsafePointer<NSURLRelationship>, ofDirectory directory: NSSearchPathDirectory, inDomain domainMask: NSSearchPathDomainMask, toItemAtURL url: NSURL!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func getRelationship(_ outRelationship: UnsafeMutablePointer<NSURLRelationship>, ofDirectory directory: NSSearchPathDirectory, inDomain domainMask: NSSearchPathDomainMask, toItemAtURL url: NSURL, error error: NSErrorPointer) -> Bool ``` |

Modified NSFileManager.getRelationship(UnsafeMutablePointer<NSURLRelationship>, ofDirectoryAtURL: NSURL, toItemAtURL: NSURL, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getRelationship(_ outRelationship: UnsafePointer<NSURLRelationship>, ofDirectoryAtURL directoryURL: NSURL!, toItemAtURL otherURL: NSURL!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func getRelationship(_ outRelationship: UnsafeMutablePointer<NSURLRelationship>, ofDirectoryAtURL directoryURL: NSURL, toItemAtURL otherURL: NSURL, error error: NSErrorPointer) -> Bool ``` |

Modified NSFileManager.isDeletableFileAtPath(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isDeletableFileAtPath(_ path: String!) -> Bool ``` |
| To | ``` func isDeletableFileAtPath(_ path: String) -> Bool ``` |

Modified NSFileManager.isExecutableFileAtPath(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isExecutableFileAtPath(_ path: String!) -> Bool ``` |
| To | ``` func isExecutableFileAtPath(_ path: String) -> Bool ``` |

Modified NSFileManager.isReadableFileAtPath(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isReadableFileAtPath(_ path: String!) -> Bool ``` |
| To | ``` func isReadableFileAtPath(_ path: String) -> Bool ``` |

Modified NSFileManager.isUbiquitousItemAtURL(NSURL) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isUbiquitousItemAtURL(_ url: NSURL!) -> Bool ``` | OS X 10.10 |
| To | ``` func isUbiquitousItemAtURL(_ url: NSURL) -> Bool ``` | OS X 10.7 |

Modified NSFileManager.isWritableFileAtPath(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isWritableFileAtPath(_ path: String!) -> Bool ``` |
| To | ``` func isWritableFileAtPath(_ path: String) -> Bool ``` |

Modified NSFileManager.linkItemAtPath(String, toPath: String, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func linkItemAtPath(_ srcPath: String!, toPath dstPath: String!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func linkItemAtPath(_ srcPath: String, toPath dstPath: String, error error: NSErrorPointer) -> Bool ``` | OS X 10.5 |

Modified NSFileManager.linkItemAtURL(NSURL, toURL: NSURL, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func linkItemAtURL(_ srcURL: NSURL!, toURL dstURL: NSURL!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func linkItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL, error error: NSErrorPointer) -> Bool ``` | OS X 10.6 |

Modified NSFileManager.mountedVolumeURLsIncludingResourceValuesForKeys([AnyObject]?, options: NSVolumeEnumerationOptions) -> [AnyObject]?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mountedVolumeURLsIncludingResourceValuesForKeys(_ propertyKeys: [AnyObject]!, options options: NSVolumeEnumerationOptions) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func mountedVolumeURLsIncludingResourceValuesForKeys(_ propertyKeys: [AnyObject]?, options options: NSVolumeEnumerationOptions) -> [AnyObject]? ``` | OS X 10.6 |

Modified NSFileManager.moveItemAtPath(String, toPath: String, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func moveItemAtPath(_ srcPath: String!, toPath dstPath: String!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func moveItemAtPath(_ srcPath: String, toPath dstPath: String, error error: NSErrorPointer) -> Bool ``` | OS X 10.5 |

Modified NSFileManager.moveItemAtURL(NSURL, toURL: NSURL, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func moveItemAtURL(_ srcURL: NSURL!, toURL dstURL: NSURL!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func moveItemAtURL(_ srcURL: NSURL, toURL dstURL: NSURL, error error: NSErrorPointer) -> Bool ``` | OS X 10.6 |

Modified NSFileManager.removeItemAtPath(String, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func removeItemAtPath(_ path: String!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func removeItemAtPath(_ path: String, error error: NSErrorPointer) -> Bool ``` | OS X 10.5 |

Modified NSFileManager.removeItemAtURL(NSURL, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func removeItemAtURL(_ URL: NSURL!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func removeItemAtURL(_ URL: NSURL, error error: NSErrorPointer) -> Bool ``` | OS X 10.6 |

Modified NSFileManager.replaceItemAtURL(NSURL, withItemAtURL: NSURL, backupItemName: String?, options: NSFileManagerItemReplacementOptions, resultingItemURL: AutoreleasingUnsafeMutablePointer<NSURL?>, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func replaceItemAtURL(_ originalItemURL: NSURL!, withItemAtURL newItemURL: NSURL!, backupItemName backupItemName: String!, options options: NSFileManagerItemReplacementOptions, resultingItemURL resultingURL: AutoreleasingUnsafePointer<NSURL?>, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func replaceItemAtURL(_ originalItemURL: NSURL, withItemAtURL newItemURL: NSURL, backupItemName backupItemName: String?, options options: NSFileManagerItemReplacementOptions, resultingItemURL resultingURL: AutoreleasingUnsafeMutablePointer<NSURL?>, error error: NSErrorPointer) -> Bool ``` | OS X 10.6 |

Modified NSFileManager.setAttributes([NSObject: AnyObject], ofItemAtPath: String, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setAttributes(_ attributes: [NSObject : AnyObject]!, ofItemAtPath path: String!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func setAttributes(_ attributes: [NSObject : AnyObject], ofItemAtPath path: String, error error: NSErrorPointer) -> Bool ``` | OS X 10.5 |

Modified NSFileManager.setUbiquitous(Bool, itemAtURL: NSURL, destinationURL: NSURL, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setUbiquitous(_ flag: Bool, itemAtURL url: NSURL!, destinationURL destinationURL: NSURL!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func setUbiquitous(_ flag: Bool, itemAtURL url: NSURL, destinationURL destinationURL: NSURL, error error: NSErrorPointer) -> Bool ``` | OS X 10.7 |

Modified NSFileManager.startDownloadingUbiquitousItemAtURL(NSURL, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func startDownloadingUbiquitousItemAtURL(_ url: NSURL!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func startDownloadingUbiquitousItemAtURL(_ url: NSURL, error error: NSErrorPointer) -> Bool ``` | OS X 10.7 |

Modified NSFileManager.stringWithFileSystemRepresentation(UnsafePointer<Int8>, length: Int) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringWithFileSystemRepresentation(_ str: ConstUnsafePointer<Int8>, length len: Int) -> String! ``` |
| To | ``` func stringWithFileSystemRepresentation(_ str: UnsafePointer<Int8>, length len: Int) -> String ``` |

Modified NSFileManager.subpathsAtPath(String) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func subpathsAtPath(_ path: String!) -> [AnyObject]! ``` |
| To | ``` func subpathsAtPath(_ path: String) -> [AnyObject]? ``` |

Modified NSFileManager.subpathsOfDirectoryAtPath(String, error: NSErrorPointer) -> [AnyObject]?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func subpathsOfDirectoryAtPath(_ path: String!, error error: NSErrorPointer) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func subpathsOfDirectoryAtPath(_ path: String, error error: NSErrorPointer) -> [AnyObject]? ``` | OS X 10.5 |

Modified NSFileManager.trashItemAtURL(NSURL, resultingItemURL: AutoreleasingUnsafeMutablePointer<NSURL?>, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func trashItemAtURL(_ url: NSURL!, resultingItemURL outResultingURL: AutoreleasingUnsafePointer<NSURL?>, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func trashItemAtURL(_ url: NSURL, resultingItemURL outResultingURL: AutoreleasingUnsafeMutablePointer<NSURL?>, error error: NSErrorPointer) -> Bool ``` | OS X 10.8 |

Modified NSFileManager.ubiquityIdentityToken

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var ubiquityIdentityToken: protocol<NSCoding, NSCopying, NSObjectProtocol>! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var ubiquityIdentityToken: protocol<NSCoding, NSCopying, NSObjectProtocol>? { get } ``` | OS X 10.8 |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldCopyItemAtPath: String, toPath: String) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldCopyItemAtPath srcPath: String!, toPath dstPath: String!) -> Bool ``` | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldCopyItemAtPath srcPath: String, toPath dstPath: String) -> Bool ``` | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldCopyItemAtURL: NSURL, toURL: NSURL) -> Bool

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldCopyItemAtURL srcURL: NSURL!, toURL dstURL: NSURL!) -> Bool ``` | OS X 10.10 | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldCopyItemAtURL srcURL: NSURL, toURL dstURL: NSURL) -> Bool ``` | OS X 10.6 | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldLinkItemAtPath: String, toPath: String) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldLinkItemAtPath srcPath: String!, toPath dstPath: String!) -> Bool ``` | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldLinkItemAtPath srcPath: String, toPath dstPath: String) -> Bool ``` | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldLinkItemAtURL: NSURL, toURL: NSURL) -> Bool

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldLinkItemAtURL srcURL: NSURL!, toURL dstURL: NSURL!) -> Bool ``` | OS X 10.10 | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldLinkItemAtURL srcURL: NSURL, toURL dstURL: NSURL) -> Bool ``` | OS X 10.6 | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldMoveItemAtPath: String, toPath: String) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldMoveItemAtPath srcPath: String!, toPath dstPath: String!) -> Bool ``` | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldMoveItemAtPath srcPath: String, toPath dstPath: String) -> Bool ``` | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldMoveItemAtURL: NSURL, toURL: NSURL) -> Bool

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldMoveItemAtURL srcURL: NSURL!, toURL dstURL: NSURL!) -> Bool ``` | OS X 10.10 | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldMoveItemAtURL srcURL: NSURL, toURL dstURL: NSURL) -> Bool ``` | OS X 10.6 | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldProceedAfterError: NSError, copyingItemAtPath: String, toPath: String) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldProceedAfterError error: NSError!, copyingItemAtPath srcPath: String!, toPath dstPath: String!) -> Bool ``` | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldProceedAfterError error: NSError, copyingItemAtPath srcPath: String, toPath dstPath: String) -> Bool ``` | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldProceedAfterError: NSError, copyingItemAtURL: NSURL, toURL: NSURL) -> Bool

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldProceedAfterError error: NSError!, copyingItemAtURL srcURL: NSURL!, toURL dstURL: NSURL!) -> Bool ``` | OS X 10.10 | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldProceedAfterError error: NSError, copyingItemAtURL srcURL: NSURL, toURL dstURL: NSURL) -> Bool ``` | OS X 10.6 | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldProceedAfterError: NSError, linkingItemAtPath: String, toPath: String) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldProceedAfterError error: NSError!, linkingItemAtPath srcPath: String!, toPath dstPath: String!) -> Bool ``` | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldProceedAfterError error: NSError, linkingItemAtPath srcPath: String, toPath dstPath: String) -> Bool ``` | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldProceedAfterError: NSError, linkingItemAtURL: NSURL, toURL: NSURL) -> Bool

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldProceedAfterError error: NSError!, linkingItemAtURL srcURL: NSURL!, toURL dstURL: NSURL!) -> Bool ``` | OS X 10.10 | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldProceedAfterError error: NSError, linkingItemAtURL srcURL: NSURL, toURL dstURL: NSURL) -> Bool ``` | OS X 10.6 | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldProceedAfterError: NSError, movingItemAtPath: String, toPath: String) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldProceedAfterError error: NSError!, movingItemAtPath srcPath: String!, toPath dstPath: String!) -> Bool ``` | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldProceedAfterError error: NSError, movingItemAtPath srcPath: String, toPath dstPath: String) -> Bool ``` | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldProceedAfterError: NSError, movingItemAtURL: NSURL, toURL: NSURL) -> Bool

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldProceedAfterError error: NSError!, movingItemAtURL srcURL: NSURL!, toURL dstURL: NSURL!) -> Bool ``` | OS X 10.10 | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldProceedAfterError error: NSError, movingItemAtURL srcURL: NSURL, toURL dstURL: NSURL) -> Bool ``` | OS X 10.6 | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldProceedAfterError: NSError, removingItemAtPath: String) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldProceedAfterError error: NSError!, removingItemAtPath path: String!) -> Bool ``` | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldProceedAfterError error: NSError, removingItemAtPath path: String) -> Bool ``` | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldProceedAfterError: NSError, removingItemAtURL: NSURL) -> Bool

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldProceedAfterError error: NSError!, removingItemAtURL URL: NSURL!) -> Bool ``` | OS X 10.10 | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldProceedAfterError error: NSError, removingItemAtURL URL: NSURL) -> Bool ``` | OS X 10.6 | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldRemoveItemAtPath: String) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldRemoveItemAtPath path: String!) -> Bool ``` | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldRemoveItemAtPath path: String) -> Bool ``` | yes |

Modified NSFileManagerDelegate.fileManager(NSFileManager, shouldRemoveItemAtURL: NSURL) -> Bool

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func fileManager(_ fileManager: NSFileManager!, shouldRemoveItemAtURL URL: NSURL!) -> Bool ``` | OS X 10.10 | -- |
| To | ``` optional func fileManager(_ fileManager: NSFileManager, shouldRemoveItemAtURL URL: NSURL) -> Bool ``` | OS X 10.6 | yes |

Modified NSFileManagerItemReplacementOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct NSFileManagerItemReplacementOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var UsingNewMetadataOnly: NSFileManagerItemReplacementOptions { get }     static var WithoutDeletingBackupItem: NSFileManagerItemReplacementOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct NSFileManagerItemReplacementOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var UsingNewMetadataOnly: NSFileManagerItemReplacementOptions { get }     static var WithoutDeletingBackupItem: NSFileManagerItemReplacementOptions { get } } ``` | RawOptionSetType | OS X 10.6 |

Modified NSFileManagerItemReplacementOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFilePresenter.accommodatePresentedItemDeletionWithCompletionHandler((NSError!) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func accommodatePresentedItemDeletionWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!) ``` | -- |
| To | ``` optional func accommodatePresentedItemDeletionWithCompletionHandler(_ completionHandler: (NSError!) -> Void) ``` | yes |

Modified NSFilePresenter.accommodatePresentedSubitemDeletionAtURL(NSURL, completionHandler:(NSError!) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func accommodatePresentedSubitemDeletionAtURL(_ url: NSURL!, completionHandler completionHandler: ((NSError!) -> Void)!) ``` | -- |
| To | ``` optional func accommodatePresentedSubitemDeletionAtURL(_ url: NSURL, completionHandler completionHandler: (NSError!) -> Void) ``` | yes |

Modified NSFilePresenter.presentedItemDidChange()

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified NSFilePresenter.presentedItemDidGainVersion(NSFileVersion)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func presentedItemDidGainVersion(_ version: NSFileVersion!) ``` | -- |
| To | ``` optional func presentedItemDidGainVersion(_ version: NSFileVersion) ``` | yes |

Modified NSFilePresenter.presentedItemDidLoseVersion(NSFileVersion)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func presentedItemDidLoseVersion(_ version: NSFileVersion!) ``` | -- |
| To | ``` optional func presentedItemDidLoseVersion(_ version: NSFileVersion) ``` | yes |

Modified NSFilePresenter.presentedItemDidMoveToURL(NSURL)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func presentedItemDidMoveToURL(_ newURL: NSURL!) ``` | -- |
| To | ``` optional func presentedItemDidMoveToURL(_ newURL: NSURL) ``` | yes |

Modified NSFilePresenter.presentedItemDidResolveConflictVersion(NSFileVersion)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func presentedItemDidResolveConflictVersion(_ version: NSFileVersion!) ``` | -- |
| To | ``` optional func presentedItemDidResolveConflictVersion(_ version: NSFileVersion) ``` | yes |

Modified NSFilePresenter.presentedItemOperationQueue

|  | Declaration |
| --- | --- |
| From | ``` var presentedItemOperationQueue: NSOperationQueue! { get } ``` |
| To | ``` var presentedItemOperationQueue: NSOperationQueue { get } ``` |

Modified NSFilePresenter.presentedItemURL

|  | Declaration |
| --- | --- |
| From | ``` var presentedItemURL: NSURL! { get } ``` |
| To | ``` @NSCopying var presentedItemURL: NSURL? { get } ``` |

Modified NSFilePresenter.presentedSubitemAtURL(NSURL, didGainVersion: NSFileVersion)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func presentedSubitemAtURL(_ url: NSURL!, didGainVersion version: NSFileVersion!) ``` | -- |
| To | ``` optional func presentedSubitemAtURL(_ url: NSURL, didGainVersion version: NSFileVersion) ``` | yes |

Modified NSFilePresenter.presentedSubitemAtURL(NSURL, didLoseVersion: NSFileVersion)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func presentedSubitemAtURL(_ url: NSURL!, didLoseVersion version: NSFileVersion!) ``` | -- |
| To | ``` optional func presentedSubitemAtURL(_ url: NSURL, didLoseVersion version: NSFileVersion) ``` | yes |

Modified NSFilePresenter.presentedSubitemAtURL(NSURL, didMoveToURL: NSURL)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func presentedSubitemAtURL(_ oldURL: NSURL!, didMoveToURL newURL: NSURL!) ``` | -- |
| To | ``` optional func presentedSubitemAtURL(_ oldURL: NSURL, didMoveToURL newURL: NSURL) ``` | yes |

Modified NSFilePresenter.presentedSubitemAtURL(NSURL, didResolveConflictVersion: NSFileVersion)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func presentedSubitemAtURL(_ url: NSURL!, didResolveConflictVersion version: NSFileVersion!) ``` | -- |
| To | ``` optional func presentedSubitemAtURL(_ url: NSURL, didResolveConflictVersion version: NSFileVersion) ``` | yes |

Modified NSFilePresenter.presentedSubitemDidAppearAtURL(NSURL)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func presentedSubitemDidAppearAtURL(_ url: NSURL!) ``` | -- |
| To | ``` optional func presentedSubitemDidAppearAtURL(_ url: NSURL) ``` | yes |

Modified NSFilePresenter.presentedSubitemDidChangeAtURL(NSURL)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func presentedSubitemDidChangeAtURL(_ url: NSURL!) ``` | -- |
| To | ``` optional func presentedSubitemDidChangeAtURL(_ url: NSURL) ``` | yes |

Modified NSFilePresenter.primaryPresentedItemURL

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional var primaryPresentedItemURL: NSURL! { get } ``` | OS X 10.10 | -- |
| To | ``` @NSCopying optional var primaryPresentedItemURL: NSURL? { get } ``` | OS X 10.8 | yes |

Modified NSFilePresenter.relinquishPresentedItemToReader(((() -> Void)!) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func relinquishPresentedItemToReader(_ reader: (((() -> Void)!) -> Void)!) ``` | -- |
| To | ``` optional func relinquishPresentedItemToReader(_ reader: ((() -> Void)!) -> Void) ``` | yes |

Modified NSFilePresenter.relinquishPresentedItemToWriter(((() -> Void)!) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func relinquishPresentedItemToWriter(_ writer: (((() -> Void)!) -> Void)!) ``` | -- |
| To | ``` optional func relinquishPresentedItemToWriter(_ writer: ((() -> Void)!) -> Void) ``` | yes |

Modified NSFilePresenter.savePresentedItemChangesWithCompletionHandler((NSError!) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func savePresentedItemChangesWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!) ``` | -- |
| To | ``` optional func savePresentedItemChangesWithCompletionHandler(_ completionHandler: (NSError!) -> Void) ``` | yes |

Modified NSFileSecurity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSFileSecurity.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSFileVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSFileVersion.URL

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL { get } ``` |

Modified NSFileVersion.addVersionOfItemAtURL(NSURL, withContentsOfURL: NSURL, options: NSFileVersionAddingOptions, error: NSErrorPointer) -> NSFileVersion? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func addVersionOfItemAtURL(_ url: NSURL!, withContentsOfURL contentsURL: NSURL!, options options: NSFileVersionAddingOptions, error outError: NSErrorPointer) -> NSFileVersion! ``` | OS X 10.10 |
| To | ``` class func addVersionOfItemAtURL(_ url: NSURL, withContentsOfURL contentsURL: NSURL, options options: NSFileVersionAddingOptions, error outError: NSErrorPointer) -> NSFileVersion? ``` | OS X 10.7 |

Modified NSFileVersion.currentVersionOfItemAtURL(NSURL) -> NSFileVersion? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func currentVersionOfItemAtURL(_ url: NSURL!) -> NSFileVersion! ``` |
| To | ``` class func currentVersionOfItemAtURL(_ url: NSURL) -> NSFileVersion? ``` |

Modified NSFileVersion.discardable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSFileVersion.getNonlocalVersionsOfItemAtURL(NSURL, completionHandler:([AnyObject]!, NSError!) -> Void) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func getNonlocalVersionsOfItemAtURL(_ url: NSURL!, completionHandler completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` class func getNonlocalVersionsOfItemAtURL(_ url: NSURL, completionHandler completionHandler: ([AnyObject]!, NSError!) -> Void) ``` |

Modified NSFileVersion.localizedName

|  | Declaration |
| --- | --- |
| From | ``` var localizedName: String! { get } ``` |
| To | ``` var localizedName: String? { get } ``` |

Modified NSFileVersion.localizedNameOfSavingComputer

|  | Declaration |
| --- | --- |
| From | ``` var localizedNameOfSavingComputer: String! { get } ``` |
| To | ``` var localizedNameOfSavingComputer: String? { get } ``` |

Modified NSFileVersion.modificationDate

|  | Declaration |
| --- | --- |
| From | ``` var modificationDate: NSDate! { get } ``` |
| To | ``` @NSCopying var modificationDate: NSDate? { get } ``` |

Modified NSFileVersion.init(ofItemAtURL: NSURL, forPersistentIdentifier: AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` init(ofItemAtURL url: NSURL!, forPersistentIdentifier persistentIdentifier: AnyObject!) -> NSFileVersion ``` |
| To | ``` init?(ofItemAtURL url: NSURL, forPersistentIdentifier persistentIdentifier: AnyObject) -> NSFileVersion ``` |

Modified NSFileVersion.otherVersionsOfItemAtURL(NSURL) -> [AnyObject]? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func otherVersionsOfItemAtURL(_ url: NSURL!) -> [AnyObject]! ``` |
| To | ``` class func otherVersionsOfItemAtURL(_ url: NSURL) -> [AnyObject]? ``` |

Modified NSFileVersion.persistentIdentifier

|  | Declaration |
| --- | --- |
| From | ``` var persistentIdentifier: NSCoding! { get } ``` |
| To | ``` var persistentIdentifier: NSCoding { get } ``` |

Modified NSFileVersion.removeOtherVersionsOfItemAtURL(NSURL, error: NSErrorPointer) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func removeOtherVersionsOfItemAtURL(_ url: NSURL!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` class func removeOtherVersionsOfItemAtURL(_ url: NSURL, error outError: NSErrorPointer) -> Bool ``` |

Modified NSFileVersion.replaceItemAtURL(NSURL, options: NSFileVersionReplacingOptions, error: NSErrorPointer) -> NSURL?

|  | Declaration |
| --- | --- |
| From | ``` func replaceItemAtURL(_ url: NSURL!, options options: NSFileVersionReplacingOptions, error error: NSErrorPointer) -> NSURL! ``` |
| To | ``` func replaceItemAtURL(_ url: NSURL, options options: NSFileVersionReplacingOptions, error error: NSErrorPointer) -> NSURL? ``` |

Modified NSFileVersion.temporaryDirectoryURLForNewVersionOfItemAtURL(NSURL) -> NSURL [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func temporaryDirectoryURLForNewVersionOfItemAtURL(_ url: NSURL!) -> NSURL! ``` | OS X 10.10 |
| To | ``` class func temporaryDirectoryURLForNewVersionOfItemAtURL(_ url: NSURL) -> NSURL ``` | OS X 10.7 |

Modified NSFileVersion.unresolvedConflictVersionsOfItemAtURL(NSURL) -> [AnyObject]? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func unresolvedConflictVersionsOfItemAtURL(_ url: NSURL!) -> [AnyObject]! ``` |
| To | ``` class func unresolvedConflictVersionsOfItemAtURL(_ url: NSURL) -> [AnyObject]? ``` |

Modified NSFileVersionAddingOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSFileVersionAddingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var ByMoving: NSFileVersionAddingOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSFileVersionAddingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ByMoving: NSFileVersionAddingOptions { get } } ``` | RawOptionSetType |

Modified NSFileVersionAddingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFileVersionReplacingOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSFileVersionReplacingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var ByMoving: NSFileVersionReplacingOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSFileVersionReplacingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ByMoving: NSFileVersionReplacingOptions { get } } ``` | RawOptionSetType |

Modified NSFileVersionReplacingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFileWrapper

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified NSFileWrapper.init(URL: NSURL, options: NSFileWrapperReadingOptions, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(URL url: NSURL!, options options: NSFileWrapperReadingOptions, error outError: NSErrorPointer) ``` | OS X 10.10 |
| To | ``` init?(URL url: NSURL, options options: NSFileWrapperReadingOptions, error outError: NSErrorPointer) ``` | OS X 10.6 |

Modified NSFileWrapper.addFileWithPath(String) -> String

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func addFileWithPath(_ path: String!) -> String! ``` | OS X 10.10 | -- |
| To | ``` func addFileWithPath(_ path: String) -> String ``` | OS X 10.0 | OS X 10.10 |

Modified NSFileWrapper.addFileWrapper(NSFileWrapper) -> String

|  | Declaration |
| --- | --- |
| From | ``` func addFileWrapper(_ child: NSFileWrapper!) -> String! ``` |
| To | ``` func addFileWrapper(_ child: NSFileWrapper) -> String ``` |

Modified NSFileWrapper.addRegularFileWithContents(NSData, preferredFilename: String) -> String

|  | Declaration |
| --- | --- |
| From | ``` func addRegularFileWithContents(_ data: NSData!, preferredFilename fileName: String!) -> String! ``` |
| To | ``` func addRegularFileWithContents(_ data: NSData, preferredFilename fileName: String) -> String ``` |

Modified NSFileWrapper.addSymbolicLinkWithDestination(String, preferredFilename: String) -> String

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func addSymbolicLinkWithDestination(_ path: String!, preferredFilename filename: String!) -> String! ``` | OS X 10.10 | -- |
| To | ``` func addSymbolicLinkWithDestination(_ path: String, preferredFilename filename: String) -> String ``` | OS X 10.0 | OS X 10.10 |

Modified NSFileWrapper.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder inCoder: NSCoder!) ``` |
| To | ``` init?(coder inCoder: NSCoder) ``` |

Modified NSFileWrapper.init(directoryWithFileWrappers: [NSObject: AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` init(directoryWithFileWrappers childrenByPreferredName: [NSObject : AnyObject]!) ``` |
| To | ``` init(directoryWithFileWrappers childrenByPreferredName: [NSObject : AnyObject]) ``` |

Modified NSFileWrapper.fileAttributes

|  | Declaration |
| --- | --- |
| From | ``` var fileAttributes: [NSObject : AnyObject]! ``` |
| To | ``` var fileAttributes: [NSObject : AnyObject] ``` |

Modified NSFileWrapper.fileWrappers

|  | Declaration |
| --- | --- |
| From | ``` var fileWrappers: [NSObject : AnyObject]! { get } ``` |
| To | ``` var fileWrappers: [NSObject : AnyObject] { get } ``` |

Modified NSFileWrapper.filename

|  | Declaration |
| --- | --- |
| From | ``` var filename: String! ``` |
| To | ``` var filename: String? ``` |

Modified NSFileWrapper.keyForFileWrapper(NSFileWrapper) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func keyForFileWrapper(_ child: NSFileWrapper!) -> String! ``` |
| To | ``` func keyForFileWrapper(_ child: NSFileWrapper) -> String? ``` |

Modified NSFileWrapper.matchesContentsOfURL(NSURL) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func matchesContentsOfURL(_ url: NSURL!) -> Bool ``` | OS X 10.10 |
| To | ``` func matchesContentsOfURL(_ url: NSURL) -> Bool ``` | OS X 10.6 |

Modified NSFileWrapper.needsToBeUpdatedFromPath(String) -> Bool

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func needsToBeUpdatedFromPath(_ path: String!) -> Bool ``` | OS X 10.10 | -- |
| To | ``` func needsToBeUpdatedFromPath(_ path: String) -> Bool ``` | OS X 10.0 | OS X 10.10 |

Modified NSFileWrapper.init(path: String)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` convenience init(path path: String!) ``` | OS X 10.10 | -- |
| To | ``` convenience init?(path path: String) ``` | OS X 10.0 | OS X 10.10 |

Modified NSFileWrapper.preferredFilename

|  | Declaration |
| --- | --- |
| From | ``` var preferredFilename: String! ``` |
| To | ``` var preferredFilename: String ``` |

Modified NSFileWrapper.readFromURL(NSURL, options: NSFileWrapperReadingOptions, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func readFromURL(_ url: NSURL!, options options: NSFileWrapperReadingOptions, error outError: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func readFromURL(_ url: NSURL, options options: NSFileWrapperReadingOptions, error outError: NSErrorPointer) -> Bool ``` | OS X 10.6 |

Modified NSFileWrapper.regularFileContents

|  | Declaration |
| --- | --- |
| From | ``` var regularFileContents: NSData! { get } ``` |
| To | ``` @NSCopying var regularFileContents: NSData? { get } ``` |

Modified NSFileWrapper.init(regularFileWithContents: NSData)

|  | Declaration |
| --- | --- |
| From | ``` init(regularFileWithContents contents: NSData!) ``` |
| To | ``` init(regularFileWithContents contents: NSData) ``` |

Modified NSFileWrapper.removeFileWrapper(NSFileWrapper)

|  | Declaration |
| --- | --- |
| From | ``` func removeFileWrapper(_ child: NSFileWrapper!) ``` |
| To | ``` func removeFileWrapper(_ child: NSFileWrapper) ``` |

Modified NSFileWrapper.serializedRepresentation

|  | Declaration |
| --- | --- |
| From | ``` var serializedRepresentation: NSData! { get } ``` |
| To | ``` @NSCopying var serializedRepresentation: NSData { get } ``` |

Modified NSFileWrapper.init(serializedRepresentation: NSData)

|  | Declaration |
| --- | --- |
| From | ``` init(serializedRepresentation serializeRepresentation: NSData!) ``` |
| To | ``` init?(serializedRepresentation serializeRepresentation: NSData) ``` |

Modified NSFileWrapper.symbolicLinkDestination() -> String

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func symbolicLinkDestination() -> String! ``` | OS X 10.10 | -- |
| To | ``` func symbolicLinkDestination() -> String ``` | OS X 10.0 | OS X 10.10 |

Modified NSFileWrapper.symbolicLinkDestinationURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var symbolicLinkDestinationURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var symbolicLinkDestinationURL: NSURL { get } ``` | OS X 10.6 |

Modified NSFileWrapper.init(symbolicLinkWithDestination: String)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` convenience init(symbolicLinkWithDestination path: String!) ``` | OS X 10.10 | -- |
| To | ``` convenience init(symbolicLinkWithDestination path: String) ``` | OS X 10.0 | OS X 10.10 |

Modified NSFileWrapper.init(symbolicLinkWithDestinationURL: NSURL)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(symbolicLinkWithDestinationURL url: NSURL!) ``` | OS X 10.10 |
| To | ``` init(symbolicLinkWithDestinationURL url: NSURL) ``` | OS X 10.6 |

Modified NSFileWrapper.updateFromPath(String) -> Bool

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func updateFromPath(_ path: String!) -> Bool ``` | OS X 10.10 | -- |
| To | ``` func updateFromPath(_ path: String) -> Bool ``` | OS X 10.0 | OS X 10.10 |

Modified NSFileWrapper.writeToFile(String, atomically: Bool, updateFilenames: Bool) -> Bool

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func writeToFile(_ path: String!, atomically atomicFlag: Bool, updateFilenames updateFilenamesFlag: Bool) -> Bool ``` | OS X 10.10 | -- |
| To | ``` func writeToFile(_ path: String, atomically atomicFlag: Bool, updateFilenames updateFilenamesFlag: Bool) -> Bool ``` | OS X 10.0 | OS X 10.10 |

Modified NSFileWrapper.writeToURL(NSURL, options: NSFileWrapperWritingOptions, originalContentsURL: NSURL?, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func writeToURL(_ url: NSURL!, options options: NSFileWrapperWritingOptions, originalContentsURL originalContentsURL: NSURL!, error outError: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func writeToURL(_ url: NSURL, options options: NSFileWrapperWritingOptions, originalContentsURL originalContentsURL: NSURL?, error outError: NSErrorPointer) -> Bool ``` | OS X 10.6 |

Modified NSFileWrapperReadingOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct NSFileWrapperReadingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Immediate: NSFileWrapperReadingOptions { get }     static var WithoutMapping: NSFileWrapperReadingOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct NSFileWrapperReadingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Immediate: NSFileWrapperReadingOptions { get }     static var WithoutMapping: NSFileWrapperReadingOptions { get } } ``` | RawOptionSetType | OS X 10.6 |

Modified NSFileWrapperReadingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFileWrapperWritingOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct NSFileWrapperWritingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Atomic: NSFileWrapperWritingOptions { get }     static var WithNameUpdating: NSFileWrapperWritingOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct NSFileWrapperWritingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Atomic: NSFileWrapperWritingOptions { get }     static var WithNameUpdating: NSFileWrapperWritingOptions { get } } ``` | RawOptionSetType | OS X 10.6 |

Modified NSFileWrapperWritingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFormatter.attributedStringForObjectValue(AnyObject, withDefaultAttributes:[NSObject: AnyObject]?) -> NSAttributedString?

|  | Declaration |
| --- | --- |
| From | ``` func attributedStringForObjectValue(_ obj: AnyObject!, withDefaultAttributes attrs: [NSObject : AnyObject]!) -> NSAttributedString! ``` |
| To | ``` func attributedStringForObjectValue(_ obj: AnyObject, withDefaultAttributes attrs: [NSObject : AnyObject]?) -> NSAttributedString? ``` |

Modified NSFormatter.editingStringForObjectValue(AnyObject) -> String

|  | Declaration |
| --- | --- |
| From | ``` func editingStringForObjectValue(_ obj: AnyObject!) -> String! ``` |
| To | ``` func editingStringForObjectValue(_ obj: AnyObject) -> String ``` |

Modified NSFormatter.getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forString: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getObjectValue(_ obj: AutoreleasingUnsafePointer<AnyObject?>, forString string: String!, errorDescription error: AutoreleasingUnsafePointer<NSString?>) -> Bool ``` |
| To | ``` func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool ``` |

Modified NSFormatter.isPartialStringValid(AutoreleasingUnsafeMutablePointer<NSString?>, proposedSelectedRange: NSRangePointer, originalString: String, originalSelectedRange: NSRange, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isPartialStringValid(_ partialStringPtr: AutoreleasingUnsafePointer<NSString?>, proposedSelectedRange proposedSelRangePtr: NSRangePointer, originalString origString: String!, originalSelectedRange origSelRange: NSRange, errorDescription error: AutoreleasingUnsafePointer<NSString?>) -> Bool ``` |
| To | ``` func isPartialStringValid(_ partialStringPtr: AutoreleasingUnsafeMutablePointer<NSString?>, proposedSelectedRange proposedSelRangePtr: NSRangePointer, originalString origString: String, originalSelectedRange origSelRange: NSRange, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool ``` |

Modified NSFormatter.isPartialStringValid(String, newEditingString: AutoreleasingUnsafeMutablePointer<NSString?>, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isPartialStringValid(_ partialString: String!, newEditingString newString: AutoreleasingUnsafePointer<NSString?>, errorDescription error: AutoreleasingUnsafePointer<NSString?>) -> Bool ``` |
| To | ``` func isPartialStringValid(_ partialString: String, newEditingString newString: AutoreleasingUnsafeMutablePointer<NSString?>, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool ``` |

Modified NSFormatter.stringForObjectValue(AnyObject) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func stringForObjectValue(_ obj: AnyObject!) -> String! ``` |
| To | ``` func stringForObjectValue(_ obj: AnyObject) -> String? ``` |

Modified NSHTTPCookie.comment

|  | Declaration |
| --- | --- |
| From | ``` var comment: String! { get } ``` |
| To | ``` var comment: String? { get } ``` |

Modified NSHTTPCookie.commentURL

|  | Declaration |
| --- | --- |
| From | ``` var commentURL: NSURL! { get } ``` |
| To | ``` @NSCopying var commentURL: NSURL? { get } ``` |

Modified NSHTTPCookie.cookiesWithResponseHeaderFields([NSObject: AnyObject], forURL: NSURL) -> [AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func cookiesWithResponseHeaderFields(_ headerFields: [NSObject : AnyObject]!, forURL URL: NSURL!) -> [AnyObject]! ``` |
| To | ``` class func cookiesWithResponseHeaderFields(_ headerFields: [NSObject : AnyObject], forURL URL: NSURL) -> [AnyObject] ``` |

Modified NSHTTPCookie.domain

|  | Declaration |
| --- | --- |
| From | ``` var domain: String! { get } ``` |
| To | ``` var domain: String { get } ``` |

Modified NSHTTPCookie.expiresDate

|  | Declaration |
| --- | --- |
| From | ``` var expiresDate: NSDate! { get } ``` |
| To | ``` @NSCopying var expiresDate: NSDate! { get } ``` |

Modified NSHTTPCookie.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified NSHTTPCookie.path

|  | Declaration |
| --- | --- |
| From | ``` var path: String! { get } ``` |
| To | ``` var path: String? { get } ``` |

Modified NSHTTPCookie.portList

|  | Declaration |
| --- | --- |
| From | ``` var portList: [AnyObject]! { get } ``` |
| To | ``` var portList: [AnyObject]? { get } ``` |

Modified NSHTTPCookie.properties

|  | Declaration |
| --- | --- |
| From | ``` var properties: [NSObject : AnyObject]! { get } ``` |
| To | ``` var properties: [NSObject : AnyObject]? { get } ``` |

Modified NSHTTPCookie.init(properties: [NSObject: AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` init(properties properties: [NSObject : AnyObject]!) ``` |
| To | ``` init?(properties properties: [NSObject : AnyObject]) ``` |

Modified NSHTTPCookie.requestHeaderFieldsWithCookies([AnyObject]) -> [NSObject: AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func requestHeaderFieldsWithCookies(_ cookies: [AnyObject]!) -> [NSObject : AnyObject]! ``` |
| To | ``` class func requestHeaderFieldsWithCookies(_ cookies: [AnyObject]) -> [NSObject : AnyObject] ``` |

Modified NSHTTPCookie.value

|  | Declaration |
| --- | --- |
| From | ``` var value: String! { get } ``` |
| To | ``` var value: String? { get } ``` |

Modified NSHTTPCookieStorage.cookies

|  | Declaration |
| --- | --- |
| From | ``` var cookies: [AnyObject]! { get } ``` |
| To | ``` var cookies: [AnyObject]? { get } ``` |

Modified NSHTTPCookieStorage.cookiesForURL(NSURL) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func cookiesForURL(_ URL: NSURL!) -> [AnyObject]! ``` |
| To | ``` func cookiesForURL(_ URL: NSURL) -> [AnyObject]? ``` |

Modified NSHTTPCookieStorage.deleteCookie(NSHTTPCookie)

|  | Declaration |
| --- | --- |
| From | ``` func deleteCookie(_ cookie: NSHTTPCookie!) ``` |
| To | ``` func deleteCookie(_ cookie: NSHTTPCookie) ``` |

Modified NSHTTPCookieStorage.getCookiesForTask(NSURLSessionTask, completionHandler:(([AnyObject]!) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func getCookiesForTask(_ task: NSURLSessionTask!, completionHandler completionHandler: (([AnyObject]!) -> Void)!) ``` |
| To | ``` func getCookiesForTask(_ task: NSURLSessionTask, completionHandler completionHandler: (([AnyObject]!) -> Void)!) ``` |

Modified NSHTTPCookieStorage.removeCookiesSinceDate(NSDate)

|  | Declaration |
| --- | --- |
| From | ``` func removeCookiesSinceDate(_ date: NSDate!) ``` |
| To | ``` func removeCookiesSinceDate(_ date: NSDate) ``` |

Modified NSHTTPCookieStorage.setCookie(NSHTTPCookie)

|  | Declaration |
| --- | --- |
| From | ``` func setCookie(_ cookie: NSHTTPCookie!) ``` |
| To | ``` func setCookie(_ cookie: NSHTTPCookie) ``` |

Modified NSHTTPCookieStorage.setCookies([AnyObject], forURL: NSURL?, mainDocumentURL: NSURL?)

|  | Declaration |
| --- | --- |
| From | ``` func setCookies(_ cookies: [AnyObject]!, forURL URL: NSURL!, mainDocumentURL mainDocumentURL: NSURL!) ``` |
| To | ``` func setCookies(_ cookies: [AnyObject], forURL URL: NSURL?, mainDocumentURL mainDocumentURL: NSURL?) ``` |

Modified NSHTTPCookieStorage.sharedHTTPCookieStorage() -> NSHTTPCookieStorage [class]

|  | Declaration |
| --- | --- |
| From | ``` class func sharedHTTPCookieStorage() -> NSHTTPCookieStorage! ``` |
| To | ``` class func sharedHTTPCookieStorage() -> NSHTTPCookieStorage ``` |

Modified NSHTTPCookieStorage.sortedCookiesUsingDescriptors([AnyObject]) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sortedCookiesUsingDescriptors(_ sortOrder: [AnyObject]!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func sortedCookiesUsingDescriptors(_ sortOrder: [AnyObject]) -> [AnyObject] ``` | OS X 10.7 |

Modified NSHTTPCookieStorage.storeCookies([AnyObject], forTask: NSURLSessionTask)

|  | Declaration |
| --- | --- |
| From | ``` func storeCookies(_ cookies: [AnyObject]!, forTask task: NSURLSessionTask!) ``` |
| To | ``` func storeCookies(_ cookies: [AnyObject], forTask task: NSURLSessionTask) ``` |

Modified NSHTTPURLResponse.init(URL: NSURL, statusCode: Int, HTTPVersion: String?, headerFields:[NSObject: AnyObject]?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(URL url: NSURL!, statusCode statusCode: Int, HTTPVersion HTTPVersion: String!, headerFields headerFields: [NSObject : AnyObject]!) ``` | OS X 10.10 |
| To | ``` init?(URL url: NSURL, statusCode statusCode: Int, HTTPVersion HTTPVersion: String?, headerFields headerFields: [NSObject : AnyObject]?) ``` | OS X 10.7 |

Modified NSHTTPURLResponse.allHeaderFields

|  | Declaration |
| --- | --- |
| From | ``` var allHeaderFields: [NSObject : AnyObject]! { get } ``` |
| To | ``` var allHeaderFields: [NSObject : AnyObject] { get } ``` |

Modified NSHTTPURLResponse.localizedStringForStatusCode(Int) -> String [class]

|  | Declaration |
| --- | --- |
| From | ``` class func localizedStringForStatusCode(_ statusCode: Int) -> String! ``` |
| To | ``` class func localizedStringForStatusCode(_ statusCode: Int) -> String ``` |

Modified NSHashEnumerator [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSHashEnumerator {     var _pi: Int     var _si: Int     var _bs: UnsafePointer<()> } ``` |
| To | ``` struct NSHashEnumerator {     var _pi: Int     var _si: Int     var _bs: UnsafeMutablePointer<Void>     init()     init(_pi _pi: Int, _si _si: Int, _bs _bs: UnsafeMutablePointer<Void>) } ``` |

Modified NSHashTable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSHashTable.addObject(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func addObject(_ object: AnyObject!) ``` |
| To | ``` func addObject(_ object: AnyObject) ``` |

Modified NSHashTable.allObjects

|  | Declaration |
| --- | --- |
| From | ``` var allObjects: [AnyObject]! { get } ``` |
| To | ``` var allObjects: [AnyObject] { get } ``` |

Modified NSHashTable.anyObject

|  | Declaration |
| --- | --- |
| From | ``` var anyObject: AnyObject! { get } ``` |
| To | ``` var anyObject: AnyObject? { get } ``` |

Modified NSHashTable.containsObject(AnyObject) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func containsObject(_ anObject: AnyObject!) -> Bool ``` |
| To | ``` func containsObject(_ anObject: AnyObject) -> Bool ``` |

Modified NSHashTable.intersectHashTable(NSHashTable)

|  | Declaration |
| --- | --- |
| From | ``` func intersectHashTable(_ other: NSHashTable!) ``` |
| To | ``` func intersectHashTable(_ other: NSHashTable) ``` |

Modified NSHashTable.intersectsHashTable(NSHashTable) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func intersectsHashTable(_ other: NSHashTable!) -> Bool ``` |
| To | ``` func intersectsHashTable(_ other: NSHashTable) -> Bool ``` |

Modified NSHashTable.isEqualToHashTable(NSHashTable) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToHashTable(_ other: NSHashTable!) -> Bool ``` |
| To | ``` func isEqualToHashTable(_ other: NSHashTable) -> Bool ``` |

Modified NSHashTable.isSubsetOfHashTable(NSHashTable) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isSubsetOfHashTable(_ other: NSHashTable!) -> Bool ``` |
| To | ``` func isSubsetOfHashTable(_ other: NSHashTable) -> Bool ``` |

Modified NSHashTable.member(AnyObject) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func member(_ object: AnyObject!) -> AnyObject! ``` |
| To | ``` func member(_ object: AnyObject) -> AnyObject? ``` |

Modified NSHashTable.minusHashTable(NSHashTable)

|  | Declaration |
| --- | --- |
| From | ``` func minusHashTable(_ other: NSHashTable!) ``` |
| To | ``` func minusHashTable(_ other: NSHashTable) ``` |

Modified NSHashTable.objectEnumerator() -> NSEnumerator

|  | Declaration |
| --- | --- |
| From | ``` func objectEnumerator() -> NSEnumerator! ``` |
| To | ``` func objectEnumerator() -> NSEnumerator ``` |

Modified NSHashTable.pointerFunctions

|  | Declaration |
| --- | --- |
| From | ``` var pointerFunctions: NSPointerFunctions! { get } ``` |
| To | ``` @NSCopying var pointerFunctions: NSPointerFunctions { get } ``` |

Modified NSHashTable.init(pointerFunctions: NSPointerFunctions, capacity: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(pointerFunctions functions: NSPointerFunctions!, capacity initialCapacity: Int) ``` |
| To | ``` init(pointerFunctions functions: NSPointerFunctions, capacity initialCapacity: Int) ``` |

Modified NSHashTable.removeObject(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func removeObject(_ object: AnyObject!) ``` |
| To | ``` func removeObject(_ object: AnyObject) ``` |

Modified NSHashTable.setRepresentation

|  | Declaration |
| --- | --- |
| From | ``` var setRepresentation: NSSet! { get } ``` |
| To | ``` var setRepresentation: Set<NSObject> { get } ``` |

Modified NSHashTable.unionHashTable(NSHashTable)

|  | Declaration |
| --- | --- |
| From | ``` func unionHashTable(_ other: NSHashTable!) ``` |
| To | ``` func unionHashTable(_ other: NSHashTable) ``` |

Modified NSHashTable.weakObjectsHashTable() -> NSHashTable [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func weakObjectsHashTable() -> NSHashTable! ``` | OS X 10.10 |
| To | ``` class func weakObjectsHashTable() -> NSHashTable ``` | OS X 10.8 |

Modified NSHashTableCallBacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSHashTableCallBacks {     var hash: CFunctionPointer<((NSHashTable!, ConstUnsafePointer<()>) -> Int)>     var isEqual: CFunctionPointer<((NSHashTable!, ConstUnsafePointer<()>, ConstUnsafePointer<()>) -> Bool)>     var retain: CFunctionPointer<((NSHashTable!, ConstUnsafePointer<()>) -> Void)>     var release: CFunctionPointer<((NSHashTable!, UnsafePointer<()>) -> Void)>     var describe: CFunctionPointer<((NSHashTable!, ConstUnsafePointer<()>) -> String!)> } ``` |
| To | ``` struct NSHashTableCallBacks {     var hash: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>) -> Int)>     var isEqual: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>, UnsafePointer<Void>) -> Bool)>     var retain: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>) -> Void)>     var release: CFunctionPointer<((NSHashTable!, UnsafeMutablePointer<Void>) -> Void)>     var describe: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>) -> String!)>     init()     init(hash hash: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>) -> Int)>, isEqual isEqual: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>, UnsafePointer<Void>) -> Bool)>, retain retain: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>) -> Void)>, release release: CFunctionPointer<((NSHashTable!, UnsafeMutablePointer<Void>) -> Void)>, describe describe: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>) -> String!)>) } ``` |

Modified NSHashTableCallBacks.describe

|  | Declaration |
| --- | --- |
| From | ``` var describe: CFunctionPointer<((NSHashTable!, ConstUnsafePointer<()>) -> String!)> ``` |
| To | ``` var describe: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>) -> String!)> ``` |

Modified NSHashTableCallBacks.hash

|  | Declaration |
| --- | --- |
| From | ``` var hash: CFunctionPointer<((NSHashTable!, ConstUnsafePointer<()>) -> Int)> ``` |
| To | ``` var hash: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>) -> Int)> ``` |

Modified NSHashTableCallBacks.isEqual

|  | Declaration |
| --- | --- |
| From | ``` var isEqual: CFunctionPointer<((NSHashTable!, ConstUnsafePointer<()>, ConstUnsafePointer<()>) -> Bool)> ``` |
| To | ``` var isEqual: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>, UnsafePointer<Void>) -> Bool)> ``` |

Modified NSHashTableCallBacks.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((NSHashTable!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((NSHashTable!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified NSHashTableCallBacks.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((NSHashTable!, ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var retain: CFunctionPointer<((NSHashTable!, UnsafePointer<Void>) -> Void)> ``` |

Modified NSHost.address

|  | Declaration |
| --- | --- |
| From | ``` var address: String! { get } ``` |
| To | ``` var address: String? { get } ``` |

Modified NSHost.init(address: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(address address: String!) ``` |
| To | ``` convenience init(address address: String) ``` |

Modified NSHost.currentHost() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func currentHost() -> Self! ``` | OS X 10.10 |
| To | ``` class func currentHost() -> Self ``` | OS X 10.10.3 |

Modified NSHost.isEqualToHost(NSHost) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToHost(_ aHost: NSHost!) -> Bool ``` |
| To | ``` func isEqualToHost(_ aHost: NSHost) -> Bool ``` |

Modified NSHost.localizedName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var localizedName: String! { get } ``` | OS X 10.10 |
| To | ``` var localizedName: String? { get } ``` | OS X 10.6 |

Modified NSHost.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String? { get } ``` |

Modified NSHost.init(name: String?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(name name: String!) ``` |
| To | ``` convenience init(name name: String?) ``` |

Modified NSHost.names

|  | Declaration |
| --- | --- |
| From | ``` var names: [AnyObject]! { get } ``` |
| To | ``` var names: [AnyObject] { get } ``` |

Modified NSIndexPath.compare(NSIndexPath) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func compare(_ otherObject: NSIndexPath!) -> NSComparisonResult ``` |
| To | ``` func compare(_ otherObject: NSIndexPath) -> NSComparisonResult ``` |

Modified NSIndexPath.getIndexes(UnsafeMutablePointer<Int>)

|  | Declaration |
| --- | --- |
| From | ``` func getIndexes(_ indexes: UnsafePointer<Int>) ``` |
| To | ``` func getIndexes(_ indexes: UnsafeMutablePointer<Int>) ``` |

Modified NSIndexPath.indexPathByAddingIndex(Int) -> NSIndexPath

|  | Declaration |
| --- | --- |
| From | ``` func indexPathByAddingIndex(_ index: Int) -> NSIndexPath! ``` |
| To | ``` func indexPathByAddingIndex(_ index: Int) -> NSIndexPath ``` |

Modified NSIndexPath.indexPathByRemovingLastIndex() -> NSIndexPath

|  | Declaration |
| --- | --- |
| From | ``` func indexPathByRemovingLastIndex() -> NSIndexPath! ``` |
| To | ``` func indexPathByRemovingLastIndex() -> NSIndexPath ``` |

Modified NSIndexPath.init(indexes: UnsafePointer<Int>, length: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(indexes indexes: ConstUnsafePointer<Int>, length length: Int) ``` |
| To | ``` init(indexes indexes: UnsafePointer<Int>, length length: Int) ``` |

Modified NSIndexSet

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding, SequenceType |

Modified NSIndexSet.containsIndexes(NSIndexSet) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func containsIndexes(_ indexSet: NSIndexSet!) -> Bool ``` |
| To | ``` func containsIndexes(_ indexSet: NSIndexSet) -> Bool ``` |

Modified NSIndexSet.countOfIndexesInRange(NSRange) -> Int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSIndexSet.enumerateIndexesInRange(NSRange, options: NSEnumerationOptions, usingBlock:((Int, UnsafeMutablePointer<ObjCBool>) -> Void)?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateIndexesInRange(_ range: NSRange, options opts: NSEnumerationOptions, usingBlock block: ((Int, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateIndexesInRange(_ range: NSRange, options opts: NSEnumerationOptions, usingBlock block: ((Int, UnsafeMutablePointer<ObjCBool>) -> Void)?) ``` | OS X 10.6 |

Modified NSIndexSet.enumerateIndexesUsingBlock((Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateIndexesUsingBlock(_ block: ((Int, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateIndexesUsingBlock(_ block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.6 |

Modified NSIndexSet.enumerateIndexesWithOptions(NSEnumerationOptions, usingBlock:(Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateIndexesWithOptions(_ opts: NSEnumerationOptions, usingBlock block: ((Int, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateIndexesWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.6 |

Modified NSIndexSet.enumerateRangesInRange(NSRange, options: NSEnumerationOptions, usingBlock:(NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateRangesInRange(_ range: NSRange, options opts: NSEnumerationOptions, usingBlock block: ((NSRange, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateRangesInRange(_ range: NSRange, options opts: NSEnumerationOptions, usingBlock block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.7 |

Modified NSIndexSet.enumerateRangesUsingBlock((NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateRangesUsingBlock(_ block: ((NSRange, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateRangesUsingBlock(_ block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.7 |

Modified NSIndexSet.enumerateRangesWithOptions(NSEnumerationOptions, usingBlock:(NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateRangesWithOptions(_ opts: NSEnumerationOptions, usingBlock block: ((NSRange, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateRangesWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.7 |

Modified NSIndexSet.getIndexes(UnsafeMutablePointer<Int>, maxCount: Int, inIndexRange: NSRangePointer) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func getIndexes(_ indexBuffer: UnsafePointer<Int>, maxCount bufferSize: Int, inIndexRange range: NSRangePointer) -> Int ``` |
| To | ``` func getIndexes(_ indexBuffer: UnsafeMutablePointer<Int>, maxCount bufferSize: Int, inIndexRange range: NSRangePointer) -> Int ``` |

Modified NSIndexSet.indexInRange(NSRange, options: NSEnumerationOptions, passingTest:(Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexInRange(_ range: NSRange, options opts: NSEnumerationOptions, passingTest predicate: ((Int, UnsafePointer<ObjCBool>) -> Bool)!) -> Int ``` | OS X 10.10 |
| To | ``` func indexInRange(_ range: NSRange, options opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` | OS X 10.6 |

Modified NSIndexSet.indexPassingTest((Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexPassingTest(_ predicate: ((Int, UnsafePointer<ObjCBool>) -> Bool)!) -> Int ``` | OS X 10.10 |
| To | ``` func indexPassingTest(_ predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` | OS X 10.6 |

Modified NSIndexSet.init(indexSet: NSIndexSet)

|  | Declaration |
| --- | --- |
| From | ``` init(indexSet indexSet: NSIndexSet!) ``` |
| To | ``` init(indexSet indexSet: NSIndexSet) ``` |

Modified NSIndexSet.indexWithOptions(NSEnumerationOptions, passingTest:(Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: ((Int, UnsafePointer<ObjCBool>) -> Bool)!) -> Int ``` | OS X 10.10 |
| To | ``` func indexWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` | OS X 10.6 |

Modified NSIndexSet.indexesInRange(NSRange, options: NSEnumerationOptions, passingTest:(Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexesInRange(_ range: NSRange, options opts: NSEnumerationOptions, passingTest predicate: ((Int, UnsafePointer<ObjCBool>) -> Bool)!) -> NSIndexSet! ``` | OS X 10.10 |
| To | ``` func indexesInRange(_ range: NSRange, options opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` | OS X 10.6 |

Modified NSIndexSet.indexesPassingTest((Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexesPassingTest(_ predicate: ((Int, UnsafePointer<ObjCBool>) -> Bool)!) -> NSIndexSet! ``` | OS X 10.10 |
| To | ``` func indexesPassingTest(_ predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` | OS X 10.6 |

Modified NSIndexSet.indexesWithOptions(NSEnumerationOptions, passingTest:(Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: ((Int, UnsafePointer<ObjCBool>) -> Bool)!) -> NSIndexSet! ``` | OS X 10.10 |
| To | ``` func indexesWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` | OS X 10.6 |

Modified NSIndexSet.isEqualToIndexSet(NSIndexSet) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToIndexSet(_ indexSet: NSIndexSet!) -> Bool ``` |
| To | ``` func isEqualToIndexSet(_ indexSet: NSIndexSet) -> Bool ``` |

Modified NSIndexSpecifier.init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier?, key: String, index: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(containerClassDescription classDesc: NSScriptClassDescription!, containerSpecifier container: NSScriptObjectSpecifier!, key property: String!, index index: Int) ``` |
| To | ``` init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String, index index: Int) ``` |

Modified NSInputStream.init(fileAtPath: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fileAtPath path: String!) ``` |
| To | ``` convenience init?(fileAtPath path: String) ``` |

Modified NSInputStream.getBuffer(UnsafeMutablePointer<UnsafeMutablePointer<UInt8>>, length: UnsafeMutablePointer<Int>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getBuffer(_ buffer: UnsafePointer<UnsafePointer<UInt8>>, length len: UnsafePointer<Int>) -> Bool ``` |
| To | ``` func getBuffer(_ buffer: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>>, length len: UnsafeMutablePointer<Int>) -> Bool ``` |

Modified NSInputStream.read(UnsafeMutablePointer<UInt8>, maxLength: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func read(_ buffer: UnsafePointer<UInt8>, maxLength len: Int) -> Int ``` |
| To | ``` func read(_ buffer: UnsafeMutablePointer<UInt8>, maxLength len: Int) -> Int ``` |

Modified NSItemProvider.init(contentsOfURL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL fileURL: NSURL!) ``` |
| To | ``` convenience init?(contentsOfURL fileURL: NSURL!) ``` |

Modified NSItemProvider.hasItemConformingToTypeIdentifier(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func hasItemConformingToTypeIdentifier(_ typeIdentifier: String!) -> Bool ``` |
| To | ``` func hasItemConformingToTypeIdentifier(_ typeIdentifier: String) -> Bool ``` |

Modified NSItemProvider.init(item: NSSecureCoding?, typeIdentifier: String?)

|  | Declaration |
| --- | --- |
| From | ``` init(item item: NSSecureCoding!, typeIdentifier typeIdentifier: String!) ``` |
| To | ``` init(item item: NSSecureCoding?, typeIdentifier typeIdentifier: String?) ``` |

Modified NSItemProvider.loadItemForTypeIdentifier(String, options:[NSObject: AnyObject]?, completionHandler: NSItemProviderCompletionHandler?)

|  | Declaration |
| --- | --- |
| From | ``` func loadItemForTypeIdentifier(_ typeIdentifier: String!, options options: [NSObject : AnyObject]!, completionHandler completionHandler: NSItemProviderCompletionHandler!) ``` |
| To | ``` func loadItemForTypeIdentifier(_ typeIdentifier: String, options options: [NSObject : AnyObject]?, completionHandler completionHandler: NSItemProviderCompletionHandler?) ``` |

Modified NSItemProvider.previewImageHandler

|  | Declaration |
| --- | --- |
| From | ``` var previewImageHandler: NSItemProviderLoadHandler! ``` |
| To | ``` var previewImageHandler: NSItemProviderLoadHandler? ``` |

Modified NSItemProvider.registerItemForTypeIdentifier(String, loadHandler: NSItemProviderLoadHandler)

|  | Declaration |
| --- | --- |
| From | ``` func registerItemForTypeIdentifier(_ typeIdentifier: String!, loadHandler loadHandler: NSItemProviderLoadHandler!) ``` |
| To | ``` func registerItemForTypeIdentifier(_ typeIdentifier: String, loadHandler loadHandler: NSItemProviderLoadHandler) ``` |

Modified NSItemProvider.registeredTypeIdentifiers

|  | Declaration |
| --- | --- |
| From | ``` var registeredTypeIdentifiers: [AnyObject]! { get } ``` |
| To | ``` var registeredTypeIdentifiers: [AnyObject] { get } ``` |

Modified NSJSONReadingOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct NSJSONReadingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var MutableContainers: NSJSONReadingOptions { get }     static var MutableLeaves: NSJSONReadingOptions { get }     static var AllowFragments: NSJSONReadingOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct NSJSONReadingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var MutableContainers: NSJSONReadingOptions { get }     static var MutableLeaves: NSJSONReadingOptions { get }     static var AllowFragments: NSJSONReadingOptions { get } } ``` | RawOptionSetType | OS X 10.7 |

Modified NSJSONReadingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSJSONSerialization

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSJSONSerialization.JSONObjectWithData(NSData, options: NSJSONReadingOptions, error: NSErrorPointer) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func JSONObjectWithData(_ data: NSData!, options opt: NSJSONReadingOptions, error error: NSErrorPointer) -> AnyObject! ``` |
| To | ``` class func JSONObjectWithData(_ data: NSData, options opt: NSJSONReadingOptions, error error: NSErrorPointer) -> AnyObject? ``` |

Modified NSJSONSerialization.JSONObjectWithStream(NSInputStream, options: NSJSONReadingOptions, error: NSErrorPointer) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func JSONObjectWithStream(_ stream: NSInputStream!, options opt: NSJSONReadingOptions, error error: NSErrorPointer) -> AnyObject! ``` |
| To | ``` class func JSONObjectWithStream(_ stream: NSInputStream, options opt: NSJSONReadingOptions, error error: NSErrorPointer) -> AnyObject? ``` |

Modified NSJSONSerialization.dataWithJSONObject(AnyObject, options: NSJSONWritingOptions, error: NSErrorPointer) -> NSData? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func dataWithJSONObject(_ obj: AnyObject!, options opt: NSJSONWritingOptions, error error: NSErrorPointer) -> NSData! ``` |
| To | ``` class func dataWithJSONObject(_ obj: AnyObject, options opt: NSJSONWritingOptions, error error: NSErrorPointer) -> NSData? ``` |

Modified NSJSONSerialization.isValidJSONObject(AnyObject) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func isValidJSONObject(_ obj: AnyObject!) -> Bool ``` |
| To | ``` class func isValidJSONObject(_ obj: AnyObject) -> Bool ``` |

Modified NSJSONSerialization.writeJSONObject(AnyObject, toStream: NSOutputStream, options: NSJSONWritingOptions, error: NSErrorPointer) -> Int [class]

|  | Declaration |
| --- | --- |
| From | ``` class func writeJSONObject(_ obj: AnyObject!, toStream stream: NSOutputStream!, options opt: NSJSONWritingOptions, error error: NSErrorPointer) -> Int ``` |
| To | ``` class func writeJSONObject(_ obj: AnyObject, toStream stream: NSOutputStream, options opt: NSJSONWritingOptions, error error: NSErrorPointer) -> Int ``` |

Modified NSJSONWritingOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct NSJSONWritingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var PrettyPrinted: NSJSONWritingOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct NSJSONWritingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var PrettyPrinted: NSJSONWritingOptions { get } } ``` | RawOptionSetType | OS X 10.7 |

Modified NSJSONWritingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSKeyValueObservingOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSKeyValueObservingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var New: NSKeyValueObservingOptions { get }     static var Old: NSKeyValueObservingOptions { get }     static var Initial: NSKeyValueObservingOptions { get }     static var Prior: NSKeyValueObservingOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSKeyValueObservingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var New: NSKeyValueObservingOptions { get }     static var Old: NSKeyValueObservingOptions { get }     static var Initial: NSKeyValueObservingOptions { get }     static var Prior: NSKeyValueObservingOptions { get } } ``` | RawOptionSetType |

Modified NSKeyValueObservingOptions.Initial

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSKeyValueObservingOptions.Prior

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSKeyValueObservingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSKeyedArchiver.archiveRootObject(AnyObject, toFile: String) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func archiveRootObject(_ rootObject: AnyObject!, toFile path: String!) -> Bool ``` |
| To | ``` class func archiveRootObject(_ rootObject: AnyObject, toFile path: String) -> Bool ``` |

Modified NSKeyedArchiver.archivedDataWithRootObject(AnyObject) -> NSData [class]

|  | Declaration |
| --- | --- |
| From | ``` class func archivedDataWithRootObject(_ rootObject: AnyObject!) -> NSData! ``` |
| To | ``` class func archivedDataWithRootObject(_ rootObject: AnyObject) -> NSData ``` |

Modified NSKeyedArchiver.classNameForClass(AnyClass) -> String? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func classNameForClass(_ cls: AnyClass!) -> String! ``` |
| To | ``` class func classNameForClass(_ cls: AnyClass) -> String? ``` |

Modified NSKeyedArchiver.classNameForClass(AnyClass) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func classNameForClass(_ cls: AnyClass!) -> String! ``` |
| To | ``` func classNameForClass(_ cls: AnyClass) -> String? ``` |

Modified NSKeyedArchiver.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: NSKeyedArchiverDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: NSKeyedArchiverDelegate? ``` |

Modified NSKeyedArchiver.encodeBool(Bool, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeBool(_ boolv: Bool, forKey key: String!) ``` |
| To | ``` func encodeBool(_ boolv: Bool, forKey key: String) ``` |

Modified NSKeyedArchiver.encodeBytes(UnsafePointer<UInt8>, length: Int, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeBytes(_ bytesp: ConstUnsafePointer<UInt8>, length lenv: Int, forKey key: String!) ``` |
| To | ``` func encodeBytes(_ bytesp: UnsafePointer<UInt8>, length lenv: Int, forKey key: String) ``` |

Modified NSKeyedArchiver.encodeConditionalObject(AnyObject?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeConditionalObject(_ objv: AnyObject!, forKey key: String!) ``` |
| To | ``` func encodeConditionalObject(_ objv: AnyObject?, forKey key: String) ``` |

Modified NSKeyedArchiver.encodeDouble(Double, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeDouble(_ realv: Double, forKey key: String!) ``` |
| To | ``` func encodeDouble(_ realv: Double, forKey key: String) ``` |

Modified NSKeyedArchiver.encodeFloat(Float, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeFloat(_ realv: Float, forKey key: String!) ``` |
| To | ``` func encodeFloat(_ realv: Float, forKey key: String) ``` |

Modified NSKeyedArchiver.encodeInt(Int32, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeInt(_ intv: Int32, forKey key: String!) ``` |
| To | ``` func encodeInt(_ intv: Int32, forKey key: String) ``` |

Modified NSKeyedArchiver.encodeInt32(Int32, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeInt32(_ intv: Int32, forKey key: String!) ``` |
| To | ``` func encodeInt32(_ intv: Int32, forKey key: String) ``` |

Modified NSKeyedArchiver.encodeInt64(Int64, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeInt64(_ intv: Int64, forKey key: String!) ``` |
| To | ``` func encodeInt64(_ intv: Int64, forKey key: String) ``` |

Modified NSKeyedArchiver.encodeObject(AnyObject?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func encodeObject(_ objv: AnyObject!, forKey key: String!) ``` |
| To | ``` func encodeObject(_ objv: AnyObject?, forKey key: String) ``` |

Modified NSKeyedArchiver.init(forWritingWithMutableData: NSMutableData)

|  | Declaration |
| --- | --- |
| From | ``` init(forWritingWithMutableData data: NSMutableData!) ``` |
| To | ``` init(forWritingWithMutableData data: NSMutableData) ``` |

Modified NSKeyedArchiver.setClassName(String?, forClass: AnyClass) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setClassName(_ codedName: String!, forClass cls: AnyClass!) ``` |
| To | ``` class func setClassName(_ codedName: String?, forClass cls: AnyClass) ``` |

Modified NSKeyedArchiver.setClassName(String?, forClass: AnyClass)

|  | Declaration |
| --- | --- |
| From | ``` func setClassName(_ codedName: String!, forClass cls: AnyClass!) ``` |
| To | ``` func setClassName(_ codedName: String?, forClass cls: AnyClass) ``` |

Modified NSKeyedArchiver.setRequiresSecureCoding(Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSKeyedArchiverDelegate.archiver(NSKeyedArchiver, didEncodeObject: AnyObject?)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func archiver(_ archiver: NSKeyedArchiver!, didEncodeObject object: AnyObject!) ``` | -- |
| To | ``` optional func archiver(_ archiver: NSKeyedArchiver, didEncodeObject object: AnyObject?) ``` | yes |

Modified NSKeyedArchiverDelegate.archiver(NSKeyedArchiver, willEncodeObject: AnyObject) -> AnyObject?

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func archiver(_ archiver: NSKeyedArchiver!, willEncodeObject object: AnyObject!) -> AnyObject! ``` | -- |
| To | ``` optional func archiver(_ archiver: NSKeyedArchiver, willEncodeObject object: AnyObject) -> AnyObject? ``` | yes |

Modified NSKeyedArchiverDelegate.archiver(NSKeyedArchiver, willReplaceObject: AnyObject, withObject: AnyObject)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func archiver(_ archiver: NSKeyedArchiver!, willReplaceObject object: AnyObject!, withObject newObject: AnyObject!) ``` | -- |
| To | ``` optional func archiver(_ archiver: NSKeyedArchiver, willReplaceObject object: AnyObject, withObject newObject: AnyObject) ``` | yes |

Modified NSKeyedArchiverDelegate.archiverDidFinish(NSKeyedArchiver)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func archiverDidFinish(_ archiver: NSKeyedArchiver!) ``` | -- |
| To | ``` optional func archiverDidFinish(_ archiver: NSKeyedArchiver) ``` | yes |

Modified NSKeyedArchiverDelegate.archiverWillFinish(NSKeyedArchiver)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func archiverWillFinish(_ archiver: NSKeyedArchiver!) ``` | -- |
| To | ``` optional func archiverWillFinish(_ archiver: NSKeyedArchiver) ``` | yes |

Modified NSKeyedUnarchiver.classForClassName(String) -> AnyClass? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func classForClassName(_ codedName: String!) -> AnyClass! ``` |
| To | ``` class func classForClassName(_ codedName: String) -> AnyClass? ``` |

Modified NSKeyedUnarchiver.classForClassName(String) -> AnyClass?

|  | Declaration |
| --- | --- |
| From | ``` func classForClassName(_ codedName: String!) -> AnyClass! ``` |
| To | ``` func classForClassName(_ codedName: String) -> AnyClass? ``` |

Modified NSKeyedUnarchiver.containsValueForKey(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func containsValueForKey(_ key: String!) -> Bool ``` |
| To | ``` func containsValueForKey(_ key: String) -> Bool ``` |

Modified NSKeyedUnarchiver.decodeBoolForKey(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func decodeBoolForKey(_ key: String!) -> Bool ``` |
| To | ``` func decodeBoolForKey(_ key: String) -> Bool ``` |

Modified NSKeyedUnarchiver.decodeBytesForKey(String, returnedLength: UnsafeMutablePointer<Int>) -> UnsafePointer<UInt8>

|  | Declaration |
| --- | --- |
| From | ``` func decodeBytesForKey(_ key: String!, returnedLength lengthp: UnsafePointer<Int>) -> ConstUnsafePointer<UInt8> ``` |
| To | ``` func decodeBytesForKey(_ key: String, returnedLength lengthp: UnsafeMutablePointer<Int>) -> UnsafePointer<UInt8> ``` |

Modified NSKeyedUnarchiver.decodeDoubleForKey(String) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func decodeDoubleForKey(_ key: String!) -> Double ``` |
| To | ``` func decodeDoubleForKey(_ key: String) -> Double ``` |

Modified NSKeyedUnarchiver.decodeFloatForKey(String) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func decodeFloatForKey(_ key: String!) -> Float ``` |
| To | ``` func decodeFloatForKey(_ key: String) -> Float ``` |

Modified NSKeyedUnarchiver.decodeInt32ForKey(String) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func decodeInt32ForKey(_ key: String!) -> Int32 ``` |
| To | ``` func decodeInt32ForKey(_ key: String) -> Int32 ``` |

Modified NSKeyedUnarchiver.decodeInt64ForKey(String) -> Int64

|  | Declaration |
| --- | --- |
| From | ``` func decodeInt64ForKey(_ key: String!) -> Int64 ``` |
| To | ``` func decodeInt64ForKey(_ key: String) -> Int64 ``` |

Modified NSKeyedUnarchiver.decodeIntForKey(String) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func decodeIntForKey(_ key: String!) -> Int32 ``` |
| To | ``` func decodeIntForKey(_ key: String) -> Int32 ``` |

Modified NSKeyedUnarchiver.decodeObjectForKey(String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func decodeObjectForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` func decodeObjectForKey(_ key: String) -> AnyObject? ``` |

Modified NSKeyedUnarchiver.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: NSKeyedUnarchiverDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: NSKeyedUnarchiverDelegate? ``` |

Modified NSKeyedUnarchiver.init(forReadingWithData: NSData)

|  | Declaration |
| --- | --- |
| From | ``` init(forReadingWithData data: NSData!) ``` |
| To | ``` init(forReadingWithData data: NSData) ``` |

Modified NSKeyedUnarchiver.setClass(AnyClass?, forClassName: String) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setClass(_ cls: AnyClass!, forClassName codedName: String!) ``` |
| To | ``` class func setClass(_ cls: AnyClass?, forClassName codedName: String) ``` |

Modified NSKeyedUnarchiver.setClass(AnyClass?, forClassName: String)

|  | Declaration |
| --- | --- |
| From | ``` func setClass(_ cls: AnyClass!, forClassName codedName: String!) ``` |
| To | ``` func setClass(_ cls: AnyClass?, forClassName codedName: String) ``` |

Modified NSKeyedUnarchiver.setRequiresSecureCoding(Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSKeyedUnarchiver.unarchiveObjectWithData(NSData) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func unarchiveObjectWithData(_ data: NSData!) -> AnyObject! ``` |
| To | ``` class func unarchiveObjectWithData(_ data: NSData) -> AnyObject? ``` |

Modified NSKeyedUnarchiver.unarchiveObjectWithFile(String) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func unarchiveObjectWithFile(_ path: String!) -> AnyObject! ``` |
| To | ``` class func unarchiveObjectWithFile(_ path: String) -> AnyObject? ``` |

Modified NSKeyedUnarchiverDelegate.unarchiver(NSKeyedUnarchiver, cannotDecodeObjectOfClassName: String, originalClasses:[AnyObject]) -> AnyClass

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func unarchiver(_ unarchiver: NSKeyedUnarchiver!, cannotDecodeObjectOfClassName name: String!, originalClasses classNames: [AnyObject]!) -> AnyClass! ``` | -- |
| To | ``` optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, cannotDecodeObjectOfClassName name: String, originalClasses classNames: [AnyObject]) -> AnyClass ``` | yes |

Modified NSKeyedUnarchiverDelegate.unarchiver(NSKeyedUnarchiver, didDecodeObject: AnyObject?) -> AnyObject?

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func unarchiver(_ unarchiver: NSKeyedUnarchiver!, didDecodeObject object: AnyObject!) -> AnyObject! ``` | -- |
| To | ``` optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, didDecodeObject object: AnyObject?) -> AnyObject? ``` | yes |

Modified NSKeyedUnarchiverDelegate.unarchiver(NSKeyedUnarchiver, willReplaceObject: AnyObject, withObject: AnyObject)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func unarchiver(_ unarchiver: NSKeyedUnarchiver!, willReplaceObject object: AnyObject!, withObject newObject: AnyObject!) ``` | -- |
| To | ``` optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, willReplaceObject object: AnyObject, withObject newObject: AnyObject) ``` | yes |

Modified NSKeyedUnarchiverDelegate.unarchiverDidFinish(NSKeyedUnarchiver)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func unarchiverDidFinish(_ unarchiver: NSKeyedUnarchiver!) ``` | -- |
| To | ``` optional func unarchiverDidFinish(_ unarchiver: NSKeyedUnarchiver) ``` | yes |

Modified NSKeyedUnarchiverDelegate.unarchiverWillFinish(NSKeyedUnarchiver)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func unarchiverWillFinish(_ unarchiver: NSKeyedUnarchiver!) ``` | -- |
| To | ``` optional func unarchiverWillFinish(_ unarchiver: NSKeyedUnarchiver) ``` | yes |

Modified NSLengthFormatter.getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forString: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getObjectValue(_ obj: AutoreleasingUnsafePointer<AnyObject?>, forString string: String!, errorDescription error: AutoreleasingUnsafePointer<NSString?>) -> Bool ``` |
| To | ``` func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool ``` |

Modified NSLengthFormatter.numberFormatter

|  | Declaration |
| --- | --- |
| From | ``` var numberFormatter: NSNumberFormatter! ``` |
| To | ``` @NSCopying var numberFormatter: NSNumberFormatter! ``` |

Modified NSLengthFormatter.stringFromMeters(Double) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringFromMeters(_ numberInMeters: Double) -> String! ``` |
| To | ``` func stringFromMeters(_ numberInMeters: Double) -> String ``` |

Modified NSLengthFormatter.stringFromValue(Double, unit: NSLengthFormatterUnit) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringFromValue(_ value: Double, unit unit: NSLengthFormatterUnit) -> String! ``` |
| To | ``` func stringFromValue(_ value: Double, unit unit: NSLengthFormatterUnit) -> String ``` |

Modified NSLengthFormatter.unitStringFromMeters(Double, usedUnit: UnsafeMutablePointer<NSLengthFormatterUnit>) -> String

|  | Declaration |
| --- | --- |
| From | ``` func unitStringFromMeters(_ numberInMeters: Double, usedUnit unitp: UnsafePointer<NSLengthFormatterUnit>) -> String! ``` |
| To | ``` func unitStringFromMeters(_ numberInMeters: Double, usedUnit unitp: UnsafeMutablePointer<NSLengthFormatterUnit>) -> String ``` |

Modified NSLengthFormatter.unitStringFromValue(Double, unit: NSLengthFormatterUnit) -> String

|  | Declaration |
| --- | --- |
| From | ``` func unitStringFromValue(_ value: Double, unit unit: NSLengthFormatterUnit) -> String! ``` |
| To | ``` func unitStringFromValue(_ value: Double, unit unit: NSLengthFormatterUnit) -> String ``` |

Modified NSLinguisticTagger

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSLinguisticTagger.availableTagSchemesForLanguage(String) -> [AnyObject] [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func availableTagSchemesForLanguage(_ language: String!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` class func availableTagSchemesForLanguage(_ language: String) -> [AnyObject] ``` | OS X 10.7 |

Modified NSLinguisticTagger.enumerateTagsInRange(NSRange, scheme: String, options: NSLinguisticTaggerOptions, usingBlock:(String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateTagsInRange(_ range: NSRange, scheme tagScheme: String!, options opts: NSLinguisticTaggerOptions, usingBlock block: ((String!, NSRange, NSRange, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, usingBlock block: (String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.7 |

Modified NSLinguisticTagger.orthographyAtIndex(Int, effectiveRange: NSRangePointer) -> NSOrthography?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func orthographyAtIndex(_ charIndex: Int, effectiveRange effectiveRange: NSRangePointer) -> NSOrthography! ``` | OS X 10.10 |
| To | ``` func orthographyAtIndex(_ charIndex: Int, effectiveRange effectiveRange: NSRangePointer) -> NSOrthography? ``` | OS X 10.7 |

Modified NSLinguisticTagger.possibleTagsAtIndex(Int, scheme: String, tokenRange: NSRangePointer, sentenceRange: NSRangePointer, scores: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject]?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func possibleTagsAtIndex(_ charIndex: Int, scheme tagScheme: String!, tokenRange tokenRange: NSRangePointer, sentenceRange sentenceRange: NSRangePointer, scores scores: AutoreleasingUnsafePointer<NSArray?>) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func possibleTagsAtIndex(_ charIndex: Int, scheme tagScheme: String, tokenRange tokenRange: NSRangePointer, sentenceRange sentenceRange: NSRangePointer, scores scores: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject]? ``` | OS X 10.7 |

Modified NSLinguisticTagger.sentenceRangeForRange(NSRange) -> NSRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSLinguisticTagger.setOrthography(NSOrthography?, range: NSRange)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setOrthography(_ orthography: NSOrthography!, range range: NSRange) ``` | OS X 10.10 |
| To | ``` func setOrthography(_ orthography: NSOrthography?, range range: NSRange) ``` | OS X 10.7 |

Modified NSLinguisticTagger.string

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var string: String! ``` | OS X 10.10 |
| To | ``` var string: String? ``` | OS X 10.7 |

Modified NSLinguisticTagger.stringEditedInRange(NSRange, changeInLength: Int)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSLinguisticTagger.tagAtIndex(Int, scheme: String, tokenRange: NSRangePointer, sentenceRange: NSRangePointer) -> String?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func tagAtIndex(_ charIndex: Int, scheme tagScheme: String!, tokenRange tokenRange: NSRangePointer, sentenceRange sentenceRange: NSRangePointer) -> String! ``` | OS X 10.10 |
| To | ``` func tagAtIndex(_ charIndex: Int, scheme tagScheme: String, tokenRange tokenRange: NSRangePointer, sentenceRange sentenceRange: NSRangePointer) -> String? ``` | OS X 10.7 |

Modified NSLinguisticTagger.tagSchemes

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var tagSchemes: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var tagSchemes: [AnyObject] { get } ``` | OS X 10.7 |

Modified NSLinguisticTagger.init(tagSchemes: [AnyObject], options: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(tagSchemes tagSchemes: [AnyObject]!, options opts: Int) ``` | OS X 10.10 |
| To | ``` init(tagSchemes tagSchemes: [AnyObject], options opts: Int) ``` | OS X 10.7 |

Modified NSLinguisticTagger.tagsInRange(NSRange, scheme: String, options: NSLinguisticTaggerOptions, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func tagsInRange(_ range: NSRange, scheme tagScheme: String!, options opts: NSLinguisticTaggerOptions, tokenRanges tokenRanges: AutoreleasingUnsafePointer<NSArray?>) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func tagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject] ``` | OS X 10.7 |

Modified NSLinguisticTaggerOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSLinguisticTaggerOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var OmitWords: NSLinguisticTaggerOptions { get }     static var OmitPunctuation: NSLinguisticTaggerOptions { get }     static var OmitWhitespace: NSLinguisticTaggerOptions { get }     static var OmitOther: NSLinguisticTaggerOptions { get }     static var JoinNames: NSLinguisticTaggerOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSLinguisticTaggerOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var OmitWords: NSLinguisticTaggerOptions { get }     static var OmitPunctuation: NSLinguisticTaggerOptions { get }     static var OmitWhitespace: NSLinguisticTaggerOptions { get }     static var OmitOther: NSLinguisticTaggerOptions { get }     static var JoinNames: NSLinguisticTaggerOptions { get } } ``` | RawOptionSetType |

Modified NSLinguisticTaggerOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSLocale.ISOCountryCodes() -> [AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func ISOCountryCodes() -> [AnyObject]! ``` |
| To | ``` class func ISOCountryCodes() -> [AnyObject] ``` |

Modified NSLocale.ISOCurrencyCodes() -> [AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func ISOCurrencyCodes() -> [AnyObject]! ``` |
| To | ``` class func ISOCurrencyCodes() -> [AnyObject] ``` |

Modified NSLocale.ISOLanguageCodes() -> [AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func ISOLanguageCodes() -> [AnyObject]! ``` |
| To | ``` class func ISOLanguageCodes() -> [AnyObject] ``` |

Modified NSLocale.autoupdatingCurrentLocale() -> NSLocale [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func autoupdatingCurrentLocale() -> NSLocale! ``` | OS X 10.10 |
| To | ``` class func autoupdatingCurrentLocale() -> NSLocale ``` | OS X 10.5 |

Modified NSLocale.availableLocaleIdentifiers() -> [AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func availableLocaleIdentifiers() -> [AnyObject]! ``` |
| To | ``` class func availableLocaleIdentifiers() -> [AnyObject] ``` |

Modified NSLocale.canonicalLanguageIdentifierFromString(String) -> String [class]

|  | Declaration |
| --- | --- |
| From | ``` class func canonicalLanguageIdentifierFromString(_ string: String!) -> String! ``` |
| To | ``` class func canonicalLanguageIdentifierFromString(_ string: String) -> String ``` |

Modified NSLocale.canonicalLocaleIdentifierFromString(String) -> String [class]

|  | Declaration |
| --- | --- |
| From | ``` class func canonicalLocaleIdentifierFromString(_ string: String!) -> String! ``` |
| To | ``` class func canonicalLocaleIdentifierFromString(_ string: String) -> String ``` |

Modified NSLocale.characterDirectionForLanguage(String) -> NSLocaleLanguageDirection [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func characterDirectionForLanguage(_ isoLangCode: String!) -> NSLocaleLanguageDirection ``` | OS X 10.10 |
| To | ``` class func characterDirectionForLanguage(_ isoLangCode: String) -> NSLocaleLanguageDirection ``` | OS X 10.6 |

Modified NSLocale.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSLocale.commonISOCurrencyCodes() -> [AnyObject] [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func commonISOCurrencyCodes() -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` class func commonISOCurrencyCodes() -> [AnyObject] ``` | OS X 10.5 |

Modified NSLocale.componentsFromLocaleIdentifier(String) -> [NSObject: AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func componentsFromLocaleIdentifier(_ string: String!) -> [NSObject : AnyObject]! ``` |
| To | ``` class func componentsFromLocaleIdentifier(_ string: String) -> [NSObject : AnyObject] ``` |

Modified NSLocale.currentLocale() -> NSLocale [class]

|  | Declaration |
| --- | --- |
| From | ``` class func currentLocale() -> NSLocale! ``` |
| To | ``` class func currentLocale() -> NSLocale ``` |

Modified NSLocale.displayNameForKey(AnyObject, value: AnyObject) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func displayNameForKey(_ key: AnyObject!, value value: AnyObject!) -> String! ``` |
| To | ``` func displayNameForKey(_ key: AnyObject, value value: AnyObject) -> String? ``` |

Modified NSLocale.lineDirectionForLanguage(String) -> NSLocaleLanguageDirection [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func lineDirectionForLanguage(_ isoLangCode: String!) -> NSLocaleLanguageDirection ``` | OS X 10.10 |
| To | ``` class func lineDirectionForLanguage(_ isoLangCode: String) -> NSLocaleLanguageDirection ``` | OS X 10.6 |

Modified NSLocale.localeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` var localeIdentifier: String! { get } ``` |
| To | ``` var localeIdentifier: String { get } ``` |

Modified NSLocale.localeIdentifierFromComponents([NSObject: AnyObject]) -> String [class]

|  | Declaration |
| --- | --- |
| From | ``` class func localeIdentifierFromComponents(_ dict: [NSObject : AnyObject]!) -> String! ``` |
| To | ``` class func localeIdentifierFromComponents(_ dict: [NSObject : AnyObject]) -> String ``` |

Modified NSLocale.localeIdentifierFromWindowsLocaleCode(UInt32) -> String? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func localeIdentifierFromWindowsLocaleCode(_ lcid: UInt32) -> String! ``` | OS X 10.10 |
| To | ``` class func localeIdentifierFromWindowsLocaleCode(_ lcid: UInt32) -> String? ``` | OS X 10.6 |

Modified NSLocale.objectForKey(AnyObject) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func objectForKey(_ key: AnyObject!) -> AnyObject! ``` |
| To | ``` func objectForKey(_ key: AnyObject) -> AnyObject? ``` |

Modified NSLocale.preferredLanguages() -> [AnyObject] [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func preferredLanguages() -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` class func preferredLanguages() -> [AnyObject] ``` | OS X 10.5 |

Modified NSLocale.systemLocale() -> NSLocale [class]

|  | Declaration |
| --- | --- |
| From | ``` class func systemLocale() -> NSLocale! ``` |
| To | ``` class func systemLocale() -> NSLocale ``` |

Modified NSLocale.windowsLocaleCodeFromLocaleIdentifier(String) -> UInt32 [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func windowsLocaleCodeFromLocaleIdentifier(_ localeIdentifier: String!) -> UInt32 ``` | OS X 10.10 |
| To | ``` class func windowsLocaleCodeFromLocaleIdentifier(_ localeIdentifier: String) -> UInt32 ``` | OS X 10.6 |

Modified NSLock.lockBeforeDate(NSDate) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func lockBeforeDate(_ limit: NSDate!) -> Bool ``` |
| To | ``` func lockBeforeDate(_ limit: NSDate) -> Bool ``` |

Modified NSLock.name

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var name: String! ``` | OS X 10.10 |
| To | ``` var name: String? ``` | OS X 10.5 |

Modified NSMachPort.delegate() -> NSMachPortDelegate?

|  | Declaration |
| --- | --- |
| From | ``` func delegate() -> NSMachPortDelegate! ``` |
| To | ``` func delegate() -> NSMachPortDelegate? ``` |

Modified NSMachPort.init(machPort: UInt32, options: Int)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSMachPort.portWithMachPort(UInt32) -> NSPort [class]

|  | Declaration |
| --- | --- |
| From | ``` class func portWithMachPort(_ machPort: UInt32) -> NSPort! ``` |
| To | ``` class func portWithMachPort(_ machPort: UInt32) -> NSPort ``` |

Modified NSMachPort.portWithMachPort(UInt32, options: Int) -> NSPort [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func portWithMachPort(_ machPort: UInt32, options f: Int) -> NSPort! ``` | OS X 10.10 |
| To | ``` class func portWithMachPort(_ machPort: UInt32, options f: Int) -> NSPort ``` | OS X 10.5 |

Modified NSMachPort.removeFromRunLoop(NSRunLoop, forMode: String)

|  | Declaration |
| --- | --- |
| From | ``` func removeFromRunLoop(_ runLoop: NSRunLoop!, forMode mode: String!) ``` |
| To | ``` func removeFromRunLoop(_ runLoop: NSRunLoop, forMode mode: String) ``` |

Modified NSMachPort.scheduleInRunLoop(NSRunLoop, forMode: String)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleInRunLoop(_ runLoop: NSRunLoop!, forMode mode: String!) ``` |
| To | ``` func scheduleInRunLoop(_ runLoop: NSRunLoop, forMode mode: String) ``` |

Modified NSMachPort.setDelegate(NSMachPortDelegate?)

|  | Declaration |
| --- | --- |
| From | ``` func setDelegate(_ anObject: NSMachPortDelegate!) ``` |
| To | ``` func setDelegate(_ anObject: NSMachPortDelegate?) ``` |

Modified NSMachPortDelegate.handleMachMessage(UnsafeMutablePointer<Void>)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func handleMachMessage(_ msg: UnsafePointer<()>) ``` | -- |
| To | ``` optional func handleMachMessage(_ msg: UnsafeMutablePointer<Void>) ``` | yes |

Modified NSMapEnumerator [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSMapEnumerator {     var _pi: Int     var _si: Int     var _bs: UnsafePointer<()> } ``` |
| To | ``` struct NSMapEnumerator {     var _pi: Int     var _si: Int     var _bs: UnsafeMutablePointer<Void>     init()     init(_pi _pi: Int, _si _si: Int, _bs _bs: UnsafeMutablePointer<Void>) } ``` |

Modified NSMapTable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSMapTable.dictionaryRepresentation() -> [NSObject: AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func dictionaryRepresentation() -> [NSObject : AnyObject]! ``` |
| To | ``` func dictionaryRepresentation() -> [NSObject : AnyObject] ``` |

Modified NSMapTable.keyEnumerator() -> NSEnumerator

|  | Declaration |
| --- | --- |
| From | ``` func keyEnumerator() -> NSEnumerator! ``` |
| To | ``` func keyEnumerator() -> NSEnumerator ``` |

Modified NSMapTable.keyPointerFunctions

|  | Declaration |
| --- | --- |
| From | ``` var keyPointerFunctions: NSPointerFunctions! { get } ``` |
| To | ``` @NSCopying var keyPointerFunctions: NSPointerFunctions { get } ``` |

Modified NSMapTable.init(keyPointerFunctions: NSPointerFunctions, valuePointerFunctions: NSPointerFunctions, capacity: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(keyPointerFunctions keyFunctions: NSPointerFunctions!, valuePointerFunctions valueFunctions: NSPointerFunctions!, capacity initialCapacity: Int) ``` |
| To | ``` init(keyPointerFunctions keyFunctions: NSPointerFunctions, valuePointerFunctions valueFunctions: NSPointerFunctions, capacity initialCapacity: Int) ``` |

Modified NSMapTable.objectEnumerator() -> NSEnumerator

|  | Declaration |
| --- | --- |
| From | ``` func objectEnumerator() -> NSEnumerator! ``` |
| To | ``` func objectEnumerator() -> NSEnumerator ``` |

Modified NSMapTable.objectForKey(AnyObject) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func objectForKey(_ aKey: AnyObject!) -> AnyObject! ``` |
| To | ``` func objectForKey(_ aKey: AnyObject) -> AnyObject? ``` |

Modified NSMapTable.removeObjectForKey(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func removeObjectForKey(_ aKey: AnyObject!) ``` |
| To | ``` func removeObjectForKey(_ aKey: AnyObject) ``` |

Modified NSMapTable.setObject(AnyObject, forKey: AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ anObject: AnyObject!, forKey aKey: AnyObject!) ``` |
| To | ``` func setObject(_ anObject: AnyObject, forKey aKey: AnyObject) ``` |

Modified NSMapTable.strongToStrongObjectsMapTable() -> NSMapTable [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func strongToStrongObjectsMapTable() -> NSMapTable! ``` | OS X 10.10 |
| To | ``` class func strongToStrongObjectsMapTable() -> NSMapTable ``` | OS X 10.8 |

Modified NSMapTable.strongToWeakObjectsMapTable() -> NSMapTable [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func strongToWeakObjectsMapTable() -> NSMapTable! ``` | OS X 10.10 |
| To | ``` class func strongToWeakObjectsMapTable() -> NSMapTable ``` | OS X 10.8 |

Modified NSMapTable.valuePointerFunctions

|  | Declaration |
| --- | --- |
| From | ``` var valuePointerFunctions: NSPointerFunctions! { get } ``` |
| To | ``` @NSCopying var valuePointerFunctions: NSPointerFunctions { get } ``` |

Modified NSMapTable.weakToStrongObjectsMapTable() -> NSMapTable [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func weakToStrongObjectsMapTable() -> NSMapTable! ``` | OS X 10.10 |
| To | ``` class func weakToStrongObjectsMapTable() -> NSMapTable ``` | OS X 10.8 |

Modified NSMapTable.weakToWeakObjectsMapTable() -> NSMapTable [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func weakToWeakObjectsMapTable() -> NSMapTable! ``` | OS X 10.10 |
| To | ``` class func weakToWeakObjectsMapTable() -> NSMapTable ``` | OS X 10.8 |

Modified NSMapTableKeyCallBacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSMapTableKeyCallBacks {     var hash: CFunctionPointer<((NSMapTable!, ConstUnsafePointer<()>) -> Int)>     var isEqual: CFunctionPointer<((NSMapTable!, ConstUnsafePointer<()>, ConstUnsafePointer<()>) -> Bool)>     var retain: CFunctionPointer<((NSMapTable!, ConstUnsafePointer<()>) -> Void)>     var release: CFunctionPointer<((NSMapTable!, UnsafePointer<()>) -> Void)>     var describe: CFunctionPointer<((NSMapTable!, ConstUnsafePointer<()>) -> String!)>     var notAKeyMarker: ConstUnsafePointer<()> } ``` |
| To | ``` struct NSMapTableKeyCallBacks {     var hash: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> Int)>     var isEqual: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>, UnsafePointer<Void>) -> Bool)>     var retain: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> Void)>     var release: CFunctionPointer<((NSMapTable!, UnsafeMutablePointer<Void>) -> Void)>     var describe: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> String!)>     var notAKeyMarker: UnsafePointer<Void>     init()     init(hash hash: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> Int)>, isEqual isEqual: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>, UnsafePointer<Void>) -> Bool)>, retain retain: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> Void)>, release release: CFunctionPointer<((NSMapTable!, UnsafeMutablePointer<Void>) -> Void)>, describe describe: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> String!)>, notAKeyMarker notAKeyMarker: UnsafePointer<Void>) } ``` |

Modified NSMapTableKeyCallBacks.describe

|  | Declaration |
| --- | --- |
| From | ``` var describe: CFunctionPointer<((NSMapTable!, ConstUnsafePointer<()>) -> String!)> ``` |
| To | ``` var describe: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> String!)> ``` |

Modified NSMapTableKeyCallBacks.hash

|  | Declaration |
| --- | --- |
| From | ``` var hash: CFunctionPointer<((NSMapTable!, ConstUnsafePointer<()>) -> Int)> ``` |
| To | ``` var hash: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> Int)> ``` |

Modified NSMapTableKeyCallBacks.isEqual

|  | Declaration |
| --- | --- |
| From | ``` var isEqual: CFunctionPointer<((NSMapTable!, ConstUnsafePointer<()>, ConstUnsafePointer<()>) -> Bool)> ``` |
| To | ``` var isEqual: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>, UnsafePointer<Void>) -> Bool)> ``` |

Modified NSMapTableKeyCallBacks.notAKeyMarker

|  | Declaration |
| --- | --- |
| From | ``` var notAKeyMarker: ConstUnsafePointer<()> ``` |
| To | ``` var notAKeyMarker: UnsafePointer<Void> ``` |

Modified NSMapTableKeyCallBacks.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((NSMapTable!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((NSMapTable!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified NSMapTableKeyCallBacks.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((NSMapTable!, ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var retain: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> Void)> ``` |

Modified NSMapTableValueCallBacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSMapTableValueCallBacks {     var retain: CFunctionPointer<((NSMapTable!, ConstUnsafePointer<()>) -> Void)>     var release: CFunctionPointer<((NSMapTable!, UnsafePointer<()>) -> Void)>     var describe: CFunctionPointer<((NSMapTable!, ConstUnsafePointer<()>) -> String!)> } ``` |
| To | ``` struct NSMapTableValueCallBacks {     var retain: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> Void)>     var release: CFunctionPointer<((NSMapTable!, UnsafeMutablePointer<Void>) -> Void)>     var describe: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> String!)>     init()     init(retain retain: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> Void)>, release release: CFunctionPointer<((NSMapTable!, UnsafeMutablePointer<Void>) -> Void)>, describe describe: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> String!)>) } ``` |

Modified NSMapTableValueCallBacks.describe

|  | Declaration |
| --- | --- |
| From | ``` var describe: CFunctionPointer<((NSMapTable!, ConstUnsafePointer<()>) -> String!)> ``` |
| To | ``` var describe: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> String!)> ``` |

Modified NSMapTableValueCallBacks.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((NSMapTable!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((NSMapTable!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified NSMapTableValueCallBacks.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((NSMapTable!, ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var retain: CFunctionPointer<((NSMapTable!, UnsafePointer<Void>) -> Void)> ``` |

Modified NSMassFormatter.getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forString: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getObjectValue(_ obj: AutoreleasingUnsafePointer<AnyObject?>, forString string: String!, errorDescription error: AutoreleasingUnsafePointer<NSString?>) -> Bool ``` |
| To | ``` func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool ``` |

Modified NSMassFormatter.numberFormatter

|  | Declaration |
| --- | --- |
| From | ``` var numberFormatter: NSNumberFormatter! ``` |
| To | ``` @NSCopying var numberFormatter: NSNumberFormatter! ``` |

Modified NSMassFormatter.stringFromKilograms(Double) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringFromKilograms(_ numberInKilograms: Double) -> String! ``` |
| To | ``` func stringFromKilograms(_ numberInKilograms: Double) -> String ``` |

Modified NSMassFormatter.stringFromValue(Double, unit: NSMassFormatterUnit) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringFromValue(_ value: Double, unit unit: NSMassFormatterUnit) -> String! ``` |
| To | ``` func stringFromValue(_ value: Double, unit unit: NSMassFormatterUnit) -> String ``` |

Modified NSMassFormatter.unitStringFromKilograms(Double, usedUnit: UnsafeMutablePointer<NSMassFormatterUnit>) -> String

|  | Declaration |
| --- | --- |
| From | ``` func unitStringFromKilograms(_ numberInKilograms: Double, usedUnit unitp: UnsafePointer<NSMassFormatterUnit>) -> String! ``` |
| To | ``` func unitStringFromKilograms(_ numberInKilograms: Double, usedUnit unitp: UnsafeMutablePointer<NSMassFormatterUnit>) -> String ``` |

Modified NSMassFormatter.unitStringFromValue(Double, unit: NSMassFormatterUnit) -> String

|  | Declaration |
| --- | --- |
| From | ``` func unitStringFromValue(_ value: Double, unit unit: NSMassFormatterUnit) -> String! ``` |
| To | ``` func unitStringFromValue(_ value: Double, unit unit: NSMassFormatterUnit) -> String ``` |

Modified NSMatchingFlags [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSMatchingFlags : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Progress: NSMatchingFlags { get }     static var Completed: NSMatchingFlags { get }     static var HitEnd: NSMatchingFlags { get }     static var RequiredEnd: NSMatchingFlags { get }     static var InternalError: NSMatchingFlags { get } } ``` | RawOptionSet |
| To | ``` struct NSMatchingFlags : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Progress: NSMatchingFlags { get }     static var Completed: NSMatchingFlags { get }     static var HitEnd: NSMatchingFlags { get }     static var RequiredEnd: NSMatchingFlags { get }     static var InternalError: NSMatchingFlags { get } } ``` | RawOptionSetType |

Modified NSMatchingFlags.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSMatchingOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSMatchingOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var ReportProgress: NSMatchingOptions { get }     static var ReportCompletion: NSMatchingOptions { get }     static var Anchored: NSMatchingOptions { get }     static var WithTransparentBounds: NSMatchingOptions { get }     static var WithoutAnchoringBounds: NSMatchingOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSMatchingOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ReportProgress: NSMatchingOptions { get }     static var ReportCompletion: NSMatchingOptions { get }     static var Anchored: NSMatchingOptions { get }     static var WithTransparentBounds: NSMatchingOptions { get }     static var WithoutAnchoringBounds: NSMatchingOptions { get } } ``` | RawOptionSetType |

Modified NSMatchingOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSMetadataItem

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSMetadataItem.init(URL: NSURL)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(URL url: NSURL!) ``` | OS X 10.10 |
| To | ``` init?(URL url: NSURL) ``` | OS X 10.9 |

Modified NSMetadataItem.attributes

|  | Declaration |
| --- | --- |
| From | ``` var attributes: [AnyObject]! { get } ``` |
| To | ``` var attributes: [AnyObject] { get } ``` |

Modified NSMetadataItem.valueForAttribute(String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func valueForAttribute(_ key: String!) -> AnyObject! ``` |
| To | ``` func valueForAttribute(_ key: String) -> AnyObject? ``` |

Modified NSMetadataItem.valuesForAttributes([AnyObject]) -> [NSObject: AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func valuesForAttributes(_ keys: [AnyObject]!) -> [NSObject : AnyObject]! ``` |
| To | ``` func valuesForAttributes(_ keys: [AnyObject]) -> [NSObject : AnyObject]? ``` |

Modified NSMetadataQuery

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSMetadataQuery.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: NSMetadataQueryDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: NSMetadataQueryDelegate? ``` |

Modified NSMetadataQuery.enumerateResultsUsingBlock((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateResultsUsingBlock(_ block: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateResultsUsingBlock(_ block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.9 |

Modified NSMetadataQuery.enumerateResultsWithOptions(NSEnumerationOptions, usingBlock:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateResultsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateResultsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.9 |

Modified NSMetadataQuery.groupedResults

|  | Declaration |
| --- | --- |
| From | ``` var groupedResults: [AnyObject]! { get } ``` |
| To | ``` var groupedResults: [AnyObject] { get } ``` |

Modified NSMetadataQuery.groupingAttributes

|  | Declaration |
| --- | --- |
| From | ``` var groupingAttributes: [AnyObject]! ``` |
| To | ``` var groupingAttributes: [AnyObject]? ``` |

Modified NSMetadataQuery.indexOfResult(AnyObject) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func indexOfResult(_ result: AnyObject!) -> Int ``` |
| To | ``` func indexOfResult(_ result: AnyObject) -> Int ``` |

Modified NSMetadataQuery.operationQueue

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var operationQueue: NSOperationQueue! ``` | OS X 10.10 |
| To | ``` var operationQueue: NSOperationQueue? ``` | OS X 10.9 |

Modified NSMetadataQuery.predicate

|  | Declaration |
| --- | --- |
| From | ``` var predicate: NSPredicate! ``` |
| To | ``` @NSCopying var predicate: NSPredicate? ``` |

Modified NSMetadataQuery.resultAtIndex(Int) -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func resultAtIndex(_ idx: Int) -> AnyObject! ``` |
| To | ``` func resultAtIndex(_ idx: Int) -> AnyObject ``` |

Modified NSMetadataQuery.results

|  | Declaration |
| --- | --- |
| From | ``` var results: [AnyObject]! { get } ``` |
| To | ``` var results: [AnyObject] { get } ``` |

Modified NSMetadataQuery.searchItems

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var searchItems: [AnyObject]! ``` | OS X 10.10 |
| To | ``` var searchItems: [AnyObject]? ``` | OS X 10.9 |

Modified NSMetadataQuery.searchScopes

|  | Declaration |
| --- | --- |
| From | ``` var searchScopes: [AnyObject]! ``` |
| To | ``` var searchScopes: [AnyObject] ``` |

Modified NSMetadataQuery.sortDescriptors

|  | Declaration |
| --- | --- |
| From | ``` var sortDescriptors: [AnyObject]! ``` |
| To | ``` var sortDescriptors: [AnyObject] ``` |

Modified NSMetadataQuery.valueListAttributes

|  | Declaration |
| --- | --- |
| From | ``` var valueListAttributes: [AnyObject]! ``` |
| To | ``` var valueListAttributes: [AnyObject] ``` |

Modified NSMetadataQuery.valueLists

|  | Declaration |
| --- | --- |
| From | ``` var valueLists: [NSObject : AnyObject]! { get } ``` |
| To | ``` var valueLists: [NSObject : AnyObject] { get } ``` |

Modified NSMetadataQuery.valueOfAttribute(String, forResultAtIndex: Int) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func valueOfAttribute(_ attrName: String!, forResultAtIndex idx: Int) -> AnyObject! ``` |
| To | ``` func valueOfAttribute(_ attrName: String, forResultAtIndex idx: Int) -> AnyObject? ``` |

Modified NSMetadataQueryAttributeValueTuple

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSMetadataQueryAttributeValueTuple.attribute

|  | Declaration |
| --- | --- |
| From | ``` var attribute: String! { get } ``` |
| To | ``` var attribute: String { get } ``` |

Modified NSMetadataQueryAttributeValueTuple.value

|  | Declaration |
| --- | --- |
| From | ``` var value: AnyObject! { get } ``` |
| To | ``` var value: AnyObject? { get } ``` |

Modified NSMetadataQueryDelegate.metadataQuery(NSMetadataQuery, replacementObjectForResultObject: NSMetadataItem) -> AnyObject

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func metadataQuery(_ query: NSMetadataQuery!, replacementObjectForResultObject result: NSMetadataItem!) -> AnyObject! ``` | -- |
| To | ``` optional func metadataQuery(_ query: NSMetadataQuery, replacementObjectForResultObject result: NSMetadataItem) -> AnyObject ``` | yes |

Modified NSMetadataQueryDelegate.metadataQuery(NSMetadataQuery, replacementValueForAttribute: String, value: AnyObject) -> AnyObject

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func metadataQuery(_ query: NSMetadataQuery!, replacementValueForAttribute attrName: String!, value attrValue: AnyObject!) -> AnyObject! ``` | -- |
| To | ``` optional func metadataQuery(_ query: NSMetadataQuery, replacementValueForAttribute attrName: String, value attrValue: AnyObject) -> AnyObject ``` | yes |

Modified NSMetadataQueryResultGroup

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSMetadataQueryResultGroup.attribute

|  | Declaration |
| --- | --- |
| From | ``` var attribute: String! { get } ``` |
| To | ``` var attribute: String { get } ``` |

Modified NSMetadataQueryResultGroup.results

|  | Declaration |
| --- | --- |
| From | ``` var results: [AnyObject]! { get } ``` |
| To | ``` var results: [AnyObject] { get } ``` |

Modified NSMetadataQueryResultGroup.subgroups

|  | Declaration |
| --- | --- |
| From | ``` var subgroups: [AnyObject]! { get } ``` |
| To | ``` var subgroups: [AnyObject]? { get } ``` |

Modified NSMetadataQueryResultGroup.value

|  | Declaration |
| --- | --- |
| From | ``` var value: AnyObject! { get } ``` |
| To | ``` var value: AnyObject { get } ``` |

Modified NSMoveCommand.keySpecifier

|  | Declaration |
| --- | --- |
| From | ``` var keySpecifier: NSScriptObjectSpecifier! { get } ``` |
| To | ``` var keySpecifier: NSScriptObjectSpecifier? { get } ``` |

Modified NSMoveCommand.setReceiversSpecifier(NSScriptObjectSpecifier)

|  | Declaration |
| --- | --- |
| From | ``` func setReceiversSpecifier(_ receiversRef: NSScriptObjectSpecifier!) ``` |
| To | ``` func setReceiversSpecifier(_ receiversRef: NSScriptObjectSpecifier) ``` |

Modified NSMutableArray

|  | Protocols |
| --- | --- |
| From | AnyObject, Sequence |
| To | AnyObject |

Modified NSMutableArray.addObject(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func addObject(_ anObject: AnyObject!) ``` |
| To | ``` func addObject(_ anObject: AnyObject) ``` |

Modified NSMutableArray.addObjectsFromArray([AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func addObjectsFromArray(_ otherArray: [AnyObject]!) ``` |
| To | ``` func addObjectsFromArray(_ otherArray: [AnyObject]) ``` |

Modified NSMutableArray.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init(coder aDecoder: NSCoder) ``` |

Modified NSMutableArray.filterUsingPredicate(NSPredicate)

|  | Declaration |
| --- | --- |
| From | ``` func filterUsingPredicate(_ predicate: NSPredicate!) ``` |
| To | ``` func filterUsingPredicate(_ predicate: NSPredicate) ``` |

Modified NSMutableArray.insertObject(AnyObject, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insertObject(_ anObject: AnyObject!, atIndex index: Int) ``` |
| To | ``` func insertObject(_ anObject: AnyObject, atIndex index: Int) ``` |

Modified NSMutableArray.insertObjects([AnyObject], atIndexes: NSIndexSet)

|  | Declaration |
| --- | --- |
| From | ``` func insertObjects(_ objects: [AnyObject]!, atIndexes indexes: NSIndexSet!) ``` |
| To | ``` func insertObjects(_ objects: [AnyObject], atIndexes indexes: NSIndexSet) ``` |

Modified NSMutableArray.removeObject(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func removeObject(_ anObject: AnyObject!) ``` |
| To | ``` func removeObject(_ anObject: AnyObject) ``` |

Modified NSMutableArray.removeObject(AnyObject, inRange: NSRange)

|  | Declaration |
| --- | --- |
| From | ``` func removeObject(_ anObject: AnyObject!, inRange range: NSRange) ``` |
| To | ``` func removeObject(_ anObject: AnyObject, inRange range: NSRange) ``` |

Modified NSMutableArray.removeObjectIdenticalTo(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func removeObjectIdenticalTo(_ anObject: AnyObject!) ``` |
| To | ``` func removeObjectIdenticalTo(_ anObject: AnyObject) ``` |

Modified NSMutableArray.removeObjectIdenticalTo(AnyObject, inRange: NSRange)

|  | Declaration |
| --- | --- |
| From | ``` func removeObjectIdenticalTo(_ anObject: AnyObject!, inRange range: NSRange) ``` |
| To | ``` func removeObjectIdenticalTo(_ anObject: AnyObject, inRange range: NSRange) ``` |

Modified NSMutableArray.removeObjectsAtIndexes(NSIndexSet)

|  | Declaration |
| --- | --- |
| From | ``` func removeObjectsAtIndexes(_ indexes: NSIndexSet!) ``` |
| To | ``` func removeObjectsAtIndexes(_ indexes: NSIndexSet) ``` |

Modified NSMutableArray.removeObjectsInArray([AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func removeObjectsInArray(_ otherArray: [AnyObject]!) ``` |
| To | ``` func removeObjectsInArray(_ otherArray: [AnyObject]) ``` |

Modified NSMutableArray.replaceObjectAtIndex(Int, withObject: AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func replaceObjectAtIndex(_ index: Int, withObject anObject: AnyObject!) ``` |
| To | ``` func replaceObjectAtIndex(_ index: Int, withObject anObject: AnyObject) ``` |

Modified NSMutableArray.replaceObjectsAtIndexes(NSIndexSet, withObjects:[AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func replaceObjectsAtIndexes(_ indexes: NSIndexSet!, withObjects objects: [AnyObject]!) ``` |
| To | ``` func replaceObjectsAtIndexes(_ indexes: NSIndexSet, withObjects objects: [AnyObject]) ``` |

Modified NSMutableArray.replaceObjectsInRange(NSRange, withObjectsFromArray:[AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func replaceObjectsInRange(_ range: NSRange, withObjectsFromArray otherArray: [AnyObject]!) ``` |
| To | ``` func replaceObjectsInRange(_ range: NSRange, withObjectsFromArray otherArray: [AnyObject]) ``` |

Modified NSMutableArray.replaceObjectsInRange(NSRange, withObjectsFromArray:[AnyObject], range: NSRange)

|  | Declaration |
| --- | --- |
| From | ``` func replaceObjectsInRange(_ range: NSRange, withObjectsFromArray otherArray: [AnyObject]!, range otherRange: NSRange) ``` |
| To | ``` func replaceObjectsInRange(_ range: NSRange, withObjectsFromArray otherArray: [AnyObject], range otherRange: NSRange) ``` |

Modified NSMutableArray.setArray([AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func setArray(_ otherArray: [AnyObject]!) ``` |
| To | ``` func setArray(_ otherArray: [AnyObject]) ``` |

Modified NSMutableArray.sortUsingComparator(NSComparator)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sortUsingComparator(_ cmptr: NSComparator!) ``` | OS X 10.10 |
| To | ``` func sortUsingComparator(_ cmptr: NSComparator) ``` | OS X 10.6 |

Modified NSMutableArray.sortUsingDescriptors([AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func sortUsingDescriptors(_ sortDescriptors: [AnyObject]!) ``` |
| To | ``` func sortUsingDescriptors(_ sortDescriptors: [AnyObject]) ``` |

Modified NSMutableArray.sortUsingFunction(CFunctionPointer<((AnyObject!, AnyObject!, UnsafeMutablePointer<Void>) -> Int)>, context: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func sortUsingFunction(_ compare: CFunctionPointer<((AnyObject!, AnyObject!, UnsafePointer<()>) -> Int)>, context context: UnsafePointer<()>) ``` |
| To | ``` func sortUsingFunction(_ compare: CFunctionPointer<((AnyObject!, AnyObject!, UnsafeMutablePointer<Void>) -> Int)>, context context: UnsafeMutablePointer<Void>) ``` |

Modified NSMutableArray.sortWithOptions(NSSortOptions, usingComparator: NSComparator)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sortWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator!) ``` | OS X 10.10 |
| To | ``` func sortWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) ``` | OS X 10.6 |

Modified NSMutableAttributedString

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified NSMutableAttributedString.addAttribute(String, value: AnyObject, range: NSRange)

|  | Declaration |
| --- | --- |
| From | ``` func addAttribute(_ name: String!, value value: AnyObject!, range range: NSRange) ``` |
| To | ``` func addAttribute(_ name: String, value value: AnyObject, range range: NSRange) ``` |

Modified NSMutableAttributedString.addAttributes([NSObject: AnyObject], range: NSRange)

|  | Declaration |
| --- | --- |
| From | ``` func addAttributes(_ attrs: [NSObject : AnyObject]!, range range: NSRange) ``` |
| To | ``` func addAttributes(_ attrs: [NSObject : AnyObject], range range: NSRange) ``` |

Modified NSMutableAttributedString.appendAttributedString(NSAttributedString)

|  | Declaration |
| --- | --- |
| From | ``` func appendAttributedString(_ attrString: NSAttributedString!) ``` |
| To | ``` func appendAttributedString(_ attrString: NSAttributedString) ``` |

Modified NSMutableAttributedString.insertAttributedString(NSAttributedString, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insertAttributedString(_ attrString: NSAttributedString!, atIndex loc: Int) ``` |
| To | ``` func insertAttributedString(_ attrString: NSAttributedString, atIndex loc: Int) ``` |

Modified NSMutableAttributedString.mutableString

|  | Declaration |
| --- | --- |
| From | ``` var mutableString: NSMutableString! { get } ``` |
| To | ``` var mutableString: NSMutableString { get } ``` |

Modified NSMutableAttributedString.removeAttribute(String, range: NSRange)

|  | Declaration |
| --- | --- |
| From | ``` func removeAttribute(_ name: String!, range range: NSRange) ``` |
| To | ``` func removeAttribute(_ name: String, range range: NSRange) ``` |

Modified NSMutableAttributedString.replaceCharactersInRange(NSRange, withAttributedString: NSAttributedString)

|  | Declaration |
| --- | --- |
| From | ``` func replaceCharactersInRange(_ range: NSRange, withAttributedString attrString: NSAttributedString!) ``` |
| To | ``` func replaceCharactersInRange(_ range: NSRange, withAttributedString attrString: NSAttributedString) ``` |

Modified NSMutableAttributedString.replaceCharactersInRange(NSRange, withString: String)

|  | Declaration |
| --- | --- |
| From | ``` func replaceCharactersInRange(_ range: NSRange, withString str: String!) ``` |
| To | ``` func replaceCharactersInRange(_ range: NSRange, withString str: String) ``` |

Modified NSMutableAttributedString.setAttributedString(NSAttributedString)

|  | Declaration |
| --- | --- |
| From | ``` func setAttributedString(_ attrString: NSAttributedString!) ``` |
| To | ``` func setAttributedString(_ attrString: NSAttributedString) ``` |

Modified NSMutableAttributedString.setAttributes([NSObject: AnyObject]?, range: NSRange)

|  | Declaration |
| --- | --- |
| From | ``` func setAttributes(_ attrs: [NSObject : AnyObject]!, range range: NSRange) ``` |
| To | ``` func setAttributes(_ attrs: [NSObject : AnyObject]?, range range: NSRange) ``` |

Modified NSMutableCharacterSet.addCharactersInString(String)

|  | Declaration |
| --- | --- |
| From | ``` func addCharactersInString(_ aString: String!) ``` |
| To | ``` func addCharactersInString(_ aString: String) ``` |

Modified NSMutableCharacterSet.alphanumericCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func alphanumericCharacterSet() -> NSMutableCharacterSet! ``` |
| To | ``` class func alphanumericCharacterSet() -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.init(bitmapRepresentation: NSData)

|  | Declaration |
| --- | --- |
| From | ``` init(bitmapRepresentation data: NSData!) -> NSMutableCharacterSet ``` |
| To | ``` init(bitmapRepresentation data: NSData) -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.capitalizedLetterCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func capitalizedLetterCharacterSet() -> NSMutableCharacterSet! ``` |
| To | ``` class func capitalizedLetterCharacterSet() -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.init(charactersInString: String)

|  | Declaration |
| --- | --- |
| From | ``` init(charactersInString aString: String!) -> NSMutableCharacterSet ``` |
| To | ``` init(charactersInString aString: String) -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.init(contentsOfFile: String)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfFile fName: String!) -> NSMutableCharacterSet ``` |
| To | ``` init?(contentsOfFile fName: String) -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.controlCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func controlCharacterSet() -> NSMutableCharacterSet! ``` |
| To | ``` class func controlCharacterSet() -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.decimalDigitCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func decimalDigitCharacterSet() -> NSMutableCharacterSet! ``` |
| To | ``` class func decimalDigitCharacterSet() -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.decomposableCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func decomposableCharacterSet() -> NSMutableCharacterSet! ``` |
| To | ``` class func decomposableCharacterSet() -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.formIntersectionWithCharacterSet(NSCharacterSet)

|  | Declaration |
| --- | --- |
| From | ``` func formIntersectionWithCharacterSet(_ otherSet: NSCharacterSet!) ``` |
| To | ``` func formIntersectionWithCharacterSet(_ otherSet: NSCharacterSet) ``` |

Modified NSMutableCharacterSet.formUnionWithCharacterSet(NSCharacterSet)

|  | Declaration |
| --- | --- |
| From | ``` func formUnionWithCharacterSet(_ otherSet: NSCharacterSet!) ``` |
| To | ``` func formUnionWithCharacterSet(_ otherSet: NSCharacterSet) ``` |

Modified NSMutableCharacterSet.illegalCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func illegalCharacterSet() -> NSMutableCharacterSet! ``` |
| To | ``` class func illegalCharacterSet() -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.letterCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func letterCharacterSet() -> NSMutableCharacterSet! ``` |
| To | ``` class func letterCharacterSet() -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.lowercaseLetterCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func lowercaseLetterCharacterSet() -> NSMutableCharacterSet! ``` |
| To | ``` class func lowercaseLetterCharacterSet() -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.newlineCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func newlineCharacterSet() -> NSMutableCharacterSet! ``` | OS X 10.10 |
| To | ``` class func newlineCharacterSet() -> NSMutableCharacterSet ``` | OS X 10.5 |

Modified NSMutableCharacterSet.nonBaseCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func nonBaseCharacterSet() -> NSMutableCharacterSet! ``` |
| To | ``` class func nonBaseCharacterSet() -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.punctuationCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func punctuationCharacterSet() -> NSMutableCharacterSet! ``` |
| To | ``` class func punctuationCharacterSet() -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.removeCharactersInString(String)

|  | Declaration |
| --- | --- |
| From | ``` func removeCharactersInString(_ aString: String!) ``` |
| To | ``` func removeCharactersInString(_ aString: String) ``` |

Modified NSMutableCharacterSet.symbolCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func symbolCharacterSet() -> NSMutableCharacterSet! ``` |
| To | ``` class func symbolCharacterSet() -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.uppercaseLetterCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func uppercaseLetterCharacterSet() -> NSMutableCharacterSet! ``` |
| To | ``` class func uppercaseLetterCharacterSet() -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.whitespaceAndNewlineCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func whitespaceAndNewlineCharacterSet() -> NSMutableCharacterSet! ``` |
| To | ``` class func whitespaceAndNewlineCharacterSet() -> NSMutableCharacterSet ``` |

Modified NSMutableCharacterSet.whitespaceCharacterSet() -> NSMutableCharacterSet [class]

|  | Declaration |
| --- | --- |
| From | ``` class func whitespaceCharacterSet() -> NSMutableCharacterSet! ``` |
| To | ``` class func whitespaceCharacterSet() -> NSMutableCharacterSet ``` |

Modified NSMutableCopying.mutableCopyWithZone(NSZone) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func mutableCopyWithZone(_ zone: NSZone) -> AnyObject! ``` |
| To | ``` func mutableCopyWithZone(_ zone: NSZone) -> AnyObject? ``` |

Modified NSMutableData.appendBytes(UnsafePointer<Void>, length: Int)

|  | Declaration |
| --- | --- |
| From | ``` func appendBytes(_ bytes: ConstUnsafePointer<()>, length length: Int) ``` |
| To | ``` func appendBytes(_ bytes: UnsafePointer<Void>, length length: Int) ``` |

Modified NSMutableData.appendData(NSData)

|  | Declaration |
| --- | --- |
| From | ``` func appendData(_ other: NSData!) ``` |
| To | ``` func appendData(_ other: NSData) ``` |

Modified NSMutableData.init(capacity: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(capacity capacity: Int) ``` |
| To | ``` init?(capacity capacity: Int) ``` |

Modified NSMutableData.init(length: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(length length: Int) ``` |
| To | ``` init?(length length: Int) ``` |

Modified NSMutableData.mutableBytes

|  | Declaration |
| --- | --- |
| From | ``` var mutableBytes: UnsafePointer<()> { get } ``` |
| To | ``` var mutableBytes: UnsafeMutablePointer<Void> { get } ``` |

Modified NSMutableData.replaceBytesInRange(NSRange, withBytes: UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func replaceBytesInRange(_ range: NSRange, withBytes bytes: ConstUnsafePointer<()>) ``` |
| To | ``` func replaceBytesInRange(_ range: NSRange, withBytes bytes: UnsafePointer<Void>) ``` |

Modified NSMutableData.replaceBytesInRange(NSRange, withBytes: UnsafePointer<Void>, length: Int)

|  | Declaration |
| --- | --- |
| From | ``` func replaceBytesInRange(_ range: NSRange, withBytes replacementBytes: ConstUnsafePointer<()>, length replacementLength: Int) ``` |
| To | ``` func replaceBytesInRange(_ range: NSRange, withBytes replacementBytes: UnsafePointer<Void>, length replacementLength: Int) ``` |

Modified NSMutableData.setData(NSData)

|  | Declaration |
| --- | --- |
| From | ``` func setData(_ data: NSData!) ``` |
| To | ``` func setData(_ data: NSData) ``` |

Modified NSMutableDictionary

|  | Protocols |
| --- | --- |
| From | AnyObject, Sequence |
| To | AnyObject |

Modified NSMutableDictionary.addEntriesFromDictionary([NSObject: AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func addEntriesFromDictionary(_ otherDictionary: [NSObject : AnyObject]!) ``` |
| To | ``` func addEntriesFromDictionary(_ otherDictionary: [NSObject : AnyObject]) ``` |

Modified NSMutableDictionary.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSMutableDictionary.removeObjectForKey(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func removeObjectForKey(_ aKey: AnyObject!) ``` |
| To | ``` func removeObjectForKey(_ aKey: AnyObject) ``` |

Modified NSMutableDictionary.removeObjectsForKeys([AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func removeObjectsForKeys(_ keyArray: [AnyObject]!) ``` |
| To | ``` func removeObjectsForKeys(_ keyArray: [AnyObject]) ``` |

Modified NSMutableDictionary.setDictionary([NSObject: AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func setDictionary(_ otherDictionary: [NSObject : AnyObject]!) ``` |
| To | ``` func setDictionary(_ otherDictionary: [NSObject : AnyObject]) ``` |

Modified NSMutableDictionary.setObject(AnyObject, forKey: NSCopying)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ anObject: AnyObject!, forKey aKey: NSCopying!) ``` |
| To | ``` func setObject(_ anObject: AnyObject, forKey aKey: NSCopying) ``` |

Modified NSMutableDictionary.setValue(AnyObject?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ value: AnyObject!, forKey key: String!) ``` |
| To | ``` func setValue(_ value: AnyObject?, forKey key: String) ``` |

Modified NSMutableDictionary.init(sharedKeySet: AnyObject)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(sharedKeySet keyset: AnyObject!) -> NSMutableDictionary ``` | OS X 10.10 |
| To | ``` init(sharedKeySet keyset: AnyObject) -> NSMutableDictionary ``` | OS X 10.8 |

Modified NSMutableIndexSet.addIndexes(NSIndexSet)

|  | Declaration |
| --- | --- |
| From | ``` func addIndexes(_ indexSet: NSIndexSet!) ``` |
| To | ``` func addIndexes(_ indexSet: NSIndexSet) ``` |

Modified NSMutableIndexSet.removeIndexes(NSIndexSet)

|  | Declaration |
| --- | --- |
| From | ``` func removeIndexes(_ indexSet: NSIndexSet!) ``` |
| To | ``` func removeIndexes(_ indexSet: NSIndexSet) ``` |

Modified NSMutableOrderedSet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSMutableOrderedSet.addObject(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func addObject(_ object: AnyObject!) ``` |
| To | ``` func addObject(_ object: AnyObject) ``` |

Modified NSMutableOrderedSet.addObjects(UnsafePointer<AnyObject?>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` func addObjects(_ objects: ConstUnsafePointer<AnyObject?>, count count: Int) ``` |
| To | ``` func addObjects(_ objects: UnsafePointer<AnyObject?>, count count: Int) ``` |

Modified NSMutableOrderedSet.addObjectsFromArray([AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func addObjectsFromArray(_ array: [AnyObject]!) ``` |
| To | ``` func addObjectsFromArray(_ array: [AnyObject]) ``` |

Modified NSMutableOrderedSet.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSMutableOrderedSet.filterUsingPredicate(NSPredicate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func filterUsingPredicate(_ p: NSPredicate!) ``` | OS X 10.10 |
| To | ``` func filterUsingPredicate(_ p: NSPredicate) ``` | OS X 10.7 |

Modified NSMutableOrderedSet.insertObject(AnyObject, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insertObject(_ object: AnyObject!, atIndex idx: Int) ``` |
| To | ``` func insertObject(_ object: AnyObject, atIndex idx: Int) ``` |

Modified NSMutableOrderedSet.insertObjects([AnyObject], atIndexes: NSIndexSet)

|  | Declaration |
| --- | --- |
| From | ``` func insertObjects(_ objects: [AnyObject]!, atIndexes indexes: NSIndexSet!) ``` |
| To | ``` func insertObjects(_ objects: [AnyObject], atIndexes indexes: NSIndexSet) ``` |

Modified NSMutableOrderedSet.intersectOrderedSet(NSOrderedSet)

|  | Declaration |
| --- | --- |
| From | ``` func intersectOrderedSet(_ other: NSOrderedSet!) ``` |
| To | ``` func intersectOrderedSet(_ other: NSOrderedSet) ``` |

Modified NSMutableOrderedSet.intersectSet(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func intersectSet(_ other: NSSet!) ``` | OS X 10.10 |
| To | ``` func intersectSet(_ other: Set<NSObject>) ``` | OS X 10.10.3 |

Modified NSMutableOrderedSet.minusOrderedSet(NSOrderedSet)

|  | Declaration |
| --- | --- |
| From | ``` func minusOrderedSet(_ other: NSOrderedSet!) ``` |
| To | ``` func minusOrderedSet(_ other: NSOrderedSet) ``` |

Modified NSMutableOrderedSet.minusSet(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func minusSet(_ other: NSSet!) ``` | OS X 10.10 |
| To | ``` func minusSet(_ other: Set<NSObject>) ``` | OS X 10.10.3 |

Modified NSMutableOrderedSet.moveObjectsAtIndexes(NSIndexSet, toIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func moveObjectsAtIndexes(_ indexes: NSIndexSet!, toIndex idx: Int) ``` |
| To | ``` func moveObjectsAtIndexes(_ indexes: NSIndexSet, toIndex idx: Int) ``` |

Modified NSMutableOrderedSet.removeObject(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func removeObject(_ object: AnyObject!) ``` |
| To | ``` func removeObject(_ object: AnyObject) ``` |

Modified NSMutableOrderedSet.removeObjectsAtIndexes(NSIndexSet)

|  | Declaration |
| --- | --- |
| From | ``` func removeObjectsAtIndexes(_ indexes: NSIndexSet!) ``` |
| To | ``` func removeObjectsAtIndexes(_ indexes: NSIndexSet) ``` |

Modified NSMutableOrderedSet.removeObjectsInArray([AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func removeObjectsInArray(_ array: [AnyObject]!) ``` |
| To | ``` func removeObjectsInArray(_ array: [AnyObject]) ``` |

Modified NSMutableOrderedSet.replaceObjectAtIndex(Int, withObject: AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func replaceObjectAtIndex(_ idx: Int, withObject object: AnyObject!) ``` |
| To | ``` func replaceObjectAtIndex(_ idx: Int, withObject object: AnyObject) ``` |

Modified NSMutableOrderedSet.replaceObjectsAtIndexes(NSIndexSet, withObjects:[AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func replaceObjectsAtIndexes(_ indexes: NSIndexSet!, withObjects objects: [AnyObject]!) ``` |
| To | ``` func replaceObjectsAtIndexes(_ indexes: NSIndexSet, withObjects objects: [AnyObject]) ``` |

Modified NSMutableOrderedSet.replaceObjectsInRange(NSRange, withObjects: UnsafePointer<AnyObject?>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` func replaceObjectsInRange(_ range: NSRange, withObjects objects: ConstUnsafePointer<AnyObject?>, count count: Int) ``` |
| To | ``` func replaceObjectsInRange(_ range: NSRange, withObjects objects: UnsafePointer<AnyObject?>, count count: Int) ``` |

Modified NSMutableOrderedSet.setObject(AnyObject, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ obj: AnyObject!, atIndex idx: Int) ``` |
| To | ``` func setObject(_ obj: AnyObject, atIndex idx: Int) ``` |

Modified NSMutableOrderedSet.sortRange(NSRange, options: NSSortOptions, usingComparator: NSComparator)

|  | Declaration |
| --- | --- |
| From | ``` func sortRange(_ range: NSRange, options opts: NSSortOptions, usingComparator cmptr: NSComparator!) ``` |
| To | ``` func sortRange(_ range: NSRange, options opts: NSSortOptions, usingComparator cmptr: NSComparator) ``` |

Modified NSMutableOrderedSet.sortUsingComparator(NSComparator)

|  | Declaration |
| --- | --- |
| From | ``` func sortUsingComparator(_ cmptr: NSComparator!) ``` |
| To | ``` func sortUsingComparator(_ cmptr: NSComparator) ``` |

Modified NSMutableOrderedSet.sortUsingDescriptors([AnyObject])

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sortUsingDescriptors(_ sortDescriptors: [AnyObject]!) ``` | OS X 10.10 |
| To | ``` func sortUsingDescriptors(_ sortDescriptors: [AnyObject]) ``` | OS X 10.7 |

Modified NSMutableOrderedSet.sortWithOptions(NSSortOptions, usingComparator: NSComparator)

|  | Declaration |
| --- | --- |
| From | ``` func sortWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator!) ``` |
| To | ``` func sortWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) ``` |

Modified NSMutableOrderedSet.unionOrderedSet(NSOrderedSet)

|  | Declaration |
| --- | --- |
| From | ``` func unionOrderedSet(_ other: NSOrderedSet!) ``` |
| To | ``` func unionOrderedSet(_ other: NSOrderedSet) ``` |

Modified NSMutableOrderedSet.unionSet(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func unionSet(_ other: NSSet!) ``` | OS X 10.10 |
| To | ``` func unionSet(_ other: Set<NSObject>) ``` | OS X 10.10.3 |

Modified NSMutableSet

|  | Protocols |
| --- | --- |
| From | AnyObject, Sequence |
| To | AnyObject |

Modified NSMutableSet.addObject(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func addObject(_ object: AnyObject!) ``` |
| To | ``` func addObject(_ object: AnyObject) ``` |

Modified NSMutableSet.addObjectsFromArray([AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func addObjectsFromArray(_ array: [AnyObject]!) ``` |
| To | ``` func addObjectsFromArray(_ array: [AnyObject]) ``` |

Modified NSMutableSet.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSMutableSet.filterUsingPredicate(NSPredicate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func filterUsingPredicate(_ predicate: NSPredicate!) ``` | OS X 10.10 |
| To | ``` func filterUsingPredicate(_ predicate: NSPredicate) ``` | OS X 10.5 |

Modified NSMutableSet.intersectSet(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func intersectSet(_ otherSet: NSSet!) ``` | OS X 10.10 |
| To | ``` func intersectSet(_ otherSet: Set<NSObject>) ``` | OS X 10.10.3 |

Modified NSMutableSet.minusSet(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func minusSet(_ otherSet: NSSet!) ``` | OS X 10.10 |
| To | ``` func minusSet(_ otherSet: Set<NSObject>) ``` | OS X 10.10.3 |

Modified NSMutableSet.removeObject(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func removeObject(_ object: AnyObject!) ``` |
| To | ``` func removeObject(_ object: AnyObject) ``` |

Modified NSMutableSet.setSet(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setSet(_ otherSet: NSSet!) ``` | OS X 10.10 |
| To | ``` func setSet(_ otherSet: Set<NSObject>) ``` | OS X 10.10.3 |

Modified NSMutableSet.unionSet(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func unionSet(_ otherSet: NSSet!) ``` | OS X 10.10 |
| To | ``` func unionSet(_ otherSet: Set<NSObject>) ``` | OS X 10.10.3 |

Modified NSMutableString.appendString(String)

|  | Declaration |
| --- | --- |
| From | ``` func appendString(_ aString: String!) ``` |
| To | ``` func appendString(_ aString: String) ``` |

Modified NSMutableString.insertString(String, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insertString(_ aString: String!, atIndex loc: Int) ``` |
| To | ``` func insertString(_ aString: String, atIndex loc: Int) ``` |

Modified NSMutableString.replaceCharactersInRange(NSRange, withString: String)

|  | Declaration |
| --- | --- |
| From | ``` func replaceCharactersInRange(_ range: NSRange, withString aString: String!) ``` |
| To | ``` func replaceCharactersInRange(_ range: NSRange, withString aString: String) ``` |

Modified NSMutableString.replaceOccurrencesOfString(String, withString: String, options: NSStringCompareOptions, range: NSRange) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func replaceOccurrencesOfString(_ target: String!, withString replacement: String!, options options: NSStringCompareOptions, range searchRange: NSRange) -> Int ``` |
| To | ``` func replaceOccurrencesOfString(_ target: String, withString replacement: String, options options: NSStringCompareOptions, range searchRange: NSRange) -> Int ``` |

Modified NSMutableString.setString(String)

|  | Declaration |
| --- | --- |
| From | ``` func setString(_ aString: String!) ``` |
| To | ``` func setString(_ aString: String) ``` |

Modified NSMutableURLRequest.HTTPBody

|  | Declaration |
| --- | --- |
| From | ``` var HTTPBody: NSData! ``` |
| To | ``` @NSCopying var HTTPBody: NSData? ``` |

Modified NSMutableURLRequest.HTTPBodyStream

|  | Declaration |
| --- | --- |
| From | ``` var HTTPBodyStream: NSInputStream! ``` |
| To | ``` var HTTPBodyStream: NSInputStream? ``` |

Modified NSMutableURLRequest.HTTPMethod

|  | Declaration |
| --- | --- |
| From | ``` var HTTPMethod: String! ``` |
| To | ``` var HTTPMethod: String ``` |

Modified NSMutableURLRequest.HTTPShouldUsePipelining

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSMutableURLRequest.URL

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL! ``` |
| To | ``` @NSCopying var URL: NSURL? ``` |

Modified NSMutableURLRequest.addValue(String?, forHTTPHeaderField: String)

|  | Declaration |
| --- | --- |
| From | ``` func addValue(_ value: String!, forHTTPHeaderField field: String!) ``` |
| To | ``` func addValue(_ value: String?, forHTTPHeaderField field: String) ``` |

Modified NSMutableURLRequest.allHTTPHeaderFields

|  | Declaration |
| --- | --- |
| From | ``` var allHTTPHeaderFields: [NSObject : AnyObject]! ``` |
| To | ``` var allHTTPHeaderFields: [NSObject : AnyObject]? ``` |

Modified NSMutableURLRequest.allowsCellularAccess

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSMutableURLRequest.mainDocumentURL

|  | Declaration |
| --- | --- |
| From | ``` var mainDocumentURL: NSURL! ``` |
| To | ``` @NSCopying var mainDocumentURL: NSURL? ``` |

Modified NSMutableURLRequest.networkServiceType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSMutableURLRequest.setValue(String?, forHTTPHeaderField: String)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ value: String!, forHTTPHeaderField field: String!) ``` |
| To | ``` func setValue(_ value: String?, forHTTPHeaderField field: String) ``` |

Modified NSNameSpecifier.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder inCoder: NSCoder!) ``` |
| To | ``` init?(coder inCoder: NSCoder) ``` |

Modified NSNameSpecifier.init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier, key: String, name: String)

|  | Declaration |
| --- | --- |
| From | ``` init(containerClassDescription classDesc: NSScriptClassDescription!, containerSpecifier container: NSScriptObjectSpecifier!, key property: String!, name name: String!) ``` |
| To | ``` init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier, key property: String, name name: String) ``` |

Modified NSNameSpecifier.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String ``` |

Modified NSNetService.addresses

|  | Declaration |
| --- | --- |
| From | ``` var addresses: [AnyObject]! { get } ``` |
| To | ``` var addresses: [AnyObject]? { get } ``` |

Modified NSNetService.dataFromTXTRecordDictionary([NSObject: AnyObject]) -> NSData [class]

|  | Declaration |
| --- | --- |
| From | ``` class func dataFromTXTRecordDictionary(_ txtDictionary: [NSObject : AnyObject]!) -> NSData! ``` |
| To | ``` class func dataFromTXTRecordDictionary(_ txtDictionary: [NSObject : AnyObject]) -> NSData ``` |

Modified NSNetService.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: NSNetServiceDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: NSNetServiceDelegate? ``` |

Modified NSNetService.dictionaryFromTXTRecordData(NSData) -> [NSObject: AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func dictionaryFromTXTRecordData(_ txtData: NSData!) -> [NSObject : AnyObject]! ``` |
| To | ``` class func dictionaryFromTXTRecordData(_ txtData: NSData) -> [NSObject : AnyObject] ``` |

Modified NSNetService.init(domain: String, type: String, name: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(domain domain: String!, type type: String!, name name: String!) ``` |
| To | ``` convenience init!(domain domain: String, type type: String, name name: String) ``` |

Modified NSNetService.init(domain: String, type: String, name: String, port: Int32)

|  | Declaration |
| --- | --- |
| From | ``` init(domain domain: String!, type type: String!, name name: String!, port port: Int32) ``` |
| To | ``` init!(domain domain: String, type type: String, name name: String, port port: Int32) ``` |

Modified NSNetService.getInputStream(UnsafeMutablePointer<NSInputStream?>, outputStream: UnsafeMutablePointer<NSOutputStream?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getInputStream(_ inputStream: UnsafePointer<NSInputStream?>, outputStream outputStream: UnsafePointer<NSOutputStream?>) -> Bool ``` |
| To | ``` func getInputStream(_ inputStream: UnsafeMutablePointer<NSInputStream?>, outputStream outputStream: UnsafeMutablePointer<NSOutputStream?>) -> Bool ``` |

Modified NSNetService.hostName

|  | Declaration |
| --- | --- |
| From | ``` var hostName: String! { get } ``` |
| To | ``` var hostName: String? { get } ``` |

Modified NSNetService.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified NSNetService.port

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSNetService.publishWithOptions(NSNetServiceOptions)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSNetService.removeFromRunLoop(NSRunLoop, forMode: String)

|  | Declaration |
| --- | --- |
| From | ``` func removeFromRunLoop(_ aRunLoop: NSRunLoop!, forMode mode: String!) ``` |
| To | ``` func removeFromRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String) ``` |

Modified NSNetService.scheduleInRunLoop(NSRunLoop, forMode: String)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleInRunLoop(_ aRunLoop: NSRunLoop!, forMode mode: String!) ``` |
| To | ``` func scheduleInRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String) ``` |

Modified NSNetService.type

|  | Declaration |
| --- | --- |
| From | ``` var type: String! { get } ``` |
| To | ``` var type: String { get } ``` |

Modified NSNetServiceBrowser.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: NSNetServiceBrowserDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: NSNetServiceBrowserDelegate? ``` |

Modified NSNetServiceBrowser.removeFromRunLoop(NSRunLoop, forMode: String)

|  | Declaration |
| --- | --- |
| From | ``` func removeFromRunLoop(_ aRunLoop: NSRunLoop!, forMode mode: String!) ``` |
| To | ``` func removeFromRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String) ``` |

Modified NSNetServiceBrowser.scheduleInRunLoop(NSRunLoop, forMode: String)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleInRunLoop(_ aRunLoop: NSRunLoop!, forMode mode: String!) ``` |
| To | ``` func scheduleInRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String) ``` |

Modified NSNetServiceBrowser.searchForServicesOfType(String, inDomain: String)

|  | Declaration |
| --- | --- |
| From | ``` func searchForServicesOfType(_ type: String!, inDomain domainString: String!) ``` |
| To | ``` func searchForServicesOfType(_ type: String, inDomain domainString: String) ``` |

Modified NSNetServiceBrowserDelegate.netServiceBrowser(NSNetServiceBrowser, didFindDomain: String, moreComing: Bool)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser!, didFindDomain domainString: String!, moreComing moreComing: Bool) ``` | -- |
| To | ``` optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser, didFindDomain domainString: String, moreComing moreComing: Bool) ``` | yes |

Modified NSNetServiceBrowserDelegate.netServiceBrowser(NSNetServiceBrowser, didFindService: NSNetService, moreComing: Bool)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser!, didFindService aNetService: NSNetService!, moreComing moreComing: Bool) ``` | -- |
| To | ``` optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser, didFindService aNetService: NSNetService, moreComing moreComing: Bool) ``` | yes |

Modified NSNetServiceBrowserDelegate.netServiceBrowser(NSNetServiceBrowser, didNotSearch:[NSObject: AnyObject])

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser!, didNotSearch errorDict: [NSObject : AnyObject]!) ``` | -- |
| To | ``` optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser, didNotSearch errorDict: [NSObject : AnyObject]) ``` | yes |

Modified NSNetServiceBrowserDelegate.netServiceBrowser(NSNetServiceBrowser, didRemoveDomain: String, moreComing: Bool)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser!, didRemoveDomain domainString: String!, moreComing moreComing: Bool) ``` | -- |
| To | ``` optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser, didRemoveDomain domainString: String, moreComing moreComing: Bool) ``` | yes |

Modified NSNetServiceBrowserDelegate.netServiceBrowser(NSNetServiceBrowser, didRemoveService: NSNetService, moreComing: Bool)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser!, didRemoveService aNetService: NSNetService!, moreComing moreComing: Bool) ``` | -- |
| To | ``` optional func netServiceBrowser(_ aNetServiceBrowser: NSNetServiceBrowser, didRemoveService aNetService: NSNetService, moreComing moreComing: Bool) ``` | yes |

Modified NSNetServiceBrowserDelegate.netServiceBrowserDidStopSearch(NSNetServiceBrowser)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netServiceBrowserDidStopSearch(_ aNetServiceBrowser: NSNetServiceBrowser!) ``` | -- |
| To | ``` optional func netServiceBrowserDidStopSearch(_ aNetServiceBrowser: NSNetServiceBrowser) ``` | yes |

Modified NSNetServiceBrowserDelegate.netServiceBrowserWillSearch(NSNetServiceBrowser)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netServiceBrowserWillSearch(_ aNetServiceBrowser: NSNetServiceBrowser!) ``` | -- |
| To | ``` optional func netServiceBrowserWillSearch(_ aNetServiceBrowser: NSNetServiceBrowser) ``` | yes |

Modified NSNetServiceDelegate.netService(NSNetService, didAcceptConnectionWithInputStream: NSInputStream, outputStream: NSOutputStream)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func netService(_ sender: NSNetService!, didAcceptConnectionWithInputStream inputStream: NSInputStream!, outputStream outputStream: NSOutputStream!) ``` | OS X 10.10 | -- |
| To | ``` optional func netService(_ sender: NSNetService, didAcceptConnectionWithInputStream inputStream: NSInputStream, outputStream outputStream: NSOutputStream) ``` | OS X 10.9 | yes |

Modified NSNetServiceDelegate.netService(NSNetService, didNotPublish:[NSObject: AnyObject])

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netService(_ sender: NSNetService!, didNotPublish errorDict: [NSObject : AnyObject]!) ``` | -- |
| To | ``` optional func netService(_ sender: NSNetService, didNotPublish errorDict: [NSObject : AnyObject]) ``` | yes |

Modified NSNetServiceDelegate.netService(NSNetService, didNotResolve:[NSObject: AnyObject])

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netService(_ sender: NSNetService!, didNotResolve errorDict: [NSObject : AnyObject]!) ``` | -- |
| To | ``` optional func netService(_ sender: NSNetService, didNotResolve errorDict: [NSObject : AnyObject]) ``` | yes |

Modified NSNetServiceDelegate.netService(NSNetService, didUpdateTXTRecordData: NSData)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netService(_ sender: NSNetService!, didUpdateTXTRecordData data: NSData!) ``` | -- |
| To | ``` optional func netService(_ sender: NSNetService, didUpdateTXTRecordData data: NSData) ``` | yes |

Modified NSNetServiceDelegate.netServiceDidPublish(NSNetService)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netServiceDidPublish(_ sender: NSNetService!) ``` | -- |
| To | ``` optional func netServiceDidPublish(_ sender: NSNetService) ``` | yes |

Modified NSNetServiceDelegate.netServiceDidResolveAddress(NSNetService)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netServiceDidResolveAddress(_ sender: NSNetService!) ``` | -- |
| To | ``` optional func netServiceDidResolveAddress(_ sender: NSNetService) ``` | yes |

Modified NSNetServiceDelegate.netServiceDidStop(NSNetService)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netServiceDidStop(_ sender: NSNetService!) ``` | -- |
| To | ``` optional func netServiceDidStop(_ sender: NSNetService) ``` | yes |

Modified NSNetServiceDelegate.netServiceWillPublish(NSNetService)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netServiceWillPublish(_ sender: NSNetService!) ``` | -- |
| To | ``` optional func netServiceWillPublish(_ sender: NSNetService) ``` | yes |

Modified NSNetServiceDelegate.netServiceWillResolve(NSNetService)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func netServiceWillResolve(_ sender: NSNetService!) ``` | -- |
| To | ``` optional func netServiceWillResolve(_ sender: NSNetService) ``` | yes |

Modified NSNetServiceOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSNetServiceOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var NoAutoRename: NSNetServiceOptions { get }     static var ListenForConnections: NSNetServiceOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSNetServiceOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var NoAutoRename: NSNetServiceOptions { get }     static var ListenForConnections: NSNetServiceOptions { get } } ``` | RawOptionSetType |

Modified NSNetServiceOptions.ListenForConnections

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSNetServiceOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSNotification.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSNotification.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified NSNotification.init(name: String, object: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(name aName: String!, object anObject: AnyObject!) ``` |
| To | ``` convenience init(name aName: String, object anObject: AnyObject?) ``` |

Modified NSNotification.object

|  | Declaration |
| --- | --- |
| From | ``` var object: AnyObject! { get } ``` |
| To | ``` var object: AnyObject? { get } ``` |

Modified NSNotification.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! { get } ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? { get } ``` |

Modified NSNotificationCenter.addObserver(AnyObject, selector: Selector, name: String?, object: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func addObserver(_ observer: AnyObject!, selector aSelector: Selector, name aName: String!, object anObject: AnyObject!) ``` |
| To | ``` func addObserver(_ observer: AnyObject, selector aSelector: Selector, name aName: String?, object anObject: AnyObject?) ``` |

Modified NSNotificationCenter.addObserverForName(String?, object: AnyObject?, queue: NSOperationQueue?, usingBlock:(NSNotification!) -> Void) -> NSObjectProtocol

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func addObserverForName(_ name: String!, object obj: AnyObject!, queue queue: NSOperationQueue!, usingBlock block: ((NSNotification!) -> Void)!) -> NSObjectProtocol! ``` | OS X 10.10 |
| To | ``` func addObserverForName(_ name: String?, object obj: AnyObject?, queue queue: NSOperationQueue?, usingBlock block: (NSNotification!) -> Void) -> NSObjectProtocol ``` | OS X 10.6 |

Modified NSNotificationCenter.defaultCenter() -> NSNotificationCenter [class]

|  | Declaration |
| --- | --- |
| From | ``` class func defaultCenter() -> NSNotificationCenter! ``` |
| To | ``` class func defaultCenter() -> NSNotificationCenter ``` |

Modified NSNotificationCenter.postNotification(NSNotification)

|  | Declaration |
| --- | --- |
| From | ``` func postNotification(_ notification: NSNotification!) ``` |
| To | ``` func postNotification(_ notification: NSNotification) ``` |

Modified NSNotificationCenter.postNotificationName(String, object: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func postNotificationName(_ aName: String!, object anObject: AnyObject!) ``` |
| To | ``` func postNotificationName(_ aName: String, object anObject: AnyObject?) ``` |

Modified NSNotificationCenter.postNotificationName(String, object: AnyObject?, userInfo:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` func postNotificationName(_ aName: String!, object anObject: AnyObject!, userInfo aUserInfo: [NSObject : AnyObject]!) ``` |
| To | ``` func postNotificationName(_ aName: String, object anObject: AnyObject?, userInfo aUserInfo: [NSObject : AnyObject]?) ``` |

Modified NSNotificationCenter.removeObserver(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func removeObserver(_ observer: AnyObject!) ``` |
| To | ``` func removeObserver(_ observer: AnyObject) ``` |

Modified NSNotificationCenter.removeObserver(AnyObject, name: String?, object: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func removeObserver(_ observer: AnyObject!, name aName: String!, object anObject: AnyObject!) ``` |
| To | ``` func removeObserver(_ observer: AnyObject, name aName: String?, object anObject: AnyObject?) ``` |

Modified NSNotificationQueue.defaultQueue() -> NSNotificationQueue [class]

|  | Declaration |
| --- | --- |
| From | ``` class func defaultQueue() -> NSNotificationQueue! ``` |
| To | ``` class func defaultQueue() -> NSNotificationQueue ``` |

Modified NSNotificationQueue.dequeueNotificationsMatching(NSNotification, coalesceMask: Int)

|  | Declaration |
| --- | --- |
| From | ``` func dequeueNotificationsMatching(_ notification: NSNotification!, coalesceMask coalesceMask: Int) ``` |
| To | ``` func dequeueNotificationsMatching(_ notification: NSNotification, coalesceMask coalesceMask: Int) ``` |

Modified NSNotificationQueue.enqueueNotification(NSNotification, postingStyle: NSPostingStyle)

|  | Declaration |
| --- | --- |
| From | ``` func enqueueNotification(_ notification: NSNotification!, postingStyle postingStyle: NSPostingStyle) ``` |
| To | ``` func enqueueNotification(_ notification: NSNotification, postingStyle postingStyle: NSPostingStyle) ``` |

Modified NSNotificationQueue.enqueueNotification(NSNotification, postingStyle: NSPostingStyle, coalesceMask: Int, forModes:[AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` func enqueueNotification(_ notification: NSNotification!, postingStyle postingStyle: NSPostingStyle, coalesceMask coalesceMask: Int, forModes modes: [AnyObject]!) ``` |
| To | ``` func enqueueNotification(_ notification: NSNotification, postingStyle postingStyle: NSPostingStyle, coalesceMask coalesceMask: Int, forModes modes: [AnyObject]?) ``` |

Modified NSNotificationQueue.init(notificationCenter: NSNotificationCenter)

|  | Declaration |
| --- | --- |
| From | ``` init(notificationCenter notificationCenter: NSNotificationCenter!) ``` |
| To | ``` init(notificationCenter notificationCenter: NSNotificationCenter) ``` |

Modified NSNumber

|  | Protocols |
| --- | --- |
| From | AnyObject, BooleanLiteralConvertible, FloatLiteralConvertible, IntegerLiteralConvertible |
| To | AnyObject, BooleanLiteralConvertible, CKRecordValue, FloatLiteralConvertible, IntegerLiteralConvertible, NSObjectProtocol |

Modified NSNumber.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSNumber.compare(NSNumber) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func compare(_ otherNumber: NSNumber!) -> NSComparisonResult ``` |
| To | ``` func compare(_ otherNumber: NSNumber) -> NSComparisonResult ``` |

Modified NSNumber.descriptionWithLocale(AnyObject?) -> String

|  | Declaration |
| --- | --- |
| From | ``` func descriptionWithLocale(_ locale: AnyObject!) -> String! ``` |
| To | ``` func descriptionWithLocale(_ locale: AnyObject?) -> String ``` |

Modified NSNumber.init(integer: Int)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSNumber.integerValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSNumber.isEqualToNumber(NSNumber) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToNumber(_ number: NSNumber!) -> Bool ``` |
| To | ``` func isEqualToNumber(_ number: NSNumber) -> Bool ``` |

Modified NSNumber.stringValue

|  | Declaration |
| --- | --- |
| From | ``` var stringValue: String! { get } ``` |
| To | ``` var stringValue: String { get } ``` |

Modified NSNumber.init(unsignedInteger: Int)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSNumber.unsignedIntegerValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSNumberFormatter.attributedStringForNil

|  | Declaration |
| --- | --- |
| From | ``` var attributedStringForNil: NSAttributedString! ``` |
| To | ``` @NSCopying var attributedStringForNil: NSAttributedString? ``` |

Modified NSNumberFormatter.attributedStringForNotANumber

|  | Declaration |
| --- | --- |
| From | ``` var attributedStringForNotANumber: NSAttributedString! ``` |
| To | ``` @NSCopying var attributedStringForNotANumber: NSAttributedString? ``` |

Modified NSNumberFormatter.attributedStringForZero

|  | Declaration |
| --- | --- |
| From | ``` var attributedStringForZero: NSAttributedString! ``` |
| To | ``` @NSCopying var attributedStringForZero: NSAttributedString ``` |

Modified NSNumberFormatter.currencyCode

|  | Declaration |
| --- | --- |
| From | ``` var currencyCode: String! ``` |
| To | ``` var currencyCode: String ``` |

Modified NSNumberFormatter.currencyDecimalSeparator

|  | Declaration |
| --- | --- |
| From | ``` var currencyDecimalSeparator: String! ``` |
| To | ``` var currencyDecimalSeparator: String? ``` |

Modified NSNumberFormatter.currencyGroupingSeparator

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var currencyGroupingSeparator: String! ``` | OS X 10.10 |
| To | ``` var currencyGroupingSeparator: String? ``` | OS X 10.5 |

Modified NSNumberFormatter.currencySymbol

|  | Declaration |
| --- | --- |
| From | ``` var currencySymbol: String! ``` |
| To | ``` var currencySymbol: String? ``` |

Modified NSNumberFormatter.decimalSeparator

|  | Declaration |
| --- | --- |
| From | ``` var decimalSeparator: String! ``` |
| To | ``` var decimalSeparator: String? ``` |

Modified NSNumberFormatter.exponentSymbol

|  | Declaration |
| --- | --- |
| From | ``` var exponentSymbol: String! ``` |
| To | ``` var exponentSymbol: String ``` |

Modified NSNumberFormatter.format

|  | Declaration |
| --- | --- |
| From | ``` var format: String! ``` |
| To | ``` var format: String ``` |

Modified NSNumberFormatter.getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forString: String, range: UnsafeMutablePointer<NSRange>, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getObjectValue(_ obj: AutoreleasingUnsafePointer<AnyObject?>, forString string: String!, range rangep: UnsafePointer<NSRange>, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>, forString string: String, range rangep: UnsafeMutablePointer<NSRange>, error error: NSErrorPointer) -> Bool ``` |

Modified NSNumberFormatter.internationalCurrencySymbol

|  | Declaration |
| --- | --- |
| From | ``` var internationalCurrencySymbol: String! ``` |
| To | ``` var internationalCurrencySymbol: String? ``` |

Modified NSNumberFormatter.lenient

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSNumberFormatter.locale

|  | Declaration |
| --- | --- |
| From | ``` var locale: NSLocale! ``` |
| To | ``` @NSCopying var locale: NSLocale? ``` |

Modified NSNumberFormatter.localizedStringFromNumber(NSNumber, numberStyle: NSNumberFormatterStyle) -> String [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func localizedStringFromNumber(_ num: NSNumber!, numberStyle nstyle: NSNumberFormatterStyle) -> String! ``` | OS X 10.10 |
| To | ``` class func localizedStringFromNumber(_ num: NSNumber, numberStyle nstyle: NSNumberFormatterStyle) -> String ``` | OS X 10.6 |

Modified NSNumberFormatter.maximum

|  | Declaration |
| --- | --- |
| From | ``` var maximum: NSNumber! ``` |
| To | ``` @NSCopying var maximum: NSNumber! ``` |

Modified NSNumberFormatter.maximumSignificantDigits

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSNumberFormatter.minimum

|  | Declaration |
| --- | --- |
| From | ``` var minimum: NSNumber! ``` |
| To | ``` @NSCopying var minimum: NSNumber! ``` |

Modified NSNumberFormatter.minimumSignificantDigits

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSNumberFormatter.minusSign

|  | Declaration |
| --- | --- |
| From | ``` var minusSign: String! ``` |
| To | ``` var minusSign: String ``` |

Modified NSNumberFormatter.multiplier

|  | Declaration |
| --- | --- |
| From | ``` var multiplier: NSNumber! ``` |
| To | ``` @NSCopying var multiplier: NSNumber? ``` |

Modified NSNumberFormatter.negativeFormat

|  | Declaration |
| --- | --- |
| From | ``` var negativeFormat: String! ``` |
| To | ``` var negativeFormat: String ``` |

Modified NSNumberFormatter.negativeInfinitySymbol

|  | Declaration |
| --- | --- |
| From | ``` var negativeInfinitySymbol: String! ``` |
| To | ``` var negativeInfinitySymbol: String ``` |

Modified NSNumberFormatter.negativePrefix

|  | Declaration |
| --- | --- |
| From | ``` var negativePrefix: String! ``` |
| To | ``` var negativePrefix: String ``` |

Modified NSNumberFormatter.negativeSuffix

|  | Declaration |
| --- | --- |
| From | ``` var negativeSuffix: String! ``` |
| To | ``` var negativeSuffix: String ``` |

Modified NSNumberFormatter.nilSymbol

|  | Declaration |
| --- | --- |
| From | ``` var nilSymbol: String! ``` |
| To | ``` var nilSymbol: String ``` |

Modified NSNumberFormatter.notANumberSymbol

|  | Declaration |
| --- | --- |
| From | ``` var notANumberSymbol: String! ``` |
| To | ``` var notANumberSymbol: String ``` |

Modified NSNumberFormatter.numberFromString(String) -> NSNumber?

|  | Declaration |
| --- | --- |
| From | ``` func numberFromString(_ string: String!) -> NSNumber! ``` |
| To | ``` func numberFromString(_ string: String) -> NSNumber? ``` |

Modified NSNumberFormatter.paddingCharacter

|  | Declaration |
| --- | --- |
| From | ``` var paddingCharacter: String! ``` |
| To | ``` var paddingCharacter: String? ``` |

Modified NSNumberFormatter.partialStringValidationEnabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSNumberFormatter.perMillSymbol

|  | Declaration |
| --- | --- |
| From | ``` var perMillSymbol: String! ``` |
| To | ``` var perMillSymbol: String ``` |

Modified NSNumberFormatter.percentSymbol

|  | Declaration |
| --- | --- |
| From | ``` var percentSymbol: String! ``` |
| To | ``` var percentSymbol: String ``` |

Modified NSNumberFormatter.plusSign

|  | Declaration |
| --- | --- |
| From | ``` var plusSign: String! ``` |
| To | ``` var plusSign: String ``` |

Modified NSNumberFormatter.positiveInfinitySymbol

|  | Declaration |
| --- | --- |
| From | ``` var positiveInfinitySymbol: String! ``` |
| To | ``` var positiveInfinitySymbol: String ``` |

Modified NSNumberFormatter.positivePrefix

|  | Declaration |
| --- | --- |
| From | ``` var positivePrefix: String! ``` |
| To | ``` var positivePrefix: String ``` |

Modified NSNumberFormatter.positiveSuffix

|  | Declaration |
| --- | --- |
| From | ``` var positiveSuffix: String! ``` |
| To | ``` var positiveSuffix: String ``` |

Modified NSNumberFormatter.roundingBehavior

|  | Declaration |
| --- | --- |
| From | ``` var roundingBehavior: NSDecimalNumberHandler! ``` |
| To | ``` @NSCopying var roundingBehavior: NSDecimalNumberHandler? ``` |

Modified NSNumberFormatter.roundingIncrement

|  | Declaration |
| --- | --- |
| From | ``` var roundingIncrement: NSNumber! ``` |
| To | ``` @NSCopying var roundingIncrement: NSNumber? ``` |

Modified NSNumberFormatter.stringFromNumber(NSNumber) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func stringFromNumber(_ number: NSNumber!) -> String! ``` |
| To | ``` func stringFromNumber(_ number: NSNumber) -> String? ``` |

Modified NSNumberFormatter.textAttributesForNegativeInfinity

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForNegativeInfinity: [NSObject : AnyObject]! ``` |
| To | ``` var textAttributesForNegativeInfinity: [NSObject : AnyObject]? ``` |

Modified NSNumberFormatter.textAttributesForNegativeValues

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForNegativeValues: [NSObject : AnyObject]! ``` |
| To | ``` var textAttributesForNegativeValues: [NSObject : AnyObject]? ``` |

Modified NSNumberFormatter.textAttributesForNil

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForNil: [NSObject : AnyObject]! ``` |
| To | ``` var textAttributesForNil: [NSObject : AnyObject]? ``` |

Modified NSNumberFormatter.textAttributesForNotANumber

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForNotANumber: [NSObject : AnyObject]! ``` |
| To | ``` var textAttributesForNotANumber: [NSObject : AnyObject]? ``` |

Modified NSNumberFormatter.textAttributesForPositiveInfinity

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForPositiveInfinity: [NSObject : AnyObject]! ``` |
| To | ``` var textAttributesForPositiveInfinity: [NSObject : AnyObject]? ``` |

Modified NSNumberFormatter.textAttributesForPositiveValues

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForPositiveValues: [NSObject : AnyObject]! ``` |
| To | ``` var textAttributesForPositiveValues: [NSObject : AnyObject]? ``` |

Modified NSNumberFormatter.textAttributesForZero

|  | Declaration |
| --- | --- |
| From | ``` var textAttributesForZero: [NSObject : AnyObject]! ``` |
| To | ``` var textAttributesForZero: [NSObject : AnyObject]? ``` |

Modified NSNumberFormatter.thousandSeparator

|  | Declaration |
| --- | --- |
| From | ``` var thousandSeparator: String! ``` |
| To | ``` var thousandSeparator: String? ``` |

Modified NSNumberFormatter.usesSignificantDigits

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSNumberFormatter.zeroSymbol

|  | Declaration |
| --- | --- |
| From | ``` var zeroSymbol: String! ``` |
| To | ``` var zeroSymbol: String? ``` |

Modified NSOperatingSystemVersion [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSOperatingSystemVersion {     var majorVersion: Int     var minorVersion: Int     var patchVersion: Int } ``` |
| To | ``` struct NSOperatingSystemVersion {     var majorVersion: Int     var minorVersion: Int     var patchVersion: Int     init()     init(majorVersion majorVersion: Int, minorVersion minorVersion: Int, patchVersion patchVersion: Int) } ``` |

Modified NSOperation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSOperation.addDependency(NSOperation)

|  | Declaration |
| --- | --- |
| From | ``` func addDependency(_ op: NSOperation!) ``` |
| To | ``` func addDependency(_ op: NSOperation) ``` |

Modified NSOperation.asynchronous

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSOperation.completionBlock

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var completionBlock: (() -> Void)! ``` | OS X 10.10 |
| To | ``` var completionBlock: (() -> Void)? ``` | OS X 10.6 |

Modified NSOperation.dependencies

|  | Declaration |
| --- | --- |
| From | ``` var dependencies: [AnyObject]! { get } ``` |
| To | ``` var dependencies: [AnyObject] { get } ``` |

Modified NSOperation.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified NSOperation.removeDependency(NSOperation)

|  | Declaration |
| --- | --- |
| From | ``` func removeDependency(_ op: NSOperation!) ``` |
| To | ``` func removeDependency(_ op: NSOperation) ``` |

Modified NSOperation.threadPriority

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.6 | OS X 10.10 |

Modified NSOperation.waitUntilFinished()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSOperationQueue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSOperationQueue.addOperation(NSOperation)

|  | Declaration |
| --- | --- |
| From | ``` func addOperation(_ op: NSOperation!) ``` |
| To | ``` func addOperation(_ op: NSOperation) ``` |

Modified NSOperationQueue.addOperationWithBlock(() -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func addOperationWithBlock(_ block: (() -> Void)!) ``` | OS X 10.10 |
| To | ``` func addOperationWithBlock(_ block: () -> Void) ``` | OS X 10.6 |

Modified NSOperationQueue.addOperations([AnyObject], waitUntilFinished: Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func addOperations(_ ops: [AnyObject]!, waitUntilFinished wait: Bool) ``` | OS X 10.10 |
| To | ``` func addOperations(_ ops: [AnyObject], waitUntilFinished wait: Bool) ``` | OS X 10.6 |

Modified NSOperationQueue.currentQueue() -> NSOperationQueue? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func currentQueue() -> NSOperationQueue! ``` | OS X 10.10 |
| To | ``` class func currentQueue() -> NSOperationQueue? ``` | OS X 10.6 |

Modified NSOperationQueue.mainQueue() -> NSOperationQueue [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func mainQueue() -> NSOperationQueue! ``` | OS X 10.10 |
| To | ``` class func mainQueue() -> NSOperationQueue ``` | OS X 10.6 |

Modified NSOperationQueue.name

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var name: String! ``` | OS X 10.10 |
| To | ``` var name: String? ``` | OS X 10.6 |

Modified NSOperationQueue.operationCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSOperationQueue.operations

|  | Declaration |
| --- | --- |
| From | ``` var operations: [AnyObject]! { get } ``` |
| To | ``` var operations: [AnyObject] { get } ``` |

Modified NSOperationQueue.underlyingQueue

|  | Declaration |
| --- | --- |
| From | ``` var underlyingQueue: dispatch_queue_t! ``` |
| To | ``` unowned(unsafe) var underlyingQueue: dispatch_queue_t ``` |

Modified NSOrderedSet

|  | Protocols | Introduction |
| --- | --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding | OS X 10.10 |
| To | AnyObject, ArrayLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, SequenceType | OS X 10.7 |

Modified NSOrderedSet.addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func addObserver(_ observer: NSObject!, forKeyPath keyPath: String!, options options: NSKeyValueObservingOptions, context context: UnsafePointer<()>) ``` |
| To | ``` func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>) ``` |

Modified NSOrderedSet.array

|  | Declaration |
| --- | --- |
| From | ``` var array: [AnyObject]! { get } ``` |
| To | ``` var array: [AnyObject] { get } ``` |

Modified NSOrderedSet.init(array: [AnyObject], copyItems: Bool)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(array set: [AnyObject]!, copyItems flag: Bool) ``` |
| To | ``` convenience init(array set: [AnyObject], copyItems flag: Bool) ``` |

Modified NSOrderedSet.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSOrderedSet.containsObject(AnyObject) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func containsObject(_ object: AnyObject!) -> Bool ``` |
| To | ``` func containsObject(_ object: AnyObject) -> Bool ``` |

Modified NSOrderedSet.description

|  | Declaration |
| --- | --- |
| From | ``` var description: String! { get } ``` |
| To | ``` var description: String { get } ``` |

Modified NSOrderedSet.descriptionWithLocale(AnyObject?) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func descriptionWithLocale(_ locale: AnyObject!) -> String! ``` |
| To | ``` func descriptionWithLocale(_ locale: AnyObject?) -> String? ``` |

Modified NSOrderedSet.descriptionWithLocale(AnyObject?, indent: Int) -> String

|  | Declaration |
| --- | --- |
| From | ``` func descriptionWithLocale(_ locale: AnyObject!, indent level: Int) -> String! ``` |
| To | ``` func descriptionWithLocale(_ locale: AnyObject?, indent level: Int) -> String ``` |

Modified NSOrderedSet.enumerateObjectsAtIndexes(NSIndexSet, options: NSEnumerationOptions, usingBlock:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsAtIndexes(_ s: NSIndexSet!, options opts: NSEnumerationOptions, usingBlock block: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified NSOrderedSet.enumerateObjectsUsingBlock((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsUsingBlock(_ block: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateObjectsUsingBlock(_ block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified NSOrderedSet.enumerateObjectsWithOptions(NSEnumerationOptions, usingBlock:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified NSOrderedSet.filteredOrderedSetUsingPredicate(NSPredicate) -> NSOrderedSet

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func filteredOrderedSetUsingPredicate(_ p: NSPredicate!) -> NSOrderedSet! ``` | OS X 10.10 |
| To | ``` func filteredOrderedSetUsingPredicate(_ p: NSPredicate) -> NSOrderedSet ``` | OS X 10.7 |

Modified NSOrderedSet.firstObject

|  | Declaration |
| --- | --- |
| From | ``` var firstObject: AnyObject! { get } ``` |
| To | ``` var firstObject: AnyObject? { get } ``` |

Modified NSOrderedSet.getObjects(AutoreleasingUnsafeMutablePointer<AnyObject?>, range: NSRange)

|  | Declaration |
| --- | --- |
| From | ``` func getObjects(_ objects: AutoreleasingUnsafePointer<AnyObject?>, range range: NSRange) ``` |
| To | ``` func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, range range: NSRange) ``` |

Modified NSOrderedSet.indexOfObject(AnyObject) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObject(_ object: AnyObject!) -> Int ``` |
| To | ``` func indexOfObject(_ object: AnyObject) -> Int ``` |

Modified NSOrderedSet.indexOfObject(AnyObject, inSortedRange: NSRange, options: NSBinarySearchingOptions, usingComparator: NSComparator) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObject(_ object: AnyObject!, inSortedRange range: NSRange, options opts: NSBinarySearchingOptions, usingComparator cmp: NSComparator!) -> Int ``` |
| To | ``` func indexOfObject(_ object: AnyObject, inSortedRange range: NSRange, options opts: NSBinarySearchingOptions, usingComparator cmp: NSComparator) -> Int ``` |

Modified NSOrderedSet.indexOfObjectAtIndexes(NSIndexSet, options: NSEnumerationOptions, passingTest:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObjectAtIndexes(_ s: NSIndexSet!, options opts: NSEnumerationOptions, passingTest predicate: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Bool)!) -> Int ``` |
| To | ``` func indexOfObjectAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |

Modified NSOrderedSet.indexOfObjectPassingTest((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObjectPassingTest(_ predicate: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Bool)!) -> Int ``` |
| To | ``` func indexOfObjectPassingTest(_ predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |

Modified NSOrderedSet.indexOfObjectWithOptions(NSEnumerationOptions, passingTest:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Bool)!) -> Int ``` |
| To | ``` func indexOfObjectWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int ``` |

Modified NSOrderedSet.indexesOfObjectsAtIndexes(NSIndexSet, options: NSEnumerationOptions, passingTest:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Declaration |
| --- | --- |
| From | ``` func indexesOfObjectsAtIndexes(_ s: NSIndexSet!, options opts: NSEnumerationOptions, passingTest predicate: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Bool)!) -> NSIndexSet! ``` |
| To | ``` func indexesOfObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |

Modified NSOrderedSet.indexesOfObjectsPassingTest((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Declaration |
| --- | --- |
| From | ``` func indexesOfObjectsPassingTest(_ predicate: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Bool)!) -> NSIndexSet! ``` |
| To | ``` func indexesOfObjectsPassingTest(_ predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |

Modified NSOrderedSet.indexesOfObjectsWithOptions(NSEnumerationOptions, passingTest:(AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet

|  | Declaration |
| --- | --- |
| From | ``` func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: ((AnyObject!, Int, UnsafePointer<ObjCBool>) -> Bool)!) -> NSIndexSet! ``` |
| To | ``` func indexesOfObjectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> NSIndexSet ``` |

Modified NSOrderedSet.intersectsOrderedSet(NSOrderedSet) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func intersectsOrderedSet(_ other: NSOrderedSet!) -> Bool ``` |
| To | ``` func intersectsOrderedSet(_ other: NSOrderedSet) -> Bool ``` |

Modified NSOrderedSet.intersectsSet(Set<NSObject>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func intersectsSet(_ set: NSSet!) -> Bool ``` | OS X 10.10 |
| To | ``` func intersectsSet(_ set: Set<NSObject>) -> Bool ``` | OS X 10.10.3 |

Modified NSOrderedSet.isEqualToOrderedSet(NSOrderedSet) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToOrderedSet(_ other: NSOrderedSet!) -> Bool ``` |
| To | ``` func isEqualToOrderedSet(_ other: NSOrderedSet) -> Bool ``` |

Modified NSOrderedSet.isSubsetOfOrderedSet(NSOrderedSet) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isSubsetOfOrderedSet(_ other: NSOrderedSet!) -> Bool ``` |
| To | ``` func isSubsetOfOrderedSet(_ other: NSOrderedSet) -> Bool ``` |

Modified NSOrderedSet.isSubsetOfSet(Set<NSObject>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isSubsetOfSet(_ set: NSSet!) -> Bool ``` | OS X 10.10 |
| To | ``` func isSubsetOfSet(_ set: Set<NSObject>) -> Bool ``` | OS X 10.10.3 |

Modified NSOrderedSet.lastObject

|  | Declaration |
| --- | --- |
| From | ``` var lastObject: AnyObject! { get } ``` |
| To | ``` var lastObject: AnyObject? { get } ``` |

Modified NSOrderedSet.objectAtIndex(Int) -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func objectAtIndex(_ idx: Int) -> AnyObject! ``` |
| To | ``` func objectAtIndex(_ idx: Int) -> AnyObject ``` |

Modified NSOrderedSet.objectEnumerator() -> NSEnumerator

|  | Declaration |
| --- | --- |
| From | ``` func objectEnumerator() -> NSEnumerator! ``` |
| To | ``` func objectEnumerator() -> NSEnumerator ``` |

Modified NSOrderedSet.init(objects: UnsafePointer<AnyObject?>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(objects objects: ConstUnsafePointer<AnyObject?>, count cnt: Int) ``` |
| To | ``` init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int) ``` |

Modified NSOrderedSet.objectsAtIndexes(NSIndexSet) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func objectsAtIndexes(_ indexes: NSIndexSet!) -> [AnyObject]! ``` |
| To | ``` func objectsAtIndexes(_ indexes: NSIndexSet) -> [AnyObject] ``` |

Modified NSOrderedSet.init(orderedSet: NSOrderedSet, copyItems: Bool)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(orderedSet set: NSOrderedSet!, copyItems flag: Bool) ``` |
| To | ``` convenience init(orderedSet set: NSOrderedSet, copyItems flag: Bool) ``` |

Modified NSOrderedSet.init(orderedSet: NSOrderedSet?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(orderedSet set: NSOrderedSet!) ``` |
| To | ``` convenience init(orderedSet set: NSOrderedSet?) ``` |

Modified NSOrderedSet.removeObserver(NSObject, forKeyPath: String)

|  | Declaration |
| --- | --- |
| From | ``` func removeObserver(_ observer: NSObject!, forKeyPath keyPath: String!) ``` |
| To | ``` func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) ``` |

Modified NSOrderedSet.removeObserver(NSObject, forKeyPath: String, context: UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func removeObserver(_ observer: NSObject!, forKeyPath keyPath: String!, context context: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>) ``` | OS X 10.7 |

Modified NSOrderedSet.reverseObjectEnumerator() -> NSEnumerator

|  | Declaration |
| --- | --- |
| From | ``` func reverseObjectEnumerator() -> NSEnumerator! ``` |
| To | ``` func reverseObjectEnumerator() -> NSEnumerator ``` |

Modified NSOrderedSet.reversedOrderedSet

|  | Declaration |
| --- | --- |
| From | ``` var reversedOrderedSet: NSOrderedSet! { get } ``` |
| To | ``` @NSCopying var reversedOrderedSet: NSOrderedSet { get } ``` |

Modified NSOrderedSet.set

|  | Declaration |
| --- | --- |
| From | ``` var set: NSSet! { get } ``` |
| To | ``` var set: Set<NSObject> { get } ``` |

Modified NSOrderedSet.init(set: Set<NSObject>?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(set set: NSSet!) ``` | OS X 10.10 |
| To | ``` convenience init(set set: Set<NSObject>?) ``` | OS X 10.10.3 |

Modified NSOrderedSet.init(set: Set<NSObject>?, copyItems: Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(set set: NSSet!, copyItems flag: Bool) ``` | OS X 10.10 |
| To | ``` convenience init(set set: Set<NSObject>?, copyItems flag: Bool) ``` | OS X 10.10.3 |

Modified NSOrderedSet.setValue(AnyObject?, forKey: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setValue(_ value: AnyObject!, forKey key: String!) ``` | OS X 10.10 |
| To | ``` func setValue(_ value: AnyObject?, forKey key: String) ``` | OS X 10.7 |

Modified NSOrderedSet.sortedArrayUsingComparator(NSComparator) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func sortedArrayUsingComparator(_ cmptr: NSComparator!) -> [AnyObject]! ``` |
| To | ``` func sortedArrayUsingComparator(_ cmptr: NSComparator) -> [AnyObject] ``` |

Modified NSOrderedSet.sortedArrayUsingDescriptors([AnyObject]) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sortedArrayUsingDescriptors(_ sortDescriptors: [AnyObject]!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func sortedArrayUsingDescriptors(_ sortDescriptors: [AnyObject]) -> [AnyObject] ``` | OS X 10.7 |

Modified NSOrderedSet.sortedArrayWithOptions(NSSortOptions, usingComparator: NSComparator) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func sortedArrayWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator!) -> [AnyObject]! ``` |
| To | ``` func sortedArrayWithOptions(_ opts: NSSortOptions, usingComparator cmptr: NSComparator) -> [AnyObject] ``` |

Modified NSOrderedSet.valueForKey(String) -> AnyObject

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func valueForKey(_ key: String!) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func valueForKey(_ key: String) -> AnyObject ``` | OS X 10.7 |

Modified NSOrthography

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSOrthography.allLanguages

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var allLanguages: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var allLanguages: [AnyObject] { get } ``` | OS X 10.6 |

Modified NSOrthography.allScripts

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var allScripts: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var allScripts: [AnyObject] { get } ``` | OS X 10.6 |

Modified NSOrthography.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSOrthography.dominantLanguage

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var dominantLanguage: String! { get } ``` | OS X 10.10 |
| To | ``` var dominantLanguage: String { get } ``` | OS X 10.6 |

Modified NSOrthography.dominantLanguageForScript(String) -> String

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func dominantLanguageForScript(_ script: String!) -> String! ``` | OS X 10.10 |
| To | ``` func dominantLanguageForScript(_ script: String) -> String ``` | OS X 10.6 |

Modified NSOrthography.dominantScript

|  | Declaration |
| --- | --- |
| From | ``` var dominantScript: String! { get } ``` |
| To | ``` var dominantScript: String { get } ``` |

Modified NSOrthography.languageMap

|  | Declaration |
| --- | --- |
| From | ``` var languageMap: [NSObject : AnyObject]! { get } ``` |
| To | ``` var languageMap: [NSObject : AnyObject] { get } ``` |

Modified NSOrthography.languagesForScript(String) -> [AnyObject]?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func languagesForScript(_ script: String!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func languagesForScript(_ script: String) -> [AnyObject]? ``` | OS X 10.6 |

Modified NSOutputStream.outputStreamToMemory() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func outputStreamToMemory() -> Self! ``` | OS X 10.10 |
| To | ``` class func outputStreamToMemory() -> Self ``` | OS X 10.10.3 |

Modified NSOutputStream.init(toBuffer: UnsafeMutablePointer<UInt8>, capacity: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(toBuffer buffer: UnsafePointer<UInt8>, capacity capacity: Int) ``` |
| To | ``` init(toBuffer buffer: UnsafeMutablePointer<UInt8>, capacity capacity: Int) ``` |

Modified NSOutputStream.init(toFileAtPath: String, append: Bool)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(toFileAtPath path: String!, append shouldAppend: Bool) ``` |
| To | ``` convenience init?(toFileAtPath path: String, append shouldAppend: Bool) ``` |

Modified NSOutputStream.write(UnsafePointer<UInt8>, maxLength: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func write(_ buffer: ConstUnsafePointer<UInt8>, maxLength len: Int) -> Int ``` |
| To | ``` func write(_ buffer: UnsafePointer<UInt8>, maxLength len: Int) -> Int ``` |

Modified NSPipe.fileHandleForReading

|  | Declaration |
| --- | --- |
| From | ``` var fileHandleForReading: NSFileHandle! { get } ``` |
| To | ``` var fileHandleForReading: NSFileHandle { get } ``` |

Modified NSPipe.fileHandleForWriting

|  | Declaration |
| --- | --- |
| From | ``` var fileHandleForWriting: NSFileHandle! { get } ``` |
| To | ``` var fileHandleForWriting: NSFileHandle { get } ``` |

Modified NSPointerArray

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPointerArray.addPointer(UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func addPointer(_ pointer: UnsafePointer<()>) ``` |
| To | ``` func addPointer(_ pointer: UnsafeMutablePointer<Void>) ``` |

Modified NSPointerArray.allObjects

|  | Declaration |
| --- | --- |
| From | ``` var allObjects: [AnyObject]! { get } ``` |
| To | ``` var allObjects: [AnyObject] { get } ``` |

Modified NSPointerArray.insertPointer(UnsafeMutablePointer<Void>, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insertPointer(_ item: UnsafePointer<()>, atIndex index: Int) ``` |
| To | ``` func insertPointer(_ item: UnsafeMutablePointer<Void>, atIndex index: Int) ``` |

Modified NSPointerArray.pointerAtIndex(Int) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func pointerAtIndex(_ index: Int) -> UnsafePointer<()> ``` |
| To | ``` func pointerAtIndex(_ index: Int) -> UnsafeMutablePointer<Void> ``` |

Modified NSPointerArray.pointerFunctions

|  | Declaration |
| --- | --- |
| From | ``` var pointerFunctions: NSPointerFunctions! { get } ``` |
| To | ``` @NSCopying var pointerFunctions: NSPointerFunctions { get } ``` |

Modified NSPointerArray.init(pointerFunctions: NSPointerFunctions)

|  | Declaration |
| --- | --- |
| From | ``` init(pointerFunctions functions: NSPointerFunctions!) ``` |
| To | ``` init(pointerFunctions functions: NSPointerFunctions) ``` |

Modified NSPointerArray.replacePointerAtIndex(Int, withPointer: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func replacePointerAtIndex(_ index: Int, withPointer item: UnsafePointer<()>) ``` |
| To | ``` func replacePointerAtIndex(_ index: Int, withPointer item: UnsafeMutablePointer<Void>) ``` |

Modified NSPointerArray.strongObjectsPointerArray() -> NSPointerArray [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func strongObjectsPointerArray() -> NSPointerArray! ``` | OS X 10.10 |
| To | ``` class func strongObjectsPointerArray() -> NSPointerArray ``` | OS X 10.8 |

Modified NSPointerArray.weakObjectsPointerArray() -> NSPointerArray [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func weakObjectsPointerArray() -> NSPointerArray! ``` | OS X 10.10 |
| To | ``` class func weakObjectsPointerArray() -> NSPointerArray ``` | OS X 10.8 |

Modified NSPointerFunctions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPointerFunctions.acquireFunction

|  | Declaration |
| --- | --- |
| From | ``` var acquireFunction: CFunctionPointer<((ConstUnsafePointer<()>, CFunctionPointer<((ConstUnsafePointer<()>) -> Int)>, Bool) -> UnsafePointer<()>)> ``` |
| To | ``` var acquireFunction: CFunctionPointer<((UnsafePointer<Void>, CFunctionPointer<((UnsafePointer<Void>) -> Int)>, Bool) -> UnsafeMutablePointer<Void>)> ``` |

Modified NSPointerFunctions.descriptionFunction

|  | Declaration |
| --- | --- |
| From | ``` var descriptionFunction: CFunctionPointer<((ConstUnsafePointer<()>) -> String!)> ``` |
| To | ``` var descriptionFunction: CFunctionPointer<((UnsafePointer<Void>) -> String!)> ``` |

Modified NSPointerFunctions.hashFunction

|  | Declaration |
| --- | --- |
| From | ``` var hashFunction: CFunctionPointer<((ConstUnsafePointer<()>, CFunctionPointer<((ConstUnsafePointer<()>) -> Int)>) -> Int)> ``` |
| To | ``` var hashFunction: CFunctionPointer<((UnsafePointer<Void>, CFunctionPointer<((UnsafePointer<Void>) -> Int)>) -> Int)> ``` |

Modified NSPointerFunctions.isEqualFunction

|  | Declaration |
| --- | --- |
| From | ``` var isEqualFunction: CFunctionPointer<((ConstUnsafePointer<()>, ConstUnsafePointer<()>, CFunctionPointer<((ConstUnsafePointer<()>) -> Int)>) -> Bool)> ``` |
| To | ``` var isEqualFunction: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>, CFunctionPointer<((UnsafePointer<Void>) -> Int)>) -> Bool)> ``` |

Modified NSPointerFunctions.relinquishFunction

|  | Declaration |
| --- | --- |
| From | ``` var relinquishFunction: CFunctionPointer<((ConstUnsafePointer<()>, CFunctionPointer<((ConstUnsafePointer<()>) -> Int)>) -> Void)> ``` |
| To | ``` var relinquishFunction: CFunctionPointer<((UnsafePointer<Void>, CFunctionPointer<((UnsafePointer<Void>) -> Int)>) -> Void)> ``` |

Modified NSPointerFunctions.sizeFunction

|  | Declaration |
| --- | --- |
| From | ``` var sizeFunction: CFunctionPointer<((ConstUnsafePointer<()>) -> Int)> ``` |
| To | ``` var sizeFunction: CFunctionPointer<((UnsafePointer<Void>) -> Int)> ``` |

Modified NSPort.delegate() -> NSPortDelegate?

|  | Declaration |
| --- | --- |
| From | ``` func delegate() -> NSPortDelegate! ``` |
| To | ``` func delegate() -> NSPortDelegate? ``` |

Modified NSPort.removeFromRunLoop(NSRunLoop, forMode: String)

|  | Declaration |
| --- | --- |
| From | ``` func removeFromRunLoop(_ runLoop: NSRunLoop!, forMode mode: String!) ``` |
| To | ``` func removeFromRunLoop(_ runLoop: NSRunLoop, forMode mode: String) ``` |

Modified NSPort.scheduleInRunLoop(NSRunLoop, forMode: String)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleInRunLoop(_ runLoop: NSRunLoop!, forMode mode: String!) ``` |
| To | ``` func scheduleInRunLoop(_ runLoop: NSRunLoop, forMode mode: String) ``` |

Modified NSPort.sendBeforeDate(NSDate, components: NSMutableArray, from: NSPort, reserved: Int) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func sendBeforeDate(_ limitDate: NSDate!, components components: NSMutableArray!, from receivePort: NSPort!, reserved headerSpaceReserved: Int) -> Bool ``` |
| To | ``` func sendBeforeDate(_ limitDate: NSDate, components components: NSMutableArray, from receivePort: NSPort, reserved headerSpaceReserved: Int) -> Bool ``` |

Modified NSPort.sendBeforeDate(NSDate, msgid: Int, components: NSMutableArray, from: NSPort, reserved: Int) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func sendBeforeDate(_ limitDate: NSDate!, msgid msgID: Int, components components: NSMutableArray!, from receivePort: NSPort!, reserved headerSpaceReserved: Int) -> Bool ``` |
| To | ``` func sendBeforeDate(_ limitDate: NSDate, msgid msgID: Int, components components: NSMutableArray, from receivePort: NSPort, reserved headerSpaceReserved: Int) -> Bool ``` |

Modified NSPort.setDelegate(NSPortDelegate?)

|  | Declaration |
| --- | --- |
| From | ``` func setDelegate(_ anObject: NSPortDelegate!) ``` |
| To | ``` func setDelegate(_ anObject: NSPortDelegate?) ``` |

Modified NSPortDelegate.handlePortMessage(NSPortMessage!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified NSPortMessage.components

|  | Declaration |
| --- | --- |
| From | ``` var components: [AnyObject]! { get } ``` |
| To | ``` var components: [AnyObject] { get } ``` |

Modified NSPortMessage.receivePort

|  | Declaration |
| --- | --- |
| From | ``` var receivePort: NSPort! { get } ``` |
| To | ``` var receivePort: NSPort? { get } ``` |

Modified NSPortMessage.sendBeforeDate(NSDate) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func sendBeforeDate(_ date: NSDate!) -> Bool ``` |
| To | ``` func sendBeforeDate(_ date: NSDate) -> Bool ``` |

Modified NSPortMessage.sendPort

|  | Declaration |
| --- | --- |
| From | ``` var sendPort: NSPort! { get } ``` |
| To | ``` var sendPort: NSPort? { get } ``` |

Modified NSPortMessage.init(sendPort: NSPort, receivePort: NSPort, components:[AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` init(sendPort sendPort: NSPort!, receivePort replyPort: NSPort!, components components: [AnyObject]!) ``` |
| To | ``` init(sendPort sendPort: NSPort, receivePort replyPort: NSPort, components components: [AnyObject]) ``` |

Modified NSPositionalSpecifier.insertionContainer

|  | Declaration |
| --- | --- |
| From | ``` var insertionContainer: AnyObject! { get } ``` |
| To | ``` var insertionContainer: AnyObject? { get } ``` |

Modified NSPositionalSpecifier.insertionKey

|  | Declaration |
| --- | --- |
| From | ``` var insertionKey: String! { get } ``` |
| To | ``` var insertionKey: String? { get } ``` |

Modified NSPositionalSpecifier.objectSpecifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var objectSpecifier: NSScriptObjectSpecifier! { get } ``` | OS X 10.10 |
| To | ``` var objectSpecifier: NSScriptObjectSpecifier { get } ``` | OS X 10.5 |

Modified NSPositionalSpecifier.position

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPositionalSpecifier.init(position: NSInsertionPosition, objectSpecifier: NSScriptObjectSpecifier)

|  | Declaration |
| --- | --- |
| From | ``` init(position position: NSInsertionPosition, objectSpecifier specifier: NSScriptObjectSpecifier!) ``` |
| To | ``` init(position position: NSInsertionPosition, objectSpecifier specifier: NSScriptObjectSpecifier) ``` |

Modified NSPositionalSpecifier.setInsertionClassDescription(NSScriptClassDescription)

|  | Declaration |
| --- | --- |
| From | ``` func setInsertionClassDescription(_ classDescription: NSScriptClassDescription!) ``` |
| To | ``` func setInsertionClassDescription(_ classDescription: NSScriptClassDescription) ``` |

Modified NSPredicate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSPredicate.allowEvaluation()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSPredicate.init(block: (AnyObject!,[NSObject: AnyObject]!) -> Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(block block: ((AnyObject!, [NSObject : AnyObject]!) -> Bool)!) -> NSPredicate ``` | OS X 10.10 |
| To | ``` init(block block: (AnyObject!, [NSObject : AnyObject]!) -> Bool) -> NSPredicate ``` | OS X 10.6 |

Modified NSPredicate.evaluateWithObject(AnyObject) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func evaluateWithObject(_ object: AnyObject!) -> Bool ``` |
| To | ``` func evaluateWithObject(_ object: AnyObject) -> Bool ``` |

Modified NSPredicate.evaluateWithObject(AnyObject, substitutionVariables:[NSObject: AnyObject]?) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func evaluateWithObject(_ object: AnyObject!, substitutionVariables bindings: [NSObject : AnyObject]!) -> Bool ``` | OS X 10.10 |
| To | ``` func evaluateWithObject(_ object: AnyObject, substitutionVariables bindings: [NSObject : AnyObject]?) -> Bool ``` | OS X 10.5 |

Modified NSPredicate.init(format: String, argumentArray:[AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(format predicateFormat: String!, argumentArray arguments: [AnyObject]!) -> NSPredicate ``` |
| To | ``` init(format predicateFormat: String, argumentArray arguments: [AnyObject]?) -> NSPredicate ``` |

Modified NSPredicate.init(format: String, arguments: CVaListPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(format predicateFormat: String!, arguments argList: CVaListPointer) -> NSPredicate ``` |
| To | ``` init(format predicateFormat: String, arguments argList: CVaListPointer) -> NSPredicate ``` |

Modified NSPredicate.init(fromMetadataQueryString: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(fromMetadataQueryString queryString: String!) -> NSPredicate ``` | OS X 10.10 |
| To | ``` init?(fromMetadataQueryString queryString: String) -> NSPredicate ``` | OS X 10.9 |

Modified NSPredicate.predicateFormat

|  | Declaration |
| --- | --- |
| From | ``` var predicateFormat: String! { get } ``` |
| To | ``` var predicateFormat: String { get } ``` |

Modified NSPredicate.predicateWithSubstitutionVariables([NSObject: AnyObject]) -> Self

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func predicateWithSubstitutionVariables(_ variables: [NSObject : AnyObject]!) -> Self! ``` | OS X 10.10 |
| To | ``` func predicateWithSubstitutionVariables(_ variables: [NSObject : AnyObject]) -> Self ``` | OS X 10.10.3 |

Modified NSPredicateOperatorType.BetweenPredicateOperatorType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPredicateOperatorType.ContainsPredicateOperatorType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSProcessInfo.activeProcessorCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSProcessInfo.arguments

|  | Declaration |
| --- | --- |
| From | ``` var arguments: [AnyObject]! { get } ``` |
| To | ``` var arguments: [AnyObject] { get } ``` |

Modified NSProcessInfo.automaticTerminationSupportEnabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSProcessInfo.beginActivityWithOptions(NSActivityOptions, reason: String) -> NSObjectProtocol

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func beginActivityWithOptions(_ options: NSActivityOptions, reason reason: String!) -> NSObjectProtocol! ``` | OS X 10.10 |
| To | ``` func beginActivityWithOptions(_ options: NSActivityOptions, reason reason: String) -> NSObjectProtocol ``` | OS X 10.9 |

Modified NSProcessInfo.disableAutomaticTermination(String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func disableAutomaticTermination(_ reason: String!) ``` | OS X 10.10 |
| To | ``` func disableAutomaticTermination(_ reason: String) ``` | OS X 10.7 |

Modified NSProcessInfo.disableSuddenTermination()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSProcessInfo.enableAutomaticTermination(String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enableAutomaticTermination(_ reason: String!) ``` | OS X 10.10 |
| To | ``` func enableAutomaticTermination(_ reason: String) ``` | OS X 10.7 |

Modified NSProcessInfo.enableSuddenTermination()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSProcessInfo.endActivity(NSObjectProtocol)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func endActivity(_ activity: NSObjectProtocol!) ``` | OS X 10.10 |
| To | ``` func endActivity(_ activity: NSObjectProtocol) ``` | OS X 10.9 |

Modified NSProcessInfo.environment

|  | Declaration |
| --- | --- |
| From | ``` var environment: [NSObject : AnyObject]! { get } ``` |
| To | ``` var environment: [NSObject : AnyObject] { get } ``` |

Modified NSProcessInfo.globallyUniqueString

|  | Declaration |
| --- | --- |
| From | ``` var globallyUniqueString: String! { get } ``` |
| To | ``` var globallyUniqueString: String { get } ``` |

Modified NSProcessInfo.hostName

|  | Declaration |
| --- | --- |
| From | ``` var hostName: String! { get } ``` |
| To | ``` var hostName: String { get } ``` |

Modified NSProcessInfo.operatingSystem() -> Int

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.0 | OS X 10.10 |

Modified NSProcessInfo.operatingSystemName() -> String

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func operatingSystemName() -> String! ``` | OS X 10.10 | -- |
| To | ``` func operatingSystemName() -> String ``` | OS X 10.0 | OS X 10.10 |

Modified NSProcessInfo.operatingSystemVersionString

|  | Declaration |
| --- | --- |
| From | ``` var operatingSystemVersionString: String! { get } ``` |
| To | ``` var operatingSystemVersionString: String { get } ``` |

Modified NSProcessInfo.performActivityWithOptions(NSActivityOptions, reason: String, usingBlock:() -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func performActivityWithOptions(_ options: NSActivityOptions, reason reason: String!, usingBlock block: (() -> Void)!) ``` | OS X 10.10 |
| To | ``` func performActivityWithOptions(_ options: NSActivityOptions, reason reason: String, usingBlock block: () -> Void) ``` | OS X 10.9 |

Modified NSProcessInfo.physicalMemory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSProcessInfo.processInfo() -> NSProcessInfo [class]

|  | Declaration |
| --- | --- |
| From | ``` class func processInfo() -> NSProcessInfo! ``` |
| To | ``` class func processInfo() -> NSProcessInfo ``` |

Modified NSProcessInfo.processName

|  | Declaration |
| --- | --- |
| From | ``` var processName: String! ``` |
| To | ``` var processName: String ``` |

Modified NSProcessInfo.processorCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSProcessInfo.systemUptime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSProgress

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSProgress.addSubscriberForFileURL(NSURL, withPublishingHandler: NSProgressPublishingHandler) -> AnyObject [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func addSubscriberForFileURL(_ url: NSURL!, withPublishingHandler publishingHandler: NSProgressPublishingHandler!) -> AnyObject! ``` | OS X 10.10 |
| To | ``` class func addSubscriberForFileURL(_ url: NSURL, withPublishingHandler publishingHandler: NSProgressPublishingHandler) -> AnyObject ``` | OS X 10.9 |

Modified NSProgress.cancellationHandler

|  | Declaration |
| --- | --- |
| From | ``` var cancellationHandler: (() -> Void)! ``` |
| To | ``` var cancellationHandler: (() -> Void)? ``` |

Modified NSProgress.currentProgress() -> NSProgress? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func currentProgress() -> NSProgress! ``` |
| To | ``` class func currentProgress() -> NSProgress? ``` |

Modified NSProgress.kind

|  | Declaration |
| --- | --- |
| From | ``` var kind: String! ``` |
| To | ``` var kind: String? ``` |

Modified NSProgress.localizedAdditionalDescription

|  | Declaration |
| --- | --- |
| From | ``` var localizedAdditionalDescription: String! ``` |
| To | ``` var localizedAdditionalDescription: String ``` |

Modified NSProgress.localizedDescription

|  | Declaration |
| --- | --- |
| From | ``` var localizedDescription: String! ``` |
| To | ``` var localizedDescription: String ``` |

Modified NSProgress.old

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSProgress.init(parent: NSProgress?, userInfo:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(parent parentProgressOrNil: NSProgress!, userInfo userInfoOrNil: [NSObject : AnyObject]!) ``` |
| To | ``` init(parent parentProgressOrNil: NSProgress?, userInfo userInfoOrNil: [NSObject : AnyObject]?) ``` |

Modified NSProgress.pausingHandler

|  | Declaration |
| --- | --- |
| From | ``` var pausingHandler: (() -> Void)! ``` |
| To | ``` var pausingHandler: (() -> Void)? ``` |

Modified NSProgress.publish()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSProgress.removeSubscriber(AnyObject) [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func removeSubscriber(_ subscriber: AnyObject!) ``` | OS X 10.10 |
| To | ``` class func removeSubscriber(_ subscriber: AnyObject) ``` | OS X 10.9 |

Modified NSProgress.setUserInfoObject(AnyObject?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setUserInfoObject(_ objectOrNil: AnyObject!, forKey key: String!) ``` |
| To | ``` func setUserInfoObject(_ objectOrNil: AnyObject?, forKey key: String) ``` |

Modified NSProgress.unpublish()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSProgress.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! { get } ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? { get } ``` |

Modified NSPropertyListMutabilityOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSPropertyListMutabilityOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Immutable: NSPropertyListMutabilityOptions { get }     static var MutableContainers: NSPropertyListMutabilityOptions { get }     static var MutableContainersAndLeaves: NSPropertyListMutabilityOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSPropertyListMutabilityOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Immutable: NSPropertyListMutabilityOptions { get }     static var MutableContainers: NSPropertyListMutabilityOptions { get }     static var MutableContainersAndLeaves: NSPropertyListMutabilityOptions { get } } ``` | RawOptionSetType |

Modified NSPropertyListMutabilityOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSPropertyListSerialization.dataFromPropertyList(AnyObject, format: NSPropertyListFormat, errorDescription: UnsafeMutablePointer<NSString?>) -> NSData? [class]

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` class func dataFromPropertyList(_ plist: AnyObject!, format format: NSPropertyListFormat, errorDescription errorString: UnsafePointer<NSString?>) -> NSData! ``` | OS X 10.10 | -- |
| To | ``` class func dataFromPropertyList(_ plist: AnyObject, format format: NSPropertyListFormat, errorDescription errorString: UnsafeMutablePointer<NSString?>) -> NSData? ``` | OS X 10.0 | OS X 10.10 |

Modified NSPropertyListSerialization.dataWithPropertyList(AnyObject, format: NSPropertyListFormat, options: NSPropertyListWriteOptions, error: NSErrorPointer) -> NSData? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func dataWithPropertyList(_ plist: AnyObject!, format format: NSPropertyListFormat, options opt: NSPropertyListWriteOptions, error error: NSErrorPointer) -> NSData! ``` | OS X 10.10 |
| To | ``` class func dataWithPropertyList(_ plist: AnyObject, format format: NSPropertyListFormat, options opt: NSPropertyListWriteOptions, error error: NSErrorPointer) -> NSData? ``` | OS X 10.6 |

Modified NSPropertyListSerialization.propertyList(AnyObject, isValidForFormat: NSPropertyListFormat) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func propertyList(_ plist: AnyObject!, isValidForFormat format: NSPropertyListFormat) -> Bool ``` |
| To | ``` class func propertyList(_ plist: AnyObject, isValidForFormat format: NSPropertyListFormat) -> Bool ``` |

Modified NSPropertyListSerialization.propertyListFromData(NSData, mutabilityOption: NSPropertyListMutabilityOptions, format: UnsafeMutablePointer<NSPropertyListFormat>, errorDescription: UnsafeMutablePointer<NSString?>) -> AnyObject? [class]

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` class func propertyListFromData(_ data: NSData!, mutabilityOption opt: NSPropertyListMutabilityOptions, format format: UnsafePointer<NSPropertyListFormat>, errorDescription errorString: UnsafePointer<NSString?>) -> AnyObject! ``` | OS X 10.10 | -- |
| To | ``` class func propertyListFromData(_ data: NSData, mutabilityOption opt: NSPropertyListMutabilityOptions, format format: UnsafeMutablePointer<NSPropertyListFormat>, errorDescription errorString: UnsafeMutablePointer<NSString?>) -> AnyObject? ``` | OS X 10.0 | OS X 10.10 |

Modified NSPropertyListSerialization.propertyListWithData(NSData, options: NSPropertyListReadOptions, format: UnsafeMutablePointer<NSPropertyListFormat>, error: NSErrorPointer) -> AnyObject? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func propertyListWithData(_ data: NSData!, options opt: NSPropertyListReadOptions, format format: UnsafePointer<NSPropertyListFormat>, error error: NSErrorPointer) -> AnyObject! ``` | OS X 10.10 |
| To | ``` class func propertyListWithData(_ data: NSData, options opt: NSPropertyListReadOptions, format format: UnsafeMutablePointer<NSPropertyListFormat>, error error: NSErrorPointer) -> AnyObject? ``` | OS X 10.6 |

Modified NSPropertyListSerialization.propertyListWithStream(NSInputStream, options: NSPropertyListReadOptions, format: UnsafeMutablePointer<NSPropertyListFormat>, error: NSErrorPointer) -> AnyObject? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func propertyListWithStream(_ stream: NSInputStream!, options opt: NSPropertyListReadOptions, format format: UnsafePointer<NSPropertyListFormat>, error error: NSErrorPointer) -> AnyObject! ``` | OS X 10.10 |
| To | ``` class func propertyListWithStream(_ stream: NSInputStream, options opt: NSPropertyListReadOptions, format format: UnsafeMutablePointer<NSPropertyListFormat>, error error: NSErrorPointer) -> AnyObject? ``` | OS X 10.6 |

Modified NSPropertyListSerialization.writePropertyList(AnyObject, toStream: NSOutputStream, format: NSPropertyListFormat, options: NSPropertyListWriteOptions, error: NSErrorPointer) -> Int [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func writePropertyList(_ plist: AnyObject!, toStream stream: NSOutputStream!, format format: NSPropertyListFormat, options opt: NSPropertyListWriteOptions, error error: NSErrorPointer) -> Int ``` | OS X 10.10 |
| To | ``` class func writePropertyList(_ plist: AnyObject, toStream stream: NSOutputStream, format format: NSPropertyListFormat, options opt: NSPropertyListWriteOptions, error error: NSErrorPointer) -> Int ``` | OS X 10.6 |

Modified NSProtocolChecker.protocol

|  | Declaration |
| --- | --- |
| From | ``` var `protocol`: Protocol! { get } ``` |
| To | ``` var `protocol`: Protocol { get } ``` |

Modified NSProtocolChecker.target

|  | Declaration |
| --- | --- |
| From | ``` var target: NSObject! { get } ``` |
| To | ``` var target: NSObject? { get } ``` |

Modified NSProxy.alloc() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func alloc() -> Self! ``` | OS X 10.10 |
| To | ``` class func alloc() -> Self ``` | OS X 10.10.3 |

Modified NSProxy.class() -> AnyClass [class]

|  | Declaration |
| --- | --- |
| From | ``` class func `class`() -> AnyClass! ``` |
| To | ``` class func `class`() -> AnyClass ``` |

Modified NSProxy.debugDescription

|  | Declaration |
| --- | --- |
| From | ``` var debugDescription: String! { get } ``` |
| To | ``` var debugDescription: String { get } ``` |

Modified NSProxy.description

|  | Declaration |
| --- | --- |
| From | ``` var description: String! { get } ``` |
| To | ``` var description: String { get } ``` |

Modified NSProxy.forwardInvocation(NSInvocation)

|  | Declaration |
| --- | --- |
| From | ``` func forwardInvocation(_ invocation: NSInvocation!) ``` |
| To | ``` func forwardInvocation(_ invocation: NSInvocation) ``` |

Modified NSPurgeableData

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSRangeSpecifier.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder inCoder: NSCoder!) ``` |
| To | ``` init?(coder inCoder: NSCoder) ``` |

Modified NSRangeSpecifier.init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier, key: String, startSpecifier: NSScriptObjectSpecifier?, endSpecifier: NSScriptObjectSpecifier?)

|  | Declaration |
| --- | --- |
| From | ``` init(containerClassDescription classDesc: NSScriptClassDescription!, containerSpecifier container: NSScriptObjectSpecifier!, key property: String!, startSpecifier startSpec: NSScriptObjectSpecifier!, endSpecifier endSpec: NSScriptObjectSpecifier!) ``` |
| To | ``` init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier, key property: String, startSpecifier startSpec: NSScriptObjectSpecifier?, endSpecifier endSpec: NSScriptObjectSpecifier?) ``` |

Modified NSRangeSpecifier.endSpecifier

|  | Declaration |
| --- | --- |
| From | ``` var endSpecifier: NSScriptObjectSpecifier! ``` |
| To | ``` var endSpecifier: NSScriptObjectSpecifier? ``` |

Modified NSRangeSpecifier.startSpecifier

|  | Declaration |
| --- | --- |
| From | ``` var startSpecifier: NSScriptObjectSpecifier! ``` |
| To | ``` var startSpecifier: NSScriptObjectSpecifier? ``` |

Modified NSRecursiveLock.lockBeforeDate(NSDate) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func lockBeforeDate(_ limit: NSDate!) -> Bool ``` |
| To | ``` func lockBeforeDate(_ limit: NSDate) -> Bool ``` |

Modified NSRecursiveLock.name

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var name: String! ``` | OS X 10.10 |
| To | ``` var name: String? ``` | OS X 10.5 |

Modified NSRegularExpression

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSRegularExpression.enumerateMatchesInString(String, options: NSMatchingOptions, range: NSRange, usingBlock:(NSTextCheckingResult!, NSMatchingFlags, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateMatchesInString(_ string: String!, options options: NSMatchingOptions, range range: NSRange, usingBlock block: ((NSTextCheckingResult!, NSMatchingFlags, UnsafePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateMatchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange, usingBlock block: (NSTextCheckingResult!, NSMatchingFlags, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified NSRegularExpression.escapedPatternForString(String) -> String [class]

|  | Declaration |
| --- | --- |
| From | ``` class func escapedPatternForString(_ string: String!) -> String! ``` |
| To | ``` class func escapedPatternForString(_ string: String) -> String ``` |

Modified NSRegularExpression.escapedTemplateForString(String) -> String [class]

|  | Declaration |
| --- | --- |
| From | ``` class func escapedTemplateForString(_ string: String!) -> String! ``` |
| To | ``` class func escapedTemplateForString(_ string: String) -> String ``` |

Modified NSRegularExpression.firstMatchInString(String, options: NSMatchingOptions, range: NSRange) -> NSTextCheckingResult?

|  | Declaration |
| --- | --- |
| From | ``` func firstMatchInString(_ string: String!, options options: NSMatchingOptions, range range: NSRange) -> NSTextCheckingResult! ``` |
| To | ``` func firstMatchInString(_ string: String, options options: NSMatchingOptions, range range: NSRange) -> NSTextCheckingResult? ``` |

Modified NSRegularExpression.matchesInString(String, options: NSMatchingOptions, range: NSRange) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func matchesInString(_ string: String!, options options: NSMatchingOptions, range range: NSRange) -> [AnyObject]! ``` |
| To | ``` func matchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange) -> [AnyObject] ``` |

Modified NSRegularExpression.numberOfMatchesInString(String, options: NSMatchingOptions, range: NSRange) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func numberOfMatchesInString(_ string: String!, options options: NSMatchingOptions, range range: NSRange) -> Int ``` |
| To | ``` func numberOfMatchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange) -> Int ``` |

Modified NSRegularExpression.pattern

|  | Declaration |
| --- | --- |
| From | ``` var pattern: String! { get } ``` |
| To | ``` var pattern: String { get } ``` |

Modified NSRegularExpression.init(pattern: String, options: NSRegularExpressionOptions, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(pattern pattern: String!, options options: NSRegularExpressionOptions, error error: NSErrorPointer) ``` |
| To | ``` init?(pattern pattern: String, options options: NSRegularExpressionOptions, error error: NSErrorPointer) ``` |

Modified NSRegularExpression.rangeOfFirstMatchInString(String, options: NSMatchingOptions, range: NSRange) -> NSRange

|  | Declaration |
| --- | --- |
| From | ``` func rangeOfFirstMatchInString(_ string: String!, options options: NSMatchingOptions, range range: NSRange) -> NSRange ``` |
| To | ``` func rangeOfFirstMatchInString(_ string: String, options options: NSMatchingOptions, range range: NSRange) -> NSRange ``` |

Modified NSRegularExpression.replaceMatchesInString(NSMutableString, options: NSMatchingOptions, range: NSRange, withTemplate: String) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func replaceMatchesInString(_ string: NSMutableString!, options options: NSMatchingOptions, range range: NSRange, withTemplate templ: String!) -> Int ``` |
| To | ``` func replaceMatchesInString(_ string: NSMutableString, options options: NSMatchingOptions, range range: NSRange, withTemplate templ: String) -> Int ``` |

Modified NSRegularExpression.replacementStringForResult(NSTextCheckingResult, inString: String, offset: Int, template: String) -> String

|  | Declaration |
| --- | --- |
| From | ``` func replacementStringForResult(_ result: NSTextCheckingResult!, inString string: String!, offset offset: Int, template templ: String!) -> String! ``` |
| To | ``` func replacementStringForResult(_ result: NSTextCheckingResult, inString string: String, offset offset: Int, template templ: String) -> String ``` |

Modified NSRegularExpression.stringByReplacingMatchesInString(String, options: NSMatchingOptions, range: NSRange, withTemplate: String) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringByReplacingMatchesInString(_ string: String!, options options: NSMatchingOptions, range range: NSRange, withTemplate templ: String!) -> String! ``` |
| To | ``` func stringByReplacingMatchesInString(_ string: String, options options: NSMatchingOptions, range range: NSRange, withTemplate templ: String) -> String ``` |

Modified NSRegularExpressionOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSRegularExpressionOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var CaseInsensitive: NSRegularExpressionOptions { get }     static var AllowCommentsAndWhitespace: NSRegularExpressionOptions { get }     static var IgnoreMetacharacters: NSRegularExpressionOptions { get }     static var DotMatchesLineSeparators: NSRegularExpressionOptions { get }     static var AnchorsMatchLines: NSRegularExpressionOptions { get }     static var UseUnixLineSeparators: NSRegularExpressionOptions { get }     static var UseUnicodeWordBoundaries: NSRegularExpressionOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSRegularExpressionOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var CaseInsensitive: NSRegularExpressionOptions { get }     static var AllowCommentsAndWhitespace: NSRegularExpressionOptions { get }     static var IgnoreMetacharacters: NSRegularExpressionOptions { get }     static var DotMatchesLineSeparators: NSRegularExpressionOptions { get }     static var AnchorsMatchLines: NSRegularExpressionOptions { get }     static var UseUnixLineSeparators: NSRegularExpressionOptions { get }     static var UseUnicodeWordBoundaries: NSRegularExpressionOptions { get } } ``` | RawOptionSetType |

Modified NSRegularExpressionOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSRelativeSpecifier.baseSpecifier

|  | Declaration |
| --- | --- |
| From | ``` var baseSpecifier: NSScriptObjectSpecifier! ``` |
| To | ``` var baseSpecifier: NSScriptObjectSpecifier ``` |

Modified NSRelativeSpecifier.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder inCoder: NSCoder!) ``` |
| To | ``` init?(coder inCoder: NSCoder) ``` |

Modified NSRelativeSpecifier.init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier, key: String, relativePosition: NSRelativePosition, baseSpecifier: NSScriptObjectSpecifier?)

|  | Declaration |
| --- | --- |
| From | ``` init(containerClassDescription classDesc: NSScriptClassDescription!, containerSpecifier container: NSScriptObjectSpecifier!, key property: String!, relativePosition relPos: NSRelativePosition, baseSpecifier baseSpecifier: NSScriptObjectSpecifier!) ``` |
| To | ``` init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier, key property: String, relativePosition relPos: NSRelativePosition, baseSpecifier baseSpecifier: NSScriptObjectSpecifier?) ``` |

Modified NSRunLoop.acceptInputForMode(String, beforeDate: NSDate)

|  | Declaration |
| --- | --- |
| From | ``` func acceptInputForMode(_ mode: String!, beforeDate limitDate: NSDate!) ``` |
| To | ``` func acceptInputForMode(_ mode: String, beforeDate limitDate: NSDate) ``` |

Modified NSRunLoop.addPort(NSPort, forMode: String)

|  | Declaration |
| --- | --- |
| From | ``` func addPort(_ aPort: NSPort!, forMode mode: String!) ``` |
| To | ``` func addPort(_ aPort: NSPort, forMode mode: String) ``` |

Modified NSRunLoop.addTimer(NSTimer, forMode: String)

|  | Declaration |
| --- | --- |
| From | ``` func addTimer(_ timer: NSTimer!, forMode mode: String!) ``` |
| To | ``` func addTimer(_ timer: NSTimer, forMode mode: String) ``` |

Modified NSRunLoop.cancelPerformSelector(Selector, target: AnyObject, argument: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func cancelPerformSelector(_ aSelector: Selector, target target: AnyObject!, argument arg: AnyObject!) ``` |
| To | ``` func cancelPerformSelector(_ aSelector: Selector, target target: AnyObject, argument arg: AnyObject?) ``` |

Modified NSRunLoop.cancelPerformSelectorsWithTarget(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func cancelPerformSelectorsWithTarget(_ target: AnyObject!) ``` |
| To | ``` func cancelPerformSelectorsWithTarget(_ target: AnyObject) ``` |

Modified NSRunLoop.currentMode

|  | Declaration |
| --- | --- |
| From | ``` var currentMode: String! { get } ``` |
| To | ``` var currentMode: String? { get } ``` |

Modified NSRunLoop.currentRunLoop() -> NSRunLoop [class]

|  | Declaration |
| --- | --- |
| From | ``` class func currentRunLoop() -> NSRunLoop! ``` |
| To | ``` class func currentRunLoop() -> NSRunLoop ``` |

Modified NSRunLoop.getCFRunLoop() -> CFRunLoop

|  | Declaration |
| --- | --- |
| From | ``` func getCFRunLoop() -> CFRunLoop! ``` |
| To | ``` func getCFRunLoop() -> CFRunLoop ``` |

Modified NSRunLoop.limitDateForMode(String) -> NSDate?

|  | Declaration |
| --- | --- |
| From | ``` func limitDateForMode(_ mode: String!) -> NSDate! ``` |
| To | ``` func limitDateForMode(_ mode: String) -> NSDate? ``` |

Modified NSRunLoop.mainRunLoop() -> NSRunLoop [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func mainRunLoop() -> NSRunLoop! ``` | OS X 10.10 |
| To | ``` class func mainRunLoop() -> NSRunLoop ``` | OS X 10.5 |

Modified NSRunLoop.removePort(NSPort, forMode: String)

|  | Declaration |
| --- | --- |
| From | ``` func removePort(_ aPort: NSPort!, forMode mode: String!) ``` |
| To | ``` func removePort(_ aPort: NSPort, forMode mode: String) ``` |

Modified NSRunLoop.runMode(String, beforeDate: NSDate) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func runMode(_ mode: String!, beforeDate limitDate: NSDate!) -> Bool ``` |
| To | ``` func runMode(_ mode: String, beforeDate limitDate: NSDate) -> Bool ``` |

Modified NSRunLoop.runUntilDate(NSDate)

|  | Declaration |
| --- | --- |
| From | ``` func runUntilDate(_ limitDate: NSDate!) ``` |
| To | ``` func runUntilDate(_ limitDate: NSDate) ``` |

Modified NSScanner.charactersToBeSkipped

|  | Declaration |
| --- | --- |
| From | ``` var charactersToBeSkipped: NSCharacterSet! ``` |
| To | ``` @NSCopying var charactersToBeSkipped: NSCharacterSet? ``` |

Modified NSScanner.locale

|  | Declaration |
| --- | --- |
| From | ``` var locale: AnyObject! ``` |
| To | ``` var locale: AnyObject? ``` |

Modified NSScanner.localizedScannerWithString(String) -> AnyObject [class]

|  | Declaration |
| --- | --- |
| From | ``` class func localizedScannerWithString(_ string: String!) -> AnyObject! ``` |
| To | ``` class func localizedScannerWithString(_ string: String) -> AnyObject ``` |

Modified NSScanner.scanCharactersFromSet(NSCharacterSet, intoString: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func scanCharactersFromSet(_ set: NSCharacterSet!, intoString result: AutoreleasingUnsafePointer<NSString?>) -> Bool ``` |
| To | ``` func scanCharactersFromSet(_ set: NSCharacterSet, intoString result: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool ``` |

Modified NSScanner.scanDecimal(UnsafeMutablePointer<NSDecimal>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func scanDecimal(_ dcm: COpaquePointer) -> Bool ``` | OS X 10.10 |
| To | ``` func scanDecimal(_ dcm: UnsafeMutablePointer<NSDecimal>) -> Bool ``` | OS X 10.10.3 |

Modified NSScanner.scanDouble(UnsafeMutablePointer<Double>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func scanDouble(_ result: UnsafePointer<Double>) -> Bool ``` |
| To | ``` func scanDouble(_ result: UnsafeMutablePointer<Double>) -> Bool ``` |

Modified NSScanner.scanFloat(UnsafeMutablePointer<Float>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func scanFloat(_ result: UnsafePointer<Float>) -> Bool ``` |
| To | ``` func scanFloat(_ result: UnsafeMutablePointer<Float>) -> Bool ``` |

Modified NSScanner.scanHexDouble(UnsafeMutablePointer<Double>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func scanHexDouble(_ result: UnsafePointer<Double>) -> Bool ``` | OS X 10.10 |
| To | ``` func scanHexDouble(_ result: UnsafeMutablePointer<Double>) -> Bool ``` | OS X 10.5 |

Modified NSScanner.scanHexFloat(UnsafeMutablePointer<Float>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func scanHexFloat(_ result: UnsafePointer<Float>) -> Bool ``` | OS X 10.10 |
| To | ``` func scanHexFloat(_ result: UnsafeMutablePointer<Float>) -> Bool ``` | OS X 10.5 |

Modified NSScanner.scanHexInt(UnsafeMutablePointer<UInt32>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func scanHexInt(_ result: UnsafePointer<UInt32>) -> Bool ``` |
| To | ``` func scanHexInt(_ result: UnsafeMutablePointer<UInt32>) -> Bool ``` |

Modified NSScanner.scanHexLongLong(UnsafeMutablePointer<UInt64>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func scanHexLongLong(_ result: UnsafePointer<UInt64>) -> Bool ``` | OS X 10.10 |
| To | ``` func scanHexLongLong(_ result: UnsafeMutablePointer<UInt64>) -> Bool ``` | OS X 10.5 |

Modified NSScanner.scanInt(UnsafeMutablePointer<Int32>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func scanInt(_ result: UnsafePointer<Int32>) -> Bool ``` |
| To | ``` func scanInt(_ result: UnsafeMutablePointer<Int32>) -> Bool ``` |

Modified NSScanner.scanInteger(UnsafeMutablePointer<Int>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func scanInteger(_ result: UnsafePointer<Int>) -> Bool ``` | OS X 10.10 |
| To | ``` func scanInteger(_ result: UnsafeMutablePointer<Int>) -> Bool ``` | OS X 10.5 |

Modified NSScanner.scanLongLong(UnsafeMutablePointer<Int64>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func scanLongLong(_ result: UnsafePointer<Int64>) -> Bool ``` |
| To | ``` func scanLongLong(_ result: UnsafeMutablePointer<Int64>) -> Bool ``` |

Modified NSScanner.scanString(String, intoString: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func scanString(_ string: String!, intoString result: AutoreleasingUnsafePointer<NSString?>) -> Bool ``` |
| To | ``` func scanString(_ string: String, intoString result: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool ``` |

Modified NSScanner.scanUnsignedLongLong(UnsafeMutablePointer<UInt64>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func scanUnsignedLongLong(_ result: UnsafePointer<UInt64>) -> Bool ``` | OS X 10.10 |
| To | ``` func scanUnsignedLongLong(_ result: UnsafeMutablePointer<UInt64>) -> Bool ``` | OS X 10.9 |

Modified NSScanner.scanUpToCharactersFromSet(NSCharacterSet, intoString: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func scanUpToCharactersFromSet(_ set: NSCharacterSet!, intoString result: AutoreleasingUnsafePointer<NSString?>) -> Bool ``` |
| To | ``` func scanUpToCharactersFromSet(_ set: NSCharacterSet, intoString result: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool ``` |

Modified NSScanner.scanUpToString(String, intoString: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func scanUpToString(_ string: String!, intoString result: AutoreleasingUnsafePointer<NSString?>) -> Bool ``` |
| To | ``` func scanUpToString(_ string: String, intoString result: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool ``` |

Modified NSScanner.string

|  | Declaration |
| --- | --- |
| From | ``` var string: String! { get } ``` |
| To | ``` var string: String { get } ``` |

Modified NSScriptClassDescription.appleEventCodeForKey(String) -> FourCharCode

|  | Declaration |
| --- | --- |
| From | ``` func appleEventCodeForKey(_ key: String!) -> FourCharCode ``` |
| To | ``` func appleEventCodeForKey(_ key: String) -> FourCharCode ``` |

Modified NSScriptClassDescription.classDescriptionForKey(String) -> NSScriptClassDescription?

|  | Declaration |
| --- | --- |
| From | ``` func classDescriptionForKey(_ key: String!) -> NSScriptClassDescription! ``` |
| To | ``` func classDescriptionForKey(_ key: String) -> NSScriptClassDescription? ``` |

Modified NSScriptClassDescription.className

|  | Declaration |
| --- | --- |
| From | ``` var className: String! { get } ``` |
| To | ``` var className: String? { get } ``` |

Modified NSScriptClassDescription.defaultSubcontainerAttributeKey

|  | Declaration |
| --- | --- |
| From | ``` var defaultSubcontainerAttributeKey: String! { get } ``` |
| To | ``` var defaultSubcontainerAttributeKey: String? { get } ``` |

Modified NSScriptClassDescription.init(forClass: AnyClass!)

|  | Declaration |
| --- | --- |
| From | ``` init(forClass aClass: AnyClass!) -> NSScriptClassDescription ``` |
| To | ``` init?(forClass aClass: AnyClass!) -> NSScriptClassDescription ``` |

Modified NSScriptClassDescription.hasOrderedToManyRelationshipForKey(String) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func hasOrderedToManyRelationshipForKey(_ key: String!) -> Bool ``` | OS X 10.10 |
| To | ``` func hasOrderedToManyRelationshipForKey(_ key: String) -> Bool ``` | OS X 10.5 |

Modified NSScriptClassDescription.hasPropertyForKey(String) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func hasPropertyForKey(_ key: String!) -> Bool ``` | OS X 10.10 |
| To | ``` func hasPropertyForKey(_ key: String) -> Bool ``` | OS X 10.5 |

Modified NSScriptClassDescription.hasReadablePropertyForKey(String) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func hasReadablePropertyForKey(_ key: String!) -> Bool ``` | OS X 10.10 |
| To | ``` func hasReadablePropertyForKey(_ key: String) -> Bool ``` | OS X 10.5 |

Modified NSScriptClassDescription.hasWritablePropertyForKey(String) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func hasWritablePropertyForKey(_ key: String!) -> Bool ``` | OS X 10.10 |
| To | ``` func hasWritablePropertyForKey(_ key: String) -> Bool ``` | OS X 10.5 |

Modified NSScriptClassDescription.implementationClassName

|  | Declaration |
| --- | --- |
| From | ``` var implementationClassName: String! { get } ``` |
| To | ``` var implementationClassName: String? { get } ``` |

Modified NSScriptClassDescription.isLocationRequiredToCreateForKey(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isLocationRequiredToCreateForKey(_ toManyRelationshipKey: String!) -> Bool ``` |
| To | ``` func isLocationRequiredToCreateForKey(_ toManyRelationshipKey: String) -> Bool ``` |

Modified NSScriptClassDescription.keyWithAppleEventCode(FourCharCode) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func keyWithAppleEventCode(_ appleEventCode: FourCharCode) -> String! ``` |
| To | ``` func keyWithAppleEventCode(_ appleEventCode: FourCharCode) -> String? ``` |

Modified NSScriptClassDescription.selectorForCommand(NSScriptCommandDescription) -> Selector

|  | Declaration |
| --- | --- |
| From | ``` func selectorForCommand(_ commandDescription: NSScriptCommandDescription!) -> Selector ``` |
| To | ``` func selectorForCommand(_ commandDescription: NSScriptCommandDescription) -> Selector ``` |

Modified NSScriptClassDescription.suiteName

|  | Declaration |
| --- | --- |
| From | ``` var suiteName: String! { get } ``` |
| To | ``` var suiteName: String? { get } ``` |

Modified NSScriptClassDescription.init(suiteName: String, className: String, dictionary:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(suiteName suiteName: String!, className className: String!, dictionary classDeclaration: [NSObject : AnyObject]!) ``` |
| To | ``` init?(suiteName suiteName: String, className className: String, dictionary classDeclaration: [NSObject : AnyObject]?) ``` |

Modified NSScriptClassDescription.superclassDescription

|  | Declaration |
| --- | --- |
| From | ``` var superclassDescription: NSScriptClassDescription! { get } ``` |
| To | ``` var superclassDescription: NSScriptClassDescription? { get } ``` |

Modified NSScriptClassDescription.supportsCommand(NSScriptCommandDescription) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func supportsCommand(_ commandDescription: NSScriptCommandDescription!) -> Bool ``` |
| To | ``` func supportsCommand(_ commandDescription: NSScriptCommandDescription) -> Bool ``` |

Modified NSScriptClassDescription.typeForKey(String) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func typeForKey(_ key: String!) -> String! ``` |
| To | ``` func typeForKey(_ key: String) -> String? ``` |

Modified NSScriptCoercionHandler.coerceValue(AnyObject, toClass: AnyClass) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func coerceValue(_ value: AnyObject!, toClass toClass: AnyClass!) -> AnyObject! ``` |
| To | ``` func coerceValue(_ value: AnyObject, toClass toClass: AnyClass) -> AnyObject? ``` |

Modified NSScriptCoercionHandler.registerCoercer(AnyObject, selector: Selector, toConvertFromClass: AnyClass, toClass: AnyClass)

|  | Declaration |
| --- | --- |
| From | ``` func registerCoercer(_ coercer: AnyObject!, selector selector: Selector, toConvertFromClass fromClass: AnyClass!, toClass toClass: AnyClass!) ``` |
| To | ``` func registerCoercer(_ coercer: AnyObject, selector selector: Selector, toConvertFromClass fromClass: AnyClass, toClass toClass: AnyClass) ``` |

Modified NSScriptCoercionHandler.sharedCoercionHandler() -> NSScriptCoercionHandler [class]

|  | Declaration |
| --- | --- |
| From | ``` class func sharedCoercionHandler() -> NSScriptCoercionHandler! ``` |
| To | ``` class func sharedCoercionHandler() -> NSScriptCoercionHandler ``` |

Modified NSScriptCommand.appleEvent

|  | Declaration |
| --- | --- |
| From | ``` var appleEvent: NSAppleEventDescriptor! { get } ``` |
| To | ``` @NSCopying var appleEvent: NSAppleEventDescriptor? { get } ``` |

Modified NSScriptCommand.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(coder inCoder: NSCoder!) ``` |
| To | ``` convenience init?(coder inCoder: NSCoder) ``` |

Modified NSScriptCommand.commandDescription

|  | Declaration |
| --- | --- |
| From | ``` var commandDescription: NSScriptCommandDescription! { get } ``` |
| To | ``` var commandDescription: NSScriptCommandDescription { get } ``` |

Modified NSScriptCommand.init(commandDescription: NSScriptCommandDescription)

|  | Declaration |
| --- | --- |
| From | ``` init(commandDescription commandDef: NSScriptCommandDescription!) ``` |
| To | ``` init(commandDescription commandDef: NSScriptCommandDescription) ``` |

Modified NSScriptCommand.currentCommand() -> NSScriptCommand? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func currentCommand() -> NSScriptCommand! ``` |
| To | ``` class func currentCommand() -> NSScriptCommand? ``` |

Modified NSScriptCommand.directParameter

|  | Declaration |
| --- | --- |
| From | ``` var directParameter: AnyObject! ``` |
| To | ``` var directParameter: AnyObject? ``` |

Modified NSScriptCommand.evaluatedArguments

|  | Declaration |
| --- | --- |
| From | ``` var evaluatedArguments: [NSObject : AnyObject]! { get } ``` |
| To | ``` var evaluatedArguments: [NSObject : AnyObject]? { get } ``` |

Modified NSScriptCommand.evaluatedReceivers

|  | Declaration |
| --- | --- |
| From | ``` var evaluatedReceivers: AnyObject! { get } ``` |
| To | ``` var evaluatedReceivers: AnyObject? { get } ``` |

Modified NSScriptCommand.executeCommand() -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func executeCommand() -> AnyObject! ``` |
| To | ``` func executeCommand() -> AnyObject? ``` |

Modified NSScriptCommand.performDefaultImplementation() -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func performDefaultImplementation() -> AnyObject! ``` |
| To | ``` func performDefaultImplementation() -> AnyObject? ``` |

Modified NSScriptCommand.receiversSpecifier

|  | Declaration |
| --- | --- |
| From | ``` var receiversSpecifier: NSScriptObjectSpecifier! ``` |
| To | ``` var receiversSpecifier: NSScriptObjectSpecifier? ``` |

Modified NSScriptCommand.resumeExecutionWithResult(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func resumeExecutionWithResult(_ result: AnyObject!) ``` |
| To | ``` func resumeExecutionWithResult(_ result: AnyObject?) ``` |

Modified NSScriptCommand.scriptErrorExpectedTypeDescriptor

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var scriptErrorExpectedTypeDescriptor: NSAppleEventDescriptor! ``` | OS X 10.10 |
| To | ``` var scriptErrorExpectedTypeDescriptor: NSAppleEventDescriptor? ``` | OS X 10.5 |

Modified NSScriptCommand.scriptErrorOffendingObjectDescriptor

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var scriptErrorOffendingObjectDescriptor: NSAppleEventDescriptor! ``` | OS X 10.10 |
| To | ``` var scriptErrorOffendingObjectDescriptor: NSAppleEventDescriptor? ``` | OS X 10.5 |

Modified NSScriptCommand.scriptErrorString

|  | Declaration |
| --- | --- |
| From | ``` var scriptErrorString: String! ``` |
| To | ``` var scriptErrorString: String? ``` |

Modified NSScriptCommandDescription.appleEventCodeForArgumentWithName(String) -> FourCharCode

|  | Declaration |
| --- | --- |
| From | ``` func appleEventCodeForArgumentWithName(_ argumentName: String!) -> FourCharCode ``` |
| To | ``` func appleEventCodeForArgumentWithName(_ argumentName: String) -> FourCharCode ``` |

Modified NSScriptCommandDescription.argumentNames

|  | Declaration |
| --- | --- |
| From | ``` var argumentNames: [AnyObject]! { get } ``` |
| To | ``` var argumentNames: [AnyObject] { get } ``` |

Modified NSScriptCommandDescription.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder inCoder: NSCoder!) ``` |
| To | ``` init?(coder inCoder: NSCoder) ``` |

Modified NSScriptCommandDescription.commandClassName

|  | Declaration |
| --- | --- |
| From | ``` var commandClassName: String! { get } ``` |
| To | ``` var commandClassName: String { get } ``` |

Modified NSScriptCommandDescription.commandName

|  | Declaration |
| --- | --- |
| From | ``` var commandName: String! { get } ``` |
| To | ``` var commandName: String { get } ``` |

Modified NSScriptCommandDescription.createCommandInstance() -> NSScriptCommand

|  | Declaration |
| --- | --- |
| From | ``` func createCommandInstance() -> NSScriptCommand! ``` |
| To | ``` func createCommandInstance() -> NSScriptCommand ``` |

Modified NSScriptCommandDescription.createCommandInstanceWithZone(NSZone) -> NSScriptCommand

|  | Declaration |
| --- | --- |
| From | ``` func createCommandInstanceWithZone(_ zone: NSZone) -> NSScriptCommand! ``` |
| To | ``` func createCommandInstanceWithZone(_ zone: NSZone) -> NSScriptCommand ``` |

Modified NSScriptCommandDescription.isOptionalArgumentWithName(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isOptionalArgumentWithName(_ argumentName: String!) -> Bool ``` |
| To | ``` func isOptionalArgumentWithName(_ argumentName: String) -> Bool ``` |

Modified NSScriptCommandDescription.returnType

|  | Declaration |
| --- | --- |
| From | ``` var returnType: String! { get } ``` |
| To | ``` var returnType: String? { get } ``` |

Modified NSScriptCommandDescription.suiteName

|  | Declaration |
| --- | --- |
| From | ``` var suiteName: String! { get } ``` |
| To | ``` var suiteName: String { get } ``` |

Modified NSScriptCommandDescription.init(suiteName: String, commandName: String, dictionary:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(suiteName suiteName: String!, commandName commandName: String!, dictionary commandDeclaration: [NSObject : AnyObject]!) ``` |
| To | ``` init?(suiteName suiteName: String, commandName commandName: String, dictionary commandDeclaration: [NSObject : AnyObject]?) ``` |

Modified NSScriptCommandDescription.typeForArgumentWithName(String) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func typeForArgumentWithName(_ argumentName: String!) -> String! ``` |
| To | ``` func typeForArgumentWithName(_ argumentName: String) -> String? ``` |

Modified NSScriptExecutionContext.objectBeingTested

|  | Declaration |
| --- | --- |
| From | ``` var objectBeingTested: AnyObject! ``` |
| To | ``` var objectBeingTested: AnyObject? ``` |

Modified NSScriptExecutionContext.rangeContainerObject

|  | Declaration |
| --- | --- |
| From | ``` var rangeContainerObject: AnyObject! ``` |
| To | ``` var rangeContainerObject: AnyObject? ``` |

Modified NSScriptExecutionContext.sharedScriptExecutionContext() -> NSScriptExecutionContext [class]

|  | Declaration |
| --- | --- |
| From | ``` class func sharedScriptExecutionContext() -> NSScriptExecutionContext! ``` |
| To | ``` class func sharedScriptExecutionContext() -> NSScriptExecutionContext ``` |

Modified NSScriptExecutionContext.topLevelObject

|  | Declaration |
| --- | --- |
| From | ``` var topLevelObject: AnyObject! ``` |
| To | ``` var topLevelObject: AnyObject? ``` |

Modified NSScriptObjectSpecifier.childSpecifier

|  | Declaration |
| --- | --- |
| From | ``` var childSpecifier: NSScriptObjectSpecifier! ``` |
| To | ``` unowned(unsafe) var childSpecifier: NSScriptObjectSpecifier? ``` |

Modified NSScriptObjectSpecifier.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder inCoder: NSCoder!) ``` |
| To | ``` init?(coder inCoder: NSCoder) ``` |

Modified NSScriptObjectSpecifier.containerClassDescription

|  | Declaration |
| --- | --- |
| From | ``` var containerClassDescription: NSScriptClassDescription! ``` |
| To | ``` var containerClassDescription: NSScriptClassDescription? ``` |

Modified NSScriptObjectSpecifier.init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier, key: String)

|  | Declaration |
| --- | --- |
| From | ``` init(containerClassDescription classDesc: NSScriptClassDescription!, containerSpecifier container: NSScriptObjectSpecifier!, key property: String!) ``` |
| To | ``` init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier, key property: String) ``` |

Modified NSScriptObjectSpecifier.containerSpecifier

|  | Declaration |
| --- | --- |
| From | ``` var containerSpecifier: NSScriptObjectSpecifier! ``` |
| To | ``` var containerSpecifier: NSScriptObjectSpecifier? ``` |

Modified NSScriptObjectSpecifier.init(containerSpecifier: NSScriptObjectSpecifier, key: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(containerSpecifier container: NSScriptObjectSpecifier!, key property: String!) ``` |
| To | ``` convenience init(containerSpecifier container: NSScriptObjectSpecifier, key property: String) ``` |

Modified NSScriptObjectSpecifier.descriptor

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var descriptor: NSAppleEventDescriptor! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var descriptor: NSAppleEventDescriptor? { get } ``` | OS X 10.5 |

Modified NSScriptObjectSpecifier.init(descriptor: NSAppleEventDescriptor)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(descriptor descriptor: NSAppleEventDescriptor!) -> NSScriptObjectSpecifier ``` | OS X 10.10 |
| To | ``` init?(descriptor descriptor: NSAppleEventDescriptor) -> NSScriptObjectSpecifier ``` | OS X 10.5 |

Modified NSScriptObjectSpecifier.evaluationErrorSpecifier

|  | Declaration |
| --- | --- |
| From | ``` var evaluationErrorSpecifier: NSScriptObjectSpecifier! { get } ``` |
| To | ``` var evaluationErrorSpecifier: NSScriptObjectSpecifier? { get } ``` |

Modified NSScriptObjectSpecifier.indicesOfObjectsByEvaluatingWithContainer(AnyObject, count: UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<Int>

|  | Declaration |
| --- | --- |
| From | ``` func indicesOfObjectsByEvaluatingWithContainer(_ container: AnyObject!, count count: UnsafePointer<Int>) -> UnsafePointer<Int> ``` |
| To | ``` func indicesOfObjectsByEvaluatingWithContainer(_ container: AnyObject, count count: UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<Int> ``` |

Modified NSScriptObjectSpecifier.key

|  | Declaration |
| --- | --- |
| From | ``` var key: String! ``` |
| To | ``` var key: String? ``` |

Modified NSScriptObjectSpecifier.keyClassDescription

|  | Declaration |
| --- | --- |
| From | ``` var keyClassDescription: NSScriptClassDescription! { get } ``` |
| To | ``` var keyClassDescription: NSScriptClassDescription? { get } ``` |

Modified NSScriptObjectSpecifier.objectsByEvaluatingSpecifier

|  | Declaration |
| --- | --- |
| From | ``` var objectsByEvaluatingSpecifier: AnyObject! { get } ``` |
| To | ``` var objectsByEvaluatingSpecifier: AnyObject? { get } ``` |

Modified NSScriptObjectSpecifier.objectsByEvaluatingWithContainers(AnyObject) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func objectsByEvaluatingWithContainers(_ containers: AnyObject!) -> AnyObject! ``` |
| To | ``` func objectsByEvaluatingWithContainers(_ containers: AnyObject) -> AnyObject? ``` |

Modified NSScriptSuiteRegistry.aeteResource(String) -> NSData?

|  | Declaration |
| --- | --- |
| From | ``` func aeteResource(_ languageName: String!) -> NSData! ``` |
| To | ``` func aeteResource(_ languageName: String) -> NSData? ``` |

Modified NSScriptSuiteRegistry.appleEventCodeForSuite(String) -> FourCharCode

|  | Declaration |
| --- | --- |
| From | ``` func appleEventCodeForSuite(_ suiteName: String!) -> FourCharCode ``` |
| To | ``` func appleEventCodeForSuite(_ suiteName: String) -> FourCharCode ``` |

Modified NSScriptSuiteRegistry.bundleForSuite(String) -> NSBundle?

|  | Declaration |
| --- | --- |
| From | ``` func bundleForSuite(_ suiteName: String!) -> NSBundle! ``` |
| To | ``` func bundleForSuite(_ suiteName: String) -> NSBundle? ``` |

Modified NSScriptSuiteRegistry.classDescriptionWithAppleEventCode(FourCharCode) -> NSScriptClassDescription?

|  | Declaration |
| --- | --- |
| From | ``` func classDescriptionWithAppleEventCode(_ appleEventCode: FourCharCode) -> NSScriptClassDescription! ``` |
| To | ``` func classDescriptionWithAppleEventCode(_ appleEventCode: FourCharCode) -> NSScriptClassDescription? ``` |

Modified NSScriptSuiteRegistry.classDescriptionsInSuite(String) -> [NSObject: AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func classDescriptionsInSuite(_ suiteName: String!) -> [NSObject : AnyObject]! ``` |
| To | ``` func classDescriptionsInSuite(_ suiteName: String) -> [NSObject : AnyObject]? ``` |

Modified NSScriptSuiteRegistry.commandDescriptionWithAppleEventClass(FourCharCode, andAppleEventCode: FourCharCode) -> NSScriptCommandDescription?

|  | Declaration |
| --- | --- |
| From | ``` func commandDescriptionWithAppleEventClass(_ appleEventClassCode: FourCharCode, andAppleEventCode appleEventIDCode: FourCharCode) -> NSScriptCommandDescription! ``` |
| To | ``` func commandDescriptionWithAppleEventClass(_ appleEventClassCode: FourCharCode, andAppleEventCode appleEventIDCode: FourCharCode) -> NSScriptCommandDescription? ``` |

Modified NSScriptSuiteRegistry.commandDescriptionsInSuite(String) -> [NSObject: AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func commandDescriptionsInSuite(_ suiteName: String!) -> [NSObject : AnyObject]! ``` |
| To | ``` func commandDescriptionsInSuite(_ suiteName: String) -> [NSObject : AnyObject]? ``` |

Modified NSScriptSuiteRegistry.loadSuiteWithDictionary([NSObject: AnyObject], fromBundle: NSBundle)

|  | Declaration |
| --- | --- |
| From | ``` func loadSuiteWithDictionary(_ suiteDeclaration: [NSObject : AnyObject]!, fromBundle bundle: NSBundle!) ``` |
| To | ``` func loadSuiteWithDictionary(_ suiteDeclaration: [NSObject : AnyObject], fromBundle bundle: NSBundle) ``` |

Modified NSScriptSuiteRegistry.loadSuitesFromBundle(NSBundle)

|  | Declaration |
| --- | --- |
| From | ``` func loadSuitesFromBundle(_ bundle: NSBundle!) ``` |
| To | ``` func loadSuitesFromBundle(_ bundle: NSBundle) ``` |

Modified NSScriptSuiteRegistry.registerClassDescription(NSScriptClassDescription)

|  | Declaration |
| --- | --- |
| From | ``` func registerClassDescription(_ classDescription: NSScriptClassDescription!) ``` |
| To | ``` func registerClassDescription(_ classDescription: NSScriptClassDescription) ``` |

Modified NSScriptSuiteRegistry.registerCommandDescription(NSScriptCommandDescription)

|  | Declaration |
| --- | --- |
| From | ``` func registerCommandDescription(_ commandDescription: NSScriptCommandDescription!) ``` |
| To | ``` func registerCommandDescription(_ commandDescription: NSScriptCommandDescription) ``` |

Modified NSScriptSuiteRegistry.setSharedScriptSuiteRegistry(NSScriptSuiteRegistry) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setSharedScriptSuiteRegistry(_ registry: NSScriptSuiteRegistry!) ``` |
| To | ``` class func setSharedScriptSuiteRegistry(_ registry: NSScriptSuiteRegistry) ``` |

Modified NSScriptSuiteRegistry.sharedScriptSuiteRegistry() -> NSScriptSuiteRegistry [class]

|  | Declaration |
| --- | --- |
| From | ``` class func sharedScriptSuiteRegistry() -> NSScriptSuiteRegistry! ``` |
| To | ``` class func sharedScriptSuiteRegistry() -> NSScriptSuiteRegistry ``` |

Modified NSScriptSuiteRegistry.suiteForAppleEventCode(FourCharCode) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func suiteForAppleEventCode(_ appleEventCode: FourCharCode) -> String! ``` |
| To | ``` func suiteForAppleEventCode(_ appleEventCode: FourCharCode) -> String? ``` |

Modified NSScriptSuiteRegistry.suiteNames

|  | Declaration |
| --- | --- |
| From | ``` var suiteNames: [AnyObject]! { get } ``` |
| To | ``` var suiteNames: [AnyObject] { get } ``` |

Modified NSScriptWhoseTest.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder inCoder: NSCoder!) ``` |
| To | ``` init?(coder inCoder: NSCoder) ``` |

Modified NSSearchPathDirectory.ApplicationScriptsDirectory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSSearchPathDirectory.AutosavedInformationDirectory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSSearchPathDirectory.DownloadsDirectory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSSearchPathDirectory.InputMethodsDirectory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSSearchPathDirectory.ItemReplacementDirectory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSSearchPathDirectory.MoviesDirectory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSSearchPathDirectory.MusicDirectory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSSearchPathDirectory.PicturesDirectory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSSearchPathDirectory.PreferencePanesDirectory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSSearchPathDirectory.PrinterDescriptionDirectory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSSearchPathDirectory.SharedPublicDirectory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSSearchPathDirectory.TrashDirectory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSSearchPathDomainMask [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSSearchPathDomainMask : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var UserDomainMask: NSSearchPathDomainMask { get }     static var LocalDomainMask: NSSearchPathDomainMask { get }     static var NetworkDomainMask: NSSearchPathDomainMask { get }     static var SystemDomainMask: NSSearchPathDomainMask { get }     static var AllDomainsMask: NSSearchPathDomainMask { get } } ``` | RawOptionSet |
| To | ``` struct NSSearchPathDomainMask : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var UserDomainMask: NSSearchPathDomainMask { get }     static var LocalDomainMask: NSSearchPathDomainMask { get }     static var NetworkDomainMask: NSSearchPathDomainMask { get }     static var SystemDomainMask: NSSearchPathDomainMask { get }     static var AllDomainsMask: NSSearchPathDomainMask { get } } ``` | RawOptionSetType |

Modified NSSearchPathDomainMask.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSSecureCoding.supportsSecureCoding() -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func supportsSecureCoding() -> Bool ``` |
| To | ``` static func supportsSecureCoding() -> Bool ``` |

Modified NSSet

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, Reflectable, Sequence |
| To | AnyObject, ArrayLiteralConvertible, NSCoding, NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding, Reflectable, SequenceType |

Modified NSSet.addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func addObserver(_ observer: NSObject!, forKeyPath keyPath: String!, options options: NSKeyValueObservingOptions, context context: UnsafePointer<()>) ``` |
| To | ``` func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>) ``` |

Modified NSSet.allObjects

|  | Declaration |
| --- | --- |
| From | ``` var allObjects: [AnyObject]! { get } ``` |
| To | ``` var allObjects: [AnyObject] { get } ``` |

Modified NSSet.anyObject() -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func anyObject() -> AnyObject! ``` |
| To | ``` func anyObject() -> AnyObject? ``` |

Modified NSSet.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified NSSet.containsObject(AnyObject) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func containsObject(_ anObject: AnyObject!) -> Bool ``` |
| To | ``` func containsObject(_ anObject: AnyObject) -> Bool ``` |

Modified NSSet.description

|  | Declaration |
| --- | --- |
| From | ``` var description: String! { get } ``` |
| To | ``` var description: String { get } ``` |

Modified NSSet.descriptionWithLocale(AnyObject?) -> String

|  | Declaration |
| --- | --- |
| From | ``` func descriptionWithLocale(_ locale: AnyObject!) -> String! ``` |
| To | ``` func descriptionWithLocale(_ locale: AnyObject?) -> String ``` |

Modified NSSet.enumerateObjectsUsingBlock((AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateObjectsUsingBlock(_ block: ((AnyObject!, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateObjectsUsingBlock(_ block: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.6 |

Modified NSSet.enumerateObjectsWithOptions(NSEnumerationOptions, usingBlock:(AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: ((AnyObject!, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.6 |

Modified NSSet.filteredSetUsingPredicate(NSPredicate) -> Set<NSObject>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func filteredSetUsingPredicate(_ predicate: NSPredicate!) -> NSSet! ``` | OS X 10.10 |
| To | ``` func filteredSetUsingPredicate(_ predicate: NSPredicate) -> Set<NSObject> ``` | OS X 10.5 |

Modified NSSet.intersectsSet(Set<NSObject>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func intersectsSet(_ otherSet: NSSet!) -> Bool ``` | OS X 10.10 |
| To | ``` func intersectsSet(_ otherSet: Set<NSObject>) -> Bool ``` | OS X 10.10.3 |

Modified NSSet.isEqualToSet(Set<NSObject>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isEqualToSet(_ otherSet: NSSet!) -> Bool ``` | OS X 10.10 |
| To | ``` func isEqualToSet(_ otherSet: Set<NSObject>) -> Bool ``` | OS X 10.10.3 |

Modified NSSet.isSubsetOfSet(Set<NSObject>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isSubsetOfSet(_ otherSet: NSSet!) -> Bool ``` | OS X 10.10 |
| To | ``` func isSubsetOfSet(_ otherSet: Set<NSObject>) -> Bool ``` | OS X 10.10.3 |

Modified NSSet.member(AnyObject) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func member(_ object: AnyObject!) -> AnyObject! ``` |
| To | ``` func member(_ object: AnyObject) -> AnyObject? ``` |

Modified NSSet.init(object: AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(object object: AnyObject!) ``` |
| To | ``` convenience init(object object: AnyObject) ``` |

Modified NSSet.objectEnumerator() -> NSEnumerator

|  | Declaration |
| --- | --- |
| From | ``` func objectEnumerator() -> NSEnumerator! ``` |
| To | ``` func objectEnumerator() -> NSEnumerator ``` |

Modified NSSet.init(objects: UnsafePointer<AnyObject?>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(objects objects: ConstUnsafePointer<AnyObject?>, count cnt: Int) ``` |
| To | ``` init(objects objects: UnsafePointer<AnyObject?>, count cnt: Int) ``` |

Modified NSSet.objectsPassingTest((AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objectsPassingTest(_ predicate: ((AnyObject!, UnsafePointer<ObjCBool>) -> Bool)!) -> NSSet! ``` | OS X 10.10 |
| To | ``` func objectsPassingTest(_ predicate: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` | OS X 10.6 |

Modified NSSet.objectsWithOptions(NSEnumerationOptions, passingTest:(AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: ((AnyObject!, UnsafePointer<ObjCBool>) -> Bool)!) -> NSSet! ``` | OS X 10.10 |
| To | ``` func objectsWithOptions(_ opts: NSEnumerationOptions, passingTest predicate: (AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<NSObject> ``` | OS X 10.6 |

Modified NSSet.removeObserver(NSObject, forKeyPath: String)

|  | Declaration |
| --- | --- |
| From | ``` func removeObserver(_ observer: NSObject!, forKeyPath keyPath: String!) ``` |
| To | ``` func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) ``` |

Modified NSSet.removeObserver(NSObject, forKeyPath: String, context: UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func removeObserver(_ observer: NSObject!, forKeyPath keyPath: String!, context context: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>) ``` | OS X 10.7 |

Modified NSSet.init(set: Set<NSObject>, copyItems: Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(set set: NSSet!, copyItems flag: Bool) ``` | OS X 10.10 |
| To | ``` convenience init(set set: Set<NSObject>, copyItems flag: Bool) ``` | OS X 10.10.3 |

Modified NSSet.setByAddingObject(AnyObject) -> Set<NSObject>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setByAddingObject(_ anObject: AnyObject!) -> NSSet! ``` | OS X 10.10 |
| To | ``` func setByAddingObject(_ anObject: AnyObject) -> Set<NSObject> ``` | OS X 10.5 |

Modified NSSet.setByAddingObjectsFromArray([AnyObject]) -> Set<NSObject>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setByAddingObjectsFromArray(_ other: [AnyObject]!) -> NSSet! ``` | OS X 10.10 |
| To | ``` func setByAddingObjectsFromArray(_ other: [AnyObject]) -> Set<NSObject> ``` | OS X 10.5 |

Modified NSSet.setByAddingObjectsFromSet(Set<NSObject>) -> Set<NSObject>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setByAddingObjectsFromSet(_ other: NSSet!) -> NSSet! ``` | OS X 10.10 |
| To | ``` func setByAddingObjectsFromSet(_ other: Set<NSObject>) -> Set<NSObject> ``` | OS X 10.5 |

Modified NSSet.setValue(AnyObject?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ value: AnyObject!, forKey key: String!) ``` |
| To | ``` func setValue(_ value: AnyObject?, forKey key: String) ``` |

Modified NSSet.sortedArrayUsingDescriptors([AnyObject]) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sortedArrayUsingDescriptors(_ sortDescriptors: [AnyObject]!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func sortedArrayUsingDescriptors(_ sortDescriptors: [AnyObject]) -> [AnyObject] ``` | OS X 10.6 |

Modified NSSet.valueForKey(String) -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func valueForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` func valueForKey(_ key: String) -> AnyObject ``` |

Modified NSSetCommand.keySpecifier

|  | Declaration |
| --- | --- |
| From | ``` var keySpecifier: NSScriptObjectSpecifier! { get } ``` |
| To | ``` var keySpecifier: NSScriptObjectSpecifier { get } ``` |

Modified NSSetCommand.setReceiversSpecifier(NSScriptObjectSpecifier)

|  | Declaration |
| --- | --- |
| From | ``` func setReceiversSpecifier(_ receiversRef: NSScriptObjectSpecifier!) ``` |
| To | ``` func setReceiversSpecifier(_ receiversRef: NSScriptObjectSpecifier) ``` |

Modified NSSocketPort.init(TCPPort: UInt16)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(TCPPort port: UInt16) ``` |
| To | ``` convenience init?(TCPPort port: UInt16) ``` |

Modified NSSocketPort.address

|  | Declaration |
| --- | --- |
| From | ``` var address: NSData! { get } ``` |
| To | ``` @NSCopying var address: NSData { get } ``` |

Modified NSSocketPort.init(protocolFamily: Int32, socketType: Int32, protocol: Int32, address: NSData)

|  | Declaration |
| --- | --- |
| From | ``` init(protocolFamily family: Int32, socketType type: Int32, `protocol` `protocol`: Int32, address address: NSData!) ``` |
| To | ``` init?(protocolFamily family: Int32, socketType type: Int32, `protocol` `protocol`: Int32, address address: NSData) ``` |

Modified NSSocketPort.init(protocolFamily: Int32, socketType: Int32, protocol: Int32, socket: NSSocketNativeHandle)

|  | Declaration |
| --- | --- |
| From | ``` init(protocolFamily family: Int32, socketType type: Int32, `protocol` `protocol`: Int32, socket sock: NSSocketNativeHandle) ``` |
| To | ``` init?(protocolFamily family: Int32, socketType type: Int32, `protocol` `protocol`: Int32, socket sock: NSSocketNativeHandle) ``` |

Modified NSSocketPort.init(remoteWithProtocolFamily: Int32, socketType: Int32, protocol: Int32, address: NSData)

|  | Declaration |
| --- | --- |
| From | ``` init(remoteWithProtocolFamily family: Int32, socketType type: Int32, `protocol` `protocol`: Int32, address address: NSData!) ``` |
| To | ``` init(remoteWithProtocolFamily family: Int32, socketType type: Int32, `protocol` `protocol`: Int32, address address: NSData) ``` |

Modified NSSocketPort.init(remoteWithTCPPort: UInt16, host: String?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(remoteWithTCPPort port: UInt16, host hostName: String!) ``` |
| To | ``` convenience init?(remoteWithTCPPort port: UInt16, host hostName: String?) ``` |

Modified NSSortDescriptor.allowEvaluation()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSSortDescriptor.comparator

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var comparator: NSComparator! { get } ``` | OS X 10.10 |
| To | ``` var comparator: NSComparator? { get } ``` | OS X 10.6 |

Modified NSSortDescriptor.compareObject(AnyObject, toObject: AnyObject) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func compareObject(_ object1: AnyObject!, toObject object2: AnyObject!) -> NSComparisonResult ``` |
| To | ``` func compareObject(_ object1: AnyObject, toObject object2: AnyObject) -> NSComparisonResult ``` |

Modified NSSortDescriptor.key

|  | Declaration |
| --- | --- |
| From | ``` var key: String! { get } ``` |
| To | ``` var key: String? { get } ``` |

Modified NSSortOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSSortOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Concurrent: NSSortOptions { get }     static var Stable: NSSortOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSSortOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Concurrent: NSSortOptions { get }     static var Stable: NSSortOptions { get } } ``` | RawOptionSetType |

Modified NSSortOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSSpecifierTest.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder inCoder: NSCoder!) ``` |
| To | ``` init?(coder inCoder: NSCoder) ``` |

Modified NSSpecifierTest.init(objectSpecifier: NSScriptObjectSpecifier?, comparisonOperator: NSTestComparisonOperation, testObject: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` init(objectSpecifier obj1: NSScriptObjectSpecifier!, comparisonOperator compOp: NSTestComparisonOperation, testObject obj2: AnyObject!) ``` |
| To | ``` init(objectSpecifier obj1: NSScriptObjectSpecifier?, comparisonOperator compOp: NSTestComparisonOperation, testObject obj2: AnyObject?) ``` |

Modified NSSpellServer.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: NSSpellServerDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: NSSpellServerDelegate? ``` |

Modified NSSpellServer.isWordInUserDictionaries(String, caseSensitive: Bool) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isWordInUserDictionaries(_ word: String!, caseSensitive flag: Bool) -> Bool ``` |
| To | ``` func isWordInUserDictionaries(_ word: String, caseSensitive flag: Bool) -> Bool ``` |

Modified NSSpellServer.registerLanguage(String?, byVendor: String?) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func registerLanguage(_ language: String!, byVendor vendor: String!) -> Bool ``` |
| To | ``` func registerLanguage(_ language: String?, byVendor vendor: String?) -> Bool ``` |

Modified NSSpellServerDelegate.spellServer(NSSpellServer, checkGrammarInString: String, language: String?, details: AutoreleasingUnsafeMutablePointer<NSArray?>) -> NSRange

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func spellServer(_ sender: NSSpellServer!, checkGrammarInString stringToCheck: String!, language language: String!, details details: AutoreleasingUnsafePointer<NSArray?>) -> NSRange ``` | OS X 10.10 | -- |
| To | ``` optional func spellServer(_ sender: NSSpellServer, checkGrammarInString stringToCheck: String, language language: String?, details details: AutoreleasingUnsafeMutablePointer<NSArray?>) -> NSRange ``` | OS X 10.5 | yes |

Modified NSSpellServerDelegate.spellServer(NSSpellServer, checkString: String, offset: Int, types: NSTextCheckingTypes, options:[NSObject: AnyObject]?, orthography: NSOrthography?, wordCount: UnsafeMutablePointer<Int>) -> [AnyObject]?

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func spellServer(_ sender: NSSpellServer!, checkString stringToCheck: String!, offset offset: Int, types checkingTypes: NSTextCheckingTypes, options options: [NSObject : AnyObject]!, orthography orthography: NSOrthography!, wordCount wordCount: UnsafePointer<Int>) -> [AnyObject]! ``` | OS X 10.10 | -- |
| To | ``` optional func spellServer(_ sender: NSSpellServer, checkString stringToCheck: String, offset offset: Int, types checkingTypes: NSTextCheckingTypes, options options: [NSObject : AnyObject]?, orthography orthography: NSOrthography?, wordCount wordCount: UnsafeMutablePointer<Int>) -> [AnyObject]? ``` | OS X 10.6 | yes |

Modified NSSpellServerDelegate.spellServer(NSSpellServer, didForgetWord: String, inLanguage: String)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func spellServer(_ sender: NSSpellServer!, didForgetWord word: String!, inLanguage language: String!) ``` | -- |
| To | ``` optional func spellServer(_ sender: NSSpellServer, didForgetWord word: String, inLanguage language: String) ``` | yes |

Modified NSSpellServerDelegate.spellServer(NSSpellServer, didLearnWord: String, inLanguage: String)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func spellServer(_ sender: NSSpellServer!, didLearnWord word: String!, inLanguage language: String!) ``` | -- |
| To | ``` optional func spellServer(_ sender: NSSpellServer, didLearnWord word: String, inLanguage language: String) ``` | yes |

Modified NSSpellServerDelegate.spellServer(NSSpellServer, findMisspelledWordInString: String, language: String, wordCount: UnsafeMutablePointer<Int>, countOnly: Bool) -> NSRange

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func spellServer(_ sender: NSSpellServer!, findMisspelledWordInString stringToCheck: String!, language language: String!, wordCount wordCount: UnsafePointer<Int>, countOnly countOnly: Bool) -> NSRange ``` | -- |
| To | ``` optional func spellServer(_ sender: NSSpellServer, findMisspelledWordInString stringToCheck: String, language language: String, wordCount wordCount: UnsafeMutablePointer<Int>, countOnly countOnly: Bool) -> NSRange ``` | yes |

Modified NSSpellServerDelegate.spellServer(NSSpellServer, recordResponse: Int, toCorrection: String, forWord: String, language: String)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func spellServer(_ sender: NSSpellServer!, recordResponse response: Int, toCorrection correction: String!, forWord word: String!, language language: String!) ``` | OS X 10.10 | -- |
| To | ``` optional func spellServer(_ sender: NSSpellServer, recordResponse response: Int, toCorrection correction: String, forWord word: String, language language: String) ``` | OS X 10.7 | yes |

Modified NSSpellServerDelegate.spellServer(NSSpellServer, suggestCompletionsForPartialWordRange: NSRange, inString: String, language: String) -> [AnyObject]?

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func spellServer(_ sender: NSSpellServer!, suggestCompletionsForPartialWordRange range: NSRange, inString string: String!, language language: String!) -> [AnyObject]! ``` | -- |
| To | ``` optional func spellServer(_ sender: NSSpellServer, suggestCompletionsForPartialWordRange range: NSRange, inString string: String, language language: String) -> [AnyObject]? ``` | yes |

Modified NSSpellServerDelegate.spellServer(NSSpellServer, suggestGuessesForWord: String, inLanguage: String) -> [AnyObject]?

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func spellServer(_ sender: NSSpellServer!, suggestGuessesForWord word: String!, inLanguage language: String!) -> [AnyObject]! ``` | -- |
| To | ``` optional func spellServer(_ sender: NSSpellServer, suggestGuessesForWord word: String, inLanguage language: String) -> [AnyObject]? ``` | yes |

Modified NSStream.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: NSStreamDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: NSStreamDelegate? ``` |

Modified NSStream.getBoundStreamsWithBufferSize(Int, inputStream: AutoreleasingUnsafeMutablePointer<NSInputStream?>, outputStream: AutoreleasingUnsafeMutablePointer<NSOutputStream?>) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func getBoundStreamsWithBufferSize(_ bufferSize: Int, inputStream inputStream: AutoreleasingUnsafePointer<NSInputStream?>, outputStream outputStream: AutoreleasingUnsafePointer<NSOutputStream?>) ``` |
| To | ``` class func getBoundStreamsWithBufferSize(_ bufferSize: Int, inputStream inputStream: AutoreleasingUnsafeMutablePointer<NSInputStream?>, outputStream outputStream: AutoreleasingUnsafeMutablePointer<NSOutputStream?>) ``` |

Modified NSStream.getStreamsToHost(NSHost, port: Int, inputStream: AutoreleasingUnsafeMutablePointer<NSInputStream?>, outputStream: AutoreleasingUnsafeMutablePointer<NSOutputStream?>) [class]

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` class func getStreamsToHost(_ host: NSHost!, port port: Int, inputStream inputStream: AutoreleasingUnsafePointer<NSInputStream?>, outputStream outputStream: AutoreleasingUnsafePointer<NSOutputStream?>) ``` | OS X 10.10 | -- |
| To | ``` class func getStreamsToHost(_ host: NSHost, port port: Int, inputStream inputStream: AutoreleasingUnsafeMutablePointer<NSInputStream?>, outputStream outputStream: AutoreleasingUnsafeMutablePointer<NSOutputStream?>) ``` | OS X 10.3 | OS X 10.10 |

Modified NSStream.getStreamsToHostWithName(String, port: Int, inputStream: AutoreleasingUnsafeMutablePointer<NSInputStream?>, outputStream: AutoreleasingUnsafeMutablePointer<NSOutputStream?>) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func getStreamsToHostWithName(_ hostname: String!, port port: Int, inputStream inputStream: AutoreleasingUnsafePointer<NSInputStream?>, outputStream outputStream: AutoreleasingUnsafePointer<NSOutputStream?>) ``` |
| To | ``` class func getStreamsToHostWithName(_ hostname: String, port port: Int, inputStream inputStream: AutoreleasingUnsafeMutablePointer<NSInputStream?>, outputStream outputStream: AutoreleasingUnsafeMutablePointer<NSOutputStream?>) ``` |

Modified NSStream.propertyForKey(String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func propertyForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` func propertyForKey(_ key: String) -> AnyObject? ``` |

Modified NSStream.removeFromRunLoop(NSRunLoop, forMode: String)

|  | Declaration |
| --- | --- |
| From | ``` func removeFromRunLoop(_ aRunLoop: NSRunLoop!, forMode mode: String!) ``` |
| To | ``` func removeFromRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String) ``` |

Modified NSStream.scheduleInRunLoop(NSRunLoop, forMode: String)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleInRunLoop(_ aRunLoop: NSRunLoop!, forMode mode: String!) ``` |
| To | ``` func scheduleInRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String) ``` |

Modified NSStream.setProperty(AnyObject?, forKey: String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func setProperty(_ property: AnyObject!, forKey key: String!) -> Bool ``` |
| To | ``` func setProperty(_ property: AnyObject?, forKey key: String) -> Bool ``` |

Modified NSStream.streamError

|  | Declaration |
| --- | --- |
| From | ``` var streamError: NSError! { get } ``` |
| To | ``` @NSCopying var streamError: NSError? { get } ``` |

Modified NSStreamDelegate.stream(NSStream, handleEvent: NSStreamEvent)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func stream(_ aStream: NSStream!, handleEvent eventCode: NSStreamEvent) ``` | -- |
| To | ``` optional func stream(_ aStream: NSStream, handleEvent eventCode: NSStreamEvent) ``` | yes |

Modified NSStreamEvent [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSStreamEvent : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var None: NSStreamEvent { get }     static var OpenCompleted: NSStreamEvent { get }     static var HasBytesAvailable: NSStreamEvent { get }     static var HasSpaceAvailable: NSStreamEvent { get }     static var ErrorOccurred: NSStreamEvent { get }     static var EndEncountered: NSStreamEvent { get } } ``` | RawOptionSet |
| To | ``` struct NSStreamEvent : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: NSStreamEvent { get }     static var OpenCompleted: NSStreamEvent { get }     static var HasBytesAvailable: NSStreamEvent { get }     static var HasSpaceAvailable: NSStreamEvent { get }     static var ErrorOccurred: NSStreamEvent { get }     static var EndEncountered: NSStreamEvent { get } } ``` | RawOptionSetType |

Modified NSStreamEvent.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSString

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding, Reflectable, StringLiteralConvertible |
| To | AnyObject, CKRecordValue, NSCoding, NSCopying, NSMutableCopying, NSObjectProtocol, NSPasteboardReading, NSPasteboardWriting, NSSecureCoding, Reflectable, StringLiteralConvertible |

Modified NSString.init(CString: UnsafePointer<Int8>, encoding: UInt)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(CString nullTerminatedCString: ConstUnsafePointer<Int8>, encoding encoding: UInt) ``` |
| To | ``` convenience init?(CString nullTerminatedCString: UnsafePointer<Int8>, encoding encoding: UInt) ``` |

Modified NSString.UTF8String

|  | Declaration |
| --- | --- |
| From | ``` var UTF8String: ConstUnsafePointer<Int8> { get } ``` |
| To | ``` var UTF8String: UnsafePointer<Int8> { get } ``` |

Modified NSString.init(UTF8String: UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(UTF8String nullTerminatedCString: ConstUnsafePointer<Int8>) ``` |
| To | ``` convenience init?(UTF8String nullTerminatedCString: UnsafePointer<Int8>) ``` |

Modified NSString.availableStringEncodings() -> UnsafePointer<UInt> [class]

|  | Declaration |
| --- | --- |
| From | ``` class func availableStringEncodings() -> ConstUnsafePointer<UInt> ``` |
| To | ``` class func availableStringEncodings() -> UnsafePointer<UInt> ``` |

Modified NSString.boolValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSString.init(bytes: UnsafePointer<Void>, length: Int, encoding: UInt)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(bytes bytes: ConstUnsafePointer<()>, length len: Int, encoding encoding: UInt) ``` |
| To | ``` convenience init?(bytes bytes: UnsafePointer<Void>, length len: Int, encoding encoding: UInt) ``` |

Modified NSString.init(bytesNoCopy: UnsafeMutablePointer<Void>, length: Int, encoding: UInt, freeWhenDone: Bool)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(bytesNoCopy bytes: UnsafePointer<()>, length len: Int, encoding encoding: UInt, freeWhenDone freeBuffer: Bool) ``` |
| To | ``` convenience init?(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length len: Int, encoding encoding: UInt, freeWhenDone freeBuffer: Bool) ``` |

Modified NSString.cStringUsingEncoding(UInt) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func cStringUsingEncoding(_ encoding: UInt) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func cStringUsingEncoding(_ encoding: UInt) -> UnsafePointer<Int8> ``` |

Modified NSString.capitalizedString

|  | Declaration |
| --- | --- |
| From | ``` var capitalizedString: String! { get } ``` |
| To | ``` var capitalizedString: String { get } ``` |

Modified NSString.capitalizedStringWithLocale(NSLocale?) -> String

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func capitalizedStringWithLocale(_ locale: NSLocale!) -> String! ``` | OS X 10.10 |
| To | ``` func capitalizedStringWithLocale(_ locale: NSLocale?) -> String ``` | OS X 10.8 |

Modified NSString.caseInsensitiveCompare(String) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func caseInsensitiveCompare(_ string: String!) -> NSComparisonResult ``` |
| To | ``` func caseInsensitiveCompare(_ string: String) -> NSComparisonResult ``` |

Modified NSString.init(characters: UnsafePointer<unichar>, length: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(characters characters: ConstUnsafePointer<unichar>, length length: Int) ``` |
| To | ``` convenience init(characters characters: UnsafePointer<unichar>, length length: Int) ``` |

Modified NSString.init(charactersNoCopy: UnsafeMutablePointer<unichar>, length: Int, freeWhenDone: Bool)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(charactersNoCopy characters: UnsafePointer<unichar>, length length: Int, freeWhenDone freeBuffer: Bool) ``` |
| To | ``` convenience init(charactersNoCopy characters: UnsafeMutablePointer<unichar>, length length: Int, freeWhenDone freeBuffer: Bool) ``` |

Modified NSString.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init(coder aDecoder: NSCoder) ``` |

Modified NSString.commonPrefixWithString(String, options: NSStringCompareOptions) -> String

|  | Declaration |
| --- | --- |
| From | ``` func commonPrefixWithString(_ aString: String!, options mask: NSStringCompareOptions) -> String! ``` |
| To | ``` func commonPrefixWithString(_ aString: String, options mask: NSStringCompareOptions) -> String ``` |

Modified NSString.compare(String) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func compare(_ string: String!) -> NSComparisonResult ``` |
| To | ``` func compare(_ string: String) -> NSComparisonResult ``` |

Modified NSString.compare(String, options: NSStringCompareOptions) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func compare(_ string: String!, options mask: NSStringCompareOptions) -> NSComparisonResult ``` |
| To | ``` func compare(_ string: String, options mask: NSStringCompareOptions) -> NSComparisonResult ``` |

Modified NSString.compare(String, options: NSStringCompareOptions, range: NSRange) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func compare(_ string: String!, options mask: NSStringCompareOptions, range compareRange: NSRange) -> NSComparisonResult ``` |
| To | ``` func compare(_ string: String, options mask: NSStringCompareOptions, range compareRange: NSRange) -> NSComparisonResult ``` |

Modified NSString.compare(String, options: NSStringCompareOptions, range: NSRange, locale: AnyObject?) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func compare(_ string: String!, options mask: NSStringCompareOptions, range compareRange: NSRange, locale locale: AnyObject!) -> NSComparisonResult ``` |
| To | ``` func compare(_ string: String, options mask: NSStringCompareOptions, range compareRange: NSRange, locale locale: AnyObject?) -> NSComparisonResult ``` |

Modified NSString.completePathIntoString(AutoreleasingUnsafeMutablePointer<NSString?>, caseSensitive: Bool, matchesIntoArray: AutoreleasingUnsafeMutablePointer<NSArray?>, filterTypes:[AnyObject]?) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func completePathIntoString(_ outputName: AutoreleasingUnsafePointer<NSString?>, caseSensitive flag: Bool, matchesIntoArray outputArray: AutoreleasingUnsafePointer<NSArray?>, filterTypes filterTypes: [AnyObject]!) -> Int ``` |
| To | ``` func completePathIntoString(_ outputName: AutoreleasingUnsafeMutablePointer<NSString?>, caseSensitive flag: Bool, matchesIntoArray outputArray: AutoreleasingUnsafeMutablePointer<NSArray?>, filterTypes filterTypes: [AnyObject]?) -> Int ``` |

Modified NSString.componentsSeparatedByCharactersInSet(NSCharacterSet) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func componentsSeparatedByCharactersInSet(_ separator: NSCharacterSet!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func componentsSeparatedByCharactersInSet(_ separator: NSCharacterSet) -> [AnyObject] ``` | OS X 10.5 |

Modified NSString.componentsSeparatedByString(String) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func componentsSeparatedByString(_ separator: String!) -> [AnyObject]! ``` |
| To | ``` func componentsSeparatedByString(_ separator: String) -> [AnyObject] ``` |

Modified NSString.containsString(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func containsString(_ aString: String!) -> Bool ``` |
| To | ``` func containsString(_ aString: String) -> Bool ``` |

Modified NSString.init(contentsOfFile: String, encoding: UInt, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfFile path: String!, encoding enc: UInt, error error: NSErrorPointer) ``` |
| To | ``` convenience init?(contentsOfFile path: String, encoding enc: UInt, error error: NSErrorPointer) ``` |

Modified NSString.init(contentsOfFile: String, usedEncoding: UnsafeMutablePointer<UInt>, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfFile path: String!, usedEncoding enc: UnsafePointer<UInt>, error error: NSErrorPointer) ``` |
| To | ``` convenience init?(contentsOfFile path: String, usedEncoding enc: UnsafeMutablePointer<UInt>, error error: NSErrorPointer) ``` |

Modified NSString.init(contentsOfURL: NSURL, encoding: UInt, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL url: NSURL!, encoding enc: UInt, error error: NSErrorPointer) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL, encoding enc: UInt, error error: NSErrorPointer) ``` |

Modified NSString.init(contentsOfURL: NSURL, usedEncoding: UnsafeMutablePointer<UInt>, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL url: NSURL!, usedEncoding enc: UnsafePointer<UInt>, error error: NSErrorPointer) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL, usedEncoding enc: UnsafeMutablePointer<UInt>, error error: NSErrorPointer) ``` |

Modified NSString.init(data: NSData, encoding: UInt)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(data data: NSData!, encoding encoding: UInt) ``` |
| To | ``` convenience init?(data data: NSData, encoding encoding: UInt) ``` |

Modified NSString.dataUsingEncoding(UInt) -> NSData?

|  | Declaration |
| --- | --- |
| From | ``` func dataUsingEncoding(_ encoding: UInt) -> NSData! ``` |
| To | ``` func dataUsingEncoding(_ encoding: UInt) -> NSData? ``` |

Modified NSString.dataUsingEncoding(UInt, allowLossyConversion: Bool) -> NSData?

|  | Declaration |
| --- | --- |
| From | ``` func dataUsingEncoding(_ encoding: UInt, allowLossyConversion lossy: Bool) -> NSData! ``` |
| To | ``` func dataUsingEncoding(_ encoding: UInt, allowLossyConversion lossy: Bool) -> NSData? ``` |

Modified NSString.decomposedStringWithCanonicalMapping

|  | Declaration |
| --- | --- |
| From | ``` var decomposedStringWithCanonicalMapping: String! { get } ``` |
| To | ``` var decomposedStringWithCanonicalMapping: String { get } ``` |

Modified NSString.decomposedStringWithCompatibilityMapping

|  | Declaration |
| --- | --- |
| From | ``` var decomposedStringWithCompatibilityMapping: String! { get } ``` |
| To | ``` var decomposedStringWithCompatibilityMapping: String { get } ``` |

Modified NSString.description

|  | Declaration |
| --- | --- |
| From | ``` var description: String! { get } ``` |
| To | ``` var description: String { get } ``` |

Modified NSString.enumerateLinesUsingBlock((String!, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateLinesUsingBlock(_ block: ((String!, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateLinesUsingBlock(_ block: (String!, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.6 |

Modified NSString.enumerateLinguisticTagsInRange(NSRange, scheme: String, options: NSLinguisticTaggerOptions, orthography: NSOrthography?, usingBlock:(String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateLinguisticTagsInRange(_ range: NSRange, scheme tagScheme: String!, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography!, usingBlock block: ((String!, NSRange, NSRange, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateLinguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, usingBlock block: (String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.7 |

Modified NSString.enumerateSubstringsInRange(NSRange, options: NSStringEnumerationOptions, usingBlock:(String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateSubstringsInRange(_ range: NSRange, options opts: NSStringEnumerationOptions, usingBlock block: ((String!, NSRange, NSRange, UnsafePointer<ObjCBool>) -> Void)!) ``` | OS X 10.10 |
| To | ``` func enumerateSubstringsInRange(_ range: NSRange, options opts: NSStringEnumerationOptions, usingBlock block: (String!, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | OS X 10.6 |

Modified NSString.fileSystemRepresentation

|  | Declaration |
| --- | --- |
| From | ``` var fileSystemRepresentation: ConstUnsafePointer<Int8> { get } ``` |
| To | ``` var fileSystemRepresentation: UnsafePointer<Int8> { get } ``` |

Modified NSString.init(format: String, arguments: CVaListPointer)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(format format: String!, arguments argList: CVaListPointer) ``` |
| To | ``` convenience init(format format: String, arguments argList: CVaListPointer) ``` |

Modified NSString.init(format: String, locale: AnyObject?, arguments: CVaListPointer)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(format format: String!, locale locale: AnyObject!, arguments argList: CVaListPointer) ``` |
| To | ``` convenience init(format format: String, locale locale: AnyObject?, arguments argList: CVaListPointer) ``` |

Modified NSString.getBytes(UnsafeMutablePointer<Void>, maxLength: Int, usedLength: UnsafeMutablePointer<Int>, encoding: UInt, options: NSStringEncodingConversionOptions, range: NSRange, remainingRange: NSRangePointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getBytes(_ buffer: UnsafePointer<()>, maxLength maxBufferCount: Int, usedLength usedBufferCount: UnsafePointer<Int>, encoding encoding: UInt, options options: NSStringEncodingConversionOptions, range range: NSRange, remainingRange leftover: NSRangePointer) -> Bool ``` |
| To | ``` func getBytes(_ buffer: UnsafeMutablePointer<Void>, maxLength maxBufferCount: Int, usedLength usedBufferCount: UnsafeMutablePointer<Int>, encoding encoding: UInt, options options: NSStringEncodingConversionOptions, range range: NSRange, remainingRange leftover: NSRangePointer) -> Bool ``` |

Modified NSString.getCString(UnsafeMutablePointer<Int8>, maxLength: Int, encoding: UInt) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getCString(_ buffer: UnsafePointer<Int8>, maxLength maxBufferCount: Int, encoding encoding: UInt) -> Bool ``` |
| To | ``` func getCString(_ buffer: UnsafeMutablePointer<Int8>, maxLength maxBufferCount: Int, encoding encoding: UInt) -> Bool ``` |

Modified NSString.getCharacters(UnsafeMutablePointer<unichar>)

|  | Declaration |
| --- | --- |
| From | ``` func getCharacters(_ buffer: UnsafePointer<unichar>) ``` |
| To | ``` func getCharacters(_ buffer: UnsafeMutablePointer<unichar>) ``` |

Modified NSString.getCharacters(UnsafeMutablePointer<unichar>, range: NSRange)

|  | Declaration |
| --- | --- |
| From | ``` func getCharacters(_ buffer: UnsafePointer<unichar>, range aRange: NSRange) ``` |
| To | ``` func getCharacters(_ buffer: UnsafeMutablePointer<unichar>, range aRange: NSRange) ``` |

Modified NSString.getFileSystemRepresentation(UnsafeMutablePointer<Int8>, maxLength: Int) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getFileSystemRepresentation(_ cname: UnsafePointer<Int8>, maxLength max: Int) -> Bool ``` |
| To | ``` func getFileSystemRepresentation(_ cname: UnsafeMutablePointer<Int8>, maxLength max: Int) -> Bool ``` |

Modified NSString.getLineStart(UnsafeMutablePointer<Int>, end: UnsafeMutablePointer<Int>, contentsEnd: UnsafeMutablePointer<Int>, forRange: NSRange)

|  | Declaration |
| --- | --- |
| From | ``` func getLineStart(_ startPtr: UnsafePointer<Int>, end lineEndPtr: UnsafePointer<Int>, contentsEnd contentsEndPtr: UnsafePointer<Int>, forRange range: NSRange) ``` |
| To | ``` func getLineStart(_ startPtr: UnsafeMutablePointer<Int>, end lineEndPtr: UnsafeMutablePointer<Int>, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>, forRange range: NSRange) ``` |

Modified NSString.getParagraphStart(UnsafeMutablePointer<Int>, end: UnsafeMutablePointer<Int>, contentsEnd: UnsafeMutablePointer<Int>, forRange: NSRange)

|  | Declaration |
| --- | --- |
| From | ``` func getParagraphStart(_ startPtr: UnsafePointer<Int>, end parEndPtr: UnsafePointer<Int>, contentsEnd contentsEndPtr: UnsafePointer<Int>, forRange range: NSRange) ``` |
| To | ``` func getParagraphStart(_ startPtr: UnsafeMutablePointer<Int>, end parEndPtr: UnsafeMutablePointer<Int>, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>, forRange range: NSRange) ``` |

Modified NSString.hasPrefix(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func hasPrefix(_ aString: String!) -> Bool ``` |
| To | ``` func hasPrefix(_ aString: String) -> Bool ``` |

Modified NSString.hasSuffix(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func hasSuffix(_ aString: String!) -> Bool ``` |
| To | ``` func hasSuffix(_ aString: String) -> Bool ``` |

Modified NSString.integerValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSString.isEqualToString(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToString(_ aString: String!) -> Bool ``` |
| To | ``` func isEqualToString(_ aString: String) -> Bool ``` |

Modified NSString.lastPathComponent

|  | Declaration |
| --- | --- |
| From | ``` var lastPathComponent: String! { get } ``` |
| To | ``` var lastPathComponent: String { get } ``` |

Modified NSString.linguisticTagsInRange(NSRange, scheme: String, options: NSLinguisticTaggerOptions, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func linguisticTagsInRange(_ range: NSRange, scheme tagScheme: String!, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography!, tokenRanges tokenRanges: AutoreleasingUnsafePointer<NSArray?>) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func linguisticTagsInRange(_ range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, tokenRanges tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>) -> [AnyObject] ``` | OS X 10.7 |

Modified NSString.localizedCaseInsensitiveCompare(String) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func localizedCaseInsensitiveCompare(_ string: String!) -> NSComparisonResult ``` |
| To | ``` func localizedCaseInsensitiveCompare(_ string: String) -> NSComparisonResult ``` |

Modified NSString.localizedCaseInsensitiveContainsString(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func localizedCaseInsensitiveContainsString(_ aString: String!) -> Bool ``` |
| To | ``` func localizedCaseInsensitiveContainsString(_ aString: String) -> Bool ``` |

Modified NSString.localizedCompare(String) -> NSComparisonResult

|  | Declaration |
| --- | --- |
| From | ``` func localizedCompare(_ string: String!) -> NSComparisonResult ``` |
| To | ``` func localizedCompare(_ string: String) -> NSComparisonResult ``` |

Modified NSString.localizedNameOfStringEncoding(UInt) -> String [class]

|  | Declaration |
| --- | --- |
| From | ``` class func localizedNameOfStringEncoding(_ encoding: UInt) -> String! ``` |
| To | ``` class func localizedNameOfStringEncoding(_ encoding: UInt) -> String ``` |

Modified NSString.localizedStandardCompare(String) -> NSComparisonResult

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func localizedStandardCompare(_ string: String!) -> NSComparisonResult ``` | OS X 10.10 |
| To | ``` func localizedStandardCompare(_ string: String) -> NSComparisonResult ``` | OS X 10.6 |

Modified NSString.longLongValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSString.lowercaseString

|  | Declaration |
| --- | --- |
| From | ``` var lowercaseString: String! { get } ``` |
| To | ``` var lowercaseString: String { get } ``` |

Modified NSString.lowercaseStringWithLocale(NSLocale?) -> String

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func lowercaseStringWithLocale(_ locale: NSLocale!) -> String! ``` | OS X 10.10 |
| To | ``` func lowercaseStringWithLocale(_ locale: NSLocale?) -> String ``` | OS X 10.8 |

Modified NSString.pathComponents

|  | Declaration |
| --- | --- |
| From | ``` var pathComponents: [AnyObject]! { get } ``` |
| To | ``` var pathComponents: [AnyObject] { get } ``` |

Modified NSString.pathExtension

|  | Declaration |
| --- | --- |
| From | ``` var pathExtension: String! { get } ``` |
| To | ``` var pathExtension: String { get } ``` |

Modified NSString.pathWithComponents([AnyObject]) -> String [class]

|  | Declaration |
| --- | --- |
| From | ``` class func pathWithComponents(_ components: [AnyObject]!) -> String! ``` |
| To | ``` class func pathWithComponents(_ components: [AnyObject]) -> String ``` |

Modified NSString.precomposedStringWithCanonicalMapping

|  | Declaration |
| --- | --- |
| From | ``` var precomposedStringWithCanonicalMapping: String! { get } ``` |
| To | ``` var precomposedStringWithCanonicalMapping: String { get } ``` |

Modified NSString.precomposedStringWithCompatibilityMapping

|  | Declaration |
| --- | --- |
| From | ``` var precomposedStringWithCompatibilityMapping: String! { get } ``` |
| To | ``` var precomposedStringWithCompatibilityMapping: String { get } ``` |

Modified NSString.propertyList() -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func propertyList() -> AnyObject! ``` |
| To | ``` func propertyList() -> AnyObject ``` |

Modified NSString.propertyListFromStringsFileFormat() -> [NSObject: AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func propertyListFromStringsFileFormat() -> [NSObject : AnyObject]! ``` |
| To | ``` func propertyListFromStringsFileFormat() -> [NSObject : AnyObject]? ``` |

Modified NSString.rangeOfCharacterFromSet(NSCharacterSet) -> NSRange

|  | Declaration |
| --- | --- |
| From | ``` func rangeOfCharacterFromSet(_ aSet: NSCharacterSet!) -> NSRange ``` |
| To | ``` func rangeOfCharacterFromSet(_ aSet: NSCharacterSet) -> NSRange ``` |

Modified NSString.rangeOfCharacterFromSet(NSCharacterSet, options: NSStringCompareOptions) -> NSRange

|  | Declaration |
| --- | --- |
| From | ``` func rangeOfCharacterFromSet(_ aSet: NSCharacterSet!, options mask: NSStringCompareOptions) -> NSRange ``` |
| To | ``` func rangeOfCharacterFromSet(_ aSet: NSCharacterSet, options mask: NSStringCompareOptions) -> NSRange ``` |

Modified NSString.rangeOfCharacterFromSet(NSCharacterSet, options: NSStringCompareOptions, range: NSRange) -> NSRange

|  | Declaration |
| --- | --- |
| From | ``` func rangeOfCharacterFromSet(_ aSet: NSCharacterSet!, options mask: NSStringCompareOptions, range searchRange: NSRange) -> NSRange ``` |
| To | ``` func rangeOfCharacterFromSet(_ aSet: NSCharacterSet, options mask: NSStringCompareOptions, range searchRange: NSRange) -> NSRange ``` |

Modified NSString.rangeOfComposedCharacterSequencesForRange(NSRange) -> NSRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSString.rangeOfString(String) -> NSRange

|  | Declaration |
| --- | --- |
| From | ``` func rangeOfString(_ aString: String!) -> NSRange ``` |
| To | ``` func rangeOfString(_ aString: String) -> NSRange ``` |

Modified NSString.rangeOfString(String, options: NSStringCompareOptions) -> NSRange

|  | Declaration |
| --- | --- |
| From | ``` func rangeOfString(_ aString: String!, options mask: NSStringCompareOptions) -> NSRange ``` |
| To | ``` func rangeOfString(_ aString: String, options mask: NSStringCompareOptions) -> NSRange ``` |

Modified NSString.rangeOfString(String, options: NSStringCompareOptions, range: NSRange) -> NSRange

|  | Declaration |
| --- | --- |
| From | ``` func rangeOfString(_ aString: String!, options mask: NSStringCompareOptions, range searchRange: NSRange) -> NSRange ``` |
| To | ``` func rangeOfString(_ aString: String, options mask: NSStringCompareOptions, range searchRange: NSRange) -> NSRange ``` |

Modified NSString.rangeOfString(String, options: NSStringCompareOptions, range: NSRange, locale: NSLocale?) -> NSRange

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func rangeOfString(_ aString: String!, options mask: NSStringCompareOptions, range searchRange: NSRange, locale locale: NSLocale!) -> NSRange ``` | OS X 10.10 |
| To | ``` func rangeOfString(_ aString: String, options mask: NSStringCompareOptions, range searchRange: NSRange, locale locale: NSLocale?) -> NSRange ``` | OS X 10.5 |

Modified NSString.init(string: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(string aString: String!) ``` |
| To | ``` convenience init(string aString: String) ``` |

Modified NSString.stringByAbbreviatingWithTildeInPath

|  | Declaration |
| --- | --- |
| From | ``` var stringByAbbreviatingWithTildeInPath: String! { get } ``` |
| To | ``` var stringByAbbreviatingWithTildeInPath: String { get } ``` |

Modified NSString.stringByAddingPercentEncodingWithAllowedCharacters(NSCharacterSet) -> String?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func stringByAddingPercentEncodingWithAllowedCharacters(_ allowedCharacters: NSCharacterSet!) -> String! ``` | OS X 10.10 |
| To | ``` func stringByAddingPercentEncodingWithAllowedCharacters(_ allowedCharacters: NSCharacterSet) -> String? ``` | OS X 10.9 |

Modified NSString.stringByAddingPercentEscapesUsingEncoding(UInt) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func stringByAddingPercentEscapesUsingEncoding(_ enc: UInt) -> String! ``` |
| To | ``` func stringByAddingPercentEscapesUsingEncoding(_ enc: UInt) -> String? ``` |

Modified NSString.stringByAppendingPathComponent(String) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringByAppendingPathComponent(_ str: String!) -> String! ``` |
| To | ``` func stringByAppendingPathComponent(_ str: String) -> String ``` |

Modified NSString.stringByAppendingPathExtension(String) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func stringByAppendingPathExtension(_ str: String!) -> String! ``` |
| To | ``` func stringByAppendingPathExtension(_ str: String) -> String? ``` |

Modified NSString.stringByAppendingString(String) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringByAppendingString(_ aString: String!) -> String! ``` |
| To | ``` func stringByAppendingString(_ aString: String) -> String ``` |

Modified NSString.stringByDeletingLastPathComponent

|  | Declaration |
| --- | --- |
| From | ``` var stringByDeletingLastPathComponent: String! { get } ``` |
| To | ``` var stringByDeletingLastPathComponent: String { get } ``` |

Modified NSString.stringByDeletingPathExtension

|  | Declaration |
| --- | --- |
| From | ``` var stringByDeletingPathExtension: String! { get } ``` |
| To | ``` var stringByDeletingPathExtension: String { get } ``` |

Modified NSString.stringByExpandingTildeInPath

|  | Declaration |
| --- | --- |
| From | ``` var stringByExpandingTildeInPath: String! { get } ``` |
| To | ``` var stringByExpandingTildeInPath: String { get } ``` |

Modified NSString.stringByFoldingWithOptions(NSStringCompareOptions, locale: NSLocale?) -> String

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func stringByFoldingWithOptions(_ options: NSStringCompareOptions, locale locale: NSLocale!) -> String! ``` | OS X 10.10 |
| To | ``` func stringByFoldingWithOptions(_ options: NSStringCompareOptions, locale locale: NSLocale?) -> String ``` | OS X 10.5 |

Modified NSString.stringByPaddingToLength(Int, withString: String, startingAtIndex: Int) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringByPaddingToLength(_ newLength: Int, withString padString: String!, startingAtIndex padIndex: Int) -> String! ``` |
| To | ``` func stringByPaddingToLength(_ newLength: Int, withString padString: String, startingAtIndex padIndex: Int) -> String ``` |

Modified NSString.stringByRemovingPercentEncoding

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var stringByRemovingPercentEncoding: String! { get } ``` | OS X 10.10 |
| To | ``` var stringByRemovingPercentEncoding: String? { get } ``` | OS X 10.9 |

Modified NSString.stringByReplacingCharactersInRange(NSRange, withString: String) -> String

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func stringByReplacingCharactersInRange(_ range: NSRange, withString replacement: String!) -> String! ``` | OS X 10.10 |
| To | ``` func stringByReplacingCharactersInRange(_ range: NSRange, withString replacement: String) -> String ``` | OS X 10.5 |

Modified NSString.stringByReplacingOccurrencesOfString(String, withString: String) -> String

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func stringByReplacingOccurrencesOfString(_ target: String!, withString replacement: String!) -> String! ``` | OS X 10.10 |
| To | ``` func stringByReplacingOccurrencesOfString(_ target: String, withString replacement: String) -> String ``` | OS X 10.5 |

Modified NSString.stringByReplacingOccurrencesOfString(String, withString: String, options: NSStringCompareOptions, range: NSRange) -> String

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func stringByReplacingOccurrencesOfString(_ target: String!, withString replacement: String!, options options: NSStringCompareOptions, range searchRange: NSRange) -> String! ``` | OS X 10.10 |
| To | ``` func stringByReplacingOccurrencesOfString(_ target: String, withString replacement: String, options options: NSStringCompareOptions, range searchRange: NSRange) -> String ``` | OS X 10.5 |

Modified NSString.stringByReplacingPercentEscapesUsingEncoding(UInt) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func stringByReplacingPercentEscapesUsingEncoding(_ enc: UInt) -> String! ``` |
| To | ``` func stringByReplacingPercentEscapesUsingEncoding(_ enc: UInt) -> String? ``` |

Modified NSString.stringByResolvingSymlinksInPath

|  | Declaration |
| --- | --- |
| From | ``` var stringByResolvingSymlinksInPath: String! { get } ``` |
| To | ``` var stringByResolvingSymlinksInPath: String { get } ``` |

Modified NSString.stringByStandardizingPath

|  | Declaration |
| --- | --- |
| From | ``` var stringByStandardizingPath: String! { get } ``` |
| To | ``` var stringByStandardizingPath: String { get } ``` |

Modified NSString.stringByTrimmingCharactersInSet(NSCharacterSet) -> String

|  | Declaration |
| --- | --- |
| From | ``` func stringByTrimmingCharactersInSet(_ set: NSCharacterSet!) -> String! ``` |
| To | ``` func stringByTrimmingCharactersInSet(_ set: NSCharacterSet) -> String ``` |

Modified NSString.stringEncodingForData(NSData, encodingOptions:[NSObject: AnyObject]?, convertedString: AutoreleasingUnsafeMutablePointer<NSString?>, usedLossyConversion: UnsafeMutablePointer<ObjCBool>) -> UInt [class]

|  | Declaration |
| --- | --- |
| From | ``` class func stringEncodingForData(_ data: NSData!, encodingOptions opts: [NSObject : AnyObject]!, convertedString string: AutoreleasingUnsafePointer<NSString?>, usedLossyConversion usedLossyConversion: UnsafePointer<ObjCBool>) -> UInt ``` |
| To | ``` class func stringEncodingForData(_ data: NSData, encodingOptions opts: [NSObject : AnyObject]?, convertedString string: AutoreleasingUnsafeMutablePointer<NSString?>, usedLossyConversion usedLossyConversion: UnsafeMutablePointer<ObjCBool>) -> UInt ``` |

Modified NSString.stringsByAppendingPaths([AnyObject]) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func stringsByAppendingPaths(_ paths: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func stringsByAppendingPaths(_ paths: [AnyObject]) -> [AnyObject] ``` |

Modified NSString.substringFromIndex(Int) -> String

|  | Declaration |
| --- | --- |
| From | ``` func substringFromIndex(_ from: Int) -> String! ``` |
| To | ``` func substringFromIndex(_ from: Int) -> String ``` |

Modified NSString.substringToIndex(Int) -> String

|  | Declaration |
| --- | --- |
| From | ``` func substringToIndex(_ to: Int) -> String! ``` |
| To | ``` func substringToIndex(_ to: Int) -> String ``` |

Modified NSString.substringWithRange(NSRange) -> String

|  | Declaration |
| --- | --- |
| From | ``` func substringWithRange(_ range: NSRange) -> String! ``` |
| To | ``` func substringWithRange(_ range: NSRange) -> String ``` |

Modified NSString.uppercaseString

|  | Declaration |
| --- | --- |
| From | ``` var uppercaseString: String! { get } ``` |
| To | ``` var uppercaseString: String { get } ``` |

Modified NSString.uppercaseStringWithLocale(NSLocale?) -> String

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func uppercaseStringWithLocale(_ locale: NSLocale!) -> String! ``` | OS X 10.10 |
| To | ``` func uppercaseStringWithLocale(_ locale: NSLocale?) -> String ``` | OS X 10.8 |

Modified NSString.writeToFile(String, atomically: Bool, encoding: UInt, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToFile(_ path: String!, atomically useAuxiliaryFile: Bool, encoding enc: UInt, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool, encoding enc: UInt, error error: NSErrorPointer) -> Bool ``` |

Modified NSString.writeToURL(NSURL, atomically: Bool, encoding: UInt, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ url: NSURL!, atomically useAuxiliaryFile: Bool, encoding enc: UInt, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func writeToURL(_ url: NSURL, atomically useAuxiliaryFile: Bool, encoding enc: UInt, error error: NSErrorPointer) -> Bool ``` |

Modified NSStringCompareOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSStringCompareOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var CaseInsensitiveSearch: NSStringCompareOptions { get }     static var LiteralSearch: NSStringCompareOptions { get }     static var BackwardsSearch: NSStringCompareOptions { get }     static var AnchoredSearch: NSStringCompareOptions { get }     static var NumericSearch: NSStringCompareOptions { get }     static var DiacriticInsensitiveSearch: NSStringCompareOptions { get }     static var WidthInsensitiveSearch: NSStringCompareOptions { get }     static var ForcedOrderingSearch: NSStringCompareOptions { get }     static var RegularExpressionSearch: NSStringCompareOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSStringCompareOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var CaseInsensitiveSearch: NSStringCompareOptions { get }     static var LiteralSearch: NSStringCompareOptions { get }     static var BackwardsSearch: NSStringCompareOptions { get }     static var AnchoredSearch: NSStringCompareOptions { get }     static var NumericSearch: NSStringCompareOptions { get }     static var DiacriticInsensitiveSearch: NSStringCompareOptions { get }     static var WidthInsensitiveSearch: NSStringCompareOptions { get }     static var ForcedOrderingSearch: NSStringCompareOptions { get }     static var RegularExpressionSearch: NSStringCompareOptions { get } } ``` | RawOptionSetType |

Modified NSStringCompareOptions.DiacriticInsensitiveSearch

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSStringCompareOptions.ForcedOrderingSearch

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSStringCompareOptions.RegularExpressionSearch

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSStringCompareOptions.WidthInsensitiveSearch

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSStringCompareOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSStringEncodingConversionOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSStringEncodingConversionOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var AllowLossy: NSStringEncodingConversionOptions { get }     static var ExternalRepresentation: NSStringEncodingConversionOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSStringEncodingConversionOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var AllowLossy: NSStringEncodingConversionOptions { get }     static var ExternalRepresentation: NSStringEncodingConversionOptions { get } } ``` | RawOptionSetType |

Modified NSStringEncodingConversionOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSStringEnumerationOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSStringEnumerationOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var ByLines: NSStringEnumerationOptions { get }     static var ByParagraphs: NSStringEnumerationOptions { get }     static var ByComposedCharacterSequences: NSStringEnumerationOptions { get }     static var ByWords: NSStringEnumerationOptions { get }     static var BySentences: NSStringEnumerationOptions { get }     static var Reverse: NSStringEnumerationOptions { get }     static var SubstringNotRequired: NSStringEnumerationOptions { get }     static var Localized: NSStringEnumerationOptions { get } } ``` | RawOptionSet |
| To | ``` struct NSStringEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ByLines: NSStringEnumerationOptions { get }     static var ByParagraphs: NSStringEnumerationOptions { get }     static var ByComposedCharacterSequences: NSStringEnumerationOptions { get }     static var ByWords: NSStringEnumerationOptions { get }     static var BySentences: NSStringEnumerationOptions { get }     static var Reverse: NSStringEnumerationOptions { get }     static var SubstringNotRequired: NSStringEnumerationOptions { get }     static var Localized: NSStringEnumerationOptions { get } } ``` | RawOptionSetType |

Modified NSStringEnumerationOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSSwappedDouble [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSSwappedDouble {     var v: UInt64 } ``` |
| To | ``` struct NSSwappedDouble {     var v: UInt64     init()     init(v v: UInt64) } ``` |

Modified NSSwappedFloat [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSSwappedFloat {     var v: UInt32 } ``` |
| To | ``` struct NSSwappedFloat {     var v: UInt32     init()     init(v v: UInt32) } ``` |

Modified NSTask.arguments

|  | Declaration |
| --- | --- |
| From | ``` var arguments: [AnyObject]! ``` |
| To | ``` var arguments: [AnyObject] ``` |

Modified NSTask.currentDirectoryPath

|  | Declaration |
| --- | --- |
| From | ``` var currentDirectoryPath: String! ``` |
| To | ``` var currentDirectoryPath: String ``` |

Modified NSTask.environment

|  | Declaration |
| --- | --- |
| From | ``` var environment: [NSObject : AnyObject]! ``` |
| To | ``` var environment: [NSObject : AnyObject] ``` |

Modified NSTask.launchPath

|  | Declaration |
| --- | --- |
| From | ``` var launchPath: String! ``` |
| To | ``` var launchPath: String ``` |

Modified NSTask.launchedTaskWithLaunchPath(String, arguments:[AnyObject]) -> NSTask [class]

|  | Declaration |
| --- | --- |
| From | ``` class func launchedTaskWithLaunchPath(_ path: String!, arguments arguments: [AnyObject]!) -> NSTask! ``` |
| To | ``` class func launchedTaskWithLaunchPath(_ path: String, arguments arguments: [AnyObject]) -> NSTask ``` |

Modified NSTask.standardError

|  | Declaration |
| --- | --- |
| From | ``` var standardError: AnyObject! ``` |
| To | ``` var standardError: AnyObject ``` |

Modified NSTask.standardInput

|  | Declaration |
| --- | --- |
| From | ``` var standardInput: AnyObject! ``` |
| To | ``` var standardInput: AnyObject ``` |

Modified NSTask.standardOutput

|  | Declaration |
| --- | --- |
| From | ``` var standardOutput: AnyObject! ``` |
| To | ``` var standardOutput: AnyObject ``` |

Modified NSTask.terminationHandler

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var terminationHandler: ((NSTask!) -> Void)! ``` | OS X 10.10 |
| To | ``` var terminationHandler: ((NSTask!) -> Void)? ``` | OS X 10.7 |

Modified NSTask.terminationReason

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSTaskTerminationReason [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSTextCheckingResult

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSTextCheckingResult.URL

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL? { get } ``` |

Modified NSTextCheckingResult.addressCheckingResultWithRange(NSRange, components:[NSObject: AnyObject]) -> NSTextCheckingResult [class]

|  | Declaration |
| --- | --- |
| From | ``` class func addressCheckingResultWithRange(_ range: NSRange, components components: [NSObject : AnyObject]!) -> NSTextCheckingResult! ``` |
| To | ``` class func addressCheckingResultWithRange(_ range: NSRange, components components: [NSObject : AnyObject]) -> NSTextCheckingResult ``` |

Modified NSTextCheckingResult.addressComponents

|  | Declaration |
| --- | --- |
| From | ``` var addressComponents: [NSObject : AnyObject]! { get } ``` |
| To | ``` var addressComponents: [NSObject : AnyObject]? { get } ``` |

Modified NSTextCheckingResult.alternativeStrings

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var alternativeStrings: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var alternativeStrings: [AnyObject]? { get } ``` | OS X 10.9 |

Modified NSTextCheckingResult.components

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var components: [NSObject : AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var components: [NSObject : AnyObject]? { get } ``` | OS X 10.7 |

Modified NSTextCheckingResult.correctionCheckingResultWithRange(NSRange, replacementString: String) -> NSTextCheckingResult [class]

|  | Declaration |
| --- | --- |
| From | ``` class func correctionCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String!) -> NSTextCheckingResult! ``` |
| To | ``` class func correctionCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String) -> NSTextCheckingResult ``` |

Modified NSTextCheckingResult.correctionCheckingResultWithRange(NSRange, replacementString: String, alternativeStrings:[AnyObject]) -> NSTextCheckingResult [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func correctionCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String!, alternativeStrings alternativeStrings: [AnyObject]!) -> NSTextCheckingResult! ``` | OS X 10.10 |
| To | ``` class func correctionCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String, alternativeStrings alternativeStrings: [AnyObject]) -> NSTextCheckingResult ``` | OS X 10.9 |

Modified NSTextCheckingResult.dashCheckingResultWithRange(NSRange, replacementString: String) -> NSTextCheckingResult [class]

|  | Declaration |
| --- | --- |
| From | ``` class func dashCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String!) -> NSTextCheckingResult! ``` |
| To | ``` class func dashCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String) -> NSTextCheckingResult ``` |

Modified NSTextCheckingResult.date

|  | Declaration |
| --- | --- |
| From | ``` var date: NSDate! { get } ``` |
| To | ``` @NSCopying var date: NSDate? { get } ``` |

Modified NSTextCheckingResult.dateCheckingResultWithRange(NSRange, date: NSDate) -> NSTextCheckingResult [class]

|  | Declaration |
| --- | --- |
| From | ``` class func dateCheckingResultWithRange(_ range: NSRange, date date: NSDate!) -> NSTextCheckingResult! ``` |
| To | ``` class func dateCheckingResultWithRange(_ range: NSRange, date date: NSDate) -> NSTextCheckingResult ``` |

Modified NSTextCheckingResult.dateCheckingResultWithRange(NSRange, date: NSDate, timeZone: NSTimeZone, duration: NSTimeInterval) -> NSTextCheckingResult [class]

|  | Declaration |
| --- | --- |
| From | ``` class func dateCheckingResultWithRange(_ range: NSRange, date date: NSDate!, timeZone timeZone: NSTimeZone!, duration duration: NSTimeInterval) -> NSTextCheckingResult! ``` |
| To | ``` class func dateCheckingResultWithRange(_ range: NSRange, date date: NSDate, timeZone timeZone: NSTimeZone, duration duration: NSTimeInterval) -> NSTextCheckingResult ``` |

Modified NSTextCheckingResult.grammarCheckingResultWithRange(NSRange, details:[AnyObject]) -> NSTextCheckingResult [class]

|  | Declaration |
| --- | --- |
| From | ``` class func grammarCheckingResultWithRange(_ range: NSRange, details details: [AnyObject]!) -> NSTextCheckingResult! ``` |
| To | ``` class func grammarCheckingResultWithRange(_ range: NSRange, details details: [AnyObject]) -> NSTextCheckingResult ``` |

Modified NSTextCheckingResult.grammarDetails

|  | Declaration |
| --- | --- |
| From | ``` var grammarDetails: [AnyObject]! { get } ``` |
| To | ``` var grammarDetails: [AnyObject]? { get } ``` |

Modified NSTextCheckingResult.linkCheckingResultWithRange(NSRange, URL: NSURL) -> NSTextCheckingResult [class]

|  | Declaration |
| --- | --- |
| From | ``` class func linkCheckingResultWithRange(_ range: NSRange, URL url: NSURL!) -> NSTextCheckingResult! ``` |
| To | ``` class func linkCheckingResultWithRange(_ range: NSRange, URL url: NSURL) -> NSTextCheckingResult ``` |

Modified NSTextCheckingResult.numberOfRanges

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSTextCheckingResult.orthography

|  | Declaration |
| --- | --- |
| From | ``` var orthography: NSOrthography! { get } ``` |
| To | ``` @NSCopying var orthography: NSOrthography? { get } ``` |

Modified NSTextCheckingResult.orthographyCheckingResultWithRange(NSRange, orthography: NSOrthography) -> NSTextCheckingResult [class]

|  | Declaration |
| --- | --- |
| From | ``` class func orthographyCheckingResultWithRange(_ range: NSRange, orthography orthography: NSOrthography!) -> NSTextCheckingResult! ``` |
| To | ``` class func orthographyCheckingResultWithRange(_ range: NSRange, orthography orthography: NSOrthography) -> NSTextCheckingResult ``` |

Modified NSTextCheckingResult.phoneNumber

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var phoneNumber: String! { get } ``` | OS X 10.10 |
| To | ``` var phoneNumber: String? { get } ``` | OS X 10.7 |

Modified NSTextCheckingResult.phoneNumberCheckingResultWithRange(NSRange, phoneNumber: String) -> NSTextCheckingResult [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func phoneNumberCheckingResultWithRange(_ range: NSRange, phoneNumber phoneNumber: String!) -> NSTextCheckingResult! ``` | OS X 10.10 |
| To | ``` class func phoneNumberCheckingResultWithRange(_ range: NSRange, phoneNumber phoneNumber: String) -> NSTextCheckingResult ``` | OS X 10.7 |

Modified NSTextCheckingResult.quoteCheckingResultWithRange(NSRange, replacementString: String) -> NSTextCheckingResult [class]

|  | Declaration |
| --- | --- |
| From | ``` class func quoteCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String!) -> NSTextCheckingResult! ``` |
| To | ``` class func quoteCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String) -> NSTextCheckingResult ``` |

Modified NSTextCheckingResult.rangeAtIndex(Int) -> NSRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSTextCheckingResult.regularExpression

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var regularExpression: NSRegularExpression! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var regularExpression: NSRegularExpression? { get } ``` | OS X 10.7 |

Modified NSTextCheckingResult.regularExpressionCheckingResultWithRanges(NSRangePointer, count: Int, regularExpression: NSRegularExpression) -> NSTextCheckingResult [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func regularExpressionCheckingResultWithRanges(_ ranges: NSRangePointer, count count: Int, regularExpression regularExpression: NSRegularExpression!) -> NSTextCheckingResult! ``` | OS X 10.10 |
| To | ``` class func regularExpressionCheckingResultWithRanges(_ ranges: NSRangePointer, count count: Int, regularExpression regularExpression: NSRegularExpression) -> NSTextCheckingResult ``` | OS X 10.7 |

Modified NSTextCheckingResult.replacementCheckingResultWithRange(NSRange, replacementString: String) -> NSTextCheckingResult [class]

|  | Declaration |
| --- | --- |
| From | ``` class func replacementCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String!) -> NSTextCheckingResult! ``` |
| To | ``` class func replacementCheckingResultWithRange(_ range: NSRange, replacementString replacementString: String) -> NSTextCheckingResult ``` |

Modified NSTextCheckingResult.replacementString

|  | Declaration |
| --- | --- |
| From | ``` var replacementString: String! { get } ``` |
| To | ``` var replacementString: String? { get } ``` |

Modified NSTextCheckingResult.resultByAdjustingRangesWithOffset(Int) -> NSTextCheckingResult

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func resultByAdjustingRangesWithOffset(_ offset: Int) -> NSTextCheckingResult! ``` | OS X 10.10 |
| To | ``` func resultByAdjustingRangesWithOffset(_ offset: Int) -> NSTextCheckingResult ``` | OS X 10.7 |

Modified NSTextCheckingResult.spellCheckingResultWithRange(NSRange) -> NSTextCheckingResult [class]

|  | Declaration |
| --- | --- |
| From | ``` class func spellCheckingResultWithRange(_ range: NSRange) -> NSTextCheckingResult! ``` |
| To | ``` class func spellCheckingResultWithRange(_ range: NSRange) -> NSTextCheckingResult ``` |

Modified NSTextCheckingResult.timeZone

|  | Declaration |
| --- | --- |
| From | ``` var timeZone: NSTimeZone! { get } ``` |
| To | ``` @NSCopying var timeZone: NSTimeZone? { get } ``` |

Modified NSTextCheckingResult.transitInformationCheckingResultWithRange(NSRange, components:[NSObject: AnyObject]) -> NSTextCheckingResult [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func transitInformationCheckingResultWithRange(_ range: NSRange, components components: [NSObject : AnyObject]!) -> NSTextCheckingResult! ``` | OS X 10.10 |
| To | ``` class func transitInformationCheckingResultWithRange(_ range: NSRange, components components: [NSObject : AnyObject]) -> NSTextCheckingResult ``` | OS X 10.7 |

Modified NSTextCheckingType [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSTextCheckingType : RawOptionSet {     init(_ value: UInt64)     var value: UInt64     static var Orthography: NSTextCheckingType { get }     static var Spelling: NSTextCheckingType { get }     static var Grammar: NSTextCheckingType { get }     static var Date: NSTextCheckingType { get }     static var Address: NSTextCheckingType { get }     static var Link: NSTextCheckingType { get }     static var Quote: NSTextCheckingType { get }     static var Dash: NSTextCheckingType { get }     static var Replacement: NSTextCheckingType { get }     static var Correction: NSTextCheckingType { get }     static var RegularExpression: NSTextCheckingType { get }     static var PhoneNumber: NSTextCheckingType { get }     static var TransitInformation: NSTextCheckingType { get } } ``` | RawOptionSet |
| To | ``` struct NSTextCheckingType : RawOptionSetType {     init(_ rawValue: UInt64)     init(rawValue rawValue: UInt64)     static var Orthography: NSTextCheckingType { get }     static var Spelling: NSTextCheckingType { get }     static var Grammar: NSTextCheckingType { get }     static var Date: NSTextCheckingType { get }     static var Address: NSTextCheckingType { get }     static var Link: NSTextCheckingType { get }     static var Quote: NSTextCheckingType { get }     static var Dash: NSTextCheckingType { get }     static var Replacement: NSTextCheckingType { get }     static var Correction: NSTextCheckingType { get }     static var RegularExpression: NSTextCheckingType { get }     static var PhoneNumber: NSTextCheckingType { get }     static var TransitInformation: NSTextCheckingType { get } } ``` | RawOptionSetType |

Modified NSTextCheckingType.PhoneNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSTextCheckingType.RegularExpression

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSTextCheckingType.TransitInformation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSTextCheckingType.init(_: UInt64)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt64) ``` |
| To | ``` init(_ rawValue: UInt64) ``` |

Modified NSThread.init()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSThread.callStackReturnAddresses() -> [AnyObject] [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func callStackReturnAddresses() -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` class func callStackReturnAddresses() -> [AnyObject] ``` | OS X 10.5 |

Modified NSThread.callStackSymbols() -> [AnyObject] [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func callStackSymbols() -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` class func callStackSymbols() -> [AnyObject] ``` | OS X 10.6 |

Modified NSThread.cancel()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSThread.cancelled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSThread.currentThread() -> NSThread [class]

|  | Declaration |
| --- | --- |
| From | ``` class func currentThread() -> NSThread! ``` |
| To | ``` class func currentThread() -> NSThread ``` |

Modified NSThread.detachNewThreadSelector(Selector, toTarget: AnyObject, withObject: AnyObject?) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func detachNewThreadSelector(_ selector: Selector, toTarget target: AnyObject!, withObject argument: AnyObject!) ``` |
| To | ``` class func detachNewThreadSelector(_ selector: Selector, toTarget target: AnyObject, withObject argument: AnyObject?) ``` |

Modified NSThread.executing

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSThread.finished

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSThread.isMainThread

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSThread.isMainThread() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSThread.main()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSThread.mainThread() -> NSThread [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func mainThread() -> NSThread! ``` | OS X 10.10 |
| To | ``` class func mainThread() -> NSThread ``` | OS X 10.5 |

Modified NSThread.name

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSThread.sleepUntilDate(NSDate) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func sleepUntilDate(_ date: NSDate!) ``` |
| To | ``` class func sleepUntilDate(_ date: NSDate) ``` |

Modified NSThread.stackSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSThread.start()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSThread.init(target: AnyObject, selector: Selector, object: AnyObject?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(target target: AnyObject!, selector selector: Selector, object argument: AnyObject!) ``` | OS X 10.10 |
| To | ``` convenience init(target target: AnyObject, selector selector: Selector, object argument: AnyObject?) ``` | OS X 10.5 |

Modified NSThread.threadDictionary

|  | Declaration |
| --- | --- |
| From | ``` var threadDictionary: NSMutableDictionary! { get } ``` |
| To | ``` var threadDictionary: NSMutableDictionary { get } ``` |

Modified NSThread.threadPriority

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSTimeZone.abbreviation

|  | Declaration |
| --- | --- |
| From | ``` var abbreviation: String! { get } ``` |
| To | ``` var abbreviation: String? { get } ``` |

Modified NSTimeZone.init(abbreviation: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(abbreviation abbreviation: String!) ``` |
| To | ``` convenience init?(abbreviation abbreviation: String) ``` |

Modified NSTimeZone.abbreviationDictionary() -> [NSObject: AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func abbreviationDictionary() -> [NSObject : AnyObject]! ``` |
| To | ``` class func abbreviationDictionary() -> [NSObject : AnyObject] ``` |

Modified NSTimeZone.abbreviationForDate(NSDate) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func abbreviationForDate(_ aDate: NSDate!) -> String! ``` |
| To | ``` func abbreviationForDate(_ aDate: NSDate) -> String? ``` |

Modified NSTimeZone.data

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData! { get } ``` |
| To | ``` @NSCopying var data: NSData { get } ``` |

Modified NSTimeZone.daylightSavingTimeOffset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSTimeZone.daylightSavingTimeOffsetForDate(NSDate) -> NSTimeInterval

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func daylightSavingTimeOffsetForDate(_ aDate: NSDate!) -> NSTimeInterval ``` | OS X 10.10 |
| To | ``` func daylightSavingTimeOffsetForDate(_ aDate: NSDate) -> NSTimeInterval ``` | OS X 10.5 |

Modified NSTimeZone.defaultTimeZone() -> NSTimeZone [class]

|  | Declaration |
| --- | --- |
| From | ``` class func defaultTimeZone() -> NSTimeZone! ``` |
| To | ``` class func defaultTimeZone() -> NSTimeZone ``` |

Modified NSTimeZone.description

|  | Declaration |
| --- | --- |
| From | ``` var description: String! { get } ``` |
| To | ``` var description: String { get } ``` |

Modified NSTimeZone.isDaylightSavingTimeForDate(NSDate) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isDaylightSavingTimeForDate(_ aDate: NSDate!) -> Bool ``` |
| To | ``` func isDaylightSavingTimeForDate(_ aDate: NSDate) -> Bool ``` |

Modified NSTimeZone.isEqualToTimeZone(NSTimeZone) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToTimeZone(_ aTimeZone: NSTimeZone!) -> Bool ``` |
| To | ``` func isEqualToTimeZone(_ aTimeZone: NSTimeZone) -> Bool ``` |

Modified NSTimeZone.knownTimeZoneNames() -> [AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func knownTimeZoneNames() -> [AnyObject]! ``` |
| To | ``` class func knownTimeZoneNames() -> [AnyObject] ``` |

Modified NSTimeZone.localTimeZone() -> NSTimeZone [class]

|  | Declaration |
| --- | --- |
| From | ``` class func localTimeZone() -> NSTimeZone! ``` |
| To | ``` class func localTimeZone() -> NSTimeZone ``` |

Modified NSTimeZone.localizedName(NSTimeZoneNameStyle, locale: NSLocale?) -> String?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func localizedName(_ style: NSTimeZoneNameStyle, locale locale: NSLocale!) -> String! ``` | OS X 10.10 |
| To | ``` func localizedName(_ style: NSTimeZoneNameStyle, locale locale: NSLocale?) -> String? ``` | OS X 10.5 |

Modified NSTimeZone.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified NSTimeZone.nextDaylightSavingTimeTransition

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var nextDaylightSavingTimeTransition: NSDate! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var nextDaylightSavingTimeTransition: NSDate? { get } ``` | OS X 10.5 |

Modified NSTimeZone.nextDaylightSavingTimeTransitionAfterDate(NSDate) -> NSDate?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func nextDaylightSavingTimeTransitionAfterDate(_ aDate: NSDate!) -> NSDate! ``` | OS X 10.10 |
| To | ``` func nextDaylightSavingTimeTransitionAfterDate(_ aDate: NSDate) -> NSDate? ``` | OS X 10.5 |

Modified NSTimeZone.secondsFromGMTForDate(NSDate) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func secondsFromGMTForDate(_ aDate: NSDate!) -> Int ``` |
| To | ``` func secondsFromGMTForDate(_ aDate: NSDate) -> Int ``` |

Modified NSTimeZone.setAbbreviationDictionary([NSObject: AnyObject]) [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func setAbbreviationDictionary(_ dict: [NSObject : AnyObject]!) ``` | OS X 10.10 |
| To | ``` class func setAbbreviationDictionary(_ dict: [NSObject : AnyObject]) ``` | OS X 10.6 |

Modified NSTimeZone.setDefaultTimeZone(NSTimeZone) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setDefaultTimeZone(_ aTimeZone: NSTimeZone!) ``` |
| To | ``` class func setDefaultTimeZone(_ aTimeZone: NSTimeZone) ``` |

Modified NSTimeZone.systemTimeZone() -> NSTimeZone [class]

|  | Declaration |
| --- | --- |
| From | ``` class func systemTimeZone() -> NSTimeZone! ``` |
| To | ``` class func systemTimeZone() -> NSTimeZone ``` |

Modified NSTimeZone.timeZoneDataVersion() -> String [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func timeZoneDataVersion() -> String! ``` | OS X 10.10 |
| To | ``` class func timeZoneDataVersion() -> String ``` | OS X 10.6 |

Modified NSTimer.fireDate

|  | Declaration |
| --- | --- |
| From | ``` var fireDate: NSDate! ``` |
| To | ``` @NSCopying var fireDate: NSDate ``` |

Modified NSTimer.init(fireDate: NSDate, interval: NSTimeInterval, target: AnyObject, selector: Selector, userInfo: AnyObject?, repeats: Bool)

|  | Declaration |
| --- | --- |
| From | ``` init(fireDate date: NSDate!, interval ti: NSTimeInterval, target t: AnyObject!, selector s: Selector, userInfo ui: AnyObject!, repeats rep: Bool) ``` |
| To | ``` init(fireDate date: NSDate, interval ti: NSTimeInterval, target t: AnyObject, selector s: Selector, userInfo ui: AnyObject?, repeats rep: Bool) ``` |

Modified NSTimer.scheduledTimerWithTimeInterval(NSTimeInterval, invocation: NSInvocation, repeats: Bool) -> NSTimer [class]

|  | Declaration |
| --- | --- |
| From | ``` class func scheduledTimerWithTimeInterval(_ ti: NSTimeInterval, invocation invocation: NSInvocation!, repeats yesOrNo: Bool) -> NSTimer! ``` |
| To | ``` class func scheduledTimerWithTimeInterval(_ ti: NSTimeInterval, invocation invocation: NSInvocation, repeats yesOrNo: Bool) -> NSTimer ``` |

Modified NSTimer.scheduledTimerWithTimeInterval(NSTimeInterval, target: AnyObject, selector: Selector, userInfo: AnyObject?, repeats: Bool) -> NSTimer [class]

|  | Declaration |
| --- | --- |
| From | ``` class func scheduledTimerWithTimeInterval(_ ti: NSTimeInterval, target aTarget: AnyObject!, selector aSelector: Selector, userInfo userInfo: AnyObject!, repeats yesOrNo: Bool) -> NSTimer! ``` |
| To | ``` class func scheduledTimerWithTimeInterval(_ ti: NSTimeInterval, target aTarget: AnyObject, selector aSelector: Selector, userInfo userInfo: AnyObject?, repeats yesOrNo: Bool) -> NSTimer ``` |

Modified NSTimer.init(timeInterval: NSTimeInterval, invocation: NSInvocation, repeats: Bool)

|  | Declaration |
| --- | --- |
| From | ``` init(timeInterval ti: NSTimeInterval, invocation invocation: NSInvocation!, repeats yesOrNo: Bool) -> NSTimer ``` |
| To | ``` init(timeInterval ti: NSTimeInterval, invocation invocation: NSInvocation, repeats yesOrNo: Bool) -> NSTimer ``` |

Modified NSTimer.init(timeInterval: NSTimeInterval, target: AnyObject, selector: Selector, userInfo: AnyObject?, repeats: Bool)

|  | Declaration |
| --- | --- |
| From | ``` init(timeInterval ti: NSTimeInterval, target aTarget: AnyObject!, selector aSelector: Selector, userInfo userInfo: AnyObject!, repeats yesOrNo: Bool) -> NSTimer ``` |
| To | ``` init(timeInterval ti: NSTimeInterval, target aTarget: AnyObject, selector aSelector: Selector, userInfo userInfo: AnyObject?, repeats yesOrNo: Bool) -> NSTimer ``` |

Modified NSTimer.tolerance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSTimer.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: AnyObject! { get } ``` |
| To | ``` var userInfo: AnyObject? { get } ``` |

Modified NSURL

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSSecureCoding, NSURLHandleClient, Reflectable |
| To | AnyObject, NSCoding, NSCopying, NSObjectProtocol, NSPasteboardReading, NSPasteboardWriting, NSSecureCoding, NSURLHandleClient, QLPreviewItem, Reflectable |

Modified NSURL.URLByAppendingPathComponent(String) -> NSURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URLByAppendingPathComponent(_ pathComponent: String!) -> NSURL! ``` | OS X 10.10 |
| To | ``` func URLByAppendingPathComponent(_ pathComponent: String) -> NSURL ``` | OS X 10.6 |

Modified NSURL.URLByAppendingPathComponent(String, isDirectory: Bool) -> NSURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URLByAppendingPathComponent(_ pathComponent: String!, isDirectory isDirectory: Bool) -> NSURL! ``` | OS X 10.10 |
| To | ``` func URLByAppendingPathComponent(_ pathComponent: String, isDirectory isDirectory: Bool) -> NSURL ``` | OS X 10.7 |

Modified NSURL.URLByAppendingPathExtension(String) -> NSURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URLByAppendingPathExtension(_ pathExtension: String!) -> NSURL! ``` | OS X 10.10 |
| To | ``` func URLByAppendingPathExtension(_ pathExtension: String) -> NSURL ``` | OS X 10.6 |

Modified NSURL.URLByDeletingLastPathComponent

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var URLByDeletingLastPathComponent: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var URLByDeletingLastPathComponent: NSURL? { get } ``` | OS X 10.6 |

Modified NSURL.URLByDeletingPathExtension

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var URLByDeletingPathExtension: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var URLByDeletingPathExtension: NSURL? { get } ``` | OS X 10.6 |

Modified NSURL.URLByResolvingSymlinksInPath

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var URLByResolvingSymlinksInPath: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var URLByResolvingSymlinksInPath: NSURL? { get } ``` | OS X 10.6 |

Modified NSURL.URLByStandardizingPath

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var URLByStandardizingPath: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var URLByStandardizingPath: NSURL? { get } ``` | OS X 10.6 |

Modified NSURL.absoluteString

|  | Declaration |
| --- | --- |
| From | ``` var absoluteString: String! { get } ``` |
| To | ``` var absoluteString: String? { get } ``` |

Modified NSURL.absoluteURL

|  | Declaration |
| --- | --- |
| From | ``` var absoluteURL: NSURL! { get } ``` |
| To | ``` @NSCopying var absoluteURL: NSURL? { get } ``` |

Modified NSURL.baseURL

|  | Declaration |
| --- | --- |
| From | ``` var baseURL: NSURL! { get } ``` |
| To | ``` @NSCopying var baseURL: NSURL? { get } ``` |

Modified NSURL.bookmarkDataWithContentsOfURL(NSURL, error: NSErrorPointer) -> NSData? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func bookmarkDataWithContentsOfURL(_ bookmarkFileURL: NSURL!, error error: NSErrorPointer) -> NSData! ``` | OS X 10.10 |
| To | ``` class func bookmarkDataWithContentsOfURL(_ bookmarkFileURL: NSURL, error error: NSErrorPointer) -> NSData? ``` | OS X 10.6 |

Modified NSURL.bookmarkDataWithOptions(NSURLBookmarkCreationOptions, includingResourceValuesForKeys:[AnyObject]?, relativeToURL: NSURL?, error: NSErrorPointer) -> NSData?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func bookmarkDataWithOptions(_ options: NSURLBookmarkCreationOptions, includingResourceValuesForKeys keys: [AnyObject]!, relativeToURL relativeURL: NSURL!, error error: NSErrorPointer) -> NSData! ``` | OS X 10.10 |
| To | ``` func bookmarkDataWithOptions(_ options: NSURLBookmarkCreationOptions, includingResourceValuesForKeys keys: [AnyObject]?, relativeToURL relativeURL: NSURL?, error error: NSErrorPointer) -> NSData? ``` | OS X 10.6 |

Modified NSURL.init(byResolvingAliasFileAtURL: NSURL, options: NSURLBookmarkResolutionOptions, error: NSErrorPointer)

|  | Name | Declaration |
| --- | --- | --- |
| From | URLByResolvingAliasFileAtURL(_:options:error:) | ``` class func URLByResolvingAliasFileAtURL(_ url: NSURL!, options options: NSURLBookmarkResolutionOptions, error error: NSErrorPointer) -> Self! ``` |
| To | init(byResolvingAliasFileAtURL:options:error:) | ``` convenience init?(byResolvingAliasFileAtURL url: NSURL, options options: NSURLBookmarkResolutionOptions, error error: NSErrorPointer) ``` |

Modified NSURL.init(byResolvingBookmarkData: NSData, options: NSURLBookmarkResolutionOptions, relativeToURL: NSURL?, bookmarkDataIsStale: UnsafeMutablePointer<ObjCBool>, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(byResolvingBookmarkData bookmarkData: NSData!, options options: NSURLBookmarkResolutionOptions, relativeToURL relativeURL: NSURL!, bookmarkDataIsStale isStale: UnsafePointer<ObjCBool>, error error: NSErrorPointer) ``` | OS X 10.10 |
| To | ``` convenience init?(byResolvingBookmarkData bookmarkData: NSData, options options: NSURLBookmarkResolutionOptions, relativeToURL relativeURL: NSURL?, bookmarkDataIsStale isStale: UnsafeMutablePointer<ObjCBool>, error error: NSErrorPointer) ``` | OS X 10.6 |

Modified NSURL.checkResourceIsReachableAndReturnError(NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSURL.filePathURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var filePathURL: NSURL! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var filePathURL: NSURL? { get } ``` | OS X 10.6 |

Modified NSURL.fileReferenceURL() -> NSURL?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func fileReferenceURL() -> NSURL! ``` | OS X 10.10 |
| To | ``` func fileReferenceURL() -> NSURL? ``` | OS X 10.6 |

Modified NSURL.fileSystemRepresentation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var fileSystemRepresentation: ConstUnsafePointer<Int8> { get } ``` | OS X 10.10 |
| To | ``` var fileSystemRepresentation: UnsafePointer<Int8> { get } ``` | OS X 10.9 |

Modified NSURL.init(fileURLWithFileSystemRepresentation: UnsafePointer<Int8>, isDirectory: Bool, relativeToURL: NSURL?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(fileURLWithFileSystemRepresentation path: ConstUnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL!) ``` | OS X 10.10 |
| To | ``` init?(fileURLWithFileSystemRepresentation path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) ``` | OS X 10.9 |

Modified NSURL.fileURLWithFileSystemRepresentation(UnsafePointer<Int8>, isDirectory: Bool, relativeToURL: NSURL?) -> NSURL? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func fileURLWithFileSystemRepresentation(_ path: ConstUnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL!) -> NSURL! ``` | OS X 10.10 |
| To | ``` class func fileURLWithFileSystemRepresentation(_ path: UnsafePointer<Int8>, isDirectory isDir: Bool, relativeToURL baseURL: NSURL?) -> NSURL? ``` | OS X 10.9 |

Modified NSURL.init(fileURLWithPath: String)

|  | Declaration |
| --- | --- |
| From | ``` init(fileURLWithPath path: String!) ``` |
| To | ``` init?(fileURLWithPath path: String) ``` |

Modified NSURL.fileURLWithPath(String) -> NSURL? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fileURLWithPath(_ path: String!) -> NSURL! ``` |
| To | ``` class func fileURLWithPath(_ path: String) -> NSURL? ``` |

Modified NSURL.init(fileURLWithPath: String, isDirectory: Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(fileURLWithPath path: String!, isDirectory isDir: Bool) ``` | OS X 10.10 |
| To | ``` init?(fileURLWithPath path: String, isDirectory isDir: Bool) ``` | OS X 10.5 |

Modified NSURL.fileURLWithPath(String, isDirectory: Bool) -> NSURL? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func fileURLWithPath(_ path: String!, isDirectory isDir: Bool) -> NSURL! ``` | OS X 10.10 |
| To | ``` class func fileURLWithPath(_ path: String, isDirectory isDir: Bool) -> NSURL? ``` | OS X 10.5 |

Modified NSURL.fileURLWithPathComponents([AnyObject]) -> NSURL? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func fileURLWithPathComponents(_ components: [AnyObject]!) -> NSURL! ``` | OS X 10.10 |
| To | ``` class func fileURLWithPathComponents(_ components: [AnyObject]) -> NSURL? ``` | OS X 10.6 |

Modified NSURL.fragment

|  | Declaration |
| --- | --- |
| From | ``` var fragment: String! { get } ``` |
| To | ``` var fragment: String? { get } ``` |

Modified NSURL.getFileSystemRepresentation(UnsafeMutablePointer<Int8>, maxLength: Int) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getFileSystemRepresentation(_ buffer: UnsafePointer<Int8>, maxLength maxBufferLength: Int) -> Bool ``` | OS X 10.10 |
| To | ``` func getFileSystemRepresentation(_ buffer: UnsafeMutablePointer<Int8>, maxLength maxBufferLength: Int) -> Bool ``` | OS X 10.9 |

Modified NSURL.getPromisedItemResourceValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getPromisedItemResourceValue(_ value: AutoreleasingUnsafePointer<AnyObject?>, forKey key: String!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func getPromisedItemResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String, error error: NSErrorPointer) -> Bool ``` |

Modified NSURL.getResourceValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getResourceValue(_ value: AutoreleasingUnsafePointer<AnyObject?>, forKey key: String!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func getResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String, error error: NSErrorPointer) -> Bool ``` | OS X 10.6 |

Modified NSURL.host

|  | Declaration |
| --- | --- |
| From | ``` var host: String! { get } ``` |
| To | ``` var host: String? { get } ``` |

Modified NSURL.isFileReferenceURL() -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSURL.lastPathComponent

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var lastPathComponent: String! { get } ``` | OS X 10.10 |
| To | ``` var lastPathComponent: String? { get } ``` | OS X 10.6 |

Modified NSURL.parameterString

|  | Declaration |
| --- | --- |
| From | ``` var parameterString: String! { get } ``` |
| To | ``` var parameterString: String? { get } ``` |

Modified NSURL.password

|  | Declaration |
| --- | --- |
| From | ``` var password: String! { get } ``` |
| To | ``` var password: String? { get } ``` |

Modified NSURL.path

|  | Declaration |
| --- | --- |
| From | ``` var path: String! { get } ``` |
| To | ``` var path: String? { get } ``` |

Modified NSURL.pathComponents

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var pathComponents: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var pathComponents: [AnyObject]? { get } ``` | OS X 10.6 |

Modified NSURL.pathExtension

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var pathExtension: String! { get } ``` | OS X 10.10 |
| To | ``` var pathExtension: String? { get } ``` | OS X 10.6 |

Modified NSURL.port

|  | Declaration |
| --- | --- |
| From | ``` var port: NSNumber! { get } ``` |
| To | ``` @NSCopying var port: NSNumber? { get } ``` |

Modified NSURL.promisedItemResourceValuesForKeys([AnyObject], error: NSErrorPointer) -> [NSObject: AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func promisedItemResourceValuesForKeys(_ keys: [AnyObject]!, error error: NSErrorPointer) -> [NSObject : AnyObject]! ``` |
| To | ``` func promisedItemResourceValuesForKeys(_ keys: [AnyObject], error error: NSErrorPointer) -> [NSObject : AnyObject]? ``` |

Modified NSURL.query

|  | Declaration |
| --- | --- |
| From | ``` var query: String! { get } ``` |
| To | ``` var query: String? { get } ``` |

Modified NSURL.relativePath

|  | Declaration |
| --- | --- |
| From | ``` var relativePath: String! { get } ``` |
| To | ``` var relativePath: String? { get } ``` |

Modified NSURL.relativeString

|  | Declaration |
| --- | --- |
| From | ``` var relativeString: String! { get } ``` |
| To | ``` var relativeString: String? { get } ``` |

Modified NSURL.removeAllCachedResourceValues()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSURL.removeCachedResourceValueForKey(String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func removeCachedResourceValueForKey(_ key: String!) ``` | OS X 10.10 |
| To | ``` func removeCachedResourceValueForKey(_ key: String) ``` | OS X 10.9 |

Modified NSURL.resourceSpecifier

|  | Declaration |
| --- | --- |
| From | ``` var resourceSpecifier: String! { get } ``` |
| To | ``` var resourceSpecifier: String? { get } ``` |

Modified NSURL.resourceValuesForKeys([AnyObject], error: NSErrorPointer) -> [NSObject: AnyObject]?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func resourceValuesForKeys(_ keys: [AnyObject]!, error error: NSErrorPointer) -> [NSObject : AnyObject]! ``` | OS X 10.10 |
| To | ``` func resourceValuesForKeys(_ keys: [AnyObject], error error: NSErrorPointer) -> [NSObject : AnyObject]? ``` | OS X 10.6 |

Modified NSURL.resourceValuesForKeys([AnyObject], fromBookmarkData: NSData) -> [NSObject: AnyObject]? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func resourceValuesForKeys(_ keys: [AnyObject]!, fromBookmarkData bookmarkData: NSData!) -> [NSObject : AnyObject]! ``` | OS X 10.10 |
| To | ``` class func resourceValuesForKeys(_ keys: [AnyObject], fromBookmarkData bookmarkData: NSData) -> [NSObject : AnyObject]? ``` | OS X 10.6 |

Modified NSURL.scheme

|  | Declaration |
| --- | --- |
| From | ``` var scheme: String! { get } ``` |
| To | ``` var scheme: String? { get } ``` |

Modified NSURL.init(scheme: String, host: String?, path: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(scheme scheme: String!, host host: String!, path path: String!) ``` |
| To | ``` convenience init?(scheme scheme: String, host host: String?, path path: String) ``` |

Modified NSURL.setResourceValue(AnyObject?, forKey: String, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setResourceValue(_ value: AnyObject!, forKey key: String!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func setResourceValue(_ value: AnyObject?, forKey key: String, error error: NSErrorPointer) -> Bool ``` | OS X 10.6 |

Modified NSURL.setResourceValues([NSObject: AnyObject], error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setResourceValues(_ keyedValues: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func setResourceValues(_ keyedValues: [NSObject : AnyObject], error error: NSErrorPointer) -> Bool ``` | OS X 10.6 |

Modified NSURL.setTemporaryResourceValue(AnyObject?, forKey: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setTemporaryResourceValue(_ value: AnyObject!, forKey key: String!) ``` | OS X 10.10 |
| To | ``` func setTemporaryResourceValue(_ value: AnyObject?, forKey key: String) ``` | OS X 10.9 |

Modified NSURL.standardizedURL

|  | Declaration |
| --- | --- |
| From | ``` var standardizedURL: NSURL! { get } ``` |
| To | ``` @NSCopying var standardizedURL: NSURL? { get } ``` |

Modified NSURL.startAccessingSecurityScopedResource() -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSURL.stopAccessingSecurityScopedResource()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSURL.init(string: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(string URLString: String!) ``` |
| To | ``` convenience init?(string URLString: String) ``` |

Modified NSURL.init(string: String, relativeToURL: NSURL?)

|  | Declaration |
| --- | --- |
| From | ``` init(string URLString: String!, relativeToURL baseURL: NSURL!) ``` |
| To | ``` init?(string URLString: String, relativeToURL baseURL: NSURL?) ``` |

Modified NSURL.user

|  | Declaration |
| --- | --- |
| From | ``` var user: String! { get } ``` |
| To | ``` var user: String? { get } ``` |

Modified NSURL.writeBookmarkData(NSData, toURL: NSURL, options: NSURLBookmarkFileCreationOptions, error: NSErrorPointer) -> Bool [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func writeBookmarkData(_ bookmarkData: NSData!, toURL bookmarkFileURL: NSURL!, options options: NSURLBookmarkFileCreationOptions, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` class func writeBookmarkData(_ bookmarkData: NSData, toURL bookmarkFileURL: NSURL, options options: NSURLBookmarkFileCreationOptions, error error: NSErrorPointer) -> Bool ``` | OS X 10.6 |

Modified NSURLAuthenticationChallenge.init(authenticationChallenge: NSURLAuthenticationChallenge, sender: NSURLAuthenticationChallengeSender)

|  | Declaration |
| --- | --- |
| From | ``` init(authenticationChallenge challenge: NSURLAuthenticationChallenge!, sender sender: NSURLAuthenticationChallengeSender!) ``` |
| To | ``` init(authenticationChallenge challenge: NSURLAuthenticationChallenge, sender sender: NSURLAuthenticationChallengeSender) ``` |

Modified NSURLAuthenticationChallenge.error

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError! { get } ``` |
| To | ``` @NSCopying var error: NSError? { get } ``` |

Modified NSURLAuthenticationChallenge.failureResponse

|  | Declaration |
| --- | --- |
| From | ``` var failureResponse: NSURLResponse! { get } ``` |
| To | ``` @NSCopying var failureResponse: NSURLResponse? { get } ``` |

Modified NSURLAuthenticationChallenge.proposedCredential

|  | Declaration |
| --- | --- |
| From | ``` var proposedCredential: NSURLCredential! { get } ``` |
| To | ``` @NSCopying var proposedCredential: NSURLCredential? { get } ``` |

Modified NSURLAuthenticationChallenge.protectionSpace

|  | Declaration |
| --- | --- |
| From | ``` var protectionSpace: NSURLProtectionSpace! { get } ``` |
| To | ``` @NSCopying var protectionSpace: NSURLProtectionSpace { get } ``` |

Modified NSURLAuthenticationChallenge.init(protectionSpace: NSURLProtectionSpace, proposedCredential: NSURLCredential?, previousFailureCount: Int, failureResponse: NSURLResponse?, error: NSError?, sender: NSURLAuthenticationChallengeSender)

|  | Declaration |
| --- | --- |
| From | ``` init(protectionSpace space: NSURLProtectionSpace!, proposedCredential credential: NSURLCredential!, previousFailureCount previousFailureCount: Int, failureResponse response: NSURLResponse!, error error: NSError!, sender sender: NSURLAuthenticationChallengeSender!) ``` |
| To | ``` init(protectionSpace space: NSURLProtectionSpace, proposedCredential credential: NSURLCredential?, previousFailureCount previousFailureCount: Int, failureResponse response: NSURLResponse?, error error: NSError?, sender sender: NSURLAuthenticationChallengeSender) ``` |

Modified NSURLAuthenticationChallenge.sender

|  | Declaration |
| --- | --- |
| From | ``` var sender: NSURLAuthenticationChallengeSender! { get } ``` |
| To | ``` var sender: NSURLAuthenticationChallengeSender { get } ``` |

Modified NSURLAuthenticationChallengeSender.cancelAuthenticationChallenge(NSURLAuthenticationChallenge)

|  | Declaration |
| --- | --- |
| From | ``` func cancelAuthenticationChallenge(_ challenge: NSURLAuthenticationChallenge!) ``` |
| To | ``` func cancelAuthenticationChallenge(_ challenge: NSURLAuthenticationChallenge) ``` |

Modified NSURLAuthenticationChallengeSender.continueWithoutCredentialForAuthenticationChallenge(NSURLAuthenticationChallenge)

|  | Declaration |
| --- | --- |
| From | ``` func continueWithoutCredentialForAuthenticationChallenge(_ challenge: NSURLAuthenticationChallenge!) ``` |
| To | ``` func continueWithoutCredentialForAuthenticationChallenge(_ challenge: NSURLAuthenticationChallenge) ``` |

Modified NSURLAuthenticationChallengeSender.performDefaultHandlingForAuthenticationChallenge(NSURLAuthenticationChallenge)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func performDefaultHandlingForAuthenticationChallenge(_ challenge: NSURLAuthenticationChallenge!) ``` | -- |
| To | ``` optional func performDefaultHandlingForAuthenticationChallenge(_ challenge: NSURLAuthenticationChallenge) ``` | yes |

Modified NSURLAuthenticationChallengeSender.rejectProtectionSpaceAndContinueWithChallenge(NSURLAuthenticationChallenge)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func rejectProtectionSpaceAndContinueWithChallenge(_ challenge: NSURLAuthenticationChallenge!) ``` | -- |
| To | ``` optional func rejectProtectionSpaceAndContinueWithChallenge(_ challenge: NSURLAuthenticationChallenge) ``` | yes |

Modified NSURLAuthenticationChallengeSender.useCredential(NSURLCredential, forAuthenticationChallenge: NSURLAuthenticationChallenge)

|  | Declaration |
| --- | --- |
| From | ``` func useCredential(_ credential: NSURLCredential!, forAuthenticationChallenge challenge: NSURLAuthenticationChallenge!) ``` |
| To | ``` func useCredential(_ credential: NSURLCredential, forAuthenticationChallenge challenge: NSURLAuthenticationChallenge) ``` |

Modified NSURLBookmarkCreationOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct NSURLBookmarkCreationOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var PreferFileIDResolution: NSURLBookmarkCreationOptions { get }     static var MinimalBookmark: NSURLBookmarkCreationOptions { get }     static var SuitableForBookmarkFile: NSURLBookmarkCreationOptions { get }     static var WithSecurityScope: NSURLBookmarkCreationOptions { get }     static var SecurityScopeAllowOnlyReadAccess: NSURLBookmarkCreationOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct NSURLBookmarkCreationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var PreferFileIDResolution: NSURLBookmarkCreationOptions { get }     static var MinimalBookmark: NSURLBookmarkCreationOptions { get }     static var SuitableForBookmarkFile: NSURLBookmarkCreationOptions { get }     static var WithSecurityScope: NSURLBookmarkCreationOptions { get }     static var SecurityScopeAllowOnlyReadAccess: NSURLBookmarkCreationOptions { get } } ``` | RawOptionSetType | OS X 10.6 |

Modified NSURLBookmarkCreationOptions.SecurityScopeAllowOnlyReadAccess

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSURLBookmarkCreationOptions.WithSecurityScope

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSURLBookmarkCreationOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSURLBookmarkResolutionOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct NSURLBookmarkResolutionOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var WithoutUI: NSURLBookmarkResolutionOptions { get }     static var WithoutMounting: NSURLBookmarkResolutionOptions { get }     static var WithSecurityScope: NSURLBookmarkResolutionOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct NSURLBookmarkResolutionOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var WithoutUI: NSURLBookmarkResolutionOptions { get }     static var WithoutMounting: NSURLBookmarkResolutionOptions { get }     static var WithSecurityScope: NSURLBookmarkResolutionOptions { get } } ``` | RawOptionSetType | OS X 10.6 |

Modified NSURLBookmarkResolutionOptions.WithSecurityScope

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSURLBookmarkResolutionOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSURLCache.cachedResponseForRequest(NSURLRequest) -> NSCachedURLResponse?

|  | Declaration |
| --- | --- |
| From | ``` func cachedResponseForRequest(_ request: NSURLRequest!) -> NSCachedURLResponse! ``` |
| To | ``` func cachedResponseForRequest(_ request: NSURLRequest) -> NSCachedURLResponse? ``` |

Modified NSURLCache.getCachedResponseForDataTask(NSURLSessionDataTask, completionHandler:(NSCachedURLResponse!) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func getCachedResponseForDataTask(_ dataTask: NSURLSessionDataTask!, completionHandler completionHandler: ((NSCachedURLResponse!) -> Void)!) ``` |
| To | ``` func getCachedResponseForDataTask(_ dataTask: NSURLSessionDataTask, completionHandler completionHandler: (NSCachedURLResponse!) -> Void) ``` |

Modified NSURLCache.init(memoryCapacity: Int, diskCapacity: Int, diskPath: String?)

|  | Declaration |
| --- | --- |
| From | ``` init(memoryCapacity memoryCapacity: Int, diskCapacity diskCapacity: Int, diskPath path: String!) ``` |
| To | ``` init(memoryCapacity memoryCapacity: Int, diskCapacity diskCapacity: Int, diskPath path: String?) ``` |

Modified NSURLCache.removeCachedResponseForDataTask(NSURLSessionDataTask)

|  | Declaration |
| --- | --- |
| From | ``` func removeCachedResponseForDataTask(_ dataTask: NSURLSessionDataTask!) ``` |
| To | ``` func removeCachedResponseForDataTask(_ dataTask: NSURLSessionDataTask) ``` |

Modified NSURLCache.removeCachedResponseForRequest(NSURLRequest)

|  | Declaration |
| --- | --- |
| From | ``` func removeCachedResponseForRequest(_ request: NSURLRequest!) ``` |
| To | ``` func removeCachedResponseForRequest(_ request: NSURLRequest) ``` |

Modified NSURLCache.removeCachedResponsesSinceDate(NSDate)

|  | Declaration |
| --- | --- |
| From | ``` func removeCachedResponsesSinceDate(_ date: NSDate!) ``` |
| To | ``` func removeCachedResponsesSinceDate(_ date: NSDate) ``` |

Modified NSURLCache.setSharedURLCache(NSURLCache) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setSharedURLCache(_ cache: NSURLCache!) ``` |
| To | ``` class func setSharedURLCache(_ cache: NSURLCache) ``` |

Modified NSURLCache.sharedURLCache() -> NSURLCache [class]

|  | Declaration |
| --- | --- |
| From | ``` class func sharedURLCache() -> NSURLCache! ``` |
| To | ``` class func sharedURLCache() -> NSURLCache ``` |

Modified NSURLCache.storeCachedResponse(NSCachedURLResponse, forDataTask: NSURLSessionDataTask)

|  | Declaration |
| --- | --- |
| From | ``` func storeCachedResponse(_ cachedResponse: NSCachedURLResponse!, forDataTask dataTask: NSURLSessionDataTask!) ``` |
| To | ``` func storeCachedResponse(_ cachedResponse: NSCachedURLResponse, forDataTask dataTask: NSURLSessionDataTask) ``` |

Modified NSURLCache.storeCachedResponse(NSCachedURLResponse, forRequest: NSURLRequest)

|  | Declaration |
| --- | --- |
| From | ``` func storeCachedResponse(_ cachedResponse: NSCachedURLResponse!, forRequest request: NSURLRequest!) ``` |
| To | ``` func storeCachedResponse(_ cachedResponse: NSCachedURLResponse, forRequest request: NSURLRequest) ``` |

Modified NSURLComponents

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSURLComponents.URL

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL? { get } ``` |

Modified NSURLComponents.init(URL: NSURL, resolvingAgainstBaseURL: Bool)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL!, resolvingAgainstBaseURL resolve: Bool) ``` |
| To | ``` init?(URL url: NSURL, resolvingAgainstBaseURL resolve: Bool) ``` |

Modified NSURLComponents.URLRelativeToURL(NSURL?) -> NSURL?

|  | Declaration |
| --- | --- |
| From | ``` func URLRelativeToURL(_ baseURL: NSURL!) -> NSURL! ``` |
| To | ``` func URLRelativeToURL(_ baseURL: NSURL?) -> NSURL? ``` |

Modified NSURLComponents.fragment

|  | Declaration |
| --- | --- |
| From | ``` var fragment: String! ``` |
| To | ``` var fragment: String? ``` |

Modified NSURLComponents.host

|  | Declaration |
| --- | --- |
| From | ``` var host: String! ``` |
| To | ``` var host: String? ``` |

Modified NSURLComponents.password

|  | Declaration |
| --- | --- |
| From | ``` var password: String! ``` |
| To | ``` var password: String? ``` |

Modified NSURLComponents.path

|  | Declaration |
| --- | --- |
| From | ``` var path: String! ``` |
| To | ``` var path: String? ``` |

Modified NSURLComponents.percentEncodedFragment

|  | Declaration |
| --- | --- |
| From | ``` var percentEncodedFragment: String! ``` |
| To | ``` var percentEncodedFragment: String? ``` |

Modified NSURLComponents.percentEncodedHost

|  | Declaration |
| --- | --- |
| From | ``` var percentEncodedHost: String! ``` |
| To | ``` var percentEncodedHost: String? ``` |

Modified NSURLComponents.percentEncodedPassword

|  | Declaration |
| --- | --- |
| From | ``` var percentEncodedPassword: String! ``` |
| To | ``` var percentEncodedPassword: String? ``` |

Modified NSURLComponents.percentEncodedPath

|  | Declaration |
| --- | --- |
| From | ``` var percentEncodedPath: String! ``` |
| To | ``` var percentEncodedPath: String? ``` |

Modified NSURLComponents.percentEncodedQuery

|  | Declaration |
| --- | --- |
| From | ``` var percentEncodedQuery: String! ``` |
| To | ``` var percentEncodedQuery: String? ``` |

Modified NSURLComponents.percentEncodedUser

|  | Declaration |
| --- | --- |
| From | ``` var percentEncodedUser: String! ``` |
| To | ``` var percentEncodedUser: String? ``` |

Modified NSURLComponents.port

|  | Declaration |
| --- | --- |
| From | ``` var port: NSNumber! ``` |
| To | ``` @NSCopying var port: NSNumber? ``` |

Modified NSURLComponents.query

|  | Declaration |
| --- | --- |
| From | ``` var query: String! ``` |
| To | ``` var query: String? ``` |

Modified NSURLComponents.queryItems

|  | Declaration |
| --- | --- |
| From | ``` var queryItems: [AnyObject]! ``` |
| To | ``` var queryItems: [AnyObject]? ``` |

Modified NSURLComponents.scheme

|  | Declaration |
| --- | --- |
| From | ``` var scheme: String! ``` |
| To | ``` var scheme: String? ``` |

Modified NSURLComponents.string

|  | Declaration |
| --- | --- |
| From | ``` var string: String! { get } ``` |
| To | ``` var string: String? { get } ``` |

Modified NSURLComponents.init(string: String)

|  | Declaration |
| --- | --- |
| From | ``` init(string URLString: String!) ``` |
| To | ``` init?(string URLString: String) ``` |

Modified NSURLComponents.user

|  | Declaration |
| --- | --- |
| From | ``` var user: String! ``` |
| To | ``` var user: String? ``` |

Modified NSURLConnection.canHandleRequest(NSURLRequest) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func canHandleRequest(_ request: NSURLRequest!) -> Bool ``` |
| To | ``` class func canHandleRequest(_ request: NSURLRequest) -> Bool ``` |

Modified NSURLConnection.currentRequest

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var currentRequest: NSURLRequest! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var currentRequest: NSURLRequest { get } ``` | OS X 10.8 |

Modified NSURLConnection.originalRequest

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var originalRequest: NSURLRequest! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var originalRequest: NSURLRequest { get } ``` | OS X 10.8 |

Modified NSURLConnection.init(request: NSURLRequest, delegate: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` init(request request: NSURLRequest!, delegate delegate: AnyObject!) ``` |
| To | ``` init?(request request: NSURLRequest, delegate delegate: AnyObject?) ``` |

Modified NSURLConnection.init(request: NSURLRequest, delegate: AnyObject?, startImmediately: Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(request request: NSURLRequest!, delegate delegate: AnyObject!, startImmediately startImmediately: Bool) ``` | OS X 10.10 |
| To | ``` init?(request request: NSURLRequest, delegate delegate: AnyObject?, startImmediately startImmediately: Bool) ``` | OS X 10.5 |

Modified NSURLConnection.scheduleInRunLoop(NSRunLoop, forMode: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func scheduleInRunLoop(_ aRunLoop: NSRunLoop!, forMode mode: String!) ``` | OS X 10.10 |
| To | ``` func scheduleInRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String) ``` | OS X 10.5 |

Modified NSURLConnection.sendAsynchronousRequest(NSURLRequest, queue: NSOperationQueue!, completionHandler:(NSURLResponse!, NSData!, NSError!) -> Void) [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func sendAsynchronousRequest(_ request: NSURLRequest!, queue queue: NSOperationQueue!, completionHandler handler: ((NSURLResponse!, NSData!, NSError!) -> Void)!) ``` | OS X 10.10 |
| To | ``` class func sendAsynchronousRequest(_ request: NSURLRequest, queue queue: NSOperationQueue!, completionHandler handler: (NSURLResponse!, NSData!, NSError!) -> Void) ``` | OS X 10.7 |

Modified NSURLConnection.sendSynchronousRequest(NSURLRequest, returningResponse: AutoreleasingUnsafeMutablePointer<NSURLResponse?>, error: NSErrorPointer) -> NSData? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func sendSynchronousRequest(_ request: NSURLRequest!, returningResponse response: AutoreleasingUnsafePointer<NSURLResponse?>, error error: NSErrorPointer) -> NSData! ``` |
| To | ``` class func sendSynchronousRequest(_ request: NSURLRequest, returningResponse response: AutoreleasingUnsafeMutablePointer<NSURLResponse?>, error error: NSErrorPointer) -> NSData? ``` |

Modified NSURLConnection.setDelegateQueue(NSOperationQueue!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSURLConnection.start()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSURLConnection.unscheduleFromRunLoop(NSRunLoop, forMode: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func unscheduleFromRunLoop(_ aRunLoop: NSRunLoop!, forMode mode: String!) ``` | OS X 10.10 |
| To | ``` func unscheduleFromRunLoop(_ aRunLoop: NSRunLoop, forMode mode: String) ``` | OS X 10.5 |

Modified NSURLConnectionDataDelegate.connection(NSURLConnection, didReceiveData: NSData)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func connection(_ connection: NSURLConnection!, didReceiveData data: NSData!) ``` | -- |
| To | ``` optional func connection(_ connection: NSURLConnection, didReceiveData data: NSData) ``` | yes |

Modified NSURLConnectionDataDelegate.connection(NSURLConnection, didReceiveResponse: NSURLResponse)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func connection(_ connection: NSURLConnection!, didReceiveResponse response: NSURLResponse!) ``` | -- |
| To | ``` optional func connection(_ connection: NSURLConnection, didReceiveResponse response: NSURLResponse) ``` | yes |

Modified NSURLConnectionDataDelegate.connection(NSURLConnection, didSendBodyData: Int, totalBytesWritten: Int, totalBytesExpectedToWrite: Int)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func connection(_ connection: NSURLConnection!, didSendBodyData bytesWritten: Int, totalBytesWritten totalBytesWritten: Int, totalBytesExpectedToWrite totalBytesExpectedToWrite: Int) ``` | -- |
| To | ``` optional func connection(_ connection: NSURLConnection, didSendBodyData bytesWritten: Int, totalBytesWritten totalBytesWritten: Int, totalBytesExpectedToWrite totalBytesExpectedToWrite: Int) ``` | yes |

Modified NSURLConnectionDataDelegate.connection(NSURLConnection, needNewBodyStream: NSURLRequest) -> NSInputStream?

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func connection(_ connection: NSURLConnection!, needNewBodyStream request: NSURLRequest!) -> NSInputStream! ``` | -- |
| To | ``` optional func connection(_ connection: NSURLConnection, needNewBodyStream request: NSURLRequest) -> NSInputStream? ``` | yes |

Modified NSURLConnectionDataDelegate.connection(NSURLConnection, willCacheResponse: NSCachedURLResponse) -> NSCachedURLResponse?

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func connection(_ connection: NSURLConnection!, willCacheResponse cachedResponse: NSCachedURLResponse!) -> NSCachedURLResponse! ``` | -- |
| To | ``` optional func connection(_ connection: NSURLConnection, willCacheResponse cachedResponse: NSCachedURLResponse) -> NSCachedURLResponse? ``` | yes |

Modified NSURLConnectionDataDelegate.connection(NSURLConnection, willSendRequest: NSURLRequest, redirectResponse: NSURLResponse?) -> NSURLRequest?

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func connection(_ connection: NSURLConnection!, willSendRequest request: NSURLRequest!, redirectResponse response: NSURLResponse!) -> NSURLRequest! ``` | -- |
| To | ``` optional func connection(_ connection: NSURLConnection, willSendRequest request: NSURLRequest, redirectResponse response: NSURLResponse?) -> NSURLRequest? ``` | yes |

Modified NSURLConnectionDataDelegate.connectionDidFinishLoading(NSURLConnection)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func connectionDidFinishLoading(_ connection: NSURLConnection!) ``` | -- |
| To | ``` optional func connectionDidFinishLoading(_ connection: NSURLConnection) ``` | yes |

Modified NSURLConnectionDelegate.connection(NSURLConnection, canAuthenticateAgainstProtectionSpace: NSURLProtectionSpace) -> Bool

|  | Declaration | Introduction | Deprecation | Optional |
| --- | --- | --- | --- | --- |
| From | ``` optional func connection(_ connection: NSURLConnection!, canAuthenticateAgainstProtectionSpace protectionSpace: NSURLProtectionSpace!) -> Bool ``` | OS X 10.10 | -- | -- |
| To | ``` optional func connection(_ connection: NSURLConnection, canAuthenticateAgainstProtectionSpace protectionSpace: NSURLProtectionSpace) -> Bool ``` | OS X 10.6 | OS X 10.10 | yes |

Modified NSURLConnectionDelegate.connection(NSURLConnection, didCancelAuthenticationChallenge: NSURLAuthenticationChallenge)

|  | Declaration | Introduction | Deprecation | Optional |
| --- | --- | --- | --- | --- |
| From | ``` optional func connection(_ connection: NSURLConnection!, didCancelAuthenticationChallenge challenge: NSURLAuthenticationChallenge!) ``` | OS X 10.10 | -- | -- |
| To | ``` optional func connection(_ connection: NSURLConnection, didCancelAuthenticationChallenge challenge: NSURLAuthenticationChallenge) ``` | OS X 10.2 | OS X 10.10 | yes |

Modified NSURLConnectionDelegate.connection(NSURLConnection, didFailWithError: NSError)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func connection(_ connection: NSURLConnection!, didFailWithError error: NSError!) ``` | -- |
| To | ``` optional func connection(_ connection: NSURLConnection, didFailWithError error: NSError) ``` | yes |

Modified NSURLConnectionDelegate.connection(NSURLConnection, didReceiveAuthenticationChallenge: NSURLAuthenticationChallenge)

|  | Declaration | Introduction | Deprecation | Optional |
| --- | --- | --- | --- | --- |
| From | ``` optional func connection(_ connection: NSURLConnection!, didReceiveAuthenticationChallenge challenge: NSURLAuthenticationChallenge!) ``` | OS X 10.10 | -- | -- |
| To | ``` optional func connection(_ connection: NSURLConnection, didReceiveAuthenticationChallenge challenge: NSURLAuthenticationChallenge) ``` | OS X 10.2 | OS X 10.10 | yes |

Modified NSURLConnectionDelegate.connection(NSURLConnection, willSendRequestForAuthenticationChallenge: NSURLAuthenticationChallenge)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func connection(_ connection: NSURLConnection!, willSendRequestForAuthenticationChallenge challenge: NSURLAuthenticationChallenge!) ``` | -- |
| To | ``` optional func connection(_ connection: NSURLConnection, willSendRequestForAuthenticationChallenge challenge: NSURLAuthenticationChallenge) ``` | yes |

Modified NSURLConnectionDelegate.connectionShouldUseCredentialStorage(NSURLConnection) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func connectionShouldUseCredentialStorage(_ connection: NSURLConnection!) -> Bool ``` | -- |
| To | ``` optional func connectionShouldUseCredentialStorage(_ connection: NSURLConnection) -> Bool ``` | yes |

Modified NSURLConnectionDownloadDelegate.connection(NSURLConnection, didWriteData: Int64, totalBytesWritten: Int64, expectedTotalBytes: Int64)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func connection(_ connection: NSURLConnection!, didWriteData bytesWritten: Int64, totalBytesWritten totalBytesWritten: Int64, expectedTotalBytes expectedTotalBytes: Int64) ``` | -- |
| To | ``` optional func connection(_ connection: NSURLConnection, didWriteData bytesWritten: Int64, totalBytesWritten totalBytesWritten: Int64, expectedTotalBytes expectedTotalBytes: Int64) ``` | yes |

Modified NSURLConnectionDownloadDelegate.connectionDidFinishDownloading(NSURLConnection, destinationURL: NSURL)

|  | Declaration |
| --- | --- |
| From | ``` func connectionDidFinishDownloading(_ connection: NSURLConnection!, destinationURL destinationURL: NSURL!) ``` |
| To | ``` func connectionDidFinishDownloading(_ connection: NSURLConnection, destinationURL destinationURL: NSURL) ``` |

Modified NSURLConnectionDownloadDelegate.connectionDidResumeDownloading(NSURLConnection, totalBytesWritten: Int64, expectedTotalBytes: Int64)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func connectionDidResumeDownloading(_ connection: NSURLConnection!, totalBytesWritten totalBytesWritten: Int64, expectedTotalBytes expectedTotalBytes: Int64) ``` | -- |
| To | ``` optional func connectionDidResumeDownloading(_ connection: NSURLConnection, totalBytesWritten totalBytesWritten: Int64, expectedTotalBytes expectedTotalBytes: Int64) ``` | yes |

Modified NSURLCredential.certificates

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var certificates: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var certificates: [AnyObject] { get } ``` | OS X 10.6 |

Modified NSURLCredential.init(forTrust: SecTrust!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSURLCredential.identity

|  | Declaration |
| --- | --- |
| From | ``` var identity: SecIdentity! { get } ``` |
| To | ``` var identity: SecIdentity? { get } ``` |

Modified NSURLCredential.init(identity: SecIdentity, certificates:[AnyObject], persistence: NSURLCredentialPersistence)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(identity identity: SecIdentity!, certificates certArray: [AnyObject]!, persistence persistence: NSURLCredentialPersistence) ``` | OS X 10.10 |
| To | ``` init(identity identity: SecIdentity, certificates certArray: [AnyObject], persistence persistence: NSURLCredentialPersistence) ``` | OS X 10.6 |

Modified NSURLCredential.password

|  | Declaration |
| --- | --- |
| From | ``` var password: String! { get } ``` |
| To | ``` var password: String? { get } ``` |

Modified NSURLCredential.init(trust: SecTrust!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSURLCredential.user

|  | Declaration |
| --- | --- |
| From | ``` var user: String! { get } ``` |
| To | ``` var user: String? { get } ``` |

Modified NSURLCredential.init(user: String, password: String, persistence: NSURLCredentialPersistence)

|  | Declaration |
| --- | --- |
| From | ``` init(user user: String!, password password: String!, persistence persistence: NSURLCredentialPersistence) ``` |
| To | ``` init(user user: String, password password: String, persistence persistence: NSURLCredentialPersistence) ``` |

Modified NSURLCredentialPersistence.Synchronizable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSURLCredentialStorage.allCredentials

|  | Declaration |
| --- | --- |
| From | ``` var allCredentials: [NSObject : AnyObject]! { get } ``` |
| To | ``` var allCredentials: [NSObject : AnyObject] { get } ``` |

Modified NSURLCredentialStorage.credentialsForProtectionSpace(NSURLProtectionSpace) -> [NSObject: AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func credentialsForProtectionSpace(_ space: NSURLProtectionSpace!) -> [NSObject : AnyObject]! ``` |
| To | ``` func credentialsForProtectionSpace(_ space: NSURLProtectionSpace) -> [NSObject : AnyObject]? ``` |

Modified NSURLCredentialStorage.defaultCredentialForProtectionSpace(NSURLProtectionSpace) -> NSURLCredential?

|  | Declaration |
| --- | --- |
| From | ``` func defaultCredentialForProtectionSpace(_ space: NSURLProtectionSpace!) -> NSURLCredential! ``` |
| To | ``` func defaultCredentialForProtectionSpace(_ space: NSURLProtectionSpace) -> NSURLCredential? ``` |

Modified NSURLCredentialStorage.getCredentialsForProtectionSpace(NSURLProtectionSpace, task: NSURLSessionTask?, completionHandler:(([NSObject: AnyObject]!) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func getCredentialsForProtectionSpace(_ protectionSpace: NSURLProtectionSpace!, task task: NSURLSessionTask!, completionHandler completionHandler: (([NSObject : AnyObject]!) -> Void)!) ``` |
| To | ``` func getCredentialsForProtectionSpace(_ protectionSpace: NSURLProtectionSpace, task task: NSURLSessionTask?, completionHandler completionHandler: (([NSObject : AnyObject]!) -> Void)!) ``` |

Modified NSURLCredentialStorage.getDefaultCredentialForProtectionSpace(NSURLProtectionSpace, task: NSURLSessionTask?, completionHandler:((NSURLCredential!) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func getDefaultCredentialForProtectionSpace(_ space: NSURLProtectionSpace!, task task: NSURLSessionTask!, completionHandler completionHandler: ((NSURLCredential!) -> Void)!) ``` |
| To | ``` func getDefaultCredentialForProtectionSpace(_ space: NSURLProtectionSpace, task task: NSURLSessionTask?, completionHandler completionHandler: ((NSURLCredential!) -> Void)!) ``` |

Modified NSURLCredentialStorage.removeCredential(NSURLCredential, forProtectionSpace: NSURLProtectionSpace)

|  | Declaration |
| --- | --- |
| From | ``` func removeCredential(_ credential: NSURLCredential!, forProtectionSpace space: NSURLProtectionSpace!) ``` |
| To | ``` func removeCredential(_ credential: NSURLCredential, forProtectionSpace space: NSURLProtectionSpace) ``` |

Modified NSURLCredentialStorage.removeCredential(NSURLCredential, forProtectionSpace: NSURLProtectionSpace, options:[NSObject: AnyObject]?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func removeCredential(_ credential: NSURLCredential!, forProtectionSpace space: NSURLProtectionSpace!, options options: [NSObject : AnyObject]!) ``` | OS X 10.10 |
| To | ``` func removeCredential(_ credential: NSURLCredential, forProtectionSpace space: NSURLProtectionSpace, options options: [NSObject : AnyObject]?) ``` | OS X 10.9 |

Modified NSURLCredentialStorage.removeCredential(NSURLCredential, forProtectionSpace: NSURLProtectionSpace, options:[NSObject: AnyObject]?, task: NSURLSessionTask?)

|  | Declaration |
| --- | --- |
| From | ``` func removeCredential(_ credential: NSURLCredential!, forProtectionSpace protectionSpace: NSURLProtectionSpace!, options options: [NSObject : AnyObject]!, task task: NSURLSessionTask!) ``` |
| To | ``` func removeCredential(_ credential: NSURLCredential, forProtectionSpace protectionSpace: NSURLProtectionSpace, options options: [NSObject : AnyObject]?, task task: NSURLSessionTask?) ``` |

Modified NSURLCredentialStorage.setCredential(NSURLCredential, forProtectionSpace: NSURLProtectionSpace)

|  | Declaration |
| --- | --- |
| From | ``` func setCredential(_ credential: NSURLCredential!, forProtectionSpace space: NSURLProtectionSpace!) ``` |
| To | ``` func setCredential(_ credential: NSURLCredential, forProtectionSpace space: NSURLProtectionSpace) ``` |

Modified NSURLCredentialStorage.setCredential(NSURLCredential, forProtectionSpace: NSURLProtectionSpace, task: NSURLSessionTask)

|  | Declaration |
| --- | --- |
| From | ``` func setCredential(_ credential: NSURLCredential!, forProtectionSpace protectionSpace: NSURLProtectionSpace!, task task: NSURLSessionTask!) ``` |
| To | ``` func setCredential(_ credential: NSURLCredential, forProtectionSpace protectionSpace: NSURLProtectionSpace, task task: NSURLSessionTask) ``` |

Modified NSURLCredentialStorage.setDefaultCredential(NSURLCredential, forProtectionSpace: NSURLProtectionSpace)

|  | Declaration |
| --- | --- |
| From | ``` func setDefaultCredential(_ credential: NSURLCredential!, forProtectionSpace space: NSURLProtectionSpace!) ``` |
| To | ``` func setDefaultCredential(_ credential: NSURLCredential, forProtectionSpace space: NSURLProtectionSpace) ``` |

Modified NSURLCredentialStorage.setDefaultCredential(NSURLCredential, forProtectionSpace: NSURLProtectionSpace, task: NSURLSessionTask)

|  | Declaration |
| --- | --- |
| From | ``` func setDefaultCredential(_ credential: NSURLCredential!, forProtectionSpace protectionSpace: NSURLProtectionSpace!, task task: NSURLSessionTask!) ``` |
| To | ``` func setDefaultCredential(_ credential: NSURLCredential, forProtectionSpace protectionSpace: NSURLProtectionSpace, task task: NSURLSessionTask) ``` |

Modified NSURLCredentialStorage.sharedCredentialStorage() -> NSURLCredentialStorage [class]

|  | Declaration |
| --- | --- |
| From | ``` class func sharedCredentialStorage() -> NSURLCredentialStorage! ``` |
| To | ``` class func sharedCredentialStorage() -> NSURLCredentialStorage ``` |

Modified NSURLDownload.canResumeDownloadDecodedWithEncodingMIMEType(String) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func canResumeDownloadDecodedWithEncodingMIMEType(_ MIMEType: String!) -> Bool ``` |
| To | ``` class func canResumeDownloadDecodedWithEncodingMIMEType(_ MIMEType: String) -> Bool ``` |

Modified NSURLDownload.request

|  | Declaration |
| --- | --- |
| From | ``` var request: NSURLRequest! { get } ``` |
| To | ``` @NSCopying var request: NSURLRequest { get } ``` |

Modified NSURLDownload.init(request: NSURLRequest, delegate: NSURLDownloadDelegate?)

|  | Declaration |
| --- | --- |
| From | ``` init(request request: NSURLRequest!, delegate delegate: NSURLDownloadDelegate!) ``` |
| To | ``` init(request request: NSURLRequest, delegate delegate: NSURLDownloadDelegate?) ``` |

Modified NSURLDownload.resumeData

|  | Declaration |
| --- | --- |
| From | ``` var resumeData: NSData! { get } ``` |
| To | ``` @NSCopying var resumeData: NSData? { get } ``` |

Modified NSURLDownload.init(resumeData: NSData, delegate: NSURLDownloadDelegate?, path: String)

|  | Declaration |
| --- | --- |
| From | ``` init(resumeData resumeData: NSData!, delegate delegate: NSURLDownloadDelegate!, path path: String!) ``` |
| To | ``` init(resumeData resumeData: NSData, delegate delegate: NSURLDownloadDelegate?, path path: String) ``` |

Modified NSURLDownload.setDestination(String, allowOverwrite: Bool)

|  | Declaration |
| --- | --- |
| From | ``` func setDestination(_ path: String!, allowOverwrite allowOverwrite: Bool) ``` |
| To | ``` func setDestination(_ path: String, allowOverwrite allowOverwrite: Bool) ``` |

Modified NSURLDownloadDelegate.download(NSURLDownload, canAuthenticateAgainstProtectionSpace: NSURLProtectionSpace) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func download(_ connection: NSURLDownload!, canAuthenticateAgainstProtectionSpace protectionSpace: NSURLProtectionSpace!) -> Bool ``` | -- |
| To | ``` optional func download(_ connection: NSURLDownload, canAuthenticateAgainstProtectionSpace protectionSpace: NSURLProtectionSpace) -> Bool ``` | yes |

Modified NSURLDownloadDelegate.download(NSURLDownload, decideDestinationWithSuggestedFilename: String)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func download(_ download: NSURLDownload!, decideDestinationWithSuggestedFilename filename: String!) ``` | -- |
| To | ``` optional func download(_ download: NSURLDownload, decideDestinationWithSuggestedFilename filename: String) ``` | yes |

Modified NSURLDownloadDelegate.download(NSURLDownload, didCancelAuthenticationChallenge: NSURLAuthenticationChallenge)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func download(_ download: NSURLDownload!, didCancelAuthenticationChallenge challenge: NSURLAuthenticationChallenge!) ``` | -- |
| To | ``` optional func download(_ download: NSURLDownload, didCancelAuthenticationChallenge challenge: NSURLAuthenticationChallenge) ``` | yes |

Modified NSURLDownloadDelegate.download(NSURLDownload, didCreateDestination: String)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func download(_ download: NSURLDownload!, didCreateDestination path: String!) ``` | -- |
| To | ``` optional func download(_ download: NSURLDownload, didCreateDestination path: String) ``` | yes |

Modified NSURLDownloadDelegate.download(NSURLDownload, didFailWithError: NSError)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func download(_ download: NSURLDownload!, didFailWithError error: NSError!) ``` | -- |
| To | ``` optional func download(_ download: NSURLDownload, didFailWithError error: NSError) ``` | yes |

Modified NSURLDownloadDelegate.download(NSURLDownload, didReceiveAuthenticationChallenge: NSURLAuthenticationChallenge)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func download(_ download: NSURLDownload!, didReceiveAuthenticationChallenge challenge: NSURLAuthenticationChallenge!) ``` | -- |
| To | ``` optional func download(_ download: NSURLDownload, didReceiveAuthenticationChallenge challenge: NSURLAuthenticationChallenge) ``` | yes |

Modified NSURLDownloadDelegate.download(NSURLDownload, didReceiveDataOfLength: Int)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func download(_ download: NSURLDownload!, didReceiveDataOfLength length: Int) ``` | -- |
| To | ``` optional func download(_ download: NSURLDownload, didReceiveDataOfLength length: Int) ``` | yes |

Modified NSURLDownloadDelegate.download(NSURLDownload, didReceiveResponse: NSURLResponse)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func download(_ download: NSURLDownload!, didReceiveResponse response: NSURLResponse!) ``` | -- |
| To | ``` optional func download(_ download: NSURLDownload, didReceiveResponse response: NSURLResponse) ``` | yes |

Modified NSURLDownloadDelegate.download(NSURLDownload, shouldDecodeSourceDataOfMIMEType: String) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func download(_ download: NSURLDownload!, shouldDecodeSourceDataOfMIMEType encodingType: String!) -> Bool ``` | -- |
| To | ``` optional func download(_ download: NSURLDownload, shouldDecodeSourceDataOfMIMEType encodingType: String) -> Bool ``` | yes |

Modified NSURLDownloadDelegate.download(NSURLDownload, willResumeWithResponse: NSURLResponse, fromByte: Int64)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func download(_ download: NSURLDownload!, willResumeWithResponse response: NSURLResponse!, fromByte startingByte: Int64) ``` | -- |
| To | ``` optional func download(_ download: NSURLDownload, willResumeWithResponse response: NSURLResponse, fromByte startingByte: Int64) ``` | yes |

Modified NSURLDownloadDelegate.download(NSURLDownload, willSendRequest: NSURLRequest, redirectResponse: NSURLResponse?) -> NSURLRequest?

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func download(_ download: NSURLDownload!, willSendRequest request: NSURLRequest!, redirectResponse redirectResponse: NSURLResponse!) -> NSURLRequest! ``` | -- |
| To | ``` optional func download(_ download: NSURLDownload, willSendRequest request: NSURLRequest, redirectResponse redirectResponse: NSURLResponse?) -> NSURLRequest? ``` | yes |

Modified NSURLDownloadDelegate.downloadDidBegin(NSURLDownload)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func downloadDidBegin(_ download: NSURLDownload!) ``` | -- |
| To | ``` optional func downloadDidBegin(_ download: NSURLDownload) ``` | yes |

Modified NSURLDownloadDelegate.downloadDidFinish(NSURLDownload)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func downloadDidFinish(_ download: NSURLDownload!) ``` | -- |
| To | ``` optional func downloadDidFinish(_ download: NSURLDownload) ``` | yes |

Modified NSURLDownloadDelegate.downloadShouldUseCredentialStorage(NSURLDownload) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func downloadShouldUseCredentialStorage(_ download: NSURLDownload!) -> Bool ``` | -- |
| To | ``` optional func downloadShouldUseCredentialStorage(_ download: NSURLDownload) -> Bool ``` | yes |

Modified NSURLProtectionSpace.authenticationMethod

|  | Declaration |
| --- | --- |
| From | ``` var authenticationMethod: String! { get } ``` |
| To | ``` var authenticationMethod: String? { get } ``` |

Modified NSURLProtectionSpace.distinguishedNames

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var distinguishedNames: [AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var distinguishedNames: [AnyObject]? { get } ``` | OS X 10.6 |

Modified NSURLProtectionSpace.host

|  | Declaration |
| --- | --- |
| From | ``` var host: String! { get } ``` |
| To | ``` var host: String { get } ``` |

Modified NSURLProtectionSpace.init(host: String, port: Int, protocol: String?, realm: String?, authenticationMethod: String?)

|  | Declaration |
| --- | --- |
| From | ``` init(host host: String!, port port: Int, `protocol` `protocol`: String!, realm realm: String!, authenticationMethod authenticationMethod: String!) ``` |
| To | ``` init(host host: String, port port: Int, `protocol` `protocol`: String?, realm realm: String?, authenticationMethod authenticationMethod: String?) ``` |

Modified NSURLProtectionSpace.protocol

|  | Declaration |
| --- | --- |
| From | ``` var `protocol`: String! { get } ``` |
| To | ``` var `protocol`: String? { get } ``` |

Modified NSURLProtectionSpace.init(proxyHost: String, port: Int, type: String?, realm: String?, authenticationMethod: String?)

|  | Declaration |
| --- | --- |
| From | ``` init(proxyHost host: String!, port port: Int, type type: String!, realm realm: String!, authenticationMethod authenticationMethod: String!) ``` |
| To | ``` init(proxyHost host: String, port port: Int, type type: String?, realm realm: String?, authenticationMethod authenticationMethod: String?) ``` |

Modified NSURLProtectionSpace.proxyType

|  | Declaration |
| --- | --- |
| From | ``` var proxyType: String! { get } ``` |
| To | ``` var proxyType: String? { get } ``` |

Modified NSURLProtectionSpace.realm

|  | Declaration |
| --- | --- |
| From | ``` var realm: String! { get } ``` |
| To | ``` var realm: String? { get } ``` |

Modified NSURLProtectionSpace.serverTrust

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var serverTrust: SecTrust! { get } ``` | OS X 10.10 |
| To | ``` var serverTrust: SecTrust? { get } ``` | OS X 10.6 |

Modified NSURLProtocol.cachedResponse

|  | Declaration |
| --- | --- |
| From | ``` var cachedResponse: NSCachedURLResponse! { get } ``` |
| To | ``` @NSCopying var cachedResponse: NSCachedURLResponse? { get } ``` |

Modified NSURLProtocol.canInitWithRequest(NSURLRequest) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func canInitWithRequest(_ request: NSURLRequest!) -> Bool ``` |
| To | ``` class func canInitWithRequest(_ request: NSURLRequest) -> Bool ``` |

Modified NSURLProtocol.canInitWithTask(NSURLSessionTask) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func canInitWithTask(_ task: NSURLSessionTask!) -> Bool ``` |
| To | ``` class func canInitWithTask(_ task: NSURLSessionTask) -> Bool ``` |

Modified NSURLProtocol.canonicalRequestForRequest(NSURLRequest) -> NSURLRequest [class]

|  | Declaration |
| --- | --- |
| From | ``` class func canonicalRequestForRequest(_ request: NSURLRequest!) -> NSURLRequest! ``` |
| To | ``` class func canonicalRequestForRequest(_ request: NSURLRequest) -> NSURLRequest ``` |

Modified NSURLProtocol.client

|  | Declaration |
| --- | --- |
| From | ``` var client: NSURLProtocolClient! { get } ``` |
| To | ``` var client: NSURLProtocolClient? { get } ``` |

Modified NSURLProtocol.propertyForKey(String, inRequest: NSURLRequest) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func propertyForKey(_ key: String!, inRequest request: NSURLRequest!) -> AnyObject! ``` |
| To | ``` class func propertyForKey(_ key: String, inRequest request: NSURLRequest) -> AnyObject? ``` |

Modified NSURLProtocol.registerClass(AnyClass) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func registerClass(_ protocolClass: AnyClass!) -> Bool ``` |
| To | ``` class func registerClass(_ protocolClass: AnyClass) -> Bool ``` |

Modified NSURLProtocol.removePropertyForKey(String, inRequest: NSMutableURLRequest) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func removePropertyForKey(_ key: String!, inRequest request: NSMutableURLRequest!) ``` |
| To | ``` class func removePropertyForKey(_ key: String, inRequest request: NSMutableURLRequest) ``` |

Modified NSURLProtocol.request

|  | Declaration |
| --- | --- |
| From | ``` var request: NSURLRequest! { get } ``` |
| To | ``` @NSCopying var request: NSURLRequest { get } ``` |

Modified NSURLProtocol.init(request: NSURLRequest, cachedResponse: NSCachedURLResponse?, client: NSURLProtocolClient?)

|  | Declaration |
| --- | --- |
| From | ``` init(request request: NSURLRequest!, cachedResponse cachedResponse: NSCachedURLResponse!, client client: NSURLProtocolClient!) ``` |
| To | ``` init(request request: NSURLRequest, cachedResponse cachedResponse: NSCachedURLResponse?, client client: NSURLProtocolClient?) ``` |

Modified NSURLProtocol.requestIsCacheEquivalent(NSURLRequest, toRequest: NSURLRequest) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func requestIsCacheEquivalent(_ a: NSURLRequest!, toRequest b: NSURLRequest!) -> Bool ``` |
| To | ``` class func requestIsCacheEquivalent(_ a: NSURLRequest, toRequest b: NSURLRequest) -> Bool ``` |

Modified NSURLProtocol.setProperty(AnyObject, forKey: String, inRequest: NSMutableURLRequest) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setProperty(_ value: AnyObject!, forKey key: String!, inRequest request: NSMutableURLRequest!) ``` |
| To | ``` class func setProperty(_ value: AnyObject, forKey key: String, inRequest request: NSMutableURLRequest) ``` |

Modified NSURLProtocol.task

|  | Declaration |
| --- | --- |
| From | ``` var task: NSURLSessionTask! { get } ``` |
| To | ``` @NSCopying var task: NSURLSessionTask? { get } ``` |

Modified NSURLProtocol.init(task: NSURLSessionTask, cachedResponse: NSCachedURLResponse?, client: NSURLProtocolClient?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(task task: NSURLSessionTask!, cachedResponse cachedResponse: NSCachedURLResponse!, client client: NSURLProtocolClient!) ``` |
| To | ``` convenience init(task task: NSURLSessionTask, cachedResponse cachedResponse: NSCachedURLResponse?, client client: NSURLProtocolClient?) ``` |

Modified NSURLProtocol.unregisterClass(AnyClass) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func unregisterClass(_ protocolClass: AnyClass!) ``` |
| To | ``` class func unregisterClass(_ protocolClass: AnyClass) ``` |

Modified NSURLProtocolClient.URLProtocol(NSURLProtocol, cachedResponseIsValid: NSCachedURLResponse)

|  | Declaration |
| --- | --- |
| From | ``` func URLProtocol(_ `protocol`: NSURLProtocol!, cachedResponseIsValid cachedResponse: NSCachedURLResponse!) ``` |
| To | ``` func URLProtocol(_ `protocol`: NSURLProtocol, cachedResponseIsValid cachedResponse: NSCachedURLResponse) ``` |

Modified NSURLProtocolClient.URLProtocol(NSURLProtocol, didCancelAuthenticationChallenge: NSURLAuthenticationChallenge)

|  | Declaration |
| --- | --- |
| From | ``` func URLProtocol(_ `protocol`: NSURLProtocol!, didCancelAuthenticationChallenge challenge: NSURLAuthenticationChallenge!) ``` |
| To | ``` func URLProtocol(_ `protocol`: NSURLProtocol, didCancelAuthenticationChallenge challenge: NSURLAuthenticationChallenge) ``` |

Modified NSURLProtocolClient.URLProtocol(NSURLProtocol, didFailWithError: NSError)

|  | Declaration |
| --- | --- |
| From | ``` func URLProtocol(_ `protocol`: NSURLProtocol!, didFailWithError error: NSError!) ``` |
| To | ``` func URLProtocol(_ `protocol`: NSURLProtocol, didFailWithError error: NSError) ``` |

Modified NSURLProtocolClient.URLProtocol(NSURLProtocol, didLoadData: NSData)

|  | Declaration |
| --- | --- |
| From | ``` func URLProtocol(_ `protocol`: NSURLProtocol!, didLoadData data: NSData!) ``` |
| To | ``` func URLProtocol(_ `protocol`: NSURLProtocol, didLoadData data: NSData) ``` |

Modified NSURLProtocolClient.URLProtocol(NSURLProtocol, didReceiveAuthenticationChallenge: NSURLAuthenticationChallenge)

|  | Declaration |
| --- | --- |
| From | ``` func URLProtocol(_ `protocol`: NSURLProtocol!, didReceiveAuthenticationChallenge challenge: NSURLAuthenticationChallenge!) ``` |
| To | ``` func URLProtocol(_ `protocol`: NSURLProtocol, didReceiveAuthenticationChallenge challenge: NSURLAuthenticationChallenge) ``` |

Modified NSURLProtocolClient.URLProtocol(NSURLProtocol, didReceiveResponse: NSURLResponse, cacheStoragePolicy: NSURLCacheStoragePolicy)

|  | Declaration |
| --- | --- |
| From | ``` func URLProtocol(_ `protocol`: NSURLProtocol!, didReceiveResponse response: NSURLResponse!, cacheStoragePolicy policy: NSURLCacheStoragePolicy) ``` |
| To | ``` func URLProtocol(_ `protocol`: NSURLProtocol, didReceiveResponse response: NSURLResponse, cacheStoragePolicy policy: NSURLCacheStoragePolicy) ``` |

Modified NSURLProtocolClient.URLProtocol(NSURLProtocol, wasRedirectedToRequest: NSURLRequest, redirectResponse: NSURLResponse)

|  | Declaration |
| --- | --- |
| From | ``` func URLProtocol(_ `protocol`: NSURLProtocol!, wasRedirectedToRequest request: NSURLRequest!, redirectResponse redirectResponse: NSURLResponse!) ``` |
| To | ``` func URLProtocol(_ `protocol`: NSURLProtocol, wasRedirectedToRequest request: NSURLRequest, redirectResponse redirectResponse: NSURLResponse) ``` |

Modified NSURLProtocolClient.URLProtocolDidFinishLoading(NSURLProtocol)

|  | Declaration |
| --- | --- |
| From | ``` func URLProtocolDidFinishLoading(_ `protocol`: NSURLProtocol!) ``` |
| To | ``` func URLProtocolDidFinishLoading(_ `protocol`: NSURLProtocol) ``` |

Modified NSURLQueryItem.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified NSURLQueryItem.init(name: String, value: String)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!, value value: String!) ``` |
| To | ``` init(name name: String, value value: String) ``` |

Modified NSURLQueryItem.value

|  | Declaration |
| --- | --- |
| From | ``` var value: String! { get } ``` |
| To | ``` var value: String? { get } ``` |

Modified NSURLRequest.HTTPBody

|  | Declaration |
| --- | --- |
| From | ``` var HTTPBody: NSData! { get } ``` |
| To | ``` @NSCopying var HTTPBody: NSData? { get } ``` |

Modified NSURLRequest.HTTPBodyStream

|  | Declaration |
| --- | --- |
| From | ``` var HTTPBodyStream: NSInputStream! { get } ``` |
| To | ``` var HTTPBodyStream: NSInputStream? { get } ``` |

Modified NSURLRequest.HTTPMethod

|  | Declaration |
| --- | --- |
| From | ``` var HTTPMethod: String! { get } ``` |
| To | ``` var HTTPMethod: String? { get } ``` |

Modified NSURLRequest.HTTPShouldUsePipelining

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSURLRequest.URL

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL? { get } ``` |

Modified NSURLRequest.init(URL: NSURL)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(URL URL: NSURL!) ``` |
| To | ``` convenience init(URL URL: NSURL) ``` |

Modified NSURLRequest.init(URL: NSURL, cachePolicy: NSURLRequestCachePolicy, timeoutInterval: NSTimeInterval)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL!, cachePolicy cachePolicy: NSURLRequestCachePolicy, timeoutInterval timeoutInterval: NSTimeInterval) ``` |
| To | ``` init(URL URL: NSURL, cachePolicy cachePolicy: NSURLRequestCachePolicy, timeoutInterval timeoutInterval: NSTimeInterval) ``` |

Modified NSURLRequest.allHTTPHeaderFields

|  | Declaration |
| --- | --- |
| From | ``` var allHTTPHeaderFields: [NSObject : AnyObject]! { get } ``` |
| To | ``` var allHTTPHeaderFields: [NSObject : AnyObject]? { get } ``` |

Modified NSURLRequest.allowsCellularAccess

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSURLRequest.mainDocumentURL

|  | Declaration |
| --- | --- |
| From | ``` var mainDocumentURL: NSURL! { get } ``` |
| To | ``` @NSCopying var mainDocumentURL: NSURL? { get } ``` |

Modified NSURLRequest.networkServiceType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSURLRequest.valueForHTTPHeaderField(String) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func valueForHTTPHeaderField(_ field: String!) -> String! ``` |
| To | ``` func valueForHTTPHeaderField(_ field: String) -> String? ``` |

Modified NSURLResponse.MIMEType

|  | Declaration |
| --- | --- |
| From | ``` var MIMEType: String! { get } ``` |
| To | ``` var MIMEType: String? { get } ``` |

Modified NSURLResponse.URL

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL? { get } ``` |

Modified NSURLResponse.init(URL: NSURL, MIMEType: String?, expectedContentLength: Int, textEncodingName: String?)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL!, MIMEType MIMEType: String!, expectedContentLength length: Int, textEncodingName name: String!) ``` |
| To | ``` init(URL URL: NSURL, MIMEType MIMEType: String?, expectedContentLength length: Int, textEncodingName name: String?) ``` |

Modified NSURLResponse.suggestedFilename

|  | Declaration |
| --- | --- |
| From | ``` var suggestedFilename: String! { get } ``` |
| To | ``` var suggestedFilename: String? { get } ``` |

Modified NSURLResponse.textEncodingName

|  | Declaration |
| --- | --- |
| From | ``` var textEncodingName: String! { get } ``` |
| To | ``` var textEncodingName: String? { get } ``` |

Modified NSURLSession

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSURLSession.configuration

|  | Declaration |
| --- | --- |
| From | ``` var configuration: NSURLSessionConfiguration! { get } ``` |
| To | ``` @NSCopying var configuration: NSURLSessionConfiguration { get } ``` |

Modified NSURLSession.init(configuration: NSURLSessionConfiguration)

|  | Declaration |
| --- | --- |
| From | ``` init(configuration configuration: NSURLSessionConfiguration!) -> NSURLSession ``` |
| To | ``` init(configuration configuration: NSURLSessionConfiguration) -> NSURLSession ``` |

Modified NSURLSession.init(configuration: NSURLSessionConfiguration?, delegate: NSURLSessionDelegate?, delegateQueue: NSOperationQueue?)

|  | Declaration |
| --- | --- |
| From | ``` init(configuration configuration: NSURLSessionConfiguration!, delegate delegate: NSURLSessionDelegate!, delegateQueue queue: NSOperationQueue!) -> NSURLSession ``` |
| To | ``` init(configuration configuration: NSURLSessionConfiguration?, delegate delegate: NSURLSessionDelegate?, delegateQueue queue: NSOperationQueue?) -> NSURLSession ``` |

Modified NSURLSession.dataTaskWithRequest(NSURLRequest) -> NSURLSessionDataTask

|  | Declaration |
| --- | --- |
| From | ``` func dataTaskWithRequest(_ request: NSURLRequest!) -> NSURLSessionDataTask! ``` |
| To | ``` func dataTaskWithRequest(_ request: NSURLRequest) -> NSURLSessionDataTask ``` |

Modified NSURLSession.dataTaskWithRequest(NSURLRequest, completionHandler:((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDataTask

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func dataTaskWithRequest(_ request: NSURLRequest!, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)!) -> NSURLSessionDataTask! ``` | OS X 10.10 |
| To | ``` func dataTaskWithRequest(_ request: NSURLRequest, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDataTask ``` | OS X 10.9 |

Modified NSURLSession.dataTaskWithURL(NSURL) -> NSURLSessionDataTask

|  | Declaration |
| --- | --- |
| From | ``` func dataTaskWithURL(_ url: NSURL!) -> NSURLSessionDataTask! ``` |
| To | ``` func dataTaskWithURL(_ url: NSURL) -> NSURLSessionDataTask ``` |

Modified NSURLSession.dataTaskWithURL(NSURL, completionHandler:((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDataTask

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func dataTaskWithURL(_ url: NSURL!, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)!) -> NSURLSessionDataTask! ``` | OS X 10.10 |
| To | ``` func dataTaskWithURL(_ url: NSURL, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDataTask ``` | OS X 10.9 |

Modified NSURLSession.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: NSURLSessionDelegate! { get } ``` |
| To | ``` var delegate: NSURLSessionDelegate? { get } ``` |

Modified NSURLSession.delegateQueue

|  | Declaration |
| --- | --- |
| From | ``` var delegateQueue: NSOperationQueue! { get } ``` |
| To | ``` var delegateQueue: NSOperationQueue { get } ``` |

Modified NSURLSession.downloadTaskWithRequest(NSURLRequest) -> NSURLSessionDownloadTask

|  | Declaration |
| --- | --- |
| From | ``` func downloadTaskWithRequest(_ request: NSURLRequest!) -> NSURLSessionDownloadTask! ``` |
| To | ``` func downloadTaskWithRequest(_ request: NSURLRequest) -> NSURLSessionDownloadTask ``` |

Modified NSURLSession.downloadTaskWithRequest(NSURLRequest, completionHandler:((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func downloadTaskWithRequest(_ request: NSURLRequest!, completionHandler completionHandler: ((NSURL!, NSURLResponse!, NSError!) -> Void)!) -> NSURLSessionDownloadTask! ``` | OS X 10.10 |
| To | ``` func downloadTaskWithRequest(_ request: NSURLRequest, completionHandler completionHandler: ((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask ``` | OS X 10.9 |

Modified NSURLSession.downloadTaskWithResumeData(NSData) -> NSURLSessionDownloadTask

|  | Declaration |
| --- | --- |
| From | ``` func downloadTaskWithResumeData(_ resumeData: NSData!) -> NSURLSessionDownloadTask! ``` |
| To | ``` func downloadTaskWithResumeData(_ resumeData: NSData) -> NSURLSessionDownloadTask ``` |

Modified NSURLSession.downloadTaskWithResumeData(NSData, completionHandler:((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func downloadTaskWithResumeData(_ resumeData: NSData!, completionHandler completionHandler: ((NSURL!, NSURLResponse!, NSError!) -> Void)!) -> NSURLSessionDownloadTask! ``` | OS X 10.10 |
| To | ``` func downloadTaskWithResumeData(_ resumeData: NSData, completionHandler completionHandler: ((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask ``` | OS X 10.9 |

Modified NSURLSession.downloadTaskWithURL(NSURL) -> NSURLSessionDownloadTask

|  | Declaration |
| --- | --- |
| From | ``` func downloadTaskWithURL(_ url: NSURL!) -> NSURLSessionDownloadTask! ``` |
| To | ``` func downloadTaskWithURL(_ url: NSURL) -> NSURLSessionDownloadTask ``` |

Modified NSURLSession.downloadTaskWithURL(NSURL, completionHandler:((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func downloadTaskWithURL(_ url: NSURL!, completionHandler completionHandler: ((NSURL!, NSURLResponse!, NSError!) -> Void)!) -> NSURLSessionDownloadTask! ``` | OS X 10.10 |
| To | ``` func downloadTaskWithURL(_ url: NSURL, completionHandler completionHandler: ((NSURL!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionDownloadTask ``` | OS X 10.9 |

Modified NSURLSession.flushWithCompletionHandler(() -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func flushWithCompletionHandler(_ completionHandler: (() -> Void)!) ``` |
| To | ``` func flushWithCompletionHandler(_ completionHandler: () -> Void) ``` |

Modified NSURLSession.getTasksWithCompletionHandler(([AnyObject]!,[AnyObject]!,[AnyObject]!) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func getTasksWithCompletionHandler(_ completionHandler: (([AnyObject]!, [AnyObject]!, [AnyObject]!) -> Void)!) ``` |
| To | ``` func getTasksWithCompletionHandler(_ completionHandler: ([AnyObject]!, [AnyObject]!, [AnyObject]!) -> Void) ``` |

Modified NSURLSession.resetWithCompletionHandler(() -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func resetWithCompletionHandler(_ completionHandler: (() -> Void)!) ``` |
| To | ``` func resetWithCompletionHandler(_ completionHandler: () -> Void) ``` |

Modified NSURLSession.sessionDescription

|  | Declaration |
| --- | --- |
| From | ``` var sessionDescription: String! ``` |
| To | ``` var sessionDescription: String? ``` |

Modified NSURLSession.sharedSession() -> NSURLSession [class]

|  | Declaration |
| --- | --- |
| From | ``` class func sharedSession() -> NSURLSession! ``` |
| To | ``` class func sharedSession() -> NSURLSession ``` |

Modified NSURLSession.uploadTaskWithRequest(NSURLRequest, fromData: NSData?) -> NSURLSessionUploadTask

|  | Declaration |
| --- | --- |
| From | ``` func uploadTaskWithRequest(_ request: NSURLRequest!, fromData bodyData: NSData!) -> NSURLSessionUploadTask! ``` |
| To | ``` func uploadTaskWithRequest(_ request: NSURLRequest, fromData bodyData: NSData?) -> NSURLSessionUploadTask ``` |

Modified NSURLSession.uploadTaskWithRequest(NSURLRequest, fromData: NSData?, completionHandler:((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionUploadTask

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func uploadTaskWithRequest(_ request: NSURLRequest!, fromData bodyData: NSData!, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)!) -> NSURLSessionUploadTask! ``` | OS X 10.10 |
| To | ``` func uploadTaskWithRequest(_ request: NSURLRequest, fromData bodyData: NSData?, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionUploadTask ``` | OS X 10.9 |

Modified NSURLSession.uploadTaskWithRequest(NSURLRequest, fromFile: NSURL) -> NSURLSessionUploadTask

|  | Declaration |
| --- | --- |
| From | ``` func uploadTaskWithRequest(_ request: NSURLRequest!, fromFile fileURL: NSURL!) -> NSURLSessionUploadTask! ``` |
| To | ``` func uploadTaskWithRequest(_ request: NSURLRequest, fromFile fileURL: NSURL) -> NSURLSessionUploadTask ``` |

Modified NSURLSession.uploadTaskWithRequest(NSURLRequest, fromFile: NSURL, completionHandler:((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionUploadTask

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func uploadTaskWithRequest(_ request: NSURLRequest!, fromFile fileURL: NSURL!, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)!) -> NSURLSessionUploadTask! ``` | OS X 10.10 |
| To | ``` func uploadTaskWithRequest(_ request: NSURLRequest, fromFile fileURL: NSURL, completionHandler completionHandler: ((NSData!, NSURLResponse!, NSError!) -> Void)?) -> NSURLSessionUploadTask ``` | OS X 10.9 |

Modified NSURLSession.uploadTaskWithStreamedRequest(NSURLRequest) -> NSURLSessionUploadTask

|  | Declaration |
| --- | --- |
| From | ``` func uploadTaskWithStreamedRequest(_ request: NSURLRequest!) -> NSURLSessionUploadTask! ``` |
| To | ``` func uploadTaskWithStreamedRequest(_ request: NSURLRequest) -> NSURLSessionUploadTask ``` |

Modified NSURLSessionAuthChallengeDisposition [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSURLSessionConfiguration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSURLSessionConfiguration.HTTPAdditionalHeaders

|  | Declaration |
| --- | --- |
| From | ``` var HTTPAdditionalHeaders: [NSObject : AnyObject]! ``` |
| To | ``` var HTTPAdditionalHeaders: [NSObject : AnyObject]? ``` |

Modified NSURLSessionConfiguration.HTTPCookieStorage

|  | Declaration |
| --- | --- |
| From | ``` var HTTPCookieStorage: NSHTTPCookieStorage! ``` |
| To | ``` var HTTPCookieStorage: NSHTTPCookieStorage? ``` |

Modified NSURLSessionConfiguration.URLCache

|  | Declaration |
| --- | --- |
| From | ``` var URLCache: NSURLCache! ``` |
| To | ``` var URLCache: NSURLCache? ``` |

Modified NSURLSessionConfiguration.URLCredentialStorage

|  | Declaration |
| --- | --- |
| From | ``` var URLCredentialStorage: NSURLCredentialStorage! ``` |
| To | ``` var URLCredentialStorage: NSURLCredentialStorage? ``` |

Modified NSURLSessionConfiguration.backgroundSessionConfiguration(String) -> NSURLSessionConfiguration [class]

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` class func backgroundSessionConfiguration(_ identifier: String!) -> NSURLSessionConfiguration! ``` | OS X 10.10 | -- |
| To | ``` class func backgroundSessionConfiguration(_ identifier: String) -> NSURLSessionConfiguration ``` | OS X 10.9 | OS X 10.10 |

Modified NSURLSessionConfiguration.backgroundSessionConfigurationWithIdentifier(String) -> NSURLSessionConfiguration [class]

|  | Declaration |
| --- | --- |
| From | ``` class func backgroundSessionConfigurationWithIdentifier(_ identifier: String!) -> NSURLSessionConfiguration! ``` |
| To | ``` class func backgroundSessionConfigurationWithIdentifier(_ identifier: String) -> NSURLSessionConfiguration ``` |

Modified NSURLSessionConfiguration.connectionProxyDictionary

|  | Declaration |
| --- | --- |
| From | ``` var connectionProxyDictionary: [NSObject : AnyObject]! ``` |
| To | ``` var connectionProxyDictionary: [NSObject : AnyObject]? ``` |

Modified NSURLSessionConfiguration.defaultSessionConfiguration() -> NSURLSessionConfiguration [class]

|  | Declaration |
| --- | --- |
| From | ``` class func defaultSessionConfiguration() -> NSURLSessionConfiguration! ``` |
| To | ``` class func defaultSessionConfiguration() -> NSURLSessionConfiguration ``` |

Modified NSURLSessionConfiguration.ephemeralSessionConfiguration() -> NSURLSessionConfiguration [class]

|  | Declaration |
| --- | --- |
| From | ``` class func ephemeralSessionConfiguration() -> NSURLSessionConfiguration! ``` |
| To | ``` class func ephemeralSessionConfiguration() -> NSURLSessionConfiguration ``` |

Modified NSURLSessionConfiguration.identifier

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` var identifier: String { get } ``` |

Modified NSURLSessionConfiguration.protocolClasses

|  | Declaration |
| --- | --- |
| From | ``` var protocolClasses: [AnyObject]! ``` |
| To | ``` var protocolClasses: [AnyObject]? ``` |

Modified NSURLSessionConfiguration.sharedContainerIdentifier

|  | Declaration |
| --- | --- |
| From | ``` var sharedContainerIdentifier: String! ``` |
| To | ``` var sharedContainerIdentifier: String? ``` |

Modified NSURLSessionDataDelegate.URLSession(NSURLSession, dataTask: NSURLSessionDataTask, didBecomeDownloadTask: NSURLSessionDownloadTask)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession!, dataTask dataTask: NSURLSessionDataTask!, didBecomeDownloadTask downloadTask: NSURLSessionDownloadTask!) ``` | -- |
| To | ``` optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didBecomeDownloadTask downloadTask: NSURLSessionDownloadTask) ``` | yes |

Modified NSURLSessionDataDelegate.URLSession(NSURLSession, dataTask: NSURLSessionDataTask, didReceiveData: NSData)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession!, dataTask dataTask: NSURLSessionDataTask!, didReceiveData data: NSData!) ``` | -- |
| To | ``` optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didReceiveData data: NSData) ``` | yes |

Modified NSURLSessionDataDelegate.URLSession(NSURLSession, dataTask: NSURLSessionDataTask, didReceiveResponse: NSURLResponse, completionHandler:(NSURLSessionResponseDisposition) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession!, dataTask dataTask: NSURLSessionDataTask!, didReceiveResponse response: NSURLResponse!, completionHandler completionHandler: ((NSURLSessionResponseDisposition) -> Void)!) ``` | -- |
| To | ``` optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, didReceiveResponse response: NSURLResponse, completionHandler completionHandler: (NSURLSessionResponseDisposition) -> Void) ``` | yes |

Modified NSURLSessionDataDelegate.URLSession(NSURLSession, dataTask: NSURLSessionDataTask, willCacheResponse: NSCachedURLResponse, completionHandler:(NSCachedURLResponse!) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession!, dataTask dataTask: NSURLSessionDataTask!, willCacheResponse proposedResponse: NSCachedURLResponse!, completionHandler completionHandler: ((NSCachedURLResponse!) -> Void)!) ``` | -- |
| To | ``` optional func URLSession(_ session: NSURLSession, dataTask dataTask: NSURLSessionDataTask, willCacheResponse proposedResponse: NSCachedURLResponse, completionHandler completionHandler: (NSCachedURLResponse!) -> Void) ``` | yes |

Modified NSURLSessionDelegate.URLSession(NSURLSession, didBecomeInvalidWithError: NSError?)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession!, didBecomeInvalidWithError error: NSError!) ``` | -- |
| To | ``` optional func URLSession(_ session: NSURLSession, didBecomeInvalidWithError error: NSError?) ``` | yes |

Modified NSURLSessionDelegate.URLSession(NSURLSession, didReceiveChallenge: NSURLAuthenticationChallenge, completionHandler:(NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession!, didReceiveChallenge challenge: NSURLAuthenticationChallenge!, completionHandler completionHandler: ((NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void)!) ``` | -- |
| To | ``` optional func URLSession(_ session: NSURLSession, didReceiveChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void) ``` | yes |

Modified NSURLSessionDownloadDelegate.URLSession(NSURLSession, downloadTask: NSURLSessionDownloadTask, didFinishDownloadingToURL: NSURL)

|  | Declaration |
| --- | --- |
| From | ``` func URLSession(_ session: NSURLSession!, downloadTask downloadTask: NSURLSessionDownloadTask!, didFinishDownloadingToURL location: NSURL!) ``` |
| To | ``` func URLSession(_ session: NSURLSession, downloadTask downloadTask: NSURLSessionDownloadTask, didFinishDownloadingToURL location: NSURL) ``` |

Modified NSURLSessionDownloadDelegate.URLSession(NSURLSession, downloadTask: NSURLSessionDownloadTask, didResumeAtOffset: Int64, expectedTotalBytes: Int64)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession!, downloadTask downloadTask: NSURLSessionDownloadTask!, didResumeAtOffset fileOffset: Int64, expectedTotalBytes expectedTotalBytes: Int64) ``` | -- |
| To | ``` optional func URLSession(_ session: NSURLSession, downloadTask downloadTask: NSURLSessionDownloadTask, didResumeAtOffset fileOffset: Int64, expectedTotalBytes expectedTotalBytes: Int64) ``` | yes |

Modified NSURLSessionDownloadDelegate.URLSession(NSURLSession, downloadTask: NSURLSessionDownloadTask, didWriteData: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession!, downloadTask downloadTask: NSURLSessionDownloadTask!, didWriteData bytesWritten: Int64, totalBytesWritten totalBytesWritten: Int64, totalBytesExpectedToWrite totalBytesExpectedToWrite: Int64) ``` | -- |
| To | ``` optional func URLSession(_ session: NSURLSession, downloadTask downloadTask: NSURLSessionDownloadTask, didWriteData bytesWritten: Int64, totalBytesWritten totalBytesWritten: Int64, totalBytesExpectedToWrite totalBytesExpectedToWrite: Int64) ``` | yes |

Modified NSURLSessionDownloadTask.cancelByProducingResumeData((NSData!) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func cancelByProducingResumeData(_ completionHandler: ((NSData!) -> Void)!) ``` |
| To | ``` func cancelByProducingResumeData(_ completionHandler: (NSData!) -> Void) ``` |

Modified NSURLSessionResponseDisposition [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSURLSessionTask

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSURLSessionTask.currentRequest

|  | Declaration |
| --- | --- |
| From | ``` var currentRequest: NSURLRequest! { get } ``` |
| To | ``` @NSCopying var currentRequest: NSURLRequest { get } ``` |

Modified NSURLSessionTask.error

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError! { get } ``` |
| To | ``` @NSCopying var error: NSError? { get } ``` |

Modified NSURLSessionTask.originalRequest

|  | Declaration |
| --- | --- |
| From | ``` var originalRequest: NSURLRequest! { get } ``` |
| To | ``` @NSCopying var originalRequest: NSURLRequest { get } ``` |

Modified NSURLSessionTask.response

|  | Declaration |
| --- | --- |
| From | ``` var response: NSURLResponse! { get } ``` |
| To | ``` @NSCopying var response: NSURLResponse? { get } ``` |

Modified NSURLSessionTask.taskDescription

|  | Declaration |
| --- | --- |
| From | ``` var taskDescription: String! ``` |
| To | ``` var taskDescription: String ``` |

Modified NSURLSessionTaskDelegate.URLSession(NSURLSession, task: NSURLSessionTask, didCompleteWithError: NSError?)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession!, task task: NSURLSessionTask!, didCompleteWithError error: NSError!) ``` | -- |
| To | ``` optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didCompleteWithError error: NSError?) ``` | yes |

Modified NSURLSessionTaskDelegate.URLSession(NSURLSession, task: NSURLSessionTask, didReceiveChallenge: NSURLAuthenticationChallenge, completionHandler:(NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession!, task task: NSURLSessionTask!, didReceiveChallenge challenge: NSURLAuthenticationChallenge!, completionHandler completionHandler: ((NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void)!) ``` | -- |
| To | ``` optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didReceiveChallenge challenge: NSURLAuthenticationChallenge, completionHandler completionHandler: (NSURLSessionAuthChallengeDisposition, NSURLCredential!) -> Void) ``` | yes |

Modified NSURLSessionTaskDelegate.URLSession(NSURLSession, task: NSURLSessionTask, didSendBodyData: Int64, totalBytesSent: Int64, totalBytesExpectedToSend: Int64)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession!, task task: NSURLSessionTask!, didSendBodyData bytesSent: Int64, totalBytesSent totalBytesSent: Int64, totalBytesExpectedToSend totalBytesExpectedToSend: Int64) ``` | -- |
| To | ``` optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, didSendBodyData bytesSent: Int64, totalBytesSent totalBytesSent: Int64, totalBytesExpectedToSend totalBytesExpectedToSend: Int64) ``` | yes |

Modified NSURLSessionTaskDelegate.URLSession(NSURLSession, task: NSURLSessionTask, needNewBodyStream:(NSInputStream!) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession!, task task: NSURLSessionTask!, needNewBodyStream completionHandler: ((NSInputStream!) -> Void)!) ``` | -- |
| To | ``` optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, needNewBodyStream completionHandler: (NSInputStream!) -> Void) ``` | yes |

Modified NSURLSessionTaskDelegate.URLSession(NSURLSession, task: NSURLSessionTask, willPerformHTTPRedirection: NSHTTPURLResponse, newRequest: NSURLRequest, completionHandler:(NSURLRequest!) -> Void)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func URLSession(_ session: NSURLSession!, task task: NSURLSessionTask!, willPerformHTTPRedirection response: NSHTTPURLResponse!, newRequest request: NSURLRequest!, completionHandler completionHandler: ((NSURLRequest!) -> Void)!) ``` | -- |
| To | ``` optional func URLSession(_ session: NSURLSession, task task: NSURLSessionTask, willPerformHTTPRedirection response: NSHTTPURLResponse, newRequest request: NSURLRequest, completionHandler completionHandler: (NSURLRequest!) -> Void) ``` | yes |

Modified NSURLSessionTaskState [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSUUID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSUUID.init(UUIDBytes: UnsafePointer<UInt8>)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(UUIDBytes bytes: ConstUnsafePointer<UInt8>) ``` |
| To | ``` convenience init(UUIDBytes bytes: UnsafePointer<UInt8>) ``` |

Modified NSUUID.UUIDString

|  | Declaration |
| --- | --- |
| From | ``` var UUIDString: String! { get } ``` |
| To | ``` var UUIDString: String { get } ``` |

Modified NSUUID.init(UUIDString: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(UUIDString string: String!) ``` |
| To | ``` convenience init?(UUIDString string: String) ``` |

Modified NSUUID.getUUIDBytes(UnsafeMutablePointer<UInt8>)

|  | Declaration |
| --- | --- |
| From | ``` func getUUIDBytes(_ uuid: UnsafePointer<UInt8>) ``` |
| To | ``` func getUUIDBytes(_ uuid: UnsafeMutablePointer<UInt8>) ``` |

Modified NSUbiquitousKeyValueStore

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSUbiquitousKeyValueStore.arrayForKey(String) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func arrayForKey(_ aKey: String!) -> [AnyObject]! ``` |
| To | ``` func arrayForKey(_ aKey: String) -> [AnyObject]? ``` |

Modified NSUbiquitousKeyValueStore.boolForKey(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func boolForKey(_ aKey: String!) -> Bool ``` |
| To | ``` func boolForKey(_ aKey: String) -> Bool ``` |

Modified NSUbiquitousKeyValueStore.dataForKey(String) -> NSData?

|  | Declaration |
| --- | --- |
| From | ``` func dataForKey(_ aKey: String!) -> NSData! ``` |
| To | ``` func dataForKey(_ aKey: String) -> NSData? ``` |

Modified NSUbiquitousKeyValueStore.defaultStore() -> NSUbiquitousKeyValueStore [class]

|  | Declaration |
| --- | --- |
| From | ``` class func defaultStore() -> NSUbiquitousKeyValueStore! ``` |
| To | ``` class func defaultStore() -> NSUbiquitousKeyValueStore ``` |

Modified NSUbiquitousKeyValueStore.dictionaryForKey(String) -> [NSObject: AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func dictionaryForKey(_ aKey: String!) -> [NSObject : AnyObject]! ``` |
| To | ``` func dictionaryForKey(_ aKey: String) -> [NSObject : AnyObject]? ``` |

Modified NSUbiquitousKeyValueStore.dictionaryRepresentation

|  | Declaration |
| --- | --- |
| From | ``` var dictionaryRepresentation: [NSObject : AnyObject]! { get } ``` |
| To | ``` var dictionaryRepresentation: [NSObject : AnyObject] { get } ``` |

Modified NSUbiquitousKeyValueStore.doubleForKey(String) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func doubleForKey(_ aKey: String!) -> Double ``` |
| To | ``` func doubleForKey(_ aKey: String) -> Double ``` |

Modified NSUbiquitousKeyValueStore.longLongForKey(String) -> Int64

|  | Declaration |
| --- | --- |
| From | ``` func longLongForKey(_ aKey: String!) -> Int64 ``` |
| To | ``` func longLongForKey(_ aKey: String) -> Int64 ``` |

Modified NSUbiquitousKeyValueStore.objectForKey(String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func objectForKey(_ aKey: String!) -> AnyObject! ``` |
| To | ``` func objectForKey(_ aKey: String) -> AnyObject? ``` |

Modified NSUbiquitousKeyValueStore.removeObjectForKey(String)

|  | Declaration |
| --- | --- |
| From | ``` func removeObjectForKey(_ aKey: String!) ``` |
| To | ``` func removeObjectForKey(_ aKey: String) ``` |

Modified NSUbiquitousKeyValueStore.setArray([AnyObject]?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setArray(_ anArray: [AnyObject]!, forKey aKey: String!) ``` |
| To | ``` func setArray(_ anArray: [AnyObject]?, forKey aKey: String) ``` |

Modified NSUbiquitousKeyValueStore.setBool(Bool, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setBool(_ value: Bool, forKey aKey: String!) ``` |
| To | ``` func setBool(_ value: Bool, forKey aKey: String) ``` |

Modified NSUbiquitousKeyValueStore.setData(NSData?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setData(_ aData: NSData!, forKey aKey: String!) ``` |
| To | ``` func setData(_ aData: NSData?, forKey aKey: String) ``` |

Modified NSUbiquitousKeyValueStore.setDictionary([NSObject: AnyObject]?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setDictionary(_ aDictionary: [NSObject : AnyObject]!, forKey aKey: String!) ``` |
| To | ``` func setDictionary(_ aDictionary: [NSObject : AnyObject]?, forKey aKey: String) ``` |

Modified NSUbiquitousKeyValueStore.setDouble(Double, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setDouble(_ value: Double, forKey aKey: String!) ``` |
| To | ``` func setDouble(_ value: Double, forKey aKey: String) ``` |

Modified NSUbiquitousKeyValueStore.setLongLong(Int64, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setLongLong(_ value: Int64, forKey aKey: String!) ``` |
| To | ``` func setLongLong(_ value: Int64, forKey aKey: String) ``` |

Modified NSUbiquitousKeyValueStore.setObject(AnyObject?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ anObject: AnyObject!, forKey aKey: String!) ``` |
| To | ``` func setObject(_ anObject: AnyObject?, forKey aKey: String) ``` |

Modified NSUbiquitousKeyValueStore.setString(String?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setString(_ aString: String!, forKey aKey: String!) ``` |
| To | ``` func setString(_ aString: String?, forKey aKey: String) ``` |

Modified NSUbiquitousKeyValueStore.stringForKey(String) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func stringForKey(_ aKey: String!) -> String! ``` |
| To | ``` func stringForKey(_ aKey: String) -> String? ``` |

Modified NSUnarchiver.classNameDecodedForArchiveClassName(String) -> String [class]

|  | Declaration |
| --- | --- |
| From | ``` class func classNameDecodedForArchiveClassName(_ inArchiveName: String!) -> String! ``` |
| To | ``` class func classNameDecodedForArchiveClassName(_ inArchiveName: String) -> String ``` |

Modified NSUnarchiver.classNameDecodedForArchiveClassName(String) -> String

|  | Declaration |
| --- | --- |
| From | ``` func classNameDecodedForArchiveClassName(_ inArchiveName: String!) -> String! ``` |
| To | ``` func classNameDecodedForArchiveClassName(_ inArchiveName: String) -> String ``` |

Modified NSUnarchiver.decodeClassName(String, asClassName: String) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func decodeClassName(_ inArchiveName: String!, asClassName trueName: String!) ``` |
| To | ``` class func decodeClassName(_ inArchiveName: String, asClassName trueName: String) ``` |

Modified NSUnarchiver.decodeClassName(String, asClassName: String)

|  | Declaration |
| --- | --- |
| From | ``` func decodeClassName(_ inArchiveName: String!, asClassName trueName: String!) ``` |
| To | ``` func decodeClassName(_ inArchiveName: String, asClassName trueName: String) ``` |

Modified NSUnarchiver.init(forReadingWithData: NSData)

|  | Declaration |
| --- | --- |
| From | ``` init(forReadingWithData data: NSData!) ``` |
| To | ``` init?(forReadingWithData data: NSData) ``` |

Modified NSUnarchiver.replaceObject(AnyObject, withObject: AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func replaceObject(_ object: AnyObject!, withObject newObject: AnyObject!) ``` |
| To | ``` func replaceObject(_ object: AnyObject, withObject newObject: AnyObject) ``` |

Modified NSUnarchiver.unarchiveObjectWithData(NSData) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func unarchiveObjectWithData(_ data: NSData!) -> AnyObject! ``` |
| To | ``` class func unarchiveObjectWithData(_ data: NSData) -> AnyObject? ``` |

Modified NSUnarchiver.unarchiveObjectWithFile(String) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func unarchiveObjectWithFile(_ path: String!) -> AnyObject! ``` |
| To | ``` class func unarchiveObjectWithFile(_ path: String) -> AnyObject? ``` |

Modified NSUndoManager

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified NSUndoManager.prepareWithInvocationTarget(AnyObject) -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func prepareWithInvocationTarget(_ target: AnyObject!) -> AnyObject! ``` |
| To | ``` func prepareWithInvocationTarget(_ target: AnyObject) -> AnyObject ``` |

Modified NSUndoManager.redoActionIsDiscardable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSUndoManager.redoActionName

|  | Declaration |
| --- | --- |
| From | ``` var redoActionName: String! { get } ``` |
| To | ``` var redoActionName: String { get } ``` |

Modified NSUndoManager.redoMenuItemTitle

|  | Declaration |
| --- | --- |
| From | ``` var redoMenuItemTitle: String! { get } ``` |
| To | ``` var redoMenuItemTitle: String { get } ``` |

Modified NSUndoManager.redoMenuTitleForUndoActionName(String) -> String

|  | Declaration |
| --- | --- |
| From | ``` func redoMenuTitleForUndoActionName(_ actionName: String!) -> String! ``` |
| To | ``` func redoMenuTitleForUndoActionName(_ actionName: String) -> String ``` |

Modified NSUndoManager.registerUndoWithTarget(AnyObject, selector: Selector, object: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func registerUndoWithTarget(_ target: AnyObject!, selector selector: Selector, object anObject: AnyObject!) ``` |
| To | ``` func registerUndoWithTarget(_ target: AnyObject, selector selector: Selector, object anObject: AnyObject?) ``` |

Modified NSUndoManager.removeAllActionsWithTarget(AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` func removeAllActionsWithTarget(_ target: AnyObject!) ``` |
| To | ``` func removeAllActionsWithTarget(_ target: AnyObject) ``` |

Modified NSUndoManager.runLoopModes

|  | Declaration |
| --- | --- |
| From | ``` var runLoopModes: [AnyObject]! ``` |
| To | ``` var runLoopModes: [AnyObject] ``` |

Modified NSUndoManager.setActionIsDiscardable(Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSUndoManager.setActionName(String)

|  | Declaration |
| --- | --- |
| From | ``` func setActionName(_ actionName: String!) ``` |
| To | ``` func setActionName(_ actionName: String) ``` |

Modified NSUndoManager.undoActionIsDiscardable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSUndoManager.undoActionName

|  | Declaration |
| --- | --- |
| From | ``` var undoActionName: String! { get } ``` |
| To | ``` var undoActionName: String { get } ``` |

Modified NSUndoManager.undoMenuItemTitle

|  | Declaration |
| --- | --- |
| From | ``` var undoMenuItemTitle: String! { get } ``` |
| To | ``` var undoMenuItemTitle: String { get } ``` |

Modified NSUndoManager.undoMenuTitleForUndoActionName(String) -> String

|  | Declaration |
| --- | --- |
| From | ``` func undoMenuTitleForUndoActionName(_ actionName: String!) -> String! ``` |
| To | ``` func undoMenuTitleForUndoActionName(_ actionName: String) -> String ``` |

Modified NSUniqueIDSpecifier.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder inCoder: NSCoder!) ``` |
| To | ``` init(coder inCoder: NSCoder) ``` |

Modified NSUniqueIDSpecifier.init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier?, key: String, uniqueID: AnyObject)

|  | Declaration |
| --- | --- |
| From | ``` init(containerClassDescription classDesc: NSScriptClassDescription!, containerSpecifier container: NSScriptObjectSpecifier!, key property: String!, uniqueID uniqueID: AnyObject!) ``` |
| To | ``` init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String, uniqueID uniqueID: AnyObject) ``` |

Modified NSUniqueIDSpecifier.uniqueID

|  | Declaration |
| --- | --- |
| From | ``` var uniqueID: AnyObject! ``` |
| To | ``` @NSCopying var uniqueID: AnyObject ``` |

Modified NSUserActivity.activityType

|  | Declaration |
| --- | --- |
| From | ``` var activityType: String! { get } ``` |
| To | ``` var activityType: String { get } ``` |

Modified NSUserActivity.init(activityType: String)

|  | Declaration |
| --- | --- |
| From | ``` init(activityType activityType: String!) ``` |
| To | ``` init(activityType activityType: String) ``` |

Modified NSUserActivity.addUserInfoEntriesFromDictionary([NSObject: AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func addUserInfoEntriesFromDictionary(_ otherDictionary: [NSObject : AnyObject]!) ``` |
| To | ``` func addUserInfoEntriesFromDictionary(_ otherDictionary: [NSObject : AnyObject]) ``` |

Modified NSUserActivity.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: NSUserActivityDelegate! ``` |
| To | ``` weak var delegate: NSUserActivityDelegate? ``` |

Modified NSUserActivity.getContinuationStreamsWithCompletionHandler((NSInputStream!, NSOutputStream!, NSError!) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func getContinuationStreamsWithCompletionHandler(_ completionHandler: ((NSInputStream!, NSOutputStream!, NSError!) -> Void)!) ``` |
| To | ``` func getContinuationStreamsWithCompletionHandler(_ completionHandler: (NSInputStream!, NSOutputStream!, NSError!) -> Void) ``` |

Modified NSUserActivity.title

|  | Declaration |
| --- | --- |
| From | ``` var title: String! ``` |
| To | ``` var title: String? ``` |

Modified NSUserActivity.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? ``` |

Modified NSUserActivity.webpageURL

|  | Declaration |
| --- | --- |
| From | ``` var webpageURL: NSURL! ``` |
| To | ``` @NSCopying var webpageURL: NSURL? ``` |

Modified NSUserActivityDelegate.userActivity(NSUserActivity, didReceiveInputStream: NSInputStream, outputStream: NSOutputStream)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func userActivity(_ userActivity: NSUserActivity!, didReceiveInputStream inputStream: NSInputStream!, outputStream outputStream: NSOutputStream!) ``` | -- |
| To | ``` optional func userActivity(_ userActivity: NSUserActivity, didReceiveInputStream inputStream: NSInputStream, outputStream outputStream: NSOutputStream) ``` | yes |

Modified NSUserActivityDelegate.userActivityWasContinued(NSUserActivity)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func userActivityWasContinued(_ userActivity: NSUserActivity!) ``` | -- |
| To | ``` optional func userActivityWasContinued(_ userActivity: NSUserActivity) ``` | yes |

Modified NSUserActivityDelegate.userActivityWillSave(NSUserActivity)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func userActivityWillSave(_ userActivity: NSUserActivity!) ``` | -- |
| To | ``` optional func userActivityWillSave(_ userActivity: NSUserActivity) ``` | yes |

Modified NSUserAppleScriptTask

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSUserAppleScriptTask.executeWithAppleEvent(NSAppleEventDescriptor, completionHandler: NSUserAppleScriptTaskCompletionHandler!)

|  | Declaration |
| --- | --- |
| From | ``` func executeWithAppleEvent(_ event: NSAppleEventDescriptor!, completionHandler handler: NSUserAppleScriptTaskCompletionHandler!) ``` |
| To | ``` func executeWithAppleEvent(_ event: NSAppleEventDescriptor, completionHandler handler: NSUserAppleScriptTaskCompletionHandler!) ``` |

Modified NSUserAutomatorTask

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSUserAutomatorTask.executeWithInput(NSSecureCoding?, completionHandler: NSUserAutomatorTaskCompletionHandler!)

|  | Declaration |
| --- | --- |
| From | ``` func executeWithInput(_ input: NSSecureCoding!, completionHandler handler: NSUserAutomatorTaskCompletionHandler!) ``` |
| To | ``` func executeWithInput(_ input: NSSecureCoding?, completionHandler handler: NSUserAutomatorTaskCompletionHandler!) ``` |

Modified NSUserAutomatorTask.variables

|  | Declaration |
| --- | --- |
| From | ``` var variables: [NSObject : AnyObject]! ``` |
| To | ``` var variables: [NSObject : AnyObject]? ``` |

Modified NSUserDefaults.URLForKey(String) -> NSURL?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URLForKey(_ defaultName: String!) -> NSURL! ``` | OS X 10.10 |
| To | ``` func URLForKey(_ defaultName: String) -> NSURL? ``` | OS X 10.6 |

Modified NSUserDefaults.addSuiteNamed(String)

|  | Declaration |
| --- | --- |
| From | ``` func addSuiteNamed(_ suiteName: String!) ``` |
| To | ``` func addSuiteNamed(_ suiteName: String) ``` |

Modified NSUserDefaults.arrayForKey(String) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func arrayForKey(_ defaultName: String!) -> [AnyObject]! ``` |
| To | ``` func arrayForKey(_ defaultName: String) -> [AnyObject]? ``` |

Modified NSUserDefaults.boolForKey(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func boolForKey(_ defaultName: String!) -> Bool ``` |
| To | ``` func boolForKey(_ defaultName: String) -> Bool ``` |

Modified NSUserDefaults.dataForKey(String) -> NSData?

|  | Declaration |
| --- | --- |
| From | ``` func dataForKey(_ defaultName: String!) -> NSData! ``` |
| To | ``` func dataForKey(_ defaultName: String) -> NSData? ``` |

Modified NSUserDefaults.dictionaryForKey(String) -> [NSObject: AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func dictionaryForKey(_ defaultName: String!) -> [NSObject : AnyObject]! ``` |
| To | ``` func dictionaryForKey(_ defaultName: String) -> [NSObject : AnyObject]? ``` |

Modified NSUserDefaults.dictionaryRepresentation() -> [NSObject: AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func dictionaryRepresentation() -> [NSObject : AnyObject]! ``` |
| To | ``` func dictionaryRepresentation() -> [NSObject : AnyObject] ``` |

Modified NSUserDefaults.doubleForKey(String) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func doubleForKey(_ defaultName: String!) -> Double ``` |
| To | ``` func doubleForKey(_ defaultName: String) -> Double ``` |

Modified NSUserDefaults.floatForKey(String) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func floatForKey(_ defaultName: String!) -> Float ``` |
| To | ``` func floatForKey(_ defaultName: String) -> Float ``` |

Modified NSUserDefaults.integerForKey(String) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func integerForKey(_ defaultName: String!) -> Int ``` |
| To | ``` func integerForKey(_ defaultName: String) -> Int ``` |

Modified NSUserDefaults.objectForKey(String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func objectForKey(_ defaultName: String!) -> AnyObject! ``` |
| To | ``` func objectForKey(_ defaultName: String) -> AnyObject? ``` |

Modified NSUserDefaults.objectIsForcedForKey(String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func objectIsForcedForKey(_ key: String!) -> Bool ``` |
| To | ``` func objectIsForcedForKey(_ key: String) -> Bool ``` |

Modified NSUserDefaults.objectIsForcedForKey(String, inDomain: String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func objectIsForcedForKey(_ key: String!, inDomain domain: String!) -> Bool ``` |
| To | ``` func objectIsForcedForKey(_ key: String, inDomain domain: String) -> Bool ``` |

Modified NSUserDefaults.persistentDomainForName(String) -> [NSObject: AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func persistentDomainForName(_ domainName: String!) -> [NSObject : AnyObject]! ``` |
| To | ``` func persistentDomainForName(_ domainName: String) -> [NSObject : AnyObject]? ``` |

Modified NSUserDefaults.registerDefaults([NSObject: AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func registerDefaults(_ registrationDictionary: [NSObject : AnyObject]!) ``` |
| To | ``` func registerDefaults(_ registrationDictionary: [NSObject : AnyObject]) ``` |

Modified NSUserDefaults.removeObjectForKey(String)

|  | Declaration |
| --- | --- |
| From | ``` func removeObjectForKey(_ defaultName: String!) ``` |
| To | ``` func removeObjectForKey(_ defaultName: String) ``` |

Modified NSUserDefaults.removePersistentDomainForName(String)

|  | Declaration |
| --- | --- |
| From | ``` func removePersistentDomainForName(_ domainName: String!) ``` |
| To | ``` func removePersistentDomainForName(_ domainName: String) ``` |

Modified NSUserDefaults.removeSuiteNamed(String)

|  | Declaration |
| --- | --- |
| From | ``` func removeSuiteNamed(_ suiteName: String!) ``` |
| To | ``` func removeSuiteNamed(_ suiteName: String) ``` |

Modified NSUserDefaults.removeVolatileDomainForName(String)

|  | Declaration |
| --- | --- |
| From | ``` func removeVolatileDomainForName(_ domainName: String!) ``` |
| To | ``` func removeVolatileDomainForName(_ domainName: String) ``` |

Modified NSUserDefaults.setBool(Bool, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setBool(_ value: Bool, forKey defaultName: String!) ``` |
| To | ``` func setBool(_ value: Bool, forKey defaultName: String) ``` |

Modified NSUserDefaults.setDouble(Double, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setDouble(_ value: Double, forKey defaultName: String!) ``` |
| To | ``` func setDouble(_ value: Double, forKey defaultName: String) ``` |

Modified NSUserDefaults.setFloat(Float, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setFloat(_ value: Float, forKey defaultName: String!) ``` |
| To | ``` func setFloat(_ value: Float, forKey defaultName: String) ``` |

Modified NSUserDefaults.setInteger(Int, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setInteger(_ value: Int, forKey defaultName: String!) ``` |
| To | ``` func setInteger(_ value: Int, forKey defaultName: String) ``` |

Modified NSUserDefaults.setObject(AnyObject?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ value: AnyObject!, forKey defaultName: String!) ``` |
| To | ``` func setObject(_ value: AnyObject?, forKey defaultName: String) ``` |

Modified NSUserDefaults.setPersistentDomain([NSObject: AnyObject], forName: String)

|  | Declaration |
| --- | --- |
| From | ``` func setPersistentDomain(_ domain: [NSObject : AnyObject]!, forName domainName: String!) ``` |
| To | ``` func setPersistentDomain(_ domain: [NSObject : AnyObject], forName domainName: String) ``` |

Modified NSUserDefaults.setURL(NSURL, forKey: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setURL(_ url: NSURL!, forKey defaultName: String!) ``` | OS X 10.10 |
| To | ``` func setURL(_ url: NSURL, forKey defaultName: String) ``` | OS X 10.6 |

Modified NSUserDefaults.setVolatileDomain([NSObject: AnyObject], forName: String)

|  | Declaration |
| --- | --- |
| From | ``` func setVolatileDomain(_ domain: [NSObject : AnyObject]!, forName domainName: String!) ``` |
| To | ``` func setVolatileDomain(_ domain: [NSObject : AnyObject], forName domainName: String) ``` |

Modified NSUserDefaults.standardUserDefaults() -> NSUserDefaults [class]

|  | Declaration |
| --- | --- |
| From | ``` class func standardUserDefaults() -> NSUserDefaults! ``` |
| To | ``` class func standardUserDefaults() -> NSUserDefaults ``` |

Modified NSUserDefaults.stringArrayForKey(String) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func stringArrayForKey(_ defaultName: String!) -> [AnyObject]! ``` |
| To | ``` func stringArrayForKey(_ defaultName: String) -> [AnyObject]? ``` |

Modified NSUserDefaults.stringForKey(String) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func stringForKey(_ defaultName: String!) -> String! ``` |
| To | ``` func stringForKey(_ defaultName: String) -> String? ``` |

Modified NSUserDefaults.init(suiteName: String?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(suiteName suitename: String!) ``` | OS X 10.10 |
| To | ``` init?(suiteName suitename: String?) ``` | OS X 10.9 |

Modified NSUserDefaults.volatileDomainForName(String) -> [NSObject: AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func volatileDomainForName(_ domainName: String!) -> [NSObject : AnyObject]! ``` |
| To | ``` func volatileDomainForName(_ domainName: String) -> [NSObject : AnyObject] ``` |

Modified NSUserDefaults.volatileDomainNames

|  | Declaration |
| --- | --- |
| From | ``` var volatileDomainNames: [AnyObject]! { get } ``` |
| To | ``` var volatileDomainNames: [AnyObject] { get } ``` |

Modified NSUserNotification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSUserNotification.actionButtonTitle

|  | Declaration |
| --- | --- |
| From | ``` var actionButtonTitle: String! ``` |
| To | ``` var actionButtonTitle: String ``` |

Modified NSUserNotification.actualDeliveryDate

|  | Declaration |
| --- | --- |
| From | ``` var actualDeliveryDate: NSDate! { get } ``` |
| To | ``` @NSCopying var actualDeliveryDate: NSDate? { get } ``` |

Modified NSUserNotification.additionalActions

|  | Declaration |
| --- | --- |
| From | ``` var additionalActions: [AnyObject]! ``` |
| To | ``` var additionalActions: [AnyObject]? ``` |

Modified NSUserNotification.additionalActivationAction

|  | Declaration |
| --- | --- |
| From | ``` var additionalActivationAction: NSUserNotificationAction! { get } ``` |
| To | ``` @NSCopying var additionalActivationAction: NSUserNotificationAction? { get } ``` |

Modified NSUserNotification.deliveryDate

|  | Declaration |
| --- | --- |
| From | ``` var deliveryDate: NSDate! ``` |
| To | ``` @NSCopying var deliveryDate: NSDate? ``` |

Modified NSUserNotification.deliveryRepeatInterval

|  | Declaration |
| --- | --- |
| From | ``` var deliveryRepeatInterval: NSDateComponents! ``` |
| To | ``` @NSCopying var deliveryRepeatInterval: NSDateComponents? ``` |

Modified NSUserNotification.deliveryTimeZone

|  | Declaration |
| --- | --- |
| From | ``` var deliveryTimeZone: NSTimeZone! ``` |
| To | ``` @NSCopying var deliveryTimeZone: NSTimeZone? ``` |

Modified NSUserNotification.hasReplyButton

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSUserNotification.identifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var identifier: String! ``` | OS X 10.10 |
| To | ``` var identifier: String? ``` | OS X 10.9 |

Modified NSUserNotification.informativeText

|  | Declaration |
| --- | --- |
| From | ``` var informativeText: String! ``` |
| To | ``` var informativeText: String? ``` |

Modified NSUserNotification.otherButtonTitle

|  | Declaration |
| --- | --- |
| From | ``` var otherButtonTitle: String! ``` |
| To | ``` var otherButtonTitle: String ``` |

Modified NSUserNotification.response

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var response: NSAttributedString! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var response: NSAttributedString? { get } ``` | OS X 10.9 |

Modified NSUserNotification.responsePlaceholder

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var responsePlaceholder: String! ``` | OS X 10.10 |
| To | ``` var responsePlaceholder: String? ``` | OS X 10.9 |

Modified NSUserNotification.soundName

|  | Declaration |
| --- | --- |
| From | ``` var soundName: String! ``` |
| To | ``` var soundName: String? ``` |

Modified NSUserNotification.subtitle

|  | Declaration |
| --- | --- |
| From | ``` var subtitle: String! ``` |
| To | ``` var subtitle: String? ``` |

Modified NSUserNotification.title

|  | Declaration |
| --- | --- |
| From | ``` var title: String! ``` |
| To | ``` var title: String? ``` |

Modified NSUserNotification.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? ``` |

Modified NSUserNotificationAction.identifier

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` var identifier: String? { get } ``` |

Modified NSUserNotificationAction.init(identifier: String?, title: String?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(identifier identifier: String!, title title: String!) ``` |
| To | ``` convenience init(identifier identifier: String?, title title: String?) ``` |

Modified NSUserNotificationAction.title

|  | Declaration |
| --- | --- |
| From | ``` var title: String! { get } ``` |
| To | ``` var title: String? { get } ``` |

Modified NSUserNotificationActivationType [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSUserNotificationActivationType.Replied

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSUserNotificationCenter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSUserNotificationCenter.defaultUserNotificationCenter() -> NSUserNotificationCenter [class]

|  | Declaration |
| --- | --- |
| From | ``` class func defaultUserNotificationCenter() -> NSUserNotificationCenter! ``` |
| To | ``` class func defaultUserNotificationCenter() -> NSUserNotificationCenter ``` |

Modified NSUserNotificationCenter.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: NSUserNotificationCenterDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: NSUserNotificationCenterDelegate? ``` |

Modified NSUserNotificationCenter.deliverNotification(NSUserNotification)

|  | Declaration |
| --- | --- |
| From | ``` func deliverNotification(_ notification: NSUserNotification!) ``` |
| To | ``` func deliverNotification(_ notification: NSUserNotification) ``` |

Modified NSUserNotificationCenter.deliveredNotifications

|  | Declaration |
| --- | --- |
| From | ``` var deliveredNotifications: [AnyObject]! { get } ``` |
| To | ``` var deliveredNotifications: [AnyObject] { get } ``` |

Modified NSUserNotificationCenter.removeDeliveredNotification(NSUserNotification)

|  | Declaration |
| --- | --- |
| From | ``` func removeDeliveredNotification(_ notification: NSUserNotification!) ``` |
| To | ``` func removeDeliveredNotification(_ notification: NSUserNotification) ``` |

Modified NSUserNotificationCenter.removeScheduledNotification(NSUserNotification)

|  | Declaration |
| --- | --- |
| From | ``` func removeScheduledNotification(_ notification: NSUserNotification!) ``` |
| To | ``` func removeScheduledNotification(_ notification: NSUserNotification) ``` |

Modified NSUserNotificationCenter.scheduleNotification(NSUserNotification)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleNotification(_ notification: NSUserNotification!) ``` |
| To | ``` func scheduleNotification(_ notification: NSUserNotification) ``` |

Modified NSUserNotificationCenter.scheduledNotifications

|  | Declaration |
| --- | --- |
| From | ``` var scheduledNotifications: [AnyObject]! ``` |
| To | ``` var scheduledNotifications: [AnyObject] ``` |

Modified NSUserNotificationCenterDelegate.userNotificationCenter(NSUserNotificationCenter, didActivateNotification: NSUserNotification)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func userNotificationCenter(_ center: NSUserNotificationCenter!, didActivateNotification notification: NSUserNotification!) ``` | -- |
| To | ``` optional func userNotificationCenter(_ center: NSUserNotificationCenter, didActivateNotification notification: NSUserNotification) ``` | yes |

Modified NSUserNotificationCenterDelegate.userNotificationCenter(NSUserNotificationCenter, didDeliverNotification: NSUserNotification)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func userNotificationCenter(_ center: NSUserNotificationCenter!, didDeliverNotification notification: NSUserNotification!) ``` | -- |
| To | ``` optional func userNotificationCenter(_ center: NSUserNotificationCenter, didDeliverNotification notification: NSUserNotification) ``` | yes |

Modified NSUserNotificationCenterDelegate.userNotificationCenter(NSUserNotificationCenter, shouldPresentNotification: NSUserNotification) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func userNotificationCenter(_ center: NSUserNotificationCenter!, shouldPresentNotification notification: NSUserNotification!) -> Bool ``` | -- |
| To | ``` optional func userNotificationCenter(_ center: NSUserNotificationCenter, shouldPresentNotification notification: NSUserNotification) -> Bool ``` | yes |

Modified NSUserScriptTask

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSUserScriptTask.init(URL: NSURL, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL!, error error: NSErrorPointer) ``` |
| To | ``` init?(URL url: NSURL, error error: NSErrorPointer) ``` |

Modified NSUserScriptTask.executeWithCompletionHandler(NSUserScriptTaskCompletionHandler?)

|  | Declaration |
| --- | --- |
| From | ``` func executeWithCompletionHandler(_ handler: NSUserScriptTaskCompletionHandler!) ``` |
| To | ``` func executeWithCompletionHandler(_ handler: NSUserScriptTaskCompletionHandler?) ``` |

Modified NSUserScriptTask.scriptURL

|  | Declaration |
| --- | --- |
| From | ``` var scriptURL: NSURL! { get } ``` |
| To | ``` @NSCopying var scriptURL: NSURL { get } ``` |

Modified NSUserUnixTask

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSUserUnixTask.executeWithArguments([AnyObject]?, completionHandler: NSUserUnixTaskCompletionHandler?)

|  | Declaration |
| --- | --- |
| From | ``` func executeWithArguments(_ arguments: [AnyObject]!, completionHandler handler: NSUserUnixTaskCompletionHandler!) ``` |
| To | ``` func executeWithArguments(_ arguments: [AnyObject]?, completionHandler handler: NSUserUnixTaskCompletionHandler?) ``` |

Modified NSUserUnixTask.standardError

|  | Declaration |
| --- | --- |
| From | ``` var standardError: NSFileHandle! ``` |
| To | ``` var standardError: NSFileHandle? ``` |

Modified NSUserUnixTask.standardInput

|  | Declaration |
| --- | --- |
| From | ``` var standardInput: NSFileHandle! ``` |
| To | ``` var standardInput: NSFileHandle? ``` |

Modified NSUserUnixTask.standardOutput

|  | Declaration |
| --- | --- |
| From | ``` var standardOutput: NSFileHandle! ``` |
| To | ``` var standardOutput: NSFileHandle? ``` |

Modified NSValue.init(_: UnsafePointer<Void>, withObjCType: UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: ConstUnsafePointer<()>, withObjCType type: ConstUnsafePointer<Int8>) -> NSValue ``` |
| To | ``` init(_ value: UnsafePointer<Void>, withObjCType type: UnsafePointer<Int8>) -> NSValue ``` |

Modified NSValue.init(bytes: UnsafePointer<Void>, objCType: UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` init(bytes value: ConstUnsafePointer<()>, objCType type: ConstUnsafePointer<Int8>) ``` |
| To | ``` init(bytes value: UnsafePointer<Void>, objCType type: UnsafePointer<Int8>) ``` |

Modified NSValue.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init(coder aDecoder: NSCoder) ``` |

Modified NSValue.getValue(UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func getValue(_ value: UnsafePointer<()>) ``` |
| To | ``` func getValue(_ value: UnsafeMutablePointer<Void>) ``` |

Modified NSValue.isEqualToValue(NSValue) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToValue(_ value: NSValue!) -> Bool ``` |
| To | ``` func isEqualToValue(_ value: NSValue) -> Bool ``` |

Modified NSValue.init(nonretainedObject: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` init(nonretainedObject anObject: AnyObject!) -> NSValue ``` |
| To | ``` init(nonretainedObject anObject: AnyObject?) -> NSValue ``` |

Modified NSValue.nonretainedObjectValue

|  | Declaration |
| --- | --- |
| From | ``` var nonretainedObjectValue: AnyObject! { get } ``` |
| To | ``` var nonretainedObjectValue: AnyObject? { get } ``` |

Modified NSValue.objCType

|  | Declaration |
| --- | --- |
| From | ``` var objCType: ConstUnsafePointer<Int8> { get } ``` |
| To | ``` var objCType: UnsafePointer<Int8> { get } ``` |

Modified NSValue.init(pointer: UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` init(pointer pointer: ConstUnsafePointer<()>) -> NSValue ``` |
| To | ``` init(pointer pointer: UnsafePointer<Void>) -> NSValue ``` |

Modified NSValue.pointerValue() -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func pointerValue() -> UnsafePointer<()> ``` |
| To | ``` func pointerValue() -> UnsafeMutablePointer<Void> ``` |

Modified NSValueTransformer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified NSValueTransformer.init(forName: String)

|  | Declaration |
| --- | --- |
| From | ``` init(forName name: String!) -> NSValueTransformer ``` |
| To | ``` init?(forName name: String) -> NSValueTransformer ``` |

Modified NSValueTransformer.reverseTransformedValue(AnyObject?) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func reverseTransformedValue(_ value: AnyObject!) -> AnyObject! ``` |
| To | ``` func reverseTransformedValue(_ value: AnyObject?) -> AnyObject? ``` |

Modified NSValueTransformer.setValueTransformer(NSValueTransformer, forName: String) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setValueTransformer(_ transformer: NSValueTransformer!, forName name: String!) ``` |
| To | ``` class func setValueTransformer(_ transformer: NSValueTransformer, forName name: String) ``` |

Modified NSValueTransformer.transformedValue(AnyObject?) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func transformedValue(_ value: AnyObject!) -> AnyObject! ``` |
| To | ``` func transformedValue(_ value: AnyObject?) -> AnyObject? ``` |

Modified NSValueTransformer.transformedValueClass() -> AnyClass [class]

|  | Declaration |
| --- | --- |
| From | ``` class func transformedValueClass() -> AnyClass! ``` |
| To | ``` class func transformedValueClass() -> AnyClass ``` |

Modified NSValueTransformer.valueTransformerNames() -> [AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func valueTransformerNames() -> [AnyObject]! ``` |
| To | ``` class func valueTransformerNames() -> [AnyObject] ``` |

Modified NSVolumeEnumerationOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct NSVolumeEnumerationOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var SkipHiddenVolumes: NSVolumeEnumerationOptions { get }     static var ProduceFileReferenceURLs: NSVolumeEnumerationOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct NSVolumeEnumerationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var SkipHiddenVolumes: NSVolumeEnumerationOptions { get }     static var ProduceFileReferenceURLs: NSVolumeEnumerationOptions { get } } ``` | RawOptionSetType | OS X 10.6 |

Modified NSVolumeEnumerationOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSWhoseSpecifier.init(coder: NSCoder)

|  | Declaration |
| --- | --- |
| From | ``` init(coder inCoder: NSCoder!) ``` |
| To | ``` init?(coder inCoder: NSCoder) ``` |

Modified NSWhoseSpecifier.init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier, key: String, test: NSScriptWhoseTest)

|  | Declaration |
| --- | --- |
| From | ``` init(containerClassDescription classDesc: NSScriptClassDescription!, containerSpecifier container: NSScriptObjectSpecifier!, key property: String!, test test: NSScriptWhoseTest!) ``` |
| To | ``` init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier, key property: String, test test: NSScriptWhoseTest) ``` |

Modified NSWhoseSpecifier.test

|  | Declaration |
| --- | --- |
| From | ``` var test: NSScriptWhoseTest! ``` |
| To | ``` var test: NSScriptWhoseTest? ``` |

Modified NSXMLDTD.addChild(NSXMLNode)

|  | Declaration |
| --- | --- |
| From | ``` func addChild(_ child: NSXMLNode!) ``` |
| To | ``` func addChild(_ child: NSXMLNode) ``` |

Modified NSXMLDTD.attributeDeclarationForName(String, elementName: String) -> NSXMLDTDNode?

|  | Declaration |
| --- | --- |
| From | ``` func attributeDeclarationForName(_ name: String!, elementName elementName: String!) -> NSXMLDTDNode! ``` |
| To | ``` func attributeDeclarationForName(_ name: String, elementName elementName: String) -> NSXMLDTDNode? ``` |

Modified NSXMLDTD.init(contentsOfURL: NSURL, options: Int, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL url: NSURL!, options mask: Int, error error: NSErrorPointer) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL, options mask: Int, error error: NSErrorPointer) ``` |

Modified NSXMLDTD.init(data: NSData, options: Int, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData!, options mask: Int, error error: NSErrorPointer) ``` |
| To | ``` init?(data data: NSData, options mask: Int, error error: NSErrorPointer) ``` |

Modified NSXMLDTD.elementDeclarationForName(String) -> NSXMLDTDNode?

|  | Declaration |
| --- | --- |
| From | ``` func elementDeclarationForName(_ name: String!) -> NSXMLDTDNode! ``` |
| To | ``` func elementDeclarationForName(_ name: String) -> NSXMLDTDNode? ``` |

Modified NSXMLDTD.entityDeclarationForName(String) -> NSXMLDTDNode?

|  | Declaration |
| --- | --- |
| From | ``` func entityDeclarationForName(_ name: String!) -> NSXMLDTDNode! ``` |
| To | ``` func entityDeclarationForName(_ name: String) -> NSXMLDTDNode? ``` |

Modified NSXMLDTD.insertChild(NSXMLNode, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insertChild(_ child: NSXMLNode!, atIndex index: Int) ``` |
| To | ``` func insertChild(_ child: NSXMLNode, atIndex index: Int) ``` |

Modified NSXMLDTD.insertChildren([AnyObject], atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insertChildren(_ children: [AnyObject]!, atIndex index: Int) ``` |
| To | ``` func insertChildren(_ children: [AnyObject], atIndex index: Int) ``` |

Modified NSXMLDTD.notationDeclarationForName(String) -> NSXMLDTDNode?

|  | Declaration |
| --- | --- |
| From | ``` func notationDeclarationForName(_ name: String!) -> NSXMLDTDNode! ``` |
| To | ``` func notationDeclarationForName(_ name: String) -> NSXMLDTDNode? ``` |

Modified NSXMLDTD.predefinedEntityDeclarationForName(String) -> NSXMLDTDNode? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func predefinedEntityDeclarationForName(_ name: String!) -> NSXMLDTDNode! ``` |
| To | ``` class func predefinedEntityDeclarationForName(_ name: String) -> NSXMLDTDNode? ``` |

Modified NSXMLDTD.publicID

|  | Declaration |
| --- | --- |
| From | ``` var publicID: String! ``` |
| To | ``` var publicID: String? ``` |

Modified NSXMLDTD.replaceChildAtIndex(Int, withNode: NSXMLNode)

|  | Declaration |
| --- | --- |
| From | ``` func replaceChildAtIndex(_ index: Int, withNode node: NSXMLNode!) ``` |
| To | ``` func replaceChildAtIndex(_ index: Int, withNode node: NSXMLNode) ``` |

Modified NSXMLDTD.setChildren([AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` func setChildren(_ children: [AnyObject]!) ``` |
| To | ``` func setChildren(_ children: [AnyObject]?) ``` |

Modified NSXMLDTD.systemID

|  | Declaration |
| --- | --- |
| From | ``` var systemID: String! ``` |
| To | ``` var systemID: String? ``` |

Modified NSXMLDTDNode.init(XMLString: String)

|  | Declaration |
| --- | --- |
| From | ``` init(XMLString string: String!) ``` |
| To | ``` init?(XMLString string: String) ``` |

Modified NSXMLDTDNode.notationName

|  | Declaration |
| --- | --- |
| From | ``` var notationName: String! ``` |
| To | ``` var notationName: String? ``` |

Modified NSXMLDTDNode.publicID

|  | Declaration |
| --- | --- |
| From | ``` var publicID: String! ``` |
| To | ``` var publicID: String? ``` |

Modified NSXMLDTDNode.systemID

|  | Declaration |
| --- | --- |
| From | ``` var systemID: String! ``` |
| To | ``` var systemID: String? ``` |

Modified NSXMLDocument.DTD

|  | Declaration |
| --- | --- |
| From | ``` var DTD: NSXMLDTD! ``` |
| To | ``` @NSCopying var DTD: NSXMLDTD? ``` |

Modified NSXMLDocument.MIMEType

|  | Declaration |
| --- | --- |
| From | ``` var MIMEType: String! ``` |
| To | ``` var MIMEType: String? ``` |

Modified NSXMLDocument.XMLData

|  | Declaration |
| --- | --- |
| From | ``` var XMLData: NSData! { get } ``` |
| To | ``` @NSCopying var XMLData: NSData { get } ``` |

Modified NSXMLDocument.XMLDataWithOptions(Int) -> NSData

|  | Declaration |
| --- | --- |
| From | ``` func XMLDataWithOptions(_ options: Int) -> NSData! ``` |
| To | ``` func XMLDataWithOptions(_ options: Int) -> NSData ``` |

Modified NSXMLDocument.init(XMLString: String, options: Int, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(XMLString string: String!, options mask: Int, error error: NSErrorPointer) ``` |
| To | ``` convenience init?(XMLString string: String, options mask: Int, error error: NSErrorPointer) ``` |

Modified NSXMLDocument.addChild(NSXMLNode)

|  | Declaration |
| --- | --- |
| From | ``` func addChild(_ child: NSXMLNode!) ``` |
| To | ``` func addChild(_ child: NSXMLNode) ``` |

Modified NSXMLDocument.characterEncoding

|  | Declaration |
| --- | --- |
| From | ``` var characterEncoding: String! ``` |
| To | ``` var characterEncoding: String? ``` |

Modified NSXMLDocument.init(contentsOfURL: NSURL, options: Int, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL url: NSURL!, options mask: Int, error error: NSErrorPointer) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL, options mask: Int, error error: NSErrorPointer) ``` |

Modified NSXMLDocument.init(data: NSData, options: Int, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData!, options mask: Int, error error: NSErrorPointer) ``` |
| To | ``` init?(data data: NSData, options mask: Int, error error: NSErrorPointer) ``` |

Modified NSXMLDocument.insertChild(NSXMLNode, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insertChild(_ child: NSXMLNode!, atIndex index: Int) ``` |
| To | ``` func insertChild(_ child: NSXMLNode, atIndex index: Int) ``` |

Modified NSXMLDocument.insertChildren([AnyObject], atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insertChildren(_ children: [AnyObject]!, atIndex index: Int) ``` |
| To | ``` func insertChildren(_ children: [AnyObject], atIndex index: Int) ``` |

Modified NSXMLDocument.objectByApplyingXSLT(NSData, arguments:[NSObject: AnyObject]?, error: NSErrorPointer) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func objectByApplyingXSLT(_ xslt: NSData!, arguments arguments: [NSObject : AnyObject]!, error error: NSErrorPointer) -> AnyObject! ``` |
| To | ``` func objectByApplyingXSLT(_ xslt: NSData, arguments arguments: [NSObject : AnyObject]?, error error: NSErrorPointer) -> AnyObject? ``` |

Modified NSXMLDocument.objectByApplyingXSLTAtURL(NSURL, arguments:[NSObject: AnyObject]?, error: NSErrorPointer) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func objectByApplyingXSLTAtURL(_ xsltURL: NSURL!, arguments argument: [NSObject : AnyObject]!, error error: NSErrorPointer) -> AnyObject! ``` |
| To | ``` func objectByApplyingXSLTAtURL(_ xsltURL: NSURL, arguments argument: [NSObject : AnyObject]?, error error: NSErrorPointer) -> AnyObject? ``` |

Modified NSXMLDocument.objectByApplyingXSLTString(String, arguments:[NSObject: AnyObject]?, error: NSErrorPointer) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func objectByApplyingXSLTString(_ xslt: String!, arguments arguments: [NSObject : AnyObject]!, error error: NSErrorPointer) -> AnyObject! ``` |
| To | ``` func objectByApplyingXSLTString(_ xslt: String, arguments arguments: [NSObject : AnyObject]?, error error: NSErrorPointer) -> AnyObject? ``` |

Modified NSXMLDocument.replaceChildAtIndex(Int, withNode: NSXMLNode)

|  | Declaration |
| --- | --- |
| From | ``` func replaceChildAtIndex(_ index: Int, withNode node: NSXMLNode!) ``` |
| To | ``` func replaceChildAtIndex(_ index: Int, withNode node: NSXMLNode) ``` |

Modified NSXMLDocument.replacementClassForClass(AnyClass) -> AnyClass! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func replacementClassForClass(_ cls: AnyClass!) -> AnyClass! ``` |
| To | ``` class func replacementClassForClass(_ cls: AnyClass) -> AnyClass! ``` |

Modified NSXMLDocument.rootElement() -> NSXMLElement?

|  | Declaration |
| --- | --- |
| From | ``` func rootElement() -> NSXMLElement! ``` |
| To | ``` func rootElement() -> NSXMLElement? ``` |

Modified NSXMLDocument.init(rootElement: NSXMLElement!)

|  | Declaration |
| --- | --- |
| From | ``` init(rootElement element: NSXMLElement!) ``` |
| To | ``` init!(rootElement element: NSXMLElement!) ``` |

Modified NSXMLDocument.setChildren([AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` func setChildren(_ children: [AnyObject]!) ``` |
| To | ``` func setChildren(_ children: [AnyObject]?) ``` |

Modified NSXMLDocument.version

|  | Declaration |
| --- | --- |
| From | ``` var version: String! ``` |
| To | ``` var version: String? ``` |

Modified NSXMLElement.init(XMLString: String, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(XMLString string: String!, error error: NSErrorPointer) ``` |
| To | ``` init?(XMLString string: String, error error: NSErrorPointer) ``` |

Modified NSXMLElement.addAttribute(NSXMLNode)

|  | Declaration |
| --- | --- |
| From | ``` func addAttribute(_ attribute: NSXMLNode!) ``` |
| To | ``` func addAttribute(_ attribute: NSXMLNode) ``` |

Modified NSXMLElement.addChild(NSXMLNode)

|  | Declaration |
| --- | --- |
| From | ``` func addChild(_ child: NSXMLNode!) ``` |
| To | ``` func addChild(_ child: NSXMLNode) ``` |

Modified NSXMLElement.addNamespace(NSXMLNode)

|  | Declaration |
| --- | --- |
| From | ``` func addNamespace(_ aNamespace: NSXMLNode!) ``` |
| To | ``` func addNamespace(_ aNamespace: NSXMLNode) ``` |

Modified NSXMLElement.attributeForLocalName(String, URI: String?) -> NSXMLNode?

|  | Declaration |
| --- | --- |
| From | ``` func attributeForLocalName(_ localName: String!, URI URI: String!) -> NSXMLNode! ``` |
| To | ``` func attributeForLocalName(_ localName: String, URI URI: String?) -> NSXMLNode? ``` |

Modified NSXMLElement.attributeForName(String) -> NSXMLNode?

|  | Declaration |
| --- | --- |
| From | ``` func attributeForName(_ name: String!) -> NSXMLNode! ``` |
| To | ``` func attributeForName(_ name: String) -> NSXMLNode? ``` |

Modified NSXMLElement.attributes

|  | Declaration |
| --- | --- |
| From | ``` var attributes: [AnyObject]! ``` |
| To | ``` var attributes: [AnyObject]? ``` |

Modified NSXMLElement.elementsForLocalName(String, URI: String?) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func elementsForLocalName(_ localName: String!, URI URI: String!) -> [AnyObject]! ``` |
| To | ``` func elementsForLocalName(_ localName: String, URI URI: String?) -> [AnyObject] ``` |

Modified NSXMLElement.elementsForName(String) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func elementsForName(_ name: String!) -> [AnyObject]! ``` |
| To | ``` func elementsForName(_ name: String) -> [AnyObject] ``` |

Modified NSXMLElement.insertChild(NSXMLNode, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insertChild(_ child: NSXMLNode!, atIndex index: Int) ``` |
| To | ``` func insertChild(_ child: NSXMLNode, atIndex index: Int) ``` |

Modified NSXMLElement.insertChildren([AnyObject], atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insertChildren(_ children: [AnyObject]!, atIndex index: Int) ``` |
| To | ``` func insertChildren(_ children: [AnyObject], atIndex index: Int) ``` |

Modified NSXMLElement.init(name: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(name name: String!) ``` |
| To | ``` convenience init(name name: String) ``` |

Modified NSXMLElement.init(name: String, URI: String?)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!, URI URI: String!) ``` |
| To | ``` init(name name: String, URI URI: String?) ``` |

Modified NSXMLElement.init(name: String, stringValue: String?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(name name: String!, stringValue string: String!) ``` |
| To | ``` convenience init(name name: String, stringValue string: String?) ``` |

Modified NSXMLElement.namespaceForPrefix(String) -> NSXMLNode?

|  | Declaration |
| --- | --- |
| From | ``` func namespaceForPrefix(_ name: String!) -> NSXMLNode! ``` |
| To | ``` func namespaceForPrefix(_ name: String) -> NSXMLNode? ``` |

Modified NSXMLElement.namespaces

|  | Declaration |
| --- | --- |
| From | ``` var namespaces: [AnyObject]! ``` |
| To | ``` var namespaces: [AnyObject]? ``` |

Modified NSXMLElement.removeAttributeForName(String)

|  | Declaration |
| --- | --- |
| From | ``` func removeAttributeForName(_ name: String!) ``` |
| To | ``` func removeAttributeForName(_ name: String) ``` |

Modified NSXMLElement.removeNamespaceForPrefix(String)

|  | Declaration |
| --- | --- |
| From | ``` func removeNamespaceForPrefix(_ name: String!) ``` |
| To | ``` func removeNamespaceForPrefix(_ name: String) ``` |

Modified NSXMLElement.replaceChildAtIndex(Int, withNode: NSXMLNode)

|  | Declaration |
| --- | --- |
| From | ``` func replaceChildAtIndex(_ index: Int, withNode node: NSXMLNode!) ``` |
| To | ``` func replaceChildAtIndex(_ index: Int, withNode node: NSXMLNode) ``` |

Modified NSXMLElement.resolveNamespaceForName(String) -> NSXMLNode?

|  | Declaration |
| --- | --- |
| From | ``` func resolveNamespaceForName(_ name: String!) -> NSXMLNode! ``` |
| To | ``` func resolveNamespaceForName(_ name: String) -> NSXMLNode? ``` |

Modified NSXMLElement.resolvePrefixForNamespaceURI(String) -> String?

|  | Declaration |
| --- | --- |
| From | ``` func resolvePrefixForNamespaceURI(_ namespaceURI: String!) -> String! ``` |
| To | ``` func resolvePrefixForNamespaceURI(_ namespaceURI: String) -> String? ``` |

Modified NSXMLElement.setAttributesAsDictionary([NSObject: AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func setAttributesAsDictionary(_ attributes: [NSObject : AnyObject]!) ``` |
| To | ``` func setAttributesAsDictionary(_ attributes: [NSObject : AnyObject]) ``` |

Modified NSXMLElement.setAttributesWithDictionary([NSObject: AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func setAttributesWithDictionary(_ attributes: [NSObject : AnyObject]!) ``` |
| To | ``` func setAttributesWithDictionary(_ attributes: [NSObject : AnyObject]) ``` |

Modified NSXMLElement.setChildren([AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` func setChildren(_ children: [AnyObject]!) ``` |
| To | ``` func setChildren(_ children: [AnyObject]?) ``` |

Modified NSXMLNode.DTDNodeWithXMLString(String) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func DTDNodeWithXMLString(_ string: String!) -> AnyObject! ``` |
| To | ``` class func DTDNodeWithXMLString(_ string: String) -> AnyObject? ``` |

Modified NSXMLNode.URI

|  | Declaration |
| --- | --- |
| From | ``` var URI: String! ``` |
| To | ``` var URI: String? ``` |

Modified NSXMLNode.XMLString

|  | Declaration |
| --- | --- |
| From | ``` var XMLString: String! { get } ``` |
| To | ``` var XMLString: String { get } ``` |

Modified NSXMLNode.XMLStringWithOptions(Int) -> String

|  | Declaration |
| --- | --- |
| From | ``` func XMLStringWithOptions(_ options: Int) -> String! ``` |
| To | ``` func XMLStringWithOptions(_ options: Int) -> String ``` |

Modified NSXMLNode.attributeWithName(String!, URI: String!, stringValue: String!) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func attributeWithName(_ name: String!, URI URI: String!, stringValue stringValue: String!) -> AnyObject! ``` |
| To | ``` class func attributeWithName(_ name: String!, URI URI: String!, stringValue stringValue: String!) -> AnyObject? ``` |

Modified NSXMLNode.attributeWithName(String, stringValue: String) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func attributeWithName(_ name: String!, stringValue stringValue: String!) -> AnyObject! ``` |
| To | ``` class func attributeWithName(_ name: String, stringValue stringValue: String) -> AnyObject? ``` |

Modified NSXMLNode.canonicalXMLStringPreservingComments(Bool) -> String

|  | Declaration |
| --- | --- |
| From | ``` func canonicalXMLStringPreservingComments(_ comments: Bool) -> String! ``` |
| To | ``` func canonicalXMLStringPreservingComments(_ comments: Bool) -> String ``` |

Modified NSXMLNode.childAtIndex(Int) -> NSXMLNode?

|  | Declaration |
| --- | --- |
| From | ``` func childAtIndex(_ index: Int) -> NSXMLNode! ``` |
| To | ``` func childAtIndex(_ index: Int) -> NSXMLNode? ``` |

Modified NSXMLNode.children

|  | Declaration |
| --- | --- |
| From | ``` var children: [AnyObject]! { get } ``` |
| To | ``` var children: [AnyObject]? { get } ``` |

Modified NSXMLNode.commentWithStringValue(String!) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func commentWithStringValue(_ stringValue: String!) -> AnyObject! ``` |
| To | ``` class func commentWithStringValue(_ stringValue: String!) -> AnyObject? ``` |

Modified NSXMLNode.description

|  | Declaration |
| --- | --- |
| From | ``` var description: String! { get } ``` |
| To | ``` var description: String { get } ``` |

Modified NSXMLNode.document() -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func document() -> AnyObject! ``` |
| To | ``` class func document() -> AnyObject? ``` |

Modified NSXMLNode.documentWithRootElement(NSXMLElement!) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func documentWithRootElement(_ element: NSXMLElement!) -> AnyObject! ``` |
| To | ``` class func documentWithRootElement(_ element: NSXMLElement!) -> AnyObject? ``` |

Modified NSXMLNode.elementWithName(String!, URI: String!) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func elementWithName(_ name: String!, URI URI: String!) -> AnyObject! ``` |
| To | ``` class func elementWithName(_ name: String!, URI URI: String!) -> AnyObject? ``` |

Modified NSXMLNode.elementWithName(String!, children:[AnyObject]?, attributes:[AnyObject]?) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func elementWithName(_ name: String!, children children: [AnyObject]!, attributes attributes: [AnyObject]!) -> AnyObject! ``` |
| To | ``` class func elementWithName(_ name: String!, children children: [AnyObject]?, attributes attributes: [AnyObject]?) -> AnyObject? ``` |

Modified NSXMLNode.elementWithName(String!, stringValue: String!) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func elementWithName(_ name: String!, stringValue string: String!) -> AnyObject! ``` |
| To | ``` class func elementWithName(_ name: String!, stringValue string: String!) -> AnyObject? ``` |

Modified NSXMLNode.elementWithName(String) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func elementWithName(_ name: String!) -> AnyObject! ``` |
| To | ``` class func elementWithName(_ name: String) -> AnyObject? ``` |

Modified NSXMLNode.localName

|  | Declaration |
| --- | --- |
| From | ``` var localName: String! { get } ``` |
| To | ``` var localName: String? { get } ``` |

Modified NSXMLNode.localNameForName(String) -> String! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func localNameForName(_ name: String!) -> String! ``` |
| To | ``` class func localNameForName(_ name: String) -> String! ``` |

Modified NSXMLNode.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified NSXMLNode.namespaceWithName(String, stringValue: String) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func namespaceWithName(_ name: String!, stringValue stringValue: String!) -> AnyObject! ``` |
| To | ``` class func namespaceWithName(_ name: String, stringValue stringValue: String) -> AnyObject? ``` |

Modified NSXMLNode.nextNode

|  | Declaration |
| --- | --- |
| From | ``` var nextNode: NSXMLNode! { get } ``` |
| To | ``` @NSCopying var nextNode: NSXMLNode? { get } ``` |

Modified NSXMLNode.nextSibling

|  | Declaration |
| --- | --- |
| From | ``` var nextSibling: NSXMLNode! { get } ``` |
| To | ``` @NSCopying var nextSibling: NSXMLNode? { get } ``` |

Modified NSXMLNode.nodesForXPath(String, error: NSErrorPointer) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func nodesForXPath(_ xpath: String!, error error: NSErrorPointer) -> [AnyObject]! ``` |
| To | ``` func nodesForXPath(_ xpath: String, error error: NSErrorPointer) -> [AnyObject]? ``` |

Modified NSXMLNode.objectValue

|  | Declaration |
| --- | --- |
| From | ``` var objectValue: AnyObject! ``` |
| To | ``` var objectValue: AnyObject? ``` |

Modified NSXMLNode.objectsForXQuery(String, constants:[NSObject: AnyObject]!, error: NSErrorPointer) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func objectsForXQuery(_ xquery: String!, constants constants: [NSObject : AnyObject]!, error error: NSErrorPointer) -> [AnyObject]! ``` |
| To | ``` func objectsForXQuery(_ xquery: String, constants constants: [NSObject : AnyObject]!, error error: NSErrorPointer) -> [AnyObject]? ``` |

Modified NSXMLNode.objectsForXQuery(String, error: NSErrorPointer) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func objectsForXQuery(_ xquery: String!, error error: NSErrorPointer) -> [AnyObject]! ``` |
| To | ``` func objectsForXQuery(_ xquery: String, error error: NSErrorPointer) -> [AnyObject]? ``` |

Modified NSXMLNode.parent

|  | Declaration |
| --- | --- |
| From | ``` var parent: NSXMLNode! { get } ``` |
| To | ``` @NSCopying var parent: NSXMLNode? { get } ``` |

Modified NSXMLNode.predefinedNamespaceForPrefix(String) -> NSXMLNode? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func predefinedNamespaceForPrefix(_ name: String!) -> NSXMLNode! ``` |
| To | ``` class func predefinedNamespaceForPrefix(_ name: String) -> NSXMLNode? ``` |

Modified NSXMLNode.prefix

|  | Declaration |
| --- | --- |
| From | ``` var prefix: String! { get } ``` |
| To | ``` var prefix: String? { get } ``` |

Modified NSXMLNode.prefixForName(String) -> String? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func prefixForName(_ name: String!) -> String! ``` |
| To | ``` class func prefixForName(_ name: String) -> String? ``` |

Modified NSXMLNode.previousNode

|  | Declaration |
| --- | --- |
| From | ``` var previousNode: NSXMLNode! { get } ``` |
| To | ``` @NSCopying var previousNode: NSXMLNode? { get } ``` |

Modified NSXMLNode.previousSibling

|  | Declaration |
| --- | --- |
| From | ``` var previousSibling: NSXMLNode! { get } ``` |
| To | ``` @NSCopying var previousSibling: NSXMLNode? { get } ``` |

Modified NSXMLNode.processingInstructionWithName(String, stringValue: String) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func processingInstructionWithName(_ name: String!, stringValue stringValue: String!) -> AnyObject! ``` |
| To | ``` class func processingInstructionWithName(_ name: String, stringValue stringValue: String) -> AnyObject? ``` |

Modified NSXMLNode.rootDocument

|  | Declaration |
| --- | --- |
| From | ``` var rootDocument: NSXMLDocument! { get } ``` |
| To | ``` var rootDocument: NSXMLDocument? { get } ``` |

Modified NSXMLNode.setStringValue(String, resolvingEntities: Bool)

|  | Declaration |
| --- | --- |
| From | ``` func setStringValue(_ string: String!, resolvingEntities resolve: Bool) ``` |
| To | ``` func setStringValue(_ string: String, resolvingEntities resolve: Bool) ``` |

Modified NSXMLNode.stringValue

|  | Declaration |
| --- | --- |
| From | ``` var stringValue: String! ``` |
| To | ``` var stringValue: String? ``` |

Modified NSXMLNode.textWithStringValue(String!) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func textWithStringValue(_ stringValue: String!) -> AnyObject! ``` |
| To | ``` class func textWithStringValue(_ stringValue: String!) -> AnyObject? ``` |

Modified NSXMLParser.init(contentsOfURL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL url: NSURL!) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL!) ``` |

Modified NSXMLParser.init(data: NSData)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(data data: NSData!) ``` | OS X 10.10 |
| To | ``` init(data data: NSData) ``` | OS X 10.10.3 |

Modified NSXMLParser.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: NSXMLParserDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: NSXMLParserDelegate? ``` |

Modified NSXMLParser.parserError

|  | Declaration |
| --- | --- |
| From | ``` var parserError: NSError! { get } ``` |
| To | ``` @NSCopying var parserError: NSError? { get } ``` |

Modified NSXMLParser.publicID

|  | Declaration |
| --- | --- |
| From | ``` var publicID: String! { get } ``` |
| To | ``` var publicID: String? { get } ``` |

Modified NSXMLParser.init(stream: NSInputStream)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(stream stream: NSInputStream!) ``` | OS X 10.10 |
| To | ``` convenience init(stream stream: NSInputStream) ``` | OS X 10.7 |

Modified NSXMLParser.systemID

|  | Declaration |
| --- | --- |
| From | ``` var systemID: String! { get } ``` |
| To | ``` var systemID: String? { get } ``` |

Modified NSXMLParserDelegate.parser(NSXMLParser, didEndElement: String, namespaceURI: String?, qualifiedName: String?)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, didEndElement elementName: String!, namespaceURI namespaceURI: String!, qualifiedName qName: String!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, didEndElement elementName: String, namespaceURI namespaceURI: String?, qualifiedName qName: String?) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, didEndMappingPrefix: String)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, didEndMappingPrefix prefix: String!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, didEndMappingPrefix prefix: String) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, didStartElement: String, namespaceURI: String?, qualifiedName: String?, attributes:[NSObject: AnyObject])

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, didStartElement elementName: String!, namespaceURI namespaceURI: String!, qualifiedName qName: String!, attributes attributeDict: [NSObject : AnyObject]!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, didStartElement elementName: String, namespaceURI namespaceURI: String?, qualifiedName qName: String?, attributes attributeDict: [NSObject : AnyObject]) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, didStartMappingPrefix: String, toURI: String)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, didStartMappingPrefix prefix: String!, toURI namespaceURI: String!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, didStartMappingPrefix prefix: String, toURI namespaceURI: String) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundAttributeDeclarationWithName: String, forElement: String, type: String?, defaultValue: String?)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundAttributeDeclarationWithName attributeName: String!, forElement elementName: String!, type type: String!, defaultValue defaultValue: String!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, foundAttributeDeclarationWithName attributeName: String, forElement elementName: String, type type: String?, defaultValue defaultValue: String?) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundCDATA: NSData)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundCDATA CDATABlock: NSData!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, foundCDATA CDATABlock: NSData) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundCharacters: String?)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundCharacters string: String!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, foundCharacters string: String?) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundComment: String?)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundComment comment: String!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, foundComment comment: String?) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundElementDeclarationWithName: String, model: String)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundElementDeclarationWithName elementName: String!, model model: String!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, foundElementDeclarationWithName elementName: String, model model: String) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundExternalEntityDeclarationWithName: String, publicID: String?, systemID: String?)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundExternalEntityDeclarationWithName name: String!, publicID publicID: String!, systemID systemID: String!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, foundExternalEntityDeclarationWithName name: String, publicID publicID: String?, systemID systemID: String?) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundIgnorableWhitespace: String)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundIgnorableWhitespace whitespaceString: String!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, foundIgnorableWhitespace whitespaceString: String) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundInternalEntityDeclarationWithName: String, value: String?)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundInternalEntityDeclarationWithName name: String!, value value: String!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, foundInternalEntityDeclarationWithName name: String, value value: String?) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundNotationDeclarationWithName: String, publicID: String?, systemID: String?)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundNotationDeclarationWithName name: String!, publicID publicID: String!, systemID systemID: String!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, foundNotationDeclarationWithName name: String, publicID publicID: String?, systemID systemID: String?) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundProcessingInstructionWithTarget: String, data: String?)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundProcessingInstructionWithTarget target: String!, data data: String!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, foundProcessingInstructionWithTarget target: String, data data: String?) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, foundUnparsedEntityDeclarationWithName: String, publicID: String?, systemID: String?, notationName: String?)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, foundUnparsedEntityDeclarationWithName name: String!, publicID publicID: String!, systemID systemID: String!, notationName notationName: String!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, foundUnparsedEntityDeclarationWithName name: String, publicID publicID: String?, systemID systemID: String?, notationName notationName: String?) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, parseErrorOccurred: NSError)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, parseErrorOccurred parseError: NSError!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, parseErrorOccurred parseError: NSError) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, resolveExternalEntityName: String, systemID: String?) -> NSData?

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, resolveExternalEntityName name: String!, systemID systemID: String!) -> NSData! ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, resolveExternalEntityName name: String, systemID systemID: String?) -> NSData? ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parser(NSXMLParser, validationErrorOccurred: NSError)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parser(_ parser: NSXMLParser!, validationErrorOccurred validationError: NSError!) ``` | OS X 10.10 | -- |
| To | ``` optional func parser(_ parser: NSXMLParser, validationErrorOccurred validationError: NSError) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parserDidEndDocument(NSXMLParser)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parserDidEndDocument(_ parser: NSXMLParser!) ``` | OS X 10.10 | -- |
| To | ``` optional func parserDidEndDocument(_ parser: NSXMLParser) ``` | OS X 10.10.3 | yes |

Modified NSXMLParserDelegate.parserDidStartDocument(NSXMLParser)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func parserDidStartDocument(_ parser: NSXMLParser!) ``` | OS X 10.10 | -- |
| To | ``` optional func parserDidStartDocument(_ parser: NSXMLParser) ``` | OS X 10.10.3 | yes |

Modified NSXPCConnection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSXPCConnection.endpoint

|  | Declaration |
| --- | --- |
| From | ``` var endpoint: NSXPCListenerEndpoint! { get } ``` |
| To | ``` var endpoint: NSXPCListenerEndpoint { get } ``` |

Modified NSXPCConnection.exportedInterface

|  | Declaration |
| --- | --- |
| From | ``` var exportedInterface: NSXPCInterface! ``` |
| To | ``` var exportedInterface: NSXPCInterface? ``` |

Modified NSXPCConnection.exportedObject

|  | Declaration |
| --- | --- |
| From | ``` var exportedObject: AnyObject! ``` |
| To | ``` var exportedObject: AnyObject? ``` |

Modified NSXPCConnection.interruptionHandler

|  | Declaration |
| --- | --- |
| From | ``` var interruptionHandler: (() -> Void)! ``` |
| To | ``` var interruptionHandler: (() -> Void)? ``` |

Modified NSXPCConnection.invalidationHandler

|  | Declaration |
| --- | --- |
| From | ``` var invalidationHandler: (() -> Void)! ``` |
| To | ``` var invalidationHandler: (() -> Void)? ``` |

Modified NSXPCConnection.init(listenerEndpoint: NSXPCListenerEndpoint)

|  | Declaration |
| --- | --- |
| From | ``` init(listenerEndpoint endpoint: NSXPCListenerEndpoint!) ``` |
| To | ``` init(listenerEndpoint endpoint: NSXPCListenerEndpoint) ``` |

Modified NSXPCConnection.init(machServiceName: String, options: NSXPCConnectionOptions)

|  | Declaration |
| --- | --- |
| From | ``` init(machServiceName name: String!, options options: NSXPCConnectionOptions) ``` |
| To | ``` init(machServiceName name: String, options options: NSXPCConnectionOptions) ``` |

Modified NSXPCConnection.remoteObjectInterface

|  | Declaration |
| --- | --- |
| From | ``` var remoteObjectInterface: NSXPCInterface! ``` |
| To | ``` var remoteObjectInterface: NSXPCInterface? ``` |

Modified NSXPCConnection.remoteObjectProxy

|  | Declaration |
| --- | --- |
| From | ``` var remoteObjectProxy: AnyObject! { get } ``` |
| To | ``` var remoteObjectProxy: AnyObject { get } ``` |

Modified NSXPCConnection.remoteObjectProxyWithErrorHandler((NSError!) -> Void) -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func remoteObjectProxyWithErrorHandler(_ handler: ((NSError!) -> Void)!) -> AnyObject! ``` |
| To | ``` func remoteObjectProxyWithErrorHandler(_ handler: (NSError!) -> Void) -> AnyObject ``` |

Modified NSXPCConnection.serviceName

|  | Declaration |
| --- | --- |
| From | ``` var serviceName: String! { get } ``` |
| To | ``` var serviceName: String? { get } ``` |

Modified NSXPCConnection.init(serviceName: String)

|  | Declaration |
| --- | --- |
| From | ``` init(serviceName serviceName: String!) ``` |
| To | ``` init(serviceName serviceName: String) ``` |

Modified NSXPCConnectionOptions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct NSXPCConnectionOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Privileged: NSXPCConnectionOptions { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct NSXPCConnectionOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Privileged: NSXPCConnectionOptions { get } } ``` | RawOptionSetType | OS X 10.8 |

Modified NSXPCConnectionOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSXPCInterface

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSXPCInterface.classesForSelector(Selector, argumentIndex: Int, ofReply: Bool) -> Set<NSObject>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func classesForSelector(_ sel: Selector, argumentIndex arg: Int, ofReply ofReply: Bool) -> NSSet! ``` | OS X 10.10 |
| To | ``` func classesForSelector(_ sel: Selector, argumentIndex arg: Int, ofReply ofReply: Bool) -> Set<NSObject> ``` | OS X 10.10.3 |

Modified NSXPCInterface.interfaceForSelector(Selector, argumentIndex: Int, ofReply: Bool) -> NSXPCInterface?

|  | Declaration |
| --- | --- |
| From | ``` func interfaceForSelector(_ sel: Selector, argumentIndex arg: Int, ofReply ofReply: Bool) -> NSXPCInterface! ``` |
| To | ``` func interfaceForSelector(_ sel: Selector, argumentIndex arg: Int, ofReply ofReply: Bool) -> NSXPCInterface? ``` |

Modified NSXPCInterface.protocol

|  | Declaration |
| --- | --- |
| From | ``` var `protocol`: Protocol! ``` |
| To | ``` unowned(unsafe) var `protocol`: Protocol ``` |

Modified NSXPCInterface.init(protocol: Protocol)

|  | Name | Declaration |
| --- | --- | --- |
| From | init(protocol:) | ``` init(`protocol` `protocol`: Protocol!) -> NSXPCInterface ``` |
| To | init(withProtocol:) | ``` init(withProtocol `protocol`: Protocol) -> NSXPCInterface ``` |

Modified NSXPCInterface.setClasses(Set<NSObject>, forSelector: Selector, argumentIndex: Int, ofReply: Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setClasses(_ classes: NSSet!, forSelector sel: Selector, argumentIndex arg: Int, ofReply ofReply: Bool) ``` | OS X 10.10 |
| To | ``` func setClasses(_ classes: Set<NSObject>, forSelector sel: Selector, argumentIndex arg: Int, ofReply ofReply: Bool) ``` | OS X 10.10.3 |

Modified NSXPCInterface.setInterface(NSXPCInterface, forSelector: Selector, argumentIndex: Int, ofReply: Bool)

|  | Declaration |
| --- | --- |
| From | ``` func setInterface(_ ifc: NSXPCInterface!, forSelector sel: Selector, argumentIndex arg: Int, ofReply ofReply: Bool) ``` |
| To | ``` func setInterface(_ ifc: NSXPCInterface, forSelector sel: Selector, argumentIndex arg: Int, ofReply ofReply: Bool) ``` |

Modified NSXPCListener

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSXPCListener.anonymousListener() -> NSXPCListener [class]

|  | Declaration |
| --- | --- |
| From | ``` class func anonymousListener() -> NSXPCListener! ``` |
| To | ``` class func anonymousListener() -> NSXPCListener ``` |

Modified NSXPCListener.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: NSXPCListenerDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: NSXPCListenerDelegate? ``` |

Modified NSXPCListener.endpoint

|  | Declaration |
| --- | --- |
| From | ``` var endpoint: NSXPCListenerEndpoint! { get } ``` |
| To | ``` var endpoint: NSXPCListenerEndpoint { get } ``` |

Modified NSXPCListener.init(machServiceName: String)

|  | Declaration |
| --- | --- |
| From | ``` init(machServiceName name: String!) ``` |
| To | ``` init(machServiceName name: String) ``` |

Modified NSXPCListener.serviceListener() -> NSXPCListener [class]

|  | Declaration |
| --- | --- |
| From | ``` class func serviceListener() -> NSXPCListener! ``` |
| To | ``` class func serviceListener() -> NSXPCListener ``` |

Modified NSXPCListenerDelegate.listener(NSXPCListener, shouldAcceptNewConnection: NSXPCConnection) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func listener(_ listener: NSXPCListener!, shouldAcceptNewConnection newConnection: NSXPCConnection!) -> Bool ``` | -- |
| To | ``` optional func listener(_ listener: NSXPCListener, shouldAcceptNewConnection newConnection: NSXPCConnection) -> Bool ``` | yes |

Modified NSXPCListenerEndpoint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSXPCProxyCreating.remoteObjectProxy() -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func remoteObjectProxy() -> AnyObject! ``` |
| To | ``` func remoteObjectProxy() -> AnyObject ``` |

Modified NSXPCProxyCreating.remoteObjectProxyWithErrorHandler((NSError!) -> Void) -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func remoteObjectProxyWithErrorHandler(_ handler: ((NSError!) -> Void)!) -> AnyObject! ``` |
| To | ``` func remoteObjectProxyWithErrorHandler(_ handler: (NSError!) -> Void) -> AnyObject ``` |

Modified NSZone [struct]

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct NSZone : NilLiteralConvertible {     var pointer: COpaquePointer     init()     static func convertFromNilLiteral() -> NSZone } ``` | Foundation |
| To | ``` struct NSZone : NilLiteralConvertible {     var pointer: COpaquePointer     init()     init(nilLiteral nilLiteral: ()) } ``` | ObjectiveC |

Modified NSZone.init()

|  | Module |
| --- | --- |
| From | Foundation |
| To | ObjectiveC |

Modified NSZone.pointer

|  | Module |
| --- | --- |
| From | Foundation |
| To | ObjectiveC |

Modified NSAllocateCollectable(Int, Int) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func NSAllocateCollectable(_ size: Int, _ options: Int) -> UnsafePointer<()> ``` |
| To | ``` func NSAllocateCollectable(_ size: Int, _ options: Int) -> UnsafeMutablePointer<Void> ``` |

Modified NSAllocateMemoryPages(Int) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func NSAllocateMemoryPages(_ bytes: Int) -> UnsafePointer<()> ``` |
| To | ``` func NSAllocateMemoryPages(_ bytes: Int) -> UnsafeMutablePointer<Void> ``` |

Modified NSAppleEventManagerWillProcessFirstEventNotification

|  | Declaration |
| --- | --- |
| From | ``` var NSAppleEventManagerWillProcessFirstEventNotification: NSString! ``` |
| To | ``` let NSAppleEventManagerWillProcessFirstEventNotification: String ``` |

Modified NSAppleScriptErrorAppName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSAppleScriptErrorAppName: NSString! ``` | OS X 10.10 |
| To | ``` let NSAppleScriptErrorAppName: String ``` | OS X 10.2 |

Modified NSAppleScriptErrorBriefMessage

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSAppleScriptErrorBriefMessage: NSString! ``` | OS X 10.10 |
| To | ``` let NSAppleScriptErrorBriefMessage: String ``` | OS X 10.2 |

Modified NSAppleScriptErrorMessage

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSAppleScriptErrorMessage: NSString! ``` | OS X 10.10 |
| To | ``` let NSAppleScriptErrorMessage: String ``` | OS X 10.2 |

Modified NSAppleScriptErrorNumber

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSAppleScriptErrorNumber: NSString! ``` | OS X 10.10 |
| To | ``` let NSAppleScriptErrorNumber: String ``` | OS X 10.2 |

Modified NSAppleScriptErrorRange

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSAppleScriptErrorRange: NSString! ``` | OS X 10.10 |
| To | ``` let NSAppleScriptErrorRange: String ``` | OS X 10.2 |

Modified NSArgumentDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSArgumentDomain: NSString! ``` |
| To | ``` let NSArgumentDomain: String ``` |

Modified NSAssertionHandlerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSAssertionHandlerKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSAssertionHandlerKey: String ``` | OS X 10.6 |

Modified NSAverageKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSAverageKeyValueOperator: NSString! ``` |
| To | ``` let NSAverageKeyValueOperator: String ``` |

Modified NSBuddhistCalendar

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let NSBuddhistCalendar: NSString! ``` | OS X 10.10 | -- |
| To | ``` let NSBuddhistCalendar: String ``` | OS X 10.4 | OS X 10.10 |

Modified NSBundleDidLoadNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSBundleDidLoadNotification: NSString! ``` |
| To | ``` let NSBundleDidLoadNotification: String ``` |

Modified NSCalendarDayChangedNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarDayChangedNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarDayChangedNotification: String ``` | OS X 10.9 |

Modified NSCalendarIdentifierBuddhist

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarIdentifierBuddhist: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarIdentifierBuddhist: String ``` | OS X 10.6 |

Modified NSCalendarIdentifierChinese

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarIdentifierChinese: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarIdentifierChinese: String ``` | OS X 10.6 |

Modified NSCalendarIdentifierCoptic

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarIdentifierCoptic: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarIdentifierCoptic: String ``` | OS X 10.6 |

Modified NSCalendarIdentifierEthiopicAmeteAlem

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarIdentifierEthiopicAmeteAlem: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarIdentifierEthiopicAmeteAlem: String ``` | OS X 10.6 |

Modified NSCalendarIdentifierEthiopicAmeteMihret

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarIdentifierEthiopicAmeteMihret: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarIdentifierEthiopicAmeteMihret: String ``` | OS X 10.6 |

Modified NSCalendarIdentifierGregorian

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarIdentifierGregorian: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarIdentifierGregorian: String ``` | OS X 10.6 |

Modified NSCalendarIdentifierHebrew

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarIdentifierHebrew: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarIdentifierHebrew: String ``` | OS X 10.6 |

Modified NSCalendarIdentifierISO8601

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarIdentifierISO8601: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarIdentifierISO8601: String ``` | OS X 10.6 |

Modified NSCalendarIdentifierIndian

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarIdentifierIndian: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarIdentifierIndian: String ``` | OS X 10.6 |

Modified NSCalendarIdentifierIslamic

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarIdentifierIslamic: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarIdentifierIslamic: String ``` | OS X 10.6 |

Modified NSCalendarIdentifierIslamicCivil

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarIdentifierIslamicCivil: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarIdentifierIslamicCivil: String ``` | OS X 10.6 |

Modified NSCalendarIdentifierIslamicTabular

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierIslamicTabular: NSString! ``` |
| To | ``` let NSCalendarIdentifierIslamicTabular: String ``` |

Modified NSCalendarIdentifierIslamicUmmAlQura

|  | Declaration |
| --- | --- |
| From | ``` let NSCalendarIdentifierIslamicUmmAlQura: NSString! ``` |
| To | ``` let NSCalendarIdentifierIslamicUmmAlQura: String ``` |

Modified NSCalendarIdentifierJapanese

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarIdentifierJapanese: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarIdentifierJapanese: String ``` | OS X 10.6 |

Modified NSCalendarIdentifierPersian

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarIdentifierPersian: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarIdentifierPersian: String ``` | OS X 10.6 |

Modified NSCalendarIdentifierRepublicOfChina

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCalendarIdentifierRepublicOfChina: NSString! ``` | OS X 10.10 |
| To | ``` let NSCalendarIdentifierRepublicOfChina: String ``` | OS X 10.6 |

Modified NSCharacterConversionException

|  | Declaration |
| --- | --- |
| From | ``` let NSCharacterConversionException: NSString! ``` |
| To | ``` let NSCharacterConversionException: String ``` |

Modified NSChineseCalendar

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let NSChineseCalendar: NSString! ``` | OS X 10.10 | -- |
| To | ``` let NSChineseCalendar: String ``` | OS X 10.4 | OS X 10.10 |

Modified NSClassDescriptionNeededForClassNotification

|  | Declaration |
| --- | --- |
| From | ``` var NSClassDescriptionNeededForClassNotification: NSString! ``` |
| To | ``` let NSClassDescriptionNeededForClassNotification: String ``` |

Modified NSCocoaErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSCocoaErrorDomain: NSString! ``` |
| To | ``` let NSCocoaErrorDomain: String ``` |

Modified NSCopyMemoryPages(UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func NSCopyMemoryPages(_ source: ConstUnsafePointer<()>, _ dest: UnsafePointer<()>, _ bytes: Int) ``` |
| To | ``` func NSCopyMemoryPages(_ source: UnsafePointer<Void>, _ dest: UnsafeMutablePointer<Void>, _ bytes: Int) ``` |

Modified NSCountKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSCountKeyValueOperator: NSString! ``` |
| To | ``` let NSCountKeyValueOperator: String ``` |

Modified NSCurrentLocaleDidChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSCurrentLocaleDidChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSCurrentLocaleDidChangeNotification: String ``` | OS X 10.5 |

Modified NSDeallocateMemoryPages(UnsafeMutablePointer<Void>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func NSDeallocateMemoryPages(_ ptr: UnsafePointer<()>, _ bytes: Int) ``` |
| To | ``` func NSDeallocateMemoryPages(_ ptr: UnsafeMutablePointer<Void>, _ bytes: Int) ``` |

Modified NSDecimalAdd(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>, UnsafePointer<NSDecimal>, NSRoundingMode) -> NSCalculationError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalAdd(_ result: COpaquePointer, _ leftOperand: COpaquePointer, _ rightOperand: COpaquePointer, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | OS X 10.10 |
| To | ``` func NSDecimalAdd(_ result: UnsafeMutablePointer<NSDecimal>, _ leftOperand: UnsafePointer<NSDecimal>, _ rightOperand: UnsafePointer<NSDecimal>, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | OS X 10.10.3 |

Modified NSDecimalCompact(UnsafeMutablePointer<NSDecimal>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalCompact(_ number: COpaquePointer) ``` | OS X 10.10 |
| To | ``` func NSDecimalCompact(_ number: UnsafeMutablePointer<NSDecimal>) ``` | OS X 10.10.3 |

Modified NSDecimalCompare(UnsafePointer<NSDecimal>, UnsafePointer<NSDecimal>) -> NSComparisonResult

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalCompare(_ leftOperand: COpaquePointer, _ rightOperand: COpaquePointer) -> NSComparisonResult ``` | OS X 10.10 |
| To | ``` func NSDecimalCompare(_ leftOperand: UnsafePointer<NSDecimal>, _ rightOperand: UnsafePointer<NSDecimal>) -> NSComparisonResult ``` | OS X 10.10.3 |

Modified NSDecimalCopy(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalCopy(_ destination: COpaquePointer, _ source: COpaquePointer) ``` | OS X 10.10 |
| To | ``` func NSDecimalCopy(_ destination: UnsafeMutablePointer<NSDecimal>, _ source: UnsafePointer<NSDecimal>) ``` | OS X 10.10.3 |

Modified NSDecimalDivide(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>, UnsafePointer<NSDecimal>, NSRoundingMode) -> NSCalculationError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalDivide(_ result: COpaquePointer, _ leftOperand: COpaquePointer, _ rightOperand: COpaquePointer, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | OS X 10.10 |
| To | ``` func NSDecimalDivide(_ result: UnsafeMutablePointer<NSDecimal>, _ leftOperand: UnsafePointer<NSDecimal>, _ rightOperand: UnsafePointer<NSDecimal>, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | OS X 10.10.3 |

Modified NSDecimalIsNotANumber(UnsafePointer<NSDecimal>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalIsNotANumber(_ dcm: COpaquePointer) -> Bool ``` | OS X 10.10 |
| To | ``` func NSDecimalIsNotANumber(_ dcm: UnsafePointer<NSDecimal>) -> Bool ``` | OS X 10.10.3 |

Modified NSDecimalMultiply(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>, UnsafePointer<NSDecimal>, NSRoundingMode) -> NSCalculationError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalMultiply(_ result: COpaquePointer, _ leftOperand: COpaquePointer, _ rightOperand: COpaquePointer, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | OS X 10.10 |
| To | ``` func NSDecimalMultiply(_ result: UnsafeMutablePointer<NSDecimal>, _ leftOperand: UnsafePointer<NSDecimal>, _ rightOperand: UnsafePointer<NSDecimal>, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | OS X 10.10.3 |

Modified NSDecimalMultiplyByPowerOf10(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>, Int16, NSRoundingMode) -> NSCalculationError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalMultiplyByPowerOf10(_ result: COpaquePointer, _ number: COpaquePointer, _ power: Int16, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | OS X 10.10 |
| To | ``` func NSDecimalMultiplyByPowerOf10(_ result: UnsafeMutablePointer<NSDecimal>, _ number: UnsafePointer<NSDecimal>, _ power: Int16, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | OS X 10.10.3 |

Modified NSDecimalNormalize(UnsafeMutablePointer<NSDecimal>, UnsafeMutablePointer<NSDecimal>, NSRoundingMode) -> NSCalculationError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalNormalize(_ number1: COpaquePointer, _ number2: COpaquePointer, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | OS X 10.10 |
| To | ``` func NSDecimalNormalize(_ number1: UnsafeMutablePointer<NSDecimal>, _ number2: UnsafeMutablePointer<NSDecimal>, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | OS X 10.10.3 |

Modified NSDecimalNumberDivideByZeroException

|  | Declaration |
| --- | --- |
| From | ``` let NSDecimalNumberDivideByZeroException: NSString! ``` |
| To | ``` let NSDecimalNumberDivideByZeroException: String ``` |

Modified NSDecimalNumberExactnessException

|  | Declaration |
| --- | --- |
| From | ``` let NSDecimalNumberExactnessException: NSString! ``` |
| To | ``` let NSDecimalNumberExactnessException: String ``` |

Modified NSDecimalNumberOverflowException

|  | Declaration |
| --- | --- |
| From | ``` let NSDecimalNumberOverflowException: NSString! ``` |
| To | ``` let NSDecimalNumberOverflowException: String ``` |

Modified NSDecimalNumberUnderflowException

|  | Declaration |
| --- | --- |
| From | ``` let NSDecimalNumberUnderflowException: NSString! ``` |
| To | ``` let NSDecimalNumberUnderflowException: String ``` |

Modified NSDecimalPower(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>, Int, NSRoundingMode) -> NSCalculationError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalPower(_ result: COpaquePointer, _ number: COpaquePointer, _ power: Int, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | OS X 10.10 |
| To | ``` func NSDecimalPower(_ result: UnsafeMutablePointer<NSDecimal>, _ number: UnsafePointer<NSDecimal>, _ power: Int, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | OS X 10.10.3 |

Modified NSDecimalRound(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>, Int, NSRoundingMode)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalRound(_ result: COpaquePointer, _ number: COpaquePointer, _ scale: Int, _ roundingMode: NSRoundingMode) ``` | OS X 10.10 |
| To | ``` func NSDecimalRound(_ result: UnsafeMutablePointer<NSDecimal>, _ number: UnsafePointer<NSDecimal>, _ scale: Int, _ roundingMode: NSRoundingMode) ``` | OS X 10.10.3 |

Modified NSDecimalString(UnsafePointer<NSDecimal>, AnyObject!) -> String!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalString(_ dcm: COpaquePointer, _ locale: AnyObject!) -> String! ``` | OS X 10.10 |
| To | ``` func NSDecimalString(_ dcm: UnsafePointer<NSDecimal>, _ locale: AnyObject!) -> String! ``` | OS X 10.10.3 |

Modified NSDecimalSubtract(UnsafeMutablePointer<NSDecimal>, UnsafePointer<NSDecimal>, UnsafePointer<NSDecimal>, NSRoundingMode) -> NSCalculationError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NSDecimalSubtract(_ result: COpaquePointer, _ leftOperand: COpaquePointer, _ rightOperand: COpaquePointer, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | OS X 10.10 |
| To | ``` func NSDecimalSubtract(_ result: UnsafeMutablePointer<NSDecimal>, _ leftOperand: UnsafePointer<NSDecimal>, _ rightOperand: UnsafePointer<NSDecimal>, _ roundingMode: NSRoundingMode) -> NSCalculationError ``` | OS X 10.10.3 |

Modified NSDefaultRunLoopMode

|  | Declaration |
| --- | --- |
| From | ``` let NSDefaultRunLoopMode: NSString! ``` |
| To | ``` let NSDefaultRunLoopMode: String ``` |

Modified NSDestinationInvalidException

|  | Declaration |
| --- | --- |
| From | ``` let NSDestinationInvalidException: NSString! ``` |
| To | ``` let NSDestinationInvalidException: String ``` |

Modified NSDidBecomeSingleThreadedNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSDidBecomeSingleThreadedNotification: NSString! ``` |
| To | ``` let NSDidBecomeSingleThreadedNotification: String ``` |

Modified NSDistinctUnionOfArraysKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSDistinctUnionOfArraysKeyValueOperator: NSString! ``` |
| To | ``` let NSDistinctUnionOfArraysKeyValueOperator: String ``` |

Modified NSDistinctUnionOfObjectsKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSDistinctUnionOfObjectsKeyValueOperator: NSString! ``` |
| To | ``` let NSDistinctUnionOfObjectsKeyValueOperator: String ``` |

Modified NSDistinctUnionOfSetsKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSDistinctUnionOfSetsKeyValueOperator: NSString! ``` |
| To | ``` let NSDistinctUnionOfSetsKeyValueOperator: String ``` |

Modified NSDivideRect(NSRect, UnsafeMutablePointer<NSRect>, UnsafeMutablePointer<NSRect>, CGFloat, NSRectEdge)

|  | Declaration |
| --- | --- |
| From | ``` func NSDivideRect(_ inRect: NSRect, _ slice: UnsafePointer<NSRect>, _ rem: UnsafePointer<NSRect>, _ amount: CGFloat, _ edge: NSRectEdge) ``` |
| To | ``` func NSDivideRect(_ inRect: NSRect, _ slice: UnsafeMutablePointer<NSRect>, _ rem: UnsafeMutablePointer<NSRect>, _ amount: CGFloat, _ edge: NSRectEdge) ``` |

Modified NSEdgeInsetsMake(CGFloat, CGFloat, CGFloat, CGFloat) -> NSEdgeInsets

|  | Module |
| --- | --- |
| From | AppKit |
| To | Foundation |

Modified NSEndHashTableEnumeration(UnsafeMutablePointer<NSHashEnumerator>)

|  | Declaration |
| --- | --- |
| From | ``` func NSEndHashTableEnumeration(_ enumerator: UnsafePointer<NSHashEnumerator>) ``` |
| To | ``` func NSEndHashTableEnumeration(_ enumerator: UnsafeMutablePointer<NSHashEnumerator>) ``` |

Modified NSEndMapTableEnumeration(UnsafeMutablePointer<NSMapEnumerator>)

|  | Declaration |
| --- | --- |
| From | ``` func NSEndMapTableEnumeration(_ enumerator: UnsafePointer<NSMapEnumerator>) ``` |
| To | ``` func NSEndMapTableEnumeration(_ enumerator: UnsafeMutablePointer<NSMapEnumerator>) ``` |

Modified NSErrorPointer

|  | Declaration |
| --- | --- |
| From | ``` typealias NSErrorPointer = AutoreleasingUnsafePointer<NSError?> ``` |
| To | ``` typealias NSErrorPointer = AutoreleasingUnsafeMutablePointer<NSError?> ``` |

Modified NSExecutableArchitectureMismatchError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSExecutableErrorMaximum

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSExecutableErrorMinimum

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSExecutableLinkError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSExecutableLoadError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSExecutableNotLoadableError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSExecutableRuntimeMismatchError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSExtensionItemAttachmentsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionItemAttachmentsKey: NSString! ``` |
| To | ``` let NSExtensionItemAttachmentsKey: String ``` |

Modified NSExtensionItemAttributedContentTextKey

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionItemAttributedContentTextKey: NSString! ``` |
| To | ``` let NSExtensionItemAttributedContentTextKey: String ``` |

Modified NSExtensionItemAttributedTitleKey

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionItemAttributedTitleKey: NSString! ``` |
| To | ``` let NSExtensionItemAttributedTitleKey: String ``` |

Modified NSExtensionItemsAndErrorsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionItemsAndErrorsKey: NSString! ``` |
| To | ``` let NSExtensionItemsAndErrorsKey: String ``` |

Modified NSExtensionJavaScriptPreprocessingResultsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSExtensionJavaScriptPreprocessingResultsKey: NSString! ``` |
| To | ``` let NSExtensionJavaScriptPreprocessingResultsKey: String ``` |

Modified NSFeatureUnsupportedError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSFileAppendOnly

|  | Declaration |
| --- | --- |
| From | ``` let NSFileAppendOnly: NSString! ``` |
| To | ``` let NSFileAppendOnly: String ``` |

Modified NSFileBusy

|  | Declaration |
| --- | --- |
| From | ``` let NSFileBusy: NSString! ``` |
| To | ``` let NSFileBusy: String ``` |

Modified NSFileCreationDate

|  | Declaration |
| --- | --- |
| From | ``` let NSFileCreationDate: NSString! ``` |
| To | ``` let NSFileCreationDate: String ``` |

Modified NSFileDeviceIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let NSFileDeviceIdentifier: NSString! ``` |
| To | ``` let NSFileDeviceIdentifier: String ``` |

Modified NSFileExtensionHidden

|  | Declaration |
| --- | --- |
| From | ``` let NSFileExtensionHidden: NSString! ``` |
| To | ``` let NSFileExtensionHidden: String ``` |

Modified NSFileGroupOwnerAccountID

|  | Declaration |
| --- | --- |
| From | ``` let NSFileGroupOwnerAccountID: NSString! ``` |
| To | ``` let NSFileGroupOwnerAccountID: String ``` |

Modified NSFileGroupOwnerAccountName

|  | Declaration |
| --- | --- |
| From | ``` let NSFileGroupOwnerAccountName: NSString! ``` |
| To | ``` let NSFileGroupOwnerAccountName: String ``` |

Modified NSFileHFSCreatorCode

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHFSCreatorCode: NSString! ``` |
| To | ``` let NSFileHFSCreatorCode: String ``` |

Modified NSFileHFSTypeCode

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHFSTypeCode: NSString! ``` |
| To | ``` let NSFileHFSTypeCode: String ``` |

Modified NSFileHandleConnectionAcceptedNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHandleConnectionAcceptedNotification: NSString! ``` |
| To | ``` let NSFileHandleConnectionAcceptedNotification: String ``` |

Modified NSFileHandleDataAvailableNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHandleDataAvailableNotification: NSString! ``` |
| To | ``` let NSFileHandleDataAvailableNotification: String ``` |

Modified NSFileHandleNotificationDataItem

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHandleNotificationDataItem: NSString! ``` |
| To | ``` let NSFileHandleNotificationDataItem: String ``` |

Modified NSFileHandleNotificationFileHandleItem

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHandleNotificationFileHandleItem: NSString! ``` |
| To | ``` let NSFileHandleNotificationFileHandleItem: String ``` |

Modified NSFileHandleOperationException

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHandleOperationException: NSString! ``` |
| To | ``` let NSFileHandleOperationException: String ``` |

Modified NSFileHandleReadCompletionNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHandleReadCompletionNotification: NSString! ``` |
| To | ``` let NSFileHandleReadCompletionNotification: String ``` |

Modified NSFileHandleReadToEndOfFileCompletionNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSFileHandleReadToEndOfFileCompletionNotification: NSString! ``` |
| To | ``` let NSFileHandleReadToEndOfFileCompletionNotification: String ``` |

Modified NSFileImmutable

|  | Declaration |
| --- | --- |
| From | ``` let NSFileImmutable: NSString! ``` |
| To | ``` let NSFileImmutable: String ``` |

Modified NSFileModificationDate

|  | Declaration |
| --- | --- |
| From | ``` let NSFileModificationDate: NSString! ``` |
| To | ``` let NSFileModificationDate: String ``` |

Modified NSFileOwnerAccountID

|  | Declaration |
| --- | --- |
| From | ``` let NSFileOwnerAccountID: NSString! ``` |
| To | ``` let NSFileOwnerAccountID: String ``` |

Modified NSFileOwnerAccountName

|  | Declaration |
| --- | --- |
| From | ``` let NSFileOwnerAccountName: NSString! ``` |
| To | ``` let NSFileOwnerAccountName: String ``` |

Modified NSFilePathErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSFilePathErrorKey: NSString! ``` |
| To | ``` let NSFilePathErrorKey: String ``` |

Modified NSFilePosixPermissions

|  | Declaration |
| --- | --- |
| From | ``` let NSFilePosixPermissions: NSString! ``` |
| To | ``` let NSFilePosixPermissions: String ``` |

Modified NSFileReadTooLargeError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSFileReadUnknownStringEncodingError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSFileReferenceCount

|  | Declaration |
| --- | --- |
| From | ``` let NSFileReferenceCount: NSString! ``` |
| To | ``` let NSFileReferenceCount: String ``` |

Modified NSFileSize

|  | Declaration |
| --- | --- |
| From | ``` let NSFileSize: NSString! ``` |
| To | ``` let NSFileSize: String ``` |

Modified NSFileSystemFileNumber

|  | Declaration |
| --- | --- |
| From | ``` let NSFileSystemFileNumber: NSString! ``` |
| To | ``` let NSFileSystemFileNumber: String ``` |

Modified NSFileSystemFreeNodes

|  | Declaration |
| --- | --- |
| From | ``` let NSFileSystemFreeNodes: NSString! ``` |
| To | ``` let NSFileSystemFreeNodes: String ``` |

Modified NSFileSystemFreeSize

|  | Declaration |
| --- | --- |
| From | ``` let NSFileSystemFreeSize: NSString! ``` |
| To | ``` let NSFileSystemFreeSize: String ``` |

Modified NSFileSystemNodes

|  | Declaration |
| --- | --- |
| From | ``` let NSFileSystemNodes: NSString! ``` |
| To | ``` let NSFileSystemNodes: String ``` |

Modified NSFileSystemNumber

|  | Declaration |
| --- | --- |
| From | ``` let NSFileSystemNumber: NSString! ``` |
| To | ``` let NSFileSystemNumber: String ``` |

Modified NSFileSystemSize

|  | Declaration |
| --- | --- |
| From | ``` let NSFileSystemSize: NSString! ``` |
| To | ``` let NSFileSystemSize: String ``` |

Modified NSFileType

|  | Declaration |
| --- | --- |
| From | ``` let NSFileType: NSString! ``` |
| To | ``` let NSFileType: String ``` |

Modified NSFileTypeBlockSpecial

|  | Declaration |
| --- | --- |
| From | ``` let NSFileTypeBlockSpecial: NSString! ``` |
| To | ``` let NSFileTypeBlockSpecial: String ``` |

Modified NSFileTypeCharacterSpecial

|  | Declaration |
| --- | --- |
| From | ``` let NSFileTypeCharacterSpecial: NSString! ``` |
| To | ``` let NSFileTypeCharacterSpecial: String ``` |

Modified NSFileTypeDirectory

|  | Declaration |
| --- | --- |
| From | ``` let NSFileTypeDirectory: NSString! ``` |
| To | ``` let NSFileTypeDirectory: String ``` |

Modified NSFileTypeRegular

|  | Declaration |
| --- | --- |
| From | ``` let NSFileTypeRegular: NSString! ``` |
| To | ``` let NSFileTypeRegular: String ``` |

Modified NSFileTypeSocket

|  | Declaration |
| --- | --- |
| From | ``` let NSFileTypeSocket: NSString! ``` |
| To | ``` let NSFileTypeSocket: String ``` |

Modified NSFileTypeSymbolicLink

|  | Declaration |
| --- | --- |
| From | ``` let NSFileTypeSymbolicLink: NSString! ``` |
| To | ``` let NSFileTypeSymbolicLink: String ``` |

Modified NSFileTypeUnknown

|  | Declaration |
| --- | --- |
| From | ``` let NSFileTypeUnknown: NSString! ``` |
| To | ``` let NSFileTypeUnknown: String ``` |

Modified NSFileWriteFileExistsError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSFileWriteVolumeReadOnlyError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSGenericException

|  | Declaration |
| --- | --- |
| From | ``` let NSGenericException: NSString! ``` |
| To | ``` let NSGenericException: String ``` |

Modified NSGetSizeAndAlignment(UnsafePointer<Int8>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func NSGetSizeAndAlignment(_ typePtr: ConstUnsafePointer<Int8>, _ sizep: UnsafePointer<Int>, _ alignp: UnsafePointer<Int>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func NSGetSizeAndAlignment(_ typePtr: UnsafePointer<Int8>, _ sizep: UnsafeMutablePointer<Int>, _ alignp: UnsafeMutablePointer<Int>) -> UnsafePointer<Int8> ``` |

Modified NSGlobalDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSGlobalDomain: NSString! ``` |
| To | ``` let NSGlobalDomain: String ``` |

Modified NSGrammarCorrections

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSGrammarCorrections: NSString! ``` | OS X 10.10 |
| To | ``` let NSGrammarCorrections: String ``` | OS X 10.5 |

Modified NSGrammarRange

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSGrammarRange: NSString! ``` | OS X 10.10 |
| To | ``` let NSGrammarRange: String ``` | OS X 10.5 |

Modified NSGrammarUserDescription

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSGrammarUserDescription: NSString! ``` | OS X 10.10 |
| To | ``` let NSGrammarUserDescription: String ``` | OS X 10.5 |

Modified NSGregorianCalendar

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let NSGregorianCalendar: NSString! ``` | OS X 10.10 | -- |
| To | ``` let NSGregorianCalendar: String ``` | OS X 10.4 | OS X 10.10 |

Modified NSHTTPCookieComment

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieComment: NSString! ``` |
| To | ``` let NSHTTPCookieComment: String ``` |

Modified NSHTTPCookieCommentURL

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieCommentURL: NSString! ``` |
| To | ``` let NSHTTPCookieCommentURL: String ``` |

Modified NSHTTPCookieDiscard

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieDiscard: NSString! ``` |
| To | ``` let NSHTTPCookieDiscard: String ``` |

Modified NSHTTPCookieDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieDomain: NSString! ``` |
| To | ``` let NSHTTPCookieDomain: String ``` |

Modified NSHTTPCookieExpires

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieExpires: NSString! ``` |
| To | ``` let NSHTTPCookieExpires: String ``` |

Modified NSHTTPCookieManagerAcceptPolicyChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieManagerAcceptPolicyChangedNotification: NSString! ``` |
| To | ``` let NSHTTPCookieManagerAcceptPolicyChangedNotification: String ``` |

Modified NSHTTPCookieManagerCookiesChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieManagerCookiesChangedNotification: NSString! ``` |
| To | ``` let NSHTTPCookieManagerCookiesChangedNotification: String ``` |

Modified NSHTTPCookieMaximumAge

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieMaximumAge: NSString! ``` |
| To | ``` let NSHTTPCookieMaximumAge: String ``` |

Modified NSHTTPCookieName

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieName: NSString! ``` |
| To | ``` let NSHTTPCookieName: String ``` |

Modified NSHTTPCookieOriginURL

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieOriginURL: NSString! ``` |
| To | ``` let NSHTTPCookieOriginURL: String ``` |

Modified NSHTTPCookiePath

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookiePath: NSString! ``` |
| To | ``` let NSHTTPCookiePath: String ``` |

Modified NSHTTPCookiePort

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookiePort: NSString! ``` |
| To | ``` let NSHTTPCookiePort: String ``` |

Modified NSHTTPCookieSecure

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieSecure: NSString! ``` |
| To | ``` let NSHTTPCookieSecure: String ``` |

Modified NSHTTPCookieValue

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieValue: NSString! ``` |
| To | ``` let NSHTTPCookieValue: String ``` |

Modified NSHTTPCookieVersion

|  | Declaration |
| --- | --- |
| From | ``` let NSHTTPCookieVersion: NSString! ``` |
| To | ``` let NSHTTPCookieVersion: String ``` |

Modified NSHashGet(NSHashTable!, UnsafePointer<Void>) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func NSHashGet(_ table: NSHashTable!, _ pointer: ConstUnsafePointer<()>) -> UnsafePointer<()> ``` |
| To | ``` func NSHashGet(_ table: NSHashTable!, _ pointer: UnsafePointer<Void>) -> UnsafeMutablePointer<Void> ``` |

Modified NSHashInsert(NSHashTable!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func NSHashInsert(_ table: NSHashTable!, _ pointer: ConstUnsafePointer<()>) ``` |
| To | ``` func NSHashInsert(_ table: NSHashTable!, _ pointer: UnsafePointer<Void>) ``` |

Modified NSHashInsertIfAbsent(NSHashTable!, UnsafePointer<Void>) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func NSHashInsertIfAbsent(_ table: NSHashTable!, _ pointer: ConstUnsafePointer<()>) -> UnsafePointer<()> ``` |
| To | ``` func NSHashInsertIfAbsent(_ table: NSHashTable!, _ pointer: UnsafePointer<Void>) -> UnsafeMutablePointer<Void> ``` |

Modified NSHashInsertKnownAbsent(NSHashTable!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func NSHashInsertKnownAbsent(_ table: NSHashTable!, _ pointer: ConstUnsafePointer<()>) ``` |
| To | ``` func NSHashInsertKnownAbsent(_ table: NSHashTable!, _ pointer: UnsafePointer<Void>) ``` |

Modified NSHashRemove(NSHashTable!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func NSHashRemove(_ table: NSHashTable!, _ pointer: ConstUnsafePointer<()>) ``` |
| To | ``` func NSHashRemove(_ table: NSHashTable!, _ pointer: UnsafePointer<Void>) ``` |

Modified NSHashTableCopyIn

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSHashTableObjectPointerPersonality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSHashTableStrongMemory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSHashTableWeakMemory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSHebrewCalendar

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let NSHebrewCalendar: NSString! ``` | OS X 10.10 | -- |
| To | ``` let NSHebrewCalendar: String ``` | OS X 10.4 | OS X 10.10 |

Modified NSHelpAnchorErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSHelpAnchorErrorKey: NSString! ``` |
| To | ``` let NSHelpAnchorErrorKey: String ``` |

Modified NSISO8601Calendar

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let NSISO8601Calendar: NSString! ``` | OS X 10.10 | -- |
| To | ``` let NSISO8601Calendar: String ``` | OS X 10.6 | OS X 10.10 |

Modified NSInconsistentArchiveException

|  | Declaration |
| --- | --- |
| From | ``` let NSInconsistentArchiveException: NSString! ``` |
| To | ``` let NSInconsistentArchiveException: String ``` |

Modified NSIndianCalendar

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let NSIndianCalendar: NSString! ``` | OS X 10.10 | -- |
| To | ``` let NSIndianCalendar: String ``` | OS X 10.6 | OS X 10.10 |

Modified NSIntegerHashCallBacks

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSIntegerMapKeyCallBacks

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSIntegerMapValueCallBacks

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSIntegralRectWithOptions(NSRect, NSAlignmentOptions) -> NSRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSInternalInconsistencyException

|  | Declaration |
| --- | --- |
| From | ``` let NSInternalInconsistencyException: NSString! ``` |
| To | ``` let NSInternalInconsistencyException: String ``` |

Modified NSInvalidArchiveOperationException

|  | Declaration |
| --- | --- |
| From | ``` let NSInvalidArchiveOperationException: NSString! ``` |
| To | ``` let NSInvalidArchiveOperationException: String ``` |

Modified NSInvalidArgumentException

|  | Declaration |
| --- | --- |
| From | ``` let NSInvalidArgumentException: NSString! ``` |
| To | ``` let NSInvalidArgumentException: String ``` |

Modified NSInvalidReceivePortException

|  | Declaration |
| --- | --- |
| From | ``` let NSInvalidReceivePortException: NSString! ``` |
| To | ``` let NSInvalidReceivePortException: String ``` |

Modified NSInvalidSendPortException

|  | Declaration |
| --- | --- |
| From | ``` let NSInvalidSendPortException: NSString! ``` |
| To | ``` let NSInvalidSendPortException: String ``` |

Modified NSInvalidUnarchiveOperationException

|  | Declaration |
| --- | --- |
| From | ``` let NSInvalidUnarchiveOperationException: NSString! ``` |
| To | ``` let NSInvalidUnarchiveOperationException: String ``` |

Modified NSInvocationOperationCancelledException

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSInvocationOperationCancelledException: NSString! ``` | OS X 10.10 |
| To | ``` let NSInvocationOperationCancelledException: String ``` | OS X 10.5 |

Modified NSInvocationOperationVoidResultException

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSInvocationOperationVoidResultException: NSString! ``` | OS X 10.10 |
| To | ``` let NSInvocationOperationVoidResultException: String ``` | OS X 10.5 |

Modified NSIsNilTransformerName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSIsNilTransformerName: NSString! ``` | OS X 10.10 |
| To | ``` let NSIsNilTransformerName: String ``` | OS X 10.3 |

Modified NSIsNotNilTransformerName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSIsNotNilTransformerName: NSString! ``` | OS X 10.10 |
| To | ``` let NSIsNotNilTransformerName: String ``` | OS X 10.3 |

Modified NSIslamicCalendar

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let NSIslamicCalendar: NSString! ``` | OS X 10.10 | -- |
| To | ``` let NSIslamicCalendar: String ``` | OS X 10.4 | OS X 10.10 |

Modified NSIslamicCivilCalendar

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let NSIslamicCivilCalendar: NSString! ``` | OS X 10.10 | -- |
| To | ``` let NSIslamicCivilCalendar: String ``` | OS X 10.4 | OS X 10.10 |

Modified NSItemProviderErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSItemProviderErrorDomain: NSString! ``` |
| To | ``` let NSItemProviderErrorDomain: String ``` |

Modified NSItemProviderPreferredImageSizeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSItemProviderPreferredImageSizeKey: NSString! ``` |
| To | ``` let NSItemProviderPreferredImageSizeKey: String ``` |

Modified NSJapaneseCalendar

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let NSJapaneseCalendar: NSString! ``` | OS X 10.10 | -- |
| To | ``` let NSJapaneseCalendar: String ``` | OS X 10.4 | OS X 10.10 |

Modified NSKeyValueChangeIndexesKey

|  | Declaration |
| --- | --- |
| From | ``` let NSKeyValueChangeIndexesKey: NSString! ``` |
| To | ``` let NSKeyValueChangeIndexesKey: String ``` |

Modified NSKeyValueChangeKindKey

|  | Declaration |
| --- | --- |
| From | ``` let NSKeyValueChangeKindKey: NSString! ``` |
| To | ``` let NSKeyValueChangeKindKey: String ``` |

Modified NSKeyValueChangeNewKey

|  | Declaration |
| --- | --- |
| From | ``` let NSKeyValueChangeNewKey: NSString! ``` |
| To | ``` let NSKeyValueChangeNewKey: String ``` |

Modified NSKeyValueChangeNotificationIsPriorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSKeyValueChangeNotificationIsPriorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSKeyValueChangeNotificationIsPriorKey: String ``` | OS X 10.5 |

Modified NSKeyValueChangeOldKey

|  | Declaration |
| --- | --- |
| From | ``` let NSKeyValueChangeOldKey: NSString! ``` |
| To | ``` let NSKeyValueChangeOldKey: String ``` |

Modified NSKeyedArchiveRootObjectKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSKeyedArchiveRootObjectKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSKeyedArchiveRootObjectKey: String ``` | OS X 10.9 |

Modified NSKeyedUnarchiveFromDataTransformerName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSKeyedUnarchiveFromDataTransformerName: NSString! ``` | OS X 10.10 |
| To | ``` let NSKeyedUnarchiveFromDataTransformerName: String ``` | OS X 10.5 |

Modified NSLinguisticTagAdjective

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagAdjective: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagAdjective: String ``` | OS X 10.7 |

Modified NSLinguisticTagAdverb

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagAdverb: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagAdverb: String ``` | OS X 10.7 |

Modified NSLinguisticTagClassifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagClassifier: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagClassifier: String ``` | OS X 10.7 |

Modified NSLinguisticTagCloseParenthesis

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagCloseParenthesis: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagCloseParenthesis: String ``` | OS X 10.7 |

Modified NSLinguisticTagCloseQuote

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagCloseQuote: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagCloseQuote: String ``` | OS X 10.7 |

Modified NSLinguisticTagConjunction

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagConjunction: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagConjunction: String ``` | OS X 10.7 |

Modified NSLinguisticTagDash

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagDash: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagDash: String ``` | OS X 10.7 |

Modified NSLinguisticTagDeterminer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagDeterminer: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagDeterminer: String ``` | OS X 10.7 |

Modified NSLinguisticTagIdiom

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagIdiom: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagIdiom: String ``` | OS X 10.7 |

Modified NSLinguisticTagInterjection

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagInterjection: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagInterjection: String ``` | OS X 10.7 |

Modified NSLinguisticTagNoun

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagNoun: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagNoun: String ``` | OS X 10.7 |

Modified NSLinguisticTagNumber

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagNumber: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagNumber: String ``` | OS X 10.7 |

Modified NSLinguisticTagOpenParenthesis

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagOpenParenthesis: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagOpenParenthesis: String ``` | OS X 10.7 |

Modified NSLinguisticTagOpenQuote

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagOpenQuote: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagOpenQuote: String ``` | OS X 10.7 |

Modified NSLinguisticTagOrganizationName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagOrganizationName: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagOrganizationName: String ``` | OS X 10.7 |

Modified NSLinguisticTagOther

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagOther: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagOther: String ``` | OS X 10.7 |

Modified NSLinguisticTagOtherPunctuation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagOtherPunctuation: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagOtherPunctuation: String ``` | OS X 10.7 |

Modified NSLinguisticTagOtherWhitespace

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagOtherWhitespace: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagOtherWhitespace: String ``` | OS X 10.7 |

Modified NSLinguisticTagOtherWord

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagOtherWord: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagOtherWord: String ``` | OS X 10.7 |

Modified NSLinguisticTagParagraphBreak

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagParagraphBreak: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagParagraphBreak: String ``` | OS X 10.7 |

Modified NSLinguisticTagParticle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagParticle: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagParticle: String ``` | OS X 10.7 |

Modified NSLinguisticTagPersonalName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagPersonalName: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagPersonalName: String ``` | OS X 10.7 |

Modified NSLinguisticTagPlaceName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagPlaceName: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagPlaceName: String ``` | OS X 10.7 |

Modified NSLinguisticTagPreposition

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagPreposition: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagPreposition: String ``` | OS X 10.7 |

Modified NSLinguisticTagPronoun

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagPronoun: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagPronoun: String ``` | OS X 10.7 |

Modified NSLinguisticTagPunctuation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagPunctuation: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagPunctuation: String ``` | OS X 10.7 |

Modified NSLinguisticTagSchemeLanguage

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagSchemeLanguage: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagSchemeLanguage: String ``` | OS X 10.7 |

Modified NSLinguisticTagSchemeLemma

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagSchemeLemma: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagSchemeLemma: String ``` | OS X 10.7 |

Modified NSLinguisticTagSchemeLexicalClass

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagSchemeLexicalClass: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagSchemeLexicalClass: String ``` | OS X 10.7 |

Modified NSLinguisticTagSchemeNameType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagSchemeNameType: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagSchemeNameType: String ``` | OS X 10.7 |

Modified NSLinguisticTagSchemeNameTypeOrLexicalClass

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagSchemeNameTypeOrLexicalClass: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagSchemeNameTypeOrLexicalClass: String ``` | OS X 10.7 |

Modified NSLinguisticTagSchemeScript

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagSchemeScript: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagSchemeScript: String ``` | OS X 10.7 |

Modified NSLinguisticTagSchemeTokenType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagSchemeTokenType: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagSchemeTokenType: String ``` | OS X 10.7 |

Modified NSLinguisticTagSentenceTerminator

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagSentenceTerminator: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagSentenceTerminator: String ``` | OS X 10.7 |

Modified NSLinguisticTagVerb

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagVerb: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagVerb: String ``` | OS X 10.7 |

Modified NSLinguisticTagWhitespace

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagWhitespace: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagWhitespace: String ``` | OS X 10.7 |

Modified NSLinguisticTagWord

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagWord: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagWord: String ``` | OS X 10.7 |

Modified NSLinguisticTagWordJoiner

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLinguisticTagWordJoiner: NSString! ``` | OS X 10.10 |
| To | ``` let NSLinguisticTagWordJoiner: String ``` | OS X 10.7 |

Modified NSLoadedClasses

|  | Declaration |
| --- | --- |
| From | ``` let NSLoadedClasses: NSString! ``` |
| To | ``` let NSLoadedClasses: String ``` |

Modified NSLocalNotificationCenterType

|  | Declaration |
| --- | --- |
| From | ``` let NSLocalNotificationCenterType: NSString! ``` |
| To | ``` let NSLocalNotificationCenterType: String ``` |

Modified NSLocaleAlternateQuotationBeginDelimiterKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLocaleAlternateQuotationBeginDelimiterKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSLocaleAlternateQuotationBeginDelimiterKey: String ``` | OS X 10.6 |

Modified NSLocaleAlternateQuotationEndDelimiterKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLocaleAlternateQuotationEndDelimiterKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSLocaleAlternateQuotationEndDelimiterKey: String ``` | OS X 10.6 |

Modified NSLocaleCalendar

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleCalendar: NSString! ``` |
| To | ``` let NSLocaleCalendar: String ``` |

Modified NSLocaleCollationIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleCollationIdentifier: NSString! ``` |
| To | ``` let NSLocaleCollationIdentifier: String ``` |

Modified NSLocaleCollatorIdentifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLocaleCollatorIdentifier: NSString! ``` | OS X 10.10 |
| To | ``` let NSLocaleCollatorIdentifier: String ``` | OS X 10.6 |

Modified NSLocaleCountryCode

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleCountryCode: NSString! ``` |
| To | ``` let NSLocaleCountryCode: String ``` |

Modified NSLocaleCurrencyCode

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleCurrencyCode: NSString! ``` |
| To | ``` let NSLocaleCurrencyCode: String ``` |

Modified NSLocaleCurrencySymbol

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleCurrencySymbol: NSString! ``` |
| To | ``` let NSLocaleCurrencySymbol: String ``` |

Modified NSLocaleDecimalSeparator

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleDecimalSeparator: NSString! ``` |
| To | ``` let NSLocaleDecimalSeparator: String ``` |

Modified NSLocaleExemplarCharacterSet

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleExemplarCharacterSet: NSString! ``` |
| To | ``` let NSLocaleExemplarCharacterSet: String ``` |

Modified NSLocaleGroupingSeparator

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleGroupingSeparator: NSString! ``` |
| To | ``` let NSLocaleGroupingSeparator: String ``` |

Modified NSLocaleIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleIdentifier: NSString! ``` |
| To | ``` let NSLocaleIdentifier: String ``` |

Modified NSLocaleLanguageCode

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleLanguageCode: NSString! ``` |
| To | ``` let NSLocaleLanguageCode: String ``` |

Modified NSLocaleMeasurementSystem

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleMeasurementSystem: NSString! ``` |
| To | ``` let NSLocaleMeasurementSystem: String ``` |

Modified NSLocaleQuotationBeginDelimiterKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLocaleQuotationBeginDelimiterKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSLocaleQuotationBeginDelimiterKey: String ``` | OS X 10.6 |

Modified NSLocaleQuotationEndDelimiterKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSLocaleQuotationEndDelimiterKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSLocaleQuotationEndDelimiterKey: String ``` | OS X 10.6 |

Modified NSLocaleScriptCode

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleScriptCode: NSString! ``` |
| To | ``` let NSLocaleScriptCode: String ``` |

Modified NSLocaleUsesMetricSystem

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleUsesMetricSystem: NSString! ``` |
| To | ``` let NSLocaleUsesMetricSystem: String ``` |

Modified NSLocaleVariantCode

|  | Declaration |
| --- | --- |
| From | ``` let NSLocaleVariantCode: NSString! ``` |
| To | ``` let NSLocaleVariantCode: String ``` |

Modified NSLocalizedDescriptionKey

|  | Declaration |
| --- | --- |
| From | ``` let NSLocalizedDescriptionKey: NSString! ``` |
| To | ``` let NSLocalizedDescriptionKey: String ``` |

Modified NSLocalizedFailureReasonErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSLocalizedFailureReasonErrorKey: NSString! ``` |
| To | ``` let NSLocalizedFailureReasonErrorKey: String ``` |

Modified NSLocalizedRecoveryOptionsErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSLocalizedRecoveryOptionsErrorKey: NSString! ``` |
| To | ``` let NSLocalizedRecoveryOptionsErrorKey: String ``` |

Modified NSLocalizedRecoverySuggestionErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSLocalizedRecoverySuggestionErrorKey: NSString! ``` |
| To | ``` let NSLocalizedRecoverySuggestionErrorKey: String ``` |

Modified NSMachErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSMachErrorDomain: NSString! ``` |
| To | ``` let NSMachErrorDomain: String ``` |

Modified NSMallocException

|  | Declaration |
| --- | --- |
| From | ``` let NSMallocException: NSString! ``` |
| To | ``` let NSMallocException: String ``` |

Modified NSMapGet(NSMapTable!, UnsafePointer<Void>) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func NSMapGet(_ table: NSMapTable!, _ key: ConstUnsafePointer<()>) -> UnsafePointer<()> ``` |
| To | ``` func NSMapGet(_ table: NSMapTable!, _ key: UnsafePointer<Void>) -> UnsafeMutablePointer<Void> ``` |

Modified NSMapInsert(NSMapTable!, UnsafePointer<Void>, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func NSMapInsert(_ table: NSMapTable!, _ key: ConstUnsafePointer<()>, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func NSMapInsert(_ table: NSMapTable!, _ key: UnsafePointer<Void>, _ value: UnsafePointer<Void>) ``` |

Modified NSMapInsertIfAbsent(NSMapTable!, UnsafePointer<Void>, UnsafePointer<Void>) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func NSMapInsertIfAbsent(_ table: NSMapTable!, _ key: ConstUnsafePointer<()>, _ value: ConstUnsafePointer<()>) -> UnsafePointer<()> ``` |
| To | ``` func NSMapInsertIfAbsent(_ table: NSMapTable!, _ key: UnsafePointer<Void>, _ value: UnsafePointer<Void>) -> UnsafeMutablePointer<Void> ``` |

Modified NSMapInsertKnownAbsent(NSMapTable!, UnsafePointer<Void>, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func NSMapInsertKnownAbsent(_ table: NSMapTable!, _ key: ConstUnsafePointer<()>, _ value: ConstUnsafePointer<()>) ``` |
| To | ``` func NSMapInsertKnownAbsent(_ table: NSMapTable!, _ key: UnsafePointer<Void>, _ value: UnsafePointer<Void>) ``` |

Modified NSMapMember(NSMapTable!, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func NSMapMember(_ table: NSMapTable!, _ key: ConstUnsafePointer<()>, _ originalKey: UnsafePointer<UnsafePointer<()>>, _ value: UnsafePointer<UnsafePointer<()>>) -> Bool ``` |
| To | ``` func NSMapMember(_ table: NSMapTable!, _ key: UnsafePointer<Void>, _ originalKey: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ value: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Bool ``` |

Modified NSMapRemove(NSMapTable!, UnsafePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func NSMapRemove(_ table: NSMapTable!, _ key: ConstUnsafePointer<()>) ``` |
| To | ``` func NSMapRemove(_ table: NSMapTable!, _ key: UnsafePointer<Void>) ``` |

Modified NSMapTableCopyIn

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSMapTableObjectPointerPersonality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSMapTableStrongMemory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSMapTableWeakMemory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSMaximumKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSMaximumKeyValueOperator: NSString! ``` |
| To | ``` let NSMaximumKeyValueOperator: String ``` |

Modified NSMetadataItemAcquisitionMakeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAcquisitionMakeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAcquisitionMakeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAcquisitionModelKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAcquisitionModelKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAcquisitionModelKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAlbumKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAlbumKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAlbumKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAltitudeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAltitudeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAltitudeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemApertureKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemApertureKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemApertureKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAppleLoopDescriptorsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAppleLoopDescriptorsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAppleLoopDescriptorsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAppleLoopsKeyFilterTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAppleLoopsKeyFilterTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAppleLoopsKeyFilterTypeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAppleLoopsLoopModeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAppleLoopsLoopModeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAppleLoopsLoopModeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAppleLoopsRootKeyKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAppleLoopsRootKeyKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAppleLoopsRootKeyKey: String ``` | OS X 10.9 |

Modified NSMetadataItemApplicationCategoriesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemApplicationCategoriesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemApplicationCategoriesKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAttributeChangeDateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAttributeChangeDateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAttributeChangeDateKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAudiencesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAudiencesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAudiencesKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAudioBitRateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAudioBitRateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAudioBitRateKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAudioChannelCountKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAudioChannelCountKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAudioChannelCountKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAudioEncodingApplicationKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAudioEncodingApplicationKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAudioEncodingApplicationKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAudioSampleRateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAudioSampleRateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAudioSampleRateKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAudioTrackNumberKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAudioTrackNumberKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAudioTrackNumberKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAuthorAddressesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAuthorAddressesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAuthorAddressesKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAuthorEmailAddressesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAuthorEmailAddressesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAuthorEmailAddressesKey: String ``` | OS X 10.9 |

Modified NSMetadataItemAuthorsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemAuthorsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemAuthorsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemBitsPerSampleKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemBitsPerSampleKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemBitsPerSampleKey: String ``` | OS X 10.9 |

Modified NSMetadataItemCFBundleIdentifierKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemCFBundleIdentifierKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemCFBundleIdentifierKey: String ``` | OS X 10.9 |

Modified NSMetadataItemCameraOwnerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemCameraOwnerKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemCameraOwnerKey: String ``` | OS X 10.9 |

Modified NSMetadataItemCityKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemCityKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemCityKey: String ``` | OS X 10.9 |

Modified NSMetadataItemCodecsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemCodecsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemCodecsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemColorSpaceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemColorSpaceKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemColorSpaceKey: String ``` | OS X 10.9 |

Modified NSMetadataItemCommentKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemCommentKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemCommentKey: String ``` | OS X 10.9 |

Modified NSMetadataItemComposerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemComposerKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemComposerKey: String ``` | OS X 10.9 |

Modified NSMetadataItemContactKeywordsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemContactKeywordsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemContactKeywordsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemContentCreationDateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemContentCreationDateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemContentCreationDateKey: String ``` | OS X 10.9 |

Modified NSMetadataItemContentModificationDateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemContentModificationDateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemContentModificationDateKey: String ``` | OS X 10.9 |

Modified NSMetadataItemContentTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemContentTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemContentTypeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemContentTypeTreeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemContentTypeTreeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemContentTypeTreeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemContributorsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemContributorsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemContributorsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemCopyrightKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemCopyrightKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemCopyrightKey: String ``` | OS X 10.9 |

Modified NSMetadataItemCountryKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemCountryKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemCountryKey: String ``` | OS X 10.9 |

Modified NSMetadataItemCoverageKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemCoverageKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemCoverageKey: String ``` | OS X 10.9 |

Modified NSMetadataItemCreatorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemCreatorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemCreatorKey: String ``` | OS X 10.9 |

Modified NSMetadataItemDateAddedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemDateAddedKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemDateAddedKey: String ``` | OS X 10.9 |

Modified NSMetadataItemDeliveryTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemDeliveryTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemDeliveryTypeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemDescriptionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemDescriptionKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemDescriptionKey: String ``` | OS X 10.9 |

Modified NSMetadataItemDirectorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemDirectorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemDirectorKey: String ``` | OS X 10.9 |

Modified NSMetadataItemDisplayNameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemDisplayNameKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemDisplayNameKey: String ``` | OS X 10.7 |

Modified NSMetadataItemDownloadedDateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemDownloadedDateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemDownloadedDateKey: String ``` | OS X 10.9 |

Modified NSMetadataItemDueDateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemDueDateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemDueDateKey: String ``` | OS X 10.9 |

Modified NSMetadataItemDurationSecondsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemDurationSecondsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemDurationSecondsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemEXIFGPSVersionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemEXIFGPSVersionKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemEXIFGPSVersionKey: String ``` | OS X 10.9 |

Modified NSMetadataItemEXIFVersionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemEXIFVersionKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemEXIFVersionKey: String ``` | OS X 10.9 |

Modified NSMetadataItemEditorsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemEditorsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemEditorsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemEmailAddressesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemEmailAddressesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemEmailAddressesKey: String ``` | OS X 10.9 |

Modified NSMetadataItemEncodingApplicationsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemEncodingApplicationsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemEncodingApplicationsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemExecutableArchitecturesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemExecutableArchitecturesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemExecutableArchitecturesKey: String ``` | OS X 10.9 |

Modified NSMetadataItemExecutablePlatformKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemExecutablePlatformKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemExecutablePlatformKey: String ``` | OS X 10.9 |

Modified NSMetadataItemExposureModeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemExposureModeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemExposureModeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemExposureProgramKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemExposureProgramKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemExposureProgramKey: String ``` | OS X 10.9 |

Modified NSMetadataItemExposureTimeSecondsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemExposureTimeSecondsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemExposureTimeSecondsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemExposureTimeStringKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemExposureTimeStringKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemExposureTimeStringKey: String ``` | OS X 10.9 |

Modified NSMetadataItemFNumberKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemFNumberKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemFNumberKey: String ``` | OS X 10.9 |

Modified NSMetadataItemFSContentChangeDateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemFSContentChangeDateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemFSContentChangeDateKey: String ``` | OS X 10.7 |

Modified NSMetadataItemFSCreationDateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemFSCreationDateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemFSCreationDateKey: String ``` | OS X 10.7 |

Modified NSMetadataItemFSNameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemFSNameKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemFSNameKey: String ``` | OS X 10.7 |

Modified NSMetadataItemFSSizeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemFSSizeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemFSSizeKey: String ``` | OS X 10.7 |

Modified NSMetadataItemFinderCommentKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemFinderCommentKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemFinderCommentKey: String ``` | OS X 10.9 |

Modified NSMetadataItemFlashOnOffKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemFlashOnOffKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemFlashOnOffKey: String ``` | OS X 10.9 |

Modified NSMetadataItemFocalLength35mmKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemFocalLength35mmKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemFocalLength35mmKey: String ``` | OS X 10.9 |

Modified NSMetadataItemFocalLengthKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemFocalLengthKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemFocalLengthKey: String ``` | OS X 10.9 |

Modified NSMetadataItemFontsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemFontsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemFontsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemGPSAreaInformationKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemGPSAreaInformationKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemGPSAreaInformationKey: String ``` | OS X 10.9 |

Modified NSMetadataItemGPSDOPKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemGPSDOPKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemGPSDOPKey: String ``` | OS X 10.9 |

Modified NSMetadataItemGPSDateStampKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemGPSDateStampKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemGPSDateStampKey: String ``` | OS X 10.9 |

Modified NSMetadataItemGPSDestBearingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemGPSDestBearingKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemGPSDestBearingKey: String ``` | OS X 10.9 |

Modified NSMetadataItemGPSDestDistanceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemGPSDestDistanceKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemGPSDestDistanceKey: String ``` | OS X 10.9 |

Modified NSMetadataItemGPSDestLatitudeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemGPSDestLatitudeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemGPSDestLatitudeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemGPSDestLongitudeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemGPSDestLongitudeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemGPSDestLongitudeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemGPSDifferentalKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemGPSDifferentalKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemGPSDifferentalKey: String ``` | OS X 10.9 |

Modified NSMetadataItemGPSMapDatumKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemGPSMapDatumKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemGPSMapDatumKey: String ``` | OS X 10.9 |

Modified NSMetadataItemGPSMeasureModeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemGPSMeasureModeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemGPSMeasureModeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemGPSProcessingMethodKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemGPSProcessingMethodKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemGPSProcessingMethodKey: String ``` | OS X 10.9 |

Modified NSMetadataItemGPSStatusKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemGPSStatusKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemGPSStatusKey: String ``` | OS X 10.9 |

Modified NSMetadataItemGPSTrackKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemGPSTrackKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemGPSTrackKey: String ``` | OS X 10.9 |

Modified NSMetadataItemGenreKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemGenreKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemGenreKey: String ``` | OS X 10.9 |

Modified NSMetadataItemHasAlphaChannelKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemHasAlphaChannelKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemHasAlphaChannelKey: String ``` | OS X 10.9 |

Modified NSMetadataItemHeadlineKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemHeadlineKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemHeadlineKey: String ``` | OS X 10.9 |

Modified NSMetadataItemISOSpeedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemISOSpeedKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemISOSpeedKey: String ``` | OS X 10.9 |

Modified NSMetadataItemIdentifierKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemIdentifierKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemIdentifierKey: String ``` | OS X 10.9 |

Modified NSMetadataItemImageDirectionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemImageDirectionKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemImageDirectionKey: String ``` | OS X 10.9 |

Modified NSMetadataItemInformationKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemInformationKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemInformationKey: String ``` | OS X 10.9 |

Modified NSMetadataItemInstantMessageAddressesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemInstantMessageAddressesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemInstantMessageAddressesKey: String ``` | OS X 10.9 |

Modified NSMetadataItemInstructionsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemInstructionsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemInstructionsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemIsApplicationManagedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemIsApplicationManagedKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemIsApplicationManagedKey: String ``` | OS X 10.9 |

Modified NSMetadataItemIsGeneralMIDISequenceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemIsGeneralMIDISequenceKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemIsGeneralMIDISequenceKey: String ``` | OS X 10.9 |

Modified NSMetadataItemIsLikelyJunkKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemIsLikelyJunkKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemIsLikelyJunkKey: String ``` | OS X 10.9 |

Modified NSMetadataItemIsUbiquitousKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemIsUbiquitousKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemIsUbiquitousKey: String ``` | OS X 10.7 |

Modified NSMetadataItemKeySignatureKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemKeySignatureKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemKeySignatureKey: String ``` | OS X 10.9 |

Modified NSMetadataItemKeywordsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemKeywordsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemKeywordsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemKindKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemKindKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemKindKey: String ``` | OS X 10.9 |

Modified NSMetadataItemLanguagesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemLanguagesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemLanguagesKey: String ``` | OS X 10.9 |

Modified NSMetadataItemLastUsedDateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemLastUsedDateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemLastUsedDateKey: String ``` | OS X 10.9 |

Modified NSMetadataItemLatitudeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemLatitudeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemLatitudeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemLayerNamesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemLayerNamesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemLayerNamesKey: String ``` | OS X 10.9 |

Modified NSMetadataItemLensModelKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemLensModelKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemLensModelKey: String ``` | OS X 10.9 |

Modified NSMetadataItemLongitudeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemLongitudeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemLongitudeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemLyricistKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemLyricistKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemLyricistKey: String ``` | OS X 10.9 |

Modified NSMetadataItemMaxApertureKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemMaxApertureKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemMaxApertureKey: String ``` | OS X 10.9 |

Modified NSMetadataItemMediaTypesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemMediaTypesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemMediaTypesKey: String ``` | OS X 10.9 |

Modified NSMetadataItemMeteringModeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemMeteringModeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemMeteringModeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemMusicalGenreKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemMusicalGenreKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemMusicalGenreKey: String ``` | OS X 10.9 |

Modified NSMetadataItemMusicalInstrumentCategoryKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemMusicalInstrumentCategoryKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemMusicalInstrumentCategoryKey: String ``` | OS X 10.9 |

Modified NSMetadataItemMusicalInstrumentNameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemMusicalInstrumentNameKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemMusicalInstrumentNameKey: String ``` | OS X 10.9 |

Modified NSMetadataItemNamedLocationKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemNamedLocationKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemNamedLocationKey: String ``` | OS X 10.9 |

Modified NSMetadataItemNumberOfPagesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemNumberOfPagesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemNumberOfPagesKey: String ``` | OS X 10.9 |

Modified NSMetadataItemOrganizationsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemOrganizationsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemOrganizationsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemOrientationKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemOrientationKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemOrientationKey: String ``` | OS X 10.9 |

Modified NSMetadataItemOriginalFormatKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemOriginalFormatKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemOriginalFormatKey: String ``` | OS X 10.9 |

Modified NSMetadataItemOriginalSourceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemOriginalSourceKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemOriginalSourceKey: String ``` | OS X 10.9 |

Modified NSMetadataItemPageHeightKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemPageHeightKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemPageHeightKey: String ``` | OS X 10.9 |

Modified NSMetadataItemPageWidthKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemPageWidthKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemPageWidthKey: String ``` | OS X 10.9 |

Modified NSMetadataItemParticipantsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemParticipantsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemParticipantsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemPathKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemPathKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemPathKey: String ``` | OS X 10.7 |

Modified NSMetadataItemPerformersKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemPerformersKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemPerformersKey: String ``` | OS X 10.9 |

Modified NSMetadataItemPhoneNumbersKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemPhoneNumbersKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemPhoneNumbersKey: String ``` | OS X 10.9 |

Modified NSMetadataItemPixelCountKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemPixelCountKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemPixelCountKey: String ``` | OS X 10.9 |

Modified NSMetadataItemPixelHeightKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemPixelHeightKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemPixelHeightKey: String ``` | OS X 10.9 |

Modified NSMetadataItemPixelWidthKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemPixelWidthKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemPixelWidthKey: String ``` | OS X 10.9 |

Modified NSMetadataItemProducerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemProducerKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemProducerKey: String ``` | OS X 10.9 |

Modified NSMetadataItemProfileNameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemProfileNameKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemProfileNameKey: String ``` | OS X 10.9 |

Modified NSMetadataItemProjectsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemProjectsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemProjectsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemPublishersKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemPublishersKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemPublishersKey: String ``` | OS X 10.9 |

Modified NSMetadataItemRecipientAddressesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemRecipientAddressesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemRecipientAddressesKey: String ``` | OS X 10.9 |

Modified NSMetadataItemRecipientEmailAddressesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemRecipientEmailAddressesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemRecipientEmailAddressesKey: String ``` | OS X 10.9 |

Modified NSMetadataItemRecipientsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemRecipientsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemRecipientsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemRecordingDateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemRecordingDateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemRecordingDateKey: String ``` | OS X 10.9 |

Modified NSMetadataItemRecordingYearKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemRecordingYearKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemRecordingYearKey: String ``` | OS X 10.9 |

Modified NSMetadataItemRedEyeOnOffKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemRedEyeOnOffKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemRedEyeOnOffKey: String ``` | OS X 10.9 |

Modified NSMetadataItemResolutionHeightDPIKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemResolutionHeightDPIKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemResolutionHeightDPIKey: String ``` | OS X 10.9 |

Modified NSMetadataItemResolutionWidthDPIKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemResolutionWidthDPIKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemResolutionWidthDPIKey: String ``` | OS X 10.9 |

Modified NSMetadataItemRightsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemRightsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemRightsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemSecurityMethodKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemSecurityMethodKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemSecurityMethodKey: String ``` | OS X 10.9 |

Modified NSMetadataItemSpeedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemSpeedKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemSpeedKey: String ``` | OS X 10.9 |

Modified NSMetadataItemStarRatingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemStarRatingKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemStarRatingKey: String ``` | OS X 10.9 |

Modified NSMetadataItemStateOrProvinceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemStateOrProvinceKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemStateOrProvinceKey: String ``` | OS X 10.9 |

Modified NSMetadataItemStreamableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemStreamableKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemStreamableKey: String ``` | OS X 10.9 |

Modified NSMetadataItemSubjectKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemSubjectKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemSubjectKey: String ``` | OS X 10.9 |

Modified NSMetadataItemTempoKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemTempoKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemTempoKey: String ``` | OS X 10.9 |

Modified NSMetadataItemTextContentKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemTextContentKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemTextContentKey: String ``` | OS X 10.9 |

Modified NSMetadataItemThemeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemThemeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemThemeKey: String ``` | OS X 10.9 |

Modified NSMetadataItemTimeSignatureKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemTimeSignatureKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemTimeSignatureKey: String ``` | OS X 10.9 |

Modified NSMetadataItemTimestampKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemTimestampKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemTimestampKey: String ``` | OS X 10.9 |

Modified NSMetadataItemTitleKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemTitleKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemTitleKey: String ``` | OS X 10.9 |

Modified NSMetadataItemTotalBitRateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemTotalBitRateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemTotalBitRateKey: String ``` | OS X 10.9 |

Modified NSMetadataItemURLKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemURLKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemURLKey: String ``` | OS X 10.7 |

Modified NSMetadataItemVersionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemVersionKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemVersionKey: String ``` | OS X 10.9 |

Modified NSMetadataItemVideoBitRateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemVideoBitRateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemVideoBitRateKey: String ``` | OS X 10.9 |

Modified NSMetadataItemWhereFromsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemWhereFromsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemWhereFromsKey: String ``` | OS X 10.9 |

Modified NSMetadataItemWhiteBalanceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataItemWhiteBalanceKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataItemWhiteBalanceKey: String ``` | OS X 10.9 |

Modified NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope: NSString! ``` |
| To | ``` let NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope: String ``` |

Modified NSMetadataQueryDidFinishGatheringNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryDidFinishGatheringNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryDidFinishGatheringNotification: String ``` | OS X 10.4 |

Modified NSMetadataQueryDidStartGatheringNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryDidStartGatheringNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryDidStartGatheringNotification: String ``` | OS X 10.4 |

Modified NSMetadataQueryDidUpdateNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryDidUpdateNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryDidUpdateNotification: String ``` | OS X 10.4 |

Modified NSMetadataQueryGatheringProgressNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryGatheringProgressNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryGatheringProgressNotification: String ``` | OS X 10.4 |

Modified NSMetadataQueryIndexedLocalComputerScope

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryIndexedLocalComputerScope: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryIndexedLocalComputerScope: String ``` | OS X 10.9 |

Modified NSMetadataQueryIndexedNetworkScope

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryIndexedNetworkScope: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryIndexedNetworkScope: String ``` | OS X 10.9 |

Modified NSMetadataQueryLocalComputerScope

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryLocalComputerScope: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryLocalComputerScope: String ``` | OS X 10.4 |

Modified NSMetadataQueryNetworkScope

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryNetworkScope: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryNetworkScope: String ``` | OS X 10.4 |

Modified NSMetadataQueryResultContentRelevanceAttribute

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryResultContentRelevanceAttribute: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryResultContentRelevanceAttribute: String ``` | OS X 10.4 |

Modified NSMetadataQueryUbiquitousDataScope

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryUbiquitousDataScope: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryUbiquitousDataScope: String ``` | OS X 10.7 |

Modified NSMetadataQueryUbiquitousDocumentsScope

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryUbiquitousDocumentsScope: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryUbiquitousDocumentsScope: String ``` | OS X 10.7 |

Modified NSMetadataQueryUpdateAddedItemsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryUpdateAddedItemsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryUpdateAddedItemsKey: String ``` | OS X 10.9 |

Modified NSMetadataQueryUpdateChangedItemsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryUpdateChangedItemsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryUpdateChangedItemsKey: String ``` | OS X 10.9 |

Modified NSMetadataQueryUpdateRemovedItemsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryUpdateRemovedItemsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryUpdateRemovedItemsKey: String ``` | OS X 10.9 |

Modified NSMetadataQueryUserHomeScope

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataQueryUserHomeScope: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataQueryUserHomeScope: String ``` | OS X 10.4 |

Modified NSMetadataUbiquitousItemContainerDisplayNameKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemContainerDisplayNameKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemContainerDisplayNameKey: String ``` |

Modified NSMetadataUbiquitousItemDownloadRequestedKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemDownloadRequestedKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemDownloadRequestedKey: String ``` |

Modified NSMetadataUbiquitousItemDownloadingErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataUbiquitousItemDownloadingErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataUbiquitousItemDownloadingErrorKey: String ``` | OS X 10.9 |

Modified NSMetadataUbiquitousItemDownloadingStatusCurrent

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataUbiquitousItemDownloadingStatusCurrent: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataUbiquitousItemDownloadingStatusCurrent: String ``` | OS X 10.9 |

Modified NSMetadataUbiquitousItemDownloadingStatusDownloaded

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataUbiquitousItemDownloadingStatusDownloaded: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataUbiquitousItemDownloadingStatusDownloaded: String ``` | OS X 10.9 |

Modified NSMetadataUbiquitousItemDownloadingStatusKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataUbiquitousItemDownloadingStatusKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataUbiquitousItemDownloadingStatusKey: String ``` | OS X 10.9 |

Modified NSMetadataUbiquitousItemDownloadingStatusNotDownloaded

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataUbiquitousItemDownloadingStatusNotDownloaded: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataUbiquitousItemDownloadingStatusNotDownloaded: String ``` | OS X 10.9 |

Modified NSMetadataUbiquitousItemHasUnresolvedConflictsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataUbiquitousItemHasUnresolvedConflictsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataUbiquitousItemHasUnresolvedConflictsKey: String ``` | OS X 10.7 |

Modified NSMetadataUbiquitousItemIsDownloadingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataUbiquitousItemIsDownloadingKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataUbiquitousItemIsDownloadingKey: String ``` | OS X 10.7 |

Modified NSMetadataUbiquitousItemIsExternalDocumentKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemIsExternalDocumentKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemIsExternalDocumentKey: String ``` |

Modified NSMetadataUbiquitousItemIsUploadedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataUbiquitousItemIsUploadedKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataUbiquitousItemIsUploadedKey: String ``` | OS X 10.7 |

Modified NSMetadataUbiquitousItemIsUploadingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataUbiquitousItemIsUploadingKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataUbiquitousItemIsUploadingKey: String ``` | OS X 10.7 |

Modified NSMetadataUbiquitousItemPercentDownloadedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataUbiquitousItemPercentDownloadedKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataUbiquitousItemPercentDownloadedKey: String ``` | OS X 10.7 |

Modified NSMetadataUbiquitousItemPercentUploadedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataUbiquitousItemPercentUploadedKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataUbiquitousItemPercentUploadedKey: String ``` | OS X 10.7 |

Modified NSMetadataUbiquitousItemURLInLocalContainerKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMetadataUbiquitousItemURLInLocalContainerKey: NSString! ``` |
| To | ``` let NSMetadataUbiquitousItemURLInLocalContainerKey: String ``` |

Modified NSMetadataUbiquitousItemUploadingErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMetadataUbiquitousItemUploadingErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMetadataUbiquitousItemUploadingErrorKey: String ``` | OS X 10.9 |

Modified NSMinimumKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSMinimumKeyValueOperator: NSString! ``` |
| To | ``` let NSMinimumKeyValueOperator: String ``` |

Modified NSNegateBooleanTransformerName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSNegateBooleanTransformerName: NSString! ``` | OS X 10.10 |
| To | ``` let NSNegateBooleanTransformerName: String ``` | OS X 10.3 |

Modified NSNetServicesErrorCode

|  | Declaration |
| --- | --- |
| From | ``` let NSNetServicesErrorCode: NSString! ``` |
| To | ``` let NSNetServicesErrorCode: String ``` |

Modified NSNetServicesErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSNetServicesErrorDomain: NSString! ``` |
| To | ``` let NSNetServicesErrorDomain: String ``` |

Modified NSNextHashEnumeratorItem(UnsafeMutablePointer<NSHashEnumerator>) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func NSNextHashEnumeratorItem(_ enumerator: UnsafePointer<NSHashEnumerator>) -> UnsafePointer<()> ``` |
| To | ``` func NSNextHashEnumeratorItem(_ enumerator: UnsafeMutablePointer<NSHashEnumerator>) -> UnsafeMutablePointer<Void> ``` |

Modified NSNextMapEnumeratorPair(UnsafeMutablePointer<NSMapEnumerator>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func NSNextMapEnumeratorPair(_ enumerator: UnsafePointer<NSMapEnumerator>, _ key: UnsafePointer<UnsafePointer<()>>, _ value: UnsafePointer<UnsafePointer<()>>) -> Bool ``` |
| To | ``` func NSNextMapEnumeratorPair(_ enumerator: UnsafeMutablePointer<NSMapEnumerator>, _ key: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ value: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Bool ``` |

Modified NSOSStatusErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSOSStatusErrorDomain: NSString! ``` |
| To | ``` let NSOSStatusErrorDomain: String ``` |

Modified NSObjectInaccessibleException

|  | Declaration |
| --- | --- |
| From | ``` let NSObjectInaccessibleException: NSString! ``` |
| To | ``` let NSObjectInaccessibleException: String ``` |

Modified NSObjectNotAvailableException

|  | Declaration |
| --- | --- |
| From | ``` let NSObjectNotAvailableException: NSString! ``` |
| To | ``` let NSObjectNotAvailableException: String ``` |

Modified NSOldStyleException

|  | Declaration |
| --- | --- |
| From | ``` let NSOldStyleException: NSString! ``` |
| To | ``` let NSOldStyleException: String ``` |

Modified NSOperationNotSupportedForKeyException

|  | Declaration |
| --- | --- |
| From | ``` var NSOperationNotSupportedForKeyException: NSString! ``` |
| To | ``` let NSOperationNotSupportedForKeyException: String ``` |

Modified NSPOSIXErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSPOSIXErrorDomain: NSString! ``` |
| To | ``` let NSPOSIXErrorDomain: String ``` |

Modified NSParseErrorException

|  | Declaration |
| --- | --- |
| From | ``` let NSParseErrorException: NSString! ``` |
| To | ``` let NSParseErrorException: String ``` |

Modified NSPersianCalendar

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let NSPersianCalendar: NSString! ``` | OS X 10.10 | -- |
| To | ``` let NSPersianCalendar: String ``` | OS X 10.6 | OS X 10.10 |

Modified NSPointArray

|  | Declaration |
| --- | --- |
| From | ``` typealias NSPointArray = UnsafePointer<NSPoint> ``` |
| To | ``` typealias NSPointArray = UnsafeMutablePointer<NSPoint> ``` |

Modified NSPointPointer

|  | Declaration |
| --- | --- |
| From | ``` typealias NSPointPointer = UnsafePointer<NSPoint> ``` |
| To | ``` typealias NSPointPointer = UnsafeMutablePointer<NSPoint> ``` |

Modified NSPointerFunctionsCStringPersonality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPointerFunctionsCopyIn

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPointerFunctionsIntegerPersonality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPointerFunctionsMachVirtualMemory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPointerFunctionsMallocMemory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPointerFunctionsObjectPersonality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPointerFunctionsObjectPointerPersonality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPointerFunctionsOpaqueMemory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPointerFunctionsOpaquePersonality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPointerFunctionsStrongMemory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPointerFunctionsStructPersonality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPointerFunctionsWeakMemory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSPortDidBecomeInvalidNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSPortDidBecomeInvalidNotification: NSString! ``` |
| To | ``` let NSPortDidBecomeInvalidNotification: String ``` |

Modified NSPortReceiveException

|  | Declaration |
| --- | --- |
| From | ``` let NSPortReceiveException: NSString! ``` |
| To | ``` let NSPortReceiveException: String ``` |

Modified NSPortSendException

|  | Declaration |
| --- | --- |
| From | ``` let NSPortSendException: NSString! ``` |
| To | ``` let NSPortSendException: String ``` |

Modified NSPortTimeoutException

|  | Declaration |
| --- | --- |
| From | ``` let NSPortTimeoutException: NSString! ``` |
| To | ``` let NSPortTimeoutException: String ``` |

Modified NSProgressEstimatedTimeRemainingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSProgressEstimatedTimeRemainingKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSProgressEstimatedTimeRemainingKey: String ``` | OS X 10.9 |

Modified NSProgressFileAnimationImageKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSProgressFileAnimationImageKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSProgressFileAnimationImageKey: String ``` | OS X 10.9 |

Modified NSProgressFileAnimationImageOriginalRectKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSProgressFileAnimationImageOriginalRectKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSProgressFileAnimationImageOriginalRectKey: String ``` | OS X 10.9 |

Modified NSProgressFileCompletedCountKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSProgressFileCompletedCountKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSProgressFileCompletedCountKey: String ``` | OS X 10.9 |

Modified NSProgressFileIconKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSProgressFileIconKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSProgressFileIconKey: String ``` | OS X 10.9 |

Modified NSProgressFileOperationKindCopying

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSProgressFileOperationKindCopying: NSString! ``` | OS X 10.10 |
| To | ``` let NSProgressFileOperationKindCopying: String ``` | OS X 10.9 |

Modified NSProgressFileOperationKindDecompressingAfterDownloading

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSProgressFileOperationKindDecompressingAfterDownloading: NSString! ``` | OS X 10.10 |
| To | ``` let NSProgressFileOperationKindDecompressingAfterDownloading: String ``` | OS X 10.9 |

Modified NSProgressFileOperationKindDownloading

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSProgressFileOperationKindDownloading: NSString! ``` | OS X 10.10 |
| To | ``` let NSProgressFileOperationKindDownloading: String ``` | OS X 10.9 |

Modified NSProgressFileOperationKindKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSProgressFileOperationKindKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSProgressFileOperationKindKey: String ``` | OS X 10.9 |

Modified NSProgressFileOperationKindReceiving

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSProgressFileOperationKindReceiving: NSString! ``` | OS X 10.10 |
| To | ``` let NSProgressFileOperationKindReceiving: String ``` | OS X 10.9 |

Modified NSProgressFileTotalCountKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSProgressFileTotalCountKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSProgressFileTotalCountKey: String ``` | OS X 10.9 |

Modified NSProgressFileURLKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSProgressFileURLKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSProgressFileURLKey: String ``` | OS X 10.9 |

Modified NSProgressKindFile

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSProgressKindFile: NSString! ``` | OS X 10.10 |
| To | ``` let NSProgressKindFile: String ``` | OS X 10.9 |

Modified NSProgressThroughputKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSProgressThroughputKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSProgressThroughputKey: String ``` | OS X 10.9 |

Modified NSPropertyListErrorMaximum

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSPropertyListErrorMinimum

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSPropertyListReadCorruptError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSPropertyListReadStreamError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSPropertyListReadUnknownVersionError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSPropertyListWriteStreamError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSProtocolFromString(String!) -> Protocol!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSRangeException

|  | Declaration |
| --- | --- |
| From | ``` let NSRangeException: NSString! ``` |
| To | ``` let NSRangeException: String ``` |

Modified NSRangePointer

|  | Declaration |
| --- | --- |
| From | ``` typealias NSRangePointer = UnsafePointer<NSRange> ``` |
| To | ``` typealias NSRangePointer = UnsafeMutablePointer<NSRange> ``` |

Modified NSReallocateCollectable(UnsafeMutablePointer<Void>, Int, Int) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func NSReallocateCollectable(_ ptr: UnsafePointer<()>, _ size: Int, _ options: Int) -> UnsafePointer<()> ``` |
| To | ``` func NSReallocateCollectable(_ ptr: UnsafeMutablePointer<Void>, _ size: Int, _ options: Int) -> UnsafeMutablePointer<Void> ``` |

Modified NSRecoveryAttempterErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSRecoveryAttempterErrorKey: NSString! ``` |
| To | ``` let NSRecoveryAttempterErrorKey: String ``` |

Modified NSRectArray

|  | Declaration |
| --- | --- |
| From | ``` typealias NSRectArray = UnsafePointer<NSRect> ``` |
| To | ``` typealias NSRectArray = UnsafeMutablePointer<NSRect> ``` |

Modified NSRectPointer

|  | Declaration |
| --- | --- |
| From | ``` typealias NSRectPointer = UnsafePointer<NSRect> ``` |
| To | ``` typealias NSRectPointer = UnsafeMutablePointer<NSRect> ``` |

Modified NSRegistrationDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSRegistrationDomain: NSString! ``` |
| To | ``` let NSRegistrationDomain: String ``` |

Modified NSRepublicOfChinaCalendar

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let NSRepublicOfChinaCalendar: NSString! ``` | OS X 10.10 | -- |
| To | ``` let NSRepublicOfChinaCalendar: String ``` | OS X 10.6 | OS X 10.10 |

Modified NSRunLoopCommonModes

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSRunLoopCommonModes: NSString! ``` | OS X 10.10 |
| To | ``` let NSRunLoopCommonModes: String ``` | OS X 10.5 |

Modified NSSizeArray

|  | Declaration |
| --- | --- |
| From | ``` typealias NSSizeArray = UnsafePointer<NSSize> ``` |
| To | ``` typealias NSSizeArray = UnsafeMutablePointer<NSSize> ``` |

Modified NSSizePointer

|  | Declaration |
| --- | --- |
| From | ``` typealias NSSizePointer = UnsafePointer<NSSize> ``` |
| To | ``` typealias NSSizePointer = UnsafeMutablePointer<NSSize> ``` |

Modified NSStreamDataWrittenToMemoryStreamKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamDataWrittenToMemoryStreamKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamDataWrittenToMemoryStreamKey: String ``` | OS X 10.3 |

Modified NSStreamFileCurrentOffsetKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamFileCurrentOffsetKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamFileCurrentOffsetKey: String ``` | OS X 10.3 |

Modified NSStreamNetworkServiceType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamNetworkServiceType: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamNetworkServiceType: String ``` | OS X 10.7 |

Modified NSStreamNetworkServiceTypeBackground

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamNetworkServiceTypeBackground: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamNetworkServiceTypeBackground: String ``` | OS X 10.7 |

Modified NSStreamNetworkServiceTypeVideo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamNetworkServiceTypeVideo: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamNetworkServiceTypeVideo: String ``` | OS X 10.7 |

Modified NSStreamNetworkServiceTypeVoIP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamNetworkServiceTypeVoIP: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamNetworkServiceTypeVoIP: String ``` | OS X 10.7 |

Modified NSStreamNetworkServiceTypeVoice

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamNetworkServiceTypeVoice: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamNetworkServiceTypeVoice: String ``` | OS X 10.7 |

Modified NSStreamSOCKSErrorDomain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSOCKSErrorDomain: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSOCKSErrorDomain: String ``` | OS X 10.3 |

Modified NSStreamSOCKSProxyConfigurationKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSOCKSProxyConfigurationKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSOCKSProxyConfigurationKey: String ``` | OS X 10.3 |

Modified NSStreamSOCKSProxyHostKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSOCKSProxyHostKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSOCKSProxyHostKey: String ``` | OS X 10.3 |

Modified NSStreamSOCKSProxyPasswordKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSOCKSProxyPasswordKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSOCKSProxyPasswordKey: String ``` | OS X 10.3 |

Modified NSStreamSOCKSProxyPortKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSOCKSProxyPortKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSOCKSProxyPortKey: String ``` | OS X 10.3 |

Modified NSStreamSOCKSProxyUserKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSOCKSProxyUserKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSOCKSProxyUserKey: String ``` | OS X 10.3 |

Modified NSStreamSOCKSProxyVersion4

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSOCKSProxyVersion4: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSOCKSProxyVersion4: String ``` | OS X 10.3 |

Modified NSStreamSOCKSProxyVersion5

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSOCKSProxyVersion5: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSOCKSProxyVersion5: String ``` | OS X 10.3 |

Modified NSStreamSOCKSProxyVersionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSOCKSProxyVersionKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSOCKSProxyVersionKey: String ``` | OS X 10.3 |

Modified NSStreamSocketSSLErrorDomain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSocketSSLErrorDomain: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSocketSSLErrorDomain: String ``` | OS X 10.3 |

Modified NSStreamSocketSecurityLevelKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSocketSecurityLevelKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSocketSecurityLevelKey: String ``` | OS X 10.3 |

Modified NSStreamSocketSecurityLevelNegotiatedSSL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSocketSecurityLevelNegotiatedSSL: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSocketSecurityLevelNegotiatedSSL: String ``` | OS X 10.3 |

Modified NSStreamSocketSecurityLevelNone

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSocketSecurityLevelNone: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSocketSecurityLevelNone: String ``` | OS X 10.3 |

Modified NSStreamSocketSecurityLevelSSLv2

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSocketSecurityLevelSSLv2: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSocketSecurityLevelSSLv2: String ``` | OS X 10.3 |

Modified NSStreamSocketSecurityLevelSSLv3

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSocketSecurityLevelSSLv3: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSocketSecurityLevelSSLv3: String ``` | OS X 10.3 |

Modified NSStreamSocketSecurityLevelTLSv1

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStreamSocketSecurityLevelTLSv1: NSString! ``` | OS X 10.10 |
| To | ``` let NSStreamSocketSecurityLevelTLSv1: String ``` | OS X 10.3 |

Modified NSStringEncodingDetectionAllowLossyKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingDetectionAllowLossyKey: NSString! ``` |
| To | ``` let NSStringEncodingDetectionAllowLossyKey: String ``` |

Modified NSStringEncodingDetectionDisallowedEncodingsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingDetectionDisallowedEncodingsKey: NSString! ``` |
| To | ``` let NSStringEncodingDetectionDisallowedEncodingsKey: String ``` |

Modified NSStringEncodingDetectionFromWindowsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingDetectionFromWindowsKey: NSString! ``` |
| To | ``` let NSStringEncodingDetectionFromWindowsKey: String ``` |

Modified NSStringEncodingDetectionLikelyLanguageKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingDetectionLikelyLanguageKey: NSString! ``` |
| To | ``` let NSStringEncodingDetectionLikelyLanguageKey: String ``` |

Modified NSStringEncodingDetectionLossySubstitutionKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingDetectionLossySubstitutionKey: NSString! ``` |
| To | ``` let NSStringEncodingDetectionLossySubstitutionKey: String ``` |

Modified NSStringEncodingDetectionSuggestedEncodingsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingDetectionSuggestedEncodingsKey: NSString! ``` |
| To | ``` let NSStringEncodingDetectionSuggestedEncodingsKey: String ``` |

Modified NSStringEncodingDetectionUseOnlySuggestedEncodingsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingDetectionUseOnlySuggestedEncodingsKey: NSString! ``` |
| To | ``` let NSStringEncodingDetectionUseOnlySuggestedEncodingsKey: String ``` |

Modified NSStringEncodingErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStringEncodingErrorKey: NSString! ``` |
| To | ``` let NSStringEncodingErrorKey: String ``` |

Modified NSStringFromProtocol(Protocol!) -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSSumKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSSumKeyValueOperator: NSString! ``` |
| To | ``` let NSSumKeyValueOperator: String ``` |

Modified NSSystemClockDidChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSSystemClockDidChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSSystemClockDidChangeNotification: String ``` | OS X 10.6 |

Modified NSSystemTimeZoneDidChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSSystemTimeZoneDidChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSSystemTimeZoneDidChangeNotification: String ``` | OS X 10.5 |

Modified NSTaskDidTerminateNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSTaskDidTerminateNotification: NSString! ``` |
| To | ``` let NSTaskDidTerminateNotification: String ``` |

Modified NSTextCheckingAirlineKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSTextCheckingAirlineKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSTextCheckingAirlineKey: String ``` | OS X 10.7 |

Modified NSTextCheckingCityKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSTextCheckingCityKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSTextCheckingCityKey: String ``` | OS X 10.6 |

Modified NSTextCheckingCountryKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSTextCheckingCountryKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSTextCheckingCountryKey: String ``` | OS X 10.6 |

Modified NSTextCheckingFlightKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSTextCheckingFlightKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSTextCheckingFlightKey: String ``` | OS X 10.7 |

Modified NSTextCheckingJobTitleKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSTextCheckingJobTitleKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSTextCheckingJobTitleKey: String ``` | OS X 10.6 |

Modified NSTextCheckingNameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSTextCheckingNameKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSTextCheckingNameKey: String ``` | OS X 10.6 |

Modified NSTextCheckingOrganizationKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSTextCheckingOrganizationKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSTextCheckingOrganizationKey: String ``` | OS X 10.6 |

Modified NSTextCheckingPhoneKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSTextCheckingPhoneKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSTextCheckingPhoneKey: String ``` | OS X 10.6 |

Modified NSTextCheckingStateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSTextCheckingStateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSTextCheckingStateKey: String ``` | OS X 10.6 |

Modified NSTextCheckingStreetKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSTextCheckingStreetKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSTextCheckingStreetKey: String ``` | OS X 10.6 |

Modified NSTextCheckingZIPKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSTextCheckingZIPKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSTextCheckingZIPKey: String ``` | OS X 10.6 |

Modified NSThreadWillExitNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSThreadWillExitNotification: NSString! ``` |
| To | ``` let NSThreadWillExitNotification: String ``` |

Modified NSThumbnail1024x1024SizeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSThumbnail1024x1024SizeKey: NSString! ``` |
| To | ``` let NSThumbnail1024x1024SizeKey: String ``` |

Modified NSURLAddedToDirectoryDateKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAddedToDirectoryDateKey: NSString! ``` |
| To | ``` let NSURLAddedToDirectoryDateKey: String ``` |

Modified NSURLAttributeModificationDateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLAttributeModificationDateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLAttributeModificationDateKey: String ``` | OS X 10.6 |

Modified NSURLAuthenticationMethodClientCertificate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLAuthenticationMethodClientCertificate: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLAuthenticationMethodClientCertificate: String ``` | OS X 10.6 |

Modified NSURLAuthenticationMethodDefault

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAuthenticationMethodDefault: NSString! ``` |
| To | ``` let NSURLAuthenticationMethodDefault: String ``` |

Modified NSURLAuthenticationMethodHTMLForm

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAuthenticationMethodHTMLForm: NSString! ``` |
| To | ``` let NSURLAuthenticationMethodHTMLForm: String ``` |

Modified NSURLAuthenticationMethodHTTPBasic

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAuthenticationMethodHTTPBasic: NSString! ``` |
| To | ``` let NSURLAuthenticationMethodHTTPBasic: String ``` |

Modified NSURLAuthenticationMethodHTTPDigest

|  | Declaration |
| --- | --- |
| From | ``` let NSURLAuthenticationMethodHTTPDigest: NSString! ``` |
| To | ``` let NSURLAuthenticationMethodHTTPDigest: String ``` |

Modified NSURLAuthenticationMethodNTLM

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLAuthenticationMethodNTLM: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLAuthenticationMethodNTLM: String ``` | OS X 10.5 |

Modified NSURLAuthenticationMethodNegotiate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLAuthenticationMethodNegotiate: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLAuthenticationMethodNegotiate: String ``` | OS X 10.5 |

Modified NSURLAuthenticationMethodServerTrust

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLAuthenticationMethodServerTrust: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLAuthenticationMethodServerTrust: String ``` | OS X 10.6 |

Modified NSURLContentAccessDateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLContentAccessDateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLContentAccessDateKey: String ``` | OS X 10.6 |

Modified NSURLContentModificationDateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLContentModificationDateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLContentModificationDateKey: String ``` | OS X 10.6 |

Modified NSURLCreationDateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLCreationDateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLCreationDateKey: String ``` | OS X 10.6 |

Modified NSURLCredentialStorageChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSURLCredentialStorageChangedNotification: NSString! ``` |
| To | ``` let NSURLCredentialStorageChangedNotification: String ``` |

Modified NSURLCredentialStorageRemoveSynchronizableCredentials

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLCredentialStorageRemoveSynchronizableCredentials: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLCredentialStorageRemoveSynchronizableCredentials: String ``` | OS X 10.9 |

Modified NSURLCustomIconKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLCustomIconKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLCustomIconKey: String ``` | OS X 10.6 |

Modified NSURLDocumentIdentifierKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLDocumentIdentifierKey: NSString! ``` |
| To | ``` let NSURLDocumentIdentifierKey: String ``` |

Modified NSURLEffectiveIconKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLEffectiveIconKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLEffectiveIconKey: String ``` | OS X 10.6 |

Modified NSURLErrorBackgroundTaskCancelledReasonKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLErrorBackgroundTaskCancelledReasonKey: NSString! ``` |
| To | ``` let NSURLErrorBackgroundTaskCancelledReasonKey: String ``` |

Modified NSURLErrorCallIsActive

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSURLErrorDataLengthExceedsMaximum

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSURLErrorDataNotAllowed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSURLErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSURLErrorDomain: NSString! ``` |
| To | ``` let NSURLErrorDomain: String ``` |

Modified NSURLErrorFailingURLErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLErrorFailingURLErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLErrorFailingURLErrorKey: String ``` | OS X 10.6 |

Modified NSURLErrorFailingURLPeerTrustErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLErrorFailingURLPeerTrustErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLErrorFailingURLPeerTrustErrorKey: String ``` | OS X 10.6 |

Modified NSURLErrorFailingURLStringErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLErrorFailingURLStringErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLErrorFailingURLStringErrorKey: String ``` | OS X 10.6 |

Modified NSURLErrorInternationalRoamingOff

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSURLErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLErrorKey: NSString! ``` |
| To | ``` let NSURLErrorKey: String ``` |

Modified NSURLErrorRequestBodyStreamExhausted

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSURLFileAllocatedSizeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLFileAllocatedSizeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLFileAllocatedSizeKey: String ``` | OS X 10.6 |

Modified NSURLFileResourceIdentifierKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLFileResourceIdentifierKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLFileResourceIdentifierKey: String ``` | OS X 10.7 |

Modified NSURLFileResourceTypeBlockSpecial

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLFileResourceTypeBlockSpecial: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLFileResourceTypeBlockSpecial: String ``` | OS X 10.7 |

Modified NSURLFileResourceTypeCharacterSpecial

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLFileResourceTypeCharacterSpecial: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLFileResourceTypeCharacterSpecial: String ``` | OS X 10.7 |

Modified NSURLFileResourceTypeDirectory

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLFileResourceTypeDirectory: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLFileResourceTypeDirectory: String ``` | OS X 10.7 |

Modified NSURLFileResourceTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLFileResourceTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLFileResourceTypeKey: String ``` | OS X 10.7 |

Modified NSURLFileResourceTypeNamedPipe

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLFileResourceTypeNamedPipe: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLFileResourceTypeNamedPipe: String ``` | OS X 10.7 |

Modified NSURLFileResourceTypeRegular

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLFileResourceTypeRegular: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLFileResourceTypeRegular: String ``` | OS X 10.7 |

Modified NSURLFileResourceTypeSocket

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLFileResourceTypeSocket: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLFileResourceTypeSocket: String ``` | OS X 10.7 |

Modified NSURLFileResourceTypeSymbolicLink

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLFileResourceTypeSymbolicLink: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLFileResourceTypeSymbolicLink: String ``` | OS X 10.7 |

Modified NSURLFileResourceTypeUnknown

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLFileResourceTypeUnknown: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLFileResourceTypeUnknown: String ``` | OS X 10.7 |

Modified NSURLFileScheme

|  | Declaration |
| --- | --- |
| From | ``` var NSURLFileScheme: NSString! ``` |
| To | ``` let NSURLFileScheme: String ``` |

Modified NSURLFileSecurityKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLFileSecurityKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLFileSecurityKey: String ``` | OS X 10.7 |

Modified NSURLFileSizeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLFileSizeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLFileSizeKey: String ``` | OS X 10.6 |

Modified NSURLGenerationIdentifierKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLGenerationIdentifierKey: NSString! ``` |
| To | ``` let NSURLGenerationIdentifierKey: String ``` |

Modified NSURLHasHiddenExtensionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLHasHiddenExtensionKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLHasHiddenExtensionKey: String ``` | OS X 10.6 |

Modified NSURLIsAliasFileKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsAliasFileKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsAliasFileKey: String ``` | OS X 10.6 |

Modified NSURLIsDirectoryKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsDirectoryKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsDirectoryKey: String ``` | OS X 10.6 |

Modified NSURLIsExcludedFromBackupKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsExcludedFromBackupKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsExcludedFromBackupKey: String ``` | OS X 10.8 |

Modified NSURLIsExecutableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsExecutableKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsExecutableKey: String ``` | OS X 10.7 |

Modified NSURLIsHiddenKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsHiddenKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsHiddenKey: String ``` | OS X 10.6 |

Modified NSURLIsMountTriggerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsMountTriggerKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsMountTriggerKey: String ``` | OS X 10.7 |

Modified NSURLIsPackageKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsPackageKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsPackageKey: String ``` | OS X 10.6 |

Modified NSURLIsReadableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsReadableKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsReadableKey: String ``` | OS X 10.7 |

Modified NSURLIsRegularFileKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsRegularFileKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsRegularFileKey: String ``` | OS X 10.6 |

Modified NSURLIsSymbolicLinkKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsSymbolicLinkKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsSymbolicLinkKey: String ``` | OS X 10.6 |

Modified NSURLIsSystemImmutableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsSystemImmutableKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsSystemImmutableKey: String ``` | OS X 10.6 |

Modified NSURLIsUbiquitousItemKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsUbiquitousItemKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsUbiquitousItemKey: String ``` | OS X 10.7 |

Modified NSURLIsUserImmutableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsUserImmutableKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsUserImmutableKey: String ``` | OS X 10.6 |

Modified NSURLIsVolumeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsVolumeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsVolumeKey: String ``` | OS X 10.6 |

Modified NSURLIsWritableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLIsWritableKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLIsWritableKey: String ``` | OS X 10.7 |

Modified NSURLKeysOfUnsetValuesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLKeysOfUnsetValuesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLKeysOfUnsetValuesKey: String ``` | OS X 10.7 |

Modified NSURLLabelColorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLLabelColorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLLabelColorKey: String ``` | OS X 10.6 |

Modified NSURLLabelNumberKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLLabelNumberKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLLabelNumberKey: String ``` | OS X 10.6 |

Modified NSURLLinkCountKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLLinkCountKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLLinkCountKey: String ``` | OS X 10.6 |

Modified NSURLLocalizedLabelKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLLocalizedLabelKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLLocalizedLabelKey: String ``` | OS X 10.6 |

Modified NSURLLocalizedNameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLLocalizedNameKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLLocalizedNameKey: String ``` | OS X 10.6 |

Modified NSURLLocalizedTypeDescriptionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLLocalizedTypeDescriptionKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLLocalizedTypeDescriptionKey: String ``` | OS X 10.6 |

Modified NSURLNameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLNameKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLNameKey: String ``` | OS X 10.6 |

Modified NSURLParentDirectoryURLKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLParentDirectoryURLKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLParentDirectoryURLKey: String ``` | OS X 10.6 |

Modified NSURLPathKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLPathKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLPathKey: String ``` | OS X 10.8 |

Modified NSURLPreferredIOBlockSizeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLPreferredIOBlockSizeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLPreferredIOBlockSizeKey: String ``` | OS X 10.7 |

Modified NSURLProtectionSpaceFTP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLProtectionSpaceFTP: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLProtectionSpaceFTP: String ``` | OS X 10.5 |

Modified NSURLProtectionSpaceFTPProxy

|  | Declaration |
| --- | --- |
| From | ``` let NSURLProtectionSpaceFTPProxy: NSString! ``` |
| To | ``` let NSURLProtectionSpaceFTPProxy: String ``` |

Modified NSURLProtectionSpaceHTTP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLProtectionSpaceHTTP: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLProtectionSpaceHTTP: String ``` | OS X 10.5 |

Modified NSURLProtectionSpaceHTTPProxy

|  | Declaration |
| --- | --- |
| From | ``` let NSURLProtectionSpaceHTTPProxy: NSString! ``` |
| To | ``` let NSURLProtectionSpaceHTTPProxy: String ``` |

Modified NSURLProtectionSpaceHTTPS

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLProtectionSpaceHTTPS: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLProtectionSpaceHTTPS: String ``` | OS X 10.5 |

Modified NSURLProtectionSpaceHTTPSProxy

|  | Declaration |
| --- | --- |
| From | ``` let NSURLProtectionSpaceHTTPSProxy: NSString! ``` |
| To | ``` let NSURLProtectionSpaceHTTPSProxy: String ``` |

Modified NSURLProtectionSpaceSOCKSProxy

|  | Declaration |
| --- | --- |
| From | ``` let NSURLProtectionSpaceSOCKSProxy: NSString! ``` |
| To | ``` let NSURLProtectionSpaceSOCKSProxy: String ``` |

Modified NSURLQuarantinePropertiesKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLQuarantinePropertiesKey: NSString! ``` |
| To | ``` let NSURLQuarantinePropertiesKey: String ``` |

Modified NSURLSessionDownloadTaskResumeData

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLSessionDownloadTaskResumeData: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLSessionDownloadTaskResumeData: String ``` | OS X 10.9 |

Modified NSURLSessionTransferSizeUnknown

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSURLTagNamesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLTagNamesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLTagNamesKey: String ``` | OS X 10.9 |

Modified NSURLThumbnailDictionaryKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLThumbnailDictionaryKey: NSString! ``` |
| To | ``` let NSURLThumbnailDictionaryKey: String ``` |

Modified NSURLThumbnailKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLThumbnailKey: NSString! ``` |
| To | ``` let NSURLThumbnailKey: String ``` |

Modified NSURLTotalFileAllocatedSizeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLTotalFileAllocatedSizeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLTotalFileAllocatedSizeKey: String ``` | OS X 10.7 |

Modified NSURLTotalFileSizeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLTotalFileSizeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLTotalFileSizeKey: String ``` | OS X 10.7 |

Modified NSURLTypeIdentifierKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLTypeIdentifierKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLTypeIdentifierKey: String ``` | OS X 10.6 |

Modified NSURLUbiquitousItemContainerDisplayNameKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLUbiquitousItemContainerDisplayNameKey: NSString! ``` |
| To | ``` let NSURLUbiquitousItemContainerDisplayNameKey: String ``` |

Modified NSURLUbiquitousItemDownloadRequestedKey

|  | Declaration |
| --- | --- |
| From | ``` let NSURLUbiquitousItemDownloadRequestedKey: NSString! ``` |
| To | ``` let NSURLUbiquitousItemDownloadRequestedKey: String ``` |

Modified NSURLUbiquitousItemDownloadingErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLUbiquitousItemDownloadingErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLUbiquitousItemDownloadingErrorKey: String ``` | OS X 10.9 |

Modified NSURLUbiquitousItemDownloadingStatusCurrent

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLUbiquitousItemDownloadingStatusCurrent: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLUbiquitousItemDownloadingStatusCurrent: String ``` | OS X 10.9 |

Modified NSURLUbiquitousItemDownloadingStatusDownloaded

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLUbiquitousItemDownloadingStatusDownloaded: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLUbiquitousItemDownloadingStatusDownloaded: String ``` | OS X 10.9 |

Modified NSURLUbiquitousItemDownloadingStatusKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLUbiquitousItemDownloadingStatusKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLUbiquitousItemDownloadingStatusKey: String ``` | OS X 10.9 |

Modified NSURLUbiquitousItemDownloadingStatusNotDownloaded

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLUbiquitousItemDownloadingStatusNotDownloaded: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLUbiquitousItemDownloadingStatusNotDownloaded: String ``` | OS X 10.9 |

Modified NSURLUbiquitousItemHasUnresolvedConflictsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLUbiquitousItemHasUnresolvedConflictsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLUbiquitousItemHasUnresolvedConflictsKey: String ``` | OS X 10.7 |

Modified NSURLUbiquitousItemIsDownloadingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLUbiquitousItemIsDownloadingKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLUbiquitousItemIsDownloadingKey: String ``` | OS X 10.7 |

Modified NSURLUbiquitousItemIsUploadedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLUbiquitousItemIsUploadedKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLUbiquitousItemIsUploadedKey: String ``` | OS X 10.7 |

Modified NSURLUbiquitousItemIsUploadingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLUbiquitousItemIsUploadingKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLUbiquitousItemIsUploadingKey: String ``` | OS X 10.7 |

Modified NSURLUbiquitousItemUploadingErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLUbiquitousItemUploadingErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLUbiquitousItemUploadingErrorKey: String ``` | OS X 10.9 |

Modified NSURLVolumeAvailableCapacityKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeAvailableCapacityKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeAvailableCapacityKey: String ``` | OS X 10.6 |

Modified NSURLVolumeCreationDateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeCreationDateKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeCreationDateKey: String ``` | OS X 10.7 |

Modified NSURLVolumeIdentifierKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeIdentifierKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeIdentifierKey: String ``` | OS X 10.7 |

Modified NSURLVolumeIsAutomountedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeIsAutomountedKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeIsAutomountedKey: String ``` | OS X 10.7 |

Modified NSURLVolumeIsBrowsableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeIsBrowsableKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeIsBrowsableKey: String ``` | OS X 10.7 |

Modified NSURLVolumeIsEjectableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeIsEjectableKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeIsEjectableKey: String ``` | OS X 10.7 |

Modified NSURLVolumeIsInternalKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeIsInternalKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeIsInternalKey: String ``` | OS X 10.7 |

Modified NSURLVolumeIsJournalingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeIsJournalingKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeIsJournalingKey: String ``` | OS X 10.6 |

Modified NSURLVolumeIsLocalKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeIsLocalKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeIsLocalKey: String ``` | OS X 10.7 |

Modified NSURLVolumeIsReadOnlyKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeIsReadOnlyKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeIsReadOnlyKey: String ``` | OS X 10.7 |

Modified NSURLVolumeIsRemovableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeIsRemovableKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeIsRemovableKey: String ``` | OS X 10.7 |

Modified NSURLVolumeLocalizedFormatDescriptionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeLocalizedFormatDescriptionKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeLocalizedFormatDescriptionKey: String ``` | OS X 10.6 |

Modified NSURLVolumeLocalizedNameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeLocalizedNameKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeLocalizedNameKey: String ``` | OS X 10.7 |

Modified NSURLVolumeMaximumFileSizeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeMaximumFileSizeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeMaximumFileSizeKey: String ``` | OS X 10.7 |

Modified NSURLVolumeNameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeNameKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeNameKey: String ``` | OS X 10.7 |

Modified NSURLVolumeResourceCountKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeResourceCountKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeResourceCountKey: String ``` | OS X 10.6 |

Modified NSURLVolumeSupportsAdvisoryFileLockingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeSupportsAdvisoryFileLockingKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeSupportsAdvisoryFileLockingKey: String ``` | OS X 10.7 |

Modified NSURLVolumeSupportsCasePreservedNamesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeSupportsCasePreservedNamesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeSupportsCasePreservedNamesKey: String ``` | OS X 10.6 |

Modified NSURLVolumeSupportsCaseSensitiveNamesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeSupportsCaseSensitiveNamesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeSupportsCaseSensitiveNamesKey: String ``` | OS X 10.6 |

Modified NSURLVolumeSupportsExtendedSecurityKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeSupportsExtendedSecurityKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeSupportsExtendedSecurityKey: String ``` | OS X 10.7 |

Modified NSURLVolumeSupportsHardLinksKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeSupportsHardLinksKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeSupportsHardLinksKey: String ``` | OS X 10.6 |

Modified NSURLVolumeSupportsJournalingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeSupportsJournalingKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeSupportsJournalingKey: String ``` | OS X 10.6 |

Modified NSURLVolumeSupportsPersistentIDsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeSupportsPersistentIDsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeSupportsPersistentIDsKey: String ``` | OS X 10.6 |

Modified NSURLVolumeSupportsRenamingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeSupportsRenamingKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeSupportsRenamingKey: String ``` | OS X 10.7 |

Modified NSURLVolumeSupportsRootDirectoryDatesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeSupportsRootDirectoryDatesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeSupportsRootDirectoryDatesKey: String ``` | OS X 10.7 |

Modified NSURLVolumeSupportsSparseFilesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeSupportsSparseFilesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeSupportsSparseFilesKey: String ``` | OS X 10.6 |

Modified NSURLVolumeSupportsSymbolicLinksKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeSupportsSymbolicLinksKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeSupportsSymbolicLinksKey: String ``` | OS X 10.6 |

Modified NSURLVolumeSupportsVolumeSizesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeSupportsVolumeSizesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeSupportsVolumeSizesKey: String ``` | OS X 10.7 |

Modified NSURLVolumeSupportsZeroRunsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeSupportsZeroRunsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeSupportsZeroRunsKey: String ``` | OS X 10.6 |

Modified NSURLVolumeTotalCapacityKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeTotalCapacityKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeTotalCapacityKey: String ``` | OS X 10.6 |

Modified NSURLVolumeURLForRemountingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeURLForRemountingKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeURLForRemountingKey: String ``` | OS X 10.7 |

Modified NSURLVolumeURLKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeURLKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeURLKey: String ``` | OS X 10.6 |

Modified NSURLVolumeUUIDStringKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSURLVolumeUUIDStringKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSURLVolumeUUIDStringKey: String ``` | OS X 10.7 |

Modified NSUbiquitousFileErrorMaximum

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSUbiquitousFileErrorMinimum

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSUbiquitousFileNotUploadedDueToQuotaError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSUbiquitousFileUbiquityServerNotAvailable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSUbiquitousFileUnavailableError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSUbiquitousKeyValueStoreAccountChange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSUbiquitousKeyValueStoreChangeReasonKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUbiquitousKeyValueStoreChangeReasonKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSUbiquitousKeyValueStoreChangeReasonKey: String ``` | OS X 10.7 |

Modified NSUbiquitousKeyValueStoreChangedKeysKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUbiquitousKeyValueStoreChangedKeysKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSUbiquitousKeyValueStoreChangedKeysKey: String ``` | OS X 10.7 |

Modified NSUbiquitousKeyValueStoreDidChangeExternallyNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUbiquitousKeyValueStoreDidChangeExternallyNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSUbiquitousKeyValueStoreDidChangeExternallyNotification: String ``` | OS X 10.7 |

Modified NSUbiquitousKeyValueStoreInitialSyncChange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSUbiquitousKeyValueStoreQuotaViolationChange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSUbiquitousKeyValueStoreServerChange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSUbiquityIdentityDidChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUbiquityIdentityDidChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSUbiquityIdentityDidChangeNotification: String ``` | OS X 10.8 |

Modified NSUnarchiveFromDataTransformerName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUnarchiveFromDataTransformerName: NSString! ``` | OS X 10.10 |
| To | ``` let NSUnarchiveFromDataTransformerName: String ``` | OS X 10.3 |

Modified NSUndefinedDateComponent

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSUndefinedKeyException

|  | Declaration |
| --- | --- |
| From | ``` let NSUndefinedKeyException: NSString! ``` |
| To | ``` let NSUndefinedKeyException: String ``` |

Modified NSUnderlyingErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSUnderlyingErrorKey: NSString! ``` |
| To | ``` let NSUnderlyingErrorKey: String ``` |

Modified NSUndoManagerCheckpointNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUndoManagerCheckpointNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSUndoManagerCheckpointNotification: String ``` | OS X 10.0 |

Modified NSUndoManagerDidCloseUndoGroupNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUndoManagerDidCloseUndoGroupNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSUndoManagerDidCloseUndoGroupNotification: String ``` | OS X 10.7 |

Modified NSUndoManagerDidOpenUndoGroupNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUndoManagerDidOpenUndoGroupNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSUndoManagerDidOpenUndoGroupNotification: String ``` | OS X 10.0 |

Modified NSUndoManagerDidRedoChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUndoManagerDidRedoChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSUndoManagerDidRedoChangeNotification: String ``` | OS X 10.0 |

Modified NSUndoManagerDidUndoChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUndoManagerDidUndoChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSUndoManagerDidUndoChangeNotification: String ``` | OS X 10.0 |

Modified NSUndoManagerGroupIsDiscardableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUndoManagerGroupIsDiscardableKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSUndoManagerGroupIsDiscardableKey: String ``` | OS X 10.7 |

Modified NSUndoManagerWillCloseUndoGroupNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUndoManagerWillCloseUndoGroupNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSUndoManagerWillCloseUndoGroupNotification: String ``` | OS X 10.0 |

Modified NSUndoManagerWillRedoChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUndoManagerWillRedoChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSUndoManagerWillRedoChangeNotification: String ``` | OS X 10.0 |

Modified NSUndoManagerWillUndoChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUndoManagerWillUndoChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSUndoManagerWillUndoChangeNotification: String ``` | OS X 10.0 |

Modified NSUnionOfArraysKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSUnionOfArraysKeyValueOperator: NSString! ``` |
| To | ``` let NSUnionOfArraysKeyValueOperator: String ``` |

Modified NSUnionOfObjectsKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSUnionOfObjectsKeyValueOperator: NSString! ``` |
| To | ``` let NSUnionOfObjectsKeyValueOperator: String ``` |

Modified NSUnionOfSetsKeyValueOperator

|  | Declaration |
| --- | --- |
| From | ``` let NSUnionOfSetsKeyValueOperator: NSString! ``` |
| To | ``` let NSUnionOfSetsKeyValueOperator: String ``` |

Modified NSUserActivityTypeBrowsingWeb

|  | Declaration |
| --- | --- |
| From | ``` let NSUserActivityTypeBrowsingWeb: NSString! ``` |
| To | ``` let NSUserActivityTypeBrowsingWeb: String ``` |

Modified NSUserDefaultsDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSUserDefaultsDidChangeNotification: NSString! ``` |
| To | ``` let NSUserDefaultsDidChangeNotification: String ``` |

Modified NSUserNotificationDefaultSoundName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUserNotificationDefaultSoundName: NSString! ``` | OS X 10.10 |
| To | ``` let NSUserNotificationDefaultSoundName: String ``` | OS X 10.8 |

Modified NSWillBecomeMultiThreadedNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSWillBecomeMultiThreadedNotification: NSString! ``` |
| To | ``` let NSWillBecomeMultiThreadedNotification: String ``` |

Modified NSWrapCalendarComponents

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSXMLParserErrorDomain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSXMLParserErrorDomain: NSString! ``` | OS X 10.10 |
| To | ``` let NSXMLParserErrorDomain: String ``` | OS X 10.3 |

Modified NSXPCConnectionErrorMaximum

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSXPCConnectionErrorMinimum

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSXPCConnectionInterrupted

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSXPCConnectionInvalid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NSXPCConnectionReplyInvalid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

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
