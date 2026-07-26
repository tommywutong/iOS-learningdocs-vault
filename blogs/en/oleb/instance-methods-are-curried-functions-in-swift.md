---
title: Instance Methods are “Curried” Functions in Swift
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/07/swift-instance-methods-curried-functions/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:0428a5cb021d5e27'
translated: false
---

> 原文：[Instance Methods are “Curried” Functions in Swift](https://oleb.net/blog/2014/07/swift-instance-methods-curried-functions/)　·　Ole Begemann

# Instance Methods are “Curried” Functions in Swift

**An instance method in Swift is just a type method that takes the instance as an argument and returns a function which will then be applied to the instance.**

I [recently learned](https://devforums.apple.com/message/1012414#1012414) about a Swift feature that blew my mind a little. Instance methods are just (partially) “curried” functions that take the instance as the first argument. What’s a curried function, you ask?

# Currying

The idea behind _currying_ (named after mathematician [Haskell Curry](https://en.wikipedia.org/wiki/Haskell_Curry)) is that you any function that takes multiple parameters can be transformed into a chained series of fundtions that take one argument each.

For example, suppose you have function of type `(Int, Double) -> String` — it takes an `Int` and a `Double`, and returns a `String`. If we _curry_ this function, we get `(Int) -> (Double) -> (String)`, i.e. a function that takes just an `Int` and returns a second function. This second function then takes the `Double` argument and returns the final `String`. To call the curried function, you’d chain two function calls:

```
let result: String = f(42)(3.14)
// f takes an Int and returns a function that takes a Double.
```

Why would you want to do this? The big advantage of curried functions is that they can be _partially applied_, i.e. some arguments can be specified (bound) before the function is ultimately called. Partial function application yields a new function that you can then e.g. pass around to another part of your code. Languages like Haskell and ML use currying for all functions.

Swift uses the same idea of partial application for instance methods. Although it’s not really accurate to say instance methods in Swift are “curried”, I still like to use this term.

# Example

Consider this simple example of a class that represents a bank account:

```
class BankAccount {
    var balance: Double = 0.0

    func deposit(_ amount: Double) {
        balance += amount
    }
}
```

We can obviously create an instance of this class and call the `deposit()` method on that instance:

```
let account = BankAccount()
account.deposit(100) // balance is now 100
```

So far, so simple. But we can also do this:

```
let depositor = BankAccount.deposit(_:)
depositor(account)(100) // balance is now 200
```

This is totally equivalent to the above. What’s going on here? We first assign the method to a variable. Note that we didn’t pass an argument after `BankAccount.deposit(_:)` — we’re not _calling_ the method here (which would yield an error because you can’t call an instance method on the type), just referencing it, much like a function pointer in C. The second step is then to call the function stored in the `depositor` variable. Its type is as follows:

```
let depositor: BankAccount -> (Double) -> ()
```

In other words, this function has a single argument, a `BankAccount` instance, and returns _another function_. This latter function takes a `Double` and returns nothing. You should recognize the signature of the `deposit()` instance method in this second part.

I hope you can see that an instance method in Swift is simply a type method that takes the instance as an argument and returns a function which will then be applied to the instance. Of course, we can also do this in one line, which makes the relationship between type methods and instance methods even clearer:

```
BankAccount.deposit(account)(100) // balance is now 300
```

By passing the instance to `BankAccount.deposit()`, the instance gets bound to the function. In a second step, that function is then called with the other arguments. Pretty cool, eh?

# Implementing Target-Action in Swift

Christoffer Lernö shows in [a post on the developer forums](https://devforums.apple.com/message/1008188#1008188) how this characteristic of Swift’s type system can be used to implement [the target-action pattern](https://developer.apple.com/library/ios/documentation/general/conceptual/Devpedia-CocoaApp/TargetAction.html) in pure Swift. In contrast to the common implementation in Cocoa, Christoffer’s solution does not rely on Objective-C’s dynamic message dispatch mechanism. And it comes with full type safety because it does not rely on selectors.

This pattern is often better than using plain closures for callbacks, especially when the receiving objects has to hold on to the closure for an indeterminate amount of time. Using closures often forces the caller of the API to do extra work to prevent strong reference cycles. With the target-action pattern, the object that provides the API can do the strong-weak dance internally, which leads to cleaner code on the calling side.

For example, a `Control` class using target-action might look like this in Swift (adopted from [a dev forums post by Jens Jakob Jensen](https://devforums.apple.com/message/1009149#1009149)):

**Update July 29, 2014:** Made the `action` property in `TargetActionWrapper` non-optional. `target` must be optional because it is `weak`.

```
protocol TargetAction {
    func performAction()
}

struct TargetActionWrapper<T: AnyObject> : TargetAction {
    weak var target: T?
    let action: (T) -> () -> ()

    func performAction() -> () {
        if let t = target {
            action(t)()
        }
    }
}

enum ControlEvent {
    case touchUpInside
    case valueChanged
    // ...
}

class Control {
    var actions = [ControlEvent: TargetAction]()

    func setTarget<T: AnyObject>(_ target: T, action: @escaping (T) -> () -> (), controlEvent: ControlEvent) {
        actions[controlEvent] = TargetActionWrapper(target: target, action: action)
    }

    func removeTargetForControlEvent(controlEvent: ControlEvent) {
        actions[controlEvent] = nil
    }

    func performActionForControlEvent(controlEvent: ControlEvent) {
        actions[controlEvent]?.performAction()
    }
}
```

Usage:

```
class MyViewController {
    let button = Control()

    func viewDidLoad() {
        button.setTarget(self, action: MyViewController.onButtonTap, controlEvent: .touchUpInside)
    }

    func onButtonTap() {
        print("Button was tapped")
    }
}
```
