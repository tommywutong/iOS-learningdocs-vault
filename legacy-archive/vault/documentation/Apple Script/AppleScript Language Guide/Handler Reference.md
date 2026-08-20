---
title: AppleScript Language Guide
apple_id: TP40000983
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-01-25'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_handlers.html
archived_at: '2026-07-15T05:19:32.621531Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Language Guide](Introduction%20to%20AppleScript%20Language%20Guide.md)


[Next](Folder%20Actions%20Reference.md)[Previous](Control%20Statements%20Reference.md)

# Handler Reference

This chapter provides reference for handlers, which are defined and introduced in [About Handlers](About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywugsscjfceessi). It describes the types of parameters you can use with handlers and how you invoke them. It also describes the `continue` and `return` statements, which you use to control the flow of execution in handlers.

continue

A `continue` statement causes AppleScript to invoke the handler with the same name in the parent of the current handler. If there is no such handler in the parent, AppleScript looks up the parent chain, ending with the current application.

A `continue` statement is like a handler call, in that after execution completes in the new location, it resumes with the statement after the `continue` statement.

##### Syntax

```
continue handlerName [ parameterList ]
```

##### Placeholders

**_handlerName_**
: A required identifier that specifies the name of the current handler (which is also the name of the handler in which to continue execution).

**_parameterList_**
: The list of parameters to be passed to _handlerName_.

The list must follow the same format as the parameter definitions in the handler definition for the command. For handlers with labeled parameters, this means that the parameter labels must match those in the handler definition. For handlers with positional parameters, the parameters must appear in the correct order.

You can list the parameter variables that were specified in the original command (and thus the original values) or you can list values that may differ from those of the original variables.

##### Examples

You can write a handler that overrides an AppleScript command but uses a `continue` statement to pass control on to the AppleScript command if desired:

```
on beep numTimes
    set x to display dialog "Start beeping?" buttons {"Yes", "No"}
    if button returned of x is "Yes" then ¬
        continue beep numTimes -- Let AppleScript handle the beep.
        -- In this example, nothing to do after returning from the continue.
end beep

beep 3 --result: local beep handler invoked; shows dialog before beeping
tell my parent to beep 3 -- result: AppleScript beep command invoked
```

When AppleScript encounters the statement `beep 3`, it invokes the local `beep` handler, which displays a dialog. If the user clicks Yes, the handler uses a `continue` statement to pass the `beep` command to the script’s parent (AppleScript), which handles the command by beeping. If the user clicks No, it does not continue the `beep` command, and no sound is heard.

The final statement, `tell my parent to beep 3`, shows how to directly invoke the AppleScript `beep` command, rather than the local handler.

For an example that uses a `continue` statement to exit a script handler and return control to the application’s default `quit` handler, see [quit Handlers](About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywvgvzz).

For additional examples, see [Using the continue Statement in Script Objects](Script%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzz).

return

A `return` statement exits a handler and optionally returns a specified value. Execution continues at the place in the script where the handler was called.

##### Syntax

```
return [ expression ]
```

##### Placeholders

**_expression_**
: Represents the value to return.

##### Examples

The following statement, inserted in the body of a handler, returns the integer `2`:

```
return 2 -- returns integer value 2
```

If you include a `return` statement without an expression, AppleScript exits the handler immediately and no value is returned:

```
return -- no value returned
```

See other sections throughout [Handler Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfuytmmzxgyza) for more examples of scripts that use the `return` statement.

```
Discussion
If a handler does not include a
return
statement, AppleScript returns the value returned by the last statement. If the last statement doesn’t return a value, AppleScript returns nothing.
When AppleScript has finished executing a handler (that is, when it executes a
return
statement or the last statement in the handler), it passes control to the place in the script immediately after the place where the handler was called. If a handler call is part of an expression, AppleScript uses the value returned by the handler to evaluate the expression.
It is often considered good programming practice to have just one
return
statement and locate it at the end of a handler. Doing so can provide the following benefits:
The script is easier to understand.
The script is easier to debug.
You can place cleanup code in one place and make sure it is executed.
In some cases, however, it may make more sense to use multiple
return
statements. For example, the
minimumValue
handler in
Handler Syntax (Positional Parameters)
is a simple script that uses two
return
statements.
For related information, see
AppleScript Error Handling
.
```

