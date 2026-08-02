---
title: Tree-Based XML Programming Guide
apple_id: TP40001269
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/Articles/QueryingXML.html
archived_at: '2026-07-15T07:17:02.904206Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Tree-Based XML Programming Guide](Introduction%20to%20Tree-Based%20XML%20Programming%20Guide%20for%20Cocoa.md)


[Next](Modifying%20an%20XML%20Document.md)[Previous](Traversing%20an%20XML%20Tree.md)

# Querying an XML Document

One way to find items of interest in an XML document is to use the NSXML methods that traverse the nodes in a document tree (see [Traversing an XML Tree](Traversing%20an%20XML%20Tree.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjxfvbecsski5eecsi)). However, this can be a time-consuming approach, especially with large documents. A more efficient strategy is to perform XPath and XQuery queries on the document object or any of the nodes in the document. This article describes the basic steps for executing XQuery and XPath queries and suggests how you can integrate such queries with an application’s user interface.

XQuery 1.0 and XPath 2.0 are query languages so well integrated that it is easy to think of them as one language. Their formal semantics, data model, and functions and operators are defined in the same W3C specifications (see [See Also](Introduction%20to%20Tree-Based%20XML%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrtfu4tmobwha) in the introduction). However there are distinctions, the primary one being that XPath uses a POSIX-style path syntax to describe the locations of nodes within an XML tree. In addition, XPath deals with nodes, while XQuery deals with nodes _and_ atomic values.

The NSXMLNode class has two query-related methods, one for making XPath queries and the other for making XQuery queries:

- `- (NSArray *)nodesForXPath:(NSString *)xpath error:(NSError **)error`
- `- (NSArray *)objectsForXQuery:(NSString *)xquery constants:(NSDictionary *)constants error:(NSError **)error`

Both methods return an array of found items—corresponding to a sequence in the data model—but the nature of the items differs, and this difference is reflected in the method names. The `nodesForXPath:error:` method returns an array of NSXMLNode objects while the `objectsForXQuery:constants:error:` method returns an array potentially containing both NSXMLNode objects and Foundation objects corresponding to the atomic types (NSNumber, NSString, NSCalendarDate, and so on). Even if these methods find only one item, they return it in an array.

Both methods also start a query with reference to an initial _context node_. The context node is the node against which the evaluation of a location path or other expression is applied. In both methods the initial context node is the receiver of the message. In a query expression, you can also refer to the context node with a period (for example, `“.//products”`).

You often begin an XPath expression with a double slash (`“//”`) followed by an element name. This gives you all the descendent elements of the context node with that name, regardless of their level in the hierarchy. (You can also use a double slash elsewhere in a path.) Single slashes, followed by an element name, indicate a singular path down the tree hierarchy. Predicates are Boolean tests within square brackets that select a subset of the nodes as evaluated to that point. Numbers within square brackets after elements identify particular child nodes by their index (which in this case is 1-based). To see this in practice, consider the following path expression:

```
.//part/chapter[1]/section[@title=”Path Expressions”]
```

The evaluation of a path expression works from left to right. This expression first gets all the elements named `part` and from that selects the first element named `chapter`; from that it gets all child elements named `section`, and from that sequence it returns the section element whose title is “Path Expressions”. XPath also lets you find attributes by name by using an at-sign (@) prefix. For example, the following path expression gets the modification date (an attribute) of the first chapter:

```
.//part/chapter[1]/@modDate
```

XPath also has function-like type specifiers that let you refer to child nodes other than elements and attributes, including text nodes (`text()`), processing instructions (`processing-instruction()`), and comments `(comment()`). If a parent has more than one node of a given type, all are returned.

Listing 1 is a fragment of code that illustrates how to make an XPath query using `nodesForXPath:error:`. It references a `city` element, which is a child of an `address` element, which is the third child element named `person` of the context node. If there are multiple elements named `city` at the end of this path, all of them are returned.

__Listing 1__  Executing an XPath query

```
NSError *err=nil;
NSXMLElement *thisCity;
NSArray *nodes = [theDocument nodesForXPath:@"./person[3]/address/city"
        error:&err];
if ([nodes count] > 0 ) {
    thisCity = [nodes objectAtIndex:0];
    // do something with element
}
if (err != nil) {
    [self handleError:err];
}
```

The initial context node for this query, an NSXMLDocument object (`theDocument`), is the receiver of the message. XPath returns the node or nodes that it finds in an array (a sequence). The code in Listing 1 is interested only in extracting the first node in the array, which it knows to be an NSXMLElement object. (Other kinds of child nodes can also be returned.) If XPath has trouble processing the query string—for example, the query has a syntax error—it directly returns `nil` and indirectly returns an NSError object. This code merely passes that object to another method to handle.

The NSXMLNode class defines an `XPath` method that can be quite useful when making XPath queries. As the name suggests, you can send an `XPath` message to any node object to get an XPath string describing that node’s location in a tree. You can send or cache this string so that the node can easily be retrieved later via an XPath query. One possible scenario is that when a node changes its location within a tree, you can broadcast a notification that contains the new location as an XPath string in the `userInfo` dictionary.

