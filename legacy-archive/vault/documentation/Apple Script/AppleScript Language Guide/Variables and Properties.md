---
title: AppleScript Language Guide
apple_id: TP40000983
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-01-25'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/conceptual/ASLR_variables.html
archived_at: '2026-07-15T05:19:31.521788Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Language Guide](Introduction%20to%20AppleScript%20Language%20Guide.md)


[Next](Script%20Objects.md)[Previous](AppleScript%20Fundamentals.md)

# Variables and Properties

Variables and properties are introduced in previous chapters in this document. You use them in `script` objects to store and manipulate values.

The following sections cover common issues in working with variables and properties, including how to declare them and how AppleScript interprets their scope in a script:

- [Defining Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgmwvgvzs)
- [Declaring Variables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgmwvgvzrge)
- [Scope of Variables and Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgmwvgvzr)

Property labels follow the rules described in [Identifiers](AppleScript%20Lexical%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzu).

Property definitions use the following syntax:

`property` _propertyLabel_ `:` _expression_

**_propertyLabel_**
: An identifier.

**_expression_**
: An AppleScript expression that sets the initial value for the property. Property definitions are evaluated before variable assignments, so property definitions cannot contain variables.

The following are examples of valid property definitions:

```
property windowCount : 0
property defaultName : "Barry"
property strangeValue : (pi * 7)^2
```

After you define a property, you can change its value with the `[copy](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgm)` or `[set](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgi)` command.

The value set by a property definition is not reset each time the script is run; instead, it persists until the script is recompiled.

You cannot declare a property in a handler but a handler can access a property defined in its containing `script` object.

Variable names follow the rules described in [Identifiers](AppleScript%20Lexical%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzu).

To create a variable in AppleScript, you assign it a value using the `[copy](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgm)` or `[set](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgi)` command. For example, the following statements create and initialize two variables, one named `circumference` and one named `savedResult`:

```
set circumference to pi * 3.5 --result: 10.995574287564
copy circumference to savedResult --result: 10.995574287564 (copy of 1st variable)
```

As shown in this example, a variable assignment can make use of a previously defined variable. It can also make use of properties declared in the same `script` object.

There are some obvious, and some more subtle, differences in using `copy` and `set` to create a variable—see [Using the copy and set Commands](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgmwvgvzx) for more information.

If you assign a new value to a variable that is already in use, it replaces the old value. You can assign a simple value, an expression, or an object specifier—expressions are evaluated and object specifiers are resolved to obtain the value to assign. To create a variable whose value is an object specifier itself, rather than the value of the object specified, use the `[a reference to](../reference/ASLR_operators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfvjvomi)` operator.

The next two sections describe how you can explicitly define a `local` or a `global` variable. These variable types differ primarily in their scope. Scope, which refers to where a variable is accessible within a script, is described in detail in [Scope of Variables and Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgmwvgvzr).

You can declare explicit `local` variables using the following syntax:

`local` _variableName_ [`,` _variableName_ ]…

**_variableName_**
: An identifier.

The following are examples of valid `local` variable declarations:

```
local windowCount -- defines one variable
local agentName, agentNumber, agentHireDate -- defines three variables
```

You cannot assign an initial value to a `local` variable in its declaration, nor can you declare a class for the variable. Instead, you use the `[copy](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgm)` or `[set](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgi)` command to initialize a variable and set its class. For example:

```
set windowCount to 0 -- initialize to zero; an integer
set agentName to "James Smith" -- assign agent name; a text string
set agentNumber to getAgentNumber(agentName) -- call handler; an integer
copy current date to agentHireDate -- call current date command; a date
```


The syntax for `global` variables is nearly identical to that for `local` variables:

`global` _variableName_ [`,` _variableName_ ]…

**_variableName_**
: An identifier.

The following are examples of valid `global` variable declarations:

```
global gAgentCount
global gStatementDate, gNextAgentNumber
```

