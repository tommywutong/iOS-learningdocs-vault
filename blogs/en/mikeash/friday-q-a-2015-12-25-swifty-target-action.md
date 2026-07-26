---
title: 'Friday Q&A 2015-12-25: Swifty Target/Action'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-12-25-swifty-targetaction.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2cbb7a7be784c112'
translated: false
---

> 原文：[Friday Q&A 2015-12-25: Swifty Target/Action](https://www.mikeash.com/pyblog/friday-qa-2015-12-25-swifty-targetaction.html)　·　mikeash.com Friday Q&A

Posted at 2015-12-25 15:11 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2016-01-29: Swift Struct Storage](https://www.mikeash.com/pyblog/friday-qa-2016-01-29-swift-struct-storage.html)  
Previous article: [Friday Q&A 2015-12-11: Swift Weak References](https://www.mikeash.com/pyblog/friday-qa-2015-12-11-swift-weak-references.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2015-12-25: Swifty Target/Action

by [Mike Ash](https://www.mikeash.com/)

**Overview**  
The target/action system is great for things like menu items which might command many different objects depending on context. For example, the Paste menu item connects to whatever object in the responder chain happens to implement a `paste:` method at the time.

It's less great when you're setting the target and and action in code and there's only ever one target object, as is commonly the case for buttons, text fields, and other such controls. It ends up being an exercise in [stringly typed](http://c2.com/cgi/wiki?StringlyTyped) code and tends to be a bit error-prone. It also forces the action to be implemented separately, even when it's simple and would naturally fit inline.

Implementing a pure Swift control that accepted a function as its action would be simple, but for real code we still need to deal with Cocoa. The goal is to adapt `NSControl` to allow setting a function as the target, while still coexisting with the target/action system.

`NSControl` doesn't have any good hooks to intercept the sending of the action, so instead we'll just co-opt the existing targe/action mechanism. This requires an adapter object to act as the target. When it receives the action, it will then invoke the function passed to it.

**First Attempt**  
Let's get started with some code. Here is an adapter object that holds a function and calls that function when its action method is called:

```
    class ActionTrampoline: NSObject {
        var action: NSControl -> Void

        init(action: NSControl -> Void) {
            self.action = action
        }

        @objc func action(sender: NSControl) {
            action(sender)
        }
    }
```

Here's an addition to `NSControl` that wraps the creation of the trampoline and setting it as the target:

```
    extension NSControl {
        @nonobjc func setAction(action: NSControl -> Void) {
            let trampoline = ActionTrampoline(action: action)
            self.target = trampoline
            self.action = "action:"
        }
    }
```

(The `@nonobjc` annotation allows this to coexist with the Objective-C `action` property on `NSControl`. Without it, this method would need a different name.)

Let's try it out:

```
    let button = NSButton()
    button.setAction({ print("Action from \($0)") })
    button.sendAction(button.action, to: button.target)
```

Oops, nothing happens.

**Extending the Trampoline's Lifetime**  
This first attempt doesn't work, because `target` is a weak property. There are no strong references to `trampoline` to keep it alive, so it's deallocated immediately. Then the call to `sendAction` sends the action to `nil`, which does nothing.

We need to extend the trampoline's lifetime. We could return it to the caller and require them to keep it around somewhere, but that would be inconvenient. A better way is to tie the trampoline's lifetime to that of the control. We can accomplish this using associated objects.

We start by defining a key for use with the associated objects API. This is a little less convenient than in Objective-C, because Swift is not so friendly about taking the address of variables, and in fact doesn't guarantee that the pointer produced by using `&` on variable will be consistent. Instead of trying to use the address of a global variable, this code just allocates a bit of memory and uses that address:

```
    let NSControlActionFunctionAssociatedObjectKey = UnsafeMutablePointer<Int8>.alloc(1)
```

The `NSControl` extension then uses `objc_setAssociatedObject` to attach the `trampoline` to the control. Although the value is never retrieved, simply setting it ensures that it is kept alive as long as the control is alive:

```
    extension NSControl {
        @nonobjc func setAction(action: NSControl -> Void) {
            let trampoline = ActionTrampoline(action: action)
            self.target = trampoline
            self.action = "action:"

            objc_setAssociatedObject(self, NSControlActionFunctionAssociatedObjectKey, trampoline, .OBJC_ASSOCIATION_RETAIN)
        }
    }
```

Let's try it again:

```
    let button = NSButton()
    button.setAction({ print("Action from \($0)") })
    button.sendAction(button.action, to: button.target)
```

This time it works!

```
    Action from <NSButton: 0x7fe1019124d0>
```

**Making it Generic**  
This first version works fine, but the types aren't quite right. The parameter to the function is always `NSControl`. That means that while the above test code works, this does not:

```
    button.setAction({ print("Action from \($0.title)") })
```

This will fail to compile, because `NSControl` doesn't have a `title` property. We know that the parameter is actually an `NSButton`, but the compiler doesn't know that. In Objective-C, we simply declare the proper type in the method and the compiler has to trust us. In Swift, we have to educate the compiler about the types.

We could make `setAction` generic, something like:

```
    func setAction<T>(action: T -> Void) { ...
```

But this requires an explicit type on the function passed in, so `$0` would no longer work. You'd have to write something like:

```
    button.setAction({ (sender: NSButton) in ...
```

It would be a lot better to have type inference work for us.

Swift's `Self` type exists for this purpose. `Self` denotes the actual type of `self`, like `instancetype` does for Objective-C. For example:

```
    extension NSControl {
        func frobnitz() -> Self {
            Swift.print("Frobbing \(self)")
            return self
        }
    }

    button.frobnitz().title = "hello"
```

Let's use this in the NSControl extension to make it generic:

```
    extension NSControl {
        @nonobjc func setAction(action: Self -> Void) {
```

Oops, we can't:

```
    error: 'Self' is only available in a protocol or as the result of a method in a class; did you mean 'NSControl'?
```

Fortunately, the error message suggests a way forward: put the method in a protocol. Start with an empty protocol:

```
    protocol NSControlActionFunctionProtocol {}
```

Let's change the name of the associated object key to fit its new home, while we're at it:

```
    let NSControlActionFunctionProtocolAssociatedObjectKey = UnsafeMutablePointer<Int8>.alloc(1)
```

We'll need a generic version of `ActionTrampoline`. This it much like the original version, but the implementation of `action` requires a forced cast since `@objc` methods aren't allowed to refer to a generic type:

```
    class ActionTrampoline<T>: NSObject {
        var action: T -> Void

        init(action: T -> Void) {
            self.action = action
        }

        @objc func action(sender: NSControl) {
            action(sender as! T)
        }
    }
```

The method implementation is basically the same as before, just with `Self` instead of `NSControl`. Constraining the extension to `Self: NSControl` lets us use all `NSControl` methods and properties on `self`, like `target` and `action`:

```
    extension NSControlActionFunctionProtocol where Self: NSControl {
        func setAction(action: Self -> Void) {
            let trampoline = ActionTrampoline(action: action)
            self.target = trampoline
            self.action = "action:"
            objc_setAssociatedObject(self, NSControlActionFunctionProtocolAssociatedObjectKey, trampoline, .OBJC_ASSOCIATION_RETAIN)
        }
    }
```

Finally, we need to make `NSControl` conform to this protocol in an extension. Since the protocol itself is empty, the extension can be empty too:

```
    extension NSControl: NSControlActionFunctionProtocol {}
```

Let's try it out!

```
    let button = NSButton()
    button.setAction({ (button: NSButton) in
        print("Action from \(button.title)")
    })
    button.sendAction(button.action, to: button.target)
```

This prints:

```
    Action from Button
```

Success!

**UIKit Version**  
Adopting this code for use in UIKit is easy. `UIControl` can have multiple targets for a variety of different events, so we just need to allow passing in the events as a parameter, and use `addTarget` to add the trampoline:

```
    class ActionTrampoline<T>: NSObject {
        var action: T -> Void

        init(action: T -> Void) {
            self.action = action
        }

        @objc func action(sender: UIControl) {
            print(sender)
            action(sender as! T)
        }
    }

    let NSControlActionFunctionProtocolAssociatedObjectKey = UnsafeMutablePointer<Int8>.alloc(1)

    protocol NSControlActionFunctionProtocol {}
    extension NSControlActionFunctionProtocol where Self: UIControl {
        func addAction(events: UIControlEvents, _ action: Self -> Void) {
            let trampoline = ActionTrampoline(action: action)
            self.addTarget(trampoline, action: "action:", forControlEvents: events)
            objc_setAssociatedObject(self, NSControlActionFunctionProtocolAssociatedObjectKey, trampoline, .OBJC_ASSOCIATION_RETAIN)
        }
    }
    extension UIControl: NSControlActionFunctionProtocol {}
```

Testing it:

```
    let button = UIButton()
    button.addAction([.TouchUpInside], { (button: UIButton) in
        print("Action from \(button.titleLabel?.text)")
    })
    button.sendActionsForControlEvents([.TouchUpInside])

    Action from nil
```

Apparently `UIButton` doesn't set a title by default like `NSButton` does. But, success!

**A Note on Retain Cycles**  
It's easy to make retain cycles using this call. For example:

```
    button.addAction({ _ in
        self.doSomething()
    })
```

If you hold a strong reference to `button` (note that even if you declare `button` as `weak`, you'll indirectly hold a strong reference to it if you hold a strong reference to a view that contains it, or its window) then this will create a cycle that will cause your object to leak.

As is usually the case with cycles, the answer is to capture `self` either as weak or unowned:

```
    button.addAction({ [weak self] _ in
        self?.doSomething()
    })
```

Optional chaining keeps the body easy to read. Or if you're sure that the action will never, ever be invoked after `self` is destroyed, use `[unowned self]` instead to get a weak reference which doesn't need to be `nil` checked since it will fail loudly if `self` is ever destroyed early.

**Conclusion**  
Making a Swift-y adapter for Cocoa target/actions is fairly straightforward. Memory management means we have to work a little to keep the trampoline object alive, but associated objects solve that problem. Making a method that has a parameter that's generic on the type of `self` requires jumping through some hoops, but a protocol extension makes it possible.

That's it for today. I'll be back with more goodies in the new year. Friday Q&A is driven by reader ideas, so if you have any topics you'd like to see covered in 2016 or beyond, please [send them in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-12-25-swifty-targetaction.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
