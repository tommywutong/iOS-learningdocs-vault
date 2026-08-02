---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/XCTest.html
archived_at: '2026-07-18T02:55:46.345897Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# XCTest Changes for Swift

### XCTest

Removed XCTest.run() -> XCTestRunRemoved [XCUIKeyModifierFlags.None](https://developer.apple.com/documentation/xctest/xcuikeymodifierflags/xcuikeymodifiernone)Removed XCT_GENERICS_AVAILABLERemoved XCT_NULLABLE_AVAILABLERemoved [XCT_UI_TESTING_AVAILABLE](https://developer.apple.com/documentation/xctest/xct_ui_testing_available)Removed [XCTAssert(_: () throws -> BooleanType, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500669-xctassert)Removed [XCTAssertEqualWithAccuracy<T : FloatingPointType>(_: () throws -> T, _: () throws -> T, accuracy: T, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500646-xctassertequalwithaccuracy)Removed [XCTAssertFalse(_: () throws -> BooleanType, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500932-xctassertfalse)Removed [XCTAssertNotEqualWithAccuracy<T : FloatingPointType>(_: () throws -> T, _: () throws -> T, _: T, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500654-xctassertnotequalwithaccuracy)Removed [XCTAssertThrowsError<T>(_: () throws -> T, _: () -> String, file: StaticString, line: UInt, _: (error: ErrorType) -> Void)](https://developer.apple.com/documentation/xctest/1500795-xctassertthrowserror)Removed [XCTAssertTrue(_: () throws -> BooleanType, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500984-xctasserttrue)Added [XCT_UI_TESTING_AVAILABLE](https://developer.apple.com/documentation/xctest/xct_ui_testing_available)Added [XCTAssert(_: () throws -> Bool, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500669-xctassert)Added [XCTAssertEqual<T : Equatable>(_: () throws -> T, _: () throws -> T, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/2142776-xctassertequal)Added [XCTAssertEqualWithAccuracy<T : FloatingPoint>(_: () throws -> T, _: () throws -> T, accuracy: T, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500646-xctassertequalwithaccuracy)Added [XCTAssertFalse(_: () throws -> Bool, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500932-xctassertfalse)Added [XCTAssertNotEqual<T : Equatable>(_: () throws -> T, _: () throws -> T, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/2142777-xctassertnotequal)Added [XCTAssertNotEqualWithAccuracy<T : FloatingPoint>(_: () throws -> T, _: () throws -> T, _: T, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500654-xctassertnotequalwithaccuracy)Added [XCTAssertThrowsError<T>(_: () throws -> T, _: () -> String, file: StaticString, line: UInt, _: (Error) -> Swift.Void)](https://developer.apple.com/documentation/xctest/1500795-xctassertthrowserror)Added [XCTAssertTrue(_: () throws -> Bool, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500984-xctasserttrue)Modified [XCTest](https://developer.apple.com/documentation/xctest/xctest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class XCTest : NSObject {     var testCaseCount: UInt { get }     var name: String? { get }     var testRunClass: AnyClass? { get }     var testRun: XCTestRun? { get }     func performTest(_ run: XCTestRun)     func run() -> XCTestRun     func runTest()     func setUp()     func tearDown() } ``` | -- |
| To | ``` class XCTest : NSObject {     var testCaseCount: UInt { get }     var name: String? { get }     var testRunClass: Swift.AnyClass? { get }     var testRun: XCTestRun? { get }     func perform(_ run: XCTestRun)     func run()     func setUp()     func tearDown()     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension XCTest : CVarArg { } extension XCTest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [XCTest.perform(_: XCTestRun)](https://developer.apple.com/documentation/xctest/xctest/1500817-perform)

|  | Declaration |
| --- | --- |
| From | ``` func performTest(_ run: XCTestRun) ``` |
| To | ``` func perform(_ run: XCTestRun) ``` |

Modified [XCTest.run()](https://developer.apple.com/documentation/xctest/xctest/1501010-runtest)

|  | Declaration |
| --- | --- |
| From | ``` func runTest() ``` |
| To | ``` func run() ``` |

Modified [XCTest.testRunClass](https://developer.apple.com/documentation/xctest/xctest/1500950-testrunclass)

|  | Declaration |
| --- | --- |
| From | ``` var testRunClass: AnyClass? { get } ``` |
| To | ``` var testRunClass: Swift.AnyClass? { get } ``` |

Modified [XCTestCase](https://developer.apple.com/documentation/xctest/xctestcase)

|  | Declaration |
| --- | --- |
| From | ``` class XCTestCase : XCTest {     convenience init(invocation invocation: NSInvocation?)     class func testCaseWithInvocation(_ invocation: NSInvocation?) -> Self     init(invocation invocation: NSInvocation?)     convenience init(selector selector: Selector)     class func testCaseWithSelector(_ selector: Selector) -> Self     init(selector selector: Selector)     var invocation: NSInvocation?     func invokeTest()     var continueAfterFailure: Bool     func recordFailureWithDescription(_ description: String, inFile filePath: String, atLine lineNumber: UInt, expected expected: Bool)     class func testInvocations() -> [NSInvocation]     class func defaultPerformanceMetrics() -> [String]     func measureBlock(_ block: () -> Void)     func measureMetrics(_ metrics: [String], automaticallyStartMeasuring automaticallyStartMeasuring: Bool, forBlock block: () -> Void)     func startMeasuring()     func stopMeasuring()     func addUIInterruptionMonitorWithDescription(_ handlerDescription: String, handler handler: (XCUIElement) -> Bool) -> NSObjectProtocol     func removeUIInterruptionMonitor(_ monitor: NSObjectProtocol) } extension XCTestCase {     class func defaultTestSuite() -> XCTestSuite     class func setUp()     class func tearDown() } extension XCTestCase {     func expectationWithDescription(_ description: String) -> XCTestExpectation     func waitForExpectationsWithTimeout(_ timeout: NSTimeInterval, handler handler: XCWaitCompletionHandler?)     func keyValueObservingExpectationForObject(_ objectToObserve: AnyObject, keyPath keyPath: String, expectedValue expectedValue: AnyObject?) -> XCTestExpectation     func keyValueObservingExpectationForObject(_ objectToObserve: AnyObject, keyPath keyPath: String, handler handler: XCKeyValueObservingExpectationHandler?) -> XCTestExpectation     func expectationForNotification(_ notificationName: String, object objectToObserve: AnyObject?, handler handler: XCNotificationExpectationHandler?) -> XCTestExpectation     func expectationForPredicate(_ predicate: NSPredicate, evaluatedWithObject object: AnyObject, handler handler: XCPredicateExpectationHandler?) -> XCTestExpectation } ``` |
| To | ``` class XCTestCase : XCTest {     convenience init(invocation invocation: NSInvocation?)     class func withInvocation(_ invocation: NSInvocation?) -> Self     init(invocation invocation: NSInvocation?)     convenience init?(selector selector: Selector)     class func withSelector(_ selector: Selector) -> Self?     init(selector selector: Selector)     var invocation: NSInvocation?     func invokeTest()     var continueAfterFailure: Bool     func recordFailure(withDescription description: String, inFile filePath: String, atLine lineNumber: UInt, expected expected: Bool)     class func testInvocations() -> [NSInvocation]     class func defaultPerformanceMetrics() -> [String]     func measure(_ block: @escaping () -> Swift.Void)     func measureMetrics(_ metrics: [String], automaticallyStartMeasuring automaticallyStartMeasuring: Bool, for block: @escaping () -> Swift.Void)     func startMeasuring()     func stopMeasuring()     func addUIInterruptionMonitor(withDescription handlerDescription: String, handler handler: @escaping (XCUIElement) -> Bool) -> NSObjectProtocol     func removeUIInterruptionMonitor(_ monitor: NSObjectProtocol)     func expectation(description description: String) -> XCTestExpectation     func waitForExpectations(timeout timeout: TimeInterval, handler handler: XCTest.XCWaitCompletionHandler? = nil)     func keyValueObservingExpectation(for objectToObserve: Any, keyPath keyPath: String, expectedValue expectedValue: Any?) -> XCTestExpectation     func keyValueObservingExpectation(for objectToObserve: Any, keyPath keyPath: String, handler handler: XCTest.XCKeyValueObservingExpectationHandler? = nil) -> XCTestExpectation     func expectation(forNotification notificationName: String, object objectToObserve: Any?, handler handler: XCTest.XCNotificationExpectationHandler? = nil) -> XCTestExpectation     func expectation(for predicate: NSPredicate, evaluatedWith object: Any, handler handler: XCTest.XCPredicateExpectationHandler? = nil) -> XCTestExpectation     class func defaultTestSuite() -> XCTestSuite     class func setUp()     class func tearDown() } extension XCTestCase {     class func defaultTestSuite() -> XCTestSuite     class func setUp()     class func tearDown() } extension XCTestCase {     func expectation(description description: String) -> XCTestExpectation     func waitForExpectations(timeout timeout: TimeInterval, handler handler: XCTest.XCWaitCompletionHandler? = nil)     func keyValueObservingExpectation(for objectToObserve: Any, keyPath keyPath: String, expectedValue expectedValue: Any?) -> XCTestExpectation     func keyValueObservingExpectation(for objectToObserve: Any, keyPath keyPath: String, handler handler: XCTest.XCKeyValueObservingExpectationHandler? = nil) -> XCTestExpectation     func expectation(forNotification notificationName: String, object objectToObserve: Any?, handler handler: XCTest.XCNotificationExpectationHandler? = nil) -> XCTestExpectation     func expectation(for predicate: NSPredicate, evaluatedWith object: Any, handler handler: XCTest.XCPredicateExpectationHandler? = nil) -> XCTestExpectation } ``` |

Modified [XCTestCase.addUIInterruptionMonitor(withDescription: String, handler: (XCUIElement) -> Bool) -> NSObjectProtocol](https://developer.apple.com/documentation/xctest/xctestcase/1496273-adduiinterruptionmonitor)

|  | Declaration |
| --- | --- |
| From | ``` func addUIInterruptionMonitorWithDescription(_ handlerDescription: String, handler handler: (XCUIElement) -> Bool) -> NSObjectProtocol ``` |
| To | ``` func addUIInterruptionMonitor(withDescription handlerDescription: String, handler handler: @escaping (XCUIElement) -> Bool) -> NSObjectProtocol ``` |

Modified [XCTestCase.expectation(description: String) -> XCTestExpectation](https://developer.apple.com/documentation/xctest/xctestcase/1500899-expectationwithdescription)

|  | Declaration |
| --- | --- |
| From | ``` func expectationWithDescription(_ description: String) -> XCTestExpectation ``` |
| To | ``` func expectation(description description: String) -> XCTestExpectation ``` |

Modified [XCTestCase.expectation(for: NSPredicate, evaluatedWith: Any, handler: XCTest.XCPredicateExpectationHandler?) -> XCTestExpectation](https://developer.apple.com/documentation/xctest/xctestcase/1500569-expectation)

|  | Declaration |
| --- | --- |
| From | ``` func expectationForPredicate(_ predicate: NSPredicate, evaluatedWithObject object: AnyObject, handler handler: XCPredicateExpectationHandler?) -> XCTestExpectation ``` |
| To | ``` func expectation(for predicate: NSPredicate, evaluatedWith object: Any, handler handler: XCTest.XCPredicateExpectationHandler? = nil) -> XCTestExpectation ``` |

Modified [XCTestCase.expectation(forNotification: String, object: Any?, handler: XCTest.XCNotificationExpectationHandler?) -> XCTestExpectation](https://developer.apple.com/documentation/xctest/xctestcase/1500964-expectationfornotification)

|  | Declaration |
| --- | --- |
| From | ``` func expectationForNotification(_ notificationName: String, object objectToObserve: AnyObject?, handler handler: XCNotificationExpectationHandler?) -> XCTestExpectation ``` |
| To | ``` func expectation(forNotification notificationName: String, object objectToObserve: Any?, handler handler: XCTest.XCNotificationExpectationHandler? = nil) -> XCTestExpectation ``` |

Modified [XCTestCase.keyValueObservingExpectation(for: Any, keyPath: String, expectedValue: Any?) -> XCTestExpectation](https://developer.apple.com/documentation/xctest/xctestcase/1500612-keyvalueobservingexpectation)

|  | Declaration |
| --- | --- |
| From | ``` func keyValueObservingExpectationForObject(_ objectToObserve: AnyObject, keyPath keyPath: String, expectedValue expectedValue: AnyObject?) -> XCTestExpectation ``` |
| To | ``` func keyValueObservingExpectation(for objectToObserve: Any, keyPath keyPath: String, expectedValue expectedValue: Any?) -> XCTestExpectation ``` |

Modified [XCTestCase.keyValueObservingExpectation(for: Any, keyPath: String, handler: XCTest.XCKeyValueObservingExpectationHandler?) -> XCTestExpectation](https://developer.apple.com/documentation/xctest/xctestcase/1500318-keyvalueobservingexpectationforo)

|  | Declaration |
| --- | --- |
| From | ``` func keyValueObservingExpectationForObject(_ objectToObserve: AnyObject, keyPath keyPath: String, handler handler: XCKeyValueObservingExpectationHandler?) -> XCTestExpectation ``` |
| To | ``` func keyValueObservingExpectation(for objectToObserve: Any, keyPath keyPath: String, handler handler: XCTest.XCKeyValueObservingExpectationHandler? = nil) -> XCTestExpectation ``` |

Modified [XCTestCase.measure(_: () -> Swift.Void)](https://developer.apple.com/documentation/xctest/xctestcase/1496290-measureblock)

|  | Declaration |
| --- | --- |
| From | ``` func measureBlock(_ block: () -> Void) ``` |
| To | ``` func measure(_ block: @escaping () -> Swift.Void) ``` |

Modified [XCTestCase.measureMetrics(_: [String], automaticallyStartMeasuring: Bool, for: () -> Swift.Void)](https://developer.apple.com/documentation/xctest/xctestcase/1496277-measuremetrics)

|  | Declaration |
| --- | --- |
| From | ``` func measureMetrics(_ metrics: [String], automaticallyStartMeasuring automaticallyStartMeasuring: Bool, forBlock block: () -> Void) ``` |
| To | ``` func measureMetrics(_ metrics: [String], automaticallyStartMeasuring automaticallyStartMeasuring: Bool, for block: @escaping () -> Swift.Void) ``` |

Modified [XCTestCase.recordFailure(withDescription: String, inFile: String, atLine: UInt, expected: Bool)](https://developer.apple.com/documentation/xctest/xctestcase/1496269-recordfailure)

|  | Declaration |
| --- | --- |
| From | ``` func recordFailureWithDescription(_ description: String, inFile filePath: String, atLine lineNumber: UInt, expected expected: Bool) ``` |
| To | ``` func recordFailure(withDescription description: String, inFile filePath: String, atLine lineNumber: UInt, expected expected: Bool) ``` |

Modified [XCTestCase.waitForExpectations(timeout: TimeInterval, handler: XCTest.XCWaitCompletionHandler?)](https://developer.apple.com/documentation/xctest/xctestcase/1500748-waitforexpectationswithtimeout)

|  | Declaration |
| --- | --- |
| From | ``` func waitForExpectationsWithTimeout(_ timeout: NSTimeInterval, handler handler: XCWaitCompletionHandler?) ``` |
| To | ``` func waitForExpectations(timeout timeout: TimeInterval, handler handler: XCTest.XCWaitCompletionHandler? = nil) ``` |

Modified [XCTestCaseRun](https://developer.apple.com/documentation/xctest/xctestcaserun)

|  | Declaration |
| --- | --- |
| From | ``` class XCTestCaseRun : XCTestRun {     func recordFailureInTest(_ testCase: XCTestCase, withDescription description: String, inFile filePath: String, atLine lineNumber: UInt, expected expected: Bool) } ``` |
| To | ``` class XCTestCaseRun : XCTestRun {     func recordFailure(inTest testCase: XCTestCase, withDescription description: String, inFile filePath: String, atLine lineNumber: UInt, expected expected: Bool) } ``` |

Modified [XCTestCaseRun.recordFailure(inTest: XCTestCase, withDescription: String, inFile: String, atLine: UInt, expected: Bool)](https://developer.apple.com/documentation/xctest/xctestcaserun/1477503-recordfailureintest)

|  | Declaration |
| --- | --- |
| From | ``` func recordFailureInTest(_ testCase: XCTestCase, withDescription description: String, inFile filePath: String, atLine lineNumber: UInt, expected expected: Bool) ``` |
| To | ``` func recordFailure(inTest testCase: XCTestCase, withDescription description: String, inFile filePath: String, atLine lineNumber: UInt, expected expected: Bool) ``` |

Modified [XCTestErrorCode [enum]](https://developer.apple.com/documentation/xctest/xctesterrorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum XCTestErrorCode : Int {     case TimeoutWhileWaiting     case FailureWhileWaiting } ``` |
| To | ``` enum XCTestErrorCode : Int {     case timeoutWhileWaiting     case failureWhileWaiting } ``` |

Modified [XCTestErrorCode.failureWhileWaiting](https://developer.apple.com/documentation/xctest/xctesterrorcode/xctesterrorcodefailurewhilewaiting)

|  | Declaration |
| --- | --- |
| From | ``` case FailureWhileWaiting ``` |
| To | ``` case failureWhileWaiting ``` |

Modified [XCTestErrorCode.timeoutWhileWaiting](https://developer.apple.com/documentation/xctest/xctesterror/code/timeoutwhilewaiting)

|  | Declaration |
| --- | --- |
| From | ``` case TimeoutWhileWaiting ``` |
| To | ``` case timeoutWhileWaiting ``` |

Modified [XCTestExpectation](https://developer.apple.com/documentation/xctest/xctestexpectation)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class XCTestExpectation : NSObject {     func fulfill() } ``` | -- |
| To | ``` class XCTestExpectation : NSObject {     func fulfill()     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension XCTestExpectation : CVarArg { } extension XCTestExpectation : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [XCTestLog](https://developer.apple.com/documentation/xctest/xctestlog)

|  | Declaration |
| --- | --- |
| From | ``` class XCTestLog : XCTestObserver {     var logFileHandle: NSFileHandle! { get }     func testLogWithFormat(_ format: String!, arguments arguments: CVaListPointer) } ``` |
| To | ``` class XCTestLog : XCTestObserver {     var logFileHandle: FileHandle! { get }     func testLog(withFormat format: String!, arguments arguments: CVaListPointer!) } ``` |

Modified [XCTestLog.logFileHandle](https://developer.apple.com/documentation/xctest/xctestlog/1501032-logfilehandle)

|  | Declaration |
| --- | --- |
| From | ``` var logFileHandle: NSFileHandle! { get } ``` |
| To | ``` var logFileHandle: FileHandle! { get } ``` |

Modified [XCTestLog.testLog(withFormat: String!, arguments: CVaListPointer!)](https://developer.apple.com/documentation/xctest/xctestlog/1500608-testlog)

|  | Declaration |
| --- | --- |
| From | ``` func testLogWithFormat(_ format: String!, arguments arguments: CVaListPointer) ``` |
| To | ``` func testLog(withFormat format: String!, arguments arguments: CVaListPointer!) ``` |

Modified [XCTestObservation](https://developer.apple.com/documentation/xctest/xctestobservation)

|  | Declaration |
| --- | --- |
| From | ``` protocol XCTestObservation : NSObjectProtocol {     optional func testBundleWillStart(_ testBundle: NSBundle)     optional func testBundleDidFinish(_ testBundle: NSBundle)     optional func testSuiteWillStart(_ testSuite: XCTestSuite)     optional func testSuite(_ testSuite: XCTestSuite, didFailWithDescription description: String, inFile filePath: String?, atLine lineNumber: UInt)     optional func testSuiteDidFinish(_ testSuite: XCTestSuite)     optional func testCaseWillStart(_ testCase: XCTestCase)     optional func testCase(_ testCase: XCTestCase, didFailWithDescription description: String, inFile filePath: String?, atLine lineNumber: UInt)     optional func testCaseDidFinish(_ testCase: XCTestCase) } ``` |
| To | ``` protocol XCTestObservation : NSObjectProtocol {     optional func testBundleWillStart(_ testBundle: Bundle)     optional func testBundleDidFinish(_ testBundle: Bundle)     optional func testSuiteWillStart(_ testSuite: XCTestSuite)     optional func testSuite(_ testSuite: XCTestSuite, didFailWithDescription description: String, inFile filePath: String?, atLine lineNumber: UInt)     optional func testSuiteDidFinish(_ testSuite: XCTestSuite)     optional func testCaseWillStart(_ testCase: XCTestCase)     optional func testCase(_ testCase: XCTestCase, didFailWithDescription description: String, inFile filePath: String?, atLine lineNumber: UInt)     optional func testCaseDidFinish(_ testCase: XCTestCase) } ``` |

Modified [XCTestObservation.testBundleDidFinish(_: Bundle)](https://developer.apple.com/documentation/xctest/xctestobservation/1500819-testbundledidfinish)

|  | Declaration |
| --- | --- |
| From | ``` optional func testBundleDidFinish(_ testBundle: NSBundle) ``` |
| To | ``` optional func testBundleDidFinish(_ testBundle: Bundle) ``` |

Modified [XCTestObservation.testBundleWillStart(_: Bundle)](https://developer.apple.com/documentation/xctest/xctestobservation/1500772-testbundlewillstart)

|  | Declaration |
| --- | --- |
| From | ``` optional func testBundleWillStart(_ testBundle: NSBundle) ``` |
| To | ``` optional func testBundleWillStart(_ testBundle: Bundle) ``` |

Modified [XCTestObservationCenter](https://developer.apple.com/documentation/xctest/xctestobservationcenter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class XCTestObservationCenter : NSObject {     class func sharedTestObservationCenter() -> XCTestObservationCenter     func addTestObserver(_ testObserver: XCTestObservation)     func removeTestObserver(_ testObserver: XCTestObservation) } ``` | -- |
| To | ``` class XCTestObservationCenter : NSObject {     class func shared() -> XCTestObservationCenter     func addTestObserver(_ testObserver: XCTestObservation)     func removeTestObserver(_ testObserver: XCTestObservation)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension XCTestObservationCenter : CVarArg { } extension XCTestObservationCenter : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [XCTestObservationCenter.shared() -> XCTestObservationCenter [class]](https://developer.apple.com/documentation/xctest/xctestobservationcenter/1428315-sharedtestobservationcenter)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedTestObservationCenter() -> XCTestObservationCenter ``` |
| To | ``` class func shared() -> XCTestObservationCenter ``` |

Modified [XCTestObserver](https://developer.apple.com/documentation/xctest/xctestobserver)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class XCTestObserver : NSObject {     func startObserving()     func stopObserving()     func testSuiteDidStart(_ testRun: XCTestRun!)     func testSuiteDidStop(_ testRun: XCTestRun!)     func testCaseDidStart(_ testRun: XCTestRun!)     func testCaseDidStop(_ testRun: XCTestRun!)     func testCaseDidFail(_ testRun: XCTestRun!, withDescription description: String!, inFile filePath: String!, atLine lineNumber: UInt) } ``` | -- |
| To | ``` class XCTestObserver : NSObject {     func startObserving()     func stopObserving()     func testSuiteDidStart(_ testRun: XCTestRun!)     func testSuiteDidStop(_ testRun: XCTestRun!)     func testCaseDidStart(_ testRun: XCTestRun!)     func testCaseDidStop(_ testRun: XCTestRun!)     func testCaseDidFail(_ testRun: XCTestRun!, withDescription description: String!, inFile filePath: String!, atLine lineNumber: UInt)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension XCTestObserver : CVarArg { } extension XCTestObserver : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [XCTestProbe](https://developer.apple.com/documentation/xctest/xctestprobe)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class XCTestProbe : NSObject {     class func isTesting() -> Bool } ``` | -- |
| To | ``` class XCTestProbe : NSObject {     class func isTesting() -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension XCTestProbe : CVarArg { } extension XCTestProbe : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [XCTestRun](https://developer.apple.com/documentation/xctest/xctestrun)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class XCTestRun : NSObject {     convenience init(test test: XCTest)     class func testRunWithTest(_ test: XCTest) -> Self     init(test test: XCTest)     var test: XCTest { get }     func start()     func stop()     @NSCopying var startDate: NSDate? { get }     @NSCopying var stopDate: NSDate? { get }     var totalDuration: NSTimeInterval { get }     var testDuration: NSTimeInterval { get }     var testCaseCount: UInt { get }     var executionCount: UInt { get }     var failureCount: UInt { get }     var unexpectedExceptionCount: UInt { get }     var totalFailureCount: UInt { get }     var hasSucceeded: Bool { get }     func recordFailureWithDescription(_ description: String, inFile filePath: String?, atLine lineNumber: UInt, expected expected: Bool) } ``` | -- |
| To | ``` class XCTestRun : NSObject {     convenience init(test test: XCTest)     class func withTest(_ test: XCTest) -> Self     init(test test: XCTest)     var test: XCTest { get }     func start()     func stop()     var startDate: Date? { get }     var stopDate: Date? { get }     var totalDuration: TimeInterval { get }     var testDuration: TimeInterval { get }     var testCaseCount: UInt { get }     var executionCount: UInt { get }     var failureCount: UInt { get }     var unexpectedExceptionCount: UInt { get }     var totalFailureCount: UInt { get }     var hasSucceeded: Bool { get }     func recordFailure(withDescription description: String, inFile filePath: String?, atLine lineNumber: UInt, expected expected: Bool)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension XCTestRun : CVarArg { } extension XCTestRun : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [XCTestRun.recordFailure(withDescription: String, inFile: String?, atLine: UInt, expected: Bool)](https://developer.apple.com/documentation/xctest/xctestrun/1449632-recordfailurewithdescription)

|  | Declaration |
| --- | --- |
| From | ``` func recordFailureWithDescription(_ description: String, inFile filePath: String?, atLine lineNumber: UInt, expected expected: Bool) ``` |
| To | ``` func recordFailure(withDescription description: String, inFile filePath: String?, atLine lineNumber: UInt, expected expected: Bool) ``` |

Modified [XCTestRun.startDate](https://developer.apple.com/documentation/xctest/xctestrun/1449646-startdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var startDate: NSDate? { get } ``` |
| To | ``` var startDate: Date? { get } ``` |

Modified [XCTestRun.stopDate](https://developer.apple.com/documentation/xctest/xctestrun/1449648-stopdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var stopDate: NSDate? { get } ``` |
| To | ``` var stopDate: Date? { get } ``` |

Modified [XCTestRun.testDuration](https://developer.apple.com/documentation/xctest/xctestrun/1449635-testduration)

|  | Declaration |
| --- | --- |
| From | ``` var testDuration: NSTimeInterval { get } ``` |
| To | ``` var testDuration: TimeInterval { get } ``` |

Modified [XCTestRun.totalDuration](https://developer.apple.com/documentation/xctest/xctestrun/1449652-totalduration)

|  | Declaration |
| --- | --- |
| From | ``` var totalDuration: NSTimeInterval { get } ``` |
| To | ``` var totalDuration: TimeInterval { get } ``` |

Modified [XCTestSuite](https://developer.apple.com/documentation/xctest/xctestsuite)

|  | Declaration |
| --- | --- |
| From | ``` class XCTestSuite : XCTest {     class func defaultTestSuite() -> Self     convenience init(forBundlePath bundlePath: String)     class func testSuiteForBundlePath(_ bundlePath: String) -> Self     convenience init(forTestCaseWithName name: String)     class func testSuiteForTestCaseWithName(_ name: String) -> Self     convenience init(forTestCaseClass testCaseClass: AnyClass)     class func testSuiteForTestCaseClass(_ testCaseClass: AnyClass) -> Self     convenience init(name name: String)     class func testSuiteWithName(_ name: String) -> Self     init(name name: String)     func addTest(_ test: XCTest)     var tests: [XCTest] { get } } ``` |
| To | ``` class XCTestSuite : XCTest {     class func `default`() -> Self     convenience init(forBundlePath bundlePath: String)     class func forBundlePath(_ bundlePath: String) -> Self     convenience init(forTestCaseWithName name: String)     class func forTestCase(withName name: String) -> Self     convenience init(forTestCaseClass testCaseClass: Swift.AnyClass)     class func forTestCaseClass(_ testCaseClass: Swift.AnyClass) -> Self     convenience init(name name: String)     class func withName(_ name: String) -> Self     init(name name: String)     func addTest(_ test: XCTest)     var tests: [XCTest] { get } } ``` |

Modified [XCTestSuite.default() [class]](https://developer.apple.com/documentation/xctest/xctestsuite/1500584-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultTestSuite() -> Self ``` |
| To | ``` class func `default`() -> Self ``` |

Modified [XCTestSuite.init(forTestCaseClass: Swift.AnyClass)](https://developer.apple.com/documentation/xctest/xctestsuite/1500818-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(forTestCaseClass testCaseClass: AnyClass) ``` |
| To | ``` convenience init(forTestCaseClass testCaseClass: Swift.AnyClass) ``` |

Modified [XCUIApplication](https://developer.apple.com/documentation/xctest/xcuiapplication)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class XCUIApplication : XCUIElement {     func launch()     func terminate()     var launchArguments: [String]     var launchEnvironment: [String : String] } ``` | -- |
| To | ``` class XCUIApplication : XCUIElement {     func launch()     func terminate()     var launchArguments: [String]     var launchEnvironment: [String : String]     func adjust(toPickerWheelValue pickerWheelValue: String)     func adjust(toNormalizedSliderPosition normalizedSliderPosition: CGFloat)     var normalizedSliderPosition: CGFloat { get }     func typeText(_ text: String)     func tap()     func doubleTap()     func twoFingerTap()     func tap(withNumberOfTaps numberOfTaps: UInt, numberOfTouches numberOfTouches: UInt)     func press(forDuration duration: TimeInterval)     func press(forDuration duration: TimeInterval, thenDragTo otherElement: XCUIElement)     func swipeUp()     func swipeDown()     func swipeLeft()     func swipeRight()     func pinch(withScale scale: CGFloat, velocity velocity: CGFloat)     func rotate(_ rotation: CGFloat, withVelocity velocity: CGFloat)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension XCUIApplication : CVarArg { } extension XCUIApplication : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [XCUICoordinate](https://developer.apple.com/documentation/xctest/xcuicoordinate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class XCUICoordinate : NSObject, NSCopying {     init()     var referencedElement: XCUIElement { get }     var screenPoint: CGPoint { get }     func coordinateWithOffset(_ offsetVector: CGVector) -> XCUICoordinate     func tap()     func doubleTap()     func pressForDuration(_ duration: NSTimeInterval)     func pressForDuration(_ duration: NSTimeInterval, thenDragToCoordinate otherCoordinate: XCUICoordinate) } ``` | NSCopying |
| To | ``` class XCUICoordinate : NSObject, NSCopying {     init()     var referencedElement: XCUIElement { get }     var screenPoint: CGPoint { get }     func withOffset(_ offsetVector: CGVector) -> XCUICoordinate     func tap()     func doubleTap()     func press(forDuration duration: TimeInterval)     func press(forDuration duration: TimeInterval, thenDragTo otherCoordinate: XCUICoordinate)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension XCUICoordinate : CVarArg { } extension XCUICoordinate : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [XCUICoordinate.press(forDuration: TimeInterval)](https://developer.apple.com/documentation/xctest/xcuicoordinate/1615002-pressforduration)

|  | Declaration |
| --- | --- |
| From | ``` func pressForDuration(_ duration: NSTimeInterval) ``` |
| To | ``` func press(forDuration duration: TimeInterval) ``` |

Modified [XCUICoordinate.press(forDuration: TimeInterval, thenDragTo: XCUICoordinate)](https://developer.apple.com/documentation/xctest/xcuicoordinate/1615003-pressforduration)

|  | Declaration |
| --- | --- |
| From | ``` func pressForDuration(_ duration: NSTimeInterval, thenDragToCoordinate otherCoordinate: XCUICoordinate) ``` |
| To | ``` func press(forDuration duration: TimeInterval, thenDragTo otherCoordinate: XCUICoordinate) ``` |

Modified [XCUICoordinate.withOffset(_: CGVector) -> XCUICoordinate](https://developer.apple.com/documentation/xctest/xcuicoordinate/1500913-coordinatewithoffset)

|  | Declaration |
| --- | --- |
| From | ``` func coordinateWithOffset(_ offsetVector: CGVector) -> XCUICoordinate ``` |
| To | ``` func withOffset(_ offsetVector: CGVector) -> XCUICoordinate ``` |

Modified [XCUIDevice](https://developer.apple.com/documentation/xctest/xcuidevice)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class XCUIDevice : NSObject {     class func sharedDevice() -> XCUIDevice     var orientation: UIDeviceOrientation     func pressButton(_ button: XCUIDeviceButton) } ``` | -- |
| To | ``` class XCUIDevice : NSObject {     class func shared() -> XCUIDevice     var orientation: UIDeviceOrientation     func press(_ button: XCUIDeviceButton)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension XCUIDevice : CVarArg { } extension XCUIDevice : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [XCUIDevice.press(_: XCUIDeviceButton)](https://developer.apple.com/documentation/xctest/xcuidevice/1619052-press)

|  | Declaration |
| --- | --- |
| From | ``` func pressButton(_ button: XCUIDeviceButton) ``` |
| To | ``` func press(_ button: XCUIDeviceButton) ``` |

Modified [XCUIDevice.shared() -> XCUIDevice [class]](https://developer.apple.com/documentation/xctest/xcuidevice/1619048-shareddevice)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedDevice() -> XCUIDevice ``` |
| To | ``` class func shared() -> XCUIDevice ``` |

Modified [XCUIDeviceButton [enum]](https://developer.apple.com/documentation/xctest/xcuidevice/button)

|  | Declaration |
| --- | --- |
| From | ``` enum XCUIDeviceButton : Int {     case Home     case VolumeUp     case VolumeDown } ``` |
| To | ``` enum XCUIDeviceButton : Int {     case home     case volumeUp     case volumeDown } ``` |

Modified [XCUIDeviceButton.home](https://developer.apple.com/documentation/xctest/xcuidevicebutton/xcuidevicebuttonhome)

|  | Declaration |
| --- | --- |
| From | ``` case Home ``` |
| To | ``` case home ``` |

Modified [XCUIDeviceButton.volumeDown](https://developer.apple.com/documentation/xctest/xcuidevicebutton/xcuidevicebuttonvolumedown)

|  | Declaration |
| --- | --- |
| From | ``` case VolumeDown ``` |
| To | ``` case volumeDown ``` |

Modified [XCUIDeviceButton.volumeUp](https://developer.apple.com/documentation/xctest/xcuidevice/button/volumeup)

|  | Declaration |
| --- | --- |
| From | ``` case VolumeUp ``` |
| To | ``` case volumeUp ``` |

Modified [XCUIElement](https://developer.apple.com/documentation/xctest/xcuielement)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class XCUIElement : NSObject, XCUIElementAttributes, XCUIElementTypeQueryProvider {     var exists: Bool { get }     var hittable: Bool { get }     func descendantsMatchingType(_ type: XCUIElementType) -> XCUIElementQuery     func childrenMatchingType(_ type: XCUIElementType) -> XCUIElementQuery     func coordinateWithNormalizedOffset(_ normalizedOffset: CGVector) -> XCUICoordinate     var debugDescription: String { get } } extension XCUIElement {     func typeText(_ text: String)     func tap()     func doubleTap()     func twoFingerTap()     func tapWithNumberOfTaps(_ numberOfTaps: UInt, numberOfTouches numberOfTouches: UInt)     func pressForDuration(_ duration: NSTimeInterval)     func pressForDuration(_ duration: NSTimeInterval, thenDragToElement otherElement: XCUIElement)     func swipeUp()     func swipeDown()     func swipeLeft()     func swipeRight()     func pinchWithScale(_ scale: CGFloat, velocity velocity: CGFloat)     func rotate(_ rotation: CGFloat, withVelocity velocity: CGFloat) } extension XCUIElement {     func adjustToNormalizedSliderPosition(_ normalizedSliderPosition: CGFloat)     var normalizedSliderPosition: CGFloat { get } } extension XCUIElement {     func adjustToPickerWheelValue(_ pickerWheelValue: String) } ``` | XCUIElementAttributes, XCUIElementTypeQueryProvider |
| To | ``` class XCUIElement : NSObject, XCUIElementAttributes, XCUIElementTypeQueryProvider {     var exists: Bool { get }     var isHittable: Bool { get }     func descendants(matching type: XCUIElementType) -> XCUIElementQuery     func children(matching type: XCUIElementType) -> XCUIElementQuery     func coordinate(withNormalizedOffset normalizedOffset: CGVector) -> XCUICoordinate     var debugDescription: String { get }     func adjust(toPickerWheelValue pickerWheelValue: String)     func adjust(toNormalizedSliderPosition normalizedSliderPosition: CGFloat)     var normalizedSliderPosition: CGFloat { get }     func typeText(_ text: String)     func tap()     func doubleTap()     func twoFingerTap()     func tap(withNumberOfTaps numberOfTaps: UInt, numberOfTouches numberOfTouches: UInt)     func press(forDuration duration: TimeInterval)     func press(forDuration duration: TimeInterval, thenDragTo otherElement: XCUIElement)     func swipeUp()     func swipeDown()     func swipeLeft()     func swipeRight()     func pinch(withScale scale: CGFloat, velocity velocity: CGFloat)     func rotate(_ rotation: CGFloat, withVelocity velocity: CGFloat)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension XCUIElement : CVarArg { } extension XCUIElement : Equatable, Hashable {     var hashValue: Int { get } } extension XCUIElement {     func typeText(_ text: String)     func tap()     func doubleTap()     func twoFingerTap()     func tap(withNumberOfTaps numberOfTaps: UInt, numberOfTouches numberOfTouches: UInt)     func press(forDuration duration: TimeInterval)     func press(forDuration duration: TimeInterval, thenDragTo otherElement: XCUIElement)     func swipeUp()     func swipeDown()     func swipeLeft()     func swipeRight()     func pinch(withScale scale: CGFloat, velocity velocity: CGFloat)     func rotate(_ rotation: CGFloat, withVelocity velocity: CGFloat) } extension XCUIElement {     func adjust(toNormalizedSliderPosition normalizedSliderPosition: CGFloat)     var normalizedSliderPosition: CGFloat { get } } extension XCUIElement {     func adjust(toPickerWheelValue pickerWheelValue: String) } ``` | CVarArg, Equatable, Hashable, XCUIElementAttributes, XCUIElementTypeQueryProvider |

Modified [XCUIElement.adjust(toNormalizedSliderPosition: CGFloat)](https://developer.apple.com/documentation/xctest/xcuielement/1501022-adjust)

|  | Declaration |
| --- | --- |
| From | ``` func adjustToNormalizedSliderPosition(_ normalizedSliderPosition: CGFloat) ``` |
| To | ``` func adjust(toNormalizedSliderPosition normalizedSliderPosition: CGFloat) ``` |

Modified [XCUIElement.adjust(toPickerWheelValue: String)](https://developer.apple.com/documentation/xctest/xcuielement/1618672-adjusttopickerwheelvalue)

|  | Declaration |
| --- | --- |
| From | ``` func adjustToPickerWheelValue(_ pickerWheelValue: String) ``` |
| To | ``` func adjust(toPickerWheelValue pickerWheelValue: String) ``` |

Modified [XCUIElement.children(matching: XCUIElementType) -> XCUIElementQuery](https://developer.apple.com/documentation/xctest/xcuielement/1500877-children)

|  | Declaration |
| --- | --- |
| From | ``` func childrenMatchingType(_ type: XCUIElementType) -> XCUIElementQuery ``` |
| To | ``` func children(matching type: XCUIElementType) -> XCUIElementQuery ``` |

Modified [XCUIElement.coordinate(withNormalizedOffset: CGVector) -> XCUICoordinate](https://developer.apple.com/documentation/xctest/xcuielement/1500960-coordinatewithnormalizedoffset)

|  | Declaration |
| --- | --- |
| From | ``` func coordinateWithNormalizedOffset(_ normalizedOffset: CGVector) -> XCUICoordinate ``` |
| To | ``` func coordinate(withNormalizedOffset normalizedOffset: CGVector) -> XCUICoordinate ``` |

Modified [XCUIElement.descendants(matching: XCUIElementType) -> XCUIElementQuery](https://developer.apple.com/documentation/xctest/xcuielement/1500791-descendantsmatchingtype)

|  | Declaration |
| --- | --- |
| From | ``` func descendantsMatchingType(_ type: XCUIElementType) -> XCUIElementQuery ``` |
| To | ``` func descendants(matching type: XCUIElementType) -> XCUIElementQuery ``` |

Modified [XCUIElement.isHittable](https://developer.apple.com/documentation/xctest/xcuielement/1500561-hittable)

|  | Declaration |
| --- | --- |
| From | ``` var hittable: Bool { get } ``` |
| To | ``` var isHittable: Bool { get } ``` |

Modified [XCUIElement.pinch(withScale: CGFloat, velocity: CGFloat)](https://developer.apple.com/documentation/xctest/xcuielement/1618669-pinchwithscale)

|  | Declaration |
| --- | --- |
| From | ``` func pinchWithScale(_ scale: CGFloat, velocity velocity: CGFloat) ``` |
| To | ``` func pinch(withScale scale: CGFloat, velocity velocity: CGFloat) ``` |

Modified [XCUIElement.press(forDuration: TimeInterval)](https://developer.apple.com/documentation/xctest/xcuielement/1618663-press)

|  | Declaration |
| --- | --- |
| From | ``` func pressForDuration(_ duration: NSTimeInterval) ``` |
| To | ``` func press(forDuration duration: TimeInterval) ``` |

Modified [XCUIElement.press(forDuration: TimeInterval, thenDragTo: XCUIElement)](https://developer.apple.com/documentation/xctest/xcuielement/1618670-pressforduration)

|  | Declaration |
| --- | --- |
| From | ``` func pressForDuration(_ duration: NSTimeInterval, thenDragToElement otherElement: XCUIElement) ``` |
| To | ``` func press(forDuration duration: TimeInterval, thenDragTo otherElement: XCUIElement) ``` |

Modified [XCUIElement.tap(withNumberOfTaps: UInt, numberOfTouches: UInt)](https://developer.apple.com/documentation/xctest/xcuielement/1618671-tap)

|  | Declaration |
| --- | --- |
| From | ``` func tapWithNumberOfTaps(_ numberOfTaps: UInt, numberOfTouches numberOfTouches: UInt) ``` |
| To | ``` func tap(withNumberOfTaps numberOfTaps: UInt, numberOfTouches numberOfTouches: UInt) ``` |

Modified [XCUIElementAttributes](https://developer.apple.com/documentation/xctest/xcuielementattributes)

|  | Declaration |
| --- | --- |
| From | ``` protocol XCUIElementAttributes {     var identifier: String { get }     var frame: CGRect { get }     var value: AnyObject? { get }     var title: String { get }     var label: String { get }     var elementType: XCUIElementType { get }     var enabled: Bool { get }     var horizontalSizeClass: XCUIUserInterfaceSizeClass { get }     var verticalSizeClass: XCUIUserInterfaceSizeClass { get }     var placeholderValue: String? { get }     var selected: Bool { get } } ``` |
| To | ``` protocol XCUIElementAttributes {     var identifier: String { get }     var frame: CGRect { get }     var value: Any? { get }     var title: String { get }     var label: String { get }     var elementType: XCUIElementType { get }     var isEnabled: Bool { get }     var horizontalSizeClass: XCUIUserInterfaceSizeClass { get }     var verticalSizeClass: XCUIUserInterfaceSizeClass { get }     var placeholderValue: String? { get }     var isSelected: Bool { get } } ``` |

Modified [XCUIElementAttributes.isEnabled](https://developer.apple.com/documentation/xctest/xcuielementattributes/1500330-isenabled)

|  | Declaration |
| --- | --- |
| From | ``` var enabled: Bool { get } ``` |
| To | ``` var isEnabled: Bool { get } ``` |

Modified [XCUIElementAttributes.isSelected](https://developer.apple.com/documentation/xctest/xcuielementattributes/1500581-selected)

|  | Declaration |
| --- | --- |
| From | ``` var selected: Bool { get } ``` |
| To | ``` var isSelected: Bool { get } ``` |

Modified [XCUIElementAttributes.value](https://developer.apple.com/documentation/xctest/xcuielementattributes/1501015-value)

|  | Declaration |
| --- | --- |
| From | ``` var value: AnyObject? { get } ``` |
| To | ``` var value: Any? { get } ``` |

Modified [XCUIElementQuery](https://developer.apple.com/documentation/xctest/xcuielementquery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class XCUIElementQuery : NSObject, XCUIElementTypeQueryProvider {     var element: XCUIElement { get }     var count: UInt { get }     func elementAtIndex(_ index: UInt) -> XCUIElement     func elementBoundByIndex(_ index: UInt) -> XCUIElement     func elementMatchingPredicate(_ predicate: NSPredicate) -> XCUIElement     func elementMatchingType(_ elementType: XCUIElementType, identifier identifier: String?) -> XCUIElement     subscript (_ key: String) -> XCUIElement { get }     func objectForKeyedSubscript(_ key: String) -> XCUIElement     var allElementsBoundByAccessibilityElement: [XCUIElement] { get }     var allElementsBoundByIndex: [XCUIElement] { get }     func descendantsMatchingType(_ type: XCUIElementType) -> XCUIElementQuery     func childrenMatchingType(_ type: XCUIElementType) -> XCUIElementQuery     func matchingPredicate(_ predicate: NSPredicate) -> XCUIElementQuery     func matchingType(_ elementType: XCUIElementType, identifier identifier: String?) -> XCUIElementQuery     func matchingIdentifier(_ identifier: String) -> XCUIElementQuery     func containingPredicate(_ predicate: NSPredicate) -> XCUIElementQuery     func containingType(_ elementType: XCUIElementType, identifier identifier: String?) -> XCUIElementQuery     var debugDescription: String { get } } ``` | XCUIElementTypeQueryProvider |
| To | ``` class XCUIElementQuery : NSObject, XCUIElementTypeQueryProvider {     var element: XCUIElement { get }     var count: UInt { get }     func element(at index: UInt) -> XCUIElement     func element(boundBy index: UInt) -> XCUIElement     func element(matching predicate: NSPredicate) -> XCUIElement     func element(matching elementType: XCUIElementType, identifier identifier: String?) -> XCUIElement     subscript(_ key: String) -> XCUIElement { get }     func objectForKeyedSubscript(_ key: String) -> XCUIElement     var allElementsBoundByAccessibilityElement: [XCUIElement] { get }     var allElementsBoundByIndex: [XCUIElement] { get }     func descendants(matching type: XCUIElementType) -> XCUIElementQuery     func children(matching type: XCUIElementType) -> XCUIElementQuery     func matching(_ predicate: NSPredicate) -> XCUIElementQuery     func matching(_ elementType: XCUIElementType, identifier identifier: String?) -> XCUIElementQuery     func matching(identifier identifier: String) -> XCUIElementQuery     func containing(_ predicate: NSPredicate) -> XCUIElementQuery     func containing(_ elementType: XCUIElementType, identifier identifier: String?) -> XCUIElementQuery     var debugDescription: String { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension XCUIElementQuery : CVarArg { } extension XCUIElementQuery : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, XCUIElementTypeQueryProvider |

Modified [XCUIElementQuery.children(matching: XCUIElementType) -> XCUIElementQuery](https://developer.apple.com/documentation/xctest/xcuielementquery/1501006-children)

|  | Declaration |
| --- | --- |
| From | ``` func childrenMatchingType(_ type: XCUIElementType) -> XCUIElementQuery ``` |
| To | ``` func children(matching type: XCUIElementType) -> XCUIElementQuery ``` |

Modified [XCUIElementQuery.containing(_: NSPredicate) -> XCUIElementQuery](https://developer.apple.com/documentation/xctest/xcuielementquery/1500956-containingpredicate)

|  | Declaration |
| --- | --- |
| From | ``` func containingPredicate(_ predicate: NSPredicate) -> XCUIElementQuery ``` |
| To | ``` func containing(_ predicate: NSPredicate) -> XCUIElementQuery ``` |

Modified [XCUIElementQuery.containing(_: XCUIElementType, identifier: String?) -> XCUIElementQuery](https://developer.apple.com/documentation/xctest/xcuielementquery/1500995-containingtype)

|  | Declaration |
| --- | --- |
| From | ``` func containingType(_ elementType: XCUIElementType, identifier identifier: String?) -> XCUIElementQuery ``` |
| To | ``` func containing(_ elementType: XCUIElementType, identifier identifier: String?) -> XCUIElementQuery ``` |

Modified [XCUIElementQuery.descendants(matching: XCUIElementType) -> XCUIElementQuery](https://developer.apple.com/documentation/xctest/xcuielementquery/1500659-descendantsmatchingtype)

|  | Declaration |
| --- | --- |
| From | ``` func descendantsMatchingType(_ type: XCUIElementType) -> XCUIElementQuery ``` |
| To | ``` func descendants(matching type: XCUIElementType) -> XCUIElementQuery ``` |

Modified [XCUIElementQuery.element(at: UInt) -> XCUIElement](https://developer.apple.com/documentation/xctest/xcuielementquery/1500465-elementatindex)

|  | Declaration |
| --- | --- |
| From | ``` func elementAtIndex(_ index: UInt) -> XCUIElement ``` |
| To | ``` func element(at index: UInt) -> XCUIElement ``` |

Modified [XCUIElementQuery.element(boundBy: UInt) -> XCUIElement](https://developer.apple.com/documentation/xctest/xcuielementquery/1500842-element)

|  | Declaration |
| --- | --- |
| From | ``` func elementBoundByIndex(_ index: UInt) -> XCUIElement ``` |
| To | ``` func element(boundBy index: UInt) -> XCUIElement ``` |

Modified [XCUIElementQuery.element(matching: NSPredicate) -> XCUIElement](https://developer.apple.com/documentation/xctest/xcuielementquery/1500768-element)

|  | Declaration |
| --- | --- |
| From | ``` func elementMatchingPredicate(_ predicate: NSPredicate) -> XCUIElement ``` |
| To | ``` func element(matching predicate: NSPredicate) -> XCUIElement ``` |

Modified [XCUIElementQuery.element(matching: XCUIElementType, identifier: String?) -> XCUIElement](https://developer.apple.com/documentation/xctest/xcuielementquery/1500715-element)

|  | Declaration |
| --- | --- |
| From | ``` func elementMatchingType(_ elementType: XCUIElementType, identifier identifier: String?) -> XCUIElement ``` |
| To | ``` func element(matching elementType: XCUIElementType, identifier identifier: String?) -> XCUIElement ``` |

Modified [XCUIElementQuery.matching(_: NSPredicate) -> XCUIElementQuery](https://developer.apple.com/documentation/xctest/xcuielementquery/1500471-matchingpredicate)

|  | Declaration |
| --- | --- |
| From | ``` func matchingPredicate(_ predicate: NSPredicate) -> XCUIElementQuery ``` |
| To | ``` func matching(_ predicate: NSPredicate) -> XCUIElementQuery ``` |

Modified [XCUIElementQuery.matching(_: XCUIElementType, identifier: String?) -> XCUIElementQuery](https://developer.apple.com/documentation/xctest/xcuielementquery/1500881-matching)

|  | Declaration |
| --- | --- |
| From | ``` func matchingType(_ elementType: XCUIElementType, identifier identifier: String?) -> XCUIElementQuery ``` |
| To | ``` func matching(_ elementType: XCUIElementType, identifier identifier: String?) -> XCUIElementQuery ``` |

Modified [XCUIElementQuery.matching(identifier: String) -> XCUIElementQuery](https://developer.apple.com/documentation/xctest/xcuielementquery/1500679-matchingidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func matchingIdentifier(_ identifier: String) -> XCUIElementQuery ``` |
| To | ``` func matching(identifier identifier: String) -> XCUIElementQuery ``` |

Modified [XCUIElementQuery.subscript(_: String) -> XCUIElement](https://developer.apple.com/documentation/xctest/xcuielementquery/1500776-objectforkeyedsubscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ key: String) -> XCUIElement { get } ``` |
| To | ``` subscript(_ key: String) -> XCUIElement { get } ``` |

Modified [XCUIElementType [enum]](https://developer.apple.com/documentation/xctest/xcuielementtype)

|  | Declaration |
| --- | --- |
| From | ``` enum XCUIElementType : UInt {     case Any     case Other     case Application     case Group     case Window     case Sheet     case Drawer     case Alert     case Dialog     case Button     case RadioButton     case RadioGroup     case CheckBox     case DisclosureTriangle     case PopUpButton     case ComboBox     case MenuButton     case ToolbarButton     case Popover     case Keyboard     case Key     case NavigationBar     case TabBar     case TabGroup     case Toolbar     case StatusBar     case Table     case TableRow     case TableColumn     case Outline     case OutlineRow     case Browser     case CollectionView     case Slider     case PageIndicator     case ProgressIndicator     case ActivityIndicator     case SegmentedControl     case Picker     case PickerWheel     case Switch     case Toggle     case Link     case Image     case Icon     case SearchField     case ScrollView     case ScrollBar     case StaticText     case TextField     case SecureTextField     case DatePicker     case TextView     case Menu     case MenuItem     case MenuBar     case MenuBarItem     case Map     case WebView     case IncrementArrow     case DecrementArrow     case Timeline     case RatingIndicator     case ValueIndicator     case SplitGroup     case Splitter     case RelevanceIndicator     case ColorWell     case HelpTag     case Matte     case DockItem     case Ruler     case RulerMarker     case Grid     case LevelIndicator     case Cell     case LayoutArea     case LayoutItem     case Handle     case Stepper     case Tab } ``` |
| To | ``` enum XCUIElementType : UInt {     case any     case other     case application     case group     case window     case sheet     case drawer     case alert     case dialog     case button     case radioButton     case radioGroup     case checkBox     case disclosureTriangle     case popUpButton     case comboBox     case menuButton     case toolbarButton     case popover     case keyboard     case key     case navigationBar     case tabBar     case tabGroup     case toolbar     case statusBar     case table     case tableRow     case tableColumn     case outline     case outlineRow     case browser     case collectionView     case slider     case pageIndicator     case progressIndicator     case activityIndicator     case segmentedControl     case picker     case pickerWheel     case `switch`     case toggle     case link     case image     case icon     case searchField     case scrollView     case scrollBar     case staticText     case textField     case secureTextField     case datePicker     case textView     case menu     case menuItem     case menuBar     case menuBarItem     case map     case webView     case incrementArrow     case decrementArrow     case timeline     case ratingIndicator     case valueIndicator     case splitGroup     case splitter     case relevanceIndicator     case colorWell     case helpTag     case matte     case dockItem     case ruler     case rulerMarker     case grid     case levelIndicator     case cell     case layoutArea     case layoutItem     case handle     case stepper     case tab } ``` |

Modified [XCUIElementType.activityIndicator](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/activityindicator)

|  | Declaration |
| --- | --- |
| From | ``` case ActivityIndicator ``` |
| To | ``` case activityIndicator ``` |

Modified [XCUIElementType.alert](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/alert)

|  | Declaration |
| --- | --- |
| From | ``` case Alert ``` |
| To | ``` case alert ``` |

Modified [XCUIElementType.any](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/any)

|  | Declaration |
| --- | --- |
| From | ``` case Any ``` |
| To | ``` case any ``` |

Modified [XCUIElementType.application](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/application)

|  | Declaration |
| --- | --- |
| From | ``` case Application ``` |
| To | ``` case application ``` |

Modified [XCUIElementType.browser](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/browser)

|  | Declaration |
| --- | --- |
| From | ``` case Browser ``` |
| To | ``` case browser ``` |

Modified [XCUIElementType.button](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/button)

|  | Declaration |
| --- | --- |
| From | ``` case Button ``` |
| To | ``` case button ``` |

Modified [XCUIElementType.cell](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypecell)

|  | Declaration |
| --- | --- |
| From | ``` case Cell ``` |
| To | ``` case cell ``` |

Modified [XCUIElementType.checkBox](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypecheckbox)

|  | Declaration |
| --- | --- |
| From | ``` case CheckBox ``` |
| To | ``` case checkBox ``` |

Modified [XCUIElementType.collectionView](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypecollectionview)

|  | Declaration |
| --- | --- |
| From | ``` case CollectionView ``` |
| To | ``` case collectionView ``` |

Modified [XCUIElementType.colorWell](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypecolorwell)

|  | Declaration |
| --- | --- |
| From | ``` case ColorWell ``` |
| To | ``` case colorWell ``` |

Modified [XCUIElementType.comboBox](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypecombobox)

|  | Declaration |
| --- | --- |
| From | ``` case ComboBox ``` |
| To | ``` case comboBox ``` |

Modified [XCUIElementType.datePicker](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/datepicker)

|  | Declaration |
| --- | --- |
| From | ``` case DatePicker ``` |
| To | ``` case datePicker ``` |

Modified [XCUIElementType.decrementArrow](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/decrementarrow)

|  | Declaration |
| --- | --- |
| From | ``` case DecrementArrow ``` |
| To | ``` case decrementArrow ``` |

Modified [XCUIElementType.dialog](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/dialog)

|  | Declaration |
| --- | --- |
| From | ``` case Dialog ``` |
| To | ``` case dialog ``` |

Modified [XCUIElementType.disclosureTriangle](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypedisclosuretriangle)

|  | Declaration |
| --- | --- |
| From | ``` case DisclosureTriangle ``` |
| To | ``` case disclosureTriangle ``` |

Modified [XCUIElementType.dockItem](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/dockitem)

|  | Declaration |
| --- | --- |
| From | ``` case DockItem ``` |
| To | ``` case dockItem ``` |

Modified [XCUIElementType.drawer](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypedrawer)

|  | Declaration |
| --- | --- |
| From | ``` case Drawer ``` |
| To | ``` case drawer ``` |

Modified [XCUIElementType.grid](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/grid)

|  | Declaration |
| --- | --- |
| From | ``` case Grid ``` |
| To | ``` case grid ``` |

Modified [XCUIElementType.group](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/group)

|  | Declaration |
| --- | --- |
| From | ``` case Group ``` |
| To | ``` case group ``` |

Modified [XCUIElementType.handle](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/handle)

|  | Declaration |
| --- | --- |
| From | ``` case Handle ``` |
| To | ``` case handle ``` |

Modified [XCUIElementType.helpTag](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/helptag)

|  | Declaration |
| --- | --- |
| From | ``` case HelpTag ``` |
| To | ``` case helpTag ``` |

Modified [XCUIElementType.icon](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/icon)

|  | Declaration |
| --- | --- |
| From | ``` case Icon ``` |
| To | ``` case icon ``` |

Modified [XCUIElementType.image](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypeimage)

|  | Declaration |
| --- | --- |
| From | ``` case Image ``` |
| To | ``` case image ``` |

Modified [XCUIElementType.incrementArrow](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypeincrementarrow)

|  | Declaration |
| --- | --- |
| From | ``` case IncrementArrow ``` |
| To | ``` case incrementArrow ``` |

Modified [XCUIElementType.key](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/key)

|  | Declaration |
| --- | --- |
| From | ``` case Key ``` |
| To | ``` case key ``` |

Modified [XCUIElementType.keyboard](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/keyboard)

|  | Declaration |
| --- | --- |
| From | ``` case Keyboard ``` |
| To | ``` case keyboard ``` |

Modified [XCUIElementType.layoutArea](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/layoutarea)

|  | Declaration |
| --- | --- |
| From | ``` case LayoutArea ``` |
| To | ``` case layoutArea ``` |

Modified [XCUIElementType.layoutItem](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/layoutitem)

|  | Declaration |
| --- | --- |
| From | ``` case LayoutItem ``` |
| To | ``` case layoutItem ``` |

Modified [XCUIElementType.levelIndicator](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypelevelindicator)

|  | Declaration |
| --- | --- |
| From | ``` case LevelIndicator ``` |
| To | ``` case levelIndicator ``` |

Modified [XCUIElementType.link](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/link)

|  | Declaration |
| --- | --- |
| From | ``` case Link ``` |
| To | ``` case link ``` |

Modified [XCUIElementType.map](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypemap)

|  | Declaration |
| --- | --- |
| From | ``` case Map ``` |
| To | ``` case map ``` |

Modified [XCUIElementType.matte](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypematte)

|  | Declaration |
| --- | --- |
| From | ``` case Matte ``` |
| To | ``` case matte ``` |

Modified [XCUIElementType.menu](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/menu)

|  | Declaration |
| --- | --- |
| From | ``` case Menu ``` |
| To | ``` case menu ``` |

Modified [XCUIElementType.menuBar](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/menubar)

|  | Declaration |
| --- | --- |
| From | ``` case MenuBar ``` |
| To | ``` case menuBar ``` |

Modified [XCUIElementType.menuBarItem](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/menubaritem)

|  | Declaration |
| --- | --- |
| From | ``` case MenuBarItem ``` |
| To | ``` case menuBarItem ``` |

Modified [XCUIElementType.menuButton](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/menubutton)

|  | Declaration |
| --- | --- |
| From | ``` case MenuButton ``` |
| To | ``` case menuButton ``` |

Modified [XCUIElementType.menuItem](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/menuitem)

|  | Declaration |
| --- | --- |
| From | ``` case MenuItem ``` |
| To | ``` case menuItem ``` |

Modified [XCUIElementType.navigationBar](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/navigationbar)

|  | Declaration |
| --- | --- |
| From | ``` case NavigationBar ``` |
| To | ``` case navigationBar ``` |

Modified [XCUIElementType.other](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/other)

|  | Declaration |
| --- | --- |
| From | ``` case Other ``` |
| To | ``` case other ``` |

Modified [XCUIElementType.outline](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypeoutline)

|  | Declaration |
| --- | --- |
| From | ``` case Outline ``` |
| To | ``` case outline ``` |

Modified [XCUIElementType.outlineRow](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/outlinerow)

|  | Declaration |
| --- | --- |
| From | ``` case OutlineRow ``` |
| To | ``` case outlineRow ``` |

Modified [XCUIElementType.pageIndicator](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/pageindicator)

|  | Declaration |
| --- | --- |
| From | ``` case PageIndicator ``` |
| To | ``` case pageIndicator ``` |

Modified [XCUIElementType.picker](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypepicker)

|  | Declaration |
| --- | --- |
| From | ``` case Picker ``` |
| To | ``` case picker ``` |

Modified [XCUIElementType.pickerWheel](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/pickerwheel)

|  | Declaration |
| --- | --- |
| From | ``` case PickerWheel ``` |
| To | ``` case pickerWheel ``` |

Modified [XCUIElementType.popover](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypepopover)

|  | Declaration |
| --- | --- |
| From | ``` case Popover ``` |
| To | ``` case popover ``` |

Modified [XCUIElementType.popUpButton](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/popupbutton)

|  | Declaration |
| --- | --- |
| From | ``` case PopUpButton ``` |
| To | ``` case popUpButton ``` |

Modified [XCUIElementType.progressIndicator](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/progressindicator)

|  | Declaration |
| --- | --- |
| From | ``` case ProgressIndicator ``` |
| To | ``` case progressIndicator ``` |

Modified [XCUIElementType.radioButton](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtyperadiobutton)

|  | Declaration |
| --- | --- |
| From | ``` case RadioButton ``` |
| To | ``` case radioButton ``` |

Modified [XCUIElementType.radioGroup](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtyperadiogroup)

|  | Declaration |
| --- | --- |
| From | ``` case RadioGroup ``` |
| To | ``` case radioGroup ``` |

Modified [XCUIElementType.ratingIndicator](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/ratingindicator)

|  | Declaration |
| --- | --- |
| From | ``` case RatingIndicator ``` |
| To | ``` case ratingIndicator ``` |

Modified [XCUIElementType.relevanceIndicator](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/relevanceindicator)

|  | Declaration |
| --- | --- |
| From | ``` case RelevanceIndicator ``` |
| To | ``` case relevanceIndicator ``` |

Modified [XCUIElementType.ruler](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtyperuler)

|  | Declaration |
| --- | --- |
| From | ``` case Ruler ``` |
| To | ``` case ruler ``` |

Modified [XCUIElementType.rulerMarker](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/rulermarker)

|  | Declaration |
| --- | --- |
| From | ``` case RulerMarker ``` |
| To | ``` case rulerMarker ``` |

Modified [XCUIElementType.scrollBar](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypescrollbar)

|  | Declaration |
| --- | --- |
| From | ``` case ScrollBar ``` |
| To | ``` case scrollBar ``` |

Modified [XCUIElementType.scrollView](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/scrollview)

|  | Declaration |
| --- | --- |
| From | ``` case ScrollView ``` |
| To | ``` case scrollView ``` |

Modified [XCUIElementType.searchField](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypesearchfield)

|  | Declaration |
| --- | --- |
| From | ``` case SearchField ``` |
| To | ``` case searchField ``` |

Modified [XCUIElementType.secureTextField](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/securetextfield)

|  | Declaration |
| --- | --- |
| From | ``` case SecureTextField ``` |
| To | ``` case secureTextField ``` |

Modified [XCUIElementType.segmentedControl](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/segmentedcontrol)

|  | Declaration |
| --- | --- |
| From | ``` case SegmentedControl ``` |
| To | ``` case segmentedControl ``` |

Modified [XCUIElementType.sheet](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/sheet)

|  | Declaration |
| --- | --- |
| From | ``` case Sheet ``` |
| To | ``` case sheet ``` |

Modified [XCUIElementType.slider](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/slider)

|  | Declaration |
| --- | --- |
| From | ``` case Slider ``` |
| To | ``` case slider ``` |

Modified [XCUIElementType.splitGroup](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypesplitgroup)

|  | Declaration |
| --- | --- |
| From | ``` case SplitGroup ``` |
| To | ``` case splitGroup ``` |

Modified [XCUIElementType.splitter](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypesplitter)

|  | Declaration |
| --- | --- |
| From | ``` case Splitter ``` |
| To | ``` case splitter ``` |

Modified [XCUIElementType.staticText](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypestatictext)

|  | Declaration |
| --- | --- |
| From | ``` case StaticText ``` |
| To | ``` case staticText ``` |

Modified [XCUIElementType.statusBar](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/statusbar)

|  | Declaration |
| --- | --- |
| From | ``` case StatusBar ``` |
| To | ``` case statusBar ``` |

Modified [XCUIElementType.stepper](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypestepper)

|  | Declaration |
| --- | --- |
| From | ``` case Stepper ``` |
| To | ``` case stepper ``` |

Modified [XCUIElementType.switch](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/switch)

|  | Declaration |
| --- | --- |
| From | ``` case Switch ``` |
| To | ``` case `switch` ``` |

Modified [XCUIElementType.tab](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/tab)

|  | Declaration |
| --- | --- |
| From | ``` case Tab ``` |
| To | ``` case tab ``` |

Modified [XCUIElementType.tabBar](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypetabbar)

|  | Declaration |
| --- | --- |
| From | ``` case TabBar ``` |
| To | ``` case tabBar ``` |

Modified [XCUIElementType.tabGroup](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypetabgroup)

|  | Declaration |
| --- | --- |
| From | ``` case TabGroup ``` |
| To | ``` case tabGroup ``` |

Modified [XCUIElementType.table](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypetable)

|  | Declaration |
| --- | --- |
| From | ``` case Table ``` |
| To | ``` case table ``` |

Modified [XCUIElementType.tableColumn](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/tablecolumn)

|  | Declaration |
| --- | --- |
| From | ``` case TableColumn ``` |
| To | ``` case tableColumn ``` |

Modified [XCUIElementType.tableRow](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypetablerow)

|  | Declaration |
| --- | --- |
| From | ``` case TableRow ``` |
| To | ``` case tableRow ``` |

Modified [XCUIElementType.textField](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/textfield)

|  | Declaration |
| --- | --- |
| From | ``` case TextField ``` |
| To | ``` case textField ``` |

Modified [XCUIElementType.textView](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/textview)

|  | Declaration |
| --- | --- |
| From | ``` case TextView ``` |
| To | ``` case textView ``` |

Modified [XCUIElementType.timeline](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypetimeline)

|  | Declaration |
| --- | --- |
| From | ``` case Timeline ``` |
| To | ``` case timeline ``` |

Modified [XCUIElementType.toggle](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/toggle)

|  | Declaration |
| --- | --- |
| From | ``` case Toggle ``` |
| To | ``` case toggle ``` |

Modified [XCUIElementType.toolbar](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/toolbar)

|  | Declaration |
| --- | --- |
| From | ``` case Toolbar ``` |
| To | ``` case toolbar ``` |

Modified [XCUIElementType.toolbarButton](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypetoolbarbutton)

|  | Declaration |
| --- | --- |
| From | ``` case ToolbarButton ``` |
| To | ``` case toolbarButton ``` |

Modified [XCUIElementType.valueIndicator](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypevalueindicator)

|  | Declaration |
| --- | --- |
| From | ``` case ValueIndicator ``` |
| To | ``` case valueIndicator ``` |

Modified [XCUIElementType.webView](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/webview)

|  | Declaration |
| --- | --- |
| From | ``` case WebView ``` |
| To | ``` case webView ``` |

Modified [XCUIElementType.window](https://developer.apple.com/documentation/xctest/xcuielementtype/xcuielementtypewindow)

|  | Declaration |
| --- | --- |
| From | ``` case Window ``` |
| To | ``` case window ``` |

Modified [XCUIKeyModifierFlags [struct]](https://developer.apple.com/documentation/xctest/xcuielement/keymodifierflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct XCUIKeyModifierFlags : OptionSetType {     init(rawValue rawValue: UInt)     static var None: XCUIKeyModifierFlags { get }     static var AlphaShift: XCUIKeyModifierFlags { get }     static var Shift: XCUIKeyModifierFlags { get }     static var Control: XCUIKeyModifierFlags { get }     static var Alternate: XCUIKeyModifierFlags { get }     static var Option: XCUIKeyModifierFlags { get }     static var Command: XCUIKeyModifierFlags { get } } ``` | OptionSetType |
| To | ``` struct XCUIKeyModifierFlags : OptionSet {     init(rawValue rawValue: UInt)     static var none: XCUIKeyModifierFlags { get }     static var alphaShift: XCUIKeyModifierFlags { get }     static var shift: XCUIKeyModifierFlags { get }     static var control: XCUIKeyModifierFlags { get }     static var alternate: XCUIKeyModifierFlags { get }     static var option: XCUIKeyModifierFlags { get }     static var command: XCUIKeyModifierFlags { get }     func intersect(_ other: XCUIKeyModifierFlags) -> XCUIKeyModifierFlags     func exclusiveOr(_ other: XCUIKeyModifierFlags) -> XCUIKeyModifierFlags     mutating func unionInPlace(_ other: XCUIKeyModifierFlags)     mutating func intersectInPlace(_ other: XCUIKeyModifierFlags)     mutating func exclusiveOrInPlace(_ other: XCUIKeyModifierFlags)     func isSubsetOf(_ other: XCUIKeyModifierFlags) -> Bool     func isDisjointWith(_ other: XCUIKeyModifierFlags) -> Bool     func isSupersetOf(_ other: XCUIKeyModifierFlags) -> Bool     mutating func subtractInPlace(_ other: XCUIKeyModifierFlags)     func isStrictSupersetOf(_ other: XCUIKeyModifierFlags) -> Bool     func isStrictSubsetOf(_ other: XCUIKeyModifierFlags) -> Bool } extension XCUIKeyModifierFlags {     func union(_ other: XCUIKeyModifierFlags) -> XCUIKeyModifierFlags     func intersection(_ other: XCUIKeyModifierFlags) -> XCUIKeyModifierFlags     func symmetricDifference(_ other: XCUIKeyModifierFlags) -> XCUIKeyModifierFlags } extension XCUIKeyModifierFlags {     func contains(_ member: XCUIKeyModifierFlags) -> Bool     mutating func insert(_ newMember: XCUIKeyModifierFlags) -> (inserted: Bool, memberAfterInsert: XCUIKeyModifierFlags)     mutating func remove(_ member: XCUIKeyModifierFlags) -> XCUIKeyModifierFlags?     mutating func update(with newMember: XCUIKeyModifierFlags) -> XCUIKeyModifierFlags? } extension XCUIKeyModifierFlags {     convenience init()     mutating func formUnion(_ other: XCUIKeyModifierFlags)     mutating func formIntersection(_ other: XCUIKeyModifierFlags)     mutating func formSymmetricDifference(_ other: XCUIKeyModifierFlags) } extension XCUIKeyModifierFlags {     convenience init<S : Sequence where S.Iterator.Element == XCUIKeyModifierFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: XCUIKeyModifierFlags...)     mutating func subtract(_ other: XCUIKeyModifierFlags)     func isSubset(of other: XCUIKeyModifierFlags) -> Bool     func isSuperset(of other: XCUIKeyModifierFlags) -> Bool     func isDisjoint(with other: XCUIKeyModifierFlags) -> Bool     func subtracting(_ other: XCUIKeyModifierFlags) -> XCUIKeyModifierFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: XCUIKeyModifierFlags) -> Bool     func isStrictSubset(of other: XCUIKeyModifierFlags) -> Bool } ``` | OptionSet |

Modified [XCUIKeyModifierFlags.alphaShift](https://developer.apple.com/documentation/xctest/xcuielement/keymodifierflags/1500756-alphashift)

|  | Declaration |
| --- | --- |
| From | ``` static var AlphaShift: XCUIKeyModifierFlags { get } ``` |
| To | ``` static var alphaShift: XCUIKeyModifierFlags { get } ``` |

Modified [XCUIKeyModifierFlags.alternate](https://developer.apple.com/documentation/xctest/xcuikeymodifierflags/xcuikeymodifieralternate)

|  | Declaration |
| --- | --- |
| From | ``` static var Alternate: XCUIKeyModifierFlags { get } ``` |
| To | ``` static var alternate: XCUIKeyModifierFlags { get } ``` |

Modified [XCUIKeyModifierFlags.command](https://developer.apple.com/documentation/xctest/xcuielement/keymodifierflags/1500890-command)

|  | Declaration |
| --- | --- |
| From | ``` static var Command: XCUIKeyModifierFlags { get } ``` |
| To | ``` static var command: XCUIKeyModifierFlags { get } ``` |

Modified [XCUIKeyModifierFlags.control](https://developer.apple.com/documentation/xctest/xcuielement/keymodifierflags/1500641-control)

|  | Declaration |
| --- | --- |
| From | ``` static var Control: XCUIKeyModifierFlags { get } ``` |
| To | ``` static var control: XCUIKeyModifierFlags { get } ``` |

Modified [XCUIKeyModifierFlags.option](https://developer.apple.com/documentation/xctest/xcuielement/keymodifierflags/1500610-option)

|  | Declaration |
| --- | --- |
| From | ``` static var Option: XCUIKeyModifierFlags { get } ``` |
| To | ``` static var option: XCUIKeyModifierFlags { get } ``` |

Modified [XCUIKeyModifierFlags.shift](https://developer.apple.com/documentation/xctest/xcuielement/keymodifierflags/1500575-shift)

|  | Declaration |
| --- | --- |
| From | ``` static var Shift: XCUIKeyModifierFlags { get } ``` |
| To | ``` static var shift: XCUIKeyModifierFlags { get } ``` |

Modified [XCUIRemoteButton [enum]](https://developer.apple.com/documentation/xctest/xcuiremote/xcuiremotebutton)

|  | Declaration |
| --- | --- |
| From | ``` enum XCUIRemoteButton : UInt {     case Up     case Down     case Left     case Right     case Select     case Menu     case PlayPause } ``` |
| To | ``` enum XCUIRemoteButton : UInt {     case up     case down     case left     case right     case select     case menu     case playPause } ``` |

Modified [XCUIRemoteButton.down](https://developer.apple.com/documentation/xctest/xcuiremotebutton/xcuiremotebuttondown)

|  | Declaration |
| --- | --- |
| From | ``` case Down ``` |
| To | ``` case down ``` |

Modified [XCUIRemoteButton.left](https://developer.apple.com/documentation/xctest/xcuiremote/xcuiremotebutton/left)

|  | Declaration |
| --- | --- |
| From | ``` case Left ``` |
| To | ``` case left ``` |

Modified [XCUIRemoteButton.menu](https://developer.apple.com/documentation/xctest/xcuiremote/xcuiremotebutton/menu)

|  | Declaration |
| --- | --- |
| From | ``` case Menu ``` |
| To | ``` case menu ``` |

Modified [XCUIRemoteButton.playPause](https://developer.apple.com/documentation/xctest/xcuiremotebutton/xcuiremotebuttonplaypause)

|  | Declaration |
| --- | --- |
| From | ``` case PlayPause ``` |
| To | ``` case playPause ``` |

Modified [XCUIRemoteButton.right](https://developer.apple.com/documentation/xctest/xcuiremotebutton/xcuiremotebuttonright)

|  | Declaration |
| --- | --- |
| From | ``` case Right ``` |
| To | ``` case right ``` |

Modified [XCUIRemoteButton.select](https://developer.apple.com/documentation/xctest/xcuiremotebutton/xcuiremotebuttonselect)

|  | Declaration |
| --- | --- |
| From | ``` case Select ``` |
| To | ``` case select ``` |

Modified [XCUIRemoteButton.up](https://developer.apple.com/documentation/xctest/xcuiremotebutton/xcuiremotebuttonup)

|  | Declaration |
| --- | --- |
| From | ``` case Up ``` |
| To | ``` case up ``` |

Modified [XCUIUserInterfaceSizeClass [enum]](https://developer.apple.com/documentation/xctest/xcuiuserinterfacesizeclass)

|  | Declaration |
| --- | --- |
| From | ``` enum XCUIUserInterfaceSizeClass : Int {     case Unspecified     case Compact     case Regular } ``` |
| To | ``` enum XCUIUserInterfaceSizeClass : Int {     case unspecified     case compact     case regular } ``` |

Modified [XCUIUserInterfaceSizeClass.compact](https://developer.apple.com/documentation/xctest/xcuiuserinterfacesizeclass/xcuiuserinterfacesizeclasscompact)

|  | Declaration |
| --- | --- |
| From | ``` case Compact ``` |
| To | ``` case compact ``` |

Modified [XCUIUserInterfaceSizeClass.regular](https://developer.apple.com/documentation/xctest/xcuielement/sizeclass/regular)

|  | Declaration |
| --- | --- |
| From | ``` case Regular ``` |
| To | ``` case regular ``` |

Modified [XCUIUserInterfaceSizeClass.unspecified](https://developer.apple.com/documentation/xctest/xcuielement/sizeclass/unspecified)

|  | Declaration |
| --- | --- |
| From | ``` case Unspecified ``` |
| To | ``` case unspecified ``` |

Modified [XCKeyValueObservingExpectationHandler](https://developer.apple.com/documentation/xctest/xckeyvalueobservingexpectationhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias XCKeyValueObservingExpectationHandler = (AnyObject, [NSObject : AnyObject]) -> Bool ``` |
| To | ``` typealias XCKeyValueObservingExpectationHandler = (Any, [AnyHashable : Any]) -> Bool ``` |

Modified [XCNotificationExpectationHandler](https://developer.apple.com/documentation/xctest/xctnsnotificationexpectation/handler)

|  | Declaration |
| --- | --- |
| From | ``` typealias XCNotificationExpectationHandler = (NSNotification) -> Bool ``` |
| To | ``` typealias XCNotificationExpectationHandler = (Notification) -> Bool ``` |

Modified XCTAssertEqual<T : Equatable>(_: () throws -> T?, _: () throws -> T?, _: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertEqual<T : Equatable>(@autoclosure _ expression1: () throws -> T?, @autoclosure _ expression2: () throws -> T?, @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertEqual<T : Equatable>(_ expression1: @autoclosure () throws -> T?, _ expression2: @autoclosure () throws -> T?, _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified XCTAssertEqual<T : Equatable>(_: () throws -> [T], _: () throws -> [T], _: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertEqual<T : Equatable>(@autoclosure _ expression1: () throws -> [T], @autoclosure _ expression2: () throws -> [T], @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertEqual<T : Equatable>(_ expression1: @autoclosure () throws -> [T], _ expression2: @autoclosure () throws -> [T], _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified XCTAssertEqual<T, U : Equatable>(_: () throws -> [T : U], _: () throws -> [T : U], _: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertEqual<T, U : Equatable>(@autoclosure _ expression1: () throws -> [T : U], @autoclosure _ expression2: () throws -> [T : U], @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertEqual<T, U : Equatable>(_ expression1: @autoclosure () throws -> [T : U], _ expression2: @autoclosure () throws -> [T : U], _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified XCTAssertEqual<T : Equatable>(_: () throws -> ArraySlice<T>, _: () throws -> ArraySlice<T>, _: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertEqual<T : Equatable>(@autoclosure _ expression1: () throws -> ArraySlice<T>, @autoclosure _ expression2: () throws -> ArraySlice<T>, @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertEqual<T : Equatable>(_ expression1: @autoclosure () throws -> ArraySlice<T>, _ expression2: @autoclosure () throws -> ArraySlice<T>, _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified XCTAssertEqual<T : Equatable>(_: () throws -> ContiguousArray<T>, _: () throws -> ContiguousArray<T>, _: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertEqual<T : Equatable>(@autoclosure _ expression1: () throws -> ContiguousArray<T>, @autoclosure _ expression2: () throws -> ContiguousArray<T>, @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertEqual<T : Equatable>(_ expression1: @autoclosure () throws -> ContiguousArray<T>, _ expression2: @autoclosure () throws -> ContiguousArray<T>, _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified [XCTAssertGreaterThan<T : Comparable>(_: () throws -> T, _: () throws -> T, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500938-xctassertgreaterthan)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertGreaterThan<T : Comparable>(@autoclosure _ expression1: () throws -> T, @autoclosure _ expression2: () throws -> T, @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertGreaterThan<T : Comparable>(_ expression1: @autoclosure () throws -> T, _ expression2: @autoclosure () throws -> T, _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified [XCTAssertGreaterThanOrEqual<T : Comparable>(_: () throws -> T, _: () throws -> T, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500833-xctassertgreaterthanorequal)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertGreaterThanOrEqual<T : Comparable>(@autoclosure _ expression1: () throws -> T, @autoclosure _ expression2: () throws -> T, @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertGreaterThanOrEqual<T : Comparable>(_ expression1: @autoclosure () throws -> T, _ expression2: @autoclosure () throws -> T, _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified [XCTAssertLessThan<T : Comparable>(_: () throws -> T, _: () throws -> T, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500384-xctassertlessthan)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertLessThan<T : Comparable>(@autoclosure _ expression1: () throws -> T, @autoclosure _ expression2: () throws -> T, @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertLessThan<T : Comparable>(_ expression1: @autoclosure () throws -> T, _ expression2: @autoclosure () throws -> T, _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified [XCTAssertLessThanOrEqual<T : Comparable>(_: () throws -> T, _: () throws -> T, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500804-xctassertlessthanorequal)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertLessThanOrEqual<T : Comparable>(@autoclosure _ expression1: () throws -> T, @autoclosure _ expression2: () throws -> T, @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertLessThanOrEqual<T : Comparable>(_ expression1: @autoclosure () throws -> T, _ expression2: @autoclosure () throws -> T, _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified [XCTAssertNil(_: () throws -> Any?, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500523-xctassertnil)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertNil(@autoclosure _ expression: () throws -> Any?, @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertNil(_ expression: @autoclosure () throws -> Any?, _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified XCTAssertNotEqual<T : Equatable>(_: () throws -> [T], _: () throws -> [T], _: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertNotEqual<T : Equatable>(@autoclosure _ expression1: () throws -> [T], @autoclosure _ expression2: () throws -> [T], @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertNotEqual<T : Equatable>(_ expression1: @autoclosure () throws -> [T], _ expression2: @autoclosure () throws -> [T], _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified XCTAssertNotEqual<T, U : Equatable>(_: () throws -> [T : U], _: () throws -> [T : U], _: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertNotEqual<T, U : Equatable>(@autoclosure _ expression1: () throws -> [T : U], @autoclosure _ expression2: () throws -> [T : U], @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertNotEqual<T, U : Equatable>(_ expression1: @autoclosure () throws -> [T : U], _ expression2: @autoclosure () throws -> [T : U], _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified XCTAssertNotEqual<T : Equatable>(_: () throws -> ArraySlice<T>, _: () throws -> ArraySlice<T>, _: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertNotEqual<T : Equatable>(@autoclosure _ expression1: () throws -> ArraySlice<T>, @autoclosure _ expression2: () throws -> ArraySlice<T>, @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertNotEqual<T : Equatable>(_ expression1: @autoclosure () throws -> ArraySlice<T>, _ expression2: @autoclosure () throws -> ArraySlice<T>, _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified XCTAssertNotEqual<T : Equatable>(_: () throws -> ContiguousArray<T>, _: () throws -> ContiguousArray<T>, _: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertNotEqual<T : Equatable>(@autoclosure _ expression1: () throws -> ContiguousArray<T>, @autoclosure _ expression2: () throws -> ContiguousArray<T>, @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertNotEqual<T : Equatable>(_ expression1: @autoclosure () throws -> ContiguousArray<T>, _ expression2: @autoclosure () throws -> ContiguousArray<T>, _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified XCTAssertNotEqual<T : Equatable>(_: () throws -> T?, _: () throws -> T?, _: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertNotEqual<T : Equatable>(@autoclosure _ expression1: () throws -> T?, @autoclosure _ expression2: () throws -> T?, @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertNotEqual<T : Equatable>(_ expression1: @autoclosure () throws -> T?, _ expression2: @autoclosure () throws -> T?, _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified [XCTAssertNotNil(_: () throws -> Any?, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/xctest/1500453-xctassertnotnil)

|  | Declaration |
| --- | --- |
| From | ``` func XCTAssertNotNil(@autoclosure _ expression: () throws -> Any?, @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |
| To | ``` func XCTAssertNotNil(_ expression: @autoclosure () throws -> Any?, _ message: @autoclosure () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified [XCWaitCompletionHandler](https://developer.apple.com/documentation/xctest/xcwaitcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias XCWaitCompletionHandler = (NSError?) -> Void ``` |
| To | ``` typealias XCWaitCompletionHandler = (Error?) -> Swift.Void ``` |

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