As with `local` variables, you use the `[copy](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgm)` or `[set](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgi)` command to initialize `global` variables and set their class types. For example:

```
set gAgentCount to getCurrentAgentCount() -- call handler to get count
set gStatementDate to current date -- get date from current date command
set gNextAgentNumber to getNextAvailNumber() -- call handler to get number
```


As its name implies, when you use the `[copy](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgm)` command to create a variable, it always creates a separate copy (though note that a copy of an object specifier still specifies the same object). However, when you use the `[set](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgi)` command to create a variable, the new variable always refers to the original object or value. You have essentially created another name for the same object.

When more than one variable refers to a changeable (or mutable) object, a change to the object is observable through any of the variables. The types of AppleScript objects that are mutable are `[date](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2hivbusra)`, `[list](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)`, `[record](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2ei5cucsa)`, and `[script](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvjvoni)` objects.

For objects that cannot be modified (immutable objects), variables created with the `set` command may seem like copies—there’s no way to change the object the variables point to, so they seem independent. This is demonstrated in the example in the next section that creates the variables `myName` and `yourName`.

You can use the `set` command to set a variable to any type of object. If the variable doesn’t exist, it is created; if it does exist, its current value is replaced:

```
set numClowns to 5 --result: 5
set myList to { 1, 2, "four" } --result: {1, 2, "four"}
tell application "TextEdit"
    set word1 to word 1 of front document --result: some word
end tell
```

The following example uses a mutable object. It creates two variables that refer to the same list, then modifies the list through one of the variables:

```
set myList to { 1, 2, 3 }
set yourList to myList
set item 1 of myList to 4
```

After executing these statements, the statements `item 1 of myList` and `item 1 of yourList` both yield `4`, because both variables refer to the same list.

Now suppose you’re working with an immutable object, such as a `text` object:

```
set myName to "Sheila"
set yourName to myName
```

Both variables refer to the same `text` object, but `text` objects are not mutable, so there is no way to change the the value `myName` such that it affects the value of `yourName`. (If you assign new text to one of the variables, you are just creating a new, separate `text` object.)

The `set` command can assign several variables at once using a pattern, which may be a list or record: a list or record of variables on one side, and a list or record of values on the other. Values are matched to variables based on their position for a list, or based on their keys for a record. Not having enough values is an error; if there are too many values, the extra ones are ignored. The order in which the values are evaluated and the variables are assigned is unspecified, but all values are evaluated before any assignments are made.

The Examples section of the `[set](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgi)` command shows some simple pattern assignments. Here is an example with more complex patterns:

```
set x to {8, 94133, {firstName:"John", lastName:"Chapman"}}
set {p, q, r} to x
(* now p, q, and r have these values:
                p = 8
                q = 94133
                r = {firstName:"John", lastName:"Chapman"}  *)
set {p, q, {lastName:r}} to x
(* now p, q, and r have these values: p = 8
                                      q = 94133
                                      r = "Chapman" *)
```

In the final assignment statement above, `{lastName:r}` is a record that hasn’t been used before in the script, and contains an item with label `lastName` and value `r` (a previously defined variable). The variable `x` has previously been set to have a record that has an item with label `lastName` and value `"Chapman"`. During the assignment, the value of the item labeled `lastName` in the new record is set to the value of the item labeled `lastName` in `x`—hence it now has the value `"Chapman"`.

As this example demonstrates, the properties of a record need not be given in the same order and need not all be used when you set a pattern to a pattern, as long as the patterns match. For details, see the `[set](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgi)` command.

You can use the `copy` command to set a variable to any type of object. If the variable doesn’t exist, it is created; if it does exist, its current value is replaced. The `copy` command creates a new copy that is independent of the original—a subsequent change does not change the original value (though note that a copy of an object specifier still specifies the same object).

