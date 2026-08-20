---
title: Automator Programming Guide
apple_id: TP40001450
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: Automator
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/AutomatorConcepts/Articles/ImplementObjCAction.html
archived_at: '2026-07-15T05:16:42.718579Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Automator Programming Guide](Introduction%20to%20Automator%20Programming%20Guide.md)


[Next](Creating%20Shell%20Script%20Actions.md)[Previous](Implementing%20an%20AppleScript%20Action.md)

# Implementing an Objective-C Action

The particular advantage of actions written in Objective-C (compared to AppleScript actions) is that they have greater access to the range of system resources of OS X. Actions that use Objective-C code can incorporate the features not only of Objective-C frameworks such as Foundation and Application Kit but of virtually any other framework (Because Objective-C is a superset of ANSI C, an Objective-C class can call functions published in a C interface). Purely Objective-C actions have an offsetting disadvantage: they cannot easily control applications or access their features except for those applications that offer a public API.

In general, data that Automator pipes through the actions of a workflow is assumed to be AppleScript-compatible. If it detects that an action is based on Objective-C, however, Automator converts it into an Objective-C object that the action can deal with. It also takes the objects that Objective-C actions provide and converts them into a form suitable for AppleScript-based actions.

An action that is purely based on Objective-C must have Cocoa-specific type identifiers for its `AMAccepts` and `AMProvides` properties. Currently there are three Cocoa public type identifiers:

- `com.apple.cocoa.string` —An NSString for text
- `com.apple.cocoa.path` — An NSString for full file-system paths
- `com.apple.cocoa.url` —An NSURL for URLs

For example, if you were to specify `com.apple.cocoa.path` as the sole type identifier of the `AMAccepts` property, the input object in the `runWithInput:fromAction:error:` method would an NSString object representing a path (or an array of such string objects). If you were to specify `com.apple.cocoa.url` as the type identifier of the `AMProvides` property, you would have to return an NSURL object (or an array of NSURL objects) in your implementation of `runWithInput:fromAction:error:`.

For further discussion of the Cocoa type identifiers, see [Type Identifiers](Automator%20Action%20Property%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjvfuytamjygazq).

In your custom subclass of AMBundleAction you must override the method `runWithInput:fromAction:error:` (inherited from the AMAction class). Aside from specifying the Cocoa type identifiers in your `AMAccepts` and `AMProvides` properties, this method implementation is the only requirement for a purely Objective-C action.

If an action does not have to deal with the input data handed it—for example, its role is to select some items in the file system—the implementation of `runWithInput:fromAction:error:` can return whatever it is designed to provide without touching the input data. In the example in Listing 1, the action returns a list of paths to movies selected in its user interface (and stored in its parameters):

__Listing 1__  An Objective-C action that does not handle its input object

```objc
- (id)runWithInput:(id)input fromAction:(AMAction *)anAction
        error:(NSDictionary **)errorInfo {
    return [[self parameters] objectForKey:@"movieFiles"];
}
```

However, most actions operate on the input data given them from the previous action. The input object and the output object for an action are almost always NSArray objects because the `Container` subproperties of `AMAccepts` and `AMProvides` are by default lists (equivalent to NSArray objects in Objective-C). Many Objective-C actions implement `runWithInput:fromAction:error:` using a general approach that is similar to a typical `on run` handler in an AppleScript-based action:

1. If the container type of the action’s `AMProvides` property is List, prepare an output array for later use (usually by creating an NSMutableArray object).
2. Iterate through the elements of the input array and for each perform whatever operation is required and write the resulting data item to the output array.
3. Return the output array.

__Listing 2__  Implementing runWithInput:fromAction:error:

```objc
- (id)runWithInput:(id)input fromAction:(AMAction *)anAction error:(NSDictionary **)errorInfo
{
    NSMutableArray *returnArray = [NSMutableArray arrayWithCapacity:[input count]];
    NSEnumerator *enumerate = [input objectEnumerator];
    NSString *xmlFile;

    while (xmlFile = [enumerate nextObject]) {
        NSError *anError=nil;
        NSString *returnStr;

        NSXMLDocument *xmlDoc = [[NSXMLDocument alloc] initWithContentsOfURL:[NSURL fileURLWithPath:xmlFile] options:nil error:&anError];
        NSLog(@"XML document = %@", [xmlDoc description]);
        if (!xmlDoc) {
            [returnArray addObject:[NSString stringWithFormat: @"ERROR: Could not make document from file: %@\n", xmlFile]];
            continue;
        }
        if (anError) {
            [returnArray addObject:[NSString stringWithFormat: @"ERROR: Error in processing file %@, because = %@\n", xmlFile, [anError localizedDescription]]];
            continue;
        }

        NSString *queryStr;
        if ([[[self parameters] objectForKey:@"elementAttributeChoice"] intValue]) { // attribute
            queryStr = [NSString stringWithFormat:@".//@%@/text()", [[self parameters] objectForKey:@"elementAttributeName"]];
        } else {
            queryStr = [NSString stringWithFormat:@".//%@/text()",  [[self parameters] objectForKey:@"elementAttributeName"]];
        }
        anError = nil;
        NSArray *results = [xmlDoc nodesForXPath:queryStr error:&anError];
        if (anError) {
            [returnArray addObject:[NSString stringWithFormat: @"ERROR: Error in XQuery because = %@\n", [anError localizedDescription]]];
            continue;
        }
        [returnArray addObject:[NSString stringWithFormat:@"\n--------- Found in file %@ ----------\n", xmlFile]];
        int i, count = [results count];
        for (i = 0; i < count; i++) {
            [returnArray addObject:[results objectAtIndex:i]];
        }
        [xmlDoc release];
    }

    return returnArray;
}
```

