---
title: AppleScript Language Guide
apple_id: TP40000983
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-01-25'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/conceptual/ASLR_lexical_conventions.html
archived_at: '2026-07-15T05:19:31.466915Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Language Guide](Introduction%20to%20AppleScript%20Language%20Guide.md)


[Next](AppleScript%20Fundamentals.md)[Previous](Introduction%20to%20AppleScript%20Language%20Guide.md)

# AppleScript Lexical Conventions

This chapter provides an overview of the vocabulary and conventions of the AppleScript Language. It starts with the character set and introduces elements of increasing complexity.

After reading this chapter, you should have an understanding of the basic language components used to construct AppleScript expressions and statements.

AppleScript Lexical Conventions contains the following sections:

- [Character Set](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzt)
- [Identifiers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzu)
- [Keywords](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzx)
- [Comments](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzy)
- [The Continuation Character](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzz)
- [Literals and Constants](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzrga)
- [Operators](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzrha)
- [Variables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzsgm)
- [Expressions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzsga)
- [Statements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzrg4)
- [Commands](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzw)
- [Results](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzrhe)
- [Raw Codes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzv)

Starting in OS X v10.5 (AppleScript 2.0), the character set for AppleScript is Unicode. AppleScript preserves all characters correctly worldwide, and comments and text constants in scripts may contain any Unicode characters.

AppleScript syntax uses several non-ASCII characters, which can be typed using special key combinations. For information on characters that AppleScript treats specially, see the sections [Identifiers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzu), [Comments](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzy), [Text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzsgy), [The Continuation Character](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzz), and [Raw Codes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzv) in this chapter, as well as [Table 9-1](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfvjvomq) in [Operators Reference](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfuytenbqg4ya).

An AppleScript _identifier_ is a series of characters that identifies a class name, variable, or other language element, such as labels for properties and handlers.

An identifier must begin with a letter and can contain any of these characters:

```
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_
```

Identifiers are not case sensitive. For example, the identifiers `myvariable` and `MyVariable` are equivalent.

AppleScript remembers and enforces the first capitalization it comes across for an identifier. So if it first encounters an identifier as `myAccount`, it will later, during compilation, change versions such as `MyAccount` and `myaccount` to `myAccount`.

The following are examples of valid identifiers: `areaOfCircle`, `Agent007`, `axis_of_rotation`.

The following are not valid identifiers: `C-`, `back&forth`, `999`, `Why^Not`.

AppleScript provides a loophole to the preceding rules: identifiers whose first and last characters are vertical bars (|) can contain any characters. The leading and trailing vertical bars are not considered part of the identifier.

The following are legal identifiers: `|back&forth|`, `|Right*Now!|`.

An identifier can contain additional vertical bars preceded by a backslash (\) character, as in the identifier `|This\|Or\|That|`. Use of the backslash character is described further in the Special String Characters section of the `[text](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` class.

A _keyword_ is a reserved word in the AppleScript language. Keywords consist of lower-case, alphabetic characters: `abcdefghijklmnopqrstuvwxyz`. In a few cases, such as `aside from`, they come in pairs.

Table 1-1 lists the keywords reserved in AppleScript 2.0 (which are the same as those used in AppleScript 1.x). For additional information, see [Table A-1](AppleScript%20Keywords.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgiwvgvzr), which provides a brief description for each keyword and points to related information, where available.

__Table 1-1__  AppleScript reserved words, listed alphabetically

| `about` | `above` | `after` | `against` | `and` | `apart from` |
| `around` | `as` | `aside from` | `at` | `back` | `before` |
| `beginning` | `behind` | `below` | `beneath` | `beside` | `between` |
| `but` | `by` | `considering` | `contain` | `contains` | `contains` |
| `continue` | `copy` | `div` | `does` | `eighth` | `else` |
| `end` | `equal` | `equals` | `error` | `every` | `exit` |
| `false` | `fifth` | `first` | `for` | `fourth` | `from` |
| `front` | `get` | `given` | `global` | `if` | `ignoring` |
| `in` | `instead of` | `into` | `is` | `it` | `its` |
| `last` | `local` | `me` | `middle` | `mod` | `my` |
| `ninth` | `not` | `of` | `on` | `onto` | `or` |
| `out of` | `over` | `prop` | `property` | `put` | `ref` |
| `reference` | `repeat` | `return` | `returning` | `script` | `second` |
| `set` | `seventh` | `since` | `sixth` | `some` | `tell` |
| `tenth` | `that` | `the` | `then` | `third` | `through` |
| `thru` | `timeout` | `times` | `to` | `transaction` | `true` |
| `try` | `until` | `where` | `while` | `whose` | `with` |
| `without` |  |  |  |  |  |

