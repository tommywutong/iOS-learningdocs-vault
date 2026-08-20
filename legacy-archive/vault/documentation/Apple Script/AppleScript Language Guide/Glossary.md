---
title: AppleScript Language Guide
apple_id: TP40000983
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-01-25'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_glossary.html
archived_at: '2026-07-15T05:19:32.603612Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Language Guide](Introduction%20to%20AppleScript%20Language%20Guide.md)


[Next](Index.md)[Previous](Document%20Revision%20History.md)

# Glossary

- __absolute object specifier__

  An object specifier that has enough information to identify an object or objects uniquely. For an object specifier to an application object to be complete, its outermost container must be the application itself. See [relative object specifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwvgvzzgu).

- 
  __Apple event__

  An interprocess message that encapsulates a command in a form that can be passed across process boundaries, performed, and responded to with a reply event. When an AppleScript script is executed, a statement that targets a scriptable application may result in an Apple event being sent to that application.

- __AppleScript__

  A scripting language that makes possible direct control of scriptable applications and scriptable parts of macOS.

- __AppleScript command__

  A script command provided by AppleScript. AppleScript commands do not have to be included in `tell` statements.

- __application command__

  A command that is defined by scriptable application to provide access to a scriptable feature. An application command must either be included in a `tell` statement or include the name of the application in its direct parameter.

- __application object__

  An object stored in an application or its documents and managed by the application.

- __arbitrary reference form__

  A reference form that specifies an arbitrary object in a container.

- __assignment statement__

  A statement that assigns a value to a variable. Assignment statements use the `copy` or `set` commands.

- __attribute__

  A characteristic that can be considered or ignored in a `considering` or `ignoring` statement.

- __binary operator__

  An operator that derives a new value from a pair of values.

- __boolean__

  A logical truth value; see the `boolean` class.

- __Boolean expression__

  An expression whose value can be either true or false.

- __chevrons__

  See [double angle brackets](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwueqsdizcukscc).

- __child script object__

  A `script` object that inherits properties and handlers from another object, called the parent.

- __class__

  (1) A category for objects that share characteristics such as properties and elements and respond to the same commands. (2) The label for the AppleScript `class` property—a reserved word that specifies the class to which an object belongs.

- __coercion__

  The process of converting an object from one class to another. For example, an integer value can be coerced into a real value. Also, the software that performs such a conversion. Also known as object conversion.

- __command__

  A word or series of words that requests an action. See also [handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwvgvzvgu).

- __comment__

  Text that remains in a script after compilation but is ignored by AppleScript when the script is executed.

- __compile__

  In AppleScript, to convert a script from the form typed into a script editor to a form that can be used by AppleScript. The process of compiling a script includes syntax and vocabulary checks. A script is compiled when you first run it and again when you modify it and then run it again, save it, or check its syntax.

- __compiled script__

  The form to which a script is converted when you compile it.

- __composite value__

  A value that contains other values. Lists, records, and strings are examples of composite values.

- __compound statement__

  A statement that occupies more than one line and contains other statements. A compound statement begins with a reserved word indicating its function and ends with the word `end`. See also [simple statement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwueqsdizbeiqsi).

- __conditional statement__

  See [if statement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwueqsdi5cusrsj).

- __considering statement__

  A control statement that lists a specific set of attributes to be considered when AppleScript performs operations on strings or sends commands to applications.

- __constant__

  A reserved word with a predefined value; see the `constant` class.

- __container__

  An object that contains one or more other objects, known as elements. You specify containers with the reserved words `of` or `in`.

- __continuation character__

  A character used in Script Editor to extend a statement to the next line. With a U.S. keyboard, you can enter this character by typing Option-l (lower-case L).

- __continue statement__

  A statement that controls when and how other statements are executed. AppleScript defines standard control statements such as `if`, `repeat`, and `while`.

- __control statement__

  A statement that causes AppleScript to exit the current handler and transfer execution to the handler with the same name in the parent. A `continue` statement can also be used to invoke an inherited handler in the local context.

- __current application__

  The application that is using the AppleScript component to compile and execute scripts (typically, Script Editor).

