---
title: 更新现有代码库以适应单元测试
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/updating-your-existing-codebase-to-accommodate-unit-tests
source_url: 'https://developer.apple.com/documentation/xcode/updating-your-existing-codebase-to-accommodate-unit-tests'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/updating-your-existing-codebase-to-accommodate-unit-tests.json'
content_hash: 'sha256:d5c5bda2b8f23f39'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [测试](testing.md)

# 更新现有代码库以适应单元测试

<sub>文章</sub>

移除组件之间的耦合，以提高测试覆盖率和可靠性。

## 概述

向现有项目添加单元测试可能很困难，因为没有考虑可测试性的设计选择可能会将不同的类或子系统耦合在一起，导致无法单独测试它们。当软件中的两个组件紧密耦合时，只有以特定方式将一个组件与另一个组件集成，才能正确使用其中任何一个。有时，这种耦合（coupling）会让测试尝试建立网络连接或与文件系统交互，导致测试速度缓慢且结果不确定。移除耦合可以让你引入单元测试，但这需要在尚无测试覆盖的地方更改代码，因而存在风险。

要提高项目的测试覆盖率，请先确定想要测试的组件，再编写测试用例来覆盖你想断言的行为。采用以风险为中心的优先级策略，优先覆盖用户 bug 报告数量较多的功能逻辑，或出现衰退（regression）时影响最大的逻辑。

当受测代码与项目的其他部分或某个框架类耦合时，请对代码进行尽可能小的更改，以便在不改变其行为的情况下隔离该组件。降低耦合可以提高在测试上下文中使用该类的能力；同时应尽量减少更改，以降低每次更改带来的风险。

以下各节针对待考察代码与其他组件之间的耦合阻碍测试的情形，提出了移除耦合的更改。每种解决方案都会演示测试函数如何使用更改后的代码来断言其行为。

### 用协议替换具体类型（concrete type）

如果代码依赖某个特定类型，而该类型的行为导致测试困难，请创建一个协议，列出代码使用的方法和属性。在与自己代码库中的组件交互时，或者与平台 SDK 和 Swift 软件包等不受你控制的其他来源 API 交互时，都可以使用这种方法。这类问题依赖项的示例包括访问用户文稿或数据库等外部状态的依赖项，以及网络连接或随机值生成器等结果不确定的依赖项。

以下代码展示了 App 中的一个类，它使用不透明服务打开表示附件的文件，而该附件由外部依赖项处理。`openAttachment(file:with:)` 方法的结果取决于不透明服务能否处理所请求类型的文件，以及 App 能否成功打开文件。所有这些变量都可能导致测试失败，你不得不调查最终发现只是与代码无关的暂时性问题的“错误”，从而拖慢开发速度。

```swift
private enum AttachmentOpeningError: Error {
    case unableToOpenAttachment
}

struct AttachmentOpener {
  func openAttachment(file location: URL, with service: OpaqueService) throws {
    if (!service.open(location)) {
      throw AttachmentOpeningError.unableToOpenAttachment
    }
  }
}
```

要测试存在这种耦合的代码，请引入一个协议，用于描述代码如何与问题依赖项交互。在代码中使用该协议，使类依赖协议中存在的方法，而不依赖这些方法的特定实现。为该协议编写一个不会执行有状态或不确定任务的替代实现，并使用这个实现编写行为可控的测试。

以下代码定义了一个包含 `open` 方法的协议，同时为不透明类添加扩展，使其符合该协议。

```swift
protocol URLOpener {
    func open(_ file: URL) -> Bool
}

extension OpaqueService : URLOpener {}

struct AttachmentOpener {
    func openAttachment(file location: URL, with service: URLOpener) throws {
        if (!service.open(location)) {
            throw AttachmentOpeningError.unableToOpenAttachment
        }
    }
}

class StubService: URLOpener {
    var isSuccessful = true

    func open(_ file: URL) -> Bool {
        return isSuccessful
    }
}
```

在测试中，为 `URLOpener` 协议编写另一个不依赖用户电脑上已安装 App 的实现。

**Swift Testing**

