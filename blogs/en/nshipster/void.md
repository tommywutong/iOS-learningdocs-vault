---
title: Void
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/void/'
original_language: en
published: 2018-10-31
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:b787fb308716ce90'
translated: false
---

> 原文：[Void](https://nshipster.com/void/)　·　NSHipster (Mattt)

# [Void](https://nshipster.com/void/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  October 31^st, 2018

Nothingness has been a regular topic of discussion on NSHipster, from [our first article about `nil` in Objective-C](https://nshipster.com/nil/) to [our recent look at the `Never` type in Swift](https://nshipster.com/never/). But today’s article is perhaps the most fraught with [_horror vacui_](https://en.wikipedia.org/wiki/Horror_vacui) of them all, as we gaze now into the `Void` of Swift.

---

What is `Void`? In Swift, it’s nothing but an empty tuple.

```
typealias Void = ()
```

We become aware of the `Void` as we fill it.

```
let void: Void = ()
void. // No Completions
```

`Void` values have no members: no methods, no values, not even a name. It’s a something more nothing than `nil`. For an empty vessel, Xcode gives us nothing more than empty advice.

## Something for Nothing

Perhaps the most prominent and curious use of the `Void` type in the standard library is found in the `ExpressibleByNilLiteral` protocol.

```
protocol ExpressibleByNilLiteral {
    init(nilLiteral: ())
}
```

Types conforming to `ExpressibleByNilLiteral` can be initialized with the `nil` literal. Most types don’t adopt this protocol, as it makes more sense to represent the absence of a specified value using an `Optional` for that type. But you may encounter it occasionally.

The required initializer for `ExpressibleByNilLiteral` shouldn’t take any real argument. (If it did, what would that even be?) However, the requirement can’t just be an empty initializer `init()` — that’s already used as the default initializer for many types.

You could try to work around this by changing the requirement to a type method that returned a `nil` instance, but some mandatory internal state may be inaccessible outside of an initializer. But a better solution — and the one used here — is to add a `nilLiteral` label by way of a `Void` argument. It’s an ingenious use of existing functionality to achieve unconventional results.

## No Things Being Equal

Tuples, along with metatypes (like `Int.Type`, the result of calling `Int.self`), function types (like `(String) -> Bool`) and existentials (like `Encodable & Decodable`), comprise non-nominal types. In contrast to the nominal, or named, types that comprise most of Swift, non-nominal types are defined in relation to other types.

Non-nominal types cannot be extended. `Void` is an empty tuple, and because tuples are non-nominal types, you can’t add methods or properties or conformance to protocols.

```
extension Void {} // Non-nominal type 'Void' cannot be extended
```

`Void` doesn’t conform to `Equatable` — it simply can’t. Yet when we invoke the “is equal to” operator (`==`), it works as expected.

```
void == void // true
```

We reconcile this apparent contradiction with a global free-function, declared outside of any formal protocol.

```
func == (lhs: (), rhs: ()) -> Bool {
    return true
}
```

This same treatment is given to the “is less than” operator (`<`), which acts as a stand-in for the `Comparable` protocol and its derived comparison operators.

```
func < (lhs: (), rhs: ()) -> Bool {
    return false
}
```

## Ghost in the Shell

`Void`, as a non-nominal type, can’t be extended. However, `Void` is still a type, and can, therefore, be used as a generic constraint.

For example, consider this generic container for a single value:

```
struct Wrapper<Value> {
    let value: Value
}
```

We can first take advantage of [conditional conformance](https://swift.org/blog/conditional-conformance/), arguably _the_ killer feature in Swift 4.1, to extend `Wrapper` to adopt `Equatable` when it wraps a value that is itself `Equatable`.

```
extension Wrapper: Equatable where Value: Equatable {
    static func ==(lhs: Wrapper<Value>, rhs: Wrapper<Value>) -> Bool {
        return lhs.value == rhs.value
    }
}
```

Using the same trick from before, we can approximate `Equatable` behavior by implementing a top-level `==` function that takes `Wrapper<Void>` arguments.

```
func ==(lhs: Wrapper<Void>, rhs: Wrapper<Void>) -> Bool {
    return true
}
```

In doing so, we can now successfully compare two constructed wrappers around `Void` values.

```
Wrapper(value: void) == Wrapper(value: void) // true
```

However, if we attempt to assign such a wrapped value to a variable, the compiler generates a mysterious error.

```
let wrapperOfVoid = Wrapper<Void>(value: void)
// 👻 error: Couldn't apply expression side effects :
// Couldn't dematerialize wrapperOfVoid: corresponding symbol wasn't found
```

The horror of the `Void` becomes once again its own inverted retort.

## The Phantom Type

Even when you dare not speak its non-nominal name, there is no escaping `Void`.

Any function declaration with no explicit return value implicitly returns `Void`

```
func doSomething() { ... }

// Is equivalent to

func doSomething() -> Void { ... }
```

This behavior is curious, but not particularly useful, and the compiler will generate a warning if you attempt to assign a variable to the result of a function that returns `Void`.

```
doSomething() // no warning

let result = doSomething()
// ⚠️ Constant 'result' inferred to have type 'Void', which may be unexpected
```

You can silence this warning by explicitly specifying the `Void` type.

```
let result: Void = doSomething() // ()
```

## Trying to Return from the Void

If you squint at `Void?` long enough, you might start to mistake it for `Bool`. These types are isometric, both having exactly two states: `true` / `.some(())` and `false` / `.none`.

But isometry doesn’t imply equivalence. The most glaring difference between the two is that `Bool` is `ExpressibleByBooleanLiteral`, whereas `Void` isn’t — and can’t be, for the same reasons that it’s not `Equatable`. So you can’t do this:

```
(true as Void?) // error
```

But hard-pressed, `Void?` can act in the same way as `Bool`. Consider the following function that randomly throws an error:

```
struct Failure: Error {}

func failsRandomly() throws {
    if Bool.random() {
        throw Failure()
    }
}
```

The correct way to use this method is to call it within a `do / catch` block using a `try` expression.

```
do {
    try failsRandomly()
    // executes on success
} catch {
    // executes on failure
}
```

The incorrect-but-ostensibly-valid way to do this would be to exploit the fact that `failsRandomly()` implicitly returns `Void`. The `try?` expression transforms the result of a statement that throws into an optional value, which in the case of `failsRandomly()`, results in `Void?`. If `Void?` has `.some` value (that is, `!= nil`), that means the method returned without throwing an error. If `success` is `nil`, then we know that the method produced an error.

```
let success: Void? = try? failsRandomly()
if success != nil {
    // executes on success
} else {
    // executes on failure
}
```

As much as you may dislike the ceremony of `do / catch` blocks, you have to admit that they’re a lot prettier than what’s happening here.

It’s a stretch, but this approach might be valid in very particular and peculiar situations. For example, you might use a static property on a class to lazily produce some kind of side effect exactly once using a self-evaluating closure:

```
static var oneTimeSideEffect: Void? = {
   return try? data.write(to: fileURL)
}()
```

Even still, an `Error` or `Bool` value would probably be more appropriate.

## Things that go _“Clang”_ in the Night

If, while reading this chilling account you start to shiver, you can channel the necrotic energy of the `Void` type to conjure immense amounts of heat to warm your spirits.

…which is to say, the following code causes `lldb-rpc-server` to max out your CPU:

```
extension Optional: ExpressibleByBooleanLiteral where Wrapped == Void {
    public typealias BooleanLiteralType = Bool

    public init(booleanLiteral value: Bool) {
        if value {
            self.init(())!
        } else {
            self.init(nilLiteral: ())!
        }
    }
}

let pseudoBool: Void? = true // we never get to find out
```

Keeping in the Lovecraft-ian tradition, `Void` has a physical form that the computer is incapable of processing; simply witnessing it renders the process incurably insane.

## A Hollow Victory

Let’s conclude our hallowed study of `Void` with a familiar refrain.

```
enum Result<Value, Error> {
    case success(Value)
    case failure(Error)
}
```

If you recall [our article about the `Never` type](https://nshipster.com/never), a `Result` type with its `Error` type set to `Never` can be used to represent operations that always succeed.

In a similar way, we might use `Void` as the `Value` type to represent operations that, when they succeed, don’t produce any meaningful result.

For example, apps may implement tell-tale heartbeat by regularly “pinging” a server with a simple network request.

```
func ping(_ url: URL, completion: (Result<Void, Error>) -> Void) {
    …
}
```

In the completion handler of the request, success would be indicated by the following call:

```
completion(.success(()))
```

Not enamored with effusive parentheticals (but why not?), you could make thing a bit nicer through a strategic extension on `Result`.

```
extension Result where Value == Void {
    static var success: Result {
        return .success(())
    }
}
```

Nothing lost; nothing gained.

```
completion(.success)
```

---

It may seem like a purely academic exercise — philosophical, even. But an investigation into the `Void` yields deep insights into the very fabric of reality for the Swift programming language.

In ancient times, long before Swift had seen the light of day, tuples played a fundamental role in the language. They represented argument lists and associated enumeration values, fluidly moving between its different contexts. At some point that model broke down. And the language has yet to reconcile the incongruities between these disparate constructs.

So according to Swift Mythos, `Void` would be the paragon of the elder gods: the true singleton, blind nullary at the center of infinity unaware of its role or influence; the compiler unable to behold it.

But perhaps this is all just an invention at the periphery of our understanding — a manifestation of our misgivings about the long-term viability of the language. After all, when you stare into the `Void`, the `Void` stares back into you.