- __current script__

  The script currently being executed.

- __current target__

  The object that is the current default target for commands.

- __data__

  A class used for data that do not belong to any of the other AppleScript classes; see the `data` class.

- __date__

  A class that specifies a time, day of the month, month, and year; see the `date` class.

- __declaration__

  The first occurrence of a variable or property identifier in a script. The form and location of the declaration determine how AppleScript treats the identifier in that script—for example, as a property, global variable, or local variable.

- __default target__

  The object that receives a command if no object is specified or if the object is incompletely specified in the command. Default (or implicit) targets are specified in `tell` statements.

- __delegation__

  The handing off of control to another object. In AppleScript, the use of a `continue` statement to call a handler in a parent object or the current application.

- __dialect__

  A version of the AppleScript language that resembles a specific human language or programming language. As of AppleScript 1.3, English is the only dialect supported.

- __dictionary__

  The set of commands, objects, and other terminology that is understood by an application or other scriptable entity. You can display an application’s dictionary with Script Editor.

- __direct parameter__

  The parameter immediately following a command, which typically specifies the object to which the command is sent.

- __double angle brackets__

  Characters («») typically used by AppleScript to enclose raw data. With a U.S. keyboard, you can enter double angle brackets (also known as chevrons) by typing Option-Backslash and Shift-Option-Backslash.

- __element__

  An object contained within another object. An object can typically contain zero or more of each of its elements.

- __empty list__

  A list containing no items. See the `list` class.

- __error expression__

  An expression, usually a `text` object, that describes an error.

- __error handler__

  A collection of statements that are executed in response to an error message. See the `try` statement.

- __error message__

  A message that is supplied by an application, by AppleScript, or by macOS when an error occurs during the handling of a command.

- __error number__

  An integer that identifies an error.

- __evaluation__

  The conversion of an expression to a value.

- __every reference form__

  A reference form that specifies every object of a particular type in a container.

- __exit statement__

  A statement used in the body of a `repeat` statement to exit the Repeat statement.

- __explicit run handler__

  A handler at the top level of a `script` object that begins with `on run` and ends with `end`. A single `script` object can include an explicit `run` handler or an implicit `run` handler, but not both.

- __expression__

  In AppleScript, any series of words that has a value.

- __filter__

  A phrase, added to a reference to a system or application object, that specifies elements in a container that match one or more conditions.

- __filter reference form__

  A reference form that specifies all objects in a container that match a condition specified by a Boolean expression.

- __formal parameter__

  See [parameter variable](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwueqsdjbfeuqsh).

- __global variable__

  A variable that is available anywhere in the script in which it is defined.

- __handler__

  A collection of statements that can be invoked by name. See also [command](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwvgvzrg4).

- __identifier__

  A series of characters that identifies a value or handler in AppleScript. Identifiers are used to name variables, handlers, parameters, properties, and commands.

- __ID reference form__

  A reference form that specifies an object by the value of its ID property.

- __if statement__

  A control statement that contains one or more Boolean expressions whose results determine whether to execute other statements within the `if` statement.

- __ignoring statement__

  A control statement that lists a specific set of attributes to be ignored when AppleScript performs operations on text strings or sends commands to applications.

- __implicit run handler__

  All the statements at the top level of a script except for property definitions, `script` object definitions, and other handlers. A single `script` object can include an explicit `run` handler or an implicit `run` handler, but not both.

- __index reference form__

  A reference form that specifies an object by describing its position with respect to the beginning or end of a container.

- __inheritance__

  The ability of a child `script` object to take on the properties and handlers of a parent object.

- __inheritance chain__

  The hierarchy of objects that AppleScript searches to find the target for a command or the definition of a term.

- __initializing a script object__

  The process of creating a `script` object from the properties and handlers listed in a `script` object definition. AppleScript creates a `script` object when it runs a script or handler that contains a `script` object definition.

- __insertion point__

  A location where another object or objects can be added.

- __integer__

  A positive or negative number without a fractional part; see the `integer` class.

- __item__

  A value in a list or record. An item can be specified by its offset from the beginning or end of the list or record.