```swift
@Suite struct AttachmentOpenerTests {
    var service = StubService()
    var attachmentOpener = AttachmentOpener()
    let location = URL(fileURLWithPath: "/tmp/a_file.txt")

    @Test("throws no error when open succeeds")
    func serviceCanOpenAttachment() {
        service.isSuccessful = true
        #expect(throws: Never.self) {
            try attachmentOpener.openAttachment(file: location, with: service)
        }
    }

    @Test("throws unableToOpenAttachment when open fails")
    func throwsIfServiceCannotOpenAttachment() {
        service.isSuccessful = false
        #expect(throws: AttachmentOpeningError.unableToOpenAttachment) {
            try attachmentOpener.openAttachment(file: location, with: service)
        }
    }
}
```

**XCTest**

```objc
class AttachmentOpenerTests: XCTestCase {
    var service: StubService! = nil
    var attachmentOpener: AttachmentOpener! = nil
    let location = URL(fileURLWithPath: "/tmp/a_file.txt")

    override func setUp() {
        service = StubService()
        attachmentOpener = AttachmentOpener()
    }

    override func tearDown() {
        service = nil
        attachmentOpener = nil
    }

    func testServiceCanOpenAttachment() {
        service.isSuccessful = true
        XCTAssertNoThrow(try attachmentOpener.openAttachment(file: location, with: service))
    }

    func testThrowIfServiceCannotOpenAttachment() {
        service.isSuccessful = false
        XCTAssertThrowsError(try attachmentOpener.openAttachment(file: location, with: service))
    }
}
```

### 用元类型值替换具名类型

如果 App 中的一个类会创建并使用另一个类的实例，而所创建的对象使测试变得困难，那么创建这些对象的类本身也可能很难测试。请将所创建对象的类型参数化，并使用必要初始化方法创建实例。这类测试困难的情形包括：控制器响应用户操作而在文件系统上创建新文稿，或者某个方法解读从 Web 服务收到的 JSON，并创建用于表示所接收数据的新 Core Data 托管对象。

在这些情况下，由于对象是由你想测试的代码创建的，因此无法向方法传入另一个对象作为参数。直到代码创建对象后，该对象才会存在，而此时它已经属于具有不可测试行为的类型。

以下代码展示了 `DocumentLoader` 类，它会创建并加载 `Document`，例如用来响应 UI 操作。它创建的文稿对象会在文件系统中读取和写入数据，因此在单元测试中不容易控制其行为。

```swift
enum DocumentError : Error {
    case cannotLoadContent
    case cannotSaveContent
}

class Document {
    private var location: URL
    private var titleContent: String?
    var title : String {
        get {
            return titleContent ?? "Untitled"
        }
        set {
            titleContent = newValue
        }
    }

    required init(fileURL: URL) {
        location = fileURL
    }
    
    func load() throws {
        do {
            let myString = try String(contentsOf: location, encoding: .utf8)
        }
        catch {
            throw DocumentError.cannotLoadContent
        }
    }
    
    func save() throws {
        do {
            try titleContent?.write(to: location, atomically: true, encoding: .utf8)
        }
        catch {
            throw DocumentError.cannotSaveContent
        }
    }
}

class DocumentLoader {
    func loadDocument(at location: URL) -> Bool {
        do {
            var document = Document(fileURL: location)
            try document.load()
            // 对文稿执行某项操作，例如在 App 的 UI 中呈现它。
            return true
        } catch {
            return false
        }
    }
}
```

要移除待测代码与其所创建对象之间的耦合，请在受测类上定义一个变量，用于表示该类应构造的对象 _类型_。这种变量称为 _元类型值（metatype value）_。将其默认值设为该类已经使用的类型。你需要确保用于构造实例的初始化方法标记为 `required`。以下代码展示了引入该变量后的文稿浏览器视图控制器（view controller）委托（delegate）。该委托会使用元类型值所定义的类型创建文稿。

```swift
class DocumentLoader {
    var DocumentClass = Document.self

    func loadDocument(at location: URL) -> Bool {
        do {
            var document = DocumentClass.init(fileURL: location)
            try document.load()
            // 对文稿执行某项操作，例如在 App 的 UI 中呈现它。
            return true
        } catch {
            return false
        }
    }
}
```