Some actions in their `AMAccepts` property specify that their input is optional (that is, the `Optional` subproperty is set to `<true/>`). This setting allow users to select a “Ignore Result...” item from an input type pop-up button in the action’s view. If your action has made input optional in its `AMAccepts` property, you need to determine if the user has made this choice by sending the action an `ignoresInput` message; if the response is `YES`. you do not need to do anything with the input object.

If your action encounters an error that prevents it from proceeding, it should give information describing the error to Automator, which then stops executing the workflow and displays an error alert. The last parameter of the `runWithInput:fromAction:error:` method is a pointer to an NSDictionary object. To report errors, you must create a dictionary containing two key-value pairs and return this object to Automator indirectly. The two dictionary properties are:

- `OSAScriptErrorNumber`—Takes an error number encapsulated as an NSNumber object.

  For suitable error codes, see the `MacErrors.h` header file of the Carbon Core framework, especially the error codes specific to the OSA framework.
- `OSAScriptErrorMessage`—Takes an NSString object containing a description of the error.

Because the code example in [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjtfu4tsobtgqwueqsdjjbeosce) output is text, it reports errors such as the lack of a valid document as part of the output. But what if this were a fatal error that required the action to stop executing? Listing 3 illustrates how you might handle such an error.

__Listing 3__  Reporting a fatal error to Automator

```
if (!xmlDoc) {
    NSArray *objsArray = [NSArray arrayWithObjects:
        [NSNumber numberWithInt:errOSASystemError],
        [NSString stringWithFormat:@”ERROR:
            Could not make document from file: %@\n", xmlFile], nil];
    NSArray *keysArray = [NSArray arrayWithObjects:OSAScriptErrorNumber,
        OSAScriptErrorMessage, nil];
    *errorInfo = [NSDictionary dictionaryWithObjects:objsArray
        forKeys:keysArray];
    return nil;
}
```

Your action has the entire gamut of possibility available to Cocoa applications. It can message Cocoa-framework objects and custom objects from its AMBundleAction subclass, and it can define and implement as many other supporting classes, protocols, and categories as is needed to accomplish the task of the action. An Objective-C action could choose to do any of the following things:

- Execute a command-line tool using an NSTask object.
- Perform animation using NSAnimation or NSViewAnimation.
- Spin off multiple secondary threads using Foundation’s threading support.
- Communicate with other applications using distributed objects or distributed notifications.
- Use a C-language framework; for example, you could use Core Graphics to draw an image directly to the screen.

An Objective-C has only two restrictions related to its implementation of `runWithInput:fromAction:error:`. It cannot return until it has completely finished whatever processing it has initiated. For instance, if an action instructs a camera to take a picture (an asynchronous process) it cannot return from `runWithInput:fromAction:error:` method until the picture is taken. So the action has to implement whatever blocking algorithm, timeout logic, or threading strategy is necessary until the picture is taken. The second restriction has to do with Automator’s threading architecture. Because Objective-C actions run on a secondary thread, if they want to display a window it must be done on the main thread. The `performSelectorOnMainThread:withObject:waitUntilDone:` method is adequate for this purpose; for example:

```
self performSelectorOnMainThread:@selector(showPreviewWithData:) withObject:data waitUntilDone:YES]
```


A typical action uses the bindings technology of Cocoa to synchronize the settings on an action’s user interface with the action’s parameters attribute. (See [Constructing the User Interface](Developing%20an%20Action.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjrfu4tmobxg4) in [Developing an Action](Developing%20an%20Action.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjrfvbecsscjfbuosa).) But an action is not required to use bindings to do this synchronization. It can choose to do it manually by implementing the `updateParameters` and `parametersUpdated` methods. These methods are invoked went it is time to run or save the action.

The `updateParameters` method is invoked when the parameters attribute of the action (an NSDictionary object) needs to be refreshed from the settings and values the user has specified in the user interface. The `parametersUpdated` method is invoked for the opposite reason: to make the pop-up items, buttons, text fields, and other objects in the action’s view reflect the current contents of the action’s parameters, especially when those contents change programmatically.

Listing 4 shows a typical implementation of the `updateParameters` method.