XQuery is a flexible and powerful query language that encompasses XPath. XQuery lets you compose logically complex queries using operators, quantifiers, functions and FLOWR expressions (referring to the keywords `for`, `let`, `order by`, `where`, and `return`). With XQuery you can sort returned values, construct nodes, perform joins, invert hierarchies, and dynamically create new XML documents.

As an example, consider the simple query shown in Listing 2.

__Listing 2__  A simple XQuery query

```
for $p in .//person
where $p/address/zip_code > 90000
order by $p/last_name
return $p
```

This query cycles through every descendent element of the context node named `person` and evaluates whether the child element at path `/address/zip_code` has a value greater than 90000. It sorts the elements that satisfy this test by the value of their `last_name` child element and returns the resulting sequence.

Executing an XQuery query in NSXML is largely a matter of passing in the query string when invoking the `objectsForXQuery:constants:error:` method. The example method in Listing 3 gets the string from a text view in the user interface.

__Listing 3__  Executing an XQuery query

```objc
- (IBAction)applyXQuery:(id)sender {
    if (document) {
        NSError *error;
        NSArray *result = [document objectsForXQuery:
            [xquerySourceTextView string] constants:nil error:&error];
        if (result) {
            unsigned count = [result count];
            unsigned i;
            NSMutableString *stringResult = [[NSMutableString alloc] init];
            for (i = 0; i < count; i++) {
                [stringResult appendString:
                    [NSString stringWithFormat:@"%d: {\r", i]];
                [stringResult appendString:[[result objectAtIndex:i]
                    description]];
                [stringResult appendString:@"\r}\r"];
            }
            [xqueryResultTextView setString:stringResult];
            [stringResult release];
        } else if (error) {
            [self handleError:error];
        }
    }
}
```

This method applies the user-supplied query and formats the results before displaying it in another text view. If there is an error processing the request, it displays information about the error in an alert panel.

The second parameter of `objectsForXQuery:constants:error:` takes an NSDictionary object whose keys are the name of variables defined as external. The value of such a key is assigned as the value of the variable when it is used in a query. Through this mechanism, the constants dictionary lets you reuse a query string containing a variable whose value can change for each separate execution of a query. For more about the constants dictionary and its potential uses for a user interface, see the following section.

Although you can make use of XPath and XQuery in your application, you can’t expect users to know enough about these query languages to construct their own queries. To use these languages effectively in your application, you need to find a way to incorporate the user’s intent into each query. There are various ways you could go about this. Two of them are discussed here, the constants dictionary and formatted strings.

The constants dictionary, introduced in [XPath and XQuery Basics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjyfu4tomjyge), allows you to assign values to external variables in an XQuery query. You declare the variables in the prolog of the query and reference the variables where required in the query. (A prolog is a series of declarations and imports that creates the environment for query processing; it includes such things as variable definitions, module declarations, and schema imports.) The query can be reused as many times as you want. Then you create a dictionary containing key-value pairs where the key is the name of the variable and the value is whatever you want it to be. The value can be derived directly from a user-interface object.

With the constants dictionary you can, for instance, have a query that looks up user-supplied terms from an online dictionary. Figure 1 gives a simple example of the user interface for this query.

__Figure 1__  Simple user interface for a terminology query

![Simple user interface for a terminology query](attachments/Articles/Art/user_interface1.gif)

With the constants dictionary, you can assign the value of the term field to an external variable in the query string.

Let’s say a controller object connects the text field to an outlet named `termField` and connects the button to an action method. The following steps show how you might (in the action method) integrate the term variable into the query string:

1. Put the following line in the prolog of a query:

```
declare variable $term as xs:string external;
```
2. Insert the variable (`$term`) in the query where you want the value to be used or evaluated.
3. Create a dictionary with a key of the same name as the variable and a value obtained from the user interface:

```
NSDictionary *dict = [NSDictionary dictionaryWithObject:[termField stringValue] forKey:@”term”];
```
4. Send the `objectsForXQuery:constants:error:` method to the context node, passing in the dictionary:

```
NSArray *result = [document objectsForXQuery:queryString constants:dict error:&err];
```

Keep in mind that external variables have assigned values, similar to the following expression:

```
let $term := “a value”
```

External variables are not like macros where the value is substituted for a placeholder. Consequently, you cannot use the constants-dictionary mechanism to do things such as dynamically changing the XQuery functions used in a query string.

The `stringWithFormat:` class method of NSString is a powerful tool. With it you can compose strings whose components can vary because of external factors, such as input from users. You can use format XQuery query strings in the same way. And unlike external variables, whose values are assigned from the constants dictionary, the “var-args” values in a formatted string are substituted for their place holders. Thus, formatted strings enable you to change language-related parts of the query string dynamically, including operators, function names, and path expressions.

