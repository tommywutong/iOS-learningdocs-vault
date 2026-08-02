---
title: Energy Efficiency Guide for iOS Apps
apple_id: TP40015243
resource_type: Guide
platform: watchOS|iOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/TestPerformance.html
archived_at: '2026-07-18T01:48:32.382859Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for iOS Apps](index.md)



## Test Performance

Performance testing identifies regressions in your code that may result in greater than expected energy usage. A performance test takes a block of your code and runs it ten times consecutively. Each time a run occurs, the test captures the execution time and standard deviation of the run. The results are then combined to form a baseline for comparison.

Performance testing uses the XCTest framework. In your test method, call `measureBlock:`, and pass it the block of code you want to measure, as shown in Listing 22-1.

__Listing 22-1__An XCTest performance test

Objective-C

1. `- (void)testPerformanceExample {`
2. `[self measureBlock:^{`
3. `// Pass a block of code to test.`
4. `}];`
5. `}`

Swift

1. `func testPerformanceExample() {`
2. `self.measureBlock() {`
3. `// Pass a block of code to test.`
4. `}`
5. `}`

Performance test results are accessible for analysis throughout Xcode—in the report navigator, the issues navigator, and the source editor. For more information on performance testing, see [Writing Performance Tests](../../Developer%20Tools/Testing%20with%20Xcode/Writing%20Test%20Classes%20and%20Methods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dcmzsfvbuqnbnknltq) in _[Testing with Xcode](../../Developer%20Tools/Testing%20with%20Xcode/About%20Testing%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dcmzs)_.

[Measure Energy Impact with Instruments](MonitorEnergyWithInstruments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmztfvjvomi)

[Related Documents](RelatedDocuments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmjvfvjvomi)