- __keyword__

  A word that is part of the AppleScript language. Synonymous with [reserved word](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwvgvzzhe).

- __labeled parameter__

  A parameter that is identified by a label. See also [positional parameter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwueqsdiraukqsf).

- __lifetime__

  The period of time over which a variable or property is in existence.

- __list__

  An ordered collection of values; see the `list` class.

- __literal__

  A value that evaluates to itself.

- __local variable__

  A variable that is available only in the handler in which it is defined. Variables that are defined within handlers are local unless they are explicitly declared as global variables.

- __log statement__

  A script statement that reports the value of one or more variables to the Event Log pane of a script window, and to the Event Log History window, if it is open.

- __loop__

  A series of statements that is repeated.

- __loop variable__

  A variable whose value controls the number of times the statements in a `repeat` statement are executed.

- __middle reference form__

  A reference form that specifies the middle object of a particular class in a container. (This form is rarely used.)

- __name reference form__

  A reference form that specifies an object by name—that is, by the value of its `name` property.

- __nested control statement__

  A control statement that is contained within another control statement.

- __number__

  A synonym for the AppleScript classes `integer` and `real`.

- __object__

  An instantiation of a class definition, which can include properties and actions.

- __object conversion__

  See [coercion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwvgvzvgq).

- __object specifier__

  A phrase specifies the information needed to find another object in terms of the objects in which it is contained. See also [absolute object specifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwvgvzs), [relative object specifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwvgvzzgu), and [reference form](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwvgvzzgq).

- __operand__

  An expression from which an operator derives a value.

- __operation__

  The evaluation of an expression that contains an operator.

- __operator__

  A symbol, word, or phrase that derives a value from another value or pair of values.

- __optional parameter__

  A parameter that need not be included for a command to be successful.

- __outside property, variable, or statement__

  A property, variable, or statement in a `script` object but occurs outside of any handlers or nested `script` objects.

- __parameter variable__

  An identifier in a handler definition that represents the actual value of a parameter when the handler is called. Also called a _formal parameter_.

- __parent object__

  An object from which another `script` object, called the child, inherits properties and handlers. A parent object may be any object, such as a `list` or an `application` object, but it is typically another `script` object.

- __positional parameter__

  A handler parameter that is identified by the order in which it is listed. In a handler call, positional parameters are enclosed in parentheses and separated by commas. They must be listed in the order in which they appear in the corresponding handler definition.

- __property__

  A labeled container in which to store a value. Properties can specify characteristics of objects.

- __property reference form__

  A reference form that specifies a property of an `application` object, `record` or `script` object.

- __range reference form__

  A reference form that specifies a series of objects of the same class in the same container.

- __raw format__

  AppleScript terms enclosed in double angle brackets, or chevrons («»). AppleScript uses raw format because it cannot find a script term in any available dictionary, or cannot display data in its native format.

- __real__

  A number that can include a decimal fraction; see the `real` class.

- __record__

  An unordered collection of properties, identified by unique labels; see the `record` class.

- __recordable application__

  An application that uses Apple events to report user actions for recording purposes. When recording is turned on, Script Editor creates statements corresponding to any significant actions you perform in a recordable application.

- __recursive handler__

  A handler that calls itself.

- __reference__

  An object that encapsulates an object specifier.

- __reference form__

  The syntax for identifying an object or group of objects in an application or other container—that is, the syntax for constructing an object specifier. AppleScript defines reference forms for arbitrary, every, filter, ID, index, middle, name, property, range, and relative.

- __relative object specifier__

  An object specifier that does not include enough information to identify an object or objects uniquely. When AppleScript encounters a partial object specifier, it uses the default object specified in the enclosing `tell` statement to complete the reference. See [absolute object specifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwvgvzs).

- __relative reference form__

  A reference form that specifies an object or location by describing its position in relation to another object, known as the base, in the same container.

- __repeat statement__

  A control statement that contains a series of statements to be repeated and, in most cases, instructions that specify when the repetition stops.

- __required parameter__

  A parameter that must be included for a command to be successful.

- __reserved word__

  A word that is part of the AppleScript language. Synonymous with [keyword](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwvgvzwgy).