在测试中为元类型设置不同的值，让代码构造一个没有同样不可测试行为的对象。在测试中，创建文稿类的“样例”版本：这个类具有相同接口，但不实现导致测试困难的行为。在本例中，样例文稿类不应与文件系统交互。

```swift
class SampleDocument : Document {
    static var loadsSuccessfully : Bool = true
    static var savesSuccessfully : Bool = true
    
    override func load() throws {
        guard SampleDocument.loadsSuccessfully else {
            throw DocumentError.cannotLoadContent
        }
    }
    
    override func save() throws {
        guard SampleDocument.savesSuccessfully else {
            throw DocumentError.cannotSaveContent
        }
    }
}
```

在测试用例的 `setUp()` 方法中，用样例类型替换文稿类型，使受测文稿加载器创建桩文稿类型（stub document type）的实例。样例文稿在测试中具有确定的行为。

**Swift Testing**

```swift
@Suite final class DocumentLoaderTests {
    let loader = DocumentLoader()

    init() {
        loader.DocumentClass = SampleDocument.self
    }

    @Test @MainActor func documentLoaderReturnsFalseWhenDocumentCannotLoad() {
        SampleDocument.loadsSuccessfully = false
        #expect(loader.loadDocument(at: URL(filePath: "/Users/example/Documents/document.txt")) == false)
    }

    @Test @MainActor func documentLoaderReturnsTrueWhenDocumentLoads() {
        SampleDocument.loadsSuccessfully = true
        #expect(loader.loadDocument(at: URL(filePath: "/Users/example/Documents/document.txt")) == true)
    }
}
```

> [!note] 注意
> 由于这些测试依赖共享的 `SampleDocument.loadsSuccessfully` 状态，因此无法并发运行。测试带有 `@MainActor` 标注，以确保它们串行运行。

**XCTest**

```swift
class DocumentLoaderTests: XCTestCase {
    var loader: DocumentLoader! = nil

    override func setUp() {
        loader = DocumentLoader()
        loader.DocumentClass = SampleDocument.self
    }

    override func tearDown() {}

    func testDocumentLoaderReturnsFalseWhenDocumentCannotLoad() {
        SampleDocument.loadsSuccessfully = false
        XCTAssertFalse(loader.loadDocument(at: URL(filePath: "/Users/example/Documents/document.txt")))
    }

    func testDocumentLoaderReturnsTrueWhenDocumentLoads() {
        SampleDocument.loadsSuccessfully = true
        XCTAssertTrue(loader.loadDocument(at: URL(filePath: "/Users/example/Documents/document.txt")))
    }
}
```

### 派生子类并覆盖不可测试的方法

如果某个类将自定逻辑与导致该类难以测试的交互或行为组合在一起，请引入一个子类，覆盖该类的部分方法，让其他方法更易于测试。类中同时包含 App 特有逻辑以及与环境或框架之间的交互十分常见，而这些交互会导致行为难以在测试中控制。常见示例是 [UIViewController](../uikit/uiviewcontroller.md) 子类，它在操作方法中包含 App 特有代码，同时还会加载视图或呈现其他视图控制器。

引入针对自定 App 逻辑的测试很有必要，这能确保逻辑按预期工作，并防止衰退。类与环境之间的交互很复杂，难以控制或绕过，因此测试该逻辑也很困难。

例如，以下账户对象提供了计算某人年龄的方法。它会计算账户所记录的出生日期与今天日期之间相隔的年数。

```swift
import Foundation

enum AccountError : Error {
    case cannotCalculateAge
}

class Account {
    let name: String
    let email: String
    let userId: String
    let dateOfBirth: Date
    
    init(name: String, email: String, userId: String, dateOfBirth: Date) {
        self.name = name
        self.email = email
        self.userId = userId
        self.dateOfBirth = dateOfBirth
    }
    
    var now : Date {
        get {
            return Date()
        }
    }
    
    func age() throws -> Int {
        let calendar = Calendar.current
        let birthday = calendar.startOfDay(for: dateOfBirth)
        let today = calendar.startOfDay(for: now)
        guard let years =  calendar.dateComponents([.year], from: birthday, to: today).year else {
            throw AccountError.cannotCalculateAge
        }
        return years
    }
}
```

