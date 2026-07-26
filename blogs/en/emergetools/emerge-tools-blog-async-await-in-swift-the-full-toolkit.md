---
title: 'Emerge Tools Blog | Async await in Swift: The Full Toolkit'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:7967d4f36025a698'
translated: false
---

> 原文：[Emerge Tools Blog | Async await in Swift: The Full Toolkit](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit)　·　Emerge Tools Blog

# Async await in Swift: The Full Toolkit

July 22, 2024 by

Jacob Bartlett

SwiftiOSGuest post

![Async await in Swift: The Full Toolkit](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcover.afa0c323.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Here's one of my favourite iOS interview questions:

> _"Tell me about the tools available in Swift Concurrency, and when you might use them"_

I like it because it's open-ended, giving candidates the scope to demonstrate junior, mid, or senior levels of knowledge. More than just asking for a list of syntax, it also checks candidates can identify when each of the tools might be the right one for the job.

Today, we're going through the many techniques in the Swift Concurrency toolkit. We'll discuss theory when it's appropriate, but for each tool we'll also provide a context where it might be the best solution.

## [The Toolkit](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#the-toolkit)

- [async / await](#async-await)
- [async let](#async-let)
- [Task](#task)
- [Task group](#task-group)
- [Actors](#actors)
- [MainActor](#main-actor)
- [Sendable](#sendable)
- [Continuations (theory)](#continuations-theory)
- [Continuations (practice)](#continuations-practice)
- [AsyncSequence](#async-sequence)
- [AsyncStream](#async-stream)
- [Async Algorithms](#async-algorithms)

### [async / await](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#async-await)

This is the fundamental syntactic building block of Swift Concurrency.

Marking a function as `async` tells the Swift compiler that it can be suspended. The `await` keyword marks these suspension points. When reaching a suspension point, the Swift runtime can store the state of the stack frame on the heap as an _async frame_, to resume it later.

While a function is suspended at an await call, the thread on which it was executing can be utilised to perform other work. The runtime can resume execution of the function when the awaited work is complete.

Let's start off simple with a very basic example of this syntax in action, fetching data from an API:

```swift
func fetchUserData() async -> User { 
  let userData = await userAPI.fetchUserData()
  return userData
}
```

`async` functions can only be called from an asynchronous context. This means another async function, a Task, or perhaps even an async `main()` function (in command line apps).

### [async let](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#async-let)

The most basic use case of concurrency is enabling the CPU to perform work while waiting for a slow operation - such as a network request - to finish. The next-most fundamental use case might be performing multiple slow operations in parallel. `async let` is the easiest way to achieve this.

With naïve use of async/await, we might introduce bottlenecks to our code:

```swift
func populateStorefront() async {
  // takes 0.4 seconds
  self.products = await fetchProducts()

  // takes 0.3 seconds
  self.promotions = await fetchPromotions()

}

// total execution time: 0.7 seconds
```

The problem here is that the two slow network requests are waited for _sequentially_. We can drastically improve performance by making these wait periods overlap: making the requests run _in parallel_.

With async let, we can kick off the these operations at the same time: execution isn't suspended until the first await, when both network requests are fired off.

```swift
func populateStorefront() async {
  // network requests begin simultane
  async let products = fetchProducts()
  async let promotions = fetchPromotions()

  // waits for 0.4 seconds
  self.products = await products

  // does not wait - results already there
  self.promotions = await promotions
}

// total execution time: 0.4 seconds
```

This allows you to manage bottlenecks and perform arbitrary async workloads efficiently - there is no limitation on the types of function we can call with async let.

### [Task](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#task)

If async/await are the syntactic building blocks of Swift Concurrency, Tasks are the foundational data structure: the "unit of async work".

Tasks on their own are incredibly useful - they are the only way Swift Concurrency provides to kick off asynchronous work from inside a synchronous context:

```swift
func fetchAndSetProducts() {
  Task {
      let products = await fetchProducts()
      self.products = products
  }
}
```

This is known as _unstructured concurrency_, since this new Task has no parent relationship - it doesn't fit into the an existing _task tree_.

Tasks arrange together in a tree hierarchy, where parent tasks can spawn multiple child tasks. If a Task is cancelled, the cancellation state cascades down from the parent to all its children. Tasks continue their work when cancelled - but we can check this state in our code and terminate processing. This is called _cooperative cancellation_.

More advanced Task use cases arise when you use Tasks as a property, consider possible cancellation, and await a result:

```swift
var calculationTask: Task<Double, Error>?

func calculateProfits() async throws -> Double? {
  calculationTask = Task {
      let data = await fetchFinancialData()
      try Task.checkCancellation()
      return performExpensiveNumberCrunching(on: data)
  }

  return try await calculationTask?.value
}
```

This allows you to avoid performing expensive work if a Task is already cancelled.

### [Task group](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#task-group)

Task groups are another, more advanced, approach to parallelisation.

Compared to async let, which allows you to simultaneously wait on a _set number_ of _arbitrary_ functions, a task group allows you to wait for an _arbitrary number_ of _specialised_ functions.

If that's not clear, let's demonstrate with a simple example - we want to submit exam results to our backend for each student in an array:

```swift
func submitExamResults(for students: [Student]) async {
  await withTaskGroup(of: Void.self) { group in 
      for student in students {
          group.addTask {
              await submit(results: student.examResults)
          }
      }
  }
}
```

Here, we're running the same function `submit(results:)` method on each student's exam results simultaneously, and returning when all these functions are complete.

`await withTaskGroup` is the core syntax here, and we pass it the `Void` type because the async functions in the group don't return anything - we simply want to perform work in parallel. We could also use `withThrowingTaskGroup` to add error handling, replacing `await` with `try await`.

Task groups conceal another use case behind progressive disclosure in their initializer: constructing a return value from the results of our async tasks.

For instance, here we are batch-fetching several images at once:

```swift
func profileImages(from urls: [URL]) async -> [UIImage] {
  await withTaskGroup(of: UIImage.self, returning: [UIImage]) { group in
      for url in urls {
          group.addTask { fetchImage(for: url) }
      }
      var images: [UIImage]
      for await image in group {
          images.append(image)
      }
      return images
  }
}
```

> _A quick warning - these don't necessarily return results in the original order!_

Constructing the return value here uses the fact that task groups conform to AsyncSequence, which allows us to use the for await in syntax. More on this later.

### [Actors](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#actors)

Actors are reference-typed entities that enforce serial access to their methods and state. This makes them ideal for work that requires concurrent access to data while avoiding race conditions.

You can think of actors like classes which run all their work on an internal serial priority queue. In Swift Concurrency, this is called the [serial executor](https://swiftrocks.com/how-actors-work-internally-in-swift).

Authentication is a classic use case for actors:

```swift
actor AuthService {
  
  /// Returns an up-to-date authentication token.
  /// If the local bearer token is expired, it is refreshed.
  ///
  func getBearerToken() async throws -> String {
      try await fetchValidAuthToken()
  }
}
```

Due to your mastery of async let and task groups, your app is likely performing many network requests simultaneously. Therefore, the AuthService needs to be safely callable from many places at once.

Furthermore, we only want to refresh an expired auth token once (per expiry period), so each network request must stop and wait for _the same token_ rather than each request triggering a separate refresh.

Actors are _re-entrant_. They enforce serial access to their state, and methods on an actor are only ever being executed by one task at a time. However, methods can still suspend at an await. During this suspension, the same method might be started by a different task. That task might in turn suspend, and either task might resume next.

This multithreaded execution is known as _interleaving_.

We can use our knowledge of re-entrancy and interleaving, in conjunction with a Task, to achieve the dream authentication scenario:

```swift
actor AuthService {
  
  private var tokenTask: Task<String, Error>?
  
  func getBearerToken() async throws -> String {
      
      if tokenTask == nil {
          // actor ensures only one task can exist at a time 
          tokenTask = Task { try await fetchValidAuthToken() }
      }
         
      defer { tokenTask = nil }

      // all requests suspend here, waiting for the task to finish
      return try await tokenTask!.value
  }
}
```

Now all our network requests cooperate in perfect harmony.

> _This is probably the hardest code in this article, so take time to step through and understand it. If you want to dive deeper, you can read [Advanced Swift Actors: Re-entrancy & Interleaving](https://jacobbartlett.substack.com/p/advanced-swift-actors-re-entrancy)._

### [MainActor](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#main-actor)

Actors ensure all their code execution and state changes run on a serial executor, which performs all work as if it was on a single serial queue.

There are many use cases for this, however one very naturally arises: single-threaded UI work. As with the main queue, there is a main actor which performs all its work on the main thread.

You can constrain functions - or entire classes - to the main actor, to ensure that they will never execute work off the main thread. This is good practice for any code that touches the UI, such as your view models or view controllers:

```swift
@MainActor @Observable 
final class LibraryViewModel { 
  var books: [Book] = [] 
  func fetchBooks() async { 
      books = await libraryAPI.fetchBooks()
  } 
}
```

You might be using unstructured concurrency to asynchronously fetch models you need on a synchronous UI thread. It's good practice to ensure this is also constrained to the main actor. It's easy to do so by applying the `@MainActor` attribute in your Task closure.

```swift
func didPressButton() {
  Task { @MainActor in
      self.result = await buttonAction()
  }
}
```

One very common misconception when you get started with Swift Concurrency is that you can't await on `@MainActor` functions without blocking the main thread.

But this misunderstands how Swift Concurrency was designed: _[code written with Swift Concurrency maintains a runtime contract that ensures threads can always make forward progress](https://developer.apple.com/videos/play/wwdc2021/10254/?time=1216)_.

Therefore, when you hit await on a function constrained to the main actor, that function suspends, but the main actor is still able to make forward progress _elsewhere_ on other methods. Once the wait is complete, the rest of the function queues back up on the main actor's executor to finish running on the UI thread.

### [Sendable](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#sendable)

One of the major goals of Swift Concurrency was to prevent data races at compile-time. The `Sendable` protocol is the most critical piece of this puzzle.

When a type conforms to the Sendable protocol, that means it's thread-safe. Sendable types can be passed across arbitrary concurrency contexts without risking data races. This means they can be passed into async functions, actors, and unstructured tasks without the risk of encountering dangerous concurrency issues.

The Sendable protocol is used extensively in the Swift Standard Library. Furthermore, concrete value types (structs and enums) with properties composed only of Sendable types are implicitly Sendable. Generic value types can also conform if their associated type is Sendable:

```swift
// Exam is *not* implicitly Sendable
struct Exam<Subject> { 
  var paper: Subject 
}

// Exam *is* implicitly Sendable
struct Exam<Subject: Sendable> { 
  var paper: Subject
}
```

Classes can also be conformed to the Sendable protocol, if their properties are immutable:

```swift
final class Employee: Sendable { 
  let employeeID: String
}
```

Actors are implicitly Sendable.

Closure argument attributes can also be marked @Sendable - this means any values passed into the closure must also be Sendable, and can't be captured by reference.

Here's a relatively uninteresting method:

```swift
func callClosureInATask(_ closure: @escaping () -> Void) {
  Task {
      closure()
  }
}
```

If, in Xcode, we turn on Swift 6 strict concurrency checking, we get a compiler warning on `closure()`:

`Capture of 'then' with non-sendable type '() -> Void' in a `@Sendable` closure`

We can mark the closure `@Sendable` to tell the compiler it's safe:

```swift
func callClosureInATask(_ closure: @escaping @Sendable () -> Void) {
  Task {
      closure()
  }
}
```

Now, the compiler warning is satisfied. Sendable closures capture parameters by value, avoiding the chance of data races from conflicting, simultaneous, mutations.

### [Continuations (theory)](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#continuations-theory)

Continuations are a critical runtime implementation detail in Swift Concurrency: lightweight objects which store the state of a function when it reaches a suspension point (await) and allows it to be resumed later.

Sound familiar? That's because it is - [at runtime, continuations are represented by async frames](https://developer.apple.com/videos/play/wwdc2021/10254/?time=1038).

Threads have notoriously high overhead. It takes a lot of memory to create new threads, and a relatively long time to context-switch from one thread to another. Swift Concurrency uses the abstraction of continuations to cheaply manage switching between async contexts, allowing the system to aim for the ideal "one thread per CPU core".

This is pretty similar to Grand Central Dispatch, where queues are a cheap, fast, lightweight abstraction to avoids the overhead of thread management.

### [Continuations (practice)](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#continuations-practice)

Slightly confusingly, continuations can also be created directly.

Continuations can bridge the gap between legacy closure-based asynchronous APIs and modern Swift Concurrency. We can await, create a continuation, perform work inside a closure callback, then resume the continuation with either results or an error, returning to the suspension point.

iOS has a deep foundation of ancient Objective-C frameworks. Bridging these tools with Swift Concurrency often involves creating a lightweight continuation wrapper.

Here, we're using `ASWebAuthenticationSession` to implement OAuth in our app. This presents a modal web view allowing users to sign in with Google, returning a callback URL with an auth token.

```swift
func runOAuthSession() async throws -> URL? {
  let authURL = URL(string: "https://authurl.com")!
  let scheme = "authapp://"
  return try await withCheckedThrowingContinuation { continuation in
      let session = ASWebAuthenticationSession(
          url: authURL,
          callbackURLScheme: scheme
      ) { url, error in
          if let error = error {
              // something went wrong 
              continuation.resume(throwing: error) 
          } else {
              // successful sign-in
              continuation.resume(returning: url) 
          }
      }
      session.start()
  }
}
```

### [AsyncSequence](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#async-sequence)

`AsyncSequence` is a protocol designed as an analogy of [the Sequence protocol](https://github.com/swiftlang/swift/blob/main/stdlib/public/core/Sequence.swift#L325) in the Swift Standard Library.

Sequence denotes a type which provides sequential, iterated access to its elements. Sequences are implemented with an [iterator](https://github.com/swiftlang/swift/blob/main/stdlib/public/core/Sequence.swift#L177), which provides the `next()` element, and iteration can be performed in code with loops, using `for-in` syntax.

AsyncSequence behaves in the same way, except that the `next()` method on its iterator is async, meaning the runtime can suspend execution between each value yielded by the sequence. We can even create loops around an AsyncSequence using `for-await-in` syntax.

AsyncSequence provides a seamless inter-op with Combine. You can convert any Publisher into an AsyncSequence using the `.values` property on the publisher, transforming it into an AsyncPublisher which conforms to AsyncSequence:

```swift
import Combine

let usersPublisher = PassthroughSubject<User, Never>()

func addAllUsers() async {
  for await user in usersPublisher.values {
      addFriend(user)
  }
}
```

I recently ran into an interesting 'bug' with AsyncSequence. We were trying to convert two Combine publishers to async sequences, then handle the values with `for-await-in` loops - but only one set of values was handled. If we merged the publishers into one first, the sequence worked fine.

```swift
// only handles friends, not photos 
func handleFriendsAndPhotos() async {
  for await friend in friendsPublisher.values {
      // ...
  }
  
  for await photos in photosPublisher.values {
      // ...
  }
}

// handles friends and photos fine
func handleFriendsAndPhotos() async {
  for await (friends, photos) in friendsPublisher
      .merge(with: photosPublisher) 
      .values {
          // ...
  }
}
```

Can you spot it?

We eventually realised that the first `for-await-in` loop never 'finished' - it would listen to values from the first async iterator forever. Therefore, the second `for-await-in` loop for our other publisher was never reached!

### [AsyncStream](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#async-stream)

`AsyncStream` is a special kind of AsyncSequence - a concrete type you can instantiate and control yourself by manually sending values through.

AsyncStream works by creating a continuation and yielding values to it. This is useful when wrapping closure-based APIs that emit many callbacks. Instead of just creating a single continuation that returns (or throws) once, AsyncStream allows us to handle values from every single callback.

Here, we create an AsyncStream alongside `URLSessionDownloadDelegate` to track progress on a long-running file download.

```swift
func trackDownload() -> AsyncStream<Double> {
  AsyncStream<Double> { continuation in 
      let delegate = DownloadProgressDelegate(continuation: continuation)
      URLSession.shared.delegate = progressDelegate
  }
}

final class DownloadProgressDelegate: NSObject, URLSessionDownloadDelegate {
  // ...
  let continuation: AsyncStream<Double>.Continuation

  func urlSession(_ session: URLSession,
                  downloadTask: URLSessionDownloadTask,
                  didWriteData bytesWritten: Int64,
                  totalBytesWritten: Int64,
                  totalBytesExpectedToWrite: Int64) {
      let progress = Double(totalBytesWritten) / Double(totalBytesExpectedToWrite)
      continuation.yield(progress * 100)
  }

}
```

### [Async Algorithms](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#async-algorithms)

Async Algorithms isn't strictly a part of Swift Concurrency, since it's a package outside the standard library. That said, it's generally considered to be the replacement for Combine, so I'd be remiss to not mention it.

[Async Algorithms](https://github.com/apple/swift-async-algorithms) is the Swift Concurrency counterpart to the open-source [Swift Algorithms](https://github.com/apple/swift-algorithms) package. It primarily works with iterable sequences of values with an AsyncSequence. It contains algorithms that affect timing of values, such as `throttle()` and `debounce()`, algorithms which combine multiple sequences together such as `zip()` or `combineLatest()`, and algorithms which modify inputs like `compacted()`, `adjacentPairs()` or `removeDuplicates()`.

Async Algorithms can do much of what Combine can do, so their use cases are similar: creating pipelines to respond to asynchronous values:

```swift
import AsyncAlgorithms

let sequence1: AsyncStream<Int> = //...
let sequence2: AsyncStream<Int> = //...

func handleDebouncedCombinedSequence() async {
  for await value in sequence1
      .combineLatest(with: sequence2)
      .removeDuplicates()
      .debounce(for: .seconds(1)) {    
          handle(value)
  }
}
```

## [Conclusion](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#conclusion)

Knowing syntax and theory is only half the battle.

As an engineer, it's critical to understand your full toolkit and identify the situations in which it's an optimal solution.

You already know the best way to get this experience: write lots of code!

Run up against compiler errors when your code tries to run on the wrong actor; framework APIs that force you to learn continuations; performance bottlenecks which are solved like magic once you use async let. Practice new techniques and integrate them into your toolkit.

🍺

Jacob Bartlett

This was an Emerge Tools guest post from **Jacob Bartlett**. If you want more of his content, you can [subscribe to Jacob's Tech Tavern](https://jacobbartlett.substack.com) to receive in-depth articles about iOS, Swift, tech, and indie projects every 2 weeks; or [follow him on Twitter](https://twitter.com/jacobs_handle).
