---
title: AppleScript Language Guide
apple_id: TP40000983
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-01-25'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_classes.html
archived_at: '2026-07-15T05:19:31.550672Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Language Guide](Introduction%20to%20AppleScript%20Language%20Guide.md)


[Next](Commands%20Reference.md)[Previous](About%20Handlers.md)

# Class Reference

A _class_ is a category for objects that share characteristics. AppleScript defines classes for common objects used in AppleScript scripts, such as aliases, Boolean values, integers, text, and so on.

Each object in a script is an instance of a specific class and has the same properties (including the `class` property), can contain the same kinds of elements, and supports the same kinds of operations and coercions as other objects of that type. Objects that are instances of AppleScript types can be used anywhere in a script—they don’t need to be within a `tell` block that specifies an application.

Scriptable applications also define their own classes, such as windows and documents, which commonly contain properties and elements based on many of the basic AppleScript classes described in this chapter. Scripts obtain these objects in the context of the applications that define them. For more information on the class types applications typically support, see “Standard Classes” in Technical Note TN2106, [Scripting Interface Guidelines](https://developer.apple.com/technotes/tn2002/tn2106.html).

alias

A persistent reference to an existing file, folder, or volume in the file system.

For related information, see `[file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvjvomjx)`, `[POSIX file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvjvomjv)`, and [Aliases and Files](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzsha).

##### Properties of alias objects

| `class` | `class` | `class` | `class` | `class` |
|  | Access: | read only | read only | read only |
|  | Class: | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` |
|  | The class identifier for the object. The value is always `alias`. | The class identifier for the object. The value is always `alias`. | The class identifier for the object. The value is always `alias`. | The class identifier for the object. The value is always `alias`. |
| `POSIX path` | `POSIX path` | `POSIX path` | `POSIX path` | `POSIX path` |
|  | Access: | read only | read only | read only |
|  | Class: | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` |
|  | The POSIX-style path to the object. | The POSIX-style path to the object. | The POSIX-style path to the object. | The POSIX-style path to the object. |

##### Coercions Supported

AppleScript supports coercion of an `alias` object to a `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` object or single-item `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)`.

##### Examples

```
set zApp to choose application as alias -- (then choose Finder.app)
--result: alias "Leopard:System:Library:CoreServices:Finder.app:"
class of zApp --result: alias
zApp as text --result: "Leopard:System:Library:CoreServices:Finder.app:"
zApp as list --result: {alias "Leopard:System:Library:CoreServices:Finder.app:"}
```

You can use the `POSIX path` property to obtain a POSIX-style path to the item referred to by an alias:

```
POSIX path of zApp --result: "/System/Library/CoreServices/Finder.app/"
```

```
Discussion
You can only create an alias to a file or folder that already exists.
```

```
Special Considerations
AppleScript 2.0 attempts to resolve aliases only when you run a script. However, in earlier versions, AppleScript attempts to resolve aliases at compile time.
```

application

An application on a local machine or an available server.

An application object in a script has all of the properties described here, which are handled by AppleScript. It may have additional properties, depending on the specific application it refers to.

##### Properties of application objects

| `class` | `class` | `class` | `class` | `class` |
|  | Access: | read only | read only | read only |
|  | Class: | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` |
|  | The class identifier for the object. The value is always `application`. | The class identifier for the object. The value is always `application`. | The class identifier for the object. The value is always `application`. | The class identifier for the object. The value is always `application`. |
| `frontmost` | `frontmost` | `frontmost` | `frontmost` | `frontmost` |
|  | Access: | read only | read only | read only |
|  | Class: | `[boolean](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jijbeory)` | `[boolean](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jijbeory)` | `[boolean](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jijbeory)` |
|  | Is the application frontmost? | Is the application frontmost? | Is the application frontmost? | Is the application frontmost? |
|  | Starting in AppleScript 2.0, accessing an application’s `frontmost` property returns a Boolean value without launching the application or sending it an event. | Starting in AppleScript 2.0, accessing an application’s `frontmost` property returns a Boolean value without launching the application or sending it an event. | Starting in AppleScript 2.0, accessing an application’s `frontmost` property returns a Boolean value without launching the application or sending it an event. | Starting in AppleScript 2.0, accessing an application’s `frontmost` property returns a Boolean value without launching the application or sending it an event. |
|  | The value of `frontmost` for background-only applications, UI element applications such as System Events, and applications that are not running is always `false`. | The value of `frontmost` for background-only applications, UI element applications such as System Events, and applications that are not running is always `false`. | The value of `frontmost` for background-only applications, UI element applications such as System Events, and applications that are not running is always `false`. | The value of `frontmost` for background-only applications, UI element applications such as System Events, and applications that are not running is always `false`. |
| `id` | `id` | `id` | `id` | `id` |
|  | Access: | read only | read only | read only |
|  | Class: | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` |
|  | The application’s bundle identifier (the default) or its four-character signature code. (New in AppleScript 2.0.) | The application’s bundle identifier (the default) or its four-character signature code. (New in AppleScript 2.0.) | The application’s bundle identifier (the default) or its four-character signature code. (New in AppleScript 2.0.) | The application’s bundle identifier (the default) or its four-character signature code. (New in AppleScript 2.0.) |
|  | For example, the bundle identifier for the TextEdit application is `"com.apple.TextEdit"`. Its four-character signature code is `'ttxt'`. If you ask for an application object’s `id` property, you will get the bundle identifier version, unless the application does not have a bundle identifier and does have a signature code. | For example, the bundle identifier for the TextEdit application is `"com.apple.TextEdit"`. Its four-character signature code is `'ttxt'`. If you ask for an application object’s `id` property, you will get the bundle identifier version, unless the application does not have a bundle identifier and does have a signature code. | For example, the bundle identifier for the TextEdit application is `"com.apple.TextEdit"`. Its four-character signature code is `'ttxt'`. If you ask for an application object’s `id` property, you will get the bundle identifier version, unless the application does not have a bundle identifier and does have a signature code. | For example, the bundle identifier for the TextEdit application is `"com.apple.TextEdit"`. Its four-character signature code is `'ttxt'`. If you ask for an application object’s `id` property, you will get the bundle identifier version, unless the application does not have a bundle identifier and does have a signature code. |
| `name` | `name` | `name` | `name` | `name` |
|  | Access: | read only | read only | read only |
|  | Class: | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` |
|  | The application’s name. | The application’s name. | The application’s name. | The application’s name. |
|  | Starting in AppleScript 2.0, accessing an application’s `name` property returns the application name as text without launching the application or sending it an event. | Starting in AppleScript 2.0, accessing an application’s `name` property returns the application name as text without launching the application or sending it an event. | Starting in AppleScript 2.0, accessing an application’s `name` property returns the application name as text without launching the application or sending it an event. | Starting in AppleScript 2.0, accessing an application’s `name` property returns the application name as text without launching the application or sending it an event. |
| `running` | `running` | `running` | `running` | `running` |
|  | Access: | read only | read only | read only |
|  | Class: | `[boolean](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jijbeory)` | `[boolean](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jijbeory)` | `[boolean](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jijbeory)` |
|  | Is the application running? (New in AppleScript 2.0.) | Is the application running? (New in AppleScript 2.0.) | Is the application running? (New in AppleScript 2.0.) | Is the application running? (New in AppleScript 2.0.) |
|  | Accessing an application’s `running` property returns a Boolean value without launching the application or sending it an event. | Accessing an application’s `running` property returns a Boolean value without launching the application or sending it an event. | Accessing an application’s `running` property returns a Boolean value without launching the application or sending it an event. | Accessing an application’s `running` property returns a Boolean value without launching the application or sending it an event. |
|  | You can also ask the System Events utility application whether an application is running. While it requires more lines in your script to do so, that option is available in earlier versions of the Mac OS. | You can also ask the System Events utility application whether an application is running. While it requires more lines in your script to do so, that option is available in earlier versions of the Mac OS. | You can also ask the System Events utility application whether an application is running. While it requires more lines in your script to do so, that option is available in earlier versions of the Mac OS. | You can also ask the System Events utility application whether an application is running. While it requires more lines in your script to do so, that option is available in earlier versions of the Mac OS. |
| `version` | `version` | `version` | `version` | `version` |
|  | Access: | read only | read only | read only |
|  | Class: | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` |
|  | The application’s version. | The application’s version. | The application’s version. | The application’s version. |
|  | Starting in AppleScript 2.0, accessing this property returns the application version as text without launching the application or sending it an event. | Starting in AppleScript 2.0, accessing this property returns the application version as text without launching the application or sending it an event. | Starting in AppleScript 2.0, accessing this property returns the application version as text without launching the application or sending it an event. | Starting in AppleScript 2.0, accessing this property returns the application version as text without launching the application or sending it an event. |

##### Coercions Supported

AppleScript supports coercion of an `application` object to a single-item `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)`.

##### Examples

You can determine whether an application on the current computer is running without launching it (this won’t work if your target is on a remote computer):

```
tell application "iTunes" -- doesn't automatically launch app
    if it is running then
        pause
    end if
end tell
```

You can also use this format:

```
if application "iTunes" is running
    tell application "iTunes" to pause
end if
```

The following statements specify the TextEdit application by, respectively, its signature, its bundle id, and by a POSIX path to a specific version of TextEdit:

```
application id "ttxt"
application id "com.apple.TextEdit"
application "/Applications/TextEdit.app"
```

You can target a remote application with a `tell` statement. For details, see `[Remote Applications](../conceptual/ASLR_fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzz)`.

```
Special Considerations
Starting in OS X v10.5, there are several changes in application behavior:
Applications launch hidden.
AppleScript has always launched applications if it needed to in order to send them a command. However, they would always launch visibly, which could be visually disruptive. AppleScript now launches applications hidden by default. They will not be visible unless the script explicitly says otherwise using
activate
.
Applications are located lazily.
When running a script, AppleScript will not attempt to locate an application until it needs to in order to send it a command. This means that a compiled script or script application may contain references to applications that do not exist on the user’s system, but AppleScript will not ask where the missing applications are until it encounters a relevant
tell
block. Previous versions of AppleScript would attempt to locate every referenced application before running the script.
When opening a script for editing, AppleScript will attempt to locate all the referenced applications in the entire script, which may mean asking where one is. Pressing the Cancel button only cancels the search for that application; the script will continue opening normally, though custom terminology for that application will display as raw codes. In older versions, pressing Cancel would cancel opening the script.
Applications are located and re-located dynamically.
Object specifiers that refer to applications, including those in
tell
blocks, are evaluated every time a script runs. This alleviates problems with scripts getting “stuck” to a particular copy of an application.
In prior versions of AppleScript, use of the new built-in application properties will fall back to sending an event to the application, but the application may not handle these properties in the same way, or handle them at all. (Most applications will handle
name
,
version
, and
frontmost
;
id
and
running
are uncommon.) The other new features described above require AppleScript 2.0.
```

boolean

A logical truth value.

A `boolean` object evaluates to one of the AppleScript constants `true` or `false`. A _Boolean expression_ contains one or more `boolean` objects and evaluates to `true` or `false`.

##### Properties of boolean objects

| `class` | `class` | `class` | `class` | `class` |
|  | Access: | read only | read only | read only |
|  | Class: | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` |
|  | The class identifier for the object. The value is always `boolean`. | The class identifier for the object. The value is always `boolean`. | The class identifier for the object. The value is always `boolean`. | The class identifier for the object. The value is always `boolean`. |

##### Operators

The operators that take `boolean` objects as operands are `and`, `or`, `not`, `&`, `=`, and `≠`, as well as their text equivalents: `is equal to`, `is not equal to`, `equals`, and so on.

The `=` operator returns `true` if both operands evaluate to the same value (either `true` or `false`); the `≠` operator returns `true` if the operands evaluate to different values.

The binary operators `and` and `or` take `boolean` objects as operands and return Boolean values. An `and` operation, such as `(2 > 1) and (4 > 3)`, has the value `true` if both its operands are `true`, and `false` otherwise. An `or` operation, such as `(theString = "Yes") or (today = "Tuesday")`, has the value `true` if either of its operands is `true`.

The unary `not` operator changes a `true` value to `false` or a `false` value to `true`.

The concatenation operator (`&`) creates a list containing the two boolean values on either side of it; for example:

```
true & false --result: {true, false}
```

For additional information on these operators, see [Operators Reference](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfuytenbqg4ya).

##### Coercions Supported

AppleScript supports coercion of a `boolean` object to a single-item `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)`, a `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` object, or an `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)`.

##### Examples

The following are simple Boolean expressions:

```
true
false
paragraphCount > 2
```

AppleScript supplies the Boolean constants `true` and `false` to serve as the result of evaluating a Boolean operation. But scripts rarely need to use these literals explicitly because a Boolean expression itself evaluates to a Boolean value. For example, consider the following two script snippets:

```
if companyName is equal to "Acme Baking" then
    return true