测试这个对象的行为很困难，因为 `now` 字段从系统时钟获取值。如果时钟设置不正确，测试可能会失败；而且随着时间流逝，`now` 返回的值会发生变化，测试对计算所得年龄的预期也会过时。

要克服这种复杂性，请派生 `Account` 的子类，并用更简单的方法覆盖那些产生复杂、不可测试交互的方法，从而对这些方法“加桩”。在测试中使用该子类来验证不被覆盖的自定逻辑行为。如果受测代码会创建目标类型的实例，你可能还需要引入元类型值。

以下代码引入了子类 `StubAccount`，它不依赖系统时钟，而是使用由调用方配置的固定日期。使用该子类的测试会为账户出生日期和表示当前日期的日期提供固定值，以确保 `Account` 对象执行的计算正确。

```swift
class StubAccount : Account {
    private var overrideNow : Date
    
    init(name: String, email: String, userId: String, dateOfBirth: Date, overrideNow: Date) {
        self.overrideNow = overrideNow
        super.init(name: name, email: email, userId: userId, dateOfBirth: dateOfBirth)
    }
    
    override var now : Date {
        overrideNow
    }
}
```

在测试类型中创建 `StubAccount` 实例，并测试从 `Account` 继承的日期计算逻辑。由于 `StubAccount` 允许测试代码控制表示当前日期的日期，测试行为不依赖系统时钟。

**Swift Testing**

```swift
@Suite struct AccountTests {
    @Test func accountCalculatesAgeCorrectly() throws {
        let dateOfBirth = Calendar.current.date(from: DateComponents(
            timeZone: TimeZone(identifier: "Europe/London"),
            year: 1970,
            month: 1,
            day: 1
        ))!
        let fixedDateForToday = Calendar.current.date(from: DateComponents(
            timeZone: TimeZone(identifier: "Europe/London"),
            year: 2024,
            month: 12,
            day: 31
        ))!
        let account = StubAccount(name: "Example Account", email: "account@example.com", userId: "example", dateOfBirth: dateOfBirth, overrideNow: fixedDateForToday)
        #expect(try account.age() == 54)
    }
}
```

**XCTest**

```swift
class AccountTests : XCTestCase {
    private var account: StubAccount! = nil

    override func setUp() {
        let dateOfBirth = Calendar.current.date(from: DateComponents(
            timeZone: TimeZone(identifier: "Europe/London"),
            year: 1970,
            month: 1,
            day: 1
        ))!
        let fixedDateForToday = Calendar.current.date(from: DateComponents(
            timeZone: TimeZone(identifier: "Europe/London"),
            year: 2024,
            month: 12,
            day: 31
        ))!
        account = StubAccount(name: "Example Account", email: "account@example.com", userId: "example", dateOfBirth: dateOfBirth, overrideNow: fixedDateForToday)
    }

    override func tearDown() { }

    func testAccountCalculatesAgeCorrectly() throws {
        XCTAssertEqual(try account.age(), 54)
    }
}
```

有时，这种模式可以帮助你测试组合了多项职责的现有类，但前提是这些类和方法未标记为 `final`；从头设计可测试代码时，这并不是一种值得采用的良好做法。请将处理不同关注点的代码分离到不同类中，例如：

- 实现 App 自定行为的控制器类。
- 管理视图层级结构（view hierarchy）并响应 UI 操作的视图控制器。
- 准备并更新你在 App 视图中呈现的数据的视图模型。

添加 UI 测试，以端到端工作流验证真实类的行为，覆盖你在单元测试中以桩替换的逻辑。

派生子类并覆盖不可测试的方法，是重新设计现有代码、将 App 逻辑与框架或外部数据的集成分离开的第一步。以这种方式划分代码后，你可以更容易地理解项目的哪些部分实现 App 功能、哪些部分与系统的其他部分集成；在更改代码以利用新 API 或采用其他技术时，这也能降低引入逻辑 bug 的可能性。

### 注入单例

如果代码使用单例对象来访问全局可用的状态或行为，请将单例变为可以替换的参数，以支持测试隔离。代码库中可能到处都在使用单例，导致你难以知道待测组件使用单例时该单例处于何种状态。以不同顺序运行测试可能会产生不同结果。

