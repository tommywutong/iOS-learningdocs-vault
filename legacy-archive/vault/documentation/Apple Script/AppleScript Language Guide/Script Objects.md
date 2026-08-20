---
title: AppleScript Language Guide
apple_id: TP40000983
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-01-25'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/conceptual/ASLR_script_objects.html
archived_at: '2026-07-15T05:19:31.501190Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Language Guide](Introduction%20to%20AppleScript%20Language%20Guide.md)


[Next](About%20Handlers.md)[Previous](Variables%20and%20Properties.md)

# Script Objects

This chapter describes the `script` object, which is used to implement all AppleScript scripts. Before reading this chapter, you should be familiar with the information in [AppleScript and Objects](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzr).

A _script object_ is a user-defined object that can combine data (in the form of properties) and actions (in the form of handlers and additional `script` objects). Script objects support inheritance, allowing you to define a hierarchy of objects that share properties and handlers. You can also extend or modify the behavior of a handler in one `script` object when calling it from another `script` object.

The top-level `[script](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvjvoni)` object is the one that implements the overall script you are working on. Any `script` object can contain nested `script` objects, each of which is defined just like a top-level `script` object, except that a nested `script` object is bracketed with statements that mark its beginning and end.

This chapter describes `script` objects in the following sections:

- [Defining Script Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzs) shows the syntax for defining `script` objects and includes a simple example .
- [Initializing Script Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzu) describes how AppleScript creates a `script` object with the properties and handlers you have defined.
- [Sending Commands to Script Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzt) describes how you use `tell` statements to send commands to `script` objects.
- [Script Libraries](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzw) describes script libraries and how to use them from other scripts.
- [Inheritance in Script Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzv) describes inheritance works and how you can use it to share functionality in the `script` objects you define.

Each `script` object definition (except for the top-level `script` object) begins with the keyword `script`, followed by a variable name, and ends with the keyword `end` (or `end script`). The statements in between can be any combination of property definitions, handler definitions, nested `script` object definitions, and other AppleScript statements.

The syntax of a `script` object definition is as follows:

`script` _variableName_

    [ ( `property` | `prop` ) `parent :` _parentSpecifier_ ]

    [ ( `property` | `prop` ) _propertyLabel_ : _initialValue_ ]...

    [ _handlerDefinition_ ]...

    [ _statement_ ]...

`end` [ `script` ]

**_variableName_**
: A variable identifier for the script. You can refer to a script object by this name elsewhere in a script.

**_parentSpecifier_**
: Specifies the parent of the `script` object, typically another `script` object.

For more information, see [Inheritance in Script Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzv).

**_propertyLabel_**
: An identifier, unique within the `script` object, that specifies a characteristic of the object; equivalent to an instance variable.

**_initialValue_**
: The value that is assigned to the property each time the `script` object is initialized. `script` objects are initialized when compiled. _initialValue_ is required in property definitions.

**_handlerDefinition_**
: A handler for a command the `script` object can respond to; equivalent to a method. For more information, see [About Handlers](About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywugsscjfceessi) and [Handler Reference](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfuytmmzxgyza).

**_statement_**
: Any AppleScript statement. Statements other than handler and property definitions are treated as if they were part of an implicit handler definition for the `run` command; they are executed when a `script` object receives the `run` command.

Here is a simple `script` object definition:

```
script John
    property HowManyTimes : 0

    to sayHello to someone
        set HowManyTimes to HowManyTimes + 1
        return "Hello " & someone
    end sayHello

end script
```

It defines a `script` object that can handle the `sayHello` command. It assigns the `script` object to the variable `John`. The definition includes a handler for the `sayHello` command. It also includes a property, called `HowManyTimes`, that indicates how many times the `sayHello` command has been called.

A handler within a `script` object definition follows the same syntax rules as any other handler.

You can use a `tell` statement to send commands to a `script` object. For example, the following statement sends the `sayHello` command the `script` object defined above.

```
tell John to sayHello to "Herb" --result: "Hello Herb"
```

You can manipulate the properties of `script` objects by using the `get` command to get the value of a property and the `set` or `copy` command to change the value. The value of a property is persistent—it gets reset every time you compile the script, but not when you run it.