- __result__

  A value generated when a command is executed or an expression evaluated.

- __return statement__

  A statement that exits a handler and optionally returns a specified value.

- __scope__

  The range over which AppleScript recognizes a variable or property, which determines where else in a script you may refer to that variable or property.

- __script__

  A series of written instructions that, when executed, cause actions in applications or macOS.

- __scriptable application__

  An application that can be controlled by a script. For AppleScript, that means being responsive to interapplication messages, called Apple events, sent when a script command targets the application.

- __script application__

  An application whose only function is to run the script associated with it.

- __script editor__

  An application used to create and modify scripts.

- __Script Editor__

  The script-editing application distributed with AppleScript.

- __scripting addition__

  A file that provides additional commands or coercions you can use in scripts. If a scripting addition is located in the Scripting Additions folder, its terminology is available for use by any script.

- __scripting addition command__

  A command that is implemented as a scripting addition.

- __script library__

  A script saved in a Script Libraries folder so it can be used by other scripts.

- __script object__

  A user-defined object that can combine data (in the form of properties) and actions (in the form of handlers and additional `script` objects).

- __script object definition__

  A compound statement that contains a collection of properties, handlers, and other AppleScript statements.

- __simple statement__

  One that can be written on a single line. See also [compound statement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwueqsdjfbugski).

- __simple value__

  A value, such as an integer or a constant, that does not contain other values.

- __Standard suite__

  A set of standard AppleScript terminology that a scriptable application should support if possible. The Standard suite contains commands such as `count`, `delete`, `duplicate`, and `make`, and classes such as `application`, `document`, and `window`.

- __statement__

  A series of lexical elements that follows a particular AppleScript syntax. Statements can include keywords, variables, operators, constants, expressions, and so on. See also [compound statement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwueqsdjfbugski), [simple statement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgmwueqsdizbeiqsi).

- __statement block__

  One or more statements enclosed in a compound statement and having an `end` statement.

- __string__

  A synonym for the `text` class.

- __styled text__

  Text that may include style and font information. Not supported in AppleScript 2.0.

- __suite__

  Within an application's scriptability information, a grouping of terms associated with related operations.

- __synonym__

  An AppleScript word, phrase, or language element that has the same meaning as another AppleScript word, phrase, or language element. For example, the operator `does not equal` is a synonym for `≠`.

- __syntax__

  The arrangement of words in an AppleScript statement.

- __syntax description__

  The rules for constructing a valid AppleScript statement of a particular type.

- __system object__

  An object that is part of a scriptable element of macOS.

- __target__

  The recipient of a command. Potential targets include `application` objects, `script` objects (including the current script), and the current application.

- __tell statement__

  A control statement that specifies the default target for the statements it contains.

- __test__

  A Boolean expression that specifies the conditions of a filter or an `if` statement.

- __text__

  An ordered series of characters (a text string); see the `text` class.

- __try statement__

  A two-part compound statement that contains a series of AppleScript statements, followed by an error handler to be invoked if any of those statements cause an error.

- __unary operator__

  An operator that derives a new value from a single value.

- __Unicode__

  An international standard that uses a 16-bit encoding to uniquely specify the characters and symbols for all commonly used languages.

- __Unicode code point__

  A unique number that represents a character and allows it to be represented in an abstract way, independent of how it is rendered.

- __Unicode text__

  A class that represents an ordered series of two-byte Unicode characters.

- __use statement__

  A control statement that declares a required resource for a script and may import terminology from that resource.

- __user-defined command__

  A command that is implemented by a handler defined in a `script` object.

- __using terms from statement__

  A control statement that instructs AppleScript to use the terminology from the specified application in compiling the enclosed statements.

- __variable__

  A named container in which to store a value.

- __with timeout statement__

  A control statement that specifies the amount of time AppleScript waits for application commands to complete before stopping execution of the script.

- __with transaction statement__

  A control statement that allows you to take advantage of applications that support the notion of a transaction—a sequence of related events that should be performed as if they were a single operation, such that either all of the changes are applied or none are.

[Next](Index.md)[Previous](Document%20Revision%20History.md)