else
    return false
end if

return companyName is equal to "Acme Baking"
```

The second, simpler version, just returns the value of the Boolean comparison `companyName is equal to "Acme Baking"`, so it doesn’t need to use a Boolean constant.

```
Discussion
When you pass a Boolean value as a parameter to a command, the form may change when you compile the command. For example, the following line
choose folder showing package contents true
is converted to this when compiled by AppleScript:
choose folder with showing package contents
It is standard for AppleScript to compile parameter expressions from the Boolean form (such as
showing package contents true
or
invisibles false
) into the
with
form (
with showing package contents
or
without invisibles
, respectively).
```

class

Specifies the class of an object or value.

All classes have a `class` property that specifies the class type. The value of the `class` property is an identifier.

##### Properties of class objects

| `class` | `class` | `class` | `class` | `class` |
|  | Access: | read only | read only | read only |
|  | Class: | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` |
|  | The class identifier for the object. The value of this property is always `class`. | The class identifier for the object. The value of this property is always `class`. | The class identifier for the object. The value of this property is always `class`. | The class identifier for the object. The value of this property is always `class`. |

##### Operators

The operators that take class identifier values as operands are `&`, `=`, `≠`, and `as`.

The coercion operator `as` takes an object of one class type and coerces it to an object of a type specified by a class identifier. For example, the following statement coerces a `text` object into a corresponding `real`:

```
"1.5" as real --result: 1.5
```


##### Coercions Supported

AppleScript supports coercion of a class identifier to a single-item `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` or a `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` object.

##### Examples

Asking for the class of a type such as `integer` results in a value of `class`:

```
class of text --result: class
class of integer --result: class
```

Here is the class of a boolean literal:

```
class of true --result: boolean
```

And here are some additional examples:

```
class of "Some text" --result: text
class of {1, 2, "hello"} --result: list
```

constant

A word with a predefined value.

Constants are generally used for enumerated types. You cannot define constants in scripts; constants can be defined only by applications and by AppleScript. See [Global Constants in AppleScript](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawueqkkijcekssj) for more information.

##### Properties of constant objects

| `class` | `class` | `class` | `class` | `class` |
|  | Access: | read-only | read-only | read-only |
|  | Class: | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` |
|  | The class identifier for the object. The value of this property is always `constant`. | The class identifier for the object. The value of this property is always `constant`. | The class identifier for the object. The value of this property is always `constant`. | The class identifier for the object. The value of this property is always `constant`. |

##### Operators

The operators that take `constant` objects as operands are `&`, `=`, `≠`, and `as`.

##### Coercions Supported

AppleScript supports coercion of a `constant` object to a single-item `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` or a `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` object.

##### Examples

One place you use constants defined by AppleScript is in text comparisons performed with `considering` or `ignoring` statements (described in `[considering / ignoring (text comparison)](ASLR_control_statements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytkojyg44q)`). For example, in the following script statements, `punctuation`, `hyphens`, and `white space` are constants:

```
considering punctuation but ignoring hyphens and white space
    "bet-the farm," = "BetTheFarm," --result: true
end considering
class of hyphens --result: constant
```

The final statement shows that the class of `hyphens` is `constant`.

```
Discussion
Constants are not text strings, and they must not be surrounded by quotation marks.
Literal constants are defined in
Literals and Constants
.
In addition to the constants defined by AppleScript, applications often define enumerated types to be used for command parameters or property values. For example, the iTunes
search
command defines these constants for specifying the search area:
albums
all
artists
composers
displayed
songs
```

date

Specifies the day of the week, the date (month, day of the month, and year), and the time (hours, minutes, and seconds).

To get the current date, use the command `[current date](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzthe)`:

```
set theDate to current date
--result: "Friday, November 9, 2007 11:35:50 AM"
```

You can get and set the different parts of a `date` object through the date and time properties described below.

When you compile a script, AppleScript displays date and time values according to the format specified in System Preferences.

##### Properties of date objects

| `class` | `class` | `class` | `class` | `class` |
|  | Access: | read only | read only | read only |
|  | Class: | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` |
|  | The class identifier for the object. The value of this property is always `date`. | The class identifier for the object. The value of this property is always `date`. | The class identifier for the object. The value of this property is always `date`. | The class identifier for the object. The value of this property is always `date`. |
| `day` | `day` | `day` | `day` | `day` |
|  | Access: | read/write | read/write | read/write |
|  | Class: | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` |
|  | Specifies the day of the month of a `date` object. | Specifies the day of the month of a `date` object. | Specifies the day of the month of a `date` object. | Specifies the day of the month of a `date` object. |
| `weekday` | `weekday` | `weekday` | `weekday` | `weekday` |
|  | Access: | read only | read only | read only |
|  | Class: | `[constant](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2finceqqy)` | `[constant](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2finceqqy)` | `[constant](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2finceqqy)` |
|  | Specifies the day of the week of a `date` object, with one of these constants: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, or `Sunday`. | Specifies the day of the week of a `date` object, with one of these constants: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, or `Sunday`. | Specifies the day of the week of a `date` object, with one of these constants: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, or `Sunday`. | Specifies the day of the week of a `date` object, with one of these constants: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, or `Sunday`. |
| `month` | `month` | `month` | `month` | `month` |
|  | Access: | read/write | read/write | read/write |
|  | Class: | `[constant](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2finceqqy)` | `[constant](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2finceqqy)` | `[constant](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2finceqqy)` |
|  | Specifies the month of the year of a `date` object, with one of the constants `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, or `December`. | Specifies the month of the year of a `date` object, with one of the constants `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, or `December`. | Specifies the month of the year of a `date` object, with one of the constants `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, or `December`. | Specifies the month of the year of a `date` object, with one of the constants `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, or `December`. |
| `year` | `year` | `year` | `year` | `year` |
|  | Access: | read/write | read/write | read/write |
|  | Class: | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` |
|  | Specifies the year of a `date` object; for example, `2004`. | Specifies the year of a `date` object; for example, `2004`. | Specifies the year of a `date` object; for example, `2004`. | Specifies the year of a `date` object; for example, `2004`. |
| `time` | `time` | `time` | `time` | `time` |
|  | Access: | read/write | read/write | read/write |
|  | Class: | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` |
|  | Specifies the number of seconds since midnight of a `date` object; for example, `2700` is equivalent to 12:45 AM (2700 / 60 seconds = 45 minutes). | Specifies the number of seconds since midnight of a `date` object; for example, `2700` is equivalent to 12:45 AM (2700 / 60 seconds = 45 minutes). | Specifies the number of seconds since midnight of a `date` object; for example, `2700` is equivalent to 12:45 AM (2700 / 60 seconds = 45 minutes). | Specifies the number of seconds since midnight of a `date` object; for example, `2700` is equivalent to 12:45 AM (2700 / 60 seconds = 45 minutes). |
| `date string` | `date string` | `date string` | `date string` | `date string` |
|  | Access: | read only | read only | read only |
|  | Class: | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` |
|  | A `text` object that specifies the date portion of a `date` object; for example, `"Friday, November 9, 2007"`. | A `text` object that specifies the date portion of a `date` object; for example, `"Friday, November 9, 2007"`. | A `text` object that specifies the date portion of a `date` object; for example, `"Friday, November 9, 2007"`. | A `text` object that specifies the date portion of a `date` object; for example, `"Friday, November 9, 2007"`. |
|  | To obtain a compact version of the date, use `short date string` . For example, `short date string of (current date) --result: "1/27/08"`. | To obtain a compact version of the date, use `short date string` . For example, `short date string of (current date) --result: "1/27/08"`. | To obtain a compact version of the date, use `short date string` . For example, `short date string of (current date) --result: "1/27/08"`. | To obtain a compact version of the date, use `short date string` . For example, `short date string of (current date) --result: "1/27/08"`. |
| `time string` | `time string` | `time string` | `time string` | `time string` |
|  | Access: | read only | read only | read only |
|  | Class: | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` |
|  | A `text` object that specifies the time portion of a `date` object; for example, `"3:20:24 PM"`. | A `text` object that specifies the time portion of a `date` object; for example, `"3:20:24 PM"`. | A `text` object that specifies the time portion of a `date` object; for example, `"3:20:24 PM"`. | A `text` object that specifies the time portion of a `date` object; for example, `"3:20:24 PM"`. |

##### Operators

The operators that take `date` object as operands are `&`, `+`, `–`, `=`, `≠`, `>`, `≥`, `<`, `≤`, `comes before`, `comes after`, and `as`. In expressions containing `>`, `≥`, `<`, `≤`, `comes before`, or `comes after`, a later time is greater than an earlier time.

AppleScript supports the following operations on `date` objects with the `+` and `–` operators:

```
date + timeDifference
--result: date
date - date
--result: timeDifference
date - timeDifference
--result: date
```

where `timeDifference` is an `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` value specifying a time difference in seconds. To simplify the notation of time differences, you can also use one or more of these of these constants:

```
minutes
    60