To copy within an application, you should use the application’s `duplicate` command, if it has one. To copy between applications, you can use the `[get](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgy)` command to obtain information from one application and the `[set](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgi)` command to set it in another.

The `copy` command creates a deep copy—that is, if you copy a nested data structure, such as a list that contains another list, the entire structure is copied, as shown in the following example. This example creates a record (`alpha`), then a list (`beta`), then a list that contains the first record and list (`gamma`), then finally a copy of `gamma` (`delta`). It then changes a property in the original record, `alpha`. The result shows that the property is changed wherever `alpha` appears, except in the copy, `delta`:

```
set alpha to {property1:10, property2:20}
set beta to {1, 2, "Hello"}
set gamma to {alpha, beta, "Goodbye"}
copy gamma to delta
set property1 of alpha to 42

{alpha, beta, gamma, delta}  -- List variables to show contents
(*result: {{property1:42, property2:20}, {1, 2, "Hello"}, {{property1:42, property2:20}, {1, 2, "Hello"}, "Goodbye"}, {{property1:10, property2:20}, {1, 2, "Hello"}, "Goodbye"}} *)
```

If you make a copy of a `reference` object, it refers to the same object as the original (because both contain the same object specifier):

```
set windowRef to a reference to window 1 of application "Finder"
name of windowRef --result: "Script testing folder"
copy windowRef to currentWindowRef --result: a new object specifier
name of currentWindowRef --result: "Script testing folder"
```


The _declaration_ of a variable or property identifier is the first valid occurrence of the identifier in a `script` object. The form and location of the declaration determine how AppleScript treats the identifier in that `script` object.

The _scope_ is the range over which AppleScript recognizes a declared identifier within a `script` object. The scope of a variable depends on where you declare it and whether you declare it as `global` or `local`. The scope of a property extends to the entire `script` object in which it is declared. After declaring a property, you can reuse the same identifier as a separate variable only if you first declare it as a `local` variable.

_Lifetime_ refers to the period of time over which a variable or property is in existence. Only the values of properties and `global` variables can persist after a script is run.

In the discussions that follow, declarations and statements in a `script` object that occur outside of any handlers or nested `script` objects are identified as _outside_.

The following examples show the four basic forms for declaring variables and properties in AppleScript:

- `property x: 3`

  The scope of a property definition is the `script` object in which it is declared, including any handlers or nested `script` objects. A property definition specifies an initial value. You cannot declare a property in a handler.

  The value set by a property definition is not reset each time the script is run; instead, it persists until the script is recompiled.
- `global x`

  The scope of a `global` variable can be limited to specific handlers or contained `script` objects or it can extend throughout a top-level `script` object. A `global` declaration doesn’t set an initial value—it must be initialized by a `[copy](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgm)` or `[set](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgi)` command before a script can access its value.

  The value of a `global` variable is not reset each time a script is run, unless its initialization statement is executed.
- `local x`

  The scope of a `local` variable can be limited to specific handlers or contained `script` objects or it can extend throughout a top-level `script` object. A `local` declaration doesn’t set an initial value—it must be initialized by a `copy` or `set` command before a script can access its value.

  The value of a `local` variable is reset each time the handler is run (either the `run` handler for the script, or the specific handler in which the variable is declared).
- `set x to 3`

  In the absence of a `global` variable declaration, the scope of a variable declared with the `copy` or `set` command is normally restricted to the `run` handler for the script, making it implicitly local to that run handler. However, a handler or nested script object can declare the same variable with a `global` declaration to gain access to it.

  The value of a variable declared with the `copy` or `set` command is reset each time a script is run.

If you want to use the same identifier in several different places in a script, you should either declare it as a property or as a `global` variable.

It is often convenient to limit the scope of a particular identifier to a single handler or nested `script` object, which you can do by defining it as a `local` variable in the handler or `script` object. Outside, the identifier has no value associated with it and can be reused elsewhere in the script. When used this way, a `local` variable is said to _shadow_ (or block access to) a `global` variable or property with the same name, making the global version inaccessible in the scope of the handler or `script` object where the `local` variable is declared.