A _comment_ is text that is ignored by AppleScript when a script is executed. You can use comments to describe what is happening in the script or make other kinds of notes. There are three kinds of comments:

- A block comment begins with the characters `(*` and ends with the characters `*)`. Block comments must be placed between other statements. That means they can be placed on the same line at the beginning or end of a statement, but cannot be embedded within a simple (one-line) statement.
- An end-of-line comment begins with the characters `--` (two hyphens) and ends with the end of the line:

```
--end-of-line comments extend to the end of the line
```
- Starting in version 2.0, AppleScript also supports use of the # symbol as an end-of-line comment. This allows you to make a plain AppleScript script into a Unix executable by beginning it with the following line and giving it execute permission:

```
#!/usr/bin/osascript
```

  Compiled scripts that use `#` will run normally on pre-2.0 systems, and if edited will display using `--`. Executable text scripts using `#!/usr/bin/osascript` will not run on pre-2.0 systems, since the `#` will be considered a syntax error.

You can nest comments—that is, comments can contain other comments, as in this example:

```
(*  Here are some
    --nested comments
    (* another comment within a comment *)
*)
```


A simple AppleScript statement must normally be entered on a single line. You can extend a statement to the next line by ending it with the _continuation character_, ¬. With a U.S. keyboard, you can enter this character by typing Option-l (lower-case L). In Script Editor, you can type Option-Return, which inserts the continuation character and moves the insertion point to the next line.

Here is a single statement displayed on two lines:

```
display dialog "This is just a test." buttons {"Great", "OK"} ¬
default button "OK" giving up after 3
```

A continuation character within a quoted text string is treated like any other character.

A _literal_ is a value that evaluates to itself—that is, it is interpreted just as it is written. In AppleScript, for example, `"Hello"` is a text literal. A _constant_ is a word with a predefined value. For example, AppleScript defines a number of enumerated constants for use with the `[path to (folder)](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzrhe)` command, each of which specifies a location for which to obtain the path.

AppleScript defines the Boolean values `true` and `false` and supplies the `[boolean](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jijbeory)` class.

[Global Constants in AppleScript](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawueqkkijcekssj) describes constants that can be used throughout your scripts. For related information, see the `[constant](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2finceqqy)` class.

A list defines an ordered collection of values, known as items, of any class. As depicted in a script, a list consists of a series of expressions contained within braces and separated by commas, such as the following:

```
{1, 7, "Beethoven", 4.5}
```

A list can contain other lists. An empty list (containing no items) is represented by a pair of empty braces: `{}`.

AppleScript provides the `[list](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2eijeesri)` class for working with lists.

A numeric literal is a sequence of digits, possibly including other characters, such as a unary minus sign, period (in reals), or `"E+"` (in exponential notation). The following are some numeric literals:

```
-94596
3.1415
9.9999999999E+10
```

AppleScript defines classes for working with `[real](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2kivbukqy)` and `[integer](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)` values, as well as the `number` class, which serves as a synonym for either `real` or `integer`.

A record is an unordered collection of labeled properties. A record appears in a script as a series of property definitions contained within braces and separated by commas. Each property definition consists of a unique label, a colon, and a value for the property. For example, the following is a record with two properties:

```
{product:"pen", price:2.34}
```


A `text` literal consists of a series of Unicode characters enclosed in a pair of double quote marks, as in the following example:

```
"A basic string."
```

AppleScript `text` objects are instances of the `[text](../reference/ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` class, which provides mechanisms for working with text. The Special String Characters section of that class describes how to use white space, backslash characters, and double quotes in text.