hours
    60 * minutes
days
    24 * hours
weeks
    7 * days
```

Here’s an example:

```
date "Friday, November 9, 2007" + 4 * days + 3 * hours + 2 *  minutes
--result: date "Tuesday, November 13, 2007 3:02:00 AM"
```

To express a time difference in more convenient form, divide the number of seconds by the appropriate constant:

```
31449600 / weeks --result: 52.0
```

To get an integral number of hours, days, and so on, use the `div` operator:

```
151200 div days --result: 1
```

To get the difference, in seconds, between the current time and Greenwich mean time, use the `[time to GMT](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzug4)` command.

##### Coercions Supported

AppleScript supports coercion of a `date` object to a single-item `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` or a `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` object.

##### Examples

The following expressions show some options for specifying a date, along with the results of compiling the statements. If you construct a date using only partial information, AppleScript fills in the missing pieces with default values. The actual format is based on the settings in System Preferences.

```
date "8/9/2007, 17:06"
     --result: date "Thursday, August 9, 2007 5:06:00 PM"
date "7/16/70"
     --result: date "Wednesday, July 16, 2070 12:00:00 AM"
date "12:06" -- specifies a time on the current date
     --result: date "Friday, November 9, 2007 12:06:00 PM"
date "Sunday, December 12, 1954 12:06 pm"
     --result: date "Sunday, December 12, 1954 12:06:00 PM"
```

The following statements access various date properties (results depend on the date the statements are executed):

```
set theDate to current date --using current date command
--result: date "Friday, November 9, 2007 11:58:38 AM"
weekday of theDate --result: Friday
day of theDate --result: 9
month of theDate --result: November
year of theDate --result: 2007
time of theDate --result: 43118 (seconds since 12:00:00 AM)
time string of theDate --result: "11:58:38 AM"
date string of theDate --result: "Friday, November 9, 2007"
```

If you want to specify a time relative to a date, you can do so by using `of`, `relative to`, or `in`, as shown in the following examples.

```
date "2:30 am" of date "Jan 1, 2008"
    --result: date "Tuesday, January 1, 2008 2:30:00 AM"
date "2:30 am" of date "Sun Jan 27, 2008"
    --result: date "Sunday, January 27, 2008 2:30:00 AM"
date "Nov 19, 2007" relative to date "3PM"
    --result: date "Monday, November 19, 2007 3:00:00 PM"
date "1:30 pm" in date "April 1, 2008"
    --result: date "Tuesday, April 1, 2008 1:30:00 PM"
```

```
Special Considerations
You can create a
date
object using a string that follows the date format specified in the Formats pane in International preferences. For example, in US English:
set myDate to date "3/4/2008"
When you compile this statement, it is converted to the following:
set myDate to date "Tuesday, March 4, 2008 12:00:00 AM"
```

file

A reference to a file, folder, or volume in the file system. A `file` object has exactly the same attributes as an `alias` object, with the addition that it can refer to an item that does not exist.

For related information, see `[alias](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvjvomy)` and `[POSIX file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvjvomjv)`. For a description of the format for a file path, see [Aliases and Files](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzsha).

##### Coercions Supported

AppleScript supports coercion of a `file` object to a `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` object or single-item `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)`.

##### Examples

```
set fp to open for access file "Leopard:Users:myUser:NewFile"
close access fp
```

```
Discussion
You can create a
file
object that refers to a file or folder that does not exist. For example, you can use the
choose file name
command to obtain a
file
object for a file that need not currently exist.
```

integer

A number without a fractional part.

##### Properties of integer objects

| `class` | `class` | `class` | `class` | `class` |
|  | Access: | read-only | read-only | read-only |
|  | Class: | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` |
|  | The class identifier for the object. The value of this property is always `integer`. | The class identifier for the object. The value of this property is always `integer`. | The class identifier for the object. The value of this property is always `integer`. | The class identifier for the object. The value of this property is always `integer`. |

##### Operators

The operators that can have `integer` values as operands are `+`, `-`, `*`, `÷` (or `/`), `div`, `mod`, `^`, `=`, `≠`, `>`, `≥`, `<`, and `≤`.

The `div` operator always returns an `integer` value as its result. The `+`, `–`, `*`, `mod`, and `^` operators return values of type `integer` or `real`.

##### Coercions Supported

AppleScript supports coercion of an `integer` value to a single-item `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)`, a `[real](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2kivbukqy)` number, or a `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` object.

Coercion of an `integer` to a `number` does nothing:

```
set myCount to 7 as number
class of myCount --result: integer
```


##### Examples

```
1
set myResult to 3 - 2
-1
1000
```

```
Discussion
The biggest value (positive or negative) that can be expressed as an integer in AppleScript is ±536870911, which is equal to ±(2^29 – 1). Larger integers are converted to real numbers, expressed in exponential notation, when scripts are compiled.
```

list

An ordered collection of values. The values contained in a list are known as items. Each item can belong to any class.

A list appears in a script as a series of expressions contained within braces and separated by commas. An empty list is a list containing no items. It is represented by a pair of empty braces: `{}`.

##### Properties of list objects

| `class` | `class` | `class` | `class` | `class` |
|  | Access: | read-only | read-only | read-only |
|  | Class: | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` |
|  | The class identifier for the object. The value of this property is always `list`. | The class identifier for the object. The value of this property is always `list`. | The class identifier for the object. The value of this property is always `list`. | The class identifier for the object. The value of this property is always `list`. |
| `length` | `length` | `length` | `length` | `length` |
|  | Access: | read only | read only | read only |
|  | Class: | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` |
|  | Specifies he number of items in the list. | Specifies he number of items in the list. | Specifies he number of items in the list. | Specifies he number of items in the list. |
| `rest` | `rest` | `rest` | `rest` | `rest` |
|  | Access: | read only | read only | read only |
|  | Class: | `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` | `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` | `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` |
|  | A list containing all items in the list except the first item.  | A list containing all items in the list except the first item.  | A list containing all items in the list except the first item.  | A list containing all items in the list except the first item.  |
| `reverse` | `reverse` | `reverse` | `reverse` | `reverse` |
|  | Access: | read only | read only | read only |
|  | Class: | `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` | `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` | `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` |
|  | A list containing all items in the list, but in the opposite order. | A list containing all items in the list, but in the opposite order. | A list containing all items in the list, but in the opposite order. | A list containing all items in the list, but in the opposite order. |

##### Elements of list objects

