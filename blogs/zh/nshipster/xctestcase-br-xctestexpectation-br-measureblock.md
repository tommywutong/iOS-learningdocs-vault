---
title: 'XCTestCase、<br/>XCTestExpectation 与<br/> measureBlock()'
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/xctestcase/'
original_language: en
published: 2014-07-21
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:d314f38c21822166'
translated: true
---

> 原文：[XCTestCase /<br/>XCTestExpectation /<br/> measureBlock()](https://nshipster.com/xctestcase/)　·　NSHipster (Mattt)

# [XCTest​Case /XCTest​Expectation / measure​Block()](https://nshipster.com/xctestcase/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　2015 年 4 月 7 日（[修订](https://github.com/nshipster/articles/commits/master/2014-07-21-xctestcase.md)）

虽然 iOS 8 和 Swift 在 WWDC 2014 的发布中获得了最多关注，但 Xcode 6 在测试方面的新增和改进，从长远来看可能会产生一些最深远的影响。

本周，我们将介绍 Xcode 内置的测试框架 `XCTest`，以及 Xcode 6 中令人兴奋的新功能：`XCTestExpectation` 和性能测试。

---

大多数 Xcode 项目模板现在都开箱即用地支持测试。例如，在 Xcode 中用 `⇧⌘N` 创建新 iOS App 时，生成的项目文件将配置两个顶级组（除了“Products”组之外）：“AppName”和“AppNameTests”。项目的自动生成 Scheme 使快捷键 `⌘R` 用于构建和运行可执行 target，`⌘U` 用于构建和运行测试 target。

测试 target 中有一个名为“AppNameTests”的文件，其中包含一个示例 `XCTestCase` 类，带有样板化的 `setUp` 和 `tearDown` 方法，以及一个示例功能测试和性能测试用例。

## XCTestCase

Xcode 的单元测试包含在 `XCTestCase` 子类（subclass）中。按照惯例，每个 `XCTestCase` 子类封装一组特定的关注点，例如某个功能、用例或 App 的流程。

> 随着代码库的增长和演变，按逻辑将测试划分到数量可管理的测试用例中，会产生巨大的差异。

### setUp 与 tearDown

`setUp` 在 `XCTestCase` 中的每个测试运行之前被调用，当该测试运行结束后，`tearDown` 被调用：

```
class Tests: XCTestCase {
    override func setUp() {
        super.setUp()
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
        super.tearDown()
    }
}
```

```
@interface Tests : XCTestCase

@property NSCalendar *calendar;
@property NSLocale *locale;

@end

@implementation Tests

- (void)setUp {
    [super setUp];
    // Put setup code here. This method is called before the invocation of each test method in the class.
}

- (void)tearDown {
    // Put teardown code here. This method is called after the invocation of each test method in the class.
    [super tearDown];
}

@end
```

这些方法对于创建测试用例中所有测试共用的对象非常有用：

```
var calendar: NSCalendar?
var locale: NSLocale?

override func setUp() {
    super.setUp()

    calendar = NSCalendar(identifier: NSCalendarIdentifierGregorian)
    locale = NSLocale(localeIdentifier: "en_US")
}
```

```
- (void)setUp {
    [super setUp];

    self.calendar = [NSCalendar calendarWithIdentifier:NSCalendarIdentifierGregorian];
    self.locale = [NSLocale localeWithLocaleIdentifier:@"en_US"];
}
```

> 由于 `XCTestCase` 并非设计为在测试用例定义中直接初始化，因此在 Swift 中，在 `setUp` 中初始化的共享属性被声明为可选值 `var`。因此，很多时候放弃使用 `setUp` 而直接赋予默认值会更简单：

```
var calendar: NSCalendar = NSCalendar(identifier: NSGregorianCalendar)
var locale: NSLocale = NSLocale(localeIdentifier: "en_US")
```

### 功能测试

测试用例中每个名称以“test”开头的方法都会被识别为一个测试，并将评估该函数内的所有断言以确定其通过还是失败。

例如，函数 `testOnePlusOneEqualsTwo` 在 `1 + 1` 等于 `2` 时将通过：

```
func testOnePlusOneEqualsTwo() {
    XCTAssertEqual(1 + 1, 2, "one plus one should equal two")
}
```

```
- (void)testOnePlusOneEqualsTwo {
    XCTAssertEqual(1 + 1, 2, "one plus one should equal two");
}
```

### 你真正需要了解的所有 XCTest 断言

`XCTest` 附带了许多内置断言，但可以归纳为几个基本类型：

#### 基本测试

完全简化来说，所有 `XCTest` 断言都可以归结为一个基础断言：

```
XCTAssert(expression, format...)
```

```
XCTAssert(expression, format...);
```

如果表达式结果为 `true`，测试通过。否则，测试失败，并打印 `format` 格式化后的消息。

虽然开发人员可以只使用 `XCTAssert`，但以下辅助断言提供了一些有用的语义，帮助明确正在测试的具体内容。尽可能使用最具体的断言，只在 `XCTAssert` 更能表达意图时才退而求其次。

#### 布尔测试

对于 `Bool` 值或简单的布尔表达式，使用 `XCTAssertTrue` 和 `XCTAssertFalse`：

```
XCTAssertTrue(expression, format...)
XCTAssertFalse(expression, format...)
```

```
XCTAssertTrue(expression, format...);
XCTAssertFalse(expression, format...);
```

> `XCTAssert` 等同于 `XCTAssertTrue`。

#### 相等性测试

在测试两个值是否相等时，对标量值使用 `XCTAssert[Not]Equal`，对对象使用 `XCTAssert[Not]EqualObjects`：

```
XCTAssertEqual(expression1, expression2, format...)
XCTAssertNotEqual(expression1, expression2, format...)
```

```
XCTAssertEqual(expression1, expression2, format...);
XCTAssertNotEqual(expression1, expression2, format...);

XCTAssertEqualObjects(expression1, expression2, format...);
XCTAssertNotEqualObjects(expression1, expression2, format...);
```

> 在 Swift 中不需要 `XCTAssert[Not]EqualObjects`，因为标量和对象之间没有区别。

在专门测试两个 `Double`、`Float` 或其他浮点值是否相等时，使用 `XCTAssert[Not]EqualWithAccuracy`，以解决[浮点精度](https://en.wikipedia.org/wiki/Floating_point#Representable_numbers.2C_conversion_and_rounding)问题：

```
XCTAssertEqualWithAccuracy(expression1, expression2, accuracy, format...)
XCTAssertNotEqualWithAccuracy(expression1, expression2, accuracy, format...)
```

```
XCTAssertEqualWithAccuracy(expression1, expression2, accuracy, format...);
XCTAssertNotEqualWithAccuracy(expression1, expression2, accuracy, format...);
```

> 除了上述相等性断言，还有 `XCTAssertGreaterThan[OrEqual]` 和 `XCTAssertLessThan[OrEqual]`，它们为可比较的值提供了 `>`、`>=`、`<` 和 `<=` 的等价断言，补充了 `==` 的使用。

#### Nil 测试

使用 `XCTAssert[Not]Nil` 来断言给定值的存在（或不存在）：

```
XCTAssertNil(expression, format...)
XCTAssertNotNil(expression, format...)
```

```
XCTAssertNil(expression, format...);
XCTAssertNotNil(expression, format...);
```

#### 无条件失败

最后，`XCTFail` 断言将始终失败：

```
XCTFail(format...)
```

```
XCTFail(format...);
```

`XCTFail` 最常用于标记一个应使其通过的测试的占位符。它也可用于处理已由其他控制流结构（如检查成功情况的 `if` 语句的 `else` 子句）覆盖的错误情况。

### 性能测试

Xcode 6 新增了[对代码进行基准测试](https://nshipster.com/benchmarking/)的功能：

```
func testDateFormatterPerformance() {
    let dateFormatter = NSDateFormatter()
    dateFormatter.dateStyle = .LongStyle
    dateFormatter.timeStyle = .ShortStyle

    let date = NSDate()

    measureBlock() {
        let string = dateFormatter.stringFromDate(date)
    }
}
```

```
- (void)testDateFormatterPerformance {
    NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
    dateFormatter.dateStyle = NSDateFormatterLongStyle;
    dateFormatter.timeStyle = NSDateFormatterShortStyle;

    NSDate *date = [NSDate date];

    [self measureBlock:^{
        NSString *string = [dateFormatter stringFromDate:date];
    }];
}
```

测试输出显示被测量 `block` 的平均执行时间，以及单次运行时间和标准偏差：

```
Test Case '-[_Tests testDateFormatterPerformance]' started.
<unknown>:0: Test Case '-[_Tests testDateFormatterPerformance]' measured [Time, seconds] average: 0.000, relative standard deviation: 242.006%, values: [0.000441, 0.000014, 0.000011, 0.000010, 0.000010, 0.000010, 0.000010, 0.000010, 0.000010, 0.000010], performanceMetricID:com.apple.XCTPerformanceMetric_WallClockTime, baselineName: "", baselineAverage: , maxPercentRegression: 10.000%, maxPercentRelativeStandardDeviation: 10.000%, maxRegression: 0.100, maxStandardDeviation: 0.100
Test Case '-[_Tests testDateFormatterPerformance]' passed (0.274 seconds).
```

性能测试有助于为热代码路径建立性能基准。将它们加入你的测试用例中，以确保重要的算法和过程随着时间的推移始终保持高性能。

## XCTestExpectation

也许 Xcode 6 最令人兴奋的特性是内置了对异步测试的支持，通过 `XCTestExpectation` 类实现。现在，测试可以等待指定时长，直到某些条件得到满足，而无需使用复杂的 GCD 咒语。

要执行异步测试，首先使用 `expectationWithDescription` 创建一个期望（expectation）：

```
let expectation = expectationWithDescription("...")
```

```
XCTestExpectation *expectation = [self expectationWithDescription:@"..."];
```

然后，在方法底部添加 `waitForExpectationsWithTimeout` 方法，指定超时时间，并可选择指定一个 handler，在测试条件满足或超时（超时自动视为测试失败）时执行：

```
waitForExpectationsWithTimeout(10) { error in
    …
}
```

```
[self waitForExpectationsWithTimeout:10 handler:^(NSError *error) {
    …
}];
```

现在，剩下的唯一步骤是在所测试异步方法的相关回调中 `fulfill` 那个 `expecation`（期望）：

```
expectation.fulfill()
```

```
[expectation fulfill];
```

> 始终在异步回调的末尾调用 `fulfill()`——过早满足期望可能会造成竞态条件（race condition），导致运行循环（run loop）在完成测试之前退出。如果测试有多个期望，则每个期望必须在 `waitForExpectationsWithTimeout()` 指定的超时时间内执行 `fulfill()`，否则测试不会通过。

以下是一个示例，展示如何使用新的 `XCTestExpectation` API 测试异步网络请求的响应：

```
func testAsynchronousURLConnection() {
    let URL = NSURL(string: "https://nshipster.com/")!
    let expectation = expectationWithDescription("GET \(URL)")

    let session = NSURLSession.sharedSession()
    let task = session.dataTaskWithURL(URL) { data, response, error in
        XCTAssertNotNil(data, "data should not be nil")
        XCTAssertNil(error, "error should be nil")

        if let HTTPResponse = response as? NSHTTPURLResponse,
            responseURL = HTTPResponse.URL,
            MIMEType = HTTPResponse.MIMEType
        {
            XCTAssertEqual(responseURL.absoluteString, URL.absoluteString, "HTTP response URL should be equal to original URL")
            XCTAssertEqual(HTTPResponse.statusCode, 200, "HTTP response status code should be 200")
            XCTAssertEqual(MIMEType, "text/html", "HTTP response content type should be text/html")
        } else {
            XCTFail("Response was not NSHTTPURLResponse")
        }

        expectation.fulfill()
    }

    task.resume()

    waitForExpectationsWithTimeout(task.originalRequest!.timeoutInterval) { error in
        if let error = error {
            print("Error: \(error.localizedDescription)")
        }
        task.cancel()
    }
}
```

```
- (void)testAsynchronousURLConnection {
    NSURL *URL = [NSURL URLWithString:@"https://nshipster.com/"];
    NSString *description = [NSString stringWithFormat:@"GET %@", URL];
    XCTestExpectation *expectation = [self expectationWithDescription:description];

    NSURLSession *session = [NSURLSession sharedSession];
    NSURLSessionDataTask *task = [session dataTaskWithURL:URL
                                        completionHandler:^(NSData *data, NSURLResponse *response, NSError *error)
    {
        XCTAssertNotNil(data, "data should not be nil");
        XCTAssertNil(error, "error should be nil");

        if ([response isKindOfClass:[NSHTTPURLResponse class]]) {
            NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)response;
            XCTAssertEqual(httpResponse.statusCode, 200, @"HTTP response status code should be 200");
            XCTAssertEqualObjects(httpResponse.URL.absoluteString, URL.absoluteString, @"HTTP response URL should be equal to original URL");
            XCTAssertEqualObjects(httpResponse.MIMEType, @"text/html", @"HTTP response content type should be text/html");
        } else {
            XCTFail(@"Response was not NSHTTPURLResponse");
        }

        [expectation fulfill];
    }];

    [task resume];

    [self waitForExpectationsWithTimeout:task.originalRequest.timeoutInterval handler:^(NSError *error) {
        if (error != nil) {
            NSLog(@"Error: %@", error.localizedDescription);
        }
        [task cancel];
    }];
}
```

## Swift 中的 Mock

随着对异步测试的一流支持，Xcode 6 似乎已经满足了现代测试驱动开发者的所有需求。好吧，也许还差一个：[mocking](https://en.wikipedia.org/wiki/Mock_object)。

Mock 是一种有用的技术，用于隔离和控制那些由于复杂性、非确定性或性能限制通常不易测试的系统中的行为。示例包括模拟特定的网络交互、密集的数据库查询，或诱发在特定竞态条件下可能出现的状态。

有几个[开源库](https://nshipster.com/unit-testing/#open-source-libraries)用于创建 mock 对象和[桩（stub）](https://en.wikipedia.org/wiki/Test_stub)方法调用，但这些库很大程度上依赖于 Objective-C 运行时操作，这在 Swift 中目前还无法实现。

然而，由于 Swift 语法约束较少，这可能实际上并不必要。

在 Swift 中，类可以在函数定义内部声明，从而允许 mock 对象实现高度自包含。只需声明一个 mock 内部类，并 `override` 必要的方法：

```
func testFetchRequestWithMockedManagedObjectContext() {
    class MockNSManagedObjectContext: NSManagedObjectContext {
        override func executeFetchRequest(request: NSFetchRequest!, error: AutoreleasingUnsafePointer<NSError?>) -> [AnyObject]! {
            return [["name": "Johnny Appleseed", "email": "[email protected]"]]
        }
    }

    let mockContext = MockNSManagedObjectContext()
    let fetchRequest = NSFetchRequest(entityName: "User")
    fetchRequest.predicate = NSPredicate(format: "email ENDSWITH[cd] %@", "@apple.com")
    fetchRequest.resultType = .DictionaryResultType

    var error: NSError?
    let results = mockContext.executeFetchRequest(fetchRequest, error: &error)

    XCTAssertNil(error, "error should be nil")
    XCTAssertEqual(results.count, 1, "fetch request should only return 1 result")

    let result = results[0] as [String: String]
    XCTAssertEqual(result["name"] as String, "Johnny Appleseed", "name should be Johnny Appleseed")
    XCTAssertEqual(result["email"] as String, "[email protected]", "email should be [email protected]")
}
```

---

随着 Xcode 6 的到来，我们终于达到了这样的境界：**内置的测试工具已经足够好到可以单独使用**。也就是说，对于绝大多数 App 和库，没有特别令人信服的理由需要使用额外的抽象来提供可接受的测试覆盖率。除非在需要大量桩、mock 或其他特殊测试结构的极端情况下，`XCTest` 断言、期望和性能测量应该已经足够。

但是，无论测试工具变得多么优秀，它们都只有在**你实际使用它们时**才发挥价值。

如果你是 iOS 或 OS X 测试方面的新手，可以先在自动生成的测试用例文件中添加几个断言，然后按下 `⌘U`。你可能会惊讶地发现整个过程如此简单，而且——我敢说——如此愉悦。
