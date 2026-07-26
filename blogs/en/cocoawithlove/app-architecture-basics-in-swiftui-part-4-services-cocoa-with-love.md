---
title: 'App architecture basics in SwiftUI Part 4: Services | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/separated-services-layer.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:70fda86240249a0f'
translated: false
---

> 原文：[App architecture basics in SwiftUI Part 4: Services | Cocoa with Love](https://www.cocoawithlove.com/blog/separated-services-layer.html)　·　Cocoa with Love (Matt Gallagher)

This article is about adding a separated Services-layer to an app. A Services-layer is, in my opinion, the single best app architectural addition you can make, after the basic Model-View separation already implicit in SwiftUI. Model-View separation decouples the Model from the front-end but a Services-layer completes Model separation by separating the Model from the back-end and is one of the few app architectural changes you can point at and say: this change unlocks these capabilities.

I’ll be changing just 9 lines from the [127 line CwlFeedReader app from the previous article](https://www.cocoawithlove.com/blog/app-submodules.html) (plus a few lines of boilerplate in new files). It’s a relatively small change but it’s a topic with plenty of different opinions about the best approach so there’s a lot of discuss.

## Let’s try to add tests to CwlFeedReader

Before we look in detail at what I mean by a “separated Services-layer”, I’d like to start by looking at the biggest capability this change will unlock: testing.

Let’s assume we want to do the bare minimum in testing. This generally means interface tests on the `Model`. By “interface”, I’m referring to the public functions of the Model (the _module’s_ interface, not the user-interface). This type of test can detect major regressions (functionality that is accidentally broken when you add new features) and is a valuable addition to any app project due to its low time cost.

The interface to the `Model` looks like this:

```swift
public class Model: ObservableObject {
   @Published public private(set) var feed: Feed?
   @Published public var error: IdentifiableError?
   @Published public private(set) var isReadStatuses: [URL: Bool]
   
   public init()
   public func setIsRead(_ value: Bool, url: URL)
   public func reload()
}
```

To test this interface, we need tests that call each of:

1. `init`
2. `setIsRead` and
3. `reload`

that validate the behavior of these functions by reading the changes to `feed`, `error` and `isReadStatuses`.

I’ve written tests for all 3 functions in [the CwlFeedReader repository](https://github.com/mattgallagher/CwlFeedReader/tree/part-four-broken-tests) but I want to focus on the test for the most important function in the program, `reload`. There’s a complication that `reload` is called from inside `init` so I’m going to simply construct `Model()` and – relying on the fact that `reload` delivers its results _asychronously_ to the main thread – I will then examine the _second_ value received via `$feed` and treat this as equivalent to the result of calling `reload`.

```swift
let feedFirstURL = URL(string: "https://www.cocoawithlove.com/blog/swiftui-natural-pattern.html")!
func testReload() {
   // Given a newly inited model and an expectation that stops on the second feed value
   let model = Model()
   let secondValue = expectation(description: "feed should emit 2 values.")
   let cancellable = model.$feed
      .dropFirst()
      .sink { _ in secondValue.fulfill() }
   
   // When the automatically invoked `reload()` completes
   wait(for: [secondValue], timeout: 30.0)
   cancellable.cancel()
   
   // Then the first feed URL should be the expected swiftui-natural-pattern.html
   XCTAssertEqual(model.feed?.items.map(\.url).first, feedFirstURL)
}
```

Everything looks good, right? I mean: there’s no bug in the code. Not exactly.

> These tests are available from the [part-four-broken-tests branch of the CwlFeedReader repository](https://github.com/mattgallagher/CwlFeedReader/tree/part-four-broken-tests)

The test fails.

Why? Because that `feedFirstURL` value was correct in late January when I wrote the test but it has already broken because the Cocoa with Love JSON feed has updated since then. We wanted this test to detect regression in the `reload` function but instead, we’ve merely detected that live-data has changed. This test is a waste of our time.

But the test isn’t the source of the problem, it is merely a symptom.

The true source of the problem is that it is not possible to isolate the code we’ve written from dependencies we use (the state of the network and data received from remote servers). If the upstream data changes, our tests fail. If the network is down, our tests fail. There are potentially worse problems that could occur if our tests overwhelm production servers or if our tests mistakenly change live data.

And even if live data isn’t a problem, our tests are _much slower_ than they should be. The test relies on asynchronous I/O, causing the test to take between a few hundred milliseconds and a few seconds, instead of a couple microseconds. While this may seem like the least significant problem here, this adds up. Even small apps can have thousands of tests. Hundreds of milliseconds per test can become _hours_.

The conclusion here is straightforward: if you can’t isolate your application from the outside world, tests are practically useless. Even if you can endure unreliability, the best you can achieve are some basic app-server integration smoke tests. Any other kind of testing will be impossible.

## The problem is broader than testing

It’s not just tests that are facing problems. We can’t do any useful work on the app if dependencies are unavailable. And dependencies are often, by their nature, beyond our control. If the server goes down, we’re blocked. If the server APIs are not finished, we’re blocked. Want to run a demo in a location without network access? You can’t.

Even the SwiftUI previews in CwlFeedReader construct the `Model()` and access the network for their content. Our SwiftUI previews can fail or misbehave when the network is unavailable. If we can’t usefully edit our _views_ without working dependencies, then we’re in trouble.

Availability isn’t the only problem. Configuration of data is also a limitation. Want to debug a situation that requires specific data or user states? You’ll have to manually create those users and states each time.

These are the symptoms of an app that we can’t isolate from its dependencies but there’s another, more conceptual problem: we don’t even have a _description_ of our app without its dependencies.

Yes, the _user_ sees the Cocoa with Love JSON feed presented as a `SwiftUI` `List` and `WKWebView` but that’s not what’s in our Model-layer. What the user _sees_ is a product of the data from connected _dependencies_ flowing through the app.

If we remove all dependencies from consideration (including the View-layer), we’ve written a program that:

1. fetches a JSON list containing identifiers, including error handling on fetch
2. can re-fetch the JSON list when requested
3. fetches a dictionary of booleans, keyed by the same identifiers in the JSON list
4. can update and save the booleans for each identifier when requested

This could be the description of a to-do list app, an email client or a control app for a network-connected set of light-switches. The only difference is the dependencies we reference.

If we control how we reference our dependencies, we can develop, test and use our program with precision, be flexible between problem domains, and we can work without getting blocked.

## Putting it in a diagram

Here’s a diagram of the CwlFeedReader app, showing the commonly identified Model-View-Controller components. Solid lines show references (use of concrete types or functions), dotted lines show data flow without reference. No solid arrow should ever point away from the Model – that would indicate a violation of Model isolation.

![MVC representation of CwlFeedReader (solid lines are explicit references, dotted lines are decoupled interactions)](https://www.cocoawithlove.com/assets/blog/mvc_minus_services.svg)

<sub>MVC representation of CwlFeedReader (solid lines are explicit references, dotted lines are decoupled interactions)</sub>

This diagram isn’t _wrong_ but it shows only the front-end of the Model-layer. Here’s a more complete architectural diagram of the CwlFeedReader app including the back-end:

![MVC+Services representation of CwlFeedReader (solid lines are explicit references, dotted lines are decoupled interactions)](https://www.cocoawithlove.com/assets/blog/mvc_services.svg)

<sub>MVC+Services representation of CwlFeedReader (solid lines are explicit references, dotted lines are decoupled interactions)</sub>

Immediately, you should be able to see the problem: there’s a solid arrow pointing away from the Model. Our Model is not isolated because it directly references `URLSession` and `UserDefaults` – sources of side-effects that affect the app.

In the same way that we need to maintain separation between the Model and the Controller+View components at the front-end, we need to maintain separation between the Model and these side-effects at the back end or we compromise our ability to test, isolate and reason about our own application.

## Some clarification around the word “Services”

There’s a few definitions of “services” around. The definition I’m using is:

> **Service**: any type or function that provides _side effects_ that can affect the testable behavior of the Model-layer

A [side effect](https://en.wikipedia.org/wiki/Side_effect_(computer_science)) is a function (including methods and computed values) that might change its behavior despite being called with the same parameters. Typical examples are anything read from the network, disk, clock or operating system. In some cases, simply asynchronously returning results is side-effect (since it may change the ordering of results).

The difficulty with services is that they’re dependent on the state of the things (network, disk, other processes running on the system). For testing and development purposes, we want to keep all of this state constant so we can focus on whether our program has changed behavior.

Identification of services is only the first step. The second step is to move them into a Services-layer:

> **Services-layer**: a collection of the app’s services and third-party dependencies, isolated so they are never directly referenced by the Model-layer, and replaceable at test or debug time with side-effect-free versions that offer robustly repeatable results.

The term “dependency injection” is commonly used to describe separation from dependencies. The term can accurately be applied to my approach but I tend to downplay this description due to its association with “dependency injection frameworks” (an approach that I avoid, as I’ll discuss later).

Notice that I’ve added “third-party dependencies”, along with “app’s services” in the Services-layer. The purpose of a Services-layer is that it lets the app swap components out at launch – good for removing services for testing, also good for removing third-party dependencies for updates, refactoring or replacements.

## How can we decouple the Model from Services?

I want to separate the Model interface from the Services interface. Separating two interfaces from each other is a process usually called “decoupling”. Where do we draw a line for this separation?

Let’s consider the network-data request pipeline that involves `URLSession` in the CwlFeedReader app. The major features of the pipeline are:

1. the Cocoa with Love domain name
2. use of the `URLSession` type
3. use of the relative path for the feed.json file, parameters and JSON encoding/decoding to marshal parameters to `URLSession`

It’s possible to separate an app along any of these 3 lines. I consider only one of these choices “correct” but let’s look at the arguments used in favor of each.

### 1. Decouple from production server using different environments

It’s common to find apps that don’t change their _code_ but change their _data_ and re-point their app at a stub-server when testing or debugging.

For the CwlFeedReader app, you could imagine the `Model` taking an API base string in its `init` function (e.g. `https://www.cocoawithlove.com`) and at test time, passing a value like `https://localhost:8080` as an alternate argument for this parameter. Assuming you’re running a webserver on port 8080 on the same machine, you could place a fixed version of the “feed.json” file at the same relative path as on the production server.

#### Pros

This approach lets you test every single line of code and, if retro-fitted to an existing codebase, requires the least effort.

#### Cons

This approach has many limitations:

- Works for network dependencies but is harder to apply to other dependencies (like `UserDefaults`) so it isn’t really usable for general service isolation.
- Even for network dependencies, it decouples network data but not network APIs. Our app can’t swap to a different network library or data source using this approach.
- You need to start the stub server before testing, meaning that your tests don’t “just work” without extra setup.
- Switching configurations on the server for testing requires side-channel configuration of the server.
- Stub servers can be complex entities, often in another language, so they add additional learning overheads for Swift developers

### 2. Put a protocol around the smallest possible subset of URLSession

Another approach is to decouple the dependency in code but to keep this effort as simple as possible. In Swift, this means: create a protocol that describes our direct usage of each dependency.

We could define the following protocol:

```swift
public protocol NetworkService {
   func fetchData(with: URLRequest, handler: @escaping (Data?, URLResponse?, Error?) -> Void) -> AnyCancellable
}
```

and provide the following implementation to wrap our use of `URLSession` completely in a protocol.

```swift
extension URLSessionDataTask: Cancellable {}

extension URLSession: NetworkService {
   public func fetchData(with request: URLRequest, handler: @escaping (Data?, URLResponse?, Error?) -> Void) -> AnyCancellable {
      let task = dataTask(with: request, completionHandler: handler)
      task.resume()
      return AnyCancellable(task)
   }
}
```

If we only use `URLSession` through this protocol, then we become decoupled from `URLSession` as a dependency and source of side-effects.

#### Pros

Wrapping dependencies in protocols is relatively simple and the resulting code maintains the same basic structure as if it were using `URLSession`.

#### Cons

Doesn’t wrap `URLRequest` or handle other details. We still need to configure details like path and headers and handle work like JSON decoding so it’s more like we need to say “fetch a JSON list whose location is defined by this URLRequest” instead of the simple “fetch the feed”.

Marshalling parameters for network requests, filling in headers, selecting endpoints, decoding responses; this is all tedious work.

We could define the `NetworkService` to have an interface that matches what our Model needs.

```swift
public protocol NetworkService {
   func fetchFeed(handler: @escaping (Result<Feed, Error>) -> Void) -> AnyCancellable
}
```

This creates a much simpler interface – no `URLRequest`, no JSON decoding, just the simple transaction that the Model desires.

#### Pros

Matches our Model’s “fetch feed” intent and makes the service feel like a clean interface.

#### Cons

Adding different interfaces for each kind of request increases the service size – and remember, most services are implemented _twice_ (once for the production services, once for the testing services) so this can be a significant additional burden.

Services themselves aren’t testable so putting more code into the service reduces potential test coverage. We’re putting Model-logic (correct headers for different endpoints, HTTP message encoding) in the untestable services.

Not reusable between different applications because it includes Model-specific logic.

### Personal opinion

I think (2) is the best option: wrap dependencies with side-effects in a protocol that _minimally_ wraps the features of the dependency that your app uses. You can change the interface slightly (as I changed `dataTask` to remove `URLSesionDataTask` from the interface) but such changes should be focussed on simplification without inclusion of _any_ Model data or logic.

Using a stub server, as in option (1), just doesn’t solve enough problems and the problems it does solve aren’t solved cleanly. It can be good as a stop-gap if you have no other option and can serve other purposes (like cross-platform validation) but keeping it running on test machines is annoying and it will never deliver a clean solution across all dependencies.

At the other end, putting app-specific logic into a service (3) is a mistake. Model-logic should be tested but services aren’t testable (they’re supposed to a dependency, not _your_ code). And the goal of (3) – to improve the abstraction of server communication – can be done by wrapping your services _inside_ your Model-layer, translating from simplified model concepts (like “feed”) into expanded model details (like the `URLRequest` and the decoding of its result).

## Using the Services-layer from the Model

Taking option (2) and wrapping our services as minimally as possible makes including it in existing code relatively painless. We can bundle all of the apps services together in a single struct:

```swift
public struct Services {
   let networkService: NetworkService
   let keyValueService: KeyValueService
}
```

With an instance of this struct available in the `Model`, we can replace the following use of `URLSession`:

```swift
task = URLSession.shared.dataTask(with: request) { data, response, error in /* ... */ }
task?.resume()
```

with

```swift
task = services.networkService.fetchData(with: request) { data, response, error in /* ... */ }
```

Replacing `UserDefaults` is similar:

```swift
UserDefaults.standard.set(try? JSONEncoder().encode(isReadStatuses), forKey: "isReadStatuses")
```

becomes:

```swift
services.keyValueService[key: "isReadStatuses", type: [URL: Bool].self] = isReadStatuses
```

It’s a drop-in replacement.

## Constructing services

What I’ve ignored is exactly how and where the `Services` instance is constructed. The reason is that different developers choose different approaches.

Historically, dependency injection frameworks were used to satisfy this problem. Services in a class would be specially named, typed or attributed and at runtime, the dependency injection framework would intercept the construction of services and set them to appropriate values (fully constructed production services or specialized testing versions).

I don’t recommend dependency injection frameworks. The purpose of service isolation should be to prevent side-effects but using a runtime framework to manipulate the contents of your classes _is_ a side-effect. It’s a conceptual conflict of interest and so completely unnecessary since manually managing services is so simple.

All we need to do configure the Model-layer with appropriate services is to pass them as a parameter at construction.

It’s weird when something so straightforward needs to be explained but I’ve seen developers go to extraordinary lengths to avoid passing a single parameter around. Here’s one approach commonly attempted to avoid passing services into the model – default constructed services:

```swift
public init(
   services: Services = Services(
      networkService: URLSession.shared,
      keyValueService: UserDefaults.standard
   )
)
```

At first, it seems highly practical because you don’t need to change how the `Model` class is constructed. The same `Model()` invocation will now construct the class with the production services and at test time, we can specify a different `services` argument for specialized testing services.

This approach works when `Model` is the only class in existence but as soon as you need other classes, it falls apart. It is not composable. If `Model` relies on class `Submodel`, then `Model` must construct `Submodel` with the same `Services` from `Model`, otherwise the two won’t agree. Letting `Submodel` default-construct its own `Services` is a potential source of bugs and should never occur. The only robust solution requires `Services` are _always_ passed into the type from outside.

Here’s the construction of `Model` in the `CwlFeedReaderApp`:

```swift
@StateObject var model = Model(services: Services())
```

I would be possible to construct all the services inline but the list of services in an app tends to grow, and precisely configuring reusable services can get complex, so it’s a good idea to move this work into a dedicated `init` function for the construction of production services:

```swift
extension Services {
   public init() {
      self.init(networkService: URLSession.shared, keyValueService: UserDefaults.standard)
   }
}
```

## Organize into modules to preserve separation

Now that we’ve added protocols, some implementations and some construction code, there’s a little organizing to consider to maintain the clean isolation we wanted.

Service _protocols_ (`NetworkService` and `KeyValueService`) and the `Services` struct which holds them should go into the “Model” module (they are the Model-layer defining its own interface).

Service _implementations_ (`extension URLSession: NetworkService` and `extension UserDefaults: KeyValueService`) must remain separated from the Model-layer. They can go into a new module named “ServiceImplementations”. This new module should be imported into the `CwlFeedReaderApp` (since it constructs the `Services` for the `Model` at startup) but shouldn’t be imported anywhere else.

## A final diagram

> The complete MVC+Services version of the app is available from the [part-four branch of the CwlFeedReader repository](https://github.com/mattgallagher/CwlFeedReader/tree/part-four)

The result is that Model-layer only references service protocols, never service implementations. This means the Model-layer no longer has any solid references to any other layer:

![MVC with separated Services-layer](https://www.cocoawithlove.com/assets/blog/mvc_separate_services.svg)

<sub>MVC with separated Services-layer</sub>

The Controller’s role in pulling everything together is apparent – it has a solid line to every other layer. Fortunately, despite the many arrows, the Controller’s workload is minimal – the connection to the Services-layer is just a single function.

The line from Services to the Model has gone from dotted to solid, indicating that Services now concretely references the Model-layer (to access the service protocol definitions). Eventually, moving these service protocols into a Definitions module (to avoid Services becoming coupled with Model details) might be helpful but we’ve added enough modules for the moment.

The effect on code was minor, particularly if you consider only the impact on existing code: we’ve changed just 9 lines of the 127 line program.

There are 46 new lines in new files (two new protocols and their implementations, the `Services` struct and its constructor) but exactly how to count these is debatable. The protocols and their implementations are reusable between apps. Like the `WebView` and `IdentifiableError` – that I ignore when counting lines of code – this new code could be considered external to the app. Additionally, service implementations grow only occasionally; we could increase the remaining program by an order of magnitude without needing additional service implementation code.

## Replacing the Services-layer at testing time

Now the Model-layer is cleanly separated from the Services-layer but we haven’t used it for any change in behavior. For this, we need test-friendly implementations of each service and an easy way to construct these test services, instead of the production services.

Here’s an implementation of `NetworkService` that pulls its data from a file resource instead of the network:

```swift
class MockNetworkService: NetworkService {
   func fetchData(with request: URLRequest, handler: @escaping (Data?, URLResponse?, Error?) -> Void) -> AnyCancellable {
      guard let method = request.httpMethod, let url = request.url else {
         handler(nil, nil, URLError(.badURL))
         return AnyCancellable {}
      }
      
      switch "\(method) \(url.absoluteString)" {
      case "GET https://www.cocoawithlove.com/feed.json": handler(mockFixture(name: "feed.json"), .successResponse(url), nil)
      default: handler(nil, .notFoundResponse(url), URLError(.fileDoesNotExist))
      }
      
      return AnyCancellable {}
   }
}
```

> **Stubs and mocks**: I’ve referred to “stub servers” and now “mock services”. These names are conventions from projects that I’ve worked on. The terms “mocks” and “stubs” have specific definitions in testing (“stubs” record data and provide output data, whereas “mocks” record the order in which functions are invoked). Just to be confusing, both “stub servers” and “mock services” generally break this terminology because they don’t record and would more correctly be termed “fakes” (partially working, isolated implementations).

As with running the app against the production services, we can construct `Services` for testing in a simplified manner:

```swift
public extension Services {
   static var mock: Services {
      return Services(networkService: MockNetworkService(), keyValueService: MockKeyValueService())
   }
}
```

Now that we have this `Services.mock` implementation, all we need to fix the failing `testReload()` from the start of the article is to replace the `let model = Model()` with `let model = Model(services: Services.mock)` and ensure we’re testing the result expected from our “feed.json” file.

Finally, we have reliable, fast tests that won’t break over time (unless we break our code – which is the breakage we _want_ to detect).

We can also run our SwiftUI previews without relying on the network by replacing the old preview code:

```swift
#if DEBUG
struct ListView_Previews: PreviewProvider {
   static var previews: some View {
      let model = Model()
      ListView(model: model)
   }
}
#endif
```

with the new `Services.mock`:

```swift
#if DEBUG
import MockServiceImplementations
struct ListView_Previews: PreviewProvider {
   static var previews: some View {
      let model = Model(services: Services.mock)
      ListView(model: model)
   }
}
#endif
```

This will let us pre-populate our SwiftUI previews however we desire, without needing the network to be available.

> These tests and previews are available from the [part-four branch of the CwlFeedReader repository](https://github.com/mattgallagher/CwlFeedReader/tree/part-four)

## Some ugliness due to missing SE-0273 functionality

As with “ServiceImplementations”, the “MockServiceImplementations” should also be its own module (by now, you should be able to see why moving to a module-based build approach was so necessary in the previous article).

At a minimum, the tests will need to import “MockServiceImplementations” but ideally, the app should be able to import it too, for use in SwiftUI previews. We don’t really want to include the mock services module in release builds (since mock fixtures take up a lot of space and we’d rather not include our internal testing details in the released product) so we need to pass `condition: .when(configuration: .debug)` to the Swift Package Manger for the “MockServiceImplementations” library.

Unfortunately, the `.when(configuration:)` condition I just mentioned is still waiting for the [Swift Package Manager developers to finish SE-0273](https://github.com/apple/swift-evolution/blob/master/proposals/0273-swiftpm-conditional-target-dependencies.md).

_Ahem_.

Until then, we need some ugly workarounds to make “MockServiceImplementations” a debug-only dependency.

First, the “MockServiceImplementations” need to be built into a separate library. The Swift `PackageDescription` begins:

```swift
let package = Package(
   name: "CwlFeedReaderLib",
   platforms: [.iOS(.v14), .macOS(.v11)],
   products: [
      .library(
         name: "CwlFeedReaderLib",
         targets: ["Model", "ServiceImplementations", "Toolbox", "ViewToolbox"]
      ),
      .library(
         name: "MockServiceImplementations",
         targets: ["MockServiceImplementations"]
      )
```

Then in the “Build Phases” for the app target, we need to add “MockServiceImplementations” to the “Dependencies” but _DO NOT_ add it to the list of libraries or linked files. Instead, find the “Other Linker Flags” setting in the “Build Settings” and expand it to reveal “Debug”/“Release” and under “Debug” add `${BUILT_PRODUCTS_DIR}/MockServiceImplementations.o`.

That’s not _too_ bad but our MockServiceImplementations module contains “fixtures” (fixed API responses in the form of JSON files) and we need to copy these into the app bundle for debug builds so we need a “Run script” build phase:

```
if [ "${CONFIGURATION}" = "Debug" ]; then
  echo "Copying ${SCRIPT_INPUT_FILE_0}"
  cp -Rf "${SCRIPT_INPUT_FILE_0}" "${SCRIPT_OUTPUT_FILE_0}"
fi
```

with input file:

```
$(BUILT_PRODUCTS_DIR)/CwlFeedReaderLib_MockServiceImplementations.bundle
```

and output file

```
$(TARGET_BUILD_DIR)/$(UNLOCALIZED_RESOURCES_FOLDER_PATH)/CwlFeedReaderLib_MockServiceImplementations.bundle
```

Yuck.

Oh and it’s not really possible to establish a dependency on the tree of contents inside a folder so if you change the contents of a fixture without changing something that alters the date on the folder itself, you may need to uncheck the “Based on dependency analysis” checkbox on the build script, briefly, and build again to pick up the changes.

Double yuck.

Hopefully, a complete SE-0273 implementation is on its way and all of this agony goes away. Until then, if anyone knows a better dependency-observing way to copy Debug-only resources please let me know. Dependency analysis omissions don’t cause problems very often but when they do, it’s when you’re debugging a test failure and you swear you’ve fixed the problem but the test is still failing and… _dammit_ I fixed the problem 20 minutes ago but it just wasn’t getting picked up by the build system.

## Conclusion

App architecture is primarily about establishing roles throughout an app. By structuring our code according to roles, we aim to make code easier to write, easier to read and easier to manage. But these roles pertain only to the expression of logic and do not usually affect the output of that logic – so app architecture rarely affects the ultimate behavior of an app.

Switching to a separated Services-layer is unusual as an architectural change because, while the app’s behavior is unchanged in production, the app can also run in a second mode where the behavior is quite different – controlled and testing-friendly. A Services-layer unlocks real changes, even if these changes are limited to debugging, testing and development on non-production builds of an app.

Despite the benefits, service separation is far from widespread in the iOS app developer community. I’ve joined multiple projects where a couple tests exist in code repositories but due to lack of service separation the tests are necessarily limited and largely useless for detecting regressions. I’ve also worked on codebases where network services were separated but tests still broke each month as they relied on the system clock to select “this month’s data”. Separating the Model from services – including more services than just the network service – is a skill I hope more developers learn.

Even though I’m strongly advocating for a separate Services-layer, total isolation of all side effects is not necessarily a goal. I identified `DispatchQueue.main.async` as a “service” in CwlFeedReader but I chose _not_ to separate it since it wouldn’t affect any of the tests I had written (my tests were already waiting for asychronous expectations). Service abstractions can be simple but they’re never free. I’d like to think that if a test broke due to asychronous behavior, I would take the effort to create a separate `SchedulingService` (see my previous [Testing actions over time](https://www.cocoawithlove.com/blog/testing-actions-over-time.html) for possible approaches). Or would I try to avoid the problem another way? There isn’t a wrong answer, only a judgement call about what is right for your project.
