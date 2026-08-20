---
title: Safari Web Inspector Guide
apple_id: TP40007874
resource_type: Guide
platform: iAd System JS|Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2018-02-07'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Safari_Developer_Guide/Console/Console.html
archived_at: '2026-07-15T05:18:15.867945Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Web Inspector Guide](About%20Safari%20Web%20Inspector.md)


[Next](The%20Develop%20Menu.md)[Previous](Debugger.md)

# The Console

The console offers a way to inspect and debug your webpages. Think of it as the Terminal of your web content. The console has access to the DOM and JavaScript of the open page. Use the console as a tool to modify your web content via interactive commands and as a teaching aid to expand your knowledge of JavaScript. Because an object’s methods and properties autocomplete as you type, you can see all available functions that are valid in Safari.

For example, open the console and type `$$(‘p’)[1]`. (`$$` is shorthand for `document.querySelectorAll`—see more shorthand commands in [Table 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqnrnknlto).) Because this paragraph is the second instance of the `p` element on this page (`[1]` in a 0-based index), the node represents this paragraph. As you hover over the node, its position on the page is visibly highlighted. You can expand the node to see its contents, and even press Command-C to copy it to your clipboard.

You can inspect HTML nodes and JavaScript objects in more detail by using the console commands listed in Table 5-1. Type the command-line APIs interactively within the console.

If your scripts share the same function name as a Command-Line API function, the function in your scripts takes precedence.

__Table 5-1__  Commands available in the Web Inspector console

| Command | Description |
| `$(`_selector_`)` | Shorthand for `document.querySelector`. |
| `$$(`_selector_`)` | Shorthand for `document.querySelectorAll`. |
| `$x(`_xpath_`)` | Returns an array of elements that match the given [XPath](http://www.w3.org/TR/xpath/) expression. |
| `$0` | Represents the currently selected node in the content browser. |
| `$`_1..4_ | Represents the last, second to last, third to last, and fourth to last selected node in the content browser, respectively. |
| `$_` | Returns the value of the last evaluated expression. |
| `dir(`_object_`)` | Prints all the properties of the object. |
| `dirxml(`_object_`)` | Prints all the properties of the object. If the object is a node, prints the node and all child nodes. |
| `keys(`_object_`)` | Prints an array of the names of the object’s own properties. |
| `values(`_object_`)` | Prints an array of the values of the object’s own properties. |
| `profile(`_[title]_`)` | Starts the JavaScript profiler. The optional argument `title` contains the string to be printed in the header of the profile report. See [JavaScript and Events Recording](Timelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqnbnknlto). |
| `profileEnd()` | Stops the JavaScript profiler and prints its report. See [JavaScript and Events Recording](Timelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqnbnknlto). |
| `getEventListeners(`_object_`)` | Prints an object containing the object’s attached event listeners. |
| `monitorEvents(`_object[, types]_`)` | Starts logging all events dispatched to the given object. The optional argument `types` defines specific events or event types to log, such as “click”. |
| `unmonitorEvents(`_object[, types]_`)` | Stops logging for all events dispatched to the given object. The optional argument `types` defines specific events or event types to stop logging, such as “click”. |
| `inspect(`_object_`)` | Inspects the given object; this is the same as clicking the Inspect button. |
| `copy(`_object_`)` | Copies the given object to the clipboard. |
| `clear()` | Clears the console. |

The functions listed in Table 5-1 are regular JavaScript functions that are part of the Web Inspector environment. That means you can use them as you would any JavaScript function. For example, you can assign a chain of Console API commands to a variable to create a useful shorthand. Listing 5-1 shows how you can quickly see all event types attached to the selected node.

__Listing 5-1__  Find the events attached to this element

```
var evs = function () {
    return keys(getEventListeners($0));
};
```

After defining this function, inspect the magnifying glass in the top-right corner of this webpage, and type `evs()` in the console. An array containing the string “click” is returned, because there is a click event listener attached to that element.

Of course, these functions shouldn’t be included in your website’s JavaScript files because they are not available in the browser environment. Only use these functions in the Web Inspector console. Console functions you can include in your scripts are described in [Console API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqnrnknltg).

You can output messages to the console, add markers to the timeline, and control the debugger directly from your scripts by using the commands listed in Table 5-2.

__Table 5-2__  JavaScript functions available in the Console API

| Function | Description |
| `console.assert(expression, object)` | Asserts whether the given expression is true. If the assertion fails, prints the error and increments the number of errors in the activity viewer. If the assertion succeeds, prints nothing. |
| `console.clear()` | Clears the console. |
| `console.count([title])` | Prints the number of times this line has been called. |
| `console.debug(object)` | Alias of `console.log()`. |
| `console.dir(object)` | Prints the properties and values of the object. |
| `console.dirxml(node)` | Prints the DOM tree of an HTML or XML node. |
| `console.error(object)` | Prints a message to the console with the error icon. Increments the number of errors shown in the activity viewer. |
| `console.group([title])` | Prints subsequent logs under a disclosure of the given title. |
| `console.groupEnd()` | Ends the previously declared console grouping. |
| `console.info(object)` | Alias of `console.log()`. |
| `console.log(object)` | Prints the object to the console with the log icon. Increments the number of logs shown in the activity viewer. |
| `console.markTimeline(`_label_`)` | Marks the Timeline with a green vertical dashed line that indicates when this line of code was called. See [Recording Timelines](Timelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqnbnknlte). |
| `console.profile(`_[title]_`)` | Starts the JavaScript profiler. The optional argument `title` contains the string to be printed in the header of the profile report. See [JavaScript and Events Recording](Timelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqnbnknlto). |
| `console.profileEnd(`_[title]_`)` | Stops the JavaScript profiler and prints its report. See [JavaScript and Events Recording](Timelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqnbnknlto). |
| `console.time(`_name_`)` | Starts a timer associated with the given name. Useful for timing the duration of segments of code. |
| `console.timeEnd(`_name_`)` | Stops the timer associated with the given name and prints the elapsed time to the console. |
| `console.trace()` | Prints a stack trace at the moment the function is called. See [Figure 4-2](Debugger.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqnjnknltm). |
| `console.warn(`_object_`)` | Prints a message to the console with the warning icon. Increments the number of warnings shown in the activity viewer. |
| `debugger` | Stops JavaScript execution at the current line. This is the equivalent of setting a breakpoint programmatically. See [Breakpoints](Debugger.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqnjnknlte). |

[Next](The%20Develop%20Menu.md)[Previous](Debugger.md)