The following sections provide additional information about scope:

- [Scope of Properties and Variables Declared in a Script Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgmwvgvzt)
- [Scope of Variables Declared in a Handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgmwvgvzv)

Table 3-1 shows the scope and lifetime for variables and properties that are declared at the top level in a `script` object (outside any handlers or nested `script` objects).

__Table 3-1__  Scope of property and variable declarations at the top level in a script object

| Declaration type | Scope (visibility) | Lifetime |
| `property x: 3` | Everywhere in script | Reset when script is recompiled |
| `global x` | Everywhere in script | Reset when reinitialized in script or when script is recompiled |
| `local x` | Within `run` handler only | Reset when script is run |
| `set x to 3` | Within `run` handler only | Reset when script is run |

The scope of a property in a `script` object extends to any subsequent statements anywhere in the script. Consider the following example:

```
property currentCount : 0
increment()

on increment()
    set currentCount to currentCount + 1
    display dialog "Count is now " & currentCount  & "."
end increment
```

When it encounters the identifier `currentCount` anywhere in this script, AppleScript associates it with the `currentCount` property.

The value of a property persists after the script in which the property is defined has been run. Thus, the value of `currentCount` is 0 the first time this script is run, 1 the next time it is run, and so on. The property’s current value is saved with the `script` object and is not reset to 0 until the script is recompiled—that is, modified and then run again, saved, or checked for syntax. 

The value of a `global` variable also persists after the script in which it is defined has been run. However, depending on how it is initialized, a `global` variable may be reset each time the script is run again. The next example shows how to initialize a `global` variable so that it is initialized only the first time a script is run, and thus produces the same result as using a property in the previous example:

```
global currentCount
increment()

on increment()
    try
        set currentCount to currentCount + 1
    on error
        set currentCount to 1
    end try
        display dialog "Count is now " & currentCount  & "."
end increment
```

The first time the script is run, the statement `set currentCount to currentCount + 1` generates an error because the `global` variable `currentCount` has not been initialized. When the error occurs, the `on error` block initializes `currentCount`. When the script is run again, the variable has already been initialized, so the error branch is not executed, and the variable keeps its previous value. Persistence is accomplished, but not as simply as in the previous example.

If you don’t want the value associated with an identifier to persist after a script is run but you want to use the same identifier throughout a script, declare a `global` variable and use the `set` command to set its value each time the script is run:

```
global currentCount
set currentCount to 0
on increment()
    set currentCount to currentCount + 1
end increment

increment() --result: 1
increment() --result: 2
```

Each time the `on increment` handler is called within the script, the `global` variable `currentCount` increases by 1. However, when you run the entire script again, `currentCount` is reset to 0.

In the absence of a `global` variable declaration, the scope of a variable declaration using the `set` command is normally restricted to the `run` handler for the script. For example, this script declares two separate `currentCount` variables:

```
set currentCount to 10
on increment()
    set currentCount to 5
end increment

increment() --result: 5
currentCount --result: 10
```

The scope of the first `currentCount` variable’s declaration is limited to the `run` handler for the script. Because this script has no explicit `run` handler, outside statements are part of its implicit `run` handler, as described in [run Handlers](About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywvgvzrgu). The scope of the second `currentCount` declaration, within the `on increment` handler, is limited to that handler. AppleScript keeps track of each variable independently.

To associate a variable in a handler with the same variable declared with the `set` command outside the handler, you can use a `global` declaration in the handler, as shown in the next example. (This approach also works to associate a variable in a nested `script` object.)

```
set currentCount to 0
on increment()
    global currentCount
    set currentCount to currentCount + 1
end increment

increment() --result: 1
currentCount --result: 1
```

