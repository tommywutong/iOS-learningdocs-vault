---
title: JavaScriptCore
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/javascriptcore/'
original_language: en
published: 2019-02-25
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:6f5b9d3abc5f4ebd'
translated: false
---

> 原文：[JavaScriptCore](https://nshipster.com/javascriptcore/)　·　NSHipster (Mattt)

# [Java​Script​Core](https://nshipster.com/javascriptcore/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  February 25^th, 2019 ([revised](https://github.com/nshipster/articles/commits/master/2019-02-25-javascriptcore.md))

Whether you love it or hate it, JavaScript has become the most important language for developers today. Yet despite any efforts we may take to change or replace it we’d be hard-pressed to deny its usefulness.

This week on NSHipster, we’ll discuss the JavaScriptCore framework, and how you can use it to set aside your core beliefs in type safety and type sanity and let JavaScript do some of the heavy lifting in your apps.

---

The JavaScriptCore framework provides direct access to WebKit’s JavaScript engine in your apps.

You can execute JavaScript code within a context by calling the `evaluateScript(_:)` method on a `JSContext` object. `evaluateScript(_:)` returns a `JSValue` object containing the value of the last expression that was evaluated. For example, a JavaScript expression that adds the numbers 1, 2, and 3 results in the number value 6.

```
import JavaScriptCore

let context = JSContext()!
let result = context.evaluateScript("1 + 2 + 3")
result?.toInt32() // 6
```

You can cast `JSValue` to a native Swift or Objective-C type by calling the corresponding method found in the following table:

| JavaScript Type | `JSValue` method | Objective-C Type | Swift Type |
|---|---|---|---|
| string | `toString` | `NSString` | `String!` |
| boolean | `toBool` | `BOOL` | `Bool` |
| number | `toNumber` `toDouble` `toInt32` `toUInt32` | `NSNumber` `double` `int32_t` `uint32_t` | `NSNumber!` `Double` `Int32` `UInt32` |
| Date | `toDate` | `NSDate` | `Date?` |
| Array | `toArray` | `NSArray` | `[Any]!` |
| Object | `toDictionary` | `NSDictionary` | `[AnyHashable: Any]!` |
| Class | `toObject` `toObjectOfClass:` | _custom type_ | _custom type_ |

JavaScript evaluation isn’t limited to single statements. When you evaluate code that declares a function or variable, it’s saved into the context’s object space.

```
context.evaluateScript(#"""
function triple(number) {
    return number * 3;
}
"""#)

context.evaluateScript("triple(5)")?
       .toInt32() // 15
```

### Handling Exceptions

The `evaluateScript(_:)` method doesn’t expose an `NSError **` pointer and isn’t imported by Swift as a method that `throws`; by default, invalid scripts fail silently when evaluated within a context. This is — you might say — less than ideal.

To get notified when things break, set the `exceptionHandler` property on `JSContext` objects before evaluation.

```
import JavaScriptCore

let context = JSContext()!
context.exceptionHandler = { context, exception in
    print(exception!.toString())
}

context.evaluateScript("**INVALID**")
// Prints "SyntaxError: Unexpected token '**'"
```

### Managing Multiple Virtual Machines and Contexts

Each `JSContext` executes on a `JSVirtualMachine` that defines a shared object space. You can execute multiple operations concurrently across multiple virtual machines.

The default `JSContext` initializer creates its virtual machine implicitly. You can initialize multiple `JSContext` objects to have a shared virtual machine.

A virtual machine performs deferred tasks, such as garbage collection and WebAssembly compilation, on the runloop on which it was initialized.

```
let queue = DispatchQueue(label: "js")
let vm = queue.sync { JSVirtualMachine()! }
let context = JSContext(virtualMachine: vm)!
```

## Getting JavaScript Context Values from Swift

You can access named values from a `JSContext` by calling the `objectForKeyedSubscript(_:)` method. For example, if you evaluate a script that declares the variable `threeTimesFive` and sets it to the result of calling the `triple()` function (declared previously), you can access the resulting value by variable name.

```
context.evaluateScript("var threeTimesFive = triple(5)")

context.objectForKeyedSubscript("threeTimesFive")?
       .toInt32() // 15
```

## Setting Swift Values on a JavaScript Context

Conversely, you can set Swift values as variables in a `JSContext` by calling the `setObject(_:forKeyedSubscript:)` method.

```
let threeTimesTwo = 2 * 3
context.setObject(threeTimesTwo,
                  forKeyedSubscript: "threeTimesTwo" as NSString)
```

In this example, we initialize a Swift constant `threeTimesTwo` to the product of 2 and 3, and set that value to a variable in `context` with the same name.

We can verify that the `threeTimesTwo` variable is stored with the expected value by performing an equality check in JavaScript.

```
context.evaluateScript("threeTimesTwo === triple(2);")?
       .toBool() // true
```

## Passing Functions between Swift and JavaScript

Functions are different from other values in JavaScript. And though you can’t convert a function contained in a `JSValue` directly to a native function type, you can execute it within the JavaScript context using the `call(withArguments:)` method.

```
let triple = context.objectForKeyedSubscript("triple")
triple?.call(withArguments: [9])?
       .toInt32() // 27
```

In this example, we access the `triple` function from before by name and call it — passing 9 an argument — to produce the value 27.

A similar limitation exists when you attempt to go the opposite direction, from Swift to JavaScript: JavaScriptCore is limited to passing Objective-C blocks to JavaScript contexts. In Swift, you can use the `@convention(block)` to create a compatible closure.

```
let quadruple: @convention(block) (Int) -> Int = { input in
    return input * 4
}

context.setObject(quadruple,
                  forKeyedSubscript: "quadruple" as NSString)
```

In this example, we define a block that multiplies an `Int` by 4 and returns the resulting `Int`, and assign it to a function in the JavaScript context with the name `quadruple`.

We can verify this assignment by either calling the function directly in evaluated JavaScript or by using `objectForKeyedSubscript(_:)` to get the function in a `JSValue` and call it with the `call(withArguments:)` method.

```
context.evaluateScript("quadruple(3)")?
       .toInt32() // 12

context.objectForKeyedSubscript("quadruple")?
       .call(withArguments: [3]) // 12
```

## Passing Swift Objects between Swift and JavaScript

All of the conversion between Swift and Javascript we’ve seen so far has involved manual conversion with intermediary `JSValue` objects. To improve interoperability between language contexts, JavaScriptCore provides the `JSExport` protocol, which allows native classes to be mapped and initialized directly.

…though to call the process “streamlined” would be generous. As we’ll see, it takes quite a bit of setup to get this working in Swift, and may not be worth the extra effort in most cases.

But for the sake of completeness, let’s take a look at what all this entails:

### Declaring the Exported JavaScript Interface

The first step is to declare a protocol that inherits `JSExport`. This protocol defines the interface exported to JavaScript: the methods that can be called; the properties that can be set and gotten.

For example, here’s the interface that might be exported for a `Person` class consisting of stored properties for `firstName`, `lastName`, and `birthYear`:

```
import Foundation
import JavaScriptCore

// Protocol must be declared with `@objc`
@objc protocol PersonJSExports: JSExport {
    var firstName: String { get set }
    var lastName: String { get set }
    var birthYear: NSNumber? { get set }

    var fullName: String { get }

    // Imported as `Person.createWithFirstNameLastName(_:_:)`
    static func createWith(firstName: String, lastName: String) -> Person
}
```

JavaScriptCore uses the Objective-C runtime to automatically convert values between the two languages, hence the `@objc` attribute here and in the corresponding class declaration.

### Conforming to the Exported JavaScript Interface

Next, create a `Person` class that adopts the `PersonJSExports` protocol and makes itself Objective-C compatible with `NSObject` inheritance and an `@objc` attribute for good measure.

```
// Class must inherit from `NSObject`
@objc public class Person : NSObject, PersonJSExports {
    // Properties must be declared with `dynamic`
    dynamic var firstName: String
    dynamic var lastName: String
    dynamic var birthYear: NSNumber?

    required init(firstName: String, lastName: String) {
        self.firstName = firstName
        self.lastName = lastName
    }

    var fullName: String {
        return "\(firstName) \(lastName)"
    }

    class func createWith(firstName: String, lastName: String) -> Person {
        return Person(firstName: firstName, lastName: lastName)
    }
}
```

Each stored property must be declared dynamic to interoperate with the Objective-C runtime. The `init(firstName:lastName:)` initializer won’t be accessible from JavaScript, because it isn’t part of the exported interface declared by `PersonJSExports`; instead, a `Person` object can be constructed through a type method imported as `Person.createWithFirstNameLastName(_:_:)`.

### Registering the Class in the JavaScript Context

Finally, register the class within the `JSContext` by passing the type to `setObject(_:forKeyedSubscript:)`.

```
context.setObject(Person.self,
                  forKeyedSubscript: "Person" as NSString)
```

### Instantiating Swift Classes from JavaScript

With all of the setup out of the way, we can now experience the singular beauty of seamless(_-ish_) interoperability between Swift and JavaScript!

We’ll start by declaring a `loadPeople()` function in JavaScript, which parses a JSON string and constructs imported `Person` objects using the JSON attributes.

```
context.evaluateScript(#"""
function loadPeople(json) {
    return JSON.parse(json)
               .map((attributes) => {
        let person = Person.createWithFirstNameLastName(
            attributes.first,
            attributes.last
        );
        person.birthYear = attributes.year;

        return person;
    });
}
"""#)
```

We can even flex our muscles by defining the JSON string in Swift and then passing it as an argument to the `loadPeople` function (accessed by name using the `objectForKeyedSubscript(_:)` method).

```
let json = """
[
    { "first": "Grace", "last": "Hopper", "year": 1906 },
    { "first": "Ada", "last": "Lovelace", "year": 1815 },
    { "first": "Margaret", "last": "Hamilton", "year": 1936 }
]
"""

let loadPeople = context.objectForKeyedSubscript("loadPeople")!
let people = loadPeople.call(withArguments: [json])!.toArray()
```

Going back and forth between languages like this is neat and all, but doesn’t quite justify all of the effort it took to get to this point.

So let’s finish up with some NSHipster-brand _pizazz_, and see decorate these aforementioned pioneers of computer science with a touch of mustache.

### Showing Off with Mustache

[Mustache](https://mustache.github.io) is a simple, logic-less templating language, with implementations in many languages, including [JavaScript](https://github.com/janl/mustache.js). We can load up `mustache.js` into our JavaScript context using the `evaluateScript(_:withSourceURL:)` to make it accessible for subsequent JS invocations.

```
guard let url = Bundle.main.url(forResource: "mustache", withExtension: "js") else {
    fatalError("missing resource mustache.js")
}

context.evaluateScript(try String(contentsOf: url),
                       withSourceURL: url)
```

From here, we can define a mustache template (in all of its curly-braced glory) using a Swift multi-line string literal. This template — along with the array of `people` from before in a keyed dictionary — are passed as arguments to the `render` method found in the `Mustache` object declared in `context` after evaluating `mustache.js`.

```
let template = """
{{#people}}
{{fullName}}, born {{birthYear}}
{{/people}}
"""

let result = context.objectForKeyedSubscript("Mustache")
                    .objectForKeyedSubscript("render")
                    .call(withArguments: [template, ["people": people]])!

print(result)
// Prints:
// "Grace Hopper, born 1906"
// "Ada Lovelace, born 1815"
// "Margaret Hamilton, born 1936"
```

---

The JavaScriptCore framework provides a convenient way to leverage the entire JavaScript ecosystem.

Whether you use it to bootstrap new functionality, foster feature parity across different platforms, or extend functionality to users by way of a scripting interface, there’s no reason not to consider what role JavaScript can play in your apps.