Handler Syntax (Labeled Parameters)

A handler is a collection of statements that can be invoked by name. This section describes the syntax for handlers that use labeled parameters.

Labeled parameters are identified by their labels and can be listed in any order.

##### Syntax

```
( on | to ) handlerName ¬   [ [ of | in ] directParamName ] ¬   [ ASLabel userParamName ]... ¬   [ given userLabel:userParamName [, userLabel:userParamName ]...]      [ statement ]...end [ handlerName ]
```

##### Placeholders

**_handlerName_**
: An identifier that names the handler.

**_directParamName_**
: An identifier for the direct parameter variable. If it is included, _directParamName_ must be listed immediately after the command name. The word `of` or `in` before _directParamName_ is required in user-defined handlers, but is optional in terminology-defined handlers (for example, those defined by applications).

If a user-defined handler includes a direct parameter, the handler must also include at least one variable parameter.

**_ASLabel_**
: An AppleScript-defined label. The available labels are: `about`, `above`, `against`, `apart from`, `around`, `aside from`, `at`, `below`, `beneath`, `beside`, `between`, `by`, `for`, `from`, `instead of`, `into`, `on`, `onto`, `out of`, `over`, `since`, `thru` (or `through`), `under`. These are the only labels that can be used without the special label `given`. Each label must be unique among the labels for the handler (that is, you cannot use the same label for more than one parameter).

**_userLabel_**
: An identifier for a user-defined label, associated with a user-defined parameter. Each label must be unique.

The first _userLabel_-_userParamName_ pair must follow the word `given`; any additional pairs are separated by commas.

**_userParamName_**
: An identifier for a parameter variable.

**_statement_**
: Any AppleScript statement. These statements can include definitions of `script` objects, each of which, like any `script` object, can contain handlers and other `script` objects. However, you cannot declare another handler within a handler, except within a `script` object.

Handlers often contain a [return](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfuytmmzzgm3q) statement.

##### Examples

For examples and related conceptual information, see [Handlers with Labeled Parameters](About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywvgvzsgi).

```
Discussion
A handler written to respond to an application command (like those in
Handlers in Script Applications
) need not include all of the possible parameters defined for that command. For example, an application might define a command with up to five possible parameters, but you could define a handler for that command with only two of the parameters.
If a script calls a handler with more parameters than are specified in the handler definition, the extra parameters are ignored.
```

Calling a Handler with Labeled Parameters

This section describes the syntax for calling a handler with labeled parameters.

##### Syntax

```
handlerName ¬  [ [ of | in ] directParam ] ¬  [ [ ASLabel paramValue ...] ¬   | [ with labelForTrueParam [, labelForTrueParam ]... ¬    [ ( and | , ) labelForTrueParam ] ] ¬   | [ without labelForFalseParam [, labelForFalseParam ]...] ¬    [ ( and | , ) labelForFalseParam ] ] ¬   | [ given userLabel:paramValue [, userLabel:paramValue ]...]... 
```

##### Placeholders

**_handlerName_**
: An identifier that names the handler.

**_directParam_**
: Any valid expression. The expression for the direct parameter must be listed first if it is included at all.

**_ASLabel_**
: One of the following AppleScript-defined labels used in the definition of the handler: `about`, `above`, `against`, `apart from,` `around`, `aside from`, `at`, `below`, `beneath`, `beside`, `between`, `by`, `for`, `from`, `instead of`, `into`, `on`, `onto`, `out of`, `over`, `since`, `thru` (or `through`), `under`.

**_paramValue_**
: The value of a parameter, which can be any valid expression.

**_labelForTrueParam_**
: The label for a Boolean parameter whose value is `true`. You use this form in `with` clauses. Because the value `true` is implied by the word `with`, you provide only the label, not the value. For an example, see the `findNumbers` handler in [Handlers with Labeled Parameters](About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywvgvzsgi). 

**_labelForFalseParam_**
: The label for a Boolean parameter whose value is `false`. You use this form in `without` clauses. Because the value `false` is implied by the word `without`, you provide only the label, not the value.

**_paramLabel_**
: Any parameter label used in the definition of the handler that is not among the labels for _ASLabel_. You must use the special label `given` to specify these parameters. For an example, see the `findNumbers` handler below.

##### Examples