To restrict the context of a variable to a script’s `run` handler regardless of subsequent `global` declarations, you must declare it explicitly as a `local` variable, as shown in this example:

```
local currentCount
set currentCount to 10
on increment()
    global currentCount
    set currentCount to currentCount + 2
end increment

increment() --error: "The variable currentCount is not defined"
```

Because the `currentCount` variable in this example is declared as local to the script, and hence to its implicit `run` handler, any subsequent attempt to declare the same variable as `global` results in an error.

If you declare an outside variable with the `set` command and then declare the same identifier as a property, the declaration with the `set` command overrides the property definition. For example, the following script returns 10, not 5. This occurs because AppleScript evaluates property definitions before it evaluates `set` command declarations:

```
set numClowns to 10 -- evaluated after property definition
property numClowns: 5 -- evaluated first
numClowns --result: 10
```

The next example, shows how to use a `global` variable declaration in a `script` object to associate a `global` variable with an outside property:

```
property currentCount : 0
script Paula
    property currentCount : 20
    script Joe
        global currentCount
        on increment()
            set currentCount to currentCount + 1
            return currentCount
        end increment
    end script
    tell Joe to increment()
end script
run Paula --result: 1
run Paula --result: 2
currentCount --result: 2
currentCount of Paula --result: 20
```

This script declares two separate `currentCount` properties: one outside any handlers (and `script` objects) in the main script and one in the `script` object `Paula` but outside of any handlers or `script` objects within `Paula`. Because the script `Joe` declares the `global` variable `currentCount`, AppleScript looks for `currentCount` at the top level of the script, thus treating Joe’s `currentCount` and `currentCount` at the top level of the script as the same variable.

A handler can’t declare a property, although it can refer to a property that is declared outside any handler in the `script` object. (A handler can contain script objects, but it can’t contain another handler, except in a contained script object.)

[Table 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgmwvgvzw) summarizes the scope of variables declared in a handler. Examples of each form of declaration follow.

__Table 3-2__  Scope of variable declarations within a handler

| Declaration type | Scope (visibility) | Lifetime |
| `global x` | Within handler only | Reset when script is recompiled; if initialized in handler, then reset when handler is run |
| `local x` | Within handler only | Reset when handler is run |
| `set x to 3` | Within handler only | Reset when handler is run |

The scope of a `global` variable declared in a handler is limited to that handler, although AppleScript looks beyond the handler when it tries to locate an earlier occurrence of the same variable. Here’s an example:

```
set currentCount to 10
on increment()
    global currentCount
    set currentCount to currentCount + 2
end increment

increment() --result: 12
currentCount --result: 12
```

When AppleScript encounters the `currentCount` variable within the `on increment` handler, it doesn’t restrict its search for a previous occurrence to that handler but keeps looking until it finds the declaration outside any handler. However, the use of `currentCount` in any subsequent handler in the script is local to that handler unless the handler also explicitly declares `currentCount` as a `global` variable.

The scope of a `local` variable declaration in a handler is limited to that handler, even if the same identifier has been declared as a property outside the handler:

```
property currentCount : 10
on increment()
    local currentCount
    set currentCount to 5
end increment

increment() --result: 5
currentCount --result: 10
```

The scope of a variable declaration using the `set` command in a handler is limited to that handler:

```
script Henry
    set currentCount to 10 -- implicit local variable in script object
    on increment()
        set currentCount to 5-- implicit local variable in handler
    end increment
    return currentCount
end script

tell Henry to increment() --result: 5
run Henry --result: 10
```

The scope of the first declaration of the first `currentCount` variable in the `script` object `Henry` is limited to the `run` handler for the `script` object (in this case, an implicit `run` handler, consisting of the last two statements in the script). The scope of the second `currentCount` declaration, within the `on increment` handler, is limited to that handler. The two instances of `currentCount` are independent variables.

[Next](Script%20Objects.md)[Previous](AppleScript%20Fundamentals.md)