| `item` | `item` | `item` | `item` | `item` |
|  |  A value contained in the list. Each value contained in a list is an item and an item may itself be another list. You can refer to values by their item numbers. For example, `item 2 of {"soup", 2, "nuts"}` is the integer `2`.  You can also refer to indexed list items by class. For example, `integer 1 of {"oatmeal", 42, "new"}` returns `42`. |  A value contained in the list. Each value contained in a list is an item and an item may itself be another list. You can refer to values by their item numbers. For example, `item 2 of {"soup", 2, "nuts"}` is the integer `2`.  You can also refer to indexed list items by class. For example, `integer 1 of {"oatmeal", 42, "new"}` returns `42`. |  A value contained in the list. Each value contained in a list is an item and an item may itself be another list. You can refer to values by their item numbers. For example, `item 2 of {"soup", 2, "nuts"}` is the integer `2`.  You can also refer to indexed list items by class. For example, `integer 1 of {"oatmeal", 42, "new"}` returns `42`. |  A value contained in the list. Each value contained in a list is an item and an item may itself be another list. You can refer to values by their item numbers. For example, `item 2 of {"soup", 2, "nuts"}` is the integer `2`.  You can also refer to indexed list items by class. For example, `integer 1 of {"oatmeal", 42, "new"}` returns `42`. |

##### Operators

The operators that can have list values as operands are `&`, `=`, `≠`, `starts with`, `ends with`, `contains`, and `is contained by`.

For detailed explanations and examples of how AppleScript operators treat lists, see [Operators Reference](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfuytenbqg4ya).

##### Commands Handled

You can count the items in a list or the elements of a specific class in a list with the `[count](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgu)` command. You can also use the `length` property of a list:

```
count {"a", "b", "c", 1, 2, 3} --result: 6
length of {"a", "b", "c", 1, 2, 3} --result: 6
```


##### Coercions Supported

AppleScript supports coercion of a single-item list to any class to which the item can be coerced if it is not part of a list.

AppleScript also supports coercion of an entire list to a `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` object if each of the items in the list can be coerced to a `text` object, as in the following example:

```
{5, "George", 11.43, "Bill"} as text --result: "5George11.43Bill"
```

The resulting `text` object concatenates all the items, separated by the current value of the AppleScript property `text item delimiters`. This property defaults to an empty string, so the items are simply concatenated. For more information, see [text item delimiters](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzsgi).

Individual items in a list can be of any class, and AppleScript supports coercion of any value to a list that contains a single item.

##### Examples

The following statement defines a list that contains a `text` object, an integer, and a Boolean value:

```
{ "it's", 2, true }
```

Each list item can be any valid expression. The following list has the same value as the previous list:

```
{ "it" & "'s", 1 + 1, 4 > 3 }
```

The following statements work with lists; note that the concatenation operator (`&`) joins two lists into a single list:

```
class of {"this", "is", "a", "list"} --result: list
item 3 of {"this", "is", "a", "list"} --result: "a"
items 2 thru 3 of {"soup", 2, "nuts"} --result: {2, "nuts"}
{"This"} & {"is", "a", "list"} --result: {"This", "is", "a", "list"}
```

For large lists, it is more efficient to use the `a reference to operator` when inserting a large number of items into a list, rather than to access the list directly. For example, using direct access, the following script takes about 10 seconds to create a list of 10,000 integers (results will vary depending on the computer and other factors):

```
set bigList to {}
set numItems to 10000
set t to (time of (current date)) --Start timing operations
repeat with n from 1 to numItems
    copy n to the end of bigList
    -- DON'T DO THE FOLLOWING--it's even slower!
    -- set bigList to bigList & n
end
set total to (time of (current date)) - t --End timing
```

But the following script, which uses the `a reference to operator`, creates a list of 100,000 integers (ten times the size) in just a couple of seconds (again, results may vary):

```
set bigList to {}
set bigListRef to a reference to bigList
set numItems to 100000
set t to (time of (current date)) --Start timing operations
repeat with n from 1 to numItems
    copy n to the end of bigListRef
end
set total to (time of (current date)) - t --End timing
```

Similarly, accessing the items in the previously created list is much faster using `a reference to`—the following takes just a few seconds:

```
set t to (time of (current date)) --Start timing
repeat with n from 1 to numItems -- where numItems = 100,000
    item n of bigListRef
end repeat
set total to (time of (current date)) - t --End timing
```

However, accessing the list directly, even for only 4,000 items, can take over a minute:

```
set numItems to 4000
set t to (time of (current date)) --Start timing
repeat with n from 1 to numItems
    item n of bigList
end repeat
set total to (time of (current date)) - t --End timing
```

number

An abstract class that can represent an `integer` or a `real`.

There is never an object whose class is `number`; the actual class of a "number" object is always one of the more specific types, `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` or `[real](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2kivbukqy)`.

##### Properties of number objects

| `class` | `class` | `class` | `class` | `class` |
|  | Access: | read-only | read-only | read-only |
|  | Class: | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` |
|  | The class identifier for the object. The value of this property is always either `integer` or `real`. | The class identifier for the object. The value of this property is always either `integer` or `real`. | The class identifier for the object. The value of this property is always either `integer` or `real`. | The class identifier for the object. The value of this property is always either `integer` or `real`. |

##### Operators

Because values identified as values of class `number` are really values of either class `integer` or class `real`, the operators available are the operators described in the definitions of the `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` or `[real](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2kivbukqy)` classes.

##### Coercions Supported

Coercing an object to `number` results in an `integer` object if the result of the coercion is an `integer`, or a `real` object if the result is a non-integer number.

##### Examples

Any valid literal expression for an `integer` or a `real` value is also a valid literal expression for a `number` value:

```
1
2
-1
1000
10.2579432
1.0
1.
```

POSIX file

A pseudo-class equivalent to the `file` class.

There is never an object whose class is `POSIX file`; the result of evaluating a POSIX file specifier is a `file` object. The difference between `file` and `POSIX file` objects is in how they interpret name specifiers: a `POSIX file` object interprets `"name"` as a POSIX path, while a `file` object interprets it as an HFS path.

For related information, see `[alias](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvjvomy)` and `[file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvjvomjx)`. For a description of the format for a POSIX path, see [Aliases and Files](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzsha).

##### Properties of POSIX file objects

See `[file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvjvomjx)`.

##### Coercions Supported

See `[file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvjvomjx)`.

##### Examples

The following example asks the user to specify a file name, starting in the temporary directory `/tmp`, which is difficult to specify using a file specifier:

```
set fileName to choose file name default location (POSIX file "/tmp")
    -result: dialog starts in /tmp folder
```

real

Numbers that can include a fractional part, such as 3.14159 and 1.0.

##### Properties of real objects

| `class` | `class` | `class` | `class` | `class` |
|  | Access: | read-only | read-only | read-only |
|  | Class: | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` |
|  | The class identifier for the object. The value of this property is always `real`. | The class identifier for the object. The value of this property is always `real`. | The class identifier for the object. The value of this property is always `real`. | The class identifier for the object. The value of this property is always `real`. |

##### Operators

The operators that can have `real` values as operands are `+`, `-`, `*`, `÷` (or `/`), `div`, `mod`, `^`, `=`, `≠`, `>`, `≥`, `<`, and `≤`.

The `÷` and `/` operators always return `real` values as their results. The `+`, `-`, `*`, `mod`, and `^` operators return `real` values if either of their operands is a `real` value.

##### Coercions Supported

AppleScript supports coercion of a `real` value to an `integer` value, rounding any fractional part.

AppleScript also supports coercion of a `real` value to a single-item `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` or a `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` object. Coercion to text uses the decimal separator specified in Numbers in the Formats pane in International preferences.

##### Examples

```
10.2579432
1.0
1.
```

As shown in the third example, a decimal point indicates a real number, even if there is no fractional part.

Real numbers can also be written using exponential notation. A letter `e` is preceded by a real number (without intervening spaces) and followed by an integer exponent (also without intervening spaces). The exponent can be either positive or negative. To obtain the value, the `real` number is multiplied by 10 to the power indicated by the exponent, as in these examples:

```
1.0e5 --equivalent to 1.0 * 10^5, or 100000
1.0e+5 --same as 1.0e5
1.0e-5 --equivalent to 1.0 * 10^-5, or .00001
```

```
Discussion
Real numbers that are greater than or equal to 10,000.0 or less than or equal to 0.0001 are converted to exponential notation when scripts are compiled. The largest value that can be evaluated (positive or negative) is 1.797693e+308.
```

record

An unordered collection of labeled properties. The only AppleScript classes that support user-defined properties are `record` and `script`.

A record appears in a script as a series of property definitions contained within braces and separated by commas. Each property definition consists of a label, a colon, and the value of the property. For example, this is a record with two properties: `{product:"pen", price:2.34}`.

Each property in a record has a unique label which distinguishes it from other properties in the collection. The values assigned to properties can belong to any class. You can change the class of a property simply by assigning a value belonging to another class.

##### Properties of record objects

| `class` | `class` | `class` | `class` | `class` |
|  | Access: | read/write | read/write | read/write |
|  | Class: | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` |
|  | The class identifier for the record. By default, the value is `record`. | The class identifier for the record. By default, the value is `record`. | The class identifier for the record. By default, the value is `record`. | The class identifier for the record. By default, the value is `record`. |
|  | If you define a `class` property explicitly in a record, the value you define replaces the implicit `class` value. In the following example, the class is set to `integer`: | If you define a `class` property explicitly in a record, the value you define replaces the implicit `class` value. In the following example, the class is set to `integer`: | If you define a `class` property explicitly in a record, the value you define replaces the implicit `class` value. In the following example, the class is set to `integer`: | If you define a `class` property explicitly in a record, the value you define replaces the implicit `class` value. In the following example, the class is set to `integer`: |
|  | `set myRecord to {class:integer, min:1, max:10}` | `set myRecord to {class:integer, min:1, max:10}` | `set myRecord to {class:integer, min:1, max:10}` | `set myRecord to {class:integer, min:1, max:10}` |
|  | `class of myRecord --result: integer` | `class of myRecord --result: integer` | `class of myRecord --result: integer` | `class of myRecord --result: integer` |
| `length` | `length` | `length` | `length` | `length` |
|  | Access: | read only | read only | read only |
|  | Class: | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` |
|  | Specifies the number of properties in the record. | Specifies the number of properties in the record. | Specifies the number of properties in the record. | Specifies the number of properties in the record. |