For examples, see [Handlers with Labeled Parameters](About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywvgvzsgi).

```
Discussion
When you call a handler with labeled parameters, you supply the following:
The handler name.
A value for the direct parameter, if the handler has one. It must directly follow the handler name.
One label-value pair for each AppleScript-defined label and parameter defined for the handler.
One label-value pair for each user-defined label and parameter defined for the handler that
is not
a boolean value.
The first pair is preceded by the word
given
; a comma precedes each additional pair. The order of the pairs does not have to match the order in the handler definition.
For each user-defined label and parameter defined for the handler that
is
a boolean value, you can either:
Supply the label, followed by a boolean expression (as with non-boolean parameters); for example:
given rounding:true
Use a combination of
with
and
without
clauses, as shown in the following examples:
with rounding, smoothing and curling
with rounding without smoothing, curling
```

Handler Syntax (Positional Parameters)

A handler is a collection of statements that can be invoked by name. This section describes the syntax for handlers that use positional parameters.

##### Syntax

```
on | to handlerName ( [ userParamName [, userParamName ]...] )    [ statement ]... end [ handlerName ] 
```

##### Placeholders

**_handlerName_**
: An identifier that names the handler.

**_userParamName_**
: An identifier for a user-defined parameter variable.

**_statement_**
: Any AppleScript statement, including global or local variable declarations. For information about the scope of local and global variables, see [Scope of Variables and Properties](Variables%20and%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgmwvgvzr).

##### Examples

For examples and related conceptual information, see [Handlers with Positional Parameters](About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywvgvzrgm).

Calling a Handler with Positional Parameters

A call for a handler with positional parameters must list the parameters in the same order as they are specified in the handler definition.

##### Syntax

```
handlerName( [ paramValue [, paramValue ]...] )
```

##### Placeholders

**_handlerName_**
: An identifier that names the handler.

**_paramValue_**
: The value of a parameter, which can be any valid expression. If there are two or more parameters, they must be listed in the same order in which they were specified in the handler definition.

##### Examples

For examples, see [Handlers with Positional Parameters](About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywvgvzrgm)

```
Discussion
When you call a handler with positional parameters, you supply the following:
The handler name.
An opening and closing parenthesis.
If the handler has any parameters, then you also list, within the parentheses, the following:
One value for each parameter defined for the handler. The value can be any valid expression.
```

Handler Syntax (Interleaved Parameters)

A handler is a collection of statements that can be invoked by name. This section describes the syntax for handlers that use interleaved parameters.

##### Syntax

```
on | tohandlerNamePart:userParamName [namePart:userParamName ]... )   [ statement ]...end [ handlerName ] 
```

##### Placeholders

**_handlerNamePart_, _namePart_**
: An identifier that, combined with the other parts, forms the handler name.

**_userParamName_**
: An identifier for a user-defined parameter variable.

**_statement_**
: Any AppleScript statement, including global or local variable declarations. For information about the scope of local and global variables, see [Scope of Variables and Properties](Variables%20and%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgmwvgvzr).

##### Examples

For examples and related conceptual information, see [Handlers with Interleaved Parameters](About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywvgvzs).

Calling a Handler with Interleaved Parameters

A call for a handler with interleaved parameters must list the parameters in the same order as they are specified in the handler definition.

##### Syntax

```
( tell scriptObject to | scriptObject's | my ) handlerNamePart:paramValue [ namePart:paramValue ]...] 
```

##### Placeholders

**scriptObject**
: A script object to direct the handler call to, which can be any valid expression.

**_handlerNamePart_, _namePart_**
: An identifier that names the handler.

**_paramValue_**
: The value of a parameter, which can be any valid expression. If there are two or more parameters, they must be listed in the same order in which they were specified in the handler definition.

##### Examples

For examples, see [Handlers with Positional Parameters](About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywvgvzrgm)

```
Discussion
When you call a handler with positional parameters, you supply the following:
A script object to direct the handler call to, either using
tell
script
to
,
script
's
, or
my
, equivalent to
tell me to
.
The first handler name part.
A value for the first parameter.
For each additional parameter, you also list the following:
The next name part, followed by a colon and a value for that parameter. The value can be any valid expression.
```

[Next](Folder%20Actions%20Reference.md)[Previous](Control%20Statements%20Reference.md)

