---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/DeltaDoc/NewInEOF3.014.html
archived_at: '2026-07-15T07:57:57.727627Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in EOF 3.0](Table%20of%20Contents-2.md)

[!Table of Contents](Table%20of%20Contents-2.md) [!Previous Section](Changes%20to%20Enterprise%20Object%20Validation.md)

# Changes to the Interface Layer

In the EOInterface framework, three association classes have been added, and some changes have been made to EODisplayGroup.

## New Associations

The following sections provide a high level overview of the new associations. For complete documentation, see the corresponding class specifications.

### EOMatrixAssociation

Binds titles or images in an NSMatrix to string or image attributes in an enterprise object. Its aspects are:

|  title |  String property of the enterprise object that should be displayed in the matrix. |
|  image |  NSImage property of the enterprise object that should be displayed in the matrix. |
|  enabled |  Boolean property of enterprise object indicating if the matrix is enabled or disabled. |

```
```


### EORecursiveBrowserAssociation

Binds display groups to an NSBrowser so that enterprise objects of a recursive nature (that is, enterprise objects where there is a parent-child relationship) are displayed in the browser. Its aspects are:

|  rootChildren |  A display group that represents the root object, the parent of all children. Bind this aspect first in Interface Builder. If you do, Interface Builder creates a second display group (bound to the children aspect) that holds the browser's current selection. |
|  isLeaf |  Boolean property of the enterprise object indicating if it has children. If the value is NO or false, the enterprise object must be able to return a value for the children aspect. |
|  children |  A display group containing the children of this enterprise object. If you bind the rootChildren aspect first, a display group is created by Interface Builder and bound to this aspect. If this display group is created by Interface Builder, it always holds the browser selection. |
|  title |  String to display in the browser title for this enterprise object. |

```
```


### EOMasterCopyAssociation

Binds a display group to a relationship property of the selected object in another display group. This association contains one aspect, __parent__, which is the key for the property in the master object. Any change performed in one of these display groups is reflected in the other display group. Both display groups always have the same set of enterprise objects for __allObjects__ but, depending on the applied qualifier, not necessarily the same set of __displayedObjects__.
This association exists mainly to support EORecursiveBrowserAssociation.

### EOColumnAssociation

Three new aspects have been added to EOColumnAssociation:

|  textColor |  NSColor property of the enterprise object indicating the text color for the row. |
|  italic |  Boolean property of the enterprise object indicating whether row text should be italicized. |
|  bold |  Boolean property of the enterprise object indicating whether row text should be bold. |

```
```


## EODisplayGroup Changes

EODisplayGroup has changed to make its API similar to the WODisplayGroup class in the WebObjects Framework.

|  Changed Methods |  Changed Methods |
|  valueForKey:object: |  Is nowvalueForObject:key: (__valueForObject__ in Java). |

```
```

|  New Methods |  New Methods |
|  insertedObjectDefaultValues |  Returns a dictionary containing the default values to be used for newly inserted objects. The keys into the dictionary are the properties of the entity that the display group manages. If the dictionary returned by this method is empty, the insert method adds an object that is initially empty. Because the object is empty, the display group has no value to display in the user interface for that object, meaning that there is nothing for the user to select and modify. Use the setInsertedObjectDefaultValues: method to set up a default value so that there is something to display. |
|  setInsertedObjectDefaultValues: |  Sets the default values to be used for newly inserted objects. You use this method to provide at least one field that can be displayed for the newly inserted object. The possible keys into the dictionary are the properties of the entity managed by this display group. Note that EODisplayGroup already contains other hooks for this purpose, such as displayGroup:shouldInsertObject:atIndex: (displayGroupShouldInsertObject in Java). |
|  queryOperatorValues |  Returns a dictionary of operators to use on items in the equalToQueryValues dictionary. If a key in the equalToQueryValues dictionary also exists in queryOperatorValues, that operator for that key is used. The possible values are defined in the EOQualifier header. |
|  setQueryOperatorValues: |  Sets a dictionary of operators to use on items in the equalToQueryValues dictionary. |
|  defaultStringMatchOperator |  Returns the operator used to perform pattern matching for NSString values in the equalToQueryValues dictionary. This operator is used for properties listed in the equalToQueryValues dictionary that have NSString values and that do not have an associated entry in the queryOperator dictionary. In these cases, the operator returned by this method is used to perform pattern matching.  The default value for the query match operator is caseInsensitiveLike, which means that the query does not consider case when matching letters. The other possible value for this operator is like, which matches the case of the letters exactly. |
|  setDefaultStringMatchOperator: |  Sets the operator used to perform pattern matching for NSString values in the equalToQueryValues dictionary. |
|  defaultStringMatchFormat |  This format is used for properties listed in the equalToQueryValues dictionary that have NSString values and that do not have an associated entry in the queryOperator dictionary. In these cases, the value is matched using pattern matching and the format returned by this method specifies how it will be matched.  The default format string for pattern matching is "%@\*" which means that the string value in the equalToQueryValues dictionary is used as a prefix. For example, if the equalToQueryValues dictionary contains a value "Jo" for the key "name", the query returns all records whose name values begin with "Jo". |
|  setDefaultStringMatchFormat: |  Sets how pattern matching will be performed on NSString values in the equalToQueryValues dictionary. |
|  queryBindingValues |  Added to support the binding of complex qualifiers to the user interface (see the section "[Binding to Complex Qualifiers](Binding%20to%20Complex%20Qualifiers.md#apple-ha3deni)"). This method returns an NSDictionary containing the actual values that the user wants to query upon. |
|  setQueryBindingValues: |  Added to support the binding of complex qualifiers to the user interface (see the section "[Binding to Complex Qualifiers](Binding%20to%20Complex%20Qualifiers.md#apple-ha3deni)"). This method sets the NSDictionary containing the actual values that the user wants to query upon. |

```
```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