##### Operators

The operators that can have records as operands are `&`, `=`, `≠`, `contains`, and `is contained by`.

For detailed explanations and examples of how AppleScript operators treat records, see [Operators Reference](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfuytenbqg4ya).

##### Commands Handled

You can count the properties in a record with the `count` command:

```
count {name:"Robin", mileage:400} --result: 2
```


##### Coercions Supported

AppleScript supports coercion of records to lists; however, all labels are lost in the coercion and the resulting list cannot be coerced back to a record.

##### Examples

The following example shows how to change the value of a property in a record:

```
set myRecord to {product:"pen", price:2.34}
product of myRecord -- result: "pen"

set product of myRecord to "pencil"
product of myRecord -- result: "pencil"
```

AppleScript evaluates expressions in a record before using the record in other expressions. For example, the following two records are equivalent:

```
{ name:"Steve", height:76 - 1.5, weight:150 + 20 }
{ name:"Steve", height:74.5, weight:170 }
```

You cannot refer to properties in records by numeric index. For example, the following object specifier, which uses the index reference form on a record, is not valid.

```
item 2 of { name:"Rollie", IQ:186, city:"Unknown" } --result: error
```

You can access the _length_ property of a record to count the properties it contains:

```
length of {name:"Chris", mileage:1957, city:"Kalamazoo"} --result: 3
```

You can get the same value with the `[count](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgu)` command:

```
count {name:"Chris", mileage:1957, city:"Kalamazoo"} --result: 3
```

```
Discussion
After you define a record, you cannot add additional properties to it. You can, however, concatenate records. For more information, see
& (concatenation)
.
```

reference

An object that encapsulates an object specifier.

The result of the `[a reference to](ASLR_operators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfvjvomi)` operator is a `reference` object, and object specifiers returned from application commands are implicitly turned into `reference` objects.

A `reference` object “wraps” an object specifier. If you target a `reference` object with the `[get](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgy)` command, the command returns the `reference` object itself. If you ask a `reference` object for its `contents` property, it returns the enclosed object specifier. All other requests to a `reference` object are forwarded to its enclosed object specifier. For example, if you ask for the `class` of a `reference` object, you get the `class` of the object specified by its object specifier.

For related information, see [Object Specifiers](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzx).

##### Properties of reference objects

Other than the `contents` property, all other property requests are forwarded to the enclosed object specifier, so the reference object appears to have all the properties of the referenced object.

| `contents` | `contents` | `contents` | `contents` | `contents` |
|  | Access: | depends on the referenced object or objects | depends on the referenced object or objects | depends on the referenced object or objects |
|  | Class: | depends on the referenced object or objects | depends on the referenced object or objects | depends on the referenced object or objects |
|  | The enclosed object specifier. | The enclosed object specifier. | The enclosed object specifier. | The enclosed object specifier. |

##### Operators

All operators are forwarded to the enclosed object specifier, so the reference object appears to support all the operators of referenced object.

The `a reference to` operator returns a reference object as its result.

##### Coercions Supported

All coercions are forwarded to the enclosed object specifier, so the reference object appears to support all the coercions of referenced object.

##### Examples

Reference objects are most often used to specify application objects. The following example creates a reference to a window within the TextEdit application:

```
set myWindow to a ref to window "top.rtf" of application "TextEdit"
--result: window "top.rtf" of application "TextEdit"
```

In subsequent script statements, you can use the variable `myWindow` in place of the longer term `window "top.rtf" of application "TextEdit"`.

Because all property requests other than `contents of` are forwarded to its enclosed specifier, the `reference` object appears to have all the properties of the referenced object. For example, both `class of` statements in the following example return `window`:

```
set myRef to a reference to window 1
class of contents of myRef  -- explicit dereference using "contents of"
class of myRef  -- implicit dereference
```

For additional examples, see the `[a reference to](ASLR_operators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfvjvomi)` operator.

RGB color

A type definition for a three-item list of `integer` values, from 0 to 65535, that specify the red, green, and blue components of a color.

Otherwise, behaves exactly like a `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` object.

##### Examples

```
set whiteColor to {65535, 65535, 65535} -- white
set yellowColor to {65535, 65535, 0} -- yellow
yellowColor as string --result: "65535655350"
set redColor to {65535, 0, 0} -- red
set userColor to choose color default color redColor
```

script

A collection of AppleScript declarations and statements that can be executed as a group.

The syntax for a `script` object is described in [Defining Script Objects](Script%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzs).

##### Properties of script objects

| `class` | `class` | `class` | `class` | `class` |
|  | Access: | read-only | read-only | read-only |
|  | Class: | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` |
|  | The class identifier for the object. The value of this property is always `script`. | The class identifier for the object. The value of this property is always `script`. | The class identifier for the object. The value of this property is always `script`. | The class identifier for the object. The value of this property is always `script`. |
| `name` | `name` | `name` | `name` | `name` |
|  | Access: | read-only | read-only | read-only |
|  | Class: | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` |
|  | The name of the script object, implicitly defined in AppleScript 2.3 and later. For top-level scripts, this is the name of the file the script is saved in, unless explicitly defined otherwise using a property, or, for a top-level script saved as a script bundle, using the Info.plist key `CFBundleName`. Script Editor’s Bundle Contents drawer includes a “Name” field to set this value. For other script objects, it is the name the script was defined with, as text. | The name of the script object, implicitly defined in AppleScript 2.3 and later. For top-level scripts, this is the name of the file the script is saved in, unless explicitly defined otherwise using a property, or, for a top-level script saved as a script bundle, using the Info.plist key `CFBundleName`. Script Editor’s Bundle Contents drawer includes a “Name” field to set this value. For other script objects, it is the name the script was defined with, as text. | The name of the script object, implicitly defined in AppleScript 2.3 and later. For top-level scripts, this is the name of the file the script is saved in, unless explicitly defined otherwise using a property, or, for a top-level script saved as a script bundle, using the Info.plist key `CFBundleName`. Script Editor’s Bundle Contents drawer includes a “Name” field to set this value. For other script objects, it is the name the script was defined with, as text. | The name of the script object, implicitly defined in AppleScript 2.3 and later. For top-level scripts, this is the name of the file the script is saved in, unless explicitly defined otherwise using a property, or, for a top-level script saved as a script bundle, using the Info.plist key `CFBundleName`. Script Editor’s Bundle Contents drawer includes a “Name” field to set this value. For other script objects, it is the name the script was defined with, as text. |
| `id` | `id` | `id` | `id` | `id` |
|  | Access: | read-only | read-only | read-only |
|  | Class: | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` |
|  | The unique identifier of the script object, implicitly defined in AppleScript 2.3 and later. Its value is `missing value` unless explicitly defined using a property, or, for a top-level script saved as a script bundle, using the Info.plist key `CFBundleIdentifier`. Script Editor’s Bundle Contents drawer includes an “Identifier” field to set this value. | The unique identifier of the script object, implicitly defined in AppleScript 2.3 and later. Its value is `missing value` unless explicitly defined using a property, or, for a top-level script saved as a script bundle, using the Info.plist key `CFBundleIdentifier`. Script Editor’s Bundle Contents drawer includes an “Identifier” field to set this value. | The unique identifier of the script object, implicitly defined in AppleScript 2.3 and later. Its value is `missing value` unless explicitly defined using a property, or, for a top-level script saved as a script bundle, using the Info.plist key `CFBundleIdentifier`. Script Editor’s Bundle Contents drawer includes an “Identifier” field to set this value. | The unique identifier of the script object, implicitly defined in AppleScript 2.3 and later. Its value is `missing value` unless explicitly defined using a property, or, for a top-level script saved as a script bundle, using the Info.plist key `CFBundleIdentifier`. Script Editor’s Bundle Contents drawer includes an “Identifier” field to set this value. |
| `version` | `version` | `version` | `version` | `version` |
|  | Access: | read-only | read-only | read-only |
|  | Class: | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` |
|  | The version of the script object, implicitly defined in AppleScript 2.3 and later. For top-level scripts, its value is `"1.0"` unless explicitly defined using a property, or, for a script bundle, using the Info.plist key `CFBundleShortVersionString`. Script Editor’s Bundle Contents drawer includes a “Short Version” field to set this value. For other script objects, its default value is `missing value`. While the version may resemble a number, it is actually of type `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)`. For best results, compare version strings using `considering numeric strings`. | The version of the script object, implicitly defined in AppleScript 2.3 and later. For top-level scripts, its value is `"1.0"` unless explicitly defined using a property, or, for a script bundle, using the Info.plist key `CFBundleShortVersionString`. Script Editor’s Bundle Contents drawer includes a “Short Version” field to set this value. For other script objects, its default value is `missing value`. While the version may resemble a number, it is actually of type `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)`. For best results, compare version strings using `considering numeric strings`. | The version of the script object, implicitly defined in AppleScript 2.3 and later. For top-level scripts, its value is `"1.0"` unless explicitly defined using a property, or, for a script bundle, using the Info.plist key `CFBundleShortVersionString`. Script Editor’s Bundle Contents drawer includes a “Short Version” field to set this value. For other script objects, its default value is `missing value`. While the version may resemble a number, it is actually of type `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)`. For best results, compare version strings using `considering numeric strings`. | The version of the script object, implicitly defined in AppleScript 2.3 and later. For top-level scripts, its value is `"1.0"` unless explicitly defined using a property, or, for a script bundle, using the Info.plist key `CFBundleShortVersionString`. Script Editor’s Bundle Contents drawer includes a “Short Version” field to set this value. For other script objects, its default value is `missing value`. While the version may resemble a number, it is actually of type `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)`. For best results, compare version strings using `considering numeric strings`. |