> [!note] 注意
> 常用单例（包括 [NSApplication](../appkit/nsapplication.md) 和默认 [FileManager](../foundation/filemanager.md)）的行为依赖外部状态。直接使用这些单例的组件会为可靠测试带来更多复杂问题。

在本例中，`LoginHandler` 对象参与向网络服务认证（authentication）用户。它的一项功能是获取 App 先前用于该服务的用户名，该用户名来自标准 UserDefaults 对象：

```swift
class LoginHandler {
    
    var previousUsername: String? {
        get {
            UserDefaults.standard.string(forKey: "ExampleAccountUsername")
        }
    }
    
}
```

[UserDefaults](../foundation/userdefaults.md) 依赖文件系统中存储的共享状态，而该状态可能被 App 中的其他代码修改，也可能被用户在 Mac 上编辑文件时修改。请将对单例对象的直接访问替换为可从受测组件外部控制的参数或属性。在 App 中，继续使用单例作为组件的协作者。在测试中，则提供更易于控制的替代对象。

以下代码展示了对上述 `LoginHandler` 类应用这项更改的结果。登录处理程序从其 `storage` 对象获取已存储的用户名，该对象默认为 UserDefaults 单例。一个扩展使 `UserDefaults` 符合 `LoginStorage` 协议，这样测试就能提供该协议的替代实现。

```swift
protocol LoginStorage {
    func string(forKey: String) -> String?
}

extension UserDefaults : LoginStorage { }

class LoginHandler {
    private var storage: LoginStorage
    
    init(storage: LoginStorage = UserDefaults.standard) {
        self.storage = storage
    }
    
    var previousUsername: String? {
        get {
            storage.string(forKey: "ExampleAccountUsername")
        }
    }
    
}
```

在测试用例中，你可以替换为其他存储对象；测试套件或 App 的其他位置不会使用该对象，因此它与其他测试和模块的行为相隔离。

**Swift Testing**

```swift
struct StubLoginStorage : LoginStorage {
    let value: String?

    init(value: String?) {
        self.value = value
    }

    func string(forKey: String) -> String? {
        value
    }
}

@Suite struct LoginHandlerTests {
    let handler: LoginHandler = LoginHandler(storage: StubLoginStorage(value: "example-username"))

    @Test func handlerGetsUsernameFromStorage() {
        #expect(handler.previousUsername == "example-username")
    }
}
```

**XCTest**

```swift
struct StubLoginStorage : LoginStorage {
    let value: String?

    init(value: String?) {
        self.value = value
    }

    func string(forKey: String) -> String? {
        value
    }
}

class XCLoginHandlerTests : XCTestCase {
    var handler: LoginHandler! = nil

    override func setUp() {
        handler = LoginHandler(storage: StubLoginStorage(value: "example-username"))
    }

    func testHandlerGetsUsernameFromStorage() {
        XCTAssertEqual(handler.previousUsername, "example-username")
    }
}
```

你可能需要将这项更改与本文各节所述的更改（[用协议替换具体类型](updating-your-existing-codebase-to-accommodate-unit-tests.md#Replace-a-concrete-type-with-a-protocol)和[派生子类并覆盖不可测试的方法](updating-your-existing-codebase-to-accommodate-unit-tests.md#Subclass-and-override-untestable-methods)）结合使用，以创建在测试中用来替换单例的替代对象。当单例提供难以在测试中控制的行为时（例如 [FileManager](../foundation/filemanager.md) 或 [NSApplication](../appkit/nsapplication.md)），你就需要这样做。

## 另请参阅

### 测试开发

- [向 Xcode 项目添加测试](adding-tests-to-your-xcode-project.md) — 包含用于构建代码的测试 target，以测试函数逻辑、检查集成问题、自动执行 UI 工作流并测量性能。
- [确定测试覆盖了多少代码](determining-how-much-code-your-tests-cover.md) — 使用代码覆盖率，将新的测试开发集中在缺少足够测试的区域。
- [将测试组织到测试计划中以改进代码评估](organizing-tests-to-improve-feedback.md) — 创建并配置测试计划，控制在软件工程流程的不同阶段从测试中收到的信息。