When you define a `script` object, it can contain properties, handlers, and nested `script` object definitions. When you execute the script containing it, AppleScript creates a `script` object with the defined properties, handlers, and nested `script` objects. The process of creating an instance of a `script` object from its definition is called initialization. A `script` object must be initialized before it can respond to commands.

A top-level `script` object is initialized each time the script’s `run` handler is executed. Similarly, if you define a script within a handler, AppleScript initializes a `script` object each time the handler is called. The parameter variables in the handler definition become local variables of the `script` object.

For example, the `makePoint` handler in the following script contains a `script` object definition for the `script` object `thePoint`:

```
on makePoint(x, y)
    script thePoint
        property xCoordinate:x
        property yCoordinate:y
    end script
    return thePoint
end makePoint

set myPoint to makePoint(10,20)
get xCoordinate of myPoint  --result: 10
get yCoordinate of myPoint  --result: 20
```

AppleScript initializes the `script` object `thePoint` when it executes the `makePoint` command. After the call to `makePoint`, the variable `myPoint` refers to this `script` object. The parameter variables in the `makePoint` handler, in this case, `x` and `y`, become local variables of the `script` object. The initial value of `x` is 10, and the initial value of `y` is 20, because those are the parameters passed to the `makePoint` handler that initialized the `script` object.

If you added the following line to the end of the previous script and ran it, the variable `myOtherPoint` would refer to a second instance of the `script` object `thePoint`, with different property values:

```
set myOtherPoint to makePoint(30,50)
```

The `makePoint` script is a kind of constructor function that creates `script` objects representing points. 

You can use `tell` statements to send commands to `script` objects. For example, the following `tell` statement sends two `sayHello` commands to the `script` object `John` (defined below):

```
tell John
    sayHello to "Herb"
    sayHello to "Grace"
end tell
```

For a `script` object to respond to a command within a `tell` statement, either the `script` object or its parent object must have a handler for the command. For more information about parent objects, see [Inheritance in Script Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzv).

A `script` object definition may include an implicit `run` handler, consisting of all executable statements that are outside of any handler or nested `script` object, or it may include an explicit `run` handler that begins with `on run`, but it may not contain both—such a script will not compile. If a script has no run handler (for example, a script that serves as a library of handlers, as described in [Parameter Specifications](About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywvgvzrgi)), executing the script does nothing. However, sending it an explicit `run` command causes an error. For more information, see [run Handlers](About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywvgvzrgu).

The `display dialog` command in the following `script` object definition is the only executable statement at the top level, so it constitutes the `script` object’s implicit `run` handler and is executed when the script sends a `run` command to `script` object `John`, with the statement `tell John to run`. 

```
script John
    property HowManyTimes : 0
    to sayHello to someone
        set HowManyTimes to HowManyTimes + 1
        return "Hello " & someone
    end sayHello
    display dialog "John received the run command"
end script

tell John to run
```

You can also use the possessive to send a command to a `script` object. For example, either of the following two forms send the `sayHello` command to script `John` (the first version compiles into the second):

```
John's sayHello to "Jake" --result: "Hello Jake"
sayHello of John to "Jake" --result: "Hello Jake"
```


A top-level `script` object saved in a Script Libraries folder becomes a _script library_ usable by other scripts. Libraries let you share and reuse handlers, reorganize large scripts into a set of smaller libraries that are easier to manage, and build richer, higher-level functionality out of simpler libraries.

The basic requirement for a script to be a script library is its location: it must be a script document in a “Script Libraries” folder in one of the following folders. When searching for a library, the locations are searched in the order listed, and the first matching script is used:

1. If the script that references the library is a bundle, the script’s bundle `Resources` directory. This means that scripts may be packaged and distributed with the libraries they use.
2. If the application running the script is a bundle, the application’s bundle `Resources` directory. This means that script applications (“applets” and “droplets”) may be packaged and distributed with the libraries they use. It also enables applications that run scripts to provide libraries for use by those scripts.
3. Any folders specified in the environment variable `OSA_LIBRARY_PATH`. This allows using a library without installing it in one of the usual locations. The value of this variable is a colon-separated list of paths, such as `/opt/local/Script Libraries:/usr/local/Script Libraries`. Unlike the other library locations, paths specified in `OSA_LIBRARY_PATH` are used exactly as-is, without appending “Script Libraries”. _Supported in OS X v10.11 and later._
4. The Library folder in the user’s home directory, `~/Library`. This is the location to install libraries for use by a single user, and is the recommended location during library development.
5. The computer Library folder, `/Library`. Libraries located here are available to all users of the computer.
6. The network Library folder, `/Network/Library`. Libraries located here are available to multiple computers on a network.
7. The system Library folder, `/System/Library`. These are libraries provided by macOS.
8. Any installed application bundle, in the application’s bundle `Library` directory. This allows distributing libraries that are associated with an application, or creating applications that exist solely to distribute libraries. _Supported in OS X v10.11 and later._

Script libraries also have `name`, `id`, and `version` properties. It is recommended that you define all three, especially for libraries you plan to distribute publicly: doing so allows clients to unambiguously identify particular versions of libraries that have the functionality they need. These properties may be defined either as `property` definitions within the script itself, or, for script bundles, in the Info.plist file, which can be edited using the Bundle Contents drawer in Script Editor. For details, see the `[script](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvjvoni)` class reference.

A script library may be a single-file (scpt) or bundle format (scptd). If a library is a bundle, it may define its own terminology.

Libraries may define scripting terminology, including commands, properties and enumerated values, by supplying a Scripting Definition (sdef) file in their bundle. Like applications, this terminology is available to client scripts when they target the library with `tell` or `use`, and to the library script itself.

