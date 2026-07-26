---
title: 'Friday Q&A 2015-01-23: Let''s Build Swift Notifications'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-01-23-lets-build-swift-notifications.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:14af26396f1914d2'
translated: false
---

> 原文：[Friday Q&A 2015-01-23: Let's Build Swift Notifications](https://www.mikeash.com/pyblog/friday-qa-2015-01-23-lets-build-swift-notifications.html)　·　mikeash.com Friday Q&A

Posted at 2015-01-23 14:52 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-02-06: Locks, Thread Safety, and Swift](https://www.mikeash.com/pyblog/friday-qa-2015-02-06-locks-thread-safety-and-swift.html)  
Previous article: [Friday Q&A 2014-11-07: Let's Build NSZombie](https://www.mikeash.com/pyblog/friday-qa-2014-11-07-lets-build-nszombie.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [notifications](https://www.mikeash.com/pyblog/?tag=notifications) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2015-01-23: Let's Build Swift Notifications

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Bosnian (translation by Vlada Catalic)](http://vladacatalic.com/lets-build-swift-notifications/), [Macedonian (translation by Vlada Catalic)](http://balkanscience.com/lets-build-swift-notifications/), [Polish (translation by Natasha Singh)](https://www.couponmachine.in/friday-qa/), [Urdu (translation by Samuel Badree)](https://mobilemall.pk/blog/friday-qa-2015-01-23-lets-build-swift-notifications-urdu/), and [Sindhi (translation by Samuel Badree)](https://www.coupontoaster.co.uk/blog/friday-2015-01-23-lets-build-swift-notifications/).

**`NSNotifications`**  
NSNotifications are both simple and powerful, which is why they show up so often in the frameworks. Specifically, they have a few distinct advantages:

1. Loose coupling between notification senders and receivers.
2. Support for multiple receivers for a single notification.
3. property.

There are some disadvantages as well:

1. Sending and registering for notifications involves interacting with a singleton instance with no clear relationship to your classes.
2. It's not always clear what notifications are available for a particular class.
3. , it's not always clear what keys are available in the dictionary.
4. keys are dynamically typed and require cooperation between the sender and receiver that can't be expressed in the language, and messy boxing/unboxing for non-object types.
5. Removing a notification registration requires an explicit removal call.
6. It's difficult to inspect which objects are registered for any given notification, which can make it hard to debug.

My goal in reimagining notifications in Swift is to remedy these problems.

**API Sketch**  
The public face of the API is a class called `ObserverSet`. An `ObserverSet` instance holds a set of observers interested in a particular notification sent by a particular object. Rather than declaring string constants and intermediating through a singleton, the existence of a notification is just a public property of the class:

```
    class ExampleNotificationSender {
        public let exampleObservers = ObserverSet<Void>()
```

The `Void` is the type of data that's sent along with the notification. `Void` denotes a pure notification with no additional data. Sending data is as simple as providing the type:

```
        public let newURLObservers = ObserverSet<NSURL>()
```

This is a notification that provides a `NSURL` to all observers each time it's sent.

Multiple pieces of data are no problem with the magic of tuples:

```
        public let newItemObservers = ObserverSet<(String, Int)>()
```

This provides each observer with the name and index of a new item. If you want to make this more explicit, you can even give the parameters names:

```
        public let newItemObservers = ObserverSet<(name: String, index: Int)>()
```

To register an observer, add a callback to the observer set:

```
    object.exampleObservers.add{ println("Got an example notification") }
    object.newURLObservers.add{ println("Got a new URL: \($0)") }
```

The `add` method returns a token that can be used to remove the observer:

```
    let token = object.newItemObservers.add{ println("Got a new item named \($0) at index \($1)") }
    ...
    object.newItemObservers.remove(token)
```

A common case for notifications is to receive them with a method, and deregister the notification when the instance is deallocated. This is easy to accomplish using a variant `add` method:

```
    object.newItemObservers.add(self, self.dynamicType.gotNewItem)

    func gotNewItem(name: String, index: Int) {
        println("Got a new item: \(name) \(index)")
    }
```

The `self.dynamicType` syntax is a bit verbose and redundant, but tolerable. The observer set will hold a weak reference to `self` and automatically remove the observer when the instance is deallocated, and in the meantime it will invoke `gotNewItem` whenever it sends a notification.

Sending a notification involves calling `notify` and passing the appropriate parameters:

```
    exampleObservers.notify()
    newURLObservers.notify(newURL)
    newItemObservers.notify(name: newItemName, index: newItemIndex)
```

This makes for a really nice API. Going through the disadvantages listed above:

1. pair is represented with a separate observer set instance.
2. All notifications available for a class are public properties of that class.
3. Explicit parameters are used to pass data to observers. They can be named in code to make it clear exactly what they are.
4. Notification parameters are statically typed. The types are specified in the observer set property and notification senders and receivers are checked by the compiler. All types are supported, with no need for boxing.
5. For the common case where an observer is removed when deallocated, removal can be automatic.
6. Each observer set maintains a list of entries which can be inspected in the debugger.

Looks good! How, then, do we build it?

**Observer Function Types**  
Let's assume that the parameters to an observer function are called `Parameters`, which is the name I'll use for the generic type in the code. Fundamentally, an observer function's type is then `Parameters -> Void`. However, for the common case where the observer function is a method, this makes it difficult to hold a weak reference to the observer object and clear the entry when the object is destroyed. When you get a method from a class, like `self.dynamicType.gotNewItem`, the type of the resulting function is actually `TheClass -> Parameters -> Void`. You call the function and pass it an instance of the class, and it then returns a new function for the method that applies to that instance.

In order to keep everything organized, we'll store a weak reference to the observer object, and we'll store the observer function in this longer form. For the simpler form of the `add` method, the function can simply be wrapped in another function that throws away its parameter and returns the original function. Since observer objects can be different types, we'll store them as `AnyObject` and the observer functions as `AnyObject -> Parameters -> Void`.

**Code**  
It's time to look at the implementation. As usual, the code is available on GitHub:

[https://github.com/mikeash/SwiftObserverSet](https://github.com/mikeash/SwiftObserverSet)

**Entries**  
Each entry in an observer set is a weakly held observer object and a function. This small generic class bundles the two together, allowing for arbitrary parameter types:

```
    public class ObserverSetEntry<Parameters> {
        private weak var object: AnyObject?
        private let f: AnyObject -> Parameters -> Void

        private init(object: AnyObject, f: AnyObject -> Parameters -> Void) {
            self.object = object
            self.f = f
        }
    }
```

The observer set can use the object and function to call observers, and can check the object for `nil` to remove entries for deallocated objects. This class is marked `public` because it will also be returned to callers to be used as the parameter to the `remove` method.

Ideally, this class would be nested inside `ObserverSet`. However, Swift doesn't allow nesting generic types, so it has to be a separate top-level type.

**Observer Set**  
The `ObserverSet` class also has generic `Parameters`:

```
    public class ObserverSet<Parameters> {
```

`NSNotificationCenter` is thread safe, and this class should be as well. I chose to use a serial dispatch queue to accomplish that:

```
        private var queue = dispatch_queue_create("com.mikeash.ObserverSet", nil)
```

I also wrote a quick helper function for it:

```
        private func synchronized(f: Void -> Void) {
            dispatch_sync(queue, f)
        }
```

With this, it's as simple as writing `synchronized{ ...code... }` on the code that uses shared data.

The entries are kept in an array:

```
        private var entries: [ObserverSetEntry<Parameters>] = []
```

Properly speaking, this should be a set rather than an array. However, sets aren't all that nice to use in Swift yet, as there's no built-in set type. Instead, you have to either use `NSSet`, or use a `Dictionary` with a `Void` value type. Since observer sets will typically contain a few entries at most, I decided to go for clarity instead.

Swift also insists on an explicit public initializer, even though it's empty, as the default one apparently isn't made public:

```
        public init() {}
```

That takes care of setup. Let's look at the main `add` method, which takes an observer object and function:

```
        public func add<T: AnyObject>(object: T, _ f: T -> Parameters -> Void) -> ObserverSetEntry<Parameters> {
```

Next, construct an entry. The type of `f` doesn't quite match what `ObserverSetEntry` expects, as it's looking for a function that takes `AnyObject`, while this one takes `T`. A small adapter takes care of the mismatch with a type cast:

```
            let entry = ObserverSetEntry<Parameters>(object: object, f: { f($0 as T) })
```

It's unfortunate to bypass Swift's type system in this way, but it gets the job done.

With the entry created, add it to the array:

```
            synchronized {
                self.entries.append(entry)
            }
```

Finally, the entry is returned to the caller:

```
            return entry
        }
```

The other `add` method is a small adapter:

```
        public func add(f: Parameters -> Void) -> ObserverSetEntry<Parameters> {
            return self.add(self, { ignored in f })
        }
```

This passes `self` as the object simply because it's a convenient pointer that's guaranteed to stay alive. Since entries with `nil` objects are removed, this keeps the entry around as long as the observer set itself. The function passed in for the second parameter just ignores its parameter and returns `f`.

The `remove` method is implemented by filtering the array to remove the matching entry. Swift's `Array` type doesn't have a `remove` method, but the `filter` method accomplishes the same task:

```
        public func remove(entry: ObserverSetEntry<Parameters>) {
            synchronized {
                self.entries = self.entries.filter{ $0 !== entry }
            }
        }
```

The `notify` method is simple in principle: for each entry, call the observer function, and remove any entry with a `nil` observer object. However, it's made a bit complicated by the fact that `entries` needs to be accessed from within `synchronized`, but it's a bad idea to call observer functions from there, because it could easily lead to a deadlock. To avoid that problem, the strategy is to collect all of the observer functions in a local array, then iterate and call them outside of the `synchronized` block. Here's the function:

```
        public func notify(parameters: Parameters) {
```

The functions to call are collected in an array:

```
            var toCall: [Parameters -> Void] = []
```

Note that the type of the functions doesn't include the initial `AnyObject ->`. To keep things simple, we'll make that first call within the `synchronized` block, so that the functions collected in the array are the final observer functions with the observer object already applied.

Iterating over the entries needs to happen in a `synchronized` block:

```
            synchronized {
                for entry in self.entries {
```

Skip entries with a `nil` object:

```
                    if let object: AnyObject = entry.object {
```

Calling `entry.f` with the object produces the observer function to call:

```
                        toCall.append(entry.f(object))
                    }
                }
```

Before we leave the `synchronized` block, clean up the entries by filtering out the ones that now contain `nil`:

```
                self.entries = self.entries.filter{ $0.object != nil }
            }
```

Now that the functions are collected and the `synchronized` block is finished, we call the observer functions:

```
            for f in toCall {
                f(parameters)
            }
        }
```

That's it for the `ObserverSet` class. Let's not forget the closing brace:

```
    }
```

**A Note on Tuples**  
You'll note that none of the `ObserverSet` code presented addresses the case where there are multiple `Parameters`, for example:

```
        public let newItemObservers = ObserverSet<(String, Int)>()
```

However, it works anyway, using the code above. What's going on?

It turns out that Swift makes no distinction between a function that takes multiple parameters and a function that takes one paremeter whose type is a tuple. For example, this code calls a function using both ways:

```
    func f(x: Int, y: Int) {}

    f(0, 0)

    let params = (0, 0)
    f(params)
```

This means that the `ObserverSet` code can be written for functions with one parameter, and it gets support for multiple parameters for free. There are some strong limits on what you can do in these cases (for example, it's essentially impossible to modify any of the parameters) but it works great in this case.

**Conclusion**  
`NSNotificationCenter` is handy, but Swift language features allow for a much improved version. Generics allow for a simple API that still allows for all the same use cases while providing static types and type checking on both sides.

That's it for today! Come back next time for more frightening experiments. In the meantime, Friday Q&A is driven by reader ideas, so if you have something you'd like to see covered here, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
