---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeltaDoc/WebObjectsAPI.html
archived_at: '2026-07-15T08:04:35.721165Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
What's New in WebObjects

---

[!](What%27s%20New%20in%20WebObjects%204.5.md)

# WebObjects Framework API Changes

This chapter details those changes in the API of
the WebObjects Framework, listing new classes and methods and identifying
API that has been deprecated since the previous release.

This chapter is organized into the following sections:

- ["New Classes"](#apple-ijdumsciirbum)
- ["New Methods"](#apple-ijdumssiijdeg)
- ["Deprecated API"](#apple-ijdumrkbirduu)
- ["WOExtensions Changes"](#apple-ijdumsckizaug)

## New Classes

This release of WebObjects adds two new classes to the WebObjects
Framework, WOEvent and WOMessage.

### WOEvent

WOEvent is a subclass of EOEvent (defined in the EOControl
framework) that serves as the parent class for objects that gather
information-such as duration-about various operations in WebObjects.
You can see the results of this information gathering in your web
browser by accessing a special "event display" page, and you
can configure how the results are displayed by accessing a special
"event setup" page.

WOEvent adds knowledge of pages and components to the EOEvent
class. Events that are subclasses of WOEvent can be grouped or aggregated
by page or by component. Although you can subclass WOEvent, in most
cases the private subclasses included in the framework will be adequate
for analyzing WebObjects applications.

### WOMessage

WOMessage is the parent class for both WORequest and WOResponse,
and implements much of the behavior that is generic to both. WOMessage
represents a message with an HTTP header and either HTML or XML
content. HTML content is typically used when interacting with a
Web browser, while XML content can be used in messages that originate from
or are destined for another application (either an application that
"speaks" XML or another WebObjects application).

The methods of the WOMessage class can be divided primarily
into two groups, those that deal with a message's content and
those that read and set header information. Most of the remaining
WOMessage methods control how the content is encoded and allow you
to attach arbitrary "user info" to your WOMessage objects in
order to pass information about a given message to other objects
within your application.

#### Messages with XML Content

The Java version of the WOMessage class contains three methods
that allow you to construct and interpret messages whose content
is formatted as XML (these methods aren't available to Objective-C
programmers).

The arguments to these methods are XML documents (or, in the
case of `appendContentDOMDocumentFragment`,
a document fragment) as defined by the Document Object Model (DOM).
Installed as a part of WebObjects is the `com.ibm.xml.dom` package (IBM's
alphaWorks), which contains various XML parsers for Java written
by IBM. The included DOM parser is used to generate document and
document fragment objects from XML data (or to manipulate and/or
generate XML data from a document object). For more information
on the Document Object Model, see the online documentation at `http://www.w3.org/DOM/`.

#### Changes to WORequest

The following methods are no longer declared in WORequest
but are instead inherited from WORequest's new parent class, WOMessage:

- `content`
- `headerForKey:` (`headerForKey` in
  Java)
- `headerKeys`
- `headersForKey:` (`headersForKey` in
  Java)
- `httpVersion`
- `userInfo`

#### Changes to WOResponse

The following methods are no longer declared in WOResponse
but are instead inherited from WOResponse's new parent class,
WOMessage:

- `defaultEncoding` (static/class
  method)
- `setDefaultEncoding:` (`setDefaultEncoding` in
  Java; static/class method)
- `addCookie:` (`addCookie` in
  Java)
- `appendContentCharacter:` (`appendContentCharacter` in
  Java)
- `appendContentData:` (`appendContentData` in
  Java)
- `appendContentString:` (`appendContentString` in
  Java)
- `content`
- `contentEncoding`
- `cookies`
- `headerForKey:` (`headerForKey` in
  Java)
- `headerKeys`
- `headersForKey:` (`headersForKey` in
  Java)
- `httpVersion`
- `removeCookie:` (`removeCookie` in
  Java)
- `setContentEncoding:` (`setContentEncoding` in
  Java)
- `setContent:` (`setContent` in
  Java)
- `setHTTPVersion:` (`setHTTPVersion` in
  Java)
- `setHeader:ForKey:` (`setHeader` in
  Java)

### WOHTTPConnection

The new WOHTTPConnection class is intended to be used as a
client for HTTP communications. It gives you direct access to the
HTTP contents and headers. WOHTTPConnection's sendRequest: method
allows you to send a WORequest object directly to a server, while
readResponse allows you to receive WOResponse objects from that
same server.

### XML Package

WebObjects 4.5 includes a new XML package, `com.apple.webobjects.xml`,
which consists of the following:

- WOXMLCoding interface
- WOXMLCoder class
- WOXMLDecoder class

Use this package to encode and decode objects as XML. The
WOXMLCoder and WOXMLDecoder classes can be used to archive and unarchive
object data, or to parse and/or generate XML obtained from or destined
for an external source (such as the World Wide Web). When working
with such "foreign" XML, you describe the XML elements and properties
and their mapping to objects in an XML-format "mapping model"
that you can create with either a text editor or an XML editor.

For complete details on the XML framework and its use, see
the reference documentation in the WOInfoCenter. For examples, see
the XML Archiving andRelatedLinks examples (accessible through the
WebObjects Info Center under Examples > WebObjects > Java).

## New Methods

In addition to the new event classes (see the discussion of WOEvent/EOEvent elsewhere
in this document), the following methods have been added to the
classes that make up the WebObjects Framework.

__WOApplication__

| __Method__ | __Description__ |
| `createContextForRequest:` (Objective-C) `createContextForRequest` (Java) | Creates a new context object for a given request. Override this method if you need to provide your own subclass of WOContext. If you override it, you need not call `super` in your overriding method. |
| `defaultRequestHandlerClassName` | The default implementation of this method returns "WOComponentRequestHandler", which is the default request handler. If you don't want a session created for your application's home page, override this method to return "WODirectActionRequestHandler", making the direct action request handler the default. |
| `sharedEditingContext` | This is a convenience method that returns the default shared editing context. |
| `traceAll:` (Objective-C only; in Java, this method is still named "`trace`") | Old "`trace`" method. |

__WOAssociation__

| __Method__ | __Description__ |
| `isValueConstantInComponent:` (Objective-C) `isValueConstantInComponent` (Java) | Returns `true` when the association is "constant." Use this for checking bindings at runtime. |
| `isValueSettableInComponent:` (Objective-C) `isValueSettableInComponent` (Java) | Returns `false` when the association is "constant." Use this for checking bindings at runtime. |

__WOComponent__

| __Method__ | __Description__ |
| `canGetValueForBinding:` (Objective-C) `canGetValueForBinding` (Java) | Verifies that the binding exists and that `valueForBinding` will return a value. |
| `canSetValueForBinding:` (Objective-C) `canSetValueForBinding` (Java) | Verifies that the binding exists and that `setValueForBinding` will succeed. |
| `isEventLoggingEnabled` | Called to determine if a component wants event logging. This is not desirable, for example, for components which are associated with event display as they would interfere with the actual event logging. The default implementation of this method returns `true`. |
| `isStateless` | By default, this method returns `false`, indicating that state will be maintained for instances of the receiver. Overriding this method to return `true` will make the component stateless. A single instance of each stateless component is shared between multiple sessions, reducing your application's memory footprint. |
| `reset` | This method-which is only invoked if the component is stateless-allows a component instance to reset or delete temporary references to objects that are specific to a given context. |

__WODisplayGroup__

| __Method__ | __Description__ |
| `globalDefaultForValidatesChangesImmediately` | This static/class method returns the class default controlling whether changes are immediately validated. |
| `globalDefaultStringMatchFormat` | This static/class method returns the default string match format for the class. |
| `globalDefaultStringMatchOperator` | This static/class method returns the default string match operator for the class. |
| `insertObjectAtIndex` (New in Java only; the Objective-C version of this method previously existed) | Inserts the supplied object into the receiver's EODataSource and displayed objects at the specified index, if possible. |
| `setGlobalDefaultForValidates ChangesImmediately:` (Objective-C) `setGlobalDefaultForValidates ChangesImmediately` (Java) | This static/class method sets the class default controlling whether changes are immediately validated. |
| `setGlobalDefaultStringMatch Format:` (Objective-C) `setGlobalDefaultStringMatch Format` (Java) | This static/class method sets the default string match format for the class. |
| `setGlobalDefaultStringMatch Operator:` (Objective-C) `setGlobalDefaultStringMatch Operator` (Java) | This static/class method sets the default string match operator for the class. |
| `stringQualifierOperators` | Returns an array containing all of the relational operators supported by EOControl's EOQualifier that work exclusively on strings: "`starts with`", "`contains`", "`ends with`", "`is`", and "`like`". |

### Other WODisplayGroup Changes

In the past, EODisplayGroup and WODisplayGroup replaced all
instances of "=" in queries involving string attributes
with the `defaultStringMatchOperator`. This
is `caseInsensitiveLike`, although
it can be changed by a variety of instance or class methods on display
group. Additionally, these string based queries had the wildcard
character appended to them by means of the `defaultStringMatchFormat` which
is initially `@"%@*"`.

These transformations took place even if the `EOQualifierOperatorEqual` is
explicitly set in the display group's `queryOperator` dictionary.

As of version 4.5, a display group won't alter "=" if
it is explicitly set. It will provide the old behavior only if
the query operator is not set. Therefore, `EOQualifierOperatorEqual` will
no longer provide any pattern matching functionality and will generate
"=" instead of "like" in the SQL.

You can get the old behavior if you set the `WORequiresWOF40Compatibility` default.
Alternatively, you can replace the "=" in the appropriate
entry of the `queryOperator` dictionary with
the empty string or with `"starts with"` (both
provide the default behavior).

Additionally, display group provides a new instance method, `stringOperators`,
which returns an array of string comparison operators including `"starts
with"`, `"ends with"`, `"contains"`, `"is"`,
and `"like"`. `"starts
with"`, `"ends with"`,
and `"contains"` all use
the `defaultStringMatchOperator` and the
match formats `@"%@*", @"*%@"`,
and `@"*%@*"` respectively.
The `defaultStringMatchOperator` is still `caseInsensitiveLike`.
`"is"` and `"like"` map
exactly to the "=" and `caseInsensitiveLike` operators.

The pre-v4.5 behavior was precisely `"starts
with"`.

These string operators are only supported by display group,
not EOQualifier, nor any other part of EOF in this release.

## Deprecated API

__WOApplication__

| __Deprecated API__ | __New API or Workaround__ |
| `logToMonitorWithFormat:` (Objective-C) `logToMonitorString` (Java) | New features in Monitor will allow logging of information. The deprecated API does nothing. |
| `monitorHost` (The Java version of this method has not yet been deprecated) | New monitor features eliminate the need for this method. |
| `setMonitorHost:` (The Java version of this method has not yet been deprecated) | New monitor features eliminate the need for this method. |
| `trace:` (Deprecated in Objective-C only; in Java, this method remains as-is) | `traceAll:` |

__WOResponse__

| __Deprecated API__ | __New API or Workaround__ |
| `appendContentBytes:` (Objective-C only; this method never existed in the Java version of WOResponse) | Deprecated. Use `appendContentData:`, which is inherited from WOMessage. |

## WOExtensions Changes

The WebObjects Extensions framework has changed in the following
ways:

- Documentation for the components is now provided
- 12 reusable components have been added
- 11 reusable components have been made stateless
- WOTableString has been deprecated

### WOExtensions Reference Documentation

A new document titled WebObjects Extensions Component Specifications
has been added to cover the reusable components in the WebObjects
Extensions framework. You can access this document from the WebObjects
Info Center.

### New Components

The following reusable components are new:

- JSAlertPanel
- JSConfirmPanel
- JSImageFlyover
- JSModalWindow
- JSTextFlyover
- JSValidatedField
- WOCheckboxMatrix
- WOEventDisplayPage
- WOEventSetupPage
- WOKeyValueConditional
- WORadioButtonMatrix
- WOTabPanel

See the WebObjects Extensions Component Specifications for
more information about these components.

### Stateless Components

Making a reusable component stateless significantly improves
the performance of the component. To this end, the following WebObjects
Extension components are now stateless:

- WOAnyField
- WOBatchNavigationBar
- WODictionaryRepetition
- WOSimpleArrayDisplay
- WOSimpleArrayDisplay2
- WOSortOrder
- WOSortOrderManyKey
- WOTable
- WOThresholdColoredNumber
- WOToManyRelationship
- WOToOneRelationship

The conversion has not changed their function.

### Deprecated Elements

WOTableString is now deprecated. This component was used to
improve the appearance of table cells containing empty strings.
The HTML specification designates that the borders for table cells
should only appear when the cell has content; which causes table
cells containing empty WOStrings appear without their borders. The
WOTableString reusable component was provided as a workaround that
rendered as a non-breaking space when its value was empty, preserving
the borders.

Instead of using the WOTableString reusable component, use
the WOString dynamic element with the valueWhenEmpty attribute bound
to " ".

[!](What%27s%20New%20in%20WebObjects%204.5.md)
