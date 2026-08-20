---
title: Sherlock Channels
apple_id: 10000121i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-04-09'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Sherlock/Concepts/Languages.html
archived_at: '2026-07-15T05:18:54.711431Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sherlock Channels](Introduction%20to%20Sherlock%20Channels.md)


[Next](Sherlock%20Reference.md)[Previous](Developing%20Channels.md)

# Sherlock Scripting Language Support

Sherlock provides you with two different languages—JavaScript and XQuery—for writing your channel’s script code. These languages provide you with both the power and flexibility to process data and manipulate your channel’s contents dynamically. This article provides a brief introduction to each language and provides information about Apple’s implementation.

The JavaScript language was originally developed by Netscape as a way to implement dynamic HTML pages in a client’s web browser. JavaScript is an interpreted language whose syntax resembles those of C in some aspects, but which also includes a mechanism for declaring and using objects. JavaScript is also known by the name ECMAScript and is typically used for writing short subroutines to manipulate browser data or respond to user interactions within web pages.

Sherlock supports JavaScript as one of the primary languages for writing triggers. Sherlock’s uses a standard implementation of the JavaScript engine to interpret and execute script code in the Sherlock application environment. The JavaScript syntax is documented in numerous third-party books and is not covered in this article. However, developers familiar with the C and Java languages will find some familiar programming constructs.

Apple provides several predefined objects for JavaScript code to use. These objects are specific to the Sherlock channel environment and are described in more detail in [JavaScript Extensions](Sherlock%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4dkljrgyydmnjq).

XQuery is a part of the XML Query specification currently being defined by the World Wide Web Consortium. The goal of XML Query is to provide a convenient way to extract data from real and virtual documents on the web. The medium for achieving this goal is XML and the script language used to manipulate the data is called XQuery.

A complete discussion of the XQuery language is beyond the scope of this article. For the latest information about XML Query, visit the World Wide Web Consortium website (`http://www.w3c.org/XML/Query`). This site includes information about the XQuery language and other current developments.

Apple provides several additions to the XQuery language that allow you to manage Sherlock resources. Apple’s additions are documented in [XQuery Extensions](Sherlock%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4dkljrgyydsobw).

For new and experienced XQuery programmers, the following sections include some tips and techniques for using XQuery in your Sherlock channels.

Because XQuery triggers do not have access to the data store, you must use the `inputs` and `output` attributes of the trigger to get and set data store values. These parameters are described further in the section [Trigger Tag Syntax](Sherlock%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4dkljrgm2domjw).

An alternative to using the `output` attribute to return values is to return a dictionary of key/value pairs instead. When you return a dictionary of values from an XQuery trigger, the data store interprets the keys of the dictionary as paths. The data store then assigns the value for each key back to the corresponding path.

Comments in XQuery begin with an open curly brace followed by two hyphens. To close the comment, use two hyphens followed by a close curly brace, as shown in the following example:

```
{-- Comments go here. --}
```


Apple defines additional data types to supplement those provided by the XQuery language. Among the data types are the `data`, `dictionary`, and `url` types, which correspond to the Core Foundation types CFDataRef, CFDictionaryRef, and CFURLRef respectively.

The `dictionary` type is especially useful when writing XQuery-based triggers. To create a dictionary, you use the `dictionary` function provided by Apple and defined in [XQuery Extensions](Sherlock%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4dkljrgyydsobw). When you return a dictionary from an XQuery trigger, Sherlock interprets the dictionary keys as data store paths and proceeds to update the corresponding values with the dictionary data.

Apple provides several additions to the XQuery language that make it easy to access web-based resources. The additions are built on top of Apple’s Web Foundation Framework and provide access to the web using the HTTP protocol.

To request a URL, you can use any of the following functions:

- `http-get`
- `http-head`
- `http-post`
- `http-request`

These functions take the requested URL and any parameters and use them to generate an HTTP request. They return a dictionary of keys identifying the returned data and status information.

When it comes time to write your trigger code, you need to choose which language to use. Most tasks can be performed using either JavaScript or XQuery; however, some tasks are better performed in one language than the other. Knowing which language to use for a given trigger can simplify the channel development process.

Common uses for the JavaScript language include executing conditional code, putting values in the data store, and opening URLs based on user actions.

Advantages of using the JavaScript language to develop triggers and services include:

- JavaScript triggers run synchronously, allowing for more dynamic processing of inputs.
- Data store variables can be retrieved and set directly using the DataStore object.
- JavaScript is an established language with numerous resources available for learning the language.
- JavaScript can use XQuery functions through the XMLQuery object.

Disadvantages include:

- Performance of JavaScript triggers is typically slower due to their synchronous execution.
- JavaScript does not have a strong set of tools for processing text and XML expressions.
- There is no direct way to initiate HTTP requests from JavaScript. They must be performed using the XQuery functions.

Common uses for the XQuery language include retrieving data from a URL and parsing XML/HTML to create a list of results.

Advantages of using the XQuery language to develop triggers and services include:

- The XQuery syntax is well suited for transforming data and processing XML expressions.
- XQuery triggers run asynchronously by default, providing better performance and the ability to process several expressions simultaneously.
- Apple-provided extensions make it easy to access web pages and Sherlock web services.

Disadvantages include:

- The XQuery specification is still in flux and subject to change.
- There are fewer resources available for learning the XQuery syntax.
- XQuery triggers cannot access the data store directly. Triggers must use the `inputs` and `output` attributes to move data back and forth

Sherlock supports a subset of the XQuery functions defined at [http://www.w3.org/TR/2002/WD-xquery-operators-20020816/](http://www.w3.org/TR/2002/WD-xquery-operators-20020816/) . The supported functions are listed here in functional groups.

__Date, Time, and Duration__: `current-dateTime`, `dateTime`, `date`, `time`, `duration`

__Numbers__: `number`, `ceiling`, `floor`, `round`, `sum`

__Strings__: `string`, `string-length`, `normalize-space`, `concat`, `contains`, `starts-with`, `ends-with`, `substring`, `substring-after`, `substring-before`, `translate`, `compare`, `lower-case`, `upper-case`, `replace`, `string-pad`, `match`, `matches`, `string-join`, `codepoints-to-string`, `string-to-codepoints`

__Other__: `document`, `count`, `local-name`, `boolean`, `false`, `true`, `not`, `empty`, `exists`, `distinct-values`, `distinct-nodes`, `insert`, `remove`, `sublist`, `min`, `max`, `to`, `item-at`, `index-of`, `deep-equal`

In Mac OS X 10.3, Table 1 list identifies the XQuery constructs that are being deprecated. You should update your channel code to eliminate calls these functions.

__Table 1__  Deprecated XQuery constructs

| Construct | Notes |
| `sortby` function | This function is being replaced by the “order by” expressions instead. |
| `==` and `!==` operators | Use the `is` and `isnot` operators instead. |
| XML constructs with non-quoted attributes | An example of this construct is `<a href={$link} />`. You must now include quotes around the attribute value, so that the above construct would now be `<a href="{$link}" />`. |
| Using uninitialized variables | If you use a variable that has not been defined or initialized with a value, you will get an error. |
| Comments | Using a close curly brace character `}` inside a comment now generates an error. |

[Next](Sherlock%20Reference.md)[Previous](Developing%20Channels.md)