__Listing 4__  Updating an Objective-C action’s parameters manually

```objc
- (void)updateParameters
{
    // text
    NSString *outputFile = [_outputFilePath stringValue];
    if (outputFile)
    {
        [[self parameters] setObject:outputFile forKey:@"outputFilePath"];
    }

    NSString *waitSeconds = [_waitSeconds stringValue];
    if (waitSeconds)
    {
        [[self parameters] setObject:[NSNumber numberWithInt:
            [_waitSeconds intValue]] forKey:@"waitSeconds"];
    }

    // radios
    [[self parameters] setObject:[NSNumber numberWithInt:
        [_interactiveType selectedRow]] forKey:@"interactiveType"];
    [[self parameters] setObject:[NSNumber numberWithInt:
        [_screenShotType indexOfSelectedItem]] forKey:@"screenshotType"];

    // popup
    [[self parameters] setObject:[NSNumber numberWithInt:
        [_outputType indexOfSelectedItem]] forKey:@"outputType"];

    // checks
    [[self parameters] setObject:[NSNumber numberWithBool:
        [_captureMainMonitorOnly state]] forKey:@"captureMainMonitorOnly"];
    [[self parameters] setObject:[NSNumber numberWithBool:
        [_disableSounds state]] forKey:@"disableSounds"];
    [[self parameters] setObject:[NSNumber numberWithBool:
        [_timedScreenshot state]] forKey:@"timedScreenshot"];
}
```

You can also update an action’s parameters to include miscellaneous data that can stay with the action as it is, for example, copied to the pasteboard or written to disk in a workflow. When Automator archives an action it includes the action’s parameters with the archive, and thus objects stored in the parameters can be unarchived and retrieved. The only restriction is that the Foundation object saved to an action’s parameters must be a property-list object—that is, an NSData, NSDate, NSNumber, NSString, NSArray, or NSDictionary object. Any object that is not one of these must be converted to a property-list object before it can be archived.

Objects that represent URLs—in other words, instances of NSURL—are an important case in point. URLs are a type of data (identified with UTI `public.url`) that actions occasionally deal with. Fortunately, there are methods for converting NSURL objects to and from a property-list object. The code in Listing 5 converts an NSURL object to an NSString object and stores that in the action parameters.

__Listing 5__  Saving an NSURL object to parameters as a string object

```
NSMutableDictionary* params;

if (mFilterURL) // NSURL object
{
    NSString* path = [mFilterURL path];
    params = [NSMutableDictionary dictionaryWithObject:path  forKey:@"URL" ];

    [self setParameters:params];
}
```

Now when the action is archived the URL is stored with it, and when it is unarchived the URL is retrievable. The code fragment in Listing 6 restores the NSURL object from the NSString object stored in the action parameters.

__Listing 6__  Restoring an NSURL object from an action’s parameters

```
NSURL* filterURL = nil;

NSMutableDictionary* params = [self parameters];

NSString* path = [params objectForKey: @"URL"];

if (path) filterURL = [NSURL fileURLWithPath:path];

if (filterURL)
{
   // do something with filterURL here
}
```

This example uses `fileURLWithPath:` to create an NSURL object representing a file-scheme URL. If you want a URL object with a different scheme, you would use something such as `URLWithString:`, an NSURL class method. However, the string for this method must contain any necessary percent-escape codes. The easiest way to obtain such a string is to send `absoluteString` to the NSURL object before storing the URL string in the action parameters. If your action for some reason does not deal with absolute URLs, then it must devise a way to save and restore the various parts of the URL.

Objective-C actions can also include AppleScript code that they load and execute, making them in effect hybrid actions. The OSA framework and the Foundation framework contain a number of classes (OSAScript, NSAppleScript, NSAppleEventDescriptor, and more) that enable creation, preparation, and execution of objects representing AppleScript scripts.

Listing 7 illustrates how an action gets an AppleScript script either from its user interface or its parameters, creates an OSAScript object with it, and then compiles and executes the script.

__Listing 7__  Executing an AppleScript script in an Objective-C action

```objc
- (OSAScript *)script
{
    OSAScript *script = nil;
    NSString *source = nil;

    if ([self controller])
    {
        [[self controller] compileScript:self];
        source = [[[self controller] scriptView] string];
    }
    else
    {
        source = [self source];
    }

    if (source)
    {
        script = [[OSAScript alloc] initWithSource:source language:[OSALanguage defaultLanguage]];
        if (script)
        {
            NSDictionary *errorInfo;
            [script compileAndReturnError:&errorInfo];
        }
    }
    return [script autorelease];
}

- (NSString *)source
{
    return [[self parameters] objectForKey:@"RunScriptSource"];
}

- (void)setSource:(NSString *)source
{
    [[self parameters] setObject:source forKey:@"RunScriptSource"];
}
```


[Next](Creating%20Shell%20Script%20Actions.md)[Previous](Implementing%20an%20AppleScript%20Action.md)