To see how this might work, it helps to follow a simple example. Figure 2 shows a possible user interface for performing an XQuery query on an XML document.

__Figure 2__  User interface for a more complex query

![User interface for a more complex query](attachments/Articles/Art/user_interface2.gif)

The choices and entries a user makes with the pop-up lists and the text field become part of the query executed when the user clicks the Find button. For the specific choices and entry in the example above, the query string becomes the following:

```
for $p in //person
where starts-with($p/phone/text(), “(408)”)
order by $p/lastName
return $p
```

For the pop-up lists, the incorporated values are “represented objects” associated with the items (NSMenuItem objects) of the lists. The represented objects of the first list’s items are XPath path expressions relative to a context node; the represented objects of the second list’s items are either operators or names of XQuery functions. Listing 4 is a method that dynamically creates the items of the second pop-up list and sets their represented objects.

__Listing 4__  Setting the represented objects for pop-up list items

```objc
- (IBAction)changeOperationsList:(id)sender {
    [operationPopUp removeAllItems];

    if ([elementPopUp indexOfSelectedItem] > 4) { // operators
        NSMenuItem *anItem;
        [operationPopUp addItemsWithTitles:[NSArray arrayWithObjects:
            @"equals", @"greater than", @"less than", nil]];

        anItem = (NSMenuItem *)[operationPopUp itemAtIndex:0];
        if (anItem) {
            [anItem setRepresentedObject:@"="];
        }
        anItem = (NSMenuItem *)[operationPopUp itemAtIndex:1];
        if (anItem) {
            [anItem setRepresentedObject:@">"];
        }
        // continued ...

    } else { // functions
        NSMenuItem *anItem;
        [operationPopUp addItemsWithTitles:[NSArray arrayWithObjects:
            @"is", @"contains", @"begins with", @"ends with", nil]];
        anItem = (NSMenuItem *)[operationPopUp itemAtIndex:0];
        if (anItem) {
            [anItem setRepresentedObject:@"matches"];
            [anItem setTag:XQFunction];
        }
        anItem = (NSMenuItem *)[operationPopUp itemAtIndex:1];
        if (anItem) {
            [anItem setRepresentedObject:@"contains"];
            [anItem setTag:XQFunction];
        }
        // continued ...
    }
}
```

When the user chooses popup-list items, enters a value for comparison in the text field, and clicks the Find button, the action method shown in Listing 5 is invoked. This method composes the query string—differently, according to whether a function or operator is required—from the represented objects and the value of the text field. It then sends the `objectsForXQuery:constants:error:` message to the context node (the document object) to execute the query.

__Listing 5__  Composing and executing the query

```objc
- (IBAction)findByXQuery:(id)sender {

    NSString *queryString;
    NSArray *results;
    NSError *err=nil;
    [queryStatus setStringValue:@""];
    if ([[operationPopUp selectedItem] tag] == XQFunction ) {
        queryString = @" \
            for $p in //person \
            where $op($p/%@/text(), $query) \
            order by $p/lastName \
            return $p",
            [[operationPopUp selectedItem] representedObject],
            [[elementPopUp selectedItem] representedObject]];
    } else {
        queryString = [NSString stringWithFormat:@" \
            for $p in //person \
            where $p/%@/text() %@ \"%@\" \
            order by $p/lastName \
            return $p",
            [[elementPopUp selectedItem] representedObject],
            [[operationPopUp selectedItem] representedObject],
    }
    results = [xmlDoc objectsForXQuery:queryString constants:[NSDictionary dictionaryWithObject:[queryValue stringValue] forKey:@"query"] error:&err];
    if (results && [results count] > 0) {
        [self doSomethingWithQueryResults:results];
    } else {
        [queryStatus setStringValue:[NSString stringWithFormat:
            @"No records found, query errors: %@",
            (err ? [err localizedDescription] : @"None")]];
    }
}
```

If any of the fields contain malicious input, the XQuery string will become invalid or manipulated into performing something it should not. In this case, `[queryValue stringValue]` comes directly from the user. For example, there is an XPath function for loading any local or remote XML document and to do further queries against it. This attack is similar to SQL injection, and we protect against it by leveraging the safe constants: parameter provided by Cocoa in the [objectsForXQuery:constants:error:](https://developer.apple.com/documentation/foundation/nsxmlnode/1409792-objectsforxquery) method.

Instead of fetching the string value of the `queryValue` field this way, you could declare an external variable in the query prolog, put the value of the `queryValue` field in the constants dictionary, and reference the variable in the query. See [The Constants Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjyfu4tqnrwgu) for details on this approach.

XQuery is a fairly complex language, and although this document summarizes the salient aspects of syntax and behavior, it does not attempt a thorough description of XQuery. Fortunately excellent online and downloadable tutorials can be found through simple searches on the Internet.

[Next](Modifying%20an%20XML%20Document.md)[Previous](Traversing%20an%20XML%20Tree.md)