##### Commands Handled

You can copy a `script` object with the `[copy](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgm)` command or create a reference to it with the `[set](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgi)` command.

##### Coercions Supported

AppleScript supports coercion of a `script` object to a single-item `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)`.

##### Examples

The following example shows a simple `script` object that displays a dialog. It is followed by a statement that shows how to run the script:

```
script helloScript
    display dialog "Hello."
end script

run helloScript -- invoke the script
```

```
Discussion
A
script
object can contain other
script
objects, called child scripts, and can have a parent object. For additional information, including more detailed examples, see
Script Objects
.
The
name
,
id
, and
version
properties are automatically defined in OS X Mavericks v10.9 (AppleScript 2.3) and later, and are used to identify scripts used as libraries, as described in
Script Objects
.
```

text

An ordered series of Unicode characters.

Starting in AppleScript 2.0, AppleScript is entirely Unicode-based. There is no longer a distinction between Unicode and non-Unicode text. Comments and text constants in scripts may contain any Unicode characters, and all text processing is done in Unicode, so all characters are preserved correctly regardless of the user’s language preferences.

For example, the following script works correctly in AppleScript 2.0, where it would not have in previous versions:

```
set jp to "日本語"
set ru to "Русский"
jp & " and " & ru -- returns "日本語 and Русский"
```

For information on compatibility with previous AppleScript versions, including the use of `string` and `Unicode text` as synonyms for `text`, see the Special Considerations section.

##### Properties of text objects

| `class` | `class` | `class` | `class` | `class` |
|  | Access: | read-only | read-only | read-only |
|  | Class: | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` | `[class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2givceoqq)` |
|  | The class identifier for the object. The value of this property is always `text`. | The class identifier for the object. The value of this property is always `text`. | The class identifier for the object. The value of this property is always `text`. | The class identifier for the object. The value of this property is always `text`. |
| `id` | `id` | `id` | `id` | `id` |
|  | Access: | read-only | read-only | read-only |
|  | Class: | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` or `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` of integer | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` or `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` of integer | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` or `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` of integer |
|  | A value (or list of values) representing the Unicode code point (or code points) for the character (or characters) in the `text` object. (A _Unicode code point_ is a unique number that represents a character and allows it to be represented in an abstract way, independent of how it is rendered. A character in a `text` object may be composed of one or more code points.) | A value (or list of values) representing the Unicode code point (or code points) for the character (or characters) in the `text` object. (A _Unicode code point_ is a unique number that represents a character and allows it to be represented in an abstract way, independent of how it is rendered. A character in a `text` object may be composed of one or more code points.) | A value (or list of values) representing the Unicode code point (or code points) for the character (or characters) in the `text` object. (A _Unicode code point_ is a unique number that represents a character and allows it to be represented in an abstract way, independent of how it is rendered. A character in a `text` object may be composed of one or more code points.) | A value (or list of values) representing the Unicode code point (or code points) for the character (or characters) in the `text` object. (A _Unicode code point_ is a unique number that represents a character and allows it to be represented in an abstract way, independent of how it is rendered. A character in a `text` object may be composed of one or more code points.) |
|  | This property, added in AppleScript 2.0, can also be used as an address, which allows mapping between Unicode code point values and the characters at those code points. For example, `id of "A"` returns `65`, and `character id 65` returns `"A"`. | This property, added in AppleScript 2.0, can also be used as an address, which allows mapping between Unicode code point values and the characters at those code points. For example, `id of "A"` returns `65`, and `character id 65` returns `"A"`. | This property, added in AppleScript 2.0, can also be used as an address, which allows mapping between Unicode code point values and the characters at those code points. For example, `id of "A"` returns `65`, and `character id 65` returns `"A"`. | This property, added in AppleScript 2.0, can also be used as an address, which allows mapping between Unicode code point values and the characters at those code points. For example, `id of "A"` returns `65`, and `character id 65` returns `"A"`. |
|  | The id of text longer than one code point is a list of integers, and vice versa: for example, `id of "hello"` returns `{104, 101, 108, 108, 111}`, and `string id {104, 101, 108, 108, 111}` returns `"hello"`. (Because of a bug, `text id ...` does not work; you must use one of `string`, `Unicode text`, or `character`.) | The id of text longer than one code point is a list of integers, and vice versa: for example, `id of "hello"` returns `{104, 101, 108, 108, 111}`, and `string id {104, 101, 108, 108, 111}` returns `"hello"`. (Because of a bug, `text id ...` does not work; you must use one of `string`, `Unicode text`, or `character`.) | The id of text longer than one code point is a list of integers, and vice versa: for example, `id of "hello"` returns `{104, 101, 108, 108, 111}`, and `string id {104, 101, 108, 108, 111}` returns `"hello"`. (Because of a bug, `text id ...` does not work; you must use one of `string`, `Unicode text`, or `character`.) | The id of text longer than one code point is a list of integers, and vice versa: for example, `id of "hello"` returns `{104, 101, 108, 108, 111}`, and `string id {104, 101, 108, 108, 111}` returns `"hello"`. (Because of a bug, `text id ...` does not work; you must use one of `string`, `Unicode text`, or `character`.) |
|  | These uses of the `id` property obsolete the older `[ASCII character](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzsge)` and `[ASCII number](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzsgi)` commands, since, unlike those, they cover the full Unicode character range and will return the same results regardless of the user's language preferences. | These uses of the `id` property obsolete the older `[ASCII character](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzsge)` and `[ASCII number](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzsgi)` commands, since, unlike those, they cover the full Unicode character range and will return the same results regardless of the user's language preferences. | These uses of the `id` property obsolete the older `[ASCII character](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzsge)` and `[ASCII number](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzsgi)` commands, since, unlike those, they cover the full Unicode character range and will return the same results regardless of the user's language preferences. | These uses of the `id` property obsolete the older `[ASCII character](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzsge)` and `[ASCII number](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzsgi)` commands, since, unlike those, they cover the full Unicode character range and will return the same results regardless of the user's language preferences. |
| `length` | `length` | `length` | `length` | `length` |
|  | Access: | read only | read only | read only |
|  | Class: | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` | `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` |
|  | The number of characters in the text. | The number of characters in the text. | The number of characters in the text. | The number of characters in the text. |
| `quoted form` | `quoted form` | `quoted form` | `quoted form` | `quoted form` |
|  | Access: | read only | read only | read only |
|  | Class: | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` | `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` |
|  | A representation of the text that is safe from further interpretation by the shell, no matter what its contents are. Mainly useful for passing a text string to the `[do shell script](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzuga)` command. | A representation of the text that is safe from further interpretation by the shell, no matter what its contents are. Mainly useful for passing a text string to the `[do shell script](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzuga)` command. | A representation of the text that is safe from further interpretation by the shell, no matter what its contents are. Mainly useful for passing a text string to the `[do shell script](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzuga)` command. | A representation of the text that is safe from further interpretation by the shell, no matter what its contents are. Mainly useful for passing a text string to the `[do shell script](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzuga)` command. |

##### Elements of text objects

A `text` object can contain these elements (which may behave differently than similar elements used in applications):