To define terminology, create an sdef file as described in the _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_ under [Preparing a Scripting Definition File](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_creating_sdef/SAppsCreateSdef.html#//apple_ref/doc/uid/TP40001979). Then, copy the file to the bundle’s Resources directory and set the Info.plist key `OSAScriptingDefinition` to the base name of the sdef file (that is, the file name without the “.sdef” extension). Script Editor’s Bundle Contents drawer can do this for you: drag the file into the “Resources” list to copy the file into the bundle, and enter the base name of the sdef file in the “Scripting Definition” field.

A script library defines a script object, which a client script may then reference and then send commands to, as described in [Sending Commands to Script Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzt). Libraries are identified by name:

```
script "My Library"
```

AppleScript will search the various Script Library folders, as described above in [Creating a Library](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzrgm), and create an instance of the library script. Unlike the result from `load script`, this instance is shared and persists for at least the lifetime of the client script, so you do not have to save it in a variable, and state will be preserved while the client script is running. For example, given this library script:

```
property name : "Counter"
property nextNumberProperty : 0
on nextNumber()
    set my nextNumberProperty to my nextNumberProperty + 1
    return my nextNumberProperty
end nextNumber
```

This client script, despite referencing the library in full both times, will log “1” and then “2”:

```
tell script "Counter" to log its nextNumber() -- logs "1"
tell script "Counter" to log its nextNumber() -- logs "2"
```


You can use the AppleScript inheritance mechanism to define related `script` objects in terms of one another. This allows you to share property and handler definitions among many `script` objects without repeating the shared definitions. Inheritance is described in the following sections:

- [The AppleScript Inheritance Chain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzrgu)
- [Defining Inheritance Through the parent Property](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzx)
- [Some Examples of Inheritance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzy)
- [Using the continue Statement in Script Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzz)

The top-level `script` object is the parent of all other `script` objects, although any `script` object can specify a different parent object. The top-level `script` object also has a parent—AppleScript itself (the AppleScript component). And even AppleScript has a parent—the current application. The name of that application (which is typically Script Editor) can be obtained through the global constant `current application`. This hierarchy defines the _inheritance chain_ that AppleScript searches to find the target for a command or the definition of a term.

Every `script` object has access to the properties, handlers, and script objects it defines, as well as to those defined by its parent, and those of any other object in the inheritance chain, including AppleScript. That’s why the constants and properties described in [Global Constants in AppleScript](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawueqkkijcekssj) are available to any script.

When working with `[script](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvjvoni)` objects, _inheritance_ is the ability of a child `script` object to take on the properties and handlers of a parent object. You specify inheritance with the `parent` property.

The object listed in a `parent` property definition is called the  _parent object_, or parent. A `script` object that includes a `parent` property is referred to as a _child script object_  , or child. The `parent` property is not required, though if one is not specified, every script is a child of the top-level script, as described in [The AppleScript Inheritance Chain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzrgu). A `script` object can have many children, but a child `script` object can have only one parent. The parent object may be any object, such as a `[list](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` or an `[application](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvjvomq)` object, but it is typically another `script` object.

The syntax for defining a parent object is

( `property` | `prop` ) `parent :` _variable_

**_variable_**
: An identifier for a variable that refers to the parent object.

A `script` object must be initialized before it can be assigned as a parent of another `script` object. This means that the definition of a parent `script` object (or a command that calls a function that creates a parent `script` object) must come before the definition of the child in the same script.

The inheritance relationship between `script` objects should be familiar to those who are acquainted with C++ or other object-oriented programming languages. A child `script` object that inherits the handlers and properties defined in its parent is like a C++ class that inherits methods and instance variables from its parent class. If the child does not have its own definition of a property or handler, it uses the inherited property or handler. If the child has its own definition of a particular property or handler, then it ignores (or overrides) the inherited property or handler.

[Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzrga) shows the definitions of a parent `script` object called `Alex` and a child `script` object called `AlexJunior`.

__Listing 4-1__  A pair of script objects with a simple parent-child relationship

```
script Alex
    on sayHello()
        return "Hello, " & getName()
    end sayHello
    on getName()
        return "Alex"
    end getName
end script

script AlexJunior
    property parent : Alex
    on getName()
        return "Alex Jr"
    end getName
end script

-- Sample calls to handlers in the script objects:
tell Alex to sayHello() --result: "Hello, Alex"
tell AlexJunior to sayHello() --result: "Hello, Alex Jr."

tell Alex to getName() --result: "Alex"
tell AlexJunior to getName() --result: "Alex Jr"
```

Each `script` object defines a `getName()` handler to return its name. The `script` object `Alex` also defines the `sayHello()` handler. Because `AlexJunior` declares Alex to be its parent object, it inherits the `sayHello()` handler.

Using a `tell` statement to invoke the `sayHello()` handler of `script` object `Alex` returns `"Hello, Alex"`. Invoking the same handler of `script` object `AlexJunior` returns `"Hello, Alex Jr"`—although the same `sayHello()` handler in `Alex` is executed, when that handler calls `getName()`, it’s the `getName()` in `AlexJunior` that is executed.

The relationship between a parent `script` object and its child `script` objects is dynamic. If the properties of the parent change, so do the inherited properties of the children. For example, the `script` object `JohnSon` in the following script inherits its `vegetable` property from `script` object `John`.

```
script John
    property vegetable : "Spinach"
end script
script JohnSon
    property parent : John
end script
set vegetable of John to "Swiss chard"
vegetable of JohnSon
--result: "Swiss chard"
```

When you change the `vegetable` property of `script` object `John` with the `set` command, you also change the `vegetable` property of the child `script` object `Simple`. The result of the last line of the script is `"Swiss chard"`.

Similarly, if a child changes one of its inherited properties, the value in the parent object also changes. For example, the `script` object `JohnSon` in the following script inherits the `vegetable` property from `script` object `John`.

```
script John
    property vegetable : "Spinach"
end script
script JohnSon
    property parent : John
    on changeVegetable()
        set my vegetable to "Zucchini"
    end changeVegetable
end script
tell JohnSon to changeVegetable()
vegetable of John
--result: "Zucchini"
```

When you change the `vegetable` property of `script` object `JohnSon` to `"Zucchini"` with the `changeVegetable` command, the `vegetable` property of `script` object `John` also changes.

The previous example demonstrates an important point about inherited properties: to refer to an inherited property from within a child `script` object, you must use the reserved word `my` or `of me` to indicate that the value to which you’re referring is a property of the current `script` object. (You can also use the words `of parent` to indicate that the value is a property of the parent `script` object.) If you don’t, AppleScript assumes the value is a local variable.

For example, if you refer to `vegetable` instead of `my vegetable` in the `changeVegetable` handler in the previous example, the result is `"Spinach"`. For related information, see [The it and me Keywords](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzu).

In a child `script` object, you can define a handler with the same name as a handler defined in its parent object. In implementing the child handler, you have several options:

- The handler in the child `script` object can be independent of the one in its parent. This allows you to call either handler, as you wish.
- The handler in the child can simply invoke the handler in its parent. This allows the child object to take advantage of the parent’s implementation (as shown in the `script` objects below that contain a `on identify` handler).
- The handler in the child can invoke the handler in its parent, changing the values passed to it or executing additional statements before or after invoking the parent handler. This allows the child object to modify or add to the behavior of its parent, but still take advantage of the parent’s implementation.

Normally, if a child `script` object and its parent both have handlers for the same command, the child uses its own handler. However, the handler in a child `script` object can handle a command first, and then use a `continue` statement to call the handler for the same command in the parent.

This handing off of control to another object is called _delegation_. By delegating commands to a parent `script` object, a child can extend the behavior of a handler contained in the parent without having to repeat the entire handler definition. After the parent handles the command, AppleScript continues at the place in the child where the `continue` statement was executed.

The syntax for a `continue` statement is shown in `[continue](../reference/ASLR_handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomi)`.

The following script includes two `script` object definitions, `Elizabeth` and `ChildOfElizabeth`.

```
script Elizabeth
    property HowManyTimes : 0
    to sayHello to someone
        set HowManyTimes to HowManyTimes + 1
        return "Hello " & someone
    end sayHello
end script

script ChildOfElizabeth
    property parent : Elizabeth
    on sayHello to someone
        if my HowManyTimes > 3 then
            return "No, I'm tired of saying hello."
        else
            continue sayHello to someone
        end if
    end sayHello
end script
tell Elizabeth to sayHello to "Matt"
--result: "Hello Matt", no matter how often the tell is executed
tell ChildOfElizabeth to sayHello to "Bob"
--result: "Hello Bob", the first four times the tell is executed;
--   after the fourth time: "No, I’m tired of saying hello."
```

In this example, the handler defined by `ChildOfElizabeth` for the `sayHello` command checks the value of the `HowManyTimes` property each time the handler is run. If the value is greater than 3, `ChildOfElizabeth` returns a message refusing to say hello. Otherwise, `ChildOfElizabeth` calls the `sayHello` handler in the parent `script` object (`Elizabeth`), which returns the standard hello message. The word `someone` in the `continue` statement is a parameter variable. It indicates that the parameter received with the original `sayHello` command will be passed to the handler in the parent script.

A `continue` statement can change the parameters of a command before delegating it. For example, suppose the following `script` object is defined in the same script as the preceding example. The first `continue` statement changes the direct parameter of the `sayHello` command from `"Bill"` to `"William"`. It does this by specifying the value `"William"` instead of the parameter variable `someone`.

```
script AnotherChildOfElizabeth
    property parent : Elizabeth
    on sayHello to someone
        if someone = "Bill" then
            continue sayHello to "William"
        else
            continue sayHello to someone
        end if
    end sayHello
end script

tell AnotherChildOfElizabeth to sayHello to "Matt"
--result: "Hello Matt"

tell AnotherChildOfElizabeth to sayHello to "Bill"
--result: "Hello William"
```

If you override a parent’s handler in this manner, the reserved words `me` and `my` in the parent’s handler no longer refer to the parent, as demonstrated in the example that follows.

```
script Hugh
    on identify()
        me
    end identify
end script
script Andrea
    property parent : Hugh
    on identify()
        continue identify()
    end identify
end script

tell Hugh to identify()
--result: «script Hugh»

tell Andrea to identify()
--result: «script Andrea»
```


[Next](About%20Handlers.md)[Previous](Variables%20and%20Properties.md)