An _operator_ is a symbol, word, or phrase that derives a value from another value or pair of values. For example, the multiplication operator (`*`) multiplies two numeric operands, while the concatenation operator (`&`) joins two objects (such as text strings). The `is equal` operator performs a test on two Boolean values.

For detailed information on AppleScript’s operators, see [Operators Reference](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfuytenbqg4ya).

A _variable_ is a named container in which to store a value. Its name, which you specify when you create the variable, follows the rules described in [Identifiers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzu). You can declare and initialize a variable at the same time with a `[copy](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgm)` or `[set](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgi)` command. For example:

```
set myName to "John"
copy 33 to myAge
```

Statements that assign values to variables are known as _assignment statements_.

When AppleScript encounters a variable, it evaluates the variable by getting its value. A variable is contained in a script and its value is normally lost when you close the script that contains it.

AppleScript variables can hold values of any class. For example, you can assign the integer value `17` to a variable, then later assign the Boolean value `true` to the same variable.

For more information, see [Variables and Properties](Variables%20and%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgmwvgvzrga).

An _expression_ is any series of lexical elements that has a value. Expressions are used in scripts to represent or derive values. The simplest kinds of expressions, called literal expressions, are representations of values in scripts. More complex expressions typically combine literals, variables, operators, and object specifiers.

When you run a script, AppleScript converts its expressions into values. This process is known as _evaluation_. For example, when the following simple expression is evaluated, the result is 21:

```
3 * 7 --result: 21
```

An object specifier specifies some or all of the information needed to find another object. For example, the following object specifier specifies a named document:

```
document named "FavoritesList"
```

For more information, see [Object Specifiers](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzx).

A _statement_ is a series of lexical elements that follows a particular AppleScript syntax. Statements can include keywords, variables, operators, constants, expressions, and so on.

Every script consists of statements. When AppleScript executes a script, it reads the statements in order and carries out their instructions.

A _control statement_ is a statement that determines when and how other statements are executed. AppleScript defines standard control statements such as `if`, `repeat`, and `while` statements, which are described in detail in [Control Statements Reference](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytknztgmza).

 A _simple statement_ is one that can be written on a single line:

```
set averageTemp to 63 as degrees Fahrenheit
```

 A _compound statement_ is written on more than one line, can contain other statements, and has the word `end` (followed, optionally, by the first word of the statement) in its last line. For example the following is a compound `tell` statement:

```
tell application "Finder"
    set savedName to name of front window
    close window savedName
end tell
```

A compound statement can contain other compound statements.

A _command_ is a word or series of words used in an AppleScript statement to request an action. Every command is directed at a _target_, which is the object that responds to the command. The target is usually an application object or an object in macOS, but it can also be a `script` object or a value in the current script.

The following statement uses AppleScript’s `[get](../reference/ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgy)` command to obtain the name of a window; the target is the front window of the Finder application:

```
get name of front window of application "Finder"
```

For more information on command types, parameters, and targets, see [Commands Overview](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzy).

The _result_ of a statement is the value generated, if any, when the statement is executed. For example, executing the statement `3 + 4` results in the value `7`. The result of the statement `set myText to "keyboard"` is the text object `"keyboard"`. A result can be of any class. AppleScript stores the result in the globally available property `result`, described in [AppleScript Constant](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvztha).

When you open, compile, edit, or run scripts with a script editor, you may occasionally see terms enclosed in double angle brackets, or chevrons («»), in a script window or in another window. These terms are called _raw format_ or _raw codes_, because they represent the underlying Apple event codes that AppleScript uses to represent scripting terms.

For compatibility with Asian national encodings, “《” and “》” are allowed as synonyms for “«” and “»” ( (Option- \ and Option-Shift- \, respectively, on a U.S. keyboard), since the latter do not exist in some Asian encodings.

For more information on raw codes, see [Double Angle Brackets](Double%20Angle%20Brackets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsguwvgvzr).

[Next](AppleScript%20Fundamentals.md)[Previous](Introduction%20to%20AppleScript%20Language%20Guide.md)

