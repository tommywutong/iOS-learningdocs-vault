---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/StdlibUnittest.html
archived_at: '2026-07-18T02:56:16.468950Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# StdlibUnittest Changes

## StdlibUnittest

Removed TestCase [struct]Removed TestCase.init(_: String)Removed TestCase.nameRemoved TestCase.run()Removed TestCase.test(String, testFunction:() -> ())Removed asHex([UInt32]) -> StringRemoved asHex([UInt8]) -> StringRemoved expectFalse(Bool, StdlibUnittest.SourceLocStack?, String, UWord)Removed expectFalse(StdlibUnittest.AssertionResult, StdlibUnittest.SourceLocStack?, String, UWord)Removed expectTrue(Bool, StdlibUnittest.SourceLocStack?, String, UWord)Removed expectTrue(StdlibUnittest.AssertionResult, StdlibUnittest.SourceLocStack?, String, UWord)Added LifetimeTrackedAdded LifetimeTracked.deinitAdded LifetimeTracked.init(_: Int)Added LifetimeTracked.descriptionAdded LifetimeTracked.instancesAdded LifetimeTracked.serialNumberAdded LifetimeTracked.successor() -> StdlibUnittest.LifetimeTrackedAdded LifetimeTracked.valueAdded OSVersion [enum]Added OSVersion.OSXAdded OSVersion.descriptionAdded OSVersion.iOSAdded OSVersion.iOSSimulatorAdded Observation1UWord [struct]Added Observation1UWord.init(_: UWord)Added Observation1UWord.descriptionAdded Observation1UWord.uw1Added Observation4UWord [struct]Added Observation4UWord.init(_: UWord, _: UWord, _: UWord, _: UWord)Added Observation4UWord.descriptionAdded Observation4UWord.uw1Added Observation4UWord.uw2Added Observation4UWord.uw3Added Observation4UWord.uw4Added Observation4Word [struct]Added Observation4Word.init(_: Word, _: Word, _: Word, _: Word)Added Observation4Word.descriptionAdded Observation4Word.w1Added Observation4Word.w2Added Observation4Word.w3Added Observation4Word.w4Added ProcessTerminationStatus [enum]Added ProcessTerminationStatus.ExitAdded ProcessTerminationStatus.SignalAdded ProcessTerminationStatus.descriptionAdded ProcessTerminationStatus.isSwiftTrapAdded RaceTestObservationEvaluation [enum]Added RaceTestObservationEvaluation.FailureAdded RaceTestObservationEvaluation.FailureInterestingAdded RaceTestObservationEvaluation.PassAdded RaceTestObservationEvaluation.PassInterestingAdded RaceTestObservationEvaluation.descriptionAdded RaceTestWithPerTrialDataTypeAdded RaceTestWithPerTrialDataType.init()Added RaceTestWithPerTrialDataType.evaluateObservations([Observation], _: S)Added RaceTestWithPerTrialDataType.makeRaceData() -> RaceDataAdded RaceTestWithPerTrialDataType.makeThreadLocalData() -> ThreadLocalDataAdded RaceTestWithPerTrialDataType.thread1(RaceData, _: ThreadLocalData) -> ObservationAdded TestRunPredicate [enum]Added TestRunPredicate.CustomAdded TestRunPredicate.OSXAnyAdded TestRunPredicate.OSXBugFixAdded TestRunPredicate.OSXBugFixRangeAdded TestRunPredicate.OSXMajorAdded TestRunPredicate.OSXMinorAdded TestRunPredicate.OSXMinorRangeAdded TestRunPredicate.descriptionAdded TestRunPredicate.evaluate() -> BoolAdded TestRunPredicate.iOSAnyAdded TestRunPredicate.iOSBugFixAdded TestRunPredicate.iOSBugFixRangeAdded TestRunPredicate.iOSMajorAdded TestRunPredicate.iOSMinorAdded TestRunPredicate.iOSMinorRangeAdded TestRunPredicate.iOSSimulatorAnyAdded TestSuiteAdded TestSuite.init(_: String)Added TestSuite.nameAdded TestSuite.setUp(() -> ())Added TestSuite.tearDown(() -> ())Added TestSuite.test(String) -> StdlibUnittest.TestSuite._TestBuilderAdded TestSuite.test(String, _:() -> ())Added pthread_attr_t.init()Added pthread_cond_t.init()Added pthread_mutex_t.init()Added RaceTestWithPerTrialDataType.ObservationAdded RaceTestWithPerTrialDataType.RaceDataAdded RaceTestWithPerTrialDataType.ThreadLocalDataAdded WEXITSTATUS(CInt) -> CIntAdded WIFEXITED(CInt) -> BoolAdded WIFSIGNALED(CInt) -> BoolAdded WTERMSIG(CInt) -> CIntAdded asHex(S) -> StringAdded asHex(T) -> StringAdded chiSquaredUniform2(Int, Int, Double) -> BoolAdded consumeCPU(Int)Added createTemporaryFile(String, String, String) -> StringAdded evaluateObservationsAllEqual([T]) -> StdlibUnittest.RaceTestObservationEvaluationAdded expectCrashLater()Added expectFalse(Bool, StdlibUnittest.SourceLocStack?,(() -> String)?, String, UWord)Added expectFalse(StdlibUnittest.AssertionResult, StdlibUnittest.SourceLocStack?,(() -> String)?, String, UWord)Added expectTrue(Bool, StdlibUnittest.SourceLocStack?,(() -> String)?, String, UWord)Added expectTrue(StdlibUnittest.AssertionResult, StdlibUnittest.SourceLocStack?,(() -> String)?, String, UWord)Added findSubstring(String, String) -> String.Index?Added getFloat32(Float32) -> Float32Added getFloat64(Float64) -> Float64Added getInt(Int) -> IntAdded getInt16(Int16) -> Int16Added getInt32(Int32) -> Int32Added getInt64(Int64) -> Int64Added getInt8(Int8) -> Int8Added getPointer(COpaquePointer) -> COpaquePointerAdded getUInt(UInt) -> UIntAdded getUInt16(UInt16) -> UInt16Added getUInt32(UInt32) -> UInt32Added getUInt64(UInt64) -> UInt64Added getUInt8(UInt8) -> UInt8Added getUWord(UWord) -> UWordAdded getWord(Word) -> WordAdded nextTrackedSerialNumberAdded posixPipe() -> (readFD: CInt, writeFD: CInt)Added posixWaitpid(pid_t) -> StdlibUnittest.ProcessTerminationStatusAdded rand32() -> UInt32Added rand32(UInt32) -> UInt32Added rand64() -> UInt64Added randArray64(Int) -> ContiguousArray<UInt64>Added randInt() -> IntAdded readAll(CInt) -> StringAdded runAllTests()Added runChild([String]) -> (stdout: String, stderr: String, status: StdlibUnittest.ProcessTerminationStatus)Added runRaceTest(RT.Type, Int, Int?)Added scan(S, U,(U, S.Generator.Element) -> U) -> [U]Added signalToString(Int) -> StringAdded spawnChild([String]) -> (pid: pid_t, stdinFD: CInt, stdoutFD: CInt, stderrFD: CInt)Added trackedCountAdded withArrayOfCStrings([String],([UnsafeMutablePointer<CChar>]) -> R) -> RModified expectEqual(T, T, StdlibUnittest.SourceLocStack?,(() -> String)?, String, UWord)

|  | Declaration |
| --- | --- |
| From | ``` func expectEqual<T : ForwardIndexType>(_ expected: T, _ actual: T, stackTrace stackTrace: StdlibUnittest.SourceLocStack? = default, _ collectMoreInfo: (() -> String)? = default, file file: String = default, line line: UWord = default) ``` |
| To | ``` func expectEqual<T : Equatable>(_ expected: T, _ actual: T, stackTrace stackTrace: StdlibUnittest.SourceLocStack? = default, _ collectMoreInfo: (() -> String)? = default, file file: String = default, line line: UWord = default) ``` |

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
