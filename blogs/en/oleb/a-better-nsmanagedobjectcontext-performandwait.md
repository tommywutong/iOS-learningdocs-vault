---
title: A better NSManagedObjectContext​.performAndWait
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2018/02/performandwait/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c4d313134d39765f'
translated: false
---

> 原文：[A better NSManagedObjectContext​.performAndWait](https://oleb.net/blog/2018/02/performandwait/)　·　Ole Begemann

# A better NSManagedObjectContext​.performAndWait

The [`DispatchQueue.sync`](https://developer.apple.com/documentation/dispatch/dispatchqueue/2016081-sync) method has this nice property that it automatically returns whatever value you return from the dispatched block. This allows you to write something like the following:

```
let v = queue.sync {
    return ... // computation that has to be run on queue
}
```

This is much more elegant than having to declare an optional result variable before the call to `sync`, capturing and assigning to the variable inside the closure, and finally force-unwrapping the value after `sync` has returned.

# `NSManaged​Object​Context​.perform​And​Wait(_:)`

I’d like to have the same convenience for Core Data, where [`NSManaged​Object​Context​.perform​And​Wait(_:)`](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506364-performandwait) plays a similar role as `DispatchQueue.sync`. Core Data doesn’t ship with a suitable overload of `performAndWait`, but we can provide our own in an extension:

```
extension NSManagedObjectContext {
    func performAndWait<T>(_ block: () -> T) -> T {
        var result: T? = nil
        // Call the framework version
        performAndWait {
            result = block()
        }
        return result!
    }
}
```

I chose to keep the original name, but in contrast to the existing `performAndWait` the new method is generic over a type parameter `T` — the return type of the `block` argument and the method itself. The implementation wraps a call to the framework version of the method with the boilerplate to handle the return value.

In my limited testing, the type checker had no trouble disambiguating between the two `performAndWait` overloads — it automatically chose the correct overload based on the expected return types. If you are worried about ambiguity errors, feel free to give the new method a different name.

# Error handling with `rethrows`

`DispatchQueue.sync` has another nice feature. Notice the [`rethrows`](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/Declarations.html#//apple_ref/doc/uid/TP40014097-CH34-ID531) keyword in the method signature:

```
func sync<T>(execute work: () throws -> T) rethrows -> T
```

A rethrowing function indicates that it can only throw an error if one of its function parameters throws an error. This enables two things:

1. It allows the caller to pass in a throwing function (or call throwing functions in the closure expression).
2. It gives the type checker granular control over the enforcement of the `try` keyword. Callers of `DispatchQueue.sync` only have to use `try` if the passed-in function is throwing.

Replicating `rethrows` for `performAndWait` isn’t trivial. We’d have to catch any error inside the inner closure and pass it to the outer scope in a similar fashion as we do for the return value. If we do this though, the compiler can no longer prove the only-throws-when-function-argument-throws invariant and therefore rejects the code.

[Becca Royal-Gordon just pitched to Swift Evolution](https://forums.swift.org/t/pitch-rethrows-unchecked/10078) to introduce a way for developers to opt out of the strict compiler checks for `rethrows`, analogous to what [we already have for escaping closures](https://developer.apple.com/documentation/swift/2827967-withoutactuallyescaping).

## Outsmarting the type checker

In her post, Becca also mentions how the Dispatch framework solves this issue:

> It is possible to work around this by exploiting certain bugs in the `rethrows` checking—the Dispatch overlay does this to add error handling to `DispatchQueue.sync(execute:)`.

We can use the same trick for our problem. [Check out the relevant code in the Swift repository](https://github.com/apple/swift/blob/bb157a070ec6534e4b534456d208b03adc07704b/stdlib/public/SDK/Dispatch/Queue.swift#L228-L249). And here’s the verbatim copy of the code (I only changed the function names) for `performAndWait`:

```
extension NSManagedObjectContext {
    func performAndWait<T>(_ block: () throws -> T) rethrows -> T {
        return try _performAndWaitHelper(
            fn: performAndWait, execute: block, rescue: { throw $0 }
        )
    }

    /// Helper function for convincing the type checker that
    /// the rethrows invariant holds for performAndWait.
    ///
    /// Source: https://github.com/apple/swift/blob/bb157a070ec6534e4b534456d208b03adc07704b/stdlib/public/SDK/Dispatch/Queue.swift#L228-L249
    private func _performAndWaitHelper<T>(
        fn: (() -> Void) -> Void,
        execute work: () throws -> T,
        rescue: ((Error) throws -> (T))) rethrows -> T
    {
        var result: T?
        var error: Error?
        withoutActuallyEscaping(work) { _work in
            fn {
                do {
                    result = try _work()
                } catch let e {
                    error = e
                }
            }
        }
        if let e = error {
            return try rescue(e)
        } else {
            return result!
        }
    }
}
```

`performAndWait` now calls through to a private helper function that takes two throwing functions (the original block and an error handler) and this convinces the compiler that the `rethrows` invariant holds.

# Usage

Here’s how you’d retrieve the number of records from a fetch request:

```
let context: NSManagedObjectContext = ...
let fetchRequest: NSFetchRequest = ...
let count = try context.performAndWait {
    return try context.count(for: fetchRequest)
}
```

Another nice improvement to `performAndWait` would be to have it pass the managed object context to the worker block, [as Michael Tsai does in his solution](https://twitter.com/mjtsai/status/965595380711870467).

---

## A simpler solution

**Update April 22, 2019:** [Karim Abou Zeid suggests](https://twitter.com/swiftkarim/status/1243601831714000898) a simpler solution: we can provide two overloads of `performAndWait`, a non-throwing one and one that takes a throwing function and rethrows any errors to its caller. The compiler is smart enough to pick the correct overload depending on whether the function the caller passes to `performAndWait` can throw errors or not.

The complete code looks like this:

```
extension NSManagedObjectContext {
    func performAndWait<T>(_ block: () throws -> T) throws -> T {
        var result: Result<T, Error>?
        performAndWait {
            result = Result { try block() }
        }
        return try result!.get()
    }

    func performAndWait<T>(_ block: () -> T) -> T {
        var result: T?
        performAndWait {
            result = block()
        }
        return result!
    }
}
```

The small downside to this approach is that both methods will appear in code completion.