| `character` | `character` | `character` | `character` | `character` |
|  | Specify by: | [Arbitrary](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbegskkivcuqri), [Every](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizeussa), [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq), [Middle](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizceeqi), [Range](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2iirfeusq) | [Arbitrary](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbegskkivcuqri), [Every](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizeussa), [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq), [Middle](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizceeqi), [Range](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2iirfeusq) | [Arbitrary](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbegskkivcuqri), [Every](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizeussa), [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq), [Middle](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizceeqi), [Range](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2iirfeusq) |
|  |  One or more Unicode characters that make up the text.  Starting in AppleScript 2.0, elements of `text` object count a combining character cluster (also known as a Unicode grapheme cluster) as a single character. (This relates to a feature of Unicode that is unlikely to have an impact on most scripters: some “characters” may be represented as either a single entity or as a base character plus a series of combining marks.  For example, “é” may be encoded as either U+00E9 (LATIN SMALL LETTER E WITH ACUTE) or as U+0065 (LATIN SMALL LETTER E), U+0301 (COMBINING ACUTE ACCENT). Nonetheless, AppleScript 2.0 will count both as one character, where older versions counted the base character and combining mark separately. |  One or more Unicode characters that make up the text.  Starting in AppleScript 2.0, elements of `text` object count a combining character cluster (also known as a Unicode grapheme cluster) as a single character. (This relates to a feature of Unicode that is unlikely to have an impact on most scripters: some “characters” may be represented as either a single entity or as a base character plus a series of combining marks.  For example, “é” may be encoded as either U+00E9 (LATIN SMALL LETTER E WITH ACUTE) or as U+0065 (LATIN SMALL LETTER E), U+0301 (COMBINING ACUTE ACCENT). Nonetheless, AppleScript 2.0 will count both as one character, where older versions counted the base character and combining mark separately. |  One or more Unicode characters that make up the text.  Starting in AppleScript 2.0, elements of `text` object count a combining character cluster (also known as a Unicode grapheme cluster) as a single character. (This relates to a feature of Unicode that is unlikely to have an impact on most scripters: some “characters” may be represented as either a single entity or as a base character plus a series of combining marks.  For example, “é” may be encoded as either U+00E9 (LATIN SMALL LETTER E WITH ACUTE) or as U+0065 (LATIN SMALL LETTER E), U+0301 (COMBINING ACUTE ACCENT). Nonetheless, AppleScript 2.0 will count both as one character, where older versions counted the base character and combining mark separately. |  One or more Unicode characters that make up the text.  Starting in AppleScript 2.0, elements of `text` object count a combining character cluster (also known as a Unicode grapheme cluster) as a single character. (This relates to a feature of Unicode that is unlikely to have an impact on most scripters: some “characters” may be represented as either a single entity or as a base character plus a series of combining marks.  For example, “é” may be encoded as either U+00E9 (LATIN SMALL LETTER E WITH ACUTE) or as U+0065 (LATIN SMALL LETTER E), U+0301 (COMBINING ACUTE ACCENT). Nonetheless, AppleScript 2.0 will count both as one character, where older versions counted the base character and combining mark separately. |
| `paragraph` | `paragraph` | `paragraph` | `paragraph` | `paragraph` |
|  | Specify by: | [Arbitrary](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbegskkivcuqri), [Every](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizeussa), [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq), [Middle](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizceeqi), [Range](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2iirfeusq) | [Arbitrary](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbegskkivcuqri), [Every](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizeussa), [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq), [Middle](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizceeqi), [Range](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2iirfeusq) | [Arbitrary](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbegskkivcuqri), [Every](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizeussa), [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq), [Middle](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizceeqi), [Range](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2iirfeusq) |
|  |  A series of characters beginning immediately after either the first character after the end of the preceding paragraph or the beginning of the text and ending with either a carriage return character (`\r`), a linefeed character (`\n`), a return/linefeed pair (`\r\n`), or the end of the text. The Unicode "paragraph separator" character (U+2029) is not supported.  Because `paragraph` elements are _separated_ by a carriage return, linefeed, or carriage return/linefeed pair, text ending with a paragraph break specifies a following (empty) paragraph. For example, `"this\nthat\n"` has three paragraphs, not two: "this", "that", and "" (the empty paragraph after the trailing linefeed).  Similarly, two paragraph breaks in a row specify an empty paragraph between them:  `paragraphs of "this\n\nthat" --result: {"this", "", "that"}` |  A series of characters beginning immediately after either the first character after the end of the preceding paragraph or the beginning of the text and ending with either a carriage return character (`\r`), a linefeed character (`\n`), a return/linefeed pair (`\r\n`), or the end of the text. The Unicode "paragraph separator" character (U+2029) is not supported.  Because `paragraph` elements are _separated_ by a carriage return, linefeed, or carriage return/linefeed pair, text ending with a paragraph break specifies a following (empty) paragraph. For example, `"this\nthat\n"` has three paragraphs, not two: "this", "that", and "" (the empty paragraph after the trailing linefeed).  Similarly, two paragraph breaks in a row specify an empty paragraph between them:  `paragraphs of "this\n\nthat" --result: {"this", "", "that"}` |  A series of characters beginning immediately after either the first character after the end of the preceding paragraph or the beginning of the text and ending with either a carriage return character (`\r`), a linefeed character (`\n`), a return/linefeed pair (`\r\n`), or the end of the text. The Unicode "paragraph separator" character (U+2029) is not supported.  Because `paragraph` elements are _separated_ by a carriage return, linefeed, or carriage return/linefeed pair, text ending with a paragraph break specifies a following (empty) paragraph. For example, `"this\nthat\n"` has three paragraphs, not two: "this", "that", and "" (the empty paragraph after the trailing linefeed).  Similarly, two paragraph breaks in a row specify an empty paragraph between them:  `paragraphs of "this\n\nthat" --result: {"this", "", "that"}` |  A series of characters beginning immediately after either the first character after the end of the preceding paragraph or the beginning of the text and ending with either a carriage return character (`\r`), a linefeed character (`\n`), a return/linefeed pair (`\r\n`), or the end of the text. The Unicode "paragraph separator" character (U+2029) is not supported.  Because `paragraph` elements are _separated_ by a carriage return, linefeed, or carriage return/linefeed pair, text ending with a paragraph break specifies a following (empty) paragraph. For example, `"this\nthat\n"` has three paragraphs, not two: "this", "that", and "" (the empty paragraph after the trailing linefeed).  Similarly, two paragraph breaks in a row specify an empty paragraph between them:  `paragraphs of "this\n\nthat" --result: {"this", "", "that"}` |
| `text` | `text` | `text` | `text` | `text` |
|  | Specify by: | [Every](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizeussa), [Name](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2jijaucsq) | [Every](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizeussa), [Name](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2jijaucsq) | [Every](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizeussa), [Name](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2jijaucsq) |
|  |  All of the text contained in the `text` object, including spaces, tabs, and all other characters.  You can use `text` to access contiguous characters (but see also the Discussion section below):  `text 1 thru 5 of "Bring me the mouse." --result: "Bring"` |  All of the text contained in the `text` object, including spaces, tabs, and all other characters.  You can use `text` to access contiguous characters (but see also the Discussion section below):  `text 1 thru 5 of "Bring me the mouse." --result: "Bring"` |  All of the text contained in the `text` object, including spaces, tabs, and all other characters.  You can use `text` to access contiguous characters (but see also the Discussion section below):  `text 1 thru 5 of "Bring me the mouse." --result: "Bring"` |  All of the text contained in the `text` object, including spaces, tabs, and all other characters.  You can use `text` to access contiguous characters (but see also the Discussion section below):  `text 1 thru 5 of "Bring me the mouse." --result: "Bring"` |
| `word` | `word` | `word` | `word` | `word` |
|  | Specify by: | [Arbitrary](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbegskkivcuqri), [Every](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizeussa), [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq), [Middle](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizceeqi), [Range](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2iirfeusq) | [Arbitrary](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbegskkivcuqri), [Every](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizeussa), [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq), [Middle](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizceeqi), [Range](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2iirfeusq) | [Arbitrary](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbegskkivcuqri), [Every](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizeussa), [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq), [Middle](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizceeqi), [Range](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2iirfeusq) |
|  |  A continuous series of characters, with word elements parsed according to the word-break rules set in the International preference pane.  Because the rules for parsing words are thus under user control, your scripts should not count on a deterministic text parsing of words. |  A continuous series of characters, with word elements parsed according to the word-break rules set in the International preference pane.  Because the rules for parsing words are thus under user control, your scripts should not count on a deterministic text parsing of words. |  A continuous series of characters, with word elements parsed according to the word-break rules set in the International preference pane.  Because the rules for parsing words are thus under user control, your scripts should not count on a deterministic text parsing of words. |  A continuous series of characters, with word elements parsed according to the word-break rules set in the International preference pane.  Because the rules for parsing words are thus under user control, your scripts should not count on a deterministic text parsing of words. |

##### Operators

The operators that can have `text` objects as operands are `&`, `=`, `≠`, `>`, `≥`, `<`, `≤`, `starts with`, `ends with`, `contains`, `is contained by`, and `as`.

In text comparisons, you can specify whether white space should be considered or ignored. For more information, see `[considering and ignoring Statements](ASLR_control_statements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytgmbsgi2a)`.

For detailed explanations and examples of how AppleScript operators treat `text` objects, see [Operators Reference](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfuytenbqg4ya).

##### Special String Characters

The backslash (`\`) and double-quote (`"`) characters have special meaning in text. AppleScript encloses text in double-quote characters and uses the backslash character to represent return (`\r`), tab (`\t`), and linefeed (\n) characters (described below). So if you want to include an actual backslash or double-quote character in a `text` object, you must use the equivalent two-character sequence. As a convenience, AppleScript also provides the text constant `quote`, which has the value `\"`. 

__Table 6-1__  Special characters in text

| Character | To insert in text |
| Backslash character (`\`) | `\\` |
| Double quote (`"`) | `\"`  `quote` (text constant) |

To declare a `text` object that looks like this when displayed:

```
He said "Use the '\' character."
```

you can use the following:

```
"He said \"Use the '\\' character.\""
```

White space refers to text characters that display as vertical or horizontal space. AppleScript defines the white space  constants `return`, `linefeed`, `space`, and `tab` to represent, respectively, a return character, a linefeed character, a space character, and a tab character. (The `linefeed` constant became available in AppleScript 2.0.)

Although you effectively use these values as text constants, they are actually defined as properties of the global constant `AppleScript`.

__Table 6-2__  White space constants

| Constant | Value |
| space | " " |
| tab | "\t" |
| return | "\r" |
| linefeed | "\n” |

To enter white space in a string, you can just type the character—that is, you can press the Space bar to insert a space, the Tab key to insert a tab character, or the Return key to insert a return. In the latter case, the string will appear on two lines in the script, like the following:

```
display dialog "Hello" & "
" & "Goodbye"
```

When you run this script, "Hello" appears above “Goodbye” in the dialog.

You can also enter a tab, return, or linefeed with the equivalent two-character sequences. When a `text` object containing any of the two-character sequences is displayed to the user, the sequences are converted. For example, if you use the following `text` object in a `[display dialog](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzrgi)` command:

```
display dialog "item 1\t1\ritem 2\t2"
```

it is displayed like this (unless you enable “Escape tabs and line breaks in strings” in the Editing tab of the of Script Editor preferences):

```
item 1      1
item 2      2
```

To use the white space constants, you use the concatenation operator to join multiple `text` objects together, as in the following example:

```
"Year" & tab & tab & "Units sold" & return & "2006" & tab ¬
    & tab & "300" & return & "2007" & tab & tab & "453"
```

When passed to `display dialog`, this text is displayed as follows:

```
Year       Units sold
2006            300
2007            453
```


##### Coercions Supported

AppleScript supports coercion of an `text` object to a single-item `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)`. If a `text` object represents an appropriate number, AppleScript supports coercion of the `text` object to an integer or a real number.

##### Examples

You can define a `text` object in a script by surrounding text characters with quotation marks, as in these examples:

```
set theObject to "some text"
set clientName to "Mr. Smith"
display dialog "This is a text object."
```

Suppose you use the following statement to obtain a `text` object named `docText` that contains all the text extracted from a particular document:

```
set docText to text of document "MyFavoriteFish.rtf" of application "TextEdit"
```

The following statements show various ways to work with the `text` object `docText`:

```
class of docText --result: text
first character of docText --result: a character
every paragraph of docText --result: a list containing all paragraphs
paragraphs 2 thru 3 of docText --result: a list containing two paragraphs
```

The next example prepares a `text` object to use with the `display dialog` command. It uses the `quote` constant to insert `\"` into the text. When this text is displayed in the dialog (above a text entry field), it looks like this: `Enter the text in quotes ("text in quotes"):`

```
set promptString to "Enter the text in quotes (" & quote ¬
    & "text in quotes" & quote & "): "
display dialog promptString default answer ""
```

The following example gets a POSIX path to a chosen folder and uses the `quoted form` property to ensure correct quoting of the resulting string for use with shell commands:

```
set folderName to quoted form of POSIX path of (choose folder)
```

Suppose that you choose the folder named `iWork '08` in your `Applications` folder. The previous statement would return the following result, which properly handles the embedded single quote and space characters in the folder name:

```
"'/Applications/iWork '\\''08/'"
```

```
Discussion
To get a contiguous range of characters within a
text
object, use the
text
element. For example, the value of the following statement is the
text
object
"y thi"
:
get text 3 thru 7 of "Try this at home"
--result: "y thi"
The result of a similar statement using the character element instead of the text element is a list:
get characters 3 thru 7 of "Try this at home"
--result: {"y", " ", "t", "h", "i"}
You cannot set the value of an element of a
text
object. For example, if you attempt to change the value of the first character of the text object
myName
as shown next, you’ll get an error:
set myName to "Boris"
set character 1 of myName to "D"
--result: error: you cannot set the values of elements of text objects
However, you can achieve the same result by getting the last four characters and concatenating them with "D":
set myName to "boris"
set myName to "D" & (get text 2 through 5 of myName)
--result: "Doris"
This example doesn’t actually modify the existing
text
object—it sets the variable
myName
to refer to a new
text
object with a different value.
```

```
Special Considerations
For compatibility with versions prior to AppleScript 2.0,
string
and
Unicode text
are still defined, but are considered synonyms for
text
. For example, all three of these statements have the same effect:
someObject as text
someObject as string
someObject as Unicode text
In addition,
text
,
string
, and
Unicode text
will all compare as equal. For example,
class of "foo" is string
is
true
, even though
class of "foo"
returns
text
. However, it is still possible for applications to distinguish between the three different types, even though AppleScript itself does not.
Starting with AppleScript 2.0, there is no style information stored with
text
objects.
Because all text is Unicode text, scripts now always get the Unicode text behavior. This may be different from the former
string
behavior for some locale-dependent operations, in particular
word
elements. To get the same behavior with 2.0 and pre-2.0, add an explicit
as Unicode text
coercion, for example,
words of (someText as Unicode text)
.
Because
text item delimiters
(described in
text item delimiters
) respect
considering
and
ignoring
attributes in AppleScript 2.0, delimiters are case-insensitive by default. Formerly, they were always case-sensitive. To enforce the previous behavior, add an explicit
considering case
statement.
Because AppleScript 2.0 scripts store all text as Unicode, any text constants count as a use of the former
Unicode text
class, which will work with any version of AppleScript back to version 1.3. A script that contains Unicode-only characters such as Arabic or Thai will run, but will not be correctly editable using versions prior to AppleScript 2.0: the Unicode-only characters will be lost.
```

unit types

Used for working with measurements of length, area, cubic and liquid volume, mass, and temperature.

The unit type classes support simple objects that do not contain other values and have only a single property, the `class` property.

##### Properties of unit type objects

| `class` | `class` | `class` | `class` | `class` |
|  | Access: | read only | read only | read only |
|  | Class: | (varies; listed below) | (varies; listed below) | (varies; listed below) |
|  | The class identifier for the object. These are the available classes: | The class identifier for the object. These are the available classes: | The class identifier for the object. These are the available classes: | The class identifier for the object. These are the available classes: |
|  | _Length:_ `centimetres`, `centimeters`, `feet`, `inches`, `kilometres`, `kilometers`, `metres`, `meters`, `miles`, `yards` | _Length:_ `centimetres`, `centimeters`, `feet`, `inches`, `kilometres`, `kilometers`, `metres`, `meters`, `miles`, `yards` | _Length:_ `centimetres`, `centimeters`, `feet`, `inches`, `kilometres`, `kilometers`, `metres`, `meters`, `miles`, `yards` | _Length:_ `centimetres`, `centimeters`, `feet`, `inches`, `kilometres`, `kilometers`, `metres`, `meters`, `miles`, `yards` |
|  | _Area:_ `square feet`, `square kilometres`, `square kilometers`, `square metres`, `square meters`, `square miles`, `square yards` | _Area:_ `square feet`, `square kilometres`, `square kilometers`, `square metres`, `square meters`, `square miles`, `square yards` | _Area:_ `square feet`, `square kilometres`, `square kilometers`, `square metres`, `square meters`, `square miles`, `square yards` | _Area:_ `square feet`, `square kilometres`, `square kilometers`, `square metres`, `square meters`, `square miles`, `square yards` |
|  | _Cubic volume:_ `cubic centimetres`, `cubic centimeters`, `cubic feet`, `cubic inches`, `cubic metres`, `cubic meters`, `cubic yards` | _Cubic volume:_ `cubic centimetres`, `cubic centimeters`, `cubic feet`, `cubic inches`, `cubic metres`, `cubic meters`, `cubic yards` | _Cubic volume:_ `cubic centimetres`, `cubic centimeters`, `cubic feet`, `cubic inches`, `cubic metres`, `cubic meters`, `cubic yards` | _Cubic volume:_ `cubic centimetres`, `cubic centimeters`, `cubic feet`, `cubic inches`, `cubic metres`, `cubic meters`, `cubic yards` |
|  | _Liquid volume:_ `gallons`, `litres`, `liters`, `quarts` | _Liquid volume:_ `gallons`, `litres`, `liters`, `quarts` | _Liquid volume:_ `gallons`, `litres`, `liters`, `quarts` | _Liquid volume:_ `gallons`, `litres`, `liters`, `quarts` |
|  | _Weight:_ `grams`, `kilograms`, `ounces`, `pounds` | _Weight:_ `grams`, `kilograms`, `ounces`, `pounds` | _Weight:_ `grams`, `kilograms`, `ounces`, `pounds` | _Weight:_ `grams`, `kilograms`, `ounces`, `pounds` |
|  | _Temperature:_ `degrees Celsius`, `degrees Fahrenheit`, `degrees Kelvin` | _Temperature:_ `degrees Celsius`, `degrees Fahrenheit`, `degrees Kelvin` | _Temperature:_ `degrees Celsius`, `degrees Fahrenheit`, `degrees Kelvin` | _Temperature:_ `degrees Celsius`, `degrees Fahrenheit`, `degrees Kelvin` |

##### Operators

None. You must explicitly coerce a unit type to a number type before you can perform operations with it.

##### Coercions Supported

You can coerce a unit type object to `[integer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)`, single-item `[list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)`, `[real](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2kivbukqy)`, or `[text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)`. You can also coerce between unit types in the same category, such as `inches` to `kilometers` (length) or `gallons` to `liters` (liquid volume). As you would expect, there is no coercion between categories, such as from `gallons` to `degrees Centigrade`.

##### Examples

The following statements calculate the area of a circle with a radius of 7 yards, then coerce the area to square feet:

```
set circleArea to (pi * 7 * 7) as square yards --result: square yards 153.9380400259
circleArea as square feet --result: square feet 1385.4423602331
```

The following statements set a variable to a value of 5.0 square kilometers, then coerce it to various other units of area:

```
set theArea to 5.0 as square kilometers --result: square kilometers 5.0
theArea as square miles --result: square miles 1.930510792712
theArea as square meters --result: square meters 5.0E+6
```

However, you cannot coerce an area measurement to a unit type in a different
category:

```
set theArea to 5.0 as square meters --result: square meters 5.0
theArea as cubic meters --result: error
theArea as degrees Celsius --result: error
```

The following statements demonstrate coercion of a unit type to a `text` object:

```
set myPounds to 2.2 as pounds --result: pounds 2.2
set textValue to myPounds as text --result: "2.2"
```

[Next](Commands%20Reference.md)[Previous](About%20Handlers.md)

