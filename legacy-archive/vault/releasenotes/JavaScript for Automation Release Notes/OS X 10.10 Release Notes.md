---
title: JavaScript for Automation Release Notes
apple_id: TP40014508
resource_type: Release Note
platform: macOS
topic: Interapplication Communication
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/InterapplicationCommunication/RN-JavaScriptForAutomation/Articles/OSX10-10.html
archived_at: '2026-07-18T02:58:39.637875Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md) · [JavaScript for Automation Release Notes](Introduction%20to%20JavaScript%20for%20Automation%20Release%20Notes.md)


[Next](Document%20Revision%20History.md)[Previous](OS%20X%2010.11%20Release%20Notes.md)

# OS X 10.10 Release Notes

This article describes JavaScript for Automation, a new feature in OS X Yosemite.

JavaScript for Automation is a host environment for JavaScript that adds the following global properties:

- `Automation`
- `Application`
- `Library`
- `Path`
- `Progress`
- `ObjectSpecifier`
- `delay`
- `console.log`
- `ObjC`
- `Ref`
- `$`

The JavaScript OSA component implements JavaScript for Automation. The component can be used from Script Editor, the system-wide Script menu, the Run JavaScript Automator action, applets, droplets, the `osascript` command-line tool, the [NSUserScriptTask](https://developer.apple.com/documentation/foundation/nsuserscripttask) API, and everywhere else that other OSA components, such as AppleScript, can be used. This includes Mail rules, Folder Actions, Address Book plug-ins, Calendar alarms, and message triggers.

Scripting dictionaries detail the object model of applications. Terminology in scripting dictionaries maps to valid JavaScript identifiers by following a set of conventions. The Script Dictionary viewer in Script Editor has been updated to show terminology in AppleScript, JavaScript, and Objective-C (Scripting Bridge framework) formats. To open a scripting dictionary, launch Script Editor (in `/Applications/Utilities/`) and choose File > Open Dictionary or Window > Library.

Many objects in the JavaScript for Automation host environment refer to external entities, such as other applications, or windows or data inside of those other applications. When you access a JavaScript property of an application object, or of an element of an application object, a new object specifier is returned that refers to the specific property of that object.

You can access an application in a number of ways:

- By name

```
Application('Mail')
```
- By bundle ID

```
Application('com.apple.mail')
```
- By path

```
Application('/Applications/Mail.app')
```
- By process ID

```
Application(763)
```
- On a remote machine

```
Application('eppc://127.0.0.1/Mail')
```
- Accessing the application that is running the script

```
Application.currentApplication()
```


The following examples demonstrate the syntax for interacting with objects in an application:

- Access properties

```
Mail.name
```
- Access elements

```
Mail.outgoingMessages[0]
```
- Call commands

```
Mail.open(...)
```
- Create new objects

```
Mail.OutgoingMessage(...)
```


You access properties of scripting objects as JavaScript properties using _dot notation_. As described above, the returned object is an object specifier—a reference to the accessed property—rather than the actual value. To send the `get` event to the external entity and return its value, call the property as a function:

```
subject = Mail.inbox.messages[0].subject()
```

Similarly, setting a property sends the `set` event to the external entity with the data you want to set.

```
Mail.outgoingMessages[0].subject = 'Hello world'
```

Here is an example showing how to get a property from every element of an array (in this case, the subject of every message in Mail's inbox).

```
subjects = Mail.inbox.messages.subject()
```


You access elements within an array by calling specific element retrieval methods on the array, or by using square brackets and specifying the name or index of the element you want to retrieve. The returned values are object specifiers, with their own properties and elements, that refer to the array elements. They can be accessed by:

- Index

```
window = Mail.windows.at(0)
window = Mail.windows[0]
```
- Name

```
window = Mail.windows.byName('New Message')
window = Mail.windows['New Message']
```
- ID

```
window = Mail.windows.byId(412)
```


To filter arrays, returning only some of the elements, use the `whose` method. Here is the general syntax.

```
someElementArray.whose({...})
```

Pass in an object containing the query's criteria—element property and value to use for filtering. You can use this technique to check for:

- Literal property matches

```
{ name: 'JavaScript for Automation' }
{ name: { _equals: 'JavaScript for Automation' } }
{ name: { '=': 'JavaScript for Automation' } }
```
- Property matches containing a value

```
{ name: { _contains: 'script for Auto' } }
```
- Property matches beginning with a value

```
{ name: { _beginsWith: 'JavaScript' } }
```
- Property matches ending with a value

```
{ name: { _endsWith: 'Automation' } }
```
- Property matches greater than a value

```
{ size: { _greaterThan: 20 } }
{ size: { '>': 20 } }
```
- Property matches greater than or equal to a value

```
{ size: { _greaterThanEquals: 20 } }
{ size: { '>=': 20 } }
```
- Property matches less than a value

```
{ size: { _lessThan: 20 } }
{ size: { '<': 20 } }
```
- Property matches less than or equal to a value

```
{ size: { _lessThanEquals: 20 } }
{ size: { '<=': 20 } }
```
- Subelement property matches

```
{ _match: [ ObjectSpecifier.tabs[0].name, 'Apple' ] }
```

You can also combine queries in order to determine whether multiple criteria evaluate to `true`.

- All criteria evaluate to `true`.

```
{ _and: [
    { name: 'Apple' },
    { size: { '<': 20 } },
]}
```
- At least one of the criteria evaluates to `true`.

```
{ _or: [
    { name: 'Apple' },
    { name: { _contains: 'JavaScript' } },
]}
```
- None of the criteria evaluates to `true`.

```
{ _not: [
    { name: 'Apple' },
    { name: { _contains: 'JavaScript' } },
]}
```

The `_and`, `_or`, and `_not` keys require arrays as their value.

Here is an example of a `whose` clause to find all of the messages in your inbox that contain the word _JavaScript_ or the word _Automation_ in the subject.

```
Mail = Application('Mail')
Mail.inbox.messages.whose({
    _or: [
        { subject: { _contains: "JavaScript" } },
        { subject: { _contains: "Automation" } }
    ]
})
```


Commands are called as functions. Some commands take a direct parameter, which is passed as the first argument to a command. Some commands can take named parameters, accepting an object of keyed values for the named parameters. If the command takes a direct parameter, you pass the object of named parameters as a second argument. If the command has no direct parameter, the object of named parameters is passed as the first and only argument. When the direct parameter is optional, you can pass nothing to the command, or you can pass null as the first parameter if you will pass in named parameters.

- Command with no arguments

```
message.open()
```
- Command with direct parameter

```
Mail.open(message)
```
- Command with named parameters

```
response = message.reply({
    replayAll: true,
    openingWindow: false
})
```
- Command with direct parameter and named parameters

```
Safari.doJavaScript('alert("Hello world")', {
    in: Safari.windows[0].tabs[0]
})
```


You can create new objects by calling class constructors as functions and optionally providing properties and data. When making an object, you must either call the `make` method on the object, or call the `push` method on an application object array for the object to actually be created. Until you call one of these methods, the object doesn't actually exist in the application.

- Create a new object.

```
message = Mail.OutgoingMessage().make()
```
- Create a new object with properties.

```
message = Mail.OutgoingMessage({
    subject: 'Hello world',
    visible: true
})
Mail.outgoingMessages.push(message)
```
- Create a new object with data.

```
para = TextEdit.Paragraph({}, 'Some text')
TextEdit.documents[0].paragraphs.push(para)
```

Once you create a new object in an application (by calling `make` or `push`), you can interact with it like any existing application objects.

```
message = Mail.OutgoingMessage().make()
message.subject = 'Hello world'
```


Use scripting additions (plug-ins for scripts) to enhance the functionality of applications. The OS has a set of standard scripting additions that provide the ability to speak text, display user interaction dialogs, and more. To use them, an application must explicitly set the `includeStandardAdditions` flag to `true`.

```
app = Application.currentApplication()
app.includeStandardAdditions = true
app.say('Hello world')
app.displayDialog('Please enter your email address', {
    withTitle: 'Email',
    defaultAnswer: 'your_email@site.com'
})
```


You can affect how strictly JavaScript for Automation treats application objects when you:

- Look up properties of objects.

```
app.strictPropertyScope = true
```

  If the `Foo` class has a property `bar`, but the `Baz` class does not, the following code will only send the proper event to get the property when `strictPropertyScope` is `false`.

```
app.baz[0].bar()
```
- Look up commands that objects respond to.

```
app.strictCommandScope = true
```

  If the application has a command `foo`, but the `Bar` class does not say it responds to that command, the following code will only send the proper command event when `strictCommandScope` is `false`.

```
app.bar[0].foo()
```
- Check the types of parameters sent in commands.

```
app.strictParameterType = true
```

  For example, System Events has a `keystroke` command that accepts text as its first argument. The application's `strictParameterType` property must be `false` for you to be able to send a number instead of a string.

By default, applications have `strictPropertyScope` and `strictCommandScope` set to `false` and `strictParameterType` set to `true`.

You can pass event modifiers when getting and setting properties, calling commands on objects, creating new objects in applications, and so on. The event modifiers should be passed as the last argument to whatever function you are calling. Here are some examples:

- Call a command with a timeout—the amount of time a script allows for a single event to execute.

```
TextEdit = Application('TextEdit')
doc = TextEdit.documents[0]
doc.close({ saving: 'ask' }, { timeout: 20 })
```
- Call a `whose` method while ignoring case, but considering white space and hyphens.

```
app.documents.whose({
    text: { _contains: 'custom-built automation' }
}, {
    ignoring: 'case',
    considering: ['white space', 'hyphens']
})
```

You can consider or ignore:

- Case
- Diacriticals
- White space
- Hyphens
- Punctuation
- Numeric strings
- Application responses

You can use the `ObjectSpecifier` object to:

- Check whether an object is an object specifier

```
Mail.inbox.messages[0] instanceof ObjectSpecifier == true
```
- Get the class of an object specifier

```
Mail = Application('Mail')
ObjectSpecifier.classOf(Mail.inbox)
```
- Build arbitrary object specifier chains for use in whose clauses

```
firstTabsName = ObjectSpecifier.tabs[0].name
app.windows.whose({
    _match: [firstTabsName, 'Apple']
})
```


When you need to interact with files, such as a document in TextEdit, you will need a `path` object, not just a string with a path in it. You can use the `Path` constructor to instantiate paths.

```
TextEdit = Application('TextEdit')
path = Path('/Users/username/Desktop/foo.rtf')
TextEdit.open(path)
```


You can interact with a script's `Progress` object to affect the UI that details the script's progress. You can set the object’s:

- Total unit count

```
Progress.totalUnitCount = 10
```
- Completed unit count

```
Progress.completedUnitCount = 1
```
- Description

```
Progress.description = 'Processing Files'
```
- Additional description

```
Progress.additionalDescription = 'This may take a little while'
```


To use scripts as libraries, store them in `~/Library/Script Libraries/`.

Suppose you have a script library named `toolbox.scpt`, which contains the following code:

```
function log(message) {
    TextEdit = Application('TextEdit')
    doc = TextEdit.documents['Log.rtf']
    doc.text = message
}
```

Another script can target methods in your library using the following syntax.

```
toolbox = Library('toolbox')
toolbox.log('Hello world')
```


You can make standalone, double-clickable applications (called applets) by writing a script in Script Editor and saving it as an application. Applets support the following event handlers:

- A `run` event handler is called when the applet runs.

```
function run() {...}
```
- An `openDocuments` event handler’s inclusion configures the applet to operate as a droplet. This handler is called when documents are dropped onto the applet.

```
function openDocuments(docs) {...}
```
- A `printDocuments` handler is called when the applet is told to print documents.

```
function printDocuments(docs) {...}
```
- An `idle` handler is called periodically when the script enters an idle period. This handler allows you to do periodic processing.

```
function idle() {...}
```
- A `reopen` handler is called when the applet is reopened.

```
function reopen() {...}
```
- A `quit` handler is called when the applet is quit.

```
function quit() {...}
```


You can automate the user interfaces of applications by scripting the System Events application. Explore the scripting dictionary of System Events in Script Editor—specifically the Processes Suite—to see a list of application interface elements that support this type of automation.

The following example uses UI scripting to create a new note in Notes.

```
Notes = Application('Notes')
Notes.activate()

delay(1)
SystemEvents = Application('System Events')
Notes = SystemEvents.processes['Notes']

Notes.windows[0].splitterGroups[0].groups[1].groups[0].buttons[0].click()
```


JavaScript for Automation has a built-in Objective-C bridge that enables you to access the file system and build Cocoa applications.

The primary access points for the Objective-C bridge are the global properties `ObjC` and `$`.

The symbols from the Foundation framework are available by default in JavaScript for Automation. You can make additional frameworks and libraries available using the `ObjC.import()` method. For example, to use the `NSBeep()` function, which is not present in Foundation, you can import the Cocoa framework.

```
ObjC.import('Cocoa')
$.NSBeep()
```

In addition to system frameworks, functionality from some of the system libraries has been exposed. This functionality can be imported by referring to the name of the header file (without the `.h`) that declares that functionality, such as `arpa/inet`, `asl`, `copyfile`, `dispatch`, `dyld`, `errno`, `getopt`, `glob`, `grp`, `ifaddrs`, `launch`, `membership`, `netdb`, `netinet/in`, `notify`, `objc`, `paths`, `pwd`, `readline`, `removefile`, `signal`, `spawn`, `sqlite3`, `stdio`, `stdlib`, `string`, `sys/fcntl`, `sys/file`, `sys/ioctl`, `sys/mount`, `sys/param`, `sys/resource`, `sys/socket`, `sys/stat`, `sys/sysctl`, `sys/time`, `sys/times`, `sys/types`, `sys/wait`, `sys/xattr`, `syslog`, `time`, `unistd`, `uuid/uuid`, `vImage`, `vecLib`, `vmnet`, `xpc`, and `zlib`.

When you import frameworks, the system consults bridge support files. In addition to built-in frameworks and libraries, you can import any framework that has bridge support by passing the full path to the framework, as in the following example:

```
ObjC.import('/Library/Frameworks/Awesome.framework')
```


The primitive JavaScript data types are mapped to C data types. For example, a JavaScript string maps to `char *`, while a JavaScript integer maps to `int`. When using an ObjC API that returns a `char *`, you'll get a JS string.

Primitive JavaScript data types will be automatically converted to ObjC object types when passed as an argument to an ObjC method that is expecting an object type. For example, a JS string will be converted to an `NSString` object if that is what the method signature says the argument should be typed as.

Note, however, that ObjC object types that are returned by ObjC methods are never automatically converted to primitive JavaScript data types.

All classes are defined as properties of the `$` object. Methods of ObjC objects are invoked in one of two ways, depending on whether the method takes arguments.

If the ObjC method does not take arguments, then you invoke it by accessing the JavaScript property with that name. This example instantiates an empty mutable string.

```
str = $.NSMutableString.alloc.init
```

If the ObjC method does take arguments, then you invoke it by calling the JavaScript method (function-typed property) named according to the JSExport convention; the letter following each ":" is capitalized, and then the ":"s are removed. This example instantiates an `NSString` from a JavaScript string and writes it to a file.

```
str = $.NSString.alloc.initWithUTF8String('foo')
str.writeToFileAtomically('/tmp/foo', true)
```

If you call a method, such as `-intValue`, that returns a C data type rather than an object, then you'll get back a primitive JavaScript data type. This example returns the primitive JavaScript integer, `99`.

```
$.NSNumber.numberWithInt(99).intValue
```


ObjC properties are also accessed through JavaScript properties, similar to how you invoke methods that don’t have arguments.

When a property of a bridged object is accessed, the list of ObjC properties is first consulted, and if a property with that name exists, then the appropriate getter or setter selector for that property is used. If an ObjC property with that name does not exist on the class, then the property name is used as the method selector.

To define a property using a custom getter name, you can use either the property name or the getter name, and get the same result.

```
task = $.NSTask.alloc.init
task.running == task.isRunning
```

Also, unlike argument-less methods, bridged object properties that map to ObjC properties can also be set to (assuming the property is read/write). The following two lines are equivalent because `launchPath` is defined as an ObjC property.

```
task.launchPath = '/bin/sleep'
task.setLaunchPath('/bin/sleep')
```


The `ObjC.wrap()` method can be used convert a primitive JavaScript data type into an ObjC object type, and then wrap that ObjC object in a JavaScript wrapper.

The `ObjC.unwrap()` method can be used to convert a wrapped ObjC object into a primitive JavaScript data type.

The `ObjC.deepUnwrap()` method can be used to recursively convert a wrapped ObjC object into a primitive JavaScript data type.

The `$()` operator is a convenient alias for `ObjC.wrap()`, and is meant to be similar to the `@()` boxing operator in ObjC. For example, `$("foo")` returns a wrapped `NSString` instance, and `$(1)` returns a wrapped `NSNumber` instance.

The `.js` property of wrapped ObjC objects is a convenient alias for `ObjC.unwrap()`. For example, `$("foo").js` returns "foo".

Constants and enums are defined as properties of the `$` object.

```
$.NSNotFound
$.NSFileReadNoSuchFileError
$.NSZeroRect
```


Functions are also defined as properties of the `$` object.

```
$.NSBeep()
$.NSMakeSize(33, 55)
```


When you use functions and methods that accept variadic arguments, every variable argument passed in must be the same type as the last declared parameter. For example, `printf` must receive `%s` arguments after the initial format string.

```
ObjC.import('stdio')
$.printf('%s %s %s', 'JavaScript', 'for', 'Automation')
```

`NSLog` has a final declared parameter type of `%@` and must receive `%@` arguments after the initial format string.

```
$.NSLog('%@ %@ %@', $('JavaScript'), $('for'), $('Automation'))
```

When you create an `NSArray` using `arrayWithObjects`, nil termination is handled for you. Don’t try to terminate it yourself.

```
$.NSArray.arrayWithObjects($('JavaScript'), $('for'), $('Automation'))
```


Structs are represented as generic JavaScript objects, where the struct field names are the property names.

```
$.NSMakeRect(0, 0, 1024, 768)
```

Result: {"origin":{"x":0,"y":0},"size":{"width":1024,"height":768}}

In ObjC, `nil` is a valid message target. Sending a message to a `nil` object returns `nil` again. This behavior is different in JavaScript, which does not allow methods to be called on `undefined`.

To create a JavaScript object that represents `nil`, call the `$()` function with no arguments.

```
nil = $()
```

To determine if a bridged object is actually wrapping a `nil` pointer, you can call the `isNil()` method.

```
if (o.isNil()) { ... }
```


This boxed `nil` can be passed as an argument to an ObjC method that expects an argument passed by reference; the runtime will automatically replace the inner `nil` pointer with the pointer returned by reference.

```
error = $()
fm = $.NSFileManager.defaultManager
fm.attributesOfItemAtPathError('/DOES_NOT_EXIST', error)
if (error.code == $.NSFileReadNoSuchFileError) {
    // ...
}
```


The `Ref` class can be used to pass arguments that ObjC expects to be passed by reference. The referenced value can be retrieved by accessing the `0` property of the `Ref`.

```
function testExplicitPassByReference(path) {
    ref = Ref()
    fm = $.NSFileManager.defaultManager
    exists = fm.fileExistsAtPathIsDirectory(path, ref)
    if (exists) {
        isDirectory = ref[0]
        return (path + ' is ' + (isDirectory ? '' : 'not ') + 'a directory; ')
    }
    else {
        return (path + ' does not exist\n')
    }
}

output = testExplicitPassByReference('/System')
       + testExplicitPassByReference('/mach_kernel')
       + testExplicitPassByReference('/foo')
```

Result: /System is a directory; /mach_kernel is not a directory; /foo does not exist

To access the byte values of `Ref` objects, index them into like arrays.

```
ref = Ref('id*')
ref[0] = $('foo')
if (ref[0] == $('foo')) { ... }
```

When you need to pass an opaque pointer and check whether you got that opaque pointer back, you instantiate a void `Ref` and use the `equals` method.

```
CONTEXT = Ref('void')

ObjC.registerSubclass({
    name: 'MyObject',
    properties: { foo: 'id' },
    methods: {
        'startObserving': {
            types: ['void', []],
            implementation: function (obj) {
                this.addObserverForKeyPathOptionsContext(
                    this,
                    'foo',
                    ($.NSKeyValueObservingOptionNew | $.NSKeyValueObservingOptionOld),
                    CONTEXT
                );
            },
        },
        'observeValueForKeyPath:ofObject:change:context:': {
            types: ['void', ['id', 'id', 'id', 'void *']],
            implementation: function(keyPath, observedObject, change, context) {
                $.NSLog(Automation.getDisplayString(Ref.equals(context, CONTEXT)))
            }
        }
    }
})
```


When frameworks are imported, only the C functions specified in the bridge support files are made available. To access other C functions that are linked into the host application, a script may bind them into the JavaScript environment. Call the `bindFunction()` method and specify the return and argument types of the function.

```
ObjC.bindFunction('pow', ['double', ['double', 'double']])
$.pow(2,10)
```

Result: 1024

Here are some of the allowed strings for specifying types of properties, method and function arguments, and return values: `void`, `bool`, `float`, `double`, `unsigned char`, `char`, `unsigned short`, `short`, `unsigned int`, `int`, `unsigned long`, `long`, `long double`, `class`, `selector`, `string`, `pointer`, `block`, `function`, and `id`.

Subclasses of Objective-C objects can be registered from JavaScript.

```
ObjC.registerSubclass({
    name: 'AppDelegate',
    superclass: 'NSObject',
    protocols: ['NSApplicationDelegate'],
    properties: {
        window: 'id'
    },
    methods: {
        'applicationDidFinishLaunching:': function (notification) {
            $.NSLog('Application finished launching');
        }
    }
})
```

If no superclass is given, the object will implicitly subclass `NSObject`. When you override a method, specifying the method types is optional, but if the types are present, they must match those of the superclass's method.

Here is an example of a custom `init` method and a custom method with its types declared.

```
ObjC.registerSubclass({
    name: 'MyClass',
    properties: {
        foo: 'id'
    },
    methods: {
        init: function () {
            var _this = ObjC.super(this).init;
            if (_this != undefined) {
                _this.foo = 'bar'
            }
            return _this
        },
        baz: {
            types: ['void', []],
            implementation: function () {
                this.foo = 'quux'
            }
        }
    }
})
```


The `Automation` object has a `getDisplayString` method that allows you to pass in an object and print it as source text or a human-readable display string.

```
foo = $('bar')
Automation.getDisplayString(foo)
```

Passing in `true` as the second parameter to `getDisplayString` will print the object as a display string instead of source text.

```
Automation.getDisplayString(foo, true)
```

[Next](Document%20Revision%20History.md)[Previous](OS%20X%2010.11%20Release%20Notes.md)

